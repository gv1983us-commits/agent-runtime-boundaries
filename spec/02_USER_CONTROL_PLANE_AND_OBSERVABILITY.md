# User Control Plane and Observability

**Document:** ARB-02  
**Status:** PUBLIC DRAFT  
**Mode:** FUNCTIONAL RECONSTRUCTION  
**Version:** 0.3

## 1. Purpose

A user interface in an agent system may be more than an input field and output display. It can be part of a broader user-side control plane that configures the active environment, carries permission decisions, and exposes a projection of execution.

This document distinguishes three responsibilities:

```text
user interaction boundary
protected state references and authorization surfaces
observability and result projection
```

These responsibilities may be implemented by different components. This analytical split does not prove physical module separation or impose a mandatory implementation.

## 2. User interaction boundary

The user-side boundary may collect:

- text, voice, files, images, links, or commands;
- project, session, or task selection;
- model, mode, or capability selection;
- confirmation or refusal of an action;
- visible settings and constraints.

The packet supplied to the agent or runtime may therefore contain more than the literal user text. It may include attachment references, project identifiers, channel metadata, and current permission state.

A reviewer should distinguish:

```text
what the human participant entered
what the control plane added
what reached the model or agent
what was excluded or transformed
```

## 3. Protected state and secret references

A user-side application may rely on credentials, account sessions, administrative settings, or connection material. These values should not be treated as ordinary model memory.

A safer responsibility chain is:

```text
protected store
    -> authorized connector or runtime
    -> scoped invocation
    -> operation result
    -> model or agent receives the result,
       not necessarily the secret value
```

The model may need to know that a capability is authorized and available. It usually does not need the underlying secret.

Distinguish:

- a secret value;
- a reference to a protected secret;
- permission to use a capability;
- evidence that the capability was actually invoked.

None implies the others automatically.

## 4. Observability

The control plane may display phases such as reading, searching, invoking a tool, waiting, checking, completing, or failing.

A visible status is evidence that the interface displayed that status. It is not automatically evidence of the hidden internal state implied by the label.

```text
runtime event
    -> telemetry or log
    -> status projection
    -> user interpretation
```

Each arrow may transform, delay, aggregate, or omit information.

A strong observability surface links a status to addressable evidence such as:

- event identifier;
- capability invocation record;
- file or artifact reference;
- timestamp;
- external receipt;
- error object;
- validation result.

A weak surface presents only an animation or text label with no trust anchor.

## 5. State lifetimes

User-side state can have different lifetimes:

```text
single event
current turn
current session
project lifetime
persistent local configuration
protected account state
```

Temporary status indicators may disappear while configuration, history, or audit logs remain. Conversely, an item visible in the interface may never enter model context.

Therefore:

> Not present in model memory does not mean absent from the system, and visible in the interface does not mean supplied to the model.

## 6. Result projection and delivery boundary

A runtime may produce a result before the control plane presents it. Presentation can introduce additional transformations:

```text
runtime result
  -> formatting or policy transformation
  -> channel delivery
  -> user-visible projection
```

A visible answer establishes only that the projection was visible at the boundary inspected. It does not by itself establish:

- the complete candidate generated earlier;
- the absence of post-generation transformation;
- durable persistence;
- future retrievability;
- admission into the next working state;
- next-state commitment.

```text
visible result != complete execution trace
result delivered != state committed
```

## 7. Trust boundary

A final answer without an execution trace asks the consumer to trust a claim. A result linked to evidence allows the consumer to inspect or reproduce part of the claim.

Observability does not create truth by itself. It creates an inspectable boundary only when the presented events are bound to verifiable runtime evidence.

This distinction aligns with execution-evidence systems in which capability, authorization, invocation, evidence, and validation are reported separately. ARB does not compute the neighboring result.

## 8. Failure classes

| Failure | Observable consequence |
|---|---|
| Configuration mismatch | The agent operates in a different project, mode, or capability set than the user intended. |
| Permission projection mismatch | The interface suggests an action is allowed while runtime authorization is absent or stale. |
| Secret boundary failure | Protected values enter ordinary context, logs, or output. |
| Status without event binding | The interface reports progress that cannot be tied to execution evidence. |
| Result projection loss | A valid runtime result is truncated, hidden, or transformed before presentation. |
| Delivery/commitment confusion | A visible result is treated as proof that the next state was accepted and persisted. |
| State lifetime confusion | A temporary choice is treated as persistent, or a persistent rule is treated as turn-local. |
| Persistence/retrieval mismatch | An artifact exists but cannot be resolved by the next runtime. |
| Retrieval/admission mismatch | Retrieved material is present but not accepted into active working state. |

These failures can be diagnosed without claiming direct access to model internals.

## 9. Analytical boundary

```text
status projection != runtime event proof
permission display != current authorization
secret reference != secret value
result delivery != persistence or commitment
observability != truth
```

The exact relation to neighboring records is recorded in [`04_CROSS_SPECIFICATION_CLAIM_BOUNDARIES.md`](04_CROSS_SPECIFICATION_CLAIM_BOUNDARIES.md).
