# Handoff Report: Survey 3 — Codebase Environment, Validator & Conformance Constraints

**Task:** Survey 3 (Explorer)  
**Target:** `c:\GitDev\apexai-os-meta\apex-meta\scripts\okf_validator.py` and `c:\GitDev\apexai-os-meta\apex-meta\informatics`  
**Working Directory:** `c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_survey_3`  
**Author:** Teamwork Explorer  
**Date:** 2026-10-19  

---

## 1. Observation

1. **Validator Script Location & Code**:
   - Path: `c:\GitDev\apexai-os-meta\apex-meta\scripts\okf_validator.py` (332 lines).
   - Entry point: `main()` (lines 304–328) parses `--target` (required) and `--json` (optional).
   - Exit code: `sys.exit(0 if report.passed else 1)` where `report.passed` is `self.okf_errors == 0 and self.apex_profile_errors == 0` (lines 40–43).
   - Severities defined: `OKF_ERROR`, `APEX_PROFILE_ERROR`, `ADVISORY_WARNING` (line 25).

2. **Validator Rules Implemented**:
   - `BUNDLE-EXISTS` (line 145): Target directory existence check.
   - `OKF-ROOT-INDEX-EXISTS` (line 160): Bundle root must contain `index.md`.
   - `OKF-INDEX-FRONTMATTER` (line 172): Root `index.md` must have valid YAML frontmatter between `---` delimiters.
   - `OKF-VERSION-DECLARATION` (line 181): Root `index.md` frontmatter must contain `okf_version: "0.2"`.
   - `APEX-LINK-INTEGRITY` (line 195): Relative links `[text](target.md)` in root `index.md` must resolve to existing files.
   - `APEX-PSEUDO-OKF-DRIFT` (line 232): Files ending in `.okf.md` must begin with `---`.
   - `OKF-FRONTMATTER-PARSE` (line 243): Concept files must have valid YAML frontmatter; error if missing `---` or missing colon `:` on any line.
   - `OKF-FRONTMATTER-MISSING` (line 254): Concept files cannot have empty frontmatter.
   - `OKF-TYPE-REQUIRED` (line 267): Concept files must declare a non-empty `type` string.
   - `APEX-UNIQUE-DURABLE-ID` (line 280): If `id` field is declared in frontmatter, it must be unique across all concept files in the bundle.
   - `STE-SENTENCE-LENGTH` (line 124): Emits `ADVISORY_WARNING` for sentences exceeding 30 words in plain prose (skipping code blocks, tables, headings, list items, quotes, URLs, and formulas).

3. **Parser Implementation Detail**:
   - `parse_frontmatter(content)` (lines 60–83) uses a deterministic line-by-line scanner without PyYAML.
   - Line 67: `if ":" not in line_clean: return None, content, f"Malformed frontmatter on line {line_num}: missing ':'"`.
   - Multiline YAML list items (`- item`) lack colons and cause an immediate `OKF-FRONTMATTER-PARSE` error. Only inline lists (e.g. `tags: [a, b]`) work.

4. **Validator Execution Evidence**:
   - Unit tests: `python -m unittest apex-meta/scripts/tests/test_okf_validator.py` executes 9 tests and outputs `Ran 9 tests in 0.031s — OK`.
   - Live run on `apex-meta/SmallSkills/OKF_Format`: `python apex-meta/scripts/okf_validator.py --target apex-meta/SmallSkills/OKF_Format` exits with code `0` (`OKF Errors: 0 | Apex Profile Errors: 0 | Advisories: 8`).
   - Live run on `apex-meta/informatics`: `python apex-meta/scripts/okf_validator.py --target apex-meta/informatics` exits with code `1`:
     ```
     Summary: OKF Errors: 1 | Apex Profile Errors: 0 | Advisories: 8
     [OKF_ERROR] Agent_Setup/NextIteration/Prompt.md: OKF-FRONTMATTER-PARSE — YAML frontmatter error: No YAML frontmatter header ('---') found at start of file
     ```

5. **Directory Tree & Sub-Bundle Pruning**:
   - Lines 206–208 of `okf_validator.py`:
     ```python
     if current_dir != target_path and (current_dir / "index.md").exists():
         dirs.clear()  # Do not recurse into separate sub-bundle
         continue
     ```
   - `apex-meta/informatics/MMM/` has `MMM/index.md`, so `okf_validator.py` prunes it when scanning `apex-meta/informatics/`.
   - `apex-meta/informatics/Agent_Setup/` does NOT contain `index.md`, so `okf_validator.py` walks into it and into `Agent_Setup/NextIteration/`.
   - File `Agent_Setup/NextIteration/Prompt.md` is an untracked 351-line document without YAML frontmatter, causing the `OKF_ERROR`.

6. **Current Informatics Package State**:
   - Files present at root: `index.md` (20 lines), `standard.md` (160 lines), `migration.md` (30 lines), `log.md` (6 lines).
   - The files reflect **Wave 1** (ratified 2026-09-01).
   - The required modular specification triad (`writing-profile.md`, `file-architecture.md`, `execution-modes.md`), consolidated general router, and Significance & Ranking tags (`[P0–P3 | I<val>/E<val>/R<val>]`) do not yet exist in `apex-meta/informatics/`.

7. **Related Schemas & Exact Patch Runner**:
   - `patch-intent-schema.json`: Located at `.claude/skills/deterministic-markdown-patcher2/references/patch-intent-schema.json` (JSON Schema draft/2020-12, schema version `patch_intent.v1`).
   - `apply_exact_patch.py`: Located at `apex-meta/scripts/apply_exact_patch.py`.

---

## 2. Logic Chain

1. From Observation 1, the script's exit status is strictly conditioned on `okf_errors == 0 and apex_profile_errors == 0`. Therefore, newly authored files in `apex-meta/informatics/` must produce zero OKF errors and zero Apex Profile errors to achieve passing validation.
2. From Observation 2, `okf_validator.py` does not check line lengths or heading depths (`#`, `##`, `###`), nor does it inspect significance tags (`[P0 | I.../E.../R...]`). However, the authoritative user request (`ORIGINAL_REQUEST.md` R1 & R2) requires these as operational orientations for agent ergonomics.
3. From Observation 3, because `parse_frontmatter` rejects any line without a colon `:`, YAML frontmatter in newly authored markdown files must be strictly flat or use inline bracket lists (`tags: [foo, bar]`). Conventional multiline YAML lists will fail validation.
4. From Observation 4 & 5, the failure of `apex-meta/informatics` is due to directory traversal leakage into `Agent_Setup/NextIteration/Prompt.md` caused by the absence of `Agent_Setup/index.md`.
5. From Observation 6, the current files in `apex-meta/informatics/` represent legacy Wave 1 artifacts. The new architecture requested in `ORIGINAL_REQUEST.md` (R1–R5) requires authoring the modular specification suite (`writing-profile.md`, `file-architecture.md`, `execution-modes.md`), updating the root router (`index.md`), and ensuring sub-bundles are cleanly isolated.

---

## 3. Caveats

- **Untracked File Modification**: `Agent_Setup/NextIteration/Prompt.md` is currently untracked in git. As a read-only explorer, I did not modify, delete, or add frontmatter to this file or create `Agent_Setup/index.md`. Resolving the existing failure on `apex-meta/informatics` will require the implementation team to either isolate `Agent_Setup/` (e.g. adding an `index.md`), add frontmatter to `Prompt.md`, or clean untracked artifacts.
- **Scope of okf_validator.py**: The validator checks structural OKF compliance, link validity from root index, and basic STE sentence length. It does not validate markdown syntax details, JSON schema conformance of inline code blocks, or semantic token counts.

---

## 4. Conclusion

1. **Validator Constraints**: `apex-meta/scripts/okf_validator.py` is fully functional and deterministically executable via Python 3 without third-party dependencies.
2. **Authoring Rules for New Files**:
   - `index.md`: Must have `okf_version: "0.2"` in YAML frontmatter and all relative links must point to existing files.
   - All concept files (`writing-profile.md`, `file-architecture.md`, `execution-modes.md`): Must start with `---`, end frontmatter with `---`, declare non-empty `type: <Type>`, maintain unique `id:` if present, and use flat/inline YAML formatting without multiline `- list` syntax.
   - Sentences in prose should aim to stay under 30 words (or use lists/tables/code blocks) to avoid advisory warnings.
3. **Target Directory State**: `apex-meta/informatics/` root files conform to OKF v0.2, but the directory as a whole currently fails validation solely because `Agent_Setup/NextIteration/Prompt.md` lacks frontmatter and `Agent_Setup/` lacks an `index.md`.
4. **Actionable Roadmap for Implementer**:
   - Author the modular suite (`writing-profile.md`, `file-architecture.md`, `execution-modes.md`) with valid frontmatter (`type: ...`, unique `id: ...`).
   - Update `index.md` to link to all newly authored modules.
   - Address `Agent_Setup/` isolation (by placing an `index.md` inside `Agent_Setup/` or addressing `Prompt.md`) so that `python apex-meta/scripts/okf_validator.py --target apex-meta/informatics` completes with `0 OKF Errors` and `0 APEX_PROFILE Errors`.

---

## 5. Verification Method

To independently verify these findings:

1. **Run Unit Tests**:
   ```powershell
   python -m unittest apex-meta/scripts/tests/test_okf_validator.py
   ```
   *Expected:* 9 tests run and pass cleanly (`OK`).

2. **Verify Canonical OKF Bundle Validation**:
   ```powershell
   python apex-meta/scripts/okf_validator.py --target apex-meta/SmallSkills/OKF_Format
   ```
   *Expected:* Returns exit code `0`, `OKF Errors: 0`, `Apex Profile Errors: 0`.

3. **Verify Existing Informatics Directory Validation Failure**:
   ```powershell
   python apex-meta/scripts/okf_validator.py --target apex-meta/informatics
   ```
   *Expected:* Returns exit code `1`, reporting `[OKF_ERROR] Agent_Setup/NextIteration/Prompt.md: OKF-FRONTMATTER-PARSE`.

4. **Verify YAML Frontmatter Parser Colon Constraint**:
   Inspect line 66 of `apex-meta/scripts/okf_validator.py`:
   ```python
   if ":" not in line_clean:
       return None, content, f"Malformed frontmatter on line {line_num}: missing ':'"
   ```
   Confirms that multiline lists without colons on list items trigger parse failures.
