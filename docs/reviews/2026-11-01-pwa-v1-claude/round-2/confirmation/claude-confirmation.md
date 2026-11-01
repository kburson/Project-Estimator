[10:08:41]
# Follow-up on R2-1 and R2-2

**Verdict: Ready for owner review.** Both wording fixes resolve their findings, and neither creates a concrete inconsistency.

## R2-1: customer tax basis — Resolved

- **The basis is now defined** (§9, l.126). Customer tax is charged on the final selling amount of each taxable segment the owner selects, after markup or override. Manual items follow their segment, and the tax is not marked up again.
- **Overrides can't be split** (§9, l.126). The spec now says there is no automatic material/labor split of an overridden selling amount, so builds can't diverge on that.
- **Manual material items are covered** (§9, l.126). Each one now has an explicit purchase-tax-included flag and, if tax isn't included, an owner-entered rate. This matches the existing rule against taxing a tax-included price twice.
- **The test pins it down** (§15.5, l.224). A $2,000 override at a 10% test rate must give $200 tax whatever the internal split, and manual items are tested both with and without purchase tax included. This matches my round-2 failure example.

## R2-2: quote snapshot terminology — Resolved

- **One snapshot mechanism for office and field** (§4 Office review, l.57; §6, l.84; §9, l.130):
  - Field snapshots are always Preliminary.
  - When freezing an office-reviewed quote, the owner chooses Preliminary or Issued.
  - The status is frozen with the snapshot, so issuing an older Preliminary quote creates a new snapshot.
  - Comparing alternatives and revisions is explicitly left to complete v1.
- **Backup and restore** (§12, l.191) now preserves all frozen Preliminary/Issued snapshots and the source-ID mappings.
- **The test covers it** (§15.4, l.223). It checks that both the field and office labels are frozen and don't change when a later status is chosen.

## Consistency check of these edits

- §6 says repeating Present/export "without changes" reuses the existing snapshot, and lists only scope or price changes as creating a new one. §4 adds that issuing a Preliminary quote creates a new snapshot. Together that means a status change counts as a change. The two sections agree; they don't conflict.
- Field snapshots imported to the Mac stay Preliminary (§12, l.183, 187). Issuing from the office creates a new snapshot, which is consistent with "Do not overwrite the submitted field version" (§4, l.57).
- No section still implies a separate issued-revision workflow in the trial.

No concrete defect remains in these edits.

## Limits

I read only §4, §6, §9, §12, acceptance cases 4 and 5 (plus the nearby lines shown) and `round-2/minor-clarifications.md`. This was not a fresh broad review. No files were written and nothing was delegated.
