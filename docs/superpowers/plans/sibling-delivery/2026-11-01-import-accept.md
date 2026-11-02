# Accept reviewed field submissions exactly once: sibling delivery plan

Owner-authorized backlog creation on November 1, 2026. **Application implementation is not authorized.** This plan supplies source scope/intent for intake; native refinement, implementation planning and approval remain later gates.

## Scope

Accept transactionally, preserve source quotes, and replay without duplication.

Root-level sibling epic only. Children deliver to this epic branch; all children complete → integrated epic Test/Review → trunk → same-SHA Cloudflare deployment and local Mac build → owner tests both. One orchestrator; at most three workers globally. No nested epic or outer integration branch.

## Technical lineage

Reviewed source Task(s) 9 in `docs/superpowers/plans/2026-11-01-first-usable-project-estimator.md`; trial specification acceptance cases 1–11 only. The reviewed files remain unchanged. Preserve all owner recipe/prices/settings/origin checkpoints and deferred-feature boundaries. Synthetic fixtures remain draft/test-only.

## Prerequisites and ownership

Prerequisite sibling keys: import-review. Cross-epic dependencies mean completed code on trunk.

Repository story 1 closes first. Application helper story 2 and acceptance guard story 3 then own separate helper/test files against its accepted API. Story 4 composes and verifies the actual office round trip; the transaction/public facade remains single-owned.

A shared schema/export/store migration/HTTP route/App composition/lockfile has one designated owner. Consumers use the accepted epic-head contract and disjoint files. Partial renderer preparation is not a complete parallel-ready story when its producer is still missing. No gate/Full-Auto preference is changed.

## Story Intent

- **Beneficiary:** construction business owner
- **Capability:** accept reviewed field submissions exactly once
- **Need:** reviewed office context may change and an attachment may return more than once
- **Value or failure prevented:** preserve office authority, original submissions and reliable repeat imports

## Implementation Tasks

### Task 1: Commit import receipts and mappings together

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** commit retained submissions receipts and mappings transactionally
- **Need:** reviewed office context may change and an attachment may return more than once. Specifically, commit retained submissions receipts and mappings transactionally
- **Value or failure prevented:** repeat imports safely and avoid partially accepted office records

#### Scope and acceptance

Immutable source, ledger and mapping transaction rolls back coherently and handles identical replay.

- Intake forecast: 4 hours (S), not measured time or implementation approval.
- Ownership: prerequisite / import repository.
- Direct prerequisite task numbers: None.

**Verification Commands:**

```sh
npm test -- packages/exchange/test apps/office/test
npm run typecheck
npm run build
```

### Task 2: Apply reviewed drafts while retaining original quote links

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** apply reviewed draft choices while retaining original quote links
- **Need:** reviewed office context may change and an attachment may return more than once. Specifically, apply reviewed draft choices while retaining original quote links
- **Value or failure prevented:** use accepted field work without rewriting its source identities or Preliminary history

#### Scope and acceptance

Explicit draft resolution preserves original source quote IDs/status and consistent selected identities.

- Intake forecast: 4 hours (S), not measured time or implementation approval.
- Ownership: after repository API / application helper.
- Direct prerequisite task numbers: 1.

**Verification Commands:**

```sh
npm test -- packages/exchange/test apps/office/test
npm run typecheck
npm run build
```

### Task 3: Require renewed review after context changes

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** require renewed review when the target context changes
- **Need:** reviewed office context may change and an attachment may return more than once. Specifically, require renewed review when the target context changes
- **Value or failure prevented:** prevent an earlier preview from authorizing unexpected office changes

#### Scope and acceptance

Revision/mapping/context changes invalidate the preview without altering known duplicate behavior.

- Intake forecast: 2 hours (XS), not measured time or implementation approval.
- Ownership: after repository contract / acceptance guard.
- Direct prerequisite task numbers: 1.

**Verification Commands:**

```sh
npm test -- packages/exchange/test apps/office/test
npm run typecheck
npm run build
```

### Task 4: Accept replayed and delayed submissions through the office UI

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** accept replayed and delayed submissions through the office interface
- **Need:** reviewed office context may change and an attachment may return more than once. Specifically, accept replayed and delayed submissions through the office interface
- **Value or failure prevented:** recover older work safely while requiring current calculation before a new office quote

#### Scope and acceptance

Actual file round trip is idempotent; old-engine snapshots display but new quotes require current recalculation.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: after repository/helpers / service composition.
- Direct prerequisite task numbers: 2, 3.

**Verification Commands:**

```sh
npm test -- packages/exchange/test apps/office/test
npm run typecheck
npm run build
```

