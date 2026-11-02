# Project Estimator: startup and delivery handoff

Updated November 2, 2026. Metadata migration is complete; application implementation remains unauthorized.

## Current authority and migration result

The owner authorized replacement backlog creation/verification and registered retirement of the old backlog, without application implementation. The authoritative delivery index is [#36](https://github.com/kburson/Project-Estimator/issues/36). It is an administrative index: no parent, children, product integration branch or blocking role. The work is organized as **28 flat root-level sibling epics with 135 XS/S child intake records**, each forecast at 2–4 hours (401 forecast hours; mean 2.97). Forecasts include targeted implementation verification, not epic integration/review, orchestration, release operations, owner waiting or repair effort. Refine oversized work again at pickup; do not lower its estimate to fit the target.

**Verified:** legacy epic #1 and children #2–35 have been superseded through AITM by administrative index #36 as **Replaced / closed not planned**, preserving historical parent links and exact old-to-new scope mapping. This means replaced planning records, not delivered application functionality. The failed-response duplicate #75 is superseded by canonical #76, excluded from the 135-story set.

The earlier instruction to decompose/dispatch #1 using ten serial deliverables is retired. Do not bind #1 or #2–35 for implementation. The original ten-task plan remains unchanged technical source material; the sibling plans and live issue graph define the replacement delivery organization.

#36 is commit-bearing documentation work. The audit-lane attempt is retained as history: AITM intentionally rejects zero-commit completion when an issue has genuine attributed documentation commits. Investigation established that a lineage exemption would weaken that contract; no AITM implementation/package change was made, and proposed functional repair ai-task-manager#2138 was closed not planned. Complete #36 through the existing documentation delivery workflow using an allowlisted branch based on public `origin/trunk`; never publish the private administration/setup ancestry merely to satisfy reachability. The current PR/delivery receipt and closure authority live on [#36](https://github.com/kburson/Project-Estimator/issues/36).

The reproducible archival checker is `python3 docs/epics/verification/36-verify-migration.py`. It retains the immutable expected graph, original source hashes and historical source-plan references while allowing #36's own documentation lifecycle and Completed/Done/Delivered terminal state. It depends on the owner's retained historical Git objects and the intake-era backlog state; it is not ongoing product CI after refinement begins. Workflow configuration, hooks, machine state and raw receipts remain local. The owner reserved #37 for a fresh session; no product implementation is authorized here. Restore temporary local verification settings and release/park the administrative binding before handoff.

## Exact records and proof

- Administrative index: [#36](https://github.com/kburson/Project-Estimator/issues/36).
- Human issue/scope map: [2026-11-01-sibling-delivery-issue-map.md](../epics/2026-11-01-sibling-delivery-issue-map.md).
- Machine-readable issue/scope map: [2026-11-01-sibling-delivery-issue-map.json](../epics/2026-11-01-sibling-delivery-issue-map.json).
- Scope and behavior-sized stories: [2026-11-01-sibling-delivery-backlog.md](../epics/2026-11-01-sibling-delivery-backlog.md).
- Per-epic implementation plans: `docs/superpowers/plans/sibling-delivery/2026-11-01-<epic-key>.md`; each child identifies its exact task section and direct prerequisites.
- Replacement pre-retirement PASS: `.scratch/gh/sibling-migration/verification/20261102T052725Z-replacements-55baed4a/receipt.json`.
- Final post-retirement PASS: `.scratch/gh/sibling-migration/verification/20261102T062306Z-final-9e363ad1/receipt.json`; exact verified snapshot is the adjacent `snapshot.json`, expected scope/graph is `expected.json`, and repository enumeration is `rest-inventory.json`.
- Final durable receipt/evidence artifact: [verified migration evidence](../epics/2026-11-02-36-sibling-migration-verification.md). Raw scratch receipts remain local evidence and are not automatically published.
- Creation journal: `.scratch/gh/sibling-migration/state.json`; source selectors and forecast/dependency manifest: `.scratch/plan/sibling-replan/native-manifest.json`.
- Native dependency readback receipts: `.scratch/gh/sibling-migration/admin-{1,2,3}/receipts.json`. Registered retirement receipts: `.scratch/gh/sibling-migration/retire-{1,2,3}/receipts.json`, plus `.scratch/gh/sibling-migration/legacy-1/supersede.json`.
- Migration metadata was first recorded locally on `codex/epic-1-backlog`. Scoped documentation publication and native closure are governed separately by #36; its live record supplies the accepted PR and delivery receipt. The private setup/administration branch and raw receipts are not publication sources.

Receipt completeness and a final PASS establish migration state only. Application AC/DoD boxes remain unchecked. No application implementation, application dependency installation, build/deployment trigger, customer data entry, physical-device acceptance or feature delivery is established by backlog administration.

## Reviewed technical sources — preserve exact bytes

- [Reviewed specification](../superpowers/specs/2026-11-01-project-estimator-pwa-v1-design.md), SHA-256 `0971e6426aadf888a3652d9fae78707793f4af7f4b221e5b577ef8deca253f2c`.
- [Reviewed original implementation plan](../superpowers/plans/2026-11-01-first-usable-project-estimator.md), SHA-256 `fb0601ece98e4f7af05a26cabcaeccbf5f33dd386e21d00215f0a1bedc2ad6f6`.
- [Claude Opus 5.5/high spec clearance](../reviews/2026-11-01-pwa-v1-claude/review-summary.md), with requests, receipts and follow-up findings beside it.
- [Astra 6/high SAR plan acceptance](../reviews/2026-11-01-first-usable-plan-sar/review-acceptance.md), two rounds/fourteen findings addressed. These are document-review receipts, not passing software evidence.
- [Technical checks](../research/2026-11-01-first-usable-plan-technical-checks.md) and [native capability log](../design/mobile-native-capability-log.md).

The reviewed spec's filename/status wording is preserved for provenance. Implement only its First real-job trial and acceptance cases 1–11. The smaller sibling cuts reorganize delivery without adding deferred features or changing accepted public contracts.

## Source-plan ancestry and publication boundary

The sibling issue records are pinned to local source-plan commit `a1f4a7bcefb82e5499219f33c34aed280c76bceb`. Keep that reference and its files available; a later metadata commit does not silently replace source-plan provenance. The approved administration worktrees were based on this metadata/setup source, not a feature branch. They must not become application implementation branches by accident. All three temporary administrative worktrees were archived through the app after clean-tree/configuration checks and empty timing-queue checks. Needed ignored workflow state is preserved under `.scratch/gh/sibling-migration/admin-state-preservation/`. For a future implementation pickup, follow AITM’s current workspace recovery/relocation guidance rather than treating an archived administrative path as a feature workspace.

Local source availability is not proof the commit or its ancestry is public. Do not blanket-push the administration/setup branch or merge its ancestry merely to publish a map or satisfy a link. Review the exact ancestry and publication diff first, preserve private setup/probe material, and follow the owner's explicit publication scope. If safe publication would require changing source-plan references, handle that through the governed source-binding workflow rather than substituting a new SHA silently. Preserve the main checkout and all unrelated local edits.

## Binding delivery contract

1. Each child works in its own governed worktree and merges **only into its parent epic branch**.
2. Once every child is complete, perform **integrated epic Test and Review** on the assembled epic branch. Individual child verification does not replace this boundary.
3. Deliver the complete passing epic to `trunk` through the governed workflow.
4. That exact `trunk` SHA triggers **both the Cloudflare deployment and the local Mac app-server build**. Retain separate target receipts tied to the same SHA; candidate rehearsal is not a postmerge trigger receipt.
5. The owner then tests **both** targets. Deployment/build success and observed owner acceptance are distinct evidence.

Cross-epic prerequisites consume code already merged to `trunk`; do not stack sibling epics on unmerged branches. Inside an epic, merge the interface producer into the epic branch before dispatching consumers. Claim parallel safety only for disjoint owned files and fixed inputs. Shared schemas, exports, composition, root tooling and lockfiles each have one named owner.

Use **one orchestrator and at most three active workers globally, including reviewers**. Workers do not spawn additional helpers outside that count. Administrative index #36 never becomes a long-lived parent integration gate.

## Next authorized boundary

**No application implementation is currently authorized.** A completed migration does not grant Plan approval, Develop entry, deployment permission or owner-data approval.

After explicit implementation direction, begin with [foundation epic #37](https://github.com/kburson/Project-Estimator/issues/37), [foundation plan](../superpowers/plans/sibling-delivery/2026-11-01-foundation.md), and its first child [#38: Pin the workspace while retaining AITM](https://github.com/kburson/Project-Estimator/issues/38). Confirm their live state, ownership, source binding and native prerequisites before pickup. Use the repository task skill and registered AITM stage workflow; backlog creation is not permission to skip Refine/Plan/approval gates. Preserve the installed AITM dependency and configured project.

Before implementation, inspect current branch/worktree/`origin/trunk` state and protect existing local files. Recover timers and bindings through registered commands; retain queued timing/audit evidence after API failures. Disk journals and previous Explain receipts do not replace fresh live authority.

The foundation must establish the real delivery mechanisms before its first trunk merge. The owner selects/provisions the stable Cloudflare project/HTTPS origin, private credentials and the mechanism for the local Mac build trigger. They remain setup inputs until separately configured and proven. No service installation or publication is authorized by this startup record.

The useful Mac estimate/proposal remains the first major owner-use milestone. Early geometry screens use clearly unsaved inputs. Durable site visits follow the actual shared calculator and preserve the reviewed non-null `JobDraft` input/result ABI. Field enrollment precedes durable field visits. Conformance helpers ship in feature epics; final qualification observes deployed capabilities rather than introducing new feature code.

## Owner-data checkpoints

- Obtain the populated single-recipe worksheet before the real recipe calculator: supports/joints, coverage/gaps, spacing, stock/pack units, fasteners, labor drivers, no-offcut-reuse and excluded options. Example spacings and workbook formulas are not structural approval. Missing decisions stay named and nonselectable.
- Use actual owner-entered prices and explicitly confirmed labor, markup, purchase-tax and customer-tax decisions. Blank is not zero; deliberate zero remains valid.
- Recipe changes require a new retained version and renewed validation. Referenced economic identities and historical price observations remain immutable.
- Synthetic fixtures remain conspicuously test-only/draft, outside production catalog data; they cannot authorize real quotes or publication. Never invent owner validation, rates, tax policy or business data.
- Real iPhone and iPad application tests remain required. Probe observations do not establish production acceptance; Android remains unavailable/untested/deferred.

## Product boundaries to preserve

- One owner's Mac construction business, fencing first. Arbitrary measured runs and explicit endpoint identities include 2–4 ft obstacle returns; labels are not GPS bearings and matching names do not merge posts.
- One deterministic decimal-safe TypeScript calculator; integer sixteenths-inch lengths, decimal-string money, explicit units, pack rounding, allowed pricing arrangements and exact cost allocation. Missing values yield named incompleteness rather than zero.
- Internal segment material/labor costs, person-hours, markup and overrides; customer output exposes allowed segment selling totals and scope without internal rates/hours/costs. Preliminary/Issued quote snapshots are immutable; display old saved results without reopening old encrypted catalogs or recalculating. Repricing is explicit.
- Mac React/Node/SQLite office; static Expo/React Native Web field PWA on Cloudflare. Pin reviewed runtime/dependency versions and validate them; do not silently substitute unrelated current versions.
- Encrypted modular catalogs and one-time QR enrollment with explicit pending/active key rotation behavior; no hosted business database, accounts, per-device revocation service, LAN/DNS/certificate setup, app-store distribution or native implementation.
- Field return uses owner-selected sharing of immutable plaintext UTF-8 JSON packages, followed by reviewed/idempotent Mac import. Catalog credentials never encrypt ordinary job/outbox records. Do not add a general synchronization or independent job-key system.
- Office backup/recovery includes actual current data, attachments and, once present, catalog archives/keys and import evidence. Safe app upgrades and physical-device recovery require observed proof; local save does not imply office backup or receipt.
- Deferred: automated gates/additional recipes, alternatives/revision comparison, drawings/calendar, office-to-mobile job transfer, vendor fetching/OCR, Gmail automation, signatures, printers, native delivery and irrigation. Manual gate allowances do not alter fence geometry or invent support counts.

## Private files and preserved local state

Preserve `Heather-Fence Bid.numbers`, earlier October 31 documents and `probes/`; they are preserved local historical material; some probes are tracked in local setup ancestry, not production authority. Do not delete them, broadly stage them, reset the workspace or copy probe credentials into the application. Ignored raw review logs stay local; preserve committed review collateral.

Never stage or publicly commit customer exports, databases, catalog keys, enrollment QR credentials, backup/recovery files or private probe/setup material. Keep business data outside deploy trees and deploy only the explicit allowlisted artifacts. Scratch administration receipts may contain live issue/configuration details; publish only reviewed evidence selected by the orchestrator.

Update the actual startup record at natural handoffs with verified completed work and the next unfinished boundary. Preserve reviewed source hashes and distinguish document integration, migration completion, code delivery, deployment and owner acceptance.
