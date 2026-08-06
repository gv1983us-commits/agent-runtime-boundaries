# Scope and Status

**Document:** ARB-00  
**Status:** PUBLIC DRAFT  
**Mode:** DESCRIPTIVE / ANALYTICAL  
**Version:** 0.3

## 1. Scope

This document set describes functional boundaries in model-based agent systems. Its purpose is to make observable responsibilities and failure locations easier to distinguish without claiming access to hidden implementation details.

The scope includes:

- separation of human, agent, model, runtime, and platform roles;
- separation of working state, persistent artifacts, resources, and execution;
- user-side control, authorization surfaces, and observability;
- delivery, persistence, retrieval, state admission, commitment, and continuation distinctions;
- provenance, receipts, open obligations, and next-action questions;
- limits on what a visible answer, status, stored artifact, or repeated explanation can establish;
- fixed-revision analytical mappings to neighboring public artifacts.

## 2. Out of scope

This document set does not define:

- consciousness, subjectivity, or personhood;
- a universal physical architecture for language models or agent systems;
- a specific identity or Identity Profile;
- a specific product, provider, model, or deployment;
- legal or organizational authority;
- a replacement for BEC, MPAA, PCA, the Review Protocol, or CDTS;
- a normative execution, architecture, continuity, review, or correlation verdict;
- a cross-step commitment, storage, retrieval, memory, or continuation protocol;
- conformance to any external specification;
- hidden reasoning or hidden runtime internals.

## 3. Canonical status and normative force

ARB is a `canonical_public_draft` as an analytical artifact.

```text
canonical analytical artifact
  != normative specification
```

ARB has zero normative specification surfaces. Canonicalization establishes the integrity and identity of the public analytical corpus; it does not impose requirements on external implementations or neighboring repositories.

The authority model is:

```text
four analytical surfaces
one explicit unadopted proposal surface
zero normative specification surfaces
```

The exact artifact declaration is in [`../CANON.md`](../CANON.md) and [`../ARTIFACT.json`](../ARTIFACT.json).

## 4. Claim classes

Every substantive statement should be readable as one of these classes:

| Class | Meaning |
|---|---|
| OBSERVATION | An externally distinguishable event, artifact, output, or behavior. |
| FUNCTIONAL RECONSTRUCTION | A division of responsibilities useful for explaining multiple observations; not a claim of physical module separation. |
| ANALYTICAL INTERPRETATION | A proposed reading of relationships among observations and reconstructions. |
| PROPOSAL | A candidate operational rule that requires adoption, implementation, and testing before stronger status. |
| UNKNOWN | A matter not established by available public evidence. |

Capitalized requirement words such as MUST or SHOULD are used only for internal publication integrity or inside an explicitly marked proposal. They do not impose requirements on BEC, MPAA, PCA, the Review Protocol, CDTS, or external implementations.

## 5. Neutral terminology

| Term | Meaning in this repository |
|---|---|
| **HUMAN PARTICIPANT** | A person who may provide goals, context, values, permissions, evaluation, and external accountability. |
| **AGENT** | The operational participant that interprets tasks, plans, uses available capabilities, and produces results within current authority. |
| **MODEL** | A cognitive or generative component used by an agent or runtime. A model is not automatically the whole agent. |
| **RUNTIME / HOST** | The execution environment that supplies state, tools, routing, permissions, evidence, and result surfaces. |
| **PLATFORM / CONTROL PLANE** | User-side and service-side facilities for configuration, project selection, permissions, protected references, status, and result presentation. |
| **WORKING STATE** | Task-local state required for the next action, including open obligations and accepted constraints. |
| **PERSISTENT CORPUS** | Addressable artifacts that may support later reconstruction or review. Existence does not imply retrieval or use. |
| **RESOURCE** | A file, service, database, tool, or other addressable object available through the runtime. |
| **EVIDENCE** | A trace that supports or contests a claim. Evidence strength depends on its trust anchor and verification method. |
| **DELIVERED** | An observable projection or transmission event; not automatically acceptance, persistence, or commitment. |
| **PERSISTED** | A durable write under a stated boundary; not automatically current retrievability. |
| **RETRIEVABLE** | A currently resolvable artifact under a scoped retrieval attempt; not automatically working-state admission. |
| **COMMITTED** | ARB-03 proposal term for a named next state durably accepted under an identified authority; no normative owner is selected here. |

These are ARB terms only. [`ARB-04`](04_CROSS_SPECIFICATION_CLAIM_BOUNDARIES.md) records partial mappings and non-equivalence rules. Vocabulary overlap does not import another artifact's definition or result.

## 6. Analytical and proposal surfaces

Analytical:

```text
ARB-00 Scope and Status
ARB-01 Functional Boundaries
ARB-02 User Control Plane and Observability
ARB-04 Cross-Artifact Claim Boundaries
```

Proposal:

```text
ARB-03 Closure, Provenance and the Next Action
```

ARB-03 is public and addressable, but it remains unadopted, has no selected normative owner, and has no multi-implementation conformance claim.

## 7. Epistemic boundary

A functional distinction does not prove a physical implementation.

For example, generation and verification can be functionally different while being performed by the same model in separate passes. Routing, memory retrieval, authorization, telemetry, and output transformation can be distributed across several services or collapsed into one implementation.

The public claim is limited to this:

> If two failures can vary independently and require different evidence to diagnose, treating them as one undifferentiated function reduces explanatory and operational precision.

## 8. Neighbor boundary

ARB is an analytical companion to BEC, MPAA, PCA, the Review Protocol, and CDTS.

It may cite their exact sources and explain non-equivalence. It cannot:

- amend their normative surfaces;
- compute their results;
- validate their records;
- import their conclusions;
- turn a shared term into shared ownership;
- treat one correlated record as proof of event identity or causality.

## 9. Status formula

> **ARB is authoritative only for how ARB classifies and presents its analytical distinctions; it is not authoritative for the systems those distinctions describe.**
