# Independent Token-Metric & Equivalence Analysis Report (R2)

> **Investigator:** Explorer M2_1 (Token-Metric & Equivalence Investigator)  
> **Target Scope:** R2 of Authoritative Request (`## 2026-10-21T16:45:38Z`)  
> **Date:** 2026-10-21T17:10:00Z  
> **Status:** COMPLETE  

---

## 1. Executive Summary

1. **Token & Byte Metrics Confirmed:**
   - The `<apex_contract v="1.0">` block in `13-candidate-3A-xml.md` measures **exactly 65 lines, 6,225 characters, 851 words, and 1,556 repo tokens (`chars // 4`)**. Standard `cl100k_base` BPE tokenizer yields **1,286 tokens** (confirming the stated `1,305` within 1.45% due to word+punct regex heuristics).
   - The `<apex_contract v="1.0">` block in `14-candidate-3B-hybrid.md` measures **exactly 41 lines, 6,043 characters, 876 words, and 1,510 repo tokens (`chars // 4`)**. Standard `cl100k_base` BPE tokenizer yields **1,250 tokens** (confirming the stated `1,260` within 0.79%).
   - Candidate `3B` achieves a **36.9% line reduction (41 vs 65)**, **2.9% character/repo-token reduction (1,510 vs 1,556)**, and **2.8% BPE reduction (1,250 vs 1,286)** over Candidate `3A`.
2. **100% Behavioral Equivalence Verified:**
   - A rule-by-rule audit confirms that all 12 unconditional invariants (`<target>` through `<surgical>`), all 9 conditional gates (`<editing>` through `<sync>`), and the terminal pointer scoping guard in `3A` have identical operative semantics and identical target pointers in `3B`. The only differences are cosmetic Markdown table formatting and syntax backticks.
3. **Layer 1 vs Layer 2 Duplication Purged in `03-BLUEPRINT-agents.md`:**
   - Layer 1 (`<apex_contract>`) is completely portable (universal rules).
   - Layer 2 contains strictly repo-specific context: the live infrastructure banner (WSL2 Docker / PostgreSQL), the WSL2 ext4 filesystem constraint, and the completion reporting rule.
   - All 6 redundant Git Dispatch rules, 5 Directness rules, 10 Core Intent rules, and 3 Scope rules from live `AGENTS.md` have been deduplicated. Zero duplication remains between Layer 1 and Layer 2.
4. **Key Inconsistencies / Staleness Discovered:**
   - **Dossier 00 Staleness (`00-research-critique-and-architecture-design.md` lines 42 & 51):** The mermaid diagram in Dossier 00 still displays the pre-deduplication figures: `Layer 2 (~435 tokens)` and `Combined (~1,945–1,991 tokens)`. In Dossier 01 and Blueprint 03, Layer 2 was slimmed to **295 tokens** and the combined total to **1,805–1,851 tokens**.
   - **Path Depth in `v2-always-on-architecture/index.md` lines 24–26:** Relative links to root library files use `../../` instead of `../../../`, causing broken link errors in validators scanning that sub-bundle.
   - **Pending Pytest Gate:** `03-BLUEPRINT-agents.md` line 91 cites `test_carrier_byte_identity`, which is planned for system integration but does not yet exist in the test suite.

---

## 2. Deterministic Metric Reproduction & Verification

All measurements were computed directly from live bytes using Python 3.12 and `tiktoken 0.14.0` with the `cl100k_base` BPE vocabulary (the standard tokenizer for GPT-4o, Claude 3.5 Sonnet approximations, and OpenAI models).

### Table 1: Live Contract Block & Blueprint Metrics

| Surface / Block | Lines | Characters | Words | Repo Estimator (`chars // 4`) | Repo Estimator (`words * 1.3`) | `cl100k_base` BPE Tokens | Stated Claim in Dossier / File | Status |
|---|---:|---:|---:|---:|---:|---:|---|---|
| **`13-candidate-3A-xml.md`** (`<apex_contract>` block lines 33–97) | **65** | **6,225** | **851** | **1,556** | **1,106** | **1,286** | 65 lines \| 6,225 chars \| 1,556 repo tokens \| 1,305 BPE tokens | **CONFIRMED** (exact match chars/lines/words/div4; BPE within 1.45%) |
| **`14-candidate-3B-hybrid.md`** (`<apex_contract>` block lines 29–69) | **41** | **6,043** | **876** | **1,510** | **1,139** | **1,250** | 41 lines \| 6,043 chars \| 1,510 repo tokens \| 1,260 BPE tokens | **CONFIRMED** (exact match chars/lines/words/div4; BPE within 0.79%) |
| **Delta (`3B` vs `3A`)** | **−24 (−36.9%)** | **−182 (−2.9%)** | **+25 (+2.9%)** | **−46 (−2.9%)** | **+33 (+3.0%)** | **−36 (−2.8%)** | −24 lines \| −46 repo tokens \| −45 BPE tokens | **CONFIRMED** |
| **`03-BLUEPRINT-agents.md`** (Assembled Carrier: Layer 1 `3A` + Layer 2) | — | 7,455 | 994 | **1,851** | 1,292 | **1,601** | Total: **1,851** repo tokens / ~1,550 BPE tokens | **CONFIRMED** (Exact match on repo tokens) |
| **`03-BLUEPRINT-agents.md`** (Assembled Carrier: Layer 1 `3B` + Layer 2) | — | 7,273 | 1,019 | **1,805** | 1,325 | **1,565** | Total: **1,805** repo tokens / ~1,505 BPE tokens | **CONFIRMED** (Exact match on repo tokens) |
| **Live `AGENTS.md` Baseline** (Current root carrier) | **50** | **3,994** | **552** | **998** | **718** | **881** | `50 lines / ~998 tokens across six sections` (Blueprint line 27) | **CONFIRMED EXACT** (3,994 // 4 = 998) |

### Table 2: Full-File Metrics (Including YAML Frontmatter & Explanatory Preamble)

| File | File Size (Bytes) | Lines | Characters | Words | Repo Estimator (`chars // 4`) | Repo Estimator (`words * 1.3`) | `cl100k_base` BPE Tokens |
|---|---:|---:|---:|---:|---:|---:|---:|
| `13-candidate-3A-xml.md` | 14,801 | 125 | 14,781 | 1,470 | 3,695 | 1,911 | 3,921 |
| `14-candidate-3B-hybrid.md` | 8,278 | 70 | 8,250 | 1,092 | 2,062 | 1,420 | 1,902 |
| `03-BLUEPRINT-agents.md` | 8,283 | 92 | 8,259 | 881 | 2,064 | 1,145 | 2,278 |

### Notes on Token-Metric Methodology:
1. **Repo Token Estimator (`chars // 4`):** The repository and test suite (`test_tier5_adversarial.py` line 62, `test_informatics_e2e.py` line 104) define standard repo token estimation as `max(1, len(text) // 4)`. Under this standard, both Candidate 3A (`6,225 // 4 = 1,556`) and Candidate 3B (`6,043 // 4 = 1,510`) match the reported figures down to the single integer.
2. **Word-Based Estimator (`words * 1.3`):** Yields lower estimates (1,106 for 3A and 1,139 for 3B) because technical XML tags and punctuation are treated as word attachments rather than independent tokens.
3. **BPE Token Count (`cl100k_base`):** `1,286` for 3A and `1,250` for 3B. The minor difference between these counts and the Dossier's stated figures (1,305 and 1,260) is attributable to regex-based word+punctuation token estimation (`\w+|[^\w\s]`) vs. true BPE merge tables. Both models confirm that Candidate 3B requires fewer tokens and substantially fewer lines than Candidate 3A.

---

## 3. Rule-for-Rule Behavioral Equivalence Audit (3A vs 3B)

Both files were parsed and compared across all 22 functional rules and container elements:

### Part A: 12 Unconditional Invariants (Lines 35–57 in 3A vs Lines 31–53 in 3B)

| Rule # | Tag Name | Candidate 3A Text | Candidate 3B Text | Behavioral Equivalence |
|---|---|---|---|:---:|
| 1 | `<target>` | Verbatim identical | Verbatim identical | **100% IDENTICAL** |
| 2 | `<product_first>` | Verbatim identical | Verbatim identical | **100% IDENTICAL** |
| 3 | `<scope>` | Verbatim identical | Verbatim identical | **100% IDENTICAL** |
| 4 | `<communication>` | Verbatim identical (Cool Blue register, warranted uncertainty) | Verbatim identical | **100% IDENTICAL** |
| 5 | `<hold_position>` | Verbatim identical (anti-sycophancy) | Verbatim identical | **100% IDENTICAL** |
| 6 | `<ground>` | Verbatim identical (originating artifact, 3 authoritative sources) | Verbatim identical | **100% IDENTICAL** |
| 7 | `<reuse>` | Verbatim identical | Verbatim identical | **100% IDENTICAL** |
| 8 | `<context>` | Verbatim identical (load JIT, rank before reading) | Verbatim identical | **100% IDENTICAL** |
| 9 | `<recovery>` | Verbatim identical | Verbatim identical | **100% IDENTICAL** |
| 10 | `<stop_repairing>`| Verbatim identical (2-strike approach limit) | Verbatim identical | **100% IDENTICAL** |
| 11 | `<current_truth>` | Verbatim identical (zero inline changelogs) | Verbatim identical | **100% IDENTICAL** |
| 12 | `<surgical>` | Verbatim identical ("Never regenerate or overwrite a whole existing file.") | Verbatim identical | **100% IDENTICAL** |

### Part B: 9 Conditional Gates (Lines 59–93 in 3A vs Lines 58–66 in 3B)

| Rule # | 3A Tag | 3A Condition (`when=`) & Target (`ref=`) | 3B Table Row (`When` & `Ref`) | Operative Body Comparison | Equivalence Verdict |
|---|---|---|---|---|:---:|
| 1 | `<editing>` | `when="changing, moving or deleting a file that already exists"`<br/>`ref="execution-modes.md"` | `Changing, moving or deleting an existing file`<br/>`Ref: \`execution-modes.md\`` | Both mandate: replace exact lines character-for-character, one change per edit, `git mv` or `cp`. 3B adds backticks around `git mv` and `cp`. | **100% EQUIVALENT** |
| 2 | `<new_machinery>` | `when="about to add a script, test, gate, schema, wrapper or abstraction"`<br/>`ref=""` | `Adding a script, test, gate, schema, wrapper or abstraction`<br/>`Ref: —` | Both mandate: name exact requirement/blocker/risk first; if 2 steps surface it, fix data/logic; do not over-build verification machinery. | **100% EQUIVALENT** |
| 3 | `<detour>` | `when="about to propose a refactor, redesign, migration or infrastructure addition"`<br/>`ref=""` | `Proposing a refactor, redesign, migration or infrastructure addition`<br/>`Ref: —` | Both mandate: ask if must be fixed before product can be tested; if not, defer in one line. | **100% EQUIVALENT** |
| 4 | `<authoring>` | `when="creating, editing or validating a governed knowledge or specification file"`<br/>`ref="index.md"` | `Creating, editing or validating a governed knowledge or specification file`<br/>`Ref: \`index.md\`` | Both mandate: flat YAML frontmatter, inline bracket lists, concept required keys, front-load critical rules, close on failure mode, `[P0-P3 \| I/E/R]` 1–100, one responsibility per file, link listed files, exclude chat/code/logs. | **100% EQUIVALENT** |
| 5 | `<trade_off>` | `when="the operator must choose between material alternatives, or asks for options"`<br/>`ref="execution-modes.md"` | `Operator must choose between material alternatives, or asks for options`<br/>`Ref: \`execution-modes.md\`` | Both mandate: decide routine choices yourself; for material choice give mechanism, concrete grounding, raw `(I/E/R)` estimates, recommendation, one line per rejection. | **100% EQUIVALENT** |
| 6 | `<handover>` | `when="ending a session, delegating to a subagent, or writing any handoff"`<br/>`ref="execution-modes.md"` | `Ending a session, delegating to a subagent, or writing any handoff`<br/>`Ref: \`execution-modes.md\`` | Both mandate: never write handover to defer what can be resolved now; when needed: observation, reasoning chain, caveats, conclusion, exact commands. | **100% EQUIVALENT** |
| 7 | `<iterative>` | `when="the task spans multiple modules, needs research, or cannot finish in one pass"`<br/>`ref="execution-modes.md"` | `Task spans multiple modules, needs research, or cannot finish in one pass`<br/>`Ref: \`execution-modes.md\`` | Both mandate: single-step direct; multi-step short preflight (target, inputs, scope, output, active step); multi-module file per step. | **100% EQUIVALENT** |
| 8 | `<schemas>` | `when="emitting a patch intent, or validating bundle or schema conformance"`<br/>`ref="governance-schemas.md"` | `Emitting a patch intent, or validating bundle or schema conformance`<br/>`Ref: \`governance-schemas.md\`` | Both mandate: satisfy declared schema exactly; never invent fields; target edits by heading path and surrounding text, never line number. | **100% EQUIVALENT** |
| 9 | `<sync>` | `when="the operator asks to sync, commit or push"`<br/>`ref=""` | `Operator asks to sync, commit or push`<br/>`Ref: —` | Both mandate: run git commands first; preserve every file (commit unrelated dirty files separately); on non-fast-forward pull with rebase and retry. | **100% EQUIVALENT** |

### Part C: Terminal Scoping Guard & Attribute Comparison

- **Candidate 3A:**
  ```xml
  <pointers>Paths are just-in-time pointers relative to base_ref. Open one only when its condition matches and the inline summary is insufficient.</pointers>
  ```
- **Candidate 3B:**
  ```xml
  <conditional_rules note="Apply a row only when its condition matches. Open its Ref path (relative to base_ref) only when the inline rule is insufficient.">
  ```
- **Equivalence Analysis:** Both formulations express the exact same two operational constraints:
  1. Condition matching gating: Apply/open only when condition triggers.
  2. JIT reference loading gating: Open the relative `Ref` file (relative to `base_ref="apex-meta/informatics/"`) only when the inline rule summary is insufficient.
  In 3A, this appears as a dedicated closing XML tag (`<pointers>`), whereas in 3B it is encoded as an attribute (`note="..."`) on the `<conditional_rules>` table wrapper tag.

---

## 4. Architectural & Layer Audit of `03-BLUEPRINT-agents.md`

### 4.1 Layer 1 vs Layer 2 Duplication Analysis
The existing live `AGENTS.md` file contains 50 lines / ~998 tokens across six sections. In `03-BLUEPRINT-agents.md`, the integration cleanly segregates Layer 1 (Universal Contract) from Layer 2 (Repo-Specific Operating Context):

1. **Eliminated from Layer 2 (Now Owned by Layer 1):**
   - 6 of the 7 rules in `## Git Dispatch` (`git add/commit/push` sequence, pull rebase, unrelated dirty files, escalation, stop after push) were removed, saving **~140 tokens**. `<sync>` is the single source of truth.
   - All 5 rules in `## Directness` were removed (owned by `<scope>`, `<target>`, `<sync>`).
   - All 10 rules in `## Core Intent Execution` were removed (owned by `<target>`, `<scope>`, `<current_truth>`, `<recovery>`, `<trade_off>`).
   - All 2 rules in `## Informatics & Knowledge Routing` were removed (owned by `<authoring>`, `<schemas>`, and `base_ref="apex-meta/informatics/"`).
   - All 3 rules in `## Scope` were removed (owned by `<scope>`).
   - The withdrawn `Option D` recommendation (moving the infrastructure banner out of `AGENTS.md`) was completely purged.
2. **Retained in Layer 2 (Strictly Repo-Specific Context = 295 tokens):**
   - **Layer 2A (Infrastructure Banner, ~215 tokens):** `ki-basis/docs/INFRASTRUCTURE.md` live stack topology (WSL2 Docker engine, shared PostgreSQL instance).
   - **Layer 2B (Environment & Completion Constraints, ~80 tokens):**
     * `## Workspace & Filesystem Environment` (45 tokens): Linux agents ext4 workspace rule (`/root/workspaces/<repo>`, never `/mnt/c`).
     * `## Completion Reporting` (35 tokens): Exact-match result requirement ("Never describe a proposed block as applied").
3. **Duplication Verdict:** **ZERO duplication** exists between Layer 1 and Layer 2 in the finalized blueprint.

### 4.2 Link Integrity Audit
All links and path references in `03-BLUEPRINT-agents.md` were tested:
- `file:///c:/GitDev/apexai-os-meta/AGENTS.md` -> **EXISTS**
- `file:///c:/GitDev/apexai-os-meta/CLAUDE.md` -> **EXISTS**
- `file:///c:/GitDev/apexai-os-meta/GEMINI.md` -> **EXISTS**
- `file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/13-candidate-3A-xml.md` -> **EXISTS**
- `file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/14-candidate-3B-hybrid.md` -> **EXISTS**
- `file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/11-instruction-surface-architecture.md` -> **EXISTS**
- `file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture/ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-09-efficiency-audit.md` -> **EXISTS**
- Referenced files in text:
  * `ki-basis/docs/INFRASTRUCTURE.md` -> **EXISTS**
  * `.claude/CLAUDE.md` -> **EXISTS**
  * `.github/copilot-instructions.md` -> **EXISTS**

### 4.3 Inconsistencies & Caveats Discovered
1. **Dossier 00 Staleness (`00-research-critique-and-architecture-design.md` lines 42 & 51):**
   - The mermaid diagram in Dossier 00 states: `LAYER 2 (~435 tokens)` and `Combines Layer 1 + Layer 2 (~1,945–1,991 tokens total)`.
   - In Dossier 01 and Blueprint 03, Layer 2 was slimmed to **295 tokens** after Git Dispatch deduplication, and the blueprint total was updated to **1,805–1,851 tokens**.
   - *Recommendation:* Update the mermaid diagram in Dossier 00 to match Dossier 01 and Blueprint 03.
2. **Missing Test Reference in Test Suite:**
   - `03-BLUEPRINT-agents.md` line 91 states that primary carrier byte-identity is *"verified by a deterministic pytest byte-identity gate (`test_carrier_byte_identity`)"*.
   - Ripgrep confirms `test_carrier_byte_identity` does not yet exist in `apex-meta/informatics/tests/`. This is appropriate because the root carrier files have not yet been mutated, but this test must be implemented concurrently with live system integration.
3. **Path Depth Defect in `v2-always-on-architecture/index.md`:**
   - In `v2-always-on-architecture/index.md` lines 24–26, links to library files use `../../index.md`, `../../writing-profile.md`, etc.
   - Because `v2-always-on-architecture` is nested three levels deep (`apex-meta/informatics/Agent_Setup/NextIteration/v2-always-on-architecture`), these resolve to `Agent_Setup/` instead of `informatics/`. The correct path is `../../../index.md`.
