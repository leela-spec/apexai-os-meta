# FILE: .claude/skills/precap-next-day/references/flow-prompt-pack-contract.md

# Flow Prompt Pack Contract

```yaml
flow_prompt_pack_contract:
  artifact_name: flow_prompt_pack
  file_role: precap_next_day_reference_contract
  purpose: >
    Define the minimum valid structure for one PreCapNextDay per-flow prompt
    pack. A flow_prompt_pack is the per-flow operational prompt container that
    groups sprint prompt sequences, prompt_packet references, routing and usage
    references, provider and prompt-design rationale references, light capture
    hints, and FlowRecap preparation notes. This file is a reference contract,
    not prompt doctrine, not a routing schema, not a usage-log schema, and not a
    daily-plan schema.

  ownership:
    owns:
      - flow_prompt_pack
      - flow_prompt_pack_metadata
      - prompt_pack_policy
      - sprint_prompt_sequence_grouping
      - sprint_prompt_sequence_reference
      - prompt_packet_reference
      - routing_usage_reference
      - provider_prompt_design_rationale_reference
      - prompt_placement_rules
      - light_capture_hints_for_prompt_pack
      - FlowRecap_prompt_pack_preparation_notes
      - flow_prompt_pack_validation_rules
      - flow_prompt_pack_examples
    must_not_own:
      - prompt_packet
      - prompt_sequence
      - final_copy_paste_prompt
      - provider_specific_prompting_rules
      - prompt_quality_review
      - routing_decision
      - routing_recommendation_packet
      - planned_usage_budget
      - usage_delta
      - monthly_quota_map
      - AI_surface_inventory
      - workflow_stage_taxonomy
      - process_stage_taxonomy
      - expected_output_type_schema
      - next_day_plan
      - flow_packet
      - FlowRecap_output
      - project_status_merge

  dependency_contracts:
    precap_next_day_skill: ../SKILL.md
    input_intake_and_resilience_contract: references/input-intake-and-resilience-contract.md
    daily_plan_output_contract: references/daily-plan-output-contract.md
    flow_packet_contract: references/flow-packet-contract.md
    prompt_packet_contract: ../prompt-engineering/references/prompt-packet-contract.md
    prompt_engineering_dependency_contract: references/prompt-engineering-dependency-contract.md
    usage_tracking_dependency_contract: references/usage-tracking-dependency-contract.md
    routing_recommendation_packet_contract: ../ai-routing-and-usage-tracking/references/routing-recommendation-packet-contract.md
    workflow_process_validation_contract: references/workflow-process-validation-contract.md
    prompt_process_alignment_validation: ../workflow-process-design/references/prompt-process-alignment-validation.md

  global_rules:
    one_prompt_pack_per_flow: true
    prompt_pack_belongs_to_one_flow_packet: true
    sprint_prompt_sequences_group_prompts_by_sprint: true
    prompt_packets_are_referenced_not_redefined: true
    prompt_engineering_owns_prompt_doctrine: true
    ai_routing_owns_routing_and_usage_recommendations: true
    workflow_process_design_owns_alignment_validation: true
    one_primary_prompt_system_per_prompt_packet: true
    fallback_notes_allowed: true
    parallel_alternative_prompt_systems_forbidden_by_default: true
    machine_readable_capture_block_inside_every_prompt_required: false
    light_capture_hints_allowed: true
    FlowRecap_preparation_notes_required: true
    prompt_pack_may_be_degraded_if_dependencies_missing: true
    project_work_not_executed: true
    prompts_not_executed_by_PreCapNextDay: true
```

## Schema: flow_prompt_pack

```yaml
flow_prompt_pack:
  type: object
  required:
    - pack_id
    - artifact_name
    - created_or_updated_at
    - execution_day
    - flow_id
    - project
    - generation_mode
    - pack_status
    - prompt_pack_policy
    - source_flow_packet_ref
    - sprint_prompt_sequences
    - routing_usage_summary
    - workflow_alignment_summary
    - FlowRecap_preparation
    - validation_status

  fields:
    pack_id:
      type: string
      format: "flow_prompt_pack_<execution_day>_<flow_id>"
      required: true

    artifact_name:
      type: string
      const: flow_prompt_pack
      required: true

    created_or_updated_at:
      type: string
      format: "YYYY-MM-DD"
      required: true

    execution_day:
      type: string
      format: "YYYY-MM-DD"
      required: true

    flow_id:
      type: string
      allowed:
        - F1
        - F2
        - F3
        - F4
        - operator_defined
      required: true

    project:
      type: string
      allowed:
        - Leela
        - MasterOfArts
        - Apex
        - Residual
        - Investment
        - Others
        - operator_defined
      required: true

    generation_mode:
      type: string
      allowed:
        - full_context_mode
        - standard_mode
        - recap_recovery_mode
        - bootstrap_mode
        - calendar_constrained_mode
        - prompt_heavy_mode
        - degraded_generic_prompt_mode
      required: true

    pack_status:
      type: string
      allowed:
        - ready_for_operator_review
        - operator_approved
        - operator_review_recommended
        - auto_generated
        - low_confidence_auto_generated
        - blocked_by_missing_operator_decision
      required: true

    prompt_pack_policy:
      type: object_ref
      ref: prompt_pack_policy
      required: true

    source_flow_packet_ref:
      type: object_ref
      ref: source_flow_packet_ref
      required: true

    daily_plan_ref:
      type: object_ref
      ref: daily_plan_ref
      required: false

    sprint_prompt_sequences:
      type: list
      item_ref: sprint_prompt_sequence_group
      min_items: 0
      max_items: 3
      required: true

    routing_usage_summary:
      type: object_ref
      ref: routing_usage_summary
      required: true

    workflow_alignment_summary:
      type: object_ref
      ref: workflow_alignment_summary
      required: true

    light_capture_hints:
      type: object_ref
      ref: light_capture_hints_for_prompt_pack
      required: false

    FlowRecap_preparation:
      type: object_ref
      ref: FlowRecap_prompt_pack_preparation
      required: true

    dependency_status:
      type: object_ref
      ref: prompt_pack_dependency_status
      required: false

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

## Schema: prompt_pack_policy

```yaml
prompt_pack_policy:
  type: object
  required:
    - storage_policy
    - prompt_system_policy
    - prompt_capture_policy
    - provider_rationale_policy
    - fallback_policy

  fields:
    storage_policy:
      type: object
      required:
        - one_file_per_flow_prompt_pack
        - embedded_in_daily_plan
        - referenced_from_flow_packet
      fields:
        one_file_per_flow_prompt_pack:
          type: boolean
          const: true
        embedded_in_daily_plan:
          type: boolean
          const: false
        referenced_from_flow_packet:
          type: boolean
          const: true

    prompt_system_policy:
      type: object
      required:
        - one_primary_prompt_system_only
        - alternatives_allowed_by_default
        - follow_up_prompts_allowed
      fields:
        one_primary_prompt_system_only:
          type: boolean
          const: true
        alternatives_allowed_by_default:
          type: boolean
          const: false
        follow_up_prompts_allowed:
          type: boolean
          const: true
        max_follow_up_prompts_per_sprint:
          type: integer
          min: 0
          max: 6

    prompt_capture_policy:
      type: object
      required:
        - light_capture_hints_allowed
        - mandatory_machine_readable_capture_block_inside_every_prompt
        - canonical_capture_home
      fields:
        light_capture_hints_allowed:
          type: boolean
          const: true
        mandatory_machine_readable_capture_block_inside_every_prompt:
          type: boolean
          const: false
        canonical_capture_home:
          type: string
          allowed:
            - raw_flow_dump
            - FlowRecap

    provider_rationale_policy:
      type: object
      required:
        - provider_rationale_required
        - prompt_design_rationale_required
        - rationale_source
      fields:
        provider_rationale_required:
          type: boolean
          const: true
        prompt_design_rationale_required:
          type: boolean
          const: true
        rationale_source:
          type: string
          allowed:
            - prompt_packet_reference
            - routing_recommendation_reference
            - degraded_generic_prompt_mode_note

    fallback_policy:
      type: object
      required:
        - fallback_notes_allowed
        - fallback_prompt_system_allowed_by_default
      fields:
        fallback_notes_allowed:
          type: boolean
          const: true
        fallback_prompt_system_allowed_by_default:
          type: boolean
          const: false
        fallback_requires_operator_review:
          type: boolean
          const: true
```

## Schema: source and dependency references

```yaml
source_flow_packet_ref:
  type: object
  required:
    - flow_packet_id
    - flow_packet_path_or_slot
    - flow_id
    - project
  fields:
    flow_packet_id:
      type: string
      required: true
    flow_packet_path_or_slot:
      type: string
      required: true
    flow_id:
      type: string
      required: true
    project:
      type: string
      required: true


daily_plan_ref:
  type: object
  required:
    - next_day_plan_id
    - next_day_plan_path_or_slot
  fields:
    next_day_plan_id:
      type: string
      required: true
    next_day_plan_path_or_slot:
      type: string
      required: true


prompt_pack_dependency_status:
  type: object
  required:
    - prompt_engineering_status
    - ai_routing_status
    - workflow_process_status
  fields:
    prompt_engineering_status:
      type: string
      allowed:
        - available
        - partially_available
        - missing_use_degraded_generic_prompt_mode
        - unknown
      required: true
    ai_routing_status:
      type: string
      allowed:
        - available
        - partially_available
        - missing_use_provider_unspecified
        - unknown
      required: true
    workflow_process_status:
      type: string
      allowed:
        - available
        - partially_available
        - missing_use_operator_review_recommended
        - unknown
      required: true
    missing_dependency_notes:
      type: list
      item_type: string
      required: false
```

## Schema: sprint prompt sequence grouping

```yaml
sprint_prompt_sequence_group:
  type: object
  required:
    - sprint_id
    - sprint_role
    - sprint_status
    - expected_output_type_ref
    - workflow_stage_ref
    - process_stage_ref
    - start_prompt_ref
    - prompt_packet_refs
    - placement_rules_applied
    - validation_status

  fields:
    sprint_id:
      type: string
      allowed:
        - S1
        - S2
        - S3
        - operator_defined
      required: true

    sprint_role:
      type: string
      allowed:
        - first_work_sprint
        - second_work_or_deepening_sprint
        - recap_digest_preparation_sprint
        - compressed_sprint
        - skipped_sprint
        - operator_defined
      required: true

    sprint_status:
      type: string
      allowed:
        - active
        - compressed
        - skipped
        - blocked
        - operator_review_needed
      required: true

    expected_output_type_ref:
      type: object_ref
      ref: expected_output_type_ref
      required: true

    workflow_stage_ref:
      type: object_ref
      ref: workflow_stage_ref
      required: true

    process_stage_ref:
      type: object_ref
      ref: process_stage_ref
      required: true

    start_prompt_ref:
      type: object_ref
      ref: prompt_packet_reference
      required: true

    follow_up_prompt_refs:
      type: list
      item_ref: prompt_packet_reference
      min_items: 0
      max_items: 6
      required: false

    prompt_sequence_ref:
      type: object_ref
      ref: prompt_sequence_reference
      required: false

    prompt_packet_refs:
      type: list
      item_ref: prompt_packet_reference
      min_items: 1
      max_items: 8
      required: true

    routing_usage_reference:
      type: object_ref
      ref: routing_usage_reference
      required: false

    light_capture_hints:
      type: object_ref
      ref: sprint_light_capture_hints
      required: false

    placement_rules_applied:
      type: list
      item_type: string
      min_items: 1
      max_items: 12
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

## Schema: external prompt references

```yaml
prompt_packet_reference:
  type: object
  purpose: >
    Reference a prompt_packet owned by prompt-engineering without duplicating
    prompt_packet schema or final prompt body rules.
  required:
    - prompt_packet_id
    - packet_role
    - prompt_task_type
    - provider_target
    - prompt_packet_path_or_slot
  fields:
    prompt_packet_id:
      type: string
      required: true
    packet_role:
      type: string
      allowed:
        - start_prompt
        - follow_up_prompt
        - prompt_sequence_container
        - standalone_prompt_packet
      required: true
    prompt_task_type:
      type: string
      required: true
      note: "Use prompt-engineering prompt-task-taxonomy values."
    provider_target:
      type: string
      allowed:
        - ChatGPT
        - Claude
        - Gemini
        - OpenRouter_later
        - provider_unspecified
      required: true
    prompt_packet_path_or_slot:
      type: string
      required: true
    provider_rationale_ref:
      type: string
      required: false
      note: "Reference only; provider_rationale schema is owned by prompt-engineering."
    prompt_design_rationale_ref:
      type: string
      required: false
      note: "Reference only; prompt_design_rationale schema is owned by prompt-engineering."
    final_copy_paste_prompt_ref:
      type: string
      required: false
      note: "Reference only; final_copy_paste_prompt schema is owned by prompt-engineering."
    prompt_failure_hints_ref:
      type: string
      required: false
    prompt_learning_hints_ref:
      type: string
      required: false


prompt_sequence_reference:
  type: object
  purpose: >
    Reference a prompt_sequence owned by prompt-engineering when a sprint uses
    a start prompt plus follow-up prompts as a coherent sequence.
  required:
    - prompt_sequence_id
    - prompt_sequence_path_or_slot
    - sequence_logic
  fields:
    prompt_sequence_id:
      type: string
      required: true
    prompt_sequence_path_or_slot:
      type: string
      required: true
    sequence_logic:
      type: string
      required: true
      note: "Use prompt-engineering iteration-loop-pattern values."
```

## Schema: workflow and expected-output references

```yaml
expected_output_type_ref:
  type: object
  required:
    - expected_output_type
    - expected_output_contract_ref
  fields:
    expected_output_type:
      type: string
      required: true
      note: "Use workflow-process-design expected-output-type-contract values."
    expected_output_contract_ref:
      type: string
      required: true
    expected_output_notes:
      type: string
      required: false


workflow_stage_ref:
  type: object
  required:
    - workflow_stage
    - taxonomy_ref
  fields:
    workflow_stage:
      type: string
      required: true
      note: "Use workflow-process-design workflow-stage-taxonomy values."
    taxonomy_ref:
      type: string
      required: true


process_stage_ref:
  type: object
  required:
    - process_stage
    - taxonomy_ref
  fields:
    process_stage:
      type: string
      required: true
      note: "Use workflow-process-design process-stage-taxonomy values."
    taxonomy_ref:
      type: string
      required: true
```

## Schema: routing and usage references

```yaml
routing_usage_summary:
  type: object
  required:
    - routing_source_status
    - route_mode
    - primary_surface_class
    - planned_usage_budget_ref
    - usage_tracking_tags_ref
    - operator_review_needed
  fields:
    routing_source_status:
      type: string
      allowed:
        - routing_recommendation_available
        - routing_recommendation_partial
        - routing_recommendation_missing
        - operator_override
      required: true

    route_mode:
      type: string
      allowed:
        - planned_flow_session
        - supplemental_or_batch_execution
        - degraded_provider_unspecified
        - operator_override
      required: true

    primary_surface_class:
      type: string
      allowed:
        - subscription_frontier_chat
        - subscription_frontier_reasoning
        - deep_research_surface
        - agent_run_surface
        - code_agent_surface
        - long_context_surface
        - supplemental_api_low_cost
        - provider_unspecified
      required: true

    routing_recommendation_packet_ref:
      type: string
      required: false
      note: "Reference only; routing_recommendation_packet schema is owned by ai-routing-and-usage-tracking."

    planned_usage_budget_ref:
      type: string
      required: true
      note: "Reference only; planned_usage_budget schema is owned by ai-routing-and-usage-tracking."

    usage_tracking_tags_ref:
      type: string
      required: true
      note: "Reference only; usage_tracking_tags schema is owned by prompt-engineering or ai-routing-and-usage-tracking interface contracts."

    quota_or_scarcity_note:
      type: string
      required: false
      rule: "Use abstract scarcity notes only unless current verified usage was supplied."

    operator_review_needed:
      type: boolean
      required: true


routing_usage_reference:
  type: object
  required:
    - routing_recommendation_ref
    - planned_usage_budget_ref
    - usage_capture_expected
  fields:
    routing_recommendation_ref:
      type: string
      required: true
    planned_usage_budget_ref:
      type: string
      required: true
    usage_capture_expected:
      type: boolean
      required: true
    usage_capture_home:
      type: string
      allowed:
        - FlowRecap_usage_delta
        - automated_API_logs_later
        - operator_manual_note
      required: false
```

## Schema: workflow alignment summary

```yaml
workflow_alignment_summary:
  type: object
  required:
    - alignment_source_status
    - prompt_process_alignment_status
    - workflow_stage_coverage
    - process_stage_coverage
    - expected_output_coverage
  fields:
    alignment_source_status:
      type: string
      allowed:
        - validated
        - valid_with_warnings
        - partially_validated
        - missing_validation
        - operator_review_recommended
      required: true

    prompt_process_alignment_status:
      type: string
      allowed:
        - aligned
        - aligned_with_warnings
        - mismatched
        - incomplete
        - unknown
      required: true

    workflow_stage_coverage:
      type: list
      item_type: string
      required: true

    process_stage_coverage:
      type: list
      item_type: string
      required: true

    expected_output_coverage:
      type: list
      item_type: string
      required: true

    alignment_validation_ref:
      type: string
      required: false

    red_flags:
      type: list
      item_type: string
      required: false
```

## Prompt Placement Rules

```yaml
prompt_placement_rules:
  start_prompt_rules:
    - rule_id: one_start_prompt_per_active_sprint
      requirement: "Every active sprint must reference exactly one start_prompt prompt_packet."
    - rule_id: start_prompt_first
      requirement: "The start_prompt_ref must appear before follow_up_prompt_refs in each sprint group."
    - rule_id: start_prompt_clean_copy_paste
      requirement: "The referenced start prompt must be copy-paste-ready according to prompt-engineering."

  follow_up_prompt_rules:
    - rule_id: follow_ups_optional
      requirement: "Follow-up prompts are optional and should only appear when the sprint likely needs iteration."
    - rule_id: no_parallel_alternative_systems
      requirement: "Follow-up prompts may refine or continue the primary system, but must not create parallel alternative prompt systems by default."
    - rule_id: bounded_follow_up_count
      requirement: "Use zero to six follow-up prompts per sprint unless the operator explicitly requests more."

  sprint_grouping_rules:
    - rule_id: group_by_sprint
      requirement: "Group prompt packets under S1, S2, and S3 rather than as one undifferentiated prompt list."
    - rule_id: preserve_sprint_role
      requirement: "Each sprint group must preserve first work, deepening, or recap-digest role."
    - rule_id: skipped_sprint_has_no_prompt_requirement
      requirement: "Skipped sprints do not require prompt_packet_refs but require a skip reason in the flow_packet or daily plan."

  rationale_rules:
    - rule_id: rationale_referenced_not_rewritten
      requirement: "Provider and prompt-design rationales are referenced from prompt packets or routing recommendations, not redefined as new schemas here."
    - rule_id: degraded_mode_flagged
      requirement: "If prompt-engineering or routing dependencies are missing, mark degraded_generic_prompt_mode and operator_review_recommended."
```

## Light Capture Hints and FlowRecap Preparation

```yaml
light_capture_hints_for_prompt_pack:
  type: object
  required:
    - capture_policy
    - suggested_operator_notes
  fields:
    capture_policy:
      type: string
      allowed:
        - light_hints_only
        - defer_to_raw_flow_dump
        - defer_to_FlowRecap
      required: true
    suggested_operator_notes:
      type: list
      item_type: string
      max_items: 12
      required: true
    forbidden_capture_requirements:
      type: list
      item_type: string
      required: false
      default:
        - mandatory_machine_readable_capture_block_inside_every_prompt
        - prompt_embedded_full_recap_schema
        - prompt_embedded_status_merge_schema


sprint_light_capture_hints:
  type: object
  required:
    - what_to_save_after_prompt
    - what_to_flag_for_recap
  fields:
    what_to_save_after_prompt:
      type: list
      item_type: string
      max_items: 8
      required: true
    what_to_flag_for_recap:
      type: list
      item_type: string
      max_items: 8
      required: true


FlowRecap_prompt_pack_preparation:
  type: object
  required:
    - FlowRecap_handoff_role
    - expected_usage_capture
    - expected_prompt_result_feedback
    - raw_flow_dump_connection
  fields:
    FlowRecap_handoff_role:
      type: string
      allowed:
        - prepare_prompt_execution_context_only
      required: true
    expected_usage_capture:
      type: boolean
      required: true
    expected_prompt_result_feedback:
      type: boolean
      required: true
    raw_flow_dump_connection:
      type: string
      allowed:
        - use_flow_packet_raw_flow_dump_template
        - use_operator_manual_dump
        - skipped_flow_no_dump_expected
      required: true
    suggested_recap_fields:
      type: list
      item_type: string
      max_items: 12
      required: false
```

## Validation Rules

```yaml
flow_prompt_pack_validation_rules:
  required_checks:
    one_pack_per_flow:
      rule: "A flow_prompt_pack must map to exactly one flow_id and one source flow_packet."
      severity: critical
    sprint_grouping_present:
      rule: "Active flow packs must group prompts by sprint rather than by provider or task only."
      severity: high
    prompt_packets_referenced_not_redefined:
      rule: "The file may reference prompt_packet IDs or slots but must not redefine prompt_packet schema."
      severity: critical
    routing_references_not_redefined:
      rule: "The file may reference routing recommendations and planned usage budgets but must not redefine their schemas."
      severity: critical
    start_prompt_before_follow_ups:
      rule: "Each active sprint group must place start_prompt_ref before follow_up_prompt_refs."
      severity: high
    no_parallel_alternatives_by_default:
      rule: "Do not include multiple alternative prompt systems unless the operator explicitly requests comparison."
      severity: high
    light_capture_only:
      rule: "Do not require a machine-readable capture block inside every prompt."
      severity: high
    FlowRecap_preparation_present:
      rule: "Include FlowRecap preparation notes without running FlowRecap."
      severity: high
    degraded_mode_flagged:
      rule: "If dependencies are missing, mark degraded mode and operator review."
      severity: medium

  correction_rules:
    prompt_schema_duplication_detected:
      correction: "Remove duplicated fields and replace with prompt_packet_reference."
    routing_schema_duplication_detected:
      correction: "Remove duplicated fields and replace with routing_usage_reference."
    ungrouped_prompt_list_detected:
      correction: "Group prompt references under S1, S2, and S3."
    parallel_prompt_systems_detected:
      correction: "Keep one primary prompt system and convert alternatives into fallback notes or operator review options."
    hard_capture_block_detected:
      correction: "Replace mandatory capture block with light capture hints and FlowRecap preparation notes."
```

## Examples

```yaml
flow_prompt_pack_examples:
  standard_Leela_flow_prompt_pack:
    pack_id: flow_prompt_pack_2026-06-17_F1
    artifact_name: flow_prompt_pack
    created_or_updated_at: "2026-06-16"
    execution_day: "2026-06-17"
    flow_id: F1
    project: Leela
    generation_mode: standard_mode
    pack_status: ready_for_operator_review
    prompt_pack_policy:
      storage_policy:
        one_file_per_flow_prompt_pack: true
        embedded_in_daily_plan: false
        referenced_from_flow_packet: true
      prompt_system_policy:
        one_primary_prompt_system_only: true
        alternatives_allowed_by_default: false
        follow_up_prompts_allowed: true
        max_follow_up_prompts_per_sprint: 3
      prompt_capture_policy:
        light_capture_hints_allowed: true
        mandatory_machine_readable_capture_block_inside_every_prompt: false
        canonical_capture_home: raw_flow_dump
      provider_rationale_policy:
        provider_rationale_required: true
        prompt_design_rationale_required: true
        rationale_source: prompt_packet_reference
      fallback_policy:
        fallback_notes_allowed: true
        fallback_prompt_system_allowed_by_default: false
        fallback_requires_operator_review: true
    source_flow_packet_ref:
      flow_packet_id: flow_packet_2026-06-17_F1
      flow_packet_path_or_slot: artifacts/flows/packets/2026-06-17/F1.md
      flow_id: F1
      project: Leela
    sprint_prompt_sequences:
      - sprint_id: S1
        sprint_role: first_work_sprint
        sprint_status: active
        expected_output_type_ref:
          expected_output_type: product_system_notes
          expected_output_contract_ref: workflow-process-design/references/expected-output-type-contract.md
        workflow_stage_ref:
          workflow_stage: system_definition
          taxonomy_ref: workflow-process-design/references/workflow-stage-taxonomy.md
        process_stage_ref:
          process_stage: draft_generation
          taxonomy_ref: workflow-process-design/references/process-stage-taxonomy.md
        start_prompt_ref:
          prompt_packet_id: prompt_packet_leela_spatial_system_S1_start
          packet_role: start_prompt
          prompt_task_type: file_generation
          provider_target: Claude
          prompt_packet_path_or_slot: prompt_packs/2026-06-17/F1/S1-start.md
        follow_up_prompt_refs:
          - prompt_packet_id: prompt_packet_leela_spatial_system_S1_critique
            packet_role: follow_up_prompt
            prompt_task_type: critique
            provider_target: Claude
            prompt_packet_path_or_slot: prompt_packs/2026-06-17/F1/S1-follow-up-1.md
        prompt_packet_refs:
          - prompt_packet_id: prompt_packet_leela_spatial_system_S1_start
            packet_role: start_prompt
            prompt_task_type: file_generation
            provider_target: Claude
            prompt_packet_path_or_slot: prompt_packs/2026-06-17/F1/S1-start.md
        placement_rules_applied:
          - one_start_prompt_per_active_sprint
          - start_prompt_first
          - follow_ups_optional
          - group_by_sprint
        validation_status: valid_with_warnings
    routing_usage_summary:
      routing_source_status: routing_recommendation_available
      route_mode: planned_flow_session
      primary_surface_class: subscription_frontier_reasoning
      routing_recommendation_packet_ref: routing_recommendation_packet_2026-06-17_F1
      planned_usage_budget_ref: planned_usage_budget_2026-06-17
      usage_tracking_tags_ref: usage_tracking_tags_F1_Leela
      quota_or_scarcity_note: Use abstract scarcity notes only; exact remaining quota not supplied.
      operator_review_needed: true
    workflow_alignment_summary:
      alignment_source_status: valid_with_warnings
      prompt_process_alignment_status: aligned_with_warnings
      workflow_stage_coverage:
        - system_definition
      process_stage_coverage:
        - draft_generation
        - critique_revision
      expected_output_coverage:
        - product_system_notes
      red_flags:
        - Confirm whether S2 should deepen architecture or produce implementation notes.
    light_capture_hints:
      capture_policy: light_hints_only
      suggested_operator_notes:
        - Save final useful output.
        - Note any major design decision.
        - Note any blocker or unresolved question.
        - Note actual provider or surface used.
    FlowRecap_preparation:
      FlowRecap_handoff_role: prepare_prompt_execution_context_only
      expected_usage_capture: true
      expected_prompt_result_feedback: true
      raw_flow_dump_connection: use_flow_packet_raw_flow_dump_template
      suggested_recap_fields:
        - prompt_results
        - artifacts_created
        - decisions
        - blockers
        - model_usage_delta
    validation_status: valid_with_warnings

  compressed_residual_flow_prompt_pack:
    pack_id: flow_prompt_pack_2026-06-17_F4
    artifact_name: flow_prompt_pack
    created_or_updated_at: "2026-06-16"
    execution_day: "2026-06-17"
    flow_id: F4
    project: Residual
    generation_mode: calendar_constrained_mode
    pack_status: operator_review_recommended
    source_flow_packet_ref:
      flow_packet_id: flow_packet_2026-06-17_F4
      flow_packet_path_or_slot: artifacts/flows/packets/2026-06-17/F4.md
      flow_id: F4
      project: Residual
    sprint_prompt_sequences:
      - sprint_id: S1
        sprint_role: compressed_sprint
        sprint_status: compressed
        expected_output_type_ref:
          expected_output_type: cleanup_decision_notes
          expected_output_contract_ref: workflow-process-design/references/expected-output-type-contract.md
        workflow_stage_ref:
          workflow_stage: prioritization_cleanup
          taxonomy_ref: workflow-process-design/references/workflow-stage-taxonomy.md
        process_stage_ref:
          process_stage: extract_normalize_validate
          taxonomy_ref: workflow-process-design/references/process-stage-taxonomy.md
        start_prompt_ref:
          prompt_packet_id: prompt_packet_residual_cleanup_S1_start
          packet_role: start_prompt
          prompt_task_type: synthesis
          provider_target: ChatGPT
          prompt_packet_path_or_slot: prompt_packs/2026-06-17/F4/S1-start.md
        prompt_packet_refs:
          - prompt_packet_id: prompt_packet_residual_cleanup_S1_start
            packet_role: start_prompt
            prompt_task_type: synthesis
            provider_target: ChatGPT
            prompt_packet_path_or_slot: prompt_packs/2026-06-17/F4/S1-start.md
        placement_rules_applied:
          - group_by_sprint
          - preserve_sprint_role
          - no_parallel_alternative_systems
        operator_review_flags:
          - compressed_flow_confirm_scope
        validation_status: operator_review_recommended
    routing_usage_summary:
      routing_source_status: routing_recommendation_partial
      route_mode: planned_flow_session
      primary_surface_class: subscription_frontier_chat
      planned_usage_budget_ref: planned_usage_budget_2026-06-17
      usage_tracking_tags_ref: usage_tracking_tags_F4_Residual
      operator_review_needed: true
    workflow_alignment_summary:
      alignment_source_status: partially_validated
      prompt_process_alignment_status: incomplete
      workflow_stage_coverage:
        - prioritization_cleanup
      process_stage_coverage:
        - extract_normalize_validate
      expected_output_coverage:
        - cleanup_decision_notes
      red_flags:
        - Residual flow scope must be confirmed before execution.
    FlowRecap_preparation:
      FlowRecap_handoff_role: prepare_prompt_execution_context_only
      expected_usage_capture: true
      expected_prompt_result_feedback: true
      raw_flow_dump_connection: use_flow_packet_raw_flow_dump_template
    validation_status: operator_review_recommended

  degraded_generic_prompt_pack:
    pack_id: flow_prompt_pack_2026-06-17_F3
    artifact_name: flow_prompt_pack
    created_or_updated_at: "2026-06-16"
    execution_day: "2026-06-17"
    flow_id: F3
    project: Apex
    generation_mode: degraded_generic_prompt_mode
    pack_status: low_confidence_auto_generated
    dependency_status:
      prompt_engineering_status: missing_use_degraded_generic_prompt_mode
      ai_routing_status: missing_use_provider_unspecified
      workflow_process_status: partially_available
      missing_dependency_notes:
        - Prompt-engineering package not available; use generic structured prompt only.
        - Routing recommendation unavailable; use provider_unspecified and operator review.
    sprint_prompt_sequences: []
    routing_usage_summary:
      routing_source_status: routing_recommendation_missing
      route_mode: degraded_provider_unspecified
      primary_surface_class: provider_unspecified
      planned_usage_budget_ref: unknown
      usage_tracking_tags_ref: unknown
      operator_review_needed: true
    workflow_alignment_summary:
      alignment_source_status: partially_validated
      prompt_process_alignment_status: unknown
      workflow_stage_coverage: []
      process_stage_coverage: []
      expected_output_coverage: []
      red_flags:
        - Missing prompt-engineering dependency.
        - Missing routing recommendation.
    FlowRecap_preparation:
      FlowRecap_handoff_role: prepare_prompt_execution_context_only
      expected_usage_capture: true
      expected_prompt_result_feedback: true
      raw_flow_dump_connection: use_flow_packet_raw_flow_dump_template
    operator_review_flags:
      - degraded_generic_prompt_mode
      - provider_unspecified
      - prompt_pack_requires_review_before_execution
    validation_status: low_confidence_auto_generated
```

---

# VALIDATION - FILE-SPECIFIC CHECKS

- [ ] Exactly one file was produced.
- [ ] File path is `.claude/skills/precap-next-day/references/flow-prompt-pack-contract.md`.
- [ ] File owns `flow_prompt_pack` as the per-flow operational prompt container produced by PreCapNextDay.
- [ ] File defines one-prompt-pack-per-flow policy.
- [ ] File defines sprint prompt sequence grouping for S1/S2/S3.
- [ ] File references `prompt_packet` and `prompt_sequence` without duplicating their schemas.
- [ ] File references routing and usage artifacts without defining `routing_decision`, `planned_usage_budget`, or `usage_delta` schemas.
- [ ] File includes provider and prompt-design rationale references without redefining prompt-engineering doctrine.
- [ ] File defines start prompt and follow-up prompt placement rules.
- [ ] File includes light capture hints and FlowRecap preparation notes.
- [ ] File does not create multiple alternative prompt systems by default.
- [ ] File does not require a machine-readable capture block inside every prompt.
- [ ] YAML blocks use 2-space indentation.
- [ ] Numeric constraints use typed `type`/`min`/`max` objects.
- [ ] File does not execute prompts, execute project work, run FlowRecap, merge project status, create calendar events, or finalize OpenRouter model mapping.

---

# NEXT PROMPT

Paste this next:
> Prompt PND6:
> Create exactly one file.
>
> # FILE: .claude/skills/precap-next-day/references/prompt-engineering-dependency-contract.md
>
> File type: dependency_contract.
> Schema ownership: owns the PreCapNextDay-to-prompt-engineering dependency interface, degraded-mode behavior, and prompt-pack assembly expectations.
> Context carry-forward:
> - .claude/skills/precap-next-day/SKILL.md
> - .claude/skills/precap-next-day/references/flow-prompt-pack-contract.md
> - .claude/skills/prompt-engineering/SKILL.md
> - .claude/skills/prompt-engineering/references/prompt-packet-contract.md
> - .claude/skills/prompt-engineering/references/prompt-task-taxonomy.md
> - .claude/skills/prompt-engineering/references/iteration-loop-patterns.md
> - .claude/skills/prompt-engineering/references/prompt-quality-validation.md
>
> This file must define:
> - dependency interface between PreCapNextDay and prompt-engineering
> - required prompt-engineering inputs and outputs
> - prompt-pack assembly expectations
> - degraded generic prompt mode when prompt-engineering is missing
> - provider-specific style availability handling
> - prompt quality validation handoff
> - prompt learning hint handoff
> - minimal examples
>
> Rules:
> - Do not redefine prompt_packet schema owned by prompt-engineering.
> - Do not redefine flow_prompt_pack schema owned by PND5.
> - Do not make PreCapNextDay own prompt doctrine.
> - Do not create multiple alternative prompt systems by default.
> - Use YAML with 2-space indentation.
>
> Next prompt target: Prompt PND7.
