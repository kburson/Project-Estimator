# Epic #1: First usable Project Estimator

[GitHub epic #1](https://github.com/kburson/Project-Estimator/issues/1)

## Assigned specification, plan and review evidence

| Artifact | Repository document | Reviewed SHA-256 |
| --- | --- | --- |
| Specification | [PWA and Mac office design](../superpowers/specs/2026-11-01-project-estimator-pwa-v1-design.md) | `0971e6426aadf888a3652d9fae78707793f4af7f4b221e5b577ef8deca253f2c` |
| Implementation plan | [First usable version](../superpowers/plans/2026-11-01-first-usable-project-estimator.md) | `fb0601ece98e4f7af05a26cabcaeccbf5f33dd386e21d00215f0a1bedc2ad6f6` |

- [Claude Opus 5.5/high specification review and disposition](../reviews/2026-11-01-pwa-v1-claude/review-summary.md), with requests, receipts, findings and follow-up confirmation in that directory.
- [Astra 6/high same-agent SAR acceptance](../reviews/2026-11-01-first-usable-plan-sar/review-acceptance.md), with both review rounds, resolutions and parent verification in that directory.
- [Technical dependency checks](../research/2026-11-01-first-usable-plan-technical-checks.md).
- [Mobile native capability log](../design/mobile-native-capability-log.md).

The reviewed documents retain their original filenames and bytes so the review hashes remain valid. This record assigns them to epic #1 without rewriting historical review evidence. The broader specification includes later features; this epic covers only its First real-job trial and acceptance cases 1–11, as bounded by the implementation plan.

## Fresh-session handoff

The owner intends to start a fresh session to hydrate the epic and begin implementation. No application implementation occurred in this planning session. No child implementation issues have been created yet; the ten plan deliverables are scope, not completed work.

In the fresh session:

1. Read this epic, the specification, implementation plan and final review dispositions. Verify the local checkout against `origin/trunk` and preserve existing untracked files.
2. Hydrate/decompose the epic into implementation work using the ten plan deliverables and their acceptance evidence. Keep deferred features outside the trial.
3. Follow Task 1 and its owner-data checkpoint: obtain the populated, owner-validated single-recipe worksheet before calculation implementation. Synthetic scaffolding may proceed only within the plan's test-only boundary. Real prices, labor/markup/tax settings and the stable production origin are explicit setup dependencies; do not invent them.
4. Deliver the useful Mac quoting workflow before mobile integration. Treat all proposed build, test, PDF and physical-device checks as future execution work, not already-passing evidence. Android remains untested/deferred.

Architecture: Mac-local React/Node/SQLite office, shared TypeScript calculator, static Expo/React Native Web PWA, encrypted modular CDN catalogs with one-time QR enrollment, and reviewed field attachment imports. No local Wi-Fi/DNS setup or hosted business database is part of this trial.

Existing untracked Numbers workbook, earlier design/research documents and disposable probes are preserved locally; they are not production authority or part of this documentation integration. Never add raw catalog keys, enrollment credentials, customer exports or recovery packages to Git or public static staging.
