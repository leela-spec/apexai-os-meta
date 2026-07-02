---
promptflow_id: special_ops_knowledge_bank_kb_update_corrected
target_agent: special_ops__knowledge_bank
repo_boundary: single_repo_only
working_repo: leela-spec/MasterOfArts
target_repo: leela-spec/MasterOfArts
source_repo: leela-spec/MasterOfArts
target_branch: main
execution_branch_required: false
branch_creation_forbidden: true
target_kb_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/
appendix_input: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/appendices/
audit_input: OpenClaw/07_finalopenclawsystem/managed/agent_kb/KB_SYSTEM_RELIABILITY_AUDIT_V1
source_index: agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md
status: approved_promptflow
quality: corrected
created_at: 2026-05-04
owner: special_ops__knowledge_bank
validator: special_ops__informatics_design
---

# PROMPTFLOW_SPECIAL_OPS_KNOWLEDGE_BANK_KB_UPDATE_CORRECTED

## 0. Purpose

Create the corrected promptflow for updating the Special Ops Knowledge Bank KB with the same high-control pattern used for the corrected Informatics Design KB update, but with the crucial execution-capability correction:

- this planning chat produces exact per-file unified diffs;
- Codex, not the GitHub connector, applies them;
- Codex has zero content-generation freedom;
- Codex executes directly on `main`, with no branch or PR path;
- older Knowledge Bank promptflows are historical context only and must not serve as the basis for this corrected flow.

## 1. Hard repo boundary

```yaml
repo_boundary: single_repo_only
working_repo: leela-spec/MasterOfArts
source_repo: leela-spec/MasterOfArts
target_repo: leela-spec/MasterOfArts
target_branch: main
execution_branch_required: false
branch_creation_forbidden: true
forbidden_repos:
  - leela-spec/apexai-os-meta
  - any Apex repo
```

## 2. Target lock

```yaml
target_agent: special_ops__knowledge_bank
target_kb_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/
appendix_input: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/appendices/
audit_input: OpenClaw/07_finalopenclawsystem/managed/agent_kb/KB_SYSTEM_RELIABILITY_AUDIT_V1
source_index: agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md
validator: special_ops__informatics_design
```

## 3. Corrected scope

```yaml
target_files:
  scaffold:
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/ESSENCE.md
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/BEST_PRACTICES.md
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/MISTAKES.md
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/TEMPLATES.md
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/LEARNING_QUEUE.md
  appendices:
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/appendices/**
```

```yaml
write_scope:
  allowed:
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/ESSENCE.md
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/BEST_PRACTICES.md
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/MISTAKES.md
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/TEMPLATES.md
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/LEARNING_QUEUE.md
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/appendices/**
  forbidden:
    - any Apex repo path
    - any apexai-os-meta path
    - any other MasterOfArts agent KB folder
    - OpenClaw/07_finalopenclawsystem/managed/config/**
    - provider/model config
    - runtime config
    - shared governance files
    - files outside target_kb_root except read-only audit/index/source files
```

## 4. Source authority

Read sources in this order:

```yaml
primary_read_order:
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/ESSENCE.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/BEST_PRACTICES.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/MISTAKES.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/TEMPLATES.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/LEARNING_QUEUE.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/appendices/**
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/KB_SYSTEM_RELIABILITY_AUDIT_V1
  - agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md
```

### Legacy promptflow quarantine

```yaml
legacy_promptflow_policy:
  possible_legacy_files:
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/PROMPTFLOW_KB_BASE_BUILD.md
    - any other promptflow under OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/
  status: historical_context_only
  allowed_use:
    - identify old target paths only when needed for conflict detection
    - record that an old promptflow exists
  forbidden_use:
    - do_not_use_as_basis
    - do_not_copy_generation_sequence
    - do_not_copy_execution_method
    - do_not_allow_to_override_this_corrected_promptflow
    - do_not_treat_as_current_authority
  stop_if:
    - old_promptflow_conflicts_with_this_corrected_promptflow_and_operator_has_not_dispositioned_conflict
```

Use failure-analysis material only as process-warning input:

```yaml
use_failure_files_as:
  - process_failure_patterns_only
  - wrong-repo prevention
  - wrong-path prevention
  - false-completion prevention
  - whole-file-replacement drift warning
  - unsupported-done-claim warning

do_not_use_failure_files_as:
  - target path authority
  - content source for the Knowledge Bank KB
  - proof that files are already corrected
  - permission to rewrite files freely
```

## 5. Prime directive

Create the best machine-readable Special Ops Knowledge Bank KB base in the exact target path.

Integrate high-impact, proven, and operator-approved Knowledge Bank improvements into scaffold files and appendices.

Do not merely append prose. Convert both existing and new content into clear, agent-followable structure.

Do not change shared governance, config, Apex paths, other agent KBs, or non-target surfaces.

## 6. Machine-readability contract

All updated KB content must use machine-readable forms where possible:

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
Failure:
Candidate:
Status:
Owner:
Validator:
Applies when:
Do not:
```

Preferred structures:

```text
compact sections
stable headings
tables for decision records
explicit status labels
single-purpose bullets
clear target-file roles
machine-checkable rules
appendix pointers for deep content
```

Reject:

```text
long prose explanation
essay-style rationale
ambiguous “should” language
hidden rules inside paragraphs
duplicate concepts with unclear role
candidate content hardened without status
self-certifying QA language without proof
```

## 7. Candidate handling rule

Before any diff is generated, produce this Candidate Decision Table:

```md
| candidate_id/source | candidate_summary | evidence_strength | possible_targets | recommendation | reason | operator_decision |
|---|---|---|---|---|---|---|
```

Allowed recommendation values:

```text
integrate_into_scaffold
integrate_into_appendix
split_between_scaffold_and_appendix
keep_as_candidate
reject_obsolete
needs_operator_decision
```

Allowed operator decisions:

```text
approved
rejected
revise
defer
```

Hard rule:

```text
No candidate may be deleted from appendices unless the decision table shows it was approved and the final validation proves it was integrated into the KB base or otherwise dispositioned.
```

Preferred default:

```text
Do not delete rows. Move or relabel candidates as integrated, resolved, deferred, rejected, or pending independent audit.
```

## 8. Knowledge Bank-specific candidate defaults

Unless current file content contradicts these, prefill the Candidate Decision Table with these recommendations:

```yaml
recommended_candidates:
  - id: KB-UPD-001
    summary: Add APPENDIX_KB_PROMOTION_TRACE.md
    priority: P0
    recommendation: integrate_into_appendix
    reason: Knowledge Bank owns candidate routing and must expose candidate-to-promotion trace.
  - id: KB-UPD-002
    summary: Add APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md
    priority: P1
    recommendation: integrate_into_appendix
    reason: Durable QA/readiness/research status should not remain chat-only.
  - id: KB-UPD-003
    summary: Add APPENDIX_KB_SOURCE_NOTES.md
    priority: P1
    recommendation: integrate_into_appendix
    reason: Knowledge Bank owns source manifesting and source-observation reuse.
  - id: KB-UPD-004
    summary: Add APPENDIX_KB_DATABASE_SCHEMA.md
    priority: P1
    recommendation: integrate_into_appendix
    reason: Existing Markdown database appendices need shared schema/status/ID conventions.
  - id: KB-UPD-005
    summary: Add APPENDIX_KB_EXAMPLES.md
    priority: P2
    recommendation: keep_as_candidate
    reason: Examples are useful after schema/QA/promotion-trace stabilization; integrate only if operator explicitly approves.
  - id: KB-UPD-006
    summary: Update TEMPLATES.md with templates for promotion trace, source notes, QA plan, and database schema rows.
    priority: P2
    recommendation: integrate_into_scaffold
    reason: Template surface should expose repeatable forms without hiding promptflow law.
  - id: KB-UPD-007
    summary: Update LEARNING_QUEUE.md with deferred source notes/schema/examples/promotion trace follow-ups after approved integrations.
    priority: P2
    recommendation: split_between_scaffold_and_appendix
    reason: Learning queue keeps deferred work visible while appendix records decision status.
```

Stop for operator approval unless the operator has already stated:

```yaml
operator_decision_policy: all_recommended_P0_P1_approved
```

or:

```yaml
operator_decision_policy: all_approved
```

## 9. Scaffold role map

```yaml
ESSENCE.md:
  role: compact activation contract
  receives:
    - highest-priority Knowledge Bank operating constraints
    - KB lane identity
    - non-negotiable candidate/evidence/status boundaries
    - compact database-governance doctrine only if essential
  must_not_receive:
    - full schemas
    - long source notes
    - deep examples

BEST_PRACTICES.md:
  role: accepted compact practice layer
  receives:
    - procedures for source manifesting
    - candidate routing
    - database appendices
    - promotion trace practice
    - source note practice
    - QA/research planning practice

MISTAKES.md:
  role: anti-drift and failure-prevention layer
  receives:
    - candidate-to-canon leak failures
    - scaffold bloat failures
    - source manifest as truth failures
    - whole-file replacement masked as patch execution
    - self-certifying QA failures

TEMPLATES.md:
  role: reusable machine-facing schemas
  receives:
    - Candidate Decision Table
    - promotion trace row schema
    - source notes row schema
    - QA/research plan schema
    - database schema appendix template
    - final proof report schema

LEARNING_QUEUE.md:
  role: unresolved or deferred candidate queue
  receives:
    - useful but unapproved candidates
    - candidates needing more evidence
    - operator-deferred items
    - future improvement backlog
    - pending independent patch audit notes
```

## 10. Appendix update rule

Appendices are writable only inside the Knowledge Bank KB root.

Appendices must be updated when:

```text
a strong candidate is integrated into scaffold files
a candidate is rejected
a candidate is deferred
a candidate is split into scaffold + appendix content
a TODO becomes obsolete
machine-readability status changes
audit status changes
a process exception affects confidence
a new database appendix is added
```

Appendix updates must preserve:

```text
candidate IDs
source references
evidence notes
ranking logic
decision history
traceability
validator ownership
promotion status boundaries
```

## 11. Unified diff rule — strict

All writes must be represented as exact unified diffs before Codex receives execution instructions.

```yaml
diff_requirements:
  - one unified diff per changed file
  - no approximate hunks
  - no ellipses
  - no "apply around here"
  - no omitted context inside a hunk
  - no whole-file replacement unless the unified diff explicitly represents the whole file and operator approved that rewrite
  - no connector update_file fallback
  - no native patch claim unless git apply is available
  - include new files as /dev/null to target path diffs
  - include deleted lines and added lines exactly
  - include only one target path per diff block
```

Important correction:

```text
Whole-file GitHub connector replacement is not unified-diff application.

If the only available execution mechanism is GitHub update_file/create_file, STOP. Do not execute. Produce the patch pack and Codex prompt only.
```

## 12. Required execution phases

### Phase 1 — Verify target

```text
confirm repo == leela-spec/MasterOfArts
confirm active branch == main
confirm target_root exists
confirm scaffold files exist
confirm appendix_input exists
confirm audit_input exists or explicitly record missing audit input
list target scaffold files
list appendix files
list promptflow files under the Knowledge Bank KB root and quarantine older promptflows as historical only
STOP if any path resolves to Apex/apexai-os-meta
STOP if target root is not special_ops__knowledge_bank
```

### Phase 2 — Read and classify inputs

```text
read current scaffold files
read appendix files
read KB_SYSTEM_RELIABILITY_AUDIT_V1 if present
read source index and relevant Knowledge Bank source-slice files
do not use older Knowledge Bank promptflows as basis
extract:
  - proven high-impact candidates
  - future research candidates
  - TODOs
  - machine-readability gaps
  - reliability/audit constraints
  - existing scaffold weaknesses
  - Knowledge Bank-specific database-governance gaps
```

### Phase 3 — Candidate Decision Table

Produce:

```md
| candidate_id/source | candidate_summary | evidence_strength | possible_targets | recommendation | reason | operator_decision |
|---|---|---|---|---|---|---|
```

Stop for operator decision unless approval rules already exist.

### Phase 4 — Design target updates

For each scaffold and appendix file:

```md
| file | current_role | needed_update | source_candidate | update_type | risk | expected_diff |
|---|---|---|---|---|---|---|
```

Allowed update types:

```text
machine_readability_refactor
candidate_integration
candidate_status_update
todo_resolution
audit_rule_integration
appendix_creation
appendix_cleanup
template_addition
failure_rule_addition
qa_status_update
database_schema_addition
promotion_trace_addition
source_notes_addition
```

### Phase 5 — Generate unified diffs

Output one diff block per changed file:

````md
## PATCH 001 — <path>

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

### Phase 6 — Validate diffs before Codex prompt

```text
diff target path inside allowed write scope
no Apex path
no other agent folder
no config files
candidate decisions respected
appendix statuses updated
machine-readable structure improved
no unsupported deletion
no false completion
one file per diff
all diffs are exact unified diffs
all diffs apply to main directly
no branch or PR path appears in execution instructions
```

### Phase 7 — Produce zero-freedom Codex prompt

The final output must include a Codex prompt that:

```text
- tells Codex not to generate content
- tells Codex to work directly on main
- tells Codex not to create a branch
- tells Codex to save each provided diff to /tmp/kb_patch_XXX.diff
- tells Codex to run git apply --check on every diff
- tells Codex to run git apply only after all checks pass
- tells Codex to run git diff --check
- tells Codex to verify changed file set is exactly the approved set
- tells Codex to commit directly on main only if all checks pass
- tells Codex to push origin main only if all checks pass
- tells Codex to stop and report if any check fails
```

### Phase 8 — Final proof schema

Planning-chat final proof must say:

```yaml
repo:
target_root:
target_branch: main
branch_creation_required: false
branch_creation_forbidden: true
audit_read:
appendices_read:
candidate_decision_table:
operator_decisions_used:
legacy_promptflows_found:
legacy_promptflows_used_as_basis: false
files_planned_for_change:
scaffold_files_planned:
appendix_files_planned:
diffs_created:
diff_application_method_required: codex_git_apply_on_main
connector_whole_file_replacement_allowed: false
changed_file_set_expected:
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
changed_file_set_actual:
changed_file_set_matches_expected:
forbidden_paths_changed:
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
  - target_root_is_not_exact_special_ops_knowledge_bank_path
  - target_agent_is_not_special_ops__knowledge_bank
  - appendix_input_missing
  - Apex_or_apexai_os_path_detected_as_target
  - other_agent_kb_folder_detected_as_target
  - runtime_config_detected_as_target
  - provider_or_model_config_detected_as_target
  - candidate_needs_operator_decision
  - old_promptflow_is_used_as_basis
  - deletion_without_integration_proof
  - diff_changes_forbidden_path
  - diff_is_not_exact_unified_diff
  - final_response_lacks_expected_changed_file_set
  - executor_claims_completion_from_prior_summary
  - executor_uses_connector_whole_file_replacement
  - executor_claims_git_apply_without_git_apply_check
  - executor_creates_branch_or_pr
```

## 14. Final compact promptflow

```text
You are preparing the Special Ops Knowledge Bank KB update in leela-spec/MasterOfArts only.

Target root:
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/

Target branch:
main only. Do not create a branch or PR.

Goal:
Create an excellent machine-readable Special Ops Knowledge Bank KB base by updating the five scaffold files and appendices.

Use:
- current Knowledge Bank scaffold files
- current Knowledge Bank appendices
- KBFuture / future-research findings when present
- KB_SYSTEM_RELIABILITY_AUDIT_V1 as reliability/process input
- source index and Knowledge Bank source-slice files

Do not use:
- old Knowledge Bank promptflows as the basis for this corrected flow
- Apex repo paths
- apexai-os-meta target assumptions
- other agent KB folders
- config files
- prior execution summaries as completion proof
- GitHub connector whole-file replacement as patch execution

Required behavior:
1. Verify exact repo, main branch, and paths.
2. Read scaffold, appendix, source-index, and audit inputs.
3. Detect old promptflows and quarantine them as historical only.
4. Extract high-impact and proven candidates.
5. Produce candidate decision table with recommendation and operator decision field.
6. Stop for operator decision where needed.
7. Convert both existing and new content into machine-readable structure.
8. Update scaffold files only where compact high-impact approved content belongs.
9. Update appendices after integration, rejection, deferral, QA status change, or new database surface creation.
10. Produce one exact unified diff per changed file.
11. Validate diffs before producing execution instructions.
12. Do not apply diffs in this chat unless native git apply is available.
13. Produce a zero-freedom Codex prompt that applies the exact diffs to main with git apply --check and git apply.
14. Report expected changed_file_set and proof schema.

Core rule:
Make the Knowledge Bank KB excellent and machine-readable, while preserving traceability, candidate status, source authority, and target-path discipline.
```

---

# Zero-freedom Codex prompt template produced at the end of the flow

Use this as the final generated executor block after the exact per-file diffs exist.

````md
# CODEX EXECUTION PROMPT — SPECIAL OPS KNOWLEDGE BANK KB PATCH

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
target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/
branch_creation_required: false
branch_creation_forbidden: true
```

## Allowed changed paths

```text
<EXACT_CHANGED_FILE_SET_FROM_PROMPTFLOW>
```

No other paths may change.

Forbidden:

```text
OpenClaw/07_finalopenclawsystem/managed/config/**
any provider/model config
any Apex path
any apexai-os-meta path
any other agent KB folder
```

## Required commands

Run exactly this sequence, adapting only patch filenames to match the patch blocks below:

```bash
git status --short
git fetch origin
git switch main
git pull --ff-only origin main

mkdir -p /tmp/openclaw_kb_patches
```

For each patch block below, write the exact diff text into:

```text
/tmp/openclaw_kb_patches/001_<safe_name>.diff
/tmp/openclaw_kb_patches/002_<safe_name>.diff
...
```

Then run:

```bash
git apply --check /tmp/openclaw_kb_patches/*.diff
```

If and only if that passes:

```bash
git apply /tmp/openclaw_kb_patches/*.diff
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
git commit -m "Update Special Ops Knowledge Bank KB machine-readability"
git push origin main
```

## Patch blocks

Paste exact patch blocks here.

### PATCH 001 — `<path>`

```diff
<exact unified diff>
```

### PATCH 002 — `<path>`

```diff
<exact unified diff>
```

## Required final report

Return only:

```yaml
repo: leela-spec/MasterOfArts
branch: main
target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/
git_apply_check_passed:
git_apply_passed:
git_diff_check_passed:
changed_file_set_expected:
changed_file_set_actual:
changed_file_set_matches_expected:
forbidden_paths_changed:
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
