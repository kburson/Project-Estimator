# Retain job and receipt evidence: sibling delivery plan

Owner-authorized backlog creation on November 1, 2026. **Application implementation is not authorized.** This plan supplies source scope/intent for intake; native refinement, implementation planning and approval remain later gates.

## Scope

Upload and reopen immutable local evidence with original metadata.

Root-level sibling epic only. Children deliver to this epic branch; all children complete → integrated epic Test/Review → trunk → same-SHA Cloudflare deployment and local Mac build → owner tests both. One orchestrator; at most three workers globally. No nested epic or outer integration branch.

## Technical lineage

Reviewed source Task(s) 4 in `docs/superpowers/plans/2026-11-01-first-usable-project-estimator.md`; trial specification acceptance cases 1–11 only. The reviewed files remain unchanged. Preserve all owner recipe/prices/settings/origin checkpoints and deferred-feature boundaries. Synthetic fixtures remain draft/test-only.

## Prerequisites and ownership

Prerequisite sibling keys: visits, catalog. Cross-epic dependencies mean completed code on trunk.

Producer chain 1 to 2 to 3; no complete independent implementation lane. UI preparation may overlap route work but acceptance requires actual routes.

A shared schema/export/store migration/HTTP route/App composition/lockfile has one designated owner. Consumers use the accepted epic-head contract and disjoint files. Partial renderer preparation is not a complete parallel-ready story when its producer is still missing. No gate/Full-Auto preference is changed.

## Story Intent

- **Beneficiary:** construction business owner
- **Capability:** retain job and receipt evidence
- **Need:** file writes and business-record references can fail independently
- **Value or failure prevented:** reopen the exact supporting files behind business records

## Implementation Tasks

### Task 1: Store verified immutable attachment files

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** store verified immutable evidence files and their metadata
- **Need:** file writes and business-record references can fail independently. Specifically, store verified immutable evidence files and their metadata
- **Value or failure prevented:** retain exact bytes without unsafe paths or broken file references

#### Scope and acceptance

Hash/name/date/size, 20MiB limit, safe paths and write-before-reference ordering are enforced.

- Intake forecast: 4 hours (S), not measured time or implementation approval.
- Ownership: prerequisite / attachment store.
- Direct prerequisite task numbers: None.

**Verification Commands:**

```sh
npm test -- apps/office/test
npm run typecheck
npm run build --workspace @estimator/office
```

### Task 2: Upload and download evidence through bounded routes

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** upload and download evidence through bounded validated routes
- **Need:** file writes and business-record references can fail independently. Specifically, upload and download evidence through bounded validated routes
- **Value or failure prevented:** access the intended owner's file without leaking local paths

#### Scope and acceptance

Exact binary content type and owner identity are checked without path or secret leaks.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: after store / attachment HTTP.
- Direct prerequisite task numbers: 1.

**Verification Commands:**

```sh
npm test -- apps/office/test
npm run typecheck
npm run build --workspace @estimator/office
```

### Task 3: Attach and reopen owner-selected evidence

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** attach and reopen selected job or receipt evidence
- **Need:** file writes and business-record references can fail independently. Specifically, attach and reopen selected job or receipt evidence
- **Value or failure prevented:** recover original metadata and bytes without false success or automatic publication

#### Scope and acceptance

Original metadata and bytes reopen; failure never reports success; no automatic CDN/field inclusion.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: after routes / attachment controls.
- Direct prerequisite task numbers: 2.

**Verification Commands:**

```sh
npm test -- apps/office/test
npm run typecheck
npm run build --workspace @estimator/office
```

