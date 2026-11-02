# Register a device and install its first catalog: sibling delivery plan

Owner-authorized backlog creation on November 1, 2026. **Application implementation is not authorized.** This plan supplies source scope/intent for intake; native refinement, implementation planning and approval remain later gates.

## Scope

Enroll once and atomically install/view validated catalog data, without requiring an existing job.

Root-level sibling epic only. Children deliver to this epic branch; all children complete → integrated epic Test/Review → trunk → same-SHA Cloudflare deployment and local Mac build → owner tests both. One orchestrator; at most three workers globally. No nested epic or outer integration branch.

## Technical lineage

Reviewed source Task(s) 7, 8 in `docs/superpowers/plans/2026-11-01-first-usable-project-estimator.md`; trial specification acceptance cases 1–11 only. The reviewed files remain unchanged. Preserve all owner recipe/prices/settings/origin checkpoints and deferred-feature boundaries. Synthetic fixtures remain draft/test-only.

## Prerequisites and ownership

Prerequisite sibling keys: catalog-release, foundation. Cross-epic dependencies mean completed code on trunk.

After parser story 1, store story 2 and QR story 4 can run independently. Client story 3 follows store closure and can overlap QR/fallback stories 4 and 5. Status story 6 follows client closure and may overlap separate fallback components. Story 7 follows status composition; Updates composition remains single-owned.

A shared schema/export/store migration/HTTP route/App composition/lockfile has one designated owner. Consumers use the accepted epic-head contract and disjoint files. Partial renderer preparation is not a complete parallel-ready story when its producer is still missing. No gate/Full-Auto preference is changed.

## Story Intent

- **Beneficiary:** construction business owner
- **Capability:** register a device and install its first catalog
- **Need:** new credentials cannot replace working catalog access before a complete matching update validates
- **Value or failure prevented:** start field work with validated data while retaining recoverable registration paths

## Implementation Tasks

### Task 1: Validate enrollment without replacing active registration

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** validate enrollment without displacing active registration
- **Need:** new credentials cannot replace working catalog access before a complete matching update validates. Specifically, validate enrollment without displacing active registration
- **Value or failure prevented:** reject the wrong business or origin and safely retain pending credentials

#### Scope and acceptance

Business/origin/key checks, harmless rescans and explicit pending replacement share one contract.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: prerequisite / enrollment parser.
- Direct prerequisite task numbers: None.

**Verification Commands:**

```sh
npm test -- apps/field/test
npm run typecheck
npm run build --workspace @estimator/field
```

### Task 2: Commit registration and catalog activation atomically

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** commit registration and catalog activation together
- **Need:** new credentials cannot replace working catalog access before a complete matching update validates. Specifically, commit registration and catalog activation together
- **Value or failure prevented:** an interruption or competing enrollment cannot leave mixed credentials and data

#### Scope and acceptance

Expected revision/CAS and short transaction preserve active data and newly scanned pending credentials.

- Intake forecast: 4 hours (S), not measured time or implementation approval.
- Ownership: after parser / field store owner.
- Direct prerequisite task numbers: 1.

**Verification Commands:**

```sh
npm test -- apps/field/test
npm run typecheck
npm run build --workspace @estimator/field
```

### Task 3: Validate and decrypt complete catalog modules before install

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** validate and decrypt complete catalog modules before installation
- **Need:** new credentials cannot replace working catalog access before a complete matching update validates. Specifically, validate and decrypt complete catalog modules before installation
- **Value or failure prevented:** use compatible data and retain the last good catalog when validation fails

#### Scope and acceptance

Bounded fetch/hash/tag/schema/engine/reference checks occur outside the transaction; cached read works offline.

- Intake forecast: 4 hours (S), not measured time or implementation approval.
- Ownership: after activation API / catalog client.
- Direct prerequisite task numbers: 2.

**Verification Commands:**

```sh
npm test -- apps/field/test
npm run typecheck
npm run build --workspace @estimator/field
```

### Task 4: Read camera and selected-image QR credentials

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** read enrollment through camera and selected QR images
- **Need:** new credentials cannot replace working catalog access before a complete matching update validates. Specifically, read enrollment through camera and selected QR images
- **Value or failure prevented:** register using the device’s available image paths without leaving the camera running

#### Scope and acceptance

Both decode paths use the same parser and release camera resources correctly.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: after parser / QR adapter.
- Direct prerequisite task numbers: 1.

**Verification Commands:**

```sh
npm test -- apps/field/test
npm run typecheck
npm run build --workspace @estimator/field
```

### Task 5: Recover enrollment input after denied camera permission

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** recover enrollment input after camera denial
- **Need:** new credentials cannot replace working catalog access before a complete matching update validates. Specifically, recover enrollment input after camera denial
- **Value or failure prevented:** continue registration through image selection or pasted credentials

#### Scope and acceptance

Paste/image fallback remains usable and all credential inputs feed the already-tested parser.

- Intake forecast: 2 hours (XS), not measured time or implementation approval.
- Ownership: after QR adapter / enrollment controls.
- Direct prerequisite task numbers: 4.

**Verification Commands:**

```sh
npm test -- apps/field/test
npm run typecheck
npm run build --workspace @estimator/field
```

### Task 6: Display catalog design and activation status

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** inspect the active catalog and activation status
- **Need:** new credentials cannot replace working catalog access before a complete matching update validates. Specifically, inspect the active catalog and activation status
- **Value or failure prevented:** know which design data is usable and why an installation remains pending

#### Scope and acceptance

Dated active release and named pending/install errors reflect real service state.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: after activation/client / Updates and Designs.
- Direct prerequisite task numbers: 3.

**Verification Commands:**

```sh
npm test -- apps/field/test
npm run typecheck
npm run build --workspace @estimator/field
```

### Task 7: Expose the read-only field conformance action

#### Story Intent

- **Beneficiary:** construction business owner
- **Capability:** run and export the bounded read-only conformance calculation
- **Need:** new credentials cannot replace working catalog access before a complete matching update validates. Specifically, run and export the bounded read-only conformance calculation
- **Value or failure prevented:** compare the real field engine without creating a synthetic customer quote or job

#### Scope and acceptance

Use the previously shipped conformance contract for actual shared-engine input/result export; no saved JobDraft or production quote is manufactured.

- Intake forecast: 2 hours (XS), not measured time or implementation approval.
- Ownership: after installed catalog / bounded Updates action.
- Direct prerequisite task numbers: 6.

**Verification Commands:**

```sh
npm test -- apps/field/test
npm run typecheck
npm run build --workspace @estimator/field
```

