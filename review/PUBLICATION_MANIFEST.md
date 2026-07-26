# Publication Manifest

**Candidate:** Agent Runtime Boundaries 0.2
**Status:** PUBLIC DRAFT — 0.2 update surface
**Prepared:** 2026-07-26

## Public files

| File | Mode |
|---|---|
| `README.md` | descriptive entry point |
| `AGENTS.md` | reviewer guidance |
| `spec/00_SCOPE_AND_STATUS.md` | descriptive / analytical |
| `spec/01_FUNCTIONAL_BOUNDARIES.md` | functional reconstruction |
| `spec/02_USER_CONTROL_PLANE_AND_OBSERVABILITY.md` | functional reconstruction |
| `spec/03_CLOSURE_PROVENANCE_AND_NEXT_ACTION.md` | operational proposal |
| `spec/04_CROSS_SPECIFICATION_CLAIM_BOUNDARIES.md` | cross-specification analytical mapping |
| `references/RELATED_PUBLIC_SPECS.md` | fixed-revision review record |
| `review/PUBLICATION_MANIFEST.md` | publication control |
| `review/2026-07-26_MAPPING_UPDATE_REVIEW.md` | fixed-candidate review trace |
| `review/test_publication.py` | executable publication checks |
| `.github/workflows/docs.yml` | independent-runner publication gate |
| `.gitignore` | generated-file exclusion |
| `LICENSE` | Apache-2.0 license |

## Baseline publication trace

The 0.1 baseline was published on 2026-07-25:

```text
repository: https://github.com/gv1983us-commits/agent-runtime-boundaries
initial commit: dd8c11d1cb06164f9c010d430dedb1fa2f206bb1
pre-update main: 791b1ebbc3fae8c926de8c436bd64aa55ba99fc3
```

The original independent disclosure review applied to the eight-file 0.1 baseline and the source revisions recorded at that time. It found no blocking disclosure or scope issue. That finding is not silently extended to changed 0.2 content.

## 0.2 mapping update

The 0.2 update adds:

1. current accepted commits for MPAA, PCA, BEC, and the Review Protocol;
2. four explicit owner/mapping tables;
3. allowed and forbidden inferences with required evidence;
4. separate treatment of capability, authorization, invocation, evidence, verification, and result;
5. separate treatment of identity-profile continuity and process continuation;
6. separate treatment of `closed`, `delivered`, `persisted`, `retrievable`, working state, and `committed`;
7. an explicit statement that ARB-03 remains a proposal and has no selected normative home;
8. executable publication checks and GitHub Actions.

## Review boundary

No independent content-review claim is made for the 0.2 mapping update. The update is self-reviewed against exact owning sources and subjected to deterministic checks. GitHub Actions runs the same checks on independent clean runners; runner success establishes reproducibility of those checks, not independent agreement with the analytical judgments.

## Fixed source revisions for 0.2

```text
MPAA:           1d369f6cd091b99f9492cfaf730f0a170b55106e
PCA:            6ad1a86d7c09b36839d162c580f84f05cfe4a598
BEC:            bb46f5f8aac96d1cffba7a334c5d17fb331ef3af
Review Protocol: 595c08b877e4dfb14593454c2eec7c8f5df46c28
```

## Required local gates

- publication unit tests pass;
- Python checker compiles;
- all relative links resolve;
- Markdown fences, final newlines, and trailing whitespace pass;
- all specification documents declare status and mode;
- required four-way mappings and pinned revisions are present;
- no stale PCA nomenclature remains;
- no local path or credential marker is present;
- a separate disclosure review checks named identities, products, events, account data, and source reconstruction risk;
- `git diff --check` passes.

## Ownership boundary

ARB is not canonical for MPAA, PCA, BEC, or the Review Protocol. Its mapping does not transfer definitions, conformance, validation, or result authority. ARB-03 remains a proposal until an owning specification explicitly adopts a rule and supplies its own conformance boundary.
