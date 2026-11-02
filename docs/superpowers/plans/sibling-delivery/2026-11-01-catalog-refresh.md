# Refresh catalogs and rotate keys safely: sibling delivery plan

Owner-authorized backlog creation on November 1, 2026. **Application implementation is not authorized.** This plan supplies source scope/intent for intake; native refinement, implementation planning and approval remain later gates.

## Scope

Install changed resources and preserve old access through failed or early rotation.

Root-level sibling epic only. Children deliver to this epic branch; all children complete → integrated epic Test/Review → trunk → same-SHA Cloudflare deployment and local Mac build → owner tests both. One orchestrator; at most three workers globally. No nested epic or outer integration branch.

## Technical lineage

Reviewed source Task(s) 8 in `docs/superpowers/plans/2026-11-01-first-usable-project-estimator.md`; trial specification acceptance cases 1–11 only. The reviewed files remain unchanged. Preserve all owner recipe/prices/settings/origin checkpoints and deferred-feature boundaries. Synthetic fixtures remain draft/test-only.

## Prerequisites and ownership

Prerequisite sibling keys: registration. Cross-epic dependencies mean completed code on trunk.

Stories 1, 2 and 3 consume registration APIs already on trunk and can run in separate fetch, rotation and lifecycle helpers/tests. One owner composes catalog-client and Updates after all three close. No concurrent shared-store/schema edits.

A shared schema/export/store migration/HTTP route/App composition/lockfile has one designated owner. Consumers use the accepted epic-head contract and disjoint files. Partial renderer preparation is not a complete parallel-ready story when its producer is still missing. No gate/Full-Auto preference is changed.

## Story Intent

- **Beneficiary:** construction business owner
- **Capability:** refresh catalogs and rotate keys safely
- **Need:** network interruptions, compatibility changes and early key scans can occur during updates
- **Value or failure prevented:** keep estimating through interrupted, incompatible or unavailable updates

## Implementation Tasks

### Task 1: Reuse unchanged modules and retain active data on failure

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** reuse unchanged modules and retain active data on failed refresh
- **Need:** network interruptions, compatibility changes and early key scans can occur during updates. Specifically, reuse unchanged modules and retain active data on failed refresh
- **Value or failure prevented:** receive current prices efficiently without losing usable estimating data

#### Scope and acceptance

Price-only update skips design; corrupt/offline/incompatible responses preserve active state.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: fixed refresh contract / fetch helper.
- Direct prerequisite task numbers: None.

**Verification Commands:**

```sh
npm test -- apps/field/test
npm run typecheck
npm run build --workspace @estimator/field
```

### Task 2: Promote a pending key only with a valid matching release

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** promote a pending key only with its valid matching release
- **Need:** network interruptions, compatibility changes and early key scans can occur during updates. Specifically, promote a pending key only with its valid matching release
- **Value or failure prevented:** prepare registration early and survive interrupted credential changes

#### Scope and acceptance

Early QR, unknown key, interrupted install and stale CAS retain old work; successful retry rotates atomically.

- Intake forecast: 4 hours (S), not measured time or implementation approval.
- Ownership: fixed activation API / rotation helper.
- Direct prerequisite task numbers: None.

**Verification Commands:**

```sh
npm test -- apps/field/test
npm run typecheck
npm run build --workspace @estimator/field
```

### Task 3: Schedule single-flight foreground catalog checks

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** check catalogs through a single foreground refresh flow
- **Need:** network interruptions, compatibility changes and early key scans can occur during updates. Specifically, check catalogs through a single foreground refresh flow
- **Value or failure prevented:** receive timely updates without races or promises of closed-app background work

#### Scope and acceptance

Launch/visibility/manual/visible interval checks do not race or promise closed-app background updates.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: fixed refresh service / lifecycle helper.
- Direct prerequisite task numbers: None.

**Verification Commands:**

```sh
npm test -- apps/field/test
npm run typecheck
npm run build --workspace @estimator/field
```

### Task 4: Explain refresh and registration status accurately

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** inspect accurate refresh and registration status
- **Need:** network interruptions, compatibility changes and early key scans can occur during updates. Specifically, inspect accurate refresh and registration status
- **Value or failure prevented:** distinguish offline checks, incompatible releases and missing credentials before acting

#### Scope and acceptance

App/key/retry/offline distinctions and attempted/successful timestamps remain truthful.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: after helpers / Updates composition.
- Direct prerequisite task numbers: 1, 2, 3.

**Verification Commands:**

```sh
npm test -- apps/field/test
npm run typecheck
npm run build --workspace @estimator/field
```

