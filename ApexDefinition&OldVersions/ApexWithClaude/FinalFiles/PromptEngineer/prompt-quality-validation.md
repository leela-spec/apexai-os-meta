# Prompt Quality Validation

```yaml
prompt_quality_validation:
  artifact_name: prompt_quality_validation
  file_role: prompt_engineering_reference_validation_rules
  purpose: >
    Define prompt-quality scoring, validation status assignment, defect classes,
    repair rules, review output shape, and minimal examples for validating
    prompt packets and final copy-paste prompts. This file validates prompt
    quality but does not define provider-specific style, routing decisions,
    prompt_packet schema, workflow/process taxonomies, or daily planning logic.

  ownership:
    owns:
      - prompt_quality_review
      - prompt_quality_score
      - prompt_quality_dimensions
      - prompt_defect_taxonomy
      - prompt_validation_gates
      - validation_status_assignment
      - prompt_repair_rules
      - prompt_quality_examples
    must_not_own:
      - provider_specific_prompting_style
      - routing_decision_schema
      - prompt_packet_schema
      - workflow_stage_taxonomy
      - process_stage_taxonomy
      - daily_plan_schema
      - FlowRecap_output_schema
      - project_status_merge_schema

  validation_policy:
    validate_clean_copy_paste_prompt_body: true
    validate_metadata_is_outside_prompt_body: true
    validate_one_primary_prompt_system: true
    validate_expected_output_contract: true
    validate_stop_condition: true
    validate_provider_fit_when_provider_target_is_supplied: true
    validate_workflow_alignment_when_workflow_labels_are_supplied: true
    require_machine_readable_capture_block_inside_every_prompt: false
```

## Schema: prompt_quality_review

```yaml
prompt_quality_review:
  type: object
  required:
    - review_id
    - reviewed_artifact
    - dimension_scores
    - total_score
    - quality_grade
    - validation_status
    - defects
    - repair_actions

  fields:
    review_id:
      type: string
      format: "prompt_quality_review_<short_slug>"
      required: true

    reviewed_artifact:
      type: object
      required: true
      fields:
        artifact_type:
          type: string
          allowed:
            - prompt_packet
            - prompt_sequence
            - final_copy_paste_prompt
            - start_prompt
            - follow_up_prompt
          required: true
        artifact_id:
          type: string
          required: false
        provider_target:
          type: string
          allowed:
            - ChatGPT
            - Claude
            - Gemini
            - OpenRouter_later
            - provider_unspecified
          required: false
        prompt_task_type:
          type: string
          required: false
        expected_output_type:
          type: string
          required: false

    dimension_scores:
      type: object_ref
      ref: prompt_quality_score
      required: true

    total_score:
      type: integer
      min: 10
      max: 50
      required: true

    quality_grade:
      type: string
      allowed:
        - excellent
        - good
        - usable_with_warnings
        - weak
        - blocked
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

    defects:
      type: object
      required: true
      fields:
        critical:
          type: list
          item_type: string
          min_items: 0
          max_items: 8
          required: true
        warnings:
          type: list
          item_type: string
          min_items: 0
          max_items: 10
          required: true

    repair_actions:
      type: list
      item_type: string
      min_items: 0
      max_items: 10
      required: true

    operator_review_flags:
      type: list
      item_type: string
      min_items: 0
      max_items: 10
      required: false
```

## Schema: prompt_quality_score

```yaml
prompt_quality_score:
  type: object
  required:
    - task_clarity
    - context_fit
    - output_contract_strength
    - constraint_strength
    - provider_fit
    - workflow_alignment
    - iteration_logic
    - validation_strength
    - boundary_control
    - operator_usability

  score_scale:
    type: integer
    min: 1
    max: 5
    meaning:
      1: unusable_or_missing
      2: weak_or_ambiguous
      3: usable_but_needs_review
      4: strong
      5: excellent

  fields:
    task_clarity:
      type: integer
      min: 1
      max: 5
      definition: "The prompt clearly states what the model must do."

    context_fit:
      type: integer
      min: 1
      max: 5
      definition: "The prompt gives enough relevant context without flooding the model."

    output_contract_strength:
      type: integer
      min: 1
      max: 5
      definition: "The requested output shape, sections, fields, and success criteria are explicit."

    constraint_strength:
      type: integer
      min: 1
      max: 5
      definition: "The prompt states boundaries, exclusions, assumptions, and forbidden behavior clearly."

    provider_fit:
      type: integer
      min: 1
      max: 5
      definition: "The prompt matches the selected provider or remains safely provider-neutral."

    workflow_alignment:
      type: integer
      min: 1
      max: 5
      definition: "The prompt matches the supplied workflow_stage, process_stage, sprint_goal, and expected_output_type."

    iteration_logic:
      type: integer
      min: 1
      max: 5
      definition: "The prompt has a suitable start/follow-up pattern, revision loop, or stop condition."

    validation_strength:
      type: integer
      min: 1
      max: 5
      definition: "The prompt tells the model how to check correctness before finishing."

    boundary_control:
      type: integer
      min: 1
      max: 5
      definition: "The prompt prevents scope creep, unrequested alternatives, unsupported claims, and unsafe execution."

    operator_usability:
      type: integer
      min: 1
      max: 5
      definition: "The prompt is copy-paste ready, concise enough to use, and easy for the operator to inspect."
```

## Quality Grade Rules

```yaml
quality_grade_rules:
  excellent:
    total_score:
      type: integer_range
      min: 45
      max: 50
    required_condition: "No critical defects."
    validation_status: valid

  good:
    total_score:
      type: integer_range
      min: 38
      max: 44
    required_condition: "No critical defects and only minor warnings."
    validation_status: valid_with_warnings

  usable_with_warnings:
    total_score:
      type: integer_range
      min: 30
      max: 37
    required_condition: "No blocking defect, but operator should review before high-value use."
    validation_status: operator_review_recommended

  weak:
    total_score:
      type: integer_range
      min: 20
      max: 29
    required_condition: "Prompt can be repaired but should not be used as final."
    validation_status: operator_review_recommended

  blocked:
    total_score:
      type: integer_range
      min: 10
      max: 19
    required_condition: "One or more critical defects make the prompt unsafe, unusable, or impossible to validate."
    validation_status: blocked_by_missing_operator_decision
```

## Prompt Validation Gates

```yaml
prompt_validation_gates:
  gates:
    task_gate:
      check: "The prompt names the task in direct operational language."
      fail_if:
        - no_explicit_task
        - task_conflicts_with_expected_output
        - task_requires_unavailable_context

    context_gate:
      check: "The prompt separates supplied context, assumptions, allowed research, and missing information."
      fail_if:
        - source_context_boundary_unclear
        - unsupported_outside_claims_allowed
        - missing_context_not_flagged

    output_contract_gate:
      check: "The prompt states the required output shape, sections, fields, or file format."
      fail_if:
        - output_shape_missing
        - multiple_conflicting_output_shapes
        - final_deliverable_not_named

    provider_gate:
      check: "The prompt matches provider_target or stays provider-neutral when target is missing."
      fail_if:
        - provider_specific_rules_conflict
        - volatile_provider_claims_unverified
        - exact_model_ranking_claimed_without_verification

    workflow_gate:
      check: "The prompt matches workflow_stage, process_stage, sprint_goal, and expected_output_type when supplied."
      fail_if:
        - workflow_stage_conflict
        - process_stage_conflict
        - expected_output_type_conflict

    iteration_gate:
      check: "The prompt includes suitable iteration behavior and a stop condition."
      fail_if:
        - no_stop_condition
        - endless_revision_loop
        - follow_up_prompt_has_unclear_delta

    boundary_gate:
      check: "The prompt prevents scope creep and respects package boundaries."
      fail_if:
        - creates_daily_plan_when_prompt_only_needed
        - executes_project_work
        - runs_FlowRecap
        - merges_project_status
        - creates_multiple_parallel_prompt_systems_by_default

    copy_paste_gate:
      check: "The final prompt body is clean and directly usable."
      fail_if:
        - metadata_inside_prompt_body
        - mandatory_machine_readable_capture_block_required
        - source_document_names_inside_prompt_body
        - commentary_mixed_with_prompt_body
```

## Defect Taxonomy

```yaml
prompt_defect_taxonomy:
  critical_defects:
    missing_task:
      trigger: "The prompt does not state a concrete task."
      correction: "Add one direct task statement near the top of the prompt."

    missing_output_contract:
      trigger: "The prompt does not define what the model must return."
      correction: "Add exact headings, fields, table columns, file format, or artifact structure."

    conflicting_output_contract:
      trigger: "The prompt asks for incompatible output shapes."
      correction: "Choose one primary output shape and move secondary needs into optional notes."

    missing_required_context:
      trigger: "The prompt requires context that is absent and cannot be inferred."
      correction: "Add a placeholder, ask for the input, or mark validation_status as blocked_by_missing_operator_decision."

    unbounded_agentic_scope:
      trigger: "The prompt allows broad autonomous action without allowed actions, forbidden actions, or stop conditions."
      correction: "Add allowed actions, forbidden actions, checkpoints, and a stop condition."

    provider_claim_drift:
      trigger: "The prompt asserts current model rankings, pricing, limits, or availability without verification."
      correction: "Remove exact volatile claims or require current verification."

    package_boundary_violation:
      trigger: "The prompt asks prompt-engineering to create daily plans, execute project work, run FlowRecap, or merge project status."
      correction: "Remove the forbidden task and route it to the owning skill or operator decision."

    copy_paste_body_contaminated:
      trigger: "The final prompt body contains metadata, source names, citations, or mandatory capture blocks not needed for use."
      correction: "Move metadata outside the prompt body and keep the copy-paste prompt clean."

  warning_defects:
    weak_role:
      trigger: "The role is vague or decorative rather than functional."
      correction: "Replace with a role that describes the exact work mode."

    weak_context_boundary:
      trigger: "The prompt does not clearly separate supplied context from assumptions."
      correction: "Add context boundary and uncertainty instructions."

    weak_validation:
      trigger: "The prompt lacks a self-check or validation method."
      correction: "Add a short validation section tied to the output contract."

    weak_stop_condition:
      trigger: "The prompt does not say when to stop."
      correction: "Add one explicit stop condition."

    variant_sprawl:
      trigger: "The prompt asks for many variants without a selection rule."
      correction: "Ask for one selected primary output and concise fallback notes only."

    overlong_prompt:
      trigger: "The prompt includes redundant instructions or unnecessary background."
      correction: "Compress context and keep only instructions that affect execution."

    underspecified_provider_fit:
      trigger: "Provider adaptation matters but provider_target is missing or unclear."
      correction: "Use provider_unspecified or request routing guidance."

    weak_learning_hints:
      trigger: "The prompt lacks useful failure or learning hints for later refinement."
      correction: "Add concise prompt_failure_hints and prompt_learning_hints outside the prompt body."
```

## Repair Rules

```yaml
prompt_repair_rules:
  repair_order:
    1: remove_package_boundary_violations
    2: resolve_missing_or_conflicting_task
    3: resolve_missing_or_conflicting_output_contract
    4: clarify_context_boundary
    5: repair_provider_fit
    6: repair_workflow_alignment
    7: add_validation_criteria
    8: add_stop_condition
    9: clean_copy_paste_prompt_body
    10: add_failure_and_learning_hints

  repair_policy:
    preserve_operator_intent: true
    preserve_one_primary_prompt_system: true
    prefer_surgical_repair_over_total_rewrite: true
    do_not_add_new_goals_without_flagging: true
    do_not_hide_low_confidence_inference: true
    operator_review_required_when:
      - task_goal_is_unclear
      - workflow_and_prompt_conflict
      - provider_or_routing_conflict
      - output_contract_tradeoff_exists
      - missing_context_blocks_validation

  status_after_repair:
    critical_defects_removed:
      assign: valid_with_warnings
      unless: "All scores are at least 4 and no warnings remain."
    critical_defects_remain:
      assign: blocked_by_missing_operator_decision
    only_minor_warnings_remain:
      assign: valid_with_warnings
    no_defects_remain:
      assign: valid
```

## Minimal Examples

### Valid prompt quality review

```yaml
example_valid_prompt_quality_review:
  prompt_quality_review:
    review_id: prompt_quality_review_skill_file_generation
    reviewed_artifact:
      artifact_type: final_copy_paste_prompt
      artifact_id: final_copy_paste_prompt_skill_file
      provider_target: Claude
      prompt_task_type: file_generation
      expected_output_type: markdown_document
    dimension_scores:
      task_clarity: 5
      context_fit: 4
      output_contract_strength: 5
      constraint_strength: 5
      provider_fit: 4
      workflow_alignment: 5
      iteration_logic: 4
      validation_strength: 5
      boundary_control: 5
      operator_usability: 5
    total_score: 47
    quality_grade: excellent
    validation_status: valid
    defects:
      critical: []
      warnings: []
    repair_actions: []
    operator_review_flags: []
```

### Repairable prompt review

```yaml
example_repairable_prompt_quality_review:
  prompt_quality_review:
    review_id: prompt_quality_review_weak_research_prompt
    reviewed_artifact:
      artifact_type: final_copy_paste_prompt
      provider_target: ChatGPT
      prompt_task_type: research
      expected_output_type: research_summary
    dimension_scores:
      task_clarity: 4
      context_fit: 3
      output_contract_strength: 2
      constraint_strength: 3
      provider_fit: 4
      workflow_alignment: 3
      iteration_logic: 2
      validation_strength: 2
      boundary_control: 3
      operator_usability: 3
    total_score: 29
    quality_grade: weak
    validation_status: operator_review_recommended
    defects:
      critical: []
      warnings:
        - weak_validation
        - weak_stop_condition
        - weak_context_boundary
    repair_actions:
      - "Add required output headings."
      - "Add source-quality and uncertainty rules."
      - "Add stop condition after evidence gaps are listed."
    operator_review_flags:
      - missing_source_quality_preference
```

### Blocked prompt review

```yaml
example_blocked_prompt_quality_review:
  prompt_quality_review:
    review_id: prompt_quality_review_blocked_agentic_scope
    reviewed_artifact:
      artifact_type: final_copy_paste_prompt
      provider_target: provider_unspecified
      prompt_task_type: planning
      expected_output_type: implementation_plan
    dimension_scores:
      task_clarity: 2
      context_fit: 2
      output_contract_strength: 1
      constraint_strength: 1
      provider_fit: 2
      workflow_alignment: 2
      iteration_logic: 1
      validation_strength: 1
      boundary_control: 1
      operator_usability: 2
    total_score: 15
    quality_grade: blocked
    validation_status: blocked_by_missing_operator_decision
    defects:
      critical:
        - missing_output_contract
        - unbounded_agentic_scope
      warnings:
        - weak_context_boundary
        - weak_stop_condition
    repair_actions:
      - "Define the exact deliverable before execution."
      - "Add allowed actions, forbidden actions, and stop condition."
      - "Ask operator to approve scope before use."
    operator_review_flags:
      - missing_output_contract
      - unbounded_scope
```
