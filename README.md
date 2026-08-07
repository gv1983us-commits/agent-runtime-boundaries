# Agent Runtime Boundaries

[![Documentation checks](https://github.com/gv1983us-commits/agent-runtime-boundaries/actions/workflows/docs.yml/badge.svg)](https://github.com/gv1983us-commits/agent-runtime-boundaries/actions/workflows/docs.yml)

Agent Runtime Boundaries (ARB) is a vendor-neutral analytical map of distinctions that are easy to blur in model-based agent systems.

```text
model output != verified reasoning
reasoning about an action != execution
stored != retrieved
retrieved != active working state
visible status != execution evidence
delivered != committed
BEC closed != next working state committed
committed != PCA process continuation
identity-profile continuity != personal identity
```

**Artifact version:** `0.3`  
**Canonical status:** `canonical_public`  
**Mode:** descriptive and analytical companion  
**Normative specification surfaces:** `0`  
**License:** Apache-2.0

Canonicalization makes the artifact identity, source revisions, analytical authority, proposal boundary, relations, provenance, and publication checks explicit. It does not convert ARB into a standard or give it authority over neighboring artifacts.

## Zero-normative-surface architecture

ARB has four analytical surfaces and one explicit proposal:

| Surface | Status | Owns inside ARB |
|---|---|---|
| [`ARB-00`](spec/00_SCOPE_AND_STATUS.md) | analytical | scope, claim classes, neutral terms, and epistemic boundary |
| [`ARB-01`](spec/01_FUNCTIONAL_BOUNDARIES.md) | analytical | functional responsibilities and independently diagnosable failure boundaries |
| [`ARB-02`](spec/02_USER_CONTROL_PLANE_AND_OBSERVABILITY.md) | analytical | control plane, protected references, authorization surfaces, observability, and projection |
| [`ARB-04`](spec/04_CROSS_SPECIFICATION_CLAIM_BOUNDARIES.md) | analytical | fixed-revision mappings and forbidden cross-domain inferences |
| [`ARB-03`](spec/03_CLOSURE_PROVENANCE_AND_NEXT_ACTION.md) | proposal | illustrative closure record and candidate next-state distinctions |

```text
normative_surface_count = 0
analytical_surface_count = 4
proposal_surface_count = 1
ARB-03 adopted = false
normative owner selected = false
```

The publication checker is not a conformance validator and does not become a normative surface.

## Purpose

ARB separates functional responsibilities that can vary independently:

```text
human participant
agent
model
runtime / host
platform / control plane
working state
persistent corpus and memory surfaces
resources and tools
evidence and user-visible observability
delivery, persistence, retrieval, commitment, and continuation
```

The repository does not assert that every implementation contains the same physical modules. A functional reconstruction can be useful even when responsibilities are collapsed into one service or distributed across several services.

## Claim classes

Every substantive ARB statement should remain identifiable as one of:

- `OBSERVATION`;
- `FUNCTIONAL RECONSTRUCTION`;
- `ANALYTICAL INTERPRETATION`;
- `PROPOSAL`;
- `UNKNOWN`.

A proposal does not become fact or norm through repetition, citation, publication, or inclusion in `ARTIFACT.json`.

## ARB-03 proposal boundary

ARB-03 proposes a minimal closure record and separates:

```text
closed
delivered
persisted
retrievable
admitted into working state
committed
process continuation
```

No field creates the event it names. ARB-03 has no selected normative owner, implementation corpus, validator, or conformance result.

## Five neighboring relations

ARB is an analytical companion to five independently authoritative artifacts:

```text
BEC             owns execution-evidence acceptance
MPAA            owns portable agent architecture and runtime reporting
PCA             owns bounded process-continuity assessment
Review Protocol owns source-selection and review procedure
CDTS            owns cross-domain correlation traces
ARB             owns non-normative analytical distinctions only
```

Current exact reviewed revisions are recorded in:

- [`RELATIONS.md`](RELATIONS.md);
- [`references/RELATED_PUBLIC_SPECS.md`](references/RELATED_PUBLIC_SPECS.md).

ARB does not amend, replace, validate, or import a conclusion from any neighbor. CDTS may cite ARB as analytical context but must not declare ARB a normative owner.

## Reading order

1. [`CANON.md`](CANON.md)
2. [`ARTIFACT.json`](ARTIFACT.json)
3. [`spec/00_SCOPE_AND_STATUS.md`](spec/00_SCOPE_AND_STATUS.md)
4. [`spec/01_FUNCTIONAL_BOUNDARIES.md`](spec/01_FUNCTIONAL_BOUNDARIES.md)
5. [`spec/02_USER_CONTROL_PLANE_AND_OBSERVABILITY.md`](spec/02_USER_CONTROL_PLANE_AND_OBSERVABILITY.md)
6. [`spec/03_CLOSURE_PROVENANCE_AND_NEXT_ACTION.md`](spec/03_CLOSURE_PROVENANCE_AND_NEXT_ACTION.md)
7. [`spec/04_CROSS_SPECIFICATION_CLAIM_BOUNDARIES.md`](spec/04_CROSS_SPECIFICATION_CLAIM_BOUNDARIES.md)
8. [`RELATIONS.md`](RELATIONS.md)
9. [`PROVENANCE.md`](PROVENANCE.md)
10. [`references/RELATED_PUBLIC_SPECS.md`](references/RELATED_PUBLIC_SPECS.md)

## Canonical surfaces

- [`CANON.md`](CANON.md) — zero-normative rule, analytical authority, proposal isolation, and acceptance gates;
- [`ARTIFACT.json`](ARTIFACT.json) — machine identity, surface counts, boundaries, checks, and five fixed relations;
- [`RELATIONS.md`](RELATIONS.md) — ARB-side boundaries with BEC, MPAA, PCA, Review Protocol, and CDTS;
- [`PROVENANCE.md`](PROVENANCE.md) — repository authority, source history, corpus representation, license, and tool participation;
- [`spec/`](spec/) — four analytical documents and one explicit proposal;
- [`review/`](review/) — publication and artifact-canon tests.

## Verification

```bash
python -m unittest discover -s review -p "test_*.py" -v
python -m json.tool ARTIFACT.json >/dev/null
git -c core.whitespace=-blank-at-eol show --check --oneline HEAD
```

The publication checker owns the stricter Markdown end-of-line rule: only no trailing spaces or the exact two-space hard break are accepted. The Git command continues to reject other whitespace errors.

GitHub Actions runs the complete Python suite on 3.10, 3.11, 3.12, and 3.13.

Passing establishes repository publication consistency at the tested revision. It does not establish:

- hidden runtime structure;
- physical module separation;
- execution, delivery, persistence, retrieval, commitment, or continuation;
- correctness of every analytical interpretation;
- neighboring conformance;
- independent implementation agreement;
- world truth.

## Publication history

```text
0.1 — initial public analytical boundary set
0.2 — four-source fixed-revision mapping and publication checks
0.3 — canonical artifact envelope, current five-neighbor mapping, CDTS boundary, and executable zero-normative invariant
```

Earlier source receipts remain historical fixed-revision traces in repository history.

## License

Apache License 2.0. See [`LICENSE`](LICENSE).

> **ARB is a checked analytical map, not the runtime, not the evidence, and not the authority it describes.**
