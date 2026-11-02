# Prepare private field catalogs: sibling delivery plan

Owner-authorized backlog creation on November 1, 2026. **Application implementation is not authorized.** This plan supplies source scope/intent for intake; native refinement, implementation planning and approval remain later gates.

## Scope

Stage verified encrypted modules and explicitly produce enrollment credentials.

Root-level sibling epic only. Children deliver to this epic branch; all children complete → integrated epic Test/Review → trunk → same-SHA Cloudflare deployment and local Mac build → owner tests both. One orchestrator; at most three workers globally. No nested epic or outer integration branch.

## Technical lineage

Reviewed source Task(s) 6 in `docs/superpowers/plans/2026-11-01-first-usable-project-estimator.md`; trial specification acceptance cases 1–11 only. The reviewed files remain unchanged. Preserve all owner recipe/prices/settings/origin checkpoints and deferred-feature boundaries. Synthetic fixtures remain draft/test-only.

## Prerequisites and ownership

Prerequisite sibling keys: proposals, backup-restore. Cross-epic dependencies mean completed code on trunk.

After story 1 closes the complete release contract, stories 2, 3 and 4 can run in parallel on separate archive, staging and key/QR helpers and tests. Story 5 integrates completed helpers; shared schemas, exports and Publishing composition have one owner.

A shared schema/export/store migration/HTTP route/App composition/lockfile has one designated owner. Consumers use the accepted epic-head contract and disjoint files. Partial renderer preparation is not a complete parallel-ready story when its producer is still missing. No gate/Full-Auto preference is changed.

## Story Intent

- **Beneficiary:** construction business owner
- **Capability:** prepare private field catalogs
- **Need:** only validated catalog data may be distributed while credentials and business records stay local
- **Value or failure prevented:** field users receive approved estimating data without exposing business records or credentials

## Implementation Tasks

### Task 1: Encrypt independently versioned catalog modules

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** encrypt independently versioned catalog modules
- **Need:** only validated catalog data may be distributed while credentials and business records stay local. Specifically, encrypt independently versioned catalog modules
- **Value or failure prevented:** approved private estimating data can be distributed without plaintext disclosure

#### Scope and acceptance

Fresh IVs/AAD, validated module references, tamper checks and unchanged ciphertext reuse work.

- Intake forecast: 4 hours (S), not measured time or implementation approval.
- Ownership: prerequisite / portable release contract.
- Direct prerequisite task numbers: None.

**Verification Commands:**

```sh
npm test -- packages/exchange/test apps/office/test
npm run typecheck
npm run build
```

### Task 2: Preserve published module and release identities

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** preserve published module and release identities
- **Need:** only validated catalog data may be distributed while credentials and business records stay local. Specifically, preserve published module and release identities
- **Value or failure prevented:** old releases remain explainable and cannot silently acquire different contents

#### Scope and acceptance

Changed content cannot reuse immutable identities; local archives remain available.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: after release contract / archive helper.
- Direct prerequisite task numbers: 1.

**Verification Commands:**

```sh
npm test -- packages/exchange/test apps/office/test
npm run typecheck
npm run build
```

### Task 3: Stage only verified public release artifacts

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** stage only verified selected publication artifacts
- **Need:** only validated catalog data may be distributed while credentials and business records stay local. Specifically, stage only verified selected publication artifacts
- **Value or failure prevented:** deployment includes a complete usable release without private office files

#### Scope and acceptance

Extend the foundation stager/verifier with validated selected ciphertext and current-manifest installation; no second deployment implementation or private-file copying.

- Intake forecast: 4 hours (S), not measured time or implementation approval.
- Ownership: after release contract / file helper.
- Direct prerequisite task numbers: 1.

**Verification Commands:**

```sh
npm test -- packages/exchange/test apps/office/test
npm run typecheck
npm run build
```

### Task 4: Keep credentials local and generate enrollment explicitly

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** keep credentials local and generate enrollment explicitly
- **Need:** only validated catalog data may be distributed while credentials and business records stay local. Specifically, keep credentials local and generate enrollment explicitly
- **Value or failure prevented:** register trusted devices and recover actual generated keys without publishing them

#### Scope and acceptance

Local key/QR/copy paths share one contract; actual generated keys and archives are captured/restored by the already-shipped backup adapter before this epic completes.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: after release contract / key and QR adapter.
- Direct prerequisite task numbers: 1.

**Verification Commands:**

```sh
npm test -- packages/exchange/test apps/office/test
npm run typecheck
npm run build
```

### Task 5: Preview the release and selected current-pack removal

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** inspect publication readiness and selected current-pack removals
- **Need:** only validated catalog data may be distributed while credentials and business records stay local. Specifically, inspect publication readiness and selected current-pack removals
- **Value or failure prevented:** approve the exact release while understanding the limits of removing old copies

#### Scope and acceptance

Production readiness is enforced and removed paths are shown without claiming revocation of old copies.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: after helpers / Publishing composition.
- Direct prerequisite task numbers: 2, 3, 4.

**Verification Commands:**

```sh
npm test -- packages/exchange/test apps/office/test
npm run typecheck
npm run build
```

