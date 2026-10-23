---
type: Procedure
title: MMM Working Method
description: Compact procedure for complexity-adaptive top-down definition, bounded realization, and bottom-up verification/validation.
status: candidate_for_testing
---

# MMM Working Method

Use this only when the task is nontrivial enough that direct execution risks losing intent, dependencies, or coherence.

## 1. Choose the smallest sufficient depth

### Simple

If the target is clear, bounded, low-risk, and can be completed coherently in one pass:

```text
understand → execute → verify → deliver
```

Do not create Macro/Meso/Micro artifacts merely for ceremony.

### Structured

If the work has multiple dependent parts, meaningful ambiguity, architectural choices, or a material risk of local work violating the larger goal:

```text
Macro → Meso → Macro check → Micro → Meso check → Macro check
```

### Large / context-heavy

If one structured pass would overload context or the target contains independently complex modules:

- keep the Macro representation compact and durable;
- decompose into bounded Meso modules;
- work one bounded module/context at a time;
- let a complex Meso module recursively use the same method;
- preserve concise decisions, interfaces, evidence, and unresolved issues between iterations;
- return bottom-up after each bounded realization rather than postponing all integration until the end.

## 2. Macro — system intent

Establish only what is necessary to keep lower-level work aligned:

- target and purpose;
- intended value / success;
- system boundary and environment;
- major capabilities or modules;
- global constraints;
- important external and cross-module dependencies;
- acceptance/validation conditions at the whole-target level.

Do not fill Macro with implementation detail.

## 3. Meso — architecture and decomposition

Define the parts required to realize Macro intent:

- modules / sub-targets;
- responsibility of each module;
- dependencies and interfaces;
- sequence or coordination where relevant;
- constraints shared across modules;
- what each module must satisfy from Macro.

Before descending to Micro, check:

> Does this decomposition collectively satisfy the Macro target without contradictions, gaps, unnecessary modules, or broken dependencies?

If not, revise Meso and, when the problem exposes a false higher-level assumption, revise Macro.

## 4. Micro — exact realization

For the active Meso module, define and execute the exact work needed:

- detailed specification/design;
- concrete actions or implementation;
- relevant files/content/code/configuration;
- acceptance conditions/tests;
- evidence of completion.

Load only the context necessary for this bounded unit plus the Macro/Meso constraints it must preserve.

## 5. Bottom-up return

### Micro → Meso: verify and integrate

Ask:

- Does the realized unit satisfy its Meso definition?
- Did implementation reveal false assumptions, missing dependencies, interface problems, or better decomposition?
- Does it integrate coherently with affected sibling modules?

Correct Micro first when the implementation is wrong. Correct Meso when the module definition or architecture is wrong.

### Meso → Macro: validate

Ask:

- Does the integrated result still satisfy the original purpose and value?
- Are system-wide constraints and external dependencies still coherent?
- Has realization revealed that the Macro definition itself must change?

Correct Macro only when evidence or integration invalidates a higher-level assumption; do not rewrite strategy merely because implementation details changed.

## 6. Context rule

Use **progressive disclosure / just-in-time context**:

```text
keep Macro compact
→ load active Meso module + relevant interfaces
→ load active Micro surface
→ execute/verify
→ persist a concise result/evidence summary
→ release unnecessary implementation detail
→ integrate upward
```

Do not load the full project when a bounded subset is sufficient.

## 7. Minimal pre-execution orientation for nontrivial work

Before execution, briefly establish:

```text
Target:
Input / evidence:
Scope:
Expected output:
Macro intent:
Meso decomposition:
Active first step:
Key dependencies / ambiguity:
```

Keep this proportional to task complexity. For obvious tasks, omit it and act directly.

## 8. Iteration rule

The method is iterative, not a one-time waterfall:

```text
Top-down definition
→ bounded realization
→ bottom-up verification/validation
→ update only the level disproven by evidence
→ repeat where necessary
```

The goal is coherent realization with minimal context and minimal process overhead, not producing three documents for every request.

## 9. Relationship to other Apex capabilities

MMM is a **reasoning and working orientation** only.

It does not replace or imply:

- Plan-Sync-Session;
- project/task state management;
- mutation gates;
- a particular agent topology;
- a specific file schema.

Those systems may use MMM when useful, but they remain separate capabilities.
