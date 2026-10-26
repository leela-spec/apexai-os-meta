# Handoff Report — Specification Mining for Candidate 16-3A-Ultra

**Agent:** `spec_miner_m5_1`  
**Date:** 2026-10-22  
**Target Artifact:** `apex-meta/informatics/final/candidates/16-candidate-3A-ultra.md`  
**Parent Orchestrator:** `8ca44b74-952a-4cfd-afc5-fcda15705e76` (`orchestrator_5`)

---

## Features Discovered

| # | Category | Feature | Description | Inputs | Outputs | Error Behavior | Discovered Via |
|---|---|---|---|---|---|---|---|
| 1 | Candidate Architecture | OKF v0.2 Frontmatter Schema | Candidate specification files require flat YAML frontmatter declaring `type: Reference`, unique durable `id`, `title`, `description`, `status: current_candidate`, and `tags: [...]`. | YAML frontmatter block at lines 1–8 of Markdown file | Validated by `okf_validator.py` | `OKF_ERROR` if delimiters missing, `APEX_PROFILE_ERROR` if non-flat or duplicate ID | `13-candidate-3A-xml.md:1-8`, `okf_validator.py:60-85` |
| 2 | Contract Formatting | Root XML Contract Wrapper | Contract blocks must use `<apex_contract v="1.0-ultra" base_ref="apex-meta/informatics/">` opening and `</apex_contract>` closing tags. | XML root element with attributes `v` and `base_ref` | Layer 1 portable relative path references (`ref="..."`) | Unrecognized attribute or broken relative path fails link checkers | `13-candidate-3A-xml.md:33,97`, `DEC-22` |
| 3 | Contract Formatting | 22 Semantic Rule Tag Order | Exactly 22 tags in strict order: `<target>`, `<product_first>`, `<scope>`, `<communication>`, `<hold_position>`, `<ground>`, `<reuse>`, `<context>`, `<recovery>`, `<stop_repairing>`, `<current_truth>`, `<surgical>`, `<editing>`, `<new_machinery>`, `<detour>`, `<authoring>`, `<trade_off>`, `<handover>`, `<iterative>`, `<schemas>`, `<sync>`, `<pointers>`. | 22 named XML elements | 12 unconditional invariants + 9 conditional JIT gates + 1 terminal pointer guard | Missing or renamed tags violate canonical provenance tests | `13-candidate-3A-xml.md:35-95`, `test_m3_challenger_tokens.py:40-48` |
| 4 | Metric Measurement | Repo Token Estimation | Repo tokens are deterministically computed as integer division of total character length by 4: `chars // 4`. | Character length of the fenced XML contract code block | Integer repo token estimate | Discrepancy between claimed and empirical fails test assertions | `verify_m3_rules.py:178`, `test_m3_challenger_tokens.py:177`, `13-candidate-3A-xml.md:14` |
| 5 | Metric Measurement | BPE Token Measurement | BPE tokens are measured using OpenAI's `tiktoken` with the `cl100k_base` encoding on the exact text inside the ` ```xml ... ``` ` code fence. | UTF-8 text string of the contract block | Integer token count (`len(enc.encode(block))`) | Discrepancy fails `test_sec1_1_metrics_accuracy` | `verify_m3_rules.py:28,177`, `test_m3_challenger_tokens.py:28,169` |
| 6 | Metric Measurement | Word & Line Counting | Word count is `len(block.split())` and line count is `len(block.splitlines())` of the contract code block. | UTF-8 text of code fence | Integer word and line counts | Discrepancy fails empirical verification tests | `verify_m3_rules.py:175-176`, `test_m3_challenger_tokens.py:175-176` |
| 7 | Rule Synthesis | Layered KB Option B Extraction | Each rule in `06-layered-rule-kb/rule-01` through `rule-22` defines an authoritative **Option B** (Recommended Surgical Compression) in §3 Rollup Table Row 2. | Markdown table row in §3 of `rule-XX-*.md` | Verbatim compressed XML rule tag | Inconsistency between §2 and §3 triggers test failures | `06-layered-rule-kb/rule-01.md:99` through `rule-22.md`, `test_m3_challenger_tokens.py:255-276` |
| 8 | Rule Synthesis | Empirical Size vs. Target Delta | Concatenating all 22 Option B blocks yields 1,225 BPE tokens (multiline) / 1,224 BPE tokens (single line) rather than the prompt's ~950 BPE estimate, due to rule authors strictly upholding R2 (Substance Over Ceremony) and WP-25 (preserving non-default invariants). | 22 Option B tags from Layer 1 KB | 1,225 BPE, 1,479 repo tokens, 5,917 chars, 769 words, 65 lines | Falsely compressing beyond Option B breaks single-source truth with Layer 1 KB | `06-layered-rule-kb/`, `inspect_rules.py` |
| 9 | Delta Analysis | Rule-by-Rule BPE Delta Table | Candidate 16 must document a 22-row comparison against `13-candidate-3A-xml.md` showing BPE before, BPE after, net BPE delta, percentage savings, and summary of compression. | 3A Baseline and 3A-Ultra Option B tag texts | 8-column Markdown comparison table | Inaccurate BPE or arithmetic fails verification | `15-candidate-3C-bullet-hybrid.md:20-26`, `test_m3_challenger_tokens.py:234-252` |
| 10 | Security & Isolation | Live Carrier Immutability Guard | Candidate files in `candidates/` must NEVER modify root `AGENTS.md`, `CLAUDE.md`, or `GEMINI.md`. | Live root carrier files | Assert `16-candidate-3A-ultra` not in carriers | Uncommitted diff in root carriers fails test suite | `test_m3_rules16_22_links.py:100-110` |

---

## Edge Cases

| # | Feature | Input | Observed Behavior |
|---|---|---|---|
| 1 | Table Cell Splitting | Markdown table rows containing backticks and parentheses (e.g. `(`SB-01.1C + 01.2B`)`) in `rule-01-target.md` | Standard regex matching on `\|` can prematurely split cells if backtick states are not properly tracked. Custom parser with backtick tracking correctly extracts column contents. |
| 2 | Code Fence Measurement | Trailing newline after opening fence ` ```xml\n ` vs leading content | The standard test suite measures `block = m.group(1)` without the markdown fence backticks themselves, preserving internal newlines and whitespace verbatim. |
| 3 | Single-Line vs. Multi-Line Tag Formatting | Conditional tags 13–21 formatted on 3 lines (`<tag when="..." ref="...">\nbody\n</tag>`) vs single line | Multi-line formatting adds exactly 1 BPE token (1,225 vs 1,224) and matches the exact 65-line visual structure of `13-candidate-3A-xml.md`. Single-line formatting produces 47 lines. Multi-line is strongly recommended for structural parity. |
| 4 | Prototype Variance in Rule 01 | Claimed metrics in `rule-01-target.md` §1.1 header (`56 BPE`) vs empirical measurement (`69 BPE`) | Rule 01 was the initial prototype written before test suites were automated. Its claimed BPE omitted XML tag tokens or used an alternate tokenizer. The live empirical BPE of 3A `<target>` is 69 BPE, and Option B is 50 BPE (a 27.5% reduction). |
| 5 | Non-Compressible Invariant Tags | Rules where Option B BPE is equal to or slightly larger than Baseline (Rule 08 `+0`, Rule 11 `+0`, Rule 12 `+1`, Rule 17 `+0`, Rule 20 `+0`, Rule 22 `+1`) | Rule authors documented that technical precision and non-default boundary enforcement (e.g. `<surgical>` "Never regenerate or overwrite an existing file in full", `<pointers>` "Open a reference only...") require explicit wording that cannot be cut without creating dangerous ambiguity. |

---

## 1. Observation

### 1.1 Live Candidate File Structures
Direct inspection of `apex-meta/informatics/final/candidates/` revealed three active candidate specifications:
1. **`13-candidate-3A-xml.md`** (Production Master):
   - Lines: 128 lines total.
   - Frontmatter (lines 1–8):
     ```yaml
     ---
     type: Reference
     id: V2-CANDIDATE-3A-XML-v1.0
     title: Contract Block Candidate 3A — Finalized v1.0 Pure Named XML
     description: Finalized v1.0-3A Always-On Contract Block implementing named XML tags throughout, base_ref Layer 1 portability, deepen_when removal (RP-08), and the empirical wording upgrades from RP-04, RP-05, and RP-07.
     status: current_candidate
     tags: [candidate, contract-block, v1.0-3A, xml, compression, finalized]
     ---
     ```
   - Structure:
     - Title & Status callout with measured sizes (lines 10–15).
     - `## 1. Research Improvements Integrated from ResearchOfFile10` (lines 18–27).
     - `## 2. The Finalized Block (v1.0-3A — Pure XML)` (lines 30–98).
     - `## 3. Canonical Provenance Map (Contract Tag <-> Library Module Rule)` (lines 102–128).
   - Measured contract block size inside ` ```xml ... ``` `:
     `6,529` chars | `1,632` repo tokens (`chars // 4`) | `1,350` BPE tokens (`cl100k_base`) | `899` words | `65` lines.
2. **`14-candidate-3B-hybrid.md`** (Table Variant):
   - Measured contract block: `6,347` chars | `1,586` repo tokens | `1,314` BPE tokens | `924` words | `41` lines.
3. **`15-candidate-3C-bullet-hybrid.md`** (Bold-Bullet Variant):
   - Measured contract block 1 (`3C-1`): `6,443` chars | `1,610` repo tokens | `1,335` BPE tokens | `923` words | `54` lines.
   - Measured contract block 2 (`3C-2`): `6,261` chars | `1,565` repo tokens | `1,299` BPE tokens | `948` words | `30` lines.

### 1.2 Metric Computation Methodology in the Codebase
Inspecting `apex-meta/informatics/tests/verify_m3_rules.py` (lines 175–188) and `apex-meta/informatics/tests/test_m3_challenger_tokens.py` (lines 169–178) reveals the exact authoritative measurement equations:
```python
emp_chars = len(code_fence_text)
emp_words = len(code_fence_text.split())
emp_bpe = len(enc.encode(code_fence_text))  # enc = tiktoken.get_encoding("cl100k_base")
emp_repo = emp_chars // 4
emp_lines = len(code_fence_text.splitlines())
```
- Character count: verbatim UTF-8 character length of the text enclosed in the code fence.
- Word count: whitespace-delimited word tokens (`split()`).
- BPE token count: token count produced by `tiktoken.get_encoding("cl100k_base")`.
- Repo token count: integer division `emp_chars // 4`.
- Line count: count of lines (`splitlines()`).

### 1.3 Layered Rule KB Option B Inventory
Analysis across all 22 rule deep dives (`rule-01-target.md` through `rule-22-pointers.md`) in `apex-meta/informatics/final/research/06-layered-rule-kb/` yielded the exact Option B compressed texts and empirical metrics:

| Rule # | Tag | Mode | 3A Baseline BPE | Ultra Option B BPE | Net Delta | Savings % |
|---|---|---|---|---|---|---|
| **01** | `<target>` | Unconditional | 69 | 50 | −19 | −27.5% |
| **02** | `<product_first>` | Unconditional | 62 | 46 | −16 | −25.8% |
| **03** | `<scope>` | Unconditional | 43 | 38 | −5 | −11.6% |
| **04** | `<communication>` | Unconditional | 73 | 64 | −9 | −12.3% |
| **05** | `<hold_position>` | Unconditional | 55 | 47 | −8 | −14.5% |
| **06** | `<ground>` | Unconditional | 81 | 70 | −11 | −13.6% |
| **07** | `<reuse>` | Unconditional | 56 | 40 | −16 | −28.6% |
| **08** | `<context>` | Unconditional | 42 | 42 | 0 | 0.0% |
| **09** | `<recovery>` | Unconditional | 38 | 34 | −4 | −10.5% |
| **10** | `<stop_repairing>` | Unconditional | 41 | 35 | −6 | −14.6% |
| **11** | `<current_truth>` | Unconditional | 38 | 38 | 0 | 0.0% |
| **12** | `<surgical>` | Unconditional | 15 | 16 | +1 | +6.7% |
| **13** | `<editing>` | Gated | 75 | 67 | −8 | −10.7% |
| **14** | `<new_machinery>` | Gated | 70 | 68 | −2 | −2.9% |
| **15** | `<detour>` | Gated | 44 | 40 | −4 | −9.1% |
| **16** | `<authoring>` | Gated | 123 | 113 | −10 | −8.1% |
| **17** | `<trade_off>` | Gated | 77 | 77 | 0 | 0.0% |
| **18** | `<handover>` | Gated | 85 | 78 | −7 | −8.2% |
| **19** | `<iterative>` | Gated | 88 | 85 | −3 | −3.4% |
| **20** | `<schemas>` | Gated | 64 | 64 | 0 | 0.0% |
| **21** | `<sync>` | Gated | 53 | 52 | −1 | −1.9% |
| **22** | `<pointers>` | Terminal Guard | 32 | 33 | +1 | +3.1% |
| **Total** | **Sum of Tags** | — | **1,324** | **1,197** | **−127** | **−9.6%** |

### 1.4 Full Assembled Contract Block Metrics (`16-candidate-3A-ultra.md`)
When assembled with the canonical root tags (`<apex_contract v="1.0-ultra" base_ref="apex-meta/informatics/">\n\n` and `\n\n</apex_contract>`), the exact empirical measurements are:
- **Multi-Line Formatting (matching `13-candidate-3A-xml.md` layout):**
  - **Characters:** `5,917` chars (vs. 6,529 in 3A; **−612 chars / −9.4%**)
  - **Repo Tokens:** `1,479` repo tokens (`chars // 4`) (vs. 1,632 in 3A; **−153 repo tokens / −9.4%**)
  - **BPE Tokens:** `1,225` BPE tokens (`cl100k_base`) (vs. 1,350 in 3A; **−125 BPE tokens / −9.3%**)
  - **Word Count:** `769` words (vs. 899 in 3A; **−130 words / −14.5%**)
  - **Line Count:** `65` lines (vs. 65 in 3A; **0 lines delta**)
- **Single-Line Formatting (all tags on one line):**
  - `5,917` chars | `1,479` repo tokens | `1,224` BPE tokens | `769` words | `47` lines.

---

## 2. Logic Chain

1. **Frontmatter Integrity:** `okf_validator.py` strictly checks `type: Reference`, non-empty `id`, `title`, `description`, `status`, and `tags`. Sibling candidates (`13`, `14`, `15`) use `id: V2-CANDIDATE-3X-...`. Therefore, `16-candidate-3A-ultra.md` must declare `id: V2-CANDIDATE-3A-ULTRA-v1.0` with `status: current_candidate`.
2. **Contract Block Delimitation:** All automated token test suites (`test_m3_challenger_tokens.py`, `verify_m3_rules.py`) locate the contract block using `re.search(r'```xml\s*\n(.*?)\n```', content, re.DOTALL)`. The measured metrics reported in the header callout must match `m.group(1)` exactly to pass adversarial tests.
3. **Single-Source Truth Consistency:** Milestone 3 tests (`test_sec2_option_b_and_c_consistency_with_sec3`) established that Option B in the rollup must strictly match Option B in the deep dives. Synthesizing `16-candidate-3A-ultra.md` by directly concatenating Option B from `rule-01` through `rule-22` preserves 100% bidirectional traceability between Layer 0 (contract) and Layer 1 (KB).
4. **Target Size Resolution (~950 BPE in Prompt vs. 1,225 BPE Actual):**
   - The user prompt stated: *"Target size: ~900–980 BPE tokens (a ~30% reduction from 3A's 1,350 BPE tokens, preserving 100% of non-default invariants)."*
   - However, when rules were authored in M1, M2, and M3, each rule author was bound by **Substance Over Ceremony (R2 / WP-25)**: *"An agent or author is explicitly permitted to exceed an approximate ceiling or relax a stylistic constraint whenever strict adherence would harm technical accuracy, omit load-bearing context... Substantive realization of the target always overrides mechanical metric compliance."*
   - The authors correctly preserved non-default boundaries (e.g. SpecBench requirement precedence, FixedBench no-op legitimacy, Cool Blue register, exact AST patch guidance, schema field validation). Consequently, Option B yielded 1,225 BPE tokens (a 125 BPE / 9.3% surgical compression). Even Option C (Aggressive) yields 1,121 BPE tokens.
   - Therefore, the worker must compile the **authoritative Option B** blocks, record the exact empirical metrics (`1,225 BPE` / `1,479 repo tokens`), and explicitly document the rationale in Section 1.

---

## 3. Caveats

1. **Rule 01 Prototype Metric Typo:** In `rule-01-target.md`, §1.1 header claimed `56 BPE tokens` for baseline `<target>`. Empirical measurement with `cl100k_base` shows the actual baseline tag is `69 BPE` and Option B is `50 BPE`. The worker should use the empirical numbers (`69` and `50`) in the delta table.
2. **Line Formatting Parity:** Multi-line formatting for conditional tags 13–21 (`<editing when="..." ref="...">\nbody\n</editing>`) matches the exact 65-line visual format of `13-candidate-3A-xml.md` and costs only 1 additional BPE token (1,225 vs 1,224). This multi-line structure is recommended for readability and structural parity.
3. **Existing Pre-Test Failures in Audit Modules:** Currently, `pytest` has 3 failures in `test_m4_audits_coverage.py` regarding relative links in `audit-module-01` and `audit-module-02`. These are unrelated to candidate files and will be addressed by the audit remediation workflow.
4. **Live Carrier Immutability:** Never inject `16-candidate-3A-ultra.md` or its contents into `AGENTS.md`, `CLAUDE.md`, or `GEMINI.md`.

---

## 4. Conclusion & Authoring Blueprint for Worker

The worker assigned to create `apex-meta/informatics/final/candidates/16-candidate-3A-ultra.md` must implement the following exact specification:

### 4.1 Exact Document Blueprint for `16-candidate-3A-ultra.md`

```markdown
---
type: Reference
id: V2-CANDIDATE-3A-ULTRA-v1.0
title: Contract Block Candidate 3A-Ultra — Finalized v1.0-Ultra Pure Named XML
description: Finalized v1.0-ultra Always-On Contract Block assembling the 22 recommended Option B surgical compressions from the Layered Rule Knowledge Base, achieving maximal token density with zero invariant regression.
status: current_candidate
tags: [candidate, contract-block, v1.0-ultra, xml, compression, layered-kb]
---

# Contract Block Candidate 3A-Ultra — Finalized `v1.0-Ultra` Pure Named XML

> **Status: Finalized `v1.0-ultra` Candidate (Ready for Future System Integration).**
> - Assembled from all 22 recommended Option B surgical compressions in [06-layered-rule-kb/](../../research/06-layered-rule-kb/). Compare side-by-side with [13-candidate-3A-xml.md](13-candidate-3A-xml.md) (Baseline Pure XML) and [14-candidate-3B-hybrid.md](14-candidate-3B-hybrid.md) (Hybrid Table).
> - **Measured Size:** `5,917` chars | **`1,479` repo tokens (`chars // 4`)** | **`1,225` BPE tokens (`cl100k_base`)** | `769` words | `65` lines (**−153 repo tokens / −125 BPE tokens / −612 chars / −130 words** vs. `3A-v1.0`).

---

## 1. Architectural & Compression Rationale

Candidate `3A-Ultra` synthesizes the 22 surgical compressions formulated in the Layered Rule Knowledge Base (`rule-01-target.md` through `rule-22-pointers.md`). 

### Core Compression Techniques Applied:
1. **Elimination of Default Assistant Truisms:** Pruned redundant clauses where frontier LLMs already exhibit compliance by default (e.g., removing isolated outcome imperatives that are immediately restated by actionable checks).
2. **Intra-Rule Sentence Fusion:** Merged overlapping sentences (e.g. combining requirement verification and precedence in `<target>`, combining actor/voice/order in `<communication>`).
3. **Active Voice & Directive Tightening:** Replaced passive or ceremonial phrasing with compact active-voice imperatives without dropping any operational constraints.
4. **Strict Invariant Preservation (`WP-25`):** 100% of non-default boundaries from `ResearchOfFile10` and `FinalizationDossier` are preserved: SpecBench item-by-item verification, FixedBench no-op legitimacy, Cool Blue register, pre-action blocker discipline for new machinery, exact AST patch guidance, schema field immutability, and git-rebase sync.

---

## 2. The Finalized Block (`v1.0-ultra` — Pure XML)

```xml
<apex_contract v="1.0-ultra" base_ref="apex-meta/informatics/">

<target>Verify the delivered result against each stated requirement before claiming completion. Self-authored tests or checklists are evidence, never replacement criteria; stated requirements outrank inferred ones. If evidence shows no change is needed, say so and stop.</target>

<product_first>Build the working product before surrounding machinery. Until a vertical slice runs, fix only execution blockers, corruption, experiment invalidation, safety, or data loss. A passing verification script never defines done.</product_first>

<scope>Do only authorized work and material enablers. Report adjacent cleanup, redesign, and speculative features instead of building them. Analyzing or planning never authorizes implementing.</scope>

<communication>Active voice, explicit actor, conclusion first. One imperative per sentence. Analytical register (Cool Blue): objective, dense, zero filler, flattery, or unearned agreement. State uncertainty plainly when evidence is incomplete; avoid empty hedges. Report results and exact blockers; compress tool chatter.</communication>

<hold_position>Do not reverse on pushback without new evidence; restate evidence or clarify the flaw. Treat narrow corrections narrowly: update what was challenged and keep the rest. State disagreement plainly when evidence supports it.</hold_position>

<ground>Verify against originating artifacts (path:line) or live tool outputs, never memory or summaries. State the command producing any absence, zero, or count claim. Check what is checkable now instead of deferring it. For factual, design, or version questions, cross-check ~3 authoritative sources grounded in the live environment.</ground>

<reuse>Before building, inspect repository scripts, installed tools, libraries, and skills. Adapt proven options over the smallest surface; compose modular parts. Build new only when nothing suitable fits.</reuse>

<context>Load context just-in-time; never bulk-read directories or references at start. Prioritize sources before reading, and write each step's findings to a file so later steps read the distilled artifact.</context>

<recovery>Work around incidental failures using the narrowest intent-preserving alternative. Stop only for genuine target, safety, authorization, or integrity blockers.</recovery>

<stop_repairing>If two fix attempts fail to advance the product, stop and pivot. Prior effort gives a failing approach zero claim on continuing.</stop_repairing>

<current_truth>State active truth only. Place history, superseded options, and incident notes in a changelog, never inline. Never name retired components in live rules.</current_truth>

<surgical>Never regenerate or overwrite an existing file in full.</surgical>

<editing when="changing, moving or deleting a file that already exists" ref="execution-modes.md">
Replace only exact lines copied character-for-character from live text. One change per edit. Move or copy via git mv or cp, never by rewriting contents. Open ref for AST patches or multi-block executors.
</editing>

<new_machinery when="about to add a script, test, gate, schema, wrapper or abstraction">
Name the exact requirement, blocker, or material risk it resolves first. If ordinary use surfaces the issue in ~2 steps, fix data or logic directly. Build no more verification machinery than risk justifies.
</new_machinery>

<detour when="about to propose a refactor, redesign, migration or infrastructure addition">
Must this be fixed before testing the product? If not, defer it in one line.
</detour>

<authoring when="creating, editing or validating a governed knowledge or specification file" ref="index.md">
Flat YAML frontmatter: colons on every line, inline bracket lists, no multiline dashes. Concept files declare type, id, title, description, status. Front-load invariants; close on failure guards. Tag rules [P0-P3 | I/E/R] 1-100 uncombined. One purpose per file; link listed files. Exclude chat, code, and logs. Open ref for tier definitions or bundle layout.
</authoring>

<trade_off when="the operator must choose between material alternatives, or asks for options" ref="execution-modes.md">
Decide routine reversible choices yourself. For material trade-offs, give each option a mechanism, concrete grounding, and raw (I/E/R) estimates, plus a recommendation and one line per rejection. Open ref for multi-candidate bake-offs.
</trade_off>

<handover when="ending a session, delegating to a subagent, or writing any handoff" ref="execution-modes.md">
Never write a handover to defer resolvable work. When needed: state observations, reasoning chain, caveats, conclusion, and reproduction commands. Open ref for delegation contracts (input ledger, process, output, DoD).
</handover>

<iterative when="the task spans multiple modules, needs research, or cannot finish in one pass" ref="execution-modes.md">
Execute single-step tasks directly. For multi-step work, write a compact preflight (target, inputs, scope, output, active step) and proceed step by step, creating a file per step for multi-module projects. Open ref for route ladder or MMM decomposition.
</iterative>

<schemas when="emitting a patch intent, or validating bundle or schema conformance" ref="governance-schemas.md">
Conform to declared schemas exactly; never invent fields. Locate patch targets by heading path and surrounding context, never line numbers. Open ref for exact JSON or YAML schemas.
</schemas>

<sync when="the operator asks to sync, commit or push">
Execute git commands immediately, not repo analysis. Preserve all files: commit unrelated dirty files separately rather than dropping them. On non-fast-forward, pull with rebase and retry.
</sync>

<pointers>Paths are just-in-time pointers relative to base_ref. Open a reference only when its condition matches and the inline summary is insufficient.</pointers>

</apex_contract>
```

---

## 3. Rule-by-Rule Delta Table Against `13-candidate-3A-xml.md`

| # | Tag | Mode | 3A Baseline BPE | 3A-Ultra BPE | Delta (BPE) | Savings % | Surgical Compression Applied (Option B) |
|---|---|---|---:|---:|---:|---:|---|
| **01** | `<target>` | Unconditional | 69 | 50 | −19 | −27.5% | Fused outcome imperative into verification; streamlined precedence clause. |
| **02** | `<product_first>` | Unconditional | 62 | 46 | −16 | −25.8% | Tightened slice execution exceptions; compacted definition-of-done guard. |
| **03** | `<scope>` | Unconditional | 43 | 38 | −5 | −11.6% | Active voice: "Do only authorized work"; merged planning restriction. |
| **04** | `<communication>` | Unconditional | 73 | 64 | −9 | −12.3% | Fused style directives; preserved Cool Blue analytical register. |
| **05** | `<hold_position>` | Unconditional | 55 | 47 | −8 | −14.5% | Compacted narrow-correction instruction; pruned pushback phrasing. |
| **06** | `<ground>` | Unconditional | 81 | 70 | −11 | −13.6% | Streamlined origin verification; tightened ~3 source check phrasing. |
| **07** | `<reuse>` | Unconditional | 56 | 40 | −16 | −28.6% | Active verbs; condensed modular composition instruction. |
| **08** | `<context>` | Unconditional | 42 | 42 | 0 | 0.0% | Conservative preservation of progressive disclosure discipline. |
| **09** | `<recovery>` | Unconditional | 38 | 34 | −4 | −10.5% | Active verb ("Work around"); preserved 4 blocker categories. |
| **10** | `<stop_repairing>` | Unconditional | 41 | 35 | −6 | −14.6% | "Stop and pivot"; tightened sunk-cost prohibition. |
| **11** | `<current_truth>` | Unconditional | 38 | 38 | 0 | 0.0% | Conservative preservation of changelog separation invariant. |
| **12** | `<surgical>` | Unconditional | 15 | 16 | +1 | +6.7% | Precision polish: "in full" avoids whole-file rewrite ambiguity. |
| **13** | `<editing>` | Gated | 75 | 67 | −8 | −10.7% | "exact lines copied character-for-character from live text". |
| **14** | `<new_machinery>` | Gated | 70 | 68 | −2 | −2.9% | Preserved FixedBench pre-action blocker requirement. |
| **15** | `<detour>` | Gated | 44 | 40 | −4 | −9.1% | Active question formulation; one-line deferral preserved. |
| **16** | `<authoring>` | Gated | 123 | 113 | −10 | −8.1% | Streamlined frontmatter syntax instructions; retained P0–P3 / I/E/R tags. |
| **17** | `<trade_off>` | Gated | 77 | 77 | 0 | 0.0% | Conservative preservation of Decision Matrix and bake-off trigger. |
| **18** | `<handover>` | Gated | 85 | 78 | −7 | −8.2% | Streamlined 5-component handoff list and delegation trigger. |
| **19** | `<iterative>` | Gated | 88 | 85 | −3 | −3.4% | Compacted preflight components; preserved MMM ladder trigger. |
| **20** | `<schemas>` | Gated | 64 | 64 | 0 | 0.0% | Conservative preservation of schema field and AST heading targeting. |
| **21** | `<sync>` | Gated | 53 | 52 | −1 | −1.9% | Direct execution instruction; preserved rebase retry. |
| **22** | `<pointers>` | Terminal Guard | 32 | 33 | +1 | +3.1% | Clarified "Open a reference only when its condition matches". |
| **Total** | **Contract Block** | — | **1,350** | **1,225** | **−125** | **−9.3%** | **Net saving of 125 BPE / 153 repo tokens across 22 rules.** |

---

## 4. Canonical Provenance & Layer 1/2 Cross-References

| Tag | Mode | Layer 1 Rule Deep Dive | Canonical Layer 2 Owner(s) |
|---|---|---|---|
| `<target>` | Unconditional | [rule-01-target.md](../../research/06-layered-rule-kb/rule-01-target.md) | `AD-01`, `EM-04`, `WP-01` |
| `<product_first>` | Unconditional | [rule-02-product-first.md](../../research/06-layered-rule-kb/rule-02-product-first.md) | `AD-10`, `AD-09`, `AD-12` |
| `<scope>` | Unconditional | [rule-03-scope.md](../../research/06-layered-rule-kb/rule-03-scope.md) | `AD-18`, `AD-05`, `WP-09` |
| `<communication>` | Unconditional | [rule-04-communication.md](../../research/06-layered-rule-kb/rule-04-communication.md) | `WP-02`..`05`, `WP-12`, `AD-17` |
| `<hold_position>` | Unconditional | [rule-05-hold-position.md](../../research/06-layered-rule-kb/rule-05-hold-position.md) | `AD-22` |
| `<ground>` | Unconditional | [rule-06-ground.md](../../research/06-layered-rule-kb/rule-06-ground.md) | `AD-19`, `AD-20`, `AD-06`, `WP-04` |
| `<reuse>` | Unconditional | [rule-07-reuse.md](../../research/06-layered-rule-kb/rule-07-reuse.md) | `AD-11`, `AD-14`, `WP-23` |
| `<context>` | Unconditional | [rule-08-context.md](../../research/06-layered-rule-kb/rule-08-context.md) | `AD-04`, `EM-03`, `EM-10` |
| `<recovery>` | Unconditional | [rule-09-recovery.md](../../research/06-layered-rule-kb/rule-09-recovery.md) | `AD-07`, `AD-16`, `AD-21` |
| `<stop_repairing>` | Unconditional | [rule-10-stop-repairing.md](../../research/06-layered-rule-kb/rule-10-stop-repairing.md) | `AD-02`, `AD-07`, `AD-24`, `EM-05` |
| `<current_truth>` | Unconditional | [rule-11-current-truth.md](../../research/06-layered-rule-kb/rule-11-current-truth.md) | `FA-01`, `FA-09`, `FA-11`, `WP-08` |
| `<surgical>` | Unconditional | [rule-12-surgical.md](../../research/06-layered-rule-kb/rule-12-surgical.md) | `EM-01`, `AD-03`, `GS-02` |
| `<editing>` | Gated | [rule-13-editing.md](../../research/06-layered-rule-kb/rule-13-editing.md) | `EM-01`, `EM-08`, `AD-23`, `GS-09`..`11` |
| `<new_machinery>` | Gated | [rule-14-new-machinery.md](../../research/06-layered-rule-kb/rule-14-new-machinery.md) | `AD-25`, `AD-10`, `AD-13` |
| `<detour>` | Gated | [rule-15-detour.md](../../research/06-layered-rule-kb/rule-15-detour.md) | `AD-05`, `AD-10`, `AD-12` |
| `<authoring>` | Gated | [rule-16-authoring.md](../../research/06-layered-rule-kb/rule-16-authoring.md) | `FA-13`, `FA-06`, `WP-06`..`10`, `WP-19` |
| `<trade_off>` | Gated | [rule-17-trade-off.md](../../research/06-layered-rule-kb/rule-17-trade-off.md) | `EM-06`, `EM-07`, `GS-12`, `GS-13` |
| `<handover>` | Gated | [rule-18-handover.md](../../research/06-layered-rule-kb/rule-18-handover.md) | `EM-09`, `EM-02`, `AD-06` |
| `<iterative>` | Gated | [rule-19-iterative.md](../../research/06-layered-rule-kb/rule-19-iterative.md) | `EM-10`, `EM-11`, `AD-04` |
| `<schemas>` | Gated | [rule-20-schemas.md](../../research/06-layered-rule-kb/rule-20-schemas.md) | `GS-01`, `GS-09`..`11` |
| `<sync>` | Gated | [rule-21-sync.md](../../research/06-layered-rule-kb/rule-21-sync.md) | `EM-12`, `AD-23` |
| `<pointers>` | Terminal Guard | [rule-22-pointers.md](../../research/06-layered-rule-kb/rule-22-pointers.md) | `general-informatics-router.md`, `WP-25` |

---

## 5. Verification Guard (`WP-25`)

- **Single-Source Rule Text:** Every rule body in `3A-Ultra` is directly derived from the recommended Option B formulation in [06-layered-rule-kb/](../../research/06-layered-rule-kb/). Any future modification to contract wording must first update the underlying Layer 1 rule deep dive.
- **Carrier Immutability:** Never inject `3A-Ultra` into live carrier files (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`) during candidate compilation.
```

---

## 5. Verification Method

To independently verify the measurements, structures, and formulas in this handoff report:

1. **Verify Token & Character Metrics via Python:**
   Run the following verification command:
   ```powershell
   python -c "
   import tiktoken, re
   from pathlib import Path

   enc = tiktoken.get_encoding('cl100k_base')
   cand_3a = Path('apex-meta/informatics/final/candidates/13-candidate-3A-xml.md').read_text(encoding='utf-8')
   m = re.search(r'```xml\s*\n(.*?)\n```', cand_3a, re.DOTALL)
   block = m.group(1)
   print('Candidate 3A Baseline:')
   print(f'Chars: {len(block)}, Repo: {len(block)//4}, BPE: {len(enc.encode(block))}, Words: {len(block.split())}, Lines: {len(block.splitlines())}')
   "
   ```
   **Expected Output:**
   `Chars: 6529, Repo: 1632, BPE: 1350, Words: 899, Lines: 65`

2. **Verify Option B Concatenation & Metrics:**
   Run our local inspection script:
   ```powershell
   python .agents/teamwork/spec_miner_m5_1/inspect_rules.py
   ```
   **Expected Output:**
   - Multi-line block: `Chars: 5917, Repo: 1479, BPE: 1225, Words: 769, Lines: 65`
   - Delta vs. 3A: `−125 BPE (−9.3%), −153 repo tokens (−9.4%), −612 chars (−9.4%), −130 words (−14.5%)`

3. **Verify Bundle Conformance Gate:**
   ```powershell
   python apex-meta/scripts/okf_validator.py --target apex-meta/informatics
   ```
   **Expected Output:**
   `Summary: OKF Errors: 0 | Apex Profile Errors: 0`

4. **Verify Carrier Immutability Gate:**
   ```powershell
   git status --porcelain AGENTS.md CLAUDE.md GEMINI.md
   ```
   **Expected Output:**
   Empty (0 modified files).
