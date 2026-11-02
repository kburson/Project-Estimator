# Review returned field work in the office: sibling delivery plan

Owner-authorized backlog creation on November 1, 2026. **Application implementation is not authorized.** This plan supplies source scope/intent for intake; native refinement, implementation planning and approval remain later gates.

## Scope

Inspect source identities/conflicts without modifying business records.

Root-level sibling epic only. Children deliver to this epic branch; all children complete → integrated epic Test/Review → trunk → same-SHA Cloudflare deployment and local Mac build → owner tests both. One orchestrator; at most three workers globally. No nested epic or outer integration branch.

## Technical lineage

Reviewed source Task(s) 9 in `docs/superpowers/plans/2026-11-01-first-usable-project-estimator.md`; trial specification acceptance cases 1–11 only. The reviewed files remain unchanged. Preserve all owner recipe/prices/settings/origin checkpoints and deferred-feature boundaries. Synthetic fixtures remain draft/test-only.

## Prerequisites and ownership

Prerequisite sibling keys: field-returns, visits. Cross-epic dependencies mean completed code on trunk.

Story 1 must establish the complete import-context contract and durable mapping-read schema. Stories 2 and 3 then run in separate context-reader and portable-planner files/tests. Story 2 cannot consume unmerged import-accept code. Story 4 integrates completed helpers into read-only UI.

A shared schema/export/store migration/HTTP route/App composition/lockfile has one designated owner. Consumers use the accepted epic-head contract and disjoint files. Partial renderer preparation is not a complete parallel-ready story when its producer is still missing. No gate/Full-Auto preference is changed.

## Story Intent

- **Beneficiary:** construction business owner
- **Capability:** review returned field work in the office
- **Need:** field and office records can describe the same customer without sharing identifiers or revision context
- **Value or failure prevented:** recognize conflicts before anything changes in the business records

## Implementation Tasks

### Task 1: Validate received attachments before review

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** validate received attachments before review
- **Need:** field and office records can describe the same customer without sharing identifiers or revision context. Specifically, validate received attachments before review
- **Value or failure prevented:** reject corrupt or inappropriate files before they affect office records

#### Scope and acceptance

Wrong business/schema/size/hash/references reject; instruction-like notes are inert text.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: prerequisite / receive boundary.
- Direct prerequisite task numbers: None.

**Verification Commands:**

```sh
npm test -- packages/exchange/test apps/office/test
npm run typecheck
npm run build
```

### Task 2: Read existing source mappings without name-based merging

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** resolve retained source mappings without merging by name
- **Need:** field and office records can describe the same customer without sharing identifiers or revision context. Specifically, resolve retained source mappings without merging by name
- **Value or failure prevented:** identify the intended office records while preserving explicit identity decisions

#### Scope and acceptance

Business/device/entity/source identity drives suggestions, never implicit replacement.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: after context contract / mapping reader.
- Direct prerequisite task numbers: 1.

**Verification Commands:**

```sh
npm test -- packages/exchange/test apps/office/test
npm run typecheck
npm run build
```

### Task 3: Explain identity and base-revision conflicts

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** inspect identity and base-revision conflicts
- **Need:** field and office records can describe the same customer without sharing identifiers or revision context. Specifically, inspect identity and base-revision conflicts
- **Value or failure prevented:** understand stale or missing context before choosing how returned work should be handled

#### Scope and acceptance

Missing/stale base and ID/content conflicts retain original values and explicit choices.

- Intake forecast: 4 hours (S), not measured time or implementation approval.
- Ownership: fixed context contract / portable planner.
- Direct prerequisite task numbers: 1.

**Verification Commands:**

```sh
npm test -- packages/exchange/test apps/office/test
npm run typecheck
npm run build
```

### Task 4: Review source values and office target choices

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** compare original source values with selected office targets
- **Need:** field and office records can describe the same customer without sharing identifiers or revision context. Specifically, compare original source values with selected office targets
- **Value or failure prevented:** review intended changes and cancel without changing business data

#### Scope and acceptance

Original/target comparison is clear; cancel writes no business data and acceptance is unavailable until implemented.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: after validator/context/planner / read-only UI.
- Direct prerequisite task numbers: 2, 3.

**Verification Commands:**

```sh
npm test -- packages/exchange/test apps/office/test
npm run typecheck
npm run build
```

