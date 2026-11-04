---
type: Adapter
id: ADPT-EXEC-MODES-v0.2
title: Execution Modes & Task Adapters Specification
description: Pluggable operational task adapters for Q&A Decision Matrices, Comparison Bake-Offs, Exact-Match Patching, Handover Protocols, and MMM Iterative Execution.
tags: [execution-modes, task-adapters, decision-matrix, patch-discipline, handover, mmm]
status: current
---

# Execution Modes & Task Adapters Specification

This specification provides deterministic task adapters for autonomous agents. Agents retrieve these adapters just-in-time when specific execution conditions trigger.

---

## 1. Core Execution Invariants (Top-Loaded Primacy)

The following invariants apply across all execution modes. Front-load these boundaries (aiming for roughly the first ~500 tokens):

- **EM-01 [P0 | I98/E96/R05] Whole-File Rewrite Prohibition**: Never overwrite existing repository files via full-file rewrites. Modify existing files strictly using surgical exact-match patch blocks or verified AST patch intents.
- **EM-02 [P0 | I96/E95/R05] Handover Non-Paralysis Invariant**: Never write a handover to defer an action or ambiguity that available tools can resolve immediately. If a fact is checkable, invoke the tool and check it now.
- **EM-03 [P0 | I96/E95/R06] Step-by-Step Context & File Iteration Invariant**: Never front-load massive amounts of files or documentation at session start. Load context step-by-step per active stage and materialize each iteration's output into a dedicated file.
- **EM-04 [P0 | I95/E95/R08] Target Dominance**: Optimize for the most balanced, value-efficient, and effective path to the stated user outcome. Do not substitute process ceremony, secondary schemas, or self-verifying scripts for the required deliverable. Canonical: `AD-01`.
- **EM-05 [P0 | I94/E92/R10] Two-Strike Pivot Rule**: Stop repairing a failing subsystem if two consecutive fix attempts fail to advance the product. Reconsider the architecture and select an alternative approach. Canonical: `AD-02`; per-subsystem tracking mechanics in `AD-24`.

### Conditional Execution Mode Dispatch (`IF`-Routing)

Evaluate the active task against these conditional gates and load only the matching adapter section:

```xml
<execution_dispatch>
  IF task == "architectural_tradeoff_or_qa_alignment"  THEN apply="#2-adapter-1-qa-decision-matrix"          ELSE skip
  IF task == "multi_candidate_comparison_or_bakeoff"   THEN apply="#3-adapter-2-comparison--bake-off-rubric" ELSE skip
  IF task == "existing_file_mutation_or_patch"         THEN apply="#4-adapter-3-exact-match-patch-discipline" ELSE skip
  IF task == "session_handover_or_subagent_delegation" THEN apply="#5-adapter-4-handover--handoff-protocol"   ELSE skip
  IF task == "multi_step_iterative_or_mmm_execution"   THEN apply="#6-adapter-5-iterative-context--mmm-execution" ELSE skip
  IF task == "repository_sync_or_synch_request"        THEN apply="#7-adapter-6-git-sync--file-preservation"  ELSE skip
</execution_dispatch>
```

---

## 2. Adapter 1: Q&A Decision Matrix

- **EM-06 [P1 | I92/E94/R10] Conditional Q&A Trigger**:
  - **IF** resolving a high-impact architectural trade-off, ambiguous requirement, or interactive Q&A alignment game with the operator → **THEN** structure every question using the Q&A Decision Matrix below.
  - **ELSE IF** the choice is routine, low-stakes, and easily reversible → **THEN** decide autonomously from evidence and **SKIP** this adapter.

### 2.1 Decision Matrix Structure
Every decision matrix block contains the following components:

- **Question**: State the exact problem or decision being resolved.
- **Options**: Enumerate viable options (`Option A`, `Option B`, etc.):
  - *Mechanism*: Detail the technical design in 2–4 concise lines.
  - *Grounding*: Provide a concrete real-world example, process flow, or user story so a reader without deep domain context can immediately grasp the practical impact.
  - *Raw 3-Metric Estimate*: Tag each option with unaggregated estimates `(I<val>/E<val>/R<val>)` on a 1–100 scale (`Impact`: value/effectiveness; `Evidence`: empirical support; `Risk`: misjudgment/complexity/aftermath).
- **Recommendation**: State the recommended option letter.
- **Reasoning**: Provide a dense, evidence-backed justification for the recommended option.
- **Notes**: Provide one concise line per rejected option stating its decisive disqualifier (`Letter — rejection reason`).

### 2.2 Canonical Decision Matrix Example
```markdown
- *Question:* Which state management library should the Flutter mobile client adopt?
- *Options:*
  - Option A (Bloc): Event-driven reactive architecture separating business logic from UI via streams. Grounding: Standard pattern in enterprise banking apps with strict audit logging. (I85/E95/R20)
  - Option B (Riverpod): Compile-safe dependency injection and reactive caching framework. Grounding: Lightweight mobile commerce app requiring rapid prototyping and minimal boilerplate. (I90/E90/R15)
  - Option C (SetState / Vanilla): Native widget-tree state passing. Grounding: Single-screen internal utility tool. (I40/E80/R70)
- *Recommendation:* Option B
- *Reasoning:* Option B delivers compile-time safety and minimal boilerplate while satisfying our offline caching requirements with ~40% less code than Option A.
- *Notes:*
  - Option A — Rejected due to heavy boilerplate overhead that slows velocity for a two-person team.
  - Option C — Rejected because widget-tree coupling fails scalability and testability requirements.
```

---

## 3. Adapter 2: Comparison & Bake-Off Rubric

- **EM-07 [P1 | I88/E90/R12] Conditional Bake-Off Trigger**:
  - **IF** conducting a landscape scan or comparing multiple competing libraries, frameworks, tools, or architectures → **THEN** execute the 4-Phase Analytical Workflow below.
  - **ELSE IF** an existing repository tool already satisfies the requirement (`Reuse Before Build`) → **THEN** reuse the existing tool and **SKIP** this adapter.

The 4-phase workflow (candidate discovery, weighted scoring, ranked verdicts, prototypes with
decision triggers) and the canonical candidate-scoring table format are owned by
[specs/execution-modes/bake-off.md](execution-modes/bake-off.md) §3.1–3.2 — open it when this
adapter fires; not restated here (`WP-23`).

---

## 4. Adapter 3: Exact-Match Patch Discipline

- **EM-08 [P1 | I98/E96/R05] Conditional Patch Trigger**:
  - **IF** modifying any existing repository file → **THEN** apply surgical exact-match replacement blocks (`Mode A`) or AST patch intents (`Mode B`).
  - **IF** exact live target lines have not been inspected in the current session → **THEN** read the target file range first; never guess `<old>` lines from memory.
  - **IF** moving or copying files → **THEN** use deterministic filesystem/git commands (`git mv`, `cp`), never whole-file content rewrites.

Mode A's block-replacement protocol and worked `<file>/<old>/<new>` example, and Mode B's
`patch_intent.v1` contract and worked JSON example, are owned by
[specs/execution-modes/patch-discipline.md](execution-modes/patch-discipline.md) §4.1–4.2 — open it
when this adapter fires; not restated here (`WP-23`).

---

## 5. Adapter 4: Handover & Handoff Protocol

- **EM-09 [P1 | I92/E95/R08] Conditional Handover Trigger**:
  - **IF** concluding an agent session, delegating work to a subagent, or transferring context across boundaries → **THEN** structure the handover using the Dimensional Contract and 5-Component Report below.
  - **IF** an open question or ambiguity is checkable right now using available tools or parallel subagents → **THEN** **DO NOT write a handover**; invoke the tool and resolve it in the current turn (`EM-02`).

The 4-Dimensional Handover Contract and the 5-Component Forensic & Completion Report structure are
owned by [specs/execution-modes/handover.md](execution-modes/handover.md) §5.1–5.2 — open it when
this adapter fires; not restated here (`WP-23`).

---

## 6. Adapter 5: Iterative Context & MMM Execution

- **EM-10 [P1 | I95/E95/R08] Conditional Iterative & MMM Trigger**:
  - **IF** the task is clear, bounded, and single-step (`Route 0`) → **THEN** execute directly (`understand → execute → verify → deliver`) and **SKIP** multi-file scaffolding.
  - **ELSE IF** the task has moderate multi-step uncertainty (`Route 1`) → **THEN** write a compact preflight block (Target, Inputs, Scope, Output, Active Step) and execute step-by-step.
  - **ELSE IF** the task is a multi-module, research-heavy, or architectural project (`Route 2 / MMM`) → **THEN** execute the **File-Backed Iterative & Step-by-Step Context Protocol** below, creating dedicated files at each iteration.

The anti-front-loading context protocol, the file-producing iterative execution loop (the four
numbered iterations), and the Macro-Meso-Micro decomposition table are owned by
[specs/execution-modes/iterative-execution.md](execution-modes/iterative-execution.md) §6.1–6.3 —
open it when this adapter fires; not restated here (`WP-23`).

- **EM-11 [P2 | I82/E86/R12] Upward Invalidation Rule**: Update only the specific architectural layer disproven by concrete evidence. Never alter high-level Macro strategy solely because low-level Micro implementation details changed.

---

## 7. Adapter 6: Git Sync & File Preservation

- **EM-12 [P2 | I80/E90/R08] Conditional Sync (`Synch`) & Scoped Push Trigger**:
  - **IF** pushing named files (`git push <paths>`) → **THEN** stage only those paths, commit, and push (`git pull --rebase` on non-fast-forward), ignoring unrelated dirty files.
  - **IF** the operator calls for a `sync` / `synch` → **THEN** execute a full push-and-pull synchronization (`git pull --rebase` and `git push`) paired with a quick status check to ensure no files are accidentally lost in the process.
  - **IF** files have been explicitly marked for deletion → **THEN** allow their deletion during sync; **ELSE** preserve all files and never drop or exclude remaining dirty files just because they were outside the current task scope (commit unrelated files in a separate commit if needed so all work is safely preserved).

---

## 8. Execution Failure Modes & Not-To-Dos

Guard actively against these recurring task-execution failure modes.

- **Do not overwrite existing files with full-file rewrites**: Always modify existing files via exact-match replacement blocks or `patch_intent.v1` (`EM-01`, `EM-08`).
- **Do not write a handover to escape checkable work**: Never defer a question that available tools or subagents can verify right now (`EM-02`, `EM-09`).
- **Do not front-load bulk repository context**: Load sources step-by-step via an Input Priority Ledger and materialize each iteration into a dedicated file (`EM-03`, `EM-10`).
- **Do not compute synthetic scores in decision matrices**: Keep `Impact`, `Evidence`, and `Risk` (`I/E/R`) as three separate raw numbers on a 1–100 scale (`EM-06`).
