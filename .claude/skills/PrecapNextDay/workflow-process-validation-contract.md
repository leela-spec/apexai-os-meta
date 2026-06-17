# FILE: .claude/skills/precap-next-day/references/workflow-process-validation-contract.md

# Workflow Process Validation Contract

```yaml
workflow_process_validation_contract:
  artifact_name: workflow_process_validation_summary
  file_role: precap_next_day_dependency_contract
  purpose: >
    Define how PreCapNextDay consumes workflow-process-design outputs when
    compiling next_day_plan, flow_packet, and flow_prompt_pack artifacts. This
    file defines the dependency interface and embedding rules for daily planning.
    It does not redefine workflow taxonomies, process taxonomies, expected-output
    contracts, workflow records, or prompt alignment validation logic.

  ownership:
    owns:
      - PreCapNextDay_workflow_process_dependency_interface
      - workflow_process_validation_summary
      - flow_level_validation_embedding_rules
      - degraded_mode_when_workflow_process_design_is_missing
      - daily_plan_implications_from_workflow_validation
      - operator_review_trigger_rules_for_process_conflicts
    must_not_own:
      - workflow_stage_taxonomy
      - process_stage_taxonomy
      - expected_output_type_schema
      - workflow_record_schema
      - prompt_process_alignment_validation_rules
      - prompt_packet_schema
      - routing_decision_schema
      - daily_plan_schema
      - flow_packet_schema
      - flow_prompt_pack_schema
      - project_status_merge

  upstream_authority:
    workflow_process_design_package:
      package_path: ".claude/skills/workflow-process-design/"
      authoritative_files:
        - path: ".claude/skills/workflow-process-design/references/workflow-stage-taxonomy.md"
          provides:
            - workflow_stage_taxonomy
        - path: ".claude/skills/workflow-process-design/references/process-stage-taxonomy.md"
          provides:
            - process_stage_taxonomy
        - path: ".claude/skills/workflow-process-design/references/expected-output-type-contract.md"
          provides:
            - expected_output_type_contract
        - path: ".claude/skills/workflow-process-design/references/prompt-process-alignment-validation.md"
          provides:
            - prompt_process_alignment_validation
        - path: ".claude/skills/workflow-process-design/references/operator-validation-and-conflict-resolution.md"
          provides:
            - operator_review_flags
            - conflict_resolution_card

  downstream_consumers:
    - next_day_plan
    - flow_packet
    - flow_prompt_pack
    - operator_review_flags
```

## Schema: workflow_process_validation_summary

```yaml
workflow_process_validation_summary:
  type: object
  required:
    - validation_id
    - dependency_status
    - validation_scope
    - flow_validations
    - daily_plan_implications
    - validation_status
  fields:
    validation_id:
      type: string
      format: "workflow_process_validation_<execution_day_id>"
      required: true

    dependency_status:
      type: string
      allowed:
        - workflow_process_design_available
        - workflow_process_design_missing
        - workflow_process_design_partial
        - low_confidence_inferred
      required: true

    validation_scope:
      type: string
      allowed:
        - full_next_day_plan
        - single_flow
        - prompt_pack_only
        - bootstrap_mode
        - degraded_mode
      required: true

    source_inputs_used:
      type: list
      item_type: string
      allowed:
        - operator_day_intent
        - current_project_status_overview
        - flow_recap_packets
        - weekly_plan_packet
        - calendar_constraints
        - flow_packet_draft
        - flow_prompt_pack_draft
        - workflow_process_design_outputs
        - inferred_from_context
      required: false

    flow_validations:
      type: list
      item_ref: flow_workflow_process_validation
      min_items: 0
      max_items: 4
      required: true

    cross_flow_flags:
      type: list
      item_ref: workflow_process_cross_flow_flag
      min_items: 0
      max_items: 12
      required: false

    daily_plan_implications:
      type: object_ref
      ref: daily_plan_workflow_process_implications
      required: true

    validation_status:
      type: string
      allowed:
        - valid
        - valid_with_warnings
        - operator_review_recommended
        - low_confidence_auto_generated
        - blocked_by_missing_operator_decision
      required: true

    operator_review_flags:
      type: list
      item_ref: operator_review_flag
      min_items: 0
      max_items: 16
      required: false
```

## Schema: flow_workflow_process_validation

```yaml
flow_workflow_process_validation:
  type: object
  required:
    - flow_id
    - project
    - workflow_stage
    - process_stage
    - expected_output_type
    - sprint_structure_fit
    - prompt_pack_fit
    - validation_status
  fields:
    flow_id:
      type: string
      allowed:
        - F1
        - F2
        - F3
        - F4
      required: true

    project:
      type: string
      allowed:
        - Leela
        - MasterOfArts
        - Apex
        - Residual
        - operator_defined
      required: true

    workflow_stage:
      type: string
      source_authority: workflow_process_design.workflow_stage_taxonomy
      required: true
      unknown_value: workflow_stage_unknown

    process_stage:
      type: string
      source_authority: workflow_process_design.process_stage_taxonomy
      required: true
      unknown_value: process_stage_unknown

    expected_output_type:
      type: string
      source_authority: workflow_process_design.expected_output_type_contract
      required: true
      unknown_value: expected_output_type_unknown

    sprint_structure_fit:
      type: object_ref
      ref: sprint_structure_fit
      required: true

    prompt_pack_fit:
      type: object_ref
      ref: prompt_pack_workflow_fit
      required: true

    conflict_flags:
      type: list
      item_ref: workflow_process_conflict_flag
      min_items: 0
      max_items: 8
      required: false

    recommended_adjustments:
      type: list
      item_ref: workflow_process_adjustment
      min_items: 0
      max_items: 8
      required: false

    operator_validation_requirement:
      type: string
      allowed:
        - no_operator_review_needed
        - operator_review_recommended
        - operator_decision_required
        - blocked_until_operator_decides
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

## Schema: sprint_structure_fit

```yaml
sprint_structure_fit:
  type: object
  required:
    - fit_status
    - sprint_count_policy
    - rationale
  fields:
    fit_status:
      type: string
      allowed:
        - valid_three_sprint_fit
        - valid_compressed_fit
        - valid_omitted_flow
        - weak_fit_operator_review
        - invalid_structure
      required: true

    sprint_count_policy:
      type: string
      allowed:
        - default_three_sprints
        - compressed_two_sprints
        - compressed_one_sprint
        - omitted_with_reason
        - operator_defined
      required: true

    sprint_roles_checked:
      type: list
      item_type: string
      allowed:
        - S1_first_work_sprint
        - S2_second_work_or_deepening_sprint
        - S3_recap_digest_preparation_sprint
      required: false

    rationale:
      type: string
      max_words: 80
      required: true

    missing_or_weak_parts:
      type: list
      item_type: string
      max_items: 6
      required: false
```

## Schema: prompt_pack_workflow_fit

```yaml
prompt_pack_workflow_fit:
  type: object
  required:
    - fit_status
    - alignment_checks
    - rationale
  fields:
    fit_status:
      type: string
      allowed:
        - aligned
        - aligned_with_warnings
        - weakly_aligned
        - misaligned
        - not_checked_dependency_missing
      required: true

    alignment_checks:
      type: object
      required: true
      fields:
        workflow_stage_matches_prompt_goal:
          type: boolean
          required: true
        process_stage_matches_iteration_logic:
          type: boolean
          required: true
        expected_output_matches_prompt_output_contract:
          type: boolean
          required: true
        capture_hints_match_FlowRecap_needs:
          type: boolean
          required: true
        operator_review_flags_present_when_needed:
          type: boolean
          required: true

    rationale:
      type: string
      max_words: 100
      required: true

    prompt_adjustment_needed:
      type: boolean
      required: false

    prompt_adjustment_notes:
      type: list
      item_type: string
      max_items: 6
      required: false
```

## Conflict and Adjustment Objects

```yaml
workflow_process_conflict_flag:
  type: object
  required:
    - conflict_id
    - severity
    - conflict_type
    - description
    - recommended_handling
  fields:
    conflict_id:
      type: string
      format: "workflow_conflict_<short_slug>"
      required: true

    severity:
      type: string
      allowed:
        - none
        - low
        - medium
        - high
        - blocking
      required: true

    conflict_type:
      type: string
      allowed:
        - workflow_stage_unclear
        - process_stage_unclear
        - expected_output_mismatch
        - sprint_structure_mismatch
        - prompt_output_contract_mismatch
        - project_priority_conflict
        - operator_intent_conflict
        - dependency_missing
      required: true

    description:
      type: string
      max_words: 80
      required: true

    recommended_handling:
      type: string
      allowed:
        - continue_with_warning
        - adjust_flow_packet
        - adjust_prompt_pack
        - create_operator_tradeoff_card
        - block_until_operator_decides
      required: true

workflow_process_adjustment:
  type: object
  required:
    - adjustment_type
    - target_artifact
    - proposed_change
  fields:
    adjustment_type:
      type: string
      allowed:
        - relabel_workflow_stage
        - relabel_process_stage
        - change_expected_output_type
        - compress_sprints
        - expand_sprints
        - alter_prompt_output_contract
        - add_operator_review_flag
        - mark_low_confidence
      required: true

    target_artifact:
      type: string
      allowed:
        - next_day_plan
        - flow_packet
        - flow_prompt_pack
        - prompt_execution_packet
        - operator_review_flags
      required: true

    proposed_change:
      type: string
      max_words: 100
      required: true

    requires_operator_decision:
      type: boolean
      required: false
```

## Daily Plan Implications

```yaml
daily_plan_workflow_process_implications:
  type: object
  required:
    - overall_fit_status
    - allowed_to_continue
    - summary
  fields:
    overall_fit_status:
      type: string
      allowed:
        - all_flows_aligned
        - aligned_with_warnings
        - mixed_fit_operator_review_recommended
        - low_confidence_dependency_missing
        - blocked_by_process_conflict
      required: true

    allowed_to_continue:
      type: boolean
      required: true

    next_day_plan_adjustments:
      type: list
      item_type: string
      max_items: 8
      required: false

    flow_prompt_pack_adjustments:
      type: list
      item_type: string
      max_items: 12
      required: false

    operator_tradeoff_cards_needed:
      type: list
      item_type: string
      max_items: 6
      required: false

    summary:
      type: string
      max_words: 120
      required: true
```

## Dependency Procedure for PreCapNextDay

```yaml
PreCapNextDay_workflow_process_dependency_procedure:
  steps:
    1_collect_available_workflow_process_inputs:
      action: Load workflow-process-design outputs when available.
      fallback: If unavailable, infer coarse labels from operator intent and mark low_confidence_auto_generated.

    2_validate_each_flow:
      action: Check every planned flow against workflow_stage, process_stage, expected_output_type, sprint_structure_fit, and prompt_pack_fit.
      output: flow_workflow_process_validation

    3_validate_cross_flow_coherence:
      action: Check whether flow labels, sprint structures, and expected outputs create conflicts across F1 to F4.
      output: cross_flow_flags

    4_apply_adjustments:
      action: Apply non-controversial label or warning adjustments inside next_day_plan, flow_packet, and flow_prompt_pack drafts.
      boundary: Do not override operator intent or workflow-process-design authority.

    5_surface_conflicts:
      action: Convert high or blocking conflicts into operator review flags or tradeoff cards.
      boundary: Do not silently resolve workflow/process conflicts when the correction changes project priority, expected output, or sprint scope.

    6_embed_summary:
      action: Embed workflow_process_validation_summary into next_day_plan and relevant flow packets as dependency evidence.
      boundary: Keep the summary compact and do not duplicate upstream taxonomy schemas.
```

## Degraded Mode Rules

```yaml
degraded_mode_rules:
  when_workflow_process_design_missing:
    allowed: true
    required_behavior:
      - infer_minimal_workflow_process_labels_from_context
      - set_dependency_status_to_workflow_process_design_missing
      - set_validation_scope_to_degraded_mode
      - mark_validation_status_low_confidence_auto_generated
      - add_operator_review_flag
      - do_not_claim_taxonomy_validity

  when_labels_are_unclear:
    allowed: true
    required_behavior:
      - use_unknown_value_placeholders
      - preserve_operator_intent
      - avoid_relabeling_to_false_precision
      - continue_if_daily_plan_is_still_useful
      - request_operator_decision_only_if_execution_shape_changes

  when_expected_output_conflicts_with_prompt:
    allowed: true
    required_behavior:
      - prefer_workflow_process_fit_over_prompt_quality
      - adjust_prompt_pack_when_non_destructive
      - create_tradeoff_card_when_adjustment_changes_task_scope
      - block_only_when_misalignment_would_make_execution_invalid
```

## Minimal Examples

```yaml
example_valid_flow_validation:
  validation_id: workflow_process_validation_2026_06_17
  dependency_status: workflow_process_design_available
  validation_scope: single_flow
  flow_validations:
    - flow_id: F1
      project: Leela
      workflow_stage: system_definition
      process_stage: outline_expand_compress
      expected_output_type: design_system_spec
      sprint_structure_fit:
        fit_status: valid_three_sprint_fit
        sprint_count_policy: default_three_sprints
        sprint_roles_checked:
          - S1_first_work_sprint
          - S2_second_work_or_deepening_sprint
          - S3_recap_digest_preparation_sprint
        rationale: "The flow needs first definition, deepening, and recap preparation before implementation."
      prompt_pack_fit:
        fit_status: aligned
        alignment_checks:
          workflow_stage_matches_prompt_goal: true
          process_stage_matches_iteration_logic: true
          expected_output_matches_prompt_output_contract: true
          capture_hints_match_FlowRecap_needs: true
          operator_review_flags_present_when_needed: true
        rationale: "Prompt outputs match the intended design-system specification and provide recap-ready capture hints."
      validation_status: valid
  daily_plan_implications:
    overall_fit_status: all_flows_aligned
    allowed_to_continue: true
    summary: "Workflow/process fit is valid for this flow. No operator review is needed."
  validation_status: valid

example_degraded_mode_missing_dependency:
  validation_id: workflow_process_validation_2026_06_17
  dependency_status: workflow_process_design_missing
  validation_scope: degraded_mode
  flow_validations:
    - flow_id: F3
      project: Apex
      workflow_stage: workflow_stage_unknown
      process_stage: process_stage_unknown
      expected_output_type: expected_output_type_unknown
      sprint_structure_fit:
        fit_status: weak_fit_operator_review
        sprint_count_policy: default_three_sprints
        rationale: "Labels were inferred from operator intent because workflow-process-design outputs were unavailable."
      prompt_pack_fit:
        fit_status: not_checked_dependency_missing
        alignment_checks:
          workflow_stage_matches_prompt_goal: false
          process_stage_matches_iteration_logic: false
          expected_output_matches_prompt_output_contract: false
          capture_hints_match_FlowRecap_needs: true
          operator_review_flags_present_when_needed: true
        rationale: "Prompt fit cannot be validated against upstream workflow/process authorities."
      operator_validation_requirement: operator_review_recommended
      validation_status: low_confidence_auto_generated
  daily_plan_implications:
    overall_fit_status: low_confidence_dependency_missing
    allowed_to_continue: true
    operator_tradeoff_cards_needed: []
    summary: "The plan can continue in degraded mode, but workflow/process labels need later review."
  validation_status: low_confidence_auto_generated
  operator_review_flags:
    - missing_workflow_process_design_dependency

example_blocking_expected_output_conflict:
  validation_id: workflow_process_validation_2026_06_17
  dependency_status: workflow_process_design_available
  validation_scope: single_flow
  flow_validations:
    - flow_id: F2
      project: MasterOfArts
      workflow_stage: offer_design
      process_stage: generate_critique_revise
      expected_output_type: offer_structure
      sprint_structure_fit:
        fit_status: valid_three_sprint_fit
        sprint_count_policy: default_three_sprints
        rationale: "The flow needs draft, critique, and recap preparation."
      prompt_pack_fit:
        fit_status: misaligned
        alignment_checks:
          workflow_stage_matches_prompt_goal: true
          process_stage_matches_iteration_logic: true
          expected_output_matches_prompt_output_contract: false
          capture_hints_match_FlowRecap_needs: true
          operator_review_flags_present_when_needed: true
        rationale: "The prompt pack asks for full website copy, but the expected output is only offer structure."
        prompt_adjustment_needed: true
        prompt_adjustment_notes:
          - "Narrow prompt output from page copy to offer structure."
      conflict_flags:
        - conflict_id: workflow_conflict_offer_output_scope
          severity: high
          conflict_type: expected_output_mismatch
          description: "Prompt output scope is broader than the workflow/process expected output."
          recommended_handling: create_operator_tradeoff_card
      recommended_adjustments:
        - adjustment_type: alter_prompt_output_contract
          target_artifact: flow_prompt_pack
          proposed_change: "Change prompt output contract from full website copy to offer structure and decision criteria."
          requires_operator_decision: true
      operator_validation_requirement: operator_decision_required
      validation_status: operator_review_recommended
  daily_plan_implications:
    overall_fit_status: mixed_fit_operator_review_recommended
    allowed_to_continue: true
    flow_prompt_pack_adjustments:
      - "Revise F2 prompt output scope before execution."
    operator_tradeoff_cards_needed:
      - "F2 offer structure versus full website copy scope."
    summary: "Daily plan can continue, but F2 needs operator decision before execution."
  validation_status: operator_review_recommended
```

---

# VALIDATION - FILE-SPECIFIC CHECKS

- [ ] Exactly one file was produced.
- [ ] The file owns `workflow_process_validation_summary` and PreCapNextDay dependency behavior only.
- [ ] The file does not redefine workflow-stage taxonomy, process-stage taxonomy, expected-output schema, prompt packet schema, routing schema, daily-plan schema, flow-packet schema, or flow-prompt-pack schema.
- [ ] YAML uses 2-space indentation.
- [ ] Numeric constraints use typed fields where numeric constraints appear.
- [ ] Degraded mode is explicit for missing workflow-process-design dependency.
- [ ] Operator review is required for conflicts that change output scope, project priority, or execution shape.
- [ ] Examples include valid, degraded, and conflict cases.

---

# NEXT PROMPT

Paste this next:
> Prompt PND10:
> Create exactly one file.
>
> # FILE: .claude/skills/precap-next-day/references/validation-checklist.md
>
> File type: reference_rules.
> Schema ownership: owns PreCapNextDay validation checklist and final completion checks.
> Context carry-forward:
> - .claude/skills/precap-next-day/SKILL.md
> - .claude/skills/precap-next-day/references/input-intake-and-resilience-contract.md
> - .claude/skills/precap-next-day/references/daily-plan-output-contract.md
> - .claude/skills/precap-next-day/references/flow-packet-contract.md
> - .claude/skills/precap-next-day/references/flow-prompt-pack-contract.md
> - .claude/skills/precap-next-day/references/prompt-engineering-dependency-contract.md
> - .claude/skills/precap-next-day/references/usage-tracking-dependency-contract.md
> - .claude/skills/precap-next-day/references/calendar-event-write-contract.md
> - .claude/skills/precap-next-day/references/workflow-process-validation-contract.md
>
> This file must define:
> - final PreCapNextDay validation checklist
> - required artifact presence checks
> - dependency degradation checks
> - operator review checks
> - calendar write request checks
> - prompt pack checks
> - usage tracking checks
> - FlowRecap readiness checks
> - examples of pass, warning, and blocked outcomes
>
> Rules:
> - Do not duplicate schemas from prior contracts.
> - Do not create package manifest content owned by PND11.
> - Do not create actual daily plan output.
> - Use YAML with 2-space indentation.
>
> Next prompt target: Prompt PND11.
