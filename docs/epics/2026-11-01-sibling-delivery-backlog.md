# Verified sibling delivery backlog

November 1, 2026. Prepared by one orchestrator with three read-only workers. The delivery contract is confirmed; the owner has approved creation/verification of these replacement scope cuts and registered retirement of the legacy set. Migration is verified complete: see [the final evidence](2026-11-02-36-sibling-migration-verification.md) and [exact issue map](2026-11-01-sibling-delivery-issue-map.md). No application work is delivered by this metadata migration. No implementation is authorized.

**28 flat sibling epics; 135 behavior-sized stories; 2.97 hours average; every forecast is 2–4 hours.** These forecasts include targeted verification, exclude unknown owner waiting time and do not promise defect-free qualification. No six-hour exception is currently proposed; difficult four-hour cuts still need evidence-based refinement. The arithmetic average does not validate an individual estimate. A larger pickup must be split again, not relabeled.

## Binding delivery rules

- Children merge only to their parent epic branch. Once every child is complete, test/review the assembled epic, then deliver that epic to `trunk` through AITM.
- Every epic trunk merge triggers the Cloudflare deployment and local Mac server build from that same SHA; the owner tests both afterward. The first epic establishes those real mechanisms. They do not exist yet.
- One orchestrator controls at most three active workers globally, including reviewers, across all epics. Workers do not spawn uncounted helpers. One owner/worktree per child; shared contracts, exports, composition and lockfiles have a named single owner.
- Cross-epic prerequisites mean merged code on `trunk`. Within an epic, accept an interface prerequisite on its epic branch before consumer fan-out. A story may advertise a parallel lane only when it owns disjoint files and consumes that fixed interface.
- Source references below refer to the unchanged reviewed ten-task implementation plan. Public interfaces and trial scope remain authoritative; these smaller cuts supersede its serial delivery organization under the owner-authorized, verified sibling migration.

## Persistence and early demonstrations

The reviewed `JobDraft` requires real `EstimateInput` and `EstimateResult`. This proposal **does not introduce a nullable result or a new capture ABI**. Durable calculated site visits follow the real shared calculator. Earlier geometry screens use clearly unsaved inputs and show actual quantities; catalog/history releases are independently useful. They do not claim to save a customer quote. Registration and catalog installation ship before durable field visits. Field visits can therefore create and reopen actual calculated snapshots immediately; fixtures are not substituted for a first live workflow. No synthetic owner validation or fabricated result substitutes for this dependency.

## Release prerequisites and ownership

The owner selects/provisions the stable Cloudflare project/origin and private credentials, plus the mechanism for triggering the local Mac build. These are explicit foundation setup checkpoints, not permission to install a service or deploy now. The one-time foundation has eight small stories because the first trunk merge must already exercise both targets; later implementation epics usually contain three to five. The final qualification epic deliberately contains more small observation stories: it accumulates evidence, not unmerged feature code, against an already-deployed release. Shared release/root files are serialized under the foundation integration owner. Pipeline success, code delivery and owner acceptance are distinct receipts.

## Sibling index

| Key (metadata only) | Epic title | Stories / hours | Prerequisites on trunk | Trunk demonstration |
| --- | --- | --- | --- | --- |
| foundation | Deliver the first office and field builds | 8 / 22 h | None | Launch both empty applications and obtain same-commit Cloudflare deployment and Mac build receipts. |
| catalog | Maintain vendor and component identities | 5 / 13 h | foundation | Enter vendors/components/offers while preserving their economic meaning. |
| prices | Keep dated prices and deliberate business settings | 4 / 13 h | catalog | Append/correct observations and choose explicit pricing/settings without rewriting history. |
| bays | Explain bays and shared posts | 4 / 11 h | foundation | Inspect real recipe/run bays and post identities without claiming a saved or priced quote. |
| requirements | Explain material cuts and stock requirements | 5 / 16 h | bays, catalog | Inspect short-return material requirements, attachments and conservative unused stock. |
| purchases | Explain purchased packs and eligible prices | 5 / 16 h | requirements, prices | Inspect rounded packs, eligible tiers, tax, provenance and exact allocations. |
| costs | Calculate complete segment costs | 6 / 17 h | purchases | Use the one shared engine to produce auditable costs/selling/tax or named incompleteness. |
| visits | Save and reopen calculated site visits | 6 / 15 h | costs | Save real calculated job snapshots with customer identity and revision protection. |
| run-editing | Edit and durably save measured runs | 3 / 9 h | visits | Edit connected runs without losing newer input or misreporting failed saves. |
| estimates | Calculate and explicitly reprice saved estimates | 5 / 13 h | run-editing, costs | Use actual shared results and review changes before repricing durable work. |
| quotes | Preserve presented quotes | 5 / 16 h | estimates | Persist immutable Preliminary/Issued snapshots and reopen history independently. |
| proposals | Export customer-safe proposals | 4 / 13 h | quotes | View and export readable frozen proposals without internal costing fields. |
| attachments | Retain job and receipt evidence | 3 / 10 h | visits, catalog | Upload and reopen immutable local evidence with original metadata. |
| backup-capture | Create verified office backups | 3 / 10 h | attachments, prices | Capture a consistent verified copy of current office data and files. |
| backup-restore | Restore office work safely | 3 / 10 h | backup-capture | Restore into an isolated directory without losing identities or overwriting on failure. |
| catalog-release | Prepare private field catalogs | 5 / 17 h | proposals, backup-restore | Stage verified encrypted modules and explicitly produce enrollment credentials. |
| field-visits | Save field site visits | 6 / 18 h | registration, proposals, run-editing | Enter and reopen field work with real snapshots and truthful save failures. |
| registration | Register a device and install its first catalog | 7 / 21 h | catalog-release, foundation | Enroll once and atomically install/view validated catalog data, without requiring an existing job. |
| catalog-refresh | Refresh catalogs and rotate keys safely | 4 / 13 h | registration | Install changed resources and preserve old access through failed or early rotation. |
| field-quotes | Present retained field quotes | 4 / 11 h | field-visits, registration, proposals | Freeze Preliminary snapshots and export the shared customer-safe PDF. |
| field-returns | Return immutable field submissions | 4 / 11 h | field-quotes | Prepare durable packages and share/download without claiming office receipt. |
| import-review | Review returned field work in the office | 4 / 13 h | field-returns, visits | Inspect source identities/conflicts without modifying business records. |
| import-accept | Accept reviewed field submissions exactly once | 4 / 13 h | import-review | Accept transactionally, preserve source quotes, and replay without duplication. |
| office-recovery | Recover catalog and imported office evidence | 3 / 9 h | backup-restore, catalog-release, import-accept | Extend existing backup proof to real keys, archives, import links and delayed replay. |
| offline-shell | Launch the field application without network | 4 / 12 h | registration, field-quotes, field-returns | Cold-open the production shell and existing work without fetching catalog requests through the worker. |
| app-upgrades | Upgrade the field app without losing work | 4 / 13 h | offline-shell, catalog-refresh, field-returns | Activate a distinct version only at a saved compatible single-window boundary. |
| field-recovery | Recover field work after storage loss | 4 / 12 h | field-returns | Export and restore reviewed local work without credential or identity loss. |
| qualification | Qualify the complete owner trial | 13 / 34 h | office-recovery, app-upgrades, field-recovery, catalog-refresh | Record independent Mac/iPhone/iPad evidence for all eleven cases against one identified deployed application release. |

The summed forecasts cover story implementation and targeted verification, not a delivery-date promise. Integrated epic Test/Review, orchestration, per-epic release operations, owner observation/waiting and repair work must be tracked separately; smaller tickets do not make that effort disappear.

The keys are only dependency references in this document. GitHub issue titles use the human title without numeric or letter prefixes.

## Complete story cuts

### Deliver the first office and field builds

Reviewed source: Task(s) 1, 4, 7, 10. Prerequisites: None.

| Story title | Hours | Ownership / dependency boundary | Behavior and verification |
| --- | ---: | --- | --- |
| Pin the workspace while retaining AITM | 2 | prerequisite / root files | Runtime, package boundaries and real consumer build commands are pinned; probes and private outputs are excluded. |
| Validate exact run and measured-length inputs | 3 | after workspace / shared contracts | Exact sixteenths, bounds and independent endpoint/run identities validate without construction defaults. |
| Build and launch the loopback office shell | 3 | after workspace / office | Actual production office build starts locally; guarded loopback API rejects foreign-origin writes. |
| Export the static field application shell | 3 | after workspace / field | Actual Expo export resolves the shared package and renders empty navigation. |
| Stage only public application assets | 2 | after export contract / release files | Allowlisted app assets verify before staging; DBs, credentials, customer/probe/recovery material are excluded. |
| Configure trunk-triggered Cloudflare delivery | 3 | after staging / cloud release wiring | Validate the owner-selected project/credential scope and candidate-preview deployment. The actual exact-trunk deployment receipt is postmerge evidence. |
| Configure trunk-triggered local server builds | 4 | after office build / local release wiring | Validate the selected mechanism using a controlled candidate build/start smoke without altering business data. First actual trunk-trigger execution is checked after merge. |
| Rehearse candidate delivery before the first trunk merge | 2 | after both triggers / orchestrator integration | Build/smoke the exact candidate office artifact and field preview, validate trigger configuration, and prepare the postmerge receipt checks. Actual trunk receipts follow the epic merge. |

### Maintain vendor and component identities

Reviewed source: Task(s) 2, 4. Prerequisites: foundation.

| Story title | Hours | Ownership / dependency boundary | Behavior and verification |
| --- | ---: | --- | --- |
| Store validated catalog identities | 3 | prerequisite / store and schema | Vendor, component and offer identities round-trip and invalid references fail transactionally. |
| Edit vendors and component specifications | 3 | after store / vendor-component UI | Contacts, branches, dimensions, stock/unit/pack fields persist through reopen. |
| Edit explicitly identified vendor offers | 3 | after store / offer UI | SKU, URL, branch, currency and purchase context validate and persist. |
| Reject changes to referenced economic context | 2 | after store / immutable repository guards | Referenced pack/spec/unit identities cannot be changed or deleted. |
| Create replacement identities for economic edits | 2 | after guard and forms / integration | Explicit new-identity action preserves original references and displays retained context. |

### Keep dated prices and deliberate business settings

Reviewed source: Task(s) 2, 4. Prerequisites: catalog.

| Story title | Hours | Ownership / dependency boundary | Behavior and verification |
| --- | ---: | --- | --- |
| Append and correct immutable price observations | 3 | prerequisite / history repository | Same ID/body retries are harmless; conflicting body rejects; unknown dates remain unknown; corrections retain originals. |
| Enter known prices and permitted arrangements | 4 | after observation contract / price UI | Retail/bulk/contractor terms and allowed stacking are explicit; missing price stays missing. |
| Require explicit business labor markup and tax decisions | 3 | after settings contract / Setup UI | Blank and deliberate zero differ; proposal identity/email and pricing settings persist. |
| Choose defaults and inspect dated corrections | 3 | after forms / catalog composition | Selected offer/observation is explicit, history remains available and selection saves do not duplicate observations. |

### Explain bays and shared posts

Reviewed source: Task(s) 1. Prerequisites: foundation.

| Story title | Hours | Ownership / dependency boundary | Behavior and verification |
| --- | ---: | --- | --- |
| Record the owner single-recipe decision | 2 | owner checkpoint / documentation | Record actual worksheet evidence or named missing fields; owner response/waiting time is not fabricated. |
| Validate versioned recipe rules | 3 | after owner checkpoint / recipe contract | Positive dimensions and rule references validate; synthetic fixture stays draft/test-only. |
| Calculate exact bays and unique post identities | 3 | after recipe contract / geometry | Reviewed spacing and connected-return cases pass; labels do not merge identities and self-loops reject. |
| Inspect geometry and named invalid inputs | 3 | render after contract; integrate after engine / UI | Real shared output explains bays/posts and errors; inputs are explicitly unsaved until durable-job features land. |

### Explain material cuts and stock requirements

Reviewed source: Task(s) 1. Prerequisites: bays, catalog.

| Story title | Hours | Ownership / dependency boundary | Behavior and verification |
| --- | ---: | --- | --- |
| Retain owner-validated recipe versions | 3 | recipe schema and catalog store on trunk / recipe repository | Persist/select the actual owner-validated recipe; a changed referenced (id,version) body is refused, a new version requires renewed owner validation, and old identities remain available. |
| Derive installed material requirements | 4 | prerequisite / requirement contract | Post/bay/run-coverage rules preserve per-run rounding and allocate shared supports once. |
| Retain cuts and conservative stock use | 3 | after requirement contract / cut helper | Oversized cuts reject; no-reuse stock, waste and unused lengths reconcile. |
| Count fasteners from installed pieces | 3 | after requirement contract / attachment helper | Attachments derive from installed rather than spare pieces; invalid references/units are named. |
| Explain requirements and unused stock | 3 | after helpers / facade and UI | Actual geometry composition and screen explain quantities/cuts/allowances with named incompleteness. |

### Explain purchased packs and eligible prices

Reviewed source: Task(s) 2. Prerequisites: requirements, prices.

| Story title | Hours | Ownership / dependency boundary | Behavior and verification |
| --- | ---: | --- | --- |
| Pool requirements before package rounding | 3 | prerequisite / purchase pool contract | Selected/default offers only; whole-pack rounding occurs once and unit/rental mismatches reject. |
| Select only permitted pricing arrangements | 4 | after pool contract / tier helper | Purchased-unit thresholds, explicit noncheapest choices, non-stacking and deterministic ties are correct. |
| Extend tax-inclusive costs and allocate cents | 4 | after pool contract / cost helper | Fractional unit precision and tax basis remain exact; allocations conserve every cent. |
| Compose purchase provenance and named failures | 2 | after helpers / pricing facade | Chosen observation/arrangement is retained; absent prices/tax/units never become fabricated zero. |
| Inspect pack spares and selected-price provenance | 3 | after facade / office display | UI explains purchases, unused stock, allocation and actual selection failures. |

### Calculate complete segment costs

Reviewed source: Task(s) 3. Prerequisites: purchases.

| Story title | Hours | Ownership / dependency boundary | Behavior and verification |
| --- | ---: | --- | --- |
| Define estimate inputs and production readiness | 2 | prerequisite / estimate schemas | Test-only/unvalidated recipes and missing/unconfirmed settings cannot authorize production quotes. |
| Attribute materials and person-hour costs once | 3 | after schemas / automatic cost helper | Acquisition effort is separate and purchase costs are charged to consuming segments exactly once. |
| Cost manual work without inventing geometry or hours | 3 | after schemas / allowance helper | Tax/category and gate confirmations are explicit; missing automatic inputs remain missing. |
| Apply segment selling rules and customer tax | 3 | after schemas / price helper | Override/markup precedence, clear/zero, rounded-selling tax and below-cost information are correct. |
| Compose complete and incomplete estimate results | 3 | after helpers / sole facade owner | Actual calculator totals reconcile, preserves named issues and emits the reviewed calculator version. |
| Expose a read-only Mac conformance calculation | 3 | after shared engine / bounded conformance action | Show/export a test-only fixture through the real engine; cannot save a job, freeze a quote or publish a catalog. This helper ships before device qualification. |

### Save and reopen calculated site visits

Reviewed source: Task(s) 4. Prerequisites: costs.

| Story title | Hours | Ownership / dependency boundary | Behavior and verification |
| --- | ---: | --- | --- |
| Define validated customer and calculated-job persistence | 2 | prerequisite / schema and API | Use the reviewed JobDraft with real EstimateInput/EstimateResult; no capture-only nullable ABI or fabricated result. |
| Persist customer identities and contact history | 2 | after contract / customer store | Validated UUIDs, original dates and customer bodies survive restart. |
| Persist and reopen calculated job snapshots | 3 | after contract / job store | Saved inputs/results and stable IDs survive restart; read/reopen does not invoke calculation. |
| Reject competing stale job revisions | 2 | after job store / revision guard | Compare-and-swap failures preserve the last durable record under meaningful competing writes. |
| Edit customer and jobsite information | 3 | after store API / customer-job controls | Contacts/referral/history/address/requirements persist through actual endpoints and reopen correctly. |
| Calculate and save the first real job | 3 | after store and customer form / creation adapter | Use actual selected recipe/pricing and the existing shared engine to create a validated JobDraft with stable identities; save then reopen it without recalculation. |

### Edit and durably save measured runs

Reviewed source: Task(s) 4. Prerequisites: visits.

| Story title | Hours | Ownership / dependency boundary | Behavior and verification |
| --- | ---: | --- | --- |
| Edit measured runs and explicit connections | 3 | fixed Run contract / run controls | Repeated labels and endpoint joins preserve identities; exact units/bounds validate. |
| Serialize writes and preserve the latest edit generation | 3 | fixed save API / save controller | An older response cannot overwrite newer input or falsely acknowledge it as Saved. |
| Expose save retry and safe navigation | 3 | after controller and controls / composition | Rejected latest save remains Unsaved; Retry and navigation flush preserve the prior durable version. |

### Calculate and explicitly reprice saved estimates

Reviewed source: Task(s) 3, 4. Prerequisites: run-editing, costs.

| Story title | Hours | Ownership / dependency boundary | Behavior and verification |
| --- | ---: | --- | --- |
| Edit explicit manual allowances | 3 | fixed manual contract / allowance controls | Quantity/category/source/tax/gate confirmations round-trip without invented hours or automatic geometry changes. |
| Edit and clear segment selling adjustments | 2 | fixed adjustment contract / selling controls | Override/markup precedence is visible and clearing restores the defined fallback. |
| Track canonical calculation freshness | 2 | canonical serializer / freshness service | Pending input/result mismatch is visibly stale and cannot be presented. |
| Display internal estimate explanations | 3 | fixed result schema / Estimate view | Known quantities/provenance/person-hours/cost/selling/tax display without labeling incomplete results valid. |
| Review and accept explicit repricing changes | 3 | after controls/view; reuse visits calculation adapter / composition | Before/after purchase/tier/selling totals are visible; accepted reprice preserves prior quote snapshots. |

### Preserve presented quotes

Reviewed source: Task(s) 5. Prerequisites: estimates.

| Story title | Hours | Ownership / dependency boundary | Behavior and verification |
| --- | ---: | --- | --- |
| Define quote content and stable fingerprints | 3 | prerequisite / quote schemas | Status/customer/input are included; generated identity/time and draft revision are excluded. |
| Persist immutable snapshots exactly once | 3 | after schema / quote repository | Unique fingerprints and transactional retries preserve one immutable stored result. |
| Freeze only current complete production calculations | 4 | after schema / portable freeze service | Stale/incomplete/old-engine/test-only production inputs reject; field Issued rejects. |
| Present a durably saved quote snapshot | 3 | after repository and freeze / office composition | Persist before display; failure opens nothing; repeated action reuses ID; status change creates new snapshot. |
| Reopen quote history without changing original bytes | 3 | after presentation / history controls | Later customer/catalog/draft edits cannot alter historical status, totals or contents. |

### Export customer-safe proposals

Reviewed source: Task(s) 5. Prerequisites: quotes.

| Story title | Hours | Ownership / dependency boundary | Behavior and verification |
| --- | ---: | --- | --- |
| Project frozen quotes into the strict customer model | 3 | prerequisite / ProposalModel | Exact allowlist includes reviewed manual descriptions and excludes internal rates/hours/cost/markup. |
| Render wrapped and paginated proposal PDFs | 4 | after model / portable PDF renderer | Bundled fonts, long text, page breaks, repeated status/ID and totals work without network fonts. |
| Display proposals from retained customer models | 3 | after model / customer view | Validated customer-only data and readable segment labels render without internal-object access. |
| Export and inspect frozen proposal files | 3 | after renderer and view / export integration | Unsupported characters name the field and retain the snapshot; actual short/multipage output is visually checked. |

### Retain job and receipt evidence

Reviewed source: Task(s) 4. Prerequisites: visits, catalog.

| Story title | Hours | Ownership / dependency boundary | Behavior and verification |
| --- | ---: | --- | --- |
| Store verified immutable attachment files | 4 | prerequisite / attachment store | Hash/name/date/size, 20MiB limit, safe paths and write-before-reference ordering are enforced. |
| Upload and download evidence through bounded routes | 3 | after store / attachment HTTP | Exact binary content type and owner identity are checked without path or secret leaks. |
| Attach and reopen owner-selected evidence | 3 | after routes / attachment controls | Original metadata and bytes reopen; failure never reports success; no automatic CDN/field inclusion. |

### Create verified office backups

Reviewed source: Task(s) 10. Prerequisites: attachments, prices.

| Story title | Hours | Ownership / dependency boundary | Behavior and verification |
| --- | ---: | --- | --- |
| Define the complete current backup inventory | 3 | prerequisite / backup contract | DB/settings/attachments and existing optional archive/key roots are covered; unsafe/missing required artifacts reject. |
| Capture a consistent database and file backup | 4 | after contract / capture helper | Brief write lock and pinned SQLite backup yield verified lengths/hashes before success. |
| Choose destinations and report verified backup status | 3 | controls after contract; integrate after capture / Backup UI | Source remains intact on failure; private-key inclusion is explained when keys exist. |

### Restore office work safely

Reviewed source: Task(s) 10. Prerequisites: backup-capture.

| Story title | Hours | Ownership / dependency boundary | Behavior and verification |
| --- | ---: | --- | --- |
| Validate every backup artifact before restore | 3 | prerequisite / validation helper | Hash/size/path/traversal/symlink failures leave the destination untouched. |
| Restore through staging and preserve the old directory | 4 | after validator / restore service | Stopped-service staging, SQLite checks and final swap preserve the pre-restore directory. |
| Prove identity and evidence preservation after restore | 3 | fixture after validator; prove after restore / recovery evidence | Compare current records/settings/observations/attachments in a real isolated restored store. |

### Prepare private field catalogs

Reviewed source: Task(s) 6. Prerequisites: proposals, backup-restore.

| Story title | Hours | Ownership / dependency boundary | Behavior and verification |
| --- | ---: | --- | --- |
| Encrypt independently versioned catalog modules | 4 | prerequisite / portable release contract | Fresh IVs/AAD, validated module references, tamper checks and unchanged ciphertext reuse work. |
| Preserve published module and release identities | 3 | after release contract / archive helper | Changed content cannot reuse immutable identities; local archives remain available. |
| Stage only verified public release artifacts | 4 | after release contract / file helper | Extend the foundation stager/verifier with validated selected ciphertext and current-manifest installation; no second deployment implementation or private-file copying. |
| Keep credentials local and generate enrollment explicitly | 3 | after release contract / key and QR adapter | Local key/QR/copy paths share one contract; actual generated keys and archives are captured/restored by the already-shipped backup adapter before this epic completes. |
| Preview the release and selected current-pack removal | 3 | after helpers / Publishing composition | Production readiness is enforced and removed paths are shown without claiming revocation of old copies. |

### Save field site visits

Reviewed source: Task(s) 7. Prerequisites: registration, proposals, run-editing.

| Story title | Hours | Ownership / dependency boundary | Behavior and verification |
| --- | ---: | --- | --- |
| Persist real field draft snapshots independently of keys | 3 | prerequisite / field store | Extend the existing registered field store with real JobDraft save/read APIs; preserve enrollment/catalog tables and all existing data. |
| Edit field customer job and run inputs | 4 | after store contract / touch controls | Stable IDs, explicit endpoint joins and measured input validation match the Mac. |
| Calculate enrolled field work with exact Mac parity | 3 | after controls and installed catalog / field calculation adapter | Actual shared input/result matches the Mac; missing/unvalidated catalog cannot produce a valid quote. |
| Preserve newer field edits in the write queue | 3 | after store contract / save algorithm | Generation-aware serialized writes cannot overwrite newer input or acknowledge it incorrectly. |
| Report field save failure and flush before navigation | 3 | after queue / UI integration | Quota/error/retry/flush paths preserve the previous durable version and truthful status. |
| Reopen field visits and report actual storage persistence | 2 | after controls and save / navigation | Saved work reopens without keys; persistence requests report actual results, not backup guarantees. |

### Register a device and install its first catalog

Reviewed source: Task(s) 7, 8. Prerequisites: catalog-release, foundation.

| Story title | Hours | Ownership / dependency boundary | Behavior and verification |
| --- | ---: | --- | --- |
| Validate enrollment without replacing active registration | 3 | prerequisite / enrollment parser | Business/origin/key checks, harmless rescans and explicit pending replacement share one contract. |
| Commit registration and catalog activation atomically | 4 | after parser / field store owner | Expected revision/CAS and short transaction preserve active data and newly scanned pending credentials. |
| Validate and decrypt complete catalog modules before install | 4 | after activation API / catalog client | Bounded fetch/hash/tag/schema/engine/reference checks occur outside the transaction; cached read works offline. |
| Read camera and selected-image QR credentials | 3 | after parser / QR adapter | Both decode paths use the same parser and release camera resources correctly. |
| Recover enrollment input after denied camera permission | 2 | after QR adapter / enrollment controls | Paste/image fallback remains usable and all credential inputs feed the already-tested parser. |
| Display catalog design and activation status | 3 | after activation/client / Updates and Designs | Dated active release and named pending/install errors reflect real service state. |
| Expose the read-only field conformance action | 2 | after installed catalog / bounded Updates action | Use the previously shipped conformance contract for actual shared-engine input/result export; no saved JobDraft or production quote is manufactured. |

### Refresh catalogs and rotate keys safely

Reviewed source: Task(s) 8. Prerequisites: registration.

| Story title | Hours | Ownership / dependency boundary | Behavior and verification |
| --- | ---: | --- | --- |
| Reuse unchanged modules and retain active data on failure | 3 | fixed refresh contract / fetch helper | Price-only update skips design; corrupt/offline/incompatible responses preserve active state. |
| Promote a pending key only with a valid matching release | 4 | fixed activation API / rotation helper | Early QR, unknown key, interrupted install and stale CAS retain old work; successful retry rotates atomically. |
| Schedule single-flight foreground catalog checks | 3 | fixed refresh service / lifecycle helper | Launch/visibility/manual/visible interval checks do not race or promise closed-app background updates. |
| Explain refresh and registration status accurately | 3 | after helpers / Updates composition | App/key/retry/offline distinctions and attempted/successful timestamps remain truthful. |

### Present retained field quotes

Reviewed source: Task(s) 7. Prerequisites: field-visits, registration, proposals.

| Story title | Hours | Ownership / dependency boundary | Behavior and verification |
| --- | ---: | --- | --- |
| Enter field allowances and selling adjustments | 3 | fixed shared calculator / internal controls | Manual gate/tax/override/clear behavior matches the Mac and does not invent hours or completeness. |
| Freeze durable Preliminary field snapshots | 3 | fixed freeze API / quote adapter | Stale/incomplete inputs reject and unique immutable snapshots read independently of keys/catalog. |
| Export the shared customer-safe field PDF | 3 | fixed ProposalModel / files-PDF adapter | Shared renderer uses no network fonts and exports no internal fields. |
| Present retained quotes after explicit repricing | 2 | after adapters and controls / integration | Saved status/totals remain unchanged after draft repricing and key/catalog removal. |

### Return immutable field submissions

Reviewed source: Task(s) 9. Prerequisites: field-quotes.

| Story title | Hours | Ownership / dependency boundary | Behavior and verification |
| --- | ---: | --- | --- |
| Build strict self-contained field packages | 3 | prerequisite / transport contract | Bounded canonical checksums and references validate; content identity excludes envelope time/ID. |
| Persist immutable outbox records before sharing | 3 | after package contract / outbox store | Same content reuses bytes; changed content creates lineage; failed save offers no share. |
| Share JSON or download it truthfully | 3 | after package contract / sharing adapter | User-selected sharing, cancellation, fallback and handoff states are distinct. |
| Retry saved submissions and confirm receipt explicitly | 2 | after outbox and adapter / Outbox UI | Resends are byte-identical and only owner confirmation sets office-confirmed. |

### Review returned field work in the office

Reviewed source: Task(s) 9. Prerequisites: field-returns, visits.

| Story title | Hours | Ownership / dependency boundary | Behavior and verification |
| --- | ---: | --- | --- |
| Validate received attachments before review | 3 | prerequisite / receive boundary | Wrong business/schema/size/hash/references reject; instruction-like notes are inert text. |
| Read existing source mappings without name-based merging | 3 | after context contract / mapping reader | Business/device/entity/source identity drives suggestions, never implicit replacement. |
| Explain identity and base-revision conflicts | 4 | fixed context contract / portable planner | Missing/stale base and ID/content conflicts retain original values and explicit choices. |
| Review source values and office target choices | 3 | after validator/context/planner / read-only UI | Original/target comparison is clear; cancel writes no business data and acceptance is unavailable until implemented. |

### Accept reviewed field submissions exactly once

Reviewed source: Task(s) 9. Prerequisites: import-review.

| Story title | Hours | Ownership / dependency boundary | Behavior and verification |
| --- | ---: | --- | --- |
| Commit import receipts and mappings together | 4 | prerequisite / import repository | Immutable source, ledger and mapping transaction rolls back coherently and handles identical replay. |
| Apply reviewed drafts while retaining original quote links | 4 | after repository API / application helper | Explicit draft resolution preserves original source quote IDs/status and consistent selected identities. |
| Require renewed review after context changes | 2 | after repository contract / acceptance guard | Revision/mapping/context changes invalidate the preview without altering known duplicate behavior. |
| Accept replayed and delayed submissions through the office UI | 3 | after repository/helpers / service composition | Actual file round trip is idempotent; old-engine snapshots display but new quotes require current recalculation. |

### Recover catalog and imported office evidence

Reviewed source: Task(s) 10. Prerequisites: backup-restore, catalog-release, import-accept.

| Story title | Hours | Ownership / dependency boundary | Behavior and verification |
| --- | ---: | --- | --- |
| Verify current archive and key backup coverage | 3 | existing backup inventory / extension owner | Extend the existing real-data recovery fixture and required-inventory checks for current generated artifacts; reuse the capture/restore implementation and earlier catalog-release key proof. |
| Restore import mappings links and duplicate receipts | 3 | fixed backup extension API / real-data fixture | A restored real accepted submission preserves identities and delayed plaintext replay needs no retired device key. |
| Verify the complete current office restore | 3 | after extensions / isolated restore evidence | Compare database, attachments, keys and archives; failed hash preserves destination and source data. |

### Launch the field application without network

Reviewed source: Task(s) 10. Prerequisites: registration, field-quotes, field-returns.

| Story title | Hours | Ownership / dependency boundary | Behavior and verification |
| --- | ---: | --- | --- |
| Generate exact versioned app-shell asset metadata | 3 | prerequisite / build assets | Actual Expo chunks/fonts and version/hash metadata are listed with isolated worker typecheck. |
| Cache only the versioned application shell | 4 | after asset interface / worker | Install precache/navigation fallback excludes catalog URLs and never skips waiting on install. |
| Register the production worker without reloading edits | 2 | after worker protocol / registration adapter | Correct production-only no-cache update behavior distinguishes initial install from requested activation. |
| Cold-open retained work and PDF output offline | 3 | after shell and adapter / browser proof | Built app reopens drafts/catalog/quotes/outbox without network; physical acceptance stays separate. |

### Upgrade the field app without losing work

Reviewed source: Task(s) 10. Prerequisites: offline-shell, catalog-refresh, field-returns.

| Story title | Hours | Ownership / dependency boundary | Behavior and verification |
| --- | ---: | --- | --- |
| Check waiting-release and stored-data compatibility | 3 | prerequisite / compatibility protocol | Read actual stored work and both enrollment slots; unsupported schema or failed decrypt defers activation. |
| Defer activation until edits are durably saved | 3 | after compatibility API / controller | Dirty/saving/failed flush preserves current app; explicit successful Save and update can proceed. |
| Keep the prior shell until replacement boot succeeds | 4 | after protocol / worker lifecycle | Two-client recheck refuses unsafe activation; cleanup follows successful boot/store read only. |
| Rehearse genuinely different preserved-store releases | 3 | after controller/worker / browser integration | Distinct visible versions and asset hashes preserve active/pending keys plus existing saved work. |

### Recover field work after storage loss

Reviewed source: Task(s) 10. Prerequisites: field-returns.

| Story title | Hours | Ownership / dependency boundary | Behavior and verification |
| --- | ---: | --- | --- |
| Export self-contained work without catalog credentials | 3 | prerequisite / recovery contract | Checksummed snapshots preserve draft/customer/quote/outbox/device identity and truthful export failure. |
| Preview recovery identity conflicts without writes | 3 | after contract / preview helper | Exact records are no-ops; conflicts and keep-existing/abort choices are explicit. |
| Restore reviewed rows in one rechecked transaction | 4 | after contract / store transaction | Changed hashes invalidate preview and injected failure leaves all prior rows intact. |
| Recover into a separate profile and reenroll explicitly | 2 | after preview/store/export / UI integration | Original IDs and duplicate behavior survive while catalog credentials are reacquired separately. |

### Qualify the complete owner trial

Reviewed source: Task(s) 10; acceptance 1–11. Prerequisites: office-recovery, app-upgrades, field-recovery, catalog-refresh.

| Story title | Hours | Ownership / dependency boundary | Behavior and verification |
| --- | ---: | --- | --- |
| Prepare exact-release conformance inputs and records | 2 | already-deployed conformance actions / evidence setup | Pin application release, fixture hash, expected results and device records. No new application helper is introduced by this evidence epic. |
| Verify iPhone offline calculations and customer output | 3 | after fixture / owner iPhone session | Exact release/fixture and actual owner inputs produce recorded results, frozen quotes and visually checked PDFs. |
| Verify iPad offline calculations and customer output | 3 | after fixture / owner iPad session | Independent iPad observations match same-release Mac output; no inherited iPhone evidence. |
| Verify real Mac quote history and explicit repricing | 2 | owner Mac session / evidence | Real quote/input/history preservation and recovery demonstrate reviewed manual/override cases. |
| Verify iPhone enrollment and key rotation | 3 | owner iPhone session / evidence | Camera/image/paste/denial, early pending key, unknown key, interruption and retry have actual recorded outcomes. |
| Verify iPad enrollment and key rotation | 3 | owner iPad session / evidence | Record independent credential/rotation behavior and retention; no unexecuted steps marked pass. |
| Verify iPhone dirty clean and offline app upgrades | 3 | owner iPhone session / evidence | Actual distinct versions preserve both key slots and saved work across failed/successful Save and update and offline reopen. |
| Verify iPad dirty clean and offline app upgrades | 3 | owner iPad session / evidence | Independently exercise the same real version change and record exact records, versions, hashes and failures. |
| Verify actual iPhone sharing and reviewed office return | 2 | owner iPhone/Mac session / evidence | Owner manually chooses/sends target; download fallback, mapping, replay and changed content have observed results. |
| Verify actual iPad sharing and reviewed office return | 2 | owner iPad/Mac session / evidence | Record iPad-specific share/download and import behavior independently. |
| Verify isolated Mac restore and delayed plaintext import | 3 | owner Mac session / evidence | Actual backup restores identities/keys/archives/mappings and duplicate receipt after key retirement. |
| Verify field recovery in separate test profiles | 3 | owner device/profile sessions / evidence | Restore exported local work, recheck conflicts/failed-save truthfulness and preserve identities without credentials. |
| Reconcile the eleven-case acceptance ledger | 2 | after observed sessions / evidence integration | Exact versions/hashes/expected/actual and unresolved failures are recorded; Android remains untested/deferred. |

## Legacy-to-replacement coverage

The original #1 planning/index scope is replaced by the complete flat sibling set, not by its first narrow epic. Registered retirement used administrative index #36 as the single truthful representative for the full mapping. It has no child relationships, app integration branch or blocking role; product work stays exclusively in the sibling epics. The owner authorized it, and administrative audit index #36 now represents this role. It has no product branch or child hierarchy.

Every legacy record was registered-superseded by #36; the rows identify its product-scope successor epics. No record was deleted or represented as delivered. Historical parent links remain.

| Old issue | Old plan slice | Replacement keys | Disposition after authorized migration |
| --- | --- | --- | --- |
| #1 | Entire first-real-job trial | All sibling epics through the non-parent delivery index | Replaced / closed not planned, not Delivered |
| #2 | 1a | foundation | Verified Replaced / closed not planned through #36 |
| #3 | 1b | bays | Verified Replaced / closed not planned through #36 |
| #4 | 1c | bays, requirements | Verified Replaced / closed not planned through #36 |
| #5 | 2a | catalog, prices | Verified Replaced / closed not planned through #36 |
| #6 | 2b | purchases | Verified Replaced / closed not planned through #36 |
| #7 | 3a | costs | Verified Replaced / closed not planned through #36 |
| #8 | 3b | costs | Verified Replaced / closed not planned through #36 |
| #9 | 4a | catalog, prices, visits, requirements | Verified Replaced / closed not planned through #36 |
| #10 | 4b | foundation, visits | Verified Replaced / closed not planned through #36 |
| #11 | 4c | attachments | Verified Replaced / closed not planned through #36 |
| #12 | 4d | catalog, prices, requirements | Verified Replaced / closed not planned through #36 |
| #13 | 4e | visits, run-editing, estimates, attachments | Verified Replaced / closed not planned through #36 |
| #14 | 4f | run-editing, estimates | Verified Replaced / closed not planned through #36 |
| #15 | 5a | quotes | Verified Replaced / closed not planned through #36 |
| #16 | 5b | proposals | Verified Replaced / closed not planned through #36 |
| #17 | 6a | catalog-release | Verified Replaced / closed not planned through #36 |
| #18 | 6b | catalog-release | Verified Replaced / closed not planned through #36 |
| #19 | 6c | catalog-release | Verified Replaced / closed not planned through #36 |
| #20 | 7a | foundation, registration, field-visits | Verified Replaced / closed not planned through #36 |
| #21 | 7b | field-visits, field-quotes | Verified Replaced / closed not planned through #36 |
| #22 | 7c | registration, field-visits, field-quotes | Verified Replaced / closed not planned through #36 |
| #23 | 8a | registration | Verified Replaced / closed not planned through #36 |
| #24 | 8b | registration, catalog-refresh | Verified Replaced / closed not planned through #36 |
| #25 | 8c | registration, catalog-refresh | Verified Replaced / closed not planned through #36 |
| #26 | 9a | field-returns | Verified Replaced / closed not planned through #36 |
| #27 | 9b | import-review, import-accept | Verified Replaced / closed not planned through #36 |
| #28 | 9c | field-returns, import-review, import-accept | Verified Replaced / closed not planned through #36 |
| #29 | 10a | backup-capture, backup-restore, office-recovery | Verified Replaced / closed not planned through #36 |
| #30 | 10b | field-recovery | Verified Replaced / closed not planned through #36 |
| #31 | 10c | offline-shell | Verified Replaced / closed not planned through #36 |
| #32 | 10d | app-upgrades | Verified Replaced / closed not planned through #36 |
| #33 | 10e | foundation, costs, registration, catalog-release, offline-shell, qualification | Verified Replaced / closed not planned through #36 |
| #34 | 10f | qualification | Verified Replaced / closed not planned through #36 |
| #35 | 10g | qualification | Verified Replaced / closed not planned through #36 |

## Completed migration verification

- Reviewed source Tasks1–10 and trial acceptance cases1–11 were cross-checked against these scope rows; owner-data, immutable history, update/rotation, recovery and physical-device requirements remain future implementation constraints.
- Canonical AITM creation fragments and pinned per-epic source plans supplied Story Intent and per-AC verification references. Intake creation does not replace native Refine/Plan approval.
- All28 epics are roots; all135 children have exact intended native parents, Backlog state, ownership, XS/S sizes, 2–4h estimates and direct prerequisites. No application dispatch occurred.
- A whole-set pre-retirement PASS observed all old1–35 OPEN. All34 old children were then retired and separately verified Done/Replaced before original epic1 was retired last.
- Registered AITM `supersede --by36` produced the requested Replaced/not-planned result for every old record; final live verification passed. No raw closure, detach, synthetic app proof or package-cap changes were used.
- [Exact issue/scope map](2026-11-01-sibling-delivery-issue-map.md) and [final verification evidence](2026-11-02-36-sibling-migration-verification.md) record the resulting authority. No implementation is authorized.

## Review provenance and unresolved execution setup

Three read-only worker passes supplied Mac cuts, field/release cuts and an independent workflow/sizing review. The orchestrator split bundled persistence/save/enrollment/device stories, chose the ABI-preserving capture ordering above, corrected functional first-create dependencies and premerge/postmerge evidence timing, and checked this dependency graph for cycles and every forecast for the 2–4-hour range. The conformance actions ship in earlier feature epics. Final qualification observes their deployed application release; its documentation/evidence commit is recorded separately. If evidence integration changes relevant application artifacts or behavior, affected observations must be rerun rather than inherited.

Cloudflare project/origin, credential provisioning and the local build trigger are still owner setup inputs. No tracked build/deploy pipeline currently exists. Later implementation must prove the selected mechanism; this planning task does not configure or publish it. Owner physical-device sessions remain observed acceptance work, not an automatically passing gate. Android remains untested/deferred.

## Trial acceptance crosswalk

| Reviewed case | Replacement scope homes |
| --- | --- |
| 1 Catalog/history/settings | catalog, prices, purchases, catalog-release; immutable recipe versions in requirements |
| 2 Geometry/purchases | bays, requirements, purchases |
| 3 Manual allowances | costs, estimates, field-quotes, quotes |
| 4 Preserved proposals | visits, quotes, proposals, field-quotes |
| 5 Allocation/disclosure | purchases, costs, estimates, proposals |
| 6 Imports/identity/outbox | field-returns, import-review, import-accept |
| 7 Catalog refresh/compatibility | registration, catalog-refresh, offline-shell |
| 8 Actual app upgrade | offline-shell, app-upgrades, qualification |
| 9 Key rotation | catalog-release, registration, catalog-refresh, qualification |
| 10 Save truthfulness/recovery | run-editing, field-visits, attachments, backup-capture, backup-restore, office-recovery, field-recovery, qualification |
| 11 Mac/iPhone/iPad parity | costs/registration conformance actions, field-visits adapter parity, qualification |

Coverage homes are not proof that a case passed. Canonical creation/refinement must bind the exact reviewed scenarios to their verifiers, including the three 150-ft counts, connected 10/3/10-ft cuts, $2,000 selling override with the configured 10% test tax, private business settings, missing/stale-base identity review, and concrete rotation/upgrade/recovery sequences.
