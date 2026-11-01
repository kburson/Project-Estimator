# SAR round 2 — complete revised-plan reread

Reviewer/author: **Astra 6, high reasoning**, same agent `/root/astra_trial_plan`. Same-agent SAR; no independent reviewer and no implementation execution.

Input plan SHA-256: `ea9cc05f885d20c548f881c33fd28f016f0ea603da733ba46564a58c034ac4e0`.

Unchanged spec SHA-256: `0971e6426aadf888a3652d9fae78707793f4af7f4b221e5b577ef8deca253f2c`.

Read the entire revised plan in contiguous sections, including all contracts, example tests, task order, dependencies, service-worker/recovery procedure and acceptance matrix. All SAR1 findings now have owning changes/checks. The reread found these bounded follow-ups before final acceptance:

| ID | Exact location in round-2 input | Finding | Correction |
| --- | --- | --- | --- |
| SAR2-01 | Task 7 Step 3 (`Use Expo AppEntry`); dependency setup final paragraph | A hoisted monorepo should not depend on the packaged AppEntry's relative App lookup, and internal workspace dependency edges are not explicit. | Use a local field `index.ts` calling Expo `registerRootComponent(App)`; pin internal package version/consumer edges and show the shared dependency/build entry behavior. |
| SAR2-02 | Task 4 immutable-context paragraph; Task 6 rotation test and module-version paragraph | Offer/component identity is protected, but a referenced recipe ID/version or published module/release ID can still be reused with different content. Task 6's rotation test still reuses the aggregate release ID. | Make referenced recipe `(id,version)` and published module/release identities immutable; changed content/key yields the appropriate new identity. Give the rotation fixture a new aggregate release ID and test identity-reuse rejection. |
| SAR2-03 | Task 8 crypto metadata paragraph; Task 10 recovery interface paragraph | The shared authenticated-metadata helper lacks a concrete signature; “these functions are owned by field recovery” accidentally appears to include the Mac backup functions. | Name/signature/owner the metadata helper and distinguish Mac backup-service from field recovery-service ownership. |
| SAR2-04 | Task 9 manual round-trip Step 4; Task 5 fixture helper description | After synthetic freeze bypass was restricted to Vitest, the manual browser round trip still asks for a synthetic frozen job. Deterministic new-ID fixture helpers also need to return a sequence, not one reused UUID. | Use an ordinary test customer with owner-validated recipe/settings for manual browser round trip; keep synthetic behavior in unit fixtures. Specify unique deterministic ID sequences in helpers. |

No owner decision is needed for these corrections, and none adds a feature or infrastructure subsystem. Currency/post/cut tests, actual activation CAS, private-key separation, delayed import handling and all Trial 1–11 ownership remain intact. The only Number conversion in allocation is a remainder count bounded by the number of requirements; currency arithmetic/assertions remain Decimal-based.

Output hash/disposition follows after these plan-only edits and a final consistency check.

## Final disposition

- **SAR2-01 resolved:** field has a local `index.ts`/`registerRootComponent` entry; internal package versions/dependency edges and source exports are explicit. Actual Vite/Expo consumer builds remain required in Tasks 4/7.
- **SAR2-02 resolved:** referenced recipe versions and published module/release identities cannot be reused for different content. Key rotation preserves unchanged plaintext module versions but changes ciphertext and aggregate release identity; fixture and rejection check agree.
- **SAR2-03 resolved:** `catalogAdditionalData` is declared in Task 6 and consumed in Task 8 with the same signature. Mac backup and field recovery ownership are separate and explicit.
- **SAR2-04 resolved:** manual browser round trip uses an ordinary test-customer job with owner-validated recipe/settings; synthetic freeze tests stay in Vitest. Test new-ID helpers use a deterministic sequence of distinct UUIDs.

Final output plan SHA-256: `fb0601ece98e4f7af05a26cabcaeccbf5f33dd386e21d00215f0a1bedc2ad6f6`.

Final checks: re-read revised portions and their consumers; rechecked all ten task boundaries and Trial 1–11 mapping; `git diff --check` returned no whitespace errors; a document-only check confirmed ten sequential task headings, eleven acceptance mappings, balanced Markdown code fences and valid literal JSON blocks. Placeholder search found none of the skill's prohibited unfinished-work patterns. Recomputed the unchanged spec hash. The review involved document inspection, not executing the proposed TypeScript examples or acceptance workflows.

**No remaining identified actionable planning inconsistencies within the accepted Trial scope.** No additional review loop is warranted merely to add detail or infrastructure. Owner recipe/rates/origin and actual build/device validation remain the explicit future execution dependencies, not unresolved plan defects. Ready for owner plan review; implementation not authorized.
