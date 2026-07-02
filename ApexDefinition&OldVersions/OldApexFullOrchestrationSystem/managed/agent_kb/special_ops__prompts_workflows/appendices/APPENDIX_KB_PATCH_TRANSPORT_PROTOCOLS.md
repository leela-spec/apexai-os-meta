---
class: appendix
role: PATCH_TRANSPORT_PROTOCOLS
surface: agent_kb_appendix
quality: proposed
scope: agent
purpose: select and validate patch transport modes for constant-frame prompt/workflow KB tasks
status: created
created_at: 2026-05-06
owner: special_ops__prompts_workflows
validator: meta_ops
task_id: TASK-03
target_agent: special_ops__prompts_workflows
target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/
source_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/
source_refs:
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/PROMPTFLOW_CONSTANT_FRAME_CONTROLLED_KB_INTEGRATION.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_CONSTANT_FAILURE_INTEGRATION_PROCESS.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_CONSTANT_FAILURE_SOURCE_NOTES.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/GPT_PATCH_WORKFLOW.md
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/06_DIFF_OUTPUT (1).md
---

# APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS

## 1. Purpose

This appendix defines how `special_ops__prompts_workflows` selects among full-body replacement, SEARCH/REPLACE blocks, unified diff, live-edit instruction, and no-patch/manual-review modes.

It resolves transport conflict by making patch format a function of context, tooling, preimage stability, operator workflow, risk, and validation method. It does not promote any one transport as universal law.

## 2. TASK-03 gate record

```yaml
GATE_CHECK:
  task_id: TASK-03
  task_type_understood: appendix_create
  scope_understood: Create a patch-transport appendix that selects between full-body replacement, SEARCH/REPLACE, unified diff, and live-edit instruction.
  target_file: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md
  ambiguity_detected: false
  ready_to_execute: true
```

## 3. Scope lock

```yaml
scope_lock:
  working_repo: leela-spec/MasterOfArts
  target_repo: leela-spec/MasterOfArts
  target_branch: main
  target_agent: special_ops__prompts_workflows
  target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/
  artifact_type: appendix_create
  scope: Create a patch-transport appendix that selects between full-body replacement, SEARCH/REPLACE, unified diff, and live-edit instruction.
  allowed_write:
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md
  forbidden_writes:
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/ESSENCE.md
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/BEST_PRACTICES.md
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/MISTAKES.md
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/TEMPLATES.md
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/LEARNING_QUEUE.md
```

## 4. Source and route-status ledger

| Source | Used for | Route status | Promotion boundary |
|---|---|---|---|
| `PROMPTFLOW_CONSTANT_FRAME_CONTROLLED_KB_INTEGRATION.md` | Frame locks, task queue, appendix-before-scaffold order, closure validation, fetch-back requirement. | `accepted_for_frame_control` | Controls this task and later promotion gates. |
| `appendices/APPENDIX_KB_CONSTANT_FAILURE_INTEGRATION_PROCESS.md` | Ranking that identifies patch transport as an appendix candidate and future chooser requirement. | `accepted_for_route_control` | Supports appendix creation; scaffold updates remain later tasks. |
| `appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md` | HALT/CLARIFY, file-output validation, fetch-back, and scaffold boundary contracts. | `accepted_for_validation_control` | Used as execution-control dependency. |
| `appendices/APPENDIX_KB_CONSTANT_FAILURE_SOURCE_NOTES.md` | Source notes showing `GPT_PATCH_WORKFLOW.md` and `06_DIFF_OUTPUT (1).md` conflict and `SOURCE_CONFLICT_REPORT.md` is missing/rejected. | `accepted_for_source_route_status` | Used to avoid relying on missing evidence. |
| `NewResearchBecauseOfConstantFailure/GPT_PATCH_WORKFLOW.md` | SEARCH/REPLACE block format, exact live preimage rule, exact-once match rule, dry-run before write, failure loop. | `appendix_protocol` | Valid for local search-replace tooling and exact-preimage edits; not universal law. |
| `NewResearchBecauseOfConstantFailure/06_DIFF_OUTPUT (1).md` | Unified diff format for targeted edits, hunk context, patch-only/no-restructure mode, `git apply`. | `appendix_protocol` | Valid when diff tooling is expected; not universal law. |
| `NewResearchBecauseOfConstantFailure/SOURCE_CONFLICT_REPORT.md` | Not used as evidence in this task. TASK-02 recorded the file as not found at the listed path and `rejected_for_promotion`. | `rejected_for_promotion` | Do not depend on it until restored or path-corrected. |

## 5. Transport conflict summary

`GPT_PATCH_WORKFLOW.md` states a strict local workflow: never emit unified diffs, hunk markers, plus/minus lines, or full-file rewrites; always emit SEARCH/REPLACE blocks with verbatim live preimage, exact-once matching, and dry-run validation.

`06_DIFF_OUTPUT (1).md` defines the opposite transport for targeted edits: emit a unified diff block with limited context, one hunk per logical change, no full file when diff is possible, and apply via `git apply`.

These instructions are not both universal rules. They describe different patch channels. This appendix resolves the conflict by selecting the transport according to:

- available tooling;
- whether the target file is new or existing;
- whether the edit is complete-file or localized;
- whether exact preimage is stable;
- whether the operator is applying patches locally, through Git tooling, or through a browser/live editor;
- validation strength available before and after the write;
- risk of accidental scaffold mutation.

## 6. Patch transport chooser

| Situation | Preferred transport | Use when | Required validation | HALT/CLARIFY trigger |
|---|---|---|---|---|
| New file creation | Full-body replacement / full-body file write | File does not exist or the task is explicitly create-file. | Validate path, frontmatter, scope, source refs, route status, then fetch back created file. | HALT if target path already exists and replacement authority is unclear. |
| Complete file replacement | Full-body replacement | Task explicitly asks for whole-file rewrite or existing file is invalid and clearly superseded. | Fetch current file first, preserve valid content unless superseded, compare final file to scope, fetch back after write. | CLARIFY if supersession boundary is unclear. |
| Small localized edit with stable exact preimage | SEARCH/REPLACE blocks | Exact live lines are available and should match exactly once; local `search-replace-py` or equivalent dry-run is expected. | Dry-run all blocks before write; each SEARCH block matches exactly once; review diff; fetch back if repository write occurs. | HALT on missing, duplicate, or stale preimage. |
| Targeted edit where diff tooling is expected | Unified diff | Operator or automation will apply with `git apply`; line-level hunks are clearer than full file. | Dry-run with `git apply --check` or equivalent; review patch-only diff; fetch back after commit/write. | HALT on failed patch check, context drift, or unrelated changed files. |
| Fragile long file where patch preimage may drift | SEARCH/REPLACE or no-patch/manual-review | Long file has unstable context, generated sections, frequent edits, or repeated similar blocks. | Prefer exact unique anchors; if exact-once cannot be guaranteed, stop for manual review. | HALT when unique preimage cannot be established. |
| Semantic rewrite with unclear boundaries | No-patch/manual-review, or full-body only after explicit authority | Edit requires architectural judgment and target section boundaries are not stable. | Operator must confirm scope boundary; fetch current file; record supersession rationale. | CLARIFY for boundary, intent, or source-authority ambiguity. |
| Missing or conflicting source file | No-patch/manual-review | Required source is missing, rejected, or conflict cannot be reconciled from accepted sources. | Record missing source and route status; do not promote unsupported claim. | HALT if source is required for the write. |
| Operator local-edit workflow | SEARCH/REPLACE or unified diff | Human will save patch text locally and run a patch command. | Mandatory dry-run before mutation, then `git diff` review before commit. | HALT if operator cannot run or report dry-run results. |
| Browser/live-edit workflow | Live-edit instruction | No patch tooling is available; user edits through UI or agent has direct file-edit API. | Provide exact file path, section, replacement intent, and post-edit fetch-back checklist. | CLARIFY if live editor cannot identify exact target region. |
| High-risk scaffold mutation | No-patch/manual-review until promotion gate passes | Target is `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md`, or `LEARNING_QUEUE.md`. | Confirm appendix prerequisites, compactness, no external-claim promotion, and fetch-back. | HALT on missing appendix support, essence-before-last, or scope creep. |

## 7. Full-body replacement protocol

Use full-body replacement when creating a new file, replacing a small complete artifact, or intentionally regenerating an entire file under explicit task authority.

```yaml
full_body_replacement_protocol:
  route_status: appendix_protocol
  use_for:
    - new_file_creation
    - explicit_complete_file_replacement
    - invalid_existing_file_with_clear_supersession_authority
    - small_complete_artifact_where_patch_fragility_exceeds_rewrite_risk
  required_preconditions:
    - target_path_under_target_root
    - task_scope_authorizes_full_body
    - current_file_fetched_if_file_exists
    - valid_existing_content_preserved_unless_superseded
    - source_refs_and_route_status_recorded
  validation:
    before_write:
      - verify_target_root
      - verify_scope_repeated
      - verify_no_scaffold_mutation_unless_task_type_is_scaffold_update
      - verify_external_claims_not_promoted
    after_write:
      - fetch_back_written_file
      - compare_path_and_scope
      - verify_source_refs_present
      - verify_changed_file_set_only_includes_authorized_target
  fail_behavior:
    target_exists_without_replacement_authority: CLARIFY
    path_outside_target_root: HALT
    scope_or_source_status_missing: HALT
```

## 8. SEARCH/REPLACE protocol

Use SEARCH/REPLACE when the local workflow expects `search-replace-py` style blocks and the target preimage can be copied from the live file.

```text
path/to/filename.ext
<<<<<<< SEARCH
[verbatim lines from current file, with enough context to match exactly once]
=======
[replacement lines]
>>>>>>> REPLACE
```

```yaml
search_replace_protocol:
  route_status: appendix_protocol
  source_basis: NewResearchBecauseOfConstantFailure/GPT_PATCH_WORKFLOW.md
  use_for:
    - localized_edits_with_stable_exact_preimage
    - local_operator_patch_workflow
    - edits_where_exact_once_match_is_safer_than_line_numbers
  required_preconditions:
    - target_file_fetched_from_live_branch
    - SEARCH_text_copied_from_live_file_not_memory
    - each_block_matches_exactly_once
    - one_block_per_logical_change
    - dry_run_available_before_mutation
  prohibited:
    - hand_editing_failed_patch_blocks_to_force_match
    - applying_without_dry_run
    - using_stale_chat_memory_as_preimage
    - bundling_unreviewed_multi_file_changes_without_per_file_diff_review
  fail_behavior:
    no_match: HALT patch_check_fail
    multiple_matches: HALT patch_check_fail
    stale_file_detected: HALT patch_check_fail
    ambiguous_replacement_intent: CLARIFY
```

## 9. Unified diff protocol

Use unified diff when the receiving workflow expects standard patch tooling and the edit is targeted rather than whole-file.

```diff
# DIFF: path/to/file.md
# SCOPE: one-line description of change only
# MODE: patch-only | no-restructure
--- a/path/to/file.md
+++ b/path/to/file.md
@@ -1,3 +1,3 @@
 unchanged context
-removed line
+added line
 unchanged context
```

```yaml
unified_diff_protocol:
  route_status: appendix_protocol
  source_basis: NewResearchBecauseOfConstantFailure/06_DIFF_OUTPUT (1).md
  use_for:
    - targeted_existing_file_edits
    - git_apply_or_standard_diff_tooling
    - line_level_review_expected_by_operator
  required_preconditions:
    - target_file_exists
    - task_is_not_full_rewrite
    - hunk_scope_is_localized
    - no_unrelated_restructure
  validation:
    before_write:
      - git_apply_check_or_equivalent
      - verify_hunks_match_current_file
      - verify_changed_lines_match_scope
    after_write:
      - review_git_diff
      - fetch_back_written_file_if_committed_or_written
      - verify_no_other_modifications
  fail_behavior:
    patch_check_fails: HALT patch_check_fail
    hunk_context_drift: HALT patch_check_fail
    diff_includes_unrelated_restructure: HALT scope_exceeded
```

## 10. Live-edit instruction protocol

Use live-edit instruction when neither SEARCH/REPLACE nor unified diff is appropriate because the operator is editing through a browser, CMS, repository UI, or direct agent write API.

```yaml
live_edit_instruction_protocol:
  route_status: appendix_protocol
  use_for:
    - browser_or_repository_ui_editing
    - human_operator_manual_edit
    - direct_file_api_write_with_no_patch_text_required
  required_content:
    - exact_repository_path
    - exact_section_or_anchor
    - intended_before_after_semantics
    - forbidden_side_effects
    - validation_checklist
  validation:
    - fetch_current_file_before_edit_when_possible
    - save_only_authorized_target_file
    - fetch_back_after_edit
    - compare_changed_file_set_when_repository_tooling_allows
  fail_behavior:
    ambiguous_anchor: CLARIFY
    editor_cannot_guarantee_target_region: HALT manual_review_required
    scaffold_promotion_gate_not_met: HALT promotion_gate_failed
```

## 11. No-patch/manual-review protocol

Use no-patch/manual-review when patching would create higher risk than it resolves.

```yaml
no_patch_manual_review_protocol:
  route_status: appendix_protocol
  use_for:
    - source_file_missing_or_rejected_for_promotion
    - conflicting_authority_not_resolved_by_chooser
    - semantic_rewrite_with_unclear_boundaries
    - high_risk_scaffold_mutation_without_promotion_gate
    - patch_preimage_cannot_be_made_unique
    - external_claim_would_be_promoted_without_verification
  required_output:
    - HALT_or_CLARIFY_signal
    - blocking_reason
    - safe_recovery_path
  allowed_recovery:
    - fetch_missing_source
    - correct_input_ref
    - split_task
    - create_appendix_first
    - get_operator_confirmation_for_boundary
    - verify_external_claim_before_promotion
```

## 12. Failure-mode matrix

| Failure mode | Detection | Required behavior | Recovery |
|---|---|---|---|
| Target path outside KB root | Path prefix check fails. | `HALT: wrong_target_root` | Retry with target under `special_ops__prompts_workflows/`. |
| Target file missing for patch edit | Fetch returns not found for an edit task. | `HALT: patch_check_fail` unless task is create-file. | Convert to create-file only if payload authorizes it. |
| Existing file found for create-file task | Fetch returns existing content. | `CLARIFY` or update only if task authorizes update. | Confirm replacement/update authority. |
| SEARCH block has no match | Dry-run reports no match. | `HALT: patch_check_fail`; write nothing. | Refetch live file and regenerate block. |
| SEARCH block has multiple matches | Dry-run reports non-unique match. | `HALT: patch_check_fail`; write nothing. | Add unique context or switch transport. |
| Unified diff fails check | `git apply --check` or equivalent fails. | `HALT: patch_check_fail`; write nothing. | Refetch and regenerate diff. |
| Diff includes unrelated restructure | Review shows changes outside task scope. | `HALT: scope_exceeded`. | Split task or narrow patch. |
| Source authority conflict | Two accepted sources appear to require incompatible behavior. | Apply chooser; if still unresolved, `CLARIFY`. | Record route status and select by tooling/context. |
| Required source is missing or rejected | Source ledger marks not found or rejected. | Do not use as evidence; `HALT` if required. | Restore source or remove dependency. |
| External claim would become doctrine | Claim lacks verification and route is not accepted. | `HALT: external_claim_unverified`. | Route to future research. |
| Scaffold file targeted before promotion gate | Appendix prerequisites missing or scope not scaffold_update. | `HALT: promotion_gate_failed`. | Create required appendix first. |
| Fetch-back unavailable after write | Written file cannot be fetched/read. | `HALT: validation_failed`; do not claim closure. | Retry fetch or inspect commit through repository tooling. |

## 13. Dry-run requirements

Dry-run is mandatory whenever a patch transport is used.

| Transport | Dry-run equivalent | Pass condition |
|---|---|---|
| SEARCH/REPLACE | `search-replace-py` dry run or equivalent exact-once matcher. | Every block matches exactly once and no file is touched before pass. |
| Unified diff | `git apply --check` or equivalent patch validation. | All hunks apply to the current file and patch scope is localized. |
| Full-body replacement | Pre-write validation against fetched target state and generated full content. | Path, scope, source refs, route status, and scaffold boundary all pass. |
| Live-edit instruction | Operator preview or read-before/write-after comparison. | Exact target region is identifiable and post-edit fetch-back validates content. |
| No-patch/manual-review | No mutation attempted. | HALT/CLARIFY records blocker and recovery path. |

Dry-run failure is not a partial success. The correct behavior is to stop, preserve safe state, and regenerate or clarify before mutation.

## 14. Fetch-back and diff validation checklist

```yaml
fetch_back_validation_checklist:
  written_file:
    exists: pass_required
    path_under_target_root: pass_required
    repository: leela-spec/MasterOfArts
    branch: main
  content:
    task_scope_repeated: pass_required
    intended_source_files_referenced: pass_required
    route_status_present_for_source_claims: pass_required
    transport_conflict_resolved_as_chooser: pass_required
    source_conflict_report_not_used_as_evidence: pass_required
  change_set:
    only_authorized_target_file_changed: pass_required
    scaffold_files_untouched: pass_required
    no_cross_repo_or_apex_target: pass_required
  closure:
    commit_or_write_identifier_recorded: pass_required
    display_url_recorded: pass_required
    next_task_identified: pass_required
```

## 15. Scaffold-promotion boundary

This appendix is evidence for later compact scaffold updates. It does not itself update scaffold files.

| Future scaffold surface | Allowed later use | Boundary |
|---|---|---|
| `TEMPLATES.md` | Compact edit-mode chooser and patch-output templates with appendix pointer. | Do not paste the full protocols into scaffold. |
| `MISTAKES.md` | Compact failure patterns for stale preimage, skipped dry-run, universalized transport rule, and false patch success. | Do not add long tool-specific workflows. |
| `BEST_PRACTICES.md` | Compact rule: choose patch transport by context and validate before mutation. | Do not declare SEARCH/REPLACE or unified diff universally preferred. |
| `ESSENCE.md` | No direct update from this appendix until essence-last gate. | Essence receives at most one compressed doctrine sentence after scaffold prerequisites. |
| `LEARNING_QUEUE.md` | Candidate-only item for formal transport tooling and missing conflict-report repair. | No accepted doctrine from missing source evidence. |

## 16. Integration dependencies for later scaffold updates

| Later task | Dependency from this appendix | Required compact promotion shape |
|---|---|---|
| `TASK-07 update TEMPLATES.md` | Patch transport chooser and minimal examples. | One compact chooser table or pointer, not the full appendix. |
| `TASK-08 update MISTAKES.md` | Failure-mode matrix. | Short entries for skipped dry-run, stale preimage, unsupported universal transport, and post-failure continuation. |
| `TASK-09 update BEST_PRACTICES.md` | Dry-run and fetch-back rules. | One rule requiring context-sensitive transport selection plus validation. |
| `TASK-10 update ESSENCE.md` | Only after other scaffold files are verified. | One compressed principle if needed; no schemas. |
| `TASK-11 update LEARNING_QUEUE.md` | Missing conflict report and tooling ownership questions. | Candidate-only unresolved questions. |

## 17. TASK-03 closure scope record

```yaml
task_scope_record:
  task_id: TASK-03
  task_type: appendix_create
  scope: Create a patch-transport appendix that selects between full-body replacement, SEARCH/REPLACE, unified diff, and live-edit instruction.
  target_file: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md
  output_format: markdown_file
  scaffold_mutation: none
  external_claim_promotion: none
  source_conflict_report_used_as_evidence: false
```
