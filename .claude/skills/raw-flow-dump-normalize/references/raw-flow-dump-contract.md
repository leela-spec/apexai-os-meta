# Raw Flow Dump Contract

```yaml
raw_flow_dump_contract:
  artifact_name: normalized_raw_flow_dump
  file_role: raw_flow_dump_normalize_reference_contract
  package: raw-flow-dump-normalize
  purpose: >
    Define the minimal interface for normalizing messy operator execution
    evidence into one reviewable raw-flow dump artifact per planned flow. This
    file prepares FlowRecap input without running FlowRecap, creating project
    status deltas, logging model usage deltas, or mutating project state.

  ownership:
    owns:
      - normalized_raw_flow_dump
      - raw_operator_input_intake_rules
      - messy_evidence_normalization_rules
      - source_reference_capture_rules
      - completion_state_normalization
      - confidence_and_gap_flags
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

  source_authority:
    inspected_sources:
      - .claude/Claude.md
      - .claude/skills/PrecapNextDay/Skill_precap-next-day.md
      - .claude/skills/PrecapNextDay/precap-next-day-package-manifest.md
      - .claude/skills/PrecapNextDay/references/flow-packet-contract.md
      - .claude/skills/PrecapNextDay/references/flow-prompt-pack-contract.md
      - .claude/skills/PrecapNextDay/references/daily-plan-output-contract.md
      - .claude/skills/PrecapNextDay/references/input-intake-and-resilience-contract.md
      - .claude/skills/PrecapNextDay/references/usage-tracking-dependency-contract.md
      - Claude_Skill_Package_BestPractice_Handover.md
      - Claude_Skill_PromptFlow_Design_Guidance_v1.md
    source_gap_register: []

  downstream_consumers:
    primary:
      - FlowRecap
    secondary:
      - model-usage-log
      - status-merge
      - next_PreCapNextDay

  global_rules:
    one_normalized_raw_flow_dump_per_flow: true
    source_flow_packet_ref_required: true
    raw_evidence_must_be_separated_from_interpretation: true
    missing_details_must_be_preserved_as_gaps: true
    decisions_must_be_captured_without_expanding_scope: true
    model_usage_notes_are_notes_only_not_usage_delta: true
    completion_state_must_be_explicit: true
    skipped_flows_should_use_skipped_flow_marker: true
    FlowRecap_not_run: true
    project_status_not_merged: true
    calendar_events_not_created: true
    project_work_not_executed: true
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
      format: "raw_flow_dump_<YYYY_MM_DD>_<flow_id>_<short_slug>"
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
      note: "Use the source flow_packet flow_id when available. Do not invent a canonical flow identity when the source is ambiguous."

    source_flow_packet_ref:
      type: object
      required: true
      fields:
        packet_id:
          type: string
          required: false
        packet_path_or_label:
          type: string
          required: false
        source_status:
          type: string
          allowed:
            - supplied
            - inferred_from_operator_note
            - missing
            - ambiguous
          required: true

    flow_prompt_pack_ref:
      type: object
      required: false
      note: "Optional reference only. Do not redefine flow_prompt_pack or prompt_packet schemas."

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
      min_items: 1
      required: true

    operator_summary:
      type: object
      required: true
      fields:
        raw_summary:
          type: string
          required: true
          note: "Preserve operator language where useful."
        normalized_summary:
          type: string
          required: true
          note: "Summarize what happened without adding unsupported facts."
        uncertainty_notes:
          type: list
          item_type: string
          required: false

    produced_outputs:
      type: list
      item_ref: produced_output
      required: true

    decisions_made:
      type: list
      item_ref: decision_made
      required: true

    blockers_or_failures:
      type: list
      item_ref: blocker_or_failure
      required: true

    open_questions:
      type: list
      item_ref: open_question
      required: true

    model_usage_notes:
      type: list
      item_ref: model_usage_note
      required: true
      note: "Capture surfaces, models, prompts, or quota observations only when known. Do not create model_usage_delta."

    normalization_confidence:
      type: object
      required: true
      fields:
        confidence_level:
          type: string
          allowed:
            - high
            - medium
            - low
            - unknown
          required: true
        confidence_reasons:
          type: list
          item_type: string
          required: true
        missing_minimum_evidence:
          type: list
          item_type: string
          required: false

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

## Schema: evidence_source

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
        - pasted_chat_history
        - uploaded_markdown
        - artifact_path
        - git_diff_or_commit_ref
        - prompt_output
        - operator_note
        - decision_note
        - blocker_note
        - model_usage_note
        - unknown
      required: true

    source_ref_or_paste_label:
      type: string
      required: true
      note: "Use a path, chat label, artifact label, commit ref, or operator-provided source label."

    reliability:
      type: string
      allowed:
        - high
        - medium
        - low
        - unknown
      required: true

    extraction_notes:
      type: string
      required: false
```

## Schema: produced_output

```yaml
produced_output:
  type: object
  required:
    - output_label
    - output_type
    - output_ref_or_status
    - confidence
  fields:
    output_label:
      type: string
      required: true
    output_type:
      type: string
      allowed:
        - file_created
        - file_updated
        - draft_text
        - analysis
        - prompt
        - decision_log
        - repo_change
        - no_output
        - unknown
      required: true
    output_ref_or_status:
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
```

## Schema: decision_made

```yaml
decision_made:
  type: object
  required:
    - decision_label
    - decision_summary
    - evidence_ref
    - review_needed
  fields:
    decision_label:
      type: string
      required: true
    decision_summary:
      type: string
      required: true
    evidence_ref:
      type: string
      required: false
    review_needed:
      type: boolean
      required: true
```

## Schema: blocker_or_failure

```yaml
blocker_or_failure:
  type: object
  required:
    - blocker_label
    - blocker_type
    - impact_on_flow
    - recommended_handling
  fields:
    blocker_label:
      type: string
      required: true
    blocker_type:
      type: string
      allowed:
        - missing_input
        - tool_failure
        - repo_access_issue
        - ambiguity
        - operator_capacity
        - dependency_missing
        - validation_failure
        - unknown
      required: true
    impact_on_flow:
      type: string
      required: true
    recommended_handling:
      type: string
      required: true
```

## Schema: open_question

```yaml
open_question:
  type: object
  required:
    - question
    - why_it_matters
    - suggested_owner
  fields:
    question:
      type: string
      required: true
    why_it_matters:
      type: string
      required: true
    suggested_owner:
      type: string
      allowed:
        - operator
        - future_FlowRecap
        - future_PreCapNextDay
        - project_status_owner
        - unknown
      required: true
```

## Schema: model_usage_note

```yaml
model_usage_note:
  type: object
  required:
    - usage_note
    - usage_source
    - usage_confidence
  fields:
    usage_note:
      type: string
      required: true
    usage_source:
      type: string
      required: false
    usage_confidence:
      type: string
      allowed:
        - high
        - medium
        - low
        - unknown
      required: true
    creates_model_usage_delta:
      type: boolean
      const: false
      required: true
```

## Boundary Rules

```yaml
boundary_rules:
  normalized_raw_flow_dump_may_include:
    - what_happened_during_the_flow
    - raw_or_normalized_operator_summary
    - source_references
    - output_references
    - decisions_made
    - blockers_or_failures
    - open_questions
    - model_usage_notes_without_delta_schema
    - confidence_and_review_flags

  normalized_raw_flow_dump_must_not_include:
    - Do not include next_day_plan schema.
    - Do not include flow_packet schema.
    - Do not include flow_prompt_pack schema.
    - Do not include prompt_packet schema.
    - Do not include FlowRecap output or flow_recap_packet schema.
    - Do not include project_status_delta or status_merge output.
    - Do not include model_usage_delta schema.
    - Do not claim execution, calendar writes, state merge, or FlowRecap completion.
```

## Validation Rules

```yaml
raw_flow_dump_validation_rules:
  valid:
    requires:
      - required_fields_present
      - at_least_one_evidence_source
      - completion_state_explicit
      - source_flow_packet_ref_status_clear
      - uncertainty_preserved
      - no_forbidden_output_created

  valid_with_warnings:
    use_when:
      - source_flow_packet_ref_is_inferred
      - evidence_is_partial_but_usable
      - some_outputs_or_decisions_need_operator_review

  operator_review_recommended:
    use_when:
      - completion_state_is_unknown_or_ambiguous
      - evidence_sources_have_low_reliability
      - important_decisions_or_outputs_are_inferred

  low_confidence:
    use_when:
      - raw_evidence_is_thin
      - multiple_required_details_are_unknown
      - normalization_depends_on_operator_memory

  blocked_by_missing_minimum_evidence:
    use_when:
      - execution_day_missing
      - flow_id_and_source_flow_packet_ref_both_missing
      - no_evidence_sources_available
      - no_operator_summary_available
```
