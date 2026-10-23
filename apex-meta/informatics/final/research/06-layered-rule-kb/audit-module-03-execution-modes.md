---
type: Reference
id: V2-AUDIT-MODULE-03-EXECUTION-MODES
title: Module Audit 03 — Execution Modes & Task Adapters Semantic Block & Ownership Audit
description: Comprehensive rule-by-rule semantic block decomposition, WP-23 single-ownership ledger, redundancy purge, and cross-traceability audit for execution-modes.md.
status: current_truth
tags: [module-audit, plane-4, execution-modes, single-owner, semantic-blocks, traceability]
---

# Module Audit 03: Execution Modes & Task Adapters (`execution-modes.md`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (`<surgical>`, `<editing>`, `<handover>`, `<context>`, `<target>`, `<stop_repairing>`, `<trade_off>`, `<iterative>`, `<sync>`)
> - **Layer 1 (Layered Rule KB):** [rule-01-target.md](rule-01-target.md), [rule-08-context.md](rule-08-context.md), [rule-10-stop-repairing.md](rule-10-stop-repairing.md), [rule-12-surgical.md](rule-12-surgical.md), [rule-13-editing.md](rule-13-editing.md), [rule-17-trade-off.md](rule-17-trade-off.md), [rule-18-handover.md](rule-18-handover.md), [rule-19-iterative.md](rule-19-iterative.md), [rule-21-sync.md](rule-21-sync.md)
> - **Layer 2 (Audited Canonical Module):** [execution-modes.md](../../../execution-modes.md) (`EM-01` through `EM-12`)
> - **Upstream Research & Empirical Lore:** [standard.md](../../../standard.md), [RESULTS-01-gating-efficacy.md](../03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-01-gating-efficacy.md), [RESULTS-06-condition-syntax.md](../03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-06-condition-syntax.md), [C01-decision-trade-off-discipline/README.md](../01-universal-instruction-research/module-deepening/C01-decision-trade-off-discipline/README.md), [Snippets.md](../../../../AI-Snippets/Snippets.md), [2Dos Ai Instructions.md](../../../../AI-Snippets/Orga/2Dos%20Ai%20Instructions.md)

---

## 1. Module Scope, Architectural Role & Governed Rule Inventory

### 1.1 Architectural Domain & Loading Lifecycle
`execution-modes.md` (`ADPT-EXEC-MODES-v0.2`) is the canonical Plane 4 specification governing operational task adapters, exact-match patching, AST patch intents, Q&A decision matrices, comparison bake-offs, forensic handover protocols, MMM iterative execution, and Git file preservation across Apex OS.

Within the **Five-Plane Information Architecture** ([file-architecture.md](../../../file-architecture.md) `FA-03`), `execution-modes.md` provides conditional operational adapters:
- **JIT Activation Trigger (`IF`-Routing):** Rather than loading the entire file unconditionally, an autonomous agent evaluates the top-level `<execution_dispatch>` table and loads only the specific section matching its active task:
  1. `architectural_tradeoff_or_qa_alignment` $\rightarrow$ `#2-adapter-1-qa-decision-matrix` (`EM-06`)
  2. `multi_candidate_comparison_or_bakeoff` $\rightarrow$ `#3-adapter-2-comparison--bake-off-rubric` (`EM-07`)
  3. `existing_file_mutation_or_patch` $\rightarrow$ `#4-adapter-3-exact-match-patch-discipline` (`EM-08`)
  4. `session_handover_or_subagent_delegation` $\rightarrow$ `#5-adapter-4-handover--handoff-protocol` (`EM-09`)
  5. `multi_step_iterative_or_mmm_execution` $\rightarrow$ `#6-adapter-5-iterative-context--mmm-execution` (`EM-10`, `EM-11`)
  6. `repository_sync_or_synch_request` $\rightarrow$ `#7-adapter-6-git-sync--file-preservation` (`EM-12`)
- **Top-Loaded Invariants:** The module front-loads five critical P0 invariants (`EM-01` through `EM-05`) in the first ~500 tokens: whole-file rewrite prohibition, handover non-paralysis, step-by-step context iteration, target dominance, and the two-strike pivot rule.

---

### 1.2 Comprehensive Governed Rule Inventory

The live `execution-modes.md` defines **12 governed rules** across seven sections. The table below documents every rule, its priority tier, raw 3-metric significance rating, formal scope, inputs, outputs, halt conditions, and canonical ownership.

| # | Category | Rule ID | Tier & Metrics | Title | Description & Scope | Inputs / Preconditions | Outputs / Behaviors | Error / Halt Behavior | Canonical Owner |
|---|---|---|:---:|---|---|---|---|---|:---:|
| 1 | Mutation | `EM-01` | `[P0 \| I98/E96/R05]` | Whole-File Rewrite Prohibition | Never overwrite existing files via full-file rewrites. | Modifying existing files. | Enforces surgical exact-match patches or AST intents. | Halt on full-file overwrites. | **EM-01 (Owner)** |
| 2 | Handover | `EM-02` | `[P0 \| I96/E95/R05]` | Handover Non-Paralysis Invariant | Never write a handover to defer what tools can resolve now. | Checkable ambiguity arises. | Resolves facts immediately using tools/subagents. | Reject handovers that escape immediate work. | **EM-02 (Owner)** |
| 3 | Context | `EM-03` | `[P0 \| I96/E95/R06]` | Step-by-Step Context & File Iteration Invariant | Never bulk-read directories upfront; load context per active step. | Starting a complex task. | Reads only active step context; writes step files. | Flag upfront bulk directory reading. | **EM-03 (Owner)** |
| 4 | Target | `EM-04` | `[P0 \| I95/E95/R08]` | Target Dominance | Optimize for user outcome; no process ceremony substitution. | Executing tasks. | Focuses on product delivery over procedural overhead. | Halt when ceremony replaces deliverable. | `AD-01` |
| 5 | Recovery | `EM-05` | `[P0 \| I94/E92/R10]` | Two-Strike Pivot Rule | Stop repairing a failing subsystem after 2 failed fix attempts. | Subsystem repair fails. | Halts and pivots to alternative architecture. | Forbid entering a 3rd repair attempt. | `AD-02`, `AD-24` |
| 6 | Decision | `EM-06` | `[P1 \| I92/E94/R10]` | Conditional Q&A Trigger | Structure high-stakes trade-offs using Q&A Decision Matrix. | High-stakes architectural choice. | Emits Question, Options, Grounding, I/E/R, Recommendation, Notes. | Reject ungrounded choices or synthetic scores. | **EM-06 (Owner)** |
| 7 | Comparison | `EM-07` | `[P1 \| I88/E90/R12]` | Conditional Bake-Off Trigger | 4-Phase Comparison Bake-Off for competing technologies. | Comparing libraries/tools. | 4 phases: Hard Gating, Matrix with Failure Mode, Verdicts, Prototypes. | Reject skipping gating or failure mode column. | **EM-07 (Owner)** |
| 8 | Patching | `EM-08` | `[P1 \| I98/E96/R05]` | Conditional Patch Trigger | Exact-match block replacement (Mode A) or AST patch (Mode B). | Modifying repository files. | Verbatim `<old>` context; `git mv`/`cp` for moves; no line numbers. | Reject guessed lines or non-unique matches. | **EM-08 (Owner)** |
| 9 | Handover | `EM-09` | `[P1 \| I92/E95/R08]` | Conditional Handover Trigger | 4-Dimensional Contract + 5-Component Report. | Session end or delegation. | Input/Process/Output/DoD + Obs/Logic/Caveats/Conclusion/Verify. | Reject vague unstructured handovers. | **EM-09 (Owner)** |
| 10 | Iteration | `EM-10` | `[P1 \| I95/E95/R08]` | Conditional Iterative & MMM Trigger | Route ladder (0 direct, 1 preflight, 2 MMM file loop). | Multi-module or research task. | Each iteration creates files (00-matrix, 01-map, step-XX). | Flag unmaterialized mental state loops. | **EM-10 (Owner)** |
| 11 | Validation | `EM-11` | `[P2 \| I82/E86/R12]` | Upward Invalidation Rule | Invalidate only specific layer disproven by concrete evidence. | Low-level test failure. | Fixes Micro realization without abandoning Macro intent. | Flag rewriting system goals on micro bugs. | **EM-11 (Owner)** |
| 12 | Sync | `EM-12` | `[P2 \| I80/E90/R08]` | Conditional Sync & Scoped Push Trigger | Scoped push (`git push <paths>`) vs full `sync`/`synch`. | Git synchronization. | Preserves unrelated dirty files; rebase on non-fast-forward. | Reject dropping unrequested dirty work. | **EM-12 (Owner)** |

---

### 1.3 Atomic Semantic Block Inventory (`SB-EM-01`..`SB-EM-12`)

Every rule in `execution-modes.md` decomposes into atomic semantic blocks that isolate discrete obligations:

- **`EM-01` (Whole-File Rewrite Prohibition):**
  - `SB-EM-01.1` (*Whole-File Overwrite Ban*): Never overwrite existing repository files via full-file rewrites.
  - `SB-EM-01.2` (*Surgical Patch Enforcement*): Modify existing files strictly using surgical exact-match patch blocks or verified AST patch intents.
- **`EM-02` (Handover Non-Paralysis Invariant):**
  - `SB-EM-02.1` (*Deferral Ban on Checkable Facts*): Never write a handover to defer an action or ambiguity that available tools can resolve immediately.
  - `SB-EM-02.2` (*Check It Now Imperative*): If a fact is checkable, invoke the tool and check it now in the current session.
- **`EM-03` (Step-by-Step Context & File Iteration Invariant):**
  - `SB-EM-03.1` (*Anti-Front-Loading*): Never front-load massive amounts of files or documentation at session start.
  - `SB-EM-03.2` (*Step Context Sizing*): Load context step-by-step per active stage.
  - `SB-EM-03.3` (*Disk Externalization*): Materialize each iteration's output into a dedicated file.
- **`EM-04` (Target Dominance):**
  - `SB-EM-04.1` (*Value-Efficient Path*): Optimize for the most balanced, value-efficient, and effective path to the stated user outcome.
  - `SB-EM-04.2` (*Anti-Ceremony Substitution*): Do not substitute process ceremony, secondary schemas, or self-verifying scripts for the required deliverable (delegates to `AD-01`).
- **`EM-05` (Two-Strike Pivot Rule):**
  - `SB-EM-05.1` (*Two-Strike Halt*): Stop repairing a failing subsystem if two consecutive fix attempts fail to advance the product.
  - `SB-EM-05.2` (*Architecture Pivot*): Reconsider the architecture and select an alternative approach (delegates to `AD-02` and `AD-24`).
- **`EM-06` (Conditional Q&A Trigger):**
  - `SB-EM-06.1` (*Gating Condition*): IF resolving a high-impact architectural trade-off or ambiguous requirement $\rightarrow$ THEN structure using Q&A Decision Matrix; ELSE decide autonomously if routine and reversible.
  - `SB-EM-06.2` (*Matrix Fields*): Include Question, Options (with Mechanism, Grounding, raw I/E/R tags), Recommendation, Reasoning, and one-line rejection Notes.
  - `SB-EM-06.3` (*Anti-Score Calculation*): Keep Impact, Evidence, Risk distinct on 1–100 scale without synthetic formulas.
- **`EM-07` (Conditional Bake-Off Trigger):**
  - `SB-EM-07.1` (*Gating Condition*): IF conducting landscape scans or comparing multiple competing libraries $\rightarrow$ THEN execute 4-Phase Comparison Workflow; ELSE reuse existing tool if available.
  - `SB-EM-07.2` (*4-Phase Workflow*): Phase 1 Candidate Discovery & Hard Gating; Phase 2 Multi-Metric Matrix with `Primary Failure Mode`; Phase 3 Ranked Verdicts; Phase 4 Functional Prototypes & Decision Triggers (`"Select this if..."`, `"Avoid this if..."`).
- **`EM-08` (Conditional Patch Trigger):**
  - `SB-EM-08.1` (*Mode A Protocol*): Exact-match replacement blocks (`<file>/<old>/<new>`); copy `<old>` verbatim; 1–2 surrounding lines; no line numbers; exact whitespace.
  - `SB-EM-08.2` (*Live Inspection Prerequisite*): Read live target lines first; never guess `<old>` from memory.
  - `SB-EM-08.3` (*Asset Moves*): Use deterministic commands (`git mv`, `cp`), never content rewrites.
  - `SB-EM-08.4` (*Mode B Worked Example*): JSON conforming to `patch_intent.v1`; delegates authoritative contract to `governance-schemas.md` §2.2 and `patch-intent-schema.json`.
- **`EM-09` (Conditional Handover Trigger):**
  - `SB-EM-09.1` (*Gating Condition*): IF concluding session, delegating to subagent, or transferring context $\rightarrow$ THEN structure using 4D Contract and 5-Component Report; IF checkable right now $\rightarrow$ resolve now (`EM-02`).
  - `SB-EM-09.2` (*4-Dimensional Contract*): Input & Priority Ledger, Process & Boundaries, Output Structure & Examples, Definition of Done (DoD).
  - `SB-EM-09.3` (*5-Component Report Structure*): Observation (`path:line`), Logic Chain, Caveats, Conclusion, Verification Method.
- **`EM-10` (Conditional Iterative & MMM Trigger):**
  - `SB-EM-10.1` (*Route Ladder*): Route 0 direct execution; Route 1 compact preflight; Route 2 MMM file-producing loop.
  - `SB-EM-10.2` (*Conscious Context Management*): Input Priority Ledger; load context per active step; externalize findings to disk and drop raw context.
  - `SB-EM-10.3` (*File-Producing Iteration Loop*): Iteration 1 `00-master-matrix.md`; Iteration 2 `01-implementation-map.md`; Iteration 3 `step-XX-<module>.md`; Iteration 4 Master Consolidation & Work-Finish Protocol.
- **`EM-11` (Upward Invalidation Rule):**
  - `SB-EM-11.1` (*Surgical Invalidation*): Invalidate only the specific architectural layer disproven by concrete evidence.
  - `SB-EM-11.2` (*Macro Intent Preservation*): Never alter high-level Macro strategy solely because low-level Micro implementation details changed.
- **`EM-12` (Conditional Sync & Scoped Push Trigger):**
  - `SB-EM-12.1` (*Scoped Push Branch*): IF pushing named files $\rightarrow$ stage only those paths, commit, and push (`git pull --rebase` on non-fast-forward), ignoring unrelated dirty files.
  - `SB-EM-12.2` (*Full Sync Branch*): IF operator calls for `sync` / `synch` $\rightarrow$ execute full push/pull with rebase and status check.
  - `SB-EM-12.3` (*Asset Preservation*): Preserve all unrelated dirty files; never drop unrequested dirty work.

---

## 2. Single-Ownership Verification Ledger (`WP-23`)

### 2.1 Rules Canonically Owned by `execution-modes.md` (10 Rules)
`execution-modes.md` is the authoritative owner of task adapter protocols and execution workflows:
1. `EM-01` — Whole-File Rewrite Prohibition (root mutation invariant)
2. `EM-02` — Handover Non-Paralysis Invariant (root check-it-now invariant)
3. `EM-03` — Step-by-Step Context & File Iteration Invariant (root anti-bloat invariant)
4. `EM-06` — Conditional Q&A Trigger & Decision Matrix Structure
5. `EM-07` — Conditional Bake-Off Trigger & 4-Phase Comparison Rubric
6. `EM-08` — Conditional Patch Trigger & Mode A block protocol (Mode B worked example)
7. `EM-09` — Conditional Handover Trigger (4D contract & 5-component report)
8. `EM-10` — Conditional Iterative & MMM Trigger (Route ladder & file-producing loop)
9. `EM-11` — Upward Invalidation Rule (layer-specific invalidation)
10. `EM-12` — Conditional Sync & Scoped Push Trigger (scoped push & dirty file preservation)

---

### 2.2 Sibling Rules Referencing `execution-modes.md` Definitions (6 Delegations)
Six rules in `anti-drift-rules.md` and `governance-schemas.md` explicitly delegate to definitions canonically owned by `execution-modes.md`:

| Sibling File | Sibling Rule | Delegated Definition from `execution-modes.md` | Relationship & Scope |
|---|---|---|---|
| `anti-drift-rules.md` | `AD-03` | `EM-01`, `EM-08` | Cites whole-file rewrite prohibition and exact-match patch protocol. |
| `anti-drift-rules.md` | `AD-04` | `EM-03`, `EM-10` | Cites step-by-step context loop and disk externalization. |
| `anti-drift-rules.md` | `AD-06` | `EM-02` | Cites checkable ambiguity resolution ("never defer checkable facts"). |
| `governance-schemas.md` | `GS-02` | `EM-01` | Enforces prohibited whole-file patch rewrites during schema validation. |
| `governance-schemas.md` | `GS-12` | `EM-06` | Validates decision records against the Q&A format owned by `execution-modes.md` §2.1. |
| `governance-schemas.md` | `GS-13` | `EM-07` | Validates bake-offs against the 4-phase rubric owned by `execution-modes.md` §3.1. |

---

### 2.3 Rules Within `execution-modes.md` Delegating to External Canonical Owners (3 Delegations)
`execution-modes.md` delegates 3 rules to external canonical owners in `anti-drift-rules.md` and `governance-schemas.md`:

| Local Rule | Priority Tier | Target Canonical Owner | Owner File | Delegation Scope & Relationship |
|---|:---:|---|---|---|
| `EM-04` | **P0** | `AD-01` | `anti-drift-rules.md` | Target Dominance Invariant. Restates operative imperative for task execution. |
| `EM-05` | **P0** | `AD-02`, `AD-24` | `anti-drift-rules.md` | Two-Strike Pivot Rule & Tracker Mechanics. Restates operative imperative for error recovery. |
| `EM-08` | **P1** | `GS-09..11` | `governance-schemas.md` | AST Patch Intent Specification. *Worked Example Only:* The JSON block in `EM-08` Mode B is an illustrative worked example that delegates the authoritative contract to `governance-schemas.md` §2.2 and `patch-intent-schema.json`. |

---

### 2.4 Mechanical Verification Evidence (`test_canonical_ownership.py`)
Deterministic test suite execution confirms complete structural compliance:
1. **Rule Prefix Integrity:** All 12 rules begin with `EM-`, and no `EM-` rules exist in other files (`test_rule_id_prefix_matches_its_home_file`).
2. **Rule ID Uniqueness:** Zero duplicate IDs exist within `execution-modes.md` (`test_no_duplicate_rule_id_within_a_file`).
3. **Canonical Pointer Resolution:** All external pointers (`AD-01`, `AD-02`, `AD-24`) resolve to live rules in `anti-drift-rules.md` (`TestCanonicalPointerIntegrity`).
4. **Zero Self-Referential Pointers:** `execution-modes.md` contains zero `Canonical: `EM-xx`` references (`test_canonical_pointer_never_targets_its_own_file`).

---

## 3. Redundancy & Stale Terminology Remediation Plan

### 3.1 Cross-Module Redundancy Clusters Involving `execution-modes.md`
The audit identified 4 prominent concept clusters where `execution-modes.md` intersects with other modules:

1. **Whole-File Rewrite Prohibition (`EM-01` [P0] vs `AD-03` [P0], `GS-02` [P0], contract `<surgical>`):**
   - *Current State:* Three separate files declare a P0 invariant forbidding whole-file overwrites.
   - *Assessment:* Fully justified under `WP-23`. An agent modifying code via `execution-modes.md` needs the immediate imperative; an agent monitoring drift via `anti-drift-rules.md` needs the operational boundary; CI tooling checking patches via `governance-schemas.md` needs the gate condition.
2. **Context Bloat & File-Producing Loop (`EM-03` [P0] & `EM-10` [P1] vs `AD-04` [P0], contract `<context>`):**
   - *Current State:* `EM-03` forbids bulk loading; `EM-10` provides the concrete 4-iteration protocol; `AD-04` codifies the operational anti-drift law.
   - *Remediation Plan:* Maintain `EM-10` as the authoritative execution recipe (Route 0/1/2 ladder and `00-master-matrix.md` workflow).
3. **Handover Non-Paralysis / Checkable Ambiguity (`EM-02` [P0] vs `AD-06` [P0], contract `<handover>`):**
   - *Current State:* Both files define a P0 invariant: "never defer checkable facts."
   - *Assessment:* `EM-02` governs handover generation; `AD-06` governs agent reasoning during active execution.
4. **Two-Strike Pivot Rule (`EM-05` [P0] vs `AD-02` [P0], `AD-24` [P2], contract `<stop_repairing>`):**
   - *Current State:* `EM-05` enforces the pivot during task execution; `AD-02` establishes the general law; `AD-24` defines the tracker mechanics.
   - *Assessment:* `EM-05` cleanly delegates per-subsystem tracking mechanics to `AD-24`.

---

### 3.2 Worked Example vs Authoritative Schema in `EM-08` Mode B
- **Defect D9 Analysis:** In historical revisions, inline copies of `patch_intent.v1` in documentation drifted from `patch-intent-schema.json`, silently dropping `maxLength` ceilings on paths and hints.
- **`WP-23` Resolution:** In `execution-modes.md` §4.2, the inline JSON block is explicitly marked as a **worked example**, stating:
  > *"The operative contract is in governance-schemas.md §2.2; the authoritative schema is patch-intent-schema.json. This block is the worked example, not a second copy of the schema (WP-23)."*
- This distinction ensures that developers and autonomous agents have an immediate concrete template to emulate without risking silent schema divergence.

---

### 3.3 Dual `<sync>` Mechanics in `EM-12`
`EM-12` defines two distinct operational branches for Git synchronization:
1. **Scoped Push (`git push <paths>`):** When the operator requests pushing specific files, the agent stages only those requested paths, commits, and pushes (`git pull --rebase` on non-fast-forward), ignoring unrelated dirty files in the workspace.
2. **Full Sync (`sync` / `synch`):** When the operator calls for a general repository sync, the agent performs a bidirectional push-and-pull synchronization, while actively preserving unrelated dirty files in separate commits so unrequested user work is never deleted or stashed away.

---

## 4. Cross-Traceability Matrix to XML `<apex_contract>` and Ultra Contract

### 4.1 100% Contract Traceability of `execution-modes.md`
Remarkably, **100% of rules in `execution-modes.md` (`EM-01` through `EM-12`) are directly codified in `<apex_contract v="1.0">`** ([13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md)) and the upcoming `16-candidate-3A-ultra.md`!

`execution-modes.md` possesses the highest contract density of any Plane 4 module:

| Semantic Contract Tag | Mode | Mapped `EM` Rules | Key Semantic Obligations Codified in Contract |
|---|---|---|---|
| `<surgical>` | Unconditional Stub | `EM-01` | Never regenerate or overwrite a whole existing file. |
| `<editing>` | Gated (`execution-modes.md`) | `EM-01`, `EM-08` | Replace exact lines verbatim; one change per edit; `git mv`/`cp`; open ref for AST patch. |
| `<handover>` | Gated (`execution-modes.md`) | `EM-02`, `EM-09` | Never defer checkable facts; 5-component report (Obs, Logic, Caveats, Conclusion, Verify). |
| `<context>` | Unconditional | `EM-03`, `EM-10` | Load JIT; no bulk reading at start; rank sources; write findings to disk per step. |
| `<target>` | Unconditional | `EM-04` | Optimize for user outcome; no process ceremony substitution. |
| `<stop_repairing>` | Unconditional | `EM-05` | Stop after 2 failed attempts; pivot approach; no sunk-cost claim. |
| `<trade_off>` | Gated (`execution-modes.md`) | `EM-06`, `EM-07` | Q&A decision matrix with raw I/E/R tags; 4-phase comparison bake-off. |
| `<iterative>` | Gated (`execution-modes.md`) | `EM-10`, `EM-11` | Route ladder (0 direct, 1 preflight, 2 MMM file loop); upward invalidation rule. |
| `<sync>` | Gated | `EM-12` | Git commands first; preserve unrelated dirty files; pull with rebase and retry. |

---

### 4.2 Unmapped Rules Ledger: Zero Unmapped Rules
- **Count:** **0 rules unmapped**.
- **Significance:** Every single rule defined in `execution-modes.md` represents an active, load-bearing execution discipline recognized by the core contract. There is zero non-operational overhead in this module.

---

### 4.3 Upstream Empirical Grounding & Research Links
The execution adapters in `execution-modes.md` directly reflect proven empirical research:
- **`EM-01` & `EM-08`:** Grounded in Research Packet [RESULTS-01-gating-efficacy.md](../03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-01-gating-efficacy.md), which demonstrated that exact-match block replacements eliminate 92% of hallucinated whole-file truncations compared to full-file generation.
- **`EM-02` & `EM-09`:** Grounded in [C01-decision-trade-off-discipline/README.md](../01-universal-instruction-research/module-deepening/C01-decision-trade-off-discipline/README.md) and [Snippets.md](../../../../AI-Snippets/Snippets.md), establishing the 5-component forensic completion report and ending "handover paralysis."
- **`EM-06`:** Grounded in operational lore from [Snippets.md](../../../../AI-Snippets/Snippets.md) and [2Dos Ai Instructions.md](../../../../AI-Snippets/Orga/2Dos%20Ai%20Instructions.md), codifying the standardized Q&A Decision Matrix format.
- **`EM-10` & `EM-11`:** Grounded in the Modular Multi-File Methodology (MMM) architecture from [standard.md](../../../standard.md), ensuring that complex tasks materialize intermediate progress files on disk rather than accumulating massive hidden context.

---

## 5. Module Failure Modes & Not-To-Dos (`WP-25`)

In accordance with `WP-25` (*Terminal-Position Operative Content*), this audit concludes with non-negotiable operational boundaries and anti-patterns for agents executing or modifying `execution-modes.md`:

- **Never Overwrite Existing Files With Full-File Rewrites (`EM-01` Violation):** Always modify existing repository files via surgical exact-match replacement blocks or structured AST patch intents (`patch_intent.v1`). Whole-file generation destroys adjacent valid code and obliterates intentional formatting.
- **Never Write a Handover to Escape Checkable Work (`EM-02` Violation):** If a question, file existence, or requirement can be checked right now using available CLI tools or parallel subagents, invoke the tool and resolve it immediately. Never pass checkable ambiguities to future sessions.
- **Never Front-Load Massive Context at Session Start (`EM-03` Violation):** Do not bulk-read entire directories or grep large swaths of the codebase upfront. Build an Input Priority Ledger, load context step-by-step per active stage, and write findings to disk.
- **Never Calculate Synthetic Scores in Decision Matrices (`EM-06` Violation):** Tag options with raw unaggregated estimates `(I<val>/E<val>/R<val>)` on a 1–100 scale. Never compute mathematical composite averages.
- **Never Use Line Numbers in Patch Blocks or Patch Intents (`EM-08` Violation):** Line numbers drift across concurrent edits. Always identify patch targets using exact text context lines or structural AST heading paths.
- **Never Drop Unrelated Dirty Files During Git Synchronization (`EM-12` Violation):** When executing a push or sync, never stash, discard, or overwrite dirty files outside your assigned scope. Preserve all unrequested dirty work safely.
