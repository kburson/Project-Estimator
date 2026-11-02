# Create verified office backups: sibling delivery plan

Owner-authorized backlog creation on November 1, 2026. **Application implementation is not authorized.** This plan supplies source scope/intent for intake; native refinement, implementation planning and approval remain later gates.

## Scope

Capture a consistent verified copy of current office data and files.

Root-level sibling epic only. Children deliver to this epic branch; all children complete → integrated epic Test/Review → trunk → same-SHA Cloudflare deployment and local Mac build → owner tests both. One orchestrator; at most three workers globally. No nested epic or outer integration branch.

## Technical lineage

Reviewed source Task(s) 10 in `docs/superpowers/plans/2026-11-01-first-usable-project-estimator.md`; trial specification acceptance cases 1–11 only. The reviewed files remain unchanged. Preserve all owner recipe/prices/settings/origin checkpoints and deferred-feature boundaries. Synthetic fixtures remain draft/test-only.

## Prerequisites and ownership

Prerequisite sibling keys: attachments, prices. Cross-epic dependencies mean completed code on trunk.

1 produces the inventory/service contract. UI preparation for 3 can overlap capture helper 2; complete story 3 depends on 2.

A shared schema/export/store migration/HTTP route/App composition/lockfile has one designated owner. Consumers use the accepted epic-head contract and disjoint files. Partial renderer preparation is not a complete parallel-ready story when its producer is still missing. No gate/Full-Auto preference is changed.

## Story Intent

- **Beneficiary:** construction business owner
- **Capability:** create verified office backups
- **Need:** copying a live database and its files separately can create an inconsistent recovery point
- **Value or failure prevented:** retain a recoverable copy without mistaking a partial copy for success

## Implementation Tasks

### Task 1: Define the complete current backup inventory

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** identify all required current backup artifacts
- **Need:** copying a live database and its files separately can create an inconsistent recovery point. Specifically, identify all required current backup artifacts
- **Value or failure prevented:** avoid omissions and reject unsafe or missing source files

#### Scope and acceptance

DB/settings/attachments and existing optional archive/key roots are covered; unsafe/missing required artifacts reject.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: prerequisite / backup contract.
- Direct prerequisite task numbers: None.

**Verification Commands:**

```sh
npm test -- apps/office/test
npm run typecheck
npm run build --workspace @estimator/office
```

### Task 2: Capture a consistent database and file backup

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** capture the database and associated files consistently
- **Need:** copying a live database and its files separately can create an inconsistent recovery point. Specifically, capture the database and associated files consistently
- **Value or failure prevented:** receive verified lengths and hashes from one coherent backup

#### Scope and acceptance

Brief write lock and pinned SQLite backup yield verified lengths/hashes before success.

- Intake forecast: 4 hours (S), not measured time or implementation approval.
- Ownership: after contract / capture helper.
- Direct prerequisite task numbers: 1.

**Verification Commands:**

```sh
npm test -- apps/office/test
npm run typecheck
npm run build --workspace @estimator/office
```

### Task 3: Choose destinations and report verified backup status

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** choose a destination and see verified backup status
- **Need:** copying a live database and its files separately can create an inconsistent recovery point. Specifically, choose a destination and see verified backup status
- **Value or failure prevented:** know when a backup completed and whether it contains private keys

#### Scope and acceptance

Source remains intact on failure; private-key inclusion is explained when keys exist.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: controls after contract; integrate after capture / Backup UI.
- Direct prerequisite task numbers: 2.

**Verification Commands:**

```sh
npm test -- apps/office/test
npm run typecheck
npm run build --workspace @estimator/office
```

