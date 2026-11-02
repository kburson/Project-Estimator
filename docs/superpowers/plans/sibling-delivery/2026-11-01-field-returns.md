# Return immutable field submissions: sibling delivery plan

Owner-authorized backlog creation on November 1, 2026. **Application implementation is not authorized.** This plan supplies source scope/intent for intake; native refinement, implementation planning and approval remain later gates.

## Scope

Prepare durable packages and share/download without claiming office receipt.

Root-level sibling epic only. Children deliver to this epic branch; all children complete → integrated epic Test/Review → trunk → same-SHA Cloudflare deployment and local Mac build → owner tests both. One orchestrator; at most three workers globally. No nested epic or outer integration branch.

## Technical lineage

Reviewed source Task(s) 9 in `docs/superpowers/plans/2026-11-01-first-usable-project-estimator.md`; trial specification acceptance cases 1–11 only. The reviewed files remain unchanged. Preserve all owner recipe/prices/settings/origin checkpoints and deferred-feature boundaries. Synthetic fixtures remain draft/test-only.

## Prerequisites and ownership

Prerequisite sibling keys: field-quotes. Cross-epic dependencies mean completed code on trunk.

Story 1 closes transport contracts first; outbox story 2 and sharing adapter story 3 then run independently on separate files. Story 4 integrates persisted bodies with truthful sharing and explicit confirmation.

A shared schema/export/store migration/HTTP route/App composition/lockfile has one designated owner. Consumers use the accepted epic-head contract and disjoint files. Partial renderer preparation is not a complete parallel-ready story when its producer is still missing. No gate/Full-Auto preference is changed.

## Story Intent

- **Beneficiary:** construction business owner
- **Capability:** return immutable field submissions
- **Need:** sharing may be cancelled, repeated or handed off without office receipt
- **Value or failure prevented:** retry delivery without changing the evidence or confusing handoff with receipt

## Implementation Tasks

### Task 1: Build strict self-contained field packages

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** build strict self-contained field packages
- **Need:** sharing may be cancelled, repeated or handed off without office receipt. Specifically, build strict self-contained field packages
- **Value or failure prevented:** return understandable original work without needing a retired catalog key

#### Scope and acceptance

Bounded canonical checksums and references validate; content identity excludes envelope time/ID.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: prerequisite / transport contract.
- Direct prerequisite task numbers: None.

**Verification Commands:**

```sh
npm test -- packages/exchange/test apps/field/test
npm run typecheck
npm run build
```

### Task 2: Persist immutable outbox records before sharing

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** persist immutable outbox records before sharing
- **Need:** sharing may be cancelled, repeated or handed off without office receipt. Specifically, persist immutable outbox records before sharing
- **Value or failure prevented:** retain retryable evidence even when sharing fails or is interrupted

#### Scope and acceptance

Same content reuses bytes; changed content creates lineage; failed save offers no share.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: after package contract / outbox store.
- Direct prerequisite task numbers: 1.

**Verification Commands:**

```sh
npm test -- packages/exchange/test apps/field/test
npm run typecheck
npm run build
```

### Task 3: Share JSON or download it truthfully

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** share JSON or save a download with truthful outcomes
- **Need:** sharing may be cancelled, repeated or handed off without office receipt. Specifically, share JSON or save a download with truthful outcomes
- **Value or failure prevented:** choose an available delivery path without mistaking handoff for office receipt

#### Scope and acceptance

User-selected sharing, cancellation, fallback and handoff states are distinct.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: after package contract / sharing adapter.
- Direct prerequisite task numbers: 1.

**Verification Commands:**

```sh
npm test -- packages/exchange/test apps/field/test
npm run typecheck
npm run build
```

### Task 4: Retry saved submissions and confirm receipt explicitly

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** retry retained submissions and confirm receipt explicitly
- **Need:** sharing may be cancelled, repeated or handed off without office receipt. Specifically, retry retained submissions and confirm receipt explicitly
- **Value or failure prevented:** resend identical evidence and distinguish acknowledged work from prepared or handed-off work

#### Scope and acceptance

Resends are byte-identical and only owner confirmation sets office-confirmed.

- Intake forecast: 2 hours (XS), not measured time or implementation approval.
- Ownership: after outbox and adapter / Outbox UI.
- Direct prerequisite task numbers: 2, 3.

**Verification Commands:**

```sh
npm test -- packages/exchange/test apps/field/test
npm run typecheck
npm run build
```

