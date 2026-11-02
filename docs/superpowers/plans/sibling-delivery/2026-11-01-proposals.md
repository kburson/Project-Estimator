# Export customer-safe proposals: sibling delivery plan

Owner-authorized backlog creation on November 1, 2026. **Application implementation is not authorized.** This plan supplies source scope/intent for intake; native refinement, implementation planning and approval remain later gates.

## Scope

View and export readable frozen proposals without internal costing fields.

Root-level sibling epic only. Children deliver to this epic branch; all children complete → integrated epic Test/Review → trunk → same-SHA Cloudflare deployment and local Mac build → owner tests both. One orchestrator; at most three workers globally. No nested epic or outer integration branch.

## Technical lineage

Reviewed source Task(s) 5 in `docs/superpowers/plans/2026-11-01-first-usable-project-estimator.md`; trial specification acceptance cases 1–11 only. The reviewed files remain unchanged. Preserve all owner recipe/prices/settings/origin checkpoints and deferred-feature boundaries. Synthetic fixtures remain draft/test-only.

## Prerequisites and ownership

Prerequisite sibling keys: quotes. Cross-epic dependencies mean completed code on trunk.

1 produces the strict customer model; 2 owns portable PDF rendering and 3 the customer screen; 4 integrates export and visual inspection.

A shared schema/export/store migration/HTTP route/App composition/lockfile has one designated owner. Consumers use the accepted epic-head contract and disjoint files. Partial renderer preparation is not a complete parallel-ready story when its producer is still missing. No gate/Full-Auto preference is changed.

## Story Intent

- **Beneficiary:** construction business owner
- **Capability:** export customer-safe proposals
- **Need:** internal costing must not leak into customer output and long text must remain readable
- **Value or failure prevented:** share frozen selling terms without exposing internal costing details

## Implementation Tasks

### Task 1: Project frozen quotes into the strict customer model

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** project frozen quotes into an explicit customer-only model
- **Need:** internal costing must not leak into customer output and long text must remain readable. Specifically, project frozen quotes into an explicit customer-only model
- **Value or failure prevented:** share scope and selling totals without internal rates, costs or hours

#### Scope and acceptance

Exact allowlist includes reviewed manual descriptions and excludes internal rates/hours/cost/markup.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: prerequisite / ProposalModel.
- Direct prerequisite task numbers: None.

**Verification Commands:**

```sh
npm test -- packages/domain/test packages/exchange/test apps/office/test
npm run typecheck
npm run build --workspace @estimator/office
```

### Task 2: Render wrapped and paginated proposal PDFs

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** render wrapped multipage proposal PDFs without network fonts
- **Need:** internal costing must not leak into customer output and long text must remain readable. Specifically, render wrapped multipage proposal PDFs without network fonts
- **Value or failure prevented:** produce readable portable documents with retained quote identity and totals

#### Scope and acceptance

Bundled fonts, long text, page breaks, repeated status/ID and totals work without network fonts.

- Intake forecast: 4 hours (S), not measured time or implementation approval.
- Ownership: after model / portable PDF renderer.
- Direct prerequisite task numbers: 1.

**Verification Commands:**

```sh
npm test -- packages/domain/test packages/exchange/test apps/office/test
npm run typecheck
npm run build --workspace @estimator/office
```

### Task 3: Display proposals from retained customer models

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** display proposals using only validated customer data
- **Need:** internal costing must not leak into customer output and long text must remain readable. Specifically, display proposals using only validated customer data
- **Value or failure prevented:** present retained selling terms without accidental internal disclosure

#### Scope and acceptance

Validated customer-only data and readable segment labels render without internal-object access.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: after model / customer view.
- Direct prerequisite task numbers: 1.

**Verification Commands:**

```sh
npm test -- packages/domain/test packages/exchange/test apps/office/test
npm run typecheck
npm run build --workspace @estimator/office
```

### Task 4: Export and inspect frozen proposal files

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** export and inspect actual frozen proposal files
- **Need:** internal costing must not leak into customer output and long text must remain readable. Specifically, export and inspect actual frozen proposal files
- **Value or failure prevented:** catch layout or unsupported-text failures while preserving the saved quote

#### Scope and acceptance

Unsupported characters name the field and retain the snapshot; actual short/multipage output is visually checked.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: after renderer and view / export integration.
- Direct prerequisite task numbers: 2, 3.

**Verification Commands:**

```sh
npm test -- packages/domain/test packages/exchange/test apps/office/test
npm run typecheck
npm run build --workspace @estimator/office
```

