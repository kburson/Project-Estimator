# Restore office work safely: sibling delivery plan

Owner-authorized backlog creation on November 1, 2026. **Application implementation is not authorized.** This plan supplies source scope/intent for intake; native refinement, implementation planning and approval remain later gates.

## Scope

Restore into an isolated directory without losing identities or overwriting on failure.

Root-level sibling epic only. Children deliver to this epic branch; all children complete → integrated epic Test/Review → trunk → same-SHA Cloudflare deployment and local Mac build → owner tests both. One orchestrator; at most three workers globally. No nested epic or outer integration branch.

## Technical lineage

Reviewed source Task(s) 10 in `docs/superpowers/plans/2026-11-01-first-usable-project-estimator.md`; trial specification acceptance cases 1–11 only. The reviewed files remain unchanged. Preserve all owner recipe/prices/settings/origin checkpoints and deferred-feature boundaries. Synthetic fixtures remain draft/test-only.

## Prerequisites and ownership

Prerequisite sibling keys: backup-capture. Cross-epic dependencies mean completed code on trunk.

1 produces validation; 2 restores. Fixture preparation for 3 can overlap 2 after 1, but final recovery proof depends on 2.

A shared schema/export/store migration/HTTP route/App composition/lockfile has one designated owner. Consumers use the accepted epic-head contract and disjoint files. Partial renderer preparation is not a complete parallel-ready story when its producer is still missing. No gate/Full-Auto preference is changed.

## Story Intent

- **Beneficiary:** construction business owner
- **Capability:** restore office work safely
- **Need:** corrupt or unsafe recovery input must not replace otherwise usable business records
- **Value or failure prevented:** recover stable business identities while retaining a safe rollback directory

## Implementation Tasks

### Task 1: Validate every backup artifact before restore

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** validate every backup artifact before restoring
- **Need:** corrupt or unsafe recovery input must not replace otherwise usable business records. Specifically, validate every backup artifact before restoring
- **Value or failure prevented:** reject corrupt or unsafe input before touching the destination

#### Scope and acceptance

Hash/size/path/traversal/symlink failures leave the destination untouched.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: prerequisite / validation helper.
- Direct prerequisite task numbers: None.

**Verification Commands:**

```sh
npm test -- apps/office/test
npm run typecheck
npm run build --workspace @estimator/office
```

### Task 2: Restore through staging and preserve the old directory

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** restore through checked staging with the service stopped
- **Need:** corrupt or unsafe recovery input must not replace otherwise usable business records. Specifically, restore through checked staging with the service stopped
- **Value or failure prevented:** replace data only after validation while retaining the previous directory

#### Scope and acceptance

Stopped-service staging, SQLite checks and final swap preserve the pre-restore directory.

- Intake forecast: 4 hours (S), not measured time or implementation approval.
- Ownership: after validator / restore service.
- Direct prerequisite task numbers: 1.

**Verification Commands:**

```sh
npm test -- apps/office/test
npm run typecheck
npm run build --workspace @estimator/office
```

### Task 3: Prove identity and evidence preservation after restore

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** compare restored identities, records, settings and evidence
- **Need:** corrupt or unsafe recovery input must not replace otherwise usable business records. Specifically, compare restored identities, records, settings and evidence
- **Value or failure prevented:** confirm the isolated recovery preserved actual business data and file bytes

#### Scope and acceptance

Compare current records/settings/observations/attachments in a real isolated restored store.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: fixture after validator; prove after restore / recovery evidence.
- Direct prerequisite task numbers: 2.

**Verification Commands:**

```sh
npm test -- apps/office/test
npm run typecheck
npm run build --workspace @estimator/office
```

