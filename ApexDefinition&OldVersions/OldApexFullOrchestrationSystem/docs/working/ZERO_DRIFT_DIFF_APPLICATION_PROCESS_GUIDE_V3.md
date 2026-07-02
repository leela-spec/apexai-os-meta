---
process_id: zero_drift_diff_application_v3
status: connector_only_working_process_guide
owner: meta_ops
validator: meta_detective
secondary_validator: special_ops__hygiene_clean
created_from_run:
  repo: leela-spec/MasterOfArts
  base_branch: main
  work_branch: patch/meta-detective-internal-modes-appendix-doctrine
  source_instruction_file: Unifeid diffs & validation.md
  run_type: unified_diff_application_experiment
  goal: apply uploaded unified diffs with no unintended information drift
execution_environment:
  mode: ChatGPT_browser_with_GitHub_connector_only
truth_model:
  source_of_intended_change: uploaded_unified_diff_file
  base_truth: current_main_target_files
  result_truth: branch_files_after_patch
  validation_equation: branch_file == main_file + intended_diff
  disallowed_truth_sources:
    - model_memory
    - inferred_improvements
    - local_git_checkout
    - local_shell_commands
    - git_apply
    - offline_repo_clone
    - stylistic rewriting
    - unrelated_repo_state
    - broad_architecture_interpretation
required_outputs:
  - branch_created_from_main
  - one_commit_per_target_file
  - touched_file_inventory
  - per_file_validation_note
  - final_compare_against_main
  - deviation_log
  - unresolved_risks
hard_guardrails:
  - no_patch_without_exact_target_file
  - no_rewrite_when_diff_is_sufficient
  - one_file_at_a_time
  - validate_file_before_next_file
  - never_apply_noop_hunks
  - record_intentional_deviations
  - do_not_mutate_config_unless_diff_explicitly_targets_config
  - do_not_create_new_agents_unless_diff_explicitly_targets_agent_creation
  - do_not_create_new_kb_roots_unless_diff_explicitly_targets_kb_root_creation
  - do_not_absorb_hygiene_into_detective
  - do_not_change_execution_authority
  - do_not_write_outside_target_repo
  - do_not_use_local_git_checkout
  - do_not_use_local_shell_commands
  - do_not_use_git_apply
  - do_not_describe_local_or_offline_alternatives
success_criteria:
  - branch_ahead_of_main
  - branch_not_behind_main_at_creation_time
  - final_changed_files_equal_expected_target_files_plus_intentional_process_artifacts_if_added
  - per_file_add_delete_counts_are_consistent_with_expected_hunk_scale
  - no_unlisted_file_changes
  - no_unexplained_semantic_changes
  - deviations_are_documented_and_source_justified
failure_conditions:
  - target_file_not_found_and_no_explicit_fallback
  - patch_requires_guessing_intent
  - source_diff_contains_ambiguous_or_conflicting_instructions
  - branch_compare_shows_unexpected_files
  - model_rewrites_file_beyond_diff_scope
  - validation_relies_on_confidence_instead_of_compare_or_content_check
  - no_op_hunk_applied_as_change
  - numbering_or_format_correction_made_without_being_recorded_as_intentional_deviation
  - any_step_introduces_local_git_checkout
  - any_step_introduces_git_apply
  - any_step_introduces_offline_repo_clone
---

> Scope rule: This guide describes the ChatGPT browser + GitHub connector workflow only.
> It does not describe local Git, local shell, `git apply`, offline repo clones, or any workflow outside the connector actions named here.
> Any future agent using this guide must not introduce local/offline alternatives.

# Zero-Drift Unified Diff Application Process Guide V3

## 1. Purpose

This guide captures the connector-only process used to apply uploaded unified-diff instruction files to `leela-spec/MasterOfArts` without introducing drift.

The core process is not "rewrite the files." The process is:

```yaml
main_file + intended_diff = branch_file
```

Any content not required by the intended diff is drift unless explicitly justified as a source-instruction correction.

---

## 2. Machine-readable connector run template

```yaml
run_template:
  inputs:
    repo_full_name: "owner/repo"
    base_branch: "main"
    work_branch: "patch/<specific-topic>"
    source_instruction_file: "<uploaded diff or patchspec>"
    expected_target_files: []
    explicit_corrections_from_source: []
  preflight:
    - confirm_GitHub_connector_access
    - identify_current_main_sha_through_GitHub_connector
    - create_branch_from_current_main_sha
    - parse_source_instruction_file
    - build_expected_target_file_allowlist
    - extract_guardrails_from_user_request
    - extract_corrections_from_source_instruction_file
  per_file_loop:
    for_each_target_file:
      - fetch_file_from_work_branch_through_GitHub_connector
      - compare_against_expected_source_context
      - apply_only_intended_hunk_to_fetched_content
      - skip_noop_hunks
      - if_needed_apply_explicit_source_correction
      - update_exactly_one_file_on_work_branch_through_GitHub_connector
      - compare_work_branch_against_main_through_GitHub_connector
      - verify_current_changed_file_inventory_equals_expected_cumulative_allowlist
      - record_commit_sha
      - record_additions_deletions
      - record_deviation_or_none
  final_validation:
    - compare_work_branch_against_main_through_GitHub_connector
    - verify_touched_file_inventory
    - verify_no_unexpected_created_deleted_renamed_files
    - verify_expected_deviations_only
    - report_unresolved_risks
  stop_rule:
    - stop_before_merge_unless_user_explicitly_requests_merge
```

---

## 3. What worked in this run

```yaml
worked:
  branch_creation:
    result: pass
    mechanics:
      - identified current main state through GitHub connector
      - created a dedicated branch from that exact SHA
    value: avoided ambiguous branch base and protected main
  one_file_at_a_time:
    result: pass
    mechanics:
      - fetched each target file from the branch through GitHub connector
      - updated exactly one file per commit through GitHub connector
      - compared branch to main after each file or small checkpoint
    value: made drift visible immediately
  source_correction_handling:
    result: pass
    examples:
      - skipped no-op MISTAKES.md hunk
      - fixed META_HEADS_KB_BASE_BUILD_INDEX.md numbering instead of leaving known offset
    value: separated mechanical patching from documented intentional deviations
  final_compare:
    result: pass
    mechanics:
      - compared branch against main through GitHub connector
      - reported all touched files and add/delete counts
    value: confirmed no unexpected file surfaces changed
  authority_guardrails:
    result: pass
    protected_boundaries:
      - no config mutation
      - no new agents
      - no new KB roots
      - no Hygiene absorption
      - no Detective execution authority change
```

---

## 4. Specific mechanics used

```yaml
mechanics_used:
  repo_access:
    tool: GitHub_connector
    actions:
      - get_repo
      - compare_commits
      - create_branch
      - fetch_file
      - update_file
      - create_file
      - create_pull_request
      - merge_pull_request
      - get_pr_info
  branch_strategy:
    base: current main SHA identified through GitHub connector metadata
    branch_name: patch/meta-detective-internal-modes-appendix-doctrine
    commit_strategy: one commit per patched target file
  patch_strategy:
    approach: connector-only full-file update built from fetched branch file plus intended diff hunk
    reason: GitHub connector update_file requires complete replacement content
    safeguards:
      - fetched branch file before each update
      - changed only diff-targeted regions
      - preserved surrounding content verbatim
      - used final compare to detect unexpected touched files
      - did_not_use_local_git
      - did_not_use_git_apply
      - did_not_use_local_shell
      - did_not_clone_repo
  validation_strategy:
    per_file:
      - inspect changed file inventory after update
      - compare additions/deletions against expected hunk scale
      - record special deviations
    final:
      - branch_vs_main compare through GitHub connector
      - touched file inventory
      - no added/deleted/renamed file check
```

---

## 5. Instructions used

```yaml
instructions_used:
  user_instructions:
    - create a branch
    - patch all target files using the unified diff from the attached file
    - validate against original main target files
    - ensure not a single unintended information change is introduced
    - validate one file at a time
    - create clear guardrails because new models introduce drift
    - move the validated branch state into main through Git, not by rewriting files on main
    - make the guide describe this exact ChatGPT browser plus GitHub connector process only
  source_file_instructions:
    - APPENDIX_INTERNAL_MODES.md required no diff
    - ESSENCE.md should point to appendix doctrine
    - BEST_PRACTICES.md should use appendix as durable mode-selection doctrine
    - MISTAKES.md first hunk only; remove no-op hunk before final patch
    - TEMPLATES.md should point to appendix doctrine
    - LEARNING_QUEUE.md should convert internal modes candidate into promoted trace
    - AGENT_KB_INDEX.md should make appendix discoverable
    - CROSS_REFERENCE_MANIFEST.md should add appendix as durable accepted reference
    - META_HEADS_KB_BASE_BUILD_INDEX.md should add appendix and resolve numbering caveat
  implicit_repo_governance_preserved:
    - working files are not canon by storage alone
    - learning queue is not runtime truth
    - Detective validates/challenges but does not execute
    - Hygiene remains separate structural QA
    - accepted appendix does not create separate agent or KB root
```

---

## 6. Mistakes and near-mistakes observed

```yaml
mistakes_or_near_mistakes:
  invalid_pr_patch_fetch:
    what_happened: attempted to fetch a PR file patch with pr_number 0
    impact: harmless API error; no repo mutation
    cause: looking for a patch-level validation path before a PR existed
    prevention:
      - do not call PR-only endpoints before PR creation
      - use compare_commits for branch validation when no PR exists
  manual_full_content_update_risk:
    what_happened: GitHub connector update_file required complete replacement content
    impact: increased risk of accidental rewrite drift
    cause: connector API writes whole file content even when only one hunk changes
    prevention:
      - fetch exact branch file before update
      - construct replacement content only from fetched file plus intended hunk
      - preserve all non-targeted lines verbatim
      - validate changed-file inventory and add/delete scale after every file
  no_line_level_machine_diff_validation:
    what_happened: validation used compare summaries and intentional scope reasoning, not a generated expected-file line comparison for every file
    impact: strong but not complete proof of line-for-line intended result
    cause: expected-output comparison was not performed for every target file in this connector-only run
    prevention:
      - fetch original main target file through GitHub connector
      - construct expected target file from original main file plus intended diff hunk
      - fetch actual branch file through GitHub connector
      - compare expected content against actual branch content line by line
      - record match or first differing line
  source_instruction_typo:
    what_happened: uploaded file name used `Unifeid` instead of `Unified`
    impact: none
    cause: source artifact typo
    prevention:
      - preserve source filename as-is in provenance
      - do not silently rename provenance references
  local_workflow_ambiguity_in_prior_guide:
    what_happened: prior guide mentioned local checkout and git apply as optional future alternatives
    impact: confused another agent about the actual browser plus GitHub connector process
    cause: guide included process alternatives outside the actual execution environment
    prevention:
      - V3 forbids local Git checkout, local shell, git apply, and offline repo clone references
      - V3 documents only connector actions actually available in this workflow
```

---

## 7. Where deviation was needed

```yaml
intentional_deviations:
  - id: skip_mistakes_noop_hunk
    source_basis: source instruction explicitly said second MISTAKES.md hunk was unnecessary/no-op
    action_taken: applied only the real appendix pointer hunk
    why_not_drift: deviation prevented a meaningless context-only patch artifact
  - id: fully_renumber_meta_detective_source_index
    source_basis: source instruction said partial numbering was visually sloppy and recommended regenerating full numbering or auto-numbering
    action_taken: fully renumbered the meta_detective list after inserting appendix and validation report entries
    why_not_drift: formatting correction was explicitly required by source caveat and did not alter source meanings beyond intended insertion/reclassification
  - id: create_process_guide
    source_basis: follow-up user requested a machine-readable process guide from this flow
    action_taken: added the process guide as a working document
    why_not_drift: separate requested artifact; not part of original diff application
  - id: create_connector_only_v3
    source_basis: user identified local/offline alternatives as process drift
    action_taken: created V3 as connector-only guide
    why_not_drift: removes ambiguity from prior guide and constrains future agents to the actual environment
```

---

## 8. What was not fully understood or not fully proven

```yaml
not_fully_understood_or_proven:
  byte_level_equivalence:
    status: not_fully_proven
    reason: no independent expected-output line comparison was generated for every patched file
    required_for_full_proof:
      - fetch original main target file through GitHub connector
      - construct expected target file from original main file plus intended diff hunk
      - fetch actual branch file through GitHub connector
      - compare expected content against actual branch content line by line
      - record match or first differing line
  appendix_preexistence:
    status: assumed_from_source_and_repo_context
    reason: source diff said no diff needed for APPENDIX_INTERNAL_MODES.md, but this run did not separately open and validate appendix content before patching references
    required_for_full_proof:
      - fetch appendix on main through GitHub connector
      - confirm it contains accepted appendix doctrine
      - record validation result
  semantic_non_drift:
    status: strongly_constrained_not_formally_proven
    reason: final compare shows intended touched files, but semantic drift requires line-by-line review against source patch
    required_for_full_proof:
      - produce connector-side expected post-patch content per target file
      - compare actual branch file content against expected post-patch content
      - flag all extra lines
  github_ci_state:
    status: not_checked
    reason: no CI statuses were used as a required validation gate for this doc-only process
    required_for_full_proof:
      - inspect GitHub connector status/check data if repo has relevant checks
```

---

## 9. How problems could have been prevented

```yaml
prevention_rules:
  make_connector_patch_application_deterministic:
    - treat uploaded diff as source_of_intended_change
    - create branch from exact current main SHA through GitHub connector
    - fetch target file from branch before every update
    - construct replacement content only from fetched file plus intended hunk
    - never reconstruct whole files from memory
    - never introduce local Git or git apply steps
  improve_validation:
    - generate expected post-patch content from fetched main file plus intended hunk
    - fetch actual branch file after update
    - compare expected content to actual branch content
    - record first differing line if any
    - save validation notes in the run report or validation manifest
  reduce_api_endpoint_errors:
    - use compare_commits before PR exists
    - use PR diff endpoints only after create_pull_request
  prevent_list_numbering_drift:
    - prefer repeated `1.` markdown numbering for long source indexes
    - or require full-section renumbering whenever inserting numbered entries
  prevent_agent_overreach:
    - state disallowed changes before first patch
    - keep a touched-file allowlist
    - treat every non-allowlisted file as failure
    - require explicit deviation records
  prevent_hidden_semantic_rewriting:
    - never paraphrase existing text outside diff hunks
    - preserve exact whitespace and punctuation outside modified blocks when possible
    - if complete file replacement API is used, only generate from fetched content plus patch transformations
  prevent_environment_drift:
    - do not mention local Git checkout
    - do not mention local shell commands
    - do not mention git apply
    - do not mention offline repo clones
    - do not provide alternate workflows outside the GitHub connector process
```

---

## 10. Required connector-only implementation pattern

```yaml
future_process:
  connector_only_path:
    - identify current main SHA through GitHub connector
    - create work branch from exact main SHA
    - parse uploaded diff artifacts into target file allowlist
    - for each target file, fetch the file from the work branch
    - apply only the intended hunk to the fetched content
    - update exactly one target file through GitHub connector update_file
    - commit exactly one target file per update_file call
    - compare work branch against main after every file
    - verify changed files equal expected cumulative allowlist
    - record add/delete counts and deviations
    - repeat until all target files are patched
    - run final compare_commits main...work_branch
    - report branch name, commit SHAs, touched files, deviations, and unresolved risks
    - stop before merge unless user explicitly requests merge
  required_validation_manifest_schema:
    file_validation:
      path: string
      source_hunks_applied: []
      skipped_hunks: []
      intentional_deviations: []
      github_connector_action: fetch_file + update_file + compare_commits
      commit_sha: string
      additions: integer
      deletions: integer
      expected_status: modified | added | deleted
      validation_status: pass | fail | partial
      first_unexpected_difference: string | null
      unresolved_risk: string | null
```

---

## 11. Minimum checklist for future agents

```yaml
minimum_checklist:
  before_patching:
    - identify current main SHA through GitHub connector
    - create dedicated branch through GitHub connector
    - parse target file list from diff
    - create allowlist of target files
    - identify source-stated corrections or caveats
    - confirm no local/offline process is being introduced
  during_patching:
    - fetch one file from work branch through GitHub connector
    - apply only its intended diff to fetched content
    - update exactly one file through GitHub connector
    - compare branch against main through GitHub connector
    - verify no unexpected file touched
    - record result
  after_patching:
    - final compare branch against main through GitHub connector
    - report touched files and counts
    - report deviations
    - report mistakes and unproven assumptions
    - do not claim line-perfect proof unless expected-vs-actual content comparison was performed
```

---

## 12. Verdict for this process

```yaml
process_verdict:
  useful_for_future: true
  drift_resistance: high
  environment_scope: ChatGPT_browser_with_GitHub_connector_only
  strongest_parts:
    - one_file_at_a_time
    - exact branch compare
    - target file allowlist
    - explicit deviation log
    - no-op hunk rejection
    - connector-only scope
  weakest_parts:
    - manual full-content update through GitHub connector API
    - no independent connector-side expected-output line comparison for every file
    - no PR UI review unless explicitly requested
  recommendation: use this connector-only workflow for ChatGPT browser plus GitHub connector patch runs; do not add local Git alternatives
```

---

## 13. Final step — move validated branch state into `main` via GitHub connector

```yaml
v3_final_step:
  name: move_validated_branch_state_to_main_without_drift
  purpose: Move the already-validated branch tree into `main` without rewriting target files.
  applies_after:
    - branch files have already been validated as the correct target versions
    - validation equation has passed: branch_file == original_main_file + intended_unified_diff
    - the remaining task is repo update, not patch application
  core_rule: Use GitHub PR merge to move the validated commit/tree; do not write target files again.
  forbidden_actions:
    - do_not_fetch_branch_files_and_rewrite_them_into_main
    - do_not_recreate_target_files_from_memory
    - do_not_apply_the_unified_diff_a_second_time_directly_to_main
    - do_not_use_update_file_for_each_target_file_on_main
    - do_not_merge_if_branch_head_changed_after_validation
    - do_not_resolve_merge_conflicts_by_model_rewriting_files
    - do_not_use_local_git_checkout
    - do_not_use_local_shell
    - do_not_use_git_apply
    - do_not_describe_local_or_offline_alternatives
  required_inputs:
    repository_full_name: owner/repo
    validated_branch: branch_name
    target_branch: main
    validated_head_sha: exact_commit_sha_of_validated_branch_state
    expected_changed_files: allowlisted_changed_file_inventory
  deterministic_github_connector_protocol:
    - compare target_branch against validated_branch
    - require compare result to show the validated branch state and expected changed-file inventory
    - create pull request from validated_branch into target_branch
    - fetch pull request metadata
    - require pull_request.head_sha == validated_head_sha
    - require pull_request.mergeable == true
    - merge pull request with expected_head_sha == validated_head_sha
    - confirm merge result reports merged == true
    - confirm pull request is closed and merged
  why_this_is_drift_free:
    - GitHub moves immutable commit/tree objects instead of asking the model to regenerate file content
    - expected_head_sha prevents merging a branch that changed after validation
    - no target file content is rewritten by the model during the main update step
    - if GitHub cannot merge cleanly, the process stops instead of inventing a resolution
```

### 13.1 GitHub connector implementation

```yaml
github_connector_implementation:
  step_1_pre_merge_compare:
    action: compare_commits
    args:
      repo_full_name: owner/repo
      base: main
      head: <validated_branch>
    pass_conditions:
      - behind_by == 0
      - files == expected_changed_files
      - no unexpected added/deleted/renamed/modified files
  step_2_create_pr:
    action: create_pull_request
    args:
      repository_full_name: owner/repo
      head_branch: <validated_branch>
      base_branch: main
      title: Move validated branch state into main
      body: include validated_head_sha, scope, and no-rewrite guardrails
  step_3_confirm_pr:
    action: get_pr_info
    pass_conditions:
      - head_sha == <validated_head_sha>
      - mergeable == true
      - changed_files == expected_changed_file_count
  step_4_merge_pr:
    action: merge_pull_request
    args:
      repository_full_name: owner/repo
      pr_number: <pr_number>
      merge_method: merge
      expected_head_sha: <validated_head_sha>
    pass_conditions:
      - merged == true
      - sha is present
  step_5_post_merge_confirmation:
    action: get_pr_info
    pass_conditions:
      - state == closed
      - merged == true
      - merged_at is present
      - merge_commit_sha is present
      - no_target_file_update_file_calls_were_made_on_main
```

### 13.2 Actual run example from this process

```yaml
actual_git_move_run:
  repository_full_name: leela-spec/MasterOfArts
  validated_branch: patch/meta-detective-internal-modes-appendix-doctrine
  target_branch: main
  validated_head_sha: a621ba966ca986bd80b0d98ef5529a10603c4bb8
  pull_request: 1
  merge_method: merge
  expected_head_sha_used: a621ba966ca986bd80b0d98ef5529a10603c4bb8
  merge_result:
    merged: true
    merge_commit_sha: 6ba7351bcc2c72cbe2d495cfbeea0f0c58d336e6
  post_merge_sample_validation:
    sampled_files_checked_on_main: 5
    sampled_changes_landed: true
```

### 13.3 Stop conditions

```yaml
main_update_stop_conditions:
  - compare shows unexpected file changes
  - branch is behind main in a way that requires conflict resolution
  - PR head SHA differs from validated_head_sha
  - PR is not mergeable
  - GitHub rejects expected_head_sha
  - merge would require manual conflict resolution
  - any step tempts the agent to rewrite files directly on main
  - any step introduces local Git checkout
  - any step introduces git apply
  - any step introduces an offline alternative process
```

### 13.4 Post-merge landed-change validation

```yaml
post_merge_validation:
  purpose: Confirm that the GitHub connector PR merge landed on main.
  method:
    - fetch selected files from main through GitHub connector
    - check for concrete expected changes in different files
    - report pass/fail per file
  note: This validates that the merge landed; it does not reapply or regenerate the patch.
  example_from_run:
    checks:
      - ESSENCE.md contained appendix doctrine pointer
      - BEST_PRACTICES.md contained durable doctrine pointer
      - LEARNING_QUEUE.md showed internal modes pack as promoted
      - AGENT_KB_INDEX.md exposed appendix as accepted doctrine
      - CROSS_REFERENCE_MANIFEST.md added appendix working references
    result: all sampled changes landed
```

### 13.5 V3 boundary

```yaml
v3_boundary:
  supersedes:
    - ZERO_DRIFT_DIFF_APPLICATION_PROCESS_GUIDE_V2.md
  removed_ambiguity:
    - local_git_checkout
    - local_shell_commands
    - git_apply
    - offline_repo_clone
    - optional_local_or_offline_alternatives
  allowed_process_surface:
    - ChatGPT_browser
    - GitHub_connector
    - GitHub_online_repo
  drift_check_rule: Compare V3 against V2; all changes must remove ambiguity or local/offline alternatives, or add connector-only main-update guardrails.
```
