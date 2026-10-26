# Handoff Report: Survey Task 3 — 3A-Ultra Compression Strategy, Conformance Gates & Index Architecture

**Agent**: `explorer_survey_4_3`  
**Working Directory**: `c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_survey_4_3`  
**Date**: 2026-10-22  
**Type**: Hard Handoff (Survey Complete)  

---

## 1. Observation

1. **`13-candidate-3A-xml.md` Physical & Token Metrics**:
   - Location: `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\candidates\13-candidate-3A-xml.md`.
   - Lines 33–97 contain the canonical `<apex_contract v="1.0" base_ref="apex-meta/informatics/">` XML block.
   - Live measurement via Python 3.12 and `tiktoken 0.14.0` (`cl100k_base`):
     - Block characters: `6,529`
     - Block lines: `65`
     - Block words: `899`
     - Repo tokens (`chars // 4`): `1,632`
     - BPE tokens (`cl100k_base`): `1,350`
     - Sum of 22 individual semantic tag contents: `1,324` BPE tokens (root tags and spacing: `26` BPE tokens).
2. **`rule-01-target.md` Prototype Structure & Option B Precedent**:
   - Location: `c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb\rule-01-target.md`.
   - Baseline `<target>` text: 69 BPE tokens (`cl100k_base`), 375 chars, 50 words.
   - Recommended Option B text (line 99):
     `"<target>Verify the delivered result against each stated requirement before claiming completion. Self-authored tests or checklists are evidence, never replacement criteria; stated requirements outrank inferred ones. If evidence shows no change is needed, say so and stop.</target>"`
   - Option B measured size: `50` BPE tokens (`cl100k_base`), 279 chars, 36 words.
   - Net token reduction for `<target>`: `−19 BPE tokens` (`−27.5%`) with zero semantic loss.
3. **`okf_validator.py` Diagnostics & Sub-Bundle Isolation**:
   - Location: `c:\GitDev\apexai-os-meta\apex-meta\scripts\okf_validator.py`.
   - Execution: `python apex-meta/scripts/okf_validator.py --target apex-meta/informatics` exited with return code `0`.
   - Output summary: `OKF Errors: 0 | Apex Profile Errors: 0 | Advisories: 12`.
   - Invariant code observation (lines 206–208):
     ```python
     if current_dir != target_path and (current_dir / "index.md").exists():
         dirs.clear()  # Do not recurse into separate sub-bundle
         continue
     ```
     Directories containing their own `index.md` are treated as separate sub-bundles and pruned during parent bundle validation.
4. **Pytest Test Suite Status**:
   - Command: `python -m pytest apex-meta/informatics/tests/ -q`.
   - Result: `196 passed, 98 subtests passed in 0.50s`.
   - Covered suites:
     - `test_canonical_ownership.py` (11 tests): checks 7 `GOVERNED_FILES` in `apex-meta/informatics/` for unique rule IDs, filename prefix consistency, canonical pointer resolution, ban on `file://` absolute links, link resolution, and no re-embedded patch schemas.
     - `test_informatics_e2e.py` (88 tests): Tier 1–4 feature tests and live bundle compliance.
     - `test_tier5_adversarial.py` (88 tests): context isolation, lore traceability, task adapters, ranking, frontmatter, compactness.
     - `stress_test_m2_challenger.py` (9 tests): router ceilings, tag validation, frontmatter parsing, formula prohibition.
5. **Git Status & Carrier Invariants**:
   - Command: `git status -s AGENTS.md CLAUDE.md GEMINI.md`.
   - Result:
     ```text
      M AGENTS.md
      M CLAUDE.md
     ```
   - Diff inspection: pre-existing modification adding `Single source of truth (live state): ki-basis/docs/INFRASTRUCTURE.md`.
   - Zero new changes were introduced.

---

## 2. Logic Chain

1. **Premise 1**: The user request and dispatch mandate compiling `16-candidate-3A-ultra.md` at ~900–980 BPE tokens (target ~950 BPE, a ~30% reduction from 1,350 BPE in `13-candidate-3A-xml.md`).
2. **Step 2 (from Obs 1 & 2)**: Concatenating Option B surgical compressions across all 22 rules (as established by the prototype `<target>` in `rule-01-target.md` saving ~27.5%) provides the mechanism to achieve a 30% reduction.
3. **Step 3 (Rule-by-rule quantification)**: Testing tightened Option B formulations for all 22 rules (detailed in Section 1.3 of `survey_report.md`) produces an aggregate tag BPE of 909 tokens. Adding the root tag (`<apex_contract v="1.0-ultra" base_ref="apex-meta/informatics/">`) and formatting brings the total block to **935 BPE tokens**, perfectly centered in the target ~900–980 BPE range.
4. **Step 4 (from Obs 3)**: `okf_validator.py` enforces flat YAML frontmatter, unique IDs, and link integrity from `index.md`. Because line 206 of `okf_validator.py` isolates any subdirectory containing an `index.md`, creating `06-layered-rule-kb/index.md` establishes a clean sub-bundle. All links within `06-layered-rule-kb/index.md` must resolve relative to `06-layered-rule-kb/`.
5. **Step 5 (from Obs 4)**: The 196 pytest tests strictly govern the 7 core Plane 4 files in `apex-meta/informatics/`. Authoring files under `final/candidates/` and `final/research/06-layered-rule-kb/` will not collide with existing test assertions as long as `final/index.md` preserves its valid links.
6. **Step 6 (from Obs 5)**: Pre-existing changes to root carrier files (`AGENTS.md`, `CLAUDE.md`) must be untouched; zero live carrier mutations will be generated during this iteration.

---

## 3. Caveats

1. **Tokenizer Model**: All BPE token counts were verified using OpenAI's `tiktoken` with `cl100k_base` vocabulary, which serves as the repository's standard approximation for frontier LLMs (GPT-4o, Claude 3.5 Sonnet approximations). Claude's proprietary tokenizer (`messages.count_tokens`) may differ by ±5–8%, but `cl100k_base` is the explicit benchmark established in `ResearchOfFile10` and `FinalizationDossier/07-teamwork-independent-validation.md`.
2. **Tag Attribute Phrasing**: In `13-candidate-3A-xml.md`, the 9 conditional gates carry descriptive `when="..."` attributes (e.g., `when="changing, moving or deleting a file that already exists"`). In our Option B ultra-compression formulation, these attributes were tightened (e.g., `when="editing, moving or deleting existing files"`) to save ~70 BPE tokens while preserving full semantic triggering clarity. If the orchestrator mandates retaining verbatim 3A `when="..."` strings, the inner rule bodies must be compressed by an additional 3–4 words per rule to hit ~950 BPE.
3. **Plane 4 Module Write Restrictions**: In Task 2, module audits will evaluate Plane 4 modules (`writing-profile.md`, `file-architecture.md`, etc.). If edits are proposed, they must be validated against `test_canonical_ownership.py` to prevent duplicate rule IDs or broken cross-references.

---

## 4. Conclusion

1. **Feasibility of `16-candidate-3A-ultra.md`**: Fully confirmed. A complete, verified draft measuring **935 BPE tokens** (65 lines, 4,498 chars, 585 words, 1,124 div4 tokens) has been formulated and recorded in `survey_report.md`, achieving a 30.7% compression over `13-candidate-3A-xml.md` with zero loss of non-default invariants.
2. **Conformance Toolchain**: `okf_validator.py` and the 196 pytest tests pass cleanly and provide clear, deterministic boundaries for new artifacts. Sub-bundle isolation protects parent validation runs.
3. **Index Architecture**: Clean layout specifications for `06-layered-rule-kb/index.md` and updates to `final/index.md` are defined with full relative path mapping.
4. **Safety Boundaries**: Root carriers and research directories are identified and protected under zero-mutation rules.

---

## 5. Verification Method

1. **Verify Token Metrics & Feasibility**:
   Run the following command to measure the exact BPE tokens of the 3A-Ultra candidate block:
   ```powershell
   python -c "
   import tiktoken
   from pathlib import Path
   enc = tiktoken.get_encoding('cl100k_base')
   report = Path('c:/GitDev/apexai-os-meta/.agents/teamwork/explorer_survey_4_3/survey_report.md').read_text(encoding='utf-8')
   import re
   m = re.search(r'```xml\s*(<apex_contract v=\"1.0-ultra\".*?</apex_contract>)\s*```', report, re.DOTALL)
   if m:
       print('Measured BPE:', len(enc.encode(m.group(1))))
   "
   ```
   *Expected output*: `Measured BPE: 935` (well within the target ~900–980 BPE ceiling).

2. **Verify OKF Validator Gate**:
   ```powershell
   python apex-meta/scripts/okf_validator.py --target apex-meta/informatics
   ```
   *Expected output*: Exits `0` with `OKF Errors: 0 | Apex Profile Errors: 0`.

3. **Verify Pytest Suite**:
   ```powershell
   python -m pytest apex-meta/informatics/tests/ -q
   ```
   *Expected output*: `196 passed, 98 subtests passed in ~0.5s`.

4. **Verify Zero Mutation on Root Carriers**:
   ```powershell
   git status -s AGENTS.md CLAUDE.md GEMINI.md
   ```
   *Expected output*: Shows only pre-existing modifications, no new changes introduced.

5. **Invalidation Conditions**:
   - The survey findings are invalidated if `tiktoken` counts for the Option B candidate exceed 980 BPE tokens.
   - The findings are invalidated if any proposed change to `final/index.md` causes `test_canonical_ownership.py` or `okf_validator.py` to raise errors.
