[10:06:32]
# Second independent specification review: Project Estimator PWA v1 (revised)

**Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), high effort, one pass, no delegation, read-only.
**Artifacts:** `docs/superpowers/specs/2026-11-01-project-estimator-pwa-v1-design.md`, `docs/design/mobile-native-capability-log.md`, the round-1 review, the author assessment and `round-2/change-response.md`.

## Verdict

**Ready for owner review.**

All ten round-1 findings are resolved, and none of the fixes contradicts another part of the spec. Two minor wording gaps remain (R2-1, R2-2). Each needs about one sentence, and the owner can settle both during spec review. Neither blocks planning.

## Resolution of C1–C10

| ID | Status | Reason | Where |
| --- | --- | --- | --- |
| C1 | Resolved | Present to customer, PDF export and proposal sharing each save an immutable quote snapshot. Repeating the action with no changes reuses the snapshot; changes produce a new ID. Old quotes are shown from their saved result and never recalculated. The internal draft preview stays separate. Acceptance 4 tests that the presented quote survives a reprice. A terminology leftover is noted in R2-2. | §3 trial row; §4 Field visit (l.51); §6 (l.84–86); §12 package contents (l.183); §15.4 |
| C2 | Resolved | Manual priced items carry: description, segment, quantity/unit, unit cost, cost category, source and a manual flag. They use the normal markup/override rules and are kept in the snapshot. They cannot make a recipe's missing inputs valid. For the manual gate, the owner enters runs without the opening and confirms supports and facing aren't counted twice. That fits the trial and claims no geometry validation. | §9 (l.124); §15.3 |
| C3 | Resolved | Each material is charged once, to the segment that consumes it. Acquisition covers only sourcing/pickup/delivery effort and fees. Pooled purchases are allocated by installed requirement, and cent rounding preserves the purchase total. | §9 (l.122); §15.5 |
| C4 | Resolved | The owner pins a default offer per component, and a job can override it explicitly. Tiers, units, discount basis and stacking conditions are shipped instead of one resolved price. Within an offer, the calculator picks the lowest eligible cost after pack rounding. Business settings live in the existing private pricing module and are snapshotted per quote. Parity means the same release plus the same inputs. | §5 (l.72); §9 (l.126); §11 Modular releases (l.148); §15.1, §15.11 |
| C5 | Resolved | Drafts, quotes and the outbox are self-contained and kept in ordinary device storage. Field packages are plaintext JSON with a checksum. A device holds at most one active and one pending key. The new key and catalog are committed together only after validation, and the old ones are discarded afterwards. Retired Mac keys are kept only to recover old catalog archives. These sections agree with each other. | §6 (l.86); §11 steps 5–6 and closing paragraph (l.174–177); §12 (l.181); §15.9, §15.10 |
| C6 | Resolved | The import preview offers Create new or Link to existing, with confirmation and no automatic merge by name. Source-ID mappings are stored and reused for later packages. A missing base revision triggers a reviewed merge. Office-to-phone transfer is assigned to complete v1, using the same file/email route. | §6 (l.88); §12 importer (l.187); §15.6, §15.15 |
| C7 | Resolved | One current manifest. App update required and Registration update required are separate states. App updates activate only at launch or a safe point, and the previous shell is kept until then. Routine trial schemas must stay compatible. No unattended breaking migration. A real app-version upgrade test is required. Small leftover: §11 step 3 (l.172) still says "supported releases" (plural). With one manifest this is harmless. | §11 Modular releases and Compatibility (l.148, 156–160); §15.7, §15.8 |
| C8 | Resolved | Every acceptance case is tagged Trial or Complete v1. Case 11 adds Mac/iPhone/iPad calculator parity, with Android recorded as deferred. | §15 (l.218–234) |
| C9 | Resolved | NC-02 is now a Candidate. NC-04 records `persistent=false` and that a full app upgrade is untested. NC-07 matches the spec. "Tested pasted-enrollment fallback" (§11, l.166) matches the probe evidence, which is desktop Chrome only (`docs/research/2026-11-01-encrypted-cdn-probe.md:14,28`). | capability log NC-02, NC-04, NC-07; spec §11 l.166 |
| C10 | Resolved | If no cut rule is configured, the default is no offcut reuse. Unused stock and its cost are shown with a notice. Any owner reduction is a documented manual adjustment, and no optimizer is added. | §7 (l.98); §15.2 |

## Remaining findings

**R2-1 — minor — the basis for customer tax is undefined once segment markups or overrides apply.**
- **Where:** §9, l.126: "Optional tax charged to the customer is calculated separately on owner-selected taxable selling categories."
- **The ambiguity:** "selling categories" could mean whole segments, or the cost categories of §9 l.124 (material, labor, equipment, other). Segment selling prices mix all cost categories. A direct override sets one segment amount with no split.
- **Failure example:** post installation costs $1,000 materials plus $500 labor, and has a $2,000 override.
  - Build A, taxing the whole segment, taxes $2,000.
  - Build B, taxing materials only, taxes $1,333.33 (the override split in proportion to cost).
  - The customer is shown two different totals, and acceptance 5 can't be checked.
- **Second gap:** the spec doesn't say whether purchase tax applies to a manual material item's directly entered unit cost.
- **Only matters if** the owner charges customer tax in the trial.
- **Smallest correction:** add one sentence. The customer-tax basis is the final selling amount of owner-selected segments (after overrides), and manual items follow their segment. A manual material unit cost is entered with its own tax-included flag.

**R2-2 — minor — trial wording still mixes "frozen quote snapshot" with "issued revision".**
- **Where:**
  - §4 Office review (l.57) says "compare alternatives and produce a reviewed bid revision" without a trial/v1 tag.
  - §9 (l.130) says "office review produces a separate reviewed/issued revision".
  - §12 restore (l.191) lists "issued revisions" but not frozen quote snapshots.
  - §6 (l.84) says a trial snapshot "may be labeled Preliminary".
- **Failure example:**
  - The owner reviews a field draft on the Mac and exports the final PDF for the customer. One build labels it Preliminary, so the customer sees "preliminary" on what is meant to be a firm bid.
  - Another build reads §4 and §9 as requiring a separate issued-revision workflow in the trial.
- **Smallest correction:** add one sentence. In the trial, an office or field presentation/export freezes the same quote snapshot, with Preliminary or Issued status chosen when it is frozen. Comparing alternatives and revisions stays in complete v1. Restore preserves frozen quote snapshots and source-ID mappings.

No blocking or important defects remain.

## Owner decisions (not defects)

1. Approve the first-trial cut in §3 and §15 "Owner review points":
   - one validated automatic recipe
   - manual allowances, including gates
   - frozen presented quotes
   - manual reviewed imports
2. Choose and fully fill in the first validated recipe, including its cut/joint rule or acceptance of the no-reuse default.
3. Decide whether the trial charges customer tax at all. If it does, confirm the basis (see R2-1). Enter the labor, markup and tax settings before the first publication.
4. Decide whether trial snapshots exported from the office may carry an Issued/Final label or are always Preliminary (see R2-2).
5. Fix the stable production origin before any real job data is collected.
6. Confirm the Monday–Friday workweek. The customer discount stays deferred, as already decided.

## Review limits

- I reviewed documents only. I didn't run the probe or the tests, and didn't check how Cloudflare Pages deploys.
- I didn't open the `.numbers` workbook or any key material.
- I checked the probe research doc (`docs/research/2026-11-01-encrypted-cdn-probe.md`) only to confirm the C9 evidence wording.
- Deferred features weren't reopened. Things like app-shell caching and how deployments are bundled belong in the implementation plan and weren't assessed.
- This was one pass and no files were written. The author saves this report.
