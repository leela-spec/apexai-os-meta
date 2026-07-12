---
name: prompt-engineering
description: Use this skill when the operator asks to generate, evaluate, or improve finalized copy-paste prompts for AI work. Accepts operator tasks, source context, workflow context, expected output types, routing notes, and prompt feedback. Produces prompt_packet, prompt_sequence, final_copy_paste_prompt, and prompt_quality_review outputs. Does not create daily plans, execute project work, run FlowRecap, or merge project status.
---

# Prompt Engineering

## Skill Contract

```yaml
skill_contract:
  primary_output: prompt_packet
  output_role: finalized_copy_paste_prompt_generator
  accepted_inputs:
    - operator_task
    - source_context
    - project_context
    - workflow_context
    - flow_packet
    - sprint_goal
    - expected_output_type
    - routing_decision
    - usage_tracking_tags
    - prompt_result_feedback
  produced_outputs:
    - prompt_packet
    - prompt_sequence
    - final_copy_paste_prompt
    - prompt_quality_review
    - operator_review_flags
  prompt_packet_must_include:
    - prompt_task_type
    - workflow_stage
    - process_stage
    - expected_output_type
    - provider_target
    - provider_rationale
    - prompt_design_rationale
    - final_copy_paste_prompt
    - prompt_failure_hints
    - prompt_learning_hints
    - usage_tracking_tags
    - validation_status
  provider_targets:
    allowed:
      - ChatGPT
      - Claude
      - Gemini
      - OpenRouter_later
      - provider_unspecified
  validation_status:
    allowed:
      - valid
      - valid_with_warnings
      - operator_review_recommended
      - low_confidence_auto_generated
      - blocked_by_missing_operator_decision
  boundaries:
    must_do:
      - generate_finalized_copy_paste_prompts
      - support_provider_specific_prompting
      - include_short_provider_rationale
      - include_short_prompt_design_rationale
      - include_prompt_failure_hints
      - include_prompt_learning_hints
      - separate_start_prompts_from_follow_up_prompts
      - use_prompt_task_taxonomy
      - use_iteration_loop_patterns
      - expose_prompt_quality_validation
      - interface_with_workflow_process_design
      - interface_with_ai_routing_and_usage_tracking
    must_not_create:
      - daily_plan
      - project_execution
      - FlowRecap_output
      - project_status_merge
      - final_OpenRouter_model_mapping
      - mandatory_machine_readable_capture_block_inside_every_prompt
      - multiple_parallel_prompt_systems_by_default
```

## Supporting Files

```yaml
supporting_files:
  - path: references/old-apex-prompting-doctrine.md
    read_when:
      - designing_prompt_packet
      - writing_final_copy_paste_prompt
      - checking_prompt_failure_modes

  - path: references/prompt-packet-contract.md
    read_when:
      - creating_prompt_packet
      - validating_prompt_sequence
      - separating_start_and_follow_up_prompts
  - path: references/prompt-task-taxonomy.md
    read_when:
      - classifying_prompt_task
      - selecting_prompt_pattern
      - matching_task_to_expected_output
  - path: references/iteration-loop-patterns.md
    read_when:
      - selecting_iteration_loop
      - adding_follow_up_prompts
      - defining_stop_conditions
  - path: references/provider-style-contract-chatgpt.md
    read_when:
      - provider_target_is_ChatGPT
      - deep_research_prompt_needed
      - agent_run_prompt_needed
  - path: references/provider-style-contract-claude.md
    read_when:
      - provider_target_is_Claude
      - Claude_Code_file_generation_prompt_needed
      - Claude_extended_thinking_prompt_needed
  - path: references/provider-style-contract-gemini.md
    read_when:
      - provider_target_is_Gemini
      - long_context_digest_prompt_needed
      - broad_document_comparison_needed
  - path: references/provider-style-contract-openrouter-todo.md
    read_when:
      - provider_target_is_OpenRouter_later
      - API_low_reasoning_placeholder_needed
      - OpenRouter_boundary_check_needed
  - path: references/prompt-quality-validation.md
    read_when:
      - validating_prompt_quality
      - assigning_validation_status
      - creating_prompt_quality_review
  - path: references/prompt-learning-feedback-contract.md
    read_when:
      - processing_prompt_result_feedback
      - capturing_failed_prompt_learning
      - preparing_pattern_update_candidate
  - path: examples/starter-prompt-pack-example.md
    read_when:
      - operator_requests_example
      - running_starter_manual_test
      - calibrating_prompt_pack_shape
  - path: package-manifest.md
    read_when:
      - operator_inspects_package_structure
      - validating_package_files
      - checking_dependency_map
```

## Procedure

1. **Load task context.** Read the operator_task, available source_context, project_context, workflow_context, flow_packet, sprint_goal, expected_output_type, routing_decision, usage_tracking_tags, and prompt_result_feedback, then mark missing but useful inputs as operator_review_flags.
2. **Classify prompt work.** Assign the prompt task type, expected_output_type, workflow_stage, process_stage, and best matching iteration loop, using low_confidence_auto_generated when labels are inferred from thin context.
3. **Resolve provider fit.** Use routing_decision when supplied, request ai-routing-and-usage-tracking guidance when needed, and set provider_target, provider_rationale, cost or scarcity notes, fallback_surface, and usage_tracking_tags without overriding operator choice.
4. **Design the prompt packet.** Create one primary prompt_packet with clean metadata outside the prompt body, a short prompt_design_rationale, success criteria, prompt_failure_hints, prompt_learning_hints, and no parallel alternative prompt systems by default.
5. **Write copy-paste prompt content.** Produce the final_copy_paste_prompt in provider-aware language with clear role, task, context, output contract, constraints, validation criteria, iteration instructions, and stop conditions.
6. **Add follow-up prompts when useful.** Separate start prompts from follow_up_prompts, include only follow-ups that advance the selected iteration loop, and keep each prompt directly executable by the operator.
7. **Validate prompt quality.** Run prompt_quality_validation, check workflow/process alignment through workflow-process-design when needed, assign validation_status, and surface any mismatch as operator_review_recommended or blocked_by_missing_operator_decision.
8. **Present final output.** Return prompt_packet, prompt_sequence when relevant, final_copy_paste_prompt, prompt_quality_review, and operator_review_flags in a compact structure ready for direct use or inclusion in a flow_prompt_pack.

## Failure Modes

```
failure_modes:  missing_task:    trigger: "The operator_task is absent or too vague to determine the prompt objective."    correction: "Ask for the task or generate a low_confidence_auto_generated prompt only if the requested output type is still inferable."  missing_expected_output_type:    trigger: "The expected_output_type is absent and cannot be inferred from workflow_context."    correction: "Set expected_output_type to operator_review_recommended and provide the most likely options."  provider_conflict:    trigger: "The requested provider conflicts with routing_decision or provider fit."    correction: "Keep operator choice visible, list the conflict, and include a fallback_surface without overriding the operator."  workflow_alignment_conflict:    trigger: "The prompt body does not match workflow_stage, process_stage, expected_output_type, or sprint_goal."    correction: "Revise the prompt to match workflow_process_fit or mark validation_status as operator_review_recommended."  overgenerated_alternatives:    trigger: "The output creates multiple parallel prompt systems instead of one primary prompt."    correction: "Collapse alternatives into one primary prompt and keep only concise fallback notes."  capture_block_drift:    trigger: "The prompt requires a mandatory machine-readable capture block inside every prompt body."    correction: "Move capture needs into light_capture_hints or FlowRecap-facing learning hints."  schema_duplication:    trigger: "A referenced contract schema is redefined inside this skill output."    correction: "Remove the duplicate schema and reference the owning contract file by key name."  unsupported_OpenRouter_specificity:    trigger: "The output finalizes OpenRouter model mapping, exact pricing, rankings, or availability."    correction: "Replace exact claims with OpenRouter_later boundary notes and request current verification outside this skill."
```

## Output Requirements

```
output_requirements:  required_outputs:    - prompt_packet    - final_copy_paste_prompt    - prompt_quality_review  optional_outputs:    - prompt_sequence    - follow_up_prompts    - operator_review_flags  prompt_packet_requirements:    metadata_outside_prompt_body: true    one_primary_prompt_system_only: true    provider_rationale_is_short: true    prompt_design_rationale_is_short: true    failure_hints_are_present: true    learning_hints_are_present: true    usage_tracking_tags_are_present_when_supplied: true    workflow_and_process_labels_are_present_when_available: true  final_copy_paste_prompt_requirements:    directly_executable: true    no_source_document_names: true    no_citations_required: true    no_unrequested_machine_readable_capture_block: true    output_contract_is_explicit: true    validation_criteria_are_explicit: true  review_requirements:    validation_status_present: true    operator_review_flags_present_when_needed: true    provider_or_workflow_conflicts_visible: true
```

## Completion Gate

```
completion_gate:  prompt_packet_created: true  final_copy_paste_prompt_created: true  provider_target_or_unspecified_status_recorded: true  provider_rationale_included: true  prompt_design_rationale_included: true  expected_output_type_recorded: true  prompt_failure_hints_included: true  prompt_learning_hints_included: true  validation_status_assigned: true  boundaries_respected: true
```