# Draft: incremental delivery through sibling epics

**Migration verified complete.** See [final evidence](2026-11-02-36-sibling-migration-verification.md) and [exact issue map](2026-11-01-sibling-delivery-issue-map.md). This strategy records the delivery contract; no implementation is authorized.

November 1, 2026. The owner authorized backlog creation/verification and registered legacy retirement on November 1, 2026. Native implementation-plan approval and application implementation remain separate and ungranted.

## Owner direction

The owner corrected the initial backlog decomposition: stories should average 2–4 hours, with an occasional justified 6-hour story. A Medium ceiling is not a target. The owner wants sibling epics containing genuinely parallel implementation stories, short integration cycles, and demonstrable/testable features reaching `trunk` while other sibling epics remain in development. Nested epics and a large parent integration branch do not meet that goal.

The earlier `1a`/`1b`/`1c` labels denoted slices of reviewed plan tasks. They did not certify parallel safety. The previous 34-story proposal was mostly 6–8 hour stories and encoded an almost entirely serial chain. It must not be used as the new execution strategy.

The reviewed specification remains the product scope authority: first real-job trial, acceptance cases 1–11, one owner-validated recipe, immutable quote history, shared calculator, local Mac office and static PWA. No deferred feature is added. The reviewed plan remains technical source material; its instruction to execute ten large deliverables serially is superseded only when the owner accepts a replacement delivery strategy. Preserve its reviewed bytes/hash.

## Proposed integration model

- Every delivery epic is a root-level sibling on the same board. No new epic is a child of #1 or another epic. Use a common trial label/milestone and native dependencies to express the overall goal.
- Each epic has one narrow, demonstrable result, a build/test boundary, explicit exclusions, and a short path to `trunk`. Most should contain 3–5 small stories; split a cut again when its integration scope becomes long-lived.
- Story titles describe behavior, without plan-number prefixes. Record source-plan references and prerequisites in metadata, not in title suffixes.
- Size each story from its actual behavior, touched surfaces and verification work. Split an 8-hour item into independently testable changes; never just change its Estimate field to 4. A 6-hour exception needs a written reason why a useful smaller boundary was not found.
- Initial WIP proposal: two sibling epics in development, with parallel stories only where their prerequisites and ownership permit. Do not open all epics at once.
- Cross-epic work consumes contracts/code already on `trunk`. Do not base one sibling on another sibling's unmerged branch. Inside an epic, accept its small interface prerequisite before dispatching consumers from that epic head.
- Give each parallel story its own worktree, file ownership, declared input/output contract and verifier. Assign one owner to shared schemas, exports, root scripts/lockfile and composition files. Consumer stories do not edit those shared files concurrently.
- An integration story must be small and explicit. It cannot absorb unfinished domain logic, migrations or tests from its siblings. If integration needs substantial implementation, the earlier cuts were incomplete.
- Keep incomplete product capabilities visibly unavailable. Merge only coherent passing increments, not production stubs, fabricated owner data or a second temporary calculator.

## Confirmed delivery and orchestration contract

The owner confirmed the merge unit and concurrency limit after the first draft:

1. Each child is implemented and verified in its own issue-bound worktree, then delivered to its **parent epic branch** through AITM. Children do not merge directly to `trunk`.
2. When every child is complete and integrated, test the assembled epic and perform its required review against the actual integrated head. Passing child checks does not replace epic integration testing/review.
3. Deliver that accepted epic head to `trunk` through the governed merge path. Sibling epics remain independent; there is no outer epic branch that accumulates them.
4. Every epic merge to `trunk` must trigger **both** a Cloudflare deployment of the field/static application and a build of the local Mac app server from that same `trunk` commit.
5. The owner tests **both** targets after each epic delivery. Record code delivery, target build/deployment success and the owner's observed acceptance separately. A merge or passing pipeline is not owner acceptance.
6. Use **one orchestrator and at most three active worker agents globally**, across all sibling epics and all roles, including reviewers. This is not three workers per epic. The orchestrator owns dispatch, dependency checks, shared-file ownership, integration, stage-level test/review scheduling, trunk delivery and release evidence. Workers do not create helper agents outside that limit.

Other ready sibling epics can continue development while the owner tests a delivered epic. The owner has not specified an additional rule that their postdeployment acceptance must block the next trunk merge; do not invent that gate or infer their approval. Preserve the exact versions tested so feedback can be attributed.

### First-delivery prerequisite: build and deployment triggers

The repository currently has no tracked application/build/deployment workflow; its root package still contains the starter placeholder test and the installed AITM dependency. This is not an already-working pipeline. The foundation backlog must include the smallest real build/deploy wiring needed for the first epic to satisfy the delivery contract.

Before the first epic can be delivered, establish the owner-selected stable production HTTPS origin and Cloudflare project, scoped deployment credentials outside source/static staging, and the actual mechanism that triggers the local Mac server build from a trunk merge. The local mechanism is a setup/design checkpoint, not an assumed installed runner or permission to add a background service. Do not run a deployment or install build automation during this planning task.

The original plan deferred production-origin setup and complete deployment verification until Task 10. The owner's new every-epic delivery requirement moves the necessary setup and app-only static staging safety checks before the **first** epic delivery. Catalog staging/compatibility checks extend that path when private modules are introduced. Preserve the static-only hosting and loopback-only local server boundaries.

Each delivery record identifies: epic and accepted head, resulting trunk SHA, Cloudflare deployment ID/URL/status and source SHA, local build result/artifact and source SHA, a concise feature-specific demo/test script, and the owner's separate results for both targets. Both target artifacts must correspond to the delivered trunk commit. Failed or unavailable builds/deployments are reported as such; they are not a completed two-target handoff.


## Verified replacement scope organization

The [complete sibling backlog and legacy mapping](2026-11-01-sibling-delivery-backlog.md) replaces the earlier illustrative twenty-epic table and six example story tables. It contains **28 flat sibling epics and 135 child intake records**, all forecast at 2–4 hours (mean 2.97). These are scope/verification forecasts, not approved delivery dates or measured effort. Integrated epic Test/Review, release operations, owner testing/waiting and repair work are additional tracked activities.

Three worker passes supplied Mac cuts, field/release cuts and independent sizing/workflow review. The orchestrator corrected bundled four-hour stories, dependency/evidence timing and duplicate implementation boundaries. All replacement issues have been created and their native graph verified; the exact IDs are in the linked issue map.

| Delivery area | Proposed small sibling cuts |
| --- | --- |
| First usable delivery path | Actual office/field shells, pinned contracts and candidate-tested Cloudflare/local-build triggers |
| Early Mac features | Catalog identities, dated prices/settings, bays/posts, material requirements and purchases |
| Calculated Mac work | Shared cost engine, real calculated visit persistence, durable run editing and explicit repricing |
| Customer output | Immutable quote history and strict customer proposals/PDF |
| Office durability | Attachments, consistent backup capture and staged restore |
| Field use | Private catalog preparation, registration/atomic activation, then actual field job creation and retained proposals |
| Field return | Immutable submissions, read-only office review, then transactional acceptance/deduplication |
| Recovery/lifecycle | Real-key/import backup extensions, cold offline launch, safe version changes and field recovery |
| Final qualification | One evidence epic with bounded per-device/workflow stories against an already-deployed application release |

The sibling organization preserves the reviewed `JobDraft` ABI. Durable jobs follow the real calculator rather than manufacturing inputs/results for an earlier capture milestone. Geometry and catalog features can still deliver first. Registration precedes field-job creation so an initial device has a real catalog rather than test-only preloaded records.

Parallelism is real only after a shared interface prerequisite is accepted on that epic branch. The detailed table assigns implementation/helper/UI/composition ownership and join points. Cross-epic consumers wait for `trunk`. The orchestrator can allocate at most three worker slots across those ready lanes, not three per epic.

Independent review identified complete scope homes for trial cases 1–11. Creation fragments still need exact AC/verifier bindings and final sizing for difficult material, crypto, catalog-validation and import-transaction boundaries. The 2.97-hour average alone does not prove those cuts fit; split again or justify a six-hour exception when refinement supplies evidence.

## Migration and AITM constraints

All 34 earlier children (#2–#35) were created before this correction; the last creation command had already been dispatched when the owner steered the task and completed with a partial-success parent-refresh refusal. They are not a parallel-ready approved backlog. Do not dispatch them or simply reduce their estimates.

The owner-authorized metadata migration is complete. AITM created the 28 root sibling epics and 135 children, their exact native dependency graph was read back, and a whole-set PASS was recorded while legacy #1–35 were still OPEN. All34 legacy children were then retired and separately verified Done/Replaced before original epic #1 was retired last through the same registered route. The final PASS and exact map are linked above. No record was deleted or represented as delivered application work.

The historical AITM epic-readiness contract limited a collected child array to32; adding old children33/34 had exposed that limit. The small sibling epics avoid it. Registered `aitm supersede <old> --by36` successfully retired every legacy record, including oversized original epic1, without raw detach, arbitrary state movement or package-cap changes. Index36 truthfully represents the complete old-to-new scope map and has no product branch, child hierarchy or native blocking role.

This strategy records the confirmed delivery contract and verified backlog organization. It does not authorize application implementation, Plan approval, builds, deployment or publication of private setup ancestry.
