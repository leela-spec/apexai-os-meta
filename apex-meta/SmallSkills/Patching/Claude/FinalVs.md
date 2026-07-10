# 1. Executive verdict

The strongest overlap is not “CC vs GPT vs GEM.” All three reports converge on the same core architecture: **Phase 1 planner AI emits semantic patch intent + replacement content; Phase 2 deterministic executor resolves the exact live target, validates uniqueness/scope, applies one bounded mutation, produces git diff proof, runs validation, and fails closed on ambiguity.** GPT frames this as “merge and simplify,” with CC as runtime/tooling and GPT as schema/resolver/finalizer . CC also says the paths converge and should merge into a minimal schema + CLI enforcement architecture . GEM independently reaches the same hybrid verdict but is more skeptical of external Markdown tools, recommending JSON intent + Python live resolver + git + yq .

**Verdict:** adopt a **hybrid, simplified architecture**.  
**Research status:** solved enough to build an MVP; not solved enough to trust `mdpatch`, `remark`, `comby`, fuzzy matching, or table edits without fixtures.

---

# 2. Cross-report overlap matrix

|component_or_process|GPT_support|CC_support|GEM_support|overlap_level|direct_evidence_summary|verdict|
|---|---|---|---|---|---|---|
|Two-phase planner/executor split|Strong|Strong|Strong|100|GPT: Phase 1 semantic intent, Phase 2 deterministic live-span executor. CC: planner intent + deterministic resolver + proof. GEM: strict firewall between planner AI and executor.|**Core**|
|Reject AI-authored diffs as primary input|Strong|Strong|Strong|100|GPT rejects AI unified diffs and raw fuzz patching; CC rejects AI-authored diffs; GEM rejects diff dependence via JSON intent.|**Core exclusion**|
|`patch_intent` schema|Strong|Strong|Strong|100|GPT requires JSON execution schema; CC requires YAML/JSON intent; GEM centers `patch_intent.schema.json`.|**Core**|
|Custom live resolver / Python executor|Strong|Strong|Strong|100|GPT ranks custom resolver #1; CC uses `patch_resolver.py`; GEM ranks custom resolver #2 and makes it central.|**Core**|
|Git proof: worktree/diff/apply-check|Strong|Strong|Strong|100|All three use git as proof/finalization/rollback layer. Git docs confirm `git apply --check` validates patch applicability without applying, and `git worktree` creates separate linked working trees.|**Core**|
|`yq --front-matter=process`|Strong|Strong|Strong|100|All three support `yq` for frontmatter. Official docs confirm process mode edits YAML frontmatter and outputs the full file including non-YAML body; docs also warn only the first passed file is processed for frontmatter.|**Core for frontmatter**|
|`rg` / ripgrep|Strong|Strong|Medium|85|GPT/CC adopt; GEM treats as substitutable. Official README supports recursive search, `.gitignore` respect, hidden/binary skipping.|**Core discovery tool, not mutator**|
|Claude Code hooks|Strong|Strong|Medium|80|GPT/CC support hooks; GEM treats them as useful but not required in rigid CI. Official docs confirm lifecycle hooks and Pre/Post tool events.|**Adopt after audit mode**|
|`mdpatch`|Trial|Trial|Reject|55|GPT and CC trial it after fixture bakeoff; GEM rejects due to fragility and maintenance/traction concerns. Current repo exists and advertises heading/block/frontmatter structure-aware edits.|**Trial only**|
|`remark` / mdast|Trial later|Adopt/trial|Reject|55|CC likes mdast; GPT says trial later; GEM rejects full AST serialization due to formatting risk. `mdast-util-heading-range` can replace a heading section until the next same/lower heading, but this does not prove formatting preservation after serialization.|**Trial only, range extraction not full rewrite**|
|`comby`|Optional|Optional|Reject|40|Useful for code-like patterns, but no cross-report support as Markdown core. Comby is structural search/replace for code-like structures, not Markdown heading semantics.|**Optional niche**|
|`sed` / `awk` / `perl`|Wrap only|Wrap only / reject|Reject|70 for exclusion|Deterministic availability is not resilience. GNU sed and awk support in-place-style editing, but they do not prove semantic target uniqueness or Markdown structure.|**Reject as first-class mutators**|

---

# 3. Tool ranking

**Risk score: higher = worse. Implementation cost: higher = cheaper/easier.**

|rank|tool_or_component|phase_role|GPT|CC|GEM|cross_report_overlap|evidence|impact|resilience|effectiveness|token_efficiency|implementation_cost|risk|adopt_trial_wrap_reject|rationale|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|1|`patch_intent.schema.json`|Phase 1 contract|Adopt|Adopt|Adopt|100|92|95|92|90|96|85|10|**Adopt**|Forces AI to emit only semantic intent, replacement text, hints, and validation—not executable byte-level claims.|
|2|Custom Python live resolver/executor|Phase 2 core|Adopt|Adopt|Adopt|100|88|96|94|91|93|72|18|**Adopt**|Only component directly matches the failure premise: executor resolves live bytes and fails on ambiguity.|
|3|Git worktree + diff + apply-check|Proof/finalization|Adopt|Adopt|Adopt|100|96|90|90|88|92|88|12|**Adopt**|`git apply --check` is a non-writing applicability gate; worktrees isolate mutation; git diff is audit proof.|
|4|`yq --front-matter=process`|Frontmatter|Adopt|Adopt|Adopt|100|94|86|88|86|95|84|18|**Adopt with guards**|Strongest external tool for YAML frontmatter. Must pre-check delimiter and loop files one-by-one.|
|5|Scope policy / allowlist|Safety gate|Adopt|Adopt|Adopt|100|85|90|92|85|90|90|10|**Adopt**|Cheap, deterministic blocker for hallucinated paths and scope creep.|
|6|Fixture runner|Validation|Adopt|Implied/adopt|Implied|85|82|86|88|82|88|78|16|**Adopt**|Converts repeated manual validation into deterministic pass/fail.|
|7|`rg` / ripgrep|Discovery/counting|Adopt|Adopt|Trial/substitutable|85|92|80|78|82|94|90|20|**Adopt as discovery only**|Fast match counting and candidate discovery; not a mutation tool.|
|8|Claude Code hooks|Enforcement|Adopt after audit|Adopt|Trial|80|88|82|84|76|82|62|35|**Adopt after audit mode**|Hooks enforce policy in Claude Code; they are not a patcher and need their own security review.|
|9|Pure-Python heading scanner|Section resolution|Implied|Alternative|Adopt|80|70|82|84|78|88|82|25|**Adopt MVP**|Cheaper than Node AST stack; sufficient for heading-path block extraction if fail-closed.|
|10|`mdpatch` / markdown-patch|Section backend|Trial|Trial|Reject|55|68|75|55|70|80|65|50|**Trial only**|Exists and targets headings/frontmatter structurally, but no report gives enough fixture evidence for core adoption.|
|11|`remark` / mdast / heading-range|AST backend|Trial later|Adopt/trial|Reject|55|75|70|62|72|60|45|52|**Trial only**|Good heading-range semantics; serialization/formatting risk remains unproven.|
|12|`comby`|Code-like pattern edits|Optional|Optional|Reject|40|70|55|50|58|70|60|48|**Optional niche**|Better for code-like structures than Markdown sections.|
|13|`awk`|Wrapped table helper|Wrap only|Reject/wrap|Reject|70 exclusion|65|45|35|45|85|76|65|**Wrap only**|Usable only after executor proves unique row/key; not first-class mutation.|
|14|`sed`|Wrapped exact replacement|Wrap only|Reject/wrap|Reject|70 exclusion|70|40|30|40|90|85|70|**Wrap only**|Deterministic but unsafe without match-count and diff gates. GNU sed supports `-i`; that does not imply target safety.|
|15|`perl -i`|Wrapped multiline regex|Wrap only|Reject/wrap|Reject|70 exclusion|55|42|30|45|88|70|75|**Wrap only / avoid**|Powerful multiline mutation; high blast radius if exposed to AI or regex guessed.|
|16|AI-authored unified diff|Executable artifact|Reject|Reject|Reject|100 exclusion|90|35|20|40|50|80|85|**Reject as primary**|Directly violates the premise. Keep only as generated proof from live mutation.|
|17|`patch --fuzz=3`|Legacy fallback|Reject|Not core|Reject implied|70 exclusion|60|30|25|35|60|80|80|**Reject as core**|Fuzz increases risk that stale context applies too generously.|

---

# 4. Process ranking

|rank|process|supported_by|evidence|impact|resilience|token_efficiency|implementation_cost|risk|verdict|
|---|---|---|---|---|---|---|---|---|---|
|1|**Hybrid schema + Python orchestrator + selected CLI tools**|GPT + CC + GEM|95|96|94|94|78|18|**Build now**|
|2|**AI semantic intent schema → deterministic live resolver**|GPT + CC + GEM|93|95|94|95|75|18|**Core architecture**|
|3|**GPT custom Python resolver/finalizer**|GPT + GEM + partial CC|85|90|90|92|75|22|**Core MVP body-edit mechanism**|
|4|**CC external toolchain + hooks**|CC + GPT + partial GEM|80|84|80|86|65|35|**Runtime/enforcement layer, not architecture alone**|
|5|**Whole-file replacement for small Claude skill files**|External project context, not all reports|60|68|70 if explicitly authorized|75|90|35|**Allowed only for small files / explicit full rewrite**|
|6|**AI exact search/replace → executor**|Weak / rejected premise|35|45|35|70|85|70|**Reject as primary; only use executor-extracted old span**|
|7|**AI-authored unified diff → git apply**|All reject as primary|25|35|20|55|80|85|**Reject**|

---

# 5. Failure-mode stress test

|scenario|best_supported_handling|which_reports_support_it|remaining_risk|must_fail_or_can_patch|implementation_requirement|
|---|---|---|---|---|---|
|Wrong line numbers|Ignore line numbers or treat as non-authoritative metadata only.|GPT, CC, GEM|Low if schema excludes executable line ranges.|**Can patch**|Schema must not include executable `line_start` / `line_end`.|
|Missing `old_text`|Executor extracts live span; planner never supplies exact old text.|GPT, CC, GEM|Low.|**Can patch**|`replace_once` uses executor-extracted span, not AI old text.|
|Paraphrased nearby phrase|Use as hint only; if no unique live span, emit ambiguity report.|GPT, CC, GEM disagree on confidence; all flag fragility|High.|**Must fail unless uniquely resolved**|No fuzzy replacement without explicit threshold + competing-candidate margin + report.|
|Duplicate heading|Require full heading path and uniqueness; otherwise fail.|GPT, CC, GEM|Medium for repeated heading paths.|**Must fail if non-unique**|Heading stack scanner; ambiguity output with candidate paths.|
|Nested heading path|Resolve by ordered heading stack, not leaf heading alone.|GPT, CC, GEM|Medium if malformed Markdown.|**Can patch**|Heading path parser with start/end bounds.|
|Frontmatter update|Use `yq --front-matter=process` or tested parser; pre-check `---`; loop per file.|GPT, CC, GEM|Low-medium: malformed YAML / no delimiter.|**Can patch with guards**|Delimiter check, YAML parse check, post-diff body preservation check.|
|Markdown table row update|Treat as trial: find table block, validate header, unique row key, replace one row.|GPT trial, CC fragile, GEM optimistic|High.|**Trial; fail on ambiguity**|Custom row parser fixture suite.|
|Large file small edit|Read file locally, extract bounded section/span, mutate only span.|GPT, CC, GEM|Low if diff scope gate works.|**Can patch**|No full-file LLM regeneration; git diff scope proof.|
|Multi-file patch pack|Iterate intent array; enforce allowed paths; validate cumulative diff/apply-check if patch pack generated.|GPT, CC, GEM|Medium: ordering and partial failures.|**Can patch**|Worktree or checkpoint; all-or-nothing validation.|
|Invalid AI-authored unified diff|Ignore/reject raw diff as input.|GPT, CC, GEM|Low if schema gate enforced.|**Must fail**|Schema rejects diff/hunk fields.|
|Formatting preservation|Raw span splice preserves unrelated bytes; AST tools trial only.|GPT strongest; GEM strongest rejection; CC acknowledges risk|Medium for section tools.|**Can patch for raw span; trial for AST/mdpatch**|Byte/span diff proof and fixture for CRLF, trailing newline, code fences.|
|Failed validation rollback|Worktree discard or git reset/checkout allowed paths; structured failure report.|GPT, CC, GEM|Low if isolated.|**Must rollback**|Worktree or clean checkpoint; no push before pass.|

---

# 6. Evidence conflicts and unresolved questions

## Claims where reports disagree

|disputed claim|GPT|CC|GEM|synthesis|
|---|---|---|---|---|
|`mdpatch` suitability|Trial|Trial|Reject|**Trial only**. Current repo exists and claims structure-aware Markdown edits, but cross-report resilience evidence is insufficient.|
|`remark/mdast` suitability|Trial later|More favorable|Reject|**Trial only**. `heading-range` semantics are real, but full serialization may reformat; use only if fixtures prove formatting stability.|
|`rg` core vs substitutable|Adopt|Adopt|Trial/substitutable|**Adopt for discovery** because it is cheap and proven; executor must still make final selection.|
|Hooks required|Adopt after audit|Adopt|Trial|**Audit first, block later**. Hooks enforce agent behavior but are not part of the patch algorithm.|
|Fuzzy matching|Fail safely / thresholds|Fragile|More optimistic|**Do not make fuzzy matching a silent writer.** It can rank candidates but must fail if confidence or margin is weak.|
|Table row update|Trial|Gap|Optimistic pass|**Trial only**. No report provides enough fixture evidence.|

## Claims needing web or fixture verification before implementation

1. `mdpatch` behavior on duplicate headings, nested paths, frontmatter, CRLF, code fences, no trailing newline.
2. `remark/mdast` stringify behavior on your actual corpus.
3. `yq` behavior on malformed/no frontmatter and multi-file invocations; official docs already warn frontmatter mode processes only the first passed file.
4. Claude Code hook blocking behavior in your exact version/config; official docs define hooks but hook scripts are privileged and need test coverage.
5. Fuzzy anchor thresholds on real Apex/skill Markdown files.
6. Table-row parser behavior across escaped pipes, alignment rows, multiline cells, code blocks.

## Hidden assumptions that could break implementation

- “Deterministic” does not mean “safe.” `sed`, `awk`, and `perl` are deterministic but can deterministically corrupt the wrong region.
- `git apply --check` validates a patch artifact; it does not validate semantic intent. It belongs after live mutation as proof, not as primary AI patch executor.
- Markdown AST tooling can identify structure but may reserialize formatting.
- Hooks can block tool calls, but hook code itself becomes part of the trusted computing base.
- `target_file_guess` is still a guess; the allowlist and resolver must verify it.

## Where implementation can be simpler than the reports suggest

- Do **not** build mdpatch/remark/comby integrations in MVP.
- Do **not** build embeddings/vector anchors.
- Do **not** build multi-agent planner/controller layers.
- Do **not** create a 20-file contract package.
- Build **one schema**, **one executor**, **one policy file**, **one fixture runner**, and optional **audit-mode hooks**.

---

# 7. Recommended final architecture

## Minimum viable process

```
architecture: deterministic_ai_patch_mvp.v1
decision: build_hybrid_minimal
core_rule: "AI writes semantic intent and new content; executor resolves exact live target or fails."
must_not_depend_on:
  - ai_authored_unified_diff
  - ai_authored_exact_old_text
  - ai_line_numbers
  - ai_hunk_headers
  - ai_search_strings
must_fail_when:
  - target_file_not_allowlisted
  - target_not_found
  - target_not_unique
  - heading_path_ambiguous
  - fuzzy_anchor_low_confidence
  - validation_fails
  - diff_touches_unallowed_path
```

## Phase 1 artifact schema

```
{
  "schema_version": "patch_intent.v1",
  "patch_id": "short-kebab-id",
  "allowed_paths": ["relative/path.md"],
  "operation": "replace_once | replace_heading_section | frontmatter_set | table_row_update | append_section | validate_only",
  "target": {
    "file_guess": "relative/path.md",
    "heading_path": ["H1", "H2"],
    "nearby_phrases": ["hint only, not executable"],
    "frontmatter_key": "status",
    "table": {
      "header_required": ["Name", "Status"],
      "row_key_column": "Name",
      "row_key_value": "Example"
    }
  },
  "replacement": {
    "new_text": "authoritative replacement content",
    "frontmatter_value": null
  },
  "validation": {
    "must_contain": [],
    "must_not_contain": [],
    "commands": [],
    "max_changed_files": 1
  },
  "safety": {
    "require_unique_target": true,
    "allow_full_file_rewrite": false,
    "allow_create_if_missing": false,
    "fail_on_ambiguous_heading": true
  }
}
```

## Phase 2 deterministic pipeline

```
phase_2_pipeline:
  - preflight:
      run:
        - git rev-parse --show-toplevel
        - git status --porcelain
      gate:
        - repo_matches_policy
        - target_paths_allowlisted
  - inspect:
      action: read_live_files_locally
      gate:
        - file_exists_or_create_allowed
  - resolve:
      action: compute_exact_span_from_live_file
      gate:
        - zero_matches_fail
        - multiple_matches_fail
        - low_confidence_fails
        - duplicate_heading_fails
  - mutate:
      action: atomic_write_selected_span_only
      gate:
        - one_operation_only
        - no_adjacent_cleanup
        - no_full_file_rewrite_unless_explicit
  - prove:
      run:
        - git diff -- <allowed_paths>
      gate:
        - diff_non_empty_when_mutation_expected
        - changed_files_subset_allowed_paths
  - validate:
      run:
        - declared_validation_commands
        - fixture_runner_checks
      gate:
        - all_checks_pass
  - finalize:
      action: write_success_or_failure_report
      optional:
        - git_generated_patch_pack
        - git_apply_check_on_generated_patch
```

## Core tools

|tool|role|
|---|---|
|Python executor|Resolver, scope gate, span extraction, mutation, reporting|
|JSON schema|Phase 1 contract|
|Git|proof, worktree isolation, diff, rollback|
|`yq`|frontmatter-only mutations|
|`rg`|discovery and match counting|
|Fixture runner|deterministic behavioral validation|

## Optional tools

|tool|condition|
|---|---|
|Claude Code hooks|Start audit-only; block direct writes after hook tests pass.|
|`mdpatch`|Only after fixture bakeoff.|
|`remark/mdast`|Only for complex section operations; avoid full-file serialization.|
|`comby`|Only for code-like patterns inside Markdown.|

## Rejected tools/processes

```
rejected:
  - ai_authored_unified_diff_as_primary_artifact
  - ai_authored_exact_old_text_as_executable_input
  - line_number_based_mutation
  - patch_fuzz_as_core_strategy
  - direct_sed_i_from_planner
  - direct_perl_i_from_planner
  - direct_awk_mutation_from_planner
  - full_file_rewrite_by_default
  - markdown_ast_full_reserialize_without_fixture_proof
```

## Safety gates

```
safety_gates:
  schema_validation: required
  path_allowlist: required
  target_uniqueness: required
  ambiguity_report: required
  diff_scope_check: required
  validation_commands: required_when_declared
  rollback_on_failure: required
  no_push_without_explicit_instruction: required
```

## Audit/reporting outputs

```
outputs:
  success:
    - patch_success.json
    - git_diff_summary.txt
    - validation_report.json
  failure:
    - patch_failure.json
    - ambiguity_report.json
    - unchanged_worktree_or_rollback_confirmation
```

---

# 8. Implementation prompt for Codex/Claude Code

```
prompt_type: deterministic_execution_build
role: deterministic_execution_orchestrator

repo: leela-spec/apexai-os-meta
branch: main

target_files:
  - apex-meta/SmallSkills/Patching/patch_executor.py
  - apex-meta/SmallSkills/Patching/patch_policy.json
  - apex-meta/SmallSkills/Patching/fixture_runner.py

task:
  - Build a minimal deterministic Markdown/config patch executor.
  - Work directly on main.
  - Do not create a branch.
  - Do not open a PR.
  - Do not read unrelated files.
  - Do not build a broad framework.
  - Reuse patterns from apex-meta/SmallSkills/Patching/stub_repair_toolkit.py only if useful.

patch_executor.py:
  must_accept:
    - patch_intent.json
  must_support:
    - inspect
    - locate
    - extract-span
    - replace-once
    - replace-heading-section
    - frontmatter-set
    - validate-scope
    - diff
    - finalize
  must_refuse:
    - target path outside patch_policy.json allowlist
    - zero target matches
    - multiple target matches
    - ambiguous duplicate headings
    - AI-authored unified diffs as input
    - AI-authored old_text unless produced by executor extract-span
    - full-file rewrite unless allow_full_file_rewrite is true
  must_emit:
    - patch_success.json on success
    - patch_failure.json on validation failure
    - ambiguity_report.json on non-unique target

patch_policy.json:
  include:
    - allowed_paths
    - protected_paths
    - allow_full_file_rewrite_default: false

fixture_runner.py:
  must_support:
    - JSON fixture spec
    - create fixture files
    - run declared commands
    - assert must_contain and must_not_contain
    - return nonzero on failure

commands:
  - git checkout main
  - git pull --ff-only origin main
  - python -m py_compile apex-meta/SmallSkills/Patching/patch_executor.py apex-meta/SmallSkills/Patching/fixture_runner.py
  - python apex-meta/SmallSkills/Patching/patch_executor.py --self-test
  - python apex-meta/SmallSkills/Patching/fixture_runner.py --self-test
  - git diff -- apex-meta/SmallSkills/Patching

expected_result:
  - compile passes
  - self-tests pass
  - fixtures cover replace-once, duplicate heading rejection, frontmatter-set, scope rejection
  - no unrelated files changed

commit:
  message: "Add deterministic Markdown patch executor"
  push: origin main

final_report:
  format:
    - changed_files
    - commands_run
    - pass_fail
    - commit_sha
```

---

# 9. Final detective conclusion

**Proven enough to build now:** the overlap-backed architecture: `patch_intent.json` → Python live resolver/executor → path allowlist → exact span/heading/frontmatter resolution → bounded mutation → git diff proof → validation → rollback/failure report. This is supported by all three reports and by current docs for git, worktrees, yq, ripgrep, and Claude Code hooks.

**Trial-only:** `mdpatch`, `remark/mdast`, `comby`, fuzzy matching, table row editing, blocking hooks. They may be valuable, but they need fixture bakeoffs before becoming core.

**Do not build:** AI-authored unified diff as the main artifact, line-number mutation, exact AI `old_text` replacement, direct `sed -i` / `perl -i` / `awk` mutation from planner output, raw fuzz patch workflows, and full-file Markdown AST reserialization as default.

**What was misunderstood before:** the “patch” should not be the thing the AI writes. The reliable artifact is the **intent**, and the reliable proof is the **git-generated diff after deterministic live mutation**. The executor, not the model, must own exact target selection.