# FILE: .claude/skills/workflow-process-design/references/process-stage-taxonomy.md

# Process Stage Taxonomy

```yaml
process_stage_taxonomy_contract:
  artifact_name: process_stage_taxonomy
  file_role: workflow_process_design_reference_taxonomy
  purpose: >
    Define stable process-stage labels for identifying where a task, sprint,
    prompt, or workflow artifact sits inside a work process. Process stages
    describe the current phase of work, not the provider, prompt style, model
    route, project plan, daily plan, or final output schema.

  ownership:
    owns:
      - process_stage_taxonomy
      - process_stage_assignment
      - process_stage_selection_rules
      - process_stage_progression_rules
      - sprint_to_process_stage_hints
      - process_stage_expected_output_hints
      - prompt_process_alignment_implications
      - process_stage_ambiguity_flags
      - process_stage_examples
    must_not_own:
      - workflow_stage_taxonomy
      - expected_output_type_contract
      - prompt_packet_schema
      - final_copy_paste_prompt_schema
      - routing_decision_schema
      - planned_usage_budget_schema
      - AI_surface_inventory_schema
      - next_day_plan_schema
      - flow_packet_schema
      - project_status_merge_schema
      - calendar_event_schema

  global_rules:
    one_primary_process_stage_per_unit: true
    secondary_process_stages_allowed: true
    max_secondary_process_stages: 2
    process_stage_is_not_workflow_stage: true
    process_stage_is_not_expected_output_type: true
    process_stage_is_not_provider_or_model_route: true
    operator_review_when_stage_conflict_affects_output: true
```

## Schema: process_stage_assignment

```yaml
process_stage_assignment:
  type: object
  required:
    - assignment_id
    - primary_process_stage
    - selection_basis
    - confidence
    - validation_status

  fields:
    assignment_id:
      type: string
      format: "process_stage_assignment_<short_slug>"
      required: true

    primary_process_stage:
      type: string
      allowed:
        - intake_and_framing
        - source_collection
        - extraction
        - normalization
        - synthesis
        - option_generation
        - decision_support
        - planning
        - drafting
        - implementation
        - refinement
        - validation
        - packaging
        - handoff
        - recap_and_learning
        - operator_review
        - blocked_or_deferred
      required: true

    secondary_process_stages:
      type: list
      item_type: string
      allowed:
        - intake_and_framing
        - source_collection
        - extraction
        - normalization
        - synthesis
        - option_generation
        - decision_support
        - planning
        - drafting
        - implementation
        - refinement
        - validation
        - packaging
        - handoff
        - recap_and_learning
        - operator_review
        - blocked_or_deferred
      min_items: 0
      max_items: 2
      required: false

    selection_basis:
      type: list
      item_type: string
      min_items: 1
      max_items: 8
      required: true

    confidence:
      type: integer
      min: 1
      max: 100
      required: true

    ambiguity_flags:
      type: list
      item_type: string
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

## Process Stage Taxonomy

```yaml
process_stage_taxonomy:
  allowed:
    intake_and_framing:
      definition: "Clarify the task, boundary, objective, input condition, and success frame before substantive work begins."
      use_when:
        - task_scope_is_unclear
        - operator_intent_needs_structuring
        - input_boundaries_need_definition
        - success_criteria_must_be_named_first
      avoid_when:
        - task_boundary_is_already_explicit
        - operator_requests_direct_artifact_generation
      typical_output_hints:
        - clarified_task_frame
        - assumptions
        - boundaries
        - open_questions
      prompt_implications:
        - ask_for_missing_constraints_only_when_blocking
        - otherwise_state_assumptions_and_continue

    source_collection:
      definition: "Gather, list, or verify source material before extraction, synthesis, or decision work."
      use_when:
        - source_material_is_missing_or_incomplete
        - current_verification_is_required
        - relevant_files_or_context_must_be_identified
      avoid_when:
        - sources_are_already_provided_and_complete
        - task_is_source_free_generation
      typical_output_hints:
        - source_list
        - evidence_map
        - missing_source_flags
      prompt_implications:
        - require source authority rules
        - separate verified facts from assumptions

    extraction:
      definition: "Pull explicit entities, steps, constraints, decisions, or artifact elements from supplied material."
      use_when:
        - messy_source_material_contains_implicit_structure
        - source_fidelity_is_primary
        - no_new_design_decision_should_be_added_yet
      avoid_when:
        - source_has_already_been_normalized
        - operator_requests_net_new_artifact_design
      typical_output_hints:
        - extracted_items
        - raw_stage_candidates
        - source_preserving_summary
      prompt_implications:
        - preserve source semantics
        - mark uncertain extraction rather than smoothing it away

    normalization:
      definition: "Convert extracted or inconsistent material into a stable contract, taxonomy, format, or naming system."
      use_when:
        - labels_need_canonicalization
        - duplicated_or_overlapping_items_need_clean_structure
        - artifact_shape_must_be_standardized
      avoid_when:
        - source_material_has_not_been_extracted
        - creative_generation_is_primary
      typical_output_hints:
        - normalized_schema
        - canonical_key_names
        - mapping_table
      prompt_implications:
        - show mapping from old terms to canonical terms when useful
        - avoid inventing unsupported domain content

    synthesis:
      definition: "Combine multiple inputs into integrated meaning, implications, or a coherent operating view."
      use_when:
        - multiple_valid_inputs_need_combination
        - operator_needs_distilled_understanding
        - decision_context_needs_compression
      avoid_when:
        - exact_extraction_or_validation_is_primary
        - input_is_too_thin_for_integration
      typical_output_hints:
        - synthesis_summary
        - integrated_model
        - implication_map
      prompt_implications:
        - distinguish facts_from_inferences
        - surface unresolved tensions

    option_generation:
      definition: "Create multiple possible approaches, structures, names, concepts, or solution paths before selection."
      use_when:
        - design_space_is_open
        - operator_needs_comparison_options
        - no_single_solution_is_implied_by_constraints
      avoid_when:
        - one_primary_output_policy_applies
        - operator_requested_final_single_artifact
      typical_output_hints:
        - option_set
        - option_dimensions
        - tradeoff_notes
      prompt_implications:
        - cap options to a useful number
        - include selection criteria

    decision_support:
      definition: "Evaluate options or conflicts and recommend a choice, tradeoff, or next operator decision."
      use_when:
        - operator_choice_is_needed
        - competing_valid_options_exist
        - tradeoff_card_is_required
      avoid_when:
        - decision_is_already_locked
        - task_is_execution_or_formatting_only
      typical_output_hints:
        - recommendation
        - tradeoff_card
        - decision_request
      prompt_implications:
        - name the decision owner
        - do not override explicit operator choice

    planning:
      definition: "Sequence work into steps, phases, dependencies, or execution-ready structure."
      use_when:
        - future_work_must_be_ordered
        - dependencies_or_gates_matter
        - operator_needs_an_action_structure
      avoid_when:
        - package_boundary_forbids_daily_or_project_plan_creation
        - task_is_current_artifact_generation_only
      typical_output_hints:
        - phase_plan
        - task_sequence
        - dependency_map
      prompt_implications:
        - distinguish planning from executing
        - include operator gates where required

    drafting:
      definition: "Create first-pass content, file bodies, prompt bodies, interface text, or structured artifacts."
      use_when:
        - an initial artifact_body_is_requested
        - source_and_contract_are_sufficient
        - iteration_will_follow
      avoid_when:
        - validation_or_extraction_is_the_only_task
        - missing_constraints_make_generation unsafe
      typical_output_hints:
        - draft_file
        - draft_prompt
        - draft_content_block
      prompt_implications:
        - use the requested output contract
        - mark uncertain generated elements

    implementation:
      definition: "Apply, code, patch, configure, or otherwise execute a bounded change in an artifact or system."
      use_when:
        - concrete_change_is_requested
        - target_scope_is_known
        - permission_or_execution_boundary_is_clear
      avoid_when:
        - task_is_design_only
        - exact_target_or_permission_is_missing
      typical_output_hints:
        - implementation_patch
        - changed_file
        - execution_log
      prompt_implications:
        - require exact target and allowed operations
        - do not expand implementation scope silently

    refinement:
      definition: "Improve an existing draft, prompt, file, process, or artifact without changing its core intent."
      use_when:
        - existing_artifact_is_supplied
        - operator_requests_polish_or_improvement
        - failure_feedback_exists
      avoid_when:
        - artifact_needs_full_redesign
        - source_fidelity_requires_no_semantic_change
      typical_output_hints:
        - revised_artifact
        - change_notes
        - before_after_delta
      prompt_implications:
        - preserve original intent and structure unless change is requested
        - state substantive deviations

    validation:
      definition: "Check an artifact, decision, prompt, or workflow against a contract, checklist, rule set, or acceptance criteria."
      use_when:
        - pass_fail_check_is_needed
        - contract_compliance_matters
        - final_gate_before_use
      avoid_when:
        - no_artifact_or_criteria_exists
        - operator_requests_generation_not_review
      typical_output_hints:
        - validation_report
        - defect_list
        - acceptance_status
      prompt_implications:
        - cite or name the checked criteria inside the working artifact when useful
        - separate blockers from warnings

    packaging:
      definition: "Prepare final usable artifact structure, file sequence, manifest, handoff bundle, or copy-paste-ready deliverable."
      use_when:
        - content_is_ready_for_distribution_or_next_system
        - package_file_index_or_final_bundle_is_needed
        - artifact_must_be_operator_ready
      avoid_when:
        - core content_is_still_unvalidated
        - task_is_early_exploration
      typical_output_hints:
        - package_manifest
        - final_bundle
        - operator_handoff
      prompt_implications:
        - avoid duplicating schemas in manifests
        - include only index-level package metadata when packaging

    handoff:
      definition: "Translate completed work into the next actor's input context, constraints, risks, and required next action."
      use_when:
        - output_crosses_role_or_skill_boundary
        - another process_or_operator_step_must_continue
        - next_context_needs_compression
      avoid_when:
        - work_is_self_contained_and_final
        - no_downstream_consumer_exists
      typical_output_hints:
        - handoff_packet
        - next_prompt
        - next_context_block
      prompt_implications:
        - name the receiver and expected next action
        - preserve unresolved decisions

    recap_and_learning:
      definition: "Convert completed work, result feedback, or execution notes into reusable state, learning, or future constraints."
      use_when:
        - task_or_flow_has_completed
        - prompt_result_feedback_exists
        - workflow_or_prompt_learning_should_be_captured
      avoid_when:
        - no_execution_or_feedback_material_exists
        - project_status_merge_is_out_of_scope
      typical_output_hints:
        - recap_notes
        - learning_signals
        - future_adjustments
      prompt_implications:
        - separate actual result from proposed next action
        - do not merge project state unless the owning skill handles it

    operator_review:
      definition: "Pause or flag the artifact for operator approval, correction, or tradeoff decision."
      use_when:
        - high_impact_uncertainty_exists
        - operator_preference_is_required
        - package_boundary_requires_approval
      avoid_when:
        - operator_has_already_approved
        - review_would_block_without_reason
      typical_output_hints:
        - review_flags
        - tradeoff_card
        - decision_needed
      prompt_implications:
        - keep the review request precise
        - provide a default recommendation only when grounded

    blocked_or_deferred:
      definition: "Mark work as unable to proceed or intentionally postponed because required inputs, authority, or decisions are absent."
      use_when:
        - required_input_is_missing
        - target_is_unavailable
        - operator_decision_blocks_progress
        - task_is_out_of_scope_for_current_skill
      avoid_when:
        - safe_assumption_can_be_made
        - partial_output_can_be_usefully_created
      typical_output_hints:
        - blocker_note
        - missing_input_list
        - deferred_next_step
      prompt_implications:
        - state the minimum unblocker
        - produce partial work if it remains useful and within scope
```

## Selection Rules

```yaml
process_stage_selection_rules:
  priority_order:
    1: explicit_operator_stage
    2: owning_skill_or_prompt_flow_instruction
    3: requested_action
    4: source_context_shape
    5: requested_output_shape
    6: sprint_role
    7: downstream_consumer
    8: validation_or_review_need

  rules:
    explicit_operator_stage:
      rule: "Use the operator-specified process_stage when it is allowed and does not violate package boundaries."
      conflict_behavior: "If it conflicts with the requested output or package boundary, mark operator_review_recommended."

    owning_skill_or_prompt_flow_instruction:
      rule: "When a skill or prompt flow names the required process stage, treat it as binding for that artifact."
      conflict_behavior: "Do not silently substitute another stage; add ambiguity_flags."

    requested_action:
      rule: "Infer the stage from the primary verb and artifact state."
      examples:
        - action: "extract"
          likely_stage: extraction
        - action: "normalize"
          likely_stage: normalization
        - action: "validate"
          likely_stage: validation
        - action: "create first draft"
          likely_stage: drafting
        - action: "package final files"
          likely_stage: packaging

    source_context_shape:
      rule: "Match the process stage to the maturity of source material."
      examples:
        - source_context_shape: raw_messy_notes
          likely_stage: extraction
        - source_context_shape: extracted_items
          likely_stage: normalization
        - source_context_shape: complete_draft
          likely_stage: validation
        - source_context_shape: failed_prompt_result
          likely_stage: recap_and_learning

    requested_output_shape:
      rule: "Use the output shape as a stage hint but not as a schema definition."
      examples:
        - requested_output_shape: tradeoff_card
          likely_stage: decision_support
        - requested_output_shape: final_manifest
          likely_stage: packaging
        - requested_output_shape: validation_report
          likely_stage: validation

    sprint_role:
      rule: "Use sprint role as a weak hint, not a hard constraint."
      examples:
        - sprint_role: S1_first_work_sprint
          common_stages:
            - intake_and_framing
            - extraction
            - drafting
            - implementation
        - sprint_role: S2_second_work_or_deepening_sprint
          common_stages:
            - synthesis
            - refinement
            - validation
            - packaging
        - sprint_role: S3_recap_digest_preparation_sprint
          common_stages:
            - handoff
            - recap_and_learning
            - operator_review

    downstream_consumer:
      rule: "When another skill or artifact will consume the result, prefer the process stage that prepares the cleanest handoff."
      examples:
        - downstream_consumer: prompt_engineering
          likely_stages:
            - normalization
            - validation
        - downstream_consumer: ai_routing_and_usage_tracking
          likely_stages:
            - decision_support
            - validation
        - downstream_consumer: PreCapNextDay
          likely_stages:
            - planning
            - handoff

    validation_or_review_need:
      rule: "If correctness, boundary compliance, or operator choice is the dominant risk, use validation or operator_review."
```

## Relationship to Workflow Stage

```yaml
workflow_stage_relationship:
  distinction:
    workflow_stage_question: "What kind of work is this overall?"
    process_stage_question: "Where is this task within that work?"

  examples:
    - workflow_stage: prompt_design_workflow
      possible_process_stages:
        - intake_and_framing
        - drafting
        - refinement
        - validation
        - recap_and_learning

    - workflow_stage: skill_package_creation_workflow
      possible_process_stages:
        - extraction
        - normalization
        - drafting
        - validation
        - packaging

    - workflow_stage: research_and_synthesis_workflow
      possible_process_stages:
        - source_collection
        - extraction
        - synthesis
        - decision_support
        - handoff

  anti_confusion_rules:
    - "Do not use workflow_stage as a substitute for process_stage."
    - "Do not use process_stage as a substitute for expected_output_type."
    - "A workflow may pass through multiple process stages."
    - "A process stage may appear inside many different workflow stages."
```

## Prompt and Process Alignment Rules

```yaml
prompt_process_alignment_implications:
  alignment_checks:
    extraction:
      prompt_should:
        - preserve_source_semantics
        - avoid_unsupported_new_design
        - mark_uncertainty
      prompt_should_not:
        - smooth_away_source_conflicts
        - finalize_unvalidated_structure

    normalization:
      prompt_should:
        - define_canonical_terms
        - map_variants_to_canonical_keys
        - validate_consistency
      prompt_should_not:
        - change_meaning_without_flagging_it
        - duplicate_schema_ownership

    drafting:
      prompt_should:
        - produce_a_complete_initial_artifact
        - follow_the_expected_output_contract
        - expose_uncertain_placeholders
      prompt_should_not:
        - claim_final_validation_if_not_checked

    refinement:
      prompt_should:
        - preserve_original_intent
        - target_specific_defects
        - state_substantive_changes
      prompt_should_not:
        - replace_user_concept_with_generic_polish

    validation:
      prompt_should:
        - name_checked_criteria
        - separate_blockers_from_warnings
        - produce_acceptance_status
      prompt_should_not:
        - silently_repair_without_reporting_defects

    packaging:
      prompt_should:
        - produce_operator_ready_structure
        - avoid_schema_duplication
        - include_next_handoff_only_if_needed
      prompt_should_not:
        - become_a_second_contract_file

    recap_and_learning:
      prompt_should:
        - capture_actual_result
        - capture_learning_signal
        - propose_future_adjustment
      prompt_should_not:
        - merge_project_status_unless_owned_elsewhere
```

## Ambiguity Flags

```yaml
process_stage_ambiguity_flags:
  allowed:
    - explicit_stage_conflicts_with_requested_output
    - workflow_stage_used_as_process_stage
    - expected_output_type_used_as_process_stage
    - too_many_process_stages_requested
    - source_context_too_thin_for_stage
    - validation_requested_without_criteria
    - implementation_requested_without_target
    - finalization_requested_before_validation
    - operator_decision_required
    - package_boundary_conflict

  correction_rules:
    explicit_stage_conflicts_with_requested_output: "Preserve the operator request, state the conflict, and recommend the safer process stage."
    workflow_stage_used_as_process_stage: "Classify workflow_stage separately and infer process_stage from the task action."
    expected_output_type_used_as_process_stage: "Keep expected_output_type as output metadata and choose process_stage from task maturity."
    too_many_process_stages_requested: "Select one primary_process_stage and move the others to secondary_process_stages or sequence notes."
    source_context_too_thin_for_stage: "Use intake_and_framing, source_collection, or blocked_or_deferred depending on whether partial progress is possible."
    validation_requested_without_criteria: "Use operator_review_recommended and request or infer criteria only when safe."
    implementation_requested_without_target: "Use blocked_or_deferred unless a safe bounded target is supplied."
    finalization_requested_before_validation: "Use validation before packaging or mark valid_with_warnings."
    operator_decision_required: "Present a compact tradeoff card or review flag."
    package_boundary_conflict: "Do not perform work owned by another package; return a compliant handoff or flag."
```

## Minimal Examples

```yaml
process_stage_examples:
  example_extract_from_messy_process_notes:
    input_summary: "Operator provides raw notes about a recurring workflow and asks to make sense of it."
    process_stage_assignment:
      assignment_id: process_stage_assignment_extract_workflow_notes
      primary_process_stage: extraction
      secondary_process_stages:
        - normalization
      selection_basis:
        - raw_messy_notes
        - implicit_steps_present
        - source_fidelity_needed
      confidence: 88
      validation_status: valid

  example_validate_prompt_against_workflow:
    input_summary: "Operator supplies a prompt packet and asks whether it fits the workflow and expected output."
    process_stage_assignment:
      assignment_id: process_stage_assignment_validate_prompt_fit
      primary_process_stage: validation
      secondary_process_stages: []
      selection_basis:
        - existing_artifact_supplied
        - contract_compliance_requested
        - prompt_process_alignment_needed
      confidence: 94
      validation_status: valid

  example_create_first_file_body:
    input_summary: "Operator asks to create one reference contract file from the next prompt in the package flow."
    process_stage_assignment:
      assignment_id: process_stage_assignment_draft_reference_file
      primary_process_stage: drafting
      secondary_process_stages:
        - validation
      selection_basis:
        - one_file_per_prompt_flow_active
        - exact_file_target_known
        - output_must_be_final
      confidence: 91
      validation_status: valid_with_warnings
      operator_review_flags:
        - validation_should_be_checked_after_generation

  example_package_manifest:
    input_summary: "Operator asks for the final package manifest after all support files exist."
    process_stage_assignment:
      assignment_id: process_stage_assignment_package_manifest
      primary_process_stage: packaging
      secondary_process_stages: []
      selection_basis:
        - final_package_index_requested
        - support_files_complete
        - no_schema_duplication_allowed
      confidence: 96
      validation_status: valid

  example_blocked_implementation:
    input_summary: "Operator asks to patch a file but no target path or allowed operation is known."
    process_stage_assignment:
      assignment_id: process_stage_assignment_blocked_patch
      primary_process_stage: blocked_or_deferred
      secondary_process_stages:
        - operator_review
      selection_basis:
        - implementation_requested_without_target
        - permission_boundary_unclear
      confidence: 89
      ambiguity_flags:
        - implementation_requested_without_target
      operator_review_flags:
        - exact_target_required
      validation_status: blocked_by_missing_operator_decision
```

---

# VALIDATION - FILE-SPECIFIC CHECKS

- [ ] Defines `process_stage_taxonomy` and `process_stage_assignment` exactly once.
- [ ] Uses process-stage labels only; does not redefine `workflow_stage_taxonomy`.
- [ ] Does not define `expected_output_type_contract` or prompt packet schema.
- [ ] Does not define routing, quota, usage, daily-plan, or project-status schemas.
- [ ] Uses typed numeric constraints for `confidence`.
- [ ] Includes selection rules, workflow-stage relationship, prompt/process alignment implications, ambiguity flags, and examples.
- [ ] Uses YAML with 2-space indentation.

---

# NEXT PROMPT

Paste this next:
> Prompt WPD4:
> Create exactly one file.
>
> # FILE: .claude/skills/workflow-process-design/references/expected-output-type-contract.md
>
> File type: reference_contract.
> Schema ownership: owns expected_output_type taxonomy and expected-output validation fields for workflow/process design.
> Context carry-forward:
> - .claude/skills/workflow-process-design/SKILL.md
> - .claude/skills/workflow-process-design/references/workflow-stage-taxonomy.md
> - .claude/skills/workflow-process-design/references/process-stage-taxonomy.md
>
> This file must define:
> - expected_output_type taxonomy
> - expected output assignment schema
> - output family tags
> - completeness and fidelity fields
> - validation status fields
> - workflow/process fit hints
> - minimal examples
>
> Rules:
> - Do not duplicate prompt_packet schema from prompt-engineering.
> - Do not define routing_decision, usage, or quota schemas.
> - Do not define workflow_stage_taxonomy or process_stage_taxonomy again.
> - Do not create daily plan, flow packet, or project-status schemas.
> - Use YAML with 2-space indentation.
>
> Next prompt target: Prompt WPD5.
