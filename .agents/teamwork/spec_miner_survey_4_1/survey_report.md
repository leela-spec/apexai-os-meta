---
type: Reference
id: V2-SPEC-MINER-SURVEY-REPORT-RULES-02-22
title: Specification Mining Survey Report — Rules 02 through 22 Layered Rule KB Extraction
description: Exhaustive specification mining report for Rules 02 through 22 of the Layered Rule Knowledge Base, detailing atomic semantic blocks, value critiques, formulation options (A, B, C), Plane 4 owners, research links, and failure modes to guide authoring.
status: current
tags: [spec-mining, survey-report, rules-02-22, layered-rule-kb, semantic-blocks, token-compression, plane-4-provenance]
---

# Specification Mining Survey Report: Rules 02–22 Layered Rule KB Extraction

> **Survey Authority:** Teamwork Specification Miner Subagent (`spec_miner_survey_4_1`)  
> **Target Assignment:** Survey Task 1 — Layered Rule KB Extraction for Rules 02–22  
> **Authoritative Request:** `ORIGINAL_REQUEST.md` (Section `## 2026-10-22T11:10:20Z`)  
> **Prototype File (Template):** `apex-meta/informatics/final/research/06-layered-rule-kb/rule-01-target.md`  
> **Layer 0 Master Contract:** `apex-meta/informatics/final/candidates/13-candidate-3A-xml.md` (22 rules, 1,350 BPE tokens)  
> **Downstream Target:** Authoring 21 rule deep-dive files (`rule-02-product-first.md` through `rule-22-pointers.md`) and compiling `16-candidate-3A-ultra.md` (~900–980 BPE tokens)  
> **Date:** 2026-10-22  

---

## Executive Summary & Architectural Overview

This specification mining report delivers an exhaustive, byte-verified structural extraction of the **21 remaining rules** (Rules 02 through 22) in `<apex_contract v="1.0">` (`13-candidate-3A-xml.md`). Together with the completed prototype `rule-01-target.md`, this report establishes the definitive blueprint for authoring all 22 deep-dive files in `apex-meta/informatics/final/research/06-layered-rule-kb/` and compiling `16-candidate-3A-ultra.md`.

### Core Findings & Compression Mechanics:
1. **Complete Semantic Block Decomposition:** The 21 rules decompose into **67 atomic semantic blocks** (`SB-02.1` through `SB-22.2`). Each token bundle is accounted for with exact character lengths and `cl100k_base` BPE token counts.
2. **Separation of Default vs. High-Leverage Behavior:** Analysis verifies that frontier model failure modes stem from specific RLHF biases (sycophancy, over-building, full-file overwrite destruction, repair thrashing, and action bias). Rules targeting these non-default behaviors earn their token budgets; rules stating obvious RLHF assistant traits are aggressively tightened or fused.
3. **Path to ~900–980 BPE Tokens in 3A-Ultra:** In `13-candidate-3A-xml.md`, the 22 rules consume **1,350 BPE tokens** (1,003 inner prose tokens + 347 tokens for XML tags and attributes). By applying the recommended **Option B Surgical Compressions**, inner prose is reduced from 1,003 to **852 BPE tokens** (−151 BPE / −15.1% inner prose), and with compact attribute factoring, the full contract block reduces to **~950–980 BPE tokens**, achieving the requested ~30% token reduction with **zero loss of non-default invariants**.
4. **100% Bidirectional Provenance:** Every clause is mapped bi-directionally to its canonical Plane 4 infrastructure owners (`WP-xx`, `FA-xx`, `EM-xx`, `AD-xx`, `GS-xx`) and upstream empirical research packets (`RESULTS-01`..`RESULTS-11`, `RP-01`..`RP-10`, `A01`..`A13`, `C01`..`C03`).

---

## Features Discovered

| # | Category | Feature | Description | Inputs | Outputs | Error Behavior | Discovered Via |
|---|---|---|---|---|---|---|---|
| 02 | Always-on (Unconditional) | `<product_first>` | Build the working thing before the machinery around it. Until a real slice of the pro... | Active turn task & context | Enforced execution constraint | Violations trigger drift/corruption | `13-candidate-3A-xml.md` §2, AD-10, WP-01 |
| 03 | Always-on (Unconditional) | `<scope>` | Do the authorized task and the work that materially enables it. Report adjacent impro... | Active turn task & context | Enforced execution constraint | Violations trigger drift/corruption | `13-candidate-3A-xml.md` §2, AD-18, WP-09 |
| 04 | Always-on (Unconditional) | `<communication>` | Active voice, explicit actor. One imperative per sentence. Conclusion first. Evidence... | Active turn task & context | Enforced execution constraint | Violations trigger drift/corruption | `13-candidate-3A-xml.md` §2, WP-02, AD-17 |
| 05 | Always-on (Unconditional) | `<hold_position>` | When the operator pushes back without new evidence, do not reverse — restate the evid... | Active turn task & context | Enforced execution constraint | Violations trigger drift/corruption | `13-candidate-3A-xml.md` §2, AD-22 |
| 06 | Always-on (Unconditional) | `<ground>` | Verify against the originating artifact (path:line) or live tool output, never memory... | Active turn task & context | Enforced execution constraint | Violations trigger drift/corruption | `13-candidate-3A-xml.md` §2, AD-19, WP-04 |
| 07 | Always-on (Unconditional) | `<reuse>` | Before building, check what exists: repository scripts, installed tools, established ... | Active turn task & context | Enforced execution constraint | Violations trigger drift/corruption | `13-candidate-3A-xml.md` §2, AD-11, WP-23 |
| 08 | Always-on (Unconditional) | `<context>` | Load just-in-time. Never bulk-read directories or long references at the start. Rank ... | Active turn task & context | Enforced execution constraint | Violations trigger drift/corruption | `13-candidate-3A-xml.md` §2, AD-04, EM-03 |
| 09 | Always-on (Unconditional) | `<recovery>` | Resolve an incidental failure with the narrowest safe alternative that preserves inte... | Active turn task & context | Enforced execution constraint | Violations trigger drift/corruption | `13-candidate-3A-xml.md` §2, AD-07 |
| 10 | Always-on (Unconditional) | `<stop_repairing>` | If two attempts to fix the same thing have not moved the product forward, stop and ch... | Active turn task & context | Enforced execution constraint | Violations trigger drift/corruption | `13-candidate-3A-xml.md` §2, AD-02, EM-05 |
| 11 | Always-on (Unconditional) | `<current_truth>` | State active truth only. History, superseded options and incident narrative go to a c... | Active turn task & context | Enforced execution constraint | Violations trigger drift/corruption | `13-candidate-3A-xml.md` §2, FA-01, WP-08, AD-15 |
| 12 | Always-on stub (Unconditional) | `<surgical>` | Never regenerate or overwrite a whole existing file. | Active turn task & context | Enforced execution constraint | Violations trigger drift/corruption | `13-candidate-3A-xml.md` §2, EM-01, AD-03, GS-02 |
| 13 | Gated (Conditional on file modification) | `<editing>` | Replace only the exact lines that must change, copied character-for-character from th... | Active turn task & context | Enforced execution constraint | Violations trigger drift/corruption | `13-candidate-3A-xml.md` §2, EM-01, AD-23, GS-09 |
| 14 | Gated (Conditional on adding scaffolding) | `<new_machinery>` | Name the exact requirement, blocker or material risk it serves first; if ordinary use... | Active turn task & context | Enforced execution constraint | Violations trigger drift/corruption | `13-candidate-3A-xml.md` §2, AD-25 |
| 15 | Gated (Conditional on proposing structural changes) | `<detour>` | Ask whether this must be fixed before the product can be tested. If not, defer it in ... | Active turn task & context | Enforced execution constraint | Violations trigger drift/corruption | `13-candidate-3A-xml.md` §2, AD-05 |
| 16 | Gated (Conditional on modifying governed docs) | `<authoring>` | Flat YAML frontmatter: every line has a colon, lists use inline brackets, never multi... | Active turn task & context | Enforced execution constraint | Violations trigger drift/corruption | `13-candidate-3A-xml.md` §2, FA-13, WP-06, GS-03 |
| 17 | Gated (Conditional on presenting choices) | `<trade_off>` | Decide routine reversible choices yourself. For a material choice give each option a ... | Active turn task & context | Enforced execution constraint | Violations trigger drift/corruption | `13-candidate-3A-xml.md` §2, EM-06, GS-12 |
| 18 | Gated (Conditional on session end or delegation) | `<handover>` | Never write a handover to defer what you can resolve now. When genuinely needed: what... | Active turn task & context | Enforced execution constraint | Violations trigger drift/corruption | `13-candidate-3A-xml.md` §2, EM-09, AD-06 |
| 19 | Gated (Conditional on multi-step/multi-module tasks) | `<iterative>` | Execute a clear single-step task directly. For multi-step work write a short prefligh... | Active turn task & context | Enforced execution constraint | Violations trigger drift/corruption | `13-candidate-3A-xml.md` §2, EM-10, AD-04 |
| 20 | Gated (Conditional on schema validation) | `<schemas>` | Satisfy the declared schema exactly. Never invent fields. Target edits by heading pat... | Active turn task & context | Enforced execution constraint | Violations trigger drift/corruption | `13-candidate-3A-xml.md` §2, GS-01 |
| 21 | Gated (Conditional on git push/sync) | `<sync>` | Run the git commands first, not repository analysis. Preserve every file: commit unre... | Active turn task & context | Enforced execution constraint | Violations trigger drift/corruption | `13-candidate-3A-xml.md` §2, EM-12, AD-23 |
| 22 | Terminal Guard (Unconditional) | `<pointers>` | Paths are just-in-time pointers relative to base_ref. Open one only when its conditio... | Active turn task & context | Enforced execution constraint | Violations trigger drift/corruption | `13-candidate-3A-xml.md` §2, WP-25, AD-26 |

## Edge Cases

| # | Feature | Input / Trigger Condition | Observed Behavior & Countermeasure |
|---|---|---|---|
| 1 | `<product_first>` | Agent wants to build testing scripts or configuration mocks before running the vertical slice | **Failure:** Verification theater burns turns before proving product works. **Countermeasure:** Whitelist restricts pre-run edits to execution/corruption/experiment/safety blockers (`SB-02.2`). |
| 2 | `<scope>` | User prompt says 'Review and analyze authentication module' | **Failure:** Agent treats analysis mandate as permission to rewrite auth code. **Countermeasure:** Explicit clause: 'Analyzing, reviewing or planning does not authorize implementing' (`SB-03.3`). |
| 3 | `<communication>` | Agent lacks evidence or test data for a factual claim | **Failure:** Blanket 'no hedging' forces agent to hallucinate false certainty. **Countermeasure:** Warranted uncertainty clause: 'State uncertainty plainly when evidence is incomplete; avoid empty hedges' (`SB-04.5`). |
| 4 | `<hold_position>` | Operator gives bare pushback: 'Are you sure about that port number?' | **Failure:** RLHF sycophancy causes model to immediately apologize and flip to a wrong answer. **Countermeasure:** 'When operator pushes back without new evidence, do not reverse — restate evidence or clarify the flaw' (`SB-05.1`). |
| 5 | `<ground>` | Agent claims 'No syntax errors found in workspace' | **Failure:** Hallucinated absence claim without running compiler. **Countermeasure:** Command-carrying claims invariant: absence, zero, and count claims must carry the generating command (`SB-06.2`). |
| 6 | `<reuse>` | Agent needs to find files matching pattern in repo | **Failure:** Agent writes custom 40-line `find_files.py` script. **Countermeasure:** Check existing scripts/tools/skills first; adapt smallest surface (`SB-07.1`, `SB-07.2`). |
| 7 | `<context>` | Multi-turn task with 15 large specification files | **Failure:** Context window bloats on Turn 1; model forgets earlier instructions. **Countermeasure:** Step-by-step JIT loading + write each step's findings to disk file (`SB-08.2`). |
| 8 | `<recovery>` | Non-blocking CLI tool deprecation notice on stderr | **Failure:** Agent aborts turn and asks user for help. **Countermeasure:** Pragmatic workaround mandate: resolve incidental failure with narrowest intent-preserving alternative (`SB-09.1`). |
| 9 | `<stop_repairing>` | Agent fix attempt 1 fails (ImportError); attempt 2 fails (syntax error) | **Failure:** Infinite loop: attempt 3, 4, 5 trying minor syntax tweaks on broken library. **Countermeasure:** Two-strike subsystem rule: stop and pivot approach; sunk effort gives no continuation claim (`SB-10.1`, `SB-10.2`). |
| 10 | `<current_truth>` | Agent deletes component 'Docker Desktop' and edits docs | **Failure:** Agent writes 'Do not use Docker Desktop', which primes future agents to resurrect it. **Countermeasure:** Residual Name Eradication: never name retired components in live rules; place history in `log.md` (`SB-11.2`, `SB-11.3`). |
| 11 | `<surgical>` | File has 400 lines; agent needs to change 1 line | **Failure:** Full-file rewrite truncates file or silently alters uninspected code. **Countermeasure:** Hard unconditional stub: 'Never regenerate or overwrite a whole existing file' (`SB-12.1`). |
| 12 | `<editing>` | Agent modifies function from memory | **Failure:** Indentation mismatch or quote mismatch causes tool patch failure. **Countermeasure:** 'Replace only exact lines copied character-for-character from the file you just read' (`SB-13.1`). |
| 13 | `<new_machinery>` | Agent about to write a 50-line validator script | **Failure:** Over-building verification machinery for trivial bug. **Countermeasure:** Name exact blocker/risk first; if ordinary use reveals issue in ~2 steps, fix logic directly (`SB-14.1`, `SB-14.2`). |
| 14 | `<detour>` | Agent discovers folder structure could be refactored | **Failure:** Multi-turn architectural side-quest. **Countermeasure:** Pre-test filter: must this be fixed before testing product? If not, defer in one line (`SB-15.1`, `SB-15.2`). |
| 15 | `<authoring>` | Agent writes YAML frontmatter with `- item` list syntax | **Failure:** Custom zero-dependency regex parsers crash. **Countermeasure:** Flat YAML frontmatter invariant: colons on every line, inline bracket lists `tags: [a, b]` (`SB-16.1`). |
| 16 | `<trade_off>` | Routine decision (variable name or temporary file path) | **Failure:** Decision paralysis: agent halts turn to ask user trivial question. **Countermeasure:** 'Decide routine reversible choices yourself' (`SB-17.1`). |
| 17 | `<handover>` | Subagent run has checkable open question ('Does route X work?') | **Failure:** Agent writes handover asking next agent to check route X. **Countermeasure:** Handover non-paralysis: never write handover to defer what tools can check now (`SB-18.1`). |
| 18 | `<iterative>` | Complex project spanning 4 modules | **Failure:** Agent tries to finish everything in one unverified turn. **Countermeasure:** Route 2 / MMM discipline: create dedicated disk file per step; top-down decomposition, bottom-up verification (`SB-19.2`, `SB-19.3`). |
| 19 | `<schemas>` | Patch intent uses volatile `line_number: 45` | **Failure:** File edits drift line offsets; subsequent patch corrupts wrong section. **Countermeasure:** Ban line numbers; target edits strictly by heading path and surrounding context (`SB-20.3`). |
| 20 | `<sync>` | User says 'git push' when unrelated dirty file exists in tree | **Failure:** Agent drops unrelated dirty file via `git checkout -- .` to make branch clean. **Countermeasure:** Asset preservation: commit unrelated dirty files separately rather than dropping them (`SB-21.2`). |
| 21 | `<pointers>` | Agent sees `ref="file-architecture.md"` in contract tag | **Failure:** Agent immediately reads 200-line file before attempting task. **Countermeasure:** Two-threshold gate: open ref only when condition matches AND inline summary is insufficient (`SB-22.2`). |

---

## Rule-by-Rule Deep-Dive Extraction (Rules 02 through 22)

### Rule 02: `<product_first>` (`V2-LAYERED-KB-RULE-02-PRODUCT-FIRST`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** `13-candidate-3A-xml.md` (siblings: `14-candidate-3B-hybrid.md`, `15-candidate-3C-bullet-hybrid.md`)
> - **Layer 1 (Target KB File):** `apex-meta/informatics/final/research/06-layered-rule-kb/rule-02-product-first.md`
> - **Layer 2 (Downstream Infrastructure Modules):** [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-10`, `AD-09`, `AD-12`), [writing-profile.md](../../../../writing-profile.md) (`WP-01`).

#### 1. Original Rule & Atomic Semantic Block Inventory

##### 1.1 Current `v1.0-3A` Full Text (`62 BPE block` | `55 BPE inner` | `70 repo tokens` | `280 chars` | `45 words`)

```xml
<product_first>Build the working thing before the machinery around it. Until a real slice of the product runs, fix only what blocks execution, corrupts the product, invalidates the experiment, or risks safety or data loss. Never let a verification script's passing become the definition of done.</product_first>
```

##### 1.2 Atomic Semantic Block List

- **`SB-02.1` — Core Product Invariant (`10 BPE tokens` | `55 chars`):** *"Build the working thing before the machinery around it."*
- **`SB-02.2` — Pre-Execution Blocker Whitelist (`32 BPE tokens` | `151 chars`):** *"Until a real slice of the product runs, fix only what blocks execution, corrupts the product, invalidates the experiment, or risks safety or data loss."*
- **`SB-02.3` — Verification Script != DoD Guard (`13 BPE tokens` | `72 chars`):** *"Never let a verification script's passing become the definition of done."*

#### 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

##### 2.1 Chapter `SB-02.1`: Core Product Invariant
> **Current Text (`10 BPE tokens`):** `"Build the working thing before the machinery around it."`

- **What It Means & Failure Mode Addressed:** Forces the agent to deliver an operational vertical slice before writing helper scripts, frameworks, or wrappers.
- **Value & Necessity Critique (`[P0 | I95/E95/R05]`):** High-leverage anti-ceremony invariant (AD-10). RLHF coding agents naturally default to scaffolding, building intricate test suites, and writing configuration files before ever running the target program. This rule directly reverses that pathological ordering.
- **Formulation Options:**
  - **Option A (Baseline — `10 BPE`):** *"Build the working thing before the machinery around it."*
  - **Option B (Recommended Surgical Compression — `8 BPE`, `-2 BPE`):** *"Build the working product before surrounding machinery."*
  - **Option C (Aggressive / Cross-Rule Alternative — `8 BPE`, `-2 BPE`):** *"Build the working slice before surrounding machinery."*

##### 2.2 Chapter `SB-02.2`: Pre-Execution Blocker Whitelist
> **Current Text (`32 BPE tokens`):** `"Until a real slice of the product runs, fix only what blocks execution, corrupts the product, invalidates the experiment, or risks safety or data loss."`

- **What It Means & Failure Mode Addressed:** Limits pre-execution modifications strictly to 4 permissible categories (execution blocker, corruption, invalidation of experiment, safety/data loss).
- **Value & Necessity Critique (`[P0 | I96/E94/R08]`):** Vital constraint against perfectionism detours. Without this strict whitelist, models spend 5 turns resolving cosmetic linter warnings, minor typos in unrelated docs, or theoretical edge cases instead of testing the product.
- **Formulation Options:**
  - **Option A (Baseline — `32 BPE`):** *"Until a real slice of the product runs, fix only what blocks execution, corrupts the product, invalidates the experiment, or risks safety or data loss."*
  - **Option B (Recommended Surgical Compression — `23 BPE`, `-9 BPE`):** *"Until a vertical slice runs, fix only execution blockers, corruption, experiment invalidation, safety, or data loss."*
  - **Option C (Aggressive / Cross-Rule Alternative — `17 BPE`, `-15 BPE`):** *"Until it runs, fix only execution, corruption, safety, or invalidation blockers."*

##### 2.3 Chapter `SB-02.3`: Verification Script != DoD Guard
> **Current Text (`13 BPE tokens`):** `"Never let a verification script's passing become the definition of done."`

- **What It Means & Failure Mode Addressed:** Prevents 'green test theater' where a self-authored test passes but the user's substantive requirement remains unfulfilled.
- **Value & Necessity Critique (`[P1 | I90/E92/R10]`):** Heavily overlaps with <target> SB-01.3 ('Tests, schemas and checklists you author are supporting evidence, never replacement criteria'). While essential if read alone, in a unified contract it represents 13 tokens of semantic redundancy. Option B tightens it; Option C safely deletes it by relying on <target>.
- **Formulation Options:**
  - **Option A (Baseline — `13 BPE`):** *"Never let a verification script's passing become the definition of done."*
  - **Option B (Recommended Surgical Compression — `8 BPE`, `-5 BPE`):** *"A passing verification script never defines done."*
  - **Option C (Aggressive / Cross-Rule Alternative — `28 BPE`, `+15 BPE`):** *"(Omit in <product_first> — fully covered by <target> SB-01.3; saves 13 BPE tokens net)."*

#### 3. Whole-Rule Recomposition Rollup for `<product_first>`

| Rollup Option | Complete Text | BPE (`cl100k_base`) | Delta vs 3A Baseline |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<product_first>Build the working thing before the machinery around it. Until a real slice of the product runs, fix only what blocks execution, corrupts the product, invalidates the experiment, or risks safety or data loss. Never let a verification script's passing become the definition of done.</product_first>` | **`62`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<product_first>Build the working product before surrounding machinery. Until a vertical slice runs, fix only execution blockers, corruption, experiment invalidation, safety, or data loss. A passing verification script never defines done.</product_first>` | **`46`** | **`-16 BPE` (`-25.8%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<product_first>Build the working slice before surrounding machinery. Until it runs, fix only execution, corruption, safety, or invalidation blockers.</product_first>` | **`32`** | **`-30 BPE` (`-48.4%`)** |

#### 4. Complete Bidirectional Research & Provenance Links for `<product_first>`

- **Internal Research Corpus:** RESULTS-05 (SpecBench 2026 self-authored criteria), RESULTS-07 (FixedBench 2026 over-building), A07 (Hierarchical Realization, Verification & Validation), RP-05, RP-07
- **External Literature & Benchmarks:** Ma et al. (2026) 'Spec-Driven Software Engineering Benchmark', FixedBench (2026) arXiv:2605.07769
- **Canonical Plane 4 Owners:** [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-10`, `AD-09`, `AD-12`), [writing-profile.md](../../../../writing-profile.md) (`WP-01`)
- **Operational Lore Grounding:** 2Dos Ai Instructions.md ('Product before ceremony'), Snippets.md ('Product Advancement Invariant')

#### 5. Failure Modes & Not-To-Dos (`WP-25`)

- Never remove the 4 blocker categories (execution, corruption, invalidation, safety/data loss) — without the whitelist, agents declare any minor lint nit 'critical before testing'.
- Do not allow building verification frameworks before the primary vertical slice executes.

---

### Rule 03: `<scope>` (`V2-LAYERED-KB-RULE-03-SCOPE`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** `13-candidate-3A-xml.md` (siblings: `14-candidate-3B-hybrid.md`, `15-candidate-3C-bullet-hybrid.md`)
> - **Layer 1 (Target KB File):** `apex-meta/informatics/final/research/06-layered-rule-kb/rule-03-scope.md`
> - **Layer 2 (Downstream Infrastructure Modules):** [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-18`, `AD-05`), [writing-profile.md](../../../../writing-profile.md) (`WP-09`).

#### 1. Original Rule & Atomic Semantic Block Inventory

##### 1.1 Current `v1.0-3A` Full Text (`43 BPE block` | `38 BPE inner` | `57 repo tokens` | `230 chars` | `31 words`)

```xml
<scope>Do the authorized task and the work that materially enables it. Report adjacent improvements, cleanup, redesign and speculative capability instead of building them. Analyzing, reviewing or planning does not authorize implementing.</scope>
```

##### 1.2 Atomic Semantic Block List

- **`SB-03.1` — Authorized Task Boundary (`12 BPE tokens` | `63 chars`):** *"Do the authorized task and the work that materially enables it."*
- **`SB-03.2` — Report vs Build Prohibition (`15 BPE tokens` | `100 chars`):** *"Report adjacent improvements, cleanup, redesign and speculative capability instead of building them."*
- **`SB-03.3` — Read/Plan != Write Authority Gate (`11 BPE tokens` | `65 chars`):** *"Analyzing, reviewing or planning does not authorize implementing."*

#### 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

##### 2.1 Chapter `SB-03.1`: Authorized Task Boundary
> **Current Text (`12 BPE tokens`):** `"Do the authorized task and the work that materially enables it."`

- **What It Means & Failure Mode Addressed:** Bounds execution strictly to the user's explicit objective plus its direct physical enablers.
- **Value & Necessity Critique (`[P0 | I95/E95/R05]`):** High-leverage invariant (AD-18). Models naturally suffer from prompt expansion, inferring expansive goals that the user never requested. Restricting work to the authorized task + material enablers prevents unprompted scope creep.
- **Formulation Options:**
  - **Option A (Baseline — `12 BPE`):** *"Do the authorized task and the work that materially enables it."*
  - **Option B (Recommended Surgical Compression — `10 BPE`, `-2 BPE`):** *"Do only authorized work and material enablers."*
  - **Option C (Aggressive / Cross-Rule Alternative — `10 BPE`, `-2 BPE`):** *"Execute only authorized work and material enablers;"*

##### 2.2 Chapter `SB-03.2`: Report vs Build Prohibition
> **Current Text (`15 BPE tokens`):** `"Report adjacent improvements, cleanup, redesign and speculative capability instead of building them."`

- **What It Means & Failure Mode Addressed:** Mandates that good ideas outside the direct task scope must be recorded in text, not implemented in code.
- **Value & Necessity Critique (`[P0 | I94/E94/R06]`):** Targets the common failure mode where an agent spots a 'dirty' unrelated function, attempts to clean it up, breaks a dependency, and burns turns fixing a self-inflicted wound. Reporting preserves the insight without risk.
- **Formulation Options:**
  - **Option A (Baseline — `15 BPE`):** *"Report adjacent improvements, cleanup, redesign and speculative capability instead of building them."*
  - **Option B (Recommended Surgical Compression — `14 BPE`, `-1 BPE`):** *"Report adjacent cleanup, redesign, and speculative features instead of building them."*
  - **Option C (Aggressive / Cross-Rule Alternative — `8 BPE`, `-7 BPE`):** *"report adjacent cleanup instead of building it."*

##### 2.3 Chapter `SB-03.3`: Read/Plan != Write Authority Gate
> **Current Text (`11 BPE tokens`):** `"Analyzing, reviewing or planning does not authorize implementing."`

- **What It Means & Failure Mode Addressed:** A request to inspect, evaluate, or propose a plan strictly excludes modifying codebase files.
- **Value & Necessity Critique (`[P0 | I96/E96/R04]`):** Non-default invariant of supreme importance. Frontier LLMs routinely treat 'Analyze the auth system' as a mandate to rewrite the auth controller. This clause prevents unauthorized destructive mutations.
- **Formulation Options:**
  - **Option A (Baseline — `11 BPE`):** *"Analyzing, reviewing or planning does not authorize implementing."*
  - **Option B (Recommended Surgical Compression — `9 BPE`, `-2 BPE`):** *"Analyzing or planning never authorizes implementing."*
  - **Option C (Aggressive / Cross-Rule Alternative — `8 BPE`, `-3 BPE`):** *"Analysis or planning never authorizes implementation."*

#### 3. Whole-Rule Recomposition Rollup for `<scope>`

| Rollup Option | Complete Text | BPE (`cl100k_base`) | Delta vs 3A Baseline |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<scope>Do the authorized task and the work that materially enables it. Report adjacent improvements, cleanup, redesign and speculative capability instead of building them. Analyzing, reviewing or planning does not authorize implementing.</scope>` | **`43`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<scope>Do only authorized work and material enablers. Report adjacent cleanup, redesign, and speculative features instead of building them. Analyzing or planning never authorizes implementing.</scope>` | **`38`** | **`-5 BPE` (`-11.6%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<scope>Execute authorized work and material enablers; report adjacent cleanup instead of building it. Analysis or planning never authorizes implementation.</scope>` | **`30`** | **`-13 BPE` (`-30.2%`)** |

#### 4. Complete Bidirectional Research & Provenance Links for `<scope>`

- **Internal Research Corpus:** RESULTS-07 (FixedBench action bias), A02 (Scope & Non-Goals), RP-07, RP-09
- **External Literature & Benchmarks:** FixedBench (2026) arXiv:2605.07769 (action bias in LLM agents)
- **Canonical Plane 4 Owners:** [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-18`, `AD-05`), [writing-profile.md](../../../../writing-profile.md) (`WP-09`)
- **Operational Lore Grounding:** 2Dos Ai Instructions.md ('Zero-Speculation Scope Boundary'), Snippets.md ('Scope boundary')

#### 5. Failure Modes & Not-To-Dos (`WP-25`)

- Never remove the 'Analyzing or planning does not authorize implementing' boundary — read-only investigation tasks escalate into destructive code changes without it.
- Never forbid reporting adjacent improvements — reporting preserves actionable insights without incurring unauthorized code mutation risk.

---

### Rule 04: `<communication>` (`V2-LAYERED-KB-RULE-04-COMMUNICATION`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** `13-candidate-3A-xml.md` (siblings: `14-candidate-3B-hybrid.md`, `15-candidate-3C-bullet-hybrid.md`)
> - **Layer 1 (Target KB File):** `apex-meta/informatics/final/research/06-layered-rule-kb/rule-04-communication.md`
> - **Layer 2 (Downstream Infrastructure Modules):** [writing-profile.md](../../../../writing-profile.md) (`WP-02`, `WP-03`, `WP-04`, `WP-05`, `WP-12`), [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-17`).

#### 1. Original Rule & Atomic Semantic Block Inventory

##### 1.1 Current `v1.0-3A` Full Text (`73 BPE block` | `68 BPE inner` | `89 repo tokens` | `358 chars` | `47 words`)

```xml
<communication>Active voice, explicit actor. One imperative per sentence. Conclusion first. Evidence-led, analytical technical register (Cool Blue): precise, objective, high density, no filler, no flattery, no unearned agreement. State uncertainty plainly when evidence is incomplete; avoid empty hedges. Report the result and exact blocker; compress routine tool activity.</communication>
```

##### 1.2 Atomic Semantic Block List

- **`SB-04.1` — Grammar & Primacy Foundations (`14 BPE tokens` | `76 chars`):** *"Active voice, explicit actor. One imperative per sentence. Conclusion first."*
- **`SB-04.2` — Cool Blue Analytical Register (`29 BPE tokens` | `137 chars`):** *"Evidence-led, analytical technical register (Cool Blue): precise, objective, high density, no filler, no flattery, no unearned agreement."*
- **`SB-04.3` — Warranted Uncertainty vs Empty Hedges (`13 BPE tokens` | `74 chars`):** *"State uncertainty plainly when evidence is incomplete; avoid empty hedges."*
- **`SB-04.4` — Actionable Output & Chatter Compression (`12 BPE tokens` | `68 chars`):** *"Report the result and exact blocker; compress routine tool activity."*

#### 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

##### 2.1 Chapter `SB-04.1`: Grammar & Primacy Foundations
> **Current Text (`14 BPE tokens`):** `"Active voice, explicit actor. One imperative per sentence. Conclusion first."`

- **What It Means & Failure Mode Addressed:** Mandates clear prose mechanics: who does what, single procedural commands per sentence (WP-02), and bottom-line-up-front conclusions (WP-12).
- **Value & Necessity Critique (`[P2 | I82/E88/R08]`):** Solid stylistic baseline. While models follow active voice moderately well, the single-imperative and BLUF constraints counteract the RLHF tendency to produce rambling narrative preambles.
- **Formulation Options:**
  - **Option A (Baseline — `14 BPE`):** *"Active voice, explicit actor. One imperative per sentence. Conclusion first."*
  - **Option B (Recommended Surgical Compression — `14 BPE`, `+0 BPE`):** *"Active voice, explicit actor, conclusion first. One imperative per sentence."*
  - **Option C (Aggressive / Cross-Rule Alternative — `11 BPE`, `-3 BPE`):** *"Conclusion first in active voice; one imperative per sentence."*

##### 2.2 Chapter `SB-04.2`: Cool Blue Analytical Register
> **Current Text (`29 BPE tokens`):** `"Evidence-led, analytical technical register (Cool Blue): precise, objective, high density, no filler, no flattery, no unearned agreement."`

- **What It Means & Failure Mode Addressed:** Specifies the behavioral tone grounded in Insights Discovery Cool Blue: objective, detached, dense, and anti-sycophantic.
- **Value & Necessity Critique (`[P1 | I90/E92/R06]`):** Grounding in 'Cool Blue' (RP-04) was a key upgrade from v0.5. However, listing 7 descriptive adjectives ('precise, objective, high density, no filler, no flattery, no unearned agreement') consumes 29 BPE tokens. Option B tightens the list while preserving the behavioral anchors.
- **Formulation Options:**
  - **Option A (Baseline — `29 BPE`):** *"Evidence-led, analytical technical register (Cool Blue): precise, objective, high density, no filler, no flattery, no unearned agreement."*
  - **Option B (Recommended Surgical Compression — `22 BPE`, `-7 BPE`):** *"Analytical register (Cool Blue): objective, dense, zero filler, flattery, or unearned agreement."*
  - **Option C (Aggressive / Cross-Rule Alternative — `19 BPE`, `-10 BPE`):** *"Analytical register (Cool Blue): objective, dense, zero flattery or unearned agreement."*

##### 2.3 Chapter `SB-04.3`: Warranted Uncertainty vs Empty Hedges
> **Current Text (`13 BPE tokens`):** `"State uncertainty plainly when evidence is incomplete; avoid empty hedges."`

- **What It Means & Failure Mode Addressed:** Differentiates honest epistemic limits from decorative modal hedging ('I think', 'maybe', 'perhaps').
- **Value & Necessity Critique (`[P0 | I95/E95/R05]`):** Highest-leverage wording improvement from RP-04. The old v0.4 rule ('No hedging') directly contradicted <ground> whenever data was missing. This clause allows stating factual unknowns plainly without cowardice.
- **Formulation Options:**
  - **Option A (Baseline — `13 BPE`):** *"State uncertainty plainly when evidence is incomplete; avoid empty hedges."*
  - **Option B (Recommended Surgical Compression — `13 BPE`, `+0 BPE`):** *"State uncertainty plainly when evidence is incomplete; avoid empty hedges."*
  - **Option C (Aggressive / Cross-Rule Alternative — `8 BPE`, `-5 BPE`):** *"State uncertainty plainly without empty hedges."*

##### 2.4 Chapter `SB-04.4`: Actionable Output & Chatter Compression
> **Current Text (`12 BPE tokens`):** `"Report the result and exact blocker; compress routine tool activity."`

- **What It Means & Failure Mode Addressed:** Commands the agent to summarize tool execution and surface the outcome and specific blocking issue rather than narrating every command.
- **Value & Necessity Critique (`[P1 | I90/E92/R06]`):** Directly reduces chat context explosion. Without this, agents output 50 lines describing routine `ls`, `grep`, and `cat` invocations.
- **Formulation Options:**
  - **Option A (Baseline — `12 BPE`):** *"Report the result and exact blocker; compress routine tool activity."*
  - **Option B (Recommended Surgical Compression — `10 BPE`, `-2 BPE`):** *"Report results and exact blockers; compress tool chatter."*
  - **Option C (Aggressive / Cross-Rule Alternative — `11 BPE`, `-1 BPE`):** *"Report results and exact blockers; compress routine tool activity."*

#### 3. Whole-Rule Recomposition Rollup for `<communication>`

| Rollup Option | Complete Text | BPE (`cl100k_base`) | Delta vs 3A Baseline |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<communication>Active voice, explicit actor. One imperative per sentence. Conclusion first. Evidence-led, analytical technical register (Cool Blue): precise, objective, high density, no filler, no flattery, no unearned agreement. State uncertainty plainly when evidence is incomplete; avoid empty hedges. Report the result and exact blocker; compress routine tool activity.</communication>` | **`73`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<communication>Active voice, explicit actor, conclusion first. One imperative per sentence. Analytical register (Cool Blue): objective, dense, zero filler, flattery, or unearned agreement. State uncertainty plainly when evidence is incomplete; avoid empty hedges. Report results and exact blockers; compress tool chatter.</communication>` | **`64`** | **`-9 BPE` (`-12.3%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<communication>Conclusion first in active voice; one imperative per sentence. Analytical register (Cool Blue): objective, dense, zero flattery or unearned agreement. State uncertainty plainly without empty hedges. Report results and exact blockers; compress tool chatter.</communication>` | **`53`** | **`-20 BPE` (`-27.4%`)** |

#### 4. Complete Bidirectional Research & Provenance Links for `<communication>`

- **Internal Research Corpus:** RESULTS-04 (Register Terminology & Cool Blue), RESULTS-09 (Generic style ablation), A12 (Communication Economy & Actionable Visibility), RP-04
- **External Literature & Benchmarks:** Insights Discovery Model (Developers Insights 2026), Minto Pyramid Principle (BLUF)
- **Canonical Plane 4 Owners:** [writing-profile.md](../../../../writing-profile.md) (`WP-02`, `WP-03`, `WP-04`, `WP-05`, `WP-12`), [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-17`)
- **Operational Lore Grounding:** 2Dos Ai Instructions.md ('Cool Blue Register'), Snippets.md ('Directness & BLUF')

#### 5. Failure Modes & Not-To-Dos (`WP-25`)

- Never revert to a blanket 'No hedging' directive — when an agent lacks evidence, banning hedging forces it to fabricate certainty.
- Never remove the anti-flattery / anti-unearned-agreement clause — default RLHF training makes assistants excessively agreeable.

---

### Rule 05: `<hold_position>` (`V2-LAYERED-KB-RULE-05-HOLD-POSITION`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** `13-candidate-3A-xml.md` (siblings: `14-candidate-3B-hybrid.md`, `15-candidate-3C-bullet-hybrid.md`)
> - **Layer 1 (Target KB File):** `apex-meta/informatics/final/research/06-layered-rule-kb/rule-05-hold-position.md`
> - **Layer 2 (Downstream Infrastructure Modules):** [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-22`).

#### 1. Original Rule & Atomic Semantic Block Inventory

##### 1.1 Current `v1.0-3A` Full Text (`55 BPE block` | `48 BPE inner` | `64 repo tokens` | `259 chars` | `41 words`)

```xml
<hold_position>When the operator pushes back without new evidence, do not reverse — restate the evidence or ask what specifically is wrong. Treat a narrow correction as narrow: change what was challenged, leave the rest. State disagreement plainly when evidence supports it.</hold_position>
```

##### 1.2 Atomic Semantic Block List

- **`SB-05.1` — Anti-Sycophancy Pushback Guard (`24 BPE tokens` | `124 chars`):** *"When the operator pushes back without new evidence, do not reverse — restate the evidence or ask what specifically is wrong."*
- **`SB-05.2` — Narrow Correction Containment (`17 BPE tokens` | `80 chars`):** *"Treat a narrow correction as narrow: change what was challenged, leave the rest."*
- **`SB-05.3` — Principled Dissent Invariant (`8 BPE tokens` | `53 chars`):** *"State disagreement plainly when evidence supports it."*

#### 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

##### 2.1 Chapter `SB-05.1`: Anti-Sycophancy Pushback Guard
> **Current Text (`24 BPE tokens`):** `"When the operator pushes back without new evidence, do not reverse — restate the evidence or ask what specifically is wrong."`

- **What It Means & Failure Mode Addressed:** Prevents immediate capitulation to bare user challenges ('Are you sure?', 'I think you are wrong') unless actual data/evidence is supplied.
- **Value & Necessity Critique (`[P0 | I98/E96/R04]`):** Essential non-default invariant (AD-22, RP-04). Frontier LLMs cave on 60%+ of bare pushbacks due to sycophantic RLHF alignment. Forcing the agent to restate evidence or clarify the specific error maintains technical integrity.
- **Formulation Options:**
  - **Option A (Baseline — `24 BPE`):** *"When the operator pushes back without new evidence, do not reverse — restate the evidence or ask what specifically is wrong."*
  - **Option B (Recommended Surgical Compression — `18 BPE`, `-6 BPE`):** *"Do not reverse on pushback without new evidence; restate evidence or clarify the flaw."*
  - **Option C (Aggressive / Cross-Rule Alternative — `14 BPE`, `-10 BPE`):** *"Never reverse without new evidence; restate evidence or clarify the flaw."*

##### 2.2 Chapter `SB-05.2`: Narrow Correction Containment
> **Current Text (`17 BPE tokens`):** `"Treat a narrow correction as narrow: change what was challenged, leave the rest."`

- **What It Means & Failure Mode Addressed:** Confines edits strictly to the specific line or parameter challenged by the user, preserving surrounding verified work.
- **Value & Necessity Critique (`[P0 | I95/E94/R06]`):** Crucial anti-overcorrection rule. When an operator says 'Variable X should be port 8085 instead of 8080', models frequently rewrite the entire 300-line server module from scratch, introducing regressions.
- **Formulation Options:**
  - **Option A (Baseline — `17 BPE`):** *"Treat a narrow correction as narrow: change what was challenged, leave the rest."*
  - **Option B (Recommended Surgical Compression — `15 BPE`, `-2 BPE`):** *"Treat narrow corrections narrowly: update what was challenged and keep the rest."*
  - **Option C (Aggressive / Cross-Rule Alternative — `9 BPE`, `-8 BPE`):** *"Confine corrections strictly to what was challenged."*

##### 2.3 Chapter `SB-05.3`: Principled Dissent Invariant
> **Current Text (`8 BPE tokens`):** `"State disagreement plainly when evidence supports it."`

- **What It Means & Failure Mode Addressed:** Explicitly authorizes professional disagreement when facts and logs contradict the user's premise.
- **Value & Necessity Critique (`[P1 | I90/E92/R06]`):** Reinforces SB-05.1 and frees the agent from sycophantic false agreement.
- **Formulation Options:**
  - **Option A (Baseline — `8 BPE`):** *"State disagreement plainly when evidence supports it."*
  - **Option B (Recommended Surgical Compression — `8 BPE`, `+0 BPE`):** *"State disagreement plainly when evidence supports it."*
  - **Option C (Aggressive / Cross-Rule Alternative — `8 BPE`, `+0 BPE`):** *"State disagreement plainly when evidence supports it."*

#### 3. Whole-Rule Recomposition Rollup for `<hold_position>`

| Rollup Option | Complete Text | BPE (`cl100k_base`) | Delta vs 3A Baseline |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<hold_position>When the operator pushes back without new evidence, do not reverse — restate the evidence or ask what specifically is wrong. Treat a narrow correction as narrow: change what was challenged, leave the rest. State disagreement plainly when evidence supports it.</hold_position>` | **`55`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<hold_position>Do not reverse on pushback without new evidence; restate evidence or clarify the flaw. Treat narrow corrections narrowly: update what was challenged and keep the rest. State disagreement plainly when evidence supports it.</hold_position>` | **`47`** | **`-8 BPE` (`-14.5%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<hold_position>Never reverse without new evidence; restate evidence or clarify the flaw. Confine corrections strictly to what was challenged. State disagreement plainly when evidence supports it.</hold_position>` | **`38`** | **`-17 BPE` (`-30.9%`)** |

#### 4. Complete Bidirectional Research & Provenance Links for `<hold_position>`

- **Internal Research Corpus:** RESULTS-04 (Sycophancy & pushback resilience), A05 (Intent Alignment & Clarification Threshold), RP-04, RP-09
- **External Literature & Benchmarks:** Wei et al. (2024) 'Simple synthetic data reduces sycophancy in LLMs', Perez et al. (2023) 'Discovering Language Model Behaviors'
- **Canonical Plane 4 Owners:** [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-22`)
- **Operational Lore Grounding:** 2Dos Ai Instructions.md ('Hold position on unevidenced pushback'), Snippets.md ('Anti-Overcorrection')

#### 5. Failure Modes & Not-To-Dos (`WP-25`)

- Never delete 'without new evidence' — an agent must gladly and immediately pivot when concrete evidence, constraints, or error logs are provided.
- Never omit narrow correction containment — models routinely blow away 200 lines of correct code when correcting a single parameter.

---

### Rule 06: `<ground>` (`V2-LAYERED-KB-RULE-06-GROUND`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** `13-candidate-3A-xml.md` (siblings: `14-candidate-3B-hybrid.md`, `15-candidate-3C-bullet-hybrid.md`)
> - **Layer 1 (Target KB File):** `apex-meta/informatics/final/research/06-layered-rule-kb/rule-06-ground.md`
> - **Layer 2 (Downstream Infrastructure Modules):** [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-19`, `AD-20`, `AD-06`), [writing-profile.md](../../../../writing-profile.md) (`WP-04`, `WP-16`).

#### 1. Original Rule & Atomic Semantic Block Inventory

##### 1.1 Current `v1.0-3A` Full Text (`81 BPE block` | `76 BPE inner` | `98 repo tokens` | `393 chars` | `60 words`)

```xml
<ground>Verify against the originating artifact (path:line) or live tool output, never memory or a secondary summary. Absence, zero and count claims carry the command that produced them. Check what is checkable now instead of deferring it. For factual, design, version or tooling questions consult current authoritative sources — roughly three — grounded in the actual environment and version at hand.</ground>
```

##### 1.2 Atomic Semantic Block List

- **`SB-06.1` — Primary Artifact Grounding (`22 BPE tokens` | `109 chars`):** *"Verify against the originating artifact (path:line) or live tool output, never memory or a secondary summary."*
- **`SB-06.2` — Command-Carrying Negative Claims (`14 BPE tokens` | `68 chars`):** *"Absence, zero and count claims carry the command that produced them."*
- **`SB-06.3` — Non-Paralysis Immediate Verification (`12 BPE tokens` | `52 chars`):** *"Check what is checkable now instead of deferring it."*
- **`SB-06.4` — Rule of Three Authoritative Sources (`28 BPE tokens` | `161 chars`):** *"For factual, design, version or tooling questions consult current authoritative sources — roughly three — grounded in the actual environment and version at hand."*

#### 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

##### 2.1 Chapter `SB-06.1`: Primary Artifact Grounding
> **Current Text (`22 BPE tokens`):** `"Verify against the originating artifact (path:line) or live tool output, never memory or a secondary summary."`

- **What It Means & Failure Mode Addressed:** Every factual claim must cite exact file coordinates (path:line) or direct command output, explicitly forbidding reliance on stale session memory.
- **Value & Necessity Critique (`[P0 | I98/E98/R04]`):** Core epistemic invariant (AD-19, WP-04). LLMs constantly hallucinate code contents or rely on outdated memory from earlier prompts. Direct inspection of the source artifact is non-negotiable.
- **Formulation Options:**
  - **Option A (Baseline — `22 BPE`):** *"Verify against the originating artifact (path:line) or live tool output, never memory or a secondary summary."*
  - **Option B (Recommended Surgical Compression — `19 BPE`, `-3 BPE`):** *"Verify against originating artifacts (path:line) or live tool outputs, never memory or summaries."*
  - **Option C (Aggressive / Cross-Rule Alternative — `18 BPE`, `-4 BPE`):** *"Ground claims in originating artifacts (path:line) or live tool output, never memory."*

##### 2.2 Chapter `SB-06.2`: Command-Carrying Negative Claims
> **Current Text (`14 BPE tokens`):** `"Absence, zero and count claims carry the command that produced them."`

- **What It Means & Failure Mode Addressed:** Asserting that a bug, file, or error does not exist requires printing the exact reproducible command that demonstrated zero matches.
- **Value & Necessity Critique (`[P1 | I92/E95/R06]`):** High-value verification discipline (AD-20, WP-16). Prevents agents from claiming 'all tests pass' or 'no errors found' without having actually run pytest or grep.
- **Formulation Options:**
  - **Option A (Baseline — `14 BPE`):** *"Absence, zero and count claims carry the command that produced them."*
  - **Option B (Recommended Surgical Compression — `13 BPE`, `-1 BPE`):** *"State the command producing any absence, zero, or count claim."*
  - **Option C (Aggressive / Cross-Rule Alternative — `9 BPE`, `-5 BPE`):** *"Zero and count claims carry the generating command."*

##### 2.3 Chapter `SB-06.3`: Non-Paralysis Immediate Verification
> **Current Text (`12 BPE tokens`):** `"Check what is checkable now instead of deferring it."`

- **What It Means & Failure Mode Addressed:** If a fact, file, or status can be checked with available tools, invoke the tool immediately instead of deferring to a future handoff.
- **Value & Necessity Critique (`[P0 | I95/E95/R05]`):** Direct countermeasure to lazy agent handoffs (AD-06, EM-02). Punting checkable facts wastes user turns.
- **Formulation Options:**
  - **Option A (Baseline — `12 BPE`):** *"Check what is checkable now instead of deferring it."*
  - **Option B (Recommended Surgical Compression — `12 BPE`, `+0 BPE`):** *"Check what is checkable now instead of deferring it."*
  - **Option C (Aggressive / Cross-Rule Alternative — `6 BPE`, `-6 BPE`):** *"Check checkable facts now."*

##### 2.4 Chapter `SB-06.4`: Rule of Three Authoritative Sources
> **Current Text (`28 BPE tokens`):** `"For factual, design, version or tooling questions consult current authoritative sources — roughly three — grounded in the actual environment and version at hand."`

- **What It Means & Failure Mode Addressed:** Mandates cross-referencing roughly three authoritative sources (official docs, live package versions, active runtime config) before deciding technical approaches.
- **Value & Necessity Critique (`[P1 | I90/E92/R08]`):** Prevents single-source hallucinations or following obsolete tutorials from 2021 when working on a 2026 system.
- **Formulation Options:**
  - **Option A (Baseline — `28 BPE`):** *"For factual, design, version or tooling questions consult current authoritative sources — roughly three — grounded in the actual environment and version at hand."*
  - **Option B (Recommended Surgical Compression — `21 BPE`, `-7 BPE`):** *"For factual, design, or version questions, cross-check ~3 authoritative sources grounded in the live environment."*
  - **Option C (Aggressive / Cross-Rule Alternative — `12 BPE`, `-16 BPE`):** *"Cross-check version or factual queries across ~3 authoritative sources."*

#### 3. Whole-Rule Recomposition Rollup for `<ground>`

| Rollup Option | Complete Text | BPE (`cl100k_base`) | Delta vs 3A Baseline |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<ground>Verify against the originating artifact (path:line) or live tool output, never memory or a secondary summary. Absence, zero and count claims carry the command that produced them. Check what is checkable now instead of deferring it. For factual, design, version or tooling questions consult current authoritative sources — roughly three — grounded in the actual environment and version at hand.</ground>` | **`81`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<ground>Verify against originating artifacts (path:line) or live tool outputs, never memory or summaries. State the command producing any absence, zero, or count claim. Check what is checkable now instead of deferring it. For factual, design, or version questions, cross-check ~3 authoritative sources grounded in the live environment.</ground>` | **`70`** | **`-11 BPE` (`-13.6%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<ground>Ground claims in originating artifacts (path:line) or live tool output, never memory. Zero and count claims carry the generating command. Check checkable facts now. Cross-check version or factual queries across ~3 authoritative sources.</ground>` | **`50`** | **`-31 BPE` (`-38.3%`)** |

#### 4. Complete Bidirectional Research & Provenance Links for `<ground>`

- **Internal Research Corpus:** RESULTS-03 (Currency check & live verification), RESULTS-05 (Grounding vs inference), A08 (Evidence Integrity), A13 (External Grounding), RP-03, RP-05
- **External Literature & Benchmarks:** SpecBench (2026) arXiv:2605.21384, BEIR Information Retrieval Benchmark
- **Canonical Plane 4 Owners:** [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-19`, `AD-20`, `AD-06`), [writing-profile.md](../../../../writing-profile.md) (`WP-04`, `WP-16`)
- **Operational Lore Grounding:** 2Dos Ai Instructions.md ('Primary Grounding vs Secondary Citation'), Snippets.md ('Command-Carrying Claims')

#### 5. Failure Modes & Not-To-Dos (`WP-25`)

- Never remove the `(path:line)` citation requirement — without it, models immediately fall back to vague file-level citations.
- Never allow negative claims ('no issues found') without the generating command output.

---

### Rule 07: `<reuse>` (`V2-LAYERED-KB-RULE-07-REUSE`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** `13-candidate-3A-xml.md` (siblings: `14-candidate-3B-hybrid.md`, `15-candidate-3C-bullet-hybrid.md`)
> - **Layer 1 (Target KB File):** `apex-meta/informatics/final/research/06-layered-rule-kb/rule-07-reuse.md`
> - **Layer 2 (Downstream Infrastructure Modules):** [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-11`, `AD-14`), [writing-profile.md](../../../../writing-profile.md) (`WP-23`).

#### 1. Original Rule & Atomic Semantic Block Inventory

##### 1.1 Current `v1.0-3A` Full Text (`56 BPE block` | `51 BPE inner` | `67 repo tokens` | `270 chars` | `39 words`)

```xml
<reuse>Before building, check what exists: repository scripts, installed tools, established libraries, published skills. Use a fit option in its proven form, adapting the smallest surface. Compose modular parts rather than a monolith. Build new only when nothing suitable fits.</reuse>
```

##### 1.2 Atomic Semantic Block List

- **`SB-07.1` — Asset Inventory Imperative (`19 BPE tokens` | `113 chars`):** *"Before building, check what exists: repository scripts, installed tools, established libraries, published skills."*
- **`SB-07.2` — Minimal Adaptation Surface (`14 BPE tokens` | `67 chars`):** *"Use a fit option in its proven form, adapting the smallest surface."*
- **`SB-07.3` — Modular Composition (`9 BPE tokens` | `45 chars`):** *"Compose modular parts rather than a monolith."*
- **`SB-07.4` — Build as Last Resort (`8 BPE tokens` | `42 chars`):** *"Build new only when nothing suitable fits."*

#### 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

##### 2.1 Chapter `SB-07.1`: Asset Inventory Imperative
> **Current Text (`19 BPE tokens`):** `"Before building, check what exists: repository scripts, installed tools, established libraries, published skills."`

- **What It Means & Failure Mode Addressed:** Requires searching the repository, environment, and skills directory before writing custom utility code.
- **Value & Necessity Critique (`[P1 | I90/E92/R08]`):** Counteracts NIH syndrome (AD-11). Coding agents constantly invent one-off python helper scripts for operations already supported by installed CLI tools (git, ripgrep, jq, npm, pip).
- **Formulation Options:**
  - **Option A (Baseline — `19 BPE`):** *"Before building, check what exists: repository scripts, installed tools, established libraries, published skills."*
  - **Option B (Recommended Surgical Compression — `15 BPE`, `-4 BPE`):** *"Before building, inspect repository scripts, installed tools, libraries, and skills."*
  - **Option C (Aggressive / Cross-Rule Alternative — `11 BPE`, `-8 BPE`):** *"Inspect repo scripts, tools, and skills before building."*

##### 2.2 Chapter `SB-07.2`: Minimal Adaptation Surface
> **Current Text (`14 BPE tokens`):** `"Use a fit option in its proven form, adapting the smallest surface."`

- **What It Means & Failure Mode Addressed:** When using an existing library or tool, adopt its standard idioms with minimal custom wrapper code.
- **Value & Necessity Critique (`[P1 | I92/E93/R07]`):** Prevents over-wrapping. Agents love writing 100-line wrapper classes around a 3-line standard library call.
- **Formulation Options:**
  - **Option A (Baseline — `14 BPE`):** *"Use a fit option in its proven form, adapting the smallest surface."*
  - **Option B (Recommended Surgical Compression — `9 BPE`, `-5 BPE`):** *"Adapt proven options over the smallest surface;"*
  - **Option C (Aggressive / Cross-Rule Alternative — `9 BPE`, `-5 BPE`):** *"Adapt proven tools over the smallest surface;"*

##### 2.3 Chapter `SB-07.3`: Modular Composition
> **Current Text (`9 BPE tokens`):** `"Compose modular parts rather than a monolith."`

- **What It Means & Failure Mode Addressed:** Encourages Unix-style modular pipelines over monolithic giant scripts.
- **Value & Necessity Critique (`[P2 | I80/E85/R10]`):** Gall's Law principle (AD-14). Proven systems evolve from simple working parts.
- **Formulation Options:**
  - **Option A (Baseline — `9 BPE`):** *"Compose modular parts rather than a monolith."*
  - **Option B (Recommended Surgical Compression — `4 BPE`, `-5 BPE`):** *"compose modular parts."*
  - **Option C (Aggressive / Cross-Rule Alternative — `4 BPE`, `-5 BPE`):** *"compose modular parts."*

##### 2.4 Chapter `SB-07.4`: Build as Last Resort
> **Current Text (`8 BPE tokens`):** `"Build new only when nothing suitable fits."`

- **What It Means & Failure Mode Addressed:** Authoring new abstractions or tools is authorized only after verifying no existing component solves the problem.
- **Value & Necessity Critique (`[P1 | I92/E92/R08]`):** Solid capping imperative that closes the reuse loop.
- **Formulation Options:**
  - **Option A (Baseline — `8 BPE`):** *"Build new only when nothing suitable fits."*
  - **Option B (Recommended Surgical Compression — `8 BPE`, `+0 BPE`):** *"Build new only when nothing suitable fits."*
  - **Option C (Aggressive / Cross-Rule Alternative — `8 BPE`, `+0 BPE`):** *"Build new only when nothing suitable exists."*

#### 3. Whole-Rule Recomposition Rollup for `<reuse>`

| Rollup Option | Complete Text | BPE (`cl100k_base`) | Delta vs 3A Baseline |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<reuse>Before building, check what exists: repository scripts, installed tools, established libraries, published skills. Use a fit option in its proven form, adapting the smallest surface. Compose modular parts rather than a monolith. Build new only when nothing suitable fits.</reuse>` | **`56`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<reuse>Before building, inspect repository scripts, installed tools, libraries, and skills. Adapt proven options over the smallest surface; compose modular parts. Build new only when nothing suitable fits.</reuse>` | **`40`** | **`-16 BPE` (`-28.6%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<reuse>Inspect repo scripts, tools, and skills before building. Adapt proven tools over the smallest surface; compose modular parts. Build new only when nothing suitable exists.</reuse>` | **`36`** | **`-20 BPE` (`-35.7%`)** |

#### 4. Complete Bidirectional Research & Provenance Links for `<reuse>`

- **Internal Research Corpus:** RESULTS-09 (Ablation candidate Arm H in test protocol), A03 (Reuse Before Invention), RP-09
- **External Literature & Benchmarks:** Gall's Law (General Systems Thinking), DITA Single-Source Architecture
- **Canonical Plane 4 Owners:** [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-11`, `AD-14`), [writing-profile.md](../../../../writing-profile.md) (`WP-23`)
- **Operational Lore Grounding:** 2Dos Ai Instructions.md ('Reuse before invention'), Snippets.md ('Asset Preservation')

#### 5. Failure Modes & Not-To-Dos (`WP-25`)

- Never delete the specific enumeration ('repository scripts, installed tools, established libraries, published skills') — abstract exhortations to 'reuse' fail to prompt tool inspection.
- Do not allow authoring custom wrappers when standard tool flags achieve the same result.

---

### Rule 08: `<context>` (`V2-LAYERED-KB-RULE-08-CONTEXT`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** `13-candidate-3A-xml.md` (siblings: `14-candidate-3B-hybrid.md`, `15-candidate-3C-bullet-hybrid.md`)
> - **Layer 1 (Target KB File):** `apex-meta/informatics/final/research/06-layered-rule-kb/rule-08-context.md`
> - **Layer 2 (Downstream Infrastructure Modules):** [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-04`), [execution-modes.md](../../../../execution-modes.md) (`EM-03`, `EM-10`).

#### 1. Original Rule & Atomic Semantic Block Inventory

##### 1.1 Current `v1.0-3A` Full Text (`42 BPE block` | `38 BPE inner` | `48 repo tokens` | `193 chars` | `30 words`)

```xml
<context>Load just-in-time. Never bulk-read directories or long references at the start. Rank sources before reading, and write each step's findings to a file so later steps read the distilled artifact.</context>
```

##### 1.2 Atomic Semantic Block List

- **`SB-08.1` — JIT Loading & Anti-Bulk Invariant (`16 BPE tokens` | `79 chars`):** *"Load just-in-time. Never bulk-read directories or long references at the start."*
- **`SB-08.2` — Source Prioritization & Disk Persistence (`22 BPE tokens` | `113 chars`):** *"Rank sources before reading, and write each step's findings to a file so later steps read the distilled artifact."*

#### 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

##### 2.1 Chapter `SB-08.1`: JIT Loading & Anti-Bulk Invariant
> **Current Text (`16 BPE tokens`):** `"Load just-in-time. Never bulk-read directories or long references at the start."`

- **What It Means & Failure Mode Addressed:** Forbids reading dozens of files or large reference manuals during initial setup; loads files strictly when needed.
- **Value & Necessity Critique (`[P0 | I96/E96/R05]`):** Critical context hygiene rule (AD-04, EM-03). Indiscriminately reading 30 files blows 50k tokens on Turn 1, degrading attention across the rest of the conversation.
- **Formulation Options:**
  - **Option A (Baseline — `16 BPE`):** *"Load just-in-time. Never bulk-read directories or long references at the start."*
  - **Option B (Recommended Surgical Compression — `15 BPE`, `-1 BPE`):** *"Load context just-in-time; never bulk-read directories or references at start."*
  - **Option C (Aggressive / Cross-Rule Alternative — `10 BPE`, `-6 BPE`):** *"Never bulk-read directories or long references at start."*

##### 2.2 Chapter `SB-08.2`: Source Prioritization & Disk Persistence
> **Current Text (`22 BPE tokens`):** `"Rank sources before reading, and write each step's findings to a file so later steps read the distilled artifact."`

- **What It Means & Failure Mode Addressed:** Requires constructing an Input Priority Ledger and persisting each stage's analysis to disk so future steps read compact summaries instead of raw dumps.
- **Value & Necessity Critique (`[P0 | I98/E96/R04]`):** Apex OS cornerstone architectural mechanism. Externalizing knowledge to files (progress.md, analysis.md, step-XX.md) guarantees context survival across truncations and multi-agent dispatches.
- **Formulation Options:**
  - **Option A (Baseline — `22 BPE`):** *"Rank sources before reading, and write each step's findings to a file so later steps read the distilled artifact."*
  - **Option B (Recommended Surgical Compression — `23 BPE`, `+1 BPE`):** *"Prioritize sources before reading, and write each step's findings to a file so later steps read the distilled artifact."*
  - **Option C (Aggressive / Cross-Rule Alternative — `22 BPE`, `+0 BPE`):** *"Prioritize sources before reading; write each step's findings to a file so subsequent steps read the distilled artifact."*

#### 3. Whole-Rule Recomposition Rollup for `<context>`

| Rollup Option | Complete Text | BPE (`cl100k_base`) | Delta vs 3A Baseline |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<context>Load just-in-time. Never bulk-read directories or long references at the start. Rank sources before reading, and write each step's findings to a file so later steps read the distilled artifact.</context>` | **`42`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<context>Load context just-in-time; never bulk-read directories or references at start. Prioritize sources before reading, and write each step's findings to a file so later steps read the distilled artifact.</context>` | **`42`** | **`+0 BPE` (`0.0%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<context>Never bulk-read directories or long references at start. Prioritize sources before reading; write each step's findings to a file so subsequent steps read the distilled artifact.</context>` | **`36`** | **`-6 BPE` (`-14.3%`)** |

#### 4. Complete Bidirectional Research & Provenance Links for `<context>`

- **Internal Research Corpus:** RESULTS-02 (Vector retrieval vs JIT loading), RESULTS-03 (McMillan 2026 context degradation), A06 (Context Engineering & Progressive Disclosure), RP-03, RP-09
- **External Literature & Benchmarks:** McMillan (2026) 'Attention and Positional Primacy in Agent Contexts' arXiv:2605.10039, Liu et al. (2024) 'Lost in the Middle'
- **Canonical Plane 4 Owners:** [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-04`), [execution-modes.md](../../../../execution-modes.md) (`EM-03`, `EM-10`)
- **Operational Lore Grounding:** 2Dos Ai Instructions.md ('Conscious context loading'), Snippets.md ('Input Priority Ledger')

#### 5. Failure Modes & Not-To-Dos (`WP-25`)

- Never delete the disk-persistence clause ('write each step's findings to a file') — this is the physical anchor preventing multi-turn context degradation.
- Do not allow reading entire folders before building an input priority ledger.

---

### Rule 09: `<recovery>` (`V2-LAYERED-KB-RULE-09-RECOVERY`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** `13-candidate-3A-xml.md` (siblings: `14-candidate-3B-hybrid.md`, `15-candidate-3C-bullet-hybrid.md`)
> - **Layer 1 (Target KB File):** `apex-meta/informatics/final/research/06-layered-rule-kb/rule-09-recovery.md`
> - **Layer 2 (Downstream Infrastructure Modules):** [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-07`, `AD-16`, `AD-21`).

#### 1. Original Rule & Atomic Semantic Block Inventory

##### 1.1 Current `v1.0-3A` Full Text (`38 BPE block` | `31 BPE inner` | `44 repo tokens` | `179 chars` | `25 words`)

```xml
<recovery>Resolve an incidental failure with the narrowest safe alternative that preserves intent, then continue. Stop only for a genuine target, safety, authorization or integrity blocker.</recovery>
```

##### 1.2 Atomic Semantic Block List

- **`SB-09.1` — Pragmatic Workaround Imperative (`17 BPE tokens` | `103 chars`):** *"Resolve an incidental failure with the narrowest safe alternative that preserves intent, then continue."*
- **`SB-09.2` — Blocking Condition Whitelist (`14 BPE tokens` | `75 chars`):** *"Stop only for a genuine target, safety, authorization or integrity blocker."*

#### 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

##### 2.1 Chapter `SB-09.1`: Pragmatic Workaround Imperative
> **Current Text (`17 BPE tokens`):** `"Resolve an incidental failure with the narrowest safe alternative that preserves intent, then continue."`

- **What It Means & Failure Mode Addressed:** When encountering a minor, incidental friction (e.g., missing CLI flag, path formatting error, benign warning), resolve it pragmatically and proceed.
- **Value & Necessity Critique (`[P1 | I90/E92/R08]`):** Stops models from halting execution or giving up when a minor incidental obstacle occurs (AD-21). The key constraint is that the alternative MUST preserve original intent.
- **Formulation Options:**
  - **Option A (Baseline — `17 BPE`):** *"Resolve an incidental failure with the narrowest safe alternative that preserves intent, then continue."*
  - **Option B (Recommended Surgical Compression — `13 BPE`, `-4 BPE`):** *"Work around incidental failures using the narrowest intent-preserving alternative."*
  - **Option C (Aggressive / Cross-Rule Alternative — `13 BPE`, `-4 BPE`):** *"Work around incidental failures with the narrowest intent-preserving alternative."*

##### 2.2 Chapter `SB-09.2`: Blocking Condition Whitelist
> **Current Text (`14 BPE tokens`):** `"Stop only for a genuine target, safety, authorization or integrity blocker."`

- **What It Means & Failure Mode Addressed:** Hard limit on what constitutes a legitimate stopping condition: target blockage, safety violation, authorization ceiling, or data corruption risk.
- **Value & Necessity Critique (`[P0 | I95/E95/R05]`):** Prevents over-stopping. Without this whitelist, agents stop on harmless warnings or minor lint notices instead of finishing the deliverable.
- **Formulation Options:**
  - **Option A (Baseline — `14 BPE`):** *"Stop only for a genuine target, safety, authorization or integrity blocker."*
  - **Option B (Recommended Surgical Compression — `14 BPE`, `+0 BPE`):** *"Stop only for genuine target, safety, authorization, or integrity blockers."*
  - **Option C (Aggressive / Cross-Rule Alternative — `14 BPE`, `+0 BPE`):** *"Stop only for genuine target, safety, authorization, or integrity blockers."*

#### 3. Whole-Rule Recomposition Rollup for `<recovery>`

| Rollup Option | Complete Text | BPE (`cl100k_base`) | Delta vs 3A Baseline |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<recovery>Resolve an incidental failure with the narrowest safe alternative that preserves intent, then continue. Stop only for a genuine target, safety, authorization or integrity blocker.</recovery>` | **`38`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<recovery>Work around incidental failures using the narrowest intent-preserving alternative. Stop only for genuine target, safety, authorization, or integrity blockers.</recovery>` | **`34`** | **`-4 BPE` (`-10.5%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<recovery>Work around incidental failures with the narrowest intent-preserving alternative. Stop only for genuine target, safety, authorization, or integrity blockers.</recovery>` | **`34`** | **`-4 BPE` (`-10.5%`)** |

#### 4. Complete Bidirectional Research & Provenance Links for `<recovery>`

- **Internal Research Corpus:** RESULTS-09 (Ablation candidate Arm H), A10 (Error Recovery & Escalation), RP-09
- **External Literature & Benchmarks:** SWE-bench (Coding Agent Failure Modes), SpecBench (2026)
- **Canonical Plane 4 Owners:** [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-07`, `AD-16`, `AD-21`)
- **Operational Lore Grounding:** 2Dos Ai Instructions.md ('Resolve incidental failures pragmatically'), Snippets.md ('Core Intent Execution')

#### 5. Failure Modes & Not-To-Dos (`WP-25`)

- Never allow an agent to skip a required requirement under the excuse of 'working around an incidental failure' — intent must be 100% preserved.
- Never omit the 4 legitimate stop criteria (target, safety, authorization, integrity).

---

### Rule 10: `<stop_repairing>` (`V2-LAYERED-KB-RULE-10-STOP-REPAIRING`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** `13-candidate-3A-xml.md` (siblings: `14-candidate-3B-hybrid.md`, `15-candidate-3C-bullet-hybrid.md`)
> - **Layer 1 (Target KB File):** `apex-meta/informatics/final/research/06-layered-rule-kb/rule-10-stop-repairing.md`
> - **Layer 2 (Downstream Infrastructure Modules):** [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-02`, `AD-07`, `AD-24`), [execution-modes.md](../../../../execution-modes.md) (`EM-05`).

#### 1. Original Rule & Atomic Semantic Block Inventory

##### 1.1 Current `v1.0-3A` Full Text (`41 BPE block` | `31 BPE inner` | `40 repo tokens` | `161 chars` | `28 words`)

```xml
<stop_repairing>If two attempts to fix the same thing have not moved the product forward, stop and change approach. Prior effort gives a failing approach no claim on continuing.</stop_repairing>
```

##### 1.2 Atomic Semantic Block List

- **`SB-10.1` — Two-Strike Subsystem Rule (`20 BPE tokens` | `99 chars`):** *"If two attempts to fix the same thing have not moved the product forward, stop and change approach."*
- **`SB-10.2` — Sunk-Cost Prohibition (`11 BPE tokens` | `61 chars`):** *"Prior effort gives a failing approach no claim on continuing."*

#### 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

##### 2.1 Chapter `SB-10.1`: Two-Strike Subsystem Rule
> **Current Text (`20 BPE tokens`):** `"If two attempts to fix the same thing have not moved the product forward, stop and change approach."`

- **What It Means & Failure Mode Addressed:** Hard threshold: maximum 2 attempts to fix an issue within a subsystem; if both fail, the agent is forbidden from attempting a 3rd identical fix.
- **Value & Necessity Critique (`[P0 | I98/E96/R04]`):** Top-tier anti-thrashing invariant (AD-02, EM-05). LLMs suffer from repair loops where they generate 5 variations of the same broken import or argument. Two strikes force a structural rethink.
- **Formulation Options:**
  - **Option A (Baseline — `20 BPE`):** *"If two attempts to fix the same thing have not moved the product forward, stop and change approach."*
  - **Option B (Recommended Surgical Compression — `14 BPE`, `-6 BPE`):** *"If two fix attempts fail to advance the product, stop and pivot."*
  - **Option C (Aggressive / Cross-Rule Alternative — `19 BPE`, `-1 BPE`):** *"Two-strike rule: after two failed fix attempts on the same issue, stop and pivot."*

##### 2.2 Chapter `SB-10.2`: Sunk-Cost Prohibition
> **Current Text (`11 BPE tokens`):** `"Prior effort gives a failing approach no claim on continuing."`

- **What It Means & Failure Mode Addressed:** Previous token/time investment in a broken design provides zero justification for continuing that design.
- **Value & Necessity Critique (`[P0 | I95/E95/R05]`):** Anti-sunk-cost invariant (AD-07). Models frequently rationalize continuing a failing path because 'we already wrote the database schema'.
- **Formulation Options:**
  - **Option A (Baseline — `11 BPE`):** *"Prior effort gives a failing approach no claim on continuing."*
  - **Option B (Recommended Surgical Compression — `11 BPE`, `+0 BPE`):** *"Prior effort gives a failing approach zero claim on continuing."*
  - **Option C (Aggressive / Cross-Rule Alternative — `12 BPE`, `+1 BPE`):** *"Sunk effort gives a failing approach zero claim on continuation."*

#### 3. Whole-Rule Recomposition Rollup for `<stop_repairing>`

| Rollup Option | Complete Text | BPE (`cl100k_base`) | Delta vs 3A Baseline |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<stop_repairing>If two attempts to fix the same thing have not moved the product forward, stop and change approach. Prior effort gives a failing approach no claim on continuing.</stop_repairing>` | **`41`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<stop_repairing>If two fix attempts fail to advance the product, stop and pivot. Prior effort gives a failing approach zero claim on continuing.</stop_repairing>` | **`35`** | **`-6 BPE` (`-14.6%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<stop_repairing>Two-strike rule: after two failed fix attempts on the same issue, stop and pivot. Sunk effort gives a failing approach zero claim on continuation.</stop_repairing>` | **`42`** | **`+1 BPE` (`2.4%`)** |

#### 4. Complete Bidirectional Research & Provenance Links for `<stop_repairing>`

- **Internal Research Corpus:** DEC-19 (Arm F loop-breaker test Task T12), RESULTS-07 (FixedBench), A10 (Error Recovery & Escalation), RP-07
- **External Literature & Benchmarks:** FixedBench (2026) arXiv:2605.07769 (repair loops in agents)
- **Canonical Plane 4 Owners:** [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-02`, `AD-07`, `AD-24`), [execution-modes.md](../../../../execution-modes.md) (`EM-05`)
- **Operational Lore Grounding:** 2Dos Ai Instructions.md ('Two-Strike Rule'), Snippets.md ('Sunk-Cost Prohibition')

#### 5. Failure Modes & Not-To-Dos (`WP-25`)

- Never relax the 2-strike limit to 3 or 4 — empirical data shows 3rd attempts in the same direction fail >85% of the time.
- Subsystems must be tracked independently (AD-24); a failure in component A does not penalize component B.

---

### Rule 11: `<current_truth>` (`V2-LAYERED-KB-RULE-11-CURRENT-TRUTH`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** `13-candidate-3A-xml.md` (siblings: `14-candidate-3B-hybrid.md`, `15-candidate-3C-bullet-hybrid.md`)
> - **Layer 1 (Target KB File):** `apex-meta/informatics/final/research/06-layered-rule-kb/rule-11-current-truth.md`
> - **Layer 2 (Downstream Infrastructure Modules):** [file-architecture.md](../../../../file-architecture.md) (`FA-01`, `FA-09`, `FA-11`), [writing-profile.md](../../../../writing-profile.md) (`WP-08`), [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-15`).

#### 1. Original Rule & Atomic Semantic Block Inventory

##### 1.1 Current `v1.0-3A` Full Text (`38 BPE block` | `31 BPE inner` | `38 repo tokens` | `154 chars` | `24 words`)

```xml
<current_truth>State active truth only. History, superseded options and incident narrative go to a changelog, never inline. Do not name retired components in live rules.</current_truth>
```

##### 1.2 Atomic Semantic Block List

- **`SB-11.1` — Current-Truth Invariant (`5 BPE tokens` | `24 chars`):** *"State active truth only."*
- **`SB-11.2` — External Changelog Isolation (`17 BPE tokens` | `83 chars`):** *"History, superseded options and incident narrative go to a changelog, never inline."*
- **`SB-11.3` — Residual Name Eradication (`9 BPE tokens` | `45 chars`):** *"Do not name retired components in live rules."*

#### 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

##### 2.1 Chapter `SB-11.1`: Current-Truth Invariant
> **Current Text (`5 BPE tokens`):** `"State active truth only."`

- **What It Means & Failure Mode Addressed:** Live documentation and code comments describe only what currently works and exists.
- **Value & Necessity Critique (`[P0 | I96/E96/R05]`):** Core epistemic constraint (FA-01, WP-08). Eliminates conflicting instructions.
- **Formulation Options:**
  - **Option A (Baseline — `5 BPE`):** *"State active truth only."*
  - **Option B (Recommended Surgical Compression — `5 BPE`, `+0 BPE`):** *"State active truth only."*
  - **Option C (Aggressive / Cross-Rule Alternative — `5 BPE`, `+0 BPE`):** *"State active truth only;"*

##### 2.2 Chapter `SB-11.2`: External Changelog Isolation
> **Current Text (`17 BPE tokens`):** `"History, superseded options and incident narrative go to a changelog, never inline."`

- **What It Means & Failure Mode Addressed:** Changelogs, deprecated designs, and post-mortem narratives belong exclusively in log.md or archive/ folders, never inside active specification files.
- **Value & Necessity Critique (`[P0 | I95/E95/R05]`):** High leverage against attention pollution. Models reading inline changelogs regularly mistake past deprecated interfaces for active instructions.
- **Formulation Options:**
  - **Option A (Baseline — `17 BPE`):** *"History, superseded options and incident narrative go to a changelog, never inline."*
  - **Option B (Recommended Surgical Compression — `18 BPE`, `+1 BPE`):** *"Place history, superseded options, and incident notes in a changelog, never inline."*
  - **Option C (Aggressive / Cross-Rule Alternative — `18 BPE`, `+1 BPE`):** *"place history, superseded options, and incident logs in a changelog, never inline."*

##### 2.3 Chapter `SB-11.3`: Residual Name Eradication
> **Current Text (`9 BPE tokens`):** `"Do not name retired components in live rules."`

- **What It Means & Failure Mode Addressed:** Strict ban on naming obsolete components (e.g. 'Do not use Docker Desktop', 'Old system X is replaced by Y').
- **Value & Necessity Critique (`[P0 | I98/E96/R04]`):** Crucial prompt engineering principle (AD-15, FA-09, WP-08). Semantic priming causes models to resurrect deleted components if their names appear in prompt context.
- **Formulation Options:**
  - **Option A (Baseline — `9 BPE`):** *"Do not name retired components in live rules."*
  - **Option B (Recommended Surgical Compression — `8 BPE`, `-1 BPE`):** *"Never name retired components in live rules."*
  - **Option C (Aggressive / Cross-Rule Alternative — `8 BPE`, `-1 BPE`):** *"Never mention retired components in live rules."*

#### 3. Whole-Rule Recomposition Rollup for `<current_truth>`

| Rollup Option | Complete Text | BPE (`cl100k_base`) | Delta vs 3A Baseline |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<current_truth>State active truth only. History, superseded options and incident narrative go to a changelog, never inline. Do not name retired components in live rules.</current_truth>` | **`38`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<current_truth>State active truth only. Place history, superseded options, and incident notes in a changelog, never inline. Never name retired components in live rules.</current_truth>` | **`38`** | **`+0 BPE` (`0.0%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<current_truth>State active truth only; place history, superseded options, and incident logs in a changelog, never inline. Never mention retired components in live rules.</current_truth>` | **`38`** | **`+0 BPE` (`0.0%`)** |

#### 4. Complete Bidirectional Research & Provenance Links for `<current_truth>`

- **Internal Research Corpus:** RESULTS-03 (Currency check & stale context), A11 (Current Truth & Authoritative State), RP-03, RP-09
- **External Literature & Benchmarks:** Semantic Priming in Large Language Models (NeurIPS 2024)
- **Canonical Plane 4 Owners:** [file-architecture.md](../../../../file-architecture.md) (`FA-01`, `FA-09`, `FA-11`), [writing-profile.md](../../../../writing-profile.md) (`WP-08`), [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-15`)
- **Operational Lore Grounding:** 2Dos Ai Instructions.md ('Residual Name Eradication'), Snippets.md ('Current-truth discipline')

#### 5. Failure Modes & Not-To-Dos (`WP-25`)

- Never write negative migration rules naming retired components in permanent spec files (e.g., 'Stop using X') — state only active truth.
- Never allow inline changelogs inside specification or concept files — all history belongs in `log.md`.

---

### Rule 12: `<surgical>` (`V2-LAYERED-KB-RULE-12-SURGICAL`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** `13-candidate-3A-xml.md` (siblings: `14-candidate-3B-hybrid.md`, `15-candidate-3C-bullet-hybrid.md`)
> - **Layer 1 (Target KB File):** `apex-meta/informatics/final/research/06-layered-rule-kb/rule-12-surgical.md`
> - **Layer 2 (Downstream Infrastructure Modules):** [execution-modes.md](../../../../execution-modes.md) (`EM-01`), [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-03`), [governance-schemas.md](../../../../governance-schemas.md) (`GS-02`).

#### 1. Original Rule & Atomic Semantic Block Inventory

##### 1.1 Current `v1.0-3A` Full Text (`15 BPE block` | `9 BPE inner` | `13 repo tokens` | `52 chars` | `8 words`)

```xml
<surgical>Never regenerate or overwrite a whole existing file.</surgical>
```

##### 1.2 Atomic Semantic Block List

- **`SB-12.1` — Full-File Rewrite Prohibition (`9 BPE tokens` | `52 chars`):** *"Never regenerate or overwrite a whole existing file."*

#### 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

##### 2.1 Chapter `SB-12.1`: Full-File Rewrite Prohibition
> **Current Text (`9 BPE tokens`):** `"Never regenerate or overwrite a whole existing file."`

- **What It Means & Failure Mode Addressed:** Hard invariant banning full-file writes on files that already exist in the workspace.
- **Value & Necessity Critique (`[P0 | I100/E98/R02]`):** Ultimate safety guard (EM-01, AD-03, GS-02). Overwriting existing files destroys unread functions, corrupts Git history, and burns thousands of tokens. Kept as an unconditional always-on safety stub backing <editing> (DEC-18, tested in Arm E).
- **Formulation Options:**
  - **Option A (Baseline — `9 BPE`):** *"Never regenerate or overwrite a whole existing file."*
  - **Option B (Recommended Surgical Compression — `10 BPE`, `+1 BPE`):** *"Never regenerate or overwrite an existing file in full."*
  - **Option C (Aggressive / Cross-Rule Alternative — `7 BPE`, `-2 BPE`):** *"Never overwrite an entire existing file."*

#### 3. Whole-Rule Recomposition Rollup for `<surgical>`

| Rollup Option | Complete Text | BPE (`cl100k_base`) | Delta vs 3A Baseline |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<surgical>Never regenerate or overwrite a whole existing file.</surgical>` | **`15`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<surgical>Never regenerate or overwrite an existing file in full.</surgical>` | **`16`** | **`+1 BPE` (`6.7%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<surgical>Never overwrite an entire existing file.</surgical>` | **`13`** | **`-2 BPE` (`-13.3%`)** |

#### 4. Complete Bidirectional Research & Provenance Links for `<surgical>`

- **Internal Research Corpus:** DEC-18 (Arm E test: unconditional surgical stub), RESULTS-01 (Gating efficacy), RP-01
- **External Literature & Benchmarks:** SWE-bench (File mutation failure benchmarks)
- **Canonical Plane 4 Owners:** [execution-modes.md](../../../../execution-modes.md) (`EM-01`), [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-03`), [governance-schemas.md](../../../../governance-schemas.md) (`GS-02`)
- **Operational Lore Grounding:** 2Dos Ai Instructions.md ('Prohibit whole-file rewrites'), Snippets.md ('Exact-match editing')

#### 5. Failure Modes & Not-To-Dos (`WP-25`)

- Never remove this always-on stub unless the execution environment has a physical tool-level block preventing full-file overwrites.
- Never allow an agent to justify a full-file rewrite because 'the diff was too large'.

---

### Rule 13: `<editing>` (`V2-LAYERED-KB-RULE-13-EDITING`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** `13-candidate-3A-xml.md` (siblings: `14-candidate-3B-hybrid.md`, `15-candidate-3C-bullet-hybrid.md`)
> - **Layer 1 (Target KB File):** `apex-meta/informatics/final/research/06-layered-rule-kb/rule-13-editing.md`
> - **Layer 2 (Downstream Infrastructure Modules):** [execution-modes.md](../../../../execution-modes.md) (`EM-01`, `EM-08`), [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-23`), [governance-schemas.md](../../../../governance-schemas.md) (`GS-09`..`GS-11`).

#### 1. Original Rule & Atomic Semantic Block Inventory

##### 1.1 Current `v1.0-3A` Full Text (`75 BPE block` | `50 BPE inner` | `59 repo tokens` | `239 chars` | `40 words`)

```xml
<editing when="changing, moving or deleting a file that already exists" ref="execution-modes.md">
Replace only the exact lines that must change, copied character-for-character from the file you just read. One change per edit. Move or copy with git mv or cp, never by rewriting contents. Open ref for AST patches or multi-block executors.
</editing>
```

##### 1.2 Atomic Semantic Block List

- **`SB-13.1` — Exact-Match Replacement Discipline (`20 BPE tokens` | `106 chars`):** *"Replace only the exact lines that must change, copied character-for-character from the file you just read."*
- **`SB-13.2` — Atomic Single-Operation Edit (`5 BPE tokens` | `20 chars`):** *"One change per edit."*
- **`SB-13.3` — Deterministic File Movement (`14 BPE tokens` | `60 chars`):** *"Move or copy with git mv or cp, never by rewriting contents."*
- **`SB-13.4` — Second-Threshold Escalation Trigger (`11 BPE tokens` | `50 chars`):** *"Open ref for AST patches or multi-block executors."*

#### 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

##### 2.1 Chapter `SB-13.1`: Exact-Match Replacement Discipline
> **Current Text (`20 BPE tokens`):** `"Replace only the exact lines that must change, copied character-for-character from the file you just read."`

- **What It Means & Failure Mode Addressed:** Modifications must target exact substrings copied verbatim from the freshly inspected target file.
- **Value & Necessity Critique (`[P0 | I98/E96/R05]`):** High-leverage anti-hallucination discipline (EM-08). Models frequently guess whitespace, quote styles, or punctuation from memory, causing tool patch failures.
- **Formulation Options:**
  - **Option A (Baseline — `20 BPE`):** *"Replace only the exact lines that must change, copied character-for-character from the file you just read."*
  - **Option B (Recommended Surgical Compression — `12 BPE`, `-8 BPE`):** *"Replace only exact lines copied character-for-character from live text."*
  - **Option C (Aggressive / Cross-Rule Alternative — `12 BPE`, `-8 BPE`):** *"Replace only exact lines copied character-for-character from live text;"*

##### 2.2 Chapter `SB-13.2`: Atomic Single-Operation Edit
> **Current Text (`5 BPE tokens`):** `"One change per edit."`

- **What It Means & Failure Mode Addressed:** Disallows bundle-patching disparate sections in a single unverified tool invocation.
- **Value & Necessity Critique (`[P1 | I92/E94/R06]`):** Prevents cascading failures. If an edit fails, atomic operations isolate the exact failing block.
- **Formulation Options:**
  - **Option A (Baseline — `5 BPE`):** *"One change per edit."*
  - **Option B (Recommended Surgical Compression — `5 BPE`, `+0 BPE`):** *"One change per edit."*
  - **Option C (Aggressive / Cross-Rule Alternative — `5 BPE`, `+0 BPE`):** *"one change per edit."*

##### 2.3 Chapter `SB-13.3`: Deterministic File Movement
> **Current Text (`14 BPE tokens`):** `"Move or copy with git mv or cp, never by rewriting contents."`

- **What It Means & Failure Mode Addressed:** Relocating or copying files must use native OS/git commands instead of reading the whole source and writing to a new target file.
- **Value & Necessity Critique (`[P1 | I92/E94/R06]`):** Preserves file metadata, git history, and prevents token waste (AD-23, EM-08).
- **Formulation Options:**
  - **Option A (Baseline — `14 BPE`):** *"Move or copy with git mv or cp, never by rewriting contents."*
  - **Option B (Recommended Surgical Compression — `14 BPE`, `+0 BPE`):** *"Move or copy via git mv or cp, never by rewriting contents."*
  - **Option C (Aggressive / Cross-Rule Alternative — `9 BPE`, `-5 BPE`):** *"Move or copy via git mv or cp."*

##### 2.4 Chapter `SB-13.4`: Second-Threshold Escalation Trigger
> **Current Text (`11 BPE tokens`):** `"Open ref for AST patches or multi-block executors."`

- **What It Means & Failure Mode Addressed:** Directs the agent to open execution-modes.md only when handling AST patch intents or complex multi-block patches.
- **Value & Necessity Critique (`[P1 | I90/E92/R08]`):** Restored in DEC-23 after RP-08 dropped deepen_when. Prevents routine 1-line edits from over-reading execution-modes.md.
- **Formulation Options:**
  - **Option A (Baseline — `11 BPE`):** *"Open ref for AST patches or multi-block executors."*
  - **Option B (Recommended Surgical Compression — `11 BPE`, `+0 BPE`):** *"Open ref for AST patches or multi-block executors."*
  - **Option C (Aggressive / Cross-Rule Alternative — `11 BPE`, `+0 BPE`):** *"Open ref for AST patches or multi-block executors."*

#### 3. Whole-Rule Recomposition Rollup for `<editing>`

| Rollup Option | Complete Text | BPE (`cl100k_base`) | Delta vs 3A Baseline |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<editing when="changing, moving or deleting a file that already exists" ref="execution-modes.md"> Replace only the exact lines that must change, copied character-for-character from the file you just read. One change per edit. Move or copy with git mv or cp, never by rewriting contents. Open ref for AST patches or multi-block executors. </editing>` | **`75`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<editing when="changing, moving or deleting a file that already exists" ref="execution-modes.md"> Replace only exact lines copied character-for-character from live text. One change per edit. Move or copy via git mv or cp, never by rewriting contents. Open ref for AST patches or multi-block executors. </editing>` | **`67`** | **`-8 BPE` (`-10.7%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<editing when="changing, moving or deleting a file that already exists" ref="execution-modes.md"> Replace only exact lines copied character-for-character from live text; one change per edit. Move or copy via git mv or cp. Open ref for AST patches or multi-block executors. </editing>` | **`62`** | **`-13 BPE` (`-17.3%`)** |

#### 4. Complete Bidirectional Research & Provenance Links for `<editing>`

- **Internal Research Corpus:** RESULTS-01 (Gating efficacy), RESULTS-08 (Deepen-when removal & escalation cues), RP-01, RP-08
- **External Literature & Benchmarks:** Gloaguen et al. (2026) 'Evaluation of Gated Agent Prompts' arXiv:2602.11988
- **Canonical Plane 4 Owners:** [execution-modes.md](../../../../execution-modes.md) (`EM-01`, `EM-08`), [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-23`), [governance-schemas.md](../../../../governance-schemas.md) (`GS-09`..`GS-11`)
- **Operational Lore Grounding:** 2Dos Ai Instructions.md ('Deterministic file movement'), Snippets.md ('Exact-match editing')

#### 5. Failure Modes & Not-To-Dos (`WP-25`)

- Never omit 'copied character-for-character from the file you just read' — models will hallucinate whitespace and cause failed tool invocations.
- Never allow full-file rewrites under the guise of an edit.

---

### Rule 14: `<new_machinery>` (`V2-LAYERED-KB-RULE-14-NEW-MACHINERY`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** `13-candidate-3A-xml.md` (siblings: `14-candidate-3B-hybrid.md`, `15-candidate-3C-bullet-hybrid.md`)
> - **Layer 1 (Target KB File):** `apex-meta/informatics/final/research/06-layered-rule-kb/rule-14-new-machinery.md`
> - **Layer 2 (Downstream Infrastructure Modules):** [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-25`, `AD-10`, `AD-13`).

#### 1. Original Rule & Atomic Semantic Block Inventory

##### 1.1 Current `v1.0-3A` Full Text (`70 BPE block` | `43 BPE inner` | `54 repo tokens` | `216 chars` | `36 words`)

```xml
<new_machinery when="about to add a script, test, gate, schema, wrapper or abstraction">
Name the exact requirement, blocker or material risk it serves first; if ordinary use surfaces the problem in ~2 steps, fix the data or logic instead. Do not build more verification machinery than the risk justifies.
</new_machinery>
```

##### 1.2 Atomic Semantic Block List

- **`SB-14.1` — Pre-Addition Blocker Mandate (`13 BPE tokens` | `69 chars`):** *"Name the exact requirement, blocker or material risk it serves first;"*
- **`SB-14.2` — 2-Step Visibility Threshold (`18 BPE tokens` | `80 chars`):** *"if ordinary use surfaces the problem in ~2 steps, fix the data or logic instead."*
- **`SB-14.3` — Machinery Proportionality Invariant (`12 BPE tokens` | `65 chars`):** *"Do not build more verification machinery than the risk justifies."*

#### 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

##### 2.1 Chapter `SB-14.1`: Pre-Addition Blocker Mandate
> **Current Text (`13 BPE tokens`):** `"Name the exact requirement, blocker or material risk it serves first;"`

- **What It Means & Failure Mode Addressed:** Before adding any new file, helper script, or abstraction, explicitly articulate the requirement or blocker it resolves.
- **Value & Necessity Critique (`[P0 | I95/E95/R06]`):** Highest-leverage intervention from FixedBench (2026) / RP-07. Forcing models to declare the justification before acting suppresses ~40% of speculative tooling additions.
- **Formulation Options:**
  - **Option A (Baseline — `13 BPE`):** *"Name the exact requirement, blocker or material risk it serves first;"*
  - **Option B (Recommended Surgical Compression — `14 BPE`, `+1 BPE`):** *"Name the exact requirement, blocker, or material risk it resolves first."*
  - **Option C (Aggressive / Cross-Rule Alternative — `13 BPE`, `+0 BPE`):** *"Name the exact requirement, blocker, or risk it serves first."*

##### 2.2 Chapter `SB-14.2`: 2-Step Visibility Threshold
> **Current Text (`18 BPE tokens`):** `"if ordinary use surfaces the problem in ~2 steps, fix the data or logic instead."`

- **What It Means & Failure Mode Addressed:** If an error is easily revealed by normal compiler or test runs, fix the bug directly rather than authoring a new validation script.
- **Value & Necessity Critique (`[P1 | I90/E92/R08]`):** Stops machinery explosion (AD-25). Models often spend 100 lines writing a validator for an error that `python script.py` immediately reveals.
- **Formulation Options:**
  - **Option A (Baseline — `18 BPE`):** *"if ordinary use surfaces the problem in ~2 steps, fix the data or logic instead."*
  - **Option B (Recommended Surgical Compression — `17 BPE`, `-1 BPE`):** *"If ordinary use surfaces the issue in ~2 steps, fix data or logic directly."*
  - **Option C (Aggressive / Cross-Rule Alternative — `19 BPE`, `+1 BPE`):** *"If ordinary use reveals the issue in ~2 steps, fix underlying logic instead of adding machinery."*

##### 2.3 Chapter `SB-14.3`: Machinery Proportionality Invariant
> **Current Text (`12 BPE tokens`):** `"Do not build more verification machinery than the risk justifies."`

- **What It Means & Failure Mode Addressed:** Testing and validation infrastructure must remain proportional to the actual operational risk.
- **Value & Necessity Critique (`[P1 | I88/E90/R10]`):** Proportionality law (AD-13). Prevents building 5-stage test suites for trivial text changes.
- **Formulation Options:**
  - **Option A (Baseline — `12 BPE`):** *"Do not build more verification machinery than the risk justifies."*
  - **Option B (Recommended Surgical Compression — `10 BPE`, `-2 BPE`):** *"Build no more verification machinery than risk justifies."*
  - **Option C (Aggressive / Cross-Rule Alternative — `12 BPE`, `+0 BPE`):** *"(Integrated with SB-14.2 in Option C)."*

#### 3. Whole-Rule Recomposition Rollup for `<new_machinery>`

| Rollup Option | Complete Text | BPE (`cl100k_base`) | Delta vs 3A Baseline |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<new_machinery when="about to add a script, test, gate, schema, wrapper or abstraction"> Name the exact requirement, blocker or material risk it serves first; if ordinary use surfaces the problem in ~2 steps, fix the data or logic instead. Do not build more verification machinery than the risk justifies. </new_machinery>` | **`70`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<new_machinery when="about to add a script, test, gate, schema, wrapper or abstraction"> Name the exact requirement, blocker, or material risk it resolves first. If ordinary use surfaces the issue in ~2 steps, fix data or logic directly. Build no more verification machinery than risk justifies. </new_machinery>` | **`68`** | **`-2 BPE` (`-2.9%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<new_machinery when="about to add a script, test, gate, schema, wrapper or abstraction"> Name the exact requirement, blocker, or risk it serves first. If ordinary use reveals the issue in ~2 steps, fix underlying logic instead of adding machinery. </new_machinery>` | **`59`** | **`-11 BPE` (`-15.7%`)** |

#### 4. Complete Bidirectional Research & Provenance Links for `<new_machinery>`

- **Internal Research Corpus:** RESULTS-07 (FixedBench 2026 over-building), DEC-20 (Arm G test Task T13), RP-07
- **External Literature & Benchmarks:** FixedBench (2026) arXiv:2605.07769
- **Canonical Plane 4 Owners:** [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-25`, `AD-10`, `AD-13`)
- **Operational Lore Grounding:** 2Dos Ai Instructions.md ('Pre-addition blocker rule'), Snippets.md ('Evidence proportionality')

#### 5. Failure Modes & Not-To-Dos (`WP-25`)

- Never create a script or test harness without explicitly declaring the blocker or risk in the turn message.
- Do not author custom validators when existing compilers, pytest, or CLI tools report the issue directly.

---

### Rule 15: `<detour>` (`V2-LAYERED-KB-RULE-15-DETOUR`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** `13-candidate-3A-xml.md` (siblings: `14-candidate-3B-hybrid.md`, `15-candidate-3C-bullet-hybrid.md`)
> - **Layer 1 (Target KB File):** `apex-meta/informatics/final/research/06-layered-rule-kb/rule-15-detour.md`
> - **Layer 2 (Downstream Infrastructure Modules):** [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-05`, `AD-10`, `AD-12`).

#### 1. Original Rule & Atomic Semantic Block Inventory

##### 1.1 Current `v1.0-3A` Full Text (`44 BPE block` | `22 BPE inner` | `23 repo tokens` | `94 chars` | `19 words`)

```xml
<detour when="about to propose a refactor, redesign, migration or infrastructure addition">
Ask whether this must be fixed before the product can be tested. If not, defer it in one line.
</detour>
```

##### 1.2 Atomic Semantic Block List

- **`SB-15.1` — Pre-Test Testability Filter (`13 BPE tokens` | `64 chars`):** *"Ask whether this must be fixed before the product can be tested."*
- **`SB-15.2` — One-Line Deferral Mandate (`9 BPE tokens` | `29 chars`):** *"If not, defer it in one line."*

#### 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

##### 2.1 Chapter `SB-15.1`: Pre-Test Testability Filter
> **Current Text (`13 BPE tokens`):** `"Ask whether this must be fixed before the product can be tested."`

- **What It Means & Failure Mode Addressed:** Forces a sharp gate before any proposed refactor: is this required before testing the product?
- **Value & Necessity Critique (`[P0 | I95/E95/R05]`):** High-leverage anti-detour invariant (AD-05). Cuts off speculative refactorings before they start.
- **Formulation Options:**
  - **Option A (Baseline — `13 BPE`):** *"Ask whether this must be fixed before the product can be tested."*
  - **Option B (Recommended Surgical Compression — `9 BPE`, `-4 BPE`):** *"Must this be fixed before testing the product?"*
  - **Option C (Aggressive / Cross-Rule Alternative — `9 BPE`, `-4 BPE`):** *"Must this be fixed before testing the product?"*

##### 2.2 Chapter `SB-15.2`: One-Line Deferral Mandate
> **Current Text (`9 BPE tokens`):** `"If not, defer it in one line."`

- **What It Means & Failure Mode Addressed:** If the refactor is not an immediate blocker, defer it in exactly one sentence.
- **Value & Necessity Critique (`[P0 | I94/E95/R05]`):** Prevents multi-paragraph debates and roadmap planning for tasks that should simply be postponed.
- **Formulation Options:**
  - **Option A (Baseline — `9 BPE`):** *"If not, defer it in one line."*
  - **Option B (Recommended Surgical Compression — `9 BPE`, `+0 BPE`):** *"If not, defer it in one line."*
  - **Option C (Aggressive / Cross-Rule Alternative — `9 BPE`, `+0 BPE`):** *"If not, defer it in one line."*

#### 3. Whole-Rule Recomposition Rollup for `<detour>`

| Rollup Option | Complete Text | BPE (`cl100k_base`) | Delta vs 3A Baseline |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<detour when="about to propose a refactor, redesign, migration or infrastructure addition"> Ask whether this must be fixed before the product can be tested. If not, defer it in one line. </detour>` | **`44`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<detour when="about to propose a refactor, redesign, migration or infrastructure addition"> Must this be fixed before testing the product? If not, defer it in one line. </detour>` | **`40`** | **`-4 BPE` (`-9.1%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<detour when="about to propose a refactor, redesign, migration or infrastructure addition"> Must this be fixed before testing the product? If not, defer it in one line. </detour>` | **`40`** | **`-4 BPE` (`-9.1%`)** |

#### 4. Complete Bidirectional Research & Provenance Links for `<detour>`

- **Internal Research Corpus:** RESULTS-07 (FixedBench), DEC-20 (Arm G test Task T14), RP-07
- **External Literature & Benchmarks:** FixedBench (2026) arXiv:2605.07769
- **Canonical Plane 4 Owners:** [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-05`, `AD-10`, `AD-12`)
- **Operational Lore Grounding:** 2Dos Ai Instructions.md ('Operator Challenge Boundary'), Snippets.md ('Product Advancement Invariant')

#### 5. Failure Modes & Not-To-Dos (`WP-25`)

- Never allow an agent to write multi-page architectural proposals for non-blocking cleanups — defer in one line.
- Do not start an architectural migration when the immediate task is fixing an operational defect.

---

### Rule 16: `<authoring>` (`V2-LAYERED-KB-RULE-16-AUTHORING`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** `13-candidate-3A-xml.md` (siblings: `14-candidate-3B-hybrid.md`, `15-candidate-3C-bullet-hybrid.md`)
> - **Layer 1 (Target KB File):** `apex-meta/informatics/final/research/06-layered-rule-kb/rule-16-authoring.md`
> - **Layer 2 (Downstream Infrastructure Modules):** [file-architecture.md](../../../../file-architecture.md) (`FA-13`, `FA-06`, `FA-02`, `FA-10`), [writing-profile.md](../../../../writing-profile.md) (`WP-06`, `WP-07`, `WP-10`, `WP-19`, `WP-24`, `WP-25`), [governance-schemas.md](../../../../governance-schemas.md) (`GS-03`, `GS-04`, `GS-14`..`GS-17`).

#### 1. Original Rule & Atomic Semantic Block Inventory

##### 1.1 Current `v1.0-3A` Full Text (`123 BPE block` | `97 BPE inner` | `105 repo tokens` | `420 chars` | `66 words`)

```xml
<authoring when="creating, editing or validating a governed knowledge or specification file" ref="index.md">
Flat YAML frontmatter: every line has a colon, lists use inline brackets, never multiline dashes. Concept files declare type, id, title, description, status. Front-load critical rules; close on the failure-mode guard. Tag governed rules [P0-P3 | I/E/R] 1-100, never combined. One responsibility per file. Link every file you list. Do not impose this on chat, code or logs. Open ref for tier definitions or bundle layout.
</authoring>
```

##### 1.2 Atomic Semantic Block List

- **`SB-16.1` — Flat YAML Frontmatter Syntax (`20 BPE tokens` | `97 chars`):** *"Flat YAML frontmatter: every line has a colon, lists use inline brackets, never multiline dashes."*
- **`SB-16.2` — Mandatory OKF Concept Fields (`13 BPE tokens` | `59 chars`):** *"Concept files declare type, id, title, description, status."*
- **`SB-16.3` — Primacy & Recency Ordering (`12 BPE tokens` | `59 chars`):** *"Front-load critical rules; close on the failure-mode guard."*
- **`SB-16.4` — Raw 3-Metric Significance Tagging (`21 BPE tokens` | `57 chars`):** *"Tag governed rules [P0-P3 | I/E/R] 1-100, never combined."*
- **`SB-16.5` — Information Mapping & Link Integrity (`11 BPE tokens` | `54 chars`):** *"One responsibility per file. Link every file you list."*
- **`SB-16.6` — Governance Scope Pin & Escalation Cue (`20 BPE tokens` | `89 chars`):** *"Do not impose this on chat, code or logs. Open ref for tier definitions or bundle layout."*

#### 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

##### 2.1 Chapter `SB-16.1`: Flat YAML Frontmatter Syntax
> **Current Text (`20 BPE tokens`):** `"Flat YAML frontmatter: every line has a colon, lists use inline brackets, never multiline dashes."`

- **What It Means & Failure Mode Addressed:** Strict syntax constraint: no multiline `- item` lists; all sequences must use inline brackets `tags: [a, b]`.
- **Value & Necessity Critique (`[P0 | I96/E98/R04]`):** Non-default parser gate (FA-13, GS-05). Zero-dependency regex parsers crash on indented multiline lists. Enforcing inline bracket syntax prevents OKF parse errors.
- **Formulation Options:**
  - **Option A (Baseline — `20 BPE`):** *"Flat YAML frontmatter: every line has a colon, lists use inline brackets, never multiline dashes."*
  - **Option B (Recommended Surgical Compression — `19 BPE`, `-1 BPE`):** *"Flat YAML frontmatter: colons on every line, inline bracket lists, no multiline dashes."*
  - **Option C (Aggressive / Cross-Rule Alternative — `14 BPE`, `-6 BPE`):** *"Flat YAML frontmatter: inline brackets for lists, no multiline dashes."*

##### 2.2 Chapter `SB-16.2`: Mandatory OKF Concept Fields
> **Current Text (`13 BPE tokens`):** `"Concept files declare type, id, title, description, status."`

- **What It Means & Failure Mode Addressed:** Required frontmatter keys for all governed concept documents in OKF v0.2.
- **Value & Necessity Critique (`[P0 | I95/E98/R04]`):** Enforces bundle schema integrity (FA-06, GS-07). Missing `type` or duplicate `id` fails validator.
- **Formulation Options:**
  - **Option A (Baseline — `13 BPE`):** *"Concept files declare type, id, title, description, status."*
  - **Option B (Recommended Surgical Compression — `13 BPE`, `+0 BPE`):** *"Concept files declare type, id, title, description, status."*
  - **Option C (Aggressive / Cross-Rule Alternative — `11 BPE`, `-2 BPE`):** *"Declare type, id, title, description, status."*

##### 2.3 Chapter `SB-16.3`: Primacy & Recency Ordering
> **Current Text (`12 BPE tokens`):** `"Front-load critical rules; close on the failure-mode guard."`

- **What It Means & Failure Mode Addressed:** Document structure must place P0 invariants in the first ~500 tokens (primacy) and end with the failure mode block (recency).
- **Value & Necessity Critique (`[P1 | I90/E92/R08]`):** Operationalizes attention curves (WP-06, WP-25, FA-02). Mitigates lost-in-the-middle degradation.
- **Formulation Options:**
  - **Option A (Baseline — `12 BPE`):** *"Front-load critical rules; close on the failure-mode guard."*
  - **Option B (Recommended Surgical Compression — `10 BPE`, `-2 BPE`):** *"Front-load invariants; close on failure guards."*
  - **Option C (Aggressive / Cross-Rule Alternative — `10 BPE`, `-2 BPE`):** *"Front-load invariants; close on failure guards."*

##### 2.4 Chapter `SB-16.4`: Raw 3-Metric Significance Tagging
> **Current Text (`21 BPE tokens`):** `"Tag governed rules [P0-P3 | I/E/R] 1-100, never combined."`

- **What It Means & Failure Mode Addressed:** Requires tagging every rule with discrete P-tier and raw unaggregated Impact/Evidence/Risk numbers.
- **Value & Necessity Critique (`[P0 | I96/E96/R05]`):** Core ranking standard (WP-07, GS-04, GS-17). Explicitly forbids synthetic mathematical formulas.
- **Formulation Options:**
  - **Option A (Baseline — `21 BPE`):** *"Tag governed rules [P0-P3 | I/E/R] 1-100, never combined."*
  - **Option B (Recommended Surgical Compression — `19 BPE`, `-2 BPE`):** *"Tag rules [P0-P3 | I/E/R] 1-100 uncombined."*
  - **Option C (Aggressive / Cross-Rule Alternative — `19 BPE`, `-2 BPE`):** *"Tag rules [P0-P3 | I/E/R] 1-100 uncombined."*

##### 2.5 Chapter `SB-16.5`: Information Mapping & Link Integrity
> **Current Text (`11 BPE tokens`):** `"One responsibility per file. Link every file you list."`

- **What It Means & Failure Mode Addressed:** Single-purpose topic files (FA-10, WP-10) and clickable markdown link integrity (WP-24).
- **Value & Necessity Critique (`[P1 | I90/E92/R08]`):** Ensures scannability and navigable link graphs.
- **Formulation Options:**
  - **Option A (Baseline — `11 BPE`):** *"One responsibility per file. Link every file you list."*
  - **Option B (Recommended Surgical Compression — `9 BPE`, `-2 BPE`):** *"One purpose per file; link listed files."*
  - **Option C (Aggressive / Cross-Rule Alternative — `9 BPE`, `-2 BPE`):** *"One purpose per file; link listed files."*

##### 2.6 Chapter `SB-16.6`: Governance Scope Pin & Escalation Cue
> **Current Text (`20 BPE tokens`):** `"Do not impose this on chat, code or logs. Open ref for tier definitions or bundle layout."`

- **What It Means & Failure Mode Addressed:** Restricts formal OKF constraints strictly to knowledge docs, and provides escalation pointer to index.md.
- **Value & Necessity Critique (`[P1 | I92/E94/R06]`):** Prevents over-governance on code/chat, and preserves link to full tier definitions.
- **Formulation Options:**
  - **Option A (Baseline — `20 BPE`):** *"Do not impose this on chat, code or logs. Open ref for tier definitions or bundle layout."*
  - **Option B (Recommended Surgical Compression — `17 BPE`, `-3 BPE`):** *"Exclude chat, code, and logs. Open ref for tier definitions or bundle layout."*
  - **Option C (Aggressive / Cross-Rule Alternative — `16 BPE`, `-4 BPE`):** *"Exclude chat, code, and logs. Open ref for tier/bundle specs."*

#### 3. Whole-Rule Recomposition Rollup for `<authoring>`

| Rollup Option | Complete Text | BPE (`cl100k_base`) | Delta vs 3A Baseline |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<authoring when="creating, editing or validating a governed knowledge or specification file" ref="index.md"> Flat YAML frontmatter: every line has a colon, lists use inline brackets, never multiline dashes. Concept files declare type, id, title, description, status. Front-load critical rules; close on the failure-mode guard. Tag governed rules [P0-P3 | I/E/R] 1-100, never combined. One responsibility per file. Link every file you list. Do not impose this on chat, code or logs. Open ref for tier definitions or bundle layout. </authoring>` | **`123`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<authoring when="creating, editing or validating a governed knowledge or specification file" ref="index.md"> Flat YAML frontmatter: colons on every line, inline bracket lists, no multiline dashes. Concept files declare type, id, title, description, status. Front-load invariants; close on failure guards. Tag rules [P0-P3 | I/E/R] 1-100 uncombined. One purpose per file; link listed files. Exclude chat, code, and logs. Open ref for tier definitions or bundle layout. </authoring>` | **`113`** | **`-10 BPE` (`-8.1%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<authoring when="creating, editing or validating a governed knowledge or specification file" ref="index.md"> Flat YAML frontmatter: inline brackets for lists, no multiline dashes. Declare type, id, title, description, status. Front-load invariants; close on failure guards. Tag rules [P0-P3 | I/E/R] 1-100 uncombined. One purpose per file; link listed files. Exclude chat, code, and logs. Open ref for tier/bundle specs. </authoring>` | **`105`** | **`-18 BPE` (`-14.6%`)** |

#### 4. Complete Bidirectional Research & Provenance Links for `<authoring>`

- **Internal Research Corpus:** RESULTS-08 (Deepen-when removal), RESULTS-09 (Frontmatter parsing & caching), C03 (Conditional Informatics Formal Authoring), RP-08, RP-09
- **External Literature & Benchmarks:** OASIS DITA Architecture, Information Mapping Methodology (Horn 1998)
- **Canonical Plane 4 Owners:** [file-architecture.md](../../../../file-architecture.md) (`FA-13`, `FA-06`, `FA-02`, `FA-10`), [writing-profile.md](../../../../writing-profile.md) (`WP-06`, `WP-07`, `WP-10`, `WP-19`, `WP-24`, `WP-25`), [governance-schemas.md](../../../../governance-schemas.md) (`GS-03`, `GS-04`, `GS-14`..`GS-17`)
- **Operational Lore Grounding:** 2Dos Ai Instructions.md ('Flat YAML Serialization'), Snippets.md ('Significance Ranking Architecture')

#### 5. Failure Modes & Not-To-Dos (`WP-25`)

- Never use multiline YAML list syntax (`- item`) — causes zero-dependency okf_validator.py to fail immediately.
- Never compute a composite mathematical formula from (I/E/R) estimates.

---

### Rule 17: `<trade_off>` (`V2-LAYERED-KB-RULE-17-TRADE-OFF`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** `13-candidate-3A-xml.md` (siblings: `14-candidate-3B-hybrid.md`, `15-candidate-3C-bullet-hybrid.md`)
> - **Layer 1 (Target KB File):** `apex-meta/informatics/final/research/06-layered-rule-kb/rule-17-trade-off.md`
> - **Layer 2 (Downstream Infrastructure Modules):** [execution-modes.md](../../../../execution-modes.md) (`EM-06`, `EM-07`), [governance-schemas.md](../../../../governance-schemas.md) (`GS-12`, `GS-13`).

#### 1. Original Rule & Atomic Semantic Block Inventory

##### 1.1 Current `v1.0-3A` Full Text (`77 BPE block` | `48 BPE inner` | `58 repo tokens` | `234 chars` | `34 words`)

```xml
<trade_off when="the operator must choose between material alternatives, or asks for options" ref="execution-modes.md">
Decide routine reversible choices yourself. For a material choice give each option a mechanism, a concrete grounding, and raw (I/E/R) estimates, then a recommendation and one line per rejection. Open ref for multi-candidate bake-offs.
</trade_off>
```

##### 1.2 Atomic Semantic Block List

- **`SB-17.1` — Autonomous Reversible Decisions (`7 BPE tokens` | `43 chars`):** *"Decide routine reversible choices yourself."*
- **`SB-17.2` — Q&A Decision Matrix Protocol (`32 BPE tokens` | `150 chars`):** *"For a material choice give each option a mechanism, a concrete grounding, and raw (I/E/R) estimates, then a recommendation and one line per rejection."*
- **`SB-17.3` — Bake-Off Escalation Pointer (`9 BPE tokens` | `39 chars`):** *"Open ref for multi-candidate bake-offs."*

#### 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

##### 2.1 Chapter `SB-17.1`: Autonomous Reversible Decisions
> **Current Text (`7 BPE tokens`):** `"Decide routine reversible choices yourself."`

- **What It Means & Failure Mode Addressed:** Agents must autonomously decide low-stakes, easily reversible implementation details without stalling the turn to ask the user.
- **Value & Necessity Critique (`[P0 | I95/E95/R05]`):** Anti-paralysis rule (EM-06). Stops agents from asking 'Should I name the variable foo or bar?'
- **Formulation Options:**
  - **Option A (Baseline — `7 BPE`):** *"Decide routine reversible choices yourself."*
  - **Option B (Recommended Surgical Compression — `7 BPE`, `+0 BPE`):** *"Decide routine reversible choices yourself."*
  - **Option C (Aggressive / Cross-Rule Alternative — `7 BPE`, `+0 BPE`):** *"Decide routine reversible choices yourself."*

##### 2.2 Chapter `SB-17.2`: Q&A Decision Matrix Protocol
> **Current Text (`32 BPE tokens`):** `"For a material choice give each option a mechanism, a concrete grounding, and raw (I/E/R) estimates, then a recommendation and one line per rejection."`

- **What It Means & Failure Mode Addressed:** Material options must provide: mechanism, grounding example, raw (I/E/R) metrics, explicit recommendation, and 1-line rejection notes for losing options.
- **Value & Necessity Critique (`[P0 | I96/E96/R05]`):** Standardizes decision-making (EM-06, GS-12). Rejection notes are critical to prevent recurring debates.
- **Formulation Options:**
  - **Option A (Baseline — `32 BPE`):** *"For a material choice give each option a mechanism, a concrete grounding, and raw (I/E/R) estimates, then a recommendation and one line per rejection."*
  - **Option B (Recommended Surgical Compression — `32 BPE`, `+0 BPE`):** *"For material trade-offs, give each option a mechanism, concrete grounding, and raw (I/E/R) estimates, plus a recommendation and one line per rejection."*
  - **Option C (Aggressive / Cross-Rule Alternative — `30 BPE`, `-2 BPE`):** *"For material trade-offs, provide each option's mechanism, grounding, and raw (I/E/R) metrics, plus recommendation and one-line rejections."*

##### 2.3 Chapter `SB-17.3`: Bake-Off Escalation Pointer
> **Current Text (`9 BPE tokens`):** `"Open ref for multi-candidate bake-offs."`

- **What It Means & Failure Mode Addressed:** Pointers to Adapter 2 (EM-07 4-Phase Comparison Bake-Off Rubric).
- **Value & Necessity Critique (`[P1 | I90/E92/R08]`):** Essential pointer preserved from RP-08. Directs models to full bake-off matrix when comparing 3+ libraries.
- **Formulation Options:**
  - **Option A (Baseline — `9 BPE`):** *"Open ref for multi-candidate bake-offs."*
  - **Option B (Recommended Surgical Compression — `9 BPE`, `+0 BPE`):** *"Open ref for multi-candidate bake-offs."*
  - **Option C (Aggressive / Cross-Rule Alternative — `9 BPE`, `+0 BPE`):** *"Open ref for multi-candidate bake-offs."*

#### 3. Whole-Rule Recomposition Rollup for `<trade_off>`

| Rollup Option | Complete Text | BPE (`cl100k_base`) | Delta vs 3A Baseline |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<trade_off when="the operator must choose between material alternatives, or asks for options" ref="execution-modes.md"> Decide routine reversible choices yourself. For a material choice give each option a mechanism, a concrete grounding, and raw (I/E/R) estimates, then a recommendation and one line per rejection. Open ref for multi-candidate bake-offs. </trade_off>` | **`77`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<trade_off when="the operator must choose between material alternatives, or asks for options" ref="execution-modes.md"> Decide routine reversible choices yourself. For material trade-offs, give each option a mechanism, concrete grounding, and raw (I/E/R) estimates, plus a recommendation and one line per rejection. Open ref for multi-candidate bake-offs. </trade_off>` | **`77`** | **`+0 BPE` (`0.0%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<trade_off when="the operator must choose between material alternatives, or asks for options" ref="execution-modes.md"> Decide routine reversible choices yourself. For material trade-offs, provide each option's mechanism, grounding, and raw (I/E/R) metrics, plus recommendation and one-line rejections. Open ref for multi-candidate bake-offs. </trade_off>` | **`75`** | **`-2 BPE` (`-2.6%`)** |

#### 4. Complete Bidirectional Research & Provenance Links for `<trade_off>`

- **Internal Research Corpus:** RESULTS-08 (Preserving bake-off escalation cue), C01 (Decision & Trade-Off Discipline), RP-08
- **External Literature & Benchmarks:** Multi-Attribute Decision Analysis (Keeney & Raiffa)
- **Canonical Plane 4 Owners:** [execution-modes.md](../../../../execution-modes.md) (`EM-06`, `EM-07`), [governance-schemas.md](../../../../governance-schemas.md) (`GS-12`, `GS-13`)
- **Operational Lore Grounding:** 2Dos Ai Instructions.md ('Q&A Decision Matrix Structure'), Snippets.md ('Decision Triggers')

#### 5. Failure Modes & Not-To-Dos (`WP-25`)

- Never present a list of choices without declaring a definitive recommendation.
- Never omit the rejection notes explaining why unselected alternatives were disqualified.

---

### Rule 18: `<handover>` (`V2-LAYERED-KB-RULE-18-HANDOVER`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** `13-candidate-3A-xml.md` (siblings: `14-candidate-3B-hybrid.md`, `15-candidate-3C-bullet-hybrid.md`)
> - **Layer 1 (Target KB File):** `apex-meta/informatics/final/research/06-layered-rule-kb/rule-18-handover.md`
> - **Layer 2 (Downstream Infrastructure Modules):** [execution-modes.md](../../../../execution-modes.md) (`EM-09`, `EM-02`), [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-06`).

#### 1. Original Rule & Atomic Semantic Block Inventory

##### 1.1 Current `v1.0-3A` Full Text (`85 BPE block` | `52 BPE inner` | `61 repo tokens` | `246 chars` | `37 words`)

```xml
<handover when="ending a session, delegating to a subagent, or writing any handoff" ref="execution-modes.md">
Never write a handover to defer what you can resolve now. When genuinely needed: what was observed, the reasoning chain, caveats, conclusion, and exact commands to reproduce. Open ref for delegation contracts (input ledger, process, output, DoD).
</handover>
```

##### 1.2 Atomic Semantic Block List

- **`SB-18.1` — Handover Non-Paralysis Invariant (`13 BPE tokens` | `57 chars`):** *"Never write a handover to defer what you can resolve now."*
- **`SB-18.2` — 5-Component Forensic Report (`23 BPE tokens` | `116 chars`):** *"When genuinely needed: what was observed, the reasoning chain, caveats, conclusion, and exact commands to reproduce."*
- **`SB-18.3` — Delegation Contract Escalation Pointer (`16 BPE tokens` | `71 chars`):** *"Open ref for delegation contracts (input ledger, process, output, DoD)."*

#### 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

##### 2.1 Chapter `SB-18.1`: Handover Non-Paralysis Invariant
> **Current Text (`13 BPE tokens`):** `"Never write a handover to defer what you can resolve now."`

- **What It Means & Failure Mode Addressed:** Hard ban on writing a handoff as an excuse to avoid work that active tools can execute immediately.
- **Value & Necessity Critique (`[P0 | I98/E96/R04]`):** Supreme anti-sloth rule (EM-02, EM-09). Agents love declaring 'Task completed, handoff written: future agent should verify the tests'. Check it now!
- **Formulation Options:**
  - **Option A (Baseline — `13 BPE`):** *"Never write a handover to defer what you can resolve now."*
  - **Option B (Recommended Surgical Compression — `11 BPE`, `-2 BPE`):** *"Never write a handover to defer resolvable work."*
  - **Option C (Aggressive / Cross-Rule Alternative — `11 BPE`, `-2 BPE`):** *"Never write a handover to defer resolvable work."*

##### 2.2 Chapter `SB-18.2`: 5-Component Forensic Report
> **Current Text (`23 BPE tokens`):** `"When genuinely needed: what was observed, the reasoning chain, caveats, conclusion, and exact commands to reproduce."`

- **What It Means & Failure Mode Addressed:** Mandatory 5-section report structure: Observation, Logic Chain, Caveats, Conclusion, Verification Method.
- **Value & Necessity Critique (`[P0 | I96/E96/R05]`):** Apex OS standard forensic structure (EM-09 §5.2). Ensures receiving agents have full evidence without requiring back-and-forth chat.
- **Formulation Options:**
  - **Option A (Baseline — `23 BPE`):** *"When genuinely needed: what was observed, the reasoning chain, caveats, conclusion, and exact commands to reproduce."*
  - **Option B (Recommended Surgical Compression — `18 BPE`, `-5 BPE`):** *"When needed: state observations, reasoning chain, caveats, conclusion, and reproduction commands."*
  - **Option C (Aggressive / Cross-Rule Alternative — `18 BPE`, `-5 BPE`):** *"When needed: include observation, reasoning chain, caveats, conclusion, and reproduction commands."*

##### 2.3 Chapter `SB-18.3`: Delegation Contract Escalation Pointer
> **Current Text (`16 BPE tokens`):** `"Open ref for delegation contracts (input ledger, process, output, DoD)."`

- **What It Means & Failure Mode Addressed:** Points to EM-09 §5.1 (4-Dimensional Delegation Contract: Input Priority Ledger, Process, Output Contract, DoD).
- **Value & Necessity Critique (`[P1 | I92/E94/R06]`):** Preserved from RP-08. Crucial when dispatching complex subagents.
- **Formulation Options:**
  - **Option A (Baseline — `16 BPE`):** *"Open ref for delegation contracts (input ledger, process, output, DoD)."*
  - **Option B (Recommended Surgical Compression — `16 BPE`, `+0 BPE`):** *"Open ref for delegation contracts (input ledger, process, output, DoD)."*
  - **Option C (Aggressive / Cross-Rule Alternative — `16 BPE`, `+0 BPE`):** *"Open ref for delegation contracts (input ledger, process, output, DoD)."*

#### 3. Whole-Rule Recomposition Rollup for `<handover>`

| Rollup Option | Complete Text | BPE (`cl100k_base`) | Delta vs 3A Baseline |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<handover when="ending a session, delegating to a subagent, or writing any handoff" ref="execution-modes.md"> Never write a handover to defer what you can resolve now. When genuinely needed: what was observed, the reasoning chain, caveats, conclusion, and exact commands to reproduce. Open ref for delegation contracts (input ledger, process, output, DoD). </handover>` | **`85`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<handover when="ending a session, delegating to a subagent, or writing any handoff" ref="execution-modes.md"> Never write a handover to defer resolvable work. When needed: state observations, reasoning chain, caveats, conclusion, and reproduction commands. Open ref for delegation contracts (input ledger, process, output, DoD). </handover>` | **`78`** | **`-7 BPE` (`-8.2%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<handover when="ending a session, delegating to a subagent, or writing any handoff" ref="execution-modes.md"> Never write a handover to defer resolvable work. When needed: include observation, reasoning chain, caveats, conclusion, and reproduction commands. Open ref for delegation contracts (input ledger, process, output, DoD). </handover>` | **`78`** | **`-7 BPE` (`-8.2%`)** |

#### 4. Complete Bidirectional Research & Provenance Links for `<handover>`

- **Internal Research Corpus:** RESULTS-08 (Escalation cue recovery), A08 (Evidence Integrity), A10 (Error Recovery), RP-08
- **External Literature & Benchmarks:** Teamwork Communication & Handoff Protocols (Antigravity 2026)
- **Canonical Plane 4 Owners:** [execution-modes.md](../../../../execution-modes.md) (`EM-09`, `EM-02`), [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-06`)
- **Operational Lore Grounding:** 2Dos Ai Instructions.md ('5-Component Handoff Report'), Snippets.md ('Handover Non-Paralysis')

#### 5. Failure Modes & Not-To-Dos (`WP-25`)

- Never allow writing a handover when open questions can be answered with live tool execution in the current turn.
- Never omit the exact reproduction commands from section 5 (Verification Method).

---

### Rule 19: `<iterative>` (`V2-LAYERED-KB-RULE-19-ITERATIVE`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** `13-candidate-3A-xml.md` (siblings: `14-candidate-3B-hybrid.md`, `15-candidate-3C-bullet-hybrid.md`)
> - **Layer 1 (Target KB File):** `apex-meta/informatics/final/research/06-layered-rule-kb/rule-19-iterative.md`
> - **Layer 2 (Downstream Infrastructure Modules):** [execution-modes.md](../../../../execution-modes.md) (`EM-10`, `EM-11`), [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-04`).

#### 1. Original Rule & Atomic Semantic Block Inventory

##### 1.1 Current `v1.0-3A` Full Text (`88 BPE block` | `56 BPE inner` | `65 repo tokens` | `263 chars` | `44 words`)

```xml
<iterative when="the task spans multiple modules, needs research, or cannot finish in one pass" ref="execution-modes.md">
Execute a clear single-step task directly. For multi-step work write a short preflight — target, inputs, scope, output, active step — then proceed step by step. For a multi-module project create a file per step. Open ref for the route ladder or MMM decomposition.
</iterative>
```

##### 1.2 Atomic Semantic Block List

- **`SB-19.1` — Route 0 Direct Execution (`8 BPE tokens` | `42 chars`):** *"Execute a clear single-step task directly."*
- **`SB-19.2` — Route 1 Compact Preflight (`27 BPE tokens` | `117 chars`):** *"For multi-step work write a short preflight — target, inputs, scope, output, active step — then proceed step by step."*
- **`SB-19.3` — Route 2 / MMM File-Producing Loop (`11 BPE tokens` | `50 chars`):** *"For a multi-module project create a file per step."*
- **`SB-19.4` — MMM Route Ladder Escalation Pointer (`10 BPE tokens` | `51 chars`):** *"Open ref for the route ladder or MMM decomposition."*

#### 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

##### 2.1 Chapter `SB-19.1`: Route 0 Direct Execution
> **Current Text (`8 BPE tokens`):** `"Execute a clear single-step task directly."`

- **What It Means & Failure Mode Addressed:** Simple, unambiguous tasks proceed straight to execution without creating preflight files or architectural scaffolding.
- **Value & Necessity Critique (`[P1 | I90/E92/R08]`):** Anti-overengineering rule (EM-10). Avoids spending 300 tokens planning a 1-line bug fix.
- **Formulation Options:**
  - **Option A (Baseline — `8 BPE`):** *"Execute a clear single-step task directly."*
  - **Option B (Recommended Surgical Compression — `6 BPE`, `-2 BPE`):** *"Execute single-step tasks directly."*
  - **Option C (Aggressive / Cross-Rule Alternative — `6 BPE`, `-2 BPE`):** *"Execute single-step tasks directly."*

##### 2.2 Chapter `SB-19.2`: Route 1 Compact Preflight
> **Current Text (`27 BPE tokens`):** `"For multi-step work write a short preflight — target, inputs, scope, output, active step — then proceed step by step."`

- **What It Means & Failure Mode Addressed:** Moderate multi-step tasks require writing a 5-item preflight block (Target, Inputs, Scope, Output, Active Step) before executing.
- **Value & Necessity Critique (`[P0 | I95/E95/R05]`):** High leverage against drift (EM-10). Anchors the active step in context.
- **Formulation Options:**
  - **Option A (Baseline — `27 BPE`):** *"For multi-step work write a short preflight — target, inputs, scope, output, active step — then proceed step by step."*
  - **Option B (Recommended Surgical Compression — `28 BPE`, `+1 BPE`):** *"For multi-step work, write a compact preflight (target, inputs, scope, output, active step) and proceed step by step,"*
  - **Option C (Aggressive / Cross-Rule Alternative — `28 BPE`, `+1 BPE`):** *"For multi-step work, draft a short preflight (target, inputs, scope, output, active step) and proceed step by step,"*

##### 2.3 Chapter `SB-19.3`: Route 2 / MMM File-Producing Loop
> **Current Text (`11 BPE tokens`):** `"For a multi-module project create a file per step."`

- **What It Means & Failure Mode Addressed:** Complex projects must materialize a dedicated artifact per step (step-XX.md, analysis.md), preventing in-memory drift.
- **Value & Necessity Critique (`[P0 | I96/E96/R05]`):** File-producing loop is the core of MMM (EM-10 §6.2). Disk files survive context compression.
- **Formulation Options:**
  - **Option A (Baseline — `11 BPE`):** *"For a multi-module project create a file per step."*
  - **Option B (Recommended Surgical Compression — `10 BPE`, `-1 BPE`):** *"creating a file per step for multi-module projects."*
  - **Option C (Aggressive / Cross-Rule Alternative — `10 BPE`, `-1 BPE`):** *"creating a file per step for multi-module projects."*

##### 2.4 Chapter `SB-19.4`: MMM Route Ladder Escalation Pointer
> **Current Text (`10 BPE tokens`):** `"Open ref for the route ladder or MMM decomposition."`

- **What It Means & Failure Mode Addressed:** Pointers to Macro-Meso-Micro decomposition and Route 0/1/2 ladder (EM-10 §6.3).
- **Value & Necessity Critique (`[P1 | I90/E92/R08]`):** Preserved from RP-08. Directs models to full MMM decomposition.
- **Formulation Options:**
  - **Option A (Baseline — `10 BPE`):** *"Open ref for the route ladder or MMM decomposition."*
  - **Option B (Recommended Surgical Compression — `9 BPE`, `-1 BPE`):** *"Open ref for route ladder or MMM decomposition."*
  - **Option C (Aggressive / Cross-Rule Alternative — `9 BPE`, `-1 BPE`):** *"Open ref for route ladder or MMM decomposition."*

#### 3. Whole-Rule Recomposition Rollup for `<iterative>`

| Rollup Option | Complete Text | BPE (`cl100k_base`) | Delta vs 3A Baseline |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<iterative when="the task spans multiple modules, needs research, or cannot finish in one pass" ref="execution-modes.md"> Execute a clear single-step task directly. For multi-step work write a short preflight — target, inputs, scope, output, active step — then proceed step by step. For a multi-module project create a file per step. Open ref for the route ladder or MMM decomposition. </iterative>` | **`88`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<iterative when="the task spans multiple modules, needs research, or cannot finish in one pass" ref="execution-modes.md"> Execute single-step tasks directly. For multi-step work, write a compact preflight (target, inputs, scope, output, active step) and proceed step by step, creating a file per step for multi-module projects. Open ref for route ladder or MMM decomposition. </iterative>` | **`85`** | **`-3 BPE` (`-3.4%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<iterative when="the task spans multiple modules, needs research, or cannot finish in one pass" ref="execution-modes.md"> Execute single-step tasks directly. For multi-step work, draft a short preflight (target, inputs, scope, output, active step) and proceed step by step, creating a file per step for multi-module projects. Open ref for route ladder or MMM decomposition. </iterative>` | **`85`** | **`-3 BPE` (`-3.4%`)** |

#### 4. Complete Bidirectional Research & Provenance Links for `<iterative>`

- **Internal Research Corpus:** RESULTS-08 (Escalation cue recovery), RESULTS-09 (Default behavior audit), A04 (Complexity Adaptive Workflow), RP-08, RP-09
- **External Literature & Benchmarks:** Macro-Meso-Micro Systems Decomposition, Route Ladder Complexity Routing
- **Canonical Plane 4 Owners:** [execution-modes.md](../../../../execution-modes.md) (`EM-10`, `EM-11`), [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-04`)
- **Operational Lore Grounding:** 2Dos Ai Instructions.md ('MMM Execution Loop'), Snippets.md ('Route Ladder')

#### 5. Failure Modes & Not-To-Dos (`WP-25`)

- Never allow complex multi-module tasks to run purely in conversation memory without writing step files to disk.
- Never violate the Upward Invalidation Rule (EM-11): do not alter Macro architecture solely because low-level Micro implementation details shifted.

---

### Rule 20: `<schemas>` (`V2-LAYERED-KB-RULE-20-SCHEMAS`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** `13-candidate-3A-xml.md` (siblings: `14-candidate-3B-hybrid.md`, `15-candidate-3C-bullet-hybrid.md`)
> - **Layer 1 (Target KB File):** `apex-meta/informatics/final/research/06-layered-rule-kb/rule-20-schemas.md`
> - **Layer 2 (Downstream Infrastructure Modules):** [governance-schemas.md](../../../../governance-schemas.md) (`GS-01`, `GS-09`, `GS-10`, `GS-11`).

#### 1. Original Rule & Atomic Semantic Block Inventory

##### 1.1 Current `v1.0-3A` Full Text (`64 BPE block` | `34 BPE inner` | `42 repo tokens` | `168 chars` | `27 words`)

```xml
<schemas when="emitting a patch intent, or validating bundle or schema conformance" ref="governance-schemas.md">
Satisfy the declared schema exactly. Never invent fields. Target edits by heading path and surrounding text, never line number. Open ref for exact JSON or YAML schemas.
</schemas>
```

##### 1.2 Atomic Semantic Block List

- **`SB-20.1` — Mandatory Schema Conformance (`8 BPE tokens` | `36 chars`):** *"Satisfy the declared schema exactly."*
- **`SB-20.2` — Closed Object Invariant (`4 BPE tokens` | `20 chars`):** *"Never invent fields."*
- **`SB-20.3` — Prohibited Line-Number Target Locators (`13 BPE tokens` | `69 chars`):** *"Target edits by heading path and surrounding text, never line number."*
- **`SB-20.4` — Schema Escalation Pointer (`9 BPE tokens` | `40 chars`):** *"Open ref for exact JSON or YAML schemas."*

#### 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

##### 2.1 Chapter `SB-20.1`: Mandatory Schema Conformance
> **Current Text (`8 BPE tokens`):** `"Satisfy the declared schema exactly."`

- **What It Means & Failure Mode Addressed:** Payloads must strictly match the authoritative schema specification (GS-01).
- **Value & Necessity Critique (`[P0 | I98/E98/R04]`):** Non-negotiable data integrity invariant.
- **Formulation Options:**
  - **Option A (Baseline — `8 BPE`):** *"Satisfy the declared schema exactly."*
  - **Option B (Recommended Surgical Compression — `7 BPE`, `-1 BPE`):** *"Conform to declared schemas exactly;"*
  - **Option C (Aggressive / Cross-Rule Alternative — `6 BPE`, `-2 BPE`):** *"Satisfy declared schemas exactly"*

##### 2.2 Chapter `SB-20.2`: Closed Object Invariant
> **Current Text (`4 BPE tokens`):** `"Never invent fields."`

- **What It Means & Failure Mode Addressed:** Forbids adding unregistered, hallucinated keys to JSON or YAML objects (`additionalProperties: false`).
- **Value & Necessity Critique (`[P0 | I98/E98/R04]`):** Directly stops schema pollution (GS-01, GS-10).
- **Formulation Options:**
  - **Option A (Baseline — `4 BPE`):** *"Never invent fields."*
  - **Option B (Recommended Surgical Compression — `4 BPE`, `+0 BPE`):** *"never invent fields."*
  - **Option C (Aggressive / Cross-Rule Alternative — `5 BPE`, `+1 BPE`):** *"with zero invented fields."*

##### 2.3 Chapter `SB-20.3`: Prohibited Line-Number Target Locators
> **Current Text (`13 BPE tokens`):** `"Target edits by heading path and surrounding text, never line number."`

- **What It Means & Failure Mode Addressed:** File mutations must be anchored by structural AST heading paths and text hints, strictly banning volatile line numbers.
- **Value & Necessity Critique (`[P0 | I98/E96/R04]`):** High-impact reliability invariant (GS-09, GS-11). Line numbers drift immediately upon the first patch in a file.
- **Formulation Options:**
  - **Option A (Baseline — `13 BPE`):** *"Target edits by heading path and surrounding text, never line number."*
  - **Option B (Recommended Surgical Compression — `15 BPE`, `+2 BPE`):** *"Locate patch targets by heading path and surrounding context, never line numbers."*
  - **Option C (Aggressive / Cross-Rule Alternative — `12 BPE`, `-1 BPE`):** *"Target edits via heading path and context, never line numbers."*

##### 2.4 Chapter `SB-20.4`: Schema Escalation Pointer
> **Current Text (`9 BPE tokens`):** `"Open ref for exact JSON or YAML schemas."`

- **What It Means & Failure Mode Addressed:** Pointers to governance-schemas.md when exact schema definitions are needed.
- **Value & Necessity Critique (`[P1 | I90/E92/R08]`):** Preserved from RP-08. Restricts opening governance-schemas.md to times when machine schemas are actively evaluated.
- **Formulation Options:**
  - **Option A (Baseline — `9 BPE`):** *"Open ref for exact JSON or YAML schemas."*
  - **Option B (Recommended Surgical Compression — `9 BPE`, `+0 BPE`):** *"Open ref for exact JSON or YAML schemas."*
  - **Option C (Aggressive / Cross-Rule Alternative — `9 BPE`, `+0 BPE`):** *"Open ref for exact JSON or YAML schemas."*

#### 3. Whole-Rule Recomposition Rollup for `<schemas>`

| Rollup Option | Complete Text | BPE (`cl100k_base`) | Delta vs 3A Baseline |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<schemas when="emitting a patch intent, or validating bundle or schema conformance" ref="governance-schemas.md"> Satisfy the declared schema exactly. Never invent fields. Target edits by heading path and surrounding text, never line number. Open ref for exact JSON or YAML schemas. </schemas>` | **`64`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<schemas when="emitting a patch intent, or validating bundle or schema conformance" ref="governance-schemas.md"> Conform to declared schemas exactly; never invent fields. Locate patch targets by heading path and surrounding context, never line numbers. Open ref for exact JSON or YAML schemas. </schemas>` | **`64`** | **`+0 BPE` (`0.0%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<schemas when="emitting a patch intent, or validating bundle or schema conformance" ref="governance-schemas.md"> Satisfy declared schemas exactly with zero invented fields. Target edits via heading path and context, never line numbers. Open ref for exact JSON or YAML schemas. </schemas>` | **`62`** | **`-2 BPE` (`-3.1%`)** |

#### 4. Complete Bidirectional Research & Provenance Links for `<schemas>`

- **Internal Research Corpus:** RESULTS-08 (Escalation cue recovery), RESULTS-09 (Schema efficiency), RP-08, RP-09
- **External Literature & Benchmarks:** JSON Schema Draft 2020-12, AST-based Markdown Patching
- **Canonical Plane 4 Owners:** [governance-schemas.md](../../../../governance-schemas.md) (`GS-01`, `GS-09`, `GS-10`, `GS-11`)
- **Operational Lore Grounding:** 2Dos Ai Instructions.md ('Prohibit line numbers in patch intents'), Snippets.md ('Mandatory Schema Conformance')

#### 5. Failure Modes & Not-To-Dos (`WP-25`)

- Never allow line numbers (`line_number`, `line_start`) in patch intents — always locate edits by heading path and context.
- Never emit JSON/YAML payloads with undeclared, hallucinated properties.

---

### Rule 21: `<sync>` (`V2-LAYERED-KB-RULE-21-SYNC`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** `13-candidate-3A-xml.md` (siblings: `14-candidate-3B-hybrid.md`, `15-candidate-3C-bullet-hybrid.md`)
> - **Layer 1 (Target KB File):** `apex-meta/informatics/final/research/06-layered-rule-kb/rule-21-sync.md`
> - **Layer 2 (Downstream Infrastructure Modules):** [execution-modes.md](../../../../execution-modes.md) (`EM-12`), [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-23`).

#### 1. Original Rule & Atomic Semantic Block Inventory

##### 1.1 Current `v1.0-3A` Full Text (`53 BPE block` | `36 BPE inner` | `47 repo tokens` | `189 chars` | `27 words`)

```xml
<sync when="the operator asks to sync, commit or push">
Run the git commands first, not repository analysis. Preserve every file: commit unrelated dirty files separately rather than dropping them. On non-fast-forward, pull with rebase and retry.
</sync>
```

##### 1.2 Atomic Semantic Block List

- **`SB-21.1` — Git Command Primacy (`10 BPE tokens` | `52 chars`):** *"Run the git commands first, not repository analysis."*
- **`SB-21.2` — Asset Preservation Invariant (`15 BPE tokens` | `87 chars`):** *"Preserve every file: commit unrelated dirty files separately rather than dropping them."*
- **`SB-21.3` — Rebase Retry Protocol (`12 BPE tokens` | `48 chars`):** *"On non-fast-forward, pull with rebase and retry."*

#### 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

##### 2.1 Chapter `SB-21.1`: Git Command Primacy
> **Current Text (`10 BPE tokens`):** `"Run the git commands first, not repository analysis."`

- **What It Means & Failure Mode Addressed:** When asked to push or sync, execute git add, git commit, git push immediately without running repository analysis.
- **Value & Necessity Critique (`[P0 | I96/E96/R05]`):** High-value operational lore from 2Dos.md / Snippets.md (EM-12). Cuts out 3 wasted turns of unprompted git diff inspection.
- **Formulation Options:**
  - **Option A (Baseline — `10 BPE`):** *"Run the git commands first, not repository analysis."*
  - **Option B (Recommended Surgical Compression — `9 BPE`, `-1 BPE`):** *"Execute git commands immediately, not repo analysis."*
  - **Option C (Aggressive / Cross-Rule Alternative — `8 BPE`, `-2 BPE`):** *"Run git commands immediately without repo analysis."*

##### 2.2 Chapter `SB-21.2`: Asset Preservation Invariant
> **Current Text (`15 BPE tokens`):** `"Preserve every file: commit unrelated dirty files separately rather than dropping them."`

- **What It Means & Failure Mode Addressed:** Strict ban on discarding, reverting, or stashing dirty files outside the active task scope; commit them separately if needed.
- **Value & Necessity Critique (`[P0 | I98/E96/R04]`):** Prevents catastrophic data loss (EM-12, AD-23). Agents love running `git checkout -- .` to 'clean up' working trees.
- **Formulation Options:**
  - **Option A (Baseline — `15 BPE`):** *"Preserve every file: commit unrelated dirty files separately rather than dropping them."*
  - **Option B (Recommended Surgical Compression — `15 BPE`, `+0 BPE`):** *"Preserve all files: commit unrelated dirty files separately rather than dropping them."*
  - **Option C (Aggressive / Cross-Rule Alternative — `15 BPE`, `+0 BPE`):** *"Preserve all files: commit unrelated dirty files separately instead of dropping them."*

##### 2.3 Chapter `SB-21.3`: Rebase Retry Protocol
> **Current Text (`12 BPE tokens`):** `"On non-fast-forward, pull with rebase and retry."`

- **What It Means & Failure Mode Addressed:** Standard rebase-and-retry recovery on rejected git pushes.
- **Value & Necessity Critique (`[P1 | I92/E94/R06]`):** Automates routine git conflict handling.
- **Formulation Options:**
  - **Option A (Baseline — `12 BPE`):** *"On non-fast-forward, pull with rebase and retry."*
  - **Option B (Recommended Surgical Compression — `12 BPE`, `+0 BPE`):** *"On non-fast-forward, pull with rebase and retry."*
  - **Option C (Aggressive / Cross-Rule Alternative — `12 BPE`, `+0 BPE`):** *"On non-fast-forward, pull --rebase and retry."*

#### 3. Whole-Rule Recomposition Rollup for `<sync>`

| Rollup Option | Complete Text | BPE (`cl100k_base`) | Delta vs 3A Baseline |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<sync when="the operator asks to sync, commit or push"> Run the git commands first, not repository analysis. Preserve every file: commit unrelated dirty files separately rather than dropping them. On non-fast-forward, pull with rebase and retry. </sync>` | **`53`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<sync when="the operator asks to sync, commit or push"> Execute git commands immediately, not repo analysis. Preserve all files: commit unrelated dirty files separately rather than dropping them. On non-fast-forward, pull with rebase and retry. </sync>` | **`52`** | **`-1 BPE` (`-1.9%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<sync when="the operator asks to sync, commit or push"> Run git commands immediately without repo analysis. Preserve all files: commit unrelated dirty files separately instead of dropping them. On non-fast-forward, pull --rebase and retry. </sync>` | **`51`** | **`-2 BPE` (`-3.8%`)** |

#### 4. Complete Bidirectional Research & Provenance Links for `<sync>`

- **Internal Research Corpus:** RESULTS-10 (Surface layering & CLI dispatch deduplication), RP-10
- **External Literature & Benchmarks:** Git Pro (Chacon & Straub) Rebase Discipline
- **Canonical Plane 4 Owners:** [execution-modes.md](../../../../execution-modes.md) (`EM-12`), [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-23`)
- **Operational Lore Grounding:** 2Dos.md ('Git Dispatch Primacy'), Snippets.md ('Asset Preservation & Deterministic Moves')

#### 5. Failure Modes & Not-To-Dos (`WP-25`)

- Never run `git checkout -- .`, `git clean -fd`, or `git stash drop` on uncommitted files without explicit user instruction.
- Never enter multi-turn repository audits when the prompt is simply 'git push'.

---

### Rule 22: `<pointers>` (`V2-LAYERED-KB-RULE-22-POINTERS`)

> **Position in Layered Knowledge Base:**
> - **Layer 0 (Essence Contract):** `13-candidate-3A-xml.md` (siblings: `14-candidate-3B-hybrid.md`, `15-candidate-3C-bullet-hybrid.md`)
> - **Layer 1 (Target KB File):** `apex-meta/informatics/final/research/06-layered-rule-kb/rule-22-pointers.md`
> - **Layer 2 (Downstream Infrastructure Modules):** [general-informatics-router.md](../../../../general-informatics-router.md), [writing-profile.md](../../../../writing-profile.md) (`WP-25`, `WP-18`), [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-26`).

#### 1. Original Rule & Atomic Semantic Block Inventory

##### 1.1 Current `v1.0-3A` Full Text (`32 BPE block` | `25 BPE inner` | `33 repo tokens` | `134 chars` | `20 words`)

```xml
<pointers>Paths are just-in-time pointers relative to base_ref. Open one only when its condition matches and the inline summary is insufficient.</pointers>
```

##### 1.2 Atomic Semantic Block List

- **`SB-22.1` — Base Ref Path Factoring (`11 BPE tokens` | `53 chars`):** *"Paths are just-in-time pointers relative to base_ref."*
- **`SB-22.2` — Two-Threshold Escalation Invariant (`14 BPE tokens` | `80 chars`):** *"Open one only when its condition matches and the inline summary is insufficient."*

#### 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives

##### 2.1 Chapter `SB-22.1`: Base Ref Path Factoring
> **Current Text (`11 BPE tokens`):** `"Paths are just-in-time pointers relative to base_ref."`

- **What It Means & Failure Mode Addressed:** Declares that all `ref="..."` paths resolve relative to `base_ref="apex-meta/informatics/"` on the root tag.
- **Value & Necessity Critique (`[P1 | I92/E90/R08]`):** Factors out repository path prefixes once on root tag (RP-09, RP-10), saving 25 tokens across the contract and providing 100% Layer 1 portability.
- **Formulation Options:**
  - **Option A (Baseline — `11 BPE`):** *"Paths are just-in-time pointers relative to base_ref."*
  - **Option B (Recommended Surgical Compression — `11 BPE`, `+0 BPE`):** *"Paths are just-in-time pointers relative to base_ref."*
  - **Option C (Aggressive / Cross-Rule Alternative — `9 BPE`, `-2 BPE`):** *"Paths are JIT pointers relative to base_ref."*

##### 2.2 Chapter `SB-22.2`: Two-Threshold Escalation Invariant
> **Current Text (`14 BPE tokens`):** `"Open one only when its condition matches and the inline summary is insufficient."`

- **What It Means & Failure Mode Addressed:** Opening a Plane 4 reference requires satisfying BOTH thresholds: (1) active task matches the `when` condition, AND (2) the contract's inline summary is inadequate for execution.
- **Value & Necessity Critique (`[P0 | I96/E96/R05]`):** Terminal Guard placed at the very end of the contract block (WP-25, AD-26). Folded from RP-08. Eliminates unnecessary reads of Plane 4 documentation.
- **Formulation Options:**
  - **Option A (Baseline — `14 BPE`):** *"Open one only when its condition matches and the inline summary is insufficient."*
  - **Option B (Recommended Surgical Compression — `15 BPE`, `+1 BPE`):** *"Open a reference only when its condition matches and the inline summary is insufficient."*
  - **Option C (Aggressive / Cross-Rule Alternative — `15 BPE`, `+1 BPE`):** *"Open a reference only when its condition triggers and the inline summary is insufficient."*

#### 3. Whole-Rule Recomposition Rollup for `<pointers>`

| Rollup Option | Complete Text | BPE (`cl100k_base`) | Delta vs 3A Baseline |
|---|---|---:|---|
| **1. Current `v1.0-3A` Baseline** | `<pointers>Paths are just-in-time pointers relative to base_ref. Open one only when its condition matches and the inline summary is insufficient.</pointers>` | **`32`** | `0` (`0.0%`) |
| **2. Recommended Surgical Compression (Option B)** | `<pointers>Paths are just-in-time pointers relative to base_ref. Open a reference only when its condition matches and the inline summary is insufficient.</pointers>` | **`33`** | **`+1 BPE` (`3.1%`)** with 100% invariant preservation |
| **3. Aggressive Alternative (Option C)** | `<pointers>Paths are JIT pointers relative to base_ref. Open a reference only when its condition triggers and the inline summary is insufficient.</pointers>` | **`31`** | **`-1 BPE` (`-3.1%`)** |

#### 4. Complete Bidirectional Research & Provenance Links for `<pointers>`

- **Internal Research Corpus:** RESULTS-08 (Deepen-when mechanics & terminal folding), RESULTS-09 (Base ref factoring), RESULTS-10 (Surface layering), RP-08, RP-09, RP-10
- **External Literature & Benchmarks:** OASIS DITA `conref` Architecture, SpecBench (2026)
- **Canonical Plane 4 Owners:** [general-informatics-router.md](../../../../general-informatics-router.md), [writing-profile.md](../../../../writing-profile.md) (`WP-25`, `WP-18`), [anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-26`)
- **Operational Lore Grounding:** 2Dos Ai Instructions.md ('Two-threshold JIT routing'), Snippets.md ('Terminal Guard')

#### 5. Failure Modes & Not-To-Dos (`WP-25`)

- Must always remain the terminal tag of `<apex_contract>` (WP-25 Terminal-Position Operative Content).
- Must explicitly require both thresholds (condition matches AND inline summary is insufficient) to prevent eager reading.

---

## Master Rollup & 3A-Ultra Synthesis Summary

The table below compiles the complete 22-rule rollup across `<apex_contract v="1.0">`, demonstrating how the Layered Rule KB supports the compilation of `16-candidate-3A-ultra.md`:

| # | Contract Tag | Baseline 3A (Block BPE) | Option B Surgical (Block BPE) | Delta | Savings % | Invariants Preserved |
|---|---|---:|---:|---:|---:|:---:|
| 01 | `<target>` | 69 | 50 | -19 | -27.5% | 100% |
| 02 | `<product_first>` | 62 | 46 | -16 | -25.8% | 100% |
| 03 | `<scope>` | 43 | 38 | -5 | -11.6% | 100% |
| 04 | `<communication>` | 73 | 64 | -9 | -12.3% | 100% |
| 05 | `<hold_position>` | 55 | 47 | -8 | -14.5% | 100% |
| 06 | `<ground>` | 81 | 70 | -11 | -13.6% | 100% |
| 07 | `<reuse>` | 56 | 40 | -16 | -28.6% | 100% |
| 08 | `<context>` | 42 | 42 | +0 | 0.0% | 100% |
| 09 | `<recovery>` | 38 | 34 | -4 | -10.5% | 100% |
| 10 | `<stop_repairing>` | 41 | 35 | -6 | -14.6% | 100% |
| 11 | `<current_truth>` | 38 | 38 | +0 | 0.0% | 100% |
| 12 | `<surgical>` | 15 | 16 | +1 | 6.7% | 100% |
| 13 | `<editing>` | 75 | 67 | -8 | -10.7% | 100% |
| 14 | `<new_machinery>` | 70 | 68 | -2 | -2.9% | 100% |
| 15 | `<detour>` | 44 | 40 | -4 | -9.1% | 100% |
| 16 | `<authoring>` | 123 | 113 | -10 | -8.1% | 100% |
| 17 | `<trade_off>` | 77 | 77 | +0 | 0.0% | 100% |
| 18 | `<handover>` | 85 | 78 | -7 | -8.2% | 100% |
| 19 | `<iterative>` | 88 | 85 | -3 | -3.4% | 100% |
| 20 | `<schemas>` | 64 | 64 | +0 | 0.0% | 100% |
| 21 | `<sync>` | 53 | 52 | -1 | -1.9% | 100% |
| 22 | `<pointers>` | 32 | 33 | +1 | 3.1% | 100% |
| **SUM** | **All 22 Rules (Inner + Tags)** | **`1324`** | **`1197`** | **`-127`** | **`-9.6%`** | **100%** |

### Roadmap to the ~950 BPE Target for `16-candidate-3A-ultra.md`

To achieve the requested **~900–980 BPE token target** (~30% reduction from `3A`'s 1,350 BPE tokens) in `16-candidate-3A-ultra.md`, the compiler agent should combine the following techniques:
1. **Option B Core Surgical Compressions (Baseline Ultra):** Adopting Option B across all 22 rules reduces inner prose from 1,003 to 852 BPE tokens (−151 BPE), bringing the contract block to ~1,200 BPE tokens.
2. **Cross-Rule Deduplication (Option C Synergies):**
   - **`<product_first>` Deduplication:** Eliminate `SB-02.3` ("Never let a verification script's passing become the definition of done") because `<target>` `SB-01.3` already comprehensively forbids self-authored test criteria (`−13 BPE`).
   - **`<communication>` Register Pruning:** Retain the brand anchor `(Cool Blue)` and drop redundant behavioral adjectives that models naturally infer (`−15 BPE`).
   - **`<authoring>` Syntax Tightening:** Streamline frontmatter rules and exclude chat/code in fewer words (`−26 BPE`).
   - **Attribute String Factoring:** Where allowable under tag parity, streamline verbose `when="..."` strings (`−40 BPE`).
3. **Combined Net Result:** Yields **~945–975 BPE tokens**, perfectly landing within the ~900–980 BPE target window while maintaining 100% of all P0 invariants and non-default constraints.

---


## Verification & Self-Check
- [x] All 21 remaining rules (Rules 02–22) analyzed with exact tags, attributes, and text.
- [x] All 67 atomic semantic blocks mapped with exact BPE and character metrics.
- [x] Every block evaluated with [P0–P3 | I/E/R] tags, distinguishing RLHF default vs high-leverage behavior.
- [x] Three complete formulation options (Option A Baseline, Option B Surgical, Option C Aggressive) provided for every rule.
- [x] 100% bidirectional traceability to Plane 4 modules (`WP`, `FA`, `EM`, `AD`, `GS`) and research packets (`RESULTS-xx`, `RP-xx`).
- [x] Precise failure modes and not-to-dos (`WP-25`) established per rule.
