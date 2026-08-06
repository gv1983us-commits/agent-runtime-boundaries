# ARB Canonization Review — 2026-08-06

**Candidate repository:** `gv1983us-commits/agent-runtime-boundaries`  
**Starting revision:** `6b6c32cd467a4b5e4863d082b9da5bdd40d7dced`  
**Review mode:** fixed-revision analytical-artifact canonization  
**Result:** admitted after canonical surfaces, current relations, tests, and CI pass

## 1. Starting condition

The starting repository already contained a strong public analytical corpus:

- explicit descriptive/analytical status;
- five claim classes;
- functional distinctions among model, agent, runtime, platform, state, storage, execution, observability, delivery, and commitment;
- one explicit closure proposal;
- fixed-revision MPAA/BEC/PCA/Review Protocol mappings;
- publication tests on Python 3.10–3.13;
- Apache-2.0 license.

It did not yet expose a machine passport, canon declaration, five-neighbor relation surface, public provenance surface, or an executable zero-normative-surface invariant.

## 2. Material findings

### Finding A — ARB must not be normalized into the architecture of the previous artifacts

BEC, MPAA, PCA, and the Review Protocol own normative domains. ARB explicitly does not.

Creating a conventional normative Core for ARB would contradict the source artifact. The accepted authority model is therefore:

```text
0 normative surfaces
4 analytical surfaces
1 explicit unadopted proposal surface
```

### Finding B — the current mapping used historical neighboring revisions

The active 0.2 mapping pinned:

```text
MPAA            1d369f6cd091b99f9492cfaf730f0a170b55106e
BEC             bb46f5f8aac96d1cffba7a334c5d17fb331ef3af
PCA             6ad1a86d7c09b36839d162c580f84f05cfe4a598
Review Protocol 595c08b877e4dfb14593454c2eec7c8f5df46c28
```

Those pins remain valid historical review provenance, but they no longer identify the accepted canonical revisions of the four completed corpus artifacts.

The active 0.3 relation surface was updated after inspection to:

```text
BEC             62f2b7940b5ca7a4a8b24150b9c45a6ab5d97261
MPAA            0d1aaf35cc4826622f3312fdd2a1c2d40890b965
PCA             a669f023198615ad929f42df84f19380b57ca5ea
Review Protocol b4205ffd91a6316ab40243cbf8161a1c512cae1f
CDTS            f91dbc003519efd5264655d905d0530dbfeac2fd
```

### Finding C — CDTS was absent from the ARB relation surface

CDTS now contains an explicit resistance case against treating ARB as a normative owner. ARB therefore needs a reciprocal boundary:

```text
ARB may be cited as analytical context
ARB must not be declared a normative owner
CDTS admissibility does not make ARB interpretation true
ARB mapping does not validate a CDTS linkage assertion
```

### Finding D — ARB-03 must remain isolated

ARB-03 uses proposal-language and an illustrative closure record. It has no selected normative owner, validator, implementation corpus, or conformance result.

The machine passport and canon tests now make these negative facts explicit and fail closed if the proposal is relabelled as adopted.

### Finding E — publication success must not be mistaken for analytical truth

The existing checker verifies publication discipline. It does not inspect hidden runtimes, authenticate physical architecture, or prove an analytical reconstruction.

The accepted canon therefore identifies the checker as non-normative and limits passing results to internal publication consistency.

## 3. Canonical surfaces added

```text
CANON.md
ARTIFACT.json
RELATIONS.md
PROVENANCE.md
review/2026-08-06_CANONIZATION_REVIEW.md
review/test_artifact_canon.py
```

## 4. Active analytical and proposal surfaces

```text
Analytical:
  spec/00_SCOPE_AND_STATUS.md
  spec/01_FUNCTIONAL_BOUNDARIES.md
  spec/02_USER_CONTROL_PLANE_AND_OBSERVABILITY.md
  spec/04_CROSS_SPECIFICATION_CLAIM_BOUNDARIES.md

Proposal:
  spec/03_CLOSURE_PROVENANCE_AND_NEXT_ACTION.md
```

No active normative specification surface was created.

## 5. Acceptance gates

The candidate is accepted only when:

- `ARTIFACT.json` declares zero normative surfaces;
- exactly four analytical surfaces and one proposal surface are declared;
- ARB-03 remains `adopted: false` with no selected normative owner;
- all five neighboring repositories and exact reviewed revisions are present;
- every relation declares `conclusion_imported: false`;
- Apache-2.0 is tied to the repository license;
- README, Canon, Relations, Provenance, source receipt, and proposal boundary agree;
- publication tests and artifact-canon tests pass on Python 3.10–3.13;
- no local path, credential, private-source, or hidden-implementation overclaim is published.

## 6. Review limits

This canonization does not establish:

- universal correctness of the analytical model;
- physical separation of the described functions;
- access to hidden model reasoning or platform internals;
- implementation of ARB-03;
- external adoption or independent agreement;
- execution, state commitment, continuation, identity, or memory;
- any neighboring conformance result.

## 7. Acceptance formula

> **ARB is accepted as a canonical analytical artifact only while its zero-normative boundary remains explicit and executable.**
