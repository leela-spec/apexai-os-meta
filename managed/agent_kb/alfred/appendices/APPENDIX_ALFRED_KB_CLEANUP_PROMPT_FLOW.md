# APPENDIX_ALFRED_KB_CLEANUP_PROMPT_FLOW

## Purpose

Controlled prompt flow for cleaning the Alfred knowledge base in `leela-spec/apexai-os-meta`.

This appendix is a planning artifact for Codex. It defines an iterative process for auditing high-impact information, creating one unified-diff proposal per affected file, and stopping for operator validation before any cleanup is applied.

## Status

```yaml
artifact_id: APPENDIX_ALFRED_KB_CLEANUP_PROMPT_FLOW
repo_scope: leela-spec/apexai-os-meta
kb_scope: managed/agent_kb/alfred/
artifact_type: prompt_flow_appendix
execution_owner: codex_after_operator_validation
operator_decisions_validated: true
patch_application_allowed_by_this_file: false
patch_file_creation_allowed_by_this_file: true
requires_operator_validation_before_apply: true
```

## Non-negotiable scope

```yaml
allowed_repo: leela-spec/apexai-os-meta
allowed_primary_scope:
  - managed/agent_kb/alfred/
allowed_patch_output_scope:
  - managed/agent_kb/alfred/appendices/cleanup_patch_proposals/
forbidden_work:
  - editing any other repository
  - editing MasterOfArts
  - editing Leela product files outside Alfred KB
  - applying cleanup patches before operator validation
  - adding improvements not explicitly defined here
```

## Operator-validated decisions

```yaml
validated_decisions:
  delete_obsolete_patch_artifact: true
  delete_working_handover_files: true
  delete_redirect_files_after_high_impact_integration_check: true
  source_manifest_and_coverage_audit_todos_after_cleanup: true
  actual_application_by_codex_last_step: true
```

## Hard guardrails

1. Stay inside `leela-spec/apexai-os-meta` and `managed/agent_kb/alfred/`.
2. Do not apply patches during proposal stage.
3. Create one unified diff proposal file per target file.
4. Do not create one giant cleanup patch.
5. Do not silently add improvements.
6. Any improvement idea must be recorded as `operator_decision_needed` and left unapplied.
7. Do not delete a file until high-impact information is confirmed integrated into the five-file scaffold, likely-to-stay appendices, or source/audit controls.
8. Do not use placeholders such as `...` inside generated diffs.
9. Every generated diff must pass `git apply --check` before later application.
10. Every final application step must be one file at a time with fetch-back verification.

## Target classes

### Class A — approved deletion after patch proposal

| Target | Decision | Context |
|---|---|---|
| `managed/agent_kb/alfred/appendices/APEX_ALFRED_CANONICAL_PATCH_DIFFS_OPTION_B.patch` | delete | Historical patch artifact; promoted content should already be represented in canonical files. |

### Class B — approved deletion after reference cleanup

| Target | Decision | Likely integration / reference cleanup target |
|---|---|---|
| `managed/agent_kb/alfred/working/APEX_VARIABLES_HANDOFF_DECISION_LOCK.md` | delete_after_reference_cleanup | `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, process-handover appendix, source/audit controls |
| `managed/agent_kb/alfred/working/APEX_ALFRED_KB_INTEGRATION_PROMPT_FLOW.md` | delete_after_reference_cleanup | `BEST_PRACTICES.md`, source/audit controls |
| `managed/agent_kb/alfred/working/ALFRED_WORKFLOW_DECISION_LOCK.md` | delete_after_reference_cleanup | workflow appendix, source/audit controls |
| `managed/agent_kb/alfred/working/ALFRED_WORKFLOW_PREFILLED_QA.md` | delete_after_high_impact_check | `LEARNING_QUEUE.md` only if candidate remains |
| `managed/agent_kb/alfred/working/APEX_ALFRED_CANONICAL_PATCH_HANDOVER.md` | delete_after_reference_cleanup | source/audit controls only if provenance remains needed |

### Class C — approved deletion only after high-impact integration check

| File | Predefined decision | Most likely target | Operator options | Default recommendation |
|---|---|---|---|---|
| `managed/agent_kb/alfred/AGENT_CARD.md` | delete_after_check | `ESSENCE.md`; maybe `TEMPLATES.md` | A delete, B extract missing content, C keep redirect | A if no unique high-impact content |
| `managed/agent_kb/alfred/DOCTRINE.md` | delete_after_check | `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md` | A delete, B extract missing content, C keep redirect | A if no unique high-impact content |
| `managed/agent_kb/alfred/ROLE_BOUNDARIES.md` | delete_after_check | `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md` | A delete, B extract boundary detail, C preserve as appendix | B if unique detail exists, else A |
| `managed/agent_kb/alfred/HANDOFF_SCHEMA.md` | delete_after_check | `TEMPLATES.md` | A delete, B extract missing template, C keep redirect | A if no unique form |
| `managed/agent_kb/alfred/ROUTING_CONTRACT.md` | delete_after_check | `appendices/APPENDIX_ROUTING_MATRIX.md`, `BEST_PRACTICES.md`, `TEMPLATES.md`, `MISTAKES.md` | A delete, B extract to appendix, C keep redirect | B if unique matrix detail exists, else A |
| `managed/agent_kb/alfred/WORKFLOW_PLAYBOOK.md` | delete_after_check | `appendices/APPENDIX_WORKFLOW_PLAYBOOK.md`, `BEST_PRACTICES.md`, `TEMPLATES.md`, `MISTAKES.md` | A delete, B extract to appendix, C keep redirect | B if unique stop/procedure detail exists, else A |

### Class D — likely-to-stay appendices

These are not deletion targets in this flow unless the operator later approves a separate appendix compression pass.

| Appendix | Predefined decision | Why likely stays |
|---|---|---|
| `appendices/APPENDIX_ROUTING_MATRIX.md` | keep | Detailed route lookup likely too bulky for canonical scaffold. |
| `appendices/APPENDIX_WORKFLOW_PLAYBOOK.md` | keep | Detailed workflow procedures and stop conditions likely too bulky for canonical scaffold. |
| `appendices/APPENDIX_PROCESS_HANDOVER_PRIORITY.md` | keep | High-impact machine contract detail for `EVD / IMP / RSK + URG`, readiness, lane, hard flags, P0-P3. |
| `appendices/APPENDIX_DAILY_COMMAND_BOARD_AND_HANDOFFS.md` | keep | Operational board and MetaOps handoff detail. |
| `appendices/APPENDIX_SESSION_EXPORT_OPSTATE_AND_TRACKING.md` | keep | Protects trace/state separation and OpState delta flow. |
| `appendices/APPENDIX_PATTERN_LEARNING_AND_RHYTHM.md` | keep_for_now | Candidate-first pattern learning and Rhythm profile detail; possible future trim candidate. |

### Class E — source-index/chat files outside Alfred KB root

No patches are authorized for these files in this prompt flow.

| Area | Decision | Reason |
|---|---|---|
| `agent_kb_source_indexes/CreatingAlfred/**` | no_action_now | Outside runtime Alfred KB root; may support later source/audit pass. |
| chat-history or prompt-history files outside `managed/agent_kb/alfred/` | no_action_now | Evidence/provenance only; not runtime KB. |

## Required reference scan before any deletion proposal

Scan references inside:

```yaml
required_reference_scan_scope:
  - managed/agent_kb/alfred/README.md
  - managed/agent_kb/alfred/ESSENCE.md
  - managed/agent_kb/alfred/BEST_PRACTICES.md
  - managed/agent_kb/alfred/MISTAKES.md
  - managed/agent_kb/alfred/TEMPLATES.md
  - managed/agent_kb/alfred/LEARNING_QUEUE.md
  - managed/agent_kb/alfred/SOURCE_MANIFEST.md
  - managed/agent_kb/alfred/COVERAGE_AUDIT.md
  - managed/agent_kb/alfred/appendices/
```

Classify references as:

```yaml
reference_classification:
  stale_after_delete: update reference in same cleanup batch
  provenance_needed: replace with commit/reference note or canonical target
  active_dependency: stop and request operator decision
  harmless_history: leave only if source/audit controls still make sense
```

## Iterative Codex flow

### Phase 0 — initialize

1. Confirm repo is `leela-spec/apexai-os-meta`.
2. Confirm work is under `managed/agent_kb/alfred/`.
3. Create or refresh `managed/agent_kb/alfred/appendices/cleanup_patch_proposals/`.
4. Do not modify target cleanup files.
5. Do not delete anything.

### Phase 1 — current-state inventory

For each target in Classes A-C:

1. Read the file.
2. Record existence: `exists | missing | blocked`.
3. Record current blob SHA or commit context when available.
4. Search references in required scan scope.
5. Summarize whether high-impact content remains unintegrated.

Output:

```text
managed/agent_kb/alfred/appendices/cleanup_patch_proposals/00_CURRENT_STATE_INVENTORY.md
```

### Phase 2 — decision matrix

Create:

```text
managed/agent_kb/alfred/appendices/cleanup_patch_proposals/01_DECISION_MATRIX.md
```

Required columns:

| Field | Meaning |
|---|---|
| `target_file` | Exact repo path. |
| `current_status` | exists / missing / blocked. |
| `operator_decision` | validated delete / delete after check / no action / operator decision needed. |
| `high_impact_info_found` | yes / no / unclear. |
| `integration_target` | scaffold file or appendix where info belongs. |
| `references_to_update` | exact files needing reference cleanup. |
| `patch_file_to_create` | exact diff proposal file path. |
| `apply_allowed_now` | always `false` at proposal stage. |
| `operator_options` | predefined A/B/C options. |
| `codex_recommendation` | recommended option and rationale. |

### Phase 3 — integration extraction

If a redirect or working file still contains high-impact information not integrated elsewhere:

1. Do not delete yet.
2. Add an integration proposal row in `01_DECISION_MATRIX.md`.
3. Generate a separate patch proposal for the likely integration target.
4. Mark that patch as `operator_decision_needed` unless the integration is already explicitly defined in this prompt flow.

Likely integration targets:

```yaml
integration_targets:
  identity_authority_boundary: managed/agent_kb/alfred/ESSENCE.md
  operating_method: managed/agent_kb/alfred/BEST_PRACTICES.md
  failure_pattern: managed/agent_kb/alfred/MISTAKES.md
  reusable_template: managed/agent_kb/alfred/TEMPLATES.md
  candidate_future_work: managed/agent_kb/alfred/LEARNING_QUEUE.md
  provenance_or_read_status: managed/agent_kb/alfred/SOURCE_MANIFEST.md
  validation_or_gap_status: managed/agent_kb/alfred/COVERAGE_AUDIT.md
  detailed_routing: managed/agent_kb/alfred/appendices/APPENDIX_ROUTING_MATRIX.md
  detailed_workflow: managed/agent_kb/alfred/appendices/APPENDIX_WORKFLOW_PLAYBOOK.md
  process_priority_detail: managed/agent_kb/alfred/appendices/APPENDIX_PROCESS_HANDOVER_PRIORITY.md
  daily_board_detail: managed/agent_kb/alfred/appendices/APPENDIX_DAILY_COMMAND_BOARD_AND_HANDOFFS.md
  session_export_opstate_tracking_detail: managed/agent_kb/alfred/appendices/APPENDIX_SESSION_EXPORT_OPSTATE_AND_TRACKING.md
  pattern_learning_rhythm_detail: managed/agent_kb/alfred/appendices/APPENDIX_PATTERN_LEARNING_AND_RHYTHM.md
```

### Phase 4 — create individual unified diff proposal files

Create one `.diff` file per target file that needs a change.

Directory:

```text
managed/agent_kb/alfred/appendices/cleanup_patch_proposals/
```

Naming format:

```text
NNNN_<action>__<path_slug>.diff
```

Each diff must start with:

```diff
# cleanup_patch_proposal_v1
# target_file: <exact path>
# action: delete | update | create | move
# apply_allowed_now: false
# operator_validation_required: true
# source_basis: <files checked>
# high_impact_info_integrated: yes | no | not_applicable | unclear
# stop_condition: do not apply if git apply --check fails or operator has not validated
```

Diff requirements:

```yaml
unified_diff_requirements:
  one_target_file_per_diff: true
  exact_current_file_read_before_diff: true
  no_placeholders: true
  no_ellipsis: true
  no_combined_patch: true
  include_standard_header: true
  git_apply_check_required: true
  apply_patch_now: false
```

### Phase 5 — patch proposal index

Create:

```text
managed/agent_kb/alfred/appendices/cleanup_patch_proposals/02_PATCH_INDEX.md
```

Required columns:

| Field | Meaning |
|---|---|
| `patch_file` | Diff proposal path. |
| `target_file` | File the patch would change. |
| `action` | delete / update / create / move. |
| `depends_on` | Prior patch that must be applied first. |
| `operator_status` | pending / approved / rejected / needs revision. |
| `git_apply_check` | pass / fail / not_run. |
| `codex_notes` | Short notes. |

### Phase 6 — operator validation checkpoint

Stop and present:

1. Current-state inventory.
2. Decision matrix.
3. Patch index.
4. Any `operator_decision_needed` rows.
5. No applied changes.

### Phase 7 — final application step, only after operator approval

When and only when the operator approves:

1. Apply one patch at a time.
2. Run `git apply --check` before applying each patch.
3. Apply the patch.
4. Fetch/read the changed path or confirm deletion.
5. Record result in `03_APPLY_REPORT.md`.
6. Stop on first failure.

Recommended apply order:

```yaml
recommended_apply_order:
  - integration updates into scaffold or appendices
  - source/audit/reference updates
  - obsolete patch artifact deletion
  - working handover deletions
  - redirect deletions
  - final README/source/audit cleanup
```

## Decision matrix seed

| ID | Target | Predefined decision | Context | Most likely integration target | Default recommendation |
|---|---|---|---|---|---|
| D001 | `appendices/APEX_ALFRED_CANONICAL_PATCH_DIFFS_OPTION_B.patch` | delete | Historical patch artifact. | none if canonical files verified | delete |
| D002 | `working/APEX_VARIABLES_HANDOFF_DECISION_LOCK.md` | delete after reference cleanup | Working lock. | scaffold, process-handover appendix, source/audit | delete after refs |
| D003 | `working/APEX_ALFRED_KB_INTEGRATION_PROMPT_FLOW.md` | delete after reference cleanup | Working prompt flow. | `BEST_PRACTICES.md`, source/audit | delete after refs |
| D004 | `working/ALFRED_WORKFLOW_DECISION_LOCK.md` | delete after reference cleanup | Parent workflow lock. | workflow appendix, source/audit | delete after refs |
| D005 | `working/ALFRED_WORKFLOW_PREFILLED_QA.md` | delete after integration check | Support QA/context. | `LEARNING_QUEUE.md` if candidate remains | delete unless candidate found |
| D006 | `working/APEX_ALFRED_CANONICAL_PATCH_HANDOVER.md` | delete after reference cleanup | Non-canonical completed handover. | source/audit only if provenance needed | delete after refs |
| D007 | `AGENT_CARD.md` | delete after integration check | Absorbed redirect. | `ESSENCE.md`, maybe `TEMPLATES.md` | delete if no unique content |
| D008 | `DOCTRINE.md` | delete after integration check | Absorbed redirect. | `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md` | delete if no unique content |
| D009 | `ROLE_BOUNDARIES.md` | delete after integration check | Boundary redirect. | `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md` | extract if unique detail, else delete |
| D010 | `HANDOFF_SCHEMA.md` | delete after integration check | Handoff-form redirect. | `TEMPLATES.md` | delete if no unique form |
| D011 | `ROUTING_CONTRACT.md` | delete after integration check | Moved routing redirect. | routing appendix, canonical files | extract if unique, else delete |
| D012 | `WORKFLOW_PLAYBOOK.md` | delete after integration check | Moved workflow redirect. | workflow appendix, canonical files | extract if unique, else delete |
| D013 | `README.md` | update if references change | Folder index must match cleanup state. | `README.md` | update after final decisions |
| D014 | `SOURCE_MANIFEST.md` | update after cleanup | Ledger must not cite deleted working files as active. | `SOURCE_MANIFEST.md` | defer to source/audit todo unless blocking |
| D015 | `COVERAGE_AUDIT.md` | update after cleanup | Audit must reflect final cleanup/source status. | `COVERAGE_AUDIT.md` | defer to source/audit todo unless blocking |
| D016 | source-index/chat files outside KB root | no action now | Evidence/provenance outside runtime KB. | future source/audit pass | no action now |
| D017 | full appendices | keep for now | Retrieval detail likely too bulky for scaffold. | appendices | keep now |

## Improvement handling rule

If Codex sees an improvement not defined above, it must not patch it.

Record only:

```yaml
operator_decision_needed:
  idea:
  why_it_might_help:
  affected_files:
  risk:
  recommended_timing:
  no_patch_created: true
```

## Proposal done definition

```yaml
proposal_done_definition:
  current_state_inventory_created: true
  decision_matrix_created: true
  one_diff_file_per_target_change_created: true
  patch_index_created: true
  no_target_cleanup_patch_applied: true
  all_unvalidated_improvements_marked_operator_decision_needed: true
  operator_validation_requested: true
```

## Application done definition

```yaml
application_done_definition:
  operator_approved_exact_patch_set: true
  patches_applied_one_file_at_a_time: true
  git_apply_check_passed_before_each_apply: true
  fetch_back_or_deletion_confirmation_done_after_each_apply: true
  apply_report_created: true
  source_manifest_and_coverage_audit_todos_recorded: true
```
