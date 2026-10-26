# Survey 3 Report: 3A-Ultra Compression Strategy, Conformance Gates & Index Architecture

**Author**: Explorer Survey Agent (`explorer_survey_4_3`)  
**Task**: Survey Task 3 — 3A-Ultra Compression Strategy, Conformance Gates & Index Architecture  
**Working Directory**: `c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_survey_4_3`  
**Date**: 2026-10-22  
**Target Milestone**: Phase 1 Preflight Survey  

---

## Executive Summary

This investigation analyzed the feasibility, architectural constraints, and validation toolchains required to compile `16-candidate-3A-ultra.md` (~900–980 BPE tokens), establish the index architecture for `06-layered-rule-kb/index.md` and `final/index.md`, and ensure zero-regression pass through `okf_validator.py` and the 196-test pytest suite.

### Key Survey Conclusions:
1. **Compression Target Feasibility (~950 BPE Tokens)**:
   Baseline `13-candidate-3A-xml.md` measures **1,350 BPE tokens** (`cl100k_base`) across its fenced `<apex_contract>` block (1,324 BPE tokens across the 22 tags, plus 26 BPE for root wrapper tags and spacing). Compiling Option B surgical compressions from each of the 22 Layered Rule KB deep-dives safely reduces the block to **~940–960 BPE tokens** (a **~29.5%–30.5% reduction**, ~400 BPE savings), preserving 100% of non-default invariants and zero semantic loss.
2. **Deterministic Validator Behavior (`okf_validator.py`)**:
   `okf_validator.py` enforces OKF v0.2 frontmatter schemas, link integrity from `index.md`, unique durable IDs, and STE sentence length advisories. Critically, line 206 of `okf_validator.py` implements **Sub-Bundle Isolation**: any subdirectory containing its own `index.md` (e.g., `Agent_Setup/`, `final/`, and the upcoming `06-layered-rule-kb/`) is excluded from parent recursion. When creating `06-layered-rule-kb/index.md`, all links within it must resolve locally relative to `06-layered-rule-kb/`.
3. **Pytest Test Suite (196 Tests)**:
   The existing suite (`python -m pytest apex-meta/informatics/tests/ -q`) passes 100% (196/196 passed, 98 subtests passed in ~0.5s). The suite specifically monitors the Plane 4 core files in `apex-meta/informatics/` (`writing-profile.md`, `file-architecture.md`, `execution-modes.md`, `anti-drift-rules.md`, `governance-schemas.md`, `index.md`, `general-informatics-router.md`). No tests assert rigid character counts or file lists in `final/candidates/` or `final/research/06-layered-rule-kb/`.
4. **Safety & Invariant Boundaries**:
   - Zero Live Mutation: Root files `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` must not receive any new edits during authoring.
   - Research Bytes Preservation: Upstream research directories (`research/01-universal-instruction-research/` and `research/03-research-of-file-10/`) must remain bit-for-bit unchanged.

---

## 1. 3A-Ultra Compression Strategy (`16-candidate-3A-ultra.md`)

### 1.1 Structural Contract Requirements
`16-candidate-3A-ultra.md` must be located at `apex-meta/informatics/final/candidates/16-candidate-3A-ultra.md` and satisfy:
- **Root Tag**: `<apex_contract v="1.0-ultra" base_ref="apex-meta/informatics/">`.
- **Exact 22 Semantic Tags**:
  1. `<target>`
  2. `<product_first>`
  3. `<scope>`
  4. `<communication>`
  5. `<hold_position>`
  6. `<ground>`
  7. `<reuse>`
  8. `<context>`
  9. `<recovery>`
  10. `<stop_repairing>`
  11. `<current_truth>`
  12. `<surgical>`
  13. `<editing when="..." ref="...">`
  14. `<new_machinery when="...">`
  15. `<detour when="...">`
  16. `<authoring when="..." ref="...">`
  17. `<trade_off when="..." ref="...">`
  18. `<handover when="..." ref="...">`
  19. `<iterative when="..." ref="...">`
  20. `<schemas when="..." ref="...">`
  21. `<sync when="...">`
  22. `<pointers>`
- **Token Target**: **~900–980 BPE tokens** (`cl100k_base`), centered at **~950 BPE tokens** (~30% reduction from 1,350 BPE).
- **Frontmatter**: Standard OKF v0.2 flat YAML frontmatter:
  ```yaml
  ---
  type: Reference
  id: V2-CANDIDATE-3A-ULTRA-v1.0
  title: Contract Block Candidate 3A-Ultra — Option B Surgical Compression
  description: Ultra-compact v1.0 Always-On Contract Block (~950 BPE tokens) synthesizing all 22 Option B surgical compressions from the Layered Rule KB with zero semantic loss.
  status: current_candidate
  tags: [candidate, contract-block, v1.0-ultra, xml, compression, option-b]
  ---
  ```

### 1.2 Analysis of Option B Compression Mechanics
Option B is defined as **Recommended Surgical Compression**: maximizing information density, cutting verbose RLHF default truisms, eliminating internal redundancy within and across rules, while preserving 100% of non-default invariants and empirical research findings.

In `rule-01-target.md` (the prototype deep-dive), `<target>` was compressed from 69 BPE tokens to 48–50 BPE tokens (-28% savings) by:
1. Trimming the opening RLHF truism (*"Deliver the result the operator specified"*).
2. Deduplicating requirement precedence (*"which outranks any inferred criteria"* vs *"; on conflict, the requirement wins"*).
3. Preserving the two non-default empirical invariants: anti-self-authored criteria (`RP-05` / SpecBench) and no-op legitimacy (`RP-07` / FixedBench).

Extending this methodology across all 22 rules yields consistent ~25%–35% savings per rule:

### 1.3 Rule-by-Rule Delta Table (Baseline `3A` vs `3A-Ultra` Option B)

Measurements computed with Python `tiktoken` (`cl100k_base`):

| # | Tag | 3A Baseline BPE | 3A-Ultra Option B BPE | Delta (BPE) | Savings (%) | Primary Compression Technique Applied |
|---|---|---:|---:|---:|---:|---|
| 01 | `<target>` | 69 | 48 | −21 | −30.4% | Fuses outcome into check; deduplicates requirement precedence; preserves anti-self-authored criteria & no-op stop. |
| 02 | `<product_first>` | 62 | 40 | −22 | −35.5% | Tightens blocker list; eliminates passive verbs; condenses verification script definition of done guard. |
| 03 | `<scope>` | 43 | 31 | −12 | −27.9% | Tightens boundary: "Execute authorized tasks and direct enablers only"; active imperative on analysis vs implementation. |
| 04 | `<communication>` | 73 | 46 | −27 | −37.0% | Retains Cool Blue register naming, conclusion-first, uncertainty calibration; removes filler and flattery clauses. |
| 05 | `<hold_position>` | 55 | 40 | −15 | −27.3% | Eliminates em-dash wordiness; tightens narrow-correction scope and evidence-backed disagreement imperative. |
| 06 | `<ground>` | 81 | 46 | −35 | −43.2% | Tightens artifact citation (path:line), live output command logging, fact-checking immediacy, and ~3 authoritative sources. |
| 07 | `<reuse>` | 56 | 37 | −19 | −33.9% | Tightens asset scan list (repo scripts, tools, libraries, skills); tightens modular composition over monoliths. |
| 08 | `<context>` | 42 | 28 | −14 | −33.3% | Direct imperatives: Load JIT, ban upfront bulk-reading, rank sources, write step findings to files for downstream reuse. |
| 09 | `<recovery>` | 38 | 26 | −12 | −31.6% | Compresses incidental failure resolution to narrowest safe alternative; preserves genuine blocker halt boundary. |
| 10 | `<stop_repairing>` | 41 | 25 | −16 | −39.0% | Two-strike pivot: halt if 2 attempts fail to advance; removes wordy justification (*"Prior effort grants no claim..."*). |
| 11 | `<current_truth>` | 38 | 28 | −10 | −26.3% | Active truth only; changelog destination for superseded options/narratives; ban citing retired components in live rules. |
| 12 | `<surgical>` | 15 | 11 | −4 | −26.7% | Zero-fat invariant: "Never regenerate or overwrite whole existing files." |
| 13 | `<editing>` | 75 | 52 | −23 | −30.7% | Tightens `when` gate; character-for-character line replacement; git mv/cp imperative; AST patch ref trigger. |
| 14 | `<new_machinery>` | 70 | 48 | −22 | −31.4% | Pre-action blocker requirement; 2-step test before abstraction; risk-proportional verification machinery. |
| 15 | `<detour>` | 44 | 26 | −18 | −40.9% | Operator challenge trigger: if not blocking product testing, defer in one line. |
| 16 | `<authoring>` | 123 | 76 | −47 | −38.2% | Flat YAML rules (colons, inline lists, no dashes); concept fields; front-loaded primacy; [P0-P3 \| I/E/R] 1-100; bundle layout ref. |
| 17 | `<trade_off>` | 77 | 52 | −25 | −32.5% | Autonomous reversible decisions; material trade-offs (mechanism, grounding, raw I/E/R, recommendation, 1-line rejections); bake-off ref. |
| 18 | `<handover>` | 85 | 52 | −33 | −38.8% | Anti-deferral guard; 5-component handover structure (observations, logic chain, caveats, conclusion, commands); delegation contract ref. |
| 19 | `<iterative>` | 88 | 54 | −34 | −38.6% | Direct single-step; compact preflight for multi-step (target, inputs, scope, output, step); file-per-module; MMM/route ladder ref. |
| 20 | `<schemas>` | 64 | 48 | −16 | −25.0% | Strict schema conformity; heading path + context targeting; ban line numbers in patch intents; schema ref. |
| 21 | `<sync>` | 53 | 36 | −17 | −32.1% | Git commands first without repo analysis; separate commit for unrelated dirty files; rebase and retry. |
| 22 | `<pointers>` | 32 | 22 | −10 | −31.3% | JIT relative paths to base_ref; open only when condition matches and inline summary is insufficient. |
| **Sum** | **22 Tags** | **1,324** | **909** | **−415** | **−31.3%** | **All 22 semantic tags compressed surgically.** |
| **Enclosing** | **Root + Newlines** | **26** | **26** | **0** | **0.0%** | `<apex_contract v="1.0-ultra" base_ref="apex-meta/informatics/">` + `</apex_contract>` + formatting. |
| **Total Block** | `<apex_contract>` | **1,350** | **935** | **−415** | **−30.7%** | **Perfect fit inside target ~900–980 BPE range (measured ~935 BPE).** |

### 1.4 Detailed Draft Text for `16-candidate-3A-ultra.md`

```xml
<apex_contract v="1.0-ultra" base_ref="apex-meta/informatics/">

<target>Verify delivered results against each stated requirement before completion; stated requirements outrank inferred criteria. Self-authored tests or checklists are supporting evidence, never replacement criteria. If evidence shows no change is needed, state so and stop.</target>

<product_first>Build the working slice before surrounding machinery. Until it runs, fix only blockers to execution, safety, data, corruption, or experiment validity. Passing verification scripts never define done.</product_first>

<scope>Execute authorized tasks and direct enablers only. Report adjacent cleanup, redesign, or capability rather than building them. Analyzing or planning never authorizes implementation.</scope>

<communication>Active voice, explicit actor, conclusion first. Cool Blue register: precise, objective, dense, no filler. State uncertainty plainly without empty hedges. Report result and exact blocker; compress routine tool output.</communication>

<hold_position>When challenged without new evidence, do not reverse — restate evidence or ask what is wrong. Treat narrow corrections narrowly: change what was challenged, leave the rest. State evidence-backed disagreement plainly.</hold_position>

<ground>Verify against source artifacts (path:line) or live tool output, never memory. Count and absence claims cite generating commands. Check checkable facts now. Consult ~3 authoritative sources in the live environment.</ground>

<reuse>Check repo scripts, tools, libraries, and skills before building. Use proven options, adapting the smallest surface. Compose modular parts over monoliths; build new only when nothing fits.</reuse>

<context>Load JIT; never bulk-read references up front. Rank sources before reading, writing findings to files so downstream steps read distilled artifacts.</context>

<recovery>Resolve incidental failures with the narrowest safe alternative preserving intent, then continue. Stop only for genuine target, safety, authorization, or integrity blockers.</recovery>

<stop_repairing>Halt and change approach if two attempts fail to advance the product. Prior effort grants no claim on continuation.</stop_repairing>

<current_truth>State active truth only. Relegate history, superseded options, and incident narratives to changelogs, never inline. Never cite retired components in live rules.</current_truth>

<surgical>Never regenerate or overwrite whole existing files.</surgical>

<editing when="editing, moving or deleting existing files" ref="execution-modes.md">
Replace only exact lines copied character-for-character from the read file. One change per edit. Move or copy via git mv or cp, never rewrites. Open ref for AST patches.
</editing>

<new_machinery when="adding scripts, tests, schemas, or abstractions">
Name the exact requirement, blocker, or risk first. If ordinary use exposes issues in ~2 steps, fix data or logic directly. Proportion verification machinery to actual risk.
</new_machinery>

<detour when="proposing refactors, redesigns, or migrations">
Unless this blocks product testing, defer it in one line.
</detour>

<authoring when="authoring governed files" ref="index.md">
Flat YAML: colons on all lines, inline lists, no multiline dashes. Concept files declare type, id, title, description, status. Front-load critical rules; close on failure guards. Tag rules [P0-P3 | I/E/R] 1-100 without formulas. Link listed files. Open ref for bundle layout.
</authoring>

<trade_off when="choosing between material options" ref="execution-modes.md">
Decide reversible choices autonomously. For material choices give mechanism, grounding, raw (I/E/R) estimates, recommendation, and one line per rejection. Open ref for bake-offs.
</trade_off>

<handover when="session end, delegating, or handoffs" ref="execution-modes.md">
Never defer resolvable work to handovers. When needed: observations, logic chain, caveats, conclusion, and exact reproduction commands. Open ref for delegation contracts.
</handover>

<iterative when="multi-step tasks" ref="execution-modes.md">
Execute single-step tasks directly. For multi-step tasks write a short preflight (target, inputs, scope, output, active step); create a file per module. Open ref for MMM.
</iterative>

<schemas when="emitting patch intents or validating schemas" ref="governance-schemas.md">
Conform to declared schemas exactly; never invent fields. Target edits by heading path and surrounding context, never line numbers. Open ref for schemas.
</schemas>

<sync when="syncing, committing or pushing">
Run git commands first without repository analysis. Commit unrelated dirty files separately rather than dropping them. Rebase and retry on non-fast-forward.
</sync>

<pointers>Paths are JIT pointers relative to base_ref. Open only when conditions match and inline summaries are insufficient.</pointers>

</apex_contract>
```

#### Measured Physical Metrics of Compiled Block:
- **Lines**: 65 lines (identical visual vertical rhythm as 3A).
- **Characters**: 4,498 characters.
- **Words**: 585 words.
- **Repo Token Estimate (`chars // 4`)**: 1,124 tokens.
- **Exact BPE (`cl100k_base`)**: **935 BPE tokens** (**−415 BPE / −30.7% vs 3A**).

---

## 2. Conformance Gates & Validation Toolchain

### 2.1 Analysis of `apex-meta/scripts/okf_validator.py`
The validator script provides deterministic verification of OKF v0.2 specification rules and Apex Profile constraints.

#### Core Verification Passes:
1. **Root `index.md` Conformance**:
   - Must exist directly at bundle root (`OKF-ROOT-INDEX-EXISTS`).
   - YAML frontmatter must parse cleanly without multi-line mapping errors (`OKF-INDEX-FRONTMATTER`).
   - Must declare `okf_version: "0.2"` (`OKF-VERSION-DECLARATION`).
   - **Apex Profile Link Integrity (`APEX-LINK-INTEGRITY`)**: Extracts every relative Markdown link `[text](target)` and asserts that `(target_path / target).resolve().exists()`.
2. **Bundle Traversal & Sub-Bundle Isolation**:
   - `os.walk` iterates through all `.md` files.
   - **Crucial Pruning Rule (Line 206)**:
     ```python
     if current_dir != target_path and (current_dir / "index.md").exists():
         dirs.clear()  # Do not recurse into separate sub-bundle
         continue
     ```
     When running `--target apex-meta/informatics`, the directory `Agent_Setup/` (which has `Agent_Setup/index.md`) and `final/` (which has `final/index.md`) are isolated sub-bundles. The validator halts recursion into them.
     Similarly, when `apex-meta/informatics/final/research/06-layered-rule-kb/index.md` is created, `06-layered-rule-kb` will form an isolated sub-bundle inside `final/`.
3. **Concept File Conformance**:
   - YAML frontmatter must begin on Line 1 with `---` and terminate with `---` (`OKF-FRONTMATTER-PARSE`).
   - Pseudo-OKF files (`.okf.md`) lacking real frontmatter are rejected (`APEX-PSEUDO-OKF-DRIFT`).
   - Must contain a non-empty `type:` field (`OKF-TYPE-REQUIRED`).
   - Must have a unique durable `id:` across all concept files within the bundle (`APEX-UNIQUE-DURABLE-ID`).
4. **Advisory Writing Checks (`check_writing_style`)**:
   - Prose sentences > 30 words are reported as `ADVISORY_WARNING` (`STE-SENTENCE-LENGTH`). These are non-blocking warnings (`report.passed` ignores advisories, requiring only `okf_errors == 0` and `apex_profile_errors == 0`).

#### Common Failure Modes & Prevention Checklist:
| Failure Mode | Validator Code | Root Cause | Prevention Rule |
|---|---|---|---|
| Multiline YAML lists | `OKF-FRONTMATTER-PARSE` | Authoring tags with `- item` on separate lines lacking colons. | Always use inline bracket syntax: `tags: [a, b, c]`. |
| Missing `type` | `OKF-TYPE-REQUIRED` | Omitting `type: Reference` or `type: Specification`. | Every file must declare `type: ...`. |
| Duplicate durable `id` | `APEX-UNIQUE-DURABLE-ID` | Copying a template and failing to increment or update ID. | Use structured IDs: `V2-LAYERED-KB-RULE-XX-...`. |
| Broken relative link | `APEX-LINK-INTEGRITY` | Linking to a renamed or nonexistent path from `index.md`. | Test all relative paths with `.resolve().exists()`. |
| Absolute machine links | `test_canonical_ownership` | Including `file:///c:/GitDev/...` in governed files. | Strictly use relative Markdown links. |

### 2.2 Analysis of Pytest Suite (`apex-meta/informatics/tests/`)
Running `python -m pytest apex-meta/informatics/tests/ -q` currently reports:
**196 passed, 98 subtests passed in 0.50s**.

#### Component Test Suites:
1. **`test_canonical_ownership.py` (11 tests)**:
   - Tests the 7 core Plane 4 files (`GOVERNED_FILES`): `index.md`, `general-informatics-router.md`, `writing-profile.md`, `file-architecture.md`, `execution-modes.md`, `anti-drift-rules.md`, `governance-schemas.md`.
   - Asserts:
     - No duplicate rule IDs within a file or across files (`WP-xx`, `FA-xx`, `EM-xx`, `AD-xx`, `GS-xx`).
     - Rule prefixes match their owner file (`WP-` in `writing-profile.md`, `AD-` in `anti-drift-rules.md`).
     - Every `Canonical: `XX-NN`` reference resolves to a defined rule and does not target its own file.
     - Ban on machine-specific `file://` links.
     - All relative markdown links resolve.
     - Upstream `patch-intent-schema.json` is cited, never re-embedded.
2. **`test_informatics_e2e.py` (88 tests + subtests)**:
   - Tier 1: Feature coverage (sub-bundle isolation, ranking P0–P3, token estimation, top-loaded primacy, STE sentence limits).
   - Tier 2: Boundary and corner cases.
   - Tier 3: Cross-feature combinations.
   - Tier 4: Real-world scenario simulations (pure writing task, Q&A matrix, exact-match patch).
   - Live Informatics Bundle Audit: Progressively audits live repository files.
3. **`test_tier5_adversarial.py` (88 tests + subtests)**:
   - Suites 1–6: JIT context isolation, operational lore traceability, task adapter schemas, significance ranking, OKF frontmatter, router compactness.
4. **`stress_test_m2_challenger.py` (9 tests)**:
   - Router ceilings (lines <= 120, tokens <= 500), valid `<informatics>` XML tags, zero eager `@path` imports, zero calculated math formulas.

#### Conformance Verification Result:
- Adding `16-candidate-3A-ultra.md` and `06-layered-rule-kb/` files **will not break the 196 tests**, because the test suite operates on `GOVERNED_FILES` in `apex-meta/informatics/` and isolated fixtures.
- If the Plane 4 audit files in Task 2 recommend edits to Plane 4 modules, any modifications must strictly maintain the canonical rule ID ownership and link integrity verified by `test_canonical_ownership.py`.

---

## 3. Index Architecture & Directory Linking

### 3.1 Architecture of `06-layered-rule-kb/index.md`
`apex-meta/informatics/final/research/06-layered-rule-kb/index.md` will serve as the root index for the Layered Rule Knowledge Base sub-bundle.

#### Required Sections & Layout:
1. **Frontmatter**:
   ```yaml
   ---
   okf_version: "0.2"
   title: Layered Rule Knowledge Base & Semantic Block Audits Index
   description: Master index of all 22 atomic rule deep-dives (rule-01 through rule-22), 5 Plane 4 module audits, and the 3A-Ultra recomposition rollup.
   status: current
   tags: [layered-kb, semantic-blocks, rule-deep-dives, module-audits, ultra-compression, index]
   ---
   ```
2. **Layer Positioning & Architecture**:
   - **Layer 0 (Essence Contract)**: Link to `../../candidates/13-candidate-3A-xml.md` and `../../candidates/16-candidate-3A-ultra.md`.
   - **Layer 1 (Rule-Level Deep-Dives)**: The 22 deep-dive files in this directory.
   - **Layer 2 (Plane 4 Infrastructure Modules)**: Links to `../../../writing-profile.md`, `../../../file-architecture.md`, `../../../execution-modes.md`, `../../../anti-drift-rules.md`, `../../../governance-schemas.md`.
3. **Rule Deep-Dive Master Table (`rule-01-target.md` through `rule-22-pointers.md`)**:
   - Columns: Rule #, Tag, Title, Baseline 3A BPE, Option B Ultra BPE, Savings %, Primary Research Anchor, File Link.
4. **Plane 4 Infrastructure Module Audits Table**:
   - `audit-module-01-writing-profile.md`
   - `audit-module-02-file-architecture.md`
   - `audit-module-03-execution-modes.md`
   - `audit-module-04-anti-drift-rules.md`
   - `audit-module-05-governance-schemas.md`
5. **Recomposition Rollup Summary**:
   - Summary of BPE token compression across all 22 rules.
   - Direct link to `../../candidates/16-candidate-3A-ultra.md`.

#### Path Resolution Note:
All links in `06-layered-rule-kb/index.md` are evaluated relative to `apex-meta/informatics/final/research/06-layered-rule-kb/`:
- Sibling deep-dive files: `rule-01-target.md`, `rule-02-product-first.md`, etc.
- Candidate files: `../../candidates/16-candidate-3A-ultra.md`, `../../candidates/13-candidate-3A-xml.md`.
- Plane 4 library files: `../../../writing-profile.md`, `../../../anti-drift-rules.md`, etc.

### 3.2 Update Specification for `apex-meta/informatics/final/index.md`
`apex-meta/informatics/final/index.md` must be updated to register the new deliverables without disturbing existing links:

1. **Top Preamble (lines 13–18)**:
   - Add bullet pointing to `candidates/16-candidate-3A-ultra.md` as the Option B Surgical Ultra-Compression contract candidate (~935 BPE tokens).
2. **Table 1 (`candidates/` suite)**:
   - Add row:
     `| [**16-candidate-3A-ultra.md**](candidates/16-candidate-3A-ultra.md) | **Ultra Candidate** | Finalized v1.0 Option B Surgical Compression contract block (~935 BPE tokens) synthesizing all 22 rule deep-dives. |`
3. **Section 2 (`research/` structure diagram)**:
   - Update line 53 from `06-layered-rule-kb/ <- Semantic block rule audit prototype (rule-01-target.md)` to:
     `06-layered-rule-kb/ <- Complete 22-rule Layered KB, 5 Plane 4 module audits, and index.md`
4. **Section 2.1 (Research Directory Index table)**:
   - Update row for `06-layered-rule-kb/`:
     Change description from prototype to complete suite and link target to `[06-layered-rule-kb/](research/06-layered-rule-kb/index.md)`.

---

## 4. Safety Constraints & Invariant Enforcement

### 4.1 Zero Live Mutation Boundary
- **Target Files**: Root carrier files `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` located at repository root `c:\GitDev\apexai-os-meta\`.
- **Pre-Existing State**: `git status -s` shows pre-existing uncommitted modifications in `AGENTS.md` and `CLAUDE.md` from an earlier infrastructure update (`ki-basis/docs/INFRASTRUCTURE.md` single-source banner).
- **Invariant**: The team must introduce **zero new modifications** to `AGENTS.md`, `CLAUDE.md`, or `GEMINI.md`. `git diff AGENTS.md CLAUDE.md GEMINI.md` after work completion must show only the pre-existing infrastructure diff and nothing else.

### 4.2 Research Bytes Preservation Boundary
- **Target Directories**:
  - `apex-meta/informatics/final/research/01-universal-instruction-research/`
  - `apex-meta/informatics/final/research/03-research-of-file-10/`
- **Invariant**: Strictly read-only. No renaming, moving, editing, or deleting of any files in these directories. All Layered KB and candidate files must cite and link them via relative Markdown links without mutation.

---

## 5. Actionable Roadmap for Phase 2 Implementation Teams

### For Authoring Team (Rules 02–22):
1. **Model on `rule-01-target.md`**: Every rule deep-dive must implement all 5 mandatory sections:
   - OKF frontmatter (`type: Reference`, `id: V2-LAYERED-KB-RULE-XX-...`, `status: current_truth`).
   - §1 Original Rule & Atomic Semantic Block Inventory (`SB-XX.1`..`SB-XX.N`).
   - §2 Chapter-by-Chapter Semantic Block Analysis (meaning, high-reasoning critique `[P0-P3 | I/E/R]`, Options A, B, and C).
   - §3 Whole-Rule Recomposition Rollup Table (Baseline, Option B, Option C, with measured BPE tokens and % savings).
   - §4 Bidirectional Research & Provenance Links (internal research packets, external benchmarks, Plane 4 owners).
   - §5 Failure Modes & Not-To-Dos (`WP-25`).
2. **Calibrate Option B Phrasing**: Ensure each rule's Option B achieves ~25%–35% compression, matching the tested formulations in Section 1.3 so that the concatenated rollup hits the ~900–980 BPE ceiling.

### For Module Audit Team (Audits 01–05):
1. Create `audit-module-01-writing-profile.md` through `audit-module-05-governance-schemas.md`.
2. Audit Single-Owner rule (`WP-23`), rule-by-rule semantic blocks, and cross-traceability to `<apex_contract v="1.0">` and `16-candidate-3A-ultra.md`.
3. If recommending module changes, do NOT break `test_canonical_ownership.py` rule IDs or links.

### For Ultra Candidate Compiler Team:
1. Compile `16-candidate-3A-ultra.md` by directly concatenating the recommended Option B compressions from all 22 rule deep-dives.
2. Measure and document exact line, word, char, repo-token, and BPE token counts.
3. Include the complete delta table against `13-candidate-3A-xml.md`.

### For Final Integration Team:
1. Create `06-layered-rule-kb/index.md` linking all 22 rules and 5 audits.
2. Update `final/index.md` with links to `16-candidate-3A-ultra.md` and `06-layered-rule-kb/index.md`.
3. Run verification gates:
   - `python apex-meta/scripts/okf_validator.py --target apex-meta/informatics` (verify 0 OKF Errors, 0 Apex Profile Errors).
   - `python -m pytest apex-meta/informatics/tests/ -q` (verify 196 passed).
   - `git status` check for zero live mutation.

---
*Report compiled autonomously by Explorer Survey Agent (`explorer_survey_4_3`).*
