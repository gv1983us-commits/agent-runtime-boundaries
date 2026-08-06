# Functional Boundaries in Agent Systems

**Document:** ARB-01  
**Status:** PUBLIC DRAFT  
**Mode:** FUNCTIONAL RECONSTRUCTION  
**Version:** 0.3

## 1. Boundary model

A model-based agent system can be inspected through a set of responsibilities without assuming that each responsibility is a separate physical component.

```text
HUMAN PARTICIPANT
        |
        v
PLATFORM / CONTROL PLANE
        |
        v
RUNTIME / HOST ---- resources, tools, persistent corpus
        |
        v
AGENT PROCESS ---- model-assisted interpretation and generation
        |
        v
execution events, evidence, result, error
        |
        v
PLATFORM / CONTROL PLANE ---- visible projection to the human participant
```

This diagram is topological, not a mandatory call sequence. Implementations may be synchronous, asynchronous, recursive, or distributed.

This document is an analytical surface. It does not prescribe a physical architecture or create conformance requirements.

## 2. Human participant and technical system

**FUNCTIONAL RECONSTRUCTION.** A human participant may contribute lived context, objectives, values, evaluation, permission, and accountability. The human participant may correct direction or approve an external action, but is not a technical submodule of the agent or runtime.

A system description should therefore avoid reducing the person to an input source, memory device, or hidden controller. Human participation and technical execution are related but remain distinct responsibility domains.

## 3. Model, agent, runtime, and platform

### 3.1 Model

A model transforms supplied inputs into candidate representations or outputs. It may contribute interpretation, reasoning, planning, verification, or generation, depending on the invocation.

A model identifier alone does not establish:

- available tools;
- current authorization;
- persistent state;
- execution evidence;
- identity continuity;
- the complete behavior of the surrounding agent.

### 3.2 Agent

The agent is the task-facing operational participant. It interprets the active request, selects a next action, uses capabilities supplied by the runtime, and communicates a result or limitation.

The agent is not reducible to one model call when the task depends on files, tools, state restoration, authorization, external actions, or verification.

### 3.3 Runtime / host

The runtime or host supplies the current execution environment. It may own:

- model access and routing;
- working state;
- tool and resource access;
- authorization and confirmation handling;
- persistent artifact access;
- execution traces and receipts;
- retries, errors, and lifecycle transitions.

A runtime feature being available does not prove that it was authorized, invoked, or used successfully.

### 3.4 Platform / control plane

The platform or control plane exposes configuration, project selection, model and tool availability, permission surfaces, protected references, status indicators, and result views. It may operate before, during, and after a model invocation.

The control plane is broader than a text input/output wrapper. It is also not necessarily one component: local application state, credential storage, service policy, and user interface may be physically separate.

## 4. State, transition, and invariants

A task step can be represented as:

```text
S0 --T--> S1
```

Where:

- `S` is the task-relevant state at a point in time;
- `T` is an operation or composite transition;
- an invariant is a condition expected to remain valid across an accepted transition.

An invariant does not prohibit all change. It defines the condition under which a change can still count as an acceptable continuation inside the analytical model.

A state description may include:

```text
active task
accepted constraints
open obligations
available capabilities
current authority
retrieved evidence
intermediate results
environment state
```

The state need not be held in one object or exposed to the model in full.

## 5. Distinctions with independent failure modes

### 5.1 Fluent generation is not verified reasoning

**OBSERVATION.** A fluent output can contain a structural, factual, or causal error.

**FUNCTIONAL RECONSTRUCTION.** Realization of an answer and evaluation of its support are different responsibilities. The same model may perform both in separate passes, or verification may be delegated to tools or external checks.

### 5.2 Deciding that an action is needed is not executing it

**OBSERVATION.** A system can correctly state that a file, search, or calculation is required without actually invoking the corresponding capability.

**FUNCTIONAL RECONSTRUCTION.** Action selection and runtime invocation must be evaluated separately. Execution claims require execution evidence, not only a plausible description.

### 5.3 Storage is not retrieval

**OBSERVATION.** Information may exist in an addressable artifact but fail to affect a task result.

```text
stored
!= selected
!= retrieved
!= admitted into working state
!= used in a decision
```

The absence of an item from an answer does not by itself prove that it was absent from storage. Conversely, existence in storage does not prove that it was used.

### 5.4 Retrieved material is not active working state

Retrieved material may be stale, irrelevant, conflicting, or incomplete. Working state is the task-local selection that has been interpreted and admitted for the next action.

A reliable transition records which source and version were used, what was accepted, and what remains unresolved.

### 5.5 Output transformation is not model intent

A visible result can be shortened, formatted, blocked, or transformed after candidate generation. The visible result alone cannot establish whether an omitted element was never produced, removed later, or intentionally withheld. Without an addressable trace, the internal path remains `UNKNOWN`.

### 5.6 Delivery is not commitment

A result may be displayed without updating the state from which the next step will begin.

```text
result delivered
+ state not committed
= possible continuation from a stale state
```

This is a distinct failure class from forgetting a stored fact. The artifact may exist while the next working state still points to an earlier snapshot.

### 5.7 Persistence is not retrievability

An artifact may be written under one storage boundary while the next runtime lacks current authority, capability, routing, or a resolvable reference to retrieve it.

```text
persisted != retrievable
```

### 5.8 Retrievability is not working-state admission

A retrieval can succeed while the result remains stale, conflicting, untrusted, or irrelevant to the active task.

```text
retrievable != admitted into working state
```

### 5.9 Commitment is not process continuation

A named next state may be durably accepted under an authority without establishing the broader PCA question of whether a process continued across an explicit transition.

```text
committed != PCA process continuation
```

`committed` remains an ARB-03 proposal term until an owning specification adopts it.

## 6. Minimal diagnostic questions

For a failed or disputed task, ask in order:

1. What input and configuration reached the task boundary?
2. What current authority and capabilities existed?
3. What sources or tools were selected and actually invoked?
4. What evidence entered working state?
5. What decision or candidate result was produced?
6. What transformation occurred before user-visible delivery?
7. Was the result persisted, and under what boundary?
8. Was it retrievable by the next runtime?
9. What material was admitted into the next working state?
10. What state change was committed, if any?
11. Which claims are verified, observed, self-reported, proposed, or unknown?

This sequence locates responsibility without claiming knowledge of hidden implementation details.

## 7. Analytical boundary

```text
useful distinction != physical module proof
failure diagnosis != neighboring verdict
analytical sequence != mandatory pipeline
```

The exact relation to BEC, MPAA, PCA, the Review Protocol, and CDTS is recorded in [`04_CROSS_SPECIFICATION_CLAIM_BOUNDARIES.md`](04_CROSS_SPECIFICATION_CLAIM_BOUNDARIES.md).
