# FILE: .claude/skills/workflow-process-design/references/expected-output-type-contract.md

````markdown id="wpd4eot"
# Expected Output Type Contract

```yaml
expected_output_type_contract:
  artifact_name: expected_output_type_contract
  file_role: workflow_process_design_reference_contract
  purpose: >
    Define the expected output type taxonomy and assignment schema used by
    workflow-process-design to make operator deliverables explicit before
    prompt generation, routing, sprint design, or workflow validation. This
    file describes the shape, completeness, fidelity, and validation needs of
    intended outputs. It does not define prompt packets, AI routing, usage,
    quota, daily plan, flow packet, project status, workflow stage, or process
    stage schemas.

  ownership:
    owns:
      - expected_output_type_taxonomy
      - expected_output_assignment
      - output_family_tags
      - output_completeness_fields
      - output_fidelity_fields
      - expected_output_validation_fields
      - workflow_process_fit_hints
      - expected_output_examples
    must_not_own:
      - prompt_packet_schema
      - prompt_sequence_schema
      - provider_specific_prompt_rules
      - routing_decision_schema
      - planned_usage_budget_schema
      - usage_delta_schema
      - monthly_quota_map_schema
      - AI_surface_inventory_schema
      - workflow_stage_taxonomy
      - process_stage_taxonomy
      - daily_plan_schema
      - flow_packet_schema
      - project_status_schema
      - workflow_record_schema

  global_rules:
    expected_output_type_is_deliverable_shape_not_task_action: true
    define_output_before_prompt_generation: true
    preserve_operator_intent_over_generic_format: true
    mark_inferred_output_types_for_review: true
    do_not_invent_source_content_when_fidelity_required: true
    use_validation_status_allowed_values: true

  validation_status_allowed:
    - valid
    - valid_with_warnings
    - operator_review_recommended
    - low_confidence_auto_generated
    - blocked_by_missing_operator_decision
```

## Schema: expected_output_type_taxonomy

```yaml
expected_output_type_taxonomy:
  type: object
  role: canonical_expected_output_type_set
  note: >
    An expected_output_type describes what the operator should receive or use.
    It is separate from workflow_stage, process_stage, prompt_task_type,
    provider_target, routing_decision, and daily planning objects.

  allowed:
    plan:
      definition: "An ordered action structure with goals, phases, dependencies, and next steps."
      output_family_tags:
        - planning_artifact
        - operator_control_artifact
      use_when:
        - sequencing_is_needed
        - dependencies_or_priorities_matter
        - operator_needs_executable_structure
      avoid_when:
        - operator_needs_decision_not_sequence
        - material_should_only_be_summarized
        - task_would_become_daily_plan_or_flow_packet_schema
      likely_workflow_stages:
        - planning
        - operator_decision
      likely_process_stages:
        - strategy
        - planning
      minimum_completion_evidence:
        - goal_or_target_state_named
        - ordered_steps_or_phases_present
        - dependencies_or_constraints_identified
        - next_action_explicit

    decision_brief:
      definition: "A compact recommendation or decision support artifact with criteria and rationale."
      output_family_tags:
        - decision_artifact
        - operator_control_artifact
      use_when:
        - operator_must_choose_between_options
        - tradeoffs_are_material
        - decision_context_requires_rationale
      avoid_when:
        - no_real_options_exist
        - source_context_is_too_thin_for_recommendation
        - operator_requested_only_raw_options
      likely_workflow_stages:
        - operator_decision
        - synthesis
      likely_process_stages:
        - strategy
        - validation
      minimum_completion_evidence:
        - decision_question_stated
        - options_listed
        - criteria_named
        - recommendation_or_review_flag_present

    tradeoff_card:
      definition: "A structured comparison of options, costs, benefits, risks, and open decisions."
      output_family_tags:
        - decision_artifact
        - validation_artifact
      use_when:
        - skill_databases_disagree
        - operator_choice_is_required
        - no_single_safe_auto_decision_exists
      avoid_when:
        - decision_is_already_locked
        - output_should_be_a_final_file
        - only_one_compliant_option_exists
      likely_workflow_stages:
        - operator_decision
        - validation
      likely_process_stages:
        - operator_review
        - validation
      minimum_completion_evidence:
        - conflicting_options_named
        - primary_tradeoffs_identified
        - authority_order_applied
        - operator_decision_request_present

    research_digest:
      definition: "A sourced or source-grounded information digest that supports later synthesis or decision."
      output_family_tags:
        - research_artifact
        - synthesis_artifact
      use_when:
        - information_collection_or_verification_is_primary
        - evidence_needs_to_be_preserved
        - later_decision_depends_on_findings
      avoid_when:
        - current_research_is_not_needed
        - operator_supplied_sources_are_already_complete
        - output_requires_final_prompt_body_only
      likely_workflow_stages:
        - exploration
        - synthesis
      likely_process_stages:
        - research
        - context_intake
      minimum_completion_evidence:
        - research_question_or_scope_present
        - findings_grouped
        - uncertainty_or_source_gaps_marked
        - downstream_use_named

    synthesis_summary:
      definition: "An integrated summary that compresses multiple inputs into coherent meaning."
      output_family_tags:
        - synthesis_artifact
      use_when:
        - multiple_inputs_need_consolidation
        - source_material_is_available
        - operator_needs_meaning_not_raw_excerpts
      avoid_when:
        - source_material_missing
        - high_source_fidelity_requires_extract_only_behavior
        - operator_needs_action_plan
      likely_workflow_stages:
        - synthesis
        - recap_preparation
      likely_process_stages:
        - synthesis
        - recap
      minimum_completion_evidence:
        - source_threads_merged
        - core_points_preserved
        - contradictions_or_gaps_flagged
        - no_unmarked_invention

    critique_report:
      definition: "A defect-focused evaluation of an existing artifact against explicit or inferred criteria."
      output_family_tags:
        - validation_artifact
      use_when:
        - existing_artifact_needs_review
        - quality_gate_is_needed
        - operator_wants_defects_and_fixes
      avoid_when:
        - no_artifact_exists_to_review
        - operator_requests_generation_from_scratch
        - review_criteria_are_unknown_and_uninferable
      likely_workflow_stages:
        - validation
      likely_process_stages:
        - validation
        - operator_review
      minimum_completion_evidence:
        - reviewed_artifact_named
        - criteria_or_contract_named
        - defects_prioritized
        - recommended_corrections_present

    validation_report:
      definition: "A pass, fail, warning, or compliance report against a known contract or checklist."
      output_family_tags:
        - validation_artifact
      use_when:
        - contract_compliance_matters
        - final_gate_before_use
        - machine_readability_or_boundary_validation_needed
      avoid_when:
        - no_contract_or_rules_exist
        - operator_needs_rewrite_not_validation
        - validation_would_duplicate_existing_completion_gate
      likely_workflow_stages:
        - validation
      likely_process_stages:
        - validation
        - packaging
      minimum_completion_evidence:
        - validation_scope_named
        - checklist_or_rules_applied
        - status_assigned
        - blocking_issues_separated_from_warnings

    workflow_record:
      definition: "A reusable record of workflow structure, labels, inputs, outputs, gates, risks, and downstream consumers."
      output_family_tags:
        - workflow_artifact
        - process_artifact
      use_when:
        - workflow_should_be_preserved
        - repeated_process_is_being_normalized
        - process_design_needs_durable_reference
      avoid_when:
        - one_off_output_only_requested
        - workflow_is_not_reusable
        - workflow_record_schema_should_be_defined_elsewhere
      likely_workflow_stages:
        - extraction
        - normalization
      likely_process_stages:
        - extraction
        - normalization
        - packaging
      minimum_completion_evidence:
        - workflow_name_or_scope_present
        - inputs_outputs_gates_identified
        - workflow_and_process_labels_present
        - downstream_consumer_named

    process_map:
      definition: "A structured map of stages, transitions, gates, dependencies, and failure points."
      output_family_tags:
        - process_artifact
        - workflow_artifact
      use_when:
        - process_sequence_must_be_understood
        - stage_boundaries_or_handoffs_are_unclear
        - operator_needs_operational_model
      avoid_when:
        - only_final_file_content_is_requested
        - task_is_provider_prompt_adaptation
        - map_would_duplicate_daily_plan_or_flow_packet_schema
      likely_workflow_stages:
        - extraction
        - normalization
        - planning
      likely_process_stages:
        - extraction
        - normalization
        - planning
      minimum_completion_evidence:
        - stages_listed
        - transitions_named
        - gates_or_review_points_identified
        - failure_or_ambiguity_points_flagged

    prompt_pack_input:
      definition: "A workflow/process-ready input block for prompt-engineering or PreCapNextDay prompt pack compilation."
      output_family_tags:
        - prompt_support_artifact
        - workflow_artifact
      use_when:
        - prompt_needs_workflow_labels
        - expected_output_type_must_be_handed_to_prompt_engineering
        - prompt_process_alignment_is_primary
      avoid_when:
        - final_prompt_body_is_requested_directly
        - provider_specific_prompt_rules_are_needed
        - routing_decision_is_primary
      likely_workflow_stages:
        - planning
        - validation
      likely_process_stages:
        - planning
        - prompt_preparation
      minimum_completion_evidence:
        - workflow_stage_present
        - process_stage_present
        - expected_output_type_present
        - success_criteria_present
        - prompt_boundary_notes_present

    implementation_spec:
      definition: "A concrete technical or operational specification for how something should be built or changed."
      output_family_tags:
        - implementation_artifact
      use_when:
        - implementation_requirements_are_known
        - file_or_system_behavior_needs_definition
        - downstream_executor_needs precise instructions
      avoid_when:
        - exact_target_is_missing
        - permission_boundary_unclear
        - task_is_strategy_or_discovery_only
      likely_workflow_stages:
        - planning
        - execution_support
      likely_process_stages:
        - implementation
        - planning
      minimum_completion_evidence:
        - target_named
        - required_behavior_defined
        - constraints_listed
        - validation_or_acceptance_criteria_present

    code_or_file_patch_plan:
      definition: "A bounded patch plan for code, config, or file edits without executing the patch."
      output_family_tags:
        - implementation_artifact
        - operator_control_artifact
      use_when:
        - operator_needs_patch_sequence
        - exact_files_or_edit_targets_are_known
        - risk_control_matters_before_execution
      avoid_when:
        - operator_requested_actual_execution
        - no_target_path_or_file_scope_exists
        - patch_requires_external_permission
      likely_workflow_stages:
        - execution_support
        - validation
      likely_process_stages:
        - implementation
        - validation
      minimum_completion_evidence:
        - target_paths_or_slots_named
        - edit_sequence_present
        - risk_or_backup_notes_present
        - validation_steps_present

    content_draft:
      definition: "A human-facing draft such as copy, article, page section, message, script, or concept text."
      output_family_tags:
        - content_artifact
      use_when:
        - operator_needs_reusable_written_content
        - tone_or_audience_matters
        - deliverable_is_text_for_humans
      avoid_when:
        - source_fidelity_requires_no_rewriting
        - task_is_contract_schema_generation
        - output_should_be_only_a_validation_report
      likely_workflow_stages:
        - execution_support
        - synthesis
      likely_process_stages:
        - generation
        - refinement
      minimum_completion_evidence:
        - audience_or_use_context_named
        - draft_body_present
        - tone_or_constraints_preserved
        - review_flags_for_uncertain_style_present

    visual_brief:
      definition: "A structured description for image, layout, spatial design, diagram, or visual artifact generation."
      output_family_tags:
        - visual_artifact
        - content_artifact
      use_when:
        - visual_output_or_layout_is_target
        - spatial_or_compositional_constraints_matter
        - downstream_visual_tool_or_designer_needs_brief
      avoid_when:
        - text_only_output_requested
        - image_generation_policy_or_tool_boundary_is_unclear
        - source_material_lacks_visual_constraints
      likely_workflow_stages:
        - exploration
        - execution_support
      likely_process_stages:
        - generation
        - planning
      minimum_completion_evidence:
        - visual_goal_named
        - composition_or_structure_defined
        - constraints_listed
        - output_use_context_present

    recap_material:
      definition: "Structured material prepared for later recap, status update, or learning capture."
      output_family_tags:
        - recap_artifact
        - learning_artifact
      use_when:
        - operator_has_completed_or_skipped_work
        - execution_evidence_needs_to_be_digested_later
        - FlowRecap_or_status_merge_requires_inputs
      avoid_when:
        - no_execution_or_work_session_occurred
        - task_requires_running_FlowRecap_now
        - project_status_merge_is_requested
      likely_workflow_stages:
        - recap_preparation
        - learning_update
      likely_process_stages:
        - recap
        - capture
      minimum_completion_evidence:
        - work_context_named
        - results_or_non_results_recorded
        - blockers_or_open_questions_flagged
        - next_recap_consumer_named

    learning_update:
      definition: "A compact update capturing what should change in future prompts, workflows, or validations."
      output_family_tags:
        - learning_artifact
      use_when:
        - prompt_or_workflow_failed
        - repeated_pattern_should_be_updated
        - feedback_should_influence_future skill behavior
      avoid_when:
        - feedback_is_too_thin
        - no reusable lesson exists
        - operator_requested_final_output_not_learning_capture
      likely_workflow_stages:
        - learning_update
        - validation
      likely_process_stages:
        - learning
        - validation
      minimum_completion_evidence:
        - trigger_or_failure_named
        - lesson_stated
        - future_change_recommended
        - owner_or_downstream_package_named

    operator_checklist:
      definition: "A compact list of actions or checks the operator can execute or approve manually."
      output_family_tags:
        - operator_control_artifact
      use_when:
        - operator_action_is_required
        - gate_or_manual_validation_must_be_made_explicit
        - human_execution_layer_needs_simple steps
      avoid_when:
        - checklist_would_replace_a_contract
        - output_requires_deep_synthesis
        - operator_approval_is_not_needed
      likely_workflow_stages:
        - operator_decision
        - execution_support
      likely_process_stages:
        - operator_review
        - validation
      minimum_completion_evidence:
        - checklist_items_present
        - completion_or_decision_condition_present
        - blocked_items_flagged
        - next_action_named

    artifact_index:
      definition: "A lightweight index of produced or referenced artifacts and their purpose."
      output_family_tags:
        - package_artifact
        - operator_control_artifact
      use_when:
        - files_or_outputs_need_traceable_listing
        - package_or_flow_outputs_need_navigation
        - downstream_user_needs_read_when_guidance
      avoid_when:
        - index_would_become_second_contract
        - too_few_artifacts_exist
        - detailed_schema_definitions_are_needed
      likely_workflow_stages:
        - packaging
        - recap_preparation
      likely_process_stages:
        - packaging
        - capture
      minimum_completion_evidence:
        - artifact_names_or_paths_present
        - purpose_present
        - read_when_or_consumer_hint_present
        - no_duplicated_schemas

    package_file:
      definition: "A final file intended to be copied into a skill package, reference folder, example folder, or manifest."
      output_family_tags:
        - package_artifact
      use_when:
        - exact_target_path_is_known
        - one_file_per_prompt_flow_is_active
        - output_must_be_final_not_outline
      avoid_when:
        - multiple_files_are_requested
        - target_path_or_file_role_is_missing
        - operator_requested_analysis_only
      likely_workflow_stages:
        - normalization
        - packaging
      likely_process_stages:
        - file_generation
        - packaging
      minimum_completion_evidence:
        - target_path_present
        - complete_file_content_present
        - validation_checklist_present_when_prompt_flow_requires
        - next_prompt_present_when_sequence_continues

    other_operator_defined:
      definition: "An operator-defined output type outside this taxonomy."
      output_family_tags:
        - operator_control_artifact
      use_when:
        - operator_names_custom_output_shape
        - standard_types_do_not_fit
        - preserving_operator_language_is_more_important_than_normalizing
      avoid_when:
        - standard_expected_output_type_is_clear
        - custom_label_hides_workflow_ambiguity
        - downstream_contract_requires_canonical_type
      likely_workflow_stages:
        - operator_decision
      likely_process_stages:
        - operator_review
      minimum_completion_evidence:
        - operator_label_preserved
        - nearest_canonical_type_suggested
        - ambiguity_flag_present
        - validation_status_noted
```

## Schema: expected_output_assignment

```yaml
expected_output_assignment:
  type: object
  required:
    - assignment_id
    - source_intent_summary
    - expected_output_type
    - output_family_tags
    - workflow_process_context
    - target_consumer
    - format_contract
    - completeness
    - fidelity
    - validation
    - validation_status

  fields:
    assignment_id:
      type: string
      format: "expected_output_assignment_<short_slug>"
      required: true

    source_intent_summary:
      type: string
      required: true
      max_words: 40

    expected_output_type:
      type: string
      allowed:
        - plan
        - decision_brief
        - tradeoff_card
        - research_digest
        - synthesis_summary
        - critique_report
        - validation_report
        - workflow_record
        - process_map
        - prompt_pack_input
        - implementation_spec
        - code_or_file_patch_plan
        - content_draft
        - visual_brief
        - recap_material
        - learning_update
        - operator_checklist
        - artifact_index
        - package_file
        - other_operator_defined
      required: true

    output_family_tags:
      type: list
      item_type: string
      allowed:
        - planning_artifact
        - decision_artifact
        - research_artifact
        - synthesis_artifact
        - validation_artifact
        - workflow_artifact
        - process_artifact
        - prompt_support_artifact
        - implementation_artifact
        - content_artifact
        - visual_artifact
        - recap_artifact
        - learning_artifact
        - package_artifact
        - operator_control_artifact
      min_items: 1
      max_items: 5
      required: true

    workflow_process_context:
      type: object
      required: true
      fields:
        workflow_stage:
          type: string
          required: false
          nullable: true
          note: "Reference only. Canonical taxonomy lives in workflow-stage-taxonomy.md."
        process_stage:
          type: string
          required: false
          nullable: true
          note: "Reference only. Canonical taxonomy lives in process-stage-taxonomy.md."
        sprint_id:
          type: string
          required: false
          nullable: true
        flow_id:
          type: string
          required: false
          nullable: true
        workflow_fit_notes:
          type: list
          item_type: string
          max_items: 8
          required: false

    target_consumer:
      type: object
      required: true
      fields:
        consumer_type:
          type: string
          allowed:
            - operator
            - prompt_engineering
            - ai_routing_and_usage_tracking
            - workflow_process_design
            - PreCapNextDay
            - FlowRecap
            - status_merge
            - downstream_executor
            - package_reader
            - unknown
          required: true
        consumer_need:
          type: string
          required: true
        handoff_notes:
          type: list
          item_type: string
          max_items: 8
          required: false

    format_contract:
      type: object
      required: true
      fields:
        primary_format:
          type: string
          allowed:
            - markdown
            - yaml
            - markdown_with_yaml_blocks
            - plain_text
            - table
            - checklist
            - code_or_config
            - visual_brief_text
            - operator_defined
          required: true
        required_sections:
          type: list
          item_type: string
          min_items: 0
          max_items: 20
          required: true
        forbidden_sections:
          type: list
          item_type: string
          min_items: 0
          max_items: 20
          required: false
        structure_notes:
          type: list
          item_type: string
          max_items: 12
          required: false

    completeness:
      type: object
      required: true
      fields:
        minimum_completion_evidence:
          type: list
          item_type: string
          min_items: 1
          max_items: 12
          required: true
        completeness_score:
          type: integer
          min: 1
          max: 100
          required: false
        missing_allowed:
          type: boolean
          required: true
        missing_items:
          type: list
          item_type: string
          required: false
        completion_status:
          type: string
          allowed:
            - complete
            - partial
            - low_confidence
            - blocked
          required: true

    fidelity:
      type: object
      required: true
      fields:
        source_fidelity_required:
          type: boolean
          required: true
        transformation_mode:
          type: string
          allowed:
            - extract_only
            - normalize
            - synthesize
            - generate_new
            - validate_only
            - operator_defined
          required: true
        invented_content_policy:
          type: string
          allowed:
            - forbidden
            - allowed_with_flags
            - allowed
            - operator_supplied_only
          required: true
        semantic_preservation_required:
          type: boolean
          required: true
        fidelity_risks:
          type: list
          item_type: string
          max_items: 10
          required: false
        fidelity_confidence:
          type: integer
          min: 1
          max: 100
          required: false

    validation:
      type: object
      required: true
      fields:
        success_criteria:
          type: list
          item_type: string
          min_items: 1
          max_items: 12
          required: true
        failure_conditions:
          type: list
          item_type: string
          min_items: 0
          max_items: 12
          required: false
        operator_review_required:
          type: boolean
          required: true
        operator_review_flags:
          type: list
          item_type: string
          required: false
        downstream_validation_needed:
          type: boolean
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

## Output Family Tags

```yaml
output_family_tags:
  role: cross_type_grouping_for_validation_and_handoff
  allowed:
    planning_artifact:
      definition: "Helps order or structure action."
      typical_types:
        - plan
        - process_map
        - prompt_pack_input

    decision_artifact:
      definition: "Supports or records operator choice."
      typical_types:
        - decision_brief
        - tradeoff_card

    research_artifact:
      definition: "Preserves findings or evidence."
      typical_types:
        - research_digest

    synthesis_artifact:
      definition: "Combines multiple inputs into coherent meaning."
      typical_types:
        - synthesis_summary
        - research_digest

    validation_artifact:
      definition: "Checks quality, compliance, fit, or correctness."
      typical_types:
        - critique_report
        - validation_report
        - tradeoff_card

    workflow_artifact:
      definition: "Describes reusable workflow structure or labels."
      typical_types:
        - workflow_record
        - process_map
        - prompt_pack_input

    process_artifact:
      definition: "Describes internal process stage, sequence, gates, or behavior."
      typical_types:
        - workflow_record
        - process_map

    prompt_support_artifact:
      definition: "Provides workflow/process context for prompt creation without defining the prompt body."
      typical_types:
        - prompt_pack_input

    implementation_artifact:
      definition: "Prepares build, patch, code, file, or operational execution."
      typical_types:
        - implementation_spec
        - code_or_file_patch_plan

    content_artifact:
      definition: "Human-facing drafted text or content concept."
      typical_types:
        - content_draft
        - visual_brief

    visual_artifact:
      definition: "Describes or supports visual, layout, spatial, or diagram output."
      typical_types:
        - visual_brief

    recap_artifact:
      definition: "Prepares completed work evidence for recap or status update."
      typical_types:
        - recap_material

    learning_artifact:
      definition: "Captures reusable lessons or future correction signals."
      typical_types:
        - learning_update
        - recap_material

    package_artifact:
      definition: "Belongs to final file package, manifest, or artifact index."
      typical_types:
        - package_file
        - artifact_index

    operator_control_artifact:
      definition: "Supports operator review, approval, action, or gating."
      typical_types:
        - operator_checklist
        - decision_brief
        - tradeoff_card
        - plan
```

## Completeness and Fidelity Rules

```yaml
completeness_and_fidelity_rules:
  completeness_policy:
    complete:
      use_when:
        - required_sections_present
        - minimum_completion_evidence_satisfied
        - no_blocking_unknowns
      validation_status_hint: valid

    partial:
      use_when:
        - output_is_useful_but_missing_non_blocking_context
        - missing_items_are_marked
        - operator_can_continue_with_warnings
      validation_status_hint: valid_with_warnings

    low_confidence:
      use_when:
        - expected_output_type_is_inferred
        - source_intent_is_ambiguous
        - success_criteria_are_partly_assumed
      validation_status_hint: low_confidence_auto_generated

    blocked:
      use_when:
        - operator_decision_needed
        - required_target_or_source_material_missing
        - safe_output_shape_cannot_be_selected
      validation_status_hint: blocked_by_missing_operator_decision

  fidelity_policy:
    extract_only:
      allowed_actions:
        - preserve_source_wording
        - label_structure
        - remove_format_noise
      forbidden_actions:
        - invent_missing_content
        - change_meaning
        - replace_operator_terms_without_note

    normalize:
      allowed_actions:
        - standardize_structure
        - rename_fields_to_canonical_keys
        - preserve_semantic_content
      forbidden_actions:
        - silently_drop_source_constraints
        - alter_operator_decisions

    synthesize:
      allowed_actions:
        - combine_multiple_sources
        - resolve_redundancy
        - make_inferences_with_flags
      forbidden_actions:
        - hide_uncertainty
        - present_inference_as_source_fact

    generate_new:
      allowed_actions:
        - create_new_draft_content
        - propose_missing_structure
        - fill_creative_or_planning_gaps
      forbidden_actions:
        - invent_source_evidence
        - ignore_operator_voice_or_constraints

    validate_only:
      allowed_actions:
        - check_against_contract
        - mark_pass_fail_warning
        - recommend_corrections
      forbidden_actions:
        - rewrite_full_artifact_unless_requested
        - change_target_output_type
```

## Workflow and Process Fit Hints

```yaml
workflow_process_fit_hints:
  selection_priority:
    1: explicit_operator_output_request
    2: downstream_consumer_requirement
    3: workflow_stage
    4: process_stage
    5: source_context_shape
    6: validation_or_fidelity_need

  workflow_stage_to_output_hint:
    intake:
      likely_expected_output_types:
        - operator_checklist
        - synthesis_summary
        - prompt_pack_input
      review_flags:
        - output_may_be_under_specified

    exploration:
      likely_expected_output_types:
        - research_digest
        - visual_brief
        - decision_brief
      review_flags:
        - evidence_need_may_be_high

    extraction:
      likely_expected_output_types:
        - process_map
        - workflow_record
        - synthesis_summary
      review_flags:
        - source_fidelity_required

    normalization:
      likely_expected_output_types:
        - package_file
        - workflow_record
        - process_map
      review_flags:
        - semantic_preservation_required

    planning:
      likely_expected_output_types:
        - plan
        - prompt_pack_input
        - implementation_spec
      review_flags:
        - dependencies_should_be_checked

    execution_support:
      likely_expected_output_types:
        - implementation_spec
        - code_or_file_patch_plan
        - content_draft
        - operator_checklist
      review_flags:
        - execution_boundary_must_be_clear

    validation:
      likely_expected_output_types:
        - validation_report
        - critique_report
        - tradeoff_card
      review_flags:
        - contract_or_criteria_required

    synthesis:
      likely_expected_output_types:
        - synthesis_summary
        - decision_brief
        - research_digest
      review_flags:
        - source_conflict_should_be_flagged

    recap_preparation:
      likely_expected_output_types:
        - recap_material
        - artifact_index
        - learning_update
      review_flags:
        - downstream_recap_consumer_should_be_named

    learning_update:
      likely_expected_output_types:
        - learning_update
        - critique_report
        - validation_report
      review_flags:
        - reusable_lesson_must_be_distinguished_from_one_off_feedback

    operator_decision:
      likely_expected_output_types:
        - tradeoff_card
        - decision_brief
        - operator_checklist
      review_flags:
        - operator_choice_required

  process_stage_to_output_hint:
    context_intake:
      likely_expected_output_types:
        - synthesis_summary
        - operator_checklist
    strategy:
      likely_expected_output_types:
        - decision_brief
        - plan
    planning:
      likely_expected_output_types:
        - plan
        - prompt_pack_input
    extraction:
      likely_expected_output_types:
        - process_map
        - workflow_record
    normalization:
      likely_expected_output_types:
        - package_file
        - workflow_record
    prompt_preparation:
      likely_expected_output_types:
        - prompt_pack_input
    generation:
      likely_expected_output_types:
        - content_draft
        - visual_brief
        - package_file
    refinement:
      likely_expected_output_types:
        - critique_report
        - content_draft
    validation:
      likely_expected_output_types:
        - validation_report
        - critique_report
    packaging:
      likely_expected_output_types:
        - package_file
        - artifact_index
    recap:
      likely_expected_output_types:
        - recap_material
        - synthesis_summary
    learning:
      likely_expected_output_types:
        - learning_update
    operator_review:
      likely_expected_output_types:
        - tradeoff_card
        - operator_checklist
    blocked_or_deferred:
      likely_expected_output_types:
        - operator_checklist
        - tradeoff_card
```

## Ambiguity and Review Rules

```yaml
expected_output_ambiguity_rules:
  ambiguity_flags:
    multiple_output_types_fit:
      trigger: "The source intent supports two or more expected_output_type labels."
      response: "Select the most downstream-useful type and list alternatives in operator_review_flags."

    output_shape_missing:
      trigger: "The operator asks for activity but not a deliverable."
      response: "Infer the safest expected_output_type and mark low_confidence_auto_generated."

    source_fidelity_unclear:
      trigger: "It is unclear whether content may be rewritten or only normalized."
      response: "Use normalize with invented_content_policy: forbidden until operator says otherwise."

    downstream_consumer_unknown:
      trigger: "The output is useful but its consumer is not named."
      response: "Set consumer_type: unknown and mark operator_review_recommended."

    workflow_prompt_conflict:
      trigger: "The expected output type implies a different job than the prompt or workflow stage."
      response: "Return a prompt_workflow_alignment warning instead of silently changing the output."

  operator_review_flag_examples:
    - expected_output_type_inferred
    - multiple_output_types_fit
    - output_format_under_specified
    - downstream_consumer_unknown
    - source_fidelity_policy_unclear
    - invented_content_risk
    - workflow_stage_output_mismatch
    - process_stage_output_mismatch
    - implementation_target_missing
    - decision_required_before_finalization
```

## Minimal Examples

```yaml
expected_output_examples:
  example_package_file:
    input_summary: "Operator asks to create one final skill reference file in a one-file-per-prompt flow."
    expected_output_assignment:
      assignment_id: expected_output_assignment_package_file
      source_intent_summary: "Create one final package reference file."
      expected_output_type: package_file
      output_family_tags:
        - package_artifact
      workflow_process_context:
        workflow_stage: normalization
        process_stage: file_generation
        workflow_fit_notes:
          - one_file_per_prompt_flow_active
          - target_path_known
      target_consumer:
        consumer_type: package_reader
        consumer_need: "Use file as final skill package reference."
      format_contract:
        primary_format: markdown_with_yaml_blocks
        required_sections:
          - file_header
          - contract_or_taxonomy_body
          - validation_checks
          - next_prompt
        forbidden_sections:
          - source_citations
          - old_decision_trace
      completeness:
        minimum_completion_evidence:
          - target_path_present
          - complete_file_content_present
          - validation_checklist_present
          - next_prompt_present
        completeness_score: 95
        missing_allowed: false
        completion_status: complete
      fidelity:
        source_fidelity_required: true
        transformation_mode: normalize
        invented_content_policy: allowed_with_flags
        semantic_preservation_required: true
        fidelity_confidence: 92
      validation:
        success_criteria:
          - one_file_only
          - schema_ownership_preserved
          - no_duplicate_foreign_schemas
        operator_review_required: false
      validation_status: valid

  example_prompt_pack_input:
    input_summary: "PreCapNextDay needs workflow labels and deliverable shape for a sprint prompt."
    expected_output_assignment:
      assignment_id: expected_output_assignment_prompt_pack_input
      source_intent_summary: "Prepare workflow/process context for prompt generation."
      expected_output_type: prompt_pack_input
      output_family_tags:
        - prompt_support_artifact
        - workflow_artifact
      workflow_process_context:
        workflow_stage: planning
        process_stage: prompt_preparation
        sprint_id: S1
        flow_id: F3
      target_consumer:
        consumer_type: prompt_engineering
        consumer_need: "Generate a workflow-aligned prompt without redefining process labels."
      format_contract:
        primary_format: yaml
        required_sections:
          - workflow_stage
          - process_stage
          - expected_output_type
          - success_criteria
          - prompt_boundary_notes
      completeness:
        minimum_completion_evidence:
          - workflow_stage_present
          - process_stage_present
          - expected_output_type_present
          - success_criteria_present
        completeness_score: 90
        missing_allowed: true
        completion_status: complete
      fidelity:
        source_fidelity_required: true
        transformation_mode: normalize
        invented_content_policy: allowed_with_flags
        semantic_preservation_required: true
        fidelity_confidence: 86
      validation:
        success_criteria:
          - does_not_include_final_prompt_body
          - includes_workflow_process_fit_notes
          - marks_uncertainty
        operator_review_required: false
      validation_status: valid_with_warnings

  example_tradeoff_card:
    input_summary: "Workflow fit suggests validation, while routing recommends a low-cost batch surface and prompt quality suggests a high-reasoning prompt."
    expected_output_assignment:
      assignment_id: expected_output_assignment_tradeoff_card
      source_intent_summary: "Resolve conflict between workflow fit, prompt quality, and routing efficiency."
      expected_output_type: tradeoff_card
      output_family_tags:
        - decision_artifact
        - validation_artifact
        - operator_control_artifact
      workflow_process_context:
        workflow_stage: operator_decision
        process_stage: operator_review
        workflow_fit_notes:
          - conflict_resolution_order_applies
      target_consumer:
        consumer_type: operator
        consumer_need: "Choose between valid but conflicting recommendations."
      format_contract:
        primary_format: markdown_with_yaml_blocks
        required_sections:
          - options
          - tradeoffs
          - authority_order
          - recommended_decision_or_review_request
      completeness:
        minimum_completion_evidence:
          - options_named
          - tradeoffs_identified
          - operator_choice_requested
        completeness_score: 88
        missing_allowed: true
        missing_items:
          - exact_operator_preference
        completion_status: partial
      fidelity:
        source_fidelity_required: true
        transformation_mode: synthesize
        invented_content_policy: allowed_with_flags
        semantic_preservation_required: true
        fidelity_confidence: 84
      validation:
        success_criteria:
          - operator_decision_authority_preserved
          - workflow_fit_ranked_above_prompt_quality_and_routing_efficiency
          - no_silent_override
        operator_review_required: true
        operator_review_flags:
          - decision_required_before_finalization
      validation_status: operator_review_recommended

  example_blocked_patch_plan:
    input_summary: "Operator asks for a patch plan, but no target file or allowed operation is known."
    expected_output_assignment:
      assignment_id: expected_output_assignment_blocked_patch_plan
      source_intent_summary: "Prepare implementation support, but target is missing."
      expected_output_type: code_or_file_patch_plan
      output_family_tags:
        - implementation_artifact
        - operator_control_artifact
      workflow_process_context:
        workflow_stage: execution_support
        process_stage: blocked_or_deferred
      target_consumer:
        consumer_type: operator
        consumer_need: "Supply missing target path or permission boundary."
      format_contract:
        primary_format: checklist
        required_sections:
          - missing_inputs
          - required_operator_decision
          - safe_next_step
      completeness:
        minimum_completion_evidence:
          - missing_target_named
          - no_patch_invented
          - operator_decision_requested
        completeness_score: 60
        missing_allowed: false
        missing_items:
          - target_path
          - allowed_operation
        completion_status: blocked
      fidelity:
        source_fidelity_required: true
        transformation_mode: validate_only
        invented_content_policy: forbidden
        semantic_preservation_required: true
        fidelity_confidence: 96
      validation:
        success_criteria:
          - does_not_execute_patch
          - does_not_invent_target
          - asks_for_operator_decision
        operator_review_required: true
        operator_review_flags:
          - implementation_target_missing
      validation_status: blocked_by_missing_operator_decision
```
````

---

# VALIDATION - FILE-SPECIFIC CHECKS

- [ ] Defines `expected_output_type_taxonomy` and `expected_output_assignment` exactly once.
- [ ] Includes output family tags, completeness fields, fidelity fields, validation fields, workflow/process fit hints, and examples.
- [ ] Does not redefine `workflow_stage_taxonomy` or `process_stage_taxonomy`.
- [ ] Does not define prompt packet, routing, usage, quota, daily-plan, flow-packet, or project-status schemas.
- [ ] Uses typed numeric constraints for completeness and fidelity confidence fields.
- [ ] Uses YAML with 2-space indentation.

---

# NEXT PROMPT

Paste this next:
> Prompt WPD5:
> Create exactly one file.
>
> # FILE: .claude/skills/workflow-process-design/references/workflow-record-contract.md
>
> File type: reference_contract.
> Schema ownership: owns workflow_record schema and reusable workflow normalization fields for workflow/process design.
> Context carry-forward:
> - .claude/skills/workflow-process-design/SKILL.md
> - .claude/skills/workflow-process-design/references/workflow-stage-taxonomy.md
> - .claude/skills/workflow-process-design/references/process-stage-taxonomy.md
> - .claude/skills/workflow-process-design/references/expected-output-type-contract.md
>
> This file must define:
> - workflow_record schema
> - workflow identity and scope fields
> - inputs, outputs, gates, and transitions
> - workflow/process label references
> - expected output references
> - operator review and conflict fields
> - downstream consumer fields
> - minimal examples
>
> Rules:
> - Do not duplicate workflow_stage_taxonomy, process_stage_taxonomy, or expected_output_type taxonomy.
> - Do not define prompt_packet, routing_decision, quota, usage, daily-plan, flow-packet, or project-status schemas.
> - Do not create provider-specific prompt rules.
> - Use YAML with 2-space indentation.
>
> Next prompt target: Prompt WPD6.
