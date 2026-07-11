# APEX Template Family Overview

## One system, twelve dominant jobs

The family uses one recognizable information grammar while preserving one dominant operator question per artifact. The templates are related, not interchangeable.

| Job | Artifact | Dominant operator question | Owns | Hands to | Must not claim |
|---|---|---|---|---|---|
| J1 | Project State Success Card | What project reality is safe to plan from? | Planning-safe state context and freshness | J2 and J3 | Weekly direction or execution plan |
| J2 | Weekly Command Brief | What should this week accomplish? | Portfolio and per-project weekly direction | J3 | Day-level execution detail |
| J3 | PreCap Next Day Brief | What should happen next day, in what order? | Compact day goal and three-sprint outline | J4 | Full tasks, inputs, conditions, or prompt bodies |
| J4 | Flow Execution Card | How is one flow executed safely and completely? | Full single-flow execution workspace | J5 and operator execution | Final prompt content or result interpretation |
| J5 | Prompt Files and Index | Which prompt file is used for which sprint? | Direct prompt access and mapping | Operator execution | Full execution plan or routing reasoning |
| J6 | Execution Evidence Handoff | Is evidence ready for interpretation, or must it be normalized? | Evidence organization and readiness | J7 | Meaning, next-step judgment, or state conclusion |
| J6a | Skip Marker | Why was a planned flow not executed, and how is it handled? | Minimal non-execution record | Planning cycle or J6 | Partial-work recap or large workflow |
| J7 | FlowRecap Result Card | What did the evidence mean, and what is only a candidate change? | Result interpretation and candidate deltas | J8 and J9 | Merge approval or durable write |
| J8 | Usage Learning Card | What reusable routing lesson is supported? | Advisory, evidence-bound usage learning | J12 | Automatic route change |
| J9 | Status Merge Decision Card | Should a candidate state change be accepted? | Operator review and merge decision | J10 | Confirmed durable write |
| J10 | Project KB Update Card | What was prepared or actually written, with what result? | Durable write boundary and result evidence | J11 | Overview truth without confirmed result |
| J11 | Project Status Overview | What confirmed accepted project truth is active now? | Cross-project accepted-state projection | J12 and planning | Candidate acceptance or merge work |
| J12 | AI Routing Card | What route is recommended, and what did the operator decide? | Advisory route plus operator route decision | J4 and J5 after approval | Execution authority by recommendation alone |

## Lifecycle map

```text
PLANNING
J1 Project State Success Card
  -> J2 Weekly Command Brief
  -> J3 PreCap Next Day Brief

EXECUTION PREPARATION AND EVIDENCE
J3
  -> J4 Flow Execution Card
  -> J5 Prompt Files and Index
  -> operator execution
  -> J6 Execution Evidence Handoff
       -> J6a Skip Marker only for a wholly unexecuted planned flow

INTERPRETATION AND LEARNING
J6
  -> J7 FlowRecap Result Card
  -> J8 Usage Learning Card

DURABLE STATE
J7 candidate state
  -> J9 Status Merge Decision Card
  -> J10 Project KB Update Card
  -> J11 Project Status Overview

ROUTING
J8 usage learning + J11 confirmed context
  -> J12 AI Routing Card
  -> J4/J5 only after an operator route decision
```

## Shared anatomy

### Layer 1: operator result card

Required on J1-J12 except J6a:

- state or result;
- concise outcome;
- exact next action;
- review need;
- material warning, confidence, or durable-state note only when it changes the decision.

### Layer 2: valid operator action

The action block uses artifact-specific verbs. Examples: `approve week`, `open first flow card`, `request evidence`, `approve for merge`, `confirm write`, or `approve route`. A generic `approve` is avoided when its meaning could be confused with a later lifecycle gate.

### Layer 3: essential work content

Each artifact exposes only content needed to understand, decide, execute, or hand off its dominant job. Repeated content is linked, not copied.

### Layer 4: review flags

A useful flag answers three questions:

1. What is wrong, missing, stale, conflicting, or uncertain?
2. Why does it matter now?
3. What operator action resolves it?

### Layer 5: provenance and confidence

The compact source section names the decisive inputs, freshness, consequential assumptions, and confidence only when useful. Full source inventories remain elsewhere.

### Layer 6: compact machine handoff

A small YAML block preserves identity, state classification, review status, and downstream references. It never reproduces the human narrative or an owning contract.

### Layer 7: authority metadata

Every template closes with static implementation references: source design, Round 6 overlay intent when applicable, live domain contract references, and overlay application status.

## Boundary pairs

### J3 versus J4

J3 is the day map. J4 is the workbench. J3 shows each flow's three sprint intentions and links to J4. J4 carries complete tasks, inputs, dependencies, outputs, done conditions, and stop or review conditions.

### J4 versus J5

J4 explains the work and links to prompt files. J5 opens and indexes the prompt content. Neither repeats the other's full content.

### J6 versus J7

J6 answers, "What evidence exists and is it usable?" J7 answers, "What does that evidence mean?" J6 must preserve conflicts without resolving them into project-state conclusions.

### J7, J9, J10, and J11

```text
J7: candidate change
J9: operator merge decision
J10: durable write and result evidence
J11: confirmed accepted truth
```

No stage may silently borrow the authority of the next stage.

### J8 versus J12

J8 provides a reusable observation for a comparable task context. J12 weighs that observation with current task and project context, recommends a route, and records the operator's decision. Neither creates automatic routing rules.

## Handoff minimums

| From | To | Minimum carried forward |
|---|---|---|
| J1 | J2 | project state reference, planning readiness, freshness or review flags |
| J2 | J3 | weekly intent, priority traces, capacity and fixed constraints |
| J3 | J4 | flow identity, project, sequence, short sprint intentions, flow-card reference |
| J4 | J5 | prompt requirement by sprint, direct file reference, routing reference |
| Execution | J6 | planned versus actual evidence, outputs, decisions, blockers, source refs |
| J6 | J7 | evidence reference, completion state, readiness, material gaps or conflicts |
| J7 | J8 | usage evidence candidate reference and confidence |
| J7 | J9 | candidate status delta, evidence reference, conflicts, review flags |
| J9 | J10 | approved change, target, provenance, operator decision reference |
| J10 | J11 | confirmed durable result reference and freshness |
| J8 | J12 | advisory route signal, task context, evidence and confidence |
| J11 | J12 | current confirmed project context and constraints |
| J12 | J4/J5 | operator-approved route context, not recommendation alone |

## Interruption recovery pattern

Execution-oriented templates include a visible `Start or resume here` line. Evidence and decision templates include a visible unresolved item or next gate. This gives an operator returning after an interruption a concrete re-entry point without rereading the entire artifact.

## Template complexity envelope

- **Tiny:** J6a Skip Marker.
- **Compact cards:** J1, J7, J8, J9, J10, J12.
- **Briefs with repeatable project or flow sections:** J2, J3, J11.
- **Full execution workspace:** J4.
- **Index plus reusable asset skeleton:** J5.
- **Conditional evidence workspace:** J6.

The shared grammar stops at recognition, action, review, provenance, and handoff. It does not force identical section counts, state values, or detail depth.
