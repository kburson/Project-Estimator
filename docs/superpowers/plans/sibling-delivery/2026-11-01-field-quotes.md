# Present retained field quotes: sibling delivery plan

Owner-authorized backlog creation on November 1, 2026. **Application implementation is not authorized.** This plan supplies source scope/intent for intake; native refinement, implementation planning and approval remain later gates.

## Scope

Freeze Preliminary snapshots and export the shared customer-safe PDF.

Root-level sibling epic only. Children deliver to this epic branch; all children complete → integrated epic Test/Review → trunk → same-SHA Cloudflare deployment and local Mac build → owner tests both. One orchestrator; at most three workers globally. No nested epic or outer integration branch.

## Technical lineage

Reviewed source Task(s) 7 in `docs/superpowers/plans/2026-11-01-first-usable-project-estimator.md`; trial specification acceptance cases 1–11 only. The reviewed files remain unchanged. Preserve all owner recipe/prices/settings/origin checkpoints and deferred-feature boundaries. Synthetic fixtures remain draft/test-only.

## Prerequisites and ownership

Prerequisite sibling keys: field-visits, registration, proposals. Cross-epic dependencies mean completed code on trunk.

Stories 1, 2 and 3 consume merged calculator/freeze/ProposalModel APIs and own separate controls, quote adapter and PDF/file adapters/tests. Store changes have one owner. Story 4 integrates completed adapters and controls.

A shared schema/export/store migration/HTTP route/App composition/lockfile has one designated owner. Consumers use the accepted epic-head contract and disjoint files. Partial renderer preparation is not a complete parallel-ready story when its producer is still missing. No gate/Full-Auto preference is changed.

## Story Intent

- **Beneficiary:** construction business owner
- **Capability:** present retained field quotes
- **Need:** field repricing or registration changes must not alter a retained customer presentation
- **Value or failure prevented:** preserve exactly what customers saw while protecting internal costing details

## Implementation Tasks

### Task 1: Enter field allowances and selling adjustments

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** enter field allowances and selling adjustments under the shared rules
- **Need:** field repricing or registration changes must not alter a retained customer presentation. Specifically, enter field allowances and selling adjustments under the shared rules
- **Value or failure prevented:** account for manual work without inventing hours or disguising incomplete automatic inputs

#### Scope and acceptance

Manual gate/tax/override/clear behavior matches the Mac and does not invent hours or completeness.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: fixed shared calculator / internal controls.
- Direct prerequisite task numbers: None.

**Verification Commands:**

```sh
npm test -- apps/field/test
npm run typecheck
npm run build --workspace @estimator/field
```

### Task 2: Freeze durable Preliminary field snapshots

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** freeze durable Preliminary field snapshots
- **Need:** field repricing or registration changes must not alter a retained customer presentation. Specifically, freeze durable Preliminary field snapshots
- **Value or failure prevented:** retain the exact complete calculation presented to a customer

#### Scope and acceptance

Stale/incomplete inputs reject and unique immutable snapshots read independently of keys/catalog.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: fixed freeze API / quote adapter.
- Direct prerequisite task numbers: None.

**Verification Commands:**

```sh
npm test -- apps/field/test
npm run typecheck
npm run build --workspace @estimator/field
```

### Task 3: Export the shared customer-safe field PDF

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** export the shared customer-safe PDF
- **Need:** field repricing or registration changes must not alter a retained customer presentation. Specifically, export the shared customer-safe PDF
- **Value or failure prevented:** give customers readable proposals without internal rates or costing details

#### Scope and acceptance

Shared renderer uses no network fonts and exports no internal fields.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: fixed ProposalModel / files-PDF adapter.
- Direct prerequisite task numbers: None.

**Verification Commands:**

```sh
npm test -- apps/field/test
npm run typecheck
npm run build --workspace @estimator/field
```

### Task 4: Present retained quotes after explicit repricing

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** reopen presented quotes after explicit draft repricing
- **Need:** field repricing or registration changes must not alter a retained customer presentation. Specifically, reopen presented quotes after explicit draft repricing
- **Value or failure prevented:** preserve the original customer commitment while reviewing changed work separately

#### Scope and acceptance

Saved status/totals remain unchanged after draft repricing and key/catalog removal.

- Intake forecast: 2 hours (XS), not measured time or implementation approval.
- Ownership: after adapters and controls / integration.
- Direct prerequisite task numbers: 1, 2, 3.

**Verification Commands:**

```sh
npm test -- apps/field/test
npm run typecheck
npm run build --workspace @estimator/field
```

