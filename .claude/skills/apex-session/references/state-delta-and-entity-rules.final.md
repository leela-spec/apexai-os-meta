# State Delta and Entity Rules

## purpose

~~~yaml
purpose:
  file_role: state_delta_and_entity_update_contract
  package_name: apex-session
  goal: >
    Define how apex-session extracts state deltas from current session evidence,
    preserves raw source references, creates entity update records, flags source
    conflicts and duplicate entity risks, and prepares clean planning_feed
    material without computing final ranking or rebuilding indexes.

llm_wiki:
  allowed_claim: conceptual/adapted source for raw/source/entity/index/audit discipline
  forbidden_claim: copied exact update-index.py behavior
~~~

## state_delta_summary_schema

~~~yaml
state_delta_summary_schema:
  required_fields:
    state_delta_id: string
    task_id: string_or_USER_INPUT_REQUIRED
    task_title: string_or_USER_INPUT_REQUIRED
    raw_source_ref: string_or_USER_INPUT_REQUIRED
    raw_source_path: string_or_USER_INPUT_REQUIRED
    delta_summary: string
    affected_fields:
      type: array
      examples:
        - status_before
        - status_after
        - status_change_reason
        - depends_on
        - next_session_context
        - planning_feed
    source_conflict: boolean
    review_flags:
      type: array
      allowed_values:
        - missing_input
        - invalid_status
        - source_conflict
        - duplicate_entity_risk
        - unresolved_dependency
        - scope_drift
        - operator_confirmation_missing
        - raw_source_missing

  required_behavior:
    - preserve_raw_source_ref_when_available
    - preserve_raw_source_path_when_available
    - flag_missing_raw_source_instead_of_inventing
    - flag_source_conflict_instead_of_resolving_silently
    - preserve_unresolved_context_for_next_session
~~~

## entity_update_record_schema

~~~yaml
entity_update_record_schema:
  required_fields:
    entity_id: string_or_USER_INPUT_REQUIRED
    entity_update_type:
      type: enum_string
      allowed_examples:
        - create
        - update
        - split
        - merge_candidate
        - archive_candidate
        - reference_only
    entity_summary: string
    raw_source_ref: string_or_USER_INPUT_REQUIRED
    raw_source_path: string_or_USER_INPUT_REQUIRED
    source_conflict: boolean
    review_flags:
      type: array
      allowed_values:
        - missing_input
        - invalid_status
        - source_conflict
        - duplicate_entity_risk
        - unresolved_dependency
        - scope_drift
        - operator_confirmation_missing
        - raw_source_missing

  optional_fields:
    task_id: string
    task_title: string
    state_delta_id: string
    depends_on:
      type: int_array
      rule: all_depends_on_items_must_be_done_before_actionable
    planning_feed: string
    next_session_context: string
~~~

## raw_source_preservation_policy

~~~yaml
raw_source_preservation_policy:
  preserve_exact_references: true
  preserve_exact_paths: true
  never_rewrite_raw_source_content: true
  never_treat_missing_source_as_verified: true

  required_when_available:
    - raw_source_ref
    - raw_source_path

  when_missing:
    raw_source_ref: USER_INPUT_REQUIRED
    raw_source_path: USER_INPUT_REQUIRED
    review_flags:
      - raw_source_missing

  output_locations:
    - findings.md
    - progress.md
    - next-session.md
    - state_delta_summary
    - entity_update_record
    - planning_feed
~~~

## raw_source_path_policy

~~~yaml
raw_source_path_policy:
  accepted_path_forms:
    - repo_relative_path
    - local_project_path
    - operator_supplied_path
    - prior_handoff_path

  path_rules:
    - keep_original_spelling_and_spacing
    - do_not_normalize_without_recording_original
    - do_not_infer_file_existence_without_read_or_operator_basis
    - include_path_drift_or_missing_path_in_review_flags

  large_or_unavailable_source_behavior:
    - preserve_pointer_or_reference
    - summarize_available_evidence_only
    - mark_missing_input_if_required_content_is_unavailable
~~~

## source_conflict_policy

~~~yaml
source_conflict_policy:
  conflict_definition: >
    A source_conflict exists when two or more task/session/raw sources support
    incompatible state deltas, entity meanings, status values, or next actions.

  required_behavior:
    - preserve_each_conflicting_raw_source_ref
    - preserve_each_conflicting_raw_source_path_when_available
    - set_source_conflict_true
    - add_source_conflict_to_review_flags
    - record_conflict_in_findings_md
    - carry_conflict_into_next_session_md_open_items

  forbidden_behavior:
    - silently_choose_one_source
    - erase_conflicting_source
    - mark_conflict_resolved_without_operator_validation
    - compute_final_rank_to_break_conflict
~~~

## duplicate_entity_risk_policy

~~~yaml
duplicate_entity_risk_policy:
  risk_definition: >
    duplicate_entity_risk exists when the session evidence may describe an
    entity that already has a durable record under another entity_id or path.

  required_behavior:
    - set_duplicate_entity_risk_review_flag
    - preserve_possible_existing_entity_id_when_known
    - create_merge_candidate_or_reference_only_record
    - require_operator_validation_before_merge

  forbidden_behavior:
    - silently_merge_entities
    - silently_create_duplicate_entity
    - delete_entity_record
    - rewrite_raw_source_path_to_match_guess
~~~

## durable_findings_policy

~~~yaml
durable_findings_policy:
  durable_finding_definition: >
    A durable finding is a session observation that should influence future
    planning, validation, status mutation, entity maintenance, or handoff.

  write_to_findings_when:
    - decision_made
    - source_conflict_detected
    - durable_state_delta_extracted
    - raw_source_ref_or_path_is_important
    - operator_validation_record_changes_future_behavior
    - unresolved_context_should_survive_session

  findings_must_include:
    - concise_finding
    - raw_source_ref_or_raw_source_missing_flag
    - raw_source_path_or_raw_source_missing_flag
    - review_flags_when_relevant
~~~

## planning_feed_policy

~~~yaml
planning_feed_policy:
  planning_feed_role: >
    Provide apex-plan with clean next-session context, durable findings, open
    items, risks, decisions made, raw source references, and review flags.

  include:
    - next_session_context
    - Current Step
    - Open Items
    - Risks
    - Decisions Made
    - Next Actions
    - durable_findings
    - raw_source_ref
    - raw_source_path
    - review_flags
    - unresolved_context

  exclude:
    - exact_next_task_ranking
    - blocker_scan_result
    - registry_rebuild_result
    - drift_detection_result
    - priority_score_computation
    - urgency_score_computation
    - unlock_depth_computation
~~~

## failure_modes

~~~yaml
failure_modes:
  missing_input:
    response: create_record_with_USER_INPUT_REQUIRED_and_review_flag
  raw_source_missing:
    response: preserve_delta_or_entity_update_but_mark_raw_source_missing
  source_conflict:
    response: preserve_all_sides_and_carry_to_next_session_open_items
  duplicate_entity_risk:
    response: create_merge_candidate_or_reference_only_record
  unresolved_dependency:
    response: preserve_depends_on_and_do_not_compute_unlock_depth
  scope_drift:
    response: route_exact_ranking_or_registry_or_decomposition_to_correct_package
~~~