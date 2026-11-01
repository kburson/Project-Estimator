[08:50:53]
**Verdict: Changes needed before planning.** The direction, the evidence handling and the key-change rules are sound. But the first-trial cut has one coherence gap that matters to a real customer (C1), and a few areas are loose enough that two implementers could build incompatible things (C3 to C7). Each fix is small and none adds infrastructure.

## Findings

**C1 — blocking — the first trial can't freeze a proposal it gives to a real customer.** Spec §3 first-trial row, §1 ("produce and retain"), §6, §15 item 3.
- The first trial delivers a "customer-safe proposal" but only "draft estimate records". Issued bid revisions are deferred to complete v1.
- Example: the owner hands a customer a $14,200 proposal from a draft. Later they reprice the draft after a catalog update or a field re-import. The record of what was actually quoted is gone. That contradicts §1 and §6 ("Issued revisions are immutable").
- Acceptance item 3 mixes trial behavior (save a job, reprice a draft) with v1 behavior (compare alternatives, issued revision), so the increment boundary is unclear.
- **Fix:** move "issue one frozen revision from a draft; the proposal is generated only from an issued revision" into the first trial. Keep alternatives and revision comparison in v1. Split item 3 to match.

**C2 — important — the first trial has no way to price work outside the one recipe.** §3, §8 ("Missing construction details… produce an incomplete estimate"), §9.
- The trial has one recipe and no gates. There is no owner-entered line item or allowance anywhere in the spec.
- Example: a typical residential job has one walk gate plus haul-off of old fence. The calculator either leaves the gate out (the bid is too low) or marks the estimate incomplete (no proposal). The owner falls back to the spreadsheet, which defeats the trial.
- **Fix:** add a manual priced line item to the first trial. It needs a cost, a segment, a customer-facing description, the normal markup/override rules, and to be kept in the revision. Whether gates also move into the trial is an owner decision (below).

**C3 — important — it's unclear which segment carries material cost.** §9 segments list; earlier spec's "Material-acquisition expenses".
- "Material acquisition" could mean all material purchases. Or it could mean only sourcing/pickup/delivery effort and fees, with post/rail/picket materials inside their installation segments.
- Segment markups, overrides and the per-segment proposal display all depend on this. Two builds would show different segment totals and, once segment markups differ, a different overall price.
- **Fix:** define it in one sentence. The earlier spec suggests this reading: each installation segment = its materials + labor + expenses, and material acquisition = sourcing/pickup/delivery effort and fees.

**C4 — important — the published pricing package isn't specified well enough for office and phone to get the same result.** §5, §8 ("same input fixtures… same output"), §11 Modular releases.
- **Offer selection is undefined.** When several vendors offer the same component, nothing says which one the calculator picks (cheapest, preferred, owner-pinned). The Mac (full history) and the phone ("one current-pricing package") could each pick differently.
- **Tier data:** bulk eligibility depends on the job's purchased quantity, so the package must carry tier rows, not one resolved price.
- **Settings have no home:** labor rates, default markup, tax settings and proposal business text aren't assigned to any package.
- **Fix:** a release publishes owner-selected default offers per component, with their tiers, plus a private business-settings module. The calculator takes these as explicit inputs. "Parity" means the same release and inputs give the same output.

**C5 — important — it's undefined whether local records and field packages depend on the catalog key.** §11 step 6 ("Preserve access needed for existing local records"), §11 last paragraph ("previous Mac keys… for delayed submissions"), §12 package contents.
There are two designs that don't work together:
- (a) drafts reference encrypted catalog data, so the device keeps a ring of old keys;
- (b) drafts store their own pricing snapshot.

"Recovery keys for delayed submissions" also suggests field packages are encrypted with the catalog key, but §12 never says so.
- Example: a device re-registers, its old key is replaced, and drafts that point at catalog v7 ciphertext can no longer be displayed.
- Example: the owner shows the new QR before publishing. The device has to hold the new key as pending without dropping the active one. Step 6 implies this but doesn't say it.
- **Fix:** state that
  - drafts and outbox store their own resolved pricing snapshot in device job storage, not encrypted with the catalog key;
  - field packages are plaintext with a checksum, or say explicitly if they are encrypted;
  - a device holds one active key plus at most one pending key, and drops the old key only after the new release validates.

**C6 — important — a customer entered at the office and again in the field becomes two customers.** §6 last paragraph, §12 importer (dedup is by package ID plus content hash only).
- Example: a customer phones the office and the owner enters them on the Mac. At the site, the phone doesn't have them, so the owner creates the customer again. Import adds a second customer and splits the contact history.
- Office-to-phone job transfer is called "an explicit package action", but it has no transport and isn't in any §3 increment. It can't go through the CDN, because §11 forbids publishing customer data.
- **Fix:** in the first trial, the import preview offers "link to existing customer/job" for records created in the field. Either put office-to-phone transfer in a named later increment, or define it as the same file/email route.

**C7 — important — app/catalog version mismatch has no defined behavior.** §11 Modular releases ("schema/engine compatibility"; "supported releases"), §12 last paragraph, §15 item 6.
- Undefined: whether there is one current manifest or one per engine version, and what an older cached app shows when the manifest needs a newer engine.
- Undefined: whether a newly activated app must still read the previously active catalog schema while offline, and when a new app version takes over (not in the middle of an edit).
- Example: a phone offline for a week reopens with an updated app and an older catalog, and can no longer price its drafts.
- The full app-version upgrade is the one path the probe didn't test, so this needs to be spelled out before acceptance item 6 can be checked.
- **Fix:** add an "App update required" state, separate from "Registration update required". Never publish an app version that can't read the catalog currently active on devices. A new app version takes over only at launch or a safe point.

**C8 — minor — acceptance cases aren't tagged by increment, and phone/Mac parity isn't tested.** §15.
- "Apply each case to the increment that delivers it" leaves items 2, 3 and 6 partly ambiguous.
- No case runs the shared calculator fixtures on the iPhone/iPad and compares them with the Mac. That parity is constraint 3.
- **Fix:** tag each case Trial or V1, and add a device parity case.

**C9 — minor — capability log and spec don't fully agree with the evidence.**
- NC-07 lists "pasted enrollment recovery", but spec §11 offers only QR scan and QR-image selection.
- NC-04 doesn't record that the iPhone reported `persistent: false` (`iphone-environment-user-reported.json:12`).
- NC-04 also doesn't say that keeping enrollment across a full app-version upgrade is untested. Spec §2 does say this.
- NC-02 is marked "Limited in PWA" without a trial, which conflicts with the log's own evidence rule. Either cite platform documentation or mark it Candidate.

**C10 — minor — no default rule for turning cut pieces into purchased stock.** §7 ("Only reuse offcuts under an explicit feasible rule").
- If a recipe declares no rule, the implied default is one stock unit per cut piece. With several 2–4 ft returns cut from 16 ft boards, that noticeably overstates materials.
- **Fix:** each recipe must declare its stock/cut rule, or say plainly that "no reuse" is the default and is shown as unused stock.

## Owner decisions needed (not defects)

1. **Gates in the first trial:** add a single gate, or rely on the C2 manual line item until the gate increment.
2. **Friend devices in the first trial:** enrolled devices receive contractor prices, internal labor rates and markup defaults (§1 says so). Decide whether friends enroll now or after the trial.
3. **Tax:** is material sales tax part of internal cost, a customer-facing line, or both? Does the proposal show tax?
4. **Customer discount:** the workbook's Bid sheet has a discount, and neither spec has one. Is a visible customer discount needed, or are overrides enough?
5. **Production origin:** fix the production domain before trial data exists. Changing it later loses enrollment and phone drafts (§11), and the probe used `kburson-estimator-probe.pages.dev`.
6. Already listed in §15: the first recipe, Monday–Friday workweek, markup defaults.

## Strengths and coverage

- Evidence is reported accurately. I checked the iPhone/iPad V4 observations and the earlier email-attachment evidence: Android and app-upgrade gaps are stated as untested, and nothing is overclaimed.
- The reference post counts check out: 35, 20 and 26 for 150 ft; five bays and six posts for the 10/3/10 path.
- Key-change limits, no silent repricing, the allowlisted proposal model, price-history provenance, idempotent import and the native-migration caveats all hold up.
- The deferred features are clearly deferred, not missing.

**Limits:** I reviewed documents only. I didn't run the probe or check Cloudflare Pages deployment details, so the deployment mechanics in C7 are framed as a spec gap, not a platform claim. I didn't open the `.numbers` workbook. No files were written.
