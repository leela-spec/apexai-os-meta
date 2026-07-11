---
promptflow_id: special_ops_hygiene_clean_kb_update_folder_local_corrected
target_agent: special_ops__hygiene_clean
repo_boundary: single_repo_only
working_repo: leela-spec/MasterOfArts
target_repo: leela-spec/MasterOfArts
source_repo: leela-spec/MasterOfArts
target_branch: main
execution_branch_required: false
branch_creation_forbidden: true
target_kb_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/
appendix_input: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/
source_authority: target_kb_folder_only
cross_agent_kb_reads_forbidden: true
stale_global_source_indexes_forbidden: true
connector_whole_file_replacement_allowed: false
diff_application_method_required: codex_git_apply_on_main
status: approved_promptflow
quality: folder_local_corrected
created_at: 2026-05-04
owner: special_ops__hygiene_clean
validator: operator
---

# PROMPTFLOW_SPECIAL_OPS_HYGIENE_CLEAN_KB_UPDATE_FOLDER_LOCAL_CORRECTED

## 0. Purpose

Create the corrected folder-local promptflow for updating the Special Ops Hygiene Clean KB.

This flow preserves the execution discipline of the corrected KB update pattern while replacing the source model with a strict target-folder-only source model.

Core correction:

- read only the `special_ops__hygiene_clean` KB folder;
- do not read sibling agent KB folders;
- do not read old global source indexes;
- do not use stale setup ledgers;
- derive all candidates only from current Hygiene Clean KB files;
- produce exact per-file unified diffs before execution;
- require Codex/native git to apply patches directly on `main`;
- forbid GitHub connector whole-file replacement as patch execution.

This file is a promptflow artifact. Its presence in the repo is not execution of the promptflow phases.

## 1. Hard repo and folder boundary

```yaml
repo_boundary: single_repo_only
working_repo: leela-spec/MasterOfArts
source_repo: leela-spec/MasterOfArts
target_repo: leela-spec/MasterOfArts
target_branch: main
execution_branch_required: false
branch_creation_forbidden: true
source_authority: target_kb_folder_only
target_agent: special_ops__hygiene_clean
target_kb_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/
appendix_input: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/
```

```yaml
allowed_read_scope:
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/**

forbidden_read_scope:
  - any other agent KB folder
  - agent_kb_source_indexes/**
  - OpenClaw/04_final-system-setup/**
  - OpenClaw/02_research-kb/**
  - old setup ledgers
  - prior agent KB outputs
  - cross-agent appendices
  - external repo material unless operator supplied it explicitly for this run
```

```yaml
allowed_write_scope:
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/ESSENCE.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/BEST_PRACTICES.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/MISTAKES.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/TEMPLATES.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/LEARNING_QUEUE.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/**

forbidden_write_scope:
  - any other agent KB folder
  - OpenClaw/07_finalopenclawsystem/managed/config/**
  - provider/model config
  - runtime config
  - shared governance files
  - files outside target_kb_root
```

## 2. Non-goals

```yaml
non_goals:
  - do_not_rebuild_from_global_source_indexes
  - do_not_copy_other_agent_kb_structures
  - do_not_read_other_agent_kb_folders
  - do_not_import_other_agent_candidates
  - do_not_use_stale_setup_ledgers
  - do_not_create_cross_agent_schema
  - do_not_update_shared_governance
  - do_not_update_runtime_config
  - do_not_claim_execution_from_promptflow_file_presence
```

## 3. Prime directive

Update only the Special Ops Hygiene Clean KB base using only the current files inside its own KB folder.

Improve machine-readability, QA/hygiene specificity, candidate status clarity, closure discipline, and execution safety without importing content from another agent KB or stale global setup source.

If required information appears to require another folder, stop and report the missing local evidence instead of widening scope.

## 4. Current-folder truth rule

```yaml
target_kb_folder_files_are_the_only_content_basis: true
external_repo_material_is_forbidden_unless_operator_supplied: true
recommended_candidates_source: derive_only_from_hygiene_kb_folder
candidate_prefix: HYG-UPD
repo_wide_promptflow_search_forbidden: true
```

### Consequences

- Do not use old global source indexes as current authority.
- Do not mine old setup ledgers for candidate defaults.
- Do not copy improvement sets from another agent KB.
- Do not treat sibling promptflows as templates except for execution-discipline concepts already embedded in this file.
- Do not create new appendices unless the local Hygiene Clean KB files show a true local gap and the operator approves the candidate row.

## 5. Machine-readability contract

All updated Hygiene Clean KB content should use machine-readable forms where possible:

```text
Rule:
Constraint:
Decision:
Validation:
Stop:
Input:
Output:
Procedure:
Template:
Finding:
Severity:
Evidence:
Closure:
Candidate:
Status:
Owner:
Applies when:
Do not:
```

Preferred structures:

```text
compact sections
stable headings
tables for findings and closure records
explicit severity labels
explicit status labels
single-purpose bullets
clear target-file roles
machine-checkable validation rules
appendix pointers for deep content
```

Reject:

```text
long prose explanation
essay-style rationale
ambiguous should language
hidden rules inside paragraphs
candidate content hardened without status
self-certifying QA language without proof
closure claims without evidence
external source assumptions
```

## 6. Required local read order

Read only these local surfaces, if present, in this order:

```yaml
primary_read_order:
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/ESSENCE.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/BEST_PRACTICES.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/MISTAKES.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/TEMPLATES.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/LEARNING_QUEUE.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/**
```

If a local source manifest exists inside the target KB folder, read it as a local provenance surface, not as permission to read old external sources.

## 7. Folder-local legacy promptflow quarantine

```yaml
legacy_promptflow_policy:
  search_scope:
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/**
  status: historical_context_only
  allowed_use:
    - record that an old local promptflow exists
    - identify local stale execution assumptions for conflict detection
  forbidden_use:
    - use_old_promptflow_as_basis
    - copy_old_execution_method
    - copy_old_source_model
    - allow_old_promptflow_to_override_this_corrected_promptflow
    - treat_old_promptflow_as_current_authority
  stop_if:
    - old_promptflow_conflicts_with_this_corrected_promptflow_and_operator_has_not_dispositioned_conflict
```

## 8. Candidate handling rule

Before any diff is generated, produce this Candidate Decision Table using only local target-folder evidence:

```md
|candidate_id|local_source_file|candidate_summary|local_evidence_strength|possible_targets|recommendation|reason|operator_decision|
|---|---|---|---|---|---|---|---|
```

Allowed recommendation values:

```text
integrate_into_scaffold
integrate_into_appendix
split_between_scaffold_and_appendix
keep_as_candidate
reject_obsolete
defer
needs_operator_decision
```

Allowed operator decisions:

```text
approved
rejected
revise
defer
```

Operator shortcut aliases:

```yaml
operator_decision_aliases:
  all_changes_are_validated: all_approved
  continue: proceed_after_approval_if_candidate_table_exists
```

Approval scope:

```yaml
operator_approval_scope:
  candidate_decisions: approved
  file_change_design: allowed
  diff_generation: allowed
  repo_write: not_allowed_without_codex_git_apply
operator_approval_does_not_authorize_connector_writes: true
```

Hard rule:

```text
No candidate may be deleted from local appendices or learning surfaces unless the decision table shows it was approved and the final validation proves it was integrated, rejected, deferred, or otherwise dispositioned.
```

## 9. Update design table

After operator approval, design the target updates before generating diffs:

```md
|file|current_role|needed_update|local_source_candidate|update_type|risk|expected_diff|
|---|---|---|---|---|---|---|
```

Allowed update types:

```text
machine_readability_refactor
candidate_integration
candidate_status_update
finding_rule_addition
closure_rule_addition
todo_resolution
appendix_creation
appendix_cleanup
template_addition
failure_rule_addition
qa_status_update
local_gap_record
```

Diff-generation order:

1. appendices and local database surfaces
2. templates
3. mistakes
4. best practices
5. essence
6. learning queue

Scaffold files must summarize local appendix/database changes, not invent them.

## 10. Changed-file whitelist rule

Before generating diffs, declare the exact changed-file set:

```yaml
changed_file_set_must_be_declared_before_diff_generation: true
changed_file_set_source: approved_update_design_table
```

No diff may touch a path outside the declared changed-file set.

New appendix creation is allowed only when:

```yaml
new_appendix_creation_rule:
  allowed_only_if:
    - local_hygiene_kb_gap_found
    - existing local appendix cannot truthfully host content
    - operator approved candidate row
```

## 11. Unified diff rule - strict

All writes must be represented as exact unified diffs before Codex receives execution instructions.

```yaml
diff_requirements:
  - one unified diff per changed file
  - no approximate hunks
  - no ellipses
  - no apply_around_here
  - no omitted context inside a hunk
  - no whole-file replacement unless the unified diff explicitly represents the whole file and operator approved that rewrite
  - no connector update_file fallback for execution
  - no native patch claim unless git apply is available
  - include new files as /dev/null to target path diffs
  - include deleted lines and added lines exactly
  - include only one target path per diff block
```

Important correction:

```text
Whole-file GitHub connector replacement is not unified-diff application.

If the only available execution mechanism is GitHub update_file/create_file, STOP. Do not execute the KB update. Produce the patch pack and Codex prompt only.
```

## 12. Required execution phases

### Phase 1 - Verify target

```text
confirm repo == leela-spec/MasterOfArts
confirm active branch == main
confirm target_root exists
confirm scaffold files exist or record missing local scaffold files
confirm appendix_input exists or record missing local appendix folder
confirm all read paths are inside target_kb_root
list target scaffold files
list local appendix files
list local promptflow files under the Hygiene Clean KB root only
quarantine older local promptflows as historical only
STOP if any read or write path leaves target_kb_root
STOP if any path resolves to another agent KB folder
STOP if target root is not special_ops__hygiene_clean
```

### Phase 2 - Read and classify local inputs

```text
read current local scaffold files
read current local appendix files
read local promptflow files only for quarantine/conflict detection
extract only local Hygiene Clean KB gaps, TODOs, candidate-status issues, closure issues, machine-readability gaps, and stale local references
do not read global source indexes
do not read sibling agent KB folders
do not use stale setup ledgers
```

### Phase 3 - Candidate Decision Table

Produce the candidate decision table from local target-folder evidence.

Stop for operator decision unless the operator explicitly provides an approval shortcut or per-row decisions.

### Phase 4 - Design target updates

Produce the update design table and exact expected changed-file set.

### Phase 5 - Generate unified diffs

Output one diff block per changed file:

````md
## PATCH 001 - <path>

```diff
diff --git a/<path> b/<path>
--- a/<path>
+++ b/<path>
@@ ...
```
````

For new files:

```diff
diff --git a/<path> b/<path>
new file mode 100644
--- /dev/null
+++ b/<path>
@@ ...
```

### Phase 6 - Validate diffs before Codex prompt

```yaml
validation:
  all_read_files_under_target_kb_folder: true
  all_changed_files_under_target_kb_folder: true
  no_source_index_dependency_added: true
  no_stale_path_reference_added: true
  no_other_agent_kb_content_added: true
  no_config_files_changed: true
  candidate_decisions_respected: true
  changed_file_set_declared_before_diffs: true
  one_file_per_diff: true
  all_diffs_are_exact_unified_diffs: true
  all_diffs_apply_to_main_directly: true
```

Forbidden new path patterns in diffs:

```yaml
forbidden_new_path_patterns:
  - OpenClaw/04_final-system-setup
  - OpenClaw/02_research-kb
  - agent_kb_source_indexes
  - AllAIBestPractice
  - Apex
  - apexai-os-meta
  - managed/config
```

The patch pack must include:

```yaml
files_read:
  - target-folder-only paths
external_files_read: []
```

If any external file was read without explicit operator permission, status is failed.

### Phase 7 - Produce zero-freedom Codex prompt

The final output must include a Codex prompt that:

```text
- tells Codex not to generate content
- tells Codex to work directly on main
- tells Codex not to create a branch
- tells Codex to save each provided diff to /tmp/hygiene_patch_XXX.diff
- tells Codex to run git apply --check on every diff
- tells Codex to run git apply only after all checks pass
- tells Codex to run git diff --check
- tells Codex to verify changed file set exactly equals the approved set
- tells Codex to report any cross-folder or forbidden-path change
- tells Codex to commit directly on main only if all checks pass
- tells Codex to push origin main only if all checks pass
- tells Codex to stop and report if any check fails
```

### Phase 8 - Final proof schema

Planning-chat final proof must say:

```yaml
repo:
target_root:
target_branch: main
branch_creation_required: false
branch_creation_forbidden: true
source_authority: target_kb_folder_only
files_read:
external_files_read: []
local_appendices_read:
local_promptflows_found:
legacy_promptflows_used_as_basis: false
candidate_decision_table:
operator_decisions_used:
files_planned_for_change:
changed_file_set_expected:
diffs_created:
diff_application_method_required: codex_git_apply_on_main
connector_whole_file_replacement_allowed: false
forbidden_paths_in_diff:
codex_prompt_produced:
status:
```

Codex final proof must say:

```yaml
repo:
branch: main
target_root:
git_apply_check_passed:
git_apply_passed:
git_diff_check_passed:
changed_file_set_expected:
changed_file_set_actual:
changed_file_set_matches_expected:
forbidden_paths_changed:
external_paths_read_or_changed:
fetch_back_or_cat_verified:
commit_created:
commit_sha:
pushed_to_origin_main:
status:
```

## 13. Stop conditions

```yaml
stop_if:
  - repo_is_not_leela_spec_MasterOfArts
  - active_branch_is_not_main
  - target_root_is_not_exact_special_ops_hygiene_clean_path
  - target_agent_is_not_special_ops__hygiene_clean
  - executor_reads_outside_target_kb_folder_without_operator_permission
  - executor_attempts_to_use_old_global_source_index
  - any_required_information_seems_to_require_other_agent_kb_folder
  - candidate_basis_depends_on_non_hygiene_agent_content
  - generated_diff_mentions_other_agent_content_as_source_authority
  - runtime_config_detected_as_target
  - provider_or_model_config_detected_as_target
  - candidate_needs_operator_decision
  - old_promptflow_is_used_as_basis
  - deletion_without_integration_or_disposition_proof
  - changed_file_set_not_declared_before_diffs
  - diff_changes_forbidden_path
  - diff_is_not_exact_unified_diff
  - final_response_lacks_expected_changed_file_set
  - executor_claims_completion_from_prior_summary
  - executor_claims_completion_from_promptflow_file_presence
  - executor_uses_connector_whole_file_replacement
  - executor_claims_git_apply_without_git_apply_check
  - executor_creates_branch_or_pr
```

## 14. Required phase ledger

Every execution of this promptflow must maintain this phase ledger in the response:

```md
|phase|required_action|completed|evidence|stop_reason_if_any|
|---|---|---|---|---|
|Phase 1|Verify target folder, repo, branch, local read scope|pending|pending|pending|
|Phase 2|Read and classify local inputs only|pending|pending|pending|
|Phase 3|Produce Candidate Decision Table|pending|pending|pending|
|Phase 4|Design target updates and changed-file set|pending|pending|pending|
|Phase 5|Generate exact unified diffs|pending|pending|pending|
|Phase 6|Validate diffs and local-only scope|pending|pending|pending|
|Phase 7|Produce zero-freedom Codex prompt|pending|pending|pending|
|Phase 8|Produce final proof schema|pending|pending|pending|
```

## 15. Final compact promptflow

```text
You are preparing the Special Ops Hygiene Clean KB update in leela-spec/MasterOfArts only.

Target root:
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/

Target branch:
main only. Do not create a branch or PR.

Source authority:
The target KB folder only. Do not read sibling agent KB folders. Do not read global source indexes. Do not use old setup ledgers. Do not import candidate defaults from another agent.

Goal:
Improve the machine-readability, QA/hygiene specificity, closure discipline, candidate status clarity, and execution safety of the Hygiene Clean KB using only its current local scaffold files and appendices.

Required behavior:
1. Verify exact repo, main branch, and target root.
2. Read only the target Hygiene Clean KB folder.
3. Detect old local promptflows and quarantine them as historical only.
4. Extract candidates only from local Hygiene Clean KB evidence.
5. Produce a Candidate Decision Table with operator decision field.
6. Stop for operator decision where needed.
7. Design target updates and declare the exact changed-file set before diffs.
8. Produce one exact unified diff per changed file.
9. Validate all diffs are target-folder-only and contain no stale external path dependencies.
10. Do not apply diffs in this chat unless native git apply is available.
11. Do not use GitHub connector whole-file replacement as patch execution.
12. Produce a zero-freedom Codex prompt that applies the exact diffs to main with git apply --check and git apply.
13. Report expected changed_file_set and proof schema.

Core rule:
Make the Hygiene Clean KB locally better and more machine-followable without importing any non-local KB content or stale source authority.
```

---

# Zero-freedom Codex prompt template

Use this as the executor block after exact per-file diffs exist.

````md
# CODEX EXECUTION PROMPT - SPECIAL OPS HYGIENE CLEAN KB PATCH

## Role

You are Codex operating on a real local checkout of `leela-spec/MasterOfArts`.

You are not a content author.
You are a patch executor and verifier only.

## Non-negotiable constraint

Do not invent, improve, rewrite, reformat, normalize, or repair content.

Apply only the exact unified diffs provided below.

If any diff fails `git apply --check`, STOP and report failure. Do not hand-edit.

## Repo

```yaml
repo: leela-spec/MasterOfArts
base_branch: main
work_branch: main
target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/
branch_creation_required: false
branch_creation_forbidden: true
source_authority: target_kb_folder_only
```

## Allowed changed paths

```text
<EXACT_CHANGED_FILE_SET_FROM_PROMPTFLOW>
```

No other paths may change.

Forbidden:

```text
any other agent KB folder
OpenClaw/07_finalopenclawsystem/managed/config/**
any provider/model config
any Apex path
any apexai-os-meta path
agent_kb_source_indexes/**
OpenClaw/04_final-system-setup/**
OpenClaw/02_research-kb/**
```

## Required commands

Run exactly this sequence, adapting only patch filenames to match the patch blocks below:

```bash
git status --short
git fetch origin
git switch main
git pull --ff-only origin main

mkdir -p /tmp/openclaw_hygiene_patches
```

For each patch block below, write the exact diff text into:

```text
/tmp/openclaw_hygiene_patches/001_<safe_name>.diff
/tmp/openclaw_hygiene_patches/002_<safe_name>.diff
...
```

Then run:

```bash
git apply --check /tmp/openclaw_hygiene_patches/*.diff
```

If and only if that passes:

```bash
git apply /tmp/openclaw_hygiene_patches/*.diff
git diff --check
git status --short
git diff --name-only
```

Verify `git diff --name-only` exactly equals:

```text
<EXACT_CHANGED_FILE_SET_FROM_PROMPTFLOW>
```

If any extra path appears, STOP and report `forbidden_path_changed`.

If all checks pass:

```bash
git add <EXACT_CHANGED_FILE_SET_FROM_PROMPTFLOW>
git commit -m "Update Special Ops Hygiene Clean KB machine-readability"
git push origin main
```

## Patch blocks

Paste exact patch blocks here.

### PATCH 001 - `<path>`

```diff
<exact unified diff>
```

## Required final report

Return only:

```yaml
repo: leela-spec/MasterOfArts
branch: main
target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/
git_apply_check_passed:
git_apply_passed:
git_diff_check_passed:
changed_file_set_expected:
changed_file_set_actual:
changed_file_set_matches_expected:
forbidden_paths_changed:
external_paths_read_or_changed:
commit_created:
commit_sha:
pushed_to_origin_main:
status:
notes:
```

## Stop rules

Stop immediately if:

```yaml
stop_if:
  - git_apply_check_fails
  - patch_requires_manual_edit
  - changed_file_set_differs_from_expected
  - forbidden_path_changed
  - target_root_not_found
  - repo_not_leela_spec_MasterOfArts
  - active_branch_not_main
  - branch_creation_required_or_attempted
  - diff_check_fails
```
````
