# Research & Verification Report: AI-Assisted Deterministic Patch Infrastructure

**Prepared by:** Outside-the-Box Research Lead, Deterministic AI Patch Infrastructure

**Date:** July 9, 2026

## Part 1: Path Comparison Summary

The core engineering challenge of AI-assisted patching lies in an architectural mismatch: LLMs are highly proficient at semantic comprehension and drafting target code, but are deeply unreliable at calculating precise text locations, hunk headers, line offsets, or structured diff formatting. To solve this, we must build a strict firewall between the **Phase 1 Planner AI** (semantic reasoning) and the **Phase 2 Deterministic Executor** (execution and structural validation).

Two core candidate architectures were evaluated:

### 1. CC Path (Toolchain + Hooks + Focused Deterministic Patchers)

The CC Path attempts to assemble a patchwork of specialized, pre-existing command-line utilities (e.g., `rg`, `yq`, `mdpatch`, `remark`) orchestrated via shell execution or Claude Code lifecycle hooks. The Planner AI outputs operational targets (e.g., a specific markdown heading path) and the executor chains these binaries to inject changes.

- **The Flaw:** This path treats structural parsing tools as highly resilient targets, but tools like `mdpatch` and `remark` are structurally rigid. If the Planner AI provides a slightly paraphrased heading or an incomplete path, these tools either crash or append content in completely wrong structural locations. Furthermore, full AST parsers like `remark` frequently rewrite the entire file's whitespace and formatting style, violating our formatting preservation guardrails.
    

### 2. GPT Path (Custom Intent Schema + Deterministic Live Resolver)

The GPT Path relies on a data-contract model. The Planner AI produces a highly structured `patch_intent.json` file populated with semantic anchors (surrounding text, heading paths, and operation intents). The Phase 2 Executor runs a dedicated, standard-library-first script (`patch_executor.py`) that reads the live codebase, scores the candidate spans using text-similarity and hierarchy-matching algorithms, ensures uniqueness, mutates raw text exactly at the matching index, and diffs via `git`.

### Strategic Convergence: The Hybrid Verdict

The CC and GPT paths should **not** remain separate; they must be **merged and simplified**.

- A pure CC path introduces fragile shell orchestration and severe dependency risks (e.g., `mdpatch` is a low-traction, unmaintained ecosystem package).
    
- A pure standard-library GPT path risks reinventing the wheel for complex formats like YAML frontmatter.
    

**The Winning Strategy:** Deploy a unified architecture that uses a strict **JSON Intent Schema** (GPT Path Core) processed by a specialized **Python Live Resolver Script**, which delegates to `git` for worktree isolation/diff-proofing and `yq` via subprocess for native frontmatter isolation.

## Part 2: Tool Ranking

The following evaluation table scores individual architectural components.

> _Metrics Notice:_ Implementation Cost is scored where **higher = lower engineering cost/effort**. Risk is scored where **higher = greater risk of catastrophic failure/corruption**.

|**Rank**|**Path / Tool**|**Phase Role**|**Evidence (1-100)**|**Impact (1-100)**|**Resilience (1-100)**|**Effectiveness (1-100)**|**Token Efficiency (1-100)**|**Implementation Cost (1-100)**|**Risk (1-100)**|**Adopt / Trial / Reject**|**Rationale**|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**1**|`git` (Worktree & Diff)|Phase 2 Isolation & Proof|100|95|98|99|95|95|5|**Adopt**|Industry standard for rolling back failed states and creating human-auditable cryptographic proofs of changes.|
|**2**|Custom Resolver (`patch_resolver.py`)|Phase 2 Target Scoring|90|95|95|92|90|75|15|**Adopt**|Essential for scoring anchors, handling paraphrased text, and generating multi-match ambiguity alerts natively.|
|**3**|`yq --front-matter=process`|Phase 2 Frontmatter Editor|95|85|90|95|88|90|10|**Adopt**|The cleanest, safest tool available for updating Markdown YAML metadata without impacting the main body content.|
|**4**|`patch_intent.schema.json`|Phase 1 Output Contract|95|90|92|90|95|85|10|**Adopt**|Forces the LLM into a deterministic schema, enabling standard JSON validation before touching disk files.|
|**5**|`rg` (ripgrep)|Phase 2 Fast Discovery|100|70|85|80|90|90|12|**Trial**|Excellent for ultra-fast multi-file string searches, but can be substituted by Python's native `pathlib` scan loops.|
|**6**|Claude Code Hooks|Phase 2 Policy Enforcement|90|75|80|75|85|80|15|**Trial**|Useful for hard-blocking unapproved tools like `sed` inside interactive agent loops, but unnecessary in rigid CI lines.|
|**7**|`mdpatch` / `markdown-patch`|Phase 2 Section Mutation|40|50|30|45|60|85|65|**Reject**|Low open-source maintainership (15 stars). Incapable of fuzzy anchor matching; appends blindly if names diverge.|
|**8**|`remark` / `mdast`|Phase 2 AST Parser|95|40|60|50|40|45|70|**Reject**|Full AST serialization breaks existing manual formatting layouts and adds heavy Node.js runtime overhead to the pipeline.|
|**9**|`comby`|Phase 2 Structural Search|85|55|50|40|70|60|45|**Reject**|Exceptional for programming language syntax blocks, but lacks structural awareness of Markdown header nesting.|
|**10**|`sed` / `awk` / `perl`|Phase 2 String Replacement|100|20|10|30|95|95|95|**Reject**|Extreme risk of catastrophic line corruption; completely breaks down when processing multi-line semantic blocks.|

## Part 3: Failure-Mode Matrix

This matrix evaluates how each path addresses the core failure modes of unreliable AI planning.

|**Required Test Scenario**|**CC Path Capability**|**GPT Path Capability**|**Hybrid (Final Architecture) Handling**|
|---|---|---|---|
|**1. simple_exact_span**|**Pass** (via `mdpatch` if heading is perfect).|**Pass** (resolves text block directly).|**Pass**. Locates block, verifies uniqueness, replaces block.|
|**2. wrong_line_numbers**|**Pass** (CLI tools ignore line numbers).|**Pass** (treats lines as a low-weight score factor).|**Pass**. Skips line numbers entirely or uses them only as low-priority hints.|
|**3. duplicate_heading**|**Fail** (Appends blindly or fails with error).|**Pass** (Flags identical match scores).|**Pass**. Throws an explicit `AmbiguityError` and lists all discovered matches.|
|**4. nested_heading_path**|**Pass** (Supports `H1::H2` syntax structure).|**Pass** (Walks array elements sequentially).|**Pass**. Tracks parent-to-child header stacks to isolate the unique targeted section.|
|**5. paraphrased_anchor**|**Fail** (Literal matching breaks CLI execution).|**Pass** (Computes string similarity weights).|**Pass**. Uses sliding window token ratio scoring to pinpoint the correct block.|
|**6. frontmatter_update**|**Pass** (Handled natively by `yq`).|**Fail** (Brittle via raw text regex).|**Pass**. Python orchestrator transparently routes frontmatter blocks directly to `yq`.|
|**7. table_row_update**|**Fail** (Extremely brittle via standard CLI).|**Pass** (Treats rows as lines within a block).|**Pass**. Targets the block span, identifies the inner row via text anchors, modifies it.|
|**8. large_file_small_edit**|**Pass** (Slices exact section out).|**Pass** (In-memory token slice edit).|**Pass**. Modifies only the targeted line boundaries without reading or outputting whole files.|
|**9. multi_file_patch_pack**|**Fail** (Requires complex wrapper scripts).|**Pass** (Iterates over structured arrays).|**Pass**. Loops through the JSON object array, checking files against an explicit allowlist.|
|**10. bad_ai_patch**|**Fail** (If dependent on AI unified diff format).|**Pass** (Ignores diff format entirely).|**Pass**. Immune to diff errors because it accepts only structured data intents.|
|**11. formatting_preservation**|**Fail** (AST tool chains reformat entire file).|**Pass** (Slices raw strings directly).|**Pass**. Performs localized byte/string splicing, guaranteeing unedited code is untouched.|
|**12. failed_validation_rollback**|**Pass** (If chained with manual shell cleanup).|**Pass** (Automatic runtime try-catch loop).|**Pass**. Runs a strict post-write test suite; immediately triggers `git reset --hard` on failure.|

## Part 4: Recommended Final Architecture

### 1. Minimum Viable Architecture (MVA)

The optimal setup consists of a centralized Python 3 engine accompanied by the `yq` binary. The system contains no external runtime application layer dependencies (e.g., node_modules, third-party wheels), eliminating supply chain vulnerabilities and runtime execution failures.

```
+---------------------------------------------------------+
|                  Phase 1: Planner AI                    |
|  Emits abstract semantic intent via strict JSON Schema  |
+---------------------------+-----------------------------+
                            |
                            | (patch_intent.json)
                            v
+---------------------------------------------------------+
|             Phase 2: Deterministic Executor             |
|                                                         |
|   +-------------------------------------------------+   |
|   |                  patch_resolver.py              |   |
|   |  * Validates File Allowlist Scopes              |   |
|   |  * Scans Headings & Computes Anchor Similarity  |   |
|   |  * Resolves Absolute Target Spans & Injects Text|   |
|   +-----------------------+-------------------------+   |
|                           |                             |
|                           | (If Frontmatter Operation)  |
|                           v                             |
|   +-------------------------------------------------+   |
|   |         yq subprocess invocation                |   |
|   +-----------------------+-------------------------+   |
|                           |                             |
|                           v                             |
|   +-------------------------------------------------+   |
|   |               git apply / check / diff          |   |
|   |  * Generates Diff Cryptographic Proofs          |   |
|   |  * Executes Test/Lint Fixtures                  |   |
|   |  * Performs Automatic Rollbacks on Failures     |   |
|   +-------------------------------------------------+   |
+---------------------------------------------------------+
```

### 2. Optional Later Additions

- **Vector Anchor Evaluation:** Embedding-based similarity check loops for cases where anchors are heavily translated or rephrased.
    
- **Interactive Elicitation Loops:** Hooking into Claude Code’s `AskUserQuestion` tool when an ambiguity is detected, prompting the engineer to choose between multiple matched paths instead of flatly rejecting.
    

### 3. Rejected Tools & Frameworks

- `sed`, `awk`, `perl` are strictly banned due to escaping risks, lack of structure validation, and high multi-line fragility.
    
- `remark` and `mdpatch` are rejected to prevent global file reformatting side effects and remove unstable Node module dependencies.
    

### 4. Phase 1 Artifact Schema (`patch_intent.schema.json`)

JSON

```
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "AIPatchIntentPack",
  "type": "object",
  "properties": {
    "patches": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "target_file": { "type": "string" },
          "operation": { "type": "string", "enum": ["replace_section", "append_section", "update_frontmatter", "update_table_row"] },
          "heading_path": { "type": "array", "items": { "type": "string" } },
          "frontmatter_key": { "type": "string" },
          "anchors": {
            "type": "object",
            "properties": {
              "nearby_phrases": { "type": "array", "items": { "type": "string" } },
              "line_number_hint": { "type": "integer" }
            },
            "required": ["nearby_phrases"]
          },
          "replacement_text": { "type": "string" }
        },
        "required": ["target_file", "operation", "anchors", "replacement_text"]
      }
    },
    "validation_commands": {
      "type": "array",
      "items": { "type": "string" }
    }
  },
  "required": ["patches", "validation_commands"]
}
```

### 5. Phase 2 Deterministic Pipeline Execution Sequence

1. **Ingestion & Validation:** Parse and validate the structure of `patch_intent.json` against the schema definitions.
    
2. **Scope Verification:** Assert that all values in `target_file` reside within the pre-defined target validation allowlist.
    
3. **Workspace Isolation Check:** Confirm that the local `git status --porcelain` is clear. If run in a automated system, open an isolated `git worktree`.
    
4. **Target Selection Scoring:**
    
    - If `update_frontmatter`: Extract the frontmatter boundaries and delegate modification to `yq`.
        
    - If body modification: Read the raw document lines. Locate the `heading_path` structural blocks. Search inside those blocks using a sliding text matching window to identify where `nearby_phrases` align.
        
    - Assign confidence values ($0.0$ to $1.0$). If the top candidate meets the matching confidence threshold ($>0.85$) and no competing candidate sits within a $0.15$ margin, select the target span index.
        
5. **Ambiguity Boundary Enforcement:** If multiple matching regions return equivalent high scores, halt the application sequence immediately and export an `AmbiguityReport` detailing the conflicting file offsets.
    
6. **Mutation & Splice:** Perform text manipulation directly on the selected line ranges without running global text normalization.
    
7. **Verification and Rollback Loop:** Run the specified `validation_commands` shell array. If any command throws a non-zero exit code, execute `git reset --hard` to restore the environment, print the test trace, and exit with error code `1`.
    
8. **Proof Serialization:** Run `git diff` to extract clean, system-generated patch details for validation tracking.
    

## Part 5: Implementation Prompt for Codex / Claude Code

Plaintext

```
Create a single, self-contained Python 3 script named `patch_executor.py` that handles deterministic file modifications using only the Python standard library (plus executing the `yq` binary via subprocess for frontmatter changes).

The script must accept a single command-line argument pointing to a `patch_intent.json` file conforming to our strict patch schema.

Core Functional Requirements:
1. Scope Gate: Read an allowed files list from `patch_policy.json`. Reject execution if intent targets unauthorized files.
2. Resolution & Anchor Scoring: For body edits, do not trust line numbers or exact match lookups. Implement a text anchor matcher using `difflib.SequenceMatcher` to find lines corresponding to `nearby_phrases` inside the block targeted by `heading_path`.
3. Guardrails: If multiple regions match with similar high confidence scores, or if the maximum match confidence score falls below 0.85, exit with exit code 2 and emit a JSON-formatted Ambiguity Report to stderr.
4. Formatting Preservation: Perform text injection using array slicing on raw content strings. Do not use Markdown parsers that re-serialize or reformat unrelated paragraphs.
5. Verification Loop: If file modifications succeed, run the commands defined in the `validation_commands` array via subprocess. If any test command fails, immediately run `git reset --hard` to discard changes and exit with exit code 1. If all checks pass, print a clean `git diff` summary to stdout and exit with exit code 0.
```

## Part 6: Final Verdict

**Decision:** **Merge both approaches into the Hybrid Intent-Resolver Architecture.**

The CC path’s reliance on third-party Markdown AST command-line options introduces severe document reformatting bugs and fails completely when faced with paraphrased or out-of-date text anchors. The GPT path's schema structure cleanly separates semantic interpretation from code updates but is inefficient when trying to modify nested frontmatter configurations via raw regular expressions. Merging them creates an optimal pipeline: we use the planner-isolated JSON intent schema from the GPT path, execute precise anchor-scoring calculations inside an explicit Python script, utilize `yq` exclusively for metadata updates, and enforce safety and execution tracking using native `git` capabilities. This configuration delivers robust error resilience with negligible token footprints.

_End of Report._