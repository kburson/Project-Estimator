# Explain purchased packs and eligible prices: sibling delivery plan

Owner-authorized backlog creation on November 1, 2026. **Application implementation is not authorized.** This plan supplies source scope/intent for intake; native refinement, implementation planning and approval remain later gates.

## Scope

Inspect rounded packs, eligible tiers, tax, provenance and exact allocations.

Root-level sibling epic only. Children deliver to this epic branch; all children complete → integrated epic Test/Review → trunk → same-SHA Cloudflare deployment and local Mac build → owner tests both. One orchestrator; at most three workers globally. No nested epic or outer integration branch.

## Technical lineage

Reviewed source Task(s) 2 in `docs/superpowers/plans/2026-11-01-first-usable-project-estimator.md`; trial specification acceptance cases 1–11 only. The reviewed files remain unchanged. Preserve all owner recipe/prices/settings/origin checkpoints and deferred-feature boundaries. Synthetic fixtures remain draft/test-only.

## Prerequisites and ownership

Prerequisite sibling keys: requirements, prices. Cross-epic dependencies mean completed code on trunk.

1 produces pooled quantities; 2 and 3 own separate eligibility and costing helpers; 4 composes them; 5 consumes the real facade.

A shared schema/export/store migration/HTTP route/App composition/lockfile has one designated owner. Consumers use the accepted epic-head contract and disjoint files. Partial renderer preparation is not a complete parallel-ready story when its producer is still missing. No gate/Full-Auto preference is changed.

## Story Intent

- **Beneficiary:** construction business owner
- **Capability:** explain purchased packs and eligible prices
- **Need:** whole-pack rounding and eligible discounts depend on combined purchased quantities
- **Value or failure prevented:** understand actual purchase cost and its exact allocation

## Implementation Tasks

### Task 1: Pool requirements before package rounding

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** pool requirements by selected offer before rounding packs
- **Need:** whole-pack rounding and eligible discounts depend on combined purchased quantities. Specifically, pool requirements by selected offer before rounding packs
- **Value or failure prevented:** avoid duplicate pack rounding and incompatible purchase units

#### Scope and acceptance

Selected/default offers only; whole-pack rounding occurs once and unit/rental mismatches reject.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: prerequisite / purchase pool contract.
- Direct prerequisite task numbers: None.

**Verification Commands:**

```sh
npm test -- packages/domain/test apps/office/test
npm run typecheck
npm run build --workspace @estimator/office
```

### Task 2: Select only permitted pricing arrangements

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** select permitted arrangements using purchased quantities
- **Need:** whole-pack rounding and eligible discounts depend on combined purchased quantities. Specifically, select permitted arrangements using purchased quantities
- **Value or failure prevented:** honor valid explicit choices without invented stacked discounts

#### Scope and acceptance

Purchased-unit thresholds, explicit noncheapest choices, non-stacking and deterministic ties are correct.

- Intake forecast: 4 hours (S), not measured time or implementation approval.
- Ownership: after pool contract / tier helper.
- Direct prerequisite task numbers: 1.

**Verification Commands:**

```sh
npm test -- packages/domain/test apps/office/test
npm run typecheck
npm run build --workspace @estimator/office
```

### Task 3: Extend tax-inclusive costs and allocate cents

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** extend precise tax-inclusive prices and allocate every cent
- **Need:** whole-pack rounding and eligible discounts depend on combined purchased quantities. Specifically, extend precise tax-inclusive prices and allocate every cent
- **Value or failure prevented:** reconcile segment charges to the actual pooled purchase cost

#### Scope and acceptance

Fractional unit precision and tax basis remain exact; allocations conserve every cent.

- Intake forecast: 4 hours (S), not measured time or implementation approval.
- Ownership: after pool contract / cost helper.
- Direct prerequisite task numbers: 1.

**Verification Commands:**

```sh
npm test -- packages/domain/test apps/office/test
npm run typecheck
npm run build --workspace @estimator/office
```

### Task 4: Compose purchase provenance and named failures

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** retain selected price provenance and named purchase failures
- **Need:** whole-pack rounding and eligible discounts depend on combined purchased quantities. Specifically, retain selected price provenance and named purchase failures
- **Value or failure prevented:** explain costs without disguising missing prices or taxes as zero

#### Scope and acceptance

Chosen observation/arrangement is retained; absent prices/tax/units never become fabricated zero.

- Intake forecast: 2 hours (XS), not measured time or implementation approval.
- Ownership: after helpers / pricing facade.
- Direct prerequisite task numbers: 2, 3.

**Verification Commands:**

```sh
npm test -- packages/domain/test apps/office/test
npm run typecheck
npm run build --workspace @estimator/office
```

### Task 5: Inspect pack spares and selected-price provenance

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** inspect selected tiers, pack spares and allocated costs
- **Need:** whole-pack rounding and eligible discounts depend on combined purchased quantities. Specifically, inspect selected tiers, pack spares and allocated costs
- **Value or failure prevented:** review why the estimate buys and charges each quantity

#### Scope and acceptance

UI explains purchases, unused stock, allocation and actual selection failures.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: after facade / office display.
- Direct prerequisite task numbers: 4.

**Verification Commands:**

```sh
npm test -- packages/domain/test apps/office/test
npm run typecheck
npm run build --workspace @estimator/office
```

