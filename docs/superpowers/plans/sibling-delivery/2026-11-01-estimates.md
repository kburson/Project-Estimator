# Calculate and explicitly reprice saved estimates: sibling delivery plan

Owner-authorized backlog creation on November 1, 2026. **Application implementation is not authorized.** This plan supplies source scope/intent for intake; native refinement, implementation planning and approval remain later gates.

## Scope

Use actual shared results and review changes before repricing durable work.

Root-level sibling epic only. Children deliver to this epic branch; all children complete → integrated epic Test/Review → trunk → same-SHA Cloudflare deployment and local Mac build → owner tests both. One orchestrator; at most three workers globally. No nested epic or outer integration branch.

## Technical lineage

Reviewed source Task(s) 3, 4 in `docs/superpowers/plans/2026-11-01-first-usable-project-estimator.md`; trial specification acceptance cases 1–11 only. The reviewed files remain unchanged. Preserve all owner recipe/prices/settings/origin checkpoints and deferred-feature boundaries. Synthetic fixtures remain draft/test-only.

## Prerequisites and ownership

Prerequisite sibling keys: run-editing, costs. Cross-epic dependencies mean completed code on trunk.

Stories 1, 2, 3 and 4 consume trunk contracts and may own separate controls/services. Story 5 is integration. The freshness controller has one owner.

A shared schema/export/store migration/HTTP route/App composition/lockfile has one designated owner. Consumers use the accepted epic-head contract and disjoint files. Partial renderer preparation is not a complete parallel-ready story when its producer is still missing. No gate/Full-Auto preference is changed.

## Story Intent

- **Beneficiary:** construction business owner
- **Capability:** calculate and explicitly reprice saved estimates
- **Need:** edited measurements and current prices can diverge from the retained calculation
- **Value or failure prevented:** control selling changes without silently replacing retained work

## Implementation Tasks

### Task 1: Edit explicit manual allowances

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** edit manual work quantities, categories, sources and tax decisions
- **Need:** edited measurements and current prices can diverge from the retained calculation. Specifically, edit manual work quantities, categories, sources and tax decisions
- **Value or failure prevented:** include documented allowances without invented hours or automatic geometry changes

#### Scope and acceptance

Quantity/category/source/tax/gate confirmations round-trip without invented hours or automatic geometry changes.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: fixed manual contract / allowance controls.
- Direct prerequisite task numbers: None.

**Verification Commands:**

```sh
npm test -- packages/domain/test apps/office/test
npm run typecheck
npm run build --workspace @estimator/office
```

### Task 2: Edit and clear segment selling adjustments

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** set and clear segment markup or selling overrides
- **Need:** edited measurements and current prices can diverge from the retained calculation. Specifically, set and clear segment markup or selling overrides
- **Value or failure prevented:** control selling prices with visible fallback behavior

#### Scope and acceptance

Override/markup precedence is visible and clearing restores the defined fallback.

- Intake forecast: 2 hours (XS), not measured time or implementation approval.
- Ownership: fixed adjustment contract / selling controls.
- Direct prerequisite task numbers: None.

**Verification Commands:**

```sh
npm test -- packages/domain/test apps/office/test
npm run typecheck
npm run build --workspace @estimator/office
```

### Task 3: Track canonical calculation freshness

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** recognize when edited inputs no longer match the saved calculation
- **Need:** edited measurements and current prices can diverge from the retained calculation. Specifically, recognize when edited inputs no longer match the saved calculation
- **Value or failure prevented:** avoid presenting stale results as current

#### Scope and acceptance

Pending input/result mismatch is visibly stale and cannot be presented.

- Intake forecast: 2 hours (XS), not measured time or implementation approval.
- Ownership: canonical serializer / freshness service.
- Direct prerequisite task numbers: None.

**Verification Commands:**

```sh
npm test -- packages/domain/test apps/office/test
npm run typecheck
npm run build --workspace @estimator/office
```

### Task 4: Display internal estimate explanations

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** inspect quantities, price provenance, hours and segment totals
- **Need:** edited measurements and current prices can diverge from the retained calculation. Specifically, inspect quantities, price provenance, hours and segment totals
- **Value or failure prevented:** understand costs while recognizing incomplete results

#### Scope and acceptance

Known quantities/provenance/person-hours/cost/selling/tax display without labeling incomplete results valid.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: fixed result schema / Estimate view.
- Direct prerequisite task numbers: None.

**Verification Commands:**

```sh
npm test -- packages/domain/test apps/office/test
npm run typecheck
npm run build --workspace @estimator/office
```

### Task 5: Review and accept explicit repricing changes

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** compare and accept explicit purchase, tier and selling changes
- **Need:** edited measurements and current prices can diverge from the retained calculation. Specifically, compare and accept explicit purchase, tier and selling changes
- **Value or failure prevented:** reprice deliberately while retaining existing quote history

#### Scope and acceptance

Before/after purchase/tier/selling totals are visible; accepted reprice preserves prior quote snapshots.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: after controls/view; reuse visits calculation adapter / composition.
- Direct prerequisite task numbers: 1, 2, 3, 4.

**Verification Commands:**

```sh
npm test -- packages/domain/test apps/office/test
npm run typecheck
npm run build --workspace @estimator/office
```

