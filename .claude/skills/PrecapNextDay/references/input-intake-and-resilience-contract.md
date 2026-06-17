# FILE: .claude/skills/precap-next-day/references/input-intake-and-resilience-contract.md

# Input Intake and Resilience Contract

```yaml
input_intake_and_resilience_contract:
  artifact_name: input_intake_context
  file_role: precap_next_day_reference_contract
  purpose: >
    Define how PreCapNextDay accepts partial planning context, classifies
    available inputs, selects an execution mode, handles missing or conflicting
    material, and produces operator review flags before daily planning output is
    created.

  ownership:
    owns:
      - input_intake_context
      - available_input_map
      - input_source_entry
      - execution_mode_selection
      - missing_input_policy
      - degraded_mode_policy
      - bootstrap_mode_policy
      - input_confidence_rules
      - input_conflict_rules
      - intake_operator_review_flags
    must_not_own:
      - next_day_plan
      - flow_packet
      - flow_prompt_pack
      - prompt_packet
      - routing_decision
      - planned_usage_budget
      - calendar_event_write_request
      - workflow_stage_taxonomy
      - process_stage_taxonomy
      - project_status_merge
      - FlowRecap_output

  global_rules:
    all_inputs_are_optional: true
    run_with_partial_context: true
    run_with_no_context_in_bootstrap_mode: true
    do_not_fabricate_missing_project_state: true
    do_not_block_daily_plan_generation_only_because_inputs_are_incomplete: true
    mark_low_confidence_when_context_is_thin: true
    surface_conflicts_before_using_conflicted_inputs: true
```

## Schema: input_intake_context

```yaml
input_intake_context:
  type: object
  required:
    - intake_id
    - created_or_updated_at
    - available_input_map
    - selected_execution_mode
    - missing_inputs
    - input_conflicts
    - confidence_summary
    - validation_status

  fields:
    intake_id:
      type: string
      format: "input_intake_<YYYYMMDD_or_short_slug>"
      required: true

    created_or_updated_at:
      type: string
      format: "YYYY-MM-DD"
      required: true

    operator_day_intent:
      type: string
      required: false
      nullable: true
      rule: "Use as the strongest daily direction signal when supplied."

    available_input_map:
      type: object_ref
      ref: available_input_map
      required: true

    selected_execution_mode:
      type: object_ref
      ref: execution_mode_selection
      required: true

    missing_inputs:
      type: list
      item_type: string
      required: true

    input_conflicts:
      type: list
      item_ref: input_conflict
      required: true

    confidence_summary:
      type: object_ref
      ref: confidence_summary
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

## Schema: available_input_map

```yaml
available_input_map:
  type: object
  required:
    - input_sources
    - strongest_available_context
    - weakest_available_context
    - usable_for_planning

  fields:
    input_sources:
      type: list
      item_ref: input_source_entry
      required: true

    strongest_available_context:
      type: string
      allowed:
        - operator_day_intent
        - current_project_status_overview
        - flow_recap_packets
        - skipped_flow_markers
        - recap_day_notes
        - precap_week_output
        - weekly_plan_packet
        - fixed_calendar_constraints
        - calendar_events
        - AI_surface_inventory
        - model_usage_summary
        - detailed_project_state_files
        - none
      required: true

    weakest_available_context:
      type: string
      allowed:
        - thin_operator_note
        - stale_status_context
        - partial_recap_context
        - no_project_context
        - no_calendar_context
        - no_usage_context
        - none
      required: true

    usable_for_planning:
      type: boolean
      required: true
      rule: "False only when operator request is not a PreCapNextDay request or an explicit operator decision is required before any output can be safely drafted."
```

## Schema: input_source_entry

```yaml
input_source_entry:
  type: object
  required:
    - input_name
    - presence
    - freshness
    - reliability
    - planning_use
    - confidence

  fields:
    input_name:
      type: string
      allowed:
        - operator_day_intent
        - current_project_status_overview
        - flow_recap_packets
        - skipped_flow_markers
        - recap_day_notes
        - precap_week_output
        - weekly_plan_packet
        - fixed_calendar_constraints
        - calendar_events
        - AI_surface_inventory
        - model_usage_summary
        - detailed_project_state_files
      required: true

    presence:
      type: string
      allowed:
        - supplied
        - available_from_context
        - missing
        - unknown
      required: true

    freshness:
      type: string
      allowed:
        - current
        - recent
        - stale
        - unknown
        - not_applicable
      required: true

    reliability:
      type: string
      allowed:
        - operator_confirmed
        - canonical_artifact
        - generated_unvalidated
        - partial_or_ambiguous
        - missing
        - unknown
      required: true

    planning_use:
      type: string
      allowed:
        - primary_direction
        - supporting_context
        - constraint_only
        - validation_only
        - unavailable
        - ignore_due_to_conflict
      required: true

    confidence:
      type: string
      allowed:
        - high
        - medium
        - low
        - unknown
      required: true

    notes:
      type: string
      required: false
```

## Execution Mode Selection

```yaml
execution_mode_selection:
  type: object
  required:
    - mode
    - reason
    - review_level
    - allowed_outputs

  fields:
    mode:
      type: string
      allowed:
        - full_context_mode
        - standard_mode
        - recap_recovery_mode
        - bootstrap_mode
        - calendar_constrained_mode
        - prompt_heavy_mode
      required: true

    reason:
      type: string
      required: true

    review_level:
      type: string
      allowed:
        - normal_review
        - operator_review_recommended
        - operator_decision_required
        - low_confidence_review_required
      required: true

    allowed_outputs:
      type: list
      item_type: string
      allowed:
        - next_day_plan_draft
        - flow_packet_drafts
        - flow_prompt_pack_drafts
        - calendar_event_write_requests
        - usage_tracking_plan
        - FlowRecap_handoff_blocks
        - raw_flow_dump_templates
        - skipped_flow_marker_templates
      required: true
```

```yaml
execution_mode_rules:
  full_context_mode:
    use_when:
      - operator_day_intent_supplied
      - current_project_status_overview_available
      - recent_flow_recap_or_weekly_plan_available
      - calendar_or_fixed_constraints_available_if_relevant
    confidence_default: high
    review_level: normal_review

  standard_mode:
    use_when:
      - enough_project_context_exists_for_daily_plan
      - no_major_conflict_detected
      - some_optional_inputs_are_missing
    confidence_default: medium
    review_level: operator_review_recommended

  recap_recovery_mode:
    use_when:
      - recent_flow_recap_packets_or_skipped_markers_are_primary_context
      - prior_day_execution_needs_recovery_or_continuation
      - project_status_context_is_partial_or_stale
    confidence_default: medium
    review_level: operator_review_recommended

  bootstrap_mode:
    use_when:
      - no_usably_structured_prior_context_exists
      - operator_still_requests_next_day_plan
    confidence_default: low
    review_level: low_confidence_review_required

  calendar_constrained_mode:
    use_when:
      - fixed_calendar_constraints_or_calendar_events_dominate_day_shape
      - workflow_blocks_must_fit_available_time
    confidence_default: medium
    review_level: operator_review_recommended

  prompt_heavy_mode:
    use_when:
      - daily_value_depends_on_prompt_pack_quality
      - prompt_engineering_usage_or_workflow_alignment_is_primary
      - project_execution_is_mostly_AI_assisted
    confidence_default: medium
    review_level: operator_review_recommended
```

## Missing Input Policy

```yaml
missing_input_policy:
  principle: "Missing optional inputs degrade confidence; they do not block output by default."

  missing_input_handling:
    operator_day_intent:
      default_response: "Infer a conservative daily plan from available project status and prior recaps."
      flag: missing_operator_day_intent
      block_output: false

    current_project_status_overview:
      default_response: "Use latest supplied summaries, recaps, or bootstrap defaults."
      flag: missing_current_project_status_overview
      block_output: false

    flow_recap_packets:
      default_response: "Do not assume prior flow outcomes; avoid status claims that require recap evidence."
      flag: missing_flow_recap_packets
      block_output: false

    weekly_plan_packet:
      default_response: "Plan one day from local context without claiming weekly alignment."
      flag: missing_weekly_plan_packet
      block_output: false

    calendar_events:
      default_response: "Create time-agnostic workflow blocks or mark calendar fit as unverified."
      flag: missing_calendar_events
      block_output: false

    AI_surface_inventory:
      default_response: "Use provider_unspecified routing placeholders and request routing review."
      flag: missing_AI_surface_inventory
      block_output: false

    model_usage_summary:
      default_response: "Avoid claims about remaining quota and mark usage planning low confidence."
      flag: missing_model_usage_summary
      block_output: false

    detailed_project_state_files:
      default_response: "Use compact project summaries only; do not invent detailed state."
      flag: missing_detailed_project_state_files
      block_output: false
```

## Input Conflict Rules

```yaml
input_conflict:
  type: object
  required:
    - conflict_id
    - conflict_type
    - affected_inputs
    - decision_rule
    - operator_review_required

  fields:
    conflict_id:
      type: string
      format: "input_conflict_<short_slug>"
      required: true

    conflict_type:
      type: string
      allowed:
        - stale_vs_current_context
        - operator_intent_vs_project_status
        - calendar_constraint_vs_workload
        - recap_delta_vs_status_overview
        - usage_summary_vs_requested_AI_surface
        - workflow_fit_vs_prompt_request
        - duplicate_or_ambiguous_input
      required: true

    affected_inputs:
      type: list
      item_type: string
      min_items: 2
      required: true

    decision_rule:
      type: string
      allowed:
        - prefer_operator_confirmed_current_input
        - prefer_canonical_status_when_no_operator_override
        - prefer_calendar_constraint_for_time_shape
        - prefer_recent_flow_recap_for_completed_flow_state
        - request_operator_decision
      required: true

    operator_review_required:
      type: boolean
      required: true

    notes:
      type: string
      required: false
```

```yaml
conflict_resolution_rules:
  priority_order:
    1: explicit_operator_decision
    2: current_calendar_or_fixed_time_constraint
    3: current_canonical_project_status
    4: recent_flow_recap_evidence
    5: weekly_plan_direction
    6: inferred_context

  mandatory_review_conflicts:
    - operator_intent_vs_project_status
    - calendar_constraint_vs_workload
    - recap_delta_vs_status_overview
    - usage_summary_vs_requested_AI_surface
    - workflow_fit_vs_prompt_request
```

## Confidence Summary

```yaml
confidence_summary:
  type: object
  required:
    - overall_confidence
    - reason
    - low_confidence_causes
    - recommended_operator_review

  fields:
    overall_confidence:
      type: string
      allowed:
        - high
        - medium
        - low
      required: true

    reason:
      type: string
      required: true

    low_confidence_causes:
      type: list
      item_type: string
      required: true

    recommended_operator_review:
      type: boolean
      required: true
```

```yaml
confidence_rules:
  high:
    requires:
      - operator_day_intent_or_recent_weekly_plan
      - current_project_status_or_recent_flow_recaps
      - no_mandatory_review_conflict
    validation_status_default: valid

  medium:
    applies_when:
      - context_is_usable_but_partial
      - optional_inputs_missing
      - plan_requires_operator_review_but_not_operator_decision
    validation_status_default: valid_with_warnings

  low:
    applies_when:
      - bootstrap_mode_selected
      - primary_project_state_missing
      - major_inputs_are_stale_or_conflicting
      - routing_or_calendar_context_is_needed_but_missing
    validation_status_default: low_confidence_auto_generated
```

## Bootstrap Mode Policy

```yaml
bootstrap_mode_policy:
  purpose: "Allow PreCapNextDay to produce a usable starter daily plan when no structured context exists."
  allowed_assumptions:
    - use_fixed_daily_flows_F1_to_F4
    - keep_flow_goals_generic
    - create_prompt_and_recap_preparation_scaffolds
    - mark_all_project_specific_claims_as_operator_review_needed
  forbidden_assumptions:
    - invent_project_deadlines
    - invent_completed_flow_results
    - invent_current_quota_remaining
    - invent_calendar_availability
    - invent_project_status_details
  required_flags:
    - bootstrap_mode_used
    - low_confidence_auto_generated
    - operator_review_required_before_execution
```

## Minimal Examples

```yaml
example_full_context_intake:
  input_intake_context:
    intake_id: input_intake_20260616_full
    created_or_updated_at: "2026-06-16"
    operator_day_intent: "Prioritize Leela spatial system, MasterOfArts website structure, and Apex skill package continuation."
    available_input_map:
      input_sources:
        - input_name: operator_day_intent
          presence: supplied
          freshness: current
          reliability: operator_confirmed
          planning_use: primary_direction
          confidence: high
        - input_name: current_project_status_overview
          presence: supplied
          freshness: recent
          reliability: canonical_artifact
          planning_use: supporting_context
          confidence: high
        - input_name: model_usage_summary
          presence: missing
          freshness: unknown
          reliability: missing
          planning_use: unavailable
          confidence: unknown
      strongest_available_context: operator_day_intent
      weakest_available_context: no_usage_context
      usable_for_planning: true
    selected_execution_mode:
      mode: standard_mode
      reason: "Project and operator context are usable, but usage summary is missing."
      review_level: operator_review_recommended
      allowed_outputs:
        - next_day_plan_draft
        - flow_packet_drafts
        - flow_prompt_pack_drafts
        - usage_tracking_plan
        - FlowRecap_handoff_blocks
    missing_inputs:
      - model_usage_summary
    input_conflicts: []
    confidence_summary:
      overall_confidence: medium
      reason: "Planning context is adequate; usage planning is low confidence."
      low_confidence_causes:
        - missing_model_usage_summary
      recommended_operator_review: true
    operator_review_flags:
      - missing_model_usage_summary
    validation_status: valid_with_warnings
```

```yaml
example_bootstrap_intake:
  input_intake_context:
    intake_id: input_intake_20260616_bootstrap
    created_or_updated_at: "2026-06-16"
    available_input_map:
      input_sources:
        - input_name: operator_day_intent
          presence: missing
          freshness: unknown
          reliability: missing
          planning_use: unavailable
          confidence: unknown
      strongest_available_context: none
      weakest_available_context: no_project_context
      usable_for_planning: true
    selected_execution_mode:
      mode: bootstrap_mode
      reason: "No structured prior context exists, but PreCapNextDay can create a conservative starter day."
      review_level: low_confidence_review_required
      allowed_outputs:
        - next_day_plan_draft
        - flow_packet_drafts
        - raw_flow_dump_templates
        - skipped_flow_marker_templates
        - FlowRecap_handoff_blocks
    missing_inputs:
      - operator_day_intent
      - current_project_status_overview
      - weekly_plan_packet
      - flow_recap_packets
      - calendar_events
      - AI_surface_inventory
      - model_usage_summary
    input_conflicts: []
    confidence_summary:
      overall_confidence: low
      reason: "Only fixed daily flow grammar can be used."
      low_confidence_causes:
        - no_project_context
        - no_calendar_context
        - no_usage_context
      recommended_operator_review: true
    operator_review_flags:
      - bootstrap_mode_used
      - operator_review_required_before_execution
    validation_status: low_confidence_auto_generated
```

---

# VALIDATION - FILE-SPECIFIC CHECKS

- [ ] Defines `input_intake_context` exactly once.
- [ ] Defines `available_input_map` and `input_source_entry` without duplicating downstream schemas.
- [ ] Supports full-context, partial-context, recap-recovery, bootstrap, calendar-constrained, and prompt-heavy modes.
- [ ] Treats all PreCapNextDay inputs as optional.
- [ ] Degrades confidence instead of blocking when optional inputs are missing.
- [ ] Does not invent project status, calendar availability, quota remaining, or completed flow results.
- [ ] Does not define `next_day_plan`, `flow_packet`, `flow_prompt_pack`, routing, usage-delta, or calendar-event schemas.
- [ ] Uses YAML with 2-space indentation.

---

# NEXT PROMPT

Paste this next:
> Prompt PND3:
> Create exactly one file.
>
> # FILE: .claude/skills/precap-next-day/references/daily-plan-output-contract.md
>
> File type: reference_contract.
> Schema ownership: owns next_day_plan, generated_file_index, daily_review_status, and top-level daily plan output structure.
> Context carry-forward:
> - .claude/skills/precap-next-day/SKILL.md
> - .claude/skills/precap-next-day/references/input-intake-and-resilience-contract.md
>
> This file must define:
> - next_day_plan schema
> - top-level daily metadata
> - fixed F1-F4 flow container requirements
> - generated file index
> - review status fields
> - operator review flags
> - output examples
>
> Rules:
> - Do not define flow_packet internals owned by PND4.
> - Do not define flow_prompt_pack internals owned by PND5.
> - Do not define calendar_event_write_request internals owned by PND8.
> - Do not define routing or usage schemas owned by dependency packages.
> - Use YAML with 2-space indentation.
>
> Next prompt target: Prompt PND4.
