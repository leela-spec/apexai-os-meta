---
type: Concept
title: Iterative Vee Working Orientation
description: Lightweight default working orientation mapping the operator's Macro-Meso-Micro model to established systems-engineering Vee and context-engineering concepts.
status: proposed_for_testing
---

# Iterative Vee Working Orientation

## What this is

This is a **small working orientation**, not another orchestration system, project-management framework, or state machine.

The closest established description of the intended method is:

> **Iterative Vee/V-model systems engineering with hierarchical decomposition, requirements flowdown, bottom-up integration, verification and validation, plus progressive disclosure for AI context management.**

The terms **Macro / Meso / Micro** remain useful local shorthand. They are not presented as formal Vee terminology; they map the operator's way of thinking onto concepts an AI is more likely to already recognize.

## The three layers

| Shorthand | Established analogue | Question | Contains |
|---|---|---|---|
| **Macro** | system-level intent / stakeholder expectations / system context | **Why and what whole are we trying to realize?** | purpose, value, success, scope/boundary, environment, major parts, external relationships, global constraints and interdependencies |
| **Meso** | system architecture / hierarchical decomposition / allocation / subsystem design | **How will the whole be organized and realized?** | modules/subtargets, responsibilities, interfaces, dependencies, sequencing, coordination and how parts jointly satisfy Macro intent |
| **Micro** | detailed design / implementation / product realization | **What exactly must be defined, built or done?** | exact specification, execution, code/content/configuration, tests, acceptance conditions and implementation evidence |

## The core loop

The method is a **Vee**, not a one-way hierarchy.

```text
MACRO — system intent / purpose
        ↓ decompose and derive
MESO — architecture / modules
        ↓ verify fit before descending
MICRO — detailed realization
        ↓ implement and test
MICRO evidence
        ↑ verify against Meso definition
MESO integration
        ↑ validate interactions and correct architecture
MACRO validation
        ↑ confirm the realized whole still serves the purpose
```

For larger or uncertain work, repeat the Vee in bounded iterations. Evidence discovered below may correct assumptions above; changes above must flow back down to affected work.

## Established concepts behind it

- **Hierarchical decomposition / requirements flowdown:** move from higher-level intent to progressively more detailed elements. NASA guidance explicitly requires derived requirements at each level to be validated against their parent before proceeding to the next level.
- **Vee / V-model:** the left side represents decomposition and definition; the return side represents integration and verification. Corresponding lower-level work is checked against what defined it.
- **Verification:** did the realized item comply with its specification?
- **Validation:** does the realized system accomplish its intended purpose?
- **Bidirectional traceability:** lower-level work must have a parent reason; higher-level intent must be traceable to realization and evidence.
- **Iterative refinement:** a failed check revises the lowest affected layer and propagates consequential changes rather than restarting everything.
- **Progressive disclosure / just-in-time context:** keep lightweight references available and load detailed information only when the active task needs it. This is the AI context-management complement to the Vee; it is not part of the classical V-model itself.

## Proposed always-on instruction

This is the candidate short rule to later test in an agent instruction surface:

> **Use the smallest sufficient process.** Simple work: execute and verify directly. Coupled or uncertain work: use an iterative Vee — Macro (purpose/system) → Meso (architecture/dependencies) → Micro (implementation), then verify/validate upward Micro → Meso → Macro and revise mismatches. Keep context just-in-time. For complex work, read `Agent Setup/Iterative-Vee/method.md`.

The rule deliberately does **not** prescribe project files, approval gates, agent roles, Plan-Sync-Session, or a new task schema. Those are separate concerns.

## Why this framing is preferable to inventing a new method

An AI does not need to infer what an entirely local "Macro/Meso/Micro process" means. The instruction gives it established anchors first: **Vee, hierarchical decomposition, verification, validation, traceability, progressive disclosure**. Macro/Meso/Micro then acts only as a compact operator-facing translation.

## Primary references

- NASA Systems Engineering Handbook, Vee discussion: https://ntrs.nasa.gov/api/citations/19930011999/downloads/19930011999.pdf
- NASA Software Engineering Handbook, hierarchical requirements decomposition and parent-level validation: https://swehb.nasa.gov/spaces/7150/pages/16449651/SWE-050%2B-%2BSoftware%2BRequirements
- NASA Systems Engineering Handbook, verification and validation: https://www.nasa.gov/reference/system-engineering-handbook-appendix/
- Anthropic, Effective Context Engineering for AI Agents: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Anthropic, Agent Skills progressive disclosure: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills

## Next step later

Test the short rule against representative tasks before adding it to any always-loaded agent instruction. This folder is currently a proposed working model only.