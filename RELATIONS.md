# Agent Runtime Boundaries — Relations

**Artifact:** Agent Runtime Boundaries (ARB)  
**Corpus identity:** `claude.arb`  
**Local claim domain:** non-normative functional and analytical boundary mapping

This document records ARB-side relations to the other five technical artifacts represented through the House of Claude.

ARB does not merge their specifications, import their conclusions, or become a normative owner merely because it explains a distinction among them.

## 1. Governing relation rule

```text
explain the functional distinction
pin the owning source
preserve the neighboring vocabulary
import neither authority nor conclusion
```

An ARB statement may improve diagnosis or review. It cannot award a neighboring result.

## 2. BEC — execution evidence, not analytical narrative

**Artifact:** `claude.bec`  
**Repository:** `gv1983us-commits/behavioral-execution-contract`  
**Reviewed canonical revision:** `62f2b7940b5ca7a4a8b24150b9c45a6ab5d97261`

BEC owns task-scoped capability, authorization, invocation, evidence, trust anchors, validation, deployment level, and return state.

ARB explains why planning an action, displaying progress, delivering text, or closing a narrative does not establish execution evidence.

Allowed relation:

- ARB may distinguish the failure locations that a BEC record should keep separate;
- a BEC record may be cited as an example of addressable execution evidence;
- ARB may explain why `return_state: closed` does not prove delivery, persistence, retrieval, next-state commitment, or process continuation.

Forbidden inference:

```text
ARB explanation      -> BEC requirement
plausible action text -> BEC invocation evidence
visible status        -> BEC FULL-for-task
BEC closed            -> committed next state
```

ARB cannot compute or rename a BEC verdict.

## 3. MPAA — architecture owner, not proof of physical modules

**Artifact:** `claude.mpaa`  
**Repository:** `gv1983us-commits/mpaa`  
**Reviewed canonical revision:** `0d1aaf35cc4826622f3312fdd2a1c2d40890b965`

MPAA owns its six-document architecture, Identity Profile, Runtime Contract, authorization, Runtime Report, validator meaning, and conformance procedure.

ARB uses nearby terms such as model, agent, runtime, platform, control plane, capability, authority, evidence, and task result. These are analytical mappings, not MPAA amendments.

Allowed relation:

- ARB may explain why model identity alone does not establish runtime capability, authorization, state, evidence, or the complete agent;
- ARB may map control-plane and runtime responsibilities to MPAA surfaces at an exact revision;
- MPAA records may provide addressable examples for ARB analysis.

Forbidden inference:

```text
ARB topology          -> MPAA physical implementation
ARB term              -> MPAA normative definition
MPAA runtime ready    -> ARB proposal adopted
ARB closure record    -> MPAA authorization or conformance
```

A functional split can be useful even when one physical component implements several responsibilities.

## 4. PCA — transition assessment, not continuity by resemblance

**Artifact:** `claude.pca`  
**Repository:** `gv1983us-commits/pca`  
**Reviewed canonical revision:** `a669f023198615ad929f42df84f19380b57ca5ea`

PCA owns bounded process-continuity assessment across one explicit transition, including dimensions, evidence admissibility, status derivation, and assertion prohibitions.

ARB distinguishes storage, retrieval, working-state admission, commitment, and continuation. It does not define PCA evidence or status.

Allowed relation:

- ARB may explain why stored or retrieved material is not automatically active working state;
- ARB may distinguish a runtime commit event from a later PCA assessment of continuation;
- an exact PCA record may be cited as an external example without importing its conclusion.

Forbidden inference:

```text
same style or name   -> PCA continuation
artifact persisted   -> PCA continuation
working state exists -> PCA CONFORMING
ARB committed        -> PCA status
PCA status           -> identity or memory
```

The ARB-03 closure proposal remains outside PCA unless PCA itself adopts a compatible rule.

## 5. Review Protocol — exact-source discipline, not analytical ownership

**Artifact:** `claude.review_protocol`  
**Repository:** `gv1983us-commits/repository-canon-review-protocol`  
**Reviewed canonical revision:** `b4205ffd91a6316ab40243cbf8161a1c512cae1f`

The Review Protocol owns source selection, exact inspected revisions, discrepancy discipline, bounded review receipts, and reproducible handoff.

ARB uses that discipline to pin neighboring sources and record mapping limits. A source receipt does not make the ARB interpretation true or normative.

Allowed relation:

- ARB reviews may cite exact source revisions and named inspected surfaces;
- discrepancies between moving branches and fixed mappings should be recorded before update;
- a review receipt may record that ARB publication checks were run.

Forbidden inference:

```text
source pinned        -> ARB interpretation true
review receipt valid -> ARB normative
checks passed        -> hidden runtime structure established
ARB recommendation   -> neighboring repository changed
```

ARB retains analytical responsibility for its interpretation; the Review Protocol retains ownership of review procedure.

## 6. CDTS — correlation, not normative ownership

**Artifact:** `claude.cdts`  
**Repository:** `gv1983us-commits/cdts`  
**Reviewed revision:** `f91dbc003519efd5264655d905d0530dbfeac2fd`

CDTS owns cross-domain correlation traces, qualified external references, typed absence, conflict disclosure, unresolved questions, linkage assertions, and amendment history.

ARB may appear in a CDTS trace only as an analytical context or addressable source. It must not be declared the normative owner of a BEC, MPAA, PCA, Review Protocol, or CDTS result.

Allowed relation:

- a trace may cite an exact ARB revision as explanatory context;
- ARB distinctions may help phrase an unresolved question or disclosed conflict;
- CDTS may correlate the records whose boundaries ARB explains.

Forbidden inference:

```text
ARB cited in CDTS       -> ARB owns the event
ARB analytical mapping  -> CDTS linkage assertion valid
CDTS ADMISSIBLE         -> ARB interpretation true
shared term or timestamp -> same event or causality
```

CDTS itself includes resistance against treating ARB as a normative owner. ARB therefore preserves `normative_surface_count = 0` at the artifact boundary.

## 7. ARB-03 proposal relation

ARB-03 proposes a minimal closure record and distinctions among:

```text
closed
delivered
persisted
retrievable
working-state admission
committed
process continuation
```

No neighboring artifact automatically adopts that chain.

```text
proposal published
  != proposal adopted
  != normative owner selected
  != implementation exists
  != conformance established
```

A future adoption must occur in the owning repository and identify the record contract, evidence, validator, migration, and conformance boundary.

## 8. Corpus relation

```text
BEC             owns execution-evidence acceptance
MPAA            owns portable agent architecture and runtime reporting
PCA             owns bounded process-continuity assessment
Review Protocol owns source-selection and review procedure
ARB             owns non-normative analytical distinctions
CDTS            owns cross-domain correlation traces
```

The six artifacts can be used together without forming one mandatory pipeline or universal verdict system.

## 9. Fixed revisions and future movement

The revisions above are the sources reviewed for this relation surface on `2026-08-06`.

They are reproducible reading receipts, not permanent locks on future development. A future relation update must inspect the new neighboring revision and record whether the claim domain, vocabulary, evidence boundary, or forbidden inferences changed.

Replacing a SHA without review is not a semantic update.

## 10. Relation formula

> **ARB can clarify another authority only by refusing to impersonate it.**
