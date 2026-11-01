# Response to first independent review

Scope: specification and capability-log corrections only. No application code, backlog, implementation plan, native distribution or new cloud/network infrastructure.

| Finding | Revision |
| --- | --- |
| C1 | Sections 3/4/6 now require immutable preliminary snapshots whenever a quote is presented, exported or shared. Internal draft preview remains distinct. Full alternatives/revision comparison stays complete v1. Trial acceptance 4 checks preservation. |
| C2 | Section 9 adds manually priced quantity/cost-category/segment items with standard pricing rules and snapshot retention. Manual gate costs require net fence runs and explicit support/facing checks; no automated gate designer is added. Trial acceptance 3 checks this. |
| C3 | Installation segments carry their own consumed materials; acquisition carries sourcing/pickup/delivery effort and fees. Job-level packs/tier purchasing is allocated without losing or doubling the purchase total. Trial acceptance 5. |
| C4 | Section 5 pins owner-selected default offers and explicit job overrides, includes tier/discount conditions and deterministic eligible-cost selection. Section 11 includes business/labor/markup/tax settings in the existing private pricing package, not a new settings subsystem. Identical release plus inputs defines parity. Trial acceptance 1/11. |
| C5 | Sections 6/11/12 separate job snapshots and plaintext JSON field attachments from the catalog key. One active plus one pending key; pre-publication scanning preserves the active key. Commit the new key/catalog only after validation, then discard the obsolete device catalog/key. Historical jobs/outbox read their own snapshots. Retired Mac keys recover encrypted catalog archives only. Trial acceptance 9/10. |
| C6 | Import preview offers Create new/Link to existing with explicit confirmation and persistent source-ID mappings for subsequent submissions. Missing base revisions require reviewed merge. Selected office-job file/email transfer is assigned to complete v1. Trial acceptance 6 and complete-v1 acceptance 15. |
| C7 | Section 11 specifies one current manifest, distinct app-update/registration-required states, safe app activation, preservation of the prior shell/data, compatible routine trial schemas and a stable production origin before trial data. No indefinite historical schema support or schema-router service. Actual app-upgrade acceptance 8. |
| C8 | Section 15 now tags/splits every case as Trial or Complete v1 and includes actual Mac/iPhone/iPad calculator parity. Android remains deferred. |
| C9 | Capability log NC-02 is an untested candidate; NC-04 records initial persistent=false and the untested full app upgrade; NC-07 and spec align on pasted/QR-image fallback and its test status. |
| C10 | Section 7 makes no-reuse the visible conservative default when a recipe lacks a feasible cut rule. Unused stock/cost is visible; owner adjustments are manual and no optimizer is added. Trial acceptance 2. |

Business rates and tax settings are owner-entered configuration, not invented numeric defaults. The workweek, initial validated recipe, production origin and proposed incremental cut remain owner-review/setup choices. A separate visible customer discount stays deferred; segment selling-price overrides cover the trial. Friend enrollment retains the already discussed business-catalog access model.
