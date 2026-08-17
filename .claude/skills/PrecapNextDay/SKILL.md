---
name: PrecapNextDay
description: Use this skill when the operator asks to create, compile, or review a resilient next-day orchestration plan from partial planning, project, recap, calendar, prompt, workflow, or usage context. Produces a PreCap Next Day Brief, one Flow Execution Card per full flow, and real prompt files. Does not execute project work, run FlowRecap, merge status, or require complete inputs.
---

# PreCap Next Day

## Skill Contract

skill_contract:
  execution:
    context: fork
    parent_context_assumed: false
  primary_operator_output: PreCap_Next_Day_Brief
  expanded_outputs:
    - Flow_Execution_Card_per_full_flow
    - actual_prompt_files
  output_role: resilient_daily_orchestration_compiler
  dependencies:
    PromptEngineer:
      load: only_when_prompt_required
    AIRouting:
      load: only_when_route_recommendation_required
  boundaries:
    must_not_create:
      - Do not execute project work.
      - Do not generate FlowRecap outputs.
      - Do not merge project status.
      - Do not create non-workflow calendar blocks.
      - Do not claim calendar writes were completed without explicit operator approval and tool confirmation.
      - Do not finalize OpenRouter model mapping.
      - Do not use API frontier models as the default daily workflow engine.
      - Do not require complete inputs before producing a degraded next-day plan.
      - Do not redefine schemas owned by prompt-engineering, workflow-process-design, ai-routing-and-usage-tracking, FlowRecap, or status-merge packages.
      - Do not treat a placeholder or degraded prompt as execution-ready -- mark it degraded and flag it.
      - Do not require a large flow_prompt_pack machine schema as a completion gate; real prompt files plus the prompt index satisfy the prompt-readiness requirement.
      - Do not duplicate the full flow context across the Brief, a Flow Execution Card, and its prompt files -- each carries only what it owns; the others reference it.
  input_policy:
    all_inputs_optional: true
    missing_inputs_degrade_confidence: true
    missing_inputs_do_not_block_by_default: true
    bootstrap_mode_allowed: true
    conflict_evidence_becomes_operator_review_flags: true
    canonical_source: references/input-intake-and-resilience-contract.md
  input_priority:
    canonical_source: references/input-intake-and-resilience-contract.md
    use_best_available_context_first: true
  execution_modes:
    type: string
    allowed:
      - full_context_mode
      - standard_mode
      - recap_recovery_mode
      - bootstrap_mode
      - calendar_constrained_mode
      - prompt_heavy_mode
    canonical_source: references/input-intake-and-resilience-contract.md
  operator_output_templates:
    PreCap_Next_Day_Brief: templates/precap-next-day-brief-template.md
    Flow_Execution_Card: templates/flow-execution-card-template.md
    Prompt_Files_and_Index: templates/prompt-files-and-index-template.md
  internal_detail_schemas:
    note: >
      These are optional internal-depth references, not required top-level
      output gates. Detailed redesign of this depth is Module 02 (Next Day
      Brief) / Module 03 (Flow Execution Card) / Module 04 (Sprint Prompts)
      work, not Module 00.
    next_day_plan: references/daily-plan-output-contract.md
    flow_packet: references/flow-packet-contract.md
    flow_prompt_pack: references/flow-prompt-pack-contract.md
    calendar_event_write_request: references/calendar-event-write-contract.md
    usage_tracking_plan: references/usage-tracking-dependency-contract.md
    workflow_process_validation_summary: references/workflow-process-validation-contract.md
    validation_status: references/validation-checklist.md

## Supporting Files

supporting_files:
  - path: templates/precap-next-day-brief-template.md
    read_when:
      - producing_the_precap_next_day_brief
      - checking_required_brief_sections
      - creating_the_compact_downstream_handoff
  - path: templates/flow-execution-card-template.md
    read_when:
      - producing_a_flow_execution_card
      - opening_the_full_workspace_for_a_represented_flow
  - path: templates/prompt-files-and-index-template.md
    read_when:
      - producing_real_prompt_files_for_a_flow
      - building_the_prompt_index
      - checking_prompt_file_quality
  - path: references/input-intake-and-resilience-contract.md
    read_when:
      - validating_input_resilience
      - missing_inputs_present
      - bootstrap_mode_needed
      - degraded_mode_needed
  - path: references/daily-plan-output-contract.md
    read_when:
      - reconciling_internal_day-level_structure_beyond_the_Brief_template
  - path: references/flow-packet-contract.md
    read_when:
      - reconciling_internal_per-flow_structure_beyond_the_Flow_Execution_Card_template
  - path: references/flow-prompt-pack-contract.md
    read_when:
      - reconciling_internal_prompt_grouping_beyond_the_Prompt_Files_and_Index_template
  - path: references/prompt-engineering-dependency-contract.md
    read_when:
      - prompt_engineering_dependency_needed
      - degraded_generic_prompt_mode_needed
      - prompt_quality_validation_needed
  - path: references/usage-tracking-dependency-contract.md
    read_when:
      - planning_AI_usage
      - applying_usage_tracking
      - usage_context_missing_or_partial
  - path: references/calendar-event-write-contract.md
    read_when:
      - calendar_workflow_blocks_requested
      - manual_calendar_constraints_available
      - calendar_write_request_needed
  - path: references/workflow-process-validation-contract.md
    read_when:
      - validating_prompt_flow_or_sprint_process_fit
      - assigning_workflow_process_references
      - workflow_process_dependency_missing
  - path: references/validation-checklist.md
    read_when:
      - final_validation
      - failure_mode_triggered
      - operator_review_flags_needed
  - path: precap-next-day-package-manifest.md
    read_when:
      - operator_inspects_package_structure
      - validating_package_files

## Procedure

1. Load the best available context, treat missing inputs as confidence and review signals, and select the safest execution mode.
2. Create the day frame: daily intent, source-context summary, review status, and operator review flags.
3. Represent each fixed daily flow as planned, compressed, skipped, or explicitly omitted with reasons.
4. For each represented flow, produce one Flow Execution Card (full workspace: goals, inputs/dependencies, S1-S3 sprint detail, evidence handoff) -- not a separate machine flow_packet schema duplicating the same content.
5. For each represented flow, produce real prompt files per sprint plus a Prompt Files and Index entry pointing at them (routing reference, readiness, target surface). A degraded or missing prompt is marked `DEGRADED`/`MISSING` and flagged -- it is never presented as ready.
6. Apply prompt-engineering, usage-tracking, and workflow-process dependency interfaces only when the flow content actually requires them, and preserve dependency gaps as degraded-mode review flags instead of redefining upstream schemas.
7. Prepare calendar workflow-block write requests only when relevant, keeping all calendar mutation pending until explicit operator approval and tool confirmation exist.
8. Assemble the PreCap Next Day Brief referencing each Flow Execution Card and its Prompt Files and Index -- the Brief's own compact downstream handoff carries the minimal cross-flow summary; it does not restate each flow's full content.
9. Validate the complete output against the validation checklist, apply the matching failure-mode correction if any check fails, and present unresolved uncertainty as operator_review_flags.

## Failure Modes

failure_modes:
  no_inputs:
    trigger: No usable planning, project, recap, calendar, workflow, prompt, or usage context is supplied.
    correction: Run bootstrap_mode, create a low-confidence PreCap Next Day Brief, define starter F1-F4 flow coverage, and add operator review flags.
  missing_project_status:
    trigger: Current project status and detailed project state are missing or stale.
    correction: Use operator intent, recaps, skipped markers, or bootstrap assumptions, and mark project-state confidence as low.
  prompt_engineering_unavailable:
    trigger: Prompt-engineering references or prompt generation inputs are missing.
    correction: Use degraded_generic_prompt_mode, mark the affected prompt file DEGRADED, reference the missing dependency, and flag prompt optimization for operator review.
  usage_tracking_unavailable:
    trigger: AI surface inventory, quota context, routing recommendations, or usage summaries are missing.
    correction: Use generic usage-tracking hooks, avoid quota claims, and mark usage planning for operator review.
  workflow_process_unavailable:
    trigger: Workflow-process validation, taxonomies, or expected-output references are missing.
    correction: Use generic workflow/process labels, avoid final taxonomy claims, and mark workflow fit for operator review.
  calendar_context_unavailable:
    trigger: Calendar events, fixed constraints, or calendar tooling are missing when workflow blocks are relevant.
    correction: Produce review-only or unscheduled workflow-block requests and mark calendar context as missing.
  unsafe_calendar_write:
    trigger: A calendar write or update is implied as completed without explicit operator approval and tool confirmation.
    correction: Convert the item to a pending calendar_event_write_request or review-only request before returning.
  validation_failure:
    trigger: The output fails the validation checklist or violates a package boundary.
    correction: Apply the relevant correction, preserve valid sections, and return only after the completion gate passes or the blocker is explicit.

## Output Requirements

output_requirements:
  may_define_outputs_in_chat: true
  filesystem_write_required: false
  primary_output:
    - PreCap_Next_Day_Brief
  required_or_defined_when_relevant:
    - Flow_Execution_Card_per_represented_flow
    - actual_prompt_files_per_sprint
    - Prompt_Files_and_Index
    - calendar_event_write_request
    - usage_tracking_plan_or_usage_tracking_summary
    - raw_flow_dump_template
    - skipped_flow_marker_template
    - FlowRecap_handoff_block
    - operator_review_flags
  must_not_include:
    - Do not include full internal schemas owned by reference files -- the operator sees the Brief/Card/Prompt-Index templates, not the underlying machine contract.
    - Do not include prompt-engineering prompt_packet schemas or final prompt doctrine.
    - Do not include workflow-process taxonomies as inline enums.
    - Do not include routing, quota, planned-budget, or usage-delta schemas.
    - Do not include FlowRecap output or project status merge output.
    - Do not present a placeholder or outline prompt as execution-ready.

## Completion Gate

completion_gate:
  precap_next_day_brief_exists: true
  fixed_flows_are_represented_or_explicitly_omitted: true
  represented_flows_have_flow_execution_cards: true
  represented_flows_have_real_prompt_files_or_explicit_degraded_flag: true
  no_placeholder_prompt_accepted_as_ready: true
  usage_tracking_hooks_exist_or_degraded_usage_review_flag_exists: true
  calendar_writes_are_request_based_and_not_claimed_completed_without_approval: true
  FlowRecap_handoff_exists_without_running_FlowRecap: true
  missing_inputs_are_review_flags_not_blockers: true
  no_project_execution_FlowRecap_output_or_status_merge_created: true
