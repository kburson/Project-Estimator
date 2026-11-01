# Project Estimator: PWA and Mac office application design

Date: November 1, 2026.
Status: **Revised draft for owner review, after independent Claude review and follow-up clarifications.** This consolidates the discussion and completed transport spike. It is a product/architecture specification, not an implementation plan or authorization to start the application. Review this document before generating the backlog or implementation plan.

## 1. Purpose and first-version goal

Help one owner run a construction business: maintain vendors and prices, record customers and requested work, measure fence runs, compare construction designs, calculate a job specification, and prepare a customer proposal with drawings and a tentative schedule. Begin with fences and gates. Preserve an extension boundary for irrigation and other home-improvement projects without implementing their rules now.

The first useful release must let the owner produce and retain an explainable fence estimate from real measurements and entered prices, then repeat that workflow offline on the phone/tablet. Delivery speed and learning from actual jobs take precedence over accounts, enterprise security and elaborate synchronization infrastructure.

One business and one owner are the administrative model. Friends or other trusted users may enroll devices to try the tool and receive that business's catalog. This is not a multi-tenant service or an employee-permission system. An enrolled user can access the catalog they are given; the customer presentation screen is a disclosure boundary in the UI, not a security role that hides decrypted information from the device owner.

## 2. Confirmed direction and evidence

- Mac-only office application: local React web UI, Node service and SQLite master database. No Windows requirement.
- Mobile: CDN-delivered PWA, installed through Add to Home Screen. No App Store distribution or Apple developer membership required for this delivery format.
- Use React Native Web with Expo for the mobile UI, retaining a possible native React Native build later. The web target remains subject to browser APIs and controls.
- Shared TypeScript calculations and contracts. Do not implement different pricing engines for office and field.
- Cloudflare serves static application files and versioned data packages. No hosted business database or always-running cloud application backend.
- The Mac publishes catalog updates. Enrolled devices fetch/decrypt them directly from the CDN and calculate offline. No household/device DNS changes, local HTTPS certificate setup, or QR exchange per connection.
- Field records return as user-shared email attachments, with reviewed import into the Mac. A Gmail collection agent is a later automation of the same importer.
- Keep the first version practical: one business catalog key and straightforward validation. No user-account server, automatic per-device revocation, native distribution work, or general sync engine.

The disposable V4 probe demonstrated QR enrollment, encrypted CDN catalog download, retained enrollment and offline encrypted-cache readback on the owner's iPhone and iPad, by owner observation. Desktop checks exercised an update without re-enrollment, unchanged-package skipping and failure preservation. Android is unavailable and untested; it remains a later validation item, not a blocker for the owner's trial. A full application-version upgrade preserving jobs/enrollment still needs a dedicated release check. The probe is not product code or a completed security assessment.

Sources: [R&D checkpoint](../../research/2026-11-01-encrypted-cdn-probe.md), [earlier requirements](2026-10-31-project-estimator-v1-design.md), and [native-capability log](../../design/mobile-native-capability-log.md). Earlier Swift/native-iOS and direct Wi-Fi architectures are historical alternatives. This draft replaces their direction only after owner approval.

## 3. Proposed release boundary for review

These are product increments, not a task plan or a new estimate of delivery time.

| Increment | Usable outcome |
| --- | --- |
| First real-job trial | Mac vendor/component catalog with manual historical pricing; one owner-validated fence design; arbitrary connected runs and short returns; segment costing/markup/overrides; customer/job/draft estimate records; frozen customer quote snapshots and customer-safe proposal/PDF; manual priced work items; mobile offline form/calculator; QR-enrolled encrypted CDN catalog; field package export and reviewed manual office import; local backup/recovery. |
| Complete fencing/gates version one | Additional validated fence recipes and single/double gates; design alternatives and revision comparison; selected office-job export/import by file/email; stock drawing/image library and measured site schematic; approximate crew calendar. |
| Subsequent improvements | Priority-vendor price adapters, automated Gmail collection, receipt extraction, price-history charts, customer-supplied-materials/labor-only bids, on-site signatures and printer integration, native app evaluation, irrigation and other project types. |

The first-trial cut is a proposal for review, not a claim that previously requested drawings, gates or schedules were cancelled. Manual price entry and manual attachment import make the trial useful before external automation is ready. Preserve data needed by later features from the start.

## 4. Main workflows and screens

### Office setup and catalog

The owner opens the local Mac application, sets business/proposal defaults and a backup destination, creates vendors and components, records vendor prices, and reviews design recipes. The owner then explicitly publishes an approved catalog release and registers mobile devices using the desktop QR. Publication excludes customer records, job documents, email credentials and the master database.

Office navigation: Customers and jobs; Catalog and vendors; Designs and drawings; Field submissions; Catalog publishing/device registration; Settings and backup. A job workspace contains Requirements/measurements, Design alternatives, Internal estimate, Customer proposal, Documents and Schedule. Screen layout follows the task; dense office tables do not have to reuse mobile layout unchanged.

### Field visit

Open the installed PWA, check catalog date/update status, select or create a local customer/job, enter requirements and named measured runs, choose a design/options, calculate a preliminary estimate, and save the draft. Use Present to customer to save a frozen preliminary quote and show its customer-safe view. An internal layout preview may remain a clearly labeled draft. Offline work must not require a network request or the Mac to be running.

Mobile navigation: Jobs; New estimate; Design library; Updates; Outbox. Save edits locally as the owner works. Label records as local draft, prepared submission, handed to mail, or office-confirmed; do not imply that local save is an office backup.

### Office review

Prepare a field package, select Mail/Gmail from the device share sheet, and tap Send. On the Mac, select the received attachment and preview the customer, job, measurements, source catalog and preliminary estimate before accepting it. Refresh prices or change the draft as needed, then freeze an office-reviewed quote. The trial uses the same quote-snapshot mechanism in office and field: field snapshots are Preliminary; when freezing an office-reviewed quote the owner chooses Preliminary or Issued. Status is part of the frozen snapshot, so issuing a previously preliminary quote creates a new snapshot rather than changing the old one. Comparing design alternatives/revisions belongs to complete v1. Do not overwrite the submitted field version.

Automatic mail collection later adds items to the same review inbox. Sender/subject filtering alone never authorizes replacing master records.

## 5. Vendors, components, offers and history

A vendor stores name, contact people, phone/email, address, website, branches/locations and notes; it may sell materials, rent equipment or both. A component defines the material/equipment independently of who sells it: description, nominal and actual dimensions, stock length, material/finish, purchase unit and package quantity. Vendor offers add SKU/product URL, exact specification/pack, currency, branch and availability notes.

Each price observation preserves observed/source/effective dates, source type and evidence, tax basis, offer identity, and independently known tiers:

- Retail price.
- Bulk price and qualifying purchase quantity/unit/range.
- Directly quoted contractor price.
- Contractor percentage discount and its stated basis.

Unknown prices stay missing, never zero. The owner selects a default vendor/offer for each component when publishing a release; the calculator never silently changes vendors to find the cheapest price. A job may explicitly override that choice with another offer included in the release. Ship each available selected offer's applicable retail/bulk/contractor tiers, quantity units, discount basis and stacking conditions, not one pre-resolved unit price. Within the chosen offer, use the lowest final cost among eligible, explicitly permitted pricing arrangements after purchase/pack rounding; an explicit valid tier selection overrides this default. Record the chosen offer, tier, basis and final cost. Compare Mac/field results using the same release and explicit inputs, not the Mac's independently refreshed live history.

Do not apply a contractor discount twice or stack bulk/promotional/contractor discounts unless permitted. Determine bulk eligibility from purchased quantities. Retain quoted and calculated prices separately, and record the selection used by an estimate.

New prices append observations. Corrections link to the original and exclude erroneous observations from selection without deleting provenance. Preserve receipt purchase dates separately from import dates; an unknown historical date remains unknown. Compare equivalent specifications and units, retaining pack rounding, branch, date, tier and tax context. Rental billing periods are explicit; day/week prices are not interchangeable.

All vendors support manual entry. The Mac can later obtain prices through vendor-specific adapters after product/branch/tier mappings and access are validated. Failure leaves the previous observation and its date intact. Public retail pages do not establish contractor-account prices. Receipt attachments can be retained initially; extraction and trend/cross-vendor charts are later features. A paid receipt price does not automatically become a reusable contractor price.

## 6. Customers, jobs, documents and revisions

A customer has contacts, referral source/how they heard about the business, first-contact date, dated contact history and derived last contact. Customers can have multiple jobs and jobsite addresses. A job stores requirements, access/site constraints, runs/connections/gates, selected designs/options, alternatives, notes, documents, estimates and bids.

Use stable identifiers, including for records first created offline. Preserve event/source times separately from import times. A bid revision captures scope, quantities, purchase choices and price observations, recipe/calculator/catalog versions, labor assumptions, markup, overrides, tax treatment, exclusions, selected drawings and totals. The trial saves an immutable quote snapshot whenever Present to customer, PDF export or proposal sharing is used. Field snapshots are labeled Preliminary; an office-reviewed snapshot may be frozen as Preliminary or Issued, recording exactly what was presented. Repeating the action without changes reuses the snapshot; changing scope/prices produces a new snapshot ID. Issued revisions are immutable; changes create another revision. A new catalog never silently reprices an existing bid or draft. Reprice a draft only through an explicit action with a visible change summary.

Local drafts and frozen quotes retain self-contained resolved pricing, quantities, recipe inputs and calculation results sufficient to display them without reopening an old encrypted catalog. These job records and the outbox use ordinary device job storage, not encryption under the catalog key. The first version does not add an independent job-encryption/key-ring system. Recalculating with a new release is an explicit action on a draft/copy; displaying an old quote uses its saved result and never recalculates it.

Documents are attached to the job and referenced by the bid revision that used them. Do not expose the entire customer database to every enrolled device: the initial mobile store contains jobs entered/imported there; the first trial links field-created records to existing office customers/jobs at import. Selected office-to-mobile private job transfer belongs to complete v1, using an owner-exported versioned job file sent by email or saved to Files, then explicitly imported into the PWA. It preserves office IDs and base revision. It is not part of the generally published catalog or a LAN-sync requirement.

## 7. Site measurements and estimating geometry

Use a form with any number of runs. A run has an ID, editable label, positive length in feet/inches, start/end connection IDs, design/options and relevant site notes. Direction names N, NE, E, SE, S, SW, W and NW are convenient labels, not bearings. Permit repeated directional names and custom labels such as Tree Return A. Identity determines whether endpoints are shared; matching text or approximate drawing location does not merge posts.

Require no GPS, compass angles, surveying or exact corner geometry. Measured lengths and construction details determine costs. An askew corner does not itself add a surcharge. Single runs, partial enclosures and connected 2–4 ft obstacle returns must work without a four-side property assumption.

For an isolated gate-free run, maximum-spacing bays are `ceil(length / maximumSpacing)` and post positions are bays + 1. Calculate runs individually, then merge shared endpoint posts by connection identity. Internal posts remain per run. Gates carve openings out of facing and introduce compatible supports/hardware/labor; count shared gate supports once. A gate opening cannot exceed or overlap another opening in its run.

Retain per-run/per-bay cuts before aggregating purchases. Short rails and endpoint posts do not disappear into an average per-foot cost. Separate installed quantities, allowance/waste, purchased whole units/packages and unused stock. Each recipe declares a simple feasible stock/cut rule. If none is configured, default explicitly to no offcut reuse: purchase one suitable stock unit for each required cut piece, then apply package rounding. Show the resulting unused stock/cost and a conservative no-reuse notice internally so the owner can review it. Any owner reduction is a documented manual adjustment, not an unverified automatic cut optimization. Only reuse offcuts under an explicit feasible rule; do not build a general cutting optimizer for the trial.

Reference cases, with maximum spacing and a shorter final bay allowed: one isolated 150 ft run needs 35 posts at 54 in, 20 at 96 in and 26 at 72 in. A connected 10 ft + 3 ft + 10 ft path at maximum 8 ft spacing has five bays and six unique posts. These geometry examples do not validate board-joint or structural details.

## 8. Versioned fence/gate designs and calculator

Design data defines supported options, dimensions/coverage/gaps, spacing, supports and joints, material requirements, compatible fasteners/attachment counts, stock/pack units and labor work units. The executable calculation engine ships with the app; recipes and parameters are separately versioned data, not downloaded arbitrary code.

Owner examples to validate and populate:

- 9 ft Postmaster galvanized steel posts driven 3 ft into the ground.
- Horizontal 1x6x16 boards with proposed 54 in post spacing.
- Vertical 5/8 in × 5.5 in × 6 ft pickets with proposed 96 in spacing; also wood-post/rail designs at 8 ft maximum spacing.
- Horizontal 6 ft pickets with proposed 72 in spacing.
- Optional kick board, cap board, trim and concrete post collars.
- Ceramic-coated screws versus stainless-steel ring-shank collated nails.
- Single/double gates with specified opening, height, frame, supports, hinges, latch and fasteners.

Select one fully specified, owner-validated recipe for the trial; additional recipes become selectable only when their required inputs and supported cuts/joints are populated. In particular, 16 ft stock at 54 in spacing does not by itself define a supported joint arrangement. Missing construction details or prices produce an incomplete estimate with named missing inputs, rather than invented defaults or a deceptively low total. Concrete collars need dimensions and yield; fasteners need attachment counts and pack quantities.

Use decimal-safe arithmetic with money serialized as decimal strings, explicit units and deterministic rounding. Store measured lengths in a fixed small integer unit sufficient for sixteenths of an inch. Validate bounds and convert units at the UI boundary. Calculations consume explicit immutable inputs and make no storage/network calls. The same input fixtures must produce the same output in Mac and field clients.

## 9. Internal costs, selling prices and customer output

Internal job specifications show quantities/purchases, selected unit costs, material cost, person-hours, internal hourly cost, equipment/other expenses, segment costs and selling prices. Initial segments: tear-out/site preparation, equipment rental, material acquisition, post installation, rail installation, cap installation, picket/facing installation, trim installation and final cleanup. Assign each material cost once to the installation segment that consumes it (posts to post installation, facing to facing installation, and so on). Material acquisition means sourcing/pickup/delivery labor and fees, not a second charge for those materials. Pool purchased quantities by selected offer across the job before testing tiers/pack rounding; allocate shared purchase cost to consuming segments in proportion to their installed requirement, with deterministic cent rounding that preserves the purchase total. Include only applicable segments; rentals are expenses, not automatically separate crew-duration blocks.

The trial permits manual priced work items for haul-off, custom work, a gate allowance or other work outside the validated recipe. Each has an ID, customer-facing description, segment, quantity/unit, explicit unit cost and cost category (material, labor, equipment or other), source/assumptions and a clearly marked manual status. Apply the same segment markup/override rules and retain it in the quote snapshot. Manual labor can carry a directly entered cost; no hours are invented for it. It cannot silently make missing inputs in an automatic recipe valid. Manual gate allowances do not alter fence geometry: the owner enters fence runs excluding the opening, accounts for gate supports not already counted at those run endpoints, and confirms no duplicated facing/support costs. Automated gate placement, support selection and opening validation remain complete-v1 work.

Labor effort is person-hours. Two people working six hours supply 12 person-hours, while elapsed workdays are calculated separately. Base selling price is cost × (1 + markup percentage). Precedence: direct segment selling-price override, segment markup, then job default markup. Allow clearing an override. Show effective markup/profit and below-cost flags internally. Markup is not margin. Business settings require the owner to confirm default labor cost, markup and tax treatment before publication/quoting; no workbook percentage is assumed. Purchase tax, when entered, is part of internal acquisition cost allocated with the relevant purchase. Optional tax charged to the customer is calculated on the final selling amount of owner-selected taxable segments, after markup or direct overrides, and shown separately on the proposal; manual items follow their segment and the tax is not marked up again. A manual material unit cost has an explicit purchase-tax-included flag and, if not included, an owner-entered purchase-tax rate. There is no automatic material/labor split of a segment selling override for customer tax. Both use explicit rates/tax-included flags so a tax-included observation is not taxed twice. This is configuration, not jurisdictional tax advice or an automatic tax-rules service. A zero rate must be intentional, not a substitute for an unknown setting. Settings are included in the private pricing module and snapshotted per quote.

Customer proposals contain scope, selected inclusions/exclusions/assumptions, segment selling totals where shown, and overall selling price. They exclude material/labor cost splits, internal unit costs, hours, hourly rates, markup and profit. If labor is presented separately, display one selling amount. Generate the customer view/PDF from an allowlisted proposal model, not by hiding columns in the internal document.

Estimates are free. No separately billed drafting fee appears. Record measurement/drawing preparation effort internally and recover it through the project price where appropriate without counting it twice. A preliminary field estimate identifies its pricing date and assumptions; office review freezes a separate Preliminary or Issued quote using the same trial snapshot mechanism. Labor-only/customer-supplied-materials bidding is later work; preserve material requirements independently of who purchases them.

## 10. Drawings, images, presentation and scheduling

Maintain uploaded stock drawings for fence/gate construction, installation details and final-look examples. Only the site plan is job-specific. Associate exact drawing versions with the bid. Photorealistic rendering, generated bespoke architectural details and survey-grade mapping are outside version one.

The site schematic preserves measured run lengths at scale with approximate orientation. Label it “Layout schematic; dimensions govern.” Do not stretch measured runs to force an irregular boundary to close; use a schematic break or separate measured runs when necessary. Directional labels remain meaningful even when the illustration is approximate.

Publish drawings and sample images as independently versioned assets. Download lightweight previews, with explicit offline download for chosen designs/full images. Missing optional sample images do not block a priced estimate. Before field use, show which required design assets are present offline.

Default crew: two people, six-hour days, five days/week. Proposed initial workweek: Monday–Friday, editable with job crew size and non-working days. Tentative scheduling begins after materials are sourced/delivered, from an entered anticipated start date. Sequence work dependencies and waiting/curing periods. Respect minimum crew and tasks that cannot speed up linearly with crew count. Show approximate duration and expected daily activity, with potential extension for weather/material/site constraints. No automatic weather forecasting or promised finish date.

On-site signature capture and portable printing are later evaluated capabilities, not prerequisites for the first real-job trial. Bind a captured acceptance to the exact customer-visible bid revision, not a mutable draft. Validate the exact printer/model and system/vendor printing path before promising Bluetooth printing. Track these in the native-capability log rather than assume they require native installation.

## 11. CDN packages, enrollment and key changes

### Modular releases

A small current-release manifest lists module IDs/versions, schema/engine compatibility, content-addressed URLs, sizes/checksums and encryption key IDs where applicable. Use one current manifest for the trial. Its required engine/app versions determine compatibility; do not create a manifest service or one manifest per device. Start with one current-pricing package (selected offers, all applicable tiers and the private business settings: labor/markup/tax defaults and proposal business text) and one design-data package; drawings and images are individually versioned assets. Retain full vendor-price history on the Mac rather than shipping the entire history to phones.

Reuse unchanged files/addresses and encrypted outputs while content and key are unchanged. Clients download only missing or changed modules. A key change necessarily produces new encrypted outputs even when the plaintext is unchanged. Publish a complete valid static release with its manifest; do not expose a manifest whose referenced files are unavailable. Routine catalog publication need not be an application-code update.

Check on launch/foreground, at a modest interval while in use, and via Check for updates. Never promise updates while the app is closed. Keep manifest requests current and exclude them from offline app-shell cache responses. Stage and validate required related data before switching the active release in one transaction. A failed/incompatible update leaves the prior usable release in place and explains the problem. Keep optional media downloads independent. Show active catalog date/version, last successful check and stale/offline status.

### Application/catalog compatibility and activation

If a manifest requires a newer app/engine, show **App update required**, keep the active catalog and local jobs usable, and defer that catalog's activation. This is separate from an unknown key's **Registration update required**. Interrupted downloads, offline checks and unsupported schemas never clear active data. Read stored quotes from their snapshots even when current catalog updates are unavailable.

Activate an app update at launch with no unsaved edit, or after an explicit Save and update action; do not reload an open edit or discard an unsent submission. Keep the previous app shell until the replacement is ready. For the trial, keep the job-store and catalog schemas compatible across routine releases; an app release must read the existing trial store/active catalog before activation. Do not perform a breaking database/catalog migration as an unattended service-worker update. A future breaking schema requires an explicit tested migration/recovery release, outside this trial's routine publishing workflow. Test an actual app-version update both online and offline, including enrollment, drafts, frozen quotes and outbox; a page reload alone is not that test.

Select a stable production HTTPS origin before collecting trial job data. The probe origin is test-only; moving origin requires an explicit data/enrollment transfer and is not an ordinary app update.

### Enrollment and private data

One random business catalog key protects sensitive prices, internal rates and other private catalog data using authenticated encryption. Public design/sample assets may remain unencrypted when intentionally approved for publication. Never publish decrypted private catalogs, keys, office credentials, customer/job data or the SQLite database with the PWA.

The Mac retains the key locally and displays its enrollment QR on explicit action. Scan in the installed PWA once; store the imported key separately from application assets. Retain it across normal PWA updates. Provide the tested pasted-enrollment fallback as well as QR-image selection for an enrollment image emailed by the owner, since a device cannot scan its own displayed email with its rear camera. Emailing the QR shares a reusable catalog credential; it is an explicit owner distribution action, not an automated action by default.

### Key-change workflow agreed with the owner

1. The owner requests a catalog-key change on the Mac. Generate a new key and key ID.
2. Re-encrypt all affected private modules, assign new package identities/hashes, and prepare a consistent release referencing the new key.
3. Publish the replacement release. Remove superseded encrypted package files from the current production publication; retain unrelated/shared assets still referenced by supported releases. Historical deployment URLs and already downloaded copies are separate from the current file set and must not be described as revoked or erased.
4. A device seeing an unknown key ID shows **Registration update required** with instructions to visit the office or use an enrollment QR supplied by the owner. Detect this through metadata; a generic decryption error is not the expected user experience.
5. Defer an unknown-key package download until registration in the trial; if a download was already staged, keep it inactive. A device holds at most one active key and one pending key. Scanning the new QR before its release is published saves a pending key without replacing the active key/catalog. Re-scanning the active key is harmless; a later pending QR replaces the earlier pending key only after explicit confirmation.
6. After registration, retry/download the matching release. Activate its key and catalog together only after decryption, compatibility and data validation succeeds; otherwise retain the current key/catalog. Then discard the superseded phone catalog/key, since local drafts/quotes/outbox contain their own snapshots and do not depend on it. A fresh device retains its pending enrollment until a matching compatible catalog can be installed. Updates requiring the new data cannot use the old key or pretend the old data is current.

Normal price/design updates under the same key require no re-registration. App updates also require no re-registration. Storage clearing, a new browser/device/origin or a deliberate key change may require enrollment again. Rotation protects future releases; it cannot retract a previously downloaded/decrypted catalog. Keep previous Mac keys only as local recovery material for encrypted catalog archives, rather than publishing them to newly enrolled users. The trial's field packages do not depend on these catalog keys.

## 12. Field packages, import and recovery

The trial uses the already tested UTF-8 JSON attachment with a checksum; it is plaintext, not encrypted with the catalog key. It contains customer/job and internal estimate data, so show the office recipient and require the owner to choose the mail target and send it. Its checksum detects corruption, not sender authenticity; reviewed import remains mandatory. Do not add an email-encryption protocol or device-signing infrastructure for the trial.

An immutable portable field package includes schema/package/device/business IDs, created time, customer/job IDs, known office base revision, catalog/design/calculator versions, self-contained selected recipe inputs, pricing and assumptions sufficient to display/explain the result, frozen quote IDs/snapshots when presented, runs/options, draft estimate and content checksum. Retain its body in the local outbox. Keep package size modest; large photos/documents are explicit separate attachments rather than silently embedding the full library.

Use the native share sheet exposed by the browser; the user chooses the mail target and taps Send. Provide download/save for unsupported file sharing. Do not rely on mailto attachments or assume recipient/subject prefill works everywhere. A successful share means handed to a target, not delivered/imported. Re-sending the same content keeps the package ID; changed content creates a new linked revision/package.

The Mac importer validates schema, size, references and checksum, previews changes, and deduplicates by package ID plus content hash. Same ID/same content is harmless; same ID/different content is a conflict. Package deduplication does not identify the same real-world customer entered separately. During preview, offer Create new or Link to existing customer/job; use stable known IDs when available and suggestions only for names/contact details. Never auto-merge by name/address. Store each accepted source-ID-to-office-ID mapping with the import record so a later package from the same field record resolves to the same office customer/job, while retaining the original submission unchanged. If a linked field record lacks an office base revision, treat its changes as a reviewed merge, not permission to replace the office record. Existing-record revisions changed since field departure require review, never silent overwrite. Preserve the received submission and commit accepted changes/import ledger together. A pending/cancelled import must not leave half a job in the master database. Do not execute attachment content or treat notes as agent instructions.

For the first trial, mark an outbox submission office-confirmed only through explicit owner confirmation after import; do not add a synchronization server just for acknowledgments. Later Gmail collection uses the same importer/inbox while the Mac is awake and authorized. Store future mail credentials outside PWA/catalog packages. Automated collection does not automatically send messages or accept arbitrary submissions.

Mac backup includes SQLite, attachments, settings, catalog release artifacts and recovery keys. Restore must preserve identities, all frozen Preliminary/Issued quote snapshots, source-ID mappings and import deduplication records. Mobile drafts/outbox need export/recovery; browser persistence is not a backup. Storage quota failures keep the last saved version and display a clear unsaved/error state. Normal application updates preserve enrollment, saved jobs and outbox; migrate compatible data transactionally and reject unsupported versions without clearing it.

## 13. Source workbook and initial data

Preserve `Heather-Fence Bid.numbers`. The earlier inspection recorded four sheets/23 tables, inconsistent 404/406 ft totals, omitted material/labor subtotal terms, fractional picket purchases, and inconsistent labor/tax assumptions. Use it as evidence and candidate seed data, not as a calculator to reproduce blindly.

The first trial can enter a small validated catalog manually. A later reviewed import stages vendors/components/prices/recipes with source locations, mappings and discrepancies; the owner accepts them before commit. Historical workbook prices remain historical observations, not newly verified current quotes. Unknown source dates stay unknown. Repeated imports must not duplicate accepted observations.

## 14. Technical boundaries and native transition

| Boundary | First-version responsibility |
| --- | --- |
| Mobile PWA | Expo/React Native Web static output, responsive touch UI, app-shell caching and foreground update checks. |
| Mac UI | React web interface for catalog/job review and publishing; reuse portable components where practical. |
| Shared domain/calculator | TypeScript models, validation, recipes, quantities, costing, segment selling prices, proposal model and scheduling rules; independent of browser/Node/device APIs. |
| Portable package contracts | Versioned manifests, catalog modules, enrollment data and field submissions. |
| Mac office service | Local Node service/SQLite and files, backup, publication, reviewed imports and later vendor/mail adapters. |
| Platform adapters | Storage, key/crypto operations, camera/QR, files, sharing, printing and application lifecycle. Implement web/Mac adapters only for this release. |

Browser IndexedDB and Web Crypto are not silently assumed to exist in a future native runtime. Native builds will need appropriate storage/key and device API adapters, data migration, signing/distribution setup and device acceptance checks. React Native Web may allow substantial UI reuse; DOM-only office grids, drawing/PDF rendering and navigation still need review. A native installation does not automatically inherit browser data or enrollment.

Maintain [the native-capability log](../../design/mobile-native-capability-log.md) during R&D and real use. Record a concrete user need, tested limitation, workaround and cost before promoting an item into native scope. Reconsider native delivery when observed benefits justify it; do not promise a build-configuration-only transition or build unused native infrastructure now.

Reference: [Expo web targets](https://docs.expo.dev/workflow/web/) explain the React Native Web/browser distinction. Dependency versions, exact file layout and build/deployment commands belong in the implementation plan after this spec is approved.

## 15. Acceptance and review

Acceptance must cover useful behavior, not only transport. **Trial** cases gate the first real-job release; **Complete v1** cases gate the later fencing/gates increment.

1. **Trial — catalog/history:** enter vendor retail/bulk/contractor arrangements; append a new observation without rewriting history or a saved quote. Demonstrate missing-price and non-stacking discount behavior, selected default offer and quantity-dependent tier selection. Confirm labor/markup/tax/business settings are shipped with the private pricing module.
2. **Trial — geometry/purchases:** produce the 150 ft post-count examples and connected 10/3/10 ft example. Price a 2–4 ft return with actual short supports/purchases and the declared cut rule or visible conservative no-reuse allowance. No arbitrary offcut reuse or total-length post averaging.
3. **Trial — manual work:** add a manual gate/haul-off allowance with quantity, cost category, description and segment. For the manual gate, enter fence runs excluding the opening and confirm supports/facing are not double counted. Verify normal markup/overrides and preservation in the frozen quote.
4. **Trial — preserved proposals:** save a customer/job and draft; Present to customer/export an immutable preliminary quote. Explicitly reprice/change the draft and prove the originally presented/exported snapshot remains unchanged. Keep the internal draft preview distinct from a frozen customer presentation; verify field Preliminary and office Preliminary/Issued labels are frozen and unchanged by later status choices.
5. **Trial — segment totals/disclosure:** attribute each material once, separately price acquisition effort/fees, apply job/segment markup and direct overrides, and clear an override. Preserve pooled purchase totals when allocating segment costs. For a taxable segment overridden to $2,000, a configured 10% customer-tax fixture produces $200, regardless of its internal material/labor split; test manual purchase-tax-included/excluded items separately. No internal unit costs/hours/markup fields enter the proposal/PDF data.
6. **Trial — imports/identity:** preserve field drafts/outbox offline; import the same attachment twice without duplicates; link a separately created field customer/job to an existing office record. A later package honors the stored mapping. Surface a missing/stale base revision for explicit review.
7. **Trial — catalog refresh:** enroll once, download only changed resources, reject corrupt/incompatible updates without damaging active data, and decrypt the cached catalog offline. An app/engine mismatch displays App update required; an unknown key displays Registration update required.
8. **Trial — actual app upgrade:** publish a different app version while the device has enrollment, active catalog, draft, frozen quote and outbox. Activate only at a safe boundary and preserve all five online and on offline reopening. Do not substitute an unchanged-version reload for this case.
9. **Trial — key rotation:** publish re-encrypted modules and remove superseded packs from the current publication. Test a new QR scanned before publication, an old-key device detecting the new release, and an interrupted/failed install. Retain the active key/catalog until a valid replacement commits. After activation, old drafts/quotes/outbox still display from snapshots without the old catalog key. QR image and pasted recovery paths use the same enrollment contract.
10. **Trial — recovery:** back up/restore Mac records, attachments and catalog recovery keys; recover/deduplicate a delayed plaintext field submission without needing a retired catalog key. Demonstrate a failed local save cannot be reported as saved.
11. **Trial — device calculation parity:** run identical validated recipe/geometry/pricing fixtures on Mac, iPhone and iPad and compare quantities, purchased packs, tiers, costs and selling totals. Record Android untested until hardware exists; it is not a trial blocker.
12. **Complete v1 — gates:** add supported single/double openings, remove their facing and count shared gate supports/hardware/labor correctly. Automated gate validation replaces the trial's manual workflow for supported designs.
13. **Complete v1 — alternatives/revisions:** compare supported design alternatives and issued bid revisions; neither comparison nor a new catalog changes the previously issued result.
14. **Complete v1 — documents/calendar:** preserve measured schematic lengths and stock drawing revisions; generate a tentative two-person/six-hour/day schedule without disclosing internal labor costing.
15. **Complete v1 — office job transfer:** export a selected private job by file/email and import it into the PWA, preserving office IDs/base revision without publishing it to the CDN. Return a field edit and resolve any intervening office edit through reviewed import.

### Owner review points

- Confirm the proposed first-trial cut in section 3: one validated automatic fence recipe, manual allowances including gates, frozen presented quotes, and manual reviewed imports. Automated gates/alternatives/drawings/calendar follow in complete v1.
- Confirm React Native Web/Expo for mobile, React/Node for office, and the realistic native migration boundary in section 14.
- Select/populate the first owner-validated recipe before calculation implementation; the example spacings do not supply missing board joints or other recipe values.
- Confirm Monday–Friday as the initial editable workweek. Enter business tax/markup/labor defaults before catalog publication; the spec defines their placement/behavior but does not invent tax rates. A separate visible customer discount is deferred; segment selling overrides cover the trial. Select the stable production origin before real job data is collected.
- Review the catalog-key change/re-registration behavior in section 11, including retention of existing work and removal limits for already distributed copies.

After owner review and corrections, approve the written spec before creating the backlog/implementation plan. No product scaffolding, new cloud service, native app enrollment or implementation tasks are started by this document.
