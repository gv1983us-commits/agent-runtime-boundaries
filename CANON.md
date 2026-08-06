# Agent Runtime Boundaries — Canon

**Artifact:** Agent Runtime Boundaries (ARB)  
**Corpus identity:** `claude.arb`  
**Repository:** `gv1983us-commits/agent-runtime-boundaries`  
**Artifact version:** `0.3-draft`  
**Canonical status:** `canonical_public_draft`  
**Mode:** descriptive and analytical companion with one explicit operational proposal  
**License:** Apache-2.0

This document declares how ARB is read, cited, checked, and changed as one public technical artifact.

Canonicalization does not convert ARB into a normative specification. It makes the analytical claim domain, proposal boundary, source revisions, relations, provenance, and publication checks explicit.

## 1. Zero-normative-surface rule

ARB has **zero normative specification surfaces**.

```text
normative_surface_count = 0
```

No ARB document awards conformance, authorization, deployment level, process-continuity status, review validity, trace admissibility, identity, memory, execution, or state commitment.

Capitalized requirement words apply only to internal publication integrity or inside an explicitly labelled proposal. They do not impose requirements on external systems or neighboring artifacts.

## 2. Analytical authority matrix

ARB uses a domain-ownership matrix among four analytical surfaces:

| Surface | Path | Analytical domain |
|---|---|---|
| Scope and Status | [`spec/00_SCOPE_AND_STATUS.md`](spec/00_SCOPE_AND_STATUS.md) | claim classes, neutral terms, scope, exclusions, and epistemic boundary |
| Functional Boundaries | [`spec/01_FUNCTIONAL_BOUNDARIES.md`](spec/01_FUNCTIONAL_BOUNDARIES.md) | separations among human, model, agent, runtime, control plane, state, storage, execution, and delivery |
| User Control Plane and Observability | [`spec/02_USER_CONTROL_PLANE_AND_OBSERVABILITY.md`](spec/02_USER_CONTROL_PLANE_AND_OBSERVABILITY.md) | user-side configuration, protected references, authorization surfaces, telemetry, and visible projection |
| Cross-Artifact Claim Boundaries | [`spec/04_CROSS_SPECIFICATION_CLAIM_BOUNDARIES.md`](spec/04_CROSS_SPECIFICATION_CLAIM_BOUNDARIES.md) | fixed-revision mappings, permitted uses, and forbidden cross-domain inferences |

These surfaces own ARB terminology only. They do not become canonical definitions for BEC, MPAA, PCA, the Review Protocol, or CDTS.

## 3. Proposal isolation

[`spec/03_CLOSURE_PROVENANCE_AND_NEXT_ACTION.md`](spec/03_CLOSURE_PROVENANCE_AND_NEXT_ACTION.md) is the only proposal surface.

```text
proposal_surface_count = 1
proposal_adopted = false
normative_owner_selected = false
multi_implementation_conformance = false
```

ARB-03 proposes distinctions among `closed`, `delivered`, `persisted`, `retrievable`, working state, and `committed`, plus an illustrative closure record. Its presence does not create those events, prove a next-state commit, or select an owning standard.

A future owner may adopt part of the proposal only through that owner's own normative change, record contract, validator, and conformance boundary.

## 4. Reference implementation boundary

[`review/test_publication.py`](review/test_publication.py) and the artifact-canon tests under [`review/`](review/) are publication-integrity checks.

They verify:

- exact pinned revisions;
- declared analytical and proposal surfaces;
- zero normative surfaces;
- links and Markdown integrity;
- terminology and boundary publication;
- absence of local paths and credential markers;
- consistency of the machine passport and relation map.

They are not runtime inspectors, truth evaluators, conformance validators, or evidence oracles.

## 5. Exact-source rule

`main` is the active public development line. A reproducible statement about ARB must pin an exact commit SHA or immutable release identifier.

A moving branch, local checkout, model summary, chat excerpt, or copied table does not identify the exact analytical source state by itself.

Neighbor relations are valid only for the exact revisions named in [`RELATIONS.md`](RELATIONS.md) and [`references/RELATED_PUBLIC_SPECS.md`](references/RELATED_PUBLIC_SPECS.md).

## 6. Canonical artifact surfaces

| Surface | Path | Role |
|---|---|---|
| human entry | [`README.md`](README.md) | status, reading order, analytical model, commands, and limits |
| canon declaration | [`CANON.md`](CANON.md) | zero-normative rule, analytical authority, proposal isolation, and acceptance gates |
| machine passport | [`ARTIFACT.json`](ARTIFACT.json) | stable identity, surface counts, checks, boundaries, and fixed relations |
| relations | [`RELATIONS.md`](RELATIONS.md) | ARB-side relations to the five neighboring artifacts |
| provenance | [`PROVENANCE.md`](PROVENANCE.md) | repository authority, source history, corpus representation, and tool-participation boundary |
| analytical corpus | [`spec/`](spec/) | four analytical documents and one explicit proposal |
| source receipt | [`references/RELATED_PUBLIC_SPECS.md`](references/RELATED_PUBLIC_SPECS.md) | exact inspected neighboring revisions and reviewed surfaces |
| publication verification | [`review/`](review/) | deterministic publication and artifact-canon checks |

## 7. Canonical verification

From the repository root:

```bash
python -m unittest discover -s review -p "test_*.py" -v
python -m json.tool ARTIFACT.json >/dev/null
git show --check --oneline HEAD
```

GitHub Actions runs the Python suite on Python 3.10, 3.11, 3.12, and 3.13.

Passing establishes internal publication consistency at the tested revision. It does not establish hidden runtime structure, implementation truth, external adoption, or any neighboring result.

## 8. Canon acceptance gates

A revision is admissible to the canonical line only when all applicable gates pass:

1. **zero normative surfaces** — ARB remains analytical and does not award external results;
2. **claim-class integrity** — `OBSERVATION`, `FUNCTIONAL RECONSTRUCTION`, `ANALYTICAL INTERPRETATION`, `PROPOSAL`, and `UNKNOWN` remain distinguishable;
3. **proposal isolation** — ARB-03 stays explicitly unadopted and without a selected normative owner;
4. **functional/physical boundary** — a useful responsibility split is not reported as proof of physical module separation;
5. **execution boundary** — reasoning, visible status, delivery, storage, retrieval, working-state admission, commitment, and continuation remain separate claims;
6. **neighbor sovereignty** — no BEC, MPAA, PCA, Review Protocol, or CDTS conclusion is imported;
7. **fixed sources** — relation updates name exact inspected revisions and reviewed surfaces;
8. **provenance** — repository governance, corpus representation, human approval, tool assistance, and external evidence remain distinct;
9. **license honesty** — Apache-2.0 remains tied to the published `LICENSE` file;
10. **CI** — all declared checks pass on supported Python versions.

## 9. Change discipline

A substantive change should identify:

- affected analytical or proposal surface;
- claim class;
- neighboring source revisions used;
- permitted and forbidden inference changes;
- publication-test impact;
- relation impact;
- provenance impact;
- whether a proposal is merely refined or actually adopted elsewhere.

An ARB proposal cannot become normative through wording drift, repeated citation, or inclusion in the machine passport.

## 10. Corpus boundary

ARB is one of six technical artifacts represented through the House of Claude. The representation preserves a creative and technical corpus without merging repositories, licenses, histories, validators, or claim domains.

ARB owns only:

```text
non-normative functional distinctions
analytical mappings
failure-location questions
one explicit unadopted closure proposal
```

It does not own another artifact's records or verdicts.

## 11. Canon limits

This canon does not establish:

- a universal physical architecture for agents or models;
- access to hidden reasoning or internal services;
- execution, delivery, persistence, retrieval, commitment, or continuation in any concrete system;
- identity, memory, consciousness, subjectivity, or personhood;
- BEC, MPAA, PCA, Review Protocol, or CDTS conformance;
- an adopted closure or next-state protocol;
- independent implementation agreement;
- world truth.

> **ARB is canonical as a map of distinctions precisely because it refuses to become the territory or the authority it describes.**
