# FILE: .claude/skills/precap-next-day/references/calendar-event-write-contract.md

# Calendar Event Write Contract

```yaml
calendar_event_write_contract:
  artifact_name: calendar_event_write_contract
  file_role: precap_next_day_reference_contract
  purpose: >
    Define how PreCapNextDay prepares workflow-block calendar write requests,
    operator approval gates, create/update intent, conflict flags, and degraded
    calendar behavior. This file enables calendar-aware daily planning without
    turning PreCapNextDay into a general calendar planner or silently writing
    events without explicit operator approval.

  ownership:
    owns:
      - calendar_event_write_request
      - calendar_workflow_block_request
      - calendar_update_request
      - calendar_write_approval_gate
      - calendar_conflict_flagging_rules
      - workflow_block_title_and_description_rules
      - degraded_calendar_behavior
      - calendar_write_examples
    must_not_own:
      - next_day_plan_schema
      - flow_packet_schema
      - flow_prompt_pack_schema
      - prompt_packet_schema
      - AI_surface_inventory_schema
      - routing_decision_schema
      - workflow_stage_taxonomy
      - process_stage_taxonomy
      - project_execution
      - FlowRecap_output_schema
      - project_status_merge
      - general_calendar_planning_system
      - non_workflow_calendar_blocks
      - actual_calendar_connector_behavior

  boundary_summary: >
    PreCapNextDay may create or update calendar workflow blocks only when the
    operator explicitly approves the requested write. Without approval, it may
    produce reviewable calendar_event_write_request artifacts, but it must not
    perform or imply actual calendar mutation.
```

## Calendar Write Policy

```yaml
calendar_write_policy:
  policy_name: workflow_blocks_only_operator_approved

  allowed_scope:
    - workflow_blocks_for_next_day_plan
    - flow_sprint_blocks
    - recap_digest_blocks
    - residual_or_overflow_workflow_blocks
    - update_existing_workflow_blocks_when_operator_approved

  forbidden_scope:
    - personal_non_workflow_events
    - social_events
    - private_life_calendar_management
    - recurring_calendar_systems
    - automatic_rescheduling_without_approval
    - hidden_calendar_writes
    - calendar_cleanup
    - project_status_merge_triggering
    - FlowRecap_triggering

  write_modes:
    allowed:
      - no_write_requested
      - review_only
      - create_new_events
      - update_existing_events
      - create_or_update
      - blocked

  approval_policy:
    operator_approval_required_for_actual_write: true
    approval_must_be_explicit: true
    approval_can_apply_to:
      - one_event
      - one_flow
      - all_workflow_blocks_in_request
    approval_cannot_be_inferred_from:
      - vague_positive_feedback
      - acceptance_of_daily_plan_only
      - prior_default_preference
      - absence_of_objection

  calendar_context_policy:
    calendar_events_available:
      behavior: "Use existing events as constraints and possible update targets."
    calendar_events_missing:
      behavior: "Create reviewable proposed workflow blocks and mark calendar context as missing."
    fixed_time_constraints_missing:
      behavior: "Use unscheduled or tentative blocks; do not invent exact times unless operator supplied a planning template."
    existing_event_match_unclear:
      behavior: "Do not update. Create review flag and either propose a new block or request operator selection."
```

## Schema: calendar_event_write_request

```yaml
calendar_event_write_request:
  type: object
  required:
    - request_id
    - request_role
    - request_status
    - write_mode
    - request_scope
    - source_plan_ref
    - calendar_context_status
    - approval_gate
    - workflow_blocks
    - validation_status

  fields:
    request_id:
      type: string
      format: "calendar_event_write_request_<execution_day_id>"
      required: true

    request_role:
      type: string
      allowed:
        - next_day_workflow_block_write_request
        - workflow_block_review_only_request
        - workflow_block_update_request
        - degraded_calendar_request
      required: true

    request_status:
      type: string
      allowed:
        - draft
        - review_ready
        - pending_operator_approval
        - approved_for_write
        - partially_approved_for_write
        - rejected
        - blocked
        - not_requested
      required: true

    write_mode:
      type: string
      allowed:
        - no_write_requested
        - review_only
        - create_new_events
        - update_existing_events
        - create_or_update
        - blocked
      required: true

    request_scope:
      type: string
      allowed:
        - workflow_blocks_only
      required: true

    source_plan_ref:
      type: object
      required: true
      fields:
        next_day_plan_id:
          type: string
          required: false
        execution_day:
          type: string
          format: "YYYY-MM-DD"
          required: false
        source_status:
          type: string
          allowed:
            - next_day_plan_generated
            - partial_plan_generated
            - bootstrap_plan_generated
            - unknown
          required: true

    calendar_context_status:
      type: string
      allowed:
        - calendar_read_available
        - manual_constraints_only
        - unavailable
        - stale
        - unknown
      required: true

    calendar_context_used:
      type: object
      required: false
      fields:
        existing_calendar_events_used:
          type: boolean
        manual_calendar_constraints_used:
          type: boolean
        time_zone_known:
          type: boolean
        existing_workflow_blocks_detected:
          type: boolean
        conflict_check_performed:
          type: boolean

    approval_gate:
      type: object_ref
      ref: calendar_write_approval_gate
      required: true

    workflow_blocks:
      type: list
      item_ref: calendar_workflow_block_request
      min_items: 0
      max_items: 12
      required: true

    request_summary_for_operator:
      type: object
      required: false
      fields:
        summary:
          type: string
        events_to_create_count:
          type: integer
          min: 0
          max: 12
        events_to_update_count:
          type: integer
          min: 0
          max: 12
        blocked_events_count:
          type: integer
          min: 0
          max: 12
        approval_instruction:
          type: string

    operator_review_flags:
      type: list
      item_type: string
      required: false

    validation_status:
      type: string
      allowed:
        - valid
        - valid_with_warnings
        - operator_review_recommended
        - low_confidence_auto_generated
        - blocked_by_missing_operator_decision
      required: true
```

## Schema: calendar_write_approval_gate

```yaml
calendar_write_approval_gate:
  type: object
  required:
    - approval_required
    - approval_status
    - approval_scope
    - explicit_operator_action_required

  fields:
    approval_required:
      type: boolean
      required: true
      rule: "Must be true for create_new_events, update_existing_events, or create_or_update write modes."

    approval_status:
      type: string
      allowed:
        - not_required_no_write_requested
        - pending_operator_approval
        - approved_for_write
        - partially_approved_for_write
        - rejected
        - blocked_by_missing_time
        - blocked_by_unclear_target
        - blocked_by_tool_unavailable
      required: true

    approval_scope:
      type: string
      allowed:
        - none
        - one_event
        - one_flow
        - all_workflow_blocks_in_request
        - partial_selection
        - unknown
      required: true

    explicit_operator_action_required:
      type: boolean
      required: true

    acceptable_operator_actions:
      type: list
      item_type: string
      allowed:
        - approve_all
        - approve_selected
        - reject_all
        - edit_times
        - edit_titles
        - select_update_targets
        - switch_to_review_only
      required: false

    approval_text_to_show_operator:
      type: string
      required: false
      rule: "Use direct review language; do not imply events have already been written."
```

## Schema: calendar_workflow_block_request

```yaml
calendar_workflow_block_request:
  type: object
  required:
    - event_request_id
    - block_role
    - flow_id
    - title
    - timing
    - write_intent
    - approval_status
    - validation_status

  fields:
    event_request_id:
      type: string
      format: "calendar_block_<flow_id>_<short_slug>"
      required: true

    block_role:
      type: string
      allowed:
        - flow_work_block
        - sprint_work_block
        - recap_digest_block
        - residual_overflow_block
        - buffer_or_transition_block
      required: true

    flow_id:
      type: string
      allowed:
        - F1
        - F2
        - F3
        - F4
        - cross_flow
        - unknown
      required: true

    sprint_ids:
      type: list
      item_type: string
      allowed:
        - S1
        - S2
        - S3
        - cross_sprint
        - not_applicable
      min_items: 0
      max_items: 3
      required: false

    project_or_flow_name:
      type: string
      required: false

    source_flow_packet_ref:
      type: object_ref
      ref: flow_packet
      required: false
      note: "Reference only; flow_packet schema is owned by flow-packet-contract.md."

    source_prompt_pack_ref:
      type: object_ref
      ref: flow_prompt_pack
      required: false
      note: "Reference only; flow_prompt_pack schema is owned by flow-prompt-pack-contract.md."

    title:
      type: string
      required: true
      rule: "Use compact workflow-block title with flow id and project or flow name."

    description:
      type: string
      required: false
      rule: "Include daily-plan context, sprint purpose, expected output, and FlowRecap reminder when useful."

    timing:
      type: object_ref
      ref: calendar_block_timing
      required: true

    write_intent:
      type: string
      allowed:
        - create_new_event
        - update_existing_event
        - review_only
        - no_write
        - blocked
      required: true

    update_target:
      type: object_ref
      ref: calendar_update_target
      required: false

    event_attributes:
      type: object_ref
      ref: calendar_event_attributes
      required: false

    conflict_status:
      type: object_ref
      ref: calendar_conflict_status
      required: false

    approval_status:
      type: string
      allowed:
        - pending_operator_approval
        - approved_for_write
        - rejected
        - blocked_by_missing_time
        - blocked_by_unclear_target
        - review_only
      required: true

    operator_review_flags:
      type: list
      item_type: string
      required: false

    validation_status:
      type: string
      allowed:
        - valid
        - valid_with_warnings
        - operator_review_recommended
        - low_confidence_auto_generated
        - blocked_by_missing_operator_decision
      required: true
```

## Schema: calendar_block_timing

```yaml
calendar_block_timing:
  type: object
  required:
    - timing_status
    - date
    - time_zone_status

  fields:
    timing_status:
      type: string
      allowed:
        - exact_time_supplied
        - proposed_time_from_calendar_gap
        - proposed_time_from_operator_template
        - tentative_unscheduled
        - blocked_by_missing_time
        - unknown
      required: true

    date:
      type: string
      format: "YYYY-MM-DD | unknown"
      required: true

    start_time:
      type: string
      format: "HH:MM | unknown"
      required: false

    end_time:
      type: string
      format: "HH:MM | unknown"
      required: false

    duration_minutes:
      type: integer
      min: 0
      max: 480
      required: false

    time_zone:
      type: string
      required: false
      example: "Europe/Berlin"

    time_zone_status:
      type: string
      allowed:
        - known
        - assumed_from_operator_context
        - unknown
      required: true

    timing_source:
      type: string
      allowed:
        - operator_supplied
        - calendar_gap_analysis
        - next_day_plan_template
        - default_flow_block_estimate
        - unknown
      required: false

    timing_note:
      type: string
      required: false
```

## Schema: calendar_update_target

```yaml
calendar_update_target:
  type: object
  required:
    - target_status

  fields:
    target_status:
      type: string
      allowed:
        - existing_event_identified
        - multiple_possible_events
        - no_existing_event_found
        - unknown
      required: true

    existing_event_id:
      type: string
      required: false
      rule: "Use only when supplied by a calendar tool or operator. Do not invent."

    existing_event_title:
      type: string
      required: false

    existing_event_time:
      type: string
      required: false

    update_reason:
      type: string
      allowed:
        - align_with_new_next_day_plan
        - replace_placeholder_block
        - adjust_time
        - adjust_description
        - avoid_calendar_conflict
        - operator_requested_update
        - unknown
      required: false

    target_review_required:
      type: boolean
      required: false
```

## Schema: calendar_event_attributes

```yaml
calendar_event_attributes:
  type: object
  required:
    - event_kind
    - transparency

  fields:
    event_kind:
      type: string
      allowed:
        - workflow_block
      required: true

    calendar_id_if_known:
      type: string
      required: false

    location:
      type: string
      required: false
      allowed:
        - none
        - online
        - offline
        - operator_defined
        - unknown

    visibility:
      type: string
      allowed:
        - default
        - private
        - public
        - unknown
      required: false

    transparency:
      type: string
      allowed:
        - opaque
        - transparent
        - unknown
      required: true
      rule: "Use opaque for focused workflow blocks unless operator preference says otherwise."

    reminders:
      type: object
      required: false
      fields:
        reminder_status:
          type: string
          allowed:
            - use_calendar_default
            - custom_requested
            - none_requested
            - unknown
        custom_minutes_before:
          type: integer
          min: 0
          max: 1440
          required: false

    color_or_label:
      type: string
      required: false
      rule: "Use only if operator supplied a calendar color or label convention."
```

## Schema: calendar_conflict_status

```yaml
calendar_conflict_status:
  type: object
  required:
    - conflict_check_status
    - conflict_level

  fields:
    conflict_check_status:
      type: string
      allowed:
        - checked_against_calendar_events
        - checked_against_manual_constraints
        - not_checked_calendar_unavailable
        - not_checked_no_times
        - unknown
      required: true

    conflict_level:
      type: string
      allowed:
        - none_detected
        - possible_conflict
        - hard_conflict
        - unknown
      required: true

    conflicting_items:
      type: list
      item_type: string
      required: false

    conflict_resolution:
      type: string
      allowed:
        - no_action_needed
        - propose_alternative_time
        - ask_operator
        - block_write_until_resolved
        - switch_to_review_only
        - unknown
      required: false

    conflict_note:
      type: string
      required: false
```

## Title and Description Rules

```yaml
workflow_block_text_rules:
  title_rules:
    preferred_pattern: "<flow_id> <project_or_flow_name> - <block_role>"
    examples:
      - "F1 Leela - workflow block"
      - "F2 MasterOfArts - S1/S2 work block"
      - "F3 Apex - recap digest block"
      - "F4 Residual - overflow block"
    avoid:
      - vague_titles_without_flow_id
      - titles_that_imply_project_work_already_completed
      - non_workflow_personal_labels
      - hidden_or_abbreviated_meaning_only_the_model_understands

  description_rules:
    include_when_available:
      - flow_goal
      - sprint_scope
      - expected_output_type
      - prompt_pack_reference
      - raw_flow_dump_instruction
      - FlowRecap_reminder
      - usage_capture_reminder
    avoid:
      - long_prompt_bodies
      - private_reasoning_trace
      - source_document_names
      - unapproved_calendar_actions

  default_description_template: |
    Flow: <flow_id> / <project_or_flow_name>
    Goal: <flow_goal>
    Sprint scope: <sprint_scope>
    Expected output: <expected_output_type>
    Execution note: use the associated flow_prompt_pack if applicable.
    After execution: create raw_flow_dump or skipped_flow_marker for FlowRecap.
```

## Calendar Dependency Behavior

```yaml
calendar_dependency_behavior:
  calendar_tool_available_and_operator_approved:
    allowed_behavior:
      - prepare_write_request
      - present_summary_for_approval
      - write_approved_workflow_blocks_only
      - report_written_event_summary
    required_flags:
      - approval_status
      - write_mode
      - conflict_check_status

  calendar_tool_available_but_no_approval:
    allowed_behavior:
      - prepare_review_only_write_request
      - present_event_preview
      - ask_for_specific_approval_or_edits
    forbidden_behavior:
      - actual_event_creation
      - actual_event_update

  calendar_tool_unavailable:
    allowed_behavior:
      - output_calendar_event_write_request_as_artifact
      - mark_calendar_context_status_unavailable
      - mark_request_as_review_only_or_blocked
      - preserve proposed titles descriptions and timing notes
    forbidden_behavior:
      - claiming_calendar_events_were_created
      - claiming_existing_events_were_updated

  missing_time_information:
    allowed_behavior:
      - produce_unscheduled_workflow_block_preview
      - ask_operator_for_times_in_calendar_review_section
      - mark blocked_by_missing_time_when_actual_write_requested
    forbidden_behavior:
      - inventing_exact_times_without_operator_or_calendar_basis
```

## Calendar Conflict Rules

```yaml
calendar_conflict_rules:
  conflict_detection_inputs:
    - existing_calendar_events
    - manual_calendar_constraints
    - proposed_workflow_block_times
    - existing_workflow_block_candidates

  hard_conflict_conditions:
    - proposed_time_overlaps_existing_busy_event
    - proposed_update_target_is_unclear
    - proposed_block_has_no_start_or_end_time_but_write_mode_requires_actual_write
    - operator_has_rejected_calendar_write

  possible_conflict_conditions:
    - calendar_context_is_stale
    - manual_constraints_are_ambiguous
    - multiple_existing_events_could_be_update_targets
    - time_zone_is_unknown
    - long_flow_block_has_no_buffer

  required_resolution_behavior:
    hard_conflict: block_write_until_resolved
    possible_conflict: mark_operator_review_recommended
    no_conflict_detected: allow_pending_operator_approval
    unknown: switch_to_review_only_or_operator_review
```

## Integration with PreCapNextDay Outputs

```yaml
precap_next_day_calendar_integration:
  next_day_plan_must_include_when_calendar_write_is_relevant:
    - calendar_event_write_request_summary
    - approval_gate_status
    - proposed_workflow_blocks
    - calendar_review_flags

  flow_packet_may_include:
    - proposed_calendar_block_ref
    - timing_window
    - calendar_constraints_note
    - post_execution_FlowRecap_reminder

  flow_prompt_pack_may_include:
    - calendar_block_context
    - execution_window_note
    - expected_capture_after_execution

  FlowRecap_handoff_block_may_include:
    - planned_calendar_block_ref
    - actual_execution_time_capture_hint
    - skipped_or_shifted_block_capture_hint

  status_after_calendar_request:
    no_write_requested: "No approval needed; preserve review notes only."
    review_only: "Operator can copy or approve later."
    pending_operator_approval: "Do not write until explicit approval."
    approved_for_write: "Actual write may proceed only for approved workflow blocks."
    blocked: "Resolve blocking issue before write."
```

## Minimal Examples

```yaml
examples:
  review_only_no_calendar_context:
    calendar_event_write_request:
      request_id: calendar_event_write_request_2026-06-17
      request_role: degraded_calendar_request
      request_status: review_ready
      write_mode: review_only
      request_scope: workflow_blocks_only
      source_plan_ref:
        next_day_plan_id: next_day_plan_2026-06-17
        execution_day: "2026-06-17"
        source_status: next_day_plan_generated
      calendar_context_status: unavailable
      calendar_context_used:
        existing_calendar_events_used: false
        manual_calendar_constraints_used: false
        time_zone_known: true
        existing_workflow_blocks_detected: false
        conflict_check_performed: false
      approval_gate:
        approval_required: false
        approval_status: not_required_no_write_requested
        approval_scope: none
        explicit_operator_action_required: false
      workflow_blocks:
        - event_request_id: calendar_block_F1_leela_work
          block_role: flow_work_block
          flow_id: F1
          sprint_ids:
            - S1
            - S2
          project_or_flow_name: Leela
          title: "F1 Leela - workflow block"
          description: "Goal: execute the planned Leela flow. After execution, create raw_flow_dump for FlowRecap."
          timing:
            timing_status: tentative_unscheduled
            date: "2026-06-17"
            time_zone: Europe/Berlin
            time_zone_status: known
            timing_source: unknown
          write_intent: review_only
          approval_status: review_only
          validation_status: valid_with_warnings
      operator_review_flags:
        - calendar_tool_unavailable
        - exact_times_not_supplied
      validation_status: valid_with_warnings

  create_workflow_blocks_pending_approval:
    calendar_event_write_request:
      request_id: calendar_event_write_request_2026-06-17
      request_role: next_day_workflow_block_write_request
      request_status: pending_operator_approval
      write_mode: create_new_events
      request_scope: workflow_blocks_only
      source_plan_ref:
        next_day_plan_id: next_day_plan_2026-06-17
        execution_day: "2026-06-17"
        source_status: next_day_plan_generated
      calendar_context_status: manual_constraints_only
      calendar_context_used:
        existing_calendar_events_used: false
        manual_calendar_constraints_used: true
        time_zone_known: true
        existing_workflow_blocks_detected: false
        conflict_check_performed: true
      approval_gate:
        approval_required: true
        approval_status: pending_operator_approval
        approval_scope: all_workflow_blocks_in_request
        explicit_operator_action_required: true
        acceptable_operator_actions:
          - approve_all
          - approve_selected
          - reject_all
          - edit_times
          - switch_to_review_only
        approval_text_to_show_operator: "Approve these workflow calendar blocks before I write them."
      workflow_blocks:
        - event_request_id: calendar_block_F3_apex_s1_s2
          block_role: sprint_work_block
          flow_id: F3
          sprint_ids:
            - S1
            - S2
          project_or_flow_name: Apex
          title: "F3 Apex - S1/S2 work block"
          description: "Expected output: one finalized process artifact. Use the associated prompt pack; capture actual usage and raw flow dump after execution."
          timing:
            timing_status: exact_time_supplied
            date: "2026-06-17"
            start_time: "10:00"
            end_time: "12:00"
            duration_minutes: 120
            time_zone: Europe/Berlin
            time_zone_status: known
            timing_source: operator_supplied
          write_intent: create_new_event
          event_attributes:
            event_kind: workflow_block
            location: none
            visibility: default
            transparency: opaque
            reminders:
              reminder_status: use_calendar_default
          conflict_status:
            conflict_check_status: checked_against_manual_constraints
            conflict_level: none_detected
            conflict_resolution: no_action_needed
          approval_status: pending_operator_approval
          validation_status: valid
      validation_status: operator_review_recommended

  update_existing_workflow_block_unclear_target:
    calendar_event_write_request:
      request_id: calendar_event_write_request_2026-06-17
      request_role: workflow_block_update_request
      request_status: blocked
      write_mode: update_existing_events
      request_scope: workflow_blocks_only
      source_plan_ref:
        next_day_plan_id: next_day_plan_2026-06-17
        execution_day: "2026-06-17"
        source_status: next_day_plan_generated
      calendar_context_status: calendar_read_available
      approval_gate:
        approval_required: true
        approval_status: blocked_by_unclear_target
        approval_scope: unknown
        explicit_operator_action_required: true
        acceptable_operator_actions:
          - select_update_targets
          - switch_to_review_only
      workflow_blocks:
        - event_request_id: calendar_block_F2_update_candidate
          block_role: flow_work_block
          flow_id: F2
          project_or_flow_name: MasterOfArts
          title: "F2 MasterOfArts - workflow block"
          timing:
            timing_status: proposed_time_from_calendar_gap
            date: "2026-06-17"
            start_time: "14:00"
            end_time: "15:30"
            duration_minutes: 90
            time_zone: Europe/Berlin
            time_zone_status: known
            timing_source: calendar_gap_analysis
          write_intent: update_existing_event
          update_target:
            target_status: multiple_possible_events
            update_reason: align_with_new_next_day_plan
            target_review_required: true
          conflict_status:
            conflict_check_status: checked_against_calendar_events
            conflict_level: possible_conflict
            conflict_resolution: ask_operator
          approval_status: blocked_by_unclear_target
          operator_review_flags:
            - multiple_possible_update_targets
          validation_status: blocked_by_missing_operator_decision
      operator_review_flags:
        - select_existing_event_before_update
      validation_status: blocked_by_missing_operator_decision
```

---

# VALIDATION - FILE-SPECIFIC CHECKS

- [ ] Exactly one file was produced.
- [ ] File path is `.claude/skills/precap-next-day/references/calendar-event-write-contract.md`.
- [ ] File defines `calendar_event_write_request` and workflow-block event request structure.
- [ ] File limits calendar write scope to workflow blocks only.
- [ ] File requires explicit operator approval before actual calendar creation or update.
- [ ] File supports create, update, review-only, and blocked modes.
- [ ] File defines conflict handling for missing time, stale calendar context, unclear update targets, and busy-time overlap.
- [ ] File does not create actual calendar events inside the contract.
- [ ] File does not define general calendar planning, recurring routines, personal events, or non-workflow blocks.
- [ ] File references daily plan, flow packet, and prompt pack context without redefining their schemas.
- [ ] File includes degraded behavior when calendar tools or calendar context are unavailable.
- [ ] YAML blocks use 2-space indentation.
- [ ] Numeric constraints use typed `type`/`min`/`max` objects.
- [ ] File does not execute project work, run FlowRecap, merge project status, or finalize OpenRouter model mapping.

---

# NEXT PROMPT

Paste this next:
> Prompt PND9:
> Create exactly one file.
>
> # FILE: .claude/skills/precap-next-day/references/workflow-process-validation-contract.md
>
> File type: dependency_contract.
> Schema ownership: owns the PreCapNextDay-to-workflow-process-design dependency interface and daily-plan workflow/process validation summary.
> Context carry-forward:
> - .claude/skills/precap-next-day/SKILL.md
> - .claude/skills/precap-next-day/references/daily-plan-output-contract.md
> - .claude/skills/precap-next-day/references/flow-packet-contract.md
> - .claude/skills/precap-next-day/references/flow-prompt-pack-contract.md
> - .claude/skills/workflow-process-design/SKILL.md
> - .claude/skills/workflow-process-design/references/workflow-stage-taxonomy.md
> - .claude/skills/workflow-process-design/references/process-stage-taxonomy.md
> - .claude/skills/workflow-process-design/references/expected-output-type-contract.md
> - .claude/skills/workflow-process-design/references/prompt-process-alignment-validation.md
>
> This file must define:
> - dependency interface between PreCapNextDay and workflow-process-design
> - workflow/process validation inputs and outputs
> - daily-plan workflow_process_validation_summary
> - flow-level validation expectations
> - prompt-pack alignment expectations
> - conflict handling when workflow/process fit disagrees with prompt quality or routing/cost
> - degraded behavior when workflow-process-design is missing
> - minimal examples
>
> Rules:
> - Do not redefine workflow_stage_taxonomy, process_stage_taxonomy, or expected_output_type schema.
> - Do not redefine prompt_packet, flow_packet, or flow_prompt_pack schemas.
> - Preserve conflict authority order: operator decision, workflow/process fit, prompt quality, routing/cost.
> - Use YAML with 2-space indentation.
>
> Next prompt target: Prompt PND10.
