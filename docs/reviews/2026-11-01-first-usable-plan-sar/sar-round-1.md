# SAR round 1 — first usable trial plan

Reviewer/author: **Astra 6, high reasoning**, same agent `/root/astra_trial_plan`. This is same-agent iterative review (SAR), not independent cross-provider review. No implementation/build/device check was performed.

Input plan: `docs/superpowers/plans/2026-11-01-first-usable-project-estimator.md`, commit `961a6cf`, SHA-256 `8819faa193ffdc73a5f3d6686a53a1155648700687ec7d123467bf2034531228`.

Scope authority: `docs/superpowers/specs/2026-11-01-project-estimator-pwa-v1-design.md`, SHA-256 `0971e6426aadf888a3652d9fae78707793f4af7f4b221e5b577ef8deca253f2c`. Read the full spec, full plan and `parent-coverage-check.md`. The locations below refer to this input plan, before edits.

## Findings recorded before revision

| ID | Location | Concrete defect and impact | Minimal correction |
| --- | --- | --- | --- |
| SAR1-01 | Task 2 lines 196–225; Task 4 lines 376, 424 | Observations are immutable but their referenced offer/component economics can be edited through `saveCatalog`; old pack/unit/branch/spec history could be reinterpreted. | Make component/offer identity immutable once referenced; changed economic context gets a new ID. Keep prior identities in history, enforce references and test attempted pack/spec changes. |
| SAR1-02 | Common contracts line 92; Task 2 lines 213–225, 264–278; Task 3 line 368 | Requirements have no unit/stock context despite required mismatch checks; “all monetary outputs two decimals” would round fractional per-unit costs too early; `preTaxCost` claims a basis that may be unknown for tax-included observations. Unused stock covers cuts but omits extra whole stock from pack/waste rounding. | Add explicit requirement units/stock length, preserve unit-cost precision, name observed cost versus added tax truthfully, and report/test full pooled unused stock/allowance purchases. |
| SAR1-03 | Task 4 lines 438–455; Task 7 lines 608–650 | The generic 5 MiB JSON-only endpoint rule makes the planned 20 MiB file attachment route unusable. Async autosave can report Saved for an old edit while a newer edit is pending. | Define one explicit bounded binary attachment route and preserve same-origin checks. Serialize per-job writes and guard Saved by current edit generation; test an edit arriving during save. |
| SAR1-04 | Tasks 5–7 lines 461–463, 551–560, 648–651; Task 9 lines 742–746 | Contract/code ownership is incomplete: build mode exists only in prose, exchange index/office crypto are introduced after first use, unnamed office calculation entrypoint is invoked in parity tests, and helper APIs gain methods outside their declarations. | Put all operational fields in final blocks, introduce files at first use, name calculation wrappers and helper methods, and reconcile package build phases. |
| SAR1-05 | Task 5 lines 463, 487–509; Task 7 line 648; Task 10 line 854 | Synthetic freeze gating is partly a public environment flag. It is unclear how production adapters prevent a flag/request from selecting bypass mode, and physical production upgrade checks could accidentally use a test build. | Hard-code production policies in production adapters; inject preview mode only in test harnesses using isolated data. Keep device conformance calculation separate from production quote/publication readiness; add explicit rejection tests. |
| SAR1-06 | Task 8 lines 658, 698–711 | Prose asks for CAS but the shown transaction overwrites state without checking or incrementing revision; `CatalogActivation` fields used by code are not specified. The rotation fixture reuses its aggregate release ID despite a different manifest. | Show the actual revision precondition/increment and exact activation payload, retain unrelated pending keys, add a stale-update test, and give rotated manifests a new release ID. |
| SAR1-07 | Task 9 lines 742, 787–799; Task 10 line 807 | Rejecting unrecognized calculator versions can prevent display/recovery of a delayed self-contained package despite compatible schema. Imported quote linkage has no owned table. Recovery “import-as-copy” can alter frozen quote/package identities and checksums. | Accept compatible-schema snapshots with calculator provenance as data; require current recalculation before a new office issue. Own quote-link storage; preserve identities and use keep-existing/abort-or-empty-store recovery rather than rewriting frozen records. |
| SAR1-08 | Task 10 lines 805–849 | No worker registration function, manifest link/bootstrap, explicit app metadata handshake or typed worker build context is assigned. `skipWaiting` does not use event lifetime. Safe update prose does not cover another open editing client. | Own registration/metadata/build scripts and show activation messaging. Check all open app clients are clean/compatible before activation; preserve previous assets until clients acknowledge safe boot. Add concrete controller checks without a new framework. |
| SAR1-09 | Task 10 line 807; backup step lines 811–827 | Recovery implementations lack exact files/types; backup hash/identity/rollback checks are prose only, while all shown test code exercises update control. | Assign recovery implementation/contracts, and add a real illustrative backup/restore/dedup test with concrete fixture API and assertions. |
| SAR1-10 | Task 5 lines 517–530; Task 3 lines 301–313 | Recipe assumptions/exclusions are not explicitly copied into the selected customer-facing draft, and the PDF standard-font path can fail on an unsupported character without a defined recoverable outcome. Job-level null markup fallback also lacks a pinned test. | Copy recipe defaults at draft creation for owner review, preserve them in snapshots, define safe unsupported-font feedback, and test job-default markup fallback. |

These are plan consistency/executability findings, not requests for new product scope. The post-count fixtures, corrected 6,528-u16 offcut example, markup/override tax formula, private catalog versus ordinary job-storage separation, reviewed import boundary and deferred-feature exclusions remain sound.

## Owner data versus defects

No new owner decision blocks finishing this plan. The already identified real recipe worksheet, actual prices/labor/markup/tax defaults and stable production origin remain execution/setup dependencies. The plan must not invent these values. Actual runtime/Expo builds, Safari storage/crypto/service-worker behavior, iPhone/iPad sharing and real-device upgrade checks remain future validation work; documentation review cannot pass them.

## Resolution record

Pending plan-only revision after this findings record was saved. Output hash and individual dispositions will be appended after the corrections.

### Applied corrections

All ten findings were addressed in the plan, with no spec or application changes:

- **SAR1-01:** Task 2 defines immutable referenced offer/component context; Task 4 prevents economic-context changes under an old ID and includes a pack-history test. Same-body append is idempotent; changed-body append is rejected.
- **SAR1-02:** Requirements carry units/stock length; purchase results distinguish observed cost/added tax and full unused stock. Fractional-unit and pack-spare tests pin the behavior. Currency subtraction uses Decimal; the only cent-remainder conversion to Number is a bounded integer count.
- **SAR1-03:** One explicit bounded binary attachment route is separate from JSON limits. Office and field save queues/generation guards retain correct dirty/Saved state during concurrent edits.
- **SAR1-04:** Build mode is in the actual contract; exchange entrypoint and office hashing are introduced when needed; office/field calculation wrappers and test helper methods are named. Field browser populated-workflow checks wait for Task 8 catalog support, while Task 7 exercises seeded snapshots in adapter tests.
- **SAR1-05:** Production wrappers hard-code production policy and reject incoming bypass fields. Synthetic freeze policy exists only in Vitest; one-off device conformance is read-only calculation with no quote/publication capability. Production-version upgrade checks use the owner's validated catalog.
- **SAR1-06:** Activation code now checks/increments the exact shared revision before writes, uses only Dexie awaits in the transaction and retains unrelated pending enrollment. Stale-context/early-QR cases and new release identity are explicit.
- **SAR1-07:** Compatible-schema delayed snapshots remain displayable/importable despite older engine provenance; new office quotes require current recalculation. Imported quote-link storage is owned by Task 9 and backed up. Recovery preserves immutable IDs and rejects silent conflict replacement.
- **SAR1-08:** Task 10 owns registration, manifest linking, release metadata, worker TS context, no-cache headers, safe activation messages and event lifetime. Other open app clients cause a simple refusal/close-other-windows instruction; no coordination framework was added.
- **SAR1-09:** Field recovery files/contracts and the concrete temporary-SQLite backup/restore/dedup/attachment/key test harness are specified; restore path/hash/rollback checks are explicit.
- **SAR1-10:** Drafts copy owner-reviewed recipe assumptions/exclusions; PDF unsupported characters cause a recoverable named export error, not silent data loss. Business-default markup fallback has a required test.

Output plan SHA-256: `ea9cc05f885d20c548f881c33fd28f016f0ea603da733ba46564a58c034ac4e0`.

Checks performed: document-only contract comparison, targeted searches, arithmetic inspection and source diff review. No test snippet was executed, no dependencies installed, no app/probe files changed and no deployment made. Proceeding to a complete reread in SAR round 2; this round is not final acceptance.
