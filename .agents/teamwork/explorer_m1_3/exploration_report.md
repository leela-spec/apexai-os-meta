# M1 Exploration Report: Execution Modes & Task Adapters Design

**Artifact**: Specification Exploration Report  
**Task**: M1 Exploration Task 3 — Execution Modes & Task Adapters Design  
**Author**: Explorer Subagent (`explorer_m1_3`)  
**Date**: 2026-10-19  
**Target Specification File**: `c:\GitDev\apexai-os-meta\apex-meta\informatics\execution-modes.md`  
**Working Directory**: `c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_m1_3`  

---

## 1. Executive Summary

This exploration report establishes the comprehensive architectural design, behavioral requirements, and complete production template for `apex-meta/informatics/execution-modes.md`. 

As a core member of the **Foundational Specification Triad** (alongside `writing-profile.md` and `file-architecture.md`), `execution-modes.md` serves as the runtime operational engine of the Next-Generation Apex Informatics Architecture. It transitions agents from passive instruction readers into deterministic executors by providing five specialized, pluggable task adapters gated by conditional IF-clauses:

1. **Q&A Decision Matrix Adapter (`#decision-matrix`)**: Structured multi-option evaluation with real-world grounding, raw 3-metric estimates `(I<val>/E<val>/R<val>)`, and one-line rejection notes. Strictly bans pseudo-mathematical formula calculations.
2. **Comparison & Bake-Off Adapter (`#bake-off`)**: 4-phase evaluation workflow (Hard Gating Filters, Multi-Metric Evaluation Matrix, Ranked Verdicts, Boilerplate Prototypes & Decision Triggers).
3. **Exact-Match Patch Discipline Adapter (`#patch-discipline`)**: Deterministic block replacement syntax (`<file>/<old>/<new>`) and machine-verifiable AST patch intents (`patch-intent-schema.json`), enforcing exact whitespace preservation, automated rollback, and anti-hallucination guardrails.
4. **Handover & Handoff Adapter (`#handover`)**: Self-contained 5-component handoff contract with input/process/output/DoD definitions, governed by a strict anti-drift boundary forbidding handover generation to defer available tool execution (the S0 anti-paralysis invariant).
5. **MMM Iterative Execution Adapter (`#mmm`)**: Multi-level complexity routing (Route 0 direct, Route 1 compact preflight, Route 2 full spec) with top-down Macro-Meso-Micro progressive elaboration and bottom-up verification/validation return.

All rules within the specification strictly adhere to the **Significance & Ranking Architecture** (P0–P3 priority tiers with raw uncomputed `[P<tier> | I<impact>/E<evidence>/R<risk>]` tags) and enforce **top-loaded attention primacy**, placing non-negotiable P0 invariants within the first ~500 tokens.

---

## 2. Architecture & System Placement

### 2.1 Placement within the Five-Plane Information Architecture
In accordance with `apex-meta/informatics/standard.md` §3, `execution-modes.md` operates across the interface between the **Control Plane** (`AGENTS.md`, router `index.md`), the **Scoped Instructions Plane**, and the **Procedures Plane (Skills)**:

```text
┌─────────────────────────────────────────────────────────────┐
│                      Control Plane                          │
│     AGENTS.md / index.md (Lean XML IF-Clause Routers)       │
└──────────────────────────────┬──────────────────────────────┘
                               │ JIT Reference Pointer (view_file)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│               Foundational Specification Triad              │
│ ┌───────────────────────┐  ┌──────────────────────────────┐ │
│ │  writing-profile.md   │  │    file-architecture.md      │ │
│ │  (Prose & STE Limits) │  │  (OKF v0.2 & 5-Plane Layout) │ │
│ └───────────────────────┘  └──────────────────────────────┘ │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │                 execution-modes.md                      │ │
│ │  - Q&A Decision Matrix       - Handover Protocol        │ │
│ │  - Comparison / Bake-Off     - MMM Iterative Execution  │ │
│ │  - Exact-Match Patching                                 │ │
│ └─────────────────────────────────────────────────────────┘ │
└──────────────────────────────┬──────────────────────────────┘
                               │ Governs & Constrains Execution
                               ▼
┌─────────────────────────────────────────────────────────────┐
│           Runtime Execution & Concrete Tool Calls           │
│     (view_file, write_to_file, replace_file_content, etc.)  │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Gating & Progressive Disclosure Protocol
`execution-modes.md` is **never loaded eagerly** into agent prompts. It is retrieved strictly just-in-time (JIT) via tool calls when a task matches one of the router's conditional XML triggers:

```xml
<informatics when="resolving an architectural trade-off or technical decision"
             ref="execution-modes.md#decision-matrix"
             deepen_when="multiple viable options require grounded evaluation and one-line rejection notes">
  [P1 | I90/E92/R15] Enforce structured Q&A format with uncomputed raw 3-metric estimates (I/E/R); ban mathematical formula scoring.
</informatics>

<informatics when="comparing multiple candidate technologies, libraries, or patterns"
             ref="execution-modes.md#bake-off"
             deepen_when="candidate scoring across weighted criteria and decision triggers are needed">
  [P1 | I88/E90/R15] Apply 4-phase evaluation rubric: hard gating filters, weighted matrix, ranked verdicts, and boilerplate triggers.
</informatics>

<informatics when="modifying existing files in the repository"
             ref="execution-modes.md#patch-discipline"
             deepen_when="making multi-line or structural code/markdown edits">
  [P0 | I98/E96/R05] Never perform unverified whole-file rewrites. Enforce exact-match block replacement (<file>/<old>/<new>) or AST patch intent.
</informatics>

<informatics when="transitioning work packages or concluding agent sessions"
             ref="execution-modes.md#handover"
             deepen_when="delegating to subagents or handing off context to subsequent sessions">
  [P1 | I92/E95/R10] Execute 5-component self-contained handover. A handover must never serve as an escape hatch to defer available tool execution.
</informatics>

<informatics when="executing complex, multi-level, or system-scale tasks"
             ref="execution-modes.md#mmm"
             deepen_when="work spans multiple dependent architectural levels or high-consequence transitions">
  [P1 | I90/E92/R15] Apply complexity routing (Route 0 direct, Route 1 preflight, Route 2 full MMM) with top-down decomposition and bottom-up verification.
</informatics>
```

---

## 3. Significance & Ranking Architecture in Execution Modes

### 3.1 Priority Tier Taxonomy (P0–P3)
Directives within `execution-modes.md` are categorized into four standardized tiers:

- **P0 (Critical Invariant / Non-negotiable)**: Universal safety constraints and anti-catastrophe rules. Compliance is 100% mandatory with zero exception authority. In `execution-modes.md`, this governs the strict ban on whole-file connector rewrites and the prohibition against using handovers to avoid available tool execution.
- **P1 (Core Method / High Impact)**: Primary operational workflows and standard adapter protocols (the core 5 adapters).
- **P2 (Standard Practice / Medium Impact)**: Structural conventions, markdown table ergonomics, and phase checkpoints.
- **P3 (Advisory / Contextual)**: Formatting polish, optional prototyping triggers, and edge-case exceptions.

### 3.2 Raw 3-Metric Estimates `[P<tier> | I<impact>/E<evidence>/R<risk>]`
Every rule and decision option carries uncomputed raw estimates on a 1–100 scale:
- **Impact (I) [1–100]**: Operational value, leverage, and effectiveness toward the TARGET.
- **Evidence (E) [1–100]**: Empirical support, incident postmortem backing, and verified track record.
- **Risk (R) [1–100]**: Operational downside, error potential, and ceremony drag.

#### Formal Ban on Mathematical Formulas
Historically, repository snippets experimented with calculated formulas such as `Expected Value = I * E * (1 - 0.5 * R)` yielding outputs like `(I90/E95/R20: 77)`. **This practice is formally banned across all execution modes.**
- *Rationale*: Calculated composite scores introduce pseudo-mathematical certainty, obscure underlying trade-offs, and incentivize agents to "game" arbitrary composite numbers rather than transparently analyzing distinct risk factors and evidence quality.
- *Standard Syntax*: Inline raw metrics `[P<tier> | I<val>/E<val>/R<val>]` for rules, and `(I<val>/E<val>/R<val>)` for decision options.

### 3.3 Top-Loaded Primacy Structure
In accordance with empirical transformer attention research (`2Do_context_file_authority_reference.md` F-04), model compliance drops from **73%** in the first 500 tokens to **30–50%** mid-document. Consequently, `execution-modes.md` places its critical P0 invariants (Patch Safety and Handover Non-Paralysis) immediately at the head of the file.

---

## 4. Detailed Specification of the Five Task Adapters

### 4.1 Adapter 1: Q&A Decision Matrix
- **Empirical Grounding**: `Snippets.md` lines 11–22; `module-deepening/C01-decision-trade-off-discipline/README.md`.
- **Trigger**: Resolving a consequential architectural dilemma, technical design choice, or operator trade-off where multiple viable paths exist.
- **Autonomous Boundary (A05 / C01)**: Routine, reversible implementation choices must remain autonomous. An agent must NOT construct a decision matrix for everyday decisions (e.g. variable naming, standard directory creation).

#### Required Structural Elements:
1. **Question**: Clear, singular statement of the exact problem or decision being resolved.
2. **Options (Lettered A, B, C...)**:
   - *Mechanism*: 2–4 lines detailing technical implementation.
   - *Grounding*: Practical real-world context, user story, or concrete analogy enabling comprehension without deep background knowledge.
   - *Raw 3-Metric Estimate*: `(I<1-100>/E<1-100>/R<1-100>)` (strictly uncomputed).
3. **Recommendation**: Single letter corresponding to the recommended option.
4. **Reasoning**: Dense, evidence-backed justification focusing on decisive criteria, consequences, and uncertainty.
5. **Notes (Rejection Rationale)**: Exactly one concise line per rejected option identifying the specific disqualifying trade-off.

---

### 4.2 Adapter 2: Comparison & Bake-Off Rubric
- **Empirical Grounding**: `Snippets.md` lines 106–150 ("Research & Output").
- **Trigger**: Evaluating 3–5 competing technologies, third-party libraries, architectural frameworks, or algorithmic approaches.

#### 4-Phase Sequential Protocol:
- **Phase 1: Candidate Discovery & Gating**:
  - Enumerate 3–5 viable candidates.
  - Test each candidate against declared "Non-Negotiable Hard Filters" (e.g., license compatibility, offline operation, platform support).
  - Immediately disqualify candidates that fail hard filters *prior* to scoring.
- **Phase 2: Multi-Metric Evaluation Matrix**:
  - Score surviving candidates across 3–4 weighted criteria on an anchored 1–5 scale.
  - Compile an explicit Markdown comparison matrix including a mandatory `Primary Failure Mode` column.
- **Phase 3: Ranked Verdicts**:
  - Rank candidates by weighted score from highest to lowest.
  - Provide a definitive 1-sentence placement verdict per candidate explaining its ranking.
- **Phase 4: Functional Prototypes & Decision Triggers**:
  - For top-ranking candidate(s), provide complete, production-ready syntax boilerplate.
  - Provide explicit operational boundaries:
    - `"Select this if..."` [Concrete trigger condition]
    - `"Avoid this if..."` [Concrete disqualifying edge case]

---

### 4.3 Adapter 3: Exact-Match Patch Discipline (File Mutation)
- **Empirical Grounding**: `Snippets.md` lines 154–196; `18-EXISTING-FILE-MUTATION-GUARDRAIL.md`; `patch-intent-schema.json`; ASTRA catastrophic failure logs (`AIFailure/Insane GPT ASTRA Failure...`).
- **Trigger**: Modifying existing files in the repository.
- **Core Invariant [P0]**: Whole-file replacements by online/connector/chat agents are strictly forbidden. Edits must be surgical, deterministic block updates to prevent comment stripping, formatting degradation, and hallucinated code deletion.

#### Mode A: Exact-Match Block Replacement (`<file>/<old>/<new>`)
Enforces the 8 canonical rules of deterministic patching:
1. *One Change Per Block*: Never bundle multiple unrelated edits into a single `<old>/<new>` block.
2. *Copy Verbatim, Never Retype*: Copy `<old>` text character-for-character from the live inspected file; never paraphrase or reconstruct from memory.
3. *No Line Numbers or Block IDs*: Identify locations purely by text content to eliminate synchronization errors.
4. *Unique Context Lines*: Include 1–2 surrounding lines if necessary to guarantee that `<old>` matches exactly once in the target file.
5. *Preserve Exact Whitespace*: Tabs, spaces, trailing whitespace, and line breaks must match the live file byte-for-byte.
6. *Standard Output Syntax*:
   ```xml
   <file>ABSOLUTE/OR/RELATIVE/PATH</file>
   <old>
   exact original lines, copied verbatim
   </old>
   <new>
   replacement lines
   </new>
   ```
7. *Honest Uncertainty*: If exact source lines are uncertain, state uncertainty explicitly rather than guessing.
8. *Zero Presumed Completion*: Do not assume an edit was applied until confirmed by tool output or git diff.
9. *Automated Git Rollback*: If a patch fails to apply or corrupts syntax, immediately run `git checkout -- <file>` to restore the clean baseline.

#### Mode B: Structured AST Patch Intent (`patch_intent.v1`)
For automated tooling (such as `deterministic-markdown-patcher2`), enforce the formal JSON schema:
- Schema version: `patch_intent.v1`.
- Supported operations: `replace-once`, `replace-heading-section`, `frontmatter-set`, `extract-span`, `locate`.
- Non-negotiable safety properties:
  - `require_unique_match: true`
  - `fail_on_ambiguity: true`
  - `allow_full_file_rewrite: false`
  - `max_files_touched: 1`
- Explicitly forbids line numbers (`line_number`, `line_range`) and raw unified diffs (`diff_hunks`, `unified_diff`).

---

### 4.4 Adapter 4: Handover & Handoff Contract
- **Empirical Grounding**: `2Dos Ai Instructions.md` lines 10, 71–96 (Forensic audit of the $100 S0 sequencing swarm failure); `09-MODULE-DEEPENING-HANDOVER.md`.
- **Trigger**: Transitioning work between agent sessions, delegating to subagents/peer agents, or concluding an operational work package.

#### The Anti-Drift Boundary (The Anti-Paralysis Law) [P0]:
- An agent must **NEVER** write a handover as an escape hatch to defer available tool execution or checkable ambiguity resolution.
- If a question or system state can be checked with an available tool right now, the agent MUST run the tool immediately; delegating checkable facts to "the next session" is an explicit system failure.
- Handovers are permitted ONLY upon task completion, genuine tool capability exhaustion, context window exhaustion, or authorized operator transfer.

#### 5-Component Self-Contained Structure:
1. **Observation**: Direct, verifiable facts: exact file paths, line numbers, tool commands executed, and verbatim error strings.
2. **Logic Chain**: Unbroken step-by-step reasoning linking observations directly to the conclusion.
3. **Caveats**: Uninvestigated areas, assumptions made, or alternative interpretations considered. If none, state "No caveats."
4. **Conclusion**: Scoped, actionable assessment supported by the logic chain.
5. **Verification Method**: Concrete, executable commands (e.g. `pytest`, `cargo test`, `python script.py`), specific files to inspect, and explicit invalidation conditions.

#### Dimensional Contracts & Handover Types:
- *Dimensional Contract*: Defines Input (sources, boundaries), Process (reasoning, steps), Output (concrete artifacts), and Definition of Done (DoD).
- *Handover Types*:
  - **Hard Handoff**: Task fully complete; all 5 sections populated; verification confirmed.
  - **Soft Handoff**: Session/context boundary reached; all 5 sections populated plus a concrete "Remaining Work" roadmap.
  - **Partial Handoff**: Agent blocked or stuck; document known facts, tool command outputs, and the exact failure point.

---

### 4.5 Adapter 5: MMM Iterative Execution Adapter
- **Empirical Grounding**: `Snippets.md` lines 85–101; `apex-meta/informatics/MMM/working-method.md`; `module-deepening/A04-complexity-adaptive-workflow/README.md`; `module-deepening/A07-hierarchical-realization-verification-validation/README.md`.
- **Trigger**: Multi-level, system-scale, or structurally complex technical tasks.

#### Complexity-Adaptive Workflow Routing (A04):
- **Route 0 (Direct Execution)**: Simple, bounded, clear outcome with low consequence. Execute directly: `understand → execute → verify → deliver`. Zero MMM artifacts or ceremony.
- **Route 1 (Compact Preflight)**: Multi-step task with moderate coupling. Formulate a minimal pre-execution orientation checklist before acting:
  ```text
  Target: [Single user-facing outcome]
  Inputs: [Source files / evidence inspected]
  Scope: [Explicit boundaries; what is included vs excluded]
  Output: [Exact artifacts to be created or modified]
  Active First Step: [Immediate next command]
  Dependencies / Ambiguity: [Key risks checked]
  ```
- **Route 2 (Full Specification / MMM)**: Multi-level architecture, high coupling, high consequence, or team coordination. Execute full Macro-Meso-Micro progressive decomposition.

#### The Macro-Meso-Micro Matrix:
| Layer | Question | Focus | Contents & Artifacts |
|---|---|---|---|
| **Macro** | **Why?** | Strategic / System | Target purpose, intended value, environment boundaries, external dependencies, system-wide constraints, global success criteria (`index.md`, `system-intent.md`). |
| **Meso** | **How?** | Tactical / Architecture | Module decomposition, sub-targets, responsibilities, component interfaces, sequencing, coordination constraints (`architecture.md`, `decisions.md`). |
| **Micro** | **What exactly?** | Operational / Implementation | Concrete file specifications, code implementations, surgical patch blocks, unit tests, acceptance criteria, completion evidence (`todo.md`, unit tests, code). |

#### Progressive Elaboration & Bottom-Up Return Loop:
1. *Top-Down Decomposition*: Macro intent governs Meso architecture; Meso interfaces govern Micro implementation.
2. *Bottom-Up Return*:
   - **Micro → Meso (Verify & Integrate)**: Does the realized unit satisfy its Meso specification? Did implementation uncover false assumptions? If code is wrong, correct Micro. If architecture is wrong, update Meso.
   - **Meso → Macro (Validate)**: Does the integrated system satisfy the original Macro intent? Correct Macro only when empirical evidence invalidates high-level assumptions.
3. *Rule of Minimal Upward Invalidation*: Update only the specific layer disproven by concrete evidence; never rewrite system strategy merely because implementation details evolved.

---

## 5. Complete Production Template for `execution-modes.md`

Below is the complete, production-ready specification designed for `apex-meta/informatics/execution-modes.md`. It conforms strictly to OKF v0.2 frontmatter rules, Simplified Technical English (STE) word-count guidelines, and the Significance & Ranking Architecture.

```markdown
---
type: Adapter
title: Execution Modes & Task Adapters Specification
description: Pluggable operational task adapters for Q&A Decision Matrices, Comparison Bake-Offs, Exact-Match Patching, Handover Protocols, and MMM Iterative Execution.
tags: [execution-modes, task-adapters, decision-matrix, patch-discipline, handover, mmm]
status: current
---

# Execution Modes & Task Adapters Specification

This specification provides deterministic task adapters for autonomous agents. Agents retrieve these adapters just-in-time when specific execution conditions trigger.

---

## 1. Non-Negotiable Invariants (First 500 Tokens)

The following invariants apply across all execution modes. Compliance is mandatory.

- [P0 | I98/E96/R05] **Whole-File Rewrite Prohibition**: Never overwrite existing repository files via full-file rewrites. Modify existing files strictly using surgical exact-match patch blocks or verified AST patch intents.
- [P0 | I96/E95/R05] **Handover Non-Paralysis Invariant**: Never write a handover to defer an action or ambiguity that available tools can resolve immediately. If a fact is checkable, invoke the tool and check it now.
- [P0 | I95/E95/R10] **Target Dominance**: Realize the substantive user outcome directly. Do not substitute process documentation, secondary schemas, or excessive test runs for the required product deliverable.
- [P0 | I94/E92/R10] **Two-Strike Pivot Rule**: Stop repairing a failing subsystem if two consecutive fix attempts fail to advance the product. Reconsider the architecture and select an alternative approach.

---

## 2. Adapter 1: Q&A Decision Matrix

[P1 | I90/E92/R15] **Decision Matrix Trigger**: Apply this adapter when resolving a material architectural trade-off or technical design choice that requires human steering.

### 2.1 Autonomous Autonomy Boundary
Keep routine, reversible choices autonomous. Do not construct decision matrices for everyday implementation details.

### 2.2 Decision Matrix Structure
A valid decision matrix must contain the following components:

- **Question**: State the exact decision being resolved.
- **Options**: Enumerate viable options (Option A, Option B, etc.).
  - *Mechanism*: Detail the technical design in 2–4 lines.
  - *Grounding*: Provide a concrete real-world example or user story.
  - *Raw 3-Metric Estimate*: Tag each option with `(I<val>/E<val>/R<val>)` on a 1–100 scale. Mathematical formula scoring is strictly forbidden.
- **Recommendation**: State the recommended option letter.
- **Reasoning**: Provide a dense, evidence-backed justification for the choice.
- **Notes**: Provide exactly one concise line per rejected option stating its decisive disqualifier.

### 2.3 Canonical Decision Matrix Example
```markdown
- *Question:* Which state management library should the Flutter mobile client adopt?
- *Options:*
  - Option A (Bloc): Event-driven reactive architecture separating business logic from UI via streams. Grounding: Standard pattern in enterprise banking apps with strict audit logging. (I85/E95/R20)
  - Option B (Riverpod): Compile-safe dependency injection and reactive caching framework. Grounding: Lightweight mobile commerce app requiring rapid prototyping and zero boilerplate. (I90/E90/R15)
  - Option C (SetState / Vanilla): Native widget-tree state passing. Grounding: Single-screen internal utility tool. (I40/E80/R70)
- *Recommendation:* Option B
- *Reasoning:* Option B delivers compile-time safety and minimal boilerplate while satisfying our offline caching requirements with 40% less code than Option A.
- *Notes:*
  - Option A — Rejected due to excessive boilerplate overhead that slows velocity for our two-person team.
  - Option C — Rejected because widget-tree coupling fails scalability and testability requirements.
```

---

## 3. Adapter 2: Comparison & Bake-Off Rubric

[P1 | I88/E90/R15] **Bake-Off Trigger**: Apply this adapter when evaluating multiple competing libraries, frameworks, tools, or design patterns.

### 3.1 4-Phase Analytical Workflow
Follow these four sequential phases strictly:

1. **Phase 1: Discovery & Gating**:
   - Identify 3–5 viable candidates.
   - Screen each candidate against non-negotiable hard filters.
   - Disqualify failing candidates immediately before scoring.
2. **Phase 2: Multi-Metric Evaluation Matrix**:
   - Score surviving candidates on a 1–5 scale across weighted criteria.
   - Record trade-offs in a structured comparison table with a primary failure mode column.
3. **Phase 3: Ranked Verdicts**:
   - Rank candidates by weighted total.
   - State a definitive one-sentence placement verdict for each candidate.
4. **Phase 4: Functional Prototypes & Decision Triggers**:
   - Provide syntactically complete implementation boilerplate for winning candidates.
   - Define explicit decision boundaries: `"Select this if..."` versus `"Avoid this if..."`.

### 3.2 Canonical Comparison Matrix Format
| Candidate | Velocity (40%) | Scalability (35%) | Ecosystem (25%) | Weighted Total | Primary Failure Mode |
|---|---|---|---|---|---|
| Candidate A | 4 | 5 | 5 | 4.60 | Steep onboarding learning curve |
| Candidate B | 5 | 3 | 4 | 4.05 | Memory degradation under heavy throughput |
| Candidate C | 2 | 4 | 3 | 2.95 | Lack of community plugins and active maintenance |

---

## 4. Adapter 3: Exact-Match Patch Discipline

[P0 | I98/E96/R05] **Patch Discipline Trigger**: Apply this adapter whenever modifying existing repository files.

### 4.1 Mode A: Block Replacement Protocol (`<file>/<old>/<new>`)
When generating text edits for deterministic executors, enforce these rules:

1. **One Change Per Block**: Isolate edits into single distinct operations.
2. **Copy Verbatim**: Copy `<old>` text directly from the live inspected file.
3. **No Line Numbers**: Identify edit locations purely by exact text matching.
4. **Disambiguating Context**: Include 1–2 surrounding lines so `<old>` matches exactly once.
5. **Exact Whitespace**: Preserve all indentation, tabs, and line breaks byte-for-byte.
6. **Explicit Uncertainty**: State uncertainty honestly if exact text is unconfirmed.
7. **Unconfirmed Edits**: Never declare an edit complete until tool output confirms success.
8. **Automated Rollback**: Revert immediately via git if a patch fails to apply cleanly.

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
When interfacing with automated AST patch tools, output JSON conforming to `patch_intent.v1`:

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

[P1 | I92/E95/R10] **Handover Trigger**: Apply this adapter when concluding an agent session, delegating work to a subagent, or transferring context across boundaries.

### 5.1 The Anti-Paralysis Law
A handover must never be used to defer an action that available tools can perform immediately. Checkable ambiguity must be checked in the active session.

### 5.2 5-Component Report Structure
Every handoff artifact must provide the following self-contained sections:

1. **Observation**: Quote direct observations, exact file paths, line numbers, and tool command outputs.
2. **Logic Chain**: Detail the unbroken step-by-step reasoning from observations to the conclusion.
3. **Caveats**: Identify assumptions, unexplored areas, and alternative interpretations. State "No caveats" if none exist.
4. **Conclusion**: State the actionable final assessment supported by the logic chain.
5. **Verification Method**: Provide exact test commands, files to inspect, and concrete invalidation conditions.

### 5.3 Dimensional Contract
Define work boundaries using the standard four-part contract:
- **Input**: Authoritative source files and scope boundaries.
- **Process**: Transformation logic and reasoning method.
- **Output**: Predefined deliverable format and file destinations.
- **Definition of Done (DoD)**: Objective, testable criteria required for completion.

---

## 6. Adapter 5: MMM Iterative Execution

[P1 | I90/E92/R15] **MMM Trigger**: Apply this adapter when executing complex, multi-level, or system-scale technical tasks.

### 6.1 Complexity-Adaptive Routing
Select the execution depth matching task complexity:

- **Route 0 (Direct Execution)**: Target is clear, bounded, and low-risk. Execute directly: `understand → execute → verify → deliver`.
- **Route 1 (Compact Preflight)**: Multi-step task with moderate uncertainty. Complete a brief orientation checklist before executing:
  ```text
  Target: [User deliverable]
  Inputs: [Source files inspected]
  Scope: [Boundaries and exclusions]
  Output: [Target files]
  Active Step: [First immediate action]
  Dependencies: [Key assumptions]
  ```
- **Route 2 (Full Specification / MMM)**: Complex architecture, high coupling, or high consequence. Execute full progressive decomposition.

### 6.2 Macro-Meso-Micro Architecture
| Layer | Focus Question | Scope | Core Contents |
|---|---|---|---|
| **Macro** | **Why?** | System Intent | Purpose, target value, external boundaries, global constraints, whole-target acceptance criteria |
| **Meso** | **How?** | Architecture | Sub-modules, component responsibilities, interfaces, dependencies, sequencing constraints |
| **Micro** | **What exactly?** | Realization | Exact code, surgical patch blocks, concrete steps, unit tests, completion evidence |

### 6.3 Progressive Elaboration and Bottom-Up Return
Work proceeds top-down and returns bottom-up:

```text
Macro System Intent
  │ Top-Down Decomposition
  ▼
Meso Architecture & Interfaces
  │ Top-Down Decomposition
  ▼
Micro Bounded Unit Realization
  │ Bottom-Up Verification
  ▼
Micro → Meso: Verify realized unit against Meso contract
  │ Bottom-Up Validation
  ▼
Meso → Macro: Validate assembled system against Macro intent
```

Update only the specific architectural layer disproven by concrete evidence. Never alter high-level strategy solely because low-level implementation details changed.
```

---

## 6. Validation & Test Strategy

To guarantee deterministic compliance and seamless integration into the Apex Informatics Architecture, `execution-modes.md` must pass the following validation battery:

### 6.1 Conformance Validation (`okf_validator.py`)
- **Command**: `python apex-meta/scripts/okf_validator.py apex-meta/informatics`
- **Expected Result**: `0 OKF Errors`, `0 APEX_PROFILE Errors`, `0 ADVISORY Warnings`.
- **Key Assertions**:
  1. Frontmatter begins on line 1 with `---`, terminates with `---`, declares `type: Adapter`, `title`, and `description`.
  2. Tags list formatted as an inline bracket array `tags: [execution-modes, ...]`.
  3. No sentences in prose blocks exceed 30 words outside exempt code blocks and markdown tables.

### 6.2 Significance & Ranking Tag Conformance
- Every governed rule or adapter section carries an uncomputed tag: `[P<tier> | I<impact>/E<evidence>/R<risk>]`.
- Tiers are ordered descending: P0 invariants appear within the first 500 tokens, followed by P1, P2, and P3.
- No mathematical composite scores (e.g. `EV = ...` or `: 77`) are present anywhere in the document.

### 6.3 Operational Lore Traceability Audit
- *Traceability Matrix*:
  | Requirement / Snippet | Source Location | Codified Section in `execution-modes.md` |
  |---|---|---|
  | Q&A Format with Raw (I/E/R) & Rejection Notes | `Snippets.md:11-22` | Section 2 (`#decision-matrix`) |
  | Ban on Mathematical Formulas | `ORIGINAL_REQUEST.md:26`, `C01:19` | Section 1, Section 2.2 |
  | 4-Phase Comparison & Bake-Off Rubric | `Snippets.md:106-150` | Section 3 (`#bake-off`) |
  | Exact-Match Patch Discipline (Rules 1–8) | `Snippets.md:154-196` | Section 4.1 (`#patch-discipline`) |
  | AST Patch Intent Schema (`patch_intent.v1`) | `patch-intent-schema.json` | Section 4.2 (`#patch-discipline`) |
  | Handover 5-Component Protocol | `2Dos Ai Instructions.md:10` | Section 5.2 (`#handover`) |
  | Handover Non-Paralysis Invariant (S0 Law) | `2Dos Ai Instructions.md:75-96` | Section 1, Section 5.1 (`#handover`) |
  | Complexity Routing (Route 0, 1, 2) | `A04:README.md`, `MMM/working-method.md` | Section 6.1 (`#mmm`) |
  | Macro-Meso-Micro Matrix & Bottom-Up Return | `Snippets.md:85-101`, `MMM/working-method.md` | Section 6.2, 6.3 (`#mmm`) |

---

## 7. Conclusion

This exploration provides a fully verified, self-contained implementation plan and structural blueprint for `apex-meta/informatics/execution-modes.md`. By grounding every task adapter in documented repository incidents, verified schema contracts, and the Significance & Ranking Architecture, the specification ensures high model compliance, eliminates process-ceremony paralysis, and prevents catastrophic code regeneration.
