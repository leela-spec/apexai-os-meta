---
type: Adapter
id: ADPT-EXEC-TASKSPEC-v0.1
title: Adapter 7 — Task Specification Contract (EM-13)
description: The six fields a task states before work starts, the framework declaration inside Process, and the redraft that makes a misread visible while it is still cheap.
tags: [execution-modes, task-specification, alignment, redraft, em-13]
status: current
---

## 8. Adapter 7: Task Specification Contract

- **EM-13 [P0 | I94/E88/R10] Pre-Work Task Contract**:
  - **IF** a task is anything other than a single trivial edit or a direct question → **THEN**
    state the six fields below and obtain confirmation before starting (`<align>`).
  - **IF** the task is a delegation or a session handover → **THEN** `EM-09`'s 4-Dimensional
    Handover Contract governs; this adapter supplies the Redraft and Framework fields it lacks.

### 8.1 The Six-Field Task Contract

State all six before work starts. Each field names the failure it exists to prevent:

- **Input**: The literal ask, in the requester's own words, never a paraphrase. Prevents the task silently becoming the thing the agent found interesting.
- **Sources**: Named artifacts to open — exact paths, never categories — in priority order, plus what to deliberately ignore. Prevents re-deriving what the corpus already records.
- **Process**: How facts are gathered and **verified**, the exact command proving each claim, and **the named reasoning framework if one is used**. Prevents assertion from memory and unstated method.
- **Skills**: The tools or skills to be invoked, or the explicit word **none**. Prevents a framework being adopted without being asked.
- **Output**: What changes on disk, and what the deliverable is. Prevents a report being delivered where a change was wanted.
- **Redraft**: A first, explicitly disposable attempt, described **by example** — one sample row, one heading structure, one finished sentence in the target voice. Prevents the budget being spent before direction is checked.

**Assumptions are named inside whichever field rests on them**, never as a separate footnote or a trailing section. They modify every field rather than sitting beside them, and a task stating no assumptions is usually a task that was not read closely.

### 8.2 Why Redraft carries the weight

Fields 1–5 describe intent. Intent is cheap to agree with and easy to misread, so agreement on
them is weak evidence. **The redraft is the first point at which a misunderstanding becomes
visible** — concrete enough to correct, small enough that discarding it costs nothing.

A rejected redraft is the adapter working, not the work failing.

### 8.3 Framework declaration inside Process

When a task uses a logical or business reasoning framework — critical path, brainstorming
divergence/convergence, decision matrix, bake-off — **Process names it**. An unnamed framework
cannot be checked, reproduced, or argued with, and the reader cannot tell a method from a mood.

> **OPEN (`TODO-EM-13-A`)**: the ranked set of highest-impact reasoning frameworks is already
> researched in this corpus and is not yet linked from here. Resolve by citing that research and
> replacing the illustrative list above with its named set. Until then this field requires a name,
> not a choice from a closed list.

### 8.4 Relationship to neighbouring rules

- `<align>` (Layer 1) is the inline summary; this adapter is its just-in-time detail per
  `<pointers>`.
- `EM-09` §5.1 owns the handover case. Input/Process/Output/DoD there and fields 1/3/5 here are
  the same contract viewed before and after delegation — **do not restate one in the other**
  (`WP-23`).
- `EM-02` still applies: if a field is checkable right now, resolve it rather than specifying
  around it.
