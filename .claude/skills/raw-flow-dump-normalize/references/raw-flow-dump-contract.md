# Raw Flow Dump Contract

```yaml
raw_flow_dump_contract:
  artifact_name: raw_flow_dump_contract
  file_role: raw_flow_dump_normalize_reference_contract
  package_name: raw-flow-dump-normalize
  package_path: ".claude/skills/raw-flow-dump-normalize/"
  purpose: >
    Define the minimal interface contract for normalizing messy operator
    execution evidence into one normalized_raw_flow_dump artifact per flow.
    This contract prepares FlowRecap input clarity without running FlowRecap,
    merging status, logging model usage deltas, executing project work, or
    overwriting project state.

  source_authority:
    inspected_sources:
      - path: ".claude/Claude.md"
        status: inspected
        role: repo_level_loop_and_missing_skill_index
      - path: ".claude/skills/PrecapNextDay/Skill_precap-next-day.md"
        status: inspected
        role: upstream_planning_boundary_and_raw_capture_preparation
      - path: ".claude/skills/PrecapNextDay/precap-next-day-package-manifest.md"
        status: inspected
        role: upstream_package_boundary_and_path_policy
      - path: ".claude/skills/PrecapNextDay/references/flow-packet-contract.md"
        status: inspected
        role: flow_packet_raw_capture_and_skipped_flow_preparation
      - path: ".claude/skills/PrecapNextDay/references/flow-prompt-pack-contract.md"
        status: inspected
        role: prompt_pack_capture_hints_and_FlowRecap_preparation_boundary
      - path: ".claude/skills/PrecapNextDay/references/daily-plan-output-contract.md"
        status: inspected
        role: next_day_plan_boundary_and_generated_file_context
      - path: ".claude/skills/PrecapNextDay/references/input-intake-and-resilience-contract.md"
        status: inspected
        role: partial_input_and_uncertainty_handling_pattern
      - path: ".claude/skills/PrecapNextDay/references/usage-tracking-dependency-contract.md"
        status: inspected
        role: model_usage_notes_boundary_without_usage_delta_ownership
      - path: ".claude/skills/PrecapNextDay/references/prompt-engineering-dependency-contract.md"
        status: inspected
        role: prompt_packet_boundary_reference
      - path: ".claude/skills/PrecapNextDay/references/calendar-event-write-contract.md"
        status: inspected
        role: no_calendar_mutation_boundary
      - path: ".claude/skills/PrecapNextDay/references/workflow-process-validation-contract.md"
        status: inspected
        role: no_workflow_taxonomy_redefinition_boundary
      - path: ".claude/skills/PrecapNextDay/references/validation-checklist.md"
        status: inspected
        role: validation_status_pattern_and_boundary_checks

    source_gap_register:
      - source_name: Claude skill best-practice guide in repo root
        attempted_path: "Claude_Skill_Package_BestPractice_Handover.md"
        status: missing_in_repo_at_tested_path
        handling: "Do not guess a repo path; use available project guidance only as structural background."
      - source_name: Claude prompt-flow design guidance in repo root
        attempted_path: "Claude_Skill_PromptFlow_Design_Guidance_v1.md"
        status: missing_in_repo_at_tested_path
        handling: "Do not guess a repo path; use available project guidance only as structural background."

  ownership:
    owns:
      - normalized_raw_flow_dump
      - raw_operator_input_intake_rules
      - messy_evidence_normalization_rules
      - source_reference_capture_rules
      - completion_state_normalization
      - confidence_and_gap_flags
      - raw_flow_dump_validation_rules
      - downstream_FlowRecap_input_readiness_rules
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

  downstream_consumers:
    primary:
      - FlowRecap
    secondary:
      - operator_review
      - future_status_merge_after_FlowRecap
      - future_model_usage_log_after_execution_review

  global_rules:
    one_normalized_raw_flow_dump_per_flow: true
    raw_evidence_must_be_separated_from_normalized_interpretation: true
    uncertainty_must_be_preserved_not_fabricated: true
    source_refs_must_be_captured_when_available: true
    missing_sources_become_gap_flags: true
    completion_state_must_be_explicit: true
    skipped_flows_should_use_skipped_flow_marker_when_no_execution_evidence_exists: true
    model_usage_notes_are_notes_only_not_usage_delta: true
    FlowRecap_not_run: true
    status_merge_not_run: true
    project_work_not_executed: true
    calendar_events_not_created: true
```

## Schema: normalized_raw_flow_dump

```yaml
normalized_raw_flow_dump:
  type: object
  required:
    - dump_id
    - artifact_name
    - execution_day
    - flow_id
    - source_flow_packet_ref
    - completion_state
    - evidence_sources
    - operator_summary
    - produced_outputs
    - decisions_made
    - blockers_or_failures
    - open_questions
    - model_usage_notes
    - normalization_confidence
    - validation_status

  fields:
    dump_id:
      type: string
      format: "raw_flow_dump_<execution_day>_<flow_id>_<short_slug>"
      required: true

    artifact_name:
      type: string
      const: normalized_raw_flow_dump
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

    completion_state:
      type: string
      allowed:
        - completed
        - partially_completed
        - skipped
        - blocked
        - abandoned
        - unknown
      required: true

    evidence_sources:
      type: list
      item_ref: evidence_source
      min_items: 0
      required: true
      item_fields:
        - source_type
        - source_ref_or_paste_label
        - reliability

    operator_summary:
      type: object
      required: true
      fields:
        raw_operator_statement:
          type: string
          required: false
          nullable: true
        normalized_summary:
          type: string
          required: true
        interpretation_notes:
          type: list
          item_type: string
          required: false
        uncertainty_flags:
          type: list
          item_type: string
          required: false

    produced_outputs:
      type: list
      item_ref: produced_output_ref
      min_items: 0
      required: true
      note: "Use empty list when no output was produced; do not invent artifacts."

    decisions_made:
      type: list
      item_ref: decision_made
      min_items: 0
      required: true
      note: "Capture explicit decisions only; inferred decisions require low confidence flag."

    blockers_or_failures:
      type: list
      item_ref: blocker_or_failure
      min_items: 0
      required: true

    open_questions:
      type: list
      item_ref: open_question
      min_items: 0
      required: true

    model_usage_notes:
      type: object
      required: true
      note: "Notes only; this package must not create model_usage_delta."
      fields:
        usage_observed:
          type: string
          allowed:
            - supplied
            - partially_supplied
            - not_supplied
            - unknown
          required: true
        notes:
          type: list
          item_type: string
          required: true
        suggested_usage_log_followup:
          type: boolean
          required: false

    normalization_confidence:
      type: object
      required: true
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
        gap_flags:
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

## Supporting Object Sketches

```yaml
evidence_source:
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
        - prompt_output
        - artifact_path
        - repo_file
        - screenshot_description
        - calendar_context
        - usage_note
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
    source_excerpt_or_summary:
      type: string
      required: false
      nullable: true

produced_output_ref:
  type: object
  required:
    - output_label
    - output_type
    - output_ref_or_location
    - confidence
  fields:
    output_label:
      type: string
      required: true
    output_type:
      type: string
      allowed:
        - repo_file
        - markdown_artifact
        - prompt_text
        - decision_log
        - research_note
        - template
        - example
        - no_output
        - other
        - unknown
      required: true
    output_ref_or_location:
      type: string
      required: false
      nullable: true
    confidence:
      type: string
      allowed:
        - high
        - medium
        - low
        - unknown
      required: true

decision_made:
  type: object
  required:
    - decision_label
    - decision_summary
    - decision_source
    - confidence
  fields:
    decision_label:
      type: string
      required: true
    decision_summary:
      type: string
      required: true
    decision_source:
      type: string
      required: true
    confidence:
      type: string
      allowed:
        - high
        - medium
        - low
        - unknown
      required: true

blocker_or_failure:
  type: object
  required:
    - blocker_label
    - blocker_summary
    - impact
    - recommended_next_handling
  fields:
    blocker_label:
      type: string
      required: true
    blocker_summary:
      type: string
      required: true
    impact:
      type: string
      allowed:
        - none
        - low
        - medium
        - high
        - blocking
        - unknown
      required: true
    recommended_next_handling:
      type: string
      required: true

open_question:
  type: object
  required:
    - question
    - why_it_matters
    - recommended_owner
  fields:
    question:
      type: string
      required: true
    why_it_matters:
      type: string
      required: true
    recommended_owner:
      type: string
      allowed:
        - operator
        - next_PreCapNextDay
        - FlowRecap
        - model_usage_log
        - status_merge
        - project_kb_manager
        - unknown
      required: true
```

## Validation Rules

```yaml
raw_flow_dump_validation_rules:
  minimum_valid_evidence:
    requires_at_least_one_of:
      - operator_summary.normalized_summary
      - produced_outputs
      - blockers_or_failures
      - open_questions
      - completion_state

  completion_state_rules:
    skipped:
      rule: "If completion_state is skipped and no execution evidence exists, create or reference skipped_flow_marker instead of forcing a normalized_raw_flow_dump."
    unknown:
      rule: "Use only when evidence is too thin to classify; set validation_status to operator_review_recommended or low_confidence."
    completed_or_partially_completed:
      rule: "Require at least one evidence source, produced output, decision, blocker, or explicit operator summary."

  boundary_checks:
    - Do not create flow_recap_packet.
    - Do not create project_status_delta.
    - Do not create model_usage_delta.
    - Do not merge project status.
    - Do not execute project work.
    - Do not create or update calendar events.
    - Do not overwrite source flow_packet or flow_prompt_pack artifacts.

  downstream_FlowRecap_readiness:
    ready_when:
      - source_flow_packet_ref.source_status is available or partially_available
      - completion_state is not unknown
      - evidence_sources or operator_summary contains usable evidence
      - normalization_confidence.operator_review_recommended is false or review flags are explicit
    not_ready_when:
      - validation_status is blocked_by_missing_minimum_evidence
      - completion_state is unknown with no evidence source
      - source_flow_packet_ref.source_status is missing and flow_id cannot be verified
```
