# Edit and durably save measured runs: sibling delivery plan

Owner-authorized backlog creation on November 1, 2026. **Application implementation is not authorized.** This plan supplies source scope/intent for intake; native refinement, implementation planning and approval remain later gates.

## Scope

Edit connected runs without losing newer input or misreporting failed saves.

Root-level sibling epic only. Children deliver to this epic branch; all children complete → integrated epic Test/Review → trunk → same-SHA Cloudflare deployment and local Mac build → owner tests both. One orchestrator; at most three workers globally. No nested epic or outer integration branch.

## Technical lineage

Reviewed source Task(s) 4 in `docs/superpowers/plans/2026-11-01-first-usable-project-estimator.md`; trial specification acceptance cases 1–11 only. The reviewed files remain unchanged. Preserve all owner recipe/prices/settings/origin checkpoints and deferred-feature boundaries. Synthetic fixtures remain draft/test-only.

## Prerequisites and ownership

Prerequisite sibling keys: visits. Cross-epic dependencies mean completed code on trunk.

1 owns run controls and 2 owns the save controller against trunk contracts. Story 3 integrates their actual behavior.

A shared schema/export/store migration/HTTP route/App composition/lockfile has one designated owner. Consumers use the accepted epic-head contract and disjoint files. Partial renderer preparation is not a complete parallel-ready story when its producer is still missing. No gate/Full-Auto preference is changed.

## Story Intent

- **Beneficiary:** construction business owner
- **Capability:** edit and durably save measured runs
- **Need:** new edits can arrive while an earlier save is pending or failing
- **Value or failure prevented:** retain newer field measurements and see when work is still unsaved

## Implementation Tasks

### Task 1: Edit measured runs and explicit connections

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** edit exact lengths and explicit endpoint connections
- **Need:** new edits can arrive while an earlier save is pending or failing. Specifically, edit exact lengths and explicit endpoint connections
- **Value or failure prevented:** preserve distinct runs and deliberate joins despite repeated names

#### Scope and acceptance

Repeated labels and endpoint joins preserve identities; exact units/bounds validate.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: fixed Run contract / run controls.
- Direct prerequisite task numbers: None.

**Verification Commands:**

```sh
npm test -- apps/office/test
npm run typecheck
npm run build --workspace @estimator/office
```

### Task 2: Serialize writes and preserve the latest edit generation

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** serialize writes while tracking the latest edit generation
- **Need:** new edits can arrive while an earlier save is pending or failing. Specifically, serialize writes while tracking the latest edit generation
- **Value or failure prevented:** avoid old responses overwriting or falsely acknowledging newer input

#### Scope and acceptance

An older response cannot overwrite newer input or falsely acknowledge it as Saved.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: fixed save API / save controller.
- Direct prerequisite task numbers: None.

**Verification Commands:**

```sh
npm test -- apps/office/test
npm run typecheck
npm run build --workspace @estimator/office
```

### Task 3: Expose save retry and safe navigation

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** retry failed saves and flush safely before navigation
- **Need:** new edits can arrive while an earlier save is pending or failing. Specifically, retry failed saves and flush safely before navigation
- **Value or failure prevented:** keep unsaved changes visible while preserving the last durable version

#### Scope and acceptance

Rejected latest save remains Unsaved; Retry and navigation flush preserve the prior durable version.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: after controller and controls / composition.
- Direct prerequisite task numbers: 1, 2.

**Verification Commands:**

```sh
npm test -- apps/office/test
npm run typecheck
npm run build --workspace @estimator/office
```

