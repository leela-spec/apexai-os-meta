# Skipped Flow Marker Contract

```yaml
skipped_flow_marker_contract:
  artifact_name: skipped_flow_marker_contract
  file_role: raw_flow_dump_normalize_reference_contract
  package_name: raw-flow-dump-normalize
  package_path: ".claude/skills/raw-flow-dump-normalize/"
  purpose: >
    Define the minimal marker artifact for planned flows that were skipped,
    blocked, replaced, or not executed enough to justify a normalized raw flow
    dump. This marker gives FlowRecap and later planning systems a clean skip
    signal without pretending execution evidence exists.

  ownership:
    owns:
      - skipped_flow_marker
      - skip_reason_capture_rules
      - skip_type_normalization
      - impact_on_plan_capture_rules
      - recommended_next_handling_rules
      - skipped_flow_validation_rules
    must_not_own:
      - next_day_plan_schema
      - flow_packet_schema
      - flow_prompt_pack_schema
      - prompt_packet_schema
      - FlowRecap_output_schema
      - flow_recap_packet_schema
      - project_status_delta_schema
      - model_usage_delta_schema
      - status_merge_schema
      - project_kb_schema
      - calendar_write_schema
      - runtime_execution
      - scheduler_behavior
      - automatic_state_overwrite

  source_relationships:
    upstream_context:
      - source_flow_packet_ref
      - optional_flow_prompt_pack_ref
      - optional_next_day_plan_ref
      - operator_skip_note_or_absence_of_execution_evidence
    downstream_consumers:
      - FlowRecap
      - next_PreCapNextDay
      - operator_review
      - future_status_merge_after_FlowRecap

  global_rules:
    one_skipped_flow_marker_per_skipped_flow: true
    marker_is_preferred_when_no_real_execution_evidence_exists: true
    skip_reason_must_preserve_uncertainty: true
    skip_marker_must_not_invent_produced_outputs: true
    model_usage_delta_not_created: true
    FlowRecap_not_run: true
    status_merge_not_run: true
    project_work_not_executed: true
    calendar_events_not_created: true
```

## Schema: skipped_flow_marker

```yaml
skipped_flow_marker:
  type: object
  required:
    - marker_id
    - artifact_name
    - execution_day
    - flow_id
    - source_flow_packet_ref
    - skip_reason
    - skip_type
    - impact_on_plan
    - recommended_next_handling
    - validation_status

  fields:
    marker_id:
      type: string
      format: "skipped_flow_marker_<execution_day>_<flow_id>_<short_slug>"
      required: true

    artifact_name:
      type: string
      const: skipped_flow_marker
      required: true

    execution_day:
      type: string
      format: "YYYY-MM-DD"
      required: true

    flow_id:
      type: string
      required: true
      note: "Use the flow_id from the source flow_packet when available."

    source_flow_packet_ref:
      type: object
      required: true
      fields:
        flow_packet_id:
          type: string
          required: false
        flow_packet_path_or_label:
          type: string
          required: false
        source_status:
          type: string
          allowed:
            - available
            - partially_available
            - missing
            - unknown
          required: true

    flow_prompt_pack_ref:
      type: object
      required: false
      fields:
        flow_prompt_pack_id:
          type: string
          required: false
        flow_prompt_pack_path_or_label:
          type: string
          required: false
        source_status:
          type: string
          allowed:
            - available
            - partially_available
            - missing
            - unknown
          required: true

    skip_reason:
      type: string
      required: true
      rule: "Capture the operator-supplied reason when available; otherwise state what evidence is missing."

    skip_type:
      type: string
      allowed:
        - intentional_skip
        - time_constraint
        - blocker
        - energy_capacity
        - dependency_missing
        - replaced_by_other_work
        - unknown
      required: true

    impact_on_plan:
      type: object
      required: true
      fields:
        impact_level:
          type: string
          allowed:
            - none
            - low
            - medium
            - high
            - blocking
            - unknown
          required: true
        impact_summary:
          type: string
          required: true
        affected_outputs:
          type: list
          item_type: string
          required: false

    recommended_next_handling:
      type: object
      required: true
      fields:
        handling_type:
          type: string
          allowed:
            - reschedule_same_flow
            - compress_into_next_plan
            - convert_to_blocker_review
            - replace_with_new_flow
            - archive_no_followup
            - ask_operator
            - unknown
          required: true
        recommendation:
          type: string
          required: true
        recommended_owner:
          type: string
          allowed:
            - operator
            - next_PreCapNextDay
            - FlowRecap
            - status_merge
            - project_kb_manager
            - unknown
          required: true

    evidence_sources:
      type: list
      item_ref: skip_evidence_source
      min_items: 0
      required: false
      note: "Optional because some skips are known only by absence of execution evidence."

    open_questions:
      type: list
      item_type: string
      min_items: 0
      required: false

    confidence:
      type: object
      required: false
      fields:
        overall:
          type: string
          allowed:
            - high
            - medium
            - low
            - unknown
          required: true
        reasons:
          type: list
          item_type: string
          required: true
        operator_review_recommended:
          type: boolean
          required: true

    validation_status:
      type: string
      allowed:
        - valid
        - valid_with_warnings
        - operator_review_recommended
        - low_confidence
        - blocked_by_missing_minimum_evidence
      required: true
```

## Supporting Object Sketch

```yaml
skip_evidence_source:
  type: object
  required:
    - source_type
    - source_ref_or_paste_label
    - reliability
  fields:
    source_type:
      type: string
      allowed:
        - operator_note
        - chat_history
        - missing_artifact
        - source_flow_packet
        - calendar_context
        - blocker_note
        - other
        - unknown
      required: true
    source_ref_or_paste_label:
      type: string
      required: true
    reliability:
      type: string
      allowed:
        - high
        - medium
        - low
        - unverified
        - unknown
      required: true
```

## Validation Rules

```yaml
skipped_flow_marker_validation_rules:
  minimum_valid_marker:
    required_truths:
      - artifact_name is skipped_flow_marker
      - execution_day is present
      - flow_id is present
      - source_flow_packet_ref.source_status is explicit
      - skip_reason is present
      - skip_type is present
      - impact_on_plan is present
      - recommended_next_handling is present
      - validation_status is present

  skip_type_rules:
    intentional_skip:
      use_when: "Operator explicitly chose not to run the planned flow."
    time_constraint:
      use_when: "Flow was not run because available time was insufficient."
    blocker:
      use_when: "Flow could not proceed because a blocker prevented execution."
    energy_capacity:
      use_when: "Flow was skipped due to operator capacity, fatigue, or attention constraints."
    dependency_missing:
      use_when: "Flow depended on missing input, missing artifact, unavailable tool, or unresolved decision."
    replaced_by_other_work:
      use_when: "Another work item consumed the flow slot or intentionally superseded the flow."
    unknown:
      use_when: "The system knows the flow did not execute, but the reason is not available."

  boundary_checks:
    - Do not create normalized_raw_flow_dump unless there is enough execution evidence to normalize.
    - Do not create flow_recap_packet.
    - Do not create project_status_delta.
    - Do not create model_usage_delta.
    - Do not merge project status.
    - Do not execute project work.
    - Do not create or update calendar events.
    - Do not overwrite source flow_packet or flow_prompt_pack artifacts.

  downstream_readiness:
    ready_when:
      - source_flow_packet_ref.source_status is explicit
      - skip_type is not unknown or skip_reason explains uncertainty
      - impact_on_plan is stated
      - recommended_next_handling is actionable or asks operator
    not_ready_when:
      - validation_status is blocked_by_missing_minimum_evidence
      - flow_id is missing
      - skip_reason is empty
      - source_flow_packet_ref.source_status is absent
```
