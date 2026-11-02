# #36 documentation publication boundary

This manifest defines the documentation delivery for the completed sibling-backlog migration. The native issue record supplies the current PR, accepted SHA, delivery receipt and closure status. It does not authorize product epic #37.

The delivery is commit-bearing `docs-only` work. The earlier audit-lane attempt is historical and is not completion authority: AITM intentionally requires zero attributed source commits in that lane. Investigation changed no AITM code or package; the proposed functional repair ai-task-manager#2138 was retired not planned. The discovered false-ready diagnostic does not justify weakening the delivery rule.

## Public ancestry and scope

The publication branch is constructed on public base `1f49087225e3911177e63c9c043b1d06b79b3d5d`, with the exact allowlist below. Only that branch may be pushed. The private setup/administration ancestry, workbooks, probes, credentials, raw receipts, machine-local configuration, hooks and tracker state are excluded. Existing original files remain in the owner's local checkouts.

The current public base contains documentation but no package lockfile. Clean AITM verification requires the already-installed package manifest, lockfile and vendor archive. These introduce no application dependency or implementation. The archive is unchanged: SHA-256 `255e6be99ecd6c2bf74a2d3727f88deb8386daaae1036499875df9c56b6d8367`; all 970 packed files byte-match published AITM source `f3bd631e4967f50fa269e0bc915775db1427d951`, and the lockfile integrity matches. Bootstrap skill instructions and ignore rules support the existing local workflow; local project configuration/templates are installed or seeded separately and are not published here.

## Provenance and verification limits

The approved maps and immutable pre-retirement/final evidence retain their original hashes. Historical source-plan commit `a1f4a7bcefb82e5499219f33c34aed280c76bceb` remains locally available and is not silently replaced in any child issue. Publishing byte-identical plan files does not publish that private commit's parents. The archival migration checker requires the retained local Git objects and intake-era issue graph; it is not a general app CI command after product work begins.

No application tests, builds, deployment, customer-data acceptance or physical-device results are asserted. Actual checks cover metadata/source hashes, native issue relationships, documentation whitespace, package installation and CLI availability. New product work must establish its own build/test commands through #37/#38; this documentation delivery does not approve those stages.

## Exact publication allowlist

- `docs/superpowers/plans/sibling-delivery/2026-11-01-app-upgrades.md`
- `docs/superpowers/plans/sibling-delivery/2026-11-01-attachments.md`
- `docs/superpowers/plans/sibling-delivery/2026-11-01-backup-capture.md`
- `docs/superpowers/plans/sibling-delivery/2026-11-01-backup-restore.md`
- `docs/superpowers/plans/sibling-delivery/2026-11-01-bays.md`
- `docs/superpowers/plans/sibling-delivery/2026-11-01-catalog-refresh.md`
- `docs/superpowers/plans/sibling-delivery/2026-11-01-catalog-release.md`
- `docs/superpowers/plans/sibling-delivery/2026-11-01-catalog.md`
- `docs/superpowers/plans/sibling-delivery/2026-11-01-costs.md`
- `docs/superpowers/plans/sibling-delivery/2026-11-01-estimates.md`
- `docs/superpowers/plans/sibling-delivery/2026-11-01-field-quotes.md`
- `docs/superpowers/plans/sibling-delivery/2026-11-01-field-recovery.md`
- `docs/superpowers/plans/sibling-delivery/2026-11-01-field-returns.md`
- `docs/superpowers/plans/sibling-delivery/2026-11-01-field-visits.md`
- `docs/superpowers/plans/sibling-delivery/2026-11-01-foundation.md`
- `docs/superpowers/plans/sibling-delivery/2026-11-01-import-accept.md`
- `docs/superpowers/plans/sibling-delivery/2026-11-01-import-review.md`
- `docs/superpowers/plans/sibling-delivery/2026-11-01-office-recovery.md`
- `docs/superpowers/plans/sibling-delivery/2026-11-01-offline-shell.md`
- `docs/superpowers/plans/sibling-delivery/2026-11-01-prices.md`
- `docs/superpowers/plans/sibling-delivery/2026-11-01-proposals.md`
- `docs/superpowers/plans/sibling-delivery/2026-11-01-purchases.md`
- `docs/superpowers/plans/sibling-delivery/2026-11-01-qualification.md`
- `docs/superpowers/plans/sibling-delivery/2026-11-01-quotes.md`
- `docs/superpowers/plans/sibling-delivery/2026-11-01-registration.md`
- `docs/superpowers/plans/sibling-delivery/2026-11-01-requirements.md`
- `docs/superpowers/plans/sibling-delivery/2026-11-01-run-editing.md`
- `docs/superpowers/plans/sibling-delivery/2026-11-01-visits.md`
- `docs/epics/2026-11-01-incremental-delivery-strategy.md`
- `docs/epics/2026-11-01-sibling-delivery-backlog.md`
- `docs/epics/2026-11-01-sibling-delivery-issue-map.md`
- `docs/epics/2026-11-01-sibling-delivery-issue-map.json`
- `docs/epics/2026-11-02-36-sibling-migration-verification.md`
- `docs/epics/2026-11-02-36-sibling-migration-verification.json`
- `docs/startup/CURRENT.md`
- `docs/epics/verification/36-migration-contract.json`
- `docs/epics/verification/36-verify-migration.py`
- `package.json`
- `package-lock.json`
- `vendors/kburson-ai-task-manager-0.1.0.tgz`
- `.gitignore`
- `AGENTS.md`
- `.agents/skills/task/SKILL.md`
- `docs/epics/2026-11-02-36-documentation-publication.md`
