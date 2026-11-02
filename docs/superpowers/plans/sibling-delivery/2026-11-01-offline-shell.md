# Launch the field application without network: sibling delivery plan

Owner-authorized backlog creation on November 1, 2026. **Application implementation is not authorized.** This plan supplies source scope/intent for intake; native refinement, implementation planning and approval remain later gates.

## Scope

Cold-open the production shell and existing work without fetching catalog requests through the worker.

Root-level sibling epic only. Children deliver to this epic branch; all children complete → integrated epic Test/Review → trunk → same-SHA Cloudflare deployment and local Mac build → owner tests both. One orchestrator; at most three workers globally. No nested epic or outer integration branch.

## Technical lineage

Reviewed source Task(s) 10 in `docs/superpowers/plans/2026-11-01-first-usable-project-estimator.md`; trial specification acceptance cases 1–11 only. The reviewed files remain unchanged. Preserve all owner recipe/prices/settings/origin checkpoints and deferred-feature boundaries. Synthetic fixtures remain draft/test-only.

## Prerequisites and ownership

Prerequisite sibling keys: registration, field-quotes, field-returns. Cross-epic dependencies mean completed code on trunk.

No genuine parallel story lane: exact asset metadata closes before worker behavior, completed worker behavior before registration, and actual integration before offline proof. Protocol drafts alone do not permit story 3 closure.

A shared schema/export/store migration/HTTP route/App composition/lockfile has one designated owner. Consumers use the accepted epic-head contract and disjoint files. Partial renderer preparation is not a complete parallel-ready story when its producer is still missing. No gate/Full-Auto preference is changed.

## Story Intent

- **Beneficiary:** construction business owner
- **Capability:** launch the field application without network
- **Need:** field work must remain accessible when neither the network nor office Mac is available
- **Value or failure prevented:** continue using saved work when neither the network nor office Mac is available

## Implementation Tasks

### Task 1: Generate exact versioned app-shell asset metadata

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** generate exact versioned app-shell asset metadata
- **Need:** field work must remain accessible when neither the network nor office Mac is available. Specifically, generate exact versioned app-shell asset metadata
- **Value or failure prevented:** identify every application resource needed for a complete offline launch

#### Scope and acceptance

Actual Expo chunks/fonts and version/hash metadata are listed with isolated worker typecheck.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: prerequisite / build assets.
- Direct prerequisite task numbers: None.

**Verification Commands:**

```sh
npm test -- apps/field/test
npm run typecheck
npm run build --workspace @estimator/field
```

### Task 2: Cache only the versioned application shell

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** cache only the versioned application shell
- **Need:** field work must remain accessible when neither the network nor office Mac is available. Specifically, cache only the versioned application shell
- **Value or failure prevented:** open offline without serving stale catalog manifests from the application cache

#### Scope and acceptance

Install precache/navigation fallback excludes catalog URLs and never skips waiting on install.

- Intake forecast: 4 hours (S), not measured time or implementation approval.
- Ownership: after asset interface / worker.
- Direct prerequisite task numbers: 1.

**Verification Commands:**

```sh
npm test -- apps/field/test
npm run typecheck
npm run build --workspace @estimator/field
```

### Task 3: Register the production worker without reloading edits

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** register the production worker without reloading edits
- **Need:** field work must remain accessible when neither the network nor office Mac is available. Specifically, register the production worker without reloading edits
- **Value or failure prevented:** install offline capability without interrupting work already in progress

#### Scope and acceptance

Correct production-only no-cache update behavior distinguishes initial install from requested activation.

- Intake forecast: 2 hours (XS), not measured time or implementation approval.
- Ownership: after worker protocol / registration adapter.
- Direct prerequisite task numbers: 2.

**Verification Commands:**

```sh
npm test -- apps/field/test
npm run typecheck
npm run build --workspace @estimator/field
```

### Task 4: Cold-open retained work and PDF output offline

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** cold-open retained work and customer PDFs without network
- **Need:** field work must remain accessible when neither the network nor office Mac is available. Specifically, cold-open retained work and customer PDFs without network
- **Value or failure prevented:** continue a site visit using saved records when connectivity disappears

#### Scope and acceptance

Built app reopens drafts/catalog/quotes/outbox without network; physical acceptance stays separate.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: after shell and adapter / browser proof.
- Direct prerequisite task numbers: 3.

**Verification Commands:**

```sh
npm test -- apps/field/test
npm run typecheck
npm run build --workspace @estimator/field
```

