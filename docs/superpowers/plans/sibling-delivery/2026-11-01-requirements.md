# Explain material cuts and stock requirements: sibling delivery plan

Owner-authorized backlog creation on November 1, 2026. **Application implementation is not authorized.** This plan supplies source scope/intent for intake; native refinement, implementation planning and approval remain later gates.

## Scope

Inspect short-return material requirements, attachments and conservative unused stock.

Root-level sibling epic only. Children deliver to this epic branch; all children complete → integrated epic Test/Review → trunk → same-SHA Cloudflare deployment and local Mac build → owner tests both. One orchestrator; at most three workers globally. No nested epic or outer integration branch.

## Technical lineage

Reviewed source Task(s) 1 in `docs/superpowers/plans/2026-11-01-first-usable-project-estimator.md`; trial specification acceptance cases 1–11 only. The reviewed files remain unchanged. Preserve all owner recipe/prices/settings/origin checkpoints and deferred-feature boundaries. Synthetic fixtures remain draft/test-only.

## Prerequisites and ownership

Prerequisite sibling keys: bays, catalog. Cross-epic dependencies mean completed code on trunk.

1 owns recipe persistence and 2 owns material derivation; they may run independently using trunk contracts. After 2, stories 3 and 4 own separate helpers. Story 5 integrates all results.

A shared schema/export/store migration/HTTP route/App composition/lockfile has one designated owner. Consumers use the accepted epic-head contract and disjoint files. Partial renderer preparation is not a complete parallel-ready story when its producer is still missing. No gate/Full-Auto preference is changed.

## Story Intent

- **Beneficiary:** construction business owner
- **Capability:** explain material cuts and stock requirements
- **Need:** installed pieces and purchased stock differ, especially at short returns and shared supports
- **Value or failure prevented:** account for short pieces, supports and conservative stock purchases

## Implementation Tasks

### Task 1: Retain owner-validated recipe versions

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** retain and select owner-validated recipe versions
- **Need:** installed pieces and purchased stock differ, especially at short returns and shared supports. Specifically, retain and select owner-validated recipe versions
- **Value or failure prevented:** change construction rules without reinterpreting earlier references

#### Scope and acceptance

Persist/select the actual owner-validated recipe; a changed referenced (id,version) body is refused, a new version requires renewed owner validation, and old identities remain available.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: recipe schema and catalog store on trunk / recipe repository.
- Direct prerequisite task numbers: None.

**Verification Commands:**

```sh
npm test -- packages/domain/test apps/office/test
npm run typecheck
npm run build --workspace @estimator/office
```

### Task 2: Derive installed material requirements

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** derive installed material quantities for each rule and run
- **Need:** installed pieces and purchased stock differ, especially at short returns and shared supports. Specifically, derive installed material quantities for each rule and run
- **Value or failure prevented:** count shared supports once and preserve per-run coverage rounding

#### Scope and acceptance

Post/bay/run-coverage rules preserve per-run rounding and allocate shared supports once.

- Intake forecast: 4 hours (S), not measured time or implementation approval.
- Ownership: prerequisite / requirement contract.
- Direct prerequisite task numbers: None.

**Verification Commands:**

```sh
npm test -- packages/domain/test apps/office/test
npm run typecheck
npm run build --workspace @estimator/office
```

### Task 3: Retain cuts and conservative stock use

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** retain individual cuts, waste and unused stock
- **Need:** installed pieces and purchased stock differ, especially at short returns and shared supports. Specifically, retain individual cuts, waste and unused stock
- **Value or failure prevented:** see the cost consequences of short returns and no offcut reuse

#### Scope and acceptance

Oversized cuts reject; no-reuse stock, waste and unused lengths reconcile.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: after requirement contract / cut helper.
- Direct prerequisite task numbers: 2.

**Verification Commands:**

```sh
npm test -- packages/domain/test apps/office/test
npm run typecheck
npm run build --workspace @estimator/office
```

### Task 4: Count fasteners from installed pieces

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** derive fasteners from installed pieces
- **Need:** installed pieces and purchased stock differ, especially at short returns and shared supports. Specifically, derive fasteners from installed pieces
- **Value or failure prevented:** avoid charging attachments for spare purchased stock

#### Scope and acceptance

Attachments derive from installed rather than spare pieces; invalid references/units are named.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: after requirement contract / attachment helper.
- Direct prerequisite task numbers: 2.

**Verification Commands:**

```sh
npm test -- packages/domain/test apps/office/test
npm run typecheck
npm run build --workspace @estimator/office
```

### Task 5: Explain requirements and unused stock

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** inspect composed material and stock explanations
- **Need:** installed pieces and purchased stock differ, especially at short returns and shared supports. Specifically, inspect composed material and stock explanations
- **Value or failure prevented:** find missing inputs and reconcile the actual fence requirements

#### Scope and acceptance

Actual geometry composition and screen explain quantities/cuts/allowances with named incompleteness.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: after helpers / facade and UI.
- Direct prerequisite task numbers: 1, 3, 4.

**Verification Commands:**

```sh
npm test -- packages/domain/test apps/office/test
npm run typecheck
npm run build --workspace @estimator/office
```

