# Mutation Gate Rules

## purpose

~~~yaml
purpose:
  file_role: status_mutation_and_operator_validation_contract
  package_name: apex-session
  goal: >
    Define how apex-session validates H1 status changes, creates mutation
    records, previews before/after state, records operator validation, and
    rejects invalid or unconfirmed mutations.

mutation_policy:
  final_package_behavior: >
    The skill creates final mutation records and handoff artifacts. It does not
    silently mutate repo files. Actual repo writes, if any, belong to a later
    explicit file-application flow.

CrewAI_task_py_SUBSTITUTE:
  allowed_claim: >
    substitute task-contract, human review, expected_output, guardrail,
    and output_file evidence
  forbidden_claim: original CrewAI getting-started skill source
~~~

## H1_status_validation

~~~yaml
H1_status_validation:
  allowed_status_values:
    - open
    - in-progress
    - blocked
    - done
    - deferred

  required_checks:
    - status_before_must_be_allowed_or_USER_INPUT_REQUIRED
    - status_after_must_be_allowed
    - status_after_must_not_use_extra_values
    - status_change_reason_must_be_present_for_consequential_mutation
    - depends_on_must_be_preserved_when_available

  invalid_status_response:
    validation_status: rejected
    review_flags:
      - invalid_status
    action: >
      Reject the mutation record as invalid, show allowed_status_values, and
      preserve the rejected request in progress.md or review flags.
~~~

## status_mutation_record_schema

~~~yaml
status_mutation_record_schema:
  required_fields:
    task_id: string
    task_title: string
    status_before:
      type: enum_or_USER_INPUT_REQUIRED
      allowed_status_values:
        - open
        - in-progress
        - blocked
        - done
        - deferred
    status_after:
      type: enum
      allowed_status_values:
        - open
        - in-progress
        - blocked
        - done
        - deferred
    status_change_reason: string
    operator_validation:
      type: enum
      allowed_values:
        - confirmed
        - rejected
        - needs_revision
        - not_requested
    validation_status:
      type: enum
      allowed_values:
        - confirmed
        - rejected
        - needs_revision
        - not_requested
    validation_timestamp: string_or_USER_INPUT_REQUIRED
    raw_source_ref: string_or_USER_INPUT_REQUIRED
    raw_source_path: string_or_USER_INPUT_REQUIRED
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
    depends_on:
      type: int_array
      rule: all_depends_on_items_must_be_done_before_actionable
    source_conflict: boolean
~~~

## before_after_preview_schema

~~~yaml
before_after_preview_schema:
  required_fields:
    task_id: string
    task_title: string
    status_before:
      type: enum_or_USER_INPUT_REQUIRED
      allowed_status_values:
        - open
        - in-progress
        - blocked
        - done
        - deferred
    status_after:
      type: enum
      allowed_status_values:
        - open
        - in-progress
        - blocked
        - done
        - deferred
    status_change_reason: string
    raw_source_ref: string_or_USER_INPUT_REQUIRED
    raw_source_path: string_or_USER_INPUT_REQUIRED
    review_flags: array

  preview_rules:
    - show_exact_field_before_and_after
    - include_raw_source_basis
    - include_unresolved_dependency_when_depends_on_blocks_actionability
    - include_operator_validation_requirement
    - do_not_apply_repo_write
~~~

## operator_validation_record_schema

~~~yaml
operator_validation_record_schema:
  required_fields:
    task_id: string
    task_title: string
    operator_validation:
      type: enum
      allowed_values:
        - confirmed
        - rejected
        - needs_revision
        - not_requested
    validation_status:
      type: enum
      allowed_values:
        - confirmed
        - rejected
        - needs_revision
        - not_requested
    validation_timestamp: string_or_USER_INPUT_REQUIRED
    status_change_reason: string
    review_flags: array

  validation_rules:
    confirmed:
      effect: mutation_record_can_be_treated_as_confirmed
    rejected:
      effect: mutation_record_must_not_be_treated_as_confirmed
    needs_revision:
      effect: mutation_record_requires_revised_status_or_reason
    not_requested:
      effect: mutation_record_is_visible_but_not_confirmed
~~~

## create_vs_update_distinction

~~~yaml
create_vs_update_distinction:
  create_record:
    use_when:
      - task_id_is_new_or_unknown
      - entity_id_is_new_or_unknown
      - session_evidence_creates_new_state_delta_id
    required_action:
      - preserve_raw_source_ref
      - preserve_raw_source_path
      - mark_missing_input_if_identity_is_incomplete

  update_record:
    use_when:
      - task_id_exists
      - entity_id_exists
      - status_before_is_known_or_explicitly_marked_USER_INPUT_REQUIRED
    required_action:
      - preserve_status_before
      - preserve_status_after
      - include_before_after_preview
      - include_operator_validation_record

  shared_rule: >
    Create and update records are final records in the handoff package, but they
    are not silent repo mutations. A later explicit file-application flow may
    apply them to files after validation.
~~~

## confirmation_gate

~~~yaml
confirmation_gate:
  consequential_mutation_requires_operator_validation: true
  confirmed_value: confirmed

  consequential_mutation_examples:
    - status_after_changes_task_state
    - entity_update_record_changes_durable_entity_meaning
    - source_conflict_resolution_is_requested
    - duplicate_entity_risk_would_be_merged
    - raw_source_missing_would_be_ignored

  if_operator_validation_is_confirmed:
    validation_status: confirmed
    allowed_result: confirmed_mutation_record

  if_operator_validation_is_rejected:
    validation_status: rejected
    required_review_flags:
      - operator_confirmation_missing

  if_operator_validation_is_needs_revision:
    validation_status: needs_revision
    required_review_flags:
      - operator_confirmation_missing

  if_operator_validation_is_not_requested:
    validation_status: not_requested
    required_review_flags:
      - operator_confirmation_missing
~~~

## invalid_mutation_rejection

~~~yaml
invalid_mutation_rejection:
  reject_when:
    - status_after_not_in_H1
    - status_before_not_in_H1_and_not_marked_USER_INPUT_REQUIRED
    - task_id_missing
    - task_title_missing
    - status_change_reason_missing_for_consequential_mutation
    - raw_source_ref_missing_when_required
    - raw_source_path_missing_when_required
    - operator_validation_missing_for_consequential_mutation
    - requested_behavior_belongs_to_apex_plan
    - requested_behavior_belongs_to_apex_sync

  rejection_output:
    - rejected_status_mutation_record
    - before_after_preview_when_possible
    - review_flags
    - safest_valid_next_action_for_operator
~~~

## final_mutation_output_contract

~~~yaml
final_mutation_output_contract:
  required_outputs_when_status_change_requested:
    - status_mutation_record
    - before_after_preview
    - operator_validation_record

  required_outputs_when_mutation_is_confirmed:
    - validation_status_confirmed
    - validation_timestamp
    - raw_source_ref_or_raw_source_missing_flag
    - raw_source_path_or_raw_source_missing_flag

  required_outputs_when_mutation_is_not_confirmed:
    - validation_status_not_confirmed_value
    - review_flags
    - before_after_preview
    - reason_not_confirmed

  never_do:
    - silently_mutate_repo_files
    - invent_status_values
    - invent_operator_validation
    - suppress_source_conflict
    - suppress_duplicate_entity_risk
    - compute_final_task_rank
    - compute_blocker_report
    - rebuild_registry
~~~