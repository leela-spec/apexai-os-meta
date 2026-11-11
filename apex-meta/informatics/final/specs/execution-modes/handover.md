---
type: Adapter
id: ADPT-EXEC-HANDOVER-v0.2
title: Adapter 4 — Handover, Step Close-Out & Continuation Protocol (EM-09/EM-14)
description: The 4-dimensional handover contract, 5-component forensic report, EM-14 major step close-out and Continuation proposal protocol, and scoped Git preflight guard.
tags: [execution-modes, handover, delegation, close-out, continuation, em-09, em-14]
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

### 5.3 Major Step Close-Out & Continuation Protocol (`EM-14`)

- **EM-14 [P0 | I92/E95/R07] Major Step Close-Out & Continuation**:
  - **IF** completing a major step or multi-step phase → **THEN** execute all four close-out steps below before declaring completion or proposing follow-up work:
    1. **Verify:** Check every stated requirement and target gate directly against the modified artifacts (`<target>`, `AD-01`). If an operating artifact owns the change, verify that file itself reflects the update.
    2. **Scoped Stage, Commit & Push (`EM-12`):** When delivery includes repo persistence or sync, stage explicitly scoped paths (`git add -- <paths>`), commit, and push (`git pull --rebase` on non-fast-forward).
    3. **Update Owning & Working Files:** Mark completed tasks/decisions in the living working plan and canonical operating artifact so later steps or chats never repeat finished work (`FA-01`).
    4. **Propose Next 6-Field `Continuation`:** Draft the next step using the unified 6-field contract (`Goal` w/ `Tasks -> Subtasks`, flowing `Input`, `Process`, `Skills`, `Output`, `Redraft` per [task-specification.md](task-specification.md) §8.1), linking prior established reasoning by `path#heading` instead of restating solved analysis (`<context>`, `WP-23`).

### 5.4 Scoped Git Preflight Guard

- Never halt a step close-out on a blanket `git status --porcelain` check over unrelated dirty workspace files.
- Scope preflight status inspection to target deliverables and their direct dependencies (`git status --short -- <target_paths>`); preserve unrelated dirty files untouched (`EM-12`).

### 5.5 Handover & Close-Out Failure Modes & Not-To-Dos (`WP-25`)

- **Never write a handover to escape resolvable work (`EM-02`):** Invoke tools and answer checkable questions in the active turn.
- **Never rewrite already-settled prior reasoning inside a `Continuation`:** Reference the authoritative rationale via `path#heading` links.
- **Never mark a rule or design change Done inside quotes or handovers alone:** Update the owning canonical operating file first (`FA-01`).
- **Never abort a scoped push or close-out over unrelated dirty workspace files:** Check only target paths and keep adjacent work untouched.

---
