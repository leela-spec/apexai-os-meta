---
process_id: zero_drift_diff_application_v1
status: working_process_guide
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
truth_model:
  source_of_intended_change: uploaded_unified_diff_file
  base_truth: current_main_target_files
  result_truth: branch_files_after_patch
  validation_equation: branch_file == main_file + intended_diff
  disallowed_truth_sources:
    - model_memory
    - inferred_improvements
    - stylistic rewriting
    - unrelated repo state
    - broad architecture interpretation
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
success_criteria:
  - branch_ahead_of_main
  - branch_not_behind_main_at_creation_time
  - final_changed_files_equal_expected_target_files_plus_intentional_process_guide_if_added
  - per_file_add_delete_counts_are_consistent_with_expected_hunk_scale
  - no_unlisted_file_changes
  - no_unexplained_semantic_changes
  - deviations_are_documented_and_source_justified
failure_conditions:
  - target_file_not_found_and_no_explicit_fallback
  - patch_requires_guessing_intent
  - source_diff_contains_ambiguous_or_conflicting instructions
  - branch_compare_shows_unexpected_files
  - model_rewrites_file_beyond_diff_scope
  - validation_relies_on_confidence_instead_of_compare_or content check
  - no_op_hunk_applied_as_change
  - numbering_or_format_correction_made_without being recorded as intentional deviation
---

# Zero-Drift Unified Diff Application Process Guide

## 1. Purpose

This guide captures the process used to apply the uploaded unified-diff instruction file to `leela-spec/MasterOfArts` without introducing drift.

The core process is not “rewrite the files.” The process is:

```yaml
main_file + intended_diff = branch_file
```

Any content not required by the intended diff is treated as drift unless explicitly justified as a source-instruction correction.

---

## 2. Machine-readable run template

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
    - confirm_repo_access
    - fetch_or_identify_current_main_sha
    - create_branch_from_main_sha
    - parse_source_instruction_file
    - build_expected_target_file_list
    - extract_guardrails_from_user_request
    - extract_corrections_from_source_instruction_file
  per_file_loop:
    for_each_target_file:
      - fetch_file_from_work_branch
      - compare_against_expected_source_context
      - apply_only_intended_hunks
      - skip_noop_hunks
      - if_needed_apply_explicit_source_correction
      - update_file_on_branch
      - compare_branch_to_main
      - verify_current_file_is_only_expected_new_or_modified_file_since_last_step
      - record_commit_sha
      - record_additions_deletions
      - record_deviation_or_none
  final_validation:
    - compare_work_branch_against_main
    - verify_touched_file_inventory
    - verify_no_unexpected_created_deleted_renamed_files
    - verify_expected_deviations_only
    - report_unresolved_risks
```

---

## 3. What worked in this run

```yaml
worked:
  branch_creation:
    result: pass
    mechanics:
      - compared main to itself to identify current base commit
      - created a dedicated branch from that exact SHA
    value: avoided ambiguous branch base and protected main
  one_file_at_a_time:
    result: pass
    mechanics:
      - fetched each target file from the branch
      - updated exactly one file per commit
      - compared branch to main after each small batch or file
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
      - compared branch against main
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
    tool: GitHub connector
    actions:
      - get_repo
      - compare_commits
      - create_branch
      - fetch_file
      - update_file
      - create_file
  branch_strategy:
    base: current main SHA
    branch_name: patch/meta-detective-internal-modes-appendix-doctrine
    commit_strategy: one commit per patched target file
  patch_strategy:
    approach: manual reconstruction of exact intended post-patch content
    reason: connector provided file update API, not local git apply
    safeguards:
      - fetched branch file before each update
      - changed only diff-targeted regions
      - preserved surrounding content verbatim
      - used final compare to detect unexpected touched files
  validation_strategy:
    per_file:
      - inspect changed file count after update
      - compare additions/deletions against expected hunk scale
      - record special deviations
    final:
      - branch_vs_main compare
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
    what_happened: connector update_file required complete replacement content
    impact: increased risk of accidental rewrite drift
    cause: no direct git apply endpoint in connector workflow
    prevention:
      - prefer local git apply when available
      - otherwise fetch exact file and edit only targeted regions
      - validate add/delete counts after every file
  no_line_level_machine_diff_validation:
    what_happened: validation used compare summaries and intentional scope reasoning, not a generated expected-file hash for every file
    impact: strong but not mathematically complete proof of byte-for-byte intended result
    cause: no local checkout/hash pipeline used in this run
    prevention:
      - create expected post-patch files locally
      - compute hashes for expected vs branch result
      - only then report 100 percent byte-level correctness
  source_instruction_typo:
    what_happened: uploaded file name used `Unifeid` instead of `Unified`
    impact: none
    cause: source artifact typo
    prevention:
      - preserve source filename as-is in provenance
      - do not silently rename provenance references
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
    action_taken: added this guide as a new working document on the same branch
    why_not_drift: separate requested artifact; not part of original diff application
```

---

## 8. What was not fully understood or not fully proven

```yaml
not_fully_understood_or_proven:
  byte_level_equivalence:
    status: not_fully_proven
    reason: no independent expected-output hash was generated for each patched file
    required_for_full_proof:
      - local checkout of main
      - apply source diff or scripted expected transformation
      - fetch branch files
      - normalize line endings only if policy allows
      - compare SHA256 expected vs actual
  appendix_preexistence:
    status: assumed_from_source_and_repo_context
    reason: source diff said no diff needed for APPENDIX_INTERNAL_MODES.md, but this run did not separately open and validate appendix content before patching references
    required_for_full_proof:
      - fetch appendix on main
      - confirm it contains accepted appendix doctrine
      - cite or record validation result
  semantic_non_drift:
    status: strongly_constrained_not_formally_proven
    reason: final compare shows intended touched files, but semantic drift requires line-by-line review against source patch
    required_for_full_proof:
      - produce expected unified patch artifact
      - compare actual branch patch against expected patch
      - flag all extra lines
  github_ui_or_ci_state:
    status: not_checked
    reason: no PR was created and CI was not inspected
    required_for_full_proof:
      - open PR
      - inspect generated diff in PR UI
      - run or inspect CI if repository has relevant checks
```

---

## 9. How problems could have been prevented

```yaml
prevention_rules:
  make_patch_apply_deterministic:
    - store the uploaded patch as a repo artifact or local file
    - run git apply --check before mutation when local checkout is available
    - use git apply --3way or --recount only when explicitly allowed
    - never hand-rewrite full files if direct patch apply is possible
  improve_validation:
    - generate expected post-patch files from main plus diff
    - compute per-file hashes
    - compare actual branch files to expected hashes
    - save validation manifest in repo
  reduce_api_endpoint_errors:
    - use compare_commits before PR exists
    - use PR diff endpoints only after create_pull_request
  prevent list_numbering_drift:
    - prefer repeated `1.` markdown list numbering for long source indexes
    - or require full-section renumbering whenever inserting numbered entries
  prevent model_overreach:
    - state disallowed changes before first patch
    - keep a touched-file allowlist
    - treat every non-allowlisted file as failure
    - require explicit deviation records
  prevent hidden semantic rewriting:
    - never paraphrase existing text outside diff hunks
    - preserve exact whitespace and punctuation outside modified blocks when possible
    - if complete file replacement API is used, only generate from fetched content plus patch transformations
```

---

## 10. Recommended future implementation pattern

```yaml
future_process:
  preferred_path_with_local_checkout:
    - checkout main
    - create branch
    - save uploaded diff as patch file
    - run git apply --check patchfile
    - if check passes, apply one file at a time
    - commit each file separately
    - after each commit run git diff main -- path
    - compare actual file patch to expected hunk
    - run final git diff --stat main...branch
    - create validation manifest
  fallback_path_with_github_connector_only:
    - create branch from exact main SHA
    - fetch target file from branch
    - produce patched content by applying only target hunk
    - update one file
    - compare branch to main
    - record changed file count and add/delete stats
    - repeat
    - run final compare
    - optionally create PR for reviewable patch UI
  required_validation_manifest_schema:
    file_validation:
      path: string
      source_hunks_applied: []
      skipped_hunks: []
      intentional_deviations: []
      commit_sha: string
      additions: integer
      deletions: integer
      expected_status: modified | added | deleted
      validation_status: pass | fail | partial
      unresolved_risk: string | null
```

---

## 11. Minimum checklist for future agents

```yaml
minimum_checklist:
  before_patching:
    - identify base branch and exact base sha
    - create dedicated branch
    - parse target file list from diff
    - create allowlist of target files
    - identify source-stated corrections or caveats
  during_patching:
    - fetch one file
    - apply only its intended diff
    - commit one file
    - compare branch against main
    - verify no unexpected file touched
    - record result
  after_patching:
    - final compare branch against main
    - report touched files and counts
    - report deviations
    - report mistakes and unproven assumptions
    - do not claim byte-perfect proof unless hashes or patch-equivalence checks were performed
```

---

## 12. Verdict for this process

```yaml
process_verdict:
  useful_for_future: true
  drift_resistance: high
  strongest_parts:
    - one_file_at_a_time
    - exact branch compare
    - target file allowlist
    - explicit deviation log
    - no-op hunk rejection
  weakest_parts:
    - manual full-content update through API
    - no independent expected-output hash
    - no PR UI review
  recommendation: use as fallback workflow when Codex/local tokens are unavailable, but improve with hash-based expected-output validation when possible
```

---

## 13. V2 final step — move validated branch state into `main` via Git

```yaml
v2_final_step:
  name: move_validated_branch_state_to_main_without_drift
  purpose: Move the already-validated branch tree into `main` without rewriting target files.
  applies_after:
    - branch files have already been validated as the correct target versions
    - validation equation has passed: branch_file == original_main_file + intended_unified_diff
    - the remaining task is repo update, not patch application
  core_rule: Use Git to move the validated commit/tree; do not write target files again.
  forbidden_actions:
    - do_not_fetch_branch_files_and_rewrite_them_into_main
    - do_not_recreate_target_files_from_memory
    - do_not_apply_the_unified_diff_a_second_time_directly_to_main
    - do_not_use_update_file_for_each_target_file_on_main
    - do_not_merge_if_branch_head_changed_after_validation
    - do_not_resolve_merge_conflicts_by_model_rewriting_files
  required_inputs:
    repository_full_name: owner/repo
    validated_branch: branch_name
    target_branch: main
    validated_head_sha: exact_commit_sha_of_validated_branch_state
    expected_changed_files: allowlisted_changed_file_inventory
  deterministic_git_protocol:
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
    - Git moves immutable commit/tree objects instead of asking the model to regenerate file content
    - expected_head_sha prevents merging a branch that changed after validation
    - no target file content is rewritten by the model during the main update step
    - if Git cannot merge cleanly, the process stops instead of inventing a resolution
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
```

### 13.4 Post-merge landed-change validation

```yaml
post_merge_validation:
  purpose: Confirm that the Git object move landed on main.
  method:
    - fetch selected files from main
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

### 13.5 V2 addition boundary

```yaml
v2_addition_boundary:
  unchanged_from_v1:
    - sections_1_through_12
    - v1_frontmatter
    - original wording and structure before this section
  added_in_v2:
    - section_13_final_git_move_to_main
  drift_check_rule: Compare V1 and V2; all differences before section 13 are drift unless explicitly approved.
```
