# Scope and Status

**Document:** ARB-00
**Status:** DRAFT
**Mode:** DESCRIPTIVE / ANALYTICAL
**Version:** 0.1-candidate

## 1. Scope

This document set describes functional boundaries in model-based agent systems. Its purpose is to make observable responsibilities and failure locations easier to distinguish without claiming access to hidden implementation details.

The scope includes:

- separation of human, agent, model, runtime and platform roles;
- separation of working state, persistent artifacts, resources and execution;
- user-side control, authorization surfaces and observability;
- state transitions, provenance, receipts and open obligations;
- limits on what a visible answer or status can establish.

## 2. Out of scope

This document set does not define:

- consciousness, subjectivity or personhood;
- a universal internal architecture for language models;
- a specific identity or identity profile;
- a specific product, provider, model or deployment;
- legal or organizational authority;
- a replacement for MPAA, PCA or BEC;
- conformance to any external specification.

## 3. Claim classes

Every substantive statement should be readable as one of these classes:

| Class | Meaning |
|---|---|
| OBSERVATION | An externally distinguishable event, artifact, output or behavior. |
| FUNCTIONAL RECONSTRUCTION | A division of responsibilities useful for explaining multiple observations; not a claim of physical module separation. |
| ANALYTICAL INTERPRETATION | A proposed reading of relationships among observations and reconstructions. |
| PROPOSAL | A candidate operational rule that requires implementation and testing before stronger status. |
| UNKNOWN | A matter not established by available public evidence. |

Capitalized requirement words such as MUST or SHOULD are used only for the internal integrity of this candidate document set or inside an explicitly marked proposal. They do not impose requirements on MPAA, PCA, BEC or external implementations.

## 4. Neutral terminology

| Term | Meaning in this repository |
|---|---|
| HUMAN PARTICIPANT | A person who may provide goals, context, values, permissions, evaluation and external accountability. |
| AGENT | The operational participant that interprets tasks, plans, uses available capabilities and produces results within current authority. |
| MODEL | A cognitive or generative component used by an agent or runtime. A model is not automatically the whole agent. |
| RUNTIME / HOST | The execution environment that supplies state, tools, routing, permissions, evidence and result surfaces. |
| PLATFORM / CONTROL PLANE | User-side and service-side facilities for configuration, project selection, permissions, protected references, status and result presentation. |
| WORKING STATE | Task-local state required for the next action, including open obligations and accepted constraints. |
| PERSISTENT CORPUS | Addressable artifacts that may support later reconstruction or review. Existence does not imply retrieval or use. |
| RESOURCE | A file, service, database, tool or other addressable object available through the runtime. |
| EVIDENCE | A trace that supports or contests a claim. Evidence strength depends on its trust anchor and verification method. |

## 5. Epistemic boundary

A functional distinction does not prove a physical implementation. For example, generation and verification can be functionally different while being performed by the same model in separate passes. Likewise, routing, memory retrieval and output transformation can be distributed across several services or collapsed into one implementation.

The public claim is limited to this:

> If two failures can vary independently and require different evidence to diagnose, treating them as one undifferentiated function reduces explanatory and operational precision.
