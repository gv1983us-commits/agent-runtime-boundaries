# Cross-Artifact Claim Boundaries and Mapping

**Document:** ARB-04  
**Status:** PUBLIC DRAFT  
**Mode:** DESCRIPTIVE / ANALYTICAL  
**Version:** 0.3

## 1. Purpose and authority boundary

This document is an analytical companion. It compares claim surfaces owned by BEC, MPAA, PCA, the Repository Canon and Review Protocol, and CDTS, and locates the ARB-03 closure proposal relative to them.

ARB is not a normative owner for any neighboring record or result.

A mapping below:

- identifies an exact, partial, or absent relation;
- permits only the stated bounded use;
- does not transfer normative ownership;
- does not import a neighboring conclusion;
- does not prove that two records describe the same event;
- does not select a normative home for ARB-03.

```text
analytical similarity
  != exact equivalence
  != imported requirement
  != imported verdict
```

`No equivalence` means one valid conclusion cannot substitute for the other. `Partial mapping` means records may refer to nearby responsibilities or the same addressable event while retaining different owners, semantics, validators, and result domains.

No cross-artifact pair in this document reaches exact equivalence.

## 2. Fixed source revisions

| Owner | Pinned public revision |
|---|---|
| BEC | [`62f2b7940b5ca7a4a8b24150b9c45a6ab5d97261`](https://github.com/gv1983us-commits/behavioral-execution-contract/tree/62f2b7940b5ca7a4a8b24150b9c45a6ab5d97261) |
| MPAA | [`0d1aaf35cc4826622f3312fdd2a1c2d40890b965`](https://github.com/gv1983us-commits/mpaa/tree/0d1aaf35cc4826622f3312fdd2a1c2d40890b965) |
| PCA | [`a669f023198615ad929f42df84f19380b57ca5ea`](https://github.com/gv1983us-commits/pca/tree/a669f023198615ad929f42df84f19380b57ca5ea) |
| Review Protocol | [`b4205ffd91a6316ab40243cbf8161a1c512cae1f`](https://github.com/gv1983us-commits/repository-canon-review-protocol/tree/b4205ffd91a6316ab40243cbf8161a1c512cae1f) |
| CDTS | [`f91dbc003519efd5264655d905d0530dbfeac2fd`](https://github.com/gv1983us-commits/cdts/tree/f91dbc003519efd5264655d905d0530dbfeac2fd) |

Exact inspected files and the transition from the 0.2 source set are recorded in [`../references/RELATED_PUBLIC_SPECS.md`](../references/RELATED_PUBLIC_SPECS.md).

## 3. Universal ARB distinctions

The following are analytical non-equivalence rules, not a shared state machine:

```text
model output != verified reasoning
reasoning about an action != execution
capability available != authorized
analysis or plan != invocation
visible status != execution evidence
invocation != verified result
result produced != result delivered
delivered != persisted
persisted != retrievable
retrievable != admitted into working state
working state present != committed
committed != PCA process continuation
process continuation != identity-profile continuity
identity-profile continuity != personal identity
```

Every arrow omitted from this chain requires its own owner, evidence, and evaluation. ARB does not fill missing evidence by interpretation.

## 4. ARB ↔ BEC

BEC owns task-scoped execution-evidence acceptance: capability, authorization, invocation, evidence, trust anchors, validation, deployment level, and return state.

ARB owns only analytical distinctions among possible failure locations.

| Pair | Relation | Permitted use | Forbidden inference | Required evidence for a stronger claim |
|---|---|---|---|---|
| plan ↔ invocation | No equivalence | A plan may identify a capability that should be used. | Describing the action proves invocation. | Addressable invocation record or equivalent BEC evidence. |
| visible status ↔ execution evidence | No equivalence | A visible status proves that the interface displayed a label. | The label proves capability invocation or `FULL-for-task`. | Event ID, capability ID, timestamp, result or receipt reference, and applicable trust anchor. |
| runtime receipt ↔ BEC evidence | Partial mapping | One addressable receipt may support a BEC record. | Presence of a receipt automatically satisfies freshness, verification, or policy. | Owner-specific BEC validation and support mapping. |
| BEC `return_state: closed` ↔ next-state commitment | No equivalence | `closed` says the BEC claim tree needs no more BEC-validator work. | `closed` means delivered, persisted, retrievable, admitted, committed, or continued. | A separately owned commitment record; a separate PCA Transition Record if continuation is claimed. |
| deployment level ↔ ARB analytical classification | No equivalence | ARB may explain why BEC keeps claim inputs separate. | ARB recomputes or renames `RELAY`, `PARTIAL`, `FULL-for-task`, or `REFUSAL`. | A valid BEC record under the BEC owner. |

```text
ARB explanation != BEC requirement
ARB question != BEC evidence
ARB publication check != BEC validation
```

## 5. ARB ↔ MPAA

MPAA owns its six-document architecture, Identity Profile, Runtime Contract, authorization semantics, Runtime Report, validator meaning, and conformance procedure.

ARB uses nearby functional terms without amending MPAA.

| Pair | Relation | Permitted use | Forbidden inference | Required evidence for a stronger claim |
|---|---|---|---|---|
| ARB model ↔ MPAA Model | Partial mapping | ARB may explain why a model is not automatically the whole agent. | ARB's term replaces MPAA's normative term or proves a physical component boundary. | Exact MPAA field or record plus implementation evidence when physical topology is claimed. |
| ARB runtime / host ↔ MPAA Runtime | Partial mapping | A concrete MPAA Runtime may instantiate responsibilities ARB describes. | ARB topology is the mandatory MPAA call graph. | Fixed MPAA revision and current Runtime Report or implementation trace. |
| ARB platform / control plane ↔ MPAA Platform and Runtime surfaces | Partial mapping | ARB may analyze configuration, permission, telemetry, and result projection. | One visible UI is the entire MPAA Platform or authority system. | Field-level mapping, current authority record, and observable event traces. |
| capability ↔ availability ↔ authorization ↔ invocation | Partial mapping with separate claims | ARB may show why each can fail independently. | One term implies the next. | MPAA-owned current observations and records for each claimed step. |
| identity-profile continuity ↔ process continuity | No equivalence | ARB may explain that the two questions have different owners. | Same profile identifier, style, or history proves continuation or personal identity. | Owner-specific MPAA and PCA records, each validated separately. |
| ARB-03 closure record ↔ MPAA Runtime state | Proposal-only mapping | MPAA is a possible future home for some operational state concepts. | ARB-03 changes the Runtime Contract or grants authorization. | A future maintainer-approved MPAA change with schema, validator, and conformance impact. |

A functional reconstruction can remain useful even when one physical service implements several responsibilities or several services implement one responsibility.

```text
functional boundary != physical module proof
ARB topology != MPAA normative architecture
```

## 6. ARB ↔ PCA

PCA owns bounded process-continuity assessment across one explicit transition, including dimensions, evidence admissibility, status derivation, and assertion prohibitions.

ARB distinguishes operational events that may precede or surround a PCA assessment.

| Pair | Relation | Permitted use | Forbidden inference | Required evidence for a stronger claim |
|---|---|---|---|---|
| persisted artifact ↔ PCA `CORPUS` evidence | Partial mapping | A durable artifact may be referenced in a PCA evidence chain. | Existence proves retrieval, use, continuation, or memory. | Artifact identity, version or digest, retrieval/use evidence, and PCA-local support mapping. |
| working state ↔ PCA `STATE` | Partial mapping | A declared task-local state may be represented in a bounded transition record. | ARB working state is the complete PCA state or proves status. | Explicit from/to states, transition identity, evidence, and PCA validation. |
| committed ↔ process continuation | No equivalence | A commit event may become evidence for a later PCA assessment. | A committed next state automatically means PCA `CONFORMING`. | Commitment evidence plus a separate valid PCA Transition Record. |
| execution success ↔ process continuation | No equivalence | Execution evidence may support an operational dimension. | Successful tool use or BEC `FULL-for-task` proves continuation. | Addressable execution evidence and independent PCA evaluation. |
| same name, style, or profile ↔ identity / continuation | No equivalence | These may be observations carried with explicit limits. | Resemblance proves identity, memory, or continuation. | PCA-required evidence; identity remains outside PCA's claim. |

```text
stored != retrieved
retrieved != active working state
committed != PCA process continuation
PCA status != identity or memory
```

ARB cannot issue `CONFORMING`, `EVOLVING`, `FORK`, `INCOMPATIBLE`, or `UNDETERMINED` as an ARB result.

## 7. ARB ↔ Review Protocol

The Review Protocol owns exact-source selection, discrepancy discipline, bounded review receipts, and reproducible handoff.

ARB consumes that discipline when updating analytical mappings.

| Pair | Relation | Permitted use | Forbidden inference | Required evidence for a stronger claim |
|---|---|---|---|---|
| fixed source receipt ↔ ARB mapping | Procedural support | ARB may identify exact source revisions and inspected surfaces. | Source pin proves the ARB interpretation true. | The named source plus transparent analytical reasoning and disclosed limits. |
| review check executed ↔ analytical conclusion | No equivalence | A receipt may record that files and checks were inspected. | Check execution proves hidden runtime structure or universal correctness. | External evidence owned by the domain of the stronger claim. |
| discrepancy recorded ↔ discrepancy resolved | No equivalence | ARB should preserve a material source difference before updating. | Recording the difference determines which interpretation is correct. | A separate resolution with owning-source evidence. |
| donor receipt ↔ ARB runtime analysis | No equivalence | A donor receipt may be cited as a bounded external record. | Valid receipt proves runtime safety, privacy, completeness, execution, or ARB theory. | Owner-specific evidence and evaluation for each stronger claim. |

```text
source pinned != source claim true
review receipt valid != ARB interpretation true
publication checks pass != hidden internals observed
```

## 8. ARB ↔ CDTS

CDTS owns cross-domain correlation traces, qualified external references, typed absence, conflict disclosure, unresolved questions, linkage assertions, and amendment history.

ARB may be carried only as analytical context or an addressable source.

| Pair | Relation | Permitted use | Forbidden inference | Required evidence for a stronger claim |
|---|---|---|---|---|
| ARB revision ↔ CDTS external reference | Partial mapping | A trace may cite a fixed ARB revision as explanatory context. | ARB becomes the normative owner of the trace or referenced event. | CDTS-valid external reference and correct owning domain for every record. |
| ARB distinction ↔ unresolved question | Analytical support | A distinction may help state what remains unresolved. | The distinction resolves the question or validates a linkage. | Evidence and local CDTS evaluation appropriate to the assertion. |
| ARB interpretation ↔ CDTS linkage assertion | No equivalence | Both may be displayed for review. | ARB interpretation proves same event, causality, completeness, or admissibility. | CDTS-required source pins, keys, assertions, conflict handling, and validation. |
| CDTS `ADMISSIBLE` ↔ ARB truth | No equivalence | `ADMISSIBLE` applies to the CDTS record boundary. | It certifies the referenced ARB interpretation. | Separate support for the analytical claim. |

The reviewed CDTS corpus contains an explicit invalid fixture for treating ARB as a normative owner. ARB reciprocally preserves:

```text
normative_surface_count = 0
ARB is not a normative owner
```

## 9. ARB-03 closure proposal

ARB-03 is an operational proposal. It distinguishes:

```text
BEC closed
result delivered
artifact persisted
artifact retrievable
material admitted into working state
next state committed
PCA process continuation
```

The illustrative closure record may preserve:

- result or explicit unresolved status;
- provenance and receipt references;
- open obligations;
- state changes;
- accepted constraints;
- next authority reference;
- retained candidate status.

It does not establish any referenced event merely by naming a field.

### Candidate ownership remains unresolved

| Proposed item | Current ARB status | Possible owner, not selected | Forbidden inference |
|---|---|---|---|
| `delivered` | observable event class | runtime/reporting or delivery evidence surface | delivered means accepted or committed |
| `persisted` | analytical distinction | runtime/storage or artifact contract | persisted means retrievable |
| `retrievable` | analytical distinction | runtime capability/reporting; BEC for one retrieval task | retrievable means admitted into working state |
| working-state admission | analytical distinction | runtime/state contract | retrieved text is automatically authoritative |
| `committed` | ARB-03 proposal | runtime/state transition contract; PCA only assesses later continuation | BEC closed or persistence proves commit |
| `next_authority_ref` | ARB-03 proposal | authority/runtime reporting surface | reference itself grants permission |
| open obligations | proposal with partial BEC relation | BEC for task-local work; runtime/state for cross-step restoration | listing work authorizes action or proves commitment |

```text
proposal published != proposal adopted
proposal adopted elsewhere != ARB becomes normative
field present != event occurred
```

## 10. Rejected composite inferences

The following chains are invalid without separately owned evidence and evaluation:

```text
capability available -> authorized -> invoked
invoked -> verified result
verified result -> BEC FULL-for-task
BEC closed -> delivered
closed or delivered -> persisted
persisted -> retrievable
retrievable -> admitted into working state
working state present -> committed
committed -> PCA process continuation
PCA process continuation -> identity-profile continuity
identity-profile continuity -> personal identity
```

Missing evidence remains missing. ARB does not supply it by explanation.

## 11. Status of ARB-03

Established analytically:

- neighboring artifacts have distinct claim domains and owners;
- BEC `closed` does not prove next-state commitment;
- MPAA separates architecture, capability, authority, invocation, evidence, result, and profile continuity surfaces;
- PCA continuation is not execution success, profile match, identity, or memory;
- the Review Protocol's source receipt does not prove an inspected claim true;
- CDTS correlation does not import conclusions or turn ARB into a normative owner.

Proposed:

- a minimal closure record;
- explicit separation of delivery, persistence, retrieval, working-state admission, commitment, and continuation.

Unresolved:

- which normative owner, if any, should define cross-step state commitment;
- whether one owner can cover local runtime restoration and cross-host continuation;
- what record contract, evidence strength, migration, implementation, and conformance suite would be required.

ARB-03 remains a proposal until an owning specification explicitly adopts a rule and supplies its own validation and conformance boundary.

## 12. Mapping formula

> **Import the source, preserve the vocabulary, explain the distinction, and leave the conclusion with its owner.**
