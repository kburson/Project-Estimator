# First trial sibling delivery issue map

Migration verification PASS: all legacy #1–35 are Done / Replaced and CLOSED / NOT_PLANNED through #36, with historical parent links retained. No application implementation or acceptance is asserted.

Administrative index: [#36](https://github.com/kburson/Project-Estimator/issues/36). This index has no parent, children, integration branch or blocking role.

28 flat sibling epics and 135 children; every child forecast is 2–4 hours (401 total, mean 2.97). These are intake forecasts, not implementation approval or delivery dates. Actual pickup must split work again if its scope exceeds the forecast.

Source-plan commit: `a1f4a7bcefb82e5499219f33c34aed280c76bceb`. Canonical task selectors, prerequisite edges and ownership are pinned in each issue and its sibling plan.

Child → epic branch; every child complete → integrated epic Test/Review → trunk merge → Cloudflare deployment and local Mac build at the same SHA → owner tests both. Cross-epic dependencies consume trunk. One orchestrator, at most three workers globally, including reviewers.

## Canonical replacement issues

### [#37](https://github.com/kburson/Project-Estimator/issues/37) Deliver the first office and field builds

Trunk prerequisites: None. Source plan: [2026-11-01-foundation.md](../superpowers/plans/sibling-delivery/2026-11-01-foundation.md).

| Child | Story | Forecast | Direct prerequisite children |
| --- | --- | ---: | --- |
| [#38](https://github.com/kburson/Project-Estimator/issues/38) | Pin the workspace while retaining AITM | 2 h / XS | None |
| [#68](https://github.com/kburson/Project-Estimator/issues/68) | Validate exact run and measured-length inputs | 3 h / S | [#38](https://github.com/kburson/Project-Estimator/issues/38) |
| [#69](https://github.com/kburson/Project-Estimator/issues/69) | Build and launch the loopback office shell | 3 h / S | [#38](https://github.com/kburson/Project-Estimator/issues/38) |
| [#72](https://github.com/kburson/Project-Estimator/issues/72) | Export the static field application shell | 3 h / S | [#38](https://github.com/kburson/Project-Estimator/issues/38) |
| [#77](https://github.com/kburson/Project-Estimator/issues/77) | Stage only public application assets | 2 h / XS | [#72](https://github.com/kburson/Project-Estimator/issues/72) |
| [#79](https://github.com/kburson/Project-Estimator/issues/79) | Configure trunk-triggered Cloudflare delivery | 3 h / S | [#77](https://github.com/kburson/Project-Estimator/issues/77) |
| [#82](https://github.com/kburson/Project-Estimator/issues/82) | Configure trunk-triggered local server builds | 4 h / S | [#69](https://github.com/kburson/Project-Estimator/issues/69) |
| [#85](https://github.com/kburson/Project-Estimator/issues/85) | Rehearse candidate delivery before the first trunk merge | 2 h / XS | [#68](https://github.com/kburson/Project-Estimator/issues/68), [#79](https://github.com/kburson/Project-Estimator/issues/79), [#82](https://github.com/kburson/Project-Estimator/issues/82) |

### [#40](https://github.com/kburson/Project-Estimator/issues/40) Maintain vendor and component identities

Trunk prerequisites: [#37](https://github.com/kburson/Project-Estimator/issues/37). Source plan: [2026-11-01-catalog.md](../superpowers/plans/sibling-delivery/2026-11-01-catalog.md).

| Child | Story | Forecast | Direct prerequisite children |
| --- | --- | ---: | --- |
| [#67](https://github.com/kburson/Project-Estimator/issues/67) | Store validated catalog identities | 3 h / S | None |
| [#70](https://github.com/kburson/Project-Estimator/issues/70) | Edit vendors and component specifications | 3 h / S | [#67](https://github.com/kburson/Project-Estimator/issues/67) |
| [#73](https://github.com/kburson/Project-Estimator/issues/73) | Edit explicitly identified vendor offers | 3 h / S | [#67](https://github.com/kburson/Project-Estimator/issues/67) |
| [#76](https://github.com/kburson/Project-Estimator/issues/76) | Reject changes to referenced economic context | 2 h / XS | [#67](https://github.com/kburson/Project-Estimator/issues/67) |
| [#80](https://github.com/kburson/Project-Estimator/issues/80) | Create replacement identities for economic edits | 2 h / XS | [#70](https://github.com/kburson/Project-Estimator/issues/70), [#73](https://github.com/kburson/Project-Estimator/issues/73), [#76](https://github.com/kburson/Project-Estimator/issues/76) |

### [#39](https://github.com/kburson/Project-Estimator/issues/39) Keep dated prices and deliberate business settings

Trunk prerequisites: [#40](https://github.com/kburson/Project-Estimator/issues/40). Source plan: [2026-11-01-prices.md](../superpowers/plans/sibling-delivery/2026-11-01-prices.md).

| Child | Story | Forecast | Direct prerequisite children |
| --- | --- | ---: | --- |
| [#66](https://github.com/kburson/Project-Estimator/issues/66) | Append and correct immutable price observations | 3 h / S | None |
| [#71](https://github.com/kburson/Project-Estimator/issues/71) | Enter known prices and permitted arrangements | 4 h / S | [#66](https://github.com/kburson/Project-Estimator/issues/66) |
| [#74](https://github.com/kburson/Project-Estimator/issues/74) | Require explicit business labor markup and tax decisions | 3 h / S | [#66](https://github.com/kburson/Project-Estimator/issues/66) |
| [#78](https://github.com/kburson/Project-Estimator/issues/78) | Choose defaults and inspect dated corrections | 3 h / S | [#71](https://github.com/kburson/Project-Estimator/issues/71), [#74](https://github.com/kburson/Project-Estimator/issues/74) |

### [#41](https://github.com/kburson/Project-Estimator/issues/41) Explain bays and shared posts

Trunk prerequisites: [#37](https://github.com/kburson/Project-Estimator/issues/37). Source plan: [2026-11-01-bays.md](../superpowers/plans/sibling-delivery/2026-11-01-bays.md).

| Child | Story | Forecast | Direct prerequisite children |
| --- | --- | ---: | --- |
| [#81](https://github.com/kburson/Project-Estimator/issues/81) | Record the owner single-recipe decision | 2 h / XS | None |
| [#84](https://github.com/kburson/Project-Estimator/issues/84) | Validate versioned recipe rules | 3 h / S | [#81](https://github.com/kburson/Project-Estimator/issues/81) |
| [#86](https://github.com/kburson/Project-Estimator/issues/86) | Calculate exact bays and unique post identities | 3 h / S | [#84](https://github.com/kburson/Project-Estimator/issues/84) |
| [#89](https://github.com/kburson/Project-Estimator/issues/89) | Inspect geometry and named invalid inputs | 3 h / S | [#86](https://github.com/kburson/Project-Estimator/issues/86) |

### [#42](https://github.com/kburson/Project-Estimator/issues/42) Explain material cuts and stock requirements

Trunk prerequisites: [#41](https://github.com/kburson/Project-Estimator/issues/41), [#40](https://github.com/kburson/Project-Estimator/issues/40). Source plan: [2026-11-01-requirements.md](../superpowers/plans/sibling-delivery/2026-11-01-requirements.md).

| Child | Story | Forecast | Direct prerequisite children |
| --- | --- | ---: | --- |
| [#83](https://github.com/kburson/Project-Estimator/issues/83) | Retain owner-validated recipe versions | 3 h / S | None |
| [#87](https://github.com/kburson/Project-Estimator/issues/87) | Derive installed material requirements | 4 h / S | None |
| [#90](https://github.com/kburson/Project-Estimator/issues/90) | Retain cuts and conservative stock use | 3 h / S | [#87](https://github.com/kburson/Project-Estimator/issues/87) |
| [#93](https://github.com/kburson/Project-Estimator/issues/93) | Count fasteners from installed pieces | 3 h / S | [#87](https://github.com/kburson/Project-Estimator/issues/87) |
| [#96](https://github.com/kburson/Project-Estimator/issues/96) | Explain requirements and unused stock | 3 h / S | [#83](https://github.com/kburson/Project-Estimator/issues/83), [#90](https://github.com/kburson/Project-Estimator/issues/90), [#93](https://github.com/kburson/Project-Estimator/issues/93) |

### [#43](https://github.com/kburson/Project-Estimator/issues/43) Explain purchased packs and eligible prices

Trunk prerequisites: [#42](https://github.com/kburson/Project-Estimator/issues/42), [#39](https://github.com/kburson/Project-Estimator/issues/39). Source plan: [2026-11-01-purchases.md](../superpowers/plans/sibling-delivery/2026-11-01-purchases.md).

| Child | Story | Forecast | Direct prerequisite children |
| --- | --- | ---: | --- |
| [#88](https://github.com/kburson/Project-Estimator/issues/88) | Pool requirements before package rounding | 3 h / S | None |
| [#92](https://github.com/kburson/Project-Estimator/issues/92) | Select only permitted pricing arrangements | 4 h / S | [#88](https://github.com/kburson/Project-Estimator/issues/88) |
| [#94](https://github.com/kburson/Project-Estimator/issues/94) | Extend tax-inclusive costs and allocate cents | 4 h / S | [#88](https://github.com/kburson/Project-Estimator/issues/88) |
| [#97](https://github.com/kburson/Project-Estimator/issues/97) | Compose purchase provenance and named failures | 2 h / XS | [#92](https://github.com/kburson/Project-Estimator/issues/92), [#94](https://github.com/kburson/Project-Estimator/issues/94) |
| [#100](https://github.com/kburson/Project-Estimator/issues/100) | Inspect pack spares and selected-price provenance | 3 h / S | [#97](https://github.com/kburson/Project-Estimator/issues/97) |

### [#44](https://github.com/kburson/Project-Estimator/issues/44) Calculate complete segment costs

Trunk prerequisites: [#43](https://github.com/kburson/Project-Estimator/issues/43). Source plan: [2026-11-01-costs.md](../superpowers/plans/sibling-delivery/2026-11-01-costs.md).

| Child | Story | Forecast | Direct prerequisite children |
| --- | --- | ---: | --- |
| [#91](https://github.com/kburson/Project-Estimator/issues/91) | Define estimate inputs and production readiness | 2 h / XS | None |
| [#95](https://github.com/kburson/Project-Estimator/issues/95) | Attribute materials and person-hour costs once | 3 h / S | [#91](https://github.com/kburson/Project-Estimator/issues/91) |
| [#98](https://github.com/kburson/Project-Estimator/issues/98) | Cost manual work without inventing geometry or hours | 3 h / S | [#91](https://github.com/kburson/Project-Estimator/issues/91) |
| [#101](https://github.com/kburson/Project-Estimator/issues/101) | Apply segment selling rules and customer tax | 3 h / S | [#91](https://github.com/kburson/Project-Estimator/issues/91) |
| [#104](https://github.com/kburson/Project-Estimator/issues/104) | Compose complete and incomplete estimate results | 3 h / S | [#95](https://github.com/kburson/Project-Estimator/issues/95), [#98](https://github.com/kburson/Project-Estimator/issues/98), [#101](https://github.com/kburson/Project-Estimator/issues/101) |
| [#107](https://github.com/kburson/Project-Estimator/issues/107) | Expose a read-only Mac conformance calculation | 3 h / S | [#104](https://github.com/kburson/Project-Estimator/issues/104) |

### [#45](https://github.com/kburson/Project-Estimator/issues/45) Save and reopen calculated site visits

Trunk prerequisites: [#44](https://github.com/kburson/Project-Estimator/issues/44). Source plan: [2026-11-01-visits.md](../superpowers/plans/sibling-delivery/2026-11-01-visits.md).

| Child | Story | Forecast | Direct prerequisite children |
| --- | --- | ---: | --- |
| [#99](https://github.com/kburson/Project-Estimator/issues/99) | Define validated customer and calculated-job persistence | 2 h / XS | None |
| [#102](https://github.com/kburson/Project-Estimator/issues/102) | Persist customer identities and contact history | 2 h / XS | [#99](https://github.com/kburson/Project-Estimator/issues/99) |
| [#105](https://github.com/kburson/Project-Estimator/issues/105) | Persist and reopen calculated job snapshots | 3 h / S | [#102](https://github.com/kburson/Project-Estimator/issues/102) |
| [#108](https://github.com/kburson/Project-Estimator/issues/108) | Reject competing stale job revisions | 2 h / XS | [#105](https://github.com/kburson/Project-Estimator/issues/105) |
| [#111](https://github.com/kburson/Project-Estimator/issues/111) | Edit customer and jobsite information | 3 h / S | [#102](https://github.com/kburson/Project-Estimator/issues/102), [#105](https://github.com/kburson/Project-Estimator/issues/105) |
| [#114](https://github.com/kburson/Project-Estimator/issues/114) | Calculate and save the first real job | 3 h / S | [#108](https://github.com/kburson/Project-Estimator/issues/108), [#111](https://github.com/kburson/Project-Estimator/issues/111) |

### [#46](https://github.com/kburson/Project-Estimator/issues/46) Edit and durably save measured runs

Trunk prerequisites: [#45](https://github.com/kburson/Project-Estimator/issues/45). Source plan: [2026-11-01-run-editing.md](../superpowers/plans/sibling-delivery/2026-11-01-run-editing.md).

| Child | Story | Forecast | Direct prerequisite children |
| --- | --- | ---: | --- |
| [#103](https://github.com/kburson/Project-Estimator/issues/103) | Edit measured runs and explicit connections | 3 h / S | None |
| [#106](https://github.com/kburson/Project-Estimator/issues/106) | Serialize writes and preserve the latest edit generation | 3 h / S | None |
| [#109](https://github.com/kburson/Project-Estimator/issues/109) | Expose save retry and safe navigation | 3 h / S | [#103](https://github.com/kburson/Project-Estimator/issues/103), [#106](https://github.com/kburson/Project-Estimator/issues/106) |

### [#47](https://github.com/kburson/Project-Estimator/issues/47) Calculate and explicitly reprice saved estimates

Trunk prerequisites: [#46](https://github.com/kburson/Project-Estimator/issues/46), [#44](https://github.com/kburson/Project-Estimator/issues/44). Source plan: [2026-11-01-estimates.md](../superpowers/plans/sibling-delivery/2026-11-01-estimates.md).

| Child | Story | Forecast | Direct prerequisite children |
| --- | --- | ---: | --- |
| [#110](https://github.com/kburson/Project-Estimator/issues/110) | Edit explicit manual allowances | 3 h / S | None |
| [#113](https://github.com/kburson/Project-Estimator/issues/113) | Edit and clear segment selling adjustments | 2 h / XS | None |
| [#116](https://github.com/kburson/Project-Estimator/issues/116) | Track canonical calculation freshness | 2 h / XS | None |
| [#119](https://github.com/kburson/Project-Estimator/issues/119) | Display internal estimate explanations | 3 h / S | None |
| [#120](https://github.com/kburson/Project-Estimator/issues/120) | Review and accept explicit repricing changes | 3 h / S | [#110](https://github.com/kburson/Project-Estimator/issues/110), [#113](https://github.com/kburson/Project-Estimator/issues/113), [#116](https://github.com/kburson/Project-Estimator/issues/116), [#119](https://github.com/kburson/Project-Estimator/issues/119) |

### [#48](https://github.com/kburson/Project-Estimator/issues/48) Preserve presented quotes

Trunk prerequisites: [#47](https://github.com/kburson/Project-Estimator/issues/47). Source plan: [2026-11-01-quotes.md](../superpowers/plans/sibling-delivery/2026-11-01-quotes.md).

| Child | Story | Forecast | Direct prerequisite children |
| --- | --- | ---: | --- |
| [#112](https://github.com/kburson/Project-Estimator/issues/112) | Define quote content and stable fingerprints | 3 h / S | None |
| [#115](https://github.com/kburson/Project-Estimator/issues/115) | Persist immutable snapshots exactly once | 3 h / S | [#112](https://github.com/kburson/Project-Estimator/issues/112) |
| [#118](https://github.com/kburson/Project-Estimator/issues/118) | Freeze only current complete production calculations | 4 h / S | [#112](https://github.com/kburson/Project-Estimator/issues/112) |
| [#122](https://github.com/kburson/Project-Estimator/issues/122) | Present a durably saved quote snapshot | 3 h / S | [#115](https://github.com/kburson/Project-Estimator/issues/115), [#118](https://github.com/kburson/Project-Estimator/issues/118) |
| [#124](https://github.com/kburson/Project-Estimator/issues/124) | Reopen quote history without changing original bytes | 3 h / S | [#122](https://github.com/kburson/Project-Estimator/issues/122) |

### [#49](https://github.com/kburson/Project-Estimator/issues/49) Export customer-safe proposals

Trunk prerequisites: [#48](https://github.com/kburson/Project-Estimator/issues/48). Source plan: [2026-11-01-proposals.md](../superpowers/plans/sibling-delivery/2026-11-01-proposals.md).

| Child | Story | Forecast | Direct prerequisite children |
| --- | --- | ---: | --- |
| [#117](https://github.com/kburson/Project-Estimator/issues/117) | Project frozen quotes into the strict customer model | 3 h / S | None |
| [#121](https://github.com/kburson/Project-Estimator/issues/121) | Render wrapped and paginated proposal PDFs | 4 h / S | [#117](https://github.com/kburson/Project-Estimator/issues/117) |
| [#123](https://github.com/kburson/Project-Estimator/issues/123) | Display proposals from retained customer models | 3 h / S | [#117](https://github.com/kburson/Project-Estimator/issues/117) |
| [#126](https://github.com/kburson/Project-Estimator/issues/126) | Export and inspect frozen proposal files | 3 h / S | [#121](https://github.com/kburson/Project-Estimator/issues/121), [#123](https://github.com/kburson/Project-Estimator/issues/123) |

### [#50](https://github.com/kburson/Project-Estimator/issues/50) Retain job and receipt evidence

Trunk prerequisites: [#45](https://github.com/kburson/Project-Estimator/issues/45), [#40](https://github.com/kburson/Project-Estimator/issues/40). Source plan: [2026-11-01-attachments.md](../superpowers/plans/sibling-delivery/2026-11-01-attachments.md).

| Child | Story | Forecast | Direct prerequisite children |
| --- | --- | ---: | --- |
| [#125](https://github.com/kburson/Project-Estimator/issues/125) | Store verified immutable attachment files | 4 h / S | None |
| [#128](https://github.com/kburson/Project-Estimator/issues/128) | Upload and download evidence through bounded routes | 3 h / S | [#125](https://github.com/kburson/Project-Estimator/issues/125) |
| [#131](https://github.com/kburson/Project-Estimator/issues/131) | Attach and reopen owner-selected evidence | 3 h / S | [#128](https://github.com/kburson/Project-Estimator/issues/128) |

### [#51](https://github.com/kburson/Project-Estimator/issues/51) Create verified office backups

Trunk prerequisites: [#50](https://github.com/kburson/Project-Estimator/issues/50), [#39](https://github.com/kburson/Project-Estimator/issues/39). Source plan: [2026-11-01-backup-capture.md](../superpowers/plans/sibling-delivery/2026-11-01-backup-capture.md).

| Child | Story | Forecast | Direct prerequisite children |
| --- | --- | ---: | --- |
| [#127](https://github.com/kburson/Project-Estimator/issues/127) | Define the complete current backup inventory | 3 h / S | None |
| [#130](https://github.com/kburson/Project-Estimator/issues/130) | Capture a consistent database and file backup | 4 h / S | [#127](https://github.com/kburson/Project-Estimator/issues/127) |
| [#133](https://github.com/kburson/Project-Estimator/issues/133) | Choose destinations and report verified backup status | 3 h / S | [#130](https://github.com/kburson/Project-Estimator/issues/130) |

### [#52](https://github.com/kburson/Project-Estimator/issues/52) Restore office work safely

Trunk prerequisites: [#51](https://github.com/kburson/Project-Estimator/issues/51). Source plan: [2026-11-01-backup-restore.md](../superpowers/plans/sibling-delivery/2026-11-01-backup-restore.md).

| Child | Story | Forecast | Direct prerequisite children |
| --- | --- | ---: | --- |
| [#129](https://github.com/kburson/Project-Estimator/issues/129) | Validate every backup artifact before restore | 3 h / S | None |
| [#132](https://github.com/kburson/Project-Estimator/issues/132) | Restore through staging and preserve the old directory | 4 h / S | [#129](https://github.com/kburson/Project-Estimator/issues/129) |
| [#135](https://github.com/kburson/Project-Estimator/issues/135) | Prove identity and evidence preservation after restore | 3 h / S | [#132](https://github.com/kburson/Project-Estimator/issues/132) |

### [#53](https://github.com/kburson/Project-Estimator/issues/53) Prepare private field catalogs

Trunk prerequisites: [#49](https://github.com/kburson/Project-Estimator/issues/49), [#52](https://github.com/kburson/Project-Estimator/issues/52). Source plan: [2026-11-01-catalog-release.md](../superpowers/plans/sibling-delivery/2026-11-01-catalog-release.md).

| Child | Story | Forecast | Direct prerequisite children |
| --- | --- | ---: | --- |
| [#134](https://github.com/kburson/Project-Estimator/issues/134) | Encrypt independently versioned catalog modules | 4 h / S | None |
| [#137](https://github.com/kburson/Project-Estimator/issues/137) | Preserve published module and release identities | 3 h / S | [#134](https://github.com/kburson/Project-Estimator/issues/134) |
| [#139](https://github.com/kburson/Project-Estimator/issues/139) | Stage only verified public release artifacts | 4 h / S | [#134](https://github.com/kburson/Project-Estimator/issues/134) |
| [#142](https://github.com/kburson/Project-Estimator/issues/142) | Keep credentials local and generate enrollment explicitly | 3 h / S | [#134](https://github.com/kburson/Project-Estimator/issues/134) |
| [#145](https://github.com/kburson/Project-Estimator/issues/145) | Preview the release and selected current-pack removal | 3 h / S | [#137](https://github.com/kburson/Project-Estimator/issues/137), [#139](https://github.com/kburson/Project-Estimator/issues/139), [#142](https://github.com/kburson/Project-Estimator/issues/142) |

### [#54](https://github.com/kburson/Project-Estimator/issues/54) Save field site visits

Trunk prerequisites: [#55](https://github.com/kburson/Project-Estimator/issues/55), [#49](https://github.com/kburson/Project-Estimator/issues/49), [#46](https://github.com/kburson/Project-Estimator/issues/46). Source plan: [2026-11-01-field-visits.md](../superpowers/plans/sibling-delivery/2026-11-01-field-visits.md).

| Child | Story | Forecast | Direct prerequisite children |
| --- | --- | ---: | --- |
| [#136](https://github.com/kburson/Project-Estimator/issues/136) | Persist real field draft snapshots independently of keys | 3 h / S | None |
| [#140](https://github.com/kburson/Project-Estimator/issues/140) | Edit field customer job and run inputs | 4 h / S | [#136](https://github.com/kburson/Project-Estimator/issues/136) |
| [#143](https://github.com/kburson/Project-Estimator/issues/143) | Calculate enrolled field work with exact Mac parity | 3 h / S | [#140](https://github.com/kburson/Project-Estimator/issues/140) |
| [#146](https://github.com/kburson/Project-Estimator/issues/146) | Preserve newer field edits in the write queue | 3 h / S | [#136](https://github.com/kburson/Project-Estimator/issues/136) |
| [#150](https://github.com/kburson/Project-Estimator/issues/150) | Report field save failure and flush before navigation | 3 h / S | [#140](https://github.com/kburson/Project-Estimator/issues/140), [#143](https://github.com/kburson/Project-Estimator/issues/143), [#146](https://github.com/kburson/Project-Estimator/issues/146) |
| [#152](https://github.com/kburson/Project-Estimator/issues/152) | Reopen field visits and report actual storage persistence | 2 h / XS | [#150](https://github.com/kburson/Project-Estimator/issues/150) |

### [#55](https://github.com/kburson/Project-Estimator/issues/55) Register a device and install its first catalog

Trunk prerequisites: [#53](https://github.com/kburson/Project-Estimator/issues/53), [#37](https://github.com/kburson/Project-Estimator/issues/37). Source plan: [2026-11-01-registration.md](../superpowers/plans/sibling-delivery/2026-11-01-registration.md).

| Child | Story | Forecast | Direct prerequisite children |
| --- | --- | ---: | --- |
| [#138](https://github.com/kburson/Project-Estimator/issues/138) | Validate enrollment without replacing active registration | 3 h / S | None |
| [#141](https://github.com/kburson/Project-Estimator/issues/141) | Commit registration and catalog activation atomically | 4 h / S | [#138](https://github.com/kburson/Project-Estimator/issues/138) |
| [#144](https://github.com/kburson/Project-Estimator/issues/144) | Validate and decrypt complete catalog modules before install | 4 h / S | [#141](https://github.com/kburson/Project-Estimator/issues/141) |
| [#147](https://github.com/kburson/Project-Estimator/issues/147) | Read camera and selected-image QR credentials | 3 h / S | [#138](https://github.com/kburson/Project-Estimator/issues/138) |
| [#148](https://github.com/kburson/Project-Estimator/issues/148) | Recover enrollment input after denied camera permission | 2 h / XS | [#147](https://github.com/kburson/Project-Estimator/issues/147) |
| [#151](https://github.com/kburson/Project-Estimator/issues/151) | Display catalog design and activation status | 3 h / S | [#144](https://github.com/kburson/Project-Estimator/issues/144) |
| [#155](https://github.com/kburson/Project-Estimator/issues/155) | Expose the read-only field conformance action | 2 h / XS | [#151](https://github.com/kburson/Project-Estimator/issues/151) |

### [#56](https://github.com/kburson/Project-Estimator/issues/56) Refresh catalogs and rotate keys safely

Trunk prerequisites: [#55](https://github.com/kburson/Project-Estimator/issues/55). Source plan: [2026-11-01-catalog-refresh.md](../superpowers/plans/sibling-delivery/2026-11-01-catalog-refresh.md).

| Child | Story | Forecast | Direct prerequisite children |
| --- | --- | ---: | --- |
| [#149](https://github.com/kburson/Project-Estimator/issues/149) | Reuse unchanged modules and retain active data on failure | 3 h / S | None |
| [#153](https://github.com/kburson/Project-Estimator/issues/153) | Promote a pending key only with a valid matching release | 4 h / S | None |
| [#156](https://github.com/kburson/Project-Estimator/issues/156) | Schedule single-flight foreground catalog checks | 3 h / S | None |
| [#159](https://github.com/kburson/Project-Estimator/issues/159) | Explain refresh and registration status accurately | 3 h / S | [#149](https://github.com/kburson/Project-Estimator/issues/149), [#153](https://github.com/kburson/Project-Estimator/issues/153), [#156](https://github.com/kburson/Project-Estimator/issues/156) |

### [#57](https://github.com/kburson/Project-Estimator/issues/57) Present retained field quotes

Trunk prerequisites: [#54](https://github.com/kburson/Project-Estimator/issues/54), [#55](https://github.com/kburson/Project-Estimator/issues/55), [#49](https://github.com/kburson/Project-Estimator/issues/49). Source plan: [2026-11-01-field-quotes.md](../superpowers/plans/sibling-delivery/2026-11-01-field-quotes.md).

| Child | Story | Forecast | Direct prerequisite children |
| --- | --- | ---: | --- |
| [#154](https://github.com/kburson/Project-Estimator/issues/154) | Enter field allowances and selling adjustments | 3 h / S | None |
| [#157](https://github.com/kburson/Project-Estimator/issues/157) | Freeze durable Preliminary field snapshots | 3 h / S | None |
| [#162](https://github.com/kburson/Project-Estimator/issues/162) | Export the shared customer-safe field PDF | 3 h / S | None |
| [#165](https://github.com/kburson/Project-Estimator/issues/165) | Present retained quotes after explicit repricing | 2 h / XS | [#154](https://github.com/kburson/Project-Estimator/issues/154), [#157](https://github.com/kburson/Project-Estimator/issues/157), [#162](https://github.com/kburson/Project-Estimator/issues/162) |

### [#58](https://github.com/kburson/Project-Estimator/issues/58) Return immutable field submissions

Trunk prerequisites: [#57](https://github.com/kburson/Project-Estimator/issues/57). Source plan: [2026-11-01-field-returns.md](../superpowers/plans/sibling-delivery/2026-11-01-field-returns.md).

| Child | Story | Forecast | Direct prerequisite children |
| --- | --- | ---: | --- |
| [#158](https://github.com/kburson/Project-Estimator/issues/158) | Build strict self-contained field packages | 3 h / S | None |
| [#161](https://github.com/kburson/Project-Estimator/issues/161) | Persist immutable outbox records before sharing | 3 h / S | [#158](https://github.com/kburson/Project-Estimator/issues/158) |
| [#164](https://github.com/kburson/Project-Estimator/issues/164) | Share JSON or download it truthfully | 3 h / S | [#158](https://github.com/kburson/Project-Estimator/issues/158) |
| [#168](https://github.com/kburson/Project-Estimator/issues/168) | Retry saved submissions and confirm receipt explicitly | 2 h / XS | [#161](https://github.com/kburson/Project-Estimator/issues/161), [#164](https://github.com/kburson/Project-Estimator/issues/164) |

### [#59](https://github.com/kburson/Project-Estimator/issues/59) Review returned field work in the office

Trunk prerequisites: [#58](https://github.com/kburson/Project-Estimator/issues/58), [#45](https://github.com/kburson/Project-Estimator/issues/45). Source plan: [2026-11-01-import-review.md](../superpowers/plans/sibling-delivery/2026-11-01-import-review.md).

| Child | Story | Forecast | Direct prerequisite children |
| --- | --- | ---: | --- |
| [#160](https://github.com/kburson/Project-Estimator/issues/160) | Validate received attachments before review | 3 h / S | None |
| [#163](https://github.com/kburson/Project-Estimator/issues/163) | Read existing source mappings without name-based merging | 3 h / S | [#160](https://github.com/kburson/Project-Estimator/issues/160) |
| [#166](https://github.com/kburson/Project-Estimator/issues/166) | Explain identity and base-revision conflicts | 4 h / S | [#160](https://github.com/kburson/Project-Estimator/issues/160) |
| [#169](https://github.com/kburson/Project-Estimator/issues/169) | Review source values and office target choices | 3 h / S | [#163](https://github.com/kburson/Project-Estimator/issues/163), [#166](https://github.com/kburson/Project-Estimator/issues/166) |

### [#60](https://github.com/kburson/Project-Estimator/issues/60) Accept reviewed field submissions exactly once

Trunk prerequisites: [#59](https://github.com/kburson/Project-Estimator/issues/59). Source plan: [2026-11-01-import-accept.md](../superpowers/plans/sibling-delivery/2026-11-01-import-accept.md).

| Child | Story | Forecast | Direct prerequisite children |
| --- | --- | ---: | --- |
| [#167](https://github.com/kburson/Project-Estimator/issues/167) | Commit import receipts and mappings together | 4 h / S | None |
| [#171](https://github.com/kburson/Project-Estimator/issues/171) | Apply reviewed drafts while retaining original quote links | 4 h / S | [#167](https://github.com/kburson/Project-Estimator/issues/167) |
| [#174](https://github.com/kburson/Project-Estimator/issues/174) | Require renewed review after context changes | 2 h / XS | [#167](https://github.com/kburson/Project-Estimator/issues/167) |
| [#176](https://github.com/kburson/Project-Estimator/issues/176) | Accept replayed and delayed submissions through the office UI | 3 h / S | [#171](https://github.com/kburson/Project-Estimator/issues/171), [#174](https://github.com/kburson/Project-Estimator/issues/174) |

### [#61](https://github.com/kburson/Project-Estimator/issues/61) Recover catalog and imported office evidence

Trunk prerequisites: [#52](https://github.com/kburson/Project-Estimator/issues/52), [#53](https://github.com/kburson/Project-Estimator/issues/53), [#60](https://github.com/kburson/Project-Estimator/issues/60). Source plan: [2026-11-01-office-recovery.md](../superpowers/plans/sibling-delivery/2026-11-01-office-recovery.md).

| Child | Story | Forecast | Direct prerequisite children |
| --- | --- | ---: | --- |
| [#170](https://github.com/kburson/Project-Estimator/issues/170) | Verify current archive and key backup coverage | 3 h / S | None |
| [#173](https://github.com/kburson/Project-Estimator/issues/173) | Restore import mappings links and duplicate receipts | 3 h / S | None |
| [#177](https://github.com/kburson/Project-Estimator/issues/177) | Verify the complete current office restore | 3 h / S | [#170](https://github.com/kburson/Project-Estimator/issues/170), [#173](https://github.com/kburson/Project-Estimator/issues/173) |

### [#62](https://github.com/kburson/Project-Estimator/issues/62) Launch the field application without network

Trunk prerequisites: [#55](https://github.com/kburson/Project-Estimator/issues/55), [#57](https://github.com/kburson/Project-Estimator/issues/57), [#58](https://github.com/kburson/Project-Estimator/issues/58). Source plan: [2026-11-01-offline-shell.md](../superpowers/plans/sibling-delivery/2026-11-01-offline-shell.md).

| Child | Story | Forecast | Direct prerequisite children |
| --- | --- | ---: | --- |
| [#172](https://github.com/kburson/Project-Estimator/issues/172) | Generate exact versioned app-shell asset metadata | 3 h / S | None |
| [#175](https://github.com/kburson/Project-Estimator/issues/175) | Cache only the versioned application shell | 4 h / S | [#172](https://github.com/kburson/Project-Estimator/issues/172) |
| [#179](https://github.com/kburson/Project-Estimator/issues/179) | Register the production worker without reloading edits | 2 h / XS | [#175](https://github.com/kburson/Project-Estimator/issues/175) |
| [#181](https://github.com/kburson/Project-Estimator/issues/181) | Cold-open retained work and PDF output offline | 3 h / S | [#179](https://github.com/kburson/Project-Estimator/issues/179) |

### [#63](https://github.com/kburson/Project-Estimator/issues/63) Upgrade the field app without losing work

Trunk prerequisites: [#62](https://github.com/kburson/Project-Estimator/issues/62), [#56](https://github.com/kburson/Project-Estimator/issues/56), [#58](https://github.com/kburson/Project-Estimator/issues/58). Source plan: [2026-11-01-app-upgrades.md](../superpowers/plans/sibling-delivery/2026-11-01-app-upgrades.md).

| Child | Story | Forecast | Direct prerequisite children |
| --- | --- | ---: | --- |
| [#178](https://github.com/kburson/Project-Estimator/issues/178) | Check waiting-release and stored-data compatibility | 3 h / S | None |
| [#182](https://github.com/kburson/Project-Estimator/issues/182) | Defer activation until edits are durably saved | 3 h / S | [#178](https://github.com/kburson/Project-Estimator/issues/178) |
| [#185](https://github.com/kburson/Project-Estimator/issues/185) | Keep the prior shell until replacement boot succeeds | 4 h / S | [#178](https://github.com/kburson/Project-Estimator/issues/178) |
| [#189](https://github.com/kburson/Project-Estimator/issues/189) | Rehearse genuinely different preserved-store releases | 3 h / S | [#182](https://github.com/kburson/Project-Estimator/issues/182), [#185](https://github.com/kburson/Project-Estimator/issues/185) |

### [#65](https://github.com/kburson/Project-Estimator/issues/65) Recover field work after storage loss

Trunk prerequisites: [#58](https://github.com/kburson/Project-Estimator/issues/58). Source plan: [2026-11-01-field-recovery.md](../superpowers/plans/sibling-delivery/2026-11-01-field-recovery.md).

| Child | Story | Forecast | Direct prerequisite children |
| --- | --- | ---: | --- |
| [#180](https://github.com/kburson/Project-Estimator/issues/180) | Export self-contained work without catalog credentials | 3 h / S | None |
| [#183](https://github.com/kburson/Project-Estimator/issues/183) | Preview recovery identity conflicts without writes | 3 h / S | [#180](https://github.com/kburson/Project-Estimator/issues/180) |
| [#186](https://github.com/kburson/Project-Estimator/issues/186) | Restore reviewed rows in one rechecked transaction | 4 h / S | [#180](https://github.com/kburson/Project-Estimator/issues/180) |
| [#188](https://github.com/kburson/Project-Estimator/issues/188) | Recover into a separate profile and reenroll explicitly | 2 h / XS | [#183](https://github.com/kburson/Project-Estimator/issues/183), [#186](https://github.com/kburson/Project-Estimator/issues/186) |

### [#64](https://github.com/kburson/Project-Estimator/issues/64) Qualify the complete owner trial

Trunk prerequisites: [#61](https://github.com/kburson/Project-Estimator/issues/61), [#63](https://github.com/kburson/Project-Estimator/issues/63), [#65](https://github.com/kburson/Project-Estimator/issues/65), [#56](https://github.com/kburson/Project-Estimator/issues/56). Source plan: [2026-11-01-qualification.md](../superpowers/plans/sibling-delivery/2026-11-01-qualification.md).

| Child | Story | Forecast | Direct prerequisite children |
| --- | --- | ---: | --- |
| [#184](https://github.com/kburson/Project-Estimator/issues/184) | Prepare exact-release conformance inputs and records | 2 h / XS | None |
| [#187](https://github.com/kburson/Project-Estimator/issues/187) | Verify iPhone offline calculations and customer output | 3 h / S | [#184](https://github.com/kburson/Project-Estimator/issues/184) |
| [#190](https://github.com/kburson/Project-Estimator/issues/190) | Verify iPad offline calculations and customer output | 3 h / S | [#184](https://github.com/kburson/Project-Estimator/issues/184) |
| [#191](https://github.com/kburson/Project-Estimator/issues/191) | Verify real Mac quote history and explicit repricing | 2 h / XS | [#184](https://github.com/kburson/Project-Estimator/issues/184) |
| [#192](https://github.com/kburson/Project-Estimator/issues/192) | Verify iPhone enrollment and key rotation | 3 h / S | [#187](https://github.com/kburson/Project-Estimator/issues/187), [#190](https://github.com/kburson/Project-Estimator/issues/190) |
| [#193](https://github.com/kburson/Project-Estimator/issues/193) | Verify iPad enrollment and key rotation | 3 h / S | [#192](https://github.com/kburson/Project-Estimator/issues/192) |
| [#194](https://github.com/kburson/Project-Estimator/issues/194) | Verify iPhone dirty clean and offline app upgrades | 3 h / S | [#193](https://github.com/kburson/Project-Estimator/issues/193) |
| [#195](https://github.com/kburson/Project-Estimator/issues/195) | Verify iPad dirty clean and offline app upgrades | 3 h / S | [#194](https://github.com/kburson/Project-Estimator/issues/194) |
| [#196](https://github.com/kburson/Project-Estimator/issues/196) | Verify actual iPhone sharing and reviewed office return | 2 h / XS | [#195](https://github.com/kburson/Project-Estimator/issues/195) |
| [#197](https://github.com/kburson/Project-Estimator/issues/197) | Verify actual iPad sharing and reviewed office return | 2 h / XS | [#196](https://github.com/kburson/Project-Estimator/issues/196) |
| [#198](https://github.com/kburson/Project-Estimator/issues/198) | Verify isolated Mac restore and delayed plaintext import | 3 h / S | [#191](https://github.com/kburson/Project-Estimator/issues/191), [#197](https://github.com/kburson/Project-Estimator/issues/197) |
| [#199](https://github.com/kburson/Project-Estimator/issues/199) | Verify field recovery in separate test profiles | 3 h / S | [#198](https://github.com/kburson/Project-Estimator/issues/198) |
| [#200](https://github.com/kburson/Project-Estimator/issues/200) | Reconcile the eleven-case acceptance ledger | 2 h / XS | [#187](https://github.com/kburson/Project-Estimator/issues/187), [#190](https://github.com/kburson/Project-Estimator/issues/190), [#191](https://github.com/kburson/Project-Estimator/issues/191), [#192](https://github.com/kburson/Project-Estimator/issues/192), [#193](https://github.com/kburson/Project-Estimator/issues/193), [#194](https://github.com/kburson/Project-Estimator/issues/194), [#195](https://github.com/kburson/Project-Estimator/issues/195), [#196](https://github.com/kburson/Project-Estimator/issues/196), [#197](https://github.com/kburson/Project-Estimator/issues/197), [#198](https://github.com/kburson/Project-Estimator/issues/198), [#199](https://github.com/kburson/Project-Estimator/issues/199) |

## Exact legacy scope mapping

The registered retirement target for every legacy record is the non-parent index #36. This table identifies the product scope successors; it creates no new parent or blocking edges. Historical #1 → #2–35 parent links remain.

| Legacy record | Scope successors |
| --- | --- |
| [#1](https://github.com/kburson/Project-Estimator/issues/1) | [#36](https://github.com/kburson/Project-Estimator/issues/36) and all 28 sibling epics above |
| [#2](https://github.com/kburson/Project-Estimator/issues/2) | [#37](https://github.com/kburson/Project-Estimator/issues/37) |
| [#3](https://github.com/kburson/Project-Estimator/issues/3) | [#41](https://github.com/kburson/Project-Estimator/issues/41) |
| [#4](https://github.com/kburson/Project-Estimator/issues/4) | [#41](https://github.com/kburson/Project-Estimator/issues/41), [#42](https://github.com/kburson/Project-Estimator/issues/42) |
| [#5](https://github.com/kburson/Project-Estimator/issues/5) | [#40](https://github.com/kburson/Project-Estimator/issues/40), [#39](https://github.com/kburson/Project-Estimator/issues/39) |
| [#6](https://github.com/kburson/Project-Estimator/issues/6) | [#43](https://github.com/kburson/Project-Estimator/issues/43) |
| [#7](https://github.com/kburson/Project-Estimator/issues/7) | [#44](https://github.com/kburson/Project-Estimator/issues/44) |
| [#8](https://github.com/kburson/Project-Estimator/issues/8) | [#44](https://github.com/kburson/Project-Estimator/issues/44) |
| [#9](https://github.com/kburson/Project-Estimator/issues/9) | [#40](https://github.com/kburson/Project-Estimator/issues/40), [#39](https://github.com/kburson/Project-Estimator/issues/39), [#45](https://github.com/kburson/Project-Estimator/issues/45), [#42](https://github.com/kburson/Project-Estimator/issues/42) |
| [#10](https://github.com/kburson/Project-Estimator/issues/10) | [#37](https://github.com/kburson/Project-Estimator/issues/37), [#45](https://github.com/kburson/Project-Estimator/issues/45) |
| [#11](https://github.com/kburson/Project-Estimator/issues/11) | [#50](https://github.com/kburson/Project-Estimator/issues/50) |
| [#12](https://github.com/kburson/Project-Estimator/issues/12) | [#40](https://github.com/kburson/Project-Estimator/issues/40), [#39](https://github.com/kburson/Project-Estimator/issues/39), [#42](https://github.com/kburson/Project-Estimator/issues/42) |
| [#13](https://github.com/kburson/Project-Estimator/issues/13) | [#45](https://github.com/kburson/Project-Estimator/issues/45), [#46](https://github.com/kburson/Project-Estimator/issues/46), [#47](https://github.com/kburson/Project-Estimator/issues/47), [#50](https://github.com/kburson/Project-Estimator/issues/50) |
| [#14](https://github.com/kburson/Project-Estimator/issues/14) | [#46](https://github.com/kburson/Project-Estimator/issues/46), [#47](https://github.com/kburson/Project-Estimator/issues/47) |
| [#15](https://github.com/kburson/Project-Estimator/issues/15) | [#48](https://github.com/kburson/Project-Estimator/issues/48) |
| [#16](https://github.com/kburson/Project-Estimator/issues/16) | [#49](https://github.com/kburson/Project-Estimator/issues/49) |
| [#17](https://github.com/kburson/Project-Estimator/issues/17) | [#53](https://github.com/kburson/Project-Estimator/issues/53) |
| [#18](https://github.com/kburson/Project-Estimator/issues/18) | [#53](https://github.com/kburson/Project-Estimator/issues/53) |
| [#19](https://github.com/kburson/Project-Estimator/issues/19) | [#53](https://github.com/kburson/Project-Estimator/issues/53) |
| [#20](https://github.com/kburson/Project-Estimator/issues/20) | [#37](https://github.com/kburson/Project-Estimator/issues/37), [#55](https://github.com/kburson/Project-Estimator/issues/55), [#54](https://github.com/kburson/Project-Estimator/issues/54) |
| [#21](https://github.com/kburson/Project-Estimator/issues/21) | [#54](https://github.com/kburson/Project-Estimator/issues/54), [#57](https://github.com/kburson/Project-Estimator/issues/57) |
| [#22](https://github.com/kburson/Project-Estimator/issues/22) | [#55](https://github.com/kburson/Project-Estimator/issues/55), [#54](https://github.com/kburson/Project-Estimator/issues/54), [#57](https://github.com/kburson/Project-Estimator/issues/57) |
| [#23](https://github.com/kburson/Project-Estimator/issues/23) | [#55](https://github.com/kburson/Project-Estimator/issues/55) |
| [#24](https://github.com/kburson/Project-Estimator/issues/24) | [#55](https://github.com/kburson/Project-Estimator/issues/55), [#56](https://github.com/kburson/Project-Estimator/issues/56) |
| [#25](https://github.com/kburson/Project-Estimator/issues/25) | [#55](https://github.com/kburson/Project-Estimator/issues/55), [#56](https://github.com/kburson/Project-Estimator/issues/56) |
| [#26](https://github.com/kburson/Project-Estimator/issues/26) | [#58](https://github.com/kburson/Project-Estimator/issues/58) |
| [#27](https://github.com/kburson/Project-Estimator/issues/27) | [#59](https://github.com/kburson/Project-Estimator/issues/59), [#60](https://github.com/kburson/Project-Estimator/issues/60) |
| [#28](https://github.com/kburson/Project-Estimator/issues/28) | [#58](https://github.com/kburson/Project-Estimator/issues/58), [#59](https://github.com/kburson/Project-Estimator/issues/59), [#60](https://github.com/kburson/Project-Estimator/issues/60) |
| [#29](https://github.com/kburson/Project-Estimator/issues/29) | [#51](https://github.com/kburson/Project-Estimator/issues/51), [#52](https://github.com/kburson/Project-Estimator/issues/52), [#61](https://github.com/kburson/Project-Estimator/issues/61) |
| [#30](https://github.com/kburson/Project-Estimator/issues/30) | [#65](https://github.com/kburson/Project-Estimator/issues/65) |
| [#31](https://github.com/kburson/Project-Estimator/issues/31) | [#62](https://github.com/kburson/Project-Estimator/issues/62) |
| [#32](https://github.com/kburson/Project-Estimator/issues/32) | [#63](https://github.com/kburson/Project-Estimator/issues/63) |
| [#33](https://github.com/kburson/Project-Estimator/issues/33) | [#37](https://github.com/kburson/Project-Estimator/issues/37), [#44](https://github.com/kburson/Project-Estimator/issues/44), [#55](https://github.com/kburson/Project-Estimator/issues/55), [#53](https://github.com/kburson/Project-Estimator/issues/53), [#62](https://github.com/kburson/Project-Estimator/issues/62), [#64](https://github.com/kburson/Project-Estimator/issues/64) |
| [#34](https://github.com/kburson/Project-Estimator/issues/34) | [#64](https://github.com/kburson/Project-Estimator/issues/64) |
| [#35](https://github.com/kburson/Project-Estimator/issues/35) | [#64](https://github.com/kburson/Project-Estimator/issues/64) |

## Creation correction

GitHub created [#75](https://github.com/kburson/Project-Estimator/issues/75) despite a failed creation response. The confirmed retry [#76](https://github.com/kburson/Project-Estimator/issues/76) is canonical; #75 is retired through registered AITM supersession to #76 as Replaced/not planned. This duplicate is excluded from the 135-story delivery set.

## Verification and release boundary

Migration verification checks inventory, ownership, source metadata, sizes, native graph edges, retained legacy links and final Replaced/not-planned states. A pre-retirement PASS is required before any legacy retirement, followed by a final PASS afterward. Application acceptance boxes remain unchecked. No app source implementation, dependency installation for the application, builds, deployment, physical-device acceptance or trunk delivery is represented by this migration.
