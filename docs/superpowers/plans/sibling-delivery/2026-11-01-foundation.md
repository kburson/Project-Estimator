# Deliver the first office and field builds: sibling delivery plan

Owner-authorized backlog creation on November 1, 2026. **Application implementation is not authorized.** This plan supplies source scope/intent for intake; native refinement, implementation planning and approval remain later gates.

## Scope

Launch both empty applications and obtain same-commit Cloudflare deployment and Mac build receipts.

Root-level sibling epic only. Children deliver to this epic branch; all children complete → integrated epic Test/Review → trunk → same-SHA Cloudflare deployment and local Mac build → owner tests both. One orchestrator; at most three workers globally. No nested epic or outer integration branch.

## Technical lineage

Reviewed source Task(s) 1, 4, 7, 10 in `docs/superpowers/plans/2026-11-01-first-usable-project-estimator.md`; trial specification acceptance cases 1–11 only. The reviewed files remain unchanged. Preserve all owner recipe/prices/settings/origin checkpoints and deferred-feature boundaries. Synthetic fixtures remain draft/test-only.

## Prerequisites and ownership

Prerequisite sibling keys: None. Cross-epic dependencies mean completed code on trunk.

After story 1 establishes root package contracts, stories 2, 3 and 4 may run in parallel on shared-contract, office and field files respectively. Story 5 follows 4; story 6 follows 5; story 7 follows 3. Story 8 joins 2, 6 and 7. One integration owner serializes root scripts, lockfile, shared exports and release composition; shell or release consumers request those changes rather than editing the same files concurrently. At most three workers are active globally. Candidate verification precedes merge; actual trunk receipts and owner tests of both targets follow merge.

A shared schema/export/store migration/HTTP route/App composition/lockfile has one designated owner. Consumers use the accepted epic-head contract and disjoint files. Partial renderer preparation is not a complete parallel-ready story when its producer is still missing. No gate/Full-Auto preference is changed.

## Story Intent

- **Beneficiary:** construction business owner and release operator
- **Capability:** deliver the first office and field builds
- **Need:** there is no existing application build and two-target delivery workflow
- **Value or failure prevented:** The owner can open both applications and identify the same delivered release on the Mac and stable field origin without exposing private business files

## Implementation Tasks

### Task 1: Pin the workspace while retaining AITM

#### Story Intent

- **Beneficiary:** construction business owner and release operator
- **Capability:** pin the workspace while retaining AITM
- **Need:** there is no existing application build and two-target delivery workflow. Specifically, The existing starter workspace does not yet provide pinned application package boundaries or usable build and verification commands
- **Value or failure prevented:** Office and field changes can be reproduced without losing the installed issue workflow or including private probe material

#### Scope and acceptance

Runtime, package boundaries and real consumer build commands are pinned; probes and private outputs are excluded.

- Intake forecast: 2 hours (XS), not measured time or implementation approval.
- Ownership: prerequisite / root files.
- Direct prerequisite task numbers: None.

**Verification Commands:**

```sh
npm run typecheck
npm test
npm run build
```

### Task 2: Validate exact run and measured-length inputs

#### Story Intent

- **Beneficiary:** construction business owner and release operator
- **Capability:** validate exact run and measured-length inputs
- **Need:** there is no existing application build and two-target delivery workflow. Specifically, Fence measurements and connected runs require exact bounded lengths and independent identities before later geometry can use them
- **Value or failure prevented:** Invalid measurements are rejected and distinct runs or endpoints cannot silently merge or lose precision

#### Scope and acceptance

Exact sixteenths, bounds and independent endpoint/run identities validate without construction defaults.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: after workspace / shared contracts.
- Direct prerequisite task numbers: 1.

**Verification Commands:**

```sh
npm run typecheck
npm test
npm run build
```

### Task 3: Build and launch the loopback office shell

#### Story Intent

- **Beneficiary:** construction business owner and release operator
- **Capability:** build and launch the loopback office shell
- **Need:** there is no existing application build and two-target delivery workflow. Specifically, The owner needs a real local office application entry point that starts from its production build
- **Value or failure prevented:** The Mac can open the office shell while write requests remain restricted to the intended loopback application origin

#### Scope and acceptance

Actual production office build starts locally; guarded loopback API rejects foreign-origin writes.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: after workspace / office.
- Direct prerequisite task numbers: 1.

**Verification Commands:**

```sh
npm run typecheck
npm test
npm run build
```

### Task 4: Export the static field application shell

#### Story Intent

- **Beneficiary:** construction business owner and release operator
- **Capability:** export the static field application shell
- **Need:** there is no existing application build and two-target delivery workflow. Specifically, The field device needs an actual static application export that can consume the shared package
- **Value or failure prevented:** The owner can open a working field shell from generated assets before later field capabilities are added

#### Scope and acceptance

Actual Expo export resolves the shared package and renders empty navigation.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: after workspace / field.
- Direct prerequisite task numbers: 1.

**Verification Commands:**

```sh
npm run typecheck
npm test
npm run build
```

### Task 5: Stage only public application assets

#### Story Intent

- **Beneficiary:** construction business owner and release operator
- **Capability:** stage only public application assets
- **Need:** there is no existing application build and two-target delivery workflow. Specifically, Public application delivery must distinguish generated app assets from local records credentials and preserved probe files
- **Value or failure prevented:** Only verified allowlisted application assets enter the deployment stage and private business material remains local

#### Scope and acceptance

Allowlisted app assets verify before staging; DBs, credentials, customer/probe/recovery material are excluded.

- Intake forecast: 2 hours (XS), not measured time or implementation approval.
- Ownership: after export contract / release files.
- Direct prerequisite task numbers: 4.

**Verification Commands:**

```sh
npm run typecheck
npm test
npm run build
```

### Task 6: Configure trunk-triggered Cloudflare delivery

#### Story Intent

- **Beneficiary:** construction business owner and release operator
- **Capability:** configure trunk-triggered Cloudflare delivery
- **Need:** there is no existing application build and two-target delivery workflow. Specifically, Each delivered increment needs a repeatable path to the owner-selected stable field origin
- **Value or failure prevented:** The candidate field build can be checked at a preview and the first trunk delivery can produce an attributable Cloudflare deployment receipt

#### Scope and acceptance

Validate the owner-selected project/credential scope and candidate-preview deployment. The actual exact-trunk deployment receipt is postmerge evidence.

- Intake forecast: 3 hours (S), not measured time or implementation approval.
- Ownership: after staging / cloud release wiring.
- Direct prerequisite task numbers: 5.

**Verification Commands:**

```sh
npm run typecheck
npm test
npm run build
```

### Task 7: Configure trunk-triggered local server builds

#### Story Intent

- **Beneficiary:** construction business owner and release operator
- **Capability:** configure trunk-triggered local server builds
- **Need:** there is no existing application build and two-target delivery workflow. Specifically, Each delivered increment also needs a reproducible Mac server build from the same source commit
- **Value or failure prevented:** The selected local build mechanism can be checked without altering business data and can identify the corresponding Mac build after trunk delivery

#### Scope and acceptance

Validate the selected mechanism using a controlled candidate build/start smoke without altering business data. First actual trunk-trigger execution is checked after merge.

- Intake forecast: 4 hours (S), not measured time or implementation approval.
- Ownership: after office build / local release wiring.
- Direct prerequisite task numbers: 3.

**Verification Commands:**

```sh
npm run typecheck
npm test
npm run build
```

### Task 8: Rehearse candidate delivery before the first trunk merge

#### Story Intent

- **Beneficiary:** construction business owner and release operator
- **Capability:** rehearse candidate delivery before the first trunk merge
- **Need:** there is no existing application build and two-target delivery workflow. Specifically, The owner needs evidence that the candidate office and field artifacts and their release triggers agree before the first epic reaches trunk
- **Value or failure prevented:** Both candidate applications can be opened and checked together with prepared postmerge checks for the actual trunk deployment and Mac build receipts

#### Scope and acceptance

Build/smoke the exact candidate office artifact and field preview, validate trigger configuration, and prepare the postmerge receipt checks. Actual trunk receipts follow the epic merge.

- Intake forecast: 2 hours (XS), not measured time or implementation approval.
- Ownership: after both triggers / orchestrator integration.
- Direct prerequisite task numbers: 2, 6, 7.

**Verification Commands:**

```sh
npm run typecheck
npm test
npm run build
```

