#!/usr/bin/env python3
"""Read-only #36 audit evidence verification from committed public metadata.

Retains the approved replacement graph and legacy retirement contract while
allowing #36 alone through its administrative completion lifecycle. No retries,
mutations, product dependencies, application builds or deployment.
"""
import argparse
import datetime as dt
import hashlib
import json
import re
import subprocess
import sys
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / '.scratch/plan/sibling-replan'
LOG = ROOT / '.scratch/gh/sibling-migration'
REPO = 'kburson/Project-Estimator'
PROJECT = 'PVT_kwHOABCEY84Bpu2b'
# Batch independent read aliases; retain per-connection pagination and all guards.
BATCH = 20
PAGE_SIZE = 50
MAX_PAGES = 10
MAX_CALLS = 100
# Explicitly identified partial creation; canonical task remains #76.
DUPLICATE_CORRECTIONS = {75: 76}
ORIGINALS = {
    'docs/superpowers/specs/2026-11-01-project-estimator-pwa-v1-design.md':
        '0971e6426aadf888a3652d9fae78707793f4af7f4b221e5b577ef8deca253f2c',
    'docs/superpowers/plans/2026-11-01-first-usable-project-estimator.md':
        'fb0601ece98e4f7af05a26cabcaeccbf5f33dd386e21d00215f0a1bedc2ad6f6',
}
EDGE = 'number repository{nameWithOwner}'
ITEM = '''id project{id}
 priority:fieldValueByName(name:"Priority"){... on ProjectV2ItemFieldSingleSelectValue{name}}
 status:fieldValueByName(name:"Status"){... on ProjectV2ItemFieldSingleSelectValue{name}}
 size:fieldValueByName(name:"Size"){... on ProjectV2ItemFieldSingleSelectValue{name}}
 estimate:fieldValueByName(name:"Estimate"){... on ProjectV2ItemFieldNumberValue{number}}
 disposition:fieldValueByName(name:"Disposition"){... on ProjectV2ItemFieldSingleSelectValue{name}}'''
CONNECTIONS = {'assignees': 'login', 'subIssues': EDGE,
               'blockedBy': EDGE, 'blocking': EDGE, 'projectItems': ITEM}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def connection(name, cursor=None):
    after = ',after:' + json.dumps(cursor) if cursor else ''
    return (f'{name}(first:{PAGE_SIZE}{after})' + '{nodes{' + CONNECTIONS[name] +
            '} pageInfo{hasNextPage endCursor}}')


def initial_query(numbers):
    entries = []
    for number in numbers:
        fields = ' '.join(connection(k) for k in CONNECTIONS)
        entries.append(f'i{number}:issue(number:{number})' + '{number title state stateReason body '
                       'parent{number repository{nameWithOwner}} ' + fields + '}')
    return ('query{rateLimit{cost remaining resetAt} repository(owner:"kburson",'
            'name:"Project-Estimator"){' + ' '.join(entries) + '}}')


def followup_query(jobs):
    entries = []
    for i, (number, name, cursor) in enumerate(jobs):
        entries.append(f'p{i}:issue(number:{number})' + '{number ' + connection(name, cursor) + '}')
    return ('query{rateLimit{cost remaining resetAt} repository(owner:"kburson",'
            'name:"Project-Estimator"){' + ' '.join(entries) + '}}')


def local_query_check(query):
    # A structural sanity check only; live schema validation remains GitHub's job.
    quoted = re.sub(r'"(?:\\.|[^"\\])*"', '""', query)
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for character in quoted:
        if character in '({[':
            stack.append(character)
        elif character in ')}]':
            if not stack or stack.pop() != pairs[character]:
                raise ValueError('unbalanced generated GraphQL query')
    if stack or not query.startswith('query{') or 'mutation' in quoted:
        raise ValueError('invalid or non-read-only generated query')


def metadata(body):
    sections = re.findall(r'^## Plan Metadata\s*\n(.*?)(?=^## |\Z)', body, re.M | re.S)
    if len(sections) != 1:
        raise ValueError('expected exactly one Plan Metadata section')
    result = {}
    for key, value in re.findall(r'^-\s+\*\*([^*]+)\*\*:\s*(.*?)\s*$', sections[0], re.M):
        if key.lower() in result:
            raise ValueError('duplicate metadata key ' + key)
        result[key.lower()] = value
    return result


def native_refs(node, name):
    values = node[name]['nodes']
    if any(x['repository']['nameWithOwner'].lower() != REPO.lower() for x in values):
        raise ValueError(f'#{node["number"]} foreign repository in {name}')
    numbers = [x['number'] for x in values]
    if len(numbers) != len(set(numbers)):
        raise ValueError(f'#{node["number"]} duplicate {name} nodes')
    return set(numbers)


def item_fields(node):
    items = [x for x in node['projectItems']['nodes'] if x['project']['id'] == PROJECT]
    if len(items) != 1:
        raise ValueError(f'#{node["number"]} expected exactly one target board item')
    item = items[0]
    return {key: (item[key] or {}).get('number' if key == 'estimate' else 'name')
            for key in ('priority', 'status', 'size', 'estimate', 'disposition')}


def expected_inventory():
    contract_path = ROOT / 'docs/epics/verification/36-migration-contract.json'
    evidence = json.loads((ROOT / 'docs/epics/2026-11-02-36-sibling-migration-verification.json').read_text())
    raw = contract_path.read_bytes()
    if digest(raw) != evidence['final']['expectedGraphSHA256']:
        raise ValueError('immutable expected graph hash mismatch')
    map_bytes = (ROOT / 'docs/epics/2026-11-01-sibling-delivery-issue-map.json').read_bytes()
    if digest(map_bytes) != evidence['issueMapJSONSHA256']:
        raise ValueError('committed public map hash mismatch')
    mapping = json.loads(map_bytes)
    if mapping['index'] != 36 or len(mapping['epics']) != 28 or sum(len(e['children']) for e in mapping['epics']) != 135:
        raise ValueError('unexpected approved map shape')
    if not evidence['preRetirement']['success'] or not evidence['success'] or evidence['preRetirement']['completedAt'] >= evidence['completedAt']:
        raise ValueError('pre-retirement chronology/evidence missing')
    expected = {int(k): value for k, value in json.loads(raw).items()}
    for value in expected.values():
        value['children'] = set(value['children'])
        value['deps'] = set(value['deps'])
    if len(expected) != 163 or set(expected) & set(range(1, 37)):
        raise ValueError('unexpected approved replacement contract')
    for plan in sorted({value['plan'] for value in expected.values()}):
        pinned = subprocess.check_output(
            ['git', 'show', mapping['sourcePlanCommit'] + ':' + plan], cwd=ROOT)
        if pinned != (ROOT / plan).read_bytes():
            raise ValueError('sibling plan differs from its pinned source: ' + plan)
    return expected, {'plan_commit': mapping['sourcePlanCommit']}


class Reader:
    def __init__(self, directory):
        self.directory = directory
        self.calls = 0
        self.rates = []

    def all_issues(self):
        """Bounded REST enumeration catches unreceipted create partial successes."""
        result = {}
        for page in range(1, MAX_PAGES + 1):
            self.calls += 1
            if self.calls > MAX_CALLS:
                raise RuntimeError('bounded API call budget exceeded')
            endpoint = f'repos/{REPO}/issues?state=all&per_page=100&page={page}'
            response = subprocess.run(['gh', 'api', '--method', 'GET', endpoint], cwd=ROOT,
                                      text=True, capture_output=True, timeout=120)
            prefix = self.directory / f'rest-issues-{page:02d}'
            prefix.with_suffix('.stdout.json').write_text(response.stdout)
            prefix.with_suffix('.stderr.txt').write_text(response.stderr)
            if response.returncode:
                raise RuntimeError(f'REST issue inventory failed; no retry: {response.stderr[-600:]}')
            values = json.loads(response.stdout)
            if not isinstance(values, list):
                raise RuntimeError('REST issue inventory is not an array')
            for value in values:
                if 'pull_request' in value:
                    continue
                number = value['number']
                if number in result:
                    raise RuntimeError('REST issue pagination repeated an issue; rerun quiescent')
                result[number] = value
            if len(values) < 100:
                return result
        raise RuntimeError('REST issue pagination bound reached; inventory incomplete')

    def request(self, query):
        local_query_check(query)
        self.calls += 1
        if self.calls > MAX_CALLS:
            raise RuntimeError('bounded API call budget exceeded')
        prefix = self.directory / f'query-{self.calls:03d}'
        prefix.with_suffix('.graphql').write_text(query + '\n')
        result = subprocess.run(['gh', 'api', 'graphql', '-f', 'query=' + query],
                                cwd=ROOT, text=True, capture_output=True, timeout=120)
        prefix.with_suffix('.stdout.json').write_text(result.stdout)
        prefix.with_suffix('.stderr.txt').write_text(result.stderr)
        if result.returncode:
            raise RuntimeError(f'GitHub query {self.calls} failed; no retry: {result.stderr[-600:]}')
        data = json.loads(result.stdout)
        if data.get('errors'):
            raise RuntimeError('GraphQL partial/error response; verification incomplete: ' +
                               json.dumps(data['errors'])[:1000])
        if not data.get('data', {}).get('repository'):
            raise RuntimeError('missing repository data')
        self.rates.append(data['data'].get('rateLimit'))
        return data['data']['repository']

    def inventory(self, numbers):
        nodes = {}
        for start in range(0, len(numbers), BATCH):
            batch = numbers[start:start+BATCH]
            response = self.request(initial_query(batch))
            for number in batch:
                node = response.get(f'i{number}')
                if not node or node.get('number') != number:
                    raise RuntimeError(f'missing/wrong issue #{number}')
                nodes[number] = node
        seen = {}
        for page in range(1, MAX_PAGES + 1):
            jobs = []
            for number, node in nodes.items():
                for name in CONNECTIONS:
                    info = node[name]['pageInfo']
                    if info['hasNextPage']:
                        cursor = info.get('endCursor')
                        if not cursor or cursor in seen.setdefault((number, name), set()):
                            raise RuntimeError('missing/repeated pagination cursor')
                        seen[(number, name)].add(cursor)
                        jobs.append((number, name, cursor))
            if not jobs:
                return nodes
            if page == MAX_PAGES:
                raise RuntimeError('connection pagination bound reached; snapshot incomplete')
            for start in range(0, len(jobs), BATCH):
                batch = jobs[start:start+BATCH]
                response = self.request(followup_query(batch))
                for i, (number, name, _) in enumerate(batch):
                    value = response[f'p{i}'][name]
                    nodes[number][name]['nodes'].extend(value['nodes'])
                    nodes[number][name]['pageInfo'] = value['pageInfo']
        raise RuntimeError('unreachable pagination exit')


def verify(nodes, expected, state, phase):
    errors = []
    def check(condition, number, message):
        if not condition:
            errors.append(f'#{number}: {message}')
    for number, contract in expected.items():
        node = nodes[number]
        fields = item_fields(node)
        check(node['title'] == contract['title'], number, 'exact title mismatch')
        check(node['state'] == 'OPEN', number, 'replacement is not OPEN')
        check(fields['status'] == 'Backlog', number, 'replacement not Backlog')
        check(fields['priority'] == 'P1', number, 'replacement priority mismatch')
        visible = re.sub(r'<!--.*?-->', '', node['body'], flags=re.S)
        check(not re.search(r'^\s*- \[x\]', visible, re.M | re.I), number, 'replacement contains checked acceptance/delivery boxes')
        check([x['login'] for x in node['assignees']['nodes']] == ['kburson'], number, 'owner mismatch')
        parent = node['parent']
        check((parent['number'] if parent else None) == contract['parent'], number, 'parent mismatch')
        if parent:
            check(parent['repository']['nameWithOwner'].lower() == REPO.lower(), number, 'foreign parent')
        check(native_refs(node, 'subIssues') == contract['children'], number, 'exact child set mismatch')
        check(native_refs(node, 'blockedBy') == contract['deps'], number, 'exact prerequisite edge set mismatch')
        check(fields['disposition'] == ('BLOCKED' if contract['deps'] else None), number, 'dependency Disposition mismatch')
        md = metadata(node['body'])
        for key in ('implementation-plan', 'source-plan'):
            check(md.get(key) == contract['plan'], number, key + ' mismatch')
        check(md.get('source-plan-commit') == state['plan_commit'], number, 'source commit mismatch')
        check(md.get('source-plan-section') == contract.get('section'), number, 'task selector mismatch')
        kinds = re.findall(r'<!--\s*aitm-issue-kind\s+kind="([^"]+)"\s*-->', node['body'])
        # AITM intentionally represents the default code kind by no marker.
        check(kinds == ([] if contract['kind'] == 'code' else [contract['kind']]), number, 'issue-kind marker mismatch')
        if contract['parent']:
            check(fields['size'] == contract['size'], number, 'board size mismatch')
            check(fields['estimate'] == contract['hours'], number, 'board estimate mismatch')
            markers = re.findall(r'<!-- aitm-fields: (.*?) -->', node['body'])
            if len(markers) != 1:
                errors.append(f'#{number}: expected one body field DB')
            else:
                values = json.loads(markers[0])['values']
                check(values.get('size') == contract['size'] and values.get('estimate') == contract['hours'], number, 'body size/estimate mismatch')
    index = nodes[36]
    check(index['parent'] is None and not native_refs(index, 'subIssues'), 36, 'index is parented or has children')
    check(not native_refs(index, 'blockedBy') and not native_refs(index, 'blocking'), 36, 'index has dependency/blocking role')
    if phase == 'audit-close':
        index_fields = item_fields(index)
        if index['state'] == 'CLOSED':
            check(index['stateReason'] == 'COMPLETED' and index_fields['status'] == 'Done'
                  and index_fields['disposition'] == 'Delivered', 36, 'index closure mismatch')
        else:
            check(index['state'] == 'OPEN' and index_fields['status'] in
                  ('Plan', 'Develop', 'Test', 'Review'), 36, 'index audit lifecycle mismatch')
    else:
        check(index['state'] == 'OPEN' and item_fields(index)['status'] == 'Backlog', 36, 'index state changed')
    check([x['login'] for x in index['assignees']['nodes']] == ['kburson'], 36, 'index owner mismatch')
    check('<!-- aitm-issue-kind kind="docs-only" -->' in index['body'], 36,
          'index not commit-bearing documentation kind')
    for number in range(1, 36):
        node = nodes[number]
        check((node['parent']['number'] if node['parent'] else None) == (None if number == 1 else 1), number, 'historical parent relationship changed')
        if phase == 'replacements':
            check(node['state'] == 'OPEN', number, 'legacy retired before replacements verification')
        else:
            fields = item_fields(node)
            check(node['state'] == 'CLOSED' and node['stateReason'] == 'NOT_PLANNED', number, 'legacy not CLOSED/NOT_PLANNED')
            check(fields['status'] == 'Done' and fields['disposition'] == 'Replaced', number, 'legacy not Done/Replaced')
            markers = re.findall(r'<!--\s*aitm-superseded-by\b([^>]*?)-->', node['body'])
            check(len(markers) == 1 and re.search(r'\brefs="#36"', markers[0]) is not None, number, 'missing/ambiguous superseded-by #36')
    for number, successor in DUPLICATE_CORRECTIONS.items():
        node = nodes[number]
        fields = item_fields(node)
        check(successor in expected, number, 'duplicate successor is not canonical inventory')
        check(node['state'] == 'CLOSED' and node['stateReason'] == 'NOT_PLANNED', number, 'partial duplicate not CLOSED/NOT_PLANNED')
        check(fields['status'] == 'Done' and fields['disposition'] == 'Replaced', number, 'partial duplicate not Done/Replaced')
        markers = re.findall(r'<!--\s*aitm-superseded-by\b([^>]*?)-->', node['body'])
        check(len(markers) == 1 and re.search(r'\brefs="#' + str(successor) + r'"', markers[0]) is not None, number, 'partial duplicate successor marker mismatch')
    return errors


def main():
    parser = argparse.ArgumentParser(description='Read-only administrative audit verification for #36; no product implementation.')
    parser.add_argument('--offline-self-check', action='store_true')
    args = parser.parse_args()
    expected, state = expected_inventory()
    originals = {name: digest((ROOT / name).read_bytes()) for name in ORIGINALS}
    if originals != ORIGINALS:
        raise ValueError('reviewed source hashes changed')
    local_query_check(initial_query([1, 36, 40]))
    local_query_check(followup_query([(1, 'subIssues', 'cursor/with+chars=')]))
    if args.offline_self_check:
        print('PASS: immutable 163-record graph, 28/135 public map, prior evidence chronology and reviewed source hashes; no API calls.')
        return 0
    directory = LOG / 'audit-close-verification' / (dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ-') + uuid.uuid4().hex[:8])
    directory.mkdir(parents=True)
    reader = Reader(directory)
    report = {'schema': 'project-estimator.administrative-close-verification/v1', 'success': False}
    try:
        rest = reader.all_issues()
        known = set(expected) | set(range(1, 37)) | set(DUPLICATE_CORRECTIONS)
        if set(rest) != known:
            raise ValueError('unexpected/missing repository issues: ' + str(sorted(set(rest) ^ known)))
        nodes = reader.inventory(sorted(known))
        (directory / 'snapshot.json').write_text(json.dumps(nodes, indent=2) + '\n')
        errors = verify(nodes, expected, state, 'audit-close')
        report.update(success=not errors, errors=errors, issuesObserved=len(nodes))
    except Exception as exc:
        report['errors'] = [str(exc)]
    report.update(completedAt=dt.datetime.now(dt.timezone.utc).isoformat(), apiCalls=reader.calls, rateLimits=reader.rates)
    (directory / 'receipt.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'success': report['success'], 'receipt': str(directory / 'receipt.json'), 'errors': report['errors']}, indent=2))
    return 0 if report['success'] else 1


if __name__ == '__main__':
    sys.exit(main())
