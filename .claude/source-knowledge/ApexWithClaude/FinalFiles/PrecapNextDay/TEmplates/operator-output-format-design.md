# Operator Output Format Design

## Role

This file defines the human-facing output layout for PreCap Next Day while preserving the existing contract ownership.

## Source contract alignment

```yaml
operator_output_format_design:
  primary_artifact: next_day_plan
  visible_format: markdown_dashboard_with_compact_yaml_blocks
  source_contracts:
    next_day_plan: references/daily-plan-output-contract.md
    flow_packet: references/flow-packet-contract.md
    flow_prompt_pack: references/flow-prompt-pack-contract.md
    calendar_event_write_request: references/calendar-event-write-contract.md
    usage_tracking_plan: references/usage-tracking-dependency-contract.md
    validation_status: references/validation-checklist.md
```

## Output layering

```yaml
output_layers:
  layer_1_main_plan:
    file: next-day-plan.md
    artifact: next_day_plan
    purpose: operator-facing command dashboard
    includes:
      - plan status
      - input context
      - day strategy summary
      - fixed flow overview
      - generated file index
      - prompt pack index
      - calendar summary
      - usage summary
      - FlowRecap preparation summary
      - operator review flags
      - completion gate
    must_not_include:
      - full flow_packet internals
      - full flow_prompt_pack internals
      - full prompt_packet schema
      - project execution results

  layer_2_flow_packets:
    file_pattern: flows/<flow_id>-flow-packet.md
    artifact: flow_packet
    purpose: per-flow execution container prepared for operator use
    includes:
      - flow identity
      - sprint plan
      - prompt pack reference
      - usage references
      - raw capture preparation
      - skipped marker shell
      - FlowRecap handoff block
    must_not_include:
      - full next_day_plan
      - flow_prompt_pack schema
      - executed work results

  layer_3_prompt_packs:
    file_pattern: prompts/<flow_id>-flow-prompt-pack.md
    artifact: flow_prompt_pack
    purpose: per-flow prompt container and prompt references
    includes:
      - prompt pack policy
      - sprint prompt sequence groups
      - prompt packet references or degraded prompt shells
      - routing/usage summary
      - workflow alignment summary
      - light capture hints
      - FlowRecap prompt preparation
    must_not_include:
      - prompt-engineering doctrine
      - routing schema
      - usage delta
      - executed prompt results

  layer_4_capture_and_handoff:
    file_pattern: capture/<flow_id>-capture-and-handoff.md
    artifacts:
      - raw_flow_dump_template
      - skipped_flow_marker_template
      - FlowRecap_handoff_block
    purpose: operator-filled execution capture after work
```

## Main plan display order

1. Plan status
2. Operator action needed
3. Input context
4. Day strategy summary
5. Flow overview table
6. Sprint overview table
7. Generated file index
8. Prompt pack index
9. Calendar write summary
10. Usage tracking summary
11. FlowRecap preparation summary
12. Operator review flags
13. Completion gate

## Table standards

### Flow overview table

| Flow | Project | Status | Goal | Sprints | Output refs | Review flags |
|---|---|---|---|---:|---|---|

### Sprint overview table

| Flow | Sprint | Sprint role | Goal | Expected output | Prompt pack ref | Capture focus | Status |
|---|---|---|---|---|---|---|---|

## No-hallucination rules

```yaml
no_hallucination_rules:
  project_status:
    rule: Do not invent current project state.
    fallback: mark missing_project_status_context.
  goals:
    rule: Only create specific goals from supplied operator intent or source artifacts.
    fallback: use operator_review_needed and low_confidence_auto_generated.
  calendar:
    rule: Do not invent exact times unless supplied by operator or calendar context.
    fallback: use review_only calendar_event_write_request.
  usage:
    rule: Do not claim remaining quota or current provider limits without verified source.
    fallback: use unknown_quota_operator_review.
  prompts:
    rule: Do not redefine prompt_packet or provider doctrine.
    fallback: create flow_prompt_pack shell with prompt_packet_ref placeholders or degraded_generic_prompt_mode.
```

## Template variants

```yaml
template_variants:
  bootstrap:
    use_when: no reliable project context exists
    status: low_confidence_auto_generated
    required_review: true
  standard:
    use_when: enough operator intent or project context exists for reviewable flow goals
    status: operator_review_recommended
    required_review: true
  calendar_constrained:
    use_when: calendar constraints compress or omit flows
    status: operator_review_recommended
    required_review: true
  prompt_heavy:
    use_when: prompt packs are the main value of the day
    status: operator_review_recommended
    required_review: true
```
