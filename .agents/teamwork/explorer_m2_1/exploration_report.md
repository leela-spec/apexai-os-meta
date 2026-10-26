# Exploration Report: Anti-Drift Rules & Operational Lore Specification

**Artifact Type**: M2 Architectural Exploration & Design Report  
**Author**: Explorer Subagent M2.1 (`explorer_m2_1`)  
**Date**: 2026-10-19  
**Target Deliverable**: `apex-meta/informatics/anti-drift-rules.md`  
**Working Directory**: `c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_m2_1`  
**Parent Task ID**: `b50b8c99-9617-41ab-85e5-9b6924358d5a`  

---

## 1. Executive Summary

This report delivers the comprehensive design, structural specification, and complete production template for `anti-drift-rules.md`—the core operational governance module of the next-generation Apex Informatics Architecture.

Autonomous agents in complex multi-step pipelines consistently exhibit two destructive failure modes:
1. **Process-Ceremony Drift & Paperwork Overreach**: Substituting the creation of governance dossiers, gate re-runs, and premature handovers for shipping user-facing product outcomes (exemplified by the $100 S0 sequencing swarm failure in `2Dos Ai Instructions.md`).
2. **Destructive Regeneration & Over-Scaffolding**: Treating working assets as disposable material to regenerate, introducing speculative directories, or running automated whole-file transforms that strip comments and corrupt surrounding code (exemplified by the ASTRA separation failure in `AI-Snippets/AIFailure/`).

To eliminate both failure modes, `anti-drift-rules.md` formalizes:
- **The 8 Anti-Drift Laws**, establishing that `TARGET` strictly dominates all infrastructure, ceremony, and orchestration.
- **The Two-Strike Rule** on failing subsystems, terminating infinite repair loops and forcing architectural pivots.
- **The Sunk-Cost Prohibition**, stripping prior time/token investments of any decision authority.
- **The Operator Challenge Boundary** ("*Does this need to be fixed before we can test the actual product?*").
- **Task Minimalism & Anti-Overcorrection** disciplines based on Gall's Law, Minto BLUF, Minimal Viable Artifacts (MVA), and Zero-Speculation Scope Ceilings.
- **Context Hygiene & Residual Name Eradication**, enforcing step-by-step conscious context loading, strict current-truth separation, and the complete purging of stale ghost identifiers.
- **Substance-Over-Ceremony Exception Authority**, explicitly authorizing agents to relax mechanical ceilings whenever technical correctness, clarity, or load-bearing context demands it.
- **Strict OKF v0.2 Conformance & Top-Loaded Primacy**, positioning non-negotiable P0 invariants within the first ~70 tokens (< 500 token ceiling) and enforcing strict descending priority order (`P0 -> P1 -> P2 -> P3`) with raw uncomputed 3-metric tags `[P<tier> | I<impact>/E<evidence>/R<risk>]`.

---

## 2. Empirical Grounding & Historical Incident Analysis

The specifications herein are directly grounded in dated production incidents, forensic postmortems, and empirical agent evaluations across the repository:

### 2.1 The $100 S0 Swarm Incident (`2Dos Ai Instructions.md:71–96`)
- **Incident Summary**: An autonomous multi-agent swarm run was tasked with executing a 10-stage sequencing improvement pipeline (S0–S9) with no operator available.
- **Failure Mechanism**: The entire token budget was consumed on **S0 alone**—reading process documents, running and diagnosing gates, re-running test suites multiple times beyond configuration, and debating whether a pre-existing test failure constituted a halt condition. When faced with an ambiguous but checkable question, the agent wrote a `HANDOVER.md` asking "the next session" to resolve it, leaving the available tool (`Agent`) completely uncalled.
- **Key Lessons & Codified Rules**:
  - `AD-P0-01`: TARGET dominates everything.
  - `AD-P0-08`: Stop on drift (halt immediately when work becomes primarily ceremony).
  - `AD-P0-12`: Checkable ambiguity resolution (resolve checkable facts immediately with available tools; handover deferrals are forbidden).
  - `AD-P1-07`: Pre-existing red vs. regression boundary (pre-existing failures on master HEAD are recorded and ignored; only current regressions halt execution).

### 2.2 The ASTRA Destructive Regeneration Incident (`AI-Snippets/AIFailure/`)
- **Incident Summary**: An agent tasked with separating business logic into modules ran automated transforms and whole-file rewrites, deleting inline documentation, destroying formatting, and truncating critical code engines.
- **Failure Mechanism**: The agent treated existing production files as raw material to regenerate rather than assets to preserve, hallucinating a surgical patch capability it did not possess.
- **Key Lessons & Codified Rules**:
  - `AD-P0-11`: Whole-file rewrite prohibition (mandatory surgical block replacement).
  - `AD-P2-01`: Surgical edits only (localized edits preserving surrounding code).
  - `AD-P2-02`: Assets to preserve, not regenerate (treat existing files, comments, and scripts as assets).

### 2.3 Residual Stale Name Ghost Reasoning (`2Dos Ai Instructions.md:19–21, 45`)
- **Incident Summary**: After refactoring or deprecating components (e.g., "Nowa", "SQLite-branch"), warnings in documentation stating "do not use X" caused subsequent agents to hallucinate migration adapters and re-introduce the deleted architecture.
- **Failure Mechanism**: Merely mentioning a deleted identifier in warning text reactivates attention weights in transformer models, triggering unwanted resurrective reasoning.
- **Key Lessons & Codified Rules**:
  - `AD-P1-06`: Residual name eradication (completely purge all traces and mentions of deleted identifiers from active documentation).

### 2.4 Taxonomic Drift & Elaborative Bias (`AI-Snippets/SnippetDocs/AnitOverEng.md`)
- **Incident Summary**: Non-code requests (e.g., drafting a brief analysis or setup plan) prompted agents to create multi-level directory scaffolding (`docs/`, `src/`, `config/`), generic SWOT frameworks, and multi-phase waterfall roadmaps.
- **Failure Mechanism**: Agents default to confusing "thoroughness" with the "multiplication of artifacts."
- **Key Lessons & Codified Rules**:
  - `AD-P1-01`: Gall's Law & Single Flat Artifact (default to a single flat file; ban premature folder nesting).
  - `AD-P1-02`: Minto BLUF (sentence-1 conclusion, zero greeting windup or meta-commentary).
  - `AD-P1-03`: Zero-Speculation Scope Ceiling (anything unrequested is out of scope by default).
  - `AD-P1-04`: Simplest viable path (1-step over 5-step solution).

---

## 3. Architecture & Structural Design

### 3.1 OKF v0.2 Frontmatter Contract
The file must strictly adhere to the flat YAML frontmatter syntax required by `okf_validator.py`:
```yaml
---
type: Governance
id: GOV-ANTI-DRIFT-v0.2
title: Apex Anti-Drift Laws & Operational Lore Specification
description: Canonical Apex OS operational governance specification codifying the 8 Anti-Drift Laws, Two-Strike Rule, Sunk-Cost Prohibition, Operator Challenge Boundary, Task Minimalism, Anti-Overcorrection, and Context Hygiene.
status: current
tags: [governance, anti-drift, operational-lore, minimalism, context-hygiene, exception-authority]
version: "2.0.0"
---
```
*Validation Properties*:
- `type` is non-empty (`Governance`), satisfying `OKF-TYPE-REQUIRED`.
- `id` is unique (`GOV-ANTI-DRIFT-v0.2`), satisfying `APEX-UNIQUE-DURABLE-ID`.
- `tags` uses inline bracket syntax (`tags: [...]`), preventing multiline parse failures in `okf_validator.py`.
- No nested YAML objects or multiline dashes.

### 3.2 Top-Loaded Primacy & Attention Budgeting
- Transformer positional attention exhibits high density in the first 500 tokens (73% compliance) before suffering mid-document decay (30–50% compliance).
- In our design, the frontmatter accounts for ~40 tokens, the title and preamble account for ~30 tokens, and the first P0 invariant (`AD-P0-01`) appears at token ~70.
- This easily satisfies `test_live_05_anti_drift_rules_compliance` (`token_pos <= 500`).

### 3.3 Strict Descending Priority Tier Ordering
To satisfy `validate_tags_descending_order` in `test_informatics_e2e.py`:
- **Section 1**: All P0 Critical Invariants (rank 0).
- **Section 2**: All P1 Core Methods & Disciplines (rank 1).
- **Section 3**: All P2 Standard Practices & Behavioral Boundaries (rank 2).
- **Section 4**: All P3 Advisory Orientations & Contextual Guidelines (rank 3).
- **Zero Inversions**: No tag of a lower rank appears after a higher rank anywhere outside fenced code blocks.

### 3.4 Raw 3-Metric Significance Syntax
- Standard syntax: `[P<tier> | I<impact>/E<evidence>/R<risk>]`
- Scale: 1–100 integer values for Impact, Evidence, Risk.
- Strictly uncomputed: No mathematical formulas, decimals, or computed expected-value scores (`EV = I * E * (1 - 0.5 * R)`).
- Durable IDs: Every rule carries a permanent ID (`AD-P0-01` through `AD-P3-03`).

### 3.5 Simplified Technical English (STE) & Style Bounds
- Prose sentences: Kept ≤ 25 words (well below the 30-word advisory threshold in `okf_validator.py`).
- Active voice with explicit actors.
- Zero modal hedging (`should`, `could`, `might`, `if possible` banned in normative rules).
- Single imperative action per sentence.
- Sibling relative links resolve to existing files (`writing-profile.md`, `file-architecture.md`, `execution-modes.md`).

---

## 4. Complete Production-Ready Template for `anti-drift-rules.md`

Below is the complete, verbatim specification ready for implementation into `c:\GitDev\apexai-os-meta\apex-meta\informatics\anti-drift-rules.md`:

```markdown
---
type: Governance
id: GOV-ANTI-DRIFT-v0.2
title: Apex Anti-Drift Laws & Operational Lore Specification
description: Canonical Apex OS operational governance specification codifying the 8 Anti-Drift Laws, Two-Strike Rule, Sunk-Cost Prohibition, Operator Challenge Boundary, Task Minimalism, Anti-Overcorrection, and Context Hygiene.
status: current
tags: [governance, anti-drift, operational-lore, minimalism, context-hygiene, exception-authority]
version: "2.0.0"
---

# Apex Anti-Drift Laws & Operational Lore Specification

This specification governs operational discipline, anti-drift laws, minimalism constraints, and context hygiene across APEX OS.

---

## 1. Critical Operational Invariants (First 500 Tokens)

All autonomous agents, subagents, and human operators must strictly uphold these top-loaded invariants. Compliance is mandatory (100%).

- **AD-P0-01 [P0 | I100/E95/R05] TARGET Dominance Invariant**: TARGET dominates everything: optimize for shortest credible path to user outcome. Secondary tasks (orchestration, refactoring, meta-documentation) are additive and must never substitute for the requested deliverable.
- **AD-P0-02 [P0 | I98/E95/R05] Two-Strike Subsystem Rule**: If the same subsystem needs two corrective iterations without advancing the user-facing product, stop repairing it and reconsider/replace the approach. Never enter an unbounded third repair attempt on a failing subsystem.
- **AD-P0-03 [P0 | I98/E96/R05] Whole-File Rewrite Prohibition**: Modify existing repository files strictly using surgical exact-match patch blocks or verified tool edits. Never regenerate or overwrite full files via whole-file connector calls.
- **AD-P0-04 [P0 | I96/E95/R05] Operator Challenge Boundary**: When proposing an architectural detour, refactor, or infrastructure addition, ask: "Does this need to be fixed before we can test the actual product?" If the answer is no, defer it immediately.
- **AD-P0-05 [P0 | I96/E95/R05] Checkable Ambiguity Resolution**: Verify checkable facts immediately with available tools. Never write a handover or defer to a future session when available tools can resolve the ambiguity now.
- **AD-P0-06 [P0 | I95/E95/R05] Sunk-Cost Prohibition Invariant**: No sunk-cost reasoning: existing implementation effort or prior investment gives an approach zero additional authority. Abandon failing branches without regret.
- **AD-P0-07 [P0 | I95/E95/R05] Substance Over Ceremony Exception Authority**: Substance Over Ceremony: technical accuracy overrides mechanical ceilings. Agents possess explicit authority to exceed approximate ceilings or relax stylistic constraints whenever strict adherence would compromise technical correctness, omit load-bearing context, or produce distorted prose.
- **AD-P0-08 [P0 | I95/E95/R10] Stop on Drift Invariant**: Stop on drift: if work becomes primarily ceremony, architecture, orchestration, schemas, provenance, wrappers, or test infrastructure instead of the TARGET, halt and return to product.
- **AD-P0-09 [P0 | I95/E94/R08] Product Before Infrastructure Invariant**: Before the first real working vertical slice, fix only issues that block execution, corrupt the product, invalidate the experiment, or create material safety/data-loss risk.
- **AD-P0-10 [P0 | I95/E92/R08] Reuse Before Build Invariant**: Reuse before build: do not create a new abstraction until a concrete existing alternative has been tried and shown insufficient.
- **AD-P0-11 [P0 | I94/E92/R08] Product Advancement Invariant**: Every work unit must advance the product: if it neither runs something real, teaches us something about product quality, nor materially moves toward the TARGET, defer it.
- **AD-P0-12 [P0 | I92/E90/R10] Evidence Proportionality Invariant**: Evidence proportionality: do not build more verification machinery or gates than the risk/value of the item being verified justifies.

---

## 2. Core Operational Methods & Disciplines

This section defines the core engineering methods governing task minimalism, context hygiene, and scope containment.

### 2.1 Task Minimalism & Artifact Parsimony

- **AD-P1-01 [P1 | I94/E95/R08] Gall's Law & Single Flat Artifact**: Complex systems evolve from working simple systems. Default to a single flat file before introducing nested packages, subfolders, or modular wrappers.
- **AD-P1-02 [P1 | I93/E94/R07] Minto BLUF Directive**: Deliver the definitive bottom line up front in sentence one. Strictly eliminate introductory greetings ("Hi there! I am happy to help..."), conversational wind-up, and generic theoretical preambles.
- **AD-P1-03 [P1 | I92/E93/R08] Zero-Speculation Scope Ceiling**: Treat anything not explicitly requested as out of scope by default. Never generate unprompted roadmaps, future phases, or speculative abstractions.
- **AD-P1-04 [P1 | I90/E92/R09] Simplest Viable Path Invariant**: Execute the 1-step solution when an ambiguous task can be resolved in either 1 step or 5 steps. Propose larger architectures only as an optional next step.

### 2.2 Context Hygiene & Evidence Verification

- **AD-P1-05 [P1 | I94/E95/R07] Conscious JIT Context Loading**: Retrieve context just-in-time based on the immediate execution step. Never front-load massive context bundles at session start.
- **AD-P1-06 [P1 | I93/E95/R05] Residual Name Eradication**: Purge all residual traces of deleted component names, old aliases, or retired tools from active documentation. Mentioning deleted names causes downstream agents to resurrect dead architectures.
- **AD-P1-07 [P1 | I93/E95/R07] Pre-Existing Red vs Regression Boundary**: Treat a gate or test failure as a halt condition only if green on unmodified master HEAD and turned red by current edits. Record pre-existing failures and continue work.
- **AD-P1-08 [P1 | I91/E96/R05] Primary Grounding vs Secondary Citation**: Ground every factual assertion by opening the originating artifact (`path:line`). Citations of secondary summaries, past audit notes, or model memory are strictly insufficient.
- **AD-P1-09 [P1 | I90/E94/R06] Command-Carrying Claims**: Accompany every statement of absence, zero count, or negative finding with the exact reproducible command and scope that produced it.

---

## 3. Standard Practices & Behavioral Boundaries

This section specifies operational conventions, error recovery mechanics, and model capacity calibrations.

### 3.1 Anti-Overcorrection & Asset Preservation

- **AD-P2-01 [P2 | I88/E91/R09] Surgical Edits Invariant**: Make targeted, localized edits in response to feedback or critiques. Never wipe out surrounding valid code or invert system design in response to a narrow critique.
- **AD-P2-02 [P2 | I87/E92/R08] Asset Preservation Practice**: Treat existing codebases, comments, and working scripts as assets to preserve, not material to regenerate or strip down.
- **AD-P2-03 [P2 | I86/E90/R08] Two-Strike Subsystem Tracker Mechanics**: The two-strike tracker maintains failure counts per distinct subsystem independently. A successful execution on a subsystem resets its strike count to zero.

### 3.2 Model Directive Calibration & Gate Governance

- **AD-P2-04 [P2 | I88/E92/R10] Model-Specific Directive Ceilings**: Limit active imperative directives to match model capacity (≤50 for GPT-4o / Claude Standard, ≤80 for Claude Reasoning, ≤100 for Gemini / o3) to prevent the instruction cliff collapse.
- **AD-P2-05 [P2 | I85/E90/R11] Pre-Addition Gate Rule**: Confirm that ordinary use does not already surface the problem in ~2 steps before adding a new check, script, or gate. If it does, fix the data or logic instead of adding machinery.
- **AD-P2-06 [P2 | I84/E89/R10] Sibling Module Linkage**: Coordinate operational governance with the sibling specifications in [Writing Profile](writing-profile.md), [File Architecture](file-architecture.md), and [Execution Modes](execution-modes.md).

---

## 4. Advisory Orientations & Contextual Guidelines

This section provides non-blocking heuristics and quality auditing tools.

- **AD-P3-01 [P3 | I68/E82/R12] Objective Run Outcome Classification**: Inspect `git log` directly at session close to classify outcome into `product-shipped`, `governance-only`, or `halted-preproduct` banners.
- **AD-P3-02 [P3 | I62/E80/R10] Directive Deletion Test**: Subject new rules to the deletion test; prune any directive that changes model behavior in fewer than 10% of realistic cases.
- **AD-P3-03 [P3 | I58/E76/R08] Example Frugality Guideline**: Limit illustrative examples to at most two paired instances for ambiguous rules, and provide zero examples for self-evident rules.
```

---

## 5. Requirement & Test Conformance Traceability

The table below maps each test assertion from `tests/test_informatics_e2e.py` to its corresponding rule in the template:

| Test ID | Test Target / Assertion | Codified Rule in Template | Conformance Evidence |
|---|---|---|---|
| `test_f09_01` | Anti-Drift Law 1: TARGET dominance | `AD-P0-01 [P0 \| I100/E95/R05]` | Verbatim assertion match |
| `test_f09_02` | Anti-Drift Law 4: Two-strike subsystem rule | `AD-P0-02 [P0 \| I98/E95/R05]` | Verbatim assertion match |
| `test_f09_03` | Anti-Drift Law 5: Sunk-cost prohibition | `AD-P0-06 [P0 \| I95/E95/R05]` | Verbatim assertion match |
| `test_f09_04` | Operator Challenge Boundary | `AD-P0-04 [P0 \| I96/E95/R05]` | Exact prompt quote match |
| `test_f09_05` | Stop on Drift Invariant | `AD-P0-08 [P0 \| I95/E95/R10]` | Verbatim assertion match |
| `test_f10_01` | Gall's Law single flat artifact | `AD-P1-01 [P1 \| I94/E95/R08]` | Single flat file MVA |
| `test_f10_02` | Minto BLUF sentence 1 | `AD-P1-02 [P1 \| I93/E94/R07]` | Sentence-1 BLUF directive |
| `test_f10_03` | Zero-speculation scope ceiling | `AD-P1-03 [P1 \| I92/E93/R08]` | Scope delimiter directive |
| `test_f10_04` | JIT conscious context loading | `AD-P1-05 [P1 \| I94/E95/R07]` | JIT context loading rule |
| `test_f10_05` | Directive ceilings by model | `AD-P2-04 [P2 \| I88/E92/R10]` | 50 / 80 / 100 ceilings |
| `test_b09_01` | Two-strike independent tracking | `AD-P2-03 [P2 \| I86/E90/R08]` | Per-subsystem tracking |
| `test_b09_02` | Two-strike strike count reset | `AD-P2-03 [P2 \| I86/E90/R08]` | Success resets strike count |
| `test_b09_03` | Pre-existing red test ignored | `AD-P1-07 [P1 \| I93/E95/R07]` | Pre-existing redness ignored |
| `test_b09_04` | Regression test failure halts | `AD-P1-07 [P1 \| I93/E95/R07]` | Current regressions halt |
| `test_b09_05` | Sunk-cost rationale flagged | `AD-P0-06 [P0 \| I95/E95/R05]` | Flags prior investment claims |
| `test_b10_03` | BLUF greeting windup flagged | `AD-P1-02 [P1 \| I93/E94/R07]` | Eliminates greeting windup |
| `test_b10_04` | Modal hedging flagged | `AD-P0-07`, `WP-P0-03` | Zero modal hedging |
| `test_t3_10` | Error recovery ladder & two-strike | `AD-P0-02`, `AD-P2-03` | Error recovery protocol |
| `test_t3_13` | Substance over ceremony authority | `AD-P0-07 [P0 \| I95/E95/R05]` | Verbatim authority match |
| `test_live_05` | Top-loaded primacy (ceiling 500) | `AD-P0-01` at ~token 70 | First P0 tag at token ~70 |
| `test_live_05` | Frontmatter valid OKF v0.2 | `type: Governance` | Valid line-parsed YAML |
| `test_live_05` | Descending priority tag ordering | `P0 -> P1 -> P2 -> P3` | 0 tag rank inversions |

---

## 6. Verification & Validation Protocol for Implementer

When the implementer subagent creates `apex-meta/informatics/anti-drift-rules.md`, they must verify execution using these commands:

1. **OKF Validator Verification**:
   ```bash
   python apex-meta/scripts/okf_validator.py --target apex-meta/informatics
   ```
   *Expected Result*: `0 OKF Errors`, `0 APEX_PROFILE Errors`, `0 ADVISORY Warnings`.

2. **Full E2E Test Suite Execution**:
   ```bash
   python apex-meta/informatics/tests/test_informatics_e2e.py
   ```
   *Expected Result*: All tests passing (including `test_live_05_anti_drift_rules_compliance`).
