---
name: apex-sync
description: >
  Use this skill when the operator asks to compute Apex read-side synchronization checks, including next actions, blockers, stalls, registry rebuilds, drift, depends_on validation, priority, urgency, unlock depth, or focus candidates. Accepts Apex task files under apex-meta/epics/. Produces deterministic reports through apex_sync.py. Does not capture projects, mutate task status, write session narrative, author handoff, or validate operator decisions.
---

# Apex Sync

## Skill Contract

```yaml
skill_contract:
  primary_output: sync_report_bundle
  output_role: deterministic_read_side_synchronization
  package_path: ".claude/skills/apex-sync/"

  durable_paths:
    base: "apex-meta/"
    epics: "apex-meta/epics/"
    registry: "apex-meta/registry/index.md"
    handoff: "apex-meta/handoff/"
    scripts: "apex-meta/scripts/"

  canonical_source:
    package_boundary: "references/sync-cluster-contract.md"
    command_interface: "references/script-command-contract.md"
    registry_and_drift_rules: "references/registry-and-drift-rules.md"
    scoring_and_focus_rules: "references/scoring-and-focus-rules.md"
    python_cli_contract: "apex-meta/scripts/apex_sync.py"

  process_scope:
    owns:
      - PM4_compute_next_action
      - PM5_detect_blockers
      - PM7_detect_stall
      - PM8_generate_work_registry
      - KB4_rebuild_index
      - KB5_detect_drift
      - PD1_compute_priority_score
      - PD2_compute_urgency_score
      - PD3_compute_unlock_depth
      - PD4_compute_focus_candidates
    does_not_own:
      - PM1_project_capture
      - PM2_human_decomposition
      - PM6_status_mutation
      - KB1_session_narrative
      - KB2_state_delta_interpretation
      - KB3_entity_synthesis
      - KB6_next_session_authoring
      - PD5_operator_validation
      - PD6_planning_feed_authoring

  required_outputs:
    - next_action_report
    - blocker_report
    - registry_report
    - stall_report
    - drift_report
    - score_report
    - focus_candidate_report
    - dependency_validation_report

  script_policy:
    python_allowed: true
    bash_allowed: false
    typescript_allowed: false
    javascript_allowed: false
    shell_out_allowed: false
    external_dependencies_allowed: false
    standard_library_only: true
    read_only_by_default: true

  registry_policy:
    default_mode: dry_run
    only_allowed_write_path: "apex-meta/registry/index.md"
    write_requires:
      - registry_subcommand
      - explicit_non_dry_run

  non_goals:
    - "Do not capture projects."
    - "Do not decompose work by reasoning."
    - "Do not mutate task status."
    - "Do not write session narrative."
    - "Do not synthesize KB entities."
    - "Do not author next-session context."
    - "Do not produce planning prose."


## Supporting Files

supporting_files:  - path: "references/sync-cluster-contract.md"    read_when:      - validating_package_boundary      - clarifying_apex_plan_boundary      - clarifying_apex_session_boundary      - checking_process_scope  - path: "references/script-command-contract.md"    read_when:      - running_apex_sync_py      - validating_subcommand_output      - checking_exit_code_policy      - checking_json_output_policy  - path: "references/registry-and-drift-rules.md"    read_when:      - rebuilding_registry      - detecting_drift      - handling_malformed_task_files      - validating_registry_schema  - path: "references/scoring-and-focus-rules.md"    read_when:      - computing_priority_score      - computing_urgency_score      - computing_unlock_depth      - ordering_focus_candidates  - path: "package-manifest.md"    read_when:      - operator_inspects_package_structure      - validating_file_inventory      - checking_canonical_sources  - path: "../../../apex-meta/scripts/apex_sync.py"    read_when:      - executing_sync_subcommands      - validating_python_cli_contract      - checking_registry_write_behavior
```

## Procedure

1. **Load scope.** Read the operator request and identify whether the requested report is next_action_report, blocker_report, registry_report, stall_report, drift_report, score_report, focus_candidate_report, or dependency_validation_report.
2. **Load the command contract.** Read `references/script-command-contract.md` before presenting or running any `apex_sync.py` command.
3. **Select the subcommand.** Use `next`, `blockers`, `registry`, `stall`, `drift`, or `score` according to the requested report, and keep `--dry-run true` unless the operator explicitly requests `registry` with non-dry-run behavior.
4. **Run deterministic computation.** Use `apex-meta/scripts/apex_sync.py` with `--root`, `--json` when machine-readable output is needed, and `--dry-run` according to the command contract.
5. **Return exact reports.** Preserve the script’s report names and review_flags without adding planning rationale, session narrative, or operator-validation prose.
6. **Apply failure modes.** If the script reports malformed_frontmatter, missing_task_id, unsupported_status, missing_dependency_target, circular_dependency_risk, blocked_without_reason, stale_task_candidate, registry_out_of_date, drift_detected, or script_failed, return the report and apply the matching correction from Failure Modes.

## Failure Modes

```
failure_modes:  malformed_frontmatter:    trigger: "A task file has missing, malformed, or unsupported frontmatter."    correction: "Report malformed_frontmatter and continue processing other task files."  missing_task_id:    trigger: "A task file lacks integer id in frontmatter or duplicates another id."    correction: "Report missing_task_id and exclude the invalid task from exact graph computation."  unsupported_status:    trigger: "A task status is not open, in-progress, blocked, done, or deferred."    correction: "Report unsupported_status and keep the task visible in validation output."  missing_dependency_target:    trigger: "A depends_on value references an id that does not exist in loaded task files."    correction: "Report missing_dependency_target in dependency_validation_report."  circular_dependency_risk:    trigger: "The depends_on graph contains a cycle."    correction: "Report circular_dependency_risk and do not treat the affected graph as fully valid."  blocked_without_reason:    trigger: "A task has status blocked but blocked_by is empty."    correction: "Report blocked_without_reason and keep the task in blocker_report."  stale_task_candidate:    trigger: "A non-done, non-deferred task exceeds the stall threshold based on task timestamps."    correction: "Report stale_task_candidate without mutating task status."  registry_out_of_date:    trigger: "The generated registry content differs from apex-meta/registry/index.md."    correction: "Report registry_out_of_date and require explicit registry non-dry-run before writing."  drift_detected:    trigger: "Current source task files and registry content do not match."    correction: "Report drift_detected and include the regenerated registry content for review."  script_failed:    trigger: "apex_sync.py exits with a nonzero script_exit_code."    correction: "Return script_stdout, script_stderr when available, and do not infer missing report data."
```

## Output Requirements

```
output_requirements:  reports:    next_action_report:      produced_by: "apex_sync.py next"    blocker_report:      produced_by: "apex_sync.py blockers"    registry_report:      produced_by: "apex_sync.py registry"    stall_report:      produced_by: "apex_sync.py stall"    drift_report:      produced_by: "apex_sync.py drift"    score_report:      produced_by: "apex_sync.py score"    focus_candidate_report:      produced_by: "apex_sync.py score"    dependency_validation_report:      produced_by:        - "apex_sync.py next"        - "apex_sync.py blockers"  required_report_fields:    - review_flags    - dry_run    - script_exit_code  allowed_short_explanations:    - reason  must_not_include:    - planning_rationale    - session_narrative    - status_mutation_claim    - operator_validation_claim    - next_session_context
```

## Completion Gate

```
completion_gate:  requested_report_identified: true  command_contract_checked: true  apex_sync_py_subcommand_selected: true  dry_run_policy_preserved: true  registry_write_policy_preserved: true  exact_report_returned: true  failure_modes_applied_when_needed: true  apex_plan_boundary_preserved: true  apex_session_boundary_preserved: true
```