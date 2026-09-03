---
type: Reference
title: Iterative Vee Method
description: Compact deeper guidance loaded only when direct execution is insufficient.
status: proposed_for_testing
---

# Iterative Vee Method

Load this file only when a task is too coupled, uncertain, high-impact, or context-heavy for reliable direct execution.

## 1. Choose the smallest sufficient mode

| Mode | Use when | Method |
|---|---|---|
| **Direct** | bounded task; outcome and dependencies are obvious | execute → verify result |
| **Single Vee** | several dependent parts; architecture or cross-part consistency matters | Macro → Meso → downward check → Micro → verification → Meso integration → Macro validation |
| **Iterative Vee** | high uncertainty, many interacting modules, large blast radius, or long-horizon work | run bounded Vee cycles; persist only decisions/evidence needed for the next cycle; revise affected layers and repeat |

Do not add process because decomposition is possible. Escalate only when direct execution would create a meaningful coherence, uncertainty, dependency, or context risk.

## 2. One Vee cycle

### A. Macro — orient the system

Establish only what lower layers need to remain coherent:

- purpose and intended value;
- success / acceptance at the whole-target level;
- scope and system boundary;
- environment and important external relationships;
- major capabilities or parts;
- global constraints and cross-cutting dependencies.

**Macro output:** a compact system orientation, not detailed implementation.

### B. Meso — decompose and architect

Define the parts needed to realize Macro:

- modules or subtargets;
- responsibility of each module;
- interfaces and dependencies between modules;
- ordering or coordination constraints;
- which Macro intent or constraint each module supports.

**Downward check:** before adding detailed implementation, test whether the Meso architecture collectively satisfies the Macro intent and whether any important Macro requirement has no owner.

### C. Micro — realize precisely

For the active Meso module only, define and execute the exact work:

- detailed specification;
- concrete actions / implementation;
- code, content, configuration, design or other deliverable;
- acceptance checks / tests;
- evidence needed to prove the result.

Do not load unrelated Micro detail from other modules unless an interface or dependency requires it.

### D. Verify upward — Micro → Meso

Ask:

- Did the implementation satisfy its Meso definition?
- Did tests/evidence support that claim?
- Did implementation reveal a wrong interface, dependency, assumption, or module boundary?

If only the implementation is wrong, revise Micro. If the module definition is wrong, revise Meso and re-check affected Micro work.

### E. Integrate upward — Meso

Check the realized modules together:

- interfaces work together;
- dependencies remain valid;
- duplicated or missing responsibility has not appeared;
- local optimizations have not broken another module;
- the architecture still covers the Macro intent.

Revise only affected modules and their descendants.

### F. Validate upward — Meso → Macro

Ask whether the realized whole still achieves the intended purpose in its actual environment.

This is the distinction from verification:

- **Verification:** built according to the definition.
- **Validation:** built the right thing for the intended purpose.

If evidence invalidates a strategic assumption, update Macro and propagate the consequential delta downward.

## 3. Context discipline

Apply **progressive disclosure / just-in-time context** throughout the Vee:

1. Keep **Macro compact and stable** enough to orient the work.
2. Load only the **Meso modules relevant to the current step**, plus interfaces they depend on.
3. Load only the **Micro artifacts needed for the active realization**.
4. Return upward with **decisions, evidence, failures and changed assumptions**, not copies of all lower-level detail.
5. Use references instead of duplicating the same fact across layers.
6. When a target becomes too large for one coherent cycle, treat a complex subtarget as a nested target and run its own Vee while preserving traceability to the parent.
7. For long work, externalize current state/checkpoints rather than keeping the entire history in conversational context.

The aim is the smallest high-signal context that still preserves the relationships required to make the current decision.

## 4. Minimum traceability

Do not require a heavyweight requirements database. Preserve these relationships in whatever artifact format the active project already uses:

```text
Macro intent/constraint
    ↓ realized by
Meso module
    ↓ implemented by
Micro work
    ↓ supported by
verification evidence
```

A Micro item with no meaningful Meso parent is suspect. A Meso module with no Macro reason is suspect. A material Macro objective with no Meso owner is incomplete.

## 5. Iteration rule

When a check fails:

```text
local Micro defect       → fix Micro → re-verify
module/relationship flaw → revise Meso → re-check affected Micro → integrate again
system/purpose flaw       → revise Macro → propagate affected changes downward → run another bounded Vee
```

Prefer the **smallest corrective loop** that restores coherence. Do not automatically reopen unaffected work.

## 6. What this method does not own

This working method does not itself define:

- project-management schemas;
- agent roles or delegation topology;
- approval or mutation gates;
- Plan-Sync-Session behavior;
- documentation formatting;
- repository write policy.

Those systems may use this orientation, but they remain separate capabilities.

## 7. Established vocabulary to use with AI

When communicating the method, prefer these phrases because they carry established engineering meaning:

- **iterative Vee / V-model**;
- **hierarchical decomposition**;
- **requirements flowdown / allocation** when requirements are actually involved;
- **system → subsystem/module → detailed realization**;
- **bidirectional traceability**;
- **integration**;
- **verification and validation (V&V)**;
- **iterative refinement**;
- **progressive disclosure / just-in-time context**.

Use **Macro / Meso / Micro** as the operator-facing shorthand for strategic/system, tactical/architecture, and operational/implementation layers. Do not imply that Macro/Meso/Micro are formal NASA or V-model terms.