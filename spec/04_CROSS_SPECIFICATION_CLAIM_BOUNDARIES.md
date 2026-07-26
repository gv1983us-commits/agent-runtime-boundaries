# Cross-Specification Claim Boundary and Mapping

**Document:** ARB-04
**Status:** PUBLIC DRAFT
**Mode:** DESCRIPTIVE / ANALYTICAL
**Version:** 0.2

## Purpose and authority boundary

This document is an **analytical companion**. It compares claim surfaces owned by MPAA, BEC, and PCA and locates the ARB-03 closure proposal relative to them.

A row in these tables:

- records an exact, partial, or absent relationship;
- permits only the stated bounded inference;
- does not transfer normative ownership;
- does not make ARB canonical for a neighboring specification;
- does not select a normative home for ARB-03.

`No equivalence` means that one valid conclusion cannot substitute for the other. `Partial mapping` means that records may refer to the same event or responsibility but retain different owners, semantics, validation, and result domains. `Exact equivalence` would require the owning specifications to define the same claim; no cross-specification pair below reaches that threshold.

## Fixed source revisions

| Owner | Pinned public revision |
|---|---|
| MPAA | [`1d369f6cd091b99f9492cfaf730f0a170b55106e`](https://github.com/gv1983us-commits/mpaa/tree/1d369f6cd091b99f9492cfaf730f0a170b55106e) |
| BEC | [`bb46f5f8aac96d1cffba7a334c5d17fb331ef3af`](https://github.com/gv1983us-commits/behavioral-execution-contract/tree/bb46f5f8aac96d1cffba7a334c5d17fb331ef3af) |
| PCA | [`6ad1a86d7c09b36839d162c580f84f05cfe4a598`](https://github.com/gv1983us-commits/pca/tree/6ad1a86d7c09b36839d162c580f84f05cfe4a598) |
| Review Protocol | [`595c08b877e4dfb14593454c2eec7c8f5df46c28`](https://github.com/gv1983us-commits/repository-canon-review-protocol/tree/595c08b877e4dfb14593454c2eec7c8f5df46c28) |

### Inspected owning surfaces

| Owner | Exact files used for this mapping |
|---|---|
| MPAA | [`spec/00_SESSION_BOOTSTRAP.md`](https://github.com/gv1983us-commits/mpaa/blob/1d369f6cd091b99f9492cfaf730f0a170b55106e/spec/00_SESSION_BOOTSTRAP.md); [`spec/02_IDENTITY_PROFILE_SPEC.md`](https://github.com/gv1983us-commits/mpaa/blob/1d369f6cd091b99f9492cfaf730f0a170b55106e/spec/02_IDENTITY_PROFILE_SPEC.md); [`spec/03_RUNTIME_CONTRACT.md`](https://github.com/gv1983us-commits/mpaa/blob/1d369f6cd091b99f9492cfaf730f0a170b55106e/spec/03_RUNTIME_CONTRACT.md); [`spec/05_RUNTIME_REPORT_SCHEMA.md`](https://github.com/gv1983us-commits/mpaa/blob/1d369f6cd091b99f9492cfaf730f0a170b55106e/spec/05_RUNTIME_REPORT_SCHEMA.md) |
| BEC | [`spec/01_BEC_COMPACT_CORE.md`](https://github.com/gv1983us-commits/behavioral-execution-contract/blob/bb46f5f8aac96d1cffba7a334c5d17fb331ef3af/spec/01_BEC_COMPACT_CORE.md); [`conformance/README.md`](https://github.com/gv1983us-commits/behavioral-execution-contract/blob/bb46f5f8aac96d1cffba7a334c5d17fb331ef3af/conformance/README.md) |
| PCA | [`spec/01_PCA_CORE.md`](https://github.com/gv1983us-commits/pca/blob/6ad1a86d7c09b36839d162c580f84f05cfe4a598/spec/01_PCA_CORE.md) |
| Review Protocol | [`repository-canon-and-review-protocol-v0.1.md`](https://github.com/gv1983us-commits/repository-canon-review-protocol/blob/595c08b877e4dfb14593454c2eec7c8f5df46c28/repository-canon-and-review-protocol-v0.1.md) |

The Review Protocol owns source-selection and fixed-revision discipline. It does not own any runtime, execution, identity, or continuation conclusion below.

## 1. MPAA ↔ BEC

MPAA owns its internal architecture, Runtime Contract, authorization semantics, and Runtime Report. BEC owns its portable consumer-facing execution-evidence contract and task-scoped deployment-level derivation.

| Term or pair | Canonical owner | Relation | Permitted inference | Forbidden inference | Required cross-reference evidence | Normative direction and pin |
|---|---|---|---|---|---|---|
| capability | MPAA for current-runtime capability; BEC for task-required/effective capability | Partial mapping | Two records may refer to the same operation and current task scope. | MPAA availability alone proves BEC effective capability or `FULL-for-task`. | Same capability identifier or explicit mapping, task identifier, current observation, availability, authorization, invocation, and evidence references. | ARB → MPAA Runtime Contract and BEC Compact Core at the pinned revisions above. |
| authorization | MPAA for runtime authority evaluation; BEC for task-scoped `authorized` input | Partial mapping | A BEC record may carry a current authorization result produced by the applicable runtime authority. | Identity data, capability existence, UI permission, or BEC producer assertion creates MPAA authorization. | Authority record reference, scope, actor, task/action, decision, freshness, and evidence sufficient for each owner. | BEC may reference an MPAA authority result; MPAA does not inherit a BEC deployment level. |
| invocation | MPAA for current runtime execution observation; BEC for evidence that a required capability was used | Partial mapping | The same addressable invocation event may support both reports. | `runtime_mode`, capability availability, authorization, or model text proves invocation. | Invocation/event ID, capability ID, time, input/output or receipt reference, and bidirectional evidence attribution. | Each owner validates its own record; ARB only maps the event. |
| evidence | MPAA for Runtime Report evidence objects; BEC for portable task evidence and trust anchors | Partial mapping | One artifact or receipt may be cited by both systems when identifiers, scope, and verification are explicit. | Presence in one record automatically satisfies the other's evidence strength, freshness, schema, or policy. | Stable evidence ID, source or trust anchor, observed time, support target, verification method, and owner-specific validation. | Evidence may be cross-referenced, never silently copied as an accepted conclusion. |
| verification | MPAA for runtime verification status; BEC for evidence/trust-anchor validation and deployment computation | Partial mapping | A verification event may be reused as evidence if its method, target, time, and confidence are preserved. | MPAA `PASSED` automatically means BEC `FULL-for-task`, or BEC validation proves MPAA conformance. | Verification ID, target, method, verifier/trust anchor, timestamp, result, and freshness. | Consumer imports the trace, then evaluates it under the receiving owner. |
| result | MPAA for `task_result` in its Runtime Report; BEC for task-scoped deployment level and return state | No equivalence | Results may be displayed side by side for one task. | Any MPAA result value is renamed as `RELAY`, `PARTIAL`, `FULL-for-task`, or `REFUSAL`, or vice versa. | Same task/sub-task identity plus both independently validated records. | No result transfer; cite both owning specifications. |

The sequence `capability → authorization → invocation → evidence → verification → result` is an analytical comparison, not a shared cross-specification state machine.

## 2. MPAA ↔ PCA

MPAA identity-profile continuity and PCA process continuation have different subjects, inputs, and result types.

| Term or pair | Canonical owner | Relation | Permitted inference | Forbidden inference | Required cross-reference evidence | Normative direction and pin |
|---|---|---|---|---|---|---|
| identity-profile continuity ↔ process continuation | MPAA Identity Profile Specification; PCA Core | No equivalence | A PCA transition record may cite a pinned MPAA profile revision as one trace among others. | Profile identifier/history match proves PCA continuation; PCA `CONFORMING` proves personal or profile identity. | Exact profile revision/history plus a separate valid PCA Transition Record with its own evidence and dimensions. | PCA may carry MPAA data with `carried-not-imported`; neither conclusion owns the other. |
| runtime ↔ host | MPAA Runtime Contract; PCA Core | Partial mapping | A concrete MPAA runtime can be named as a PCA `HOST` for one transition. | MPAA runtime readiness, alignment, or classification proves continuation. | Runtime identifier/revision, current observation time, PCA from/to states, and transition receipt. | PCA references the runtime; MPAA does not issue PCA status. |
| runtime state ↔ PCA `STATE` | MPAA Runtime Contract/Report; PCA Core | Partial mapping | Selected runtime facts may populate a bounded PCA state reference. | An MPAA report is the complete PCA state or a PCA record is an MPAA Runtime Report. | Field-level mapping, omitted/unknown declaration, revisions, timestamps, and owner-specific validation. | Mapping is directional and partial. |
| profile history ↔ provenance | MPAA Identity Profile Specification; PCA Core | Partial mapping | Profile history may support a provenance statement about an inspected transition. | Stored profile history establishes current runtime truth or all seven PCA dimensions. | Profile identifiers, explicit history entries, transition relation, and independently verified support links. | PCA owns the provenance assessment; MPAA owns profile history rules. |
| session readiness ↔ continuation | MPAA Session Bootstrap/Runtime surfaces; PCA Core | No equivalence | Readiness may be evidence that a host can begin work. | Initialized or aligned session proves that a process continued into it. | MPAA readiness trace plus a separate PCA transition receipt and admissible claim. | No conclusion transfer. |

Neither identical style nor identical interaction conventions establish either result.

## 3. BEC ↔ PCA

BEC evaluates execution claims for a bounded task. PCA evaluates a process-continuation claim across a bounded transition.

| Term or pair | Canonical owner | Relation | Permitted inference | Forbidden inference | Required cross-reference evidence | Normative direction and pin |
|---|---|---|---|---|---|---|
| verified execution ↔ process continuation | BEC; PCA | No equivalence | Verified execution may support one PCA operational-dimension statement when explicitly cited. | `FULL-for-task`, a receipt, or successful tool use proves overall continuation. | Valid BEC record, pinned revision/reference, PCA evidence object, support target, and independent PCA evaluation. | PCA carries the BEC record as evidence; it does not import deployment level as PCA status. |
| `closed` ↔ `committed` | BEC for `return_state: closed`; no selected owner for cross-step commitment | No equivalence | `closed` says the BEC task claim tree needs no more BEC-validator work; a separate commitment trace may be referenced. | `closed` means a next working state was persisted, admitted, retrievable, or committed. | BEC record plus separately named external reference and an owner-specific commitment/transition receipt. | BEC explicitly points outward; ARB and PCA must not reinterpret `closed`. |
| BEC evidence ↔ PCA evidence | Each specification for its own evidence object | Partial mapping | One receipt can be referenced in both records with explicit support scope. | BEC trust level automatically verifies a PCA dimension or PCA `verified: true` awards BEC deployment level. | Stable evidence identity, source/trust anchor, timestamps, verification method, and bidirectional local links. | Import the trace, not the conclusion. |
| BEC `external_reference` ↔ PCA external reference | Each specification for its transport boundary | Partial mapping | A BEC record may point to a PCA record, and PCA may carry a pinned BEC record. | An external reference proves that the external evaluation occurred or passed. | Non-empty owner/system ID, record ID, pinned revision where required, and explicit boundary. | Direction is always from referencing record to owning external record. |
| archived BEC pointer ↔ PCA `CORPUS` | BEC lifecycle; PCA | Partial mapping | An archived BEC record may become an inspectable artifact in a PCA corpus projection. | Archival means retrieval, active working state, memory, or continuation. | Durable artifact reference, version/hash, retrieval observation when claimed, and PCA support mapping. | BEC owns archival state; PCA owns corpus use in its claim. |
| deployment level ↔ continuity status | BEC; PCA | No equivalence | Both may be reported for one event if clearly labeled. | `FULL-for-task` is renamed `CONFORMING`, or a PCA status is treated as BEC task acceptance. | Two separately validated records bound to the same task/transition references. | No result transfer. |

PCA `CORPUS` means inspectable artifacts relevant to process history. ARB `PERSISTENT CORPUS` means addressable artifacts that may support later reconstruction or review. This is a partial descriptive mapping, not exact equivalence: PCA owns the transition-assessment term; ARB does not define storage conformance, retrieval, admission into working state, or memory.

## 4. ARB-03 closure proposal ↔ normative domains

ARB-03 is an operational proposal. The table identifies possible homes for future rules but does not select a normative home. Until an owning specification adopts a field and its conformance rules, the field remains analytical/proposed.

| ARB term or claim | Current owner | Relation to MPAA / BEC / PCA | Permitted inference | Forbidden inference | Required evidence | Possible normative home, not selected |
|---|---|---|---|---|---|---|
| `delivered` | No ARB normative owner; observable projection event | BEC may report a result; MPAA may report runtime output; PCA does not own delivery | A referenced interface/runtime emitted or displayed a result at a stated time. | Delivery means acceptance, persistence, retrieval, commitment, or continuation. | Delivery event/receipt, result reference, channel/interface, timestamp, and transformation status where known. | Runtime/reporting surface or a task execution contract. |
| `persisted` | No ARB normative owner | MPAA may observe persistence mechanisms; BEC may archive record pointers; PCA may reference a carrier/corpus | An identified artifact was durably written under a stated retention boundary. | Persistence means future retrieval, admission to working state, memory, or correctness. | Artifact ID, storage/carrier, version/hash, write receipt, timestamp, retention/availability boundary. | Runtime Contract/report schema or a dedicated storage/artifact contract. |
| `retrievable` | No ARB normative owner | Closest to current MPAA capability/availability; BEC can evidence a retrieval task; PCA corpus existence is insufficient | A current scoped retrieval attempt can resolve the identified artifact. | Previously persisted or publicly visible means currently retrievable by the next runtime. | Current capability, authorization where needed, invocation receipt, resolved artifact/version, freshness. | Runtime capability/reporting surface; BEC for the bounded retrieval task. |
| working state | ARB descriptive term | MPAA owns current operational/runtime semantics; BEC intentionally excludes memory systems; PCA assesses referenced states | Declared task-local constraints, obligations, evidence, and environment references are available for the next action. | Retrieved text or a prior response automatically becomes authoritative working state. | State identifier/version, admission or restoration receipt, selected source revisions, open obligations, applicable authority reference. | MPAA Runtime Contract/report or a future separately adopted state contract. |
| `committed` | ARB-03 proposal only | BEC explicitly does not own next-state commitment; PCA may assess a transition after evidence; MPAA is the closest operational domain | A named next state was durably accepted under an identified authority and can be restored for a next action. | BEC `closed`, result delivery, persistence alone, or a PCA citation proves commitment. | Commit/admission receipt, state ID/version, authority record, provenance, persistence and retrieval evidence, timestamp. | MPAA runtime/state surface or a dedicated state-transition contract; PCA could own only a separate assessment after commitment evidence, not the commit operation; unresolved. |
| `next_authority_ref` | ARB-03 proposal only | May reference applicable MPAA authority/profile/runtime records; is outside BEC core; does not create PCA authority | A named external authority record should be consulted for the next action. | The free-form reference grants permission, overrides policy, or proves current authorization. | Resolvable owner, record ID/version, scope, freshness, and current authority evaluation. | MPAA authority/runtime reporting surface is a candidate; not selected here. |
| open obligations | ARB-03 proposal; BEC owns task-open/blocked semantics within BEC | Partial mapping to BEC remaining work and MPAA task state; PCA may carry changed/unknown statements | Listed work remains unresolved and should not be silently treated as complete. | Listing an obligation authorizes action or proves it was committed into the next state. | Obligation ID, source task/result, status, owner/next action, evidence and state-commit reference where claimed. | BEC for task-local obligations; runtime/state domain for cross-step restoration. |
| ARB `PERSISTENT CORPUS` | ARB descriptive term only | Partial mapping to PCA `CORPUS`; may be implemented by MPAA runtime resources | Addressable artifacts exist and may support reconstruction or review. | Existence proves selection, retrieval, admission, use, memory, truth, or continuity. | Artifact identifiers, versions/hashes, storage observations; separate retrieval/use evidence for stronger claims. | PCA owns its own corpus role; storage/runtime ownership remains implementation-specific. |
| retained candidates | ARB-03 proposal only | Outside BEC execution core; may appear as PCA `unknown`/`reconstructed` statements only through PCA rules | A hypothesis remains available with its uncertainty preserved. | Repetition, prior presence, or persistence promotes it to accepted constraint or fact. | Candidate ID, status, evidence references, acceptance authority when changed, and revision trace. | A future working-state contract or owner-specific extension; unresolved. |

## Rejected composite inferences

The following chains remain invalid even if every term appears in one narrative:

```text
capability available -> authorized -> invoked
invoked -> verified result
verified result -> BEC FULL-for-task
BEC closed -> delivered
closed or delivered -> persisted
persisted -> retrievable
retrieved -> admitted into working state
working state present -> committed
committed -> PCA continuation
PCA continuation -> identity-profile continuity
```

Each arrow requires the evidence and owning evaluation named above. Missing evidence remains missing; ARB does not fill it by interpretation.

## Status of ARB-03

Established:

- the three neighboring specifications have distinct normative domains;
- BEC explicitly rejects `closed` as proof of next-state commitment;
- PCA explicitly rejects verified execution and identity-profile match as proof of process continuation;
- MPAA separates capability existence, availability, authorization, invocation, evidence, verification, runtime result, and identity continuity.

Proposed:

- a minimal closure record preserving result, provenance, receipts, obligations, state changes, accepted constraints, applicable authority reference, and retained candidate status;
- explicit distinction among `delivered`, `persisted`, `retrievable`, working state, and `committed`.

Unresolved:

- which normative owner, if any, should define cross-step state commitment;
- whether one owner can cover both local runtime restoration and cross-host continuation;
- what evidence strength and conformance suite would be required.

ARB-03 remains a proposal until an owning specification explicitly adopts a rule and supplies its own validation/conformance boundary.
