# Publication Manifest

**Candidate:** Agent Runtime Boundaries 0.3-draft  
**Status:** `canonical_public_draft` analytical artifact  
**Prepared:** 2026-08-06  
**Normative specification surfaces:** 0

## Public files

| File | Mode |
|---|---|
| `README.md` | human entry point |
| `CANON.md` | zero-normative rule, analytical authority, proposal isolation, and acceptance gates |
| `ARTIFACT.json` | machine passport |
| `RELATIONS.md` | five-neighbor relation surface |
| `PROVENANCE.md` | public provenance and authority separation |
| `AGENTS.md` | reviewer and coding-agent guidance |
| `spec/00_SCOPE_AND_STATUS.md` | descriptive / analytical scope and claim classes |
| `spec/01_FUNCTIONAL_BOUNDARIES.md` | functional reconstruction |
| `spec/02_USER_CONTROL_PLANE_AND_OBSERVABILITY.md` | functional reconstruction |
| `spec/03_CLOSURE_PROVENANCE_AND_NEXT_ACTION.md` | explicit unadopted operational proposal |
| `spec/04_CROSS_SPECIFICATION_CLAIM_BOUNDARIES.md` | five-artifact analytical mapping |
| `references/RELATED_PUBLIC_SPECS.md` | current fixed-revision source receipt |
| `review/PUBLICATION_MANIFEST.md` | publication control |
| `review/2026-07-26_MAPPING_UPDATE_REVIEW.md` | historical 0.2 fixed-candidate review trace |
| `review/2026-08-06_CANONIZATION_REVIEW.md` | 0.3 canonization audit |
| `review/test_publication.py` | publication-discipline checks |
| `review/test_artifact_canon.py` | machine and human canon checks |
| `.github/workflows/docs.yml` | clean-runner publication gate |
| `.gitignore` | generated-file exclusion |
| `LICENSE` | Apache-2.0 license |

## Version history

### 0.1 baseline

Published on 2026-07-25:

```text
repository: https://github.com/gv1983us-commits/agent-runtime-boundaries
initial commit: dd8c11d1cb06164f9c010d430dedb1fa2f206bb1
pre-0.2 main: 791b1ebbc3fae8c926de8c436bd64aa55ba99fc3
```

The original disclosure review applied to the eight-file 0.1 baseline and the source revisions recorded at that time. Its finding is not silently extended to later content.

### 0.2 mapping update

The 0.2 update added:

- fixed-revision MPAA, PCA, BEC, and Review Protocol mapping;
- explicit permitted and forbidden inferences;
- separation of `closed`, `delivered`, `persisted`, `retrievable`, working state, and `committed`;
- publication checks and GitHub Actions.

The 0.2 source receipt remains historical provenance in repository history.

### 0.3 canonization

The 0.3 update adds:

1. `CANON.md`, `ARTIFACT.json`, `RELATIONS.md`, and `PROVENANCE.md`;
2. an executable authority model with **0 normative surfaces**, 4 analytical surfaces, and 1 proposal surface;
3. explicit ARB-03 `adopted: false` and `normative_owner_selected: false` boundaries;
4. accepted canonical revisions for BEC, MPAA, PCA, and the Review Protocol;
5. the first reciprocal ARB↔CDTS relation at `f91dbc003519efd5264655d905d0530dbfeac2fd`;
6. a current five-source receipt;
7. artifact-canon tests;
8. a complete 0.3 analytical corpus aligned around delivery, persistence, retrieval, working-state admission, commitment, and continuation.

## Current fixed source revisions

```text
BEC:             62f2b7940b5ca7a4a8b24150b9c45a6ab5d97261
MPAA:            0d1aaf35cc4826622f3312fdd2a1c2d40890b965
PCA:             a669f023198615ad929f42df84f19380b57ca5ea
Review Protocol: b4205ffd91a6316ab40243cbf8161a1c512cae1f
CDTS:            f91dbc003519efd5264655d905d0530dbfeac2fd
```

## Authority boundary

```text
normative surfaces: 0
analytical surfaces: 4
proposal surfaces: 1
```

ARB-03 remains an unadopted proposal. No publication file, test, CI run, citation, or corpus representation selects a normative owner for it.

ARB remains authoritative only for its own analytical classification and publication state. It is not canonical for the records, schemas, validators, or results of neighboring artifacts.

## Review boundary

No independent analytical-truth claim is made for the 0.3 update.

The update is reviewed against exact owning sources and subjected to deterministic checks. GitHub Actions runs the same checks on clean runners. Runner success establishes reproducibility of the checks, not independent agreement with analytical judgments or access to hidden runtime internals.

## Required gates

- `ARTIFACT.json` parses and declares `normative_surface_count: 0`;
- four analytical surfaces and one proposal surface are exact and complete;
- ARB-03 remains unadopted and without a selected normative owner;
- five current neighboring revisions are present in the source receipt, relation map, and machine passport;
- every relation keeps `conclusion_imported: false`;
- the rejected inference chain is published;
- all relative links resolve;
- Markdown fences, final newlines, tables, and end-of-line policy pass;
- Markdown lines use either no trailing spaces or exactly two spaces for a hard break;
- all specification documents declare status, mode, and version;
- no stale PCA nomenclature remains;
- no local path or credential marker is present;
- Apache-2.0 remains tied to `LICENSE`;
- Python 3.10, 3.11, 3.12, and 3.13 complete the full suite;
- `git -c core.whitespace=-blank-at-eol show --check --oneline HEAD` passes for non-Markdown-EOL whitespace errors.

## Ownership formula

> **The publication can be canonical while the analysis remains non-normative and the proposal remains unadopted.**
