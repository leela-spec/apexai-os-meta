---
name: status-merge
description: Use this skill when you need to review validated FlowRecap-derived candidate deltas, compare them against previous project state references, surface conflicts before acceptance, produce a proposal-only status_merge_packet, and prepare compact next_PreCapNextDay_input_context without directly mutating durable project KB state.
---

# status-merge

## Purpose

Use `status-merge` as the APEX loop interface for turning validated recap-derived candidates into an operator-reviewable merge proposal.

This skill does **not** write durable project state. It does **not** replace `project-kb-manager`, `ProjectStatus`, `flow-recap`, `model-usage-log`, `PreCapNextDay`, `PreCapWeek`, `apex-plan`, `apex-sync`, or `apex-session`.

## Use When

- A validated `flow_recap_packet` or recap-derived candidate set needs review against previous project state refs.
- Candidate deltas need to be sorted into accepted, rejected, deferred, or conflicting groups.
- The operator needs a compact merge proposal before any durable project KB update.
- Conflicts must be surfaced before acceptance.
- A compact `next_PreCapNextDay_input_context` seed is needed for later daily planning.

## Do Not Use When

- The user asks to create the next-day plan itself. Use `PreCapNextDay`.
- The user asks to generate or validate a FlowRecap packet. Use `flow-recap`.
- The user asks to mutate durable project KB records directly. Use `project-kb-manager` after operator confirmation.
- The user asks for current project status overview generation. Use `ProjectStatus`.
- The task requires runtime execution, scheduler behavior, cron, agents, auto-triggering, or autonomous overwrite.

## Inputs

```yaml
inputs:
  required:
    - source_flow_recap_refs
    - previous_state_refs
  optional:
    - source_usage_summary_refs
    - operator_review_constraints
    - merge_scope
    - known_conflict_refs
    - evidence_refs
```

## Outputs

```yaml
outputs:
  primary:
    - status_merge_packet
  included_sections:
    - merge_proposal
    - accepted_delta_candidates
    - rejected_or_deferred_delta_candidates
    - conflict_notes
    - proposed_project_kb_update
    - updated_all_project_status_packet
    - next_PreCapNextDay_input_context
    - operator_review_flags
    - validation_status
```

## Procedure

1. **Load source boundaries.** Read this file first, then load the packet contract, next-PreCap context contract, template, example, or manifest only when their `read_when` conditions apply.

2. **Normalize inputs as references.** Treat FlowRecap outputs, usage summaries, previous state, and evidence as refs. Do not redefine their schemas and do not treat candidate deltas as accepted durable state.

3. **Classify candidate deltas.** Sort every recap-derived item into accepted, rejected, deferred, or conflict-noted buckets. Preserve evidence refs and confidence for each item.

4. **Surface conflicts before acceptance.** Put conflicts and operator decisions before accepted deltas. If a conflict blocks safe interpretation or owner routing, mark the packet `blocked_by_conflict` or `operator_review_recommended`.

5. **Draft proposal-only state views.** Produce `proposed_project_kb_update` and `updated_all_project_status_packet` as review/proposal views only. Durable project KB writes remain `project-kb-manager` owned and operator-gated.

6. **Prepare next planning seed.** Produce `next_PreCapNextDay_input_context` as compact context for later daily planning. Do not create a `next_day_plan` and do not trigger PreCapNextDay.

7. **Run the completion gate.** Verify ownership boundaries, source gaps, conflict visibility, proposal-only write status, and absence of runtime/overwrite behavior before returning the packet.

## Validation Status Selection

```yaml
validation_status_rules:
  valid: Use only when required refs are present, conflicts are absent or non-blocking, and all boundaries pass.
  valid_with_warnings: Use when the packet is usable but has non-blocking gaps, low-confidence items, or opaque refs.
  operator_review_recommended: Use when human judgment is needed before owner-safe write routing.
  blocked_by_conflict: Use when unresolved conflicts prevent safe acceptance or next-context generation.
  blocked_by_missing_state_owner: Use when the correct owner for a proposed update is absent or unclear.
```

## Boundary Rules

```yaml
boundary_rules:
  project_kb_manager_boundary_preserved: true
  project_status_schema_not_redefined: true
  flow_recap_packet_schema_not_redefined: true
  model_usage_schema_not_redefined: true
  usage_summary_schema_not_redefined: true
  apex_orchestration_state_packet_schema_not_redefined: true
  next_day_plan_not_created: true
  weekly_plan_not_created: true
  calendar_write_not_created: true
  runtime_not_created: true
  automatic_status_overwrite_forbidden: true
  durable_write_status_default: proposal_only
```

## Failure Modes

```yaml
failure_modes:
  - trigger: Candidate deltas are treated as durable accepted state.
    correction: Reclassify them as proposal-only and route durable updates through the owning package.

  - trigger: Conflict notes appear after accepted deltas or are omitted.
    correction: Move conflicts before acceptance and update validation_status accordingly.

  - trigger: proposed_project_kb_update performs or implies direct mutation.
    correction: Mark it proposal_only and require operator confirmation plus project-kb-manager handling.

  - trigger: next_PreCapNextDay_input_context becomes a next_day_plan.
    correction: Reduce it to compact seed context and defer plan creation to PreCapNextDay.

  - trigger: Missing usage-summary or project-status-delta contract is filled by inference.
    correction: Record a source gap and keep external schema refs opaque.

  - trigger: updated_all_project_status_packet replaces ProjectStatus output.
    correction: Mark it as a review view only and preserve ProjectStatus ownership.

  - trigger: Runtime, scheduler, cron, agent, or auto-trigger behavior is introduced.
    correction: Remove runtime behavior; this package is an interface-only skill.

  - trigger: Evidence refs or confidence are missing from candidate classifications.
    correction: Add refs and confidence, or downgrade validation_status.
```

## Supporting Files

```yaml
supporting_files:
  - path: .claude/skills/status-merge/references/status-merge-packet-contract.md
    read_when:
      - defining_status_merge_packet_schema
      - validating_required_packet_fields
      - checking_merge_scope_values
      - auditing_project_kb_manager_boundary

  - path: .claude/skills/status-merge/references/next-precaphandoff-context-contract.md
    read_when:
      - defining_next_PreCapNextDay_input_context
      - validating_compact_daily_planning_seed
      - separating_context_seed_from_next_day_plan
      - handling_usage_summary_ref_gaps

  - path: .claude/skills/status-merge/templates/status-merge-packet-template.md
    read_when:
      - producing_operator_facing_status_merge_packet
      - drafting_merge_review_cards
      - separating_accepted_rejected_deferred_and_conflicting_deltas
      - preparing_next_PreCapNextDay_input_context_output

  - path: .claude/skills/status-merge/examples/apex-minimal-status-merge-example.md
    read_when:
      - needing_minimal_APEX_example
      - checking_one_accepted_delta_one_conflict_pattern
      - confirming_no_project_kb_mutation_pattern
      - showing_valid_with_warnings_packet_shape

  - path: .claude/skills/status-merge/package-manifest.md
    read_when:
      - auditing_package_inventory
      - checking_source_authority_and_gaps
      - verifying_non_runtime_scope
      - confirming_completion_status
```

## Source Gap Handling

```yaml
source_gap_handling:
  known_gaps:
    - path: .claude/skills/flow-recap/references/project-status-delta-contract.md
      handling: Do not infer or redefine project_status_delta schema; carry only proposal summaries and refs.
    - path: .claude/skills/model-usage-log/references/usage-summary-contract.md
      handling: Keep usage_summary_ref opaque and nullable; do not define usage_summary schema here.
```

## Completion Gate

```yaml
completion_gate:
  source_files_inspected_or_gaps_recorded: true
  package_path_created: true
  status_merge_packet_contract_created: true
  next_precap_context_contract_created: true
  template_created: true
  apex_minimal_example_created: true
  manifest_created: true
  SKILL_md_created_with_valid_frontmatter: true
  project_kb_manager_boundary_preserved: true
  conflicts_are_surfaced_before_acceptance: true
  no_automatic_status_overwrite_created: true
  next_PreCapNextDay_input_context_is_clear: true
  no_runtime_execution_created: true
  no_calendar_write_created: true
  no_next_day_plan_created: true
```
