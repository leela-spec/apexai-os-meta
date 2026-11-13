---
type: Adapter
id: ADPT-EXEC-ITERATIVE-v0.2
title: Adapter 5 — Iterative Context & MMM Execution (EM-10/EM-11)
description: Anti-front-loading context management, the file-producing iteration loop, and Macro-Meso-Micro decomposition.
tags: [execution-modes, iterative, mmm, context, em-10, em-11]
status: current
---

## 6. Adapter 5: Iterative Context & MMM Execution

- **EM-10 [P1 | I95/E95/R08] Conditional Iterative & MMM Trigger**:
  - **IF** the task is clear, bounded, and single-step (`Route 0`) → **THEN** execute directly (`understand → execute → verify → deliver`) and **SKIP** multi-file scaffolding.
  - **ELSE IF** the task has moderate multi-step uncertainty (`Route 1`) → **THEN** write a compact 6-field preflight (`Goal` w/ `Tasks -> Subtasks`, flowing `Input`, `Process`, `Skills`, `Output`, `Redraft` per `EM-13`) and execute step by step.
  - **ELSE IF** the task is a multi-module, research-heavy, or architectural project (`Route 2 / MMM`) → **THEN** open matched conditional `ref`s, align once on the unified 6-field contract, and execute the **File-Backed Iterative & Step-by-Step Context Protocol** below, creating dedicated files at each iteration.

### 6.1 Step-by-Step Conscious Context Management (Anti-Front-Loading)
Never bulk-load massive amounts of files or directories at the start of a task:
1. **Build an Input Priority Ledger First**: List candidate sources, rank their priority, note what specific aspect is needed from each file, and mark unrelated files as excluded.
2. **Load Context Per Active Step Only**: Read only the sources required for the current step/module.
3. **Externalize to Disk & Drop Raw Context**: Write the distilled findings and decisions of the current step into a dedicated step file so subsequent steps read the compact step artifact rather than re-reading raw source dumps.

### 6.2 File-Producing Iterative Execution Loop (`Each Iteration Creates Files`)
Work iteratively from a rough meta-layer skeleton down to verified module details, materializing files at every stage:

1. **Iteration 1 — Master Matrix & Meta-Layer Draft (`00-master-matrix.md`)**:
   - Create a rough draft of the `Goal -> Tasks -> Subtasks` tree, planned files, processes, and expected outcomes (the **meta-layer**) first.
   - Include a matrix of all steps and options so the overall structure can be verified before investing tokens in deep detail ("meat").
2. **Iteration 2 — Implementation Map & Theoretical Simulation (`01-implementation-map.md`)**:
   - Map out all recommended options and architectural connections.
   - Test or simulate the workflow theoretically to catch structural flaws early.
3. **Iteration 3 — Per-Step / Per-Module Files (`step-XX-<module>.md`)**:
   - Create a dedicated file for each step or module covering all options and recording:
     - **Existing Assets to Copy/Reuse**: What already exists in the repo and can be deterministically reused or copied.
     - **Input & Context Scope**: The exact sources loaded for this step.
     - **Surfaced Details & Realization**: The concrete implementation/prose meat plus new edge cases or details discovered during this step.
     - **Step Verification**: Concrete validation of the step's output against target intent.
4. **Iteration 4 — Master File Consolidation & Work-Finish Protocol**:
   - Recreate/update the Master Matrix file incorporating all newly surfaced details and verified outcomes from each step file.
   - Execute the **Work-Finish & Close-Out Protocol** (`EM-14` in [handover.md](handover.md)): verify against stated requirements, commit/push scoped paths (ignoring unrelated dirty files per `EM-12`), update the canonical/plan files, and propose the next 6-field `Continuation` linking prior reasoning by `path#heading`.

### 6.3 Macro-Meso-Micro (MMM) Decomposition & Bottom-Up Return
| Layer | Focus Question | Scope | Core Contents |
|---|---|---|---|
| **Macro** | **Why?** | System Intent | Purpose, target value, external boundaries, global constraints, whole-target acceptance criteria |
| **Meso** | **How?** | Architecture | Sub-modules, component responsibilities, interfaces, dependencies, sequencing constraints |
| **Micro** | **What exactly?** | Realization | Exact code/prose, surgical patch blocks, concrete steps, unit tests, completion evidence |

- **Top-Down Decomposition, Bottom-Up Verification**: Decompose intent `Macro → Meso → Micro`, then verify each realized `Micro` unit against its `Meso` interface and validate the assembled system against `Macro` intent.
- **EM-11 [P2 | I82/E86/R12] Upward Invalidation Rule**: Update only the specific architectural layer disproven by concrete evidence. Never alter high-level Macro strategy solely because low-level Micro implementation details changed.

---
