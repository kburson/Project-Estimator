# Project Estimator: PWA and Mac office application design

Date: November 1, 2026.
Status: **Draft for owner review.** This consolidates the discussion and completed transport spike. It is a product/architecture specification, not an implementation plan or authorization to start the application. Review this document before generating the backlog or implementation plan.

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
| First real-job trial | Mac vendor/component catalog with manual historical pricing; one owner-validated fence design; arbitrary connected runs and short returns; segment costing/markup/overrides; customer/job/draft estimate records; customer-safe proposal; mobile offline form/calculator; QR-enrolled encrypted CDN catalog; field package export and reviewed manual office import; local backup/recovery. |
| Complete fencing/gates version one | Additional validated fence recipes and single/double gates; design alternatives and issued bid revisions; stock drawing/image library and measured site schematic; approximate crew calendar. |
| Subsequent improvements | Priority-vendor price adapters, automated Gmail collection, receipt extraction, price-history charts, customer-supplied-materials/labor-only bids, on-site signatures and printer integration, native app evaluation, irrigation and other project types. |

The first-trial cut is a proposal for review, not a claim that previously requested drawings, gates or schedules were cancelled. Manual price entry and manual attachment import make the trial useful before external automation is ready. Preserve data needed by later features from the start.

## 4. Main workflows and screens

### Office setup and catalog

The owner opens the local Mac application, sets business/proposal defaults and a backup destination, creates vendors and components, records vendor prices, and reviews design recipes. The owner then explicitly publishes an approved catalog release and registers mobile devices using the desktop QR. Publication excludes customer records, job documents, email credentials and the master database.

Office navigation: Customers and jobs; Catalog and vendors; Designs and drawings; Field submissions; Catalog publishing/device registration; Settings and backup. A job workspace contains Requirements/measurements, Design alternatives, Internal estimate, Customer proposal, Documents and Schedule. Screen layout follows the task; dense office tables do not have to reuse mobile layout unchanged.

### Field visit

Open the installed PWA, check catalog date/update status, select or create a local customer/job, enter requirements and named measured runs, choose a design/options, calculate a preliminary estimate, and save the draft. Show the customer-safe view when presenting the result. Offline work must not require a network request or the Mac to be running.

Mobile navigation: Jobs; New estimate; Design library; Updates; Outbox. Save edits locally as the owner works. Label records as local draft, prepared submission, handed to mail, or office-confirmed; do not imply that local save is an office backup.

### Office review

Prepare a field package, select Mail/Gmail from the device share sheet, and tap Send. On the Mac, select the received attachment and preview the customer, job, measurements, source catalog and preliminary estimate before accepting it. Refresh prices or change designs as needed, compare alternatives and produce a reviewed bid revision. Do not overwrite the submitted field version.

Automatic mail collection later adds items to the same review inbox. Sender/subject filtering alone never authorizes replacing master records.

## 5. Vendors, components, offers and history

A vendor stores name, contact people, phone/email, address, website, branches/locations and notes; it may sell materials, rent equipment or both. A component defines the material/equipment independently of who sells it: description, nominal and actual dimensions, stock length, material/finish, purchase unit and package quantity. Vendor offers add SKU/product URL, exact specification/pack, currency, branch and availability notes.

Each price observation preserves observed/source/effective dates, source type and evidence, tax basis, offer identity, and independently known tiers:

- Retail price.
- Bulk price and qualifying purchase quantity/unit/range.
- Directly quoted contractor price.
- Contractor percentage discount and its stated basis.

Unknown prices stay missing, never zero. Do not apply a contractor discount twice or stack bulk/promotional/contractor discounts unless permitted. Determine bulk eligibility from purchased quantities. Retain quoted and calculated prices separately, and record the selection used by an estimate.

New prices append observations. Corrections link to the original and exclude erroneous observations from selection without deleting provenance. Preserve receipt purchase dates separately from import dates; an unknown historical date remains unknown. Compare equivalent specifications and units, retaining pack rounding, branch, date, tier and tax context. Rental billing periods are explicit; day/week prices are not interchangeable.

All vendors support manual entry. The Mac can later obtain prices through vendor-specific adapters after product/branch/tier mappings and access are validated. Failure leaves the previous observation and its date intact. Public retail pages do not establish contractor-account prices. Receipt attachments can be retained initially; extraction and trend/cross-vendor charts are later features. A paid receipt price does not automatically become a reusable contractor price.

## 6. Customers, jobs, documents and revisions

A customer has contacts, referral source/how they heard about the business, first-contact date, dated contact history and derived last contact. Customers can have multiple jobs and jobsite addresses. A job stores requirements, access/site constraints, runs/connections/gates, selected designs/options, alternatives, notes, documents, estimates and bids.

Use stable identifiers, including for records first created offline. Preserve event/source times separately from import times. A bid revision captures scope, quantities, purchase choices and price observations, recipe/calculator/catalog versions, labor assumptions, markup, overrides, tax treatment, exclusions, selected drawings and totals. Issued revisions are immutable; changes create another revision. A new catalog never silently reprices an existing bid or draft. Reprice a draft only through an explicit action with a visible change summary.

Documents are attached to the job and referenced by the bid revision that used them. Do not expose the entire customer database to every enrolled device: the initial mobile store contains jobs entered/imported there; desktop-to-mobile transfer of selected private jobs is an explicit package action, not part of the generally published catalog.

## 7. Site measurements and estimating geometry

Use a form with any number of runs. A run has an ID, editable label, positive length in feet/inches, start/end connection IDs, design/options and relevant site notes. Direction names N, NE, E, SE, S, SW, W and NW are convenient labels, not bearings. Permit repeated directional names and custom labels such as Tree Return A. Identity determines whether endpoints are shared; matching text or approximate drawing location does not merge posts.

Require no GPS, compass angles, surveying or exact corner geometry. Measured lengths and construction details determine costs. An askew corner does not itself add a surcharge. Single runs, partial enclosures and connected 2–4 ft obstacle returns must work without a four-side property assumption.

For an isolated gate-free run, maximum-spacing bays are `ceil(length / maximumSpacing)` and post positions are bays + 1. Calculate runs individually, then merge shared endpoint posts by connection identity. Internal posts remain per run. Gates carve openings out of facing and introduce compatible supports/hardware/labor; count shared gate supports once. A gate opening cannot exceed or overlap another opening in its run.

Retain per-run/per-bay cuts before aggregating purchases. Short rails and endpoint posts do not disappear into an average per-foot cost. Separate installed quantities, allowance/waste, purchased whole units/packages and unused stock. Only reuse offcuts under an explicit feasible rule; do not build a general cutting optimizer for the trial.

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

Internal job specifications show quantities/purchases, selected unit costs, material cost, person-hours, internal hourly cost, equipment/other expenses, segment costs and selling prices. Initial segments: tear-out/site preparation, equipment rental, material acquisition, post installation, rail installation, cap installation, picket/facing installation, trim installation and final cleanup. Include only applicable segments; rentals are expenses, not automatically separate crew-duration blocks.

Labor effort is person-hours. Two people working six hours supply 12 person-hours, while elapsed workdays are calculated separately. Base selling price is cost × (1 + markup percentage). Precedence: direct segment selling-price override, segment markup, then job default markup. Allow clearing an override. Show effective markup/profit and below-cost flags internally. Markup is not margin. Set tax treatment explicitly; do not inherit inconsistent spreadsheet assumptions.

Customer proposals contain scope, selected inclusions/exclusions/assumptions, segment selling totals where shown, and overall selling price. They exclude material/labor cost splits, internal unit costs, hours, hourly rates, markup and profit. If labor is presented separately, display one selling amount. Generate the customer view/PDF from an allowlisted proposal model, not by hiding columns in the internal document.

Estimates are free. No separately billed drafting fee appears. Record measurement/drawing preparation effort internally and recover it through the project price where appropriate without counting it twice. A preliminary field estimate identifies its pricing date and assumptions; office review produces a separate reviewed/issued revision. Labor-only/customer-supplied-materials bidding is later work; preserve material requirements independently of who purchases them.

## 10. Drawings, images, presentation and scheduling

Maintain uploaded stock drawings for fence/gate construction, installation details and final-look examples. Only the site plan is job-specific. Associate exact drawing versions with the bid. Photorealistic rendering, generated bespoke architectural details and survey-grade mapping are outside version one.

The site schematic preserves measured run lengths at scale with approximate orientation. Label it “Layout schematic; dimensions govern.” Do not stretch measured runs to force an irregular boundary to close; use a schematic break or separate measured runs when necessary. Directional labels remain meaningful even when the illustration is approximate.

Publish drawings and sample images as independently versioned assets. Download lightweight previews, with explicit offline download for chosen designs/full images. Missing optional sample images do not block a priced estimate. Before field use, show which required design assets are present offline.

Default crew: two people, six-hour days, five days/week. Proposed initial workweek: Monday–Friday, editable with job crew size and non-working days. Tentative scheduling begins after materials are sourced/delivered, from an entered anticipated start date. Sequence work dependencies and waiting/curing periods. Respect minimum crew and tasks that cannot speed up linearly with crew count. Show approximate duration and expected daily activity, with potential extension for weather/material/site constraints. No automatic weather forecasting or promised finish date.

On-site signature capture and portable printing are later evaluated capabilities, not prerequisites for the first real-job trial. Bind a captured acceptance to the exact customer-visible bid revision, not a mutable draft. Validate the exact printer/model and system/vendor printing path before promising Bluetooth printing. Track these in the native-capability log rather than assume they require native installation.

## 11. CDN packages, enrollment and key changes

### Modular releases

A small current-release manifest lists module IDs/versions, schema/engine compatibility, content-addressed URLs, sizes/checksums and encryption key IDs where applicable. Start with one current-pricing package and one design-data package; drawings and images are individually versioned assets. Retain full vendor-price history on the Mac rather than shipping the entire history to phones.

Reuse unchanged files/addresses and encrypted outputs while content and key are unchanged. Clients download only missing or changed modules. A key change necessarily produces new encrypted outputs even when the plaintext is unchanged. Publish a complete valid static release with its manifest; do not expose a manifest whose referenced files are unavailable. Routine catalog publication need not be an application-code update.

Check on launch/foreground, at a modest interval while in use, and via Check for updates. Never promise updates while the app is closed. Keep manifest requests current and exclude them from offline app-shell cache responses. Stage and validate required related data before switching the active release in one transaction. A failed/incompatible update leaves the prior usable release in place and explains the problem. Keep optional media downloads independent. Show active catalog date/version, last successful check and stale/offline status.

### Enrollment and private data

One random business catalog key protects sensitive prices, internal rates and other private catalog data using authenticated encryption. Public design/sample assets may remain unencrypted when intentionally approved for publication. Never publish decrypted private catalogs, keys, office credentials, customer/job data or the SQLite database with the PWA.

The Mac retains the key locally and displays its enrollment QR on explicit action. Scan in the installed PWA once; store the imported key separately from application assets. Retain it across normal PWA updates. Provide QR-image selection for an enrollment image emailed by the owner, since a device cannot scan its own displayed email with its rear camera. Emailing the QR shares a reusable catalog credential; it is an explicit owner distribution action, not an automated action by default.

### Key-change workflow agreed with the owner

1. The owner requests a catalog-key change on the Mac. Generate a new key and key ID.
2. Re-encrypt all affected private modules, assign new package identities/hashes, and prepare a consistent release referencing the new key.
3. Publish the replacement release. Remove superseded encrypted package files from the current production publication; retain unrelated/shared assets still referenced by supported releases. Historical deployment URLs and already downloaded copies are separate from the current file set and must not be described as revoked or erased.
4. A device seeing an unknown key ID shows **Registration update required** with instructions to visit the office or use an enrollment QR supplied by the owner. Detect this through metadata; a generic decryption error is not the expected user experience.
5. The new encrypted package may be staged, but it cannot replace active usable data until the new key is registered and decryption/validation succeeds. If staging is not useful, defer that download until enrollment. Neither path exposes plaintext or clears the old catalog/jobs.
6. After registration, retry/install the pending release. Activate the new key/catalog together only after successful validation. Preserve access needed for existing local records and issued revisions. Updates requiring the new data cannot use the old key or pretend the old data is current.

Normal price/design updates under the same key require no re-registration. App updates also require no re-registration. Storage clearing, a new browser/device/origin or a deliberate key change may require enrollment again. Rotation protects future releases; it cannot retract a previously downloaded/decrypted catalog. Keep previous Mac keys as local recovery material for delayed submissions/archives rather than publishing them to newly enrolled users.

## 12. Field packages, import and recovery

An immutable portable field package includes schema/package/device/business IDs, created time, customer/job IDs, known office base revision, catalog/design/calculator versions, selected pricing and assumptions sufficient to explain the result, runs/options, draft estimate and content checksum. Retain its body in the local outbox. Keep package size modest; large photos/documents are explicit separate attachments rather than silently embedding the full library.

Use the native share sheet exposed by the browser; the user chooses the mail target and taps Send. Provide download/save for unsupported file sharing. Do not rely on mailto attachments or assume recipient/subject prefill works everywhere. A successful share means handed to a target, not delivered/imported. Re-sending the same content keeps the package ID; changed content creates a new linked revision/package.

The Mac importer validates schema, size, references and checksum, previews changes, and deduplicates by package ID plus content hash. Same ID/same content is harmless; same ID/different content is a conflict. Existing-record revisions changed since field departure require review, never silent overwrite. Preserve the received submission and commit accepted changes/import ledger together. A pending/cancelled import must not leave half a job in the master database. Do not execute attachment content or treat notes as agent instructions.

For the first trial, mark an outbox submission office-confirmed only through explicit owner confirmation after import; do not add a synchronization server just for acknowledgments. Later Gmail collection uses the same importer/inbox while the Mac is awake and authorized. Store future mail credentials outside PWA/catalog packages. Automated collection does not automatically send messages or accept arbitrary submissions.

Mac backup includes SQLite, attachments, settings, catalog release artifacts and recovery keys. Restore must preserve identities, issued revisions and import deduplication records. Mobile drafts/outbox need export/recovery; browser persistence is not a backup. Storage quota failures keep the last saved version and display a clear unsaved/error state. Normal application updates preserve enrollment, saved jobs and outbox; migrate compatible data transactionally and reject unsupported versions without clearing it.

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

Acceptance must cover useful behavior, not only transport. Apply each case to the increment that delivers it; later drawing/gate/calendar cases do not block the first-trial scope:

1. Enter a real vendor offer and retail/bulk/contractor arrangements; add a new observation without rewriting history or an existing estimate. Demonstrate missing-price and non-stacking discount behavior.
2. Produce the 150 ft geometry examples, connected 10/3/10 ft example and a 2–4 ft return with real short supports/purchases. Adding an opening removes its facing and counts correct gate supports when the gate increment is delivered.
3. Save a customer/job and compare design alternatives. Reprice a draft explicitly; retain the issued revision unchanged.
4. Change default/segment markup and direct selling override, clear the override, and verify a customer proposal contains no hidden internal cost/hour/markup fields in its rendered/exported data.
5. Preserve a field draft/outbox across closure and offline reopening; send/import the same package twice without duplicating a job, and surface a concurrent office edit for review.
6. Enroll once, download only changed CDN resources, reject a failed/incompatible update without damaging active data, and read the encrypted catalog offline. Preserve enrollment and jobs across a real application-version update.
7. Rotate the catalog key, publish re-encrypted packages and remove the old packages from the current publication. An old-key device must request re-registration and preserve its work; registration with the new QR enables installation. Test the emailed-image enrollment route if used.
8. For drawings/calendar delivery, preserve measured lengths, attach the correct stock drawing revision, and generate a tentative schedule for two people at six hours/day without exposing labor cost calculations.
9. Back up/restore Mac records, attachments and keys; recover and deduplicate a delayed field submission.
10. Validate implemented field workflows on the owner's iPhone/iPad. Record Android as untested until hardware is available. Do not claim phone behavior from a desktop-only pass.

### Owner review points

- Confirm the proposed first-trial cut versus the complete fencing/gates version-one scope in section 3.
- Confirm React Native Web/Expo for mobile, React/Node for office, and the realistic native migration boundary in section 14.
- Select/populate the first owner-validated recipe before calculation implementation; the example spacings do not supply missing board joints or other recipe values.
- Confirm Monday–Friday as the initial editable workweek. Define tax/markup defaults through business settings rather than inventing them from the workbook.
- Review the catalog-key change/re-registration behavior in section 11, including retention of existing work and removal limits for already distributed copies.

After owner review and corrections, approve the written spec before creating the backlog/implementation plan. No product scaffolding, new cloud service, native app enrollment or implementation tasks are started by this document.
