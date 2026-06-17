# FILE: .claude/skills/workflow-process-design/references/workflow-stage-taxonomy.md

# Workflow Stage Taxonomy

```yaml
workflow_stage_taxonomy:
  artifact_name: workflow_stage_taxonomy
  file_role: workflow_process_design_reference_rules
  purpose: >
    Define compact reusable workflow_stage labels for workflow design,
    prompt-process alignment, sprint planning, validation, handoff, recap
    preparation, and learning capture. This file owns workflow_stage taxonomy
    only. It does not define process_stage, expected_output_type,
    prompt_packet, routing_decision, daily_plan, flow_packet, or project-specific
    workflow doctrine.

  ownership:
    owns:
      - workflow_stage_taxonomy
      - workflow_stage_selection_rules
      - workflow_stage_prompt_implications
      - workflow_stage_validation_checks
      - workflow_stage_examples
    must_not_own:
      - process_stage_taxonomy
      - expected_output_type_contract
      - sprint_structure_contract
      - workflow_record_schema
      - prompt_packet_schema
      - prompt_quality_validation
      - routing_decision_schema
      - daily_plan_schema

  taxonomy_policy:
    simple_enough_for_PreCapNextDay_use: true
    project_specific_stage_sprawl_forbidden: true
    examples_are_calibration_not_doctrine: true
    label_only_when_it_improves_prompt_or_validation: true

  workflow_stage_values:
    intake:
      meaning: "Capture the operator request, goal, constraint, or initial work signal before processing."
      when_to_use:
        - operator_request_is_new
        - task_boundary_is_unclear
        - input_source_has_not_been_classified
      expected_inputs:
        - operator_task
        - raw_request
        - available_context_notes
      expected_outputs:
        - normalized_task_brief
        - missing_context_flags
        - initial_operator_review_flags
      prompt_implications:
        - ask_for_goal_boundary_when_required
        - preserve_operator_words_for_intent
        - avoid_generation_before_task_shape_is_known
      validation_checks:
        - task_goal_is_stated_or_flagged_missing
        - known_constraints_are_preserved
        - no_downstream_output_is_silently_assumed

    source_scan:
      meaning: "Inspect available source material to identify relevant evidence, structure, gaps, and authority conflicts."
      when_to_use:
        - source_context_is_large_or_mixed
        - multiple_documents_or_notes_are_supplied
        - source_authority_may_conflict
      expected_inputs:
        - source_context
        - project_context
        - operator_task
      expected_outputs:
        - source_relevance_map
        - source_gap_notes
        - conflict_or_uncertainty_flags
      prompt_implications:
        - ask_for_or_extract_source_boundaries
        - separate evidence from inference
        - do not cite or name sources inside final package files
      validation_checks:
        - relevant_sources_are_distinguished_from_noise
        - missing_or_conflicting_sources_are_flagged
        - no unsupported source authority is invented

    extraction:
      meaning: "Pull workflow-relevant steps, roles, inputs, outputs, decisions, gates, or examples from raw material."
      when_to_use:
        - raw_notes_contain_implicit_process_logic
        - operator_needs_workflow_record_material
        - examples_need_to_be_converted_into_reusable_parts
      expected_inputs:
        - raw_process_material
        - source_context
        - operator_task
      expected_outputs:
        - extracted_steps
        - extracted_inputs_outputs
        - extracted_gates_or_conflicts
      prompt_implications:
        - preserve source fidelity before cleanup
        - mark inferred structure explicitly
        - do not normalize too early
      validation_checks:
        - extracted_items_trace_to_supplied_material
        - inferred_items_are_marked
        - no project-specific example becomes a universal rule

    normalization:
      meaning: "Convert extracted or messy material into a consistent reusable structure, label set, or contract shape."
      when_to_use:
        - extracted_material_is_inconsistent
        - terms_need_canonical_names
        - workflow_record_or_expected_output_shape_needs_alignment
      expected_inputs:
        - extracted_steps
        - canonical_key_names
        - workflow_context
      expected_outputs:
        - normalized_workflow_shape
        - canonical_labels
        - normalization_notes
      prompt_implications:
        - use canonical keys consistently
        - collapse duplicate labels
        - avoid changing operator intent while cleaning format
      validation_checks:
        - canonical_labels_are_used_consistently
        - removed_or_merged_items_are_not_semantically_lost
        - noncanonical terms_are_translated_without_runtime_drift

    decomposition:
      meaning: "Break a goal, workflow, flow, sprint, or artifact into smaller executable or reviewable units."
      when_to_use:
        - work_is_too_large_for_one_prompt
        - flow_or_sprint_needs_meso_steps
        - dependencies_or_sequence_matter
      expected_inputs:
        - normalized_task_brief
        - workflow_context
        - sprint_goal
      expected_outputs:
        - ordered_subtasks
        - dependency_notes
        - unit_boundaries
      prompt_implications:
        - produce bounded prompt units
        - keep one unit tied to one observable output
        - avoid excessive micro-step expansion
      validation_checks:
        - each_unit_has_a_clear_output
        - dependencies_are_explicit
        - decomposition_does_not_create_extra_process_layers

    planning:
      meaning: "Arrange known tasks, units, constraints, and dependencies into an intended action sequence."
      when_to_use:
        - operator_needs_sequence_or_tradeoff_plan
        - sprint_or_flow_structure_needs_ordering
        - routing_or_prompt_pack_inputs_need_workflow_context
      expected_inputs:
        - decomposed_units
        - constraints
        - operator_intent
      expected_outputs:
        - action_sequence
        - planning_assumptions
        - review_flags
      prompt_implications:
        - include assumptions and stop conditions
        - identify which outputs belong to which stage
        - do not create final daily plans unless another skill owns that output
      validation_checks:
        - sequence_has_rationale
        - constraints_are_respected_or_flagged
        - plan_boundary_does_not_cross_skill_scope

    generation:
      meaning: "Create a new artifact, section, prompt body, contract instance, or structured output from validated context."
      when_to_use:
        - output_shape_is_known
        - input_context_is_sufficient
        - operator_requested_creation_not_review_only
      expected_inputs:
        - output_contract_or_shape
        - validated_context
        - generation_constraints
      expected_outputs:
        - generated_artifact
        - generation_notes
        - operator_review_flags
      prompt_implications:
        - specify final output shape
        - enforce source and boundary constraints
        - include validation criteria in the prompt
      validation_checks:
        - generated_output_matches_expected_shape
        - no forbidden ownership is claimed
        - uncertain_content_is_flagged

    critique:
      meaning: "Evaluate an existing artifact or proposed output against criteria, defects, tradeoffs, and fit."
      when_to_use:
        - artifact_exists_for_review
        - quality_or_alignment_must_be_checked
        - operator_requests_feedback_before_revision
      expected_inputs:
        - existing_artifact
        - validation_criteria
        - expected_output_type
      expected_outputs:
        - critique_report
        - defect_list
        - repair_recommendations
      prompt_implications:
        - make criteria explicit
        - separate critical defects from improvement options
        - avoid rewriting unless requested or paired with generation
      validation_checks:
        - critique_targets_existing_artifact
        - each_defect_maps_to_a_rule_or_goal
        - recommendations_preserve_operator_intent

    validation:
      meaning: "Check whether labels, structures, prompt-process alignment, or artifacts satisfy required rules."
      when_to_use:
        - contract_compliance_matters
        - prompt_process_fit_is_uncertain
        - output_is_ready_for_handoff_or_operator_use
      expected_inputs:
        - candidate_output
        - validation_rules
        - workflow_stage
        - process_stage
        - expected_output_type
      expected_outputs:
        - validation_status
        - validation_findings
        - required_corrections
      prompt_implications:
        - require pass_warning_fail_result
        - make blocking issues explicit
        - use canonical validation_status values
      validation_checks:
        - all_required_rules_are_checked
        - warnings_are_distinguished_from_blockers
        - operator_review_flags_are_present_when_needed

    synthesis:
      meaning: "Combine multiple findings, outputs, sources, or options into a coherent operator-usable conclusion."
      when_to_use:
        - multiple_inputs_need_integration
        - operator_needs_decision_support
        - findings_need_compact_takeaways
      expected_inputs:
        - extracted_findings
        - critique_or_validation_results
        - operator_goal
      expected_outputs:
        - synthesized_summary
        - tradeoff_card
        - recommended_next_step
      prompt_implications:
        - preserve important minority signals
        - separate conclusion from evidence
        - show tradeoffs when choices conflict
      validation_checks:
        - synthesis_covers_all_material_inputs
        - recommendation_matches_operator_goal
        - conflicts_are_not_hidden

    finalization:
      meaning: "Convert a validated or revised output into its final copy-ready, handoff-ready, or package-ready form."
      when_to_use:
        - artifact_has_passed_validation_or_warnings_are_accepted
        - operator_needs_final_copy_ready_output
        - previous_steps_have_resolved_major_defects
      expected_inputs:
        - validated_artifact
        - final_output_constraints
        - accepted_warnings
      expected_outputs:
        - final_artifact
        - completion_notes
        - remaining_operator_review_flags
      prompt_implications:
        - remove draft scaffolding
        - avoid source names and derivation notes in final files
        - keep output focused on target artifact only
      validation_checks:
        - final_output_is_copy_ready
        - no_old_decision_trace_remains
        - remaining_warnings_are_explicit

    handoff:
      meaning: "Prepare a structured transfer from one role, skill, package, workflow, or planning layer to another."
      when_to_use:
        - downstream_skill_or_operator_needs_context
        - output_will_seed_next_process
        - conflict_or_status_needs_transfer
      expected_inputs:
        - finalized_or_validated_output
        - downstream_consumer
        - handoff_constraints
      expected_outputs:
        - handoff_summary
        - consumer_inputs
        - unresolved_flags
      prompt_implications:
        - identify downstream consumer
        - include only necessary context
        - distinguish required next action from optional followup
      validation_checks:
        - downstream_consumer_is_named_by_role_or_artifact
        - required_inputs_are_present_or_flagged
        - handoff_does_not_execute_downstream_work

    recap_preparation:
      meaning: "Prepare work-session material so a recap process can convert it into durable state or learning."
      when_to_use:
        - sprint_or_flow_is_ending
        - raw_execution_material_needs_capture
        - prompt_results_or_failures_need_future_use
      expected_inputs:
        - sprint_outputs
        - raw_notes
        - prompt_result_feedback
      expected_outputs:
        - recap_ready_notes
        - decisions_blockers_next_step_candidates
        - usage_or_learning_notes
      prompt_implications:
        - request concise evidence of what happened
        - separate decisions blockers outputs and open questions
        - do not run recap or status merge inside this stage
      validation_checks:
        - recap_material_is_sufficient_for_downstream_digest
        - skipped_or_partial_work_is_marked
        - recap_or_merge_outputs_are_not_created_here

    learning_capture:
      meaning: "Record reusable learning from failed outputs, provider friction, prompt/process mismatch, or operator correction."
      when_to_use:
        - prompt_failed_or_underperformed
        - operator_correction_reveals_pattern
        - workflow_label_or_output_type_was_wrong
      expected_inputs:
        - failed_output_or_feedback
        - correction
        - workflow_context
      expected_outputs:
        - learning_signal
        - avoid_or_repeat_pattern
        - future_validation_hint
      prompt_implications:
        - capture pattern not transcript
        - keep learning lightweight
        - route prompt-quality lessons to prompt engineering when appropriate
      validation_checks:
        - learning_signal_is_actionable
        - private_reasoning_or_unneeded_transcript_is_not_captured
        - downstream_learning_owner_is_clear
```

## Selection Rules

```yaml
workflow_stage_selection_rules:
  priority_order:
    1: explicit_operator_stage_label
    2: requested_action
    3: current_material_state
    4: expected_output_type
    5: downstream_consumer

  rules:
    explicit_operator_stage_label:
      rule: "Use the operator-provided workflow_stage when it is in workflow_stage_values and does not conflict with the requested action."
      conflict_behavior: "Mark operator_review_recommended and list the likely corrected stage."

    requested_action:
      rule: "Classify by the dominant action: read, extract, normalize, plan, generate, critique, validate, synthesize, finalize, hand off, prepare recap, or capture learning."

    current_material_state:
      rule: "Raw material usually maps to source_scan or extraction; cleaned but inconsistent material maps to normalization; validated material maps to finalization or handoff."

    expected_output_type:
      rule: "Choose the workflow_stage that best supports the required expected_output_type without redefining that output type here."

    downstream_consumer:
      rule: "When the output is meant for another skill or planning process, prefer handoff unless the task is still generation or validation."
```

## Examples

```yaml
workflow_stage_examples:
  minimal_intake:
    input_signal:
      operator_task: "Turn this rough workflow idea into a usable process later."
      material_state: rough_request_only
    classification:
      workflow_stage: intake
      reason: "The task boundary and source shape are not yet stable."
      validation_status: operator_review_recommended

  realistic_prompt_pack_planning:
    input_signal:
      operator_task: "Prepare prompts for a sprint from a flow goal."
      material_state: defined_sprint_goal_with_partial_context
      expected_output_type: prompt_pack
    classification:
      workflow_stage: planning
      reason: "The prompt pack needs ordered units before prompt generation."
      prompt_implications:
        - "Ask for sprint goal, output type, success criteria, and stop conditions."
        - "Use prompt-engineering for actual prompt body quality."
      validation_status: valid_with_warnings

  validation_before_handoff:
    input_signal:
      operator_task: "Check whether this generated contract can be passed to the next package file."
      material_state: generated_reference_contract
      expected_output_type: validation_report
    classification:
      workflow_stage: validation
      reason: "The artifact exists and needs compliance checking before transfer."
      next_stage_if_valid: handoff
      validation_status: valid

  example_not_doctrine:
    input_signal:
      operator_task: "Use this project example to infer reusable workflow labels."
      material_state: project_specific_example
    classification:
      workflow_stage: extraction
      reason: "The example may contain reusable structure, but its project-specific choices must not become universal doctrine."
      operator_review_flags:
        - examples_are_calibration_not_doctrine
        - project_specific_stage_sprawl_forbidden
      validation_status: operator_review_recommended
```

---

# VALIDATION - FILE-SPECIFIC CHECKS

- [ ] workflow_stage taxonomy is defined once.
- [ ] Each stage has prompt implications.
- [ ] Examples do not become doctrine.

---

# NEXT PROMPT

Paste this next:
> Prompt WP3:
> Create exactly one file.
>
> # FILE: .claude/skills/workflow-process-design/references/process-stage-taxonomy.md
>
> File type: reference_rules.
> Schema ownership: owns process_stage_taxonomy.
> Context carry-forward:
> - .claude/skills/workflow-process-design/SKILL.md
> - .claude/skills/workflow-process-design/references/workflow-stage-taxonomy.md
>
> Structure constraints:
> - YAML-first taxonomy.
> - Define process_stage values exactly once.
> - For each stage define meaning, compatible workflow stages, compatible expected output types, red flags, and examples.
>
> Content constraints:
> - Include strategy, planning, execution_preparation, operator_execution, recap, status_update, recovery, residual_cleanup, validation, and learning.
> - Keep labels reusable and not project-specific.
> - Make incompatibilities explicit through red flags.
>
> File-specific checks:
> - [ ] process_stage taxonomy is defined once.
> - [ ] Compatibility with workflow_stage is explicit.
> - [ ] Red flags are included.
