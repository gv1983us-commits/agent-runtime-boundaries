# Related Public Specifications

**Status:** Fixed-revision review record
**Review date:** 2026-07-26
**Source policy:** GitHub-first; exact inspected revisions recorded below

## Reviewed revisions

| Source | Repository | Branch | Inspected commit |
|---|---|---|---|
| Minimal Portable Agent Architecture (MPAA) | https://github.com/gv1983us-commits/mpaa | `main` | [`1d369f6cd091b99f9492cfaf730f0a170b55106e`](https://github.com/gv1983us-commits/mpaa/tree/1d369f6cd091b99f9492cfaf730f0a170b55106e) |
| Process Continuity Architecture (PCA) | https://github.com/gv1983us-commits/pca | `main` | [`6ad1a86d7c09b36839d162c580f84f05cfe4a598`](https://github.com/gv1983us-commits/pca/tree/6ad1a86d7c09b36839d162c580f84f05cfe4a598) |
| Behavioral Execution Contract (BEC) | https://github.com/gv1983us-commits/behavioral-execution-contract | `main` | [`bb46f5f8aac96d1cffba7a334c5d17fb331ef3af`](https://github.com/gv1983us-commits/behavioral-execution-contract/tree/bb46f5f8aac96d1cffba7a334c5d17fb331ef3af) |
| Repository Canon and Review Protocol | https://github.com/gv1983us-commits/repository-canon-review-protocol | `main` | [`595c08b877e4dfb14593454c2eec7c8f5df46c28`](https://github.com/gv1983us-commits/repository-canon-review-protocol/tree/595c08b877e4dfb14593454c2eec7c8f5df46c28) |

Each GitHub `main` revision was resolved immediately before this review. Conclusions in ARB-04 apply to these immutable commits, not to future branch movement.

## Revision transition from the 2026-07-25 review

| Source | Previously inspected | Current inspected | Relevant change for ARB |
|---|---|---|---|
| MPAA | `0288ccf54c12607f204ed2be475169b2e02b25e8` | `1d369f6cd091b99f9492cfaf730f0a170b55106e` | Current runtime-report validator and explicit prohibition on deriving PCA process continuation from MPAA coordination or identity continuity. |
| PCA | `9b7df45a1d9872d9fa78b3afa13401042d009174` | `6ad1a86d7c09b36839d162c580f84f05cfe4a598` | Portable Core, Transition Record, fail-closed validator, and explicit MPAA/BEC boundaries. |
| BEC | `22ccd889fe11f14a7837297aeb7784f4de473035` | `bb46f5f8aac96d1cffba7a334c5d17fb331ef3af` | Fail-closed validator and explicit rule that `closed` is not next-state commitment. |
| Review Protocol | `90a5765094d5267ebdf8000966b6400b15df04f3` | `595c08b877e4dfb14593454c2eec7c8f5df46c28` | External-standard identity and ownership rules; PCA nomenclature corrected in its owning review source. |

The earlier nomenclature discrepancy is therefore a resolved historical trace, not a current discrepancy. The current Review Protocol and PCA repository both use **Process Continuity Architecture**. This update records the revision change rather than silently mixing the old and new source states.

## Scope relationship

### MPAA

MPAA owns the neutral architecture, Identity Profile boundary, Runtime Contract, authorization model, Runtime Report, and MPAA conformance requirements.

ARB contributes explanatory boundary mappings only. It does not redefine MPAA participants, layers, authorization, task results, identity continuity, conformance, or report schemas.

### PCA

PCA owns representation and assessment of bounded process-continuation claims across explicit transitions.

ARB uses related terms such as state, transition, provenance, evidence, host, and corpus but does not issue a PCA continuation result or define PCA conformance.

### BEC

BEC owns portable execution-evidence records for task-scoped claims, including capability, authorization, invocation, evidence, validation, deployment level, and return state.

ARB explains why visible status, plausible text, delivery, or closure are insufficient for stronger execution or next-state claims. It does not add fields to BEC or compute a deployment level.

### Repository Canon and Review Protocol

The Review Protocol owns fixed-source selection, discrepancy reporting, and reproducibility rules. It does not own the mapped architectural or operational conclusions.

## No transitive canonical status

Publication of ARB does not make it canonical for MPAA, PCA, BEC, or the Review Protocol. A citation carries a trace; it does not transfer normative ownership or import a result.
