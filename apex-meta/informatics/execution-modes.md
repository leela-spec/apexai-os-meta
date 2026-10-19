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
- **EM-04 [P0 | I95/E95/R08] Target Dominance**: Optimize for the most balanced, value-efficient, and effective path to the stated user outcome. Do not substitute process ceremony, secondary schemas, or self-verifying scripts for the required deliverable.
- **EM-05 [P0 | I94/E92/R10] Two-Strike Pivot Rule**: Stop repairing a failing subsystem if two consecutive fix attempts fail to advance the product. Reconsider the architecture and select an alternative approach.

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

### 3.1 4-Phase Analytical Workflow

1. **Phase 1: Candidate Discovery & Hard Gating**:
   - Identify ~3–5 viable candidates.
   - Screen each candidate against non-negotiable hard filters; disqualify failing candidates before scoring.
2. **Phase 2: Multi-Metric Evaluation Matrix**:
   - Score surviving candidates on a 1–5 scale across weighted criteria.
   - Record trade-offs in a structured Markdown comparison table including a `Primary Failure Mode` column.
3. **Phase 3: Ranked Verdicts**:
   - Rank candidates from highest to lowest and state a one-sentence placement verdict per candidate.
4. **Phase 4: Functional Prototypes & Decision Triggers**:
   - Provide syntactically complete implementation boilerplate for the winning candidates.
   - Define explicit conditional decision boundaries:
     - `"Select this if..."` `[Exact condition]`
     - `"Avoid this if..."` `[Exact disqualifying edge case]`

### 3.2 Canonical Comparison Matrix Format
| Candidate | Velocity (40%) | Scalability (35%) | Ecosystem (25%) | Weighted Total | Primary Failure Mode |
|---|---|---|---|---|---|
| Candidate A | 4 | 5 | 5 | 4.60 | Steep onboarding learning curve |
| Candidate B | 5 | 3 | 4 | 4.05 | Memory degradation under heavy throughput |
| Candidate C | 2 | 4 | 3 | 2.95 | Lack of community plugins and active maintenance |

---

## 4. Adapter 3: Exact-Match Patch Discipline

- **EM-08 [P1 | I98/E96/R05] Conditional Patch Trigger**:
  - **IF** modifying any existing repository file → **THEN** apply surgical exact-match replacement blocks (`Mode A`) or AST patch intents (`Mode B`).
  - **IF** exact live target lines have not been inspected in the current session → **THEN** read the target file range first; never guess `<old>` lines from memory.
  - **IF** moving or copying files → **THEN** use deterministic filesystem/git commands (`git mv`, `cp`), never whole-file content rewrites.

### 4.1 Mode A: Block Replacement Protocol (`<file>/<old>/<new>`)
When generating file edits for deterministic executors:

1. **One Change Per Block**: Isolate edits into single distinct operations.
2. **Copy Verbatim**: Copy `<old>` text directly from the live inspected file character-for-character.
3. **No Line Numbers**: Identify edit locations purely by exact text matching.
4. **Disambiguating Context**: Include 1–2 surrounding lines so `<old>` matches a single unique location.
5. **Exact Whitespace**: Preserve all indentation, tabs, and line breaks byte-for-byte.
6. **Explicit Uncertainty**: State uncertainty honestly if exact text is unconfirmed rather than guessing.
7. **Unconfirmed Edits**: Never declare an edit complete until tool output confirms application and test evidence passes.
8. **Iterative Application & Git Sync**: Apply patches iteratively, resolve minor incidental friction pragmatically, and synchronize via `git add`, `git commit`, and `git push` (`git pull --rebase` on non-fast-forward).

```xml
<file>path/to/target/file.md</file>
<old>
exact live lines to replace
including surrounding context
</old>
<new>
replacement lines to insert
including surrounding context
</new>
```

### 4.2 Mode B: Structured AST Patch Intent (`patch_intent.v1`)
When interfacing with automated AST patch tools, output JSON conforming to `patch_intent.v1` (see [Governance Schemas](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/governance-schemas.md)):

```json
{
  "schema_version": "patch_intent.v1",
  "intents": [
    {
      "intent_id": "update-auth-port",
      "operation": "replace-once",
      "target": {
        "target_file_guess": "config/services.yaml"
      },
      "hints": {
        "nearby_phrases": ["auth_service:", "port: 8080"]
      },
      "replacement": {
        "content": "  port: 8085\n",
        "content_role": "span_replacement"
      },
      "safety": {
        "require_unique_match": true,
        "fail_on_ambiguity": true,
        "allow_full_file_rewrite": false,
        "max_files_touched": 1
      }
    }
  ]
}
```

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

## 6. Adapter 5: Iterative Context & MMM Execution

- **EM-10 [P1 | I95/E95/R08] Conditional Iterative & MMM Trigger**:
  - **IF** the task is clear, bounded, and single-step (`Route 0`) → **THEN** execute directly (`understand → execute → verify → deliver`) and **SKIP** multi-file scaffolding.
  - **ELSE IF** the task has moderate multi-step uncertainty (`Route 1`) → **THEN** write a compact preflight block (Target, Inputs, Scope, Output, Active Step) and execute step-by-step.
  - **ELSE IF** the task is a multi-module, research-heavy, or architectural project (`Route 2 / MMM`) → **THEN** execute the **File-Backed Iterative & Step-by-Step Context Protocol** below, creating dedicated files at each iteration.

### 6.1 Step-by-Step Conscious Context Management (Anti-Front-Loading)
Never bulk-load massive amounts of files or directories at the start of a task:
1. **Build an Input Priority Ledger First**: List candidate sources, rank their priority, note what specific aspect is needed from each file, and mark unrelated files as excluded.
2. **Load Context Per Active Step Only**: Read only the sources required for the current step/module.
3. **Externalize to Disk & Drop Raw Context**: Write the distilled findings and decisions of the current step into a dedicated step file so subsequent steps read the compact step artifact rather than re-reading raw source dumps.

### 6.2 File-Producing Iterative Execution Loop (`Each Iteration Creates Files`)
Work iteratively from a rough meta-layer skeleton down to verified module details, materializing files at every stage:

1. **Iteration 1 — Master Matrix & Meta-Layer Draft (`00-master-matrix.md`)**:
   - Create a rough draft of all planned files, processes, steps, and expected outcomes (the **meta-layer**) first.
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
   - Execute the **Work-Finish Protocol**: update relevant `README.md` / `index.md` / plan files with completed work and next steps, verify branch status, and synchronize via Git.

### 6.3 Macro-Meso-Micro (MMM) Decomposition & Bottom-Up Return
| Layer | Focus Question | Scope | Core Contents |
|---|---|---|---|
| **Macro** | **Why?** | System Intent | Purpose, target value, external boundaries, global constraints, whole-target acceptance criteria |
| **Meso** | **How?** | Architecture | Sub-modules, component responsibilities, interfaces, dependencies, sequencing constraints |
| **Micro** | **What exactly?** | Realization | Exact code/prose, surgical patch blocks, concrete steps, unit tests, completion evidence |

- **Top-Down Decomposition, Bottom-Up Verification**: Decompose intent `Macro → Meso → Micro`, then verify each realized `Micro` unit against its `Meso` interface and validate the assembled system against `Macro` intent.
- **EM-11 [P2 | I82/E86/R12] Upward Invalidation Rule**: Update only the specific architectural layer disproven by concrete evidence. Never alter high-level Macro strategy solely because low-level Micro implementation details changed.

---

## 7. Adapter 6: Git Sync & File Preservation

- **EM-12 [P2 | I80/E90/R08] Conditional Sync (`Synch`) Trigger**:
  - **IF** the operator calls for a `sync` / `synch` → **THEN** execute a full push-and-pull synchronization (`git pull --rebase` and `git push`) paired with a quick status check to ensure no files are accidentally lost in the process.
  - **IF** files have been explicitly marked for deletion → **THEN** allow their deletion during sync; **ELSE** preserve all files and never drop or exclude remaining dirty files just because they were outside the current task scope (commit unrelated files in a separate commit if needed so all work is safely preserved).
