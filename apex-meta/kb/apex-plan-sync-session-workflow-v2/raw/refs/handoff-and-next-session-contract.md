# Handoff and Next Session Contract

## H6_file_set

~~~yaml
H6_file_set:
  handoff_root: apex-meta/handoff/
  required_files:
    - task_plan.md
    - findings.md
    - progress.md
    - next-session.md

  next_session_required_sections:
    - Current Step
    - Open Items
    - Risks
    - Decisions Made
    - Next Actions
~~~

The H6 handoff format is the final artifact contract for `apex-session`. The files capture the plan, durable findings, progress log, and clean continuation context needed by the next session or planning layer.

## task_plan_contract

~~~yaml
task_plan_contract:
  file_name: task_plan.md
  purpose: >
    Preserve the session goal, current step, phase structure, decisions, open
    items, risks, and next actions so the next session can resume without
    relying on chat memory.

  exact_sections:
    - Goal
    - Current Step
    - Phases
    - Decisions
    - Open Items
    - Risks
    - Next Actions

  required_behavior:
    - state_goal_in_operator_language
    - identify_current_step
    - preserve_phases_without_over_planning
    - record_decisions_made
    - carry_open_items_forward
    - carry_risks_forward
    - avoid_exact_rank_or_score_computation
~~~

## findings_contract

~~~yaml
findings_contract:
  file_name: findings.md
  purpose: >
    Preserve durable findings, decisions made, source notes, open questions,
    and operator validations that should survive the current session.

  exact_sections:
    - Durable Findings
    - Decisions Made
    - Source Notes
    - Open Questions
    - Operator Validations

  required_behavior:
    - include_durable_findings_only
    - preserve_raw_source_ref
    - preserve_raw_source_path
    - record_source_conflict_when_present
    - record_operator_validation_when_present
    - avoid_unverified_claims
~~~

## progress_contract

~~~yaml
progress_contract:
  file_name: progress.md
  purpose: >
    Preserve the session log, actions taken, status mutations, state deltas,
    errors, review flags, and next step for continuity.

  exact_sections:
    - Session Log
    - Actions Taken
    - Status Mutations
    - State Deltas
    - Errors or Review Flags
    - Next Step

  required_behavior:
    - log_actions_taken
    - log_status_mutation_records
    - log_state_delta_summary
    - log_errors_and_review_flags
    - preserve_operator_validation_record
    - record_next_step_without_computing_final_rank
~~~

## next_session_contract

~~~yaml
next_session_contract:
  file_name: next-session.md
  purpose: >
    Provide the smallest clean context packet that lets the next session resume
    safely and lets apex-plan consume current context without reconstructing
    chat history.

  exact_sections:
    - Current Step
    - Open Items
    - Risks
    - Decisions Made
    - Next Actions

  required_behavior:
    - summarize_current_step
    - list_open_items
    - list_risks
    - list_decisions_made
    - list_next_actions
    - include_review_flags_when_relevant
    - include_raw_source_ref_and_raw_source_path_when_needed
~~~

## required_next_session_sections

~~~yaml
required_next_session_sections:
  exact_order:
    - Current Step
    - Open Items
    - Risks
    - Decisions Made
    - Next Actions

  section_rules:
    Current Step:
      must_capture: current operative session position
    Open Items:
      must_capture: unresolved context, missing inputs, source conflicts, unfinished validation
    Risks:
      must_capture: scope drift, invalid status risk, duplicate entity risk, raw source gaps
    Decisions Made:
      must_capture: confirmed operator validations and durable decisions
    Next Actions:
      must_capture: actions for the next session or planning layer without final ranking
~~~

## read_before_decide_rule

~~~yaml
read_before_decide_rule:
  principle: >
    Before producing final handoff or mutation records, read the available plan,
    findings, progress, next-session context, raw sources, and operator
    instructions.

  required_reads_when_available:
    - task_plan.md
    - findings.md
    - progress.md
    - next-session.md
    - raw_source_ref
    - raw_source_path
    - operator_instructions

  missing_context_behavior:
    - mark_missing_input
    - preserve_missing_path
    - continue_with_available_evidence_if_safe
    - do_not_invent_source_basis
~~~

## planning_layer_feed_contract

~~~yaml
planning_layer_feed_contract:
  artifact_name: planning_feed
  primary_consumer: apex-plan
  purpose: >
    Provide the planning layer with clean next-session context, durable
    findings, unresolved context, risks, decisions made, and source references.

  include:
    - Current Step
    - Open Items
    - Risks
    - Decisions Made
    - Next Actions
    - state_delta_summary
    - entity_update_record
    - raw_source_ref
    - raw_source_path
    - review_flags

  exclude:
    - exact_next_task_ranking
    - blocker_scan
    - registry_rebuild
    - drift_detection
    - priority_score_computation
    - urgency_score_computation
    - unlock_depth_computation
    - new_project_decomposition
~~~

## missing_context_behavior

~~~yaml
missing_context_behavior:
  when_required_input_missing:
    add_review_flags:
      - missing_input
    write_to:
      - Open Items
      - Errors or Review Flags
    use_marker: USER_INPUT_REQUIRED

  when_raw_source_missing:
    add_review_flags:
      - raw_source_missing
    preserve_available_raw_source_ref: true
    preserve_available_raw_source_path: true

  when_scope_drift_detected:
    add_review_flags:
      - scope_drift
    route_to_apex_plan_or_apex_sync: true
~~~

## final_handoff_acceptance_checks

~~~yaml
final_handoff_acceptance_checks:
  required_file_count: 4
  required_files_present:
    - task_plan.md
    - findings.md
    - progress.md
    - next-session.md
  task_plan_sections_exact:
    - Goal
    - Current Step
    - Phases
    - Decisions
    - Open Items
    - Risks
    - Next Actions
  findings_sections_exact:
    - Durable Findings
    - Decisions Made
    - Source Notes
    - Open Questions
    - Operator Validations
  progress_sections_exact:
    - Session Log
    - Actions Taken
    - Status Mutations
    - State Deltas
    - Errors or Review Flags
    - Next Step
  next_session_sections_exact:
    - Current Step
    - Open Items
    - Risks
    - Decisions Made
    - Next Actions
  no_forbidden_sync_or_plan_behavior: true
  raw_source_basis_preserved_when_available: true
  unresolved_context_visible: true
~~~