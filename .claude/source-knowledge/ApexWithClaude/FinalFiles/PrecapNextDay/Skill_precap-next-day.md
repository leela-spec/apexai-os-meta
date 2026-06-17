```markdown
---
name: precap-next-day
description: Use this skill when the operator asks to create, compile, or review a resilient next-day orchestration plan from partial planning, project, recap, calendar, prompt, workflow, or usage context. Produces next_day_plan-centered planning artifacts. Does not execute project work, run FlowRecap, merge status, or require complete inputs.
---

# PreCap Next Day

## Skill Contract

skill_contract:
  primary_output: next_day_plan
  output_role: resilient_daily_orchestration_compiler
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
  fixed_daily_flows:
    canonical_source: references/flow-packet-contract.md
  sprint_policy:
    canonical_source: references/flow-packet-contract.md
  dependency_interfaces:
    prompt_engineering: references/prompt-engineering-dependency-contract.md
    usage_tracking: references/usage-tracking-dependency-contract.md
    workflow_process_validation: references/workflow-process-validation-contract.md
    calendar_write: references/calendar-event-write-contract.md
  schema_authority:
    next_day_plan: references/daily-plan-output-contract.md
    flow_packet: references/flow-packet-contract.md
    flow_prompt_pack: references/flow-prompt-pack-contract.md
    calendar_event_write_request: references/calendar-event-write-contract.md
    usage_tracking_plan: references/usage-tracking-dependency-contract.md
    workflow_process_validation_summary: references/workflow-process-validation-contract.md
    validation_status: references/validation-checklist.md

## Supporting Files

supporting_files:
  - path: references/input-intake-and-resilience-contract.md
    read_when:
      - validating_input_resilience
      - missing_inputs_present
      - bootstrap_mode_needed
      - degraded_mode_needed
  - path: references/daily-plan-output-contract.md
    read_when:
      - creating_next_day_plan
      - validating_daily_plan_output
      - building_generated_file_index
  - path: references/flow-packet-contract.md
    read_when:
      - creating_flow_packets
      - compressing_or_omitting_flow
      - preparing_raw_flow_dump
      - preparing_FlowRecap_handoff
  - path: references/flow-prompt-pack-contract.md
    read_when:
      - creating_flow_prompt_packs
      - validating_prompt_pack_structure
      - bridging_prompt_execution_packets
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
  - path: package-manifest.md
    read_when:
      - operator_inspects_package_structure
      - validating_package_files

## Procedure

1. Load the best available context, treat missing inputs as confidence and review signals, and select the safest execution mode.
2. Create the day frame by defining the next_day_plan, daily intent, source-context summary, review status, generated-file index, and operator review flags.
3. Represent each fixed daily flow as planned, compressed, skipped, or explicitly omitted with reasons.
4. Create or define one flow_packet for each represented flow, including sprint intent, expected outputs, raw-flow-dump preparation, skipped-flow-marker handling, and FlowRecap handoff context.
5. Create or define one flow_prompt_pack for each represented flow, referencing prompt-engineering-owned prompt packets and marking degraded generic prompt mode when prompt dependencies are missing.
6. Apply prompt-engineering, usage-tracking, and workflow-process dependency interfaces when available, and preserve dependency gaps as degraded-mode review flags instead of redefining upstream schemas.
7. Prepare calendar workflow-block write requests only when relevant, keeping all calendar mutation pending until explicit operator approval and tool confirmation exist.
8. Validate the complete output against the validation checklist, apply the matching failure-mode correction if any check fails, and present unresolved uncertainty as operator_review_flags.

## Failure Modes

failure_modes:
  no_inputs:
    trigger: No usable planning, project, recap, calendar, workflow, prompt, or usage context is supplied.
    correction: Run bootstrap_mode, create a low-confidence next_day_plan, define starter F1-F4 flow coverage, and add operator review flags.
  missing_project_status:
    trigger: Current project status and detailed project state are missing or stale.
    correction: Use operator intent, recaps, skipped markers, or bootstrap assumptions, and mark project-state confidence as low.
  prompt_engineering_unavailable:
    trigger: Prompt-engineering references or prompt packet generation inputs are missing.
    correction: Use degraded_generic_prompt_mode, reference the missing dependency, and mark prompt optimization for operator review.
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
    - next_day_plan
  required_or_defined_when_relevant:
    - flow_packet
    - flow_prompt_pack
    - calendar_event_write_request
    - usage_tracking_plan_or_usage_tracking_summary
    - raw_flow_dump_template
    - skipped_flow_marker_template
    - FlowRecap_handoff_block
    - operator_review_flags
  must_not_include:
    - Do not include full schemas owned by reference files.
    - Do not include prompt-engineering prompt_packet schemas or final prompt doctrine.
    - Do not include workflow-process taxonomies as inline enums.
    - Do not include routing, quota, planned-budget, or usage-delta schemas.
    - Do not include FlowRecap output or project status merge output.

## Completion Gate

completion_gate:
  next_day_plan_exists: true
  fixed_flows_are_represented_or_explicitly_omitted: true
  represented_flows_have_flow_packet_references: true
  represented_flows_have_flow_prompt_pack_references: true
  prompt_packs_are_ready_or_marked_degraded_with_review_flags: true
  usage_tracking_hooks_exist_or_degraded_usage_review_flag_exists: true
  calendar_writes_are_request_based_and_not_claimed_completed_without_approval: true
  FlowRecap_handoff_exists_without_running_FlowRecap: true
  missing_inputs_are_review_flags_not_blockers: true
  no_project_execution_FlowRecap_output_or_status_merge_created: true
```