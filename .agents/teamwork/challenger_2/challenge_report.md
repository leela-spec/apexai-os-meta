# Empirical Challenge Report: Architecture & Ecosystem Stress-Testing

**Agent**: Challenger 2 (`challenger_2`) — Empirical Adversarial Architecture & Ecosystem Stress-Tester  
**Authoritative Scope**: Requirements R1–R4 of `ORIGINAL_REQUEST.md` (section `## 2026-10-21T16:45:38Z`) and `DISPATCH.md`  
**Target Scope**: `FinalizationDossier/` (`00`–`06`, `07`, `index.md`), `ResearchOfFile10/` (`RESULTS-01`–`RESULTS-11`), `13-candidate-3A-xml.md`, `14-candidate-3B-hybrid.md`, `03-BLUEPRINT-agents.md`, `01-decision-register.md`, and Plane 4 library suite  
**Date**: 2026-10-21  

---

## Challenge Summary

**Overall Risk Assessment**: **MEDIUM-HIGH**

While the foundational two-layer architecture (`DEC-22`) and empirical wording upgrades (`DEC-24`) are structurally robust and verified by 196 passing tests and 0 OKF/Profile errors, adversarial stress-testing reveals **three critical vulnerabilities** and **one research dilution** in the `v1.0` candidate specifications that must be addressed prior to live carrier installation into root `AGENTS.md`:

1. **`DEC-21` Dual-Carrier Context Bloat & Flawed Option C Mitigation (HIGH RISK)**: Harnesses that inject multiple instruction files (observed directly in this session where Antigravity injects both `AGENTS.md` and `GEMINI.md` as separate `<RULE>` blocks) suffer verbatim double-loading of the 1,556 repo / 1,286 BPE token contract (~3,112 repo / 2,572 BPE tokens). Furthermore, the proposed **Option C (Carrier Role Hierarchy)** mitigation would cause **total governance loss** in Claude Code CLI and Gemini CLI under default settings.
2. **`DEC-23` Multi-Block Editing Escalation Vacuum (MEDIUM-HIGH RISK)**: Dropping all 5 `deepen_when` attributes saved 99 tokens, but created an operational vacuum: agents reading the self-contained inline summary in `<editing>` have no trigger to open `execution-modes.md` for multi-block replacement protocols or AST `patch_intent.v1`.
3. **Candidate 3B Syntax Fragility vs Marginal Token Economy (MEDIUM RISK)**: Candidate 3B saves only **36 BPE tokens (2.8%)** over Candidate 3A. Because both 3A and 3B span exactly 2 prompt cache blocks (1,024–2,048 tokens), 3B saves **zero cache chunks** and yields an active cost delta of only 3.6 cached tokens ($0.0000045) on Turn 2+. In exchange, 3B introduces severe pipe-escaping vulnerability (`\|`) and collapses completely under standard 80-column word-wrapping (exploding 27 cells into 45 corrupted cells).
4. **`ResearchOfFile10` RP-08 Warning Dilution (MEDIUM RISK)**: The dossier adopted RP-08's count correction and token reduction, but diluted RP-08's explicit core warning: that nontrivial edits require a named second-threshold cue to prevent costly under-reads.

---

## Challenges

### [High Risk] Challenge 1: Multi-Carrier Double-Loading in Antigravity & Flawed Option C Mitigation

- **Assumption Challenged**:
  That maintaining byte-identical `<apex_contract v="1.0">` blocks across `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` (`DEC-21`) is an unproblematic sync strategy, and that Option C ("Carrier Role Hierarchy: `AGENTS.md` master + specialized stubs") is a viable mitigation.
- **Empirical Observation & Attack Scenario**:
  1. *Direct Harness Injection Observation*: Direct inspection of this active agent session's system context proves that Google Antigravity injects **both** files simultaneously:
     ```xml
     <RULE[c:\GitDev\apexai-os-meta\AGENTS.md]> ... </RULE>
     <RULE[c:\GitDev\apexai-os-meta\GEMINI.md]> ... </RULE>
     ```
  2. *Duplicate Context Penalty*: Installing identical 1,556 repo / 1,286 BPE token `<apex_contract>` blocks into both files forces Antigravity to load **2,572 BPE tokens of contract instructions** on every single turn, wasting 1,286 BPE tokens of active window space, increasing per-turn costs, and directly violating `WP-23` (Single-Owner Instruction Reuse).
  3. *Adversarial Breakdown of Option C*:
     In `07-teamwork-independent-validation.md` §2.3, Option C proposed: *"AGENTS.md is master; GEMINI.md and CLAUDE.md carry Layer 2 facts + pointer unless deployed in CLI-only mode."*
     This mitigation is **fatally flawed for standalone CLI environments**:
     - **Claude Code CLI Default**: As proven by `RP-10` (`RESULTS-10-surface-layering.md` lines 21 & 42), Claude Code CLI in its default configuration **ignores `AGENTS.md` when `CLAUDE.md` exists**! If `CLAUDE.md` is a stub with a pointer, Claude Code CLI will execute with **zero contract rules in context**.
     - **Gemini CLI Default**: Gemini CLI defaults to loading *only* `GEMINI.md` unless explicitly overridden in `context.fileName`. A stub leaves Gemini CLI agents unguided.
     - **Preprocessor Absence**: IDE extensions and agent injectors (Antigravity, Cursor, Windsurf, VS Code Copilot) do not parse CLI `@AGENTS.md` import preprocessors; they inject raw file strings.
- **Blast Radius**: Double-loading costs 1,286 wasted tokens per turn in Antigravity. Option C, if naively installed, breaks governance across standard CLI tools.
- **Mitigation**:
  1. Explicitly ratify Option A (`DEC-21` byte-identical sync via `pytest`) as the **only safe runtime compatibility baseline today** across heterogeneous IDE and CLI tools, but attach an explicit `WARN` regarding multi-carrier harnesses.
  2. For Antigravity users, document the required harness configuration (`context.fileName: AGENTS.md`) to suppress duplicate loading of `GEMINI.md`.
  3. For long-term multi-repo distribution, adopt an explicit build-time single-source compiler (DITA projection model) rather than runtime pointer stubs.

---

### [Medium-High Risk] Challenge 2: Escalation Threshold Vacuum for Multi-Block Editing in `execution-modes.md`

- **Assumption Challenged**:
  That dropping all 5 `deepen_when` attributes from `v0.5` is an uncompromised efficiency gain (-99 tokens), and that the generic terminal guard (`<pointers>Paths are just-in-time pointers relative to base_ref. Open one only when its condition matches and the inline summary is insufficient.</pointers>`) provides sufficient operational guidance.
- **Attack Scenario**:
  1. In `v0.5`, `<editing>` carried `deepen_when="the edit spans multiple blocks or goes to a deterministic executor"`.
  2. In `v1.0-3A` (and `3B`), `deepen_when` was removed. The inline rule is:
     `<editing when="changing, moving or deleting a file that already exists" ref="execution-modes.md">`
     `Replace only the exact lines that must change, copied character-for-character from the file you just read. One change per edit. Move or copy with git mv or cp, never by rewriting contents.`
     `</editing>`
  3. When an agent is tasked with modifying multiple functions across a file or emitting patches for a deterministic runner, the agent reads the inline rule. Because the inline rule appears completely self-contained and clear (*"Replace only the exact lines... One change per edit"*), the agent has **no indication** that `execution-modes.md` §4 contains:
     - Mode A: Block Replacement Protocol (`<file>/<old>/<new>`) with 8 strict requirements (Disambiguating Context, Exact Whitespace, No Line Numbers, etc.).
     - Mode B: Structured AST Patch Intent (`patch_intent.v1`).
  4. The agent concludes the inline summary is "sufficient", never opens `execution-modes.md`, and emits non-conforming ad-hoc edits.
- **Blast Radius**: Automated patch tools and deterministic executors fail due to non-conforming patch output, and complex multi-block edits suffer regression risk.
- **Mitigation**:
  Fold the second-threshold escalation cue directly into the `<editing>` operative text:
  ```xml
  <editing when="changing, moving or deleting a file that already exists" ref="execution-modes.md">
  Replace only the exact lines that must change, copied character-for-character from the file you just read. One change per edit. Move or copy with git mv or cp, never by rewriting contents. For multi-block edits, AST patches, or deterministic executors, open ref for exact protocols.
  </editing>
  ```
  This addition costs only **14 BPE tokens**, completely eliminates the escalation vacuum, and preserves the full benefit of dropping unparsed XML attributes.

---

### [Medium Risk] Challenge 3: Candidate 3B Syntax Fragility vs Marginal Token Economy

- **Assumption Challenged**:
  That Candidate 3B (Hybrid XML + Markdown Table) is a co-equal candidate to Candidate 3A (Pure XML) whose token savings justify table pipe-escaping complexity.
- **Empirical Stress Test Results**:
  1. *Token Arithmetic*:
     - Candidate 3A (`<apex_contract>` block): **1,286 BPE tokens** (6,226 chars, 851 words).
     - Candidate 3B (`<apex_contract>` block): **1,250 BPE tokens** (6,044 chars, 876 words).
     - **Delta (3A vs 3B): exactly 36 BPE tokens (2.80%)**. The 190-token saving projected in `RP-06` was an unverified extrapolation from a 3-rule test that failed to materialize on the complete block.
  2. *Prompt Caching Dynamics*:
     - Assembled Blueprint with 3A: **1,833 BPE tokens**.
     - Assembled Blueprint with 3B: **1,797 BPE tokens**.
     - Both configurations span **exactly 2 prompt cache blocks (1,024–2,048 tokens)** under standard 1,024-token prefix chunking (OpenAI / Anthropic). Candidate 3B saves **zero cache chunks**.
     - On Turn 2+ with a 90% prompt cache read discount, 36 BPE tokens equals **3.6 active billing tokens ($0.0000045 per query)**.
  3. *Table Pipe-Escaping Corruption*:
     In Candidate 3B line 61, tagging syntax requires pipe escaping: `[P0-P3 \| I/E/R]`.
     Using Python's standard CommonMark parser (`markdown-it-py`), we tested table cell splitting:
     - When unescaped (`[P0-P3 | I/E/R]`), even inside backticks `` `[P0-P3 | I/E/R]` ``, the parser splits the cell into two, shifts content, and **completely drops Column 3 (`Ref`)**.
  4. *Word-Wrapping Catastrophe*:
     We tested automated code/markdown formatters (e.g. Prettier, IDE line wrapping at 80 columns) on Candidate 3B line 61 (a 423-character single-line cell):
     - Line wrapping destroyed the markdown table structure, ballooning parsed table cells from **27 cells to 45 corrupted cells**.
     - In contrast, aggressive 60-character word-wrapping on Candidate 3A (XML) preserved **100% of XML tags and attributes without error**.
- **Blast Radius**: Broken table formatting, dropped file references, and syntax corruption under automated linting or formatting tools.
- **Mitigation**:
  Formally ratify **Candidate 3A (Pure XML)** as the sole blueprint default for future system integration (`DEC-17`). Demote Candidate 3B to an experimental benchmark arm in `04-empirical-test-protocol.md`.

---

### [Medium Risk] Challenge 4: ResearchOfFile10 Dilution: RP-08's Two-Threshold Warning Was Omitted

- **Assumption Challenged**:
  That the Finalization Dossier fully captured all high-leverage empirical findings from `ResearchOfFile10`.
- **Empirical Comparison & Omission Finding**:
  In `RESULTS-08-deepen-when-mechanics.md` (lines 46 & 61–63), RP-08 explicitly stated:
  > *"For schema authoring and nontrivial edits, there may be a genuine two-threshold requirement: the reduced rule applies to many tasks, while the precise schema or multi-block patch protocol is needed only rarely. Explicitly naming that second threshold could spare thousands of tokens on routine tasks or prevent a costly under-read... Suggested shortest behavior-preserving formulation: `Read ref only if exact frontmatter/schema detail is needed.`"*
  
  The Finalization Dossier (`FinalizationDossier/00` and `01-decision-register.md`) adopted RP-08's count correction (5 attributes instead of 6 or 9) and claimed the 99-token saving, but **completely omitted RP-08's behavior-preserving second threshold** from `<editing>` and `<schemas>`.
- **Blast Radius**: Omitting the second threshold created the exact escalation vacuum identified in Challenge 2.
- **Mitigation**:
  Incorporate RP-08's explicit second threshold into the operative text of `<editing>` and `<schemas>` as designed in Challenge 2.

---

## Stress Test Results

| Scenario / Test Case | Tool / Method | Expected Behavior | Actual Empirical Result | Status |
|---|---|---|---|:---:|
| **Antigravity Multi-Carrier Injection** | Direct Context Inspection | Single contract in context | Both `AGENTS.md` and `GEMINI.md` injected as separate `<RULE>` blocks (~3,112 repo tokens total) | **CONFIRMED VULNERABILITY** |
| **Candidate 3A vs 3B BPE Tokenization** | Python `tiktoken` (`cl100k_base`) | Delta >= 100 tokens | Candidate 3A = 1,286 BPE; Candidate 3B = 1,250 BPE. Delta is only 36 BPE tokens (2.80%) | **CONFIRMED MEASUREMENT** |
| **Prefix Cache Boundary Alignment** | Python `tiktoken` (1,024-block multiples) | 3B saves 1 cache block | 3A = 1,833 BPE (1.79 blocks); 3B = 1,797 BPE (1.75 blocks). Both require ceil = 2 cache blocks | **CONFIRMED NO CACHE WIN** |
| **Markdown Table Pipe Escaping** | `markdown-it-py` Table Parser | Unescaped pipe inside code span preserved | Unescaped pipe splits cell and truncates Column 3 (`Ref`) | **CONFIRMED SYNTAX FRAGILITY** |
| **80-Column Line Wrapping on 3B** | `markdown-it-py` + `textwrap` | Markdown table remains valid | Table corrupted: cells explode from 27 to 45 broken cells | **CONFIRMED COLLAPSE** |
| **60-Column Line Wrapping on 3A** | `xml.etree.ElementTree` + `textwrap` | XML parses identically | 22/22 tags and attributes preserved 100% intact | **CONFIRMED XML ROBUSTNESS** |
| **Canonical Ownership & Collisions** | `pytest apex-meta/informatics/tests/` | 100% test pass | 196 passed, 97 subtests passed in 0.40s | **PASS** |
| **Deterministic Schema Conformance** | `python okf_validator.py` | 0 errors | 0 OKF Errors, 0 Profile Errors, 12 pre-existing style advisories | **PASS** |
| **Live Root Carrier Boundary** | `git diff AGENTS.md CLAUDE.md GEMINI.md` | Zero modifications introduced | Zero new changes introduced by audit | **PASS** |

---

## Unchallenged Areas

- **Two-Layer Architecture (`DEC-22`)**: The separation of Layer 1 (Universal Invariants) and Layer 2 (Repo-Specific Context) is empirically sound, cleanly decouples portable rules from local infrastructure facts, and eliminates 140 tokens of duplication in the blueprint.
- **Empirical Wording Upgrades (`DEC-24`)**: The integration of SpecBench requirement-based validation (`RP-05`), FixedBench no-op permission (`RP-07`), Insights Discovery Cool Blue register (`RP-04`), and pre-action blocker requirements in `<new_machinery>` are fully grounded and verified across both contract candidates and the Plane 4 library.
- **Deterministic Conformance Suite**: The 196 unit tests and OKF frontmatter validation are deterministic, fully passing, and maintain high standards.
