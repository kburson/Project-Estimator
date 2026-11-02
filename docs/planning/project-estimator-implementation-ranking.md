# Project Estimator: implementation order and epic ranks

Applied and independently verified November 02, 2026 at 10:46 AM CST.

All 28 open epics have been ranked on the GitHub Project board and in their AITM field caches. There are 19 dependency waves, from 100 to 1900. Lower ranks precede higher ranks; epics sharing a rank have no dependency path between them.

## Scheduling rule

For each epic: `rank = 100 + max(prerequisite ranks)`, with an empty prerequisite list yielding rank 100. This assigns each epic its earliest dependency wave. The graph has a longest prerequisite chain of 19 epics, so fewer than 19 sequential waves cannot satisfy it. Each wave contains at most three epics, fitting the recorded maximum of three workers.

This optimizes dependency depth, not elapsed delivery time: actual durations, shared-file ownership, child-story dependencies, owner-data availability and review/integration capacity can alter real scheduling. Start an epic when its own prerequisites are delivered; unrelated unfinished work in an earlier wave need not impose an additional barrier. Rank assignment does not authorize implementation or stage transitions.

## Stack-ranked backlog

| Rank | Epic stories |
| --- | --- |
| 100 | [#37](https://github.com/kburson/Project-Estimator/issues/37) — Deliver the first office and field builds |
| 200 | [#40](https://github.com/kburson/Project-Estimator/issues/40) — Maintain vendor and component identities<br>[#41](https://github.com/kburson/Project-Estimator/issues/41) — Explain bays and shared posts |
| 300 | [#39](https://github.com/kburson/Project-Estimator/issues/39) — Keep dated prices and deliberate business settings<br>[#42](https://github.com/kburson/Project-Estimator/issues/42) — Explain material cuts and stock requirements |
| 400 | [#43](https://github.com/kburson/Project-Estimator/issues/43) — Explain purchased packs and eligible prices |
| 500 | [#44](https://github.com/kburson/Project-Estimator/issues/44) — Calculate complete segment costs |
| 600 | [#45](https://github.com/kburson/Project-Estimator/issues/45) — Save and reopen calculated site visits |
| 700 | [#46](https://github.com/kburson/Project-Estimator/issues/46) — Edit and durably save measured runs<br>[#50](https://github.com/kburson/Project-Estimator/issues/50) — Retain job and receipt evidence |
| 800 | [#47](https://github.com/kburson/Project-Estimator/issues/47) — Calculate and explicitly reprice saved estimates<br>[#51](https://github.com/kburson/Project-Estimator/issues/51) — Create verified office backups |
| 900 | [#48](https://github.com/kburson/Project-Estimator/issues/48) — Preserve presented quotes<br>[#52](https://github.com/kburson/Project-Estimator/issues/52) — Restore office work safely |
| 1000 | [#49](https://github.com/kburson/Project-Estimator/issues/49) — Export customer-safe proposals |
| 1100 | [#53](https://github.com/kburson/Project-Estimator/issues/53) — Prepare private field catalogs |
| 1200 | [#55](https://github.com/kburson/Project-Estimator/issues/55) — Register a device and install its first catalog |
| 1300 | [#54](https://github.com/kburson/Project-Estimator/issues/54) — Save field site visits<br>[#56](https://github.com/kburson/Project-Estimator/issues/56) — Refresh catalogs and rotate keys safely |
| 1400 | [#57](https://github.com/kburson/Project-Estimator/issues/57) — Present retained field quotes |
| 1500 | [#58](https://github.com/kburson/Project-Estimator/issues/58) — Return immutable field submissions |
| 1600 | [#59](https://github.com/kburson/Project-Estimator/issues/59) — Review returned field work in the office<br>[#62](https://github.com/kburson/Project-Estimator/issues/62) — Launch the field application without network<br>[#65](https://github.com/kburson/Project-Estimator/issues/65) — Recover field work after storage loss |
| 1700 | [#60](https://github.com/kburson/Project-Estimator/issues/60) — Accept reviewed field submissions exactly once<br>[#63](https://github.com/kburson/Project-Estimator/issues/63) — Upgrade the field app without losing work |
| 1800 | [#61](https://github.com/kburson/Project-Estimator/issues/61) — Recover catalog and imported office evidence |
| 1900 | [#64](https://github.com/kburson/Project-Estimator/issues/64) — Qualify the complete owner trial |

## Verification

- Re-read the live inventory and 48 native prerequisite links before computing ranks.
- Applied ranks sequentially through `npx aitm set-rank <issue> <rank>`, which verifies both board fields and fresh issue-body caches.
- Independently read back all 28 board Rank values and issue-body caches after the updates. Every value matched; all epics remain open; all other cached field values were preserved.
- All 48 dependency edges point from a lower rank to a higher rank. No wave contains more than three epics.
- Superseded epic #1, administrative index #36, and child-story ranks were not included in this update.

[GitHub Project board](https://github.com/users/kburson/projects/23) · [Dependency table and Mermaid diagram](project-estimator-epic-dependencies.md)
