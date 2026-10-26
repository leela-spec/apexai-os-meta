# Survey 3 Report: Codebase Environment, Validator & Conformance Constraints

**Date:** 2026-10-19  
**Investigator:** Teamwork Explorer (Survey 3)  
**Target Domain:** `apex-meta/scripts/okf_validator.py`, `apex-meta/informatics/`, and associated repository schemas/validators  
**Governing Request:** `c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md`

---

## 1. Executive Summary

This investigation analyzed `apex-meta/scripts/okf_validator.py`, the current state and structure of `apex-meta/informatics/`, related schemas, and live execution behavior. The deterministic validator enforces an exact 3-tier diagnostic model (`OKF_ERROR`, `APEX_PROFILE_ERROR`, `ADVISORY_WARNING`) across 11 specific rules. Running the validator requires only Python 3 without external dependencies (no PyYAML).

Crucially, a live run on `apex-meta/informatics/` currently **fails** with `1 OKF_ERROR` (and 8 Advisories) because an untracked file (`Agent_Setup/NextIteration/Prompt.md`) lacks YAML frontmatter. Furthermore, because `Agent_Setup/` does not possess an `index.md`, the validator's directory tree traversal treats all files inside `Agent_Setup/` as concept documents of `apex-meta/informatics`. The validator does **not** enforce line length, markdown heading depth, or significance tags (`[P0 | I.../E.../R...]`). However, its custom lightweight YAML parser imposes strict syntax constraints (e.g. every non-comment line must contain `:`, meaning multiline `- item` lists will throw parse errors).

---

## 2. Detailed Technical Analysis: `apex-meta/scripts/okf_validator.py`

### 2.1 Diagnostic Architecture & Pass/Fail Criteria

`okf_validator.py` classifies every diagnostic finding into one of three severities (defined at lines 23–29):
1. **`OKF_ERROR`**: Violations of upstream Open Knowledge Format (OKF) v0.2 specifications.
2. **`APEX_PROFILE_ERROR`**: Violations of Apex OS repository-specific profile and integrity rules.
3. **`ADVISORY_WARNING`**: Non-blocking technical writing and style recommendations derived from Simplified Technical English (STE).

**Exit Code Contract (lines 40–43, 327):**
```python
@property
def passed(self) -> bool:
    return self.okf_errors == 0 and self.apex_profile_errors == 0
```
- The validator returns exit code `0` if and only if `passed` is `True` (`0 OKF Errors` and `0 Apex Profile Errors`).
- `ADVISORY_WARNING` counts do **not** fail validation and do not block exit code `0`.

---

### 2.2 Complete Rule Catalog & Diagnostic Table

The validator contains exactly 11 checks implemented across 332 lines:

| Severity | Rule ID | Scope / Target | Trigger Condition | Exact Message / Error | Code Line |
|---|---|---|---|---|---|
| **OKF_ERROR** | `BUNDLE-EXISTS` | Target argument | `not Path(target_dir).is_dir()` | `Target bundle directory does not exist: {target_dir}` | L145 |
| **OKF_ERROR** | `OKF-ROOT-INDEX-EXISTS` | `index.md` | `not (target_path / "index.md").is_file()` | `Bundle root index.md does not exist` | L160 |
| **OKF_ERROR** | `OKF-INDEX-FRONTMATTER` | `index.md` | Frontmatter missing `---` boundary or syntax error | `Invalid root index.md frontmatter: {err}` | L172 |
| **OKF_ERROR** | `OKF-VERSION-DECLARATION` | `index.md` | `fm.get("okf_version") != "0.2"` | `Root index.md must declare okf_version: '0.2'` | L181 |
| **APEX_PROFILE_ERROR** | `APEX-LINK-INTEGRITY` | `index.md` | Link `[text](target)` points to relative file that doesn't exist | `Governed index link does not resolve to target file: '{link}'` | L195 |
| **APEX_PROFILE_ERROR** | `APEX-PSEUDO-OKF-DRIFT` | Any `*.okf.md` | File name ends with `.okf.md` but content does not start with `---` | `File uses '.okf.md' extension but lacks real YAML frontmatter` | L232 |
| **OKF_ERROR** | `OKF-FRONTMATTER-PARSE` | Any concept `.md` | Frontmatter missing closing delimiter or missing `:` on key line | `YAML frontmatter error: {err}` | L243 |
| **OKF_ERROR** | `OKF-FRONTMATTER-MISSING` | Any concept `.md` | Frontmatter block empty or `None` | `Concept file must have YAML frontmatter` | L254 |
| **OKF_ERROR** | `OKF-TYPE-REQUIRED` | Any concept `.md` | Frontmatter missing `type` or `type` is empty whitespace | `Frontmatter must contain a non-empty 'type' field` | L267 |
| **APEX_PROFILE_ERROR** | `APEX-UNIQUE-DURABLE-ID` | Any concept `.md` | Frontmatter `id` field value already seen in another concept in bundle | `Duplicate durable ID '{doc_id}' (previously defined in '{durable_ids[doc_id]}')` | L280 |
| **ADVISORY_WARNING** | `STE-SENTENCE-LENGTH` | Body prose | Prose sentence > 30 words (ignoring code, tables, headers, lists, quotes, URLs, math) | `Sentence exceeds recommended limit ({len(words)} words > 25-30 words): '...'` | L124 |

---

### 2.3 YAML Frontmatter Parser Mechanics & Traps

The parser `parse_frontmatter(content)` (lines 45–84) is a custom, zero-dependency parser designed to eliminate PyYAML runtime requirements.

**Parsing Rules:**
1. File must start with `---` (line 50).
2. Must have a closing `---` delimiter (line 53).
3. The content between delimiters is split by line.
4. Blank lines and lines starting with `#` are ignored.
5. **Critical Syntax Rule (Line 66):**
   ```python
   if ":" not in line_clean:
       return None, content, f"Malformed frontmatter on line {line_num}: missing ':'"
   ```
   **Trap Warning for Authors:**
   Standard YAML multiline lists:
   ```yaml
   tags:
     - tag1
     - tag2
   ```
   will **fail** because line `- tag1` lacks a colon (`:`)!
   The parser only supports inline lists:
   ```yaml
   tags: [tag1, tag2]
   ```
   or flat scalar mappings:
   ```yaml
   key: value
   key: "value"
   ```
6. Nested dictionaries: If a line has `generated: { by: gemini, at: 2026-09-01 }`, the key is `generated` and the raw string is `{ by: gemini, at: 2026-09-01 }`. It does not parse into a nested Python dict, but it does not error because line 66 sees `:`.

---

### 2.4 Prose Style Checking (`STE-SENTENCE-LENGTH`)

`check_writing_style(path, body_text)` (lines 98–129) checks prose sentence length:
1. Strips fenced code blocks (`r"```[\s\S]*?```"`).
2. Strips inline code (`` `.*?` ``).
3. Strips markdown tables (any line starting with `|`).
4. Splits text into sentences using `(?<=[.!?])\s+`.
5. Skips sentences starting with `#` (headings), `-` or `*` (lists), or `>` (blockquotes).
6. Skips sentences containing `http` (URLs) or `$` (math/variables).
7. If the word count of remaining prose exceeds 30 words, emits an `ADVISORY_WARNING`.

**What is NOT checked by the validator:**
- **No Line Length Check:** There is no 80-character, 100-character, or 120-character line length limit.
- **No Heading Depth Check:** Nesting depth (`#`, `##`, `###`, `####`, etc.) is neither checked nor restricted.
- **No Significance Tag Check:** Tags such as `[P0 | I95/E95/R10]` are not validated by `okf_validator.py`.

---

### 2.5 Traversal and Sub-Bundle Pruning Mechanics

The file discovery loop (lines 203–223) operates via `os.walk(target_path)`:
```python
for root, dirs, files in os.walk(target_path):
    current_dir = Path(root)
    if current_dir != target_path and (current_dir / "index.md").exists():
        dirs.clear()  # Do not recurse into separate sub-bundle
        continue
```
**Key Behavior:**
- If a subdirectory contains an `index.md`, the validator considers it an independent sub-bundle. It calls `dirs.clear()`, completely pruning that subdirectory and its children from the current scan!
- If a subdirectory **does not** contain `index.md`, the validator recursively traverses into it, and every `.md` file inside is treated as a concept document of the parent bundle.
- Reserved files:
  - `index.md` is handled only at the root; child `index.md` files prune recursion.
  - `log.md` is skipped (`if rel_path == "log.md": continue`), meaning `log.md` does not need frontmatter.

---

## 3. Conformance Test Suite & Live Execution Results

### 3.1 Unit Test Suite (`apex-meta/scripts/tests/test_okf_validator.py`)
- Test runner: `python -m unittest apex-meta/scripts/tests/test_okf_validator.py`
- Test suite covers 9 test cases:
  - 3 Green tests: valid bundle, custom local types (`Research`, `Plan`, `Standard`), code block exemptions.
  - 6 Red tests: missing root index, missing `type`, malformed YAML, broken index link, duplicate durable `id`, pseudo-OKF drift.
- **Execution Result:** `Ran 9 tests in 0.031s — OK`.

### 3.2 Live Execution Matrix on Existing Directories

| Target Directory | Command Executed | Result | OKF Errors | APEX Errors | Advisories | Failure Root Cause |
|---|---|---|---|---|---|---|
| `apex-meta/informatics` | `python apex-meta/scripts/okf_validator.py --target apex-meta/informatics` | **FAIL** (Exit 1) | 1 | 0 | 8 | Untracked `Agent_Setup/NextIteration/Prompt.md` has no frontmatter header (`---`) |
| `apex-meta/SmallSkills/OKF_Format` | `python apex-meta/scripts/okf_validator.py --target apex-meta/SmallSkills/OKF_Format` | **PASS** (Exit 0) | 0 | 0 | 8 | Fully conformant canonical OKF v0.2 bundle |
| `apex-meta/informatics/MMM` | `python apex-meta/scripts/okf_validator.py --target apex-meta/informatics/MMM` | **FAIL** (Exit 1) | 1 | 0 | 8 | `MMM/index.md` lacks `okf_version: "0.2"` (has `type: Index` instead) |
| `Agent_Setup/Lika Charity` | `python apex-meta/scripts/okf_validator.py --target "apex-meta/informatics/Agent_Setup/Lika Charity"` | **FAIL** (Exit 1) | 0 | 2 | 0 | `APEX-LINK-INTEGRITY`: 2 broken relative links in `index.md` |
| `Agent_Setup/Master of Arts Business` | `python apex-meta/scripts/okf_validator.py --target "apex-meta/informatics/Agent_Setup/Master of Arts Business"` | **FAIL** (Exit 1) | 0 | 2 | 0 | `APEX-LINK-INTEGRITY`: 2 broken relative links in `index.md` |

---

## 4. Current State of `apex-meta/informatics/`

### 4.1 Repository Inventory

The directory `c:\GitDev\apexai-os-meta\apex-meta\informatics` contains:

```
apex-meta/informatics/
├── index.md           # Canonical entrypoint (OKF v0.2, links standard.md, migration.md, log.md)
├── standard.md        # Apex Informatics Standard (14 sections, Wave 1, dated 2026-09-01)
├── migration.md       # Migration & Onboarding Policy (5 governing principles)
├── log.md             # Change Log (Wave 1 Ratification record)
├── MMM/               # Sub-bundle (has index.md, pruned from informatics walk)
│   ├── index.md
│   ├── established-concepts.md
│   └── working-method.md
└── Agent_Setup/       # Subdirectory WITHOUT index.md! (Causes walk leakage into informatics)
    ├── 00-README.md
    ├── 01-method-and-vocabulary-decision.md
    ├── 02-preflight-and-progressive-disclosure-design.md
    ├── 03-plan-sync-session-integration-and-patch-plan.md
    ├── 04-simulation-evaluation-suite.yaml
    ├── readmetest.txt
    ├── Lika Charity/  (sub-bundle with index.md)
    ├── Master of Arts Business/ (sub-bundle with index.md)
    └── NextIteration/
        └── Prompt.md  # UNTRACKED, NO FRONTMATTER (Triggers validation failure)
```

### 4.2 Structural Conformance Analysis

1. **Root Bundle Files (`index.md`, `standard.md`, `migration.md`, `log.md`):**
   - Cleanly conform to OKF v0.2.
   - `index.md` has `okf_version: "0.2"`, valid relative links.
   - `standard.md` has `type: Standard`.
   - `migration.md` has `type: Policy`.
   - `log.md` is reserved and properly formatted.

2. **Directory Leakage / Sub-Bundle Isolation Defect:**
   - Because `Agent_Setup/` has no `index.md`, `okf_validator.py` treats `Agent_Setup/` as part of the `apex-meta/informatics/` bundle.
   - `Agent_Setup/NextIteration/Prompt.md` (351 lines, research prompt for tax/insurance) lacks frontmatter, causing the validator run on `apex-meta/informatics` to fail.
   - If `Agent_Setup/` were either isolated with its own `index.md` declaring `okf_version: "0.2"` or moved/cleaned, `apex-meta/informatics` root files pass with `0 OKF Errors` and `0 APEX_PROFILE Errors`.

3. **Status Relative to `ORIGINAL_REQUEST.md` (Next-Generation Informatics):**
   - The current `apex-meta/informatics/standard.md` represents **Wave 1** (September 1, 2026).
   - It is a monolithic 160-line document describing the 14-section conformance profile.
   - It does **not** feature the required next-generation architecture:
     - No consolidated general router (`general-informatics-router.md` or updated `index.md` with XML IF-dispatch tags: `<informatics when="..." ref="..." deepen_when="...">`).
     - No modular specification triad (`writing-profile.md`, `file-architecture.md`, `execution-modes.md`).
     - No Significance & Ranking System (`[P0–P3 | I<val>/E<val>/R<val>]`).
     - No exact-match patch intent discipline references (`patch-intent-schema.json`).

---

## 5. Other Schemas and Tooling in `apex-meta/`

1. **`patch-intent-schema.json`**:
   - Location: `.claude/skills/deterministic-markdown-patcher2/references/patch-intent-schema.json`
   - Purpose: Standard JSON Schema (`draft/2020-12`) governing deterministic AST/regex markdown patch intents (`patch_intent.v1`). Requires `intents` array with `intent_id`, `operation`, `target`, `safety`.
2. **`apply_exact_patch.py`**:
   - Location: `apex-meta/scripts/apply_exact_patch.py`
   - Purpose: Deterministic patch executor enforcing `<file>`, `<old>`, `<new>` exact byte matching, single match uniqueness, and backup creation.
3. **`test_doc_schema_examples.py`**:
   - Location: `apex-meta/scripts/tests/test_doc_schema_examples.py`
   - Purpose: Anti-drift guard ensuring all `<!-- schema: <name>.schema.json -->` markdown code blocks validate against their JSON schemas.

---

## 6. Recommendations & Conformance Guidelines for Authors

To guarantee that newly authored files in `apex-meta/informatics/` achieve `0 OKF Errors` and `0 APEX_PROFILE Errors`:

1. **Root `index.md` Contract:**
   - Must begin with:
     ```yaml
     ---
     okf_version: "0.2"
     title: ...
     description: ...
     ---
     ```
   - Every markdown link `[Text](target.md)` in `index.md` must resolve to an existing file in `target_path`.

2. **Concept File Frontmatter Contract (`writing-profile.md`, `file-architecture.md`, `execution-modes.md`, etc.):**
   - Must begin on line 1 with `---` and close with `---`.
   - Must contain a non-empty `type: <TypeName>` field (e.g. `type: Specification`, `type: Standard`, `type: Reference`).
   - If `id:` is provided, it must be unique across all files in the bundle (e.g. `id: APEX-INF-WRITE-001`).
   - Use flat key-value pairs or inline bracket lists (`tags: [tag1, tag2]`). **Do not use multiline YAML lists** (`- item`), as they break the custom parser.

3. **Sub-Bundle Isolation:**
   - If subdirectories exist in `apex-meta/informatics/` (like `Agent_Setup/` or `MMM/`), they must either contain their own `index.md` with `okf_version: "0.2"` to trigger the validator's pruning logic, or non-concept markdown files inside must carry valid frontmatter.

4. **Style Advisory Guardrails:**
   - To avoid `STE-SENTENCE-LENGTH` advisory warnings, keep prose sentences <= 30 words, or wrap long structured instructions in lists, tables, or code fences (which are exempted).
