---
type: Adapter
id: ADPT-EXEC-TASKSPEC-v0.1
title: Adapter 7 — Task Specification Contract (EM-13)
description: The six unified fields (Goal w/ Tasks->Subtasks, flowing Input, Process, Skills, Output, scaled Redraft), approved-step boundary, two-phase ref pre-read, and reasoning frameworks.
tags: [execution-modes, task-specification, alignment, redraft, em-13]
status: current
---

## 8. Adapter 7: Task Specification Contract

- **EM-13 [P0 | I94/E88/R10] Pre-Work Task Contract**:
  - **IF** a task is non-trivial, not a direct question, and not already defined by an approved step → **THEN** follow a two-phase sequence (`<align>` + `<pointers>`):
    1. Open all matched conditional `ref` specifications first (before editing or proposing a final design).
    2. State the six fields below without preamble and wait for operator confirmation before executing.
  - **Approved-Step Exemption Boundary:** Treat a step as already defined ONLY when it is a trivial `Route 0` typo/lookup OR the next bounded step of a multi-step plan whose `Goal`, `Tasks -> Subtasks`, `Output`, and constraints were explicitly confirmed by the operator without subsequent scope drift (`EM-11`). Unconfirmed prior analysis or exploration never self-authorizes skipping `<align>` (`AD-18`).
  - **IF** the task is a delegation or a session handover → **THEN** `EM-09` (`§5.1`) governs the 4D contract; this adapter supplies `Goal` decomposition and `Redraft` alignment before work begins.

### 8.1 The Six-Field Task Contract (Unified with `EM-10`)

State all six before work starts. Each field prevents a distinct execution failure:

- **Goal**: Concrete desired outcome and hard constraints. For multi-step or multi-module work, decompose into nested **`Tasks -> Subtasks`** before listing edits. Prevents fragmented effort and dropped secondary constraints (`SpecBench`).
- **Input**: Flowing context that feeds execution — opened conditional `ref` specs, authoritative sources with priority rank, verified assumptions, and explicit exclusions (what to ignore). **Never copy-paste the user's raw prompt verbatim.** Prevents redundant noise and missing upstream constraints.
- **Process**: How facts are gathered and **verified** (the exact command or inspection per claim), matched execution adapters, and the **named reasoning framework** if used. Prevents guessing from memory and opaque reasoning.
- **Skills**: The tools or skills to invoke, or explicit `none`. Prevents silent adoption of unrequested workflows.
- **Output**: Target changes on disk and deliverables produced, nested **per subtask** when `Goal` spans multiple subtasks. Prevents status reports substituting for real changes.
- **Redraft**: Compact, explicitly disposable preview **by example** — user story, outline, `Given-When-Then` scenario, or sample diff — nested **per subtask** when multi-step and scaled by `EM-06a` (`L0–L3`). Prevents spending execution budget on the wrong mental model.

**Assumptions live inside whichever field depends on them**, never in a trailing footnote. A non-trivial specification claiming zero assumptions usually skipped reading its sources closely.

### 8.2 Scaled `Redraft` & Value Delivery (`EM-06a`)

Match `Redraft` depth to decision stakes and reversibility ([qa-decision-matrix.md](qa-decision-matrix.md) §2.3) so alignment stays high-signal without causing token bloat:

- **`L0` (Routine & Reversible Single Step):** Skip formal redrafting; execute directly (`Route 0`).
- **`L1` (Medium Scope):** One compact outline or brief user story showing section structure and intent per task.
- **`L2` (`Impact >= 80`):** One concrete worked example or `Given-When-Then` acceptance slice per subtask built from real repository data or artifacts.
- **`L3` (High-Risk / Irreversible / Cross-Feature):** Multiple scenarios or failure-edge walkthroughs per subtask with explicit fixture checks before execution begins.

A rejected redraft is the adapter succeeding cheaply before code or prose churn occurs.

### 8.3 Named Reasoning Framework Declaration Inside `Process`

When a task uses a logical or business reasoning framework, **`Process` names it explicitly** so the reader can inspect, challenge, or reproduce the method. *(Verified 2026-11-11 across `apex-meta/informatics/`, `AI-Snippets/`, and local QMD collections: no closed internal framework ranking study exists; use this practical taxonomy and never invent composite ranking scores per `WP-07`.)*

- **Root-Cause & Decomposition:** First Principles breakdown, 5-Whys causal chain.
- **Sequencing & Architecture:** Dependency / Critical Path ordering, Macro-Meso-Micro (`EM-10`).
- **Communication & Product Shaping:** SCQA / Minto BLUF (`WP-12`), User Story Mapping (`Goal -> Tasks -> Subtasks`).
- **Evaluation & Trade-Offs:** Q&A Decision Matrix (`EM-06`), 4-Phase Bake-Off (`EM-07`).
- **Adversarial Verification:** Premortem / Inversion (`FixedBench`-style negative check).

### 8.4 Relationship to Neighbouring Rules

- `<align>` + `<pointers>` in Layer 1 enforce cross-harness pre-action ref reads and 6-field alignment across Claude, Codex, and Gemini without relying on Claude-only hooks (`EM-13` detail lives here).
- `EM-09` §5.1 owns subagent/session handoffs and `EM-14` (`handover.md`) owns step close-out `Continuation` proposals referencing prior reasoning by `path#heading`; never duplicate schemas across adapters (`WP-23`).
- `EM-10` (`iterative-execution.md`) reuses this identical 6-field schema for Route 1 / Route 2 preflights.
- `EM-02` still governs: resolve immediately checkable questions with tools rather than specifying around them.

### 8.5 Task Specification Failure Modes & Not-To-Dos (`WP-25`)

- **Never copy-paste the user prompt into `Input`:** Extract flowing sources, `ref` specs, assumptions, and exclusions while expressing intent in `Goal`.
- **Never skip matched conditional `ref` reads before acting:** Two-phase alignment requires opening matched `ref` files prior to editing or proposing final architecture.
- **Never treat unconfirmed prior analysis as an "approved step":** Only explicit operator confirmation or trivial `Route 0` typos/lookups bypass `<align>`.
- **Never inflate low-risk tasks with `L3` ceremony:** Keep `Redraft` depth proportional to stakes via `EM-06a`.
