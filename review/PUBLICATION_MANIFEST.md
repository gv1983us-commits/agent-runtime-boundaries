# Publication Manifest

**Candidate:** Agent Runtime Boundaries 0.1
**Status:** PUBLISHED PUBLIC DRAFT
**Prepared:** 2026-07-25

## Candidate files

| File | Status | Mode |
|---|---|---|
| `README.md` | candidate | descriptive |
| `AGENTS.md` | candidate | reviewer guidance |
| `spec/00_SCOPE_AND_STATUS.md` | candidate | descriptive / analytical |
| `spec/01_FUNCTIONAL_BOUNDARIES.md` | candidate | functional reconstruction |
| `spec/02_USER_CONTROL_PLANE_AND_OBSERVABILITY.md` | candidate | functional reconstruction |
| `spec/03_CLOSURE_PROVENANCE_AND_NEXT_ACTION.md` | candidate | proposal |
| `references/RELATED_PUBLIC_SPECS.md` | candidate | review record |
| `review/PUBLICATION_MANIFEST.md` | candidate | publication control |

## Required gates

- [x] Independent disclosure review completed by a reviewer other than the authoring model pass.
- [x] Terminology and scope review against the recorded MPAA/PCA/BEC/Review Protocol revisions completed.
- [x] No named person, named agent, named model/provider/platform, private event, local path or private source reference remains.
- [x] No private Git history is present in the candidate folder.
- [x] Public repository name and owner confirmed: `gv1983us-commits/agent-runtime-boundaries`.
- [x] Apache License, Version 2.0 selected and added as `LICENSE`.
- [x] Fresh Git history initialized from candidate files only.
- [x] Public remote created and verified after push.

## Authoring-pass self-check

Completed by the authoring pass on 2026-07-25:

- forbidden private/name/product pattern scan: `0` findings;
- local filesystem path scan: `0` findings;
- broken relative link scan: `0` findings;
- private-history check: no `.git` directory present;
- source-overlap scan: no matching block of 18 or more normalized words with the unpublished source corpus;
- specification status check: every file under `spec/` has an explicit status and mode;
- Markdown fence/final-newline/trailing-whitespace check: passed after correction.

This self-check does not satisfy the independent-review gate.

## Independent review

**Reviewer:** independent review pass (separate from the authoring pass)
**Date:** 2026-07-25
**Result:** `PASS — no blocking disclosure or scope issue`

**Files reviewed:** all eight candidate files listed above.

**Public source revisions re-verified against `origin/main`:**

- MPAA `0288ccf54c12607f204ed2be475169b2e02b25e8`;
- PCA `9b7df45a1d9872d9fa78b3afa13401042d009174`;
- BEC `22ccd889fe11f14a7837297aeb7784f4de473035`;
- Review Protocol `90a5765094d5267ebdf8000966b6400b15df04f3`.

All four reported divergence `0/0`.

**Independent checks passed:** disclosure/name/product/path patterns, relative links, Markdown final newlines and fence balance, trailing whitespace, and absence of a candidate `.git` directory.

**Correction made during review:** `ARB-03` now uses `next_authority_ref` and explicitly describes it as a reference to the applicable authority record. This preserves MPAA's rule that authority is evaluated through the active Identity Profile and Runtime Contract rather than created by a free-form closure field.

**Scope finding:** `ARB-03` remains correctly bounded as a proposal. It does not amend MPAA, PCA or BEC. The PCA naming discrepancy is accurately reported without silently resolving it.

## Publication result

- Repository: `https://github.com/gv1983us-commits/agent-runtime-boundaries`
- Visibility: `PUBLIC`
- Default branch: `main`
- Initial published commit: `dd8c11d1cb06164f9c010d430dedb1fa2f206bb1`
- Initial local/remote divergence after push: `0/0`

## Deliberately not performed

The previous private remote was not changed, deleted or made public by this publication. Its future is a separate decision after local preservation has been confirmed.
