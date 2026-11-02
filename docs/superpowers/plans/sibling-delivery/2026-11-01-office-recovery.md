# Recover catalog and imported office evidence: sibling delivery plan

Owner-authorized backlog creation on November 1, 2026. **Application implementation is not authorized.** This plan supplies source scope/intent for intake; native refinement, implementation planning and approval remain later gates.

## Scope

Extend existing backup proof to real keys, archives, import links and delayed replay.

Root-level sibling epic only. Children deliver to this epic branch; all children complete → integrated epic Test/Review → trunk → same-SHA Cloudflare deployment and local Mac build → owner tests both. One orchestrator; at most three workers globally. No nested epic or outer integration branch.

## Technical lineage

Reviewed source Task(s) 10 in `docs/superpowers/plans/2026-11-01-first-usable-project-estimator.md`; trial specification acceptance cases 1–11 only. The reviewed files remain unchanged. Preserve all owner recipe/prices/settings/origin checkpoints and deferred-feature boundaries. Synthetic fixtures remain draft/test-only.

## Prerequisites and ownership

Prerequisite sibling keys: backup-restore, catalog-release, import-accept. Cross-epic dependencies mean completed code on trunk.

Stories 1 and 2 use the merged backup extension API and may run independently only with separately owned archive/key and import fixture/test files. Shared backup core has one owner; do not concurrently edit a common fixture. Story 3 performs complete restore integration.

A shared schema/export/store migration/HTTP route/App composition/lockfile has one designated owner. Consumers use the accepted epic-head contract and disjoint files. Partial renderer preparation is not a complete parallel-ready story when its producer is still missing. No gate/Full-Auto preference is changed.

## Story Intent

- **Beneficiary:** construction business owner
- **Capability:** recover catalog and imported office evidence
- **Need:** publication keys and source mappings are needed for later recovery as well as database rows
- **Value or failure prevented:** restore the business record with its identities, credentials and duplicate protections intact

## Implementation Tasks

### Task 1: Verify current archive and key backup coverage

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** verify current archive and recovery-key backup coverage
- **Need:** publication keys and source mappings are needed for later recovery as well as database rows. Specifically, verify current archive and recovery-key backup coverage
- **Value or failure prevented:** restore the actual catalog publication evidence rather than an incomplete older backup inventory

#### Scope and acceptance

Extend the existing real-data recovery fixture and required-inventory checks for current generated artifacts; reuse the capture/restore implementation and earlier catalog-release key proof.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: existing backup inventory / extension owner.
- Direct prerequisite task numbers: None.

**Verification Commands:**

```sh
npm test -- packages/exchange/test apps/office/test
npm run typecheck
npm run build
```

### Task 2: Restore import mappings links and duplicate receipts

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** restore import mappings quote links and duplicate receipts
- **Need:** publication keys and source mappings are needed for later recovery as well as database rows. Specifically, restore import mappings quote links and duplicate receipts
- **Value or failure prevented:** preserve accepted identities and recognize delayed or repeated plaintext submissions

#### Scope and acceptance

A restored real accepted submission preserves identities and delayed plaintext replay needs no retired device key.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: fixed backup extension API / real-data fixture.
- Direct prerequisite task numbers: None.

**Verification Commands:**

```sh
npm test -- packages/exchange/test apps/office/test
npm run typecheck
npm run build
```

### Task 3: Verify the complete current office restore

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** verify a complete isolated restore of current office evidence
- **Need:** publication keys and source mappings are needed for later recovery as well as database rows. Specifically, verify a complete isolated restore of current office evidence
- **Value or failure prevented:** recover the business record without damaging source data or an existing destination

#### Scope and acceptance

Compare database, attachments, keys and archives; failed hash preserves destination and source data.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: after extensions / isolated restore evidence.
- Direct prerequisite task numbers: 1, 2.

**Verification Commands:**

```sh
npm test -- packages/exchange/test apps/office/test
npm run typecheck
npm run build
```

