---
type: Adapter
id: ADPT-EXEC-HANDOVER-v0.2
title: Adapter 4 — Handover & Handoff Protocol (EM-09)
description: The 4-dimensional handover contract and 5-component forensic completion report, plus the non-paralysis guard.
tags: [execution-modes, handover, delegation, em-09]
status: current
---

## 5. Adapter 4: Handover & Handoff Protocol

- **EM-09 [P1 | I92/E95/R08] Conditional Handover Trigger**:
  - **IF** concluding an agent session, delegating work to a subagent, or transferring context across boundaries → **THEN** structure the handover using the Dimensional Contract and 5-Component Report below.
  - **IF** an open question or ambiguity is checkable right now using available tools or parallel subagents → **THEN** **DO NOT write a handover**; invoke the tool and resolve it in the current turn (`EM-02`).

### 5.1 4-Dimensional Handover Contract (Intent & Outcome Focus)
Define every delegated task or handover around concrete outcomes and anti-drift boundaries:
- **Input & Priority Ledger**: Authoritative source files, what specific information is important per source, priority ranking, and what to ignore/exclude.
- **Process**: Expected thinking process, transformation logic, and explicit anti-drift / anti-hallucination boundaries.
- **Output (Predefined Meta-Layer & Examples)**: Target file paths, predefined structure, and concrete example bullets showing expected depth and style.
- **Definition of Done (DoD & Independent Verification)**: Objective simulation, execution run, and output evaluation criteria (explicitly forbidding self-verifying scripts that only check superficial string presence).

### 5.2 5-Component Forensic & Completion Report Structure
1. **Observation**: Direct observations with clickable file links (`path:line`) and exact command outputs.
2. **Logic Chain**: Unbroken step-by-step reasoning connecting observations to the conclusion.
3. **Caveats**: Remaining assumptions, unverified edges, or alternative interpretations (`"No caveats"` if none).
4. **Conclusion**: Actionable final assessment or state of the deliverable.
5. **Verification Method**: Exact reproducible commands, files to inspect, and concrete invalidation conditions.

---
