# Path comparison summary

**Verdict:** merge and simplify both paths.

The two paths are not true alternatives. They describe different layers:

|Path|Real role|Keep?|Reason|
|---|---|--:|---|
|**CC path**|Runtime enforcement + toolchain surface|**Yes, but slimmed down**|Claude Code/Codex is where hooks, git, `rg`, `yq`, validators, and final mutation can run.|
|**GPT path**|Intent schema + deterministic resolver/finalizer|**Yes, as the core architecture**|This directly matches the real failure model: planner AI gives semantic intent and new text; executor owns exact live-file resolution.|

The corrected architecture is therefore:

> **Phase 1:** AI emits structured semantic patch intent and replacement content.  
> **Phase 2:** deterministic executor resolves live span, validates uniqueness, mutates through approved modes, generates git diff proof, runs fixtures/tests, and fails closed on ambiguity.

This aligns with the internal baseline that rejects AI-authored exact patches/search strings and makes the executor select live spans, replace once, validate, diff, and optionally commit/push. It also matches the existing `stub_repair_toolkit.py` split: LLM does semantic repair/new content; script does worktree management, git diff/check, fixtures, scope checks, manifest/finalization.

# Tool ranking

Scores are analytic 1–100. **Risk: higher = worse.** **Implementation cost: higher = cheaper/easier.**

|rank|path_or_tool|phase_role|evidence|impact|resilience|effectiveness|token_efficiency|implementation_cost|risk|adopt_trial_reject|rationale|
|--:|---|---|--:|--:|--:|--:|--:|--:|--:|---|---|
|1|**custom live-span resolver/executor**|Core Phase 2|88|96|94|90|92|72|18|**Adopt**|Best fit for “AI gives intent/new text, not exact old text.” Must own extraction, uniqueness, mutation, diff, rollback.|
|2|**git worktree + git diff + git apply --check**|Proof/finalization|95|86|88|84|90|86|15|**Adopt**|Git docs confirm `git apply` expects unified diff context and can check applicability before write; use patches as generated proof, not AI-authored input. ([Git](https://git-scm.com/docs/git-apply?utm_source=chatgpt.com "Git - git-apply Documentation"))|
|3|**rg / ripgrep**|Discovery/match counting|95|78|75|80|92|90|20|**Adopt**|Fast recursive search, respects `.gitignore`, skips hidden/binary files by default. Use for candidate discovery only, not final mutation. ([GitHub](https://github.com/BurntSushi/ripgrep?utm_source=chatgpt.com "GitHub - BurntSushi/ripgrep: ripgrep recursively searches directories ..."))|
|4|**yq `--front-matter=process`**|Frontmatter mutation|92|84|86|82|95|84|20|**Adopt**|Official yq docs support YAML frontmatter processing and show batch loops with `find`; limitation: only first passed file is processed, so loop explicitly. ([yq](https://mikefarah.gitbook.io/yq/usage/front-matter?utm_source=chatgpt.com "Front Matter \| yq - GitBook"))|
|5|**Claude Code hooks**|Enforcement|92|82|86|75|82|60|38|**Adopt after audit mode**|Official docs expose PreToolUse/PostToolUse/FileChanged/Stop and decision control; hooks enforce rules but are not a patcher. ([Claude](https://code.claude.com/docs/en/hooks?utm_source=chatgpt.com "Hooks reference - Claude Code Docs"))|
|6|**mdpatch / markdown-patch**|Markdown section backend|78|86|76|82|86|68|30|**Trial**|Structure-aware heading/block/frontmatter edits; available as CLI and JS/TS library. Needs fixture bakeoff for duplicate/nested headings and formatting preservation. ([GitHub](https://github.com/coddingtonbear/markdown-patch?utm_source=chatgpt.com "GitHub - coddingtonbear/markdown-patch: Make predictable, controllable ..."))|
|7|**remark / unified / mdast / heading-range**|V2 AST backend|88|78|80|82|70|45|42|**Trial later**|`mdast-util-heading-range` can replace content under a heading until next same/lower heading. Strong but heavier; stringify may reformat. ([npm](https://www.npmjs.com/package/mdast-util-heading-range?utm_source=chatgpt.com "mdast-util-heading-range - npm"))|
|8|**fixture runner**|Validation|86|82|88|80|85|76|18|**Adopt**|Existing toolkit already supports JSON fixture creation, command execution, and JSON-path assertions.|
|9|**comby**|Patternized structural edits|78|64|58|65|75|58|46|**Optional**|Good for code-like structures; less ideal for prose-heavy Markdown because Markdown heading semantics are better handled by mdpatch/mdast/custom parser. ([comby.dev](https://comby.dev/?utm_source=chatgpt.com "Comby · Structural code search and replace for ~every language."))|
|10|**sed**|Low-level wrapped utility|70|50|40|55|90|85|62|**Wrap only**|Safe only when executor verifies match count and diff. Do not let AI issue `sed -i` directly. Regex overreach is a known operational risk in mass text patching. ([mironsoft.de](https://www.mironsoft.de/blog/bash-textdateien-massenhaft-patchen-und-transformieren?utm_source=chatgpt.com "Textdateien massenhaft patchen und transformieren mit sed, awk und perl"))|
|11|**awk**|Table/field utility|70|55|45|60|88|76|58|**Wrap only**|Useful for Markdown table rows if row/key uniqueness is verified first. Not a first-class free agent mutation tool.|
|12|**perl**|Multi-line regex utility|68|52|42|58|88|70|66|**Wrap only**|Powerful but high blast radius. Use only inside executor with pre/post diff and exact scope checks.|
|13|**AI-authored unified diff**|Patch artifact|45|38|25|45|50|80|78|**Reject as primary**|Can be kept as emergency fallback only. It violates the premise that exact hunk context and line spans are unreliable.|
|14|**raw `patch --fuzz=3` flow**|Legacy fallback|45|35|30|45|55|78|72|**Reject as core**|Fuzz can make stale hunks apply too generously. Use git-generated patches from live mutation instead.|

# Failure-mode matrix

|scenario|CC path|GPT path|final merged architecture|
|---|---|---|---|
|simple_exact_span|Works if toolchain extracts span|Works if resolver has `replace_once`|**Pass**: extract live span, require one match.|
|wrong_line_numbers|Ignores line numbers if policy forbids them|Ignores line numbers by schema|**Pass**: line numbers are non-authoritative metadata only.|
|duplicate_heading|mdpatch may fail or pick wrong unless wrapped|Custom resolver can reject duplicates|**Pass**: require heading path + uniqueness; otherwise ambiguity report.|
|nested_heading_path|Needs mdpatch/mdast/custom path logic|Resolver can implement heading path|**Pass with heading-path resolver.**|
|paraphrased_anchor|`rg` alone insufficient|Resolver can score but must fail under threshold|**Fail safely** unless exact live span can be selected.|
|frontmatter_update|yq strong|Executor can call yq or parser|**Pass**: yq first-class for YAML frontmatter.|
|table_row_update|awk/comby possible but risky|Custom table resolver safer|**Trial**: implement row-key uniqueness, then mutate one row.|
|large_file_small_edit|Good with `rg` + section resolver|Good with live extraction|**Pass**: no full-file rewrite.|
|multi_file_patch_pack|Good with git scope validator|Good with policy allowlist|**Pass**: validate allowed files + cumulative diff.|
|bad_ai_patch|`git apply --check` rejects|Intent schema ignores raw diff|**Pass**: raw diff is ignored unless explicitly fallback.|
|formatting_preservation|mdpatch/mdast must be tested|span replacement preserves best|**Pass for span/frontmatter; trial for mdpatch.**|
|failed_validation_rollback|worktree/checkpoint handles|executor rollback handles|**Pass**: worktree discard or checkout allowed files.|

# Recommended final architecture

## Minimum viable architecture

```okf
architecture: deterministic_ai_patch_infrastructure.v1

decision:
  final_verdict: merge_and_simplify
  core: custom_gpt_style_intent_schema_plus_executor
  runtime: cc_style_toolchain_hooks_git_validation
  rejected_core:
    - ai_authored_unified_diff
    - ai_authored_exact_old_text
    - direct_write_edit_multiedit_on_protected_paths
    - direct_sed_i_perl_i_without_executor

phase_1_artifact:
  format: patch_intent.json
  reason: deterministic_parseability
  human_authoring_format_allowed: patch_intent.okf.md
  conversion_required_before_execution: true

phase_2_executor:
  required_file: patch_executor.py
  required_modes:
    - inspect
    - locate
    - extract_span
    - replace_once
    - replace_heading_section
    - frontmatter_set
    - table_row_update
    - validate_scope
    - diff
    - finalize

proof_layer:
  required:
    - git_status
    - git_diff
    - git_apply_check_for_generated_patches
    - fixture_runner
    - scope_allowlist
    - rollback_or_clean_worktree

enforcement_layer:
  initial_mode: audit_only_hooks
  final_mode: blocking_hooks
  block:
    - Write
    - Edit
    - MultiEdit
    - Bash_mutations_outside_executor
  allow:
    - rg
    - git status
    - git diff
    - executor commands
```

## Exact Phase 1 artifact schema

Use JSON for execution. OKF/YAML can exist as a human-readable planning wrapper, but the executor should consume JSON only.

```json
{
  "schema_version": "patch_intent.v1",
  "patch_id": "short-kebab-id",
  "allowed_paths": ["relative/path.md"],
  "operation": "replace_once | replace_heading_section | frontmatter_set | table_row_update | append_section | validate_only",
  "target": {
    "file_guess": "relative/path.md",
    "heading_path": ["H1 title", "H2 title"],
    "nearby_phrases": ["non-authoritative phrase"],
    "before_anchor": "optional non-authoritative phrase",
    "after_anchor": "optional non-authoritative phrase",
    "table": {
      "header_required": ["Column A", "Column B"],
      "row_key_column": "Name",
      "row_key_value": "Exact logical key"
    },
    "frontmatter_key": "status"
  },
  "replacement": {
    "new_text": "authoritative replacement content",
    "frontmatter_value": null
  },
  "validation": {
    "must_contain": ["string expected after change"],
    "must_not_contain": ["string not expected after change"],
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

## Exact Phase 2 deterministic pipeline

```okf
phase_2_pipeline:
  - step: preflight
    commands:
      - git status --porcelain
      - git rev-parse --show-toplevel
    gates:
      - repo_root_matches_policy
      - patch_targets_inside_allowed_paths

  - step: inspect
    action: executor reads live target files
    gates:
      - file_exists_or_create_allowed
      - protected_paths_respected

  - step: resolve_target
    action: executor computes exact span from live bytes
    gates:
      - no_match_fails
      - multiple_matches_fail
      - low_confidence_fails
      - duplicate_heading_fails_unless_heading_path_unique

  - step: mutate
    action: executor writes via temp file and atomic replace
    gates:
      - one_declared_operation_only
      - no_adjacent_cleanup
      - preserve_unrelated_bytes_where_possible

  - step: prove
    commands:
      - git diff -- <allowed paths>
    gates:
      - diff_non_empty_for_mutation
      - changed_files_equal_or_subset_allowed_paths

  - step: validate
    commands:
      - declared fixture commands
      - frontmatter parse checks
      - markdown structure checks
      - optional lint only if scoped
    gates:
      - all_declared_checks_pass

  - step: finalize
    action: generate final report and optional git-generated patch pack
    gates:
      - git_apply_check_passes_if_patch_pack_created
      - rollback_on_failure
      - no_push_unless_explicit
```

## Optional later additions

|addition|when to add|
|---|---|
|mdpatch backend|After fixture bakeoff passes duplicate/nested heading, code fence, CRLF, frontmatter, no-trailing-newline tests.|
|remark/mdast backend|If mdpatch fails or complex AST transformations become common.|
|generated Markdown from structured store|Only for high-volume recurring KB state where prose patching remains frequent.|
|markdownlint / remark-lint|Only when baseline corpus is lint-clean or rules are scoped to changed files.|
|comby|Only for repeated code-like transformations, not general Markdown prose.|

# Implementation prompt for Codex/Claude Code

```okf
prompt_type: deterministic_execution_build
role: deterministic_execution_orchestrator

repo: leela-spec/apexai-os-meta
branch: main
work_policy:
  work_directly_on: main
  do_not_create_branch: true
  do_not_open_pr: true
  commit_and_push: true

target_files:
  - apex-meta/SmallSkills/Patching/patch_executor.py
  - apex-meta/SmallSkills/Patching/patch_policy.json
  - apex-meta/SmallSkills/Patching/fixture_runner.py
  - apex-meta/SmallSkills/Patching/hooks/pre_tool_use.py
  - apex-meta/SmallSkills/Patching/hooks/post_tool_use_or_file_changed.py
  - apex-meta/SmallSkills/Patching/fixtures/README.md

task:
  - Build minimal deterministic Markdown/config patch executor.
  - Do not build a broad framework.
  - Do not read unrelated files.
  - Reuse patterns from existing stub_repair_toolkit.py where helpful.
  - Executor must accept patch_intent.json.
  - Executor must support:
      - inspect
      - locate
      - extract-span
      - replace-once
      - replace-heading-section
      - frontmatter-set
      - table-row-update
      - validate-scope
      - diff
      - finalize
  - Executor must refuse:
      - target path outside allowlist
      - zero target matches
      - multiple target matches
      - ambiguous duplicate headings
      - full-file rewrite unless allow_full_file_rewrite is true
      - direct old_text supplied by AI unless extracted from live file
  - Git diff is proof.
  - AI-authored unified diffs are not accepted as primary input.
  - Hooks must block Write/Edit/MultiEdit and dangerous Bash mutations on protected paths unless command invokes patch_executor.py.

commands:
  - git checkout main
  - git pull --ff-only origin main
  - python -m py_compile apex-meta/SmallSkills/Patching/patch_executor.py apex-meta/SmallSkills/Patching/fixture_runner.py apex-meta/SmallSkills/Patching/hooks/pre_tool_use.py apex-meta/SmallSkills/Patching/hooks/post_tool_use_or_file_changed.py
  - python apex-meta/SmallSkills/Patching/patch_executor.py --self-test
  - python apex-meta/SmallSkills/Patching/fixture_runner.py --self-test
  - git diff -- apex-meta/SmallSkills/Patching

expected_result:
  - compile passes
  - self-tests pass
  - fixtures cover replace-once, duplicate heading rejection, frontmatter-set, table-row-update, scope rejection
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

# Final verdict

**Adopt a merged, simplified architecture:** GPT path for the strict `patch_intent.json` + deterministic resolver/finalizer; CC path for execution tooling, hooks, git proof, and local enforcement.

The smallest reliable system is not a large planner contract stack. It is: **one intent schema, one executor, one policy file, one fixture runner, git proof, and hooks that block direct mutation.** `mdpatch`, `yq`, `rg`, and git should be tools behind the executor, not free tools the model calls directly. This satisfies the hard requirement: Phase 1 can be wrong about exact old text, while Phase 2 still either resolves one exact live target or fails safely.