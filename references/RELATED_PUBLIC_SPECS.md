# Related Public Specifications

**Status:** Candidate review record
**Review date:** 2026-07-25
**Source policy:** GitHub-first; exact inspected revisions recorded below

## Reviewed revisions

| Source | Repository | Branch | Inspected commit |
|---|---|---|---|
| Minimal Portable Agent Architecture (MPAA) | https://github.com/gv1983us-commits/mpaa | `main` | `0288ccf54c12607f204ed2be475169b2e02b25e8` |
| Process Continuity Architecture (PCA) | https://github.com/gv1983us-commits/pca | `main` | `9b7df45a1d9872d9fa78b3afa13401042d009174` |
| Behavioral Execution Contract (BEC) | https://github.com/gv1983us-commits/behavioral-execution-contract | `main` | `22ccd889fe11f14a7837297aeb7784f4de473035` |
| Repository Canon and Review Protocol | https://github.com/gv1983us-commits/repository-canon-review-protocol | `main` | `90a5765094d5267ebdf8000966b6400b15df04f3` |

At review time, each local checkout matched its corresponding `origin/main` with divergence `0/0`.

## Scope relationship

### MPAA

MPAA owns the neutral architecture, identity-profile boundary, runtime contract, authorization model and runtime reporting requirements.

This repository contributes explanatory boundary examples only. It does not redefine MPAA participants, layers, conformance or report schemas.

### PCA

PCA owns the representation and assessment of continuity claims across changing hosts, organs, environments and historical states.

This repository uses compatible terms such as transition, provenance, evidence and human participant but does not assert a continuation claim or define PCA conformance.

### BEC

BEC owns execution-evidence records for task-scoped claims, including capability, authorization, invocation, evidence, validation and result status.

This repository explains why visible status and plausible model text are insufficient execution evidence. It does not add fields to the BEC schema or compute deployment level.

### Repository Canon and Review Protocol

The review protocol owns source-selection and reproducibility rules. This candidate records exact source revisions and reports discrepancies rather than silently merging source states.

## Reported nomenclature discrepancy

At the inspected revision, the Repository Canon and Review Protocol expands `PCA` as **Persistent Continuity Architecture**, while the canonical PCA repository identifies itself as **Process Continuity Architecture**.

This candidate uses the title from the canonical PCA repository. It does not silently correct the review protocol and does not claim that the discrepancy has been resolved upstream.

## No transitive canonical status

Publication of this repository would not make it canonical for MPAA, PCA, BEC or their review protocol. A reference does not transfer normative ownership.
