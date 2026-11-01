# First Usable Project Estimator Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Let the owner make, preserve and export an explainable real fence quote on the Mac, then perform the same calculation offline on an enrolled iPhone/iPad and review its returned attachment in the office.

**Architecture:** One npm/TypeScript workspace contains a pure shared calculation/contracts package, a local Node/SQLite office service with a React UI, and a static Expo/React Native Web PWA. The office publishes encrypted, versioned catalog modules to a static CDN; the field keeps ordinary local job snapshots and returns immutable plaintext JSON attachments through user-selected sharing. Small web/Mac storage, crypto, file and lifecycle adapters isolate platform APIs; no native adapters or hosted business service are built.

**Tech Stack:** Node 26.8.1, TypeScript, React, Vite 8.3.5, Expo SDK 58 (`expo` 58.0.22), React Native Web 0.21.4, Node `node:sqlite`, Zod 4.6.7, decimal.js 10.6.0, Dexie 4.4.7, pdf-lib 1.17.1, Vitest 5.0.5; Web Crypto, IndexedDB, service workers and the browser share/file APIs. Exact compatible React/React Native and auxiliary tool pins are recorded in the dependency table below. Node's SQLite API is release-candidate, not represented as stable: pin the runtime and exercise persistence/backup at that version.

**Spec:** `docs/superpowers/specs/2026-11-01-project-estimator-pwa-v1-design.md`; supporting platform evidence: `docs/design/mobile-native-capability-log.md`. The owner's request authorizes this plan after Claude review clearance. It does not authorize implementation or publication. Earlier Swift/LAN plans are historical and are not execution instructions.

## Global Constraints

- “Mac-only office application: local React web UI, Node service and SQLite master database. No Windows requirement.”
- “Use React Native Web with Expo for the mobile UI, retaining a possible native React Native build later.”
- “Shared TypeScript calculations and contracts. Do not implement different pricing engines for office and field.”
- “Cloudflare serves static application files and versioned data packages. No hosted business database or always-running cloud application backend.”
- “No household/device DNS changes, local HTTPS certificate setup, or QR exchange per connection.”
- “Use decimal-safe arithmetic with money serialized as decimal strings, explicit units and deterministic rounding.”
- “Store measured lengths in a fixed small integer unit sufficient for sixteenths of an inch.”
- “Unknown prices stay missing, never zero.”
- “Base selling price is cost × (1 + markup percentage). Precedence: direct segment selling-price override, segment markup, then job default markup.”
- “The first version does not add an independent job-encryption/key-ring system.”
- “The trial uses the already tested UTF-8 JSON attachment with a checksum; it is plaintext, not encrypted with the catalog key.”
- “A device holds at most one active key and one pending key.”
- “Android is unavailable and untested; it remains a later validation item, not a blocker for the owner's trial.”
- Implement only section 3's **First real-job trial** and section 15 acceptance cases **1–11**. Automated gates, additional recipes, alternatives/revision comparison, drawings, calendar, office-to-mobile job transfer, Gmail automation, vendor fetching, OCR, signatures, printing, native distribution and irrigation are deferred.
- Preserve `Heather-Fence Bid.numbers`, existing documents and disposable `probes/pwa-feasibility`; neither workbook formulas nor probe code become production authority.
- No automatic network access inside calculation, no remote executable recipes, no accounts, no per-device revocation service and no generalized synchronization system.
- Owner enters real prices, validates the single recipe, confirms labor/markup/tax settings and selects the stable production HTTPS origin. Synthetic fixtures are conspicuously test-only and cannot be selected/published for real quotes.
- Commands below are future execution instructions. During this planning/review task run none of the scaffold/install/build/publish/commit commands.

## Review Focus

1. Repeated run labels, very short returns and shared endpoint identities must preserve real posts and cut purchases without name-based merging (Task 1 geometry tests).
2. A missing price/rate, fractional pack threshold or unpermitted contractor discount must yield named incompleteness or the correct eligible arrangement, never a cheap-looking valid quote (Tasks 2–3).
3. A failed local save, duplicate click or quota failure must not advance a saved/outbox/presented indicator or replace the last durable state (Tasks 4, 5 and 7).
4. A pending key scanned early, an interrupted replacement and an actual application upgrade must leave the active catalog, enrollment and existing job snapshots usable (Tasks 8 and 10).
5. A delayed submission with a separately created customer and stale/missing base revision must preserve the original, honor saved identity mappings and require explicit merge choices (Task 9).

---

## Delivery order and boundaries

There are **10 deliverables**. Tasks 1–5 deliver a usable local Mac quote before mobile integration. Tasks 6–9 add static publication and field round trips. Task 10 proves recovery and the real-device release. Do them in order; a task is complete only when its stated checks pass and its change is committed. The plan's skill header applies only to a separately authorized future implementation. This request ends at plan/SAR review.

Before Task 1 calculation implementation, obtain the owner's populated single-recipe worksheet described below. Contract/test scaffolding may proceed with test-only data; do not guess construction rules to remove that checkpoint. Before real quoting/publication, complete all setup checks in Task 4. Production domain/Cloudflare project access is needed only before Task 10's production deployment; synthetic preview tests can run earlier.

### File ownership map

| Area | Files and responsibility |
| --- | --- |
| Workspace | `package.json`, `package-lock.json`, `.nvmrc`, `.gitignore`, `tsconfig.base.json`, `vitest.config.ts`: pinned workspace, checks and explicit source/test roots. |
| Portable domain | `packages/domain/src/{contracts,recipe,geometry,pricing,estimate,quotes,proposal,canonical}.ts`, `packages/domain/src/index.ts`: schemas and pure calculations. `packages/domain/src/contracts.ts` owns every serialized model below. |
| Test fixtures | `packages/domain/test/fixtures.ts`: synthetic populated recipe, catalog, customers, jobs and deterministic identifiers/times; `packages/domain/test/*.test.ts`: domain behavior. Nothing in this directory is copied to app catalog data. |
| Portable package workflow | `packages/exchange/src/{contracts,catalog,field-package,import-plan}.ts`, `packages/exchange/src/index.ts`: validation, module/package construction and reviewed import plans; no Node/browser storage. |
| Office | `apps/office/src/server/{database,catalog-store,job-store,quote-service,publish-service,import-service,backup-service,http}.ts`; `apps/office/src/ui/{App,Catalog,Setup,JobEditor,Estimate,Proposal,Publishing,Imports,Backup}.tsx`; `apps/office/src/platform/{crypto,files,pdf}.ts`: local service/UI and adapters. |
| Field | `apps/field/App.tsx`, `apps/field/src/screens/{Jobs,Job,Designs,Updates,Outbox}.tsx`; `apps/field/src/{store,job-service,catalog-client,enrollment,update-controller}.ts`; `apps/field/src/platform/{crypto,qr,files,sharing,lifecycle,pdf}.ts`: only web adapters and React Native Web screens. |
| Static release | `apps/field/public/{manifest.webmanifest,icon-192.png,icon-512.png}`, `apps/field/scripts/{build-sw,stage-release}.mjs`, `apps/field/src/sw.ts`: app-shell/update behavior and allowlisted deploy staging. Generated files live in ignored `.local/` and `dist/`, not alongside keys/business data. |
| Operator docs | `docs/trial/{recipe-validation,setup,quote-workflow,publishing,field-workflow,recovery,acceptance}.md`: short real-use procedures and evidence. |

Each task lists its exact files; no existing probe files are modified. A lightweight manual tab switch is enough for office navigation; no office routing/state-management library is needed. Mobile uses a small explicit screen switch in `App.tsx` with Expo static web output. No shared UI abstraction is required between dense office forms and mobile controls.

### Common serialized contracts (implemented in the task that first uses them)

Use `z.strictObject` schemas (including the customer-only `ProposalModel`); exported TypeScript types are `z.infer` of those schemas. Schema version is the literal `1`. Persistent record identities (business, device, customer, job, run, connection, quote, package, vendor, component, offer and observation) are UUID strings generated at creation and preserved on import. Recipe rule keys, segment keys, tier/arrangement keys, version strings and key IDs are scoped nonempty semantic strings; they are not UUIDs. Times are ISO UTC strings; source/observed/effective dates may be `null` and must not be replaced by import time. Money/rates/quantities are nonnegative finite decimal strings, except signed profit/adjustment outputs. Rates are fractions (`"0.10"` means 10%); UI displays percentages. All lengths are integer `u16` units (1/16 inch). Bound a run to `1..1_920_000` u16 (10,000 ft), jobs to 500 runs and 500 manual items, attachments to 5 MiB JSON; these generous implementation limits are visible errors, not silent clipping. IDs, text length limits and relationship checks are validated at every file/module/service boundary.

```ts
// Task 1: packages/domain/src/contracts.ts
export type SegmentId = 'site-prep' | 'equipment' | 'acquisition' | 'posts'
  | 'rails' | 'cap' | 'facing' | 'trim' | 'cleanup';
export type Money = string;
export type Run = { id: string; label: string; lengthU16: number;
  startConnectionId: string; endConnectionId: string; notes: string };
export type MaterialRule = { id: string; componentId: string; segment: SegmentId;
  basis: 'post' | 'bay' | 'run-coverage'; countPerBasis: string;
  coverageU16: number | null;
  cut: null | { length: 'bay' | 'fixed'; fixedU16: number | null; stockU16: number };
  wasteFraction: string };
export type AttachmentRule = { id: string; componentId: string;
  segment: SegmentId; materialRuleId: string; unitsPerInstalledPiece: string };
export type LaborRule = { id: string; segment: SegmentId;
  driver: { kind: 'material-rule'; ruleId: string } | { kind: 'run-foot' };
  personHoursPerUnit: string };
export type Recipe = { id: string; version: string; name: string;
  validation: { status: 'draft' | 'validated'; purpose: 'production' | 'test-only';
    validatedBy: string | null; validatedAt: string | null; notes: string };
  maxSpacingU16: number; materials: MaterialRule[];
  attachments: AttachmentRule[]; labor: LaborRule[];
  cutRule: 'no-offcut-reuse'; assumptions: string[]; exclusions: string[] };
export type Requirement = { id: string; componentId: string; segment: SegmentId;
  installedUnits: string; requiredPurchaseUnits: string;
  cuts: { runId: string; bayIndex: number | null; lengthU16: number }[];
  unusedStockU16: number; sourceRuleId: string };
export type Issue = { code: string; path: string; message: string };
export type GeometryResult = { bays: { runId: string; lengthsU16: number[] }[];
  postCount: number; requirements: Requirement[]; issues: Issue[] };
```

A material `post` basis uses unique post identities; a `bay` basis retains each bay and cut; `run-coverage` uses `ceil(run.lengthU16 / coverageU16)` per run, never all-run averaging. Waste is additional purchased quantity, not installed quantity. A cut purchases one stock unit per piece with no reuse; reject a cut longer than its stock. Non-cut items use declared units. Attachment counts derive from installed pieces of their referenced rule, never purchased spare stock. Shared endpoint post requirements are allocated once across incident runs by sorted run ID; differing supports are unsupported by the single-recipe trial. The owner must validate that this deliberately small recipe vocabulary represents the chosen recipe; do not expand it into an arbitrary formula language.

## Task 1: Shared workspace and owner-validated geometry

**Files:** Create workspace files above and `scripts/verify.mjs`; `packages/domain/{package.json,tsconfig.json}`; `packages/domain/src/{contracts,recipe,geometry,index}.ts`; `packages/domain/test/{fixtures,geometry.test}.ts`; `docs/trial/recipe-validation.md`.

**Interfaces:** Produces `parseMeasuredLength(feet: string, inches: string): number`; `validateRecipe(recipe: Recipe): Issue[]`; `calculateGeometry(runs: Run[], recipe: Recipe): GeometryResult`. These are synchronous, deterministic and platform-independent. `calculateGeometry` returns named issues for invalid recipe/runs; it does not silently produce a complete estimate. Task 1 also defines the test-fixture API `syntheticRecipe()`, `syntheticRuns(lengthsFeet: number[], connected?: boolean)` and `id(n: number)` **from the test fixture file only**, using valid deterministic UUIDs.

- [ ] **Step 1: Record the actual recipe worksheet and scaffold only the needed workspace.** In `docs/trial/recipe-validation.md`, include fields for owner/name/date; fence height/coverage/gap; maximum spacing; post and support/joint details; material stock lengths/pack units; per-bay/coverage quantities; fastener attachment counts; labor work-unit assumptions; no-offcut-reuse rule; options excluded from this recipe; owner validation result. Enter the owner's supplied values and evidence, or keep the recipe nonselectable with named missing fields. No example spacing constitutes structural validation. Preserve historical workbook source dates and discrepancies. The checkpoint is completion of this worksheet before implementing the real recipe calculation.

  Establish private root workspaces `apps/*` and `packages/*`, ESM, strict TypeScript, and create `@estimator/domain` now; reserve `@estimator/exchange`, `@estimator/office`, `@estimator/field` for their owning tasks. Root `test` is `vitest run`; `typecheck` runs `tsc --noEmit` for each workspace; `verify` runs typecheck, tests and both app builds through a small Node script that stops on the first failure. Configure Vitest `include` as `packages/**/*.test.ts` and `apps/**/*.test.ts`; exclude `probes/**`, `dist/**` and `.local/**`. `.gitignore` adds `node_modules/`, `.local/`, `dist/`, `.expo/`, coverage and SQLite sidecar files without hiding source fixtures.

```json
// Root package.json: establish these keys; dependency pins are below.
{
  "name": "project-estimator", "private": true, "type": "module",
  "workspaces": ["apps/*", "packages/*"],
  "engines": { "node": "26.8.1" },
  "scripts": { "test": "vitest run", "typecheck": "npm run typecheck --workspaces --if-present",
    "dev:office": "npm run dev --workspace @estimator/office",
    "dev:field": "npm run start --workspace @estimator/field",
    "build": "npm run build --workspaces --if-present",
    "verify": "node scripts/verify.mjs" }
}
```

  Create `scripts/verify.mjs` in this step: use `spawnSync('npm', args, {stdio:'inherit'})` for `['run','typecheck']`, `['test']`, `['run','build']`; exit nonzero immediately on failure. Add it to this task's files/commit. Pin `.nvmrc` to `26.8.1`. Install only the dependencies needed at each task with exact versions and retain the lockfile; never run a generator inside `probes/`.

- [ ] **Step 2: Write the geometry tests and synthetic fixture.** The fixture recipe is visibly `purpose:'test-only'`, with 8-ft maximum spacing, one post per unique identity, two bay-length rails per bay from 8-ft stock, no waste and one synthetic fastener rule. Its validation status stays `draft`, purpose is `test-only`, and owner name/date stay null. Its numeric values are test fixtures, not construction advice. `syntheticRuns` gives every run the same label `'N'`; when connected, run `i` ends at run `i+1`'s start ID.

```ts
import { describe, expect, it } from 'vitest';
import { calculateGeometry, parseMeasuredLength } from '../src/index.ts';
import { syntheticRecipe, syntheticRuns } from './fixtures.ts';

describe('measured geometry', () => {
  it.each([[54, 35], [96, 20], [72, 26]])('150 ft at %i in', (inches, posts) => {
    const recipe = { ...syntheticRecipe(), maxSpacingU16: inches * 16 };
    expect(calculateGeometry(syntheticRuns([150]), recipe).postCount).toBe(posts);
  });
  it('counts connected returns by identity and retains short cuts', () => {
    const result = calculateGeometry(syntheticRuns([10, 3, 10], true), syntheticRecipe());
    expect(result.postCount).toBe(6);
    expect(result.bays.flatMap(b => b.lengthsU16)).toEqual([1536, 384, 576, 1536, 384]);
    expect(result.requirements.find(r => r.sourceRuleId === 'rails')?.cuts)
      .toHaveLength(10);
    expect(result.requirements.find(r => r.sourceRuleId === 'rails')?.unusedStockU16)
      .toBe(6528); // ten 8-ft stocks minus two copies of 23 installed feet
  });
  it('does not merge repeated labels', () => {
    expect(calculateGeometry(syntheticRuns([3, 3]), syntheticRecipe()).postCount).toBe(4);
  });
  it('converts sixteenths exactly and rejects nonpositive or excessive lengths', () => {
    expect(parseMeasuredLength('2', '3.0625')).toBe(433);
    expect(() => parseMeasuredLength('0', '0')).toThrow();
    expect(() => parseMeasuredLength('10001', '0')).toThrow();
    expect(() => parseMeasuredLength('1', '0.01')).toThrow(/sixteenth/);
  });
});
```

- [ ] **Step 3: Run the red check.** `npm test -- packages/domain/test/geometry.test.ts` must fail because the exported functions are absent, not because the workspace runner is broken.
- [ ] **Step 4: Implement geometry, validation and exact conversion.** Use decimal arithmetic to require an integral number of sixteenths; do not round entered measurements silently. Compute integer bays and explicit unique posts as follows; reject a self-loop and nonpositive spacing before this loop. Shared endpoints are only shared when their UUIDs match.

```ts
const endpoints = new Set<string>();
let internalPosts = 0;
const bays = runs.map(run => {
  const count = Math.ceil(run.lengthU16 / recipe.maxSpacingU16);
  endpoints.add(run.startConnectionId);
  endpoints.add(run.endConnectionId);
  internalPosts += count - 1;
  return { runId: run.id, lengthsU16: Array.from({ length: count }, (_, i) =>
    Math.min(recipe.maxSpacingU16, run.lengthU16 - i * recipe.maxSpacingU16)) };
});
const postCount = endpoints.size + internalPosts;
```

  Build `Requirement` rows from the declared rules, preserving cuts before purchase aggregation. Reject missing coverage, unresolved rule references, no materials, nonpositive stock and oversized cuts. Calculation validates populated rule semantics; production selection/freeze/publication separately require owner validation through `assertTrialReady`. A synthetic fixture remains `validation.status:'draft'` and `purpose:'test-only'`, never falsely owner-approved. A 2–4 ft return must retain its short rails and support cost; show the conservative no-reuse explanation in results. Add tests for 2-ft and 4-ft returns, oversized cuts and missing recipe inputs using full fixture changes in the test file.
- [ ] **Step 5: Run green and document the boundary.** Run the geometry test and `npm run typecheck`. Document one recipe only, no automated gate/corner surcharge/cut optimizer, and the owner validation evidence. Verify fixture exports are absent from `src/index.ts`.
- [ ] **Step 6: Commit.** `git add package.json package-lock.json .nvmrc .gitignore tsconfig.base.json vitest.config.ts scripts/verify.mjs packages/domain docs/trial/recipe-validation.md` then `git commit -m "feat: add shared validated fence geometry"`.

## Task 2: Immutable prices and deterministic pooled purchases

**Files:** Create `packages/domain/src/pricing.ts`, `packages/domain/test/pricing.test.ts`; modify `contracts.ts`, `index.ts`, test `fixtures.ts`.

**Interfaces:** Consumes `Requirement[]`. Produces `selectPurchases(requirements: Requirement[], pricing: PricingModule, choices: OfferChoice[]): PurchaseResult`; `appendObservation(history: PriceObservation[], observation: PriceObservation): PriceObservation[]`; `correctObservation(history: PriceObservation[], originalId: string, correction: PriceObservation): PriceObservation[]`. History functions never mutate existing records. The office persists them in Task 4.

```ts
// Add to contracts.ts in this task.
export type PriceTier = { id: string;
  kind: 'retail' | 'bulk' | 'contractor-quote' | 'contractor-discount';
  unitPrice: Money | null; discountFraction: string | null; basisTierId: string | null;
  minPurchasedUnits: string | null; maxPurchasedUnits: string | null };
export type Arrangement = { id: string; baseTierId: string; discountTierIds: string[] };
export type PriceObservation = { id: string; offerId: string; recordedAt: string;
  observedAt: string | null; effectiveAt: string | null; sourceDate: string | null;
  sourceType: 'manual' | 'quote' | 'receipt'; evidence: string;
  taxIncluded: boolean; purchaseTaxFraction: string | null;
  tiers: PriceTier[]; arrangements: Arrangement[]; correctsId: string | null };
export type Vendor = { id: string; name: string; contacts: {name: string; phone: string; email: string}[];
  address: string; website: string; branches: string[]; notes: string };
export type Component = { id: string; description: string; nominalDimensions: string;
  actualDimensions: string; stockLengthU16: number | null; material: string; finish: string;
  purchaseUnit: string; packageQuantity: string };
export type Offer = { id: string; vendorId: string; componentId: string; sku: string;
  productUrl: string; specification: string; currency: 'USD'; branch: string;
  purchaseUnit: string; packageQuantity: string; availabilityNotes: string;
  rentalPeriod: 'day' | 'week' | null };
export type OfferChoice = { componentId: string; offerId: string; arrangementId: string | null };
export type Purchase = { offerId: string; observationId: string; arrangementId: string;
  purchasedUnits: string; packages: number; unitPrice: Money;
  preTaxCost: Money; purchaseTax: Money; cost: Money;
  allocations: { requirementId: string; segment: SegmentId; cost: Money }[] };
export type PurchaseResult = { purchases: Purchase[]; issues: Issue[] };
export type BusinessSettings = { confirmedAt: string | null; laborCostPerPersonHour: Money | null;
  defaultMarkupFraction: string | null; customerTaxFraction: string | null;
  taxableSegments: SegmentId[]; businessName: string; proposalText: string;
  officeRecipient: string; currency: 'USD' };
export type PricingModule = { schema: 1; businessId: string; version: string;
  effectiveAt: string; offers: Offer[]; observations: PriceObservation[];
  defaultOffers: { componentId: string; offerId: string }[]; settings: BusinessSettings };
```

`unitPrice` means per declared purchase unit, not per pack; the UI always labels that unit. A pack quantity of 10 and a requirement of 11 units means 2 packs/20 purchased units. An observation may omit tiers; unknown is `null`/absent, never fabricated `"0.00"`. An explicitly entered free item may be `"0.00"` with evidence. `arrangements` is the complete allowlist of permitted base-plus-discount combinations: no implicit stacking, and a discount must name the base it actually discounts. Corrected observations stay in history but are excluded from current selection by `correctsId`. Publishing selects the observation explicitly; it does not guess “latest” from an unknown source date.

- [ ] **Step 1: Add test fixtures and failing selection tests.** Extend `fixtures.ts` with `syntheticPricing()` containing one 10-unit pack offer, retail `$10/unit`, bulk `$8/unit` at 20 purchased units, a contractor quote `$9/unit`, and contractor 10% off retail only. Give each arrangement a distinct ID and permit no bulk-plus-discount arrangement. Add `syntheticRequirement(segment, units)` and use decimal strings throughout.

```ts
import { expect, it } from 'vitest';
import { selectPurchases, correctObservation } from '../src/index.ts';
import { syntheticPricing, syntheticRequirement } from './fixtures.ts';

it('pools requirements before pack rounding and bulk selection', () => {
  const result = selectPurchases([
    syntheticRequirement('posts', '6'), syntheticRequirement('rails', '5')
  ], syntheticPricing(), []);
  expect(result.issues).toEqual([]);
  expect(result.purchases[0]).toMatchObject({ purchasedUnits: '20', packages: 2,
    arrangementId: 'bulk', cost: '160.00' });
  expect(result.purchases[0].allocations.map(a => a.cost)).toEqual(['87.27', '72.73']);
});
it('does not manufacture a bulk contractor discount', () => {
  const result = selectPurchases([syntheticRequirement('posts', '20')], syntheticPricing(), []);
  expect(result.purchases[0].cost).toBe('160.00'); // not $144
});
it('missing price is incomplete rather than zero', () => {
  const pricing = syntheticPricing();
  pricing.observations[0].tiers = [];
  pricing.observations[0].arrangements = [];
  expect(selectPurchases([syntheticRequirement('posts', '1')], pricing, []).issues)
    .toContainEqual(expect.objectContaining({ code: 'MISSING_ELIGIBLE_PRICE' }));
});
it('correction retains the exact original record', () => {
  const original = syntheticPricing().observations[0];
  const result = correctObservation([original], original.id,
    { ...original, id: '00000000-0000-4000-8000-000000000099', correctsId: original.id });
  expect(result[0]).toEqual(original);
  expect(result).toHaveLength(2);
});
```

- [ ] **Step 2: Run red.** `npm test -- packages/domain/test/pricing.test.ts`; expect missing API failures.
- [ ] **Step 3: Implement selection and cent allocation.** Group required purchases by chosen offer (explicit override, otherwise published default). Reject an offer absent from the release or a unit mismatch. Round whole packages once per pooled offer; filter arrangements by all thresholds on **purchased** units; validate discount basis and allowlist; compare final tax-inclusive costs with Decimal. A valid explicit arrangement wins even if more expensive; an ineligible explicit choice is an issue, not silently substituted. Tie-break by arrangement ID. Record all selected provenance.

```ts
const packages = requiredUnits.div(offer.packageQuantity).ceil();
const purchasedUnits = packages.mul(offer.packageQuantity);
// Work in integer cents for allocation after the pooled purchase total is rounded.
const totalCents = totalCost.mul(100).toDecimalPlaces(0, Decimal.ROUND_HALF_UP);
const shares = requirements.map(r => ({ id: r.id, segment: r.segment,
  exact: totalCents.mul(r.installedUnits).div(installedTotal) }));
const rounded = shares.map(s => ({ ...s, cents: s.exact.floor() }));
// Allocate remaining cents by descending fractional remainder, then stable ID.
// Return allocations sorted by requirement ID; their integer-cent sum equals totalCents.
```

  Implement that remainder loop explicitly, with a zero-total/zero-weight guard. Add tests for fractional required units around a bulk boundary, explicit non-cheapest tier, invalid discount bases, tax-included versus excluded observations, missing purchase tax, unchanged default vendor despite cheaper other offers, and day/week rental mismatch. `observedAt:null` remains null after append/correction.
- [ ] **Step 4: Run green.** `npm test -- packages/domain/test/pricing.test.ts packages/domain/test/geometry.test.ts` and `npm run typecheck`.
- [ ] **Step 5: Commit.** `git add packages/domain` then `git commit -m "feat: preserve price history and select pooled purchase tiers"`.

## Task 3: Complete segment costing, manual allowances and explainable totals

**Files:** Create `packages/domain/src/estimate.ts`, `packages/domain/test/estimate.test.ts`; modify domain contracts/index/fixtures.

**Interfaces:** Consumes Tasks 1–2. Produces `calculateEstimate(input: EstimateInput): EstimateResult`; `priceSegment(input: SegmentPriceInput): SegmentResult`; `assertTrialReady(recipe: Recipe, pricing: PricingModule): Issue[]`. `assertTrialReady` rejects test-only/unvalidated recipes and unconfirmed/null business settings; explicit zero values remain valid.

```ts
export type ManualItem = { id: string; description: string; segment: SegmentId;
  quantity: string; unit: string; unitCost: Money;
  category: 'material' | 'labor' | 'equipment' | 'other'; source: string;
  assumptions: string; manual: true; purchaseTaxIncluded: boolean;
  purchaseTaxFraction: string | null;
  gateCheck: null | { runsExcludeOpening: true; supportsAndFacingNotDuplicated: true } };
export type SegmentAdjustment = { segment: SegmentId; markupFraction: string | null;
  sellingOverride: Money | null; reason: string };
export type EstimateInput = { catalogReleaseId: string; runs: Run[]; recipe: Recipe; pricing: PricingModule;
  choices: OfferChoice[]; manualItems: ManualItem[]; adjustments: SegmentAdjustment[];
  jobMarkupFraction: string | null; assumptions: string[]; exclusions: string[] };
export type SegmentPriceInput = { segment: SegmentId; cost: Money;
  personHours: string | null; jobMarkupFraction: string;
  adjustment: SegmentAdjustment | null; customerTaxFraction: string; taxable: boolean };
export type SegmentResult = { segment: SegmentId; cost: Money;
  personHours: string | null; selling: Money; customerTax: Money;
  profit: Money; effectiveMarkupFraction: string | null; belowCost: boolean };
export type EstimateResult = { schema: 1; calculatorVersion: string;
  state: 'complete' | 'incomplete'; issues: Issue[];
  geometry: GeometryResult; purchases: Purchase[]; segments: SegmentResult[];
  cost: Money; selling: Money; customerTax: Money; total: Money;
  internalNotices: string[] };
```

Manual material tax is added only when excluded; a missing excluded rate is incomplete. Manual labor costs never invent hours; `null` distinguishes unknown hours from zero. Rentals retain their explicit billing unit. Manual gate allowance UI requires both confirmations; the engine never subtracts an opening or inserts support posts. Missing automatic recipe inputs remain issues even with an allowance. Incomplete results can show known line costs but the UI must not label their subtotal a valid quote or permit a freeze.

- [ ] **Step 1: Write failing money/allowance tests.** Extend fixtures with `syntheticEstimateInput()` using the earlier populated fixture objects, and `syntheticManualItem()` with explicit test costs/tax flags.

```ts
import { expect, it } from 'vitest';
import { calculateEstimate, priceSegment } from '../src/index.ts';
import { syntheticEstimateInput, syntheticManualItem } from './fixtures.ts';

it('taxes the final selling override, without splitting material and labor', () => {
  const result = priceSegment({ segment: 'posts', cost: '1000.00', personHours: '12',
    jobMarkupFraction: '0.20', adjustment: { segment: 'posts', markupFraction: '0.50',
      sellingOverride: '2000.00', reason: 'owner price' },
    customerTaxFraction: '0.10', taxable: true });
  expect(result.selling).toBe('2000.00');
  expect(result.customerTax).toBe('200.00');
});
it('clearing direct override restores segment markup, then job markup', () => {
  const base = { segment: 'posts' as const, cost: '100.00', personHours: '0',
    jobMarkupFraction: '0.20', customerTaxFraction: '0', taxable: false };
  expect(priceSegment({ ...base, adjustment: { segment: 'posts', markupFraction: '0.50',
    sellingOverride: null, reason: '' } }).selling).toBe('150.00');
  expect(priceSegment({ ...base, adjustment: null }).selling).toBe('120.00');
});
it.each([[true, '110.00'], [false, '121.00']])('manual purchase tax included=%s', (included, cost) => {
  const input = syntheticEstimateInput();
  input.manualItems = [{ ...syntheticManualItem(), quantity: '1', unitCost: '110.00',
    purchaseTaxIncluded: included, purchaseTaxFraction: '0.10' }];
  const withItem = calculateEstimate(input);
  const without = calculateEstimate({ ...input, manualItems: [] });
  expect(Number(withItem.cost) - Number(without.cost)).toBe(Number(cost));
});
it('a manual gate does not repair an incomplete automatic recipe', () => {
  const input = syntheticEstimateInput();
  input.recipe.materials = [];
  input.manualItems = [{ ...syntheticManualItem(), gateCheck:
    { runsExcludeOpening: true, supportsAndFacingNotDuplicated: true } }];
  expect(calculateEstimate(input).state).toBe('incomplete');
});
```

- [ ] **Step 2: Run red.** `npm test -- packages/domain/test/estimate.test.ts`.
- [ ] **Step 3: Implement pure composition and pricing.** Geometry feeds pooled purchases; allocations feed only their consuming segments; acquisition gets its own sourcing/delivery labor/fees, never the material purchase again. Recipe labor is person-hours times the explicitly configured hourly cost. Add manual cost rows to their selected segment, then price applicable segments once. Use Decimal everywhere; the `Number` conversions above are fixture assertions only.

```ts
const markup = input.adjustment?.markupFraction ?? input.jobMarkupFraction;
const selling = input.adjustment?.sellingOverride !== null && input.adjustment?.sellingOverride !== undefined
  ? new Decimal(input.adjustment.sellingOverride)
  : new Decimal(input.cost).mul(new Decimal(1).plus(markup));
const roundedSelling = selling.toDecimalPlaces(2, Decimal.ROUND_HALF_UP);
const customerTax = input.taxable
  ? roundedSelling.mul(input.customerTaxFraction).toDecimalPlaces(2, Decimal.ROUND_HALF_UP)
  : new Decimal(0);
```

  Return internal profit/below-cost flags and `effectiveMarkupFraction:null` for zero cost. Totals sum rounded segment amounts. Add tests that purchases are counted once, penny allocations sum exactly, direct override zero is respected, missing versus intentionally zero settings differ, manual labor contributes no made-up hours, invalid manual gate confirmations block save/freeze, and purchase tax is not re-marked-up after customer tax. Add assertion that all serialized monetary outputs are fixed two-decimal strings.
- [ ] **Step 4: Run green.** `npm test -- packages/domain/test` and `npm run typecheck`.
- [ ] **Step 5: Commit.** `git add packages/domain` then `git commit -m "feat: calculate segment quotes and manual work allowances"`.

## Task 4: Useful Mac catalog, customer/job editor and durable drafts

**Files:** Create `apps/office/{package.json,tsconfig.json,index.html,vite.config.ts}`, `apps/office/scripts/dev.mjs`; office server `database.ts`, `catalog-store.ts`, `job-store.ts`, `http.ts`; UI `App.tsx`, `Catalog.tsx`, `Setup.tsx`, `JobEditor.tsx`, `Estimate.tsx`, `main.tsx`, `styles.css`; `apps/office/test/{database,job-save,http}.test.ts`; modify domain contracts/fixtures and create `packages/domain/src/canonical.ts`; create `apps/office/src/server/attachments.ts` and `apps/office/test/attachments.test.ts`; create `docs/trial/setup.md` and `docs/trial/quote-workflow.md`.

**Interfaces:** `openOfficeStore(rootDir: string): OfficeStore` owns `DatabaseSync` and file paths; `OfficeStore.close(): void`. Store methods: `appendPrice(observation: PriceObservation): void`; `saveCatalog(input: {vendors: Vendor[]; components: Component[]; offers: Offer[]; recipe: Recipe; pricing: PricingModule}): void`; `loadCatalog():` that same shape; `saveCustomer(customer: Customer): void`; `saveDraft(draft: JobDraft, expectedRevision: number | null): JobDraft`; `getDraft(id: string): JobDraft | null`; `listJobs(): JobDraft[]`. Revisions are optimistic integers. `saveDraft` increments only after a successful transaction; a conflict returns a named error and the existing revision. Neither opening a draft nor refreshing a catalog recalculates it.

```ts
// Add schemas/types to domain contracts.ts.
export type Customer = { id: string; name: string; contacts: {name: string; phone: string; email: string}[];
  referralSource: string; firstContactDate: string | null;
  contactHistory: { id: string; occurredAt: string; note: string }[] };
export type JobDraft = { id: string; customerId: string; customerSnapshot: Customer; revision: number;
  calculatedInputCanonical: string;
  createdAt: string; updatedAt: string; jobsiteAddress: string;
  requirements: string; accessNotes: string; input: EstimateInput; result: EstimateResult;
  source: { deviceId: string | null; businessId: string; officeBaseRevision: number | null } };
```

Draft input/result are self-contained JSON. The UI creates a new calculation only after explicit Calculate/Reprice; a changed input makes the displayed result visibly stale until Calculate succeeds. Saving edits persists the input plus the last result and a derived “needs calculation” flag (fingerprint comparison introduced in Task 5); a quote freeze requires a matching current input/result. Existing quotes are never touched by draft saves. The `calculatedInputCanonical` field in `JobDraft` is populated by a stable sorted-key serializer added to `packages/domain/src/canonical.ts`; Task 5 adds hashing for durable identity.

- [ ] **Step 1: Write SQLite transaction/revision tests.** Add `syntheticCustomer()` and `syntheticDraft()` fixtures; drafts include the canonical string of their calculation input. Use a unique OS temp directory per test and close the store in `afterEach`.

```ts
import { afterEach, expect, it } from 'vitest';
import { mkdtempSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { openOfficeStore } from '../src/server/database.ts';
import { syntheticCustomer, syntheticDraft } from '../../../packages/domain/test/fixtures.ts';
const roots: string[] = [];
const stores: ReturnType<typeof openOfficeStore>[] = [];
afterEach(() => { stores.splice(0).forEach(s => s.close());
  roots.splice(0).forEach(p => rmSync(p, {recursive: true, force: true})); });
it('retains the saved revision on a conflicting write', () => {
  const root = mkdtempSync(join(tmpdir(), 'estimator-')); roots.push(root);
  const store = openOfficeStore(root); stores.push(store);
  store.saveCustomer(syntheticCustomer());
  const saved = store.saveDraft(syntheticDraft(), null);
  expect(saved.revision).toBe(1);
  expect(() => store.saveDraft({...saved, requirements: 'stale edit'}, 0)).toThrow(/revision/i);
  expect(store.getDraft(saved.id)?.requirements).toBe(saved.requirements);
});
it('append-only observation storage refuses update/delete', () => {
  const root = mkdtempSync(join(tmpdir(), 'estimator-')); roots.push(root);
  const store = openOfficeStore(root); stores.push(store);
  const observation = syntheticDraft().input.pricing.observations[0];
  store.appendPrice(observation);
  expect(() => store.appendPrice({...observation, evidence: 'overwrite'})).toThrow(/immutable/i);
});
```

- [ ] **Step 2: Run red.** `npm test -- apps/office/test/database.test.ts apps/office/test/job-save.test.ts`.
- [ ] **Step 3: Implement the store and local-only service.** Create version-1 tables `customers`, `jobs`, `vendors`, `components`, `offers`, `price_observations`, `recipes`, `settings`, `quote_snapshots`, `attachments`, `catalog_releases`, `import_ledger`, `source_mappings`, `received_submissions`; JSON columns are validated at repository boundaries, with indexed IDs/revisions. Unused tables support the immediately following tasks, not a general ORM. Enable foreign keys; use transactions and immutable-row triggers for observations/quotes/received submissions. Store files under an owner-chosen local data directory, defaulting to `~/Library/Application Support/Project Estimator/`; never under the deploy tree. Use restricted directory/file permissions for keys and backups. All SQL values are bound parameters.

```sql
CREATE TABLE jobs (
  id TEXT PRIMARY KEY, customer_id TEXT NOT NULL REFERENCES customers(id),
  revision INTEGER NOT NULL CHECK(revision > 0), body TEXT NOT NULL
);
CREATE TABLE price_observations (id TEXT PRIMARY KEY, offer_id TEXT NOT NULL, body TEXT NOT NULL);
CREATE TRIGGER price_observations_no_update BEFORE UPDATE ON price_observations
BEGIN SELECT RAISE(ABORT, 'immutable observation'); END;
CREATE TRIGGER price_observations_no_delete BEFORE DELETE ON price_observations
BEGIN SELECT RAISE(ABORT, 'immutable observation'); END;
```

  `http.ts` uses Node HTTP, a 5 MiB request limit and a small explicit route table; no framework/server account system. Bind `127.0.0.1` only. Development Vite proxies `/api`; production Node serves the built UI and API on the same origin. Reject mutation requests with a foreign `Origin` or non-JSON content type; reject unexpected Host values. Routes: GET/POST `/api/catalog`, POST `/api/prices`, GET/POST `/api/customers`, GET `/api/jobs`, GET/PUT `/api/jobs/:id`; later tasks add their routes. Return typed JSON errors without local paths/secrets. Test foreign-origin writes and body limits once; this is a local guard, not authentication infrastructure.

- [ ] **Step 4: Implement usable office forms and save feedback.** Catalog forms enter vendor/component/offer units and append dated prices/corrections; Setup requires explicit labor, markup, purchase/customer-tax decisions, selected default offers, business proposal text and office email. Show owner validation of one recipe, unavailable selections and named missing inputs. Customer/job forms cover contact/referral/history (last contact derived from dated entries), address, constraints, repeatable named runs and endpoint connections, manual items and gate checks. Estimate displays quantities/cuts/unused stock, packs/tiers/provenance, person-hours, segment cost/selling/tax and overrides with Clear. Only trial navigation is shown. A simple Attach file action retains owner-selected job/receipt evidence as immutable local files with original name, content hash, byte length and source date; render links, not a drawing library. `attachments.ts` owns `attachFile(ownerId: string, bytes: Uint8Array, metadata: {name: string; sourceDate: string|null}): AttachmentRecord`, with `AttachmentRecord` storing ID/owner/hash/relative path/name/date/size. Bound files to 20 MiB, reject path traversal, write verified files before the referencing transaction and remove unreferenced temp files on failure. Expose explicit local upload/download routes and test failed writes/references; never include attachments automatically in field JSON or CDN.

```ts
// UI save controller contract: persist before acknowledging.
export async function persistDraft(
  draft: JobDraft,
  save: (draft: JobDraft) => Promise<JobDraft>,
  setState: (state: 'saving' | 'saved' | 'unsaved') => void
): Promise<JobDraft> {
  setState('saving');
  try { const durable = await save(draft); setState('saved'); return durable; }
  catch (error) { setState('unsaved'); throw error; }
}
```

  Define `persistDraft` in `apps/office/src/ui/JobEditor.tsx`; test its rejected-promise path in `job-save.test.ts`. Debounce edits briefly, retain visible unsaved/error status and provide Retry. Disable presenting while saving/dirty/incomplete. Reprice is an explicit button with before/after purchase/tier/selling totals shown before saving the repriced draft. Zero-rate fields require deliberate owner entry; blank is not zero.
- [ ] **Step 5: Run green and the Mac smoke workflow.** Run `npm test -- apps/office/test packages/domain/test`, `npm run typecheck`, `npm run build --workspace @estimator/office`. Start `npm run dev:office` and use the browser to enter a small test catalog/customer/job, connect 10/3/10-ft runs, calculate, override/clear, save, restart the service and reopen the exact result. Confirm a price-history edit leaves it unchanged. Record this in `docs/trial/quote-workflow.md`. Do not present synthetic data as a real quote.
- [ ] **Step 6: Commit.** `git add apps/office packages/domain docs/trial/setup.md docs/trial/quote-workflow.md package.json package-lock.json` then `git commit -m "feat: add local Mac catalog and estimate workflow"`.

## Task 5: Immutable Preliminary/Issued quotes and allowlisted PDF

**Files:** Create domain `quotes.ts`, `proposal.ts`; extend `canonical.ts`, contracts/index; tests `quotes.test.ts`, `proposal.test.ts`; office `server/quote-service.ts`, `platform/pdf.ts`, `ui/Proposal.tsx`, test `quote-service.test.ts`; modify job editor/store/HTTP/workflow doc. Create `packages/exchange/{package.json,tsconfig.json}`, `packages/exchange/src/proposal-pdf.ts` and `packages/domain/src/quote-service.ts` for portable freeze orchestration and `packages/domain/test/quote-service.test.ts`.

**Interfaces:** `canonicalJson(value: unknown): string` recursively sorts object keys, preserves array order and rejects undefined/nonfinite numbers. Platform `sha256(bytes: Uint8Array): Promise<string>` returns lowercase hex. `quoteContent(draft: JobDraft, status: QuoteStatus): QuoteContent`; `toProposal(quote: FrozenQuote): ProposalModel`; `renderProposalPdf(proposal: ProposalModel): Promise<Uint8Array>` uses pdf-lib and no network fonts. `freezeQuote(draft: JobDraft, status: QuoteStatus, platform: 'office' | 'field', deps: FreezeDeps): Promise<FrozenQuote>` is shared orchestration. `FreezeDeps` has `mode: 'production' | 'synthetic-preview'`, `sha256`, `newId(): string`, `now(): string`, and `putIfAbsent(fingerprint: string, quote: FrozenQuote): Promise<FrozenQuote>`; the store enforces fingerprint uniqueness and returns the existing row for repeat actions.

```ts
export type QuoteStatus = 'Preliminary' | 'Issued';
export type QuoteContent = { jobId: string; customer: Customer; jobsiteAddress: string;
  requirements: string; status: QuoteStatus; input: EstimateInput; result: EstimateResult };
export type FrozenQuote = QuoteContent & { id: string; fingerprint: string; frozenAt: string };
export type ProposalModel = { quoteId: string; status: QuoteStatus; frozenAt: string;
  testOnly: boolean;
  businessName: string; businessText: string; customerName: string; jobsiteAddress: string;
  scope: string; inclusions: string[]; exclusions: string[]; assumptions: string[];
  pricingDate: string; segments: { label: string; selling: Money }[];
  subtotal: Money; customerTax: Money; total: Money; currency: 'USD' };
```

`quoteContent` reads `JobDraft.customerSnapshot`, populated when customer/job data is saved and copied into the freeze. Keep immutable snapshot display independent of current customer details/catalog. Include selected manual descriptions in proposal inclusions, with the allowance identified as such, but not their internal costs/source notes. No separately billed estimating/drafting fee.

- [ ] **Step 1: Write snapshot and disclosure tests.** Add `syntheticFrozenQuote()` and `memoryFreezeDeps()` to fixtures; the latter uses a map, deterministic UUID/time and a real SHA-256 test adapter. Production hashing stays in platform adapters.

```ts
import { expect, it } from 'vitest';
import { freezeQuote, toProposal } from '../src/index.ts';
import { syntheticDraft, memoryFreezeDeps } from './fixtures.ts';
it('reuses unchanged presentation, but issuing creates a different frozen quote', async () => {
  const draft = syntheticDraft(); const deps = memoryFreezeDeps();
  const first = await freezeQuote(draft, 'Preliminary', 'office', deps);
  const repeated = await freezeQuote(draft, 'Preliminary', 'office', deps);
  const issued = await freezeQuote(draft, 'Issued', 'office', deps);
  expect(repeated.id).toBe(first.id);
  expect(issued.id).not.toBe(first.id);
  expect(first.status).toBe('Preliminary');
  await expect(freezeQuote(draft, 'Issued', 'field', deps)).rejects.toThrow(/Preliminary/);
});
it('proposal exposes only the customer-safe schema', async () => {
  const quote = await freezeQuote(syntheticDraft(), 'Preliminary', 'office', memoryFreezeDeps());
  const proposal = toProposal(quote);
  expect(Object.keys(proposal).sort()).toEqual([
    'assumptions','businessName','businessText','currency','customerName','customerTax',
    'exclusions','frozenAt','inclusions','jobsiteAddress','pricingDate','quoteId',
    'scope','segments','status','subtotal','testOnly','total'
  ].sort());
  expect(JSON.stringify(proposal)).not.toMatch(/unitCost|personHours|markup|profit|laborCost/);
});
```

- [ ] **Step 2: Run red.** `npm test -- packages/domain/test/quotes.test.ts packages/domain/test/proposal.test.ts packages/domain/test/quote-service.test.ts apps/office/test/quote-service.test.ts`.
- [ ] **Step 3: Implement content-addressed freeze and customer-only rendering.** Require current input to match `calculatedInputCanonical`, complete result, no pending save and field status Preliminary. Production mode requires `assertTrialReady`; synthetic-preview mode permits populated test-only fixtures with a prominent TEST ONLY presentation/PDF label and cannot be enabled in production builds. `memoryFreezeDeps` explicitly selects synthetic-preview; it does not change fixture validation to approved. Fingerprint the canonical `QuoteContent`, including status and customer-facing content, excluding generated ID/time and mutable draft revision/update time. Persist snapshot once transactionally before displaying, sharing or exporting it. A deliberate status change creates a new fingerprint. Office store `putQuoteIfAbsent` has a unique fingerprint index and immutable triggers; clicking twice returns the same stored ID. No UPDATE path exists for a frozen quote.

```ts
export function toProposal(q: FrozenQuote): ProposalModel {
  return {
    quoteId: q.id, status: q.status, frozenAt: q.frozenAt,
    testOnly: q.input.recipe.validation.purpose === 'test-only',
    businessName: q.input.pricing.settings.businessName,
    businessText: q.input.pricing.settings.proposalText,
    customerName: q.customer.name, jobsiteAddress: q.jobsiteAddress,
    scope: q.requirements,
    inclusions: q.input.manualItems.map(x => `${x.description} (manual allowance)`),
    exclusions: q.input.exclusions, assumptions: q.input.assumptions,
    pricingDate: q.input.pricing.effectiveAt,
    segments: q.result.segments.map(s => ({ label: s.segment, selling: s.selling })),
    subtotal: q.result.selling, customerTax: q.result.customerTax,
    total: q.result.total, currency: 'USD'
  };
}
```

  Replace raw segment IDs with fixed readable labels in the renderer; use that same allowlisted model in both customer screen and PDF. Validate `ProposalModel` at the PDF/view entrypoint, rejecting extra keys. Share `renderProposalPdf` as `packages/exchange/src/proposal-pdf.ts` (create exchange package here) so mobile reuses it; office `platform/pdf.ts` only writes/returns the bytes. Layout wrapped text and page breaks explicitly, repeating quote ID/status on each page; use bundled standard PDF fonts. PDF function accepts only `ProposalModel`, never a draft/quote/internal object.
- [ ] **Step 4: Run green and inspect actual output.** Add tests that repricing/changing the draft leaves old snapshot bytes unchanged; a failed quote transaction opens no presentation; a customer detail change creates a new snapshot; PDF bytes are nonempty and generated without fetch. Run the test command, typecheck and office build. Open a short and multi-page PDF with long scope/customer names; confirm wrapping, page breaks, readable totals and no internal costs/hours/markup. Record check in quote-workflow doc. Preliminary watermark/status and pricing date must remain on saved output after later issuing.
- [ ] **Step 5: Commit.** `git add packages apps/office docs/trial/quote-workflow.md package-lock.json` then `git commit -m "feat: freeze customer quotes and export safe proposals"`.

## Task 6: Safe modular catalog staging, encryption and office enrollment QR

**Files:** Create exchange `contracts.ts`, `catalog.ts`, `index.ts`, tests `catalog.test.ts`; office `server/publish-service.ts`, `platform/crypto.ts`, `platform/files.ts`, `ui/Publishing.tsx`, test `publishing.test.ts`; modify office HTTP/database; create `docs/trial/publishing.md`.

**Interfaces:** `buildCatalogRelease(input: CatalogBuildInput, crypto: CatalogCrypto, previous: CatalogArtifact[]): Promise<CatalogBuildResult>`; `validateManifest(value: unknown): Manifest`; `makeEnrollment(origin: string, businessId: string, key: CatalogKey): Enrollment`; `stagePublication(root: string, release: CatalogBuildResult): Promise<PublicationPreview>`. `CatalogCrypto` implements `sha256(bytes)`, `encrypt(key, iv, plaintext, additionalData)`, `randomBytes(count)`. Keys are 32 random bytes; AES-GCM uses a fresh random 12-byte IV per newly encrypted artifact and authenticated metadata. Never reuse an IV across new encryption. Reuse the **entire already generated ciphertext** only when plaintext hash, metadata and key ID are unchanged.

```ts
// Exchange contracts; keys appear only in local/enrollment contracts, never Manifest.
export type CatalogKey = { id: string; rawBase64: string };
export type Enrollment = { schema: 1; businessId: string; origin: string; key: CatalogKey };
export type ModuleRef = { id: 'pricing' | 'design'; version: string; schema: 1;
  url: string; bytes: number; sha256: string; keyId: string | null;
  ivBase64: string | null; plaintextSha256: string };
export type Manifest = { schema: 1; businessId: string; releaseId: string; publishedAt: string;
  minAppVersion: string; engineVersion: string; modules: ModuleRef[] };
export type DesignModule = { schema: 1; version: string; recipe: Recipe; components: Component[] };
export type CatalogArtifact = { ref: ModuleRef; body: Uint8Array };
export type CatalogBuildInput = { manifest: Omit<Manifest, 'modules'>;
  pricing: PricingModule; design: DesignModule; key: CatalogKey };
export type CatalogBuildResult = { manifest: Manifest; artifacts: CatalogArtifact[] };
export type PublicationPreview = { stageDir: string; includedPaths: string[];
  removedCurrentPaths: string[]; releaseId: string };
```

For the trial encrypt **both** pricing and design; this is the simplest explicit default and avoids accidentally leaking rates embedded in design notes. No drawing/media library is introduced. Later intentionally public assets remain a schema extension, not required trial files. Pricing contains selected published offers, their selected observations/all permitted tiers, default-offer selection and business settings, not full vendor history. Design contains the one validated recipe and required component definitions. Validate cross-module component/offer/rule IDs and matching business/module versions before publishing. `Manifest.releaseId` identifies the aggregate catalog; `PricingModule.version` and `DesignModule.version` identify independently versioned module payloads. `EstimateInput.catalogReleaseId` preserves the exact aggregate used. A pricing-only change therefore does not edit design payload bytes.

- [ ] **Step 1: Write release/encryption tests.** Add `syntheticCatalogBuild()` and Node Web Crypto test adapter fixtures in `packages/exchange/test/fixtures.ts`; test-only catalogs are allowed in test builds through an explicit `mode:'synthetic-preview'` argument added to `CatalogBuildInput`. Real `mode:'production'` calls `assertTrialReady`.

```ts
import { expect, it } from 'vitest';
import { buildCatalogRelease } from '../src/catalog.ts';
import { syntheticCatalogBuild, nodeTestCrypto } from './fixtures.ts';
it('reuses identical encrypted artifacts and changes them on rotation', async () => {
  const input = syntheticCatalogBuild(); const crypto = nodeTestCrypto();
  const first = await buildCatalogRelease(input, crypto, []);
  const again = await buildCatalogRelease(input, crypto, first.artifacts);
  expect(again.artifacts).toEqual(first.artifacts);
  const rotated = await buildCatalogRelease({...input, key: {
    id: 'key-2', rawBase64: Buffer.alloc(32, 2).toString('base64') }}, crypto, first.artifacts);
  expect(rotated.artifacts[0].ref.sha256).not.toBe(first.artifacts[0].ref.sha256);
  expect(rotated.artifacts.every(a => a.ref.keyId === 'key-2')).toBe(true);
});
it('publication metadata never contains an enrollment secret or customer', async () => {
  const input = syntheticCatalogBuild();
  const result = await buildCatalogRelease(input, nodeTestCrypto(), []);
  expect(JSON.stringify(result.manifest)).not.toContain(input.key.rawBase64);
  expect(Object.keys(result.manifest).sort()).toEqual([
    'businessId','engineVersion','minAppVersion','modules','publishedAt','releaseId','schema'
  ].sort());
});
```

- [ ] **Step 2: Run red.** `npm test -- packages/exchange/test/catalog.test.ts apps/office/test/publishing.test.ts`.
- [ ] **Step 3: Implement staging with an explicit publication allowlist.** Save local keys/recovery material outside every staged/deployed directory; generate/display QR only on owner's action using `qrcode`. Payload is the exact serialized `Enrollment`; provide Copy enrollment and Download QR, with a note that this shares a reusable catalog credential. Do not send email. Accept only HTTPS production origins and same-origin content-addressed relative module URLs; preview localhost is a separately labeled test mode.

```ts
// Content-addressed path derives from ciphertext, after encryption.
const ciphertextHash = await crypto.sha256(ciphertext);
const relativePath = `catalog/modules/${ciphertextHash}.bin`;
// The current manifest is written only after all referenced artifacts exist and verify.
await writeVerifiedArtifacts(stageDir, result.artifacts);
await writeJsonAtomically(join(stageDir, 'catalog/current.json'), result.manifest);
```

  Define `writeVerifiedArtifacts` and `writeJsonAtomically` in office `platform/files.ts`, checking byte count/hash and writing temp-file+rename. Staging builds a fresh directory from explicit manifest refs and built app allowlist, not `cp -R` of data/root. `PublicationPreview` compares the previous current manifest's module paths with the new referenced set and lists superseded packs to remove from the **current** deployment only. Do not delete local archives/recovery keys or claim old deployment URLs/device copies are revoked. A Cloudflare Pages static upload of this exact staged directory is a later explicit owner Publish action; no Cloudflare API key is shipped to the PWA.

  A module version changes only with that module's content; the aggregate manifest release ID is independent. Test that a design-only change leaves pricing ciphertext/URL unchanged and that draft inputs retain the aggregate release ID.
- [ ] **Step 4: Run green and inspect staging.** Add tests that missing referenced files prevent manifest installation, changing only pricing preserves design bytes, synthetic recipe blocks production, a malicious path/foreign URL is rejected and a staged directory contains neither SQLite/customer JSON/raw key/QR nor unencrypted pricing. Run tests/typecheck/office build. Document owner Publish, key-change preview, recovery-key backup and deployment removal limitations.
- [ ] **Step 5: Commit.** `git add packages/exchange apps/office docs/trial/publishing.md package-lock.json` then `git commit -m "feat: stage encrypted modular catalogs and enrollment"`.

## Task 7: Offline field jobs and the same calculator/customer output

**Files:** Create `apps/field/{package.json,tsconfig.json,app.json,App.tsx,metro.config.cjs}`; `apps/field/src/screens/{Jobs,Job,Designs,Updates,Outbox}.tsx`; field `store.ts`, `job-service.ts`, `platform/{crypto,files,pdf}.ts`; tests `store.test.ts`, `job-service.test.ts`; create `docs/trial/field-workflow.md`; modify workspace lockfile. Use a small screen state in `App.tsx`; Expo Router is not required.

**Interfaces:** `openFieldStore(name: string): FieldStore` wraps Dexie. Methods `saveDraft(draft: JobDraft): Promise<void>`, `getDraft(id): Promise<JobDraft | undefined>`, `listDrafts(): Promise<JobDraft[]>`, `putQuoteIfAbsent(fingerprint, quote): Promise<FrozenQuote>`, `listQuotes(jobId): Promise<FrozenQuote[]>`, `close(): void`; later tasks add catalog/outbox tables/methods. `saveFieldDraft(draft: JobDraft, store: Pick<FieldStore,'saveDraft'>, report: (state: 'saving'|'saved'|'unsaved') => void): Promise<void>` persists before reporting saved; `calculateFieldDraft(draft): JobDraft` calls shared `calculateEstimate` and refreshes the canonical-input marker. `renderProposalPdf` is reused unchanged through the field file adapter.

- [ ] **Step 1: Write durable-save tests using fake-indexeddb.** Dexie database names are unique per test; always delete test DBs. Fixtures are imported only by test files, not app bundles.

```ts
import 'fake-indexeddb/auto';
import { expect, it, vi } from 'vitest';
import { openFieldStore } from '../src/store.ts';
import { saveFieldDraft } from '../src/job-service.ts';
import { syntheticDraft } from '../../../packages/domain/test/fixtures.ts';
it('reads saved job input and result after reopening without a catalog key', async () => {
  const name = `test-${crypto.randomUUID()}`;
  const first = openFieldStore(name); const draft = syntheticDraft();
  await first.saveDraft(draft); first.close();
  const reopened = openFieldStore(name);
  expect(await reopened.getDraft(draft.id)).toEqual(draft);
  reopened.close(); await new Promise<void>((resolve, reject) => {
    const request = indexedDB.deleteDatabase(name);
    request.onsuccess = () => resolve(); request.onerror = () => reject(request.error);
  });
});
it('quota failure is unsaved and never acknowledged as saved', async () => {
  const report = vi.fn();
  const store = { saveDraft: vi.fn().mockRejectedValue(new DOMException('full', 'QuotaExceededError')) };
  await expect(saveFieldDraft(syntheticDraft(), store, report)).rejects.toThrow('full');
  expect(report.mock.calls.map(([state]) => state)).toEqual(['saving', 'unsaved']);
});
```

- [ ] **Step 2: Run red.** `npm test -- apps/field/test/store.test.ts apps/field/test/job-service.test.ts`.
- [ ] **Step 3: Implement field storage and touch forms.** Dexie v1 tables: `drafts`, `quotes` (unique fingerprint), `outbox`, `enrollment`, `catalogModules`, `catalogState`, `preferences`. Keep job/quote/outbox JSON ordinary local records independent of catalog-key encryption; catalog ciphertext and enrollment keys have separate tables. Save draft edits transactionally with bounded debounce, explicit error/retry and before-navigation flush. Request `navigator.storage.persist()` when appropriate but report its actual result; never call it a backup or guarantee. Current app version must read v1 without destructive migration.

```ts
this.version(1).stores({
  drafts: 'id,customerId', quotes: 'id,&fingerprint,jobId',
  outbox: 'id,jobId,state', enrollment: 'slot',
  catalogModules: 'sha256', catalogState: 'id', preferences: 'id'
});
```

  Use Expo `AppEntry`, `getDefaultConfig` from `expo/metro-config`, `web.output:'single'`, and static `expo export --platform web`; no legacy monorepo resolver/watch-folder overrides. UI uses React Native `View`, `Text`, `TextInput`, `Pressable`, `ScrollView`; web-specific file/QR/share code stays in platform files. Screens implement Jobs/New estimate/Design library/Updates/Outbox. Enter runs and explicit endpoint joins with flexible labels; duplicate labels remain separate IDs. Show dated active release and complete/incomplete calculation details; manual allowances and overrides match office behavior. Test-only fixture access exists only in a dedicated `EXPO_PUBLIC_TRIAL_TEST_MODE=1` build with a persistent visible banner, never production startup data.

  Present/PDF calls shared freeze logic with platform `'field'`; after durable write, render `ProposalModel`. Old drafts/quotes display from saved inputs/results even with no active catalog. Reprice is explicit with visible comparison and only succeeds when a compatible catalog is installed. Pending edits may be saved incomplete, but incomplete/stale calculations cannot be presented. Do not introduce scheduling/drawings or native-only controls.
- [ ] **Step 4: Run green and browser smoke.** Add a shared fixture parity test importing the office and field calculation entrypoints and comparing entire deterministic results. Test field Preliminary enforcement and frozen read after key/catalog rows are removed. Run tests/typecheck, `npm run build --workspace @estimator/field` and serve exported output over a local test origin. Create/save/reopen/Present a synthetic job, use long text and touch-width layout, then disable network within the already-loaded UI and reopen saved data through a fresh store instance. Cold offline app reload depends on Task 10's app-shell cache and is not claimed here. Physical-device storage/crypto claims wait for Task 10.
- [ ] **Step 5: Commit.** `git add apps/field packages/domain packages/exchange docs/trial/field-workflow.md package-lock.json` then `git commit -m "feat: add offline field estimates with shared calculation"`.

## Task 8: Enrollment and atomic foreground catalog refresh

**Files:** Create field `enrollment.ts`, `catalog-client.ts`, `platform/qr.ts`, `platform/lifecycle.ts`; tests `catalog-client.test.ts`, `enrollment.test.ts`, `qr.test.ts`; extend field store/Updates and exchange contracts/catalog validation; update field-workflow/publishing docs.

**Interfaces:** `parseEnrollment(text: string, expectedOrigin: string): Enrollment`; `acceptEnrollment(enrollment: Enrollment, replacePending: boolean, store: FieldStore): Promise<'unchanged' | 'pending'>`; `refreshCatalog(deps: RefreshDeps): Promise<RefreshResult>`; `readActiveCatalog(store: FieldStore, crypto: WebCatalogCrypto): Promise<ActiveCatalog | null>`. `RefreshDeps` contains store, `fetchBytes(url, maxBytes): Promise<Uint8Array>`, crypto, `appVersion`, `engineVersion`, `origin`, `now()`. `RefreshResult` status is `'unchanged' | 'updated' | 'offline' | 'invalid' | 'app-update-required' | 'registration-update-required'`, with message and active release ID. `ActiveCatalog` contains manifest, parsed pricing and design. Store adds `getEnrollment(): Promise<{active: Enrollment|null; pending: Enrollment|null}>`, `setPending(value): Promise<void>`, `getCatalogState()`, `getModule(hash)`, and `activateCatalog(transaction: CatalogActivation): Promise<void>`; `CatalogActivation` includes validated manifest/ciphertexts, chosen key slot, check time, module references and `expectedStateRevision: number`. `catalogState` maintains a monotonically increasing revision advanced by enrollment or activation changes; the transaction rejects a mismatched expected revision.

`WebCatalogCrypto` is an implementation of the Task 6 `CatalogCrypto` contract plus `decrypt(key, iv, ciphertext, additionalData): Promise<Uint8Array>`. Use the same canonical authenticated metadata builder exported from exchange `catalog.ts` for encryption and decryption; `additionalData` contains business ID, module ID, module version, schema and key ID, excluding ciphertext hash (which cannot exist before encryption). Store only ciphertext for private catalog modules; keys persist separately in enrollment. Decrypted catalog objects live in memory. Active/pending enrollment rows hold the reusable credential; this is simple catalog protection, not protection from the enrolled device owner.

- [ ] **Step 1: Write staged-update tests.** Create `apps/field/test/catalog-fixture.ts` exporting `catalogHarness()` using fake IndexedDB, the real Web Crypto adapter and an in-memory fetch map; its API is `{store, deps, publish(input), corruptModule(id), fetches, close()}`. `publish` calls `buildCatalogRelease` and replaces the map's current manifest/artifacts, while preserving references only as specified by the release. Add early-QR and failure tests.

```ts
import 'fake-indexeddb/auto';
import { expect, it } from 'vitest';
import { acceptEnrollment } from '../src/enrollment.ts';
import { refreshCatalog, readActiveCatalog } from '../src/catalog-client.ts';
import { catalogHarness } from './catalog-fixture.ts';
import { syntheticCatalogBuild, enrollmentFor } from '../../../packages/exchange/test/fixtures.ts';
it('keeps active key/catalog when a future QR is scanned before publication', async () => {
  const h = await catalogHarness(); const v1 = syntheticCatalogBuild();
  await h.publish(v1);
  await acceptEnrollment(enrollmentFor(v1), false, h.store);
  expect((await refreshCatalog(h.deps)).status).toBe('updated');
  const v2 = {...v1, key: {id: 'key-2', rawBase64: btoa(String.fromCharCode(...new Uint8Array(32).fill(2)))}};
  await acceptEnrollment(enrollmentFor(v2), false, h.store);
  expect((await h.store.getEnrollment()).active?.key.id).toBe(v1.key.id);
  expect((await refreshCatalog(h.deps)).status).toBe('unchanged');
  expect((await h.store.getEnrollment()).pending?.key.id).toBe('key-2');
  await h.publish(v2); h.corruptModule('pricing');
  expect((await refreshCatalog(h.deps)).status).toBe('invalid');
  expect((await h.store.getEnrollment()).active?.key.id).toBe(v1.key.id);
  expect((await readActiveCatalog(h.store, h.deps.crypto))?.manifest.releaseId).toBe(v1.manifest.releaseId);
  await h.close();
});
it('reports unknown key before downloading private modules', async () => {
  const h = await catalogHarness(); await h.publish(syntheticCatalogBuild());
  expect((await refreshCatalog(h.deps)).status).toBe('registration-update-required');
  expect(h.fetches.filter(path => path.endsWith('.bin'))).toEqual([]);
  await h.close();
});
```

  `enrollmentFor(input)` is added to exchange test fixtures and returns the same schema from every enrollment method. Add tests for successful retry rotating both key/catalog, replacing a pending key requiring confirmation, harmless active-key rescan, a fresh pending registration surviving incompatible release, unchanged module skipping, bad checksum/AES tag/schema/cross-reference, and app/engine mismatch distinct from missing key. A module fetch is limited to 5 MiB and the manifest to 64 KiB; reject too many modules and non-allowlisted module IDs.
- [ ] **Step 2: Run red.** `npm test -- apps/field/test/catalog-client.test.ts apps/field/test/enrollment.test.ts apps/field/test/qr.test.ts`.
- [ ] **Step 3: Implement the bounded activation state machine.** Fetch current manifest with `cache:'no-store'`; validate same business/origin, schemas, exact engine compatibility and supported minimum app version. Check key ID before private fetch. Choose matching active or pending key; download only absent/changed modules, verify size/hash, decrypt and validate both modules/cross-references. Keep staged bytes in memory until validated; do all network, hashing, decryption and schema work before entering IndexedDB transactions (crypto awaits can let Safari transactions expire). Serialize refresh/enrollment mutations through one small in-process queue and compare the expected enrollment/catalog revision again at commit, aborting stale work if a new QR changed it; then one Dexie transaction writes module rows, active manifest, active key and last successful check, removes the matching pending row, and discards obsolete active key/unreferenced catalog ciphertext. Failure leaves the existing state untouched. Never clear drafts/quotes/outbox.

```ts
await db.transaction('rw', db.enrollment, db.catalogModules, db.catalogState, async () => {
  for (const module of activation.modules) await db.catalogModules.put(module);
  await db.catalogState.put({id: 'active', manifest: activation.manifest,
    lastSuccessfulCheck: activation.checkedAt});
  if (activation.promotePending) {
    await db.enrollment.put({slot: 'active', value: activation.enrollment});
    await db.enrollment.delete('pending');
  }
  // Delete only catalog module rows not referenced by this active manifest.
});
```

  Implement the referenced-row deletion in the same transaction. A pending key unrelated to the matching active release remains pending. Distinguish last attempted check from last successful check; offline/error status never changes catalog effective date. Foreground launch/visibility and Check for updates share a single-flight refresh; use a 15-minute interval only while visible. No background guarantees.

  `platform/qr.ts` uses `getUserMedia` plus jsQR on a canvas frame, stops camera tracks on success/cancel/unmount, and decodes a user-selected QR image through the same decoder. Pasted JSON calls the same parser. Enforce exact production origin/business; a different business is an explicit error, not an implicit replacement. Treat QR text as data only; never log/publish the raw credential. Permission denial leaves pasted/image paths usable. No camera/BarcodeDetector support is assumed on Safari.
- [ ] **Step 4: Run green and offline browser checks.** Run field tests/typecheck/build. Enroll a synthetic preview from pasted JSON and image, install v1, check offline cached decryption, publish a same-key price-only update and confirm design is not downloaded. Close/reopen the database while the page remains loaded, without network. Cold offline application launch is tested after Task 10 adds app-shell caching. Record that fake IndexedDB/desktop results do not prove iPhone/iPad retention; physical checks remain Task 10.
- [ ] **Step 5: Commit.** `git add apps/field packages/exchange docs/trial/field-workflow.md docs/trial/publishing.md package-lock.json` then `git commit -m "feat: enroll devices and activate catalog updates atomically"`.

## Task 9: Immutable field outbox and reviewed idempotent office import

**Files:** Create exchange `field-package.ts`, `import-plan.ts`, tests `field-package.test.ts`, `import-plan.test.ts`; field `platform/sharing.ts`, `outbox-service.ts`, test `outbox.test.ts`; office `server/import-service.ts`, `ui/Imports.tsx`, test `import-service.test.ts`; extend stores/contracts/HTTP/Outbox and docs.

**Interfaces:** `prepareFieldPackage(content: FieldContent, deps: PackageDeps): Promise<FieldPackage>`; `validateFieldPackage(bytes: Uint8Array, sha256): Promise<FieldPackage>`; `sharePackage(pkg: FieldPackage, adapter: ShareAdapter, store: FieldStore): Promise<'handed-to-target'|'downloaded'|'cancelled'>`; `previewImport(pkg: FieldPackage, context: ImportContext): ImportPreview`; `acceptImport(preview: ImportPreview, choices: ImportChoices, store: OfficeStore): ImportReceipt`.

```ts
export type FieldContent = { schema: 1; deviceId: string; businessId: string;
  customer: Customer; job: JobDraft; quotes: FrozenQuote[];
  officeBaseRevision: number | null; catalogReleaseId: string;
  designVersion: string; calculatorVersion: string };
export type FieldPackage = { schema: 1; id: string; createdAt: string;
  previousPackageId: string | null; contentHash: string; content: FieldContent };
export type OutboxRecord = { id: string; jobId: string; package: FieldPackage;
  state: 'prepared' | 'handed-to-target' | 'office-confirmed';
  lastShareAt: string | null; confirmedAt: string | null };
export type ImportChoices = { customer: { action: 'create' } | { action: 'link'; officeId: string };
  job: { action: 'create' } | { action: 'link'; officeId: string; expectedRevision: number };
  resolution: 'retain-office-draft' | 'save-submitted-as-new-draft';
  reviewedConflicts: string[] };
export type ImportReceipt = { packageId: string; contentHash: string;
  customerId: string; jobId: string; importedAt: string; duplicate: boolean };
```

`PackageDeps` provides `newId`, `now`, `sha256` and `findByContentHash(hash): Promise<FieldPackage|null>` plus `previousPackageId`; hash canonical **content**, excluding envelope ID/time/previous ID. The package checksum is `contentHash`; validates all content bytes after canonical parsing. Same content returns the already stored immutable package; changed content gets a new ID and previous-package link. Outbox timestamps/state are mutable separate metadata, never edits to the package body. `ShareAdapter` has `canShare(file): boolean`, `share(file): Promise<void>`, `download(file): Promise<void>`; sharing a JSON File is user initiated. Recipient is visibly shown from business settings, but user chooses target and taps Send; no mailto attachment or delivery claim.

`ImportContext` provides existing package hash, known identity mappings and selected office customer/job revisions. Mapping key is `(businessId, deviceId, sourceEntityType, sourceId)`. `ImportPreview` contains validated package, resolved/suggested target IDs, current revisions, conflict codes (`MISSING_BASE`, `STALE_BASE`, `IDENTITY_CHOICE`, `ID_CONTENT_CONFLICT`), a human-readable change list and an immutable hash of the preview context. Sender/name/address similarities are suggestions only.

- [ ] **Step 1: Write package/outbox/import tests.** Add `syntheticFieldContent()`, `memoryPackageDeps()` and `importHarness()` fixtures to exchange/office test helpers. The office harness uses a temp real SQLite DB and exports `{store, seedExisting(), preview(pkg), accept(preview, choices), counts(), close()}`; seedExisting returns customer/job IDs and current revision.

```ts
import { expect, it } from 'vitest';
import { prepareFieldPackage } from '../src/field-package.ts';
import { syntheticFieldContent, memoryPackageDeps } from './fixtures.ts';
it('resend preserves package identity; changed work creates a linked package', async () => {
  const deps = memoryPackageDeps(); const content = syntheticFieldContent();
  const first = await prepareFieldPackage(content, deps); deps.remember(first);
  const again = await prepareFieldPackage(content, deps);
  expect(again.id).toBe(first.id);
  const changed = await prepareFieldPackage({...content, job: {...content.job,
    requirements: 'different scope'}}, {...deps, previousPackageId: first.id});
  expect(changed.id).not.toBe(first.id);
  expect(changed.previousPackageId).toBe(first.id);
});
```

```ts
// apps/office/test/import-service.test.ts
it('deduplicates and remembers explicit source-ID links for later packages', async () => {
  const h = await importHarness(); const target = h.seedExisting();
  const pkg = await h.makePackage({officeBaseRevision: null});
  const choices: ImportChoices = {customer: {action: 'link', officeId: target.customerId},
    job: {action: 'link', officeId: target.jobId, expectedRevision: target.revision},
    resolution: 'retain-office-draft', reviewedConflicts: ['MISSING_BASE']};
  const receipt = h.accept(h.preview(pkg), choices);
  expect(h.accept(h.preview(pkg), choices).duplicate).toBe(true);
  const later = await h.makePackage({officeBaseRevision: null, previousPackageId: pkg.id,
    requirements: 'revised measured scope'});
  expect(h.preview(later).resolvedJobId).toBe(target.jobId);
  expect(h.counts()).toMatchObject({customers: 1, jobs: 1, imports: 1});
  expect(receipt.customerId).toBe(target.customerId); await h.close();
});
```

  Define `makePackage(change: {officeBaseRevision: number|null; previousPackageId?: string; requirements?: string}): Promise<FieldPackage>` on the harness; copy its explicit requirements change into field content. Import `ImportChoices` from exchange contracts in this test. A resend with unchanged content correctly reuses the first package. Additional tests: same ID/different content conflicts; oversized/unsupported/corrupt/reference-invalid input rejected; cancelled preview writes nothing; stale preview is rejected if office revision changes before acceptance; injected transaction failure rolls back customer/job/mapping/ledger; source times stay unchanged.
- [ ] **Step 2: Run red.** `npm test -- packages/exchange/test/field-package.test.ts packages/exchange/test/import-plan.test.ts apps/field/test/outbox.test.ts apps/office/test/import-service.test.ts`.
- [ ] **Step 3: Implement prepare/share/review/commit.** Prepare persists the exact package/outbox before offering sharing. Display “Contains customer and internal estimate data; send to [configured recipient].” Save/download is not mail delivery; successful share becomes Handed to target; cancellation leaves Prepared. Only explicit owner confirmation after office import sets Office-confirmed. Re-export the retained body on resend, even after key rotation.

```ts
// Import acceptance, inside one SQLite transaction after rechecking preview revisions.
const prior = store.findImport(pkg.id);
if (prior && prior.contentHash !== pkg.contentHash) throw new Error('ID_CONTENT_CONFLICT');
if (prior) return {...prior, duplicate: true};
store.insertReceivedSubmission(pkg); // immutable original, with source IDs intact
store.applyReviewedImport(pkg, choices); // only selected fields/new draft, never blind replacement
store.saveSourceMappings(pkg, resolvedOfficeIds);
store.insertImportReceipt(receipt);
```

  Add these internal repository methods in `import-service.ts`/`database.ts`; public `acceptImport` owns the transaction. For linked jobs, the simple trial choices are retain office draft and retain the submission, or create a new office draft revision from the reviewed submission (with selected customer/job IDs rewritten in the office copy). Do not mutate the submitted draft or its frozen quotes; store imported quotes as immutable source snapshots linked to the target office job using a separate association. The submitted Preliminary status stays Preliminary. To issue, office reviews/calculates a draft and creates its own new snapshot. Recheck target revisions and mappings at commit; a changed preview requires renewed review. Existing known mappings preselect targets but do not waive stale/missing-base conflict review. UI shows original source values and target values before acceptance.

  Schema validation rejects prototype/extra fields, bad UUID references, unrecognized calculator/schema versions and wrong business. Checksum establishes corruption detection only. Render notes as text; no HTML/eval/agent execution. Explicitly test payload strings containing instruction-like text remain inert notes.
- [ ] **Step 4: Run green and a manual round trip.** Run the test command/typecheck/both builds. Export a synthetic field package, download it, import on Mac, link to an existing test customer/job and import again; verify one ledger entry and retained original. Change field content and verify the next package resolves through the mapping but requires missing/stale-base review. Use the actual iPhone/iPad share flows in Task 10; do not send mail from automated code.
- [ ] **Step 5: Commit.** `git add packages/exchange apps/field apps/office docs/trial package-lock.json` then `git commit -m "feat: review and deduplicate field submissions"`.

## Task 10: Backups, safe app upgrades and real-device trial release

**Files:** Create office `server/backup-service.ts`, `ui/Backup.tsx`, test `backup.test.ts`; field `update-controller.ts`, `sw.ts`, `scripts/{build-sw,stage-release}.mjs`, `public/{manifest.webmanifest,icon-192.png,icon-512.png}`, tests `update-controller.test.ts`, `recovery.test.ts`; create `scripts/{verify-deploy,trial-fixture}.mjs`, `docs/trial/recovery.md`, `docs/trial/acceptance.md`; modify app build/lifecycle/store/files/publishing interfaces and native-capability log only with observed results.

**Interfaces:** `createBackup(store: OfficeStore, destination: string): Promise<BackupManifest>`; `restoreBackup(source: string, destination: string): Promise<void>`; `exportFieldRecovery(store: FieldStore): Promise<Uint8Array>`; `importFieldRecovery(bytes, store): Promise<RecoveryPreview>` followed by `acceptFieldRecovery(preview, choices): Promise<void>`. `BackupManifest` schema 1 lists database, attachments, settings, catalog archives/recovery keys with relative paths/byte lengths/SHA-256 and creation time. Field recovery is a versioned plaintext file of self-contained drafts/quotes/outbox/customer snapshots with checksum and business/device IDs, **excluding catalog credentials**; reacquire enrollment separately after storage loss. `RecoveryPreview` shows new/conflicting IDs; exact existing records are no-ops, conflicting content requires explicit keep-existing or import-as-copy decisions; never silently overwrite.

`requestAppActivation(input: {dirty: boolean; saving: boolean; waitingVersion: string|null}, actions: {flush(): Promise<void>; activate(): Promise<void>}): Promise<'deferred'|'activated'>` defers when dirty/saving unless called by explicit Save and update after a successful flush. `checkStoredCompatibility(store): Promise<boolean>` reads existing v1 enrollment/catalog/jobs/quotes/outbox before activation; unsupported stores remain on the current app and show recovery guidance. No destructive migration or account setup.

- [ ] **Step 1: Write failure/recovery/update tests.** Back up a real test DB with a quote, import receipt/mapping, attachment and local recovery key; restore to a new directory and compare those identities/bytes, then retry a previously imported package and assert duplicate. Inject hash failure and verify the existing destination is untouched. Use Node `backup()` for a consistent SQLite snapshot while holding a brief application write lock across DB/file-manifest capture; disallow catalog/import/attachment mutations during backup. Restore validates into a sibling staging directory with the service stopped, runs SQLite integrity/foreign-key checks, then swaps directories; preserve the pre-restore directory until owner verifies it.

```ts
import { expect, it, vi } from 'vitest';
import { requestAppActivation, saveAndActivate } from '../src/update-controller.ts';
it('never activates over an unsaved edit', async () => {
  const actions = {flush: vi.fn(), activate: vi.fn()};
  expect(await requestAppActivation({dirty: true, saving: false, waitingVersion: '1.0.1'}, actions))
    .toBe('deferred');
  expect(actions.activate).not.toHaveBeenCalled();
});
it('a failed Save and update preserves the current app', async () => {
  const actions = {flush: vi.fn().mockRejectedValue(new Error('quota')), activate: vi.fn()};
  await expect(saveAndActivate(actions)).rejects.toThrow('quota');
  expect(actions.activate).not.toHaveBeenCalled();
});
```

  Define `saveAndActivate(actions: {flush(): Promise<void>; activate(): Promise<void>}): Promise<void>` in update-controller: await flush, await compatibility check through the activation adapter, then activate. No `finally` activation. Add tests for pending outbox preservation, malformed recovery checksum, conflicts requiring choices and failed recovery transaction rollback. These tests complement actual service-worker/device checks; they do not establish them.
- [ ] **Step 2: Run red.** `npm test -- apps/office/test/backup.test.ts apps/field/test/recovery.test.ts apps/field/test/update-controller.test.ts`.
- [ ] **Step 3: Implement backup/export and a narrow app-shell service worker.** Backup UI chooses destination, reports success only after copied artifacts/hashes verify, and explains that the backup includes private recovery keys. Do not put backups in static staging; do not add another encryption/key system. Field UI offers export recovery from Jobs/Outbox, preserves originals during failed writes and clearly distinguishes local save from office backup.

  `build-sw.mjs` takes the Expo output's exact asset list and app version, transpiles the import-free `sw.ts` using pinned TypeScript `transpileModule`, and emits `sw.js` plus a precache list. `stage-release.mjs` merges only built app files and Task 6's selected encrypted modules/current manifest. App metadata/icons are plain generated local assets (a simple high-contrast “PE” icon rendered to 192/512 PNG by a small canvas export in the browser during setup is sufficient); no image-generation or design platform is required.

```ts
// sw.ts: essential control flow, with precache list injected by build-sw.mjs.
self.addEventListener('install', event => {
  event.waitUntil(caches.open(APP_CACHE).then(cache => cache.addAll(APP_ASSETS)));
  // Do not call skipWaiting here: an edit may be open in the old app.
});
self.addEventListener('message', event => {
  if (event.data?.type === 'ACTIVATE_READY_APP') void self.skipWaiting();
});
// Fetch handling must exclude /catalog/current.json and /catalog/modules/*.
// Navigation falls back to this version's cached index.html; hashed app assets use its cache.
```

  Define injected `APP_CACHE`, `APP_ASSETS` and `APP_VERSION` explicitly in the build output and include all static chunks/fonts needed offline. Avoid caching catalog requests in the service worker; catalog-client owns encrypted cache. `activate` checks the app build's supported schema/version metadata and performs no IndexedDB changes. Keep previous app-shell cache until the new page reports `APP_BOOT_OK` after reading the store; then remove only older app-shell caches. Do not delete enrollment/job/catalog databases. Controller waits for the waiting worker and a clean saved state; an explicit Save and update awaits flush, then sends activation and reloads on controllerchange. On launch, auto-activate only when no unsaved edit; prepared/unsent submissions remain durable. If storage/compatibility check fails, keep the current version and explain the error. A future breaking schema release is outside this routine path.

  `verify-deploy.mjs` checks that every manifest module and precache asset exists, size/hash matches, no path escapes, and no `.db`, `.sqlite`, `.pem`, raw-key JSON, QR credentials, customer exports or recovery packages are staged. Restrict by allowlisted generated paths rather than filename blacklists alone. Configure current manifest and service-worker responses as revalidate/no-cache; immutable hashed assets may use long cache lifetime. Publish the assembled directory atomically using the owner's existing Cloudflare Pages project/credentials, with no Functions or service additions. Add a documented `wrangler pages deploy <stage-dir> --project-name <owner-selected-project>` command using actual selected values in the local execution record; do not invent a production name/domain in this plan.

- [ ] **Step 4: Run green and the full automated checks once.** Run `npm test -- apps/office/test/backup.test.ts apps/field/test/recovery.test.ts apps/field/test/update-controller.test.ts`, then `npm run verify`. Run `node scripts/verify-deploy.mjs <actual-stage-directory>` after staging. Keep the command arguments in the execution evidence with the actual paths. Confirm a restored Mac quote, import mapping and duplicate ledger behavior against original bytes, and a delayed plaintext package imported after old catalog keys are removed from the device.
- [ ] **Step 5: Perform concrete iPhone/iPad acceptance at the stable origin.** In `docs/trial/acceptance.md`, record app/engine versions, catalog IDs/hashes, device/iOS/browser/install mode, fixture hash, expected/actual result and pass/fail. The one-off `trial-fixture.mjs` emits the canonical synthetic conformance input/results as a downloadable JSON, not a diagnostics platform. Test mode can load it explicitly on Mac/iPhone/iPad and compare quantities, packs, selected tiers, costs and selling/tax totals byte-for-byte. Production UI refuses it as an owner-validated real quote. Repeat the useful workflow with the owner's validated recipe/settings/prices before the first real-job quote.

  Execute this sequence on **both** iPhone and iPad:

  1. Install app **1.0.0** on the chosen stable HTTPS origin, enroll by camera, and separately check QR-image and pasted enrollment. Denied camera permission must leave both recovery paths usable. Populate active catalog, saved draft, frozen Preliminary quote and prepared outbox. Export a local recovery file.
  2. Airplane/offline reopen: read/decrypt catalog and calculate the conformance input, reopen draft/quote/outbox and generate PDF without network. Compare Mac results using the exact same release/inputs; do not compare against refreshed office live prices. Inspect customer PDF visually.
  3. Publish a same-key pricing-only release: foreground updates fetch only changed pricing, preserve design bytes and leave existing draft/quote totals unchanged. Corrupt a preview release, publish incompatible app/engine metadata and try offline refresh: each retains active data and shows the correct status.
  4. Rotate using a pending QR scanned **before** publication. Check active-key access remains; a different pending QR requires explicit confirmation. Publish re-encrypted modules and remove superseded packs from the current file set. On an old-key-only enrollment, verify Registration update required before module download. Interrupt a matching new-key install, reopen offline with old active data, then retry successfully; old draft/quote/outbox still display after old device key/catalog are removed.
  5. Publish a genuinely different app **1.0.1** with visible version text and a distinct app-shell asset hash while the device has active enrollment, **a pending key**, catalog, draft, frozen quote and outbox. Leave an edit unsaved: no reload or activation. Use Save and update; verify failed-save behavior first, then successful activation. Assert all stored records/keys remain byte-equivalent and reopen **1.0.1** offline. Repeat upgrade once from a clean launch. A reload of 1.0.0 is not evidence of this case.
  6. Share the prepared JSON attachment through the device's user-selected mail app, inspect its recipient and send it manually; download/save fallback must also work. Record actual iPad sharing behavior rather than inheriting the earlier iPhone probe result. Import on Mac, link identities, replay the same package, then a changed package. Confirm explicit office-confirmed state only after owner action.
  7. Restore Mac backup into an isolated data directory and field recovery into a separate test browser profile; verify snapshot identities, source mappings, duplicate ledger, attachment and recovery-key bytes. Demonstrate a failed local save leaves the previous durable job available and does not display Saved.

  Record Android **untested/deferred**. Update the native-capability log only with these observed devices/workflows; do not infer native limitations from untested features. If any of acceptance 1–11 fails, fix the owning task's defect and rerun the affected check before real-job use. Missing owner recipe/rates/production origin is an explicit setup dependency, not permission to substitute fixtures.
- [ ] **Step 6: Commit the verified trial.** `git add apps packages scripts docs/trial docs/design/mobile-native-capability-log.md package-lock.json` then `git commit -m "feat: verify recoverable office and field trial release"`. Do not include local databases, recovery keys, real customer exports, catalog secrets or generated deployment directories in Git.

## Dependency pins and execution setup

Technical checks and official sources are recorded in `docs/research/2026-11-01-first-usable-plan-technical-checks.md`. Use these exact initial pins, install at the task that needs them, and commit the resolved lockfile. Registry freshness is not authorization to upgrade during implementation. Expo's SDK-matched packages are preferable to an unrelated latest React Native release.

| Scope | Exact initial dependencies |
| --- | --- |
| Root tooling | `typescript@6.0.3`, `vitest@5.0.5`, `tsx@4.23.15`, `@types/node@26.6.6`, `@types/react@19.3.0`, `@types/react-dom@19.3.0`, `fake-indexeddb@6.2.7` (tests only). |
| Domain | `zod@4.6.7`, `decimal.js@10.6.0`. |
| Exchange/PDF | `zod@4.6.7`, `pdf-lib@1.17.1`. |
| Office | `react@19.3.0`, `react-dom@19.3.0`, `vite@8.3.5`, `qrcode@1.5.4`, `@types/qrcode@1.5.6`; built-in `node:sqlite`, `node:crypto`, `node:http`, filesystem. Vite's basic TSX support is sufficient; do not add React Compiler. |
| Field | `expo@58.0.22`, `react@19.3.0`, `react-dom@19.3.0`, `react-native@0.88.1`, `react-native-web@0.21.4`, `@expo/metro-runtime@58.0.16`, `dexie@4.4.7`, `jsqr@1.4.0`. No Router/native scanner dependency. |

Representative future commands, after the corresponding `package.json` files exist:

```bash
node --version
npm install --save-dev --save-exact typescript@6.0.3 vitest@5.0.5 tsx@4.23.15 @types/node@26.6.6 @types/react@19.3.0 @types/react-dom@19.3.0 fake-indexeddb@6.2.7
npm install --workspace @estimator/domain --save-exact zod@4.6.7 decimal.js@10.6.0
npm install --workspace @estimator/exchange --save-exact zod@4.6.7 pdf-lib@1.17.1
npm install --workspace @estimator/office --save-exact react@19.3.0 react-dom@19.3.0 vite@8.3.5 qrcode@1.5.4
npm install --workspace @estimator/office --save-dev --save-exact @types/qrcode@1.5.6
npm install --workspace @estimator/field --save-exact expo@58.0.22 react@19.3.0 react-dom@19.3.0 react-native@0.88.1 react-native-web@0.21.4 @expo/metro-runtime@58.0.16 dexie@4.4.7 jsqr@1.4.0
npm exec --workspace @estimator/field -- expo install --check
```

Define package exports as `".": "./src/index.ts"` for shared packages and use explicit `.ts` relative imports in their source/tests. Use `module: "ESNext"`, `moduleResolution: "Bundler"`, `allowImportingTsExtensions: true`, `noEmit: true`, `strict: true`, and `jsx: "react-jsx"`; `tsc --noEmit` checks each workspace. Vite, Expo Metro and Vitest consume the same source entrypoints; office Node starts with the pinned `tsx` runner so no unbuilt TypeScript is passed to unsupported runtime paths. Office scripts: `dev` starts local API and Vite using `apps/office/scripts/dev.mjs` (create in Task 4; Node spawn supervisor); `build` runs Vite; `start` serves the built UI from Node. Field `start` runs Expo web. Task 7's `build` runs Expo web export only; Task 10 appends `build-sw.mjs` after creating it. Task 4's real Vite build and Task 7's real Expo export are required consumer-resolution gates, not just typechecks; resolve any SDK/Metro incompatibility before continuing. Root build runs only app builds; shared libraries are typechecked and bundled by consumers. Add missing script/config files within the owning task, not an infrastructure-only deliverable. The office dev supervisor stops both children on exit and never binds LAN interfaces.

## Trial acceptance coverage and stop condition

| Spec acceptance | Owning tasks and evidence |
| --- | --- |
| 1 Catalog/history/settings | 2, 4, 6: append/correct/select tests, manual entry, private module inspection. |
| 2 Geometry/purchases | 1–3: all three 150-ft counts, connected returns, short cuts, no-reuse purchase/cost. |
| 3 Manual work | 3–5, 7: allowance confirmations, normal pricing and frozen preservation. |
| 4 Preserved proposals | 4–5, 7: draft/current-input check, immutable status/snapshot, explicit reprice. |
| 5 Segment totals/disclosure | 2–3, 5: allocation conservation, tax/overrides and strict proposal projection/PDF inspection. |
| 6 Import identity | 7, 9: durable outbox, duplicate/conflict/mapping/review transaction. |
| 7 Catalog refresh | 6, 8: changed-only modules, compatibility, key-specific errors, offline decrypt. |
| 8 Actual app upgrade | 10: 1.0.0 → 1.0.1 with active/pending enrollment and existing work, dirty edit, offline reopen. |
| 9 Rotation | 6, 8, 10: early QR, unknown key, interrupted activation, old snapshot independence and current-pack removal. |
| 10 Recovery | 4, 7, 9–10: failed-save truthfulness, full office restore and delayed plaintext submission. |
| 11 Device parity | 1–3, 7, 10: identical-release fixtures on Mac/iPhone/iPad; Android explicitly untested. |

The trial is ready only when all 11 trial cases pass with recorded device evidence, owner recipe/settings are validated, production-origin setup is complete, and a real Mac quote can be produced and recovered. This plan does not create backlog issues, authorize implementation, or include deferred complete-v1 features. Planning ends after plan review/SAR; execution awaits the owner's later instruction.
