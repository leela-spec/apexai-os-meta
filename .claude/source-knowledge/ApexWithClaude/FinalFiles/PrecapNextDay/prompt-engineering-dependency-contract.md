# FILE: .claude/skills/precap-next-day/references/prompt-engineering-dependency-contract.md

# Prompt Engineering Dependency Contract

```yaml
prompt_engineering_dependency_contract:
  artifact_name: prompt_engineering_dependency_contract
  file_role: precap_next_day_dependency_reference
  purpose: >
    Define how PreCapNextDay consumes the prompt-engineering skill package when
    compiling flow_prompt_pack and prompt_execution_packet outputs. This file is
    an interface contract, not prompt doctrine, not a prompt_packet schema, and
    not a provider-specific prompting guide.

  ownership:
    owns:
      - prompt_engineering_dependency_interface
      - prompt_engineering_availability_states
      - prompt_compilation_inputs_required_by_PreCapNextDay
      - prompt_compilation_outputs_expected_from_prompt_engineering
      - degraded_generic_prompt_mode
      - prompt_quality_gate_interface
      - provider_style_contract_reference_policy
      - prompt_learning_hint_interface
      - PreCapNextDay_prompt_boundary_rules
      - dependency_examples
    must_not_own:
      - prompt_packet_schema
      - prompt_sequence_schema
      - final_copy_paste_prompt_schema
      - provider_specific_prompting_rules
      - prompt_task_taxonomy
      - iteration_loop_patterns
      - routing_decision_schema
      - workflow_stage_taxonomy
      - process_stage_taxonomy
      - flow_prompt_pack_schema
      - daily_plan_schema

  upstream_authority:
    prompt_engineering_package: ".claude/skills/prompt-engineering/"
    canonical_prompt_packet_contract: ".claude/skills/prompt-engineering/references/prompt-packet-contract.md"
    canonical_prompt_task_taxonomy: ".claude/skills/prompt-engineering/references/prompt-task-taxonomy.md"
    canonical_iteration_loops: ".claude/skills/prompt-engineering/references/iteration-loop-patterns.md"
    provider_style_contracts:
      - ".claude/skills/prompt-engineering/references/provider-style-contract-chatgpt.md"
      - ".claude/skills/prompt-engineering/references/provider-style-contract-claude.md"
      - ".claude/skills/prompt-engineering/references/provider-style-contract-gemini.md"
      - ".claude/skills/prompt-engineering/references/provider-style-contract-openrouter-todo.md"
    prompt_quality_validation: ".claude/skills/prompt-engineering/references/prompt-quality-validation.md"
    prompt_learning_feedback: ".claude/skills/prompt-engineering/references/prompt-learning-feedback-contract.md"

  downstream_consumer:
    skill_package: ".claude/skills/precap-next-day/"
    consumer_outputs:
      - next_day_plan
      - flow_packet
      - flow_prompt_pack
      - prompt_execution_packet
      - FlowRecap_handoff_block
```

## Dependency Boundary

```yaml
PreCapNextDay_prompt_boundary:
  owns:
    - selecting_daily_flow_context
    - selecting_sprint_goal
    - compiling_flow_prompt_pack
    - placing_prompt_execution_packets_inside_flow_prompt_pack
    - carrying_prompt_quality_flags_into_operator_review
    - carrying_prompt_learning_hints_into_FlowRecap_handoff
    - marking_prompt_engineering_dependency_status

  consumes_from_prompt_engineering:
    - prompt_packet_contract
    - prompt_task_taxonomy
    - iteration_loop_patterns
    - provider_style_contracts
    - prompt_quality_validation_rules
    - prompt_learning_feedback_contract

  must_not_do:
    - "Do not redefine prompt_packet schema."
    - "Do not redefine prompt_sequence schema."
    - "Do not redefine provider-specific prompting style contracts."
    - "Do not create prompt doctrine inside PreCapNextDay."
    - "Do not create multiple alternative prompt systems by default."
    - "Do not require machine-readable capture blocks inside every prompt."
    - "Do not treat degraded generic prompt mode as equivalent to full provider optimization."
    - "Do not override workflow-process validation or operator decision."

  correct_behavior: >
    PreCapNextDay compiles final per-flow prompt packs by requesting or applying
    prompt-engineering rules, then stores the resulting prompt packets inside
    the flow_prompt_pack structure owned by PreCapNextDay.
```

## Prompt Engineering Availability States

```yaml
prompt_engineering_availability:
  type: object
  required:
    - availability_status
    - dependency_confidence
    - validation_status

  fields:
    availability_status:
      type: string
      allowed:
        - available_full
        - available_partial
        - missing_degraded_mode
        - unavailable_blocked
      required: true

    dependency_confidence:
      type: string
      allowed:
        - high
        - medium
        - low
        - unknown
      required: true

    loaded_reference_files:
      type: list
      item_type: string
      required: false

    missing_reference_files:
      type: list
      item_type: string
      required: false

    degraded_mode_reason:
      type: string
      required: false
      nullable: true

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

## Dependency Input Interface

```yaml
prompt_engineering_dependency_input:
  type: object
  required:
    - flow_id
    - sprint_id
    - sprint_goal
    - expected_output_type
    - workflow_stage
    - process_stage
    - prompt_task_type_request
    - provider_target_or_surface_hint
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

    sprint_id:
      type: string
      allowed:
        - S1
        - S2
        - S3
        - flow_level
      required: true

    project_or_domain:
      type: string
      required: false

    sprint_goal:
      type: string
      required: true

    source_context_summary:
      type: string
      required: false

    expected_output_type:
      type: string
      required: true
      note: "Canonical validation belongs to workflow-process-design."

    workflow_stage:
      type: string
      required: true
      note: "Canonical taxonomy belongs to workflow-process-design."

    process_stage:
      type: string
      required: true
      note: "Canonical taxonomy belongs to workflow-process-design."

    prompt_task_type_request:
      type: string
      allowed:
        - research
        - synthesis
        - planning
        - coding
        - critique
        - file_generation
        - creative_generation
        - visual_briefing
        - long_context_digestion
        - validation
        - workflow_extraction
        - workflow_normalization
        - prompt_refinement
        - operator_defined
        - infer_from_context
      required: true

    iteration_loop_hint:
      type: string
      allowed:
        - start_then_optional_follow_up
        - generate_critique_revise
        - research_synthesize_decide
        - outline_expand_compress
        - extract_normalize_validate
        - compare_provider_outputs_select_finalize
        - prompt_result_learn_update
        - operator_defined
        - infer_from_context
      required: false

    provider_target_or_surface_hint:
      type: string
      allowed:
        - ChatGPT
        - Claude
        - Gemini
        - OpenRouter_later
        - provider_unspecified
        - surface_class_from_ai_routing
      required: true

    routing_context_ref:
      type: string
      required: false
      note: "Reference routing_decision or routing_recommendation_packet if available."

    prompt_constraints:
      type: list
      item_type: string
      required: false

    operator_preferences:
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

## Dependency Output Interface

```yaml
prompt_engineering_dependency_output:
  type: object
  required:
    - prompt_compilation_status
    - prompt_packet_refs
    - prompt_quality_summary
    - prompt_design_rationale_summary
    - prompt_failure_hints_summary
    - prompt_learning_hints_summary
    - validation_status

  fields:
    prompt_compilation_status:
      type: string
      allowed:
        - compiled_with_full_prompt_engineering
        - compiled_with_partial_prompt_engineering
        - compiled_in_degraded_generic_prompt_mode
        - blocked
      required: true

    prompt_packet_refs:
      type: list
      item_ref: prompt_packet
      min_items: 0
      required: true
      note: "Prompt packet schema is owned by prompt-engineering."

    prompt_sequence_ref:
      type: string
      required: false
      nullable: true
      note: "Prompt sequence schema is owned by prompt-engineering."

    final_prompt_body_location:
      type: string
      required: false
      note: "Usually embedded in flow_prompt_pack as a prompt_execution_packet."

    provider_style_contract_used:
      type: string
      allowed:
        - ChatGPT
        - Claude
        - Gemini
        - OpenRouter_later
        - provider_unspecified
        - none_degraded_generic
      required: false

    prompt_quality_summary:
      type: object
      required: true
      fields:
        quality_gate_status:
          type: string
          allowed:
            - passed
            - passed_with_warnings
            - operator_review_recommended
            - failed
            - not_checked_degraded_mode
        key_warnings:
          type: list
          item_type: string
          max_items: 8

    prompt_design_rationale_summary:
      type: string
      required: true
      rule: "Use a short rationale suitable for display inside the flow_prompt_pack."

    prompt_failure_hints_summary:
      type: list
      item_type: string
      min_items: 0
      max_items: 6
      required: true

    prompt_learning_hints_summary:
      type: list
      item_type: string
      min_items: 0
      max_items: 6
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

## Full Prompt Engineering Mode

```yaml
full_prompt_engineering_mode:
  use_when:
    - prompt_engineering_package_available
    - prompt_packet_contract_available
    - prompt_task_taxonomy_available
    - provider_style_contract_available_or_provider_unspecified_allowed
    - prompt_quality_validation_available

  required_steps:
    1: "Classify or confirm prompt_task_type from the prompt-engineering taxonomy."
    2: "Select iteration_loop from prompt-engineering loop patterns."
    3: "Apply provider style contract for the selected provider target when known."
    4: "Generate one primary copy-paste prompt or prompt sequence."
    5: "Add short provider rationale and prompt design rationale."
    6: "Add prompt failure hints and prompt learning hints."
    7: "Run prompt quality validation or mark warnings."
    8: "Return prompt packet references and summary fields for flow_prompt_pack compilation."

  required_outputs:
    - prompt_packet_refs
    - prompt_quality_summary
    - prompt_design_rationale_summary
    - prompt_failure_hints_summary
    - prompt_learning_hints_summary
    - validation_status
```

## Partial Prompt Engineering Mode

```yaml
partial_prompt_engineering_mode:
  use_when:
    - prompt_engineering_package_available
    - one_or_more_reference_files_missing
    - prompt_task_type_or_provider_style_can_still_be_inferred

  policy:
    allowed: true
    confidence_ceiling: medium
    requires_operator_review_flag: true
    must_name_missing_dependency_classes: true

  missing_dependency_handling:
    missing_provider_style_contract:
      behavior: "Use provider_unspecified prompt style and flag provider optimization as incomplete."
      validation_status: operator_review_recommended

    missing_prompt_task_taxonomy:
      behavior: "Use infer_from_context, keep task type provisional, and flag classification."
      validation_status: operator_review_recommended

    missing_quality_validation:
      behavior: "Perform only local structural checks and flag quality gate as partial."
      validation_status: valid_with_warnings

    missing_learning_feedback_contract:
      behavior: "Include simple learning hints but do not claim canonical feedback compliance."
      validation_status: valid_with_warnings
```

## Degraded Generic Prompt Mode

```yaml
degraded_generic_prompt_mode:
  use_when:
    - prompt_engineering_package_missing
    - prompt_packet_contract_unavailable
    - operator_requests_bootstrap_daily_plan
    - missing_dependency_should_not_block_next_day_plan

  policy:
    allowed: true
    confidence_ceiling: low
    validation_status: low_confidence_auto_generated
    provider_optimization_status: not_available
    must_mark_operator_review: true

  allowed_behavior:
    - create_clean_copy_paste_prompt_body
    - include short task and output contract
    - include basic constraints and stop condition
    - include minimal failure hints
    - include minimal learning hints
    - mark prompt_quality_summary.quality_gate_status as not_checked_degraded_mode

  forbidden_behavior:
    - "Do not claim provider-specific optimization."
    - "Do not claim prompt_packet contract compliance if the contract is unavailable."
    - "Do not invent prompt-engineering taxonomy values outside known allowed values."
    - "Do not block the whole next_day_plan unless the operator requires full prompt-engineering compliance."
```

## Prompt Quality Gate Interface

```yaml
prompt_quality_gate_interface:
  gate_role: flow_prompt_pack_quality_check
  authority: prompt_engineering

  required_checks:
    - prompt_has_clear_task
    - prompt_has_context_boundary
    - prompt_has_expected_output_contract
    - prompt_has_validation_criteria
    - prompt_has_stop_condition_or_completion_gate
    - prompt_has_provider_or_surface_rationale_when_provider_known
    - prompt_has_failure_hints
    - prompt_has_learning_hints
    - prompt_body_is_clean_copy_paste_ready
    - prompt_does_not_include_source_document_names_unless_requested
    - prompt_does_not_require_machine_readable_capture_block

  result_mapping:
    passed:
      PreCapNextDay_action: "Include prompt normally in flow_prompt_pack."
      validation_status: valid
    passed_with_warnings:
      PreCapNextDay_action: "Include prompt and add operator_review_flags."
      validation_status: valid_with_warnings
    operator_review_recommended:
      PreCapNextDay_action: "Include prompt but surface review flag in next_day_plan."
      validation_status: operator_review_recommended
    failed:
      PreCapNextDay_action: "Regenerate if possible; otherwise block that prompt packet only."
      validation_status: blocked_by_missing_operator_decision
    not_checked_degraded_mode:
      PreCapNextDay_action: "Include prompt only as low-confidence bootstrap output."
      validation_status: low_confidence_auto_generated
```

## Flow Prompt Pack Integration Rules

```yaml
flow_prompt_pack_integration_rules:
  insertion_target: flow_prompt_pack.prompt_execution_packets

  for_each_prompt_execution_packet:
    must_include_from_prompt_engineering:
      - prompt_task_type
      - expected_output_contract_ref_or_summary
      - provider_target
      - provider_rationale
      - prompt_design_rationale
      - final_copy_paste_prompt
      - prompt_failure_hints
      - prompt_learning_hints
      - validation_status

    may_include_from_prompt_engineering:
      - prompt_sequence_ref
      - follow_up_prompt_refs
      - light_capture_hints
      - quality_warnings
      - prior_feedback_reference

  PreCapNextDay_adds:
    - flow_id
    - sprint_id
    - daily_plan_context
    - flow_packet_reference
    - routing_decision_reference
    - workflow_validation_reference
    - FlowRecap_handoff_reference

  duplication_policy:
    prompt_packet_schema: "reference_only"
    prompt_body: "embed_or_reference_as_needed_for_operator_use"
    provider_style_contract: "reference_only"
    prompt_quality_rules: "summarize_result_only"
```

## Prompt Learning Handoff

```yaml
prompt_learning_handoff:
  purpose: >
    Carry prompt feedback requirements from PreCapNextDay into FlowRecap so
    later prompt-engineering improvements are grounded in actual execution.

  fields_to_carry_into_FlowRecap_handoff:
    - prompt_packet_id
    - provider_target
    - prompt_task_type
    - expected_output_type
    - prompt_learning_hints_summary
    - failure_hints_to_watch
    - operator_should_note_prompt_result_quality
    - actual_model_or_surface_used_if_known

  capture_policy:
    mandatory_machine_readable_block_inside_prompt: false
    canonical_capture_location: raw_flow_dump_and_FlowRecap
    light_capture_hints_allowed: true
```

## Conflict Handling

```yaml
prompt_engineering_conflict_handling:
  conflict_types:
    workflow_prompt_mismatch:
      trigger: "Prompt-engineering recommendation conflicts with workflow-process validation."
      resolution_order:
        1: operator_decision_from_tradeoff_card
        2: workflow_process_fit
        3: prompt_quality
        4: ai_routing_cost_or_efficiency
      PreCapNextDay_action: "Surface tradeoff and use operator review if not safely resolvable."

    routing_prompt_mismatch:
      trigger: "Provider style recommendation conflicts with AI routing recommendation."
      resolution_order:
        1: operator_decision_from_tradeoff_card
        2: workflow_process_fit
        3: prompt_quality
        4: ai_routing_cost_or_efficiency
      PreCapNextDay_action: "Prefer quality for planned flow sessions unless operator chooses cost efficiency."

    missing_prompt_engineering_dependency:
      trigger: "Prompt-engineering package or required reference is unavailable."
      resolution_order:
        1: use_partial_mode_if_safe
        2: use_degraded_generic_prompt_mode_if_daily_plan_should_continue
        3: block_only_prompt_pack_if_operator_requires_full_compliance
      PreCapNextDay_action: "Do not block the entire daily plan unless required by operator."

    prompt_quality_failure:
      trigger: "Prompt quality gate fails for a prompt packet."
      resolution_order:
        1: regenerate_prompt_packet
        2: downgrade_to_operator_review_recommended
        3: omit_prompt_with_reason_if_still_invalid
      PreCapNextDay_action: "Keep flow packet valid and mark prompt pack issue explicitly."
```

## Minimal Examples

### Example 1 - Full Prompt Engineering Available

```yaml
example_full_prompt_engineering_available:
  prompt_engineering_availability:
    availability_status: available_full
    dependency_confidence: high
    loaded_reference_files:
      - prompt-packet-contract.md
      - prompt-task-taxonomy.md
      - iteration-loop-patterns.md
      - provider-style-contract-claude.md
      - prompt-quality-validation.md
      - prompt-learning-feedback-contract.md
    validation_status: valid

  prompt_engineering_dependency_input:
    flow_id: F3
    sprint_id: S1
    project_or_domain: Apex
    sprint_goal: "Create one Claude-native skill reference contract."
    expected_output_type: reference_contract
    workflow_stage: artifact_creation
    process_stage: file_generation
    prompt_task_type_request: file_generation
    iteration_loop_hint: extract_normalize_validate
    provider_target_or_surface_hint: Claude
    prompt_constraints:
      - "Create exactly one file."
      - "Use YAML with 2-space indentation."
      - "Do not include source citations inside final file content."
    validation_status: valid

  prompt_engineering_dependency_output:
    prompt_compilation_status: compiled_with_full_prompt_engineering
    prompt_packet_refs:
      - prompt_packet_f3_s1_skill_reference_contract
    provider_style_contract_used: Claude
    prompt_quality_summary:
      quality_gate_status: passed
      key_warnings: []
    prompt_design_rationale_summary: "Structured as a Claude file-generation prompt with explicit schema ownership boundaries."
    prompt_failure_hints_summary:
      - "Check that only one file is produced."
      - "Check that schema ownership is not duplicated."
    prompt_learning_hints_summary:
      - "During FlowRecap, note whether the generated file needed schema-boundary corrections."
    validation_status: valid
```

### Example 2 - Prompt Engineering Missing, Bootstrap Mode

```yaml
example_missing_prompt_engineering_bootstrap:
  prompt_engineering_availability:
    availability_status: missing_degraded_mode
    dependency_confidence: low
    loaded_reference_files: []
    missing_reference_files:
      - prompt-packet-contract.md
      - prompt-task-taxonomy.md
      - provider-style-contract-chatgpt.md
      - prompt-quality-validation.md
    degraded_mode_reason: "Prompt-engineering package has not been installed or loaded yet."
    operator_review_flags:
      - prompt_engineering_dependency_missing
      - provider_optimization_not_available
    validation_status: low_confidence_auto_generated

  degraded_generic_prompt_mode_result:
    prompt_compilation_status: compiled_in_degraded_generic_prompt_mode
    provider_style_contract_used: none_degraded_generic
    prompt_quality_summary:
      quality_gate_status: not_checked_degraded_mode
      key_warnings:
        - "Prompt is generic and not provider-optimized."
        - "Prompt-packet contract compliance is not guaranteed."
    validation_status: low_confidence_auto_generated
```

### Example 3 - Routing and Prompt Recommendation Conflict

```yaml
example_routing_prompt_conflict:
  conflict:
    type: routing_prompt_mismatch
    prompt_engineering_recommendation: Claude
    ai_routing_recommendation: supplemental_api_low_cost
    reason: "Prompt quality indicates complex file-generation work, while routing optimized for cost."
    resolution_order:
      - operator_decision_from_tradeoff_card
      - workflow_process_fit
      - prompt_quality
      - ai_routing_cost_or_efficiency
    PreCapNextDay_recommended_action: "Use Claude or another frontier subscription surface for the planned flow session unless operator chooses cost-saving mode."
    validation_status: operator_review_recommended
```

---

# VALIDATION - FILE-SPECIFIC CHECKS

- [ ] Exactly one file was produced.
- [ ] Target path is `.claude/skills/precap-next-day/references/prompt-engineering-dependency-contract.md`.
- [ ] File owns only the PreCapNextDay to prompt-engineering dependency interface.
- [ ] File does not redefine `prompt_packet`, `prompt_sequence`, or `final_copy_paste_prompt` schemas.
- [ ] File does not redefine provider-specific prompting rules.
- [ ] File defines full, partial, and degraded prompt-engineering modes.
- [ ] File includes prompt quality gate integration.
- [ ] File includes prompt learning handoff into FlowRecap.
- [ ] YAML uses 2-space indentation.
- [ ] No current pricing, product-limit, benchmark, or model-ranking claims are made.

---

# NEXT PROMPT

Paste this next:
> Prompt PND7:
> Create exactly one file.
>
> # FILE: .claude/skills/precap-next-day/references/usage-tracking-dependency-contract.md
>
> File type: reference_contract.
> Schema ownership: owns the PreCapNextDay dependency interface for ai-routing-and-usage-tracking outputs.
> Context carry-forward:
> - .claude/skills/precap-next-day/SKILL.md
> - .claude/skills/precap-next-day/references/flow-prompt-pack-contract.md
> - .claude/skills/precap-next-day/references/prompt-engineering-dependency-contract.md
> - .claude/skills/ai-routing-and-usage-tracking/SKILL.md
> - all ai-routing-and-usage-tracking reference contracts
>
> This file must define:
> - usage tracking dependency interface
> - how PreCapNextDay consumes AI_surface_inventory
> - how PreCapNextDay consumes monthly_quota_map
> - how PreCapNextDay consumes routing_recommendation_packet
> - how planned_usage_budget enters next_day_plan and flow_prompt_pack
> - how FlowRecap later returns usage_delta
> - degraded behavior when usage data is missing
> - examples
>
> Rules:
> - Do not redefine AI_surface_inventory schema.
> - Do not redefine monthly_quota_map schema.
> - Do not redefine routing_decision schema.
> - Do not redefine planned_usage_budget schema.
> - Do not redefine usage_delta schema.
> - Do not invent exact quotas, prices, availability, or model rankings.
> - Use YAML with 2-space indentation.
>
> Next prompt target: Prompt PND8.
