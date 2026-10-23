---
type: Reference
id: V2-AUDIT-MODULE-04-ANTI-DRIFT-RULES
title: Module Audit 04 — Anti-Drift Laws & Operational Lore Semantic Block & Ownership Audit
description: Comprehensive rule-by-rule semantic block decomposition, WP-23 single-ownership ledger, redundancy purge, and cross-traceability audit for anti-drift-rules.md.
status: current_truth
tags: [module-audit, plane-4, anti-drift-rules, single-owner, semantic-blocks, traceability]
---

# Module Audit 04: Anti-Drift Laws & Operational Lore (`anti-drift-rules.md`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** [13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md) (`<target>`, `<product_first>`, `<scope>`, `<hold_position>`, `<ground>`, `<reuse>`, `<recovery>`, `<stop_repairing>`, `<new_machinery>`, `<detour>`)
> - **Layer 1 (Layered Rule KB):** [rule-01-target.md](rule-01-target.md), [rule-02-product-first.md](rule-02-product-first.md), [rule-03-scope.md](rule-03-scope.md), [rule-05-hold-position.md](rule-05-hold-position.md), [rule-06-ground.md](rule-06-ground.md), [rule-07-reuse.md](rule-07-reuse.md), [rule-09-recovery.md](rule-09-recovery.md), [rule-10-stop-repairing.md](rule-10-stop-repairing.md), [rule-14-new-machinery.md](rule-14-new-machinery.md), [rule-15-detour.md](rule-15-detour.md)
> - **Layer 2 (Audited Canonical Module):** [anti-drift-rules.md](../../specs/anti-drift-rules.md) (`AD-01` through `AD-28`)
> - **Upstream Research & Empirical Lore:** [standard.md](../../specs/standard.md), [RESULTS-05-self-authored-criteria.md](../03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-05-self-authored-criteria.md), [RESULTS-07-over-building.md](../03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-07-over-building.md), [A01-target-outcome-alignment/README.md](../01-universal-instruction-research/module-deepening/A01-target-outcome-alignment/README.md), [A03-reuse-before-invention/README.md](../01-universal-instruction-research/module-deepening/A03-reuse-before-invention/README.md), [Snippets.md](../../../../AI-Snippets/Snippets.md), [2Dos Ai Instructions.md](../../../../AI-Snippets/Orga/2Dos%20Ai%20Instructions.md)

---

## 1. Module Scope, Architectural Role & Governed Rule Inventory

### 1.1 Architectural Domain & Loading Lifecycle
`anti-drift-rules.md` (`GOV-ANTI-DRIFT-v0.2`) is the canonical Plane 4 governance specification codifying the 8 Anti-Drift Laws, the Two-Strike Subsystem Rule, the Sunk-Cost Prohibition, the Operator Challenge Boundary, Task Minimalism, Anti-Overcorrection (Hold Position), and Context Hygiene across Apex OS.

Within the **Five-Plane Information Architecture** ([file-architecture.md](../../specs/file-architecture.md) `FA-03`), `anti-drift-rules.md` acts as the primary operational governor:
- **JIT Activation Trigger:** An autonomous agent or operator loads `anti-drift-rules.md` when evaluating task boundaries, designing technical solutions, diagnosing broken subsystem repair loops, handling operator pushback, or auditing session alignment against requested deliverables.
- **Top-Loaded Invariants:** The module front-loads 13 non-negotiable P0 invariants (`AD-01` through `AD-13`) in the first ~500 tokens, establishing target dominance, the two-strike limit, whole-file rewrite bans, context bloat prevention, the operator challenge boundary, sunk-cost bans, and product-before-infrastructure priority.
- **Expanded Rule Inventory (`AD-01..AD-28`):** While early historical drafting referenced `AD-01..AD-26`, the active canonical module includes **28 passing rules**, incorporating `AD-27` (*Sibling Module Linkage*) and `AD-28` (*Objective Run Outcome Classification*).

---

### 1.2 Comprehensive Governed Rule Inventory

The live `anti-drift-rules.md` defines **28 governed rules** across four functional sections. The table below documents every rule, its priority tier, raw 3-metric significance rating, formal scope, inputs, outputs, halt conditions, and canonical ownership.

| # | Category | Rule ID | Tier & Metrics | Title | Description & Scope | Inputs / Preconditions | Outputs / Behaviors | Error / Halt Behavior | Canonical Owner |
|---|---|---|:---:|---|---|---|---|---|:---:|
| 1 | Target | `AD-01` | `[P0 \| I100/E95/R05]` | TARGET Dominance Invariant | TARGET dominates everything; verify requirements; no-op permission. | Executing any task. | Prioritizes product path; reports no-op if already met. | Halt if meta-ceremony displaces target. | **AD-01 (Owner)** |
| 2 | Recovery | `AD-02` | `[P0 \| I98/E95/R05]` | Two-Strike Subsystem Rule | If 2 iterations fail on a subsystem, stop and change approach. | Subsystem failure. | Caps attempts at 2; forces architecture pivot. | Reject entering 3rd fix attempt. | **AD-02 (Owner)** |
| 3 | Mutation | `AD-03` | `[P0 \| I98/E96/R05]` | Whole-File Rewrite Prohibition | Modify files via surgical patch blocks or verified tool edits. | File modifications. | Prevents full-file wipes; surgical replacements. | Halt on whole-file regeneration. | `EM-01`, `EM-08` |
| 4 | Context | `AD-04` | `[P0 \| I96/E95/R05]` | Step-by-Step Context & File Iteration Invariant | Never front-load massive files; Source Priority Ledger. | Multi-file research/task. | Reads per active step; externalizes findings to disk. | Halt on upfront context bloat. | `EM-03`, `EM-10` |
| 5 | Detour | `AD-05` | `[P0 \| I96/E95/R05]` | Operator Challenge Boundary | Must this be fixed before testing product? If not, defer. | Proposing refactor/detour. | Halts speculative architecture; defers in one line. | Reject speculative unblocking work. | **AD-05 (Owner)** |
| 6 | Ambiguity | `AD-06` | `[P0 \| I96/E95/R05]` | Checkable Ambiguity Resolution | Verify checkable facts immediately; never defer checkable items. | Ambiguity encountered. | Invocates tools immediately; eliminates handoff escapism. | Reject handoffs deferring checkable facts. | `EM-02` |
| 7 | Sunk Cost | `AD-07` | `[P0 \| I95/E95/R05]` | Sunk-Cost Prohibition Invariant | Prior investment gives failing approach zero authority. | Deciding whether to continue. | Abandons dead-end branches without regret. | Reject continuing failing branch on sunk cost. | **AD-07 (Owner)** |
| 8 | Authority | `AD-08` | `[P0 \| I95/E95/R05]` | Substance Over Ceremony Exception Authority | Substantive realization of target overrides mechanical ceilings. | Evaluating constraints. | Authorizes exceeding ceilings for correctness. | Reject mechanical cuts that damage truth. | `WP-01` |
| 9 | Drift | `AD-09` | `[P0 \| I95/E95/R08]` | Stop on Drift Invariant | Halt if work becomes ceremony, wrappers, or meta-docs. | Monitoring ongoing work. | Stops drifting work; redirects to core deliverable. | Halt on self-indulgent ceremony drift. | **AD-09 (Owner)** |
| 10 | Product | `AD-10` | `[P0 \| I95/E94/R08]` | Product Before Infrastructure Invariant | Fix only execution/data-loss blockers before first working slice. | Pre-product development. | Blocks pre-mature test/infra building. | Reject scaffolding before working slice runs. | **AD-10 (Owner)** |
| 11 | Reuse | `AD-11` | `[P0 \| I95/E92/R08]` | Reuse Before Build Invariant | Try existing alternative before building new abstraction. | Facing new problem. | Inspects existing repo tools, skills, libraries. | Reject building new without trying existing. | **AD-11 (Owner)** |
| 12 | Product | `AD-12` | `[P0 \| I94/E92/R08]` | Product Advancement Invariant | Every work unit must run something, teach quality, or advance target. | Task execution. | Defer any work that does not advance product. | Reject busy-work that doesn't advance product. | **AD-12 (Owner)** |
| 13 | Machinery | `AD-13` | `[P0 \| I92/E90/R10]` | Evidence Proportionality Invariant | Do not build more verification machinery than risk justifies. | Designing tests/gates. | Scales verification effort to failure downside. | Reject heavy test harnesses for trivial risks. | **AD-13 (Owner)** |
| 14 | Minimalism | `AD-14` | `[P1 \| I94/E95/R08]` | Gall's Law & Single Flat Artifact | Default to single flat file before nested packages/modules. | System design. | Keeps initial implementation simple and flat. | Flag premature multi-package architectures. | **AD-14 (Owner)** |
| 15 | Hygiene | `AD-15` | `[P1 \| I93/E95/R05]` | Residual Name Eradication | Purge all residual mentions of deleted names from live docs. | Deleting/renaming code. | Eradicates dead names; prevents ghost reasoning. | Flag zombie references in active rules. | **AD-15 (Owner)** |
| 16 | Recovery | `AD-16` | `[P1 \| I93/E95/R07]` | Pre-Existing Red vs Regression Boundary | Halt only if test was green on HEAD and broken by current edits. | Running test suites. | Records pre-existing failures with command; continues. | Halt only on new regressions. | **AD-16 (Owner)** |
| 17 | Primacy | `AD-17` | `[P1 \| I93/E94/R07]` | Minto BLUF Directive | Deliver definitive bottom line up front in sentence one. | Reporting findings. | Eliminates wind-up greetings and preambles. | Flag bury-the-lede narrative openings. | `WP-12` |
| 18 | Scope | `AD-18` | `[P1 \| I92/E93/R08]` | Zero-Speculation Scope Boundary | Out of scope by default unless requested or strictly required. | Defining task scope. | No precautionary guardrails for hypothetical risks. | Reject speculative features or roadmaps. | **AD-18 (Owner)** |
| 19 | Grounding | `AD-19` | `[P1 \| I91/E96/R05]` | Primary Grounding vs Secondary Citation | Ground facts in originating artifact (`path:line`) or tool. | Verifying claims. | Opens primary source; never relies on memory. | Reject ungrounded citations. | **AD-19 (Owner)** |
| 20 | Grounding | `AD-20` | `[P1 \| I90/E94/R06]` | Command-Carrying Claims | Statements of zero/absence must carry reproducible command. | Negative/absence claims. | Attaches command and exact scope to claim. | Reject unverified "none found" claims. | **AD-20 (Owner)** |
| 21 | Path | `AD-21` | `[P1 \| I90/E92/R08]` | Balanced Viable Path | Direct step first before elaborate multi-layer architecture. | Choosing solution path. | Executes simple value-efficient path first. | Reject over-engineered detour solutions. | **AD-21 (Owner)** |
| 22 | Feedback | `AD-22` | `[P2 \| I88/E91/R08]` | Surgical Edits & Anti-Overcorrection (Hold Position) | Update only on evidence, never pushback alone; narrow edits. | Operator feedback. | Resists sycophancy; confines changes to what was challenged. | Reject whole-module rewrites on pushback. | **AD-22 (Owner)** |
| 23 | Asset | `AD-23` | `[P2 \| I87/E92/R08]` | Asset Preservation & Deterministic Moves | Treat code/scripts as assets; move via `git mv`/`cp`. | Managing files. | Preserves existing assets; never regenerates. | Reject destroying working code during moves. | **AD-23 (Owner)** |
| 24 | Recovery | `AD-24` | `[P2 \| I86/E90/R08]` | Two-Strike Subsystem Tracker Mechanics | Track failure counts per distinct subsystem independently. | Multiple subsystems failing. | Success resets count to 0; 2 strikes triggers pivot. | Prevent mixing failure counts across modules. | **AD-24 (Owner)** |
| 25 | Machinery | `AD-25` | `[P2 \| I85/E90/R09]` | Pre-Addition Gate & Machinery Rule | Name requirement/blocker before adding abstraction/gate. | Adding new machinery. | Confirms problem isn't surfaced in ~2 steps of use. | Reject adding machinery without named blocker. | **AD-25 (Owner)** |
| 26 | Sizing | `AD-26` | `[P2 \| I85/E90/R10]` | Universal Instruction Parsimony | Standalone file concise (~30–50 rules max); JIT links. | Managing rule sets. | Routes specialized domains JIT to prevent dilution. | Flag rule-wall bloat. | `WP-18` |
| 27 | Linkage | `AD-27` | `[P2 \| I84/E89/R08]` | Sibling Module Linkage | Coordinate with WP, FA, EM, GS via repository-relative links. | Cross-module referencing. | Relative links ensure resolution across all runners. | Flag broken or absolute links. | **AD-27 (Owner)** |
| 28 | Metrics | `AD-28` | `[P3 \| I68/E82/R10]` | Objective Run Outcome Classification | Classify session close: `product-shipped`, `governance-only`, etc. | Post-mortem session audit. | Checks git log and deliverable state objectively. | Flag unclassified session outcomes. | **AD-28 (Owner)** |

---

### 1.3 Atomic Semantic Block Inventory (`SB-AD-01`..`SB-AD-28`)

Every rule in `anti-drift-rules.md` decomposes into atomic semantic blocks that isolate discrete obligations:

- **`AD-01` (TARGET Dominance Invariant):**
  - `SB-AD-01.1` (*Outcome Dominance*): TARGET dominates everything: optimize for the most balanced, value-efficient path to the user outcome.
  - `SB-AD-01.2` (*Anti-Ceremony Precedence*): Secondary tasks (orchestration, refactoring, meta-docs) must never substitute for the deliverable.
  - `SB-AD-01.3` (*Pre-Completion Positive Verification*): Positively verify each stated requirement against the output before concluding.
  - `SB-AD-01.4` (*No-Op Legitimacy Clause*): When evidence shows no change is needed, report that finding with its proof as the complete deliverable.
- **`AD-02` (Two-Strike Subsystem Rule):**
  - `SB-AD-02.1` (*Two-Strike Limit*): If the same subsystem needs two corrective iterations without advancing the product, stop repairing it.
  - `SB-AD-02.2` (*Architecture Pivot*): Reconsider and replace the approach; never enter an unbounded third attempt.
- **`AD-03` (Whole-File Rewrite Prohibition):**
  - `SB-AD-03.1` (*Surgical Patching*): Modify existing files strictly using surgical exact-match patch blocks or verified tool edits.
  - `SB-AD-03.2` (*Regeneration Ban*): Never regenerate full files via whole-file rewrites (delegates to `EM-01` and `EM-08`).
- **`AD-04` (Step-by-Step Context & File Iteration Invariant):**
  - `SB-AD-04.1` (*Anti-Context-Bloat*): Never front-load massive files or documentation at session start.
  - `SB-AD-04.2` (*Source Priority Ledger*): Manage context step-by-step using an Input Priority Ledger and materialize outputs to disk (delegates to `EM-03` and `EM-10`).
- **`AD-05` (Operator Challenge Boundary):**
  - `SB-AD-05.1` (*Pre-Product Test Filter*): When proposing a detour or refactor, ask: "Does this need to be fixed before we can test the actual product?"
  - `SB-AD-05.2` (*Immediate Deferral*): If the answer is no, defer it immediately in one line.
- **`AD-06` (Checkable Ambiguity Resolution):**
  - `SB-AD-06.1` (*Immediate Tool Invocation*): Verify checkable facts immediately with available tools or parallel subagents.
  - `SB-AD-06.2` (*Anti-Handover Escapism*): Never write a handover or defer to future sessions when tools can resolve it now (delegates to `EM-02`).
- **`AD-07` (Sunk-Cost Prohibition Invariant):**
  - `SB-AD-07.1` (*Zero Authority for Prior Investment*): Prior implementation effort gives an approach zero additional authority.
  - `SB-AD-07.2` (*Dead-End Abandonment*): Abandon failing branches without hesitation or regret.
- **`AD-08` (Substance Over Ceremony Exception Authority):**
  - `SB-AD-08.1` (*Accuracy Dominates Ceilings*): Substantive target realization overrides mechanical ceilings (delegates to `WP-01`).
- **`AD-09` (Stop on Drift Invariant):**
  - `SB-AD-09.1` (*Drift Detection*): Stop on drift: if work becomes ceremony, wrappers, or meta-docs instead of TARGET, halt immediately.
  - `SB-AD-09.2` (*Product Return*): Redirect focus to the direct product path.
- **`AD-10` (Product Before Infrastructure Invariant):**
  - `SB-AD-10.1` (*Vertical Slice Precedence*): Build the working slice before authoring scaffolding or test machinery.
  - `SB-AD-10.2` (*Pre-Slice Blocker Whitelist*): Fix only what blocks execution, corrupts data, invalidates experiments, or causes safety risks.
- **`AD-11` (Reuse Before Build Invariant):**
  - `SB-AD-11.1` (*Existing Alternative Check*): Do not create a new abstraction until a concrete existing alternative has been tested and shown insufficient.
- **`AD-12` (Product Advancement Invariant):**
  - `SB-AD-12.1` (*Tri-Partite Advancement Gate*): Every work unit must run something real, teach quality, or advance the TARGET; otherwise defer.
- **`AD-13` (Evidence Proportionality Invariant):**
  - `SB-AD-13.1` (*Risk-Proportional Machinery*): Do not build more verification machinery or gates than the risk and value of the target justifies.
- **`AD-14` (Gall's Law & Single Flat Artifact):**
  - `SB-AD-14.1` (*Flat Simplicity First*): Complex systems evolve from simple working systems; default to a single flat file before introducing nested packages.
- **`AD-15` (Residual Name Eradication):**
  - `SB-AD-15.1` (*Dead Name Purge*): Purge all residual mentions of deleted component names or old aliases from active documentation.
  - `SB-AD-15.2` (*Ghost Reasoning Prevention*): Mentioning deleted names causes models to hallucinate dead workflows.
- **`AD-16` (Pre-Existing Red vs Regression Boundary):**
  - `SB-AD-16.1` (*Regression Halt Gate*): Treat a test failure as a halt condition only if green on unmodified master HEAD and turned red by current edits.
  - `SB-AD-16.2` (*Pre-Existing Recording*): Record pre-existing failures with reproduction commands and continue product work.
- **`AD-17` (Minto BLUF Directive):**
  - `SB-AD-17.1` (*Sentence-One Conclusion*): Deliver the definitive bottom line up front in sentence one; eliminate conversational wind-up (delegates to `WP-12`).
- **`AD-18` (Zero-Speculation Scope Boundary):**
  - `SB-AD-18.1` (*Out of Scope Default*): Treat anything not requested or strictly required as out of scope by default.
  - `SB-AD-18.2` (*No Precautionary Roadmaps*): Do not add precautionary guardrails for hypothetical risks or unprompted multi-phase plans.
- **`AD-19` (Primary Grounding vs Secondary Citation):**
  - `SB-AD-19.1` (*Primary Source Inspection*): Ground facts by opening originating artifacts (`path:line`) or running tools directly.
  - `SB-AD-19.2` (*Secondary Citation Ban*): Secondary summaries, past audit notes, and model memory are insufficient.
- **`AD-20` (Command-Carrying Claims):**
  - `SB-AD-20.1` (*Reproducibility Command Requirement*): Statements of zero count, absence, or benchmark metrics must carry the reproducible command and scope.
- **`AD-21` (Balanced Viable Path):**
  - `SB-AD-21.1` (*Direct Step First*): When a direct step solves the problem cleanly, execute it before proposing multi-layer architectures.
- **`AD-22` (Surgical Edits & Anti-Overcorrection - Hold Position):**
  - `SB-AD-22.1` (*Evidence-Based Updates Only*): Update conclusions only when new evidence, missed constraints, or concrete flaws are shown—never from pushback alone.
  - `SB-AD-22.2` (*Anti-Sycophancy & Narrow Scope*): Resist sycophancy; confine edits to what was challenged; never wipe out adjacent valid content.
- **`AD-23` (Asset Preservation & Deterministic Moves):**
  - `SB-AD-23.1` (*Assets Preservation*): Treat existing codebases, comments, and scripts as assets to preserve.
  - `SB-AD-23.2` (*Deterministic Filesystem Operations*): Move or copy files strictly via `git mv` or `cp`, never by regenerating file contents.
- **`AD-24` (Two-Strike Subsystem Tracker Mechanics):**
  - `SB-AD-24.1` (*Independent Tracking*): Track failure counts per distinct subsystem independently.
  - `SB-AD-24.2` (*Strike Reset on Success*): A successful execution on a subsystem resets its strike count to zero; two strikes triggers a pivot.
- **`AD-25` (Pre-Addition Gate & Machinery Rule):**
  - `SB-AD-25.1` (*Named Blocker Prerequisite*): Name the exact requirement or blocker before adding an abstraction, config, or verification gate.
  - `SB-AD-25.2` (*Two-Step Heuristic*): Confirm that ordinary use does not surface the issue in ~2 steps; if it does, fix the underlying logic instead.
- **`AD-26` (Universal Instruction Parsimony):**
  - `SB-AD-26.1` (*Parsimonious File Ceilings*): Keep active directives concise (~30–50 max per standalone file); route specialized rules JIT (delegates to `WP-18`).
- **`AD-27` (Sibling Module Linkage):**
  - `SB-AD-27.1` (*Cross-Module Coordination*): Coordinate operational governance with `writing-profile.md`, `file-architecture.md`, `execution-modes.md`, and `governance-schemas.md`.
  - `SB-AD-27.2` (*Portable Relative Links*): Use repository-relative links so references resolve across all runners.
- **`AD-28` (Objective Run Outcome Classification):**
  - `SB-AD-28.1` (*Session Outcome Post-Mortem*): Inspect `git log` and deliverable state at session close to classify outcomes into `product-shipped`, `governance-only`, or `halted-preproduct`.

---

## 2. Single-Ownership Verification Ledger (`WP-23`)

### 2.1 Rules Canonically Owned by `anti-drift-rules.md` (22 Rules)
`anti-drift-rules.md` canonically defines 22 rules that establish the behavioral discipline of Apex OS:
1. `AD-01` — TARGET Dominance Invariant (highest rated rule in suite: `[P0 | I100/E95/R05]`)
2. `AD-02` — Two-Strike Subsystem Rule (two consecutive failures on a subsystem mandates a pivot)
3. `AD-05` — Operator Challenge Boundary (defer detours unless needed before testing product)
4. `AD-07` — Sunk-Cost Prohibition Invariant (zero authority for prior investment)
5. `AD-09` — Stop on Drift Invariant (halt when work becomes ceremony or wrappers)
6. `AD-10` — Product Before Infrastructure Invariant (fix only blockers before first working slice)
7. `AD-11` — Reuse Before Build Invariant (try existing tool before inventing new abstraction)
8. `AD-12` — Product Advancement Invariant (every work unit must advance the target)
9. `AD-13` — Evidence Proportionality Invariant (scale verification machinery to downside risk)
10. `AD-14` — Gall's Law & Single Flat Artifact (default to single flat file before nested modules)
11. `AD-15` — Residual Name Eradication (canonical owner of dead alias purge)
12. `AD-16` — Pre-Existing Red vs Regression Boundary (halt only on new regressions)
13. `AD-18` — Zero-Speculation Scope Boundary (treat unrequested work as out of scope)
14. `AD-19` — Primary Grounding vs Secondary Citation (canonical owner of `path:line` primary inspection)
15. `AD-20` — Command-Carrying Claims (canonical owner of command-carrying absence claims)
16. `AD-21` — Balanced Viable Path (execute direct value-efficient step first)
17. `AD-22` — Surgical Edits & Anti-Overcorrection (Hold Position canonical definition)
18. `AD-23` — Asset Preservation & Deterministic Moves (code as asset; move via `git mv`/`cp`)
19. `AD-24` — Two-Strike Subsystem Tracker Mechanics (independent per-subsystem tracking)
20. `AD-25` — Pre-Addition Gate & Machinery Rule (name blocker before adding abstraction)
21. `AD-27` — Sibling Module Linkage (cross-module coordination via relative links)
22. `AD-28` — Objective Run Outcome Classification (forensic outcome taxonomy)

---

### 2.2 Sibling Rules Referencing `anti-drift-rules.md` Definitions (6 Delegations)
Six rules across `writing-profile.md`, `file-architecture.md`, and `execution-modes.md` explicitly reference definitions canonically owned by `anti-drift-rules.md`:

| Sibling File | Sibling Rule | Delegated Definition from `anti-drift-rules.md` | Relationship & Scope |
|---|---|---|---|
| `writing-profile.md` | `WP-04` | `AD-19` | Cites primary grounding vs secondary citation for technical text. |
| `writing-profile.md` | `WP-08` | `AD-15` | Cites dead alias eradication to prevent ghost reasoning in active docs. |
| `writing-profile.md` | `WP-16` | `AD-20` | Cites command-carrying claims for absence or benchmark metrics. |
| `file-architecture.md` | `FA-09` | `AD-15` | Cites residual name eradication when refactoring or deleting components. |
| `execution-modes.md` | `EM-04` | `AD-01` | Restates TARGET dominance operative imperative for task execution. |
| `execution-modes.md` | `EM-05` | `AD-02`, `AD-24` | Restates two-strike pivot rule and subsystem tracking mechanics for error recovery. |

---

### 2.3 Rules Within `anti-drift-rules.md` Delegating to External Canonical Owners (6 Delegations)
`anti-drift-rules.md` delegates 6 rules to external canonical owners in `execution-modes.md` and `writing-profile.md`:

| Local Rule | Priority Tier | Target Canonical Owner | Owner File | Delegation Scope & Relationship |
|---|:---:|---|---|---|
| `AD-03` | **P0** | `EM-01`, `EM-08` | `execution-modes.md` | Whole-File Rewrite Prohibition Protocol. Restates surgical patch imperative. |
| `AD-04` | **P0** | `EM-03`, `EM-10` | `execution-modes.md` | Step-by-Step Context & File Iteration Loop. Restates anti-context-bloat loop. |
| `AD-06` | **P0** | `EM-02` | `execution-modes.md` | Checkable Ambiguity Resolution. Restates "never defer checkable facts" imperative. |
| `AD-08` | **P0** | `WP-01` | `writing-profile.md` | Substance Over Ceremony Exception Authority. Restates operative authority. |
| `AD-17` | **P1** | `WP-12` | `writing-profile.md` | Minto BLUF Directive. Restates sentence-one conclusion directive for reporting. |
| `AD-26` | **P2** | `WP-18` | `writing-profile.md` | Universal Instruction Parsimony. Cites ~30–50 directive ceiling. |

---

### 2.4 Mechanical Verification Evidence (`test_canonical_ownership.py`)
Deterministic verification via `test_canonical_ownership.py` confirms 100% adherence to single-ownership discipline:
1. **Rule Prefix Integrity:** All 28 rules begin with `AD-`, and no `AD-` rules exist in any other file (`test_rule_id_prefix_matches_its_home_file`).
2. **Rule ID Uniqueness:** Zero duplicate IDs exist within `anti-drift-rules.md` (`test_no_duplicate_rule_id_within_a_file`).
3. **Canonical Pointer Resolution:** All external pointers (`EM-01`/`EM-08`, `EM-03`/`EM-10`, `EM-02`, `WP-01`, `WP-12`, `WP-18`) resolve to active rules in the suite (`TestCanonicalPointerIntegrity`).
4. **Zero Self-Referential Pointers:** `anti-drift-rules.md` contains zero `Canonical: `AD-xx`` references (`test_canonical_pointer_never_targets_its_own_file`).

---

## 3. Redundancy & Stale Terminology Remediation Plan

### 3.1 Cross-Module Redundancy Clusters Involving `anti-drift-rules.md`
The audit identified 6 prominent concept clusters where `anti-drift-rules.md` intersects with other modules:

1. **TARGET Dominance (`AD-01` [P0] vs `EM-04` [P0], router headers, contract `<target>`):**
   - *Current State:* `AD-01` is the authoritative root definition (`[P0 | I100/E95/R05]`). `EM-04` restates the operative imperative during task execution.
   - *Assessment:* Fully compliant with `WP-23`.
2. **Two-Strike Subsystem Rule (`AD-02` [P0], `AD-24` [P2] vs `EM-05` [P0], contract `<stop_repairing>`):**
   - *Current State:* `AD-02` sets the general law; `AD-24` establishes per-subsystem counter mechanics; `EM-05` triggers the halt during runtime.
   - *Assessment:* Clean architectural separation.
3. **Residual Name Eradication (`AD-15` [P1] vs `WP-08` [P0], `FA-09` [P1]):**
   - *Deliberate Tier Inversion:* In `writing-profile.md`, `WP-08` is elevated to **P0** because referencing dead names in active specifications directly causes model hallucinations (a critical failure mode). In general governance, `AD-15` and `FA-09` operate as **P1** core hygiene methods.
4. **Primary Grounding & Verification (`AD-19` [P1], `AD-20` [P1] vs `WP-04` [P0], `WP-16` [P1]):**
   - *Deliberate Tier Inversion:* In technical writing, unanchored claims directly invalidate documentation (P0); in general operational lore, primary grounding is a core method (P1).
5. **Operator Challenge Boundary & Detours (`AD-05` [P0], `AD-10` [P0], `AD-12` [P0] vs contract `<detour>`):**
   - *Current State:* `AD-05` asks "Must this be fixed before testing the product?"; `AD-10` enforces product before infrastructure; `AD-12` enforces product advancement.
   - *Remediation Plan:* In future contract revisions, these three invariants can be cited collectively as the "Anti-Detour Triad."
6. **Hold Position & Anti-Sycophancy (`AD-22` [P2] vs contract `<hold_position>`):**
   - *Current State:* `AD-22` fuses anti-sycophancy (*"Update only on new evidence, never pushback alone"*) with narrow correction discipline (*"Confine edits to what was challenged"*).
   - *Assessment:* High-leverage behavioral guard that directly counters RLHF sycophancy.

---

### 3.2 Stale Terminology & Legacy Rule Scope (`AD-01..AD-26` vs `AD-01..AD-28`)
- Early design specifications and task prompts referenced `AD-01..AD-26`.
- The live canonical file defines **28 rules** (`AD-01` through `AD-28`).
- The two additional rules are:
  - `AD-27 [P2 | I84/E89/R08] Sibling Module Linkage`: Coordinates operational governance with sibling modules via repository-relative links.
  - `AD-28 [P3 | I68/E82/R10] Objective Run Outcome Classification`: Inspects git logs and deliverables at session close to classify runs into `product-shipped`, `governance-only`, or `halted-preproduct`.
- *Verification:* Both `AD-27` and `AD-28` are fully functional, passing members of the test suite and represent legitimate operational additions.

---

## 4. Cross-Traceability Matrix to XML `<apex_contract>` and Ultra Contract

### 4.1 Upward Mapping to Contract Tags
Every anti-drift rule relevant to agent execution maps directly to tags in `<apex_contract v="1.0">` ([13-candidate-3A-xml.md](../../candidates/13-candidate-3A-xml.md)) and the upcoming `16-candidate-3A-ultra.md`:

| Semantic Contract Tag | Mode | Mapped `AD` Rules | Key Semantic Obligations Codified in Contract |
|---|---|---|---|
| `<target>` | Unconditional | `AD-01` | Deliver result; positive requirement check; anti-self-authored criteria; no-op permission. |
| `<product_first>` | Unconditional | `AD-10`, `AD-09`, `AD-12` | Build working thing before machinery; fix only blockers before first working slice; product > script. |
| `<scope>` | Unconditional | `AD-18`, `AD-05` | Do authorized task; report adjacent work; analyzing does not authorize implementing. |
| `<hold_position>` | Unconditional | `AD-22` | Do not reverse on pushback without evidence; treat narrow correction as narrow; state disagreement. |
| `<ground>` | Unconditional | `AD-19`, `AD-20`, `AD-06` | Verify against artifact (`path:line`); command with absence claims; check now. |
| `<reuse>` | Unconditional | `AD-11`, `AD-14` | Check existing scripts/tools/skills; modular composition; Gall's law flat artifact. |
| `<context>` | Unconditional | `AD-04` | Load JIT; no bulk reading at start; rank sources; write findings to disk per step. |
| `<recovery>` | Unconditional | `AD-07`, `AD-16`, `AD-21` | Narrow safe alternative preserving intent; halt only on genuine target/safety blockers. |
| `<stop_repairing>` | Unconditional | `AD-02`, `AD-07`, `AD-24` | Stop after 2 failed attempts; pivot approach; no sunk-cost claim; per-subsystem counter. |
| `<current_truth>` | Unconditional | `AD-15` | State active truth only; purge retired component names. |
| `<surgical>` | Unconditional Stub | `AD-03` | Never regenerate or overwrite a whole existing file. |
| `<editing>` | Gated | `AD-23` | Code as asset; move via `git mv`/`cp`. |
| `<new_machinery>` | Gated | `AD-25`, `AD-10`, `AD-13` | Name requirement/blocker before adding machinery; risk proportionality. |
| `<detour>` | Gated | `AD-05`, `AD-10`, `AD-12` | Ask if needed before testing product; defer in one line if not. |
| `<pointers>` | Terminal Guard | `AD-26` | Instruction parsimony (~30–50 directives max); JIT links. |

---

### 4.2 Analysis of the 3 "Unmapped" Rules
Three rules in `anti-drift-rules.md` are not explicitly cited in the Layer 0 contract block:
1. `AD-08` (Substance Over Ceremony pointer to `WP-01`)
2. `AD-27` (Sibling Module Linkage)
3. `AD-28` (Objective Run Outcome Classification)

**Inclusion Rationale for Plane 4:**
- `AD-08` is a canonical pointer maintaining standalone JIT self-sufficiency for `anti-drift-rules.md` (`WP-23`).
- `AD-27` provides repository-level linking instructions for cross-module coordination.
- `AD-28` governs post-session forensics and auditing (`product-shipped` vs `governance-only`), which executes after an agent session concludes rather than during active task execution.

---

### 4.3 Upstream Empirical Grounding & Research Links
The rules in `anti-drift-rules.md` codify critical empirical research and battle-proven operational lore:
- **`AD-01`:** Grounded in Research Packet [RESULTS-05-self-authored-criteria.md](../03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-05-self-authored-criteria.md) (SpecBench positive requirement verification) and [A01-target-outcome-alignment/README.md](../01-universal-instruction-research/module-deepening/A01-target-outcome-alignment/README.md).
- **`AD-02` & `AD-07`:** Grounded in operational lore from [2Dos Ai Instructions.md](../../../../AI-Snippets/Orga/2Dos%20Ai%20Instructions.md) and [Snippets.md](../../../../AI-Snippets/Snippets.md), codifying the two-strike pivot rule and the absolute ban on sunk-cost rationalizations.
- **`AD-10`, `AD-12` & `AD-25`:** Grounded in Research Packet [RESULTS-07-over-building.md](../03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-07-over-building.md), which demonstrated that coding agents spend 42% of total session tokens authoring unused test frameworks and configuration wrappers before running basic business logic.
- **`AD-11` & `AD-14`:** Grounded in [A03-reuse-before-invention/README.md](../01-universal-instruction-research/module-deepening/A03-reuse-before-invention/README.md) and Gall's Law, establishing that robust systems must grow from working simple systems.
- **`AD-22`:** Grounded in research on LLM sycophancy and overcorrection, establishing the "Hold Position" discipline where agents refuse to reverse valid technical conclusions without empirical counter-evidence.

---

## 5. Module Failure Modes & Not-To-Dos (`WP-25`)

In accordance with `WP-25` (*Terminal-Position Operative Content*), this audit concludes with non-negotiable operational boundaries and anti-patterns for agents executing or modifying `anti-drift-rules.md`:

- **Never Enter a Third Repair Attempt on a Failing Subsystem (`AD-02` Violation):** If two consecutive fix attempts fail to advance the product, halt immediately. Never justify a third attempt by claiming "this time the syntax is right." Reconsider the architecture and select an alternative path.
- **Never Justify a Failing Path Via Sunk Cost (`AD-07` Violation):** Hours invested or thousands of lines written give an approach zero authority to continue once shown deficient. Abandon dead-end branches without hesitation.
- **Never Substitute Self-Verifying Scripts for Product Deliverables (`AD-01` Violation):** Do not write scripts that merely check for the existence of your own self-authored strings or mock files and declare victory based on a green exit code. Verification must validate real user requirements.
- **Never Overcorrect on Operator Feedback (`AD-22` Violation):** When the operator corrects a specific parameter or challenges an assumption, do not swing to an opposite extreme or delete valid adjacent structures. Treat narrow corrections as narrow, and update conclusions only when supported by evidence.
- **Never Add Machinery Without Naming the Requirement or Blocker (`AD-25` Violation):** Before adding any wrapper, config, abstraction, or verification gate, explicitly state the exact requirement or blocker that necessitates it.
- **Never Regenerate Files During Filesystem Moves (`AD-23` Violation):** Always move or copy existing scripts, tests, and documentation using deterministic commands (`git mv`, `cp`). Full-file regeneration during moves inevitably introduces silent regressions.
