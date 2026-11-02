# Upgrade the field app without losing work: sibling delivery plan

Owner-authorized backlog creation on November 1, 2026. **Application implementation is not authorized.** This plan supplies source scope/intent for intake; native refinement, implementation planning and approval remain later gates.

## Scope

Activate a distinct version only at a saved compatible single-window boundary.

Root-level sibling epic only. Children deliver to this epic branch; all children complete → integrated epic Test/Review → trunk → same-SHA Cloudflare deployment and local Mac build → owner tests both. One orchestrator; at most three workers globally. No nested epic or outer integration branch.

## Technical lineage

Reviewed source Task(s) 10 in `docs/superpowers/plans/2026-11-01-first-usable-project-estimator.md`; trial specification acceptance cases 1–11 only. The reviewed files remain unchanged. Preserve all owner recipe/prices/settings/origin checkpoints and deferred-feature boundaries. Synthetic fixtures remain draft/test-only.

## Prerequisites and ownership

Prerequisite sibling keys: offline-shell, catalog-refresh, field-returns. Cross-epic dependencies mean completed code on trunk.

After compatibility protocol story 1 closes, controller story 2 and worker lifecycle story 3 run in separately owned files/tests. Story 4 joins completed behavior and proves distinct visible versions and asset hashes; actual device evidence remains qualification.

A shared schema/export/store migration/HTTP route/App composition/lockfile has one designated owner. Consumers use the accepted epic-head contract and disjoint files. Partial renderer preparation is not a complete parallel-ready story when its producer is still missing. No gate/Full-Auto preference is changed.

## Story Intent

- **Beneficiary:** construction business owner
- **Capability:** upgrade the field app without losing work
- **Need:** a new app release can arrive while unsaved edits or other app windows still exist
- **Value or failure prevented:** gain the new release without losing edits, registration or retained submissions

## Implementation Tasks

### Task 1: Check waiting-release and stored-data compatibility

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** check waiting-release and existing-store compatibility
- **Need:** a new app release can arrive while unsaved edits or other app windows still exist. Specifically, check waiting-release and existing-store compatibility
- **Value or failure prevented:** keep the working version when the replacement cannot read retained data

#### Scope and acceptance

Read actual stored work and both enrollment slots; unsupported schema or failed decrypt defers activation.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: prerequisite / compatibility protocol.
- Direct prerequisite task numbers: None.

**Verification Commands:**

```sh
npm test -- apps/field/test
npm run typecheck
npm run build --workspace @estimator/field
```

### Task 2: Defer activation until edits are durably saved

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** defer activation until current edits are durably saved
- **Need:** a new app release can arrive while unsaved edits or other app windows still exist. Specifically, defer activation until current edits are durably saved
- **Value or failure prevented:** update without discarding unsaved work or activating after a failed save

#### Scope and acceptance

Dirty/saving/failed flush preserves current app; explicit successful Save and update can proceed.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: after compatibility API / controller.
- Direct prerequisite task numbers: 1.

**Verification Commands:**

```sh
npm test -- apps/field/test
npm run typecheck
npm run build --workspace @estimator/field
```

### Task 3: Keep the prior shell until replacement boot succeeds

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** retain the previous shell until replacement boot succeeds
- **Need:** a new app release can arrive while unsaved edits or other app windows still exist. Specifically, retain the previous shell until replacement boot succeeds
- **Value or failure prevented:** recover from failed activation and avoid updating across conflicting open app windows

#### Scope and acceptance

Two-client recheck refuses unsafe activation; cleanup follows successful boot/store read only.

- Intake forecast: 4 hours (S), not measured time or implementation approval.
- Ownership: after protocol / worker lifecycle.
- Direct prerequisite task numbers: 1.

**Verification Commands:**

```sh
npm test -- apps/field/test
npm run typecheck
npm run build --workspace @estimator/field
```

### Task 4: Rehearse genuinely different preserved-store releases

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** rehearse genuinely distinct releases with retained records
- **Need:** a new app release can arrive while unsaved edits or other app windows still exist. Specifically, rehearse genuinely distinct releases with retained records
- **Value or failure prevented:** verify preservation across a real version change rather than an unchanged page reload

#### Scope and acceptance

Distinct visible versions and asset hashes preserve active/pending keys plus existing saved work.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: after controller/worker / browser integration.
- Direct prerequisite task numbers: 2, 3.

**Verification Commands:**

```sh
npm test -- apps/field/test
npm run typecheck
npm run build --workspace @estimator/field
```

