---
promptflow_id: prompts_workflows_bounded_execution_guardrails
repo_boundary: single_repo_only
working_repo: leela-spec/MasterOfArts
target_repo: leela-spec/MasterOfArts
target_branch: main
target_agent: special_ops__prompts_workflows
target_kb_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/
artifact_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/
status: active
mode: bounded_artifact_manufacturing
created_for: runnable sister promptflow for Promptflows KB bounded execution guardrails
learning_source: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/LEARNINGS_PROMPTFLOW_HYGIENE_CLEAN_EXECUTION.md
source_template: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/PROMPTFLOW_HYGIENE_CLEAN_UNIFIED_DIFF_ARTIFACT_MANUFACTURING.md
---

# Promptflow: Prompts Workflows Bounded Execution Guardrails

## 0. Run manifest

This file is a runnable sister promptflow, not a generic guardrail memo.

```yaml
run_manifest:
  current_phase: MANUFACTURE
  mission: update this Promptflows KB promptflow so future promptflow-agent executions remain bounded, exact, and unambiguous
  exact_output_artifact: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/PROMPTFLOW_PROMPTS_WORKFLOWS_BOUNDED_EXECUTION_GUARDRAILS.md
  write_mode: update_existing_file_only
  source_input_files:
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/PROMPTFLOW_HYGIENE_CLEAN_UNIFIED_DIFF_ARTIFACT_MANUFACTURING.md
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/LEARNINGS_PROMPTFLOW_HYGIENE_CLEAN_EXECUTION.md
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/PROMPTFLOW_PROMPTS_WORKFLOWS_BOUNDED_EXECUTION_GUARDRAILS.md
  allowed_changes:
    - target_agent
    - target_kb_root
    - artifact_root
    - run_manifest
    - promptflows KB naming
    - learning-derived anti-drift rules
  forbidden_changes:
    - create_new_file
    - convert_to_general_advice
    - remove_runnable_payload
    - omit_exact_output_artifact
    - omit_current_phase
    - search_outside_listed_files
    - broad_governance_reread
    - stale_or_historical_promptflow_authority
  stop_after: write_and_validate_exact_output_artifact
  next_pending_artifact: none
```

## 1. Purpose

Create and maintain bounded, exact, machine-followable promptflow artifacts for the `special_ops__prompts_workflows` KB.

This promptflow exists to prevent context loss and scope drift during promptflow-agent executions.

It governs artifact creation only. Each execution must name the current phase, exact input files, exact output artifact, allowed actions, forbidden actions, validation checks, and stop condition.

## 2. Hard scope boundary

- **Only repo:** `leela-spec/MasterOfArts`.
- **Only branch:** `main`.
- **Only target root:** `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/`.
- **Only artifact root:** `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/`.
- **Allowed write type:** create or update exactly one artifact named by the active run manifest or operator contract.
- **Forbidden:** source expansion outside the explicit source-input list.
- **Forbidden:** broad governance, bootstrap, project-wide protocol, architecture, config, sibling-agent, stale historical, or repo-wide rereads.
- **Forbidden:** revisiting approved decisions unless the operator explicitly reopens DECIDE.
- **Forbidden:** inferred improvements, repairs, missing-content generation, style normalization, or helpful additions during MANUFACTURE/APPLY phases.

## 3. Source authority

Use only these source classes:

1. the source artifact explicitly named by the operator or run manifest;
2. the learning source explicitly named by the operator or run manifest;
3. the current target artifact, if updating an existing file;
4. current target file content for one active diff artifact, if the phase is diff manufacturing;
5. prior artifacts in this same appendix folder only to avoid duplicate numbering or duplicate work.

No other source is authorized by default.

If a requested source is missing, stop and report `missing_source_input`. Do not search for substitutes.

## 4. Phase lock

| Phase | Meaning | Allowed behavior | Stop rule |
|---|---|---|---|
| `DISCOVER` | broad research | only when explicitly requested | stop after findings or source list |
| `DESIGN` | tradeoffs and target design | produce design/options only | stop before artifact manufacturing |
| `DECIDE` | matrix/options for approval | produce matrix/options | stop for operator approval |
| `MANUFACTURE` | exact artifact creation | create/update only the named artifact | stop after validation |
| `VERIFY` | listed checks only | validate only declared checks | stop after report |
| `APPLY` | execute approved diffs/commands | no content generation; stop on failure | stop after apply/report |

Once a DECIDE output is approved, discovery and design are closed. Do not reopen them without explicit operator instruction.

## 5. Required execution contract

Before acting on any non-trivial promptflow or repo-write task, produce or consume a contract with this shape:

```yaml
task_contract:
  mode: DISCOVER | DESIGN | DECIDE | MANUFACTURE | VERIFY | APPLY | CLONE_AND_RETARGET
  user_wants:
  artifact_to_create_or_update:
  planned_artifact_type:
  source_inputs_allowed: []
  source_inputs_forbidden: []
  allowed_actions: []
  forbidden_actions: []
  stop_after:
  non_goals: []
```

If the operator has already supplied and approved the contract, execute it. Do not output another contract unless asked.

## 6. Required bounded-manufacturing prompt shape

Every MANUFACTURE request must resolve to:

```yaml
execution_mode: bounded_artifact_manufacturing
current_phase: MANUFACTURE
exact_input_files: []
exact_output_artifact:
allowed_actions: []
forbidden_actions:
  - source_expansion
  - broad_governance_reread
  - phase_reopen
  - extra_files
  - explanatory_recaps
validation_checks: []
stop_condition: stop_after_named_artifact
```

If `exact_output_artifact` or `current_phase` is missing, stop and report `missing_runnable_payload`. Do not infer a broad task.

## 7. Clone-and-retarget procedure

For CLONE_AND_RETARGET, execute exactly this sequence:

1. Read the source artifact.
2. Read the learning source.
3. Read the existing target artifact.
4. Preserve the source artifact's runnable structure.
5. Retarget only the allowed fields and naming.
6. Add or update the run manifest.
7. Integrate only learning-derived anti-drift rules.
8. Update exactly the target artifact.
9. Validate against the contract.
10. Stop.

Do not create a new file. Do not convert the artifact into generic guidance. Do not omit runnable payload.

## 8. Per-iteration manufacturing procedure

For each artifact iteration, execute exactly this sequence:

1. Read only the explicit input files for the active step.
2. Read only the active target file, if needed.
3. Create or update exactly one requested artifact.
4. Write it directly to the requested repo path.
5. Validate only the declared checks.
6. Stop.

Do not produce additional artifacts, recaps, alternate plans, sidecar files, generalized advice, or broad proof schemas unless explicitly requested.

## 9. Diff artifact requirements

Every `.diff` artifact must satisfy:

- starts with `diff --git a/... b/...`;
- contains exactly one target file diff unless the operator explicitly approved a multi-file patch;
- uses the approved target path exactly;
- writes only under the approved target root;
- contains no ellipses, placeholders, TODO patch text, or omitted hunks;
- contains no changes to unapproved files;
- is written to the repo artifact path when the user says to create/write it in repo.

## 10. Content control requirements

Artifacts must implement only approved rows, current-phase instructions, and named source inputs.

Deferred and rejected items must remain deferred or rejected. They must not be silently integrated.

Candidate, evidence, QA finding, promptflow placement, or scaffold placement does not become runtime truth without a governed promotion path.

## 11. Validation gate after each artifact

After writing an artifact, validate it against declared controls. Default controls:

```yaml
validation_gate:
  artifact_exists: true
  artifact_path_under_declared_artifact_root: true
  exactly_one_requested_artifact_created: true
  target_path_under_declared_target_root: true
  current_phase_present: true
  exact_output_artifact_present: true
  run_manifest_present: true
  content_maps_to_named_inputs: true
  no_unapproved_targets: true
  no_deferred_item_integrated: true
  no_rejected_item_integrated: true
  no_broad_governance_or_project_scope: true
  no_helpful_improvement_drift: true
  stopped_after_current_phase: true
```

If any check fails, stop and report the failed check. Do not proceed to the next artifact.

## 12. Final validation after a patch-artifact sequence

If the operator authorizes a multi-artifact patch sequence, the promptflow must include a concrete table with:

| Step | Target file | Artifact path | Status |
|---:|---|---|---|

After all artifacts exist, perform a final control pass:

1. Confirm expected artifact count.
2. Confirm each artifact has the expected format.
3. Confirm the observed changed-file set exactly matches the approved changed-file set.
4. Confirm every approved candidate/update row is represented or explicitly deferred/rejected.
5. Confirm no artifact writes outside the target root.
6. Emit a compact validation report only if explicitly required by the sequence.

No patch sequence is implied by this promptflow unless a run manifest or operator contract names it.

## 13. Codex/APPLY guardrails

A Codex or APPLY plan must define:

```yaml
codex_role: deterministic_patch_executor_only
git_apply_check_required: true
changed_file_allowlist_required: true
forbidden_paths_required: true
stop_on_failed_check: true
hand_edit_allowed: false
content_generation_allowed: false
three_way_merge_allowed: false
reject_mode_allowed: false
branch_creation_allowed: false
scope_widening_allowed: false
```

Codex must not invent, improve, rewrite, reformat, normalize, repair, or broaden content. If a diff fails, Codex stops and reports. It does not hand-edit.

## 14. Anti-drift rules from learning source

```yaml
learned_rules:
  - id: R-001
    rule: once operator approves a decision matrix, do not reopen discovery or design unless explicitly requested
  - id: R-002
    rule: for MANUFACTURE tasks, produce only the named artifact and stop
  - id: R-003
    rule: if user says write or create directly in repo, do not output artifact only in chat
  - id: R-004
    rule: every multi-file patch workflow needs a repo-local promptflow anchor with next_pending_artifact
  - id: R-005
    rule: every diff artifact must be one target file only and validated before continuing
  - id: R-006
    rule: Codex plans must define executor-only role, exact patch list, git apply --check, changed-file allowlist, forbidden paths, and stop-on-failure
  - id: R-007
    rule: no hand edits, no inferred improvements, no missing-content generation during APPLY phase
  - id: R-008
    rule: do not substitute a general guardrail memo for a runnable promptflow when a sister promptflow is requested
  - id: R-009
    rule: if artifact type planned does not match artifact type requested, stop before writing
```

## 15. Output-location rule

If the operator says any of these terms, write to repo unless explicitly told otherwise:

- `create file`
- `write directly into the repo`
- `create that file in ... folder`
- `appendix folder`
- `artifact path`
- `commit`
- `update the existing file`

Chat output should then be only a compact status report with path, commit SHA, and validation status.

## 16. Stop rule

For the next iteration, perform only the current requested phase and stop.

Do not continue to the next phase automatically unless the operator says `continue` or explicitly requests the next phase.

The current run manifest for this file has no next pending artifact after this update:

```text
none
```

## 17. Final report schema

```yaml
artifact_created: true | false
artifact_updated: true | false
path:
commit_sha:
validation:
  artifact_exists:
  artifact_path_under_declared_artifact_root:
  exactly_one_requested_artifact_created_or_updated:
  current_phase_present:
  exact_output_artifact_present:
  run_manifest_present:
  content_maps_to_named_inputs:
  no_unapproved_targets:
  no_broad_governance_or_project_scope:
  no_helpful_improvement_drift:
status: written_to_main | stopped
next_pending_artifact:
```
