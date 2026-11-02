# Save field site visits: sibling delivery plan

Owner-authorized backlog creation on November 1, 2026. **Application implementation is not authorized.** This plan supplies source scope/intent for intake; native refinement, implementation planning and approval remain later gates.

## Scope

Enter and reopen field work with real snapshots and truthful save failures.

Root-level sibling epic only. Children deliver to this epic branch; all children complete → integrated epic Test/Review → trunk → same-SHA Cloudflare deployment and local Mac build → owner tests both. One orchestrator; at most three workers globally. No nested epic or outer integration branch.

## Technical lineage

Reviewed source Task(s) 7 in `docs/superpowers/plans/2026-11-01-first-usable-project-estimator.md`; trial specification acceptance cases 1–11 only. The reviewed files remain unchanged. Preserve all owner recipe/prices/settings/origin checkpoints and deferred-feature boundaries. Synthetic fixtures remain draft/test-only.

## Prerequisites and ownership

Prerequisite sibling keys: registration, proposals, run-editing. Cross-epic dependencies mean completed code on trunk.

After store story 1 closes, touch controls story 2 and save algorithm story 4 are separate lanes. Calculator story 3 follows completed controls and may overlap the save algorithm. Story 5 requires actual controls, calculator and queue; story 6 follows completed save integration. Rendering a partial form does not close story 2.

A shared schema/export/store migration/HTTP route/App composition/lockfile has one designated owner. Consumers use the accepted epic-head contract and disjoint files. Partial renderer preparation is not a complete parallel-ready story when its producer is still missing. No gate/Full-Auto preference is changed.

## Story Intent

- **Beneficiary:** construction business owner
- **Capability:** save field site visits
- **Need:** connectivity and catalog access can change while the device holds measured work
- **Value or failure prevented:** measurements and estimates remain usable after restart or loss of catalog access

## Implementation Tasks

### Task 1: Persist real field draft snapshots independently of keys

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** persist real field draft snapshots independently of catalog keys
- **Need:** connectivity and catalog access can change while the device holds measured work. Specifically, persist real field draft snapshots independently of catalog keys
- **Value or failure prevented:** reopen retained measurements and results even after registration changes

#### Scope and acceptance

Extend the existing registered field store with real JobDraft save/read APIs; preserve enrollment/catalog tables and all existing data.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: prerequisite / field store.
- Direct prerequisite task numbers: None.

**Verification Commands:**

```sh
npm test -- apps/field/test
npm run typecheck
npm run build --workspace @estimator/field
```

### Task 2: Edit field customer job and run inputs

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** edit customer job and measured-run inputs on a touch device
- **Need:** connectivity and catalog access can change while the device holds measured work. Specifically, edit customer job and measured-run inputs on a touch device
- **Value or failure prevented:** capture stable identities and explicit connections at the jobsite

#### Scope and acceptance

Stable IDs, explicit endpoint joins and measured input validation match the Mac.

- Intake forecast: 4 hours (S), not measured time or implementation approval.
- Ownership: after store contract / touch controls.
- Direct prerequisite task numbers: 1.

**Verification Commands:**

```sh
npm test -- apps/field/test
npm run typecheck
npm run build --workspace @estimator/field
```

### Task 3: Calculate enrolled field work with exact Mac parity

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** calculate enrolled work with exact Mac parity
- **Need:** connectivity and catalog access can change while the device holds measured work. Specifically, calculate enrolled work with exact Mac parity
- **Value or failure prevented:** rely on one validated calculation rather than a divergent field estimate

#### Scope and acceptance

Actual shared input/result matches the Mac; missing/unvalidated catalog cannot produce a valid quote.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: after controls and installed catalog / field calculation adapter.
- Direct prerequisite task numbers: 2.

**Verification Commands:**

```sh
npm test -- apps/field/test
npm run typecheck
npm run build --workspace @estimator/field
```

### Task 4: Preserve newer field edits in the write queue

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** serialize saves while preserving the latest edit generation
- **Need:** connectivity and catalog access can change while the device holds measured work. Specifically, serialize saves while preserving the latest edit generation
- **Value or failure prevented:** an older save cannot overwrite or falsely acknowledge newer work

#### Scope and acceptance

Generation-aware serialized writes cannot overwrite newer input or acknowledge it incorrectly.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: after store contract / save algorithm.
- Direct prerequisite task numbers: 1.

**Verification Commands:**

```sh
npm test -- apps/field/test
npm run typecheck
npm run build --workspace @estimator/field
```

### Task 5: Report field save failure and flush before navigation

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** see save failures and flush edits before navigation
- **Need:** connectivity and catalog access can change while the device holds measured work. Specifically, see save failures and flush edits before navigation
- **Value or failure prevented:** retry safely while keeping the last durable visit available

#### Scope and acceptance

Quota/error/retry/flush paths preserve the previous durable version and truthful status.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: after queue / UI integration.
- Direct prerequisite task numbers: 2, 3, 4.

**Verification Commands:**

```sh
npm test -- apps/field/test
npm run typecheck
npm run build --workspace @estimator/field
```

### Task 6: Reopen field visits and report actual storage persistence

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** reopen visits and inspect actual storage persistence
- **Need:** connectivity and catalog access can change while the device holds measured work. Specifically, reopen visits and inspect actual storage persistence
- **Value or failure prevented:** distinguish usable local records from guarantees the browser cannot provide

#### Scope and acceptance

Saved work reopens without keys; persistence requests report actual results, not backup guarantees.

- Intake forecast: 2 hours (XS), not measured time or implementation approval.
- Ownership: after controls and save / navigation.
- Direct prerequisite task numbers: 5.

**Verification Commands:**

```sh
npm test -- apps/field/test
npm run typecheck
npm run build --workspace @estimator/field
```

