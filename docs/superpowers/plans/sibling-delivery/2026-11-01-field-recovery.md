# Recover field work after storage loss: sibling delivery plan

Owner-authorized backlog creation on November 1, 2026. **Application implementation is not authorized.** This plan supplies source scope/intent for intake; native refinement, implementation planning and approval remain later gates.

## Scope

Export and restore reviewed local work without credential or identity loss.

Root-level sibling epic only. Children deliver to this epic branch; all children complete → integrated epic Test/Review → trunk → same-SHA Cloudflare deployment and local Mac build → owner tests both. One orchestrator; at most three workers globally. No nested epic or outer integration branch.

## Technical lineage

Reviewed source Task(s) 10 in `docs/superpowers/plans/2026-11-01-first-usable-project-estimator.md`; trial specification acceptance cases 1–11 only. The reviewed files remain unchanged. Preserve all owner recipe/prices/settings/origin checkpoints and deferred-feature boundaries. Synthetic fixtures remain draft/test-only.

## Prerequisites and ownership

Prerequisite sibling keys: field-returns. Cross-epic dependencies mean completed code on trunk.

Story 1 closes recovery and preview contracts. Preview helper story 2 and transaction/store story 3 then run independently against those contracts in separate files/tests. One owner composes the service/UI in story 4 after both helpers close.

A shared schema/export/store migration/HTTP route/App composition/lockfile has one designated owner. Consumers use the accepted epic-head contract and disjoint files. Partial renderer preparation is not a complete parallel-ready story when its producer is still missing. No gate/Full-Auto preference is changed.

## Story Intent

- **Beneficiary:** construction business owner
- **Capability:** recover field work after storage loss
- **Need:** browser persistence is not a backup and restored records can conflict with local identities
- **Value or failure prevented:** retain original work identities without treating browser persistence as backup

## Implementation Tasks

### Task 1: Export self-contained work without catalog credentials

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** export self-contained field work without catalog credentials
- **Need:** browser persistence is not a backup and restored records can conflict with local identities. Specifically, export self-contained field work without catalog credentials
- **Value or failure prevented:** retain a portable recovery copy without distributing enrollment secrets

#### Scope and acceptance

Checksummed snapshots preserve draft/customer/quote/outbox/device identity and truthful export failure.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: prerequisite / recovery contract.
- Direct prerequisite task numbers: None.

**Verification Commands:**

```sh
npm test -- apps/field/test
npm run typecheck
npm run build --workspace @estimator/field
```

### Task 2: Preview recovery identity conflicts without writes

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** preview recovery identity conflicts before writing
- **Need:** browser persistence is not a backup and restored records can conflict with local identities. Specifically, preview recovery identity conflicts before writing
- **Value or failure prevented:** choose how conflicting local records are handled without silently manufacturing copies

#### Scope and acceptance

Exact records are no-ops; conflicts and keep-existing/abort choices are explicit.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: after contract / preview helper.
- Direct prerequisite task numbers: 1.

**Verification Commands:**

```sh
npm test -- apps/field/test
npm run typecheck
npm run build --workspace @estimator/field
```

### Task 3: Restore reviewed rows in one rechecked transaction

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** restore reviewed rows in one rechecked transaction
- **Need:** browser persistence is not a backup and restored records can conflict with local identities. Specifically, restore reviewed rows in one rechecked transaction
- **Value or failure prevented:** preserve existing work if the target changes or recovery fails

#### Scope and acceptance

Changed hashes invalidate preview and injected failure leaves all prior rows intact.

- Intake forecast: 4 hours (S), not measured time or implementation approval.
- Ownership: after contract / store transaction.
- Direct prerequisite task numbers: 1.

**Verification Commands:**

```sh
npm test -- apps/field/test
npm run typecheck
npm run build --workspace @estimator/field
```

### Task 4: Recover into a separate profile and reenroll explicitly

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** recover into a separate profile and reenroll explicitly
- **Need:** browser persistence is not a backup and restored records can conflict with local identities. Specifically, recover into a separate profile and reenroll explicitly
- **Value or failure prevented:** restore original work identities while reacquiring catalog access through the normal registration path

#### Scope and acceptance

Original IDs and duplicate behavior survive while catalog credentials are reacquired separately.

- Intake forecast: 2 hours (XS), not measured time or implementation approval.
- Ownership: after preview/store/export / UI integration.
- Direct prerequisite task numbers: 2, 3.

**Verification Commands:**

```sh
npm test -- apps/field/test
npm run typecheck
npm run build --workspace @estimator/field
```

