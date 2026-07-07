# Next PreCap Handoff Context Contract

## Contract Role

```yaml
next_precap_handoff_context_contract:
  artifact_name: next_PreCapNextDay_input_context
  file_role: status_merge_reference_contract
  package: status-merge
  purpose: >
    Define the compact downstream context seed that StatusMerge may produce for
    the next PreCapNextDay run after reviewing accepted, rejected, deferred, and
    conflicting recap-derived deltas. This artifact is a planning seed, not a
    next_day_plan, not a project KB durable write, and not an autonomous trigger.

  ownership:
    owns:
      - next_PreCapNextDay_input_context
      - compact_next_daily_planning_seed
      - updated_project_focus_view
      - active_next_actions_view
      - blocker_digest
      - unresolved_operator_decisions_view
      - usage_summary_ref_view
      - evidence_refs_for_next_planning
      - handoff_validation_status
    must_not_own:
      - next_day_plan_schema
      - flow_packet_schema
      - flow_prompt_pack_schema
      - project_kb_durable_schema
      - current_project_status_overview_schema
      - weekly_plan_packet_schema
      - calendar_write_schema
      - model_usage_delta_schema
      - usage_summary_schema
      - runtime_triggering
      - automatic_status_overwrite

  upstream_owner:
    source_status_merge_packet: status_merge_packet

  downstream_consumer:
    primary: PreCapNextDay
    secondary:
      - PreCapWeek
      - project-kb-manager
      - ProjectStatus

  global_rules:
    compact_seed_only: true
    PreCapNextDay_must_still_create_the_plan: true
    project_kb_manager_remains_durable_write_boundary: true
    unresolved_conflicts_become_operator_review_flags: true
    usage_context_is_reference_only: true
    evidence_refs_must_be_preserved: true
    no_runtime_or_auto_trigger: true
    no_calendar_write: true
```

## Source Authority Inspection

```yaml
source_authority:
  inspected_sources:
    - path: .claude/Claude.md
      status: inspected
      relevant_finding: >
        The orchestration registry places StatusMerge behind operator gate G5 and
        forbids auto-triggering skills, cron or scheduler creation, calendar
        auto-events, and unconfirmed state overwrite.
    - path: .claude/skills/project-kb-manager/SKILL.md
      status: inspected
      relevant_finding: >
        project-kb-manager owns durable project KB updates and next PreCap context
        writes when such writes are accepted by the operator.
    - path: .claude/skills/project-kb-manager/references/project-schema.md
      status: inspected
      relevant_finding: >
        durable project record fields, types, registries, and consumed recap
        records remain owned by the project KB schema.
    - path: .claude/skills/project-kb-manager/references/apex-orchestration-state-packet-contract.md
      status: inspected
      relevant_finding: >
        apex_orchestration_state_packet is a compact handoff view that may be
        referenced, not redefined or overwritten by this package.
    - path: .claude/skills/ProjectStatus/project-status-overview_SKILL_v3.md
      status: inspected
      relevant_finding: >
        ProjectStatus owns current_project_status_overview and does not own
        status_merge or next-day planning artifacts.
    - path: .claude/skills/flow-recap/references/flow-recap-packet-contract.md
      status: inspected
      relevant_finding: >
        FlowRecap candidate deltas are candidate-only and must be reconciled by a
        downstream merge interface before any durable project state proposal.
    - path: .claude/skills/status-merge/references/status-merge-packet-contract.md
      status: created_in_this_package
      relevant_finding: >
        status_merge_packet owns next_PreCapNextDay_input_context as a compact
        planning seed while keeping durable project writes proposal-gated and
        project-kb-manager-boundary-safe.
    - path: apex-meta/kb/claude-code-orchestration-design/wiki/concepts/status-merge-packet.md
      status: inspected
      relevant_finding: >
        StatusMerge produces updated status, conflict notes, and next-context seed
        after accepted recap deltas are reviewed.

  source_gap_register:
    - path: .claude/skills/flow-recap/references/project-status-delta-contract.md
      status: present
      handling: Use flow_recap_packet candidate_project_status_delta references only; do not define a separate durable delta schema here.
    - path: .claude/skills/model-usage-log/references/usage-summary-contract.md
      status: present
      handling: Keep usage_summary_ref Reference only; the usage summary schema remains owned by model-usage-log.
```

## Schema: next_PreCapNextDay_input_context

```yaml
next_PreCapNextDay_input_context:
  type: object
  required:
    - context_id
    - created_or_updated_at
    - source_status_merge_packet_ref
    - updated_project_focus
    - active_next_actions
    - blockers
    - unresolved_operator_decisions
    - usage_summary_ref
    - evidence_refs
    - confidence
    - validation_status

  fields:
    context_id:
      type: string
      format: next_precap_context_<YYYY_MM_DD>_<short_slug>
      required: true

    created_or_updated_at:
      type: string
      format: YYYY-MM-DD
      required: true

    source_status_merge_packet_ref:
      type: string
      ref: status_merge_packet.merge_packet_id
      required: true
      note: The context must be traceable to exactly one status_merge_packet source.

    updated_project_focus:
      type: list
      item_ref: updated_project_focus_item
      min_items: 0
      max_items: 12
      required: true
      note: Compact list of project focus changes proposed by StatusMerge.

    active_next_actions:
      type: list
      item_ref: active_next_action_item
      min_items: 0
      max_items: 24
      required: true
      note: Candidate next actions for PreCapNextDay input, not a generated next_day_plan.

    blockers:
      type: list
      item_ref: blocker_item
      min_items: 0
      max_items: 16
      required: true
      note: Blockers must include source evidence or operator decision requirements when available.

    unresolved_operator_decisions:
      type: list
      item_ref: unresolved_operator_decision
      min_items: 0
      max_items: 16
      required: true
      note: Conflicts and unresolved choices must remain visible to the next planning run.

    usage_summary_ref:
      type: string_or_null
      ref: usage_summary
      required: true
      note: Reference only. The usage summary schema is not owned by status-merge.

    evidence_refs:
      type: list
      item_ref: evidence_ref
      min_items: 0
      max_items: 32
      required: true
      note: Preserve refs to FlowRecap, usage summaries, previous state packets, and operator notes.

    confidence:
      type: object_ref
      ref: confidence_summary
      required: true
      note: Confidence summarizes readiness for downstream planning, not factual certainty for durable state writes.

    validation_status:
      type: string
      allowed:
        - valid
        - valid_with_warnings
        - operator_review_recommended
        - blocked_by_conflict
        - blocked_by_missing_state_owner
      required: true
```

## Minimal Supporting Object Sketches

```yaml
updated_project_focus_item:
  type: object
  required:
    - focus_id
    - project_ref
    - focus_summary
    - source_refs
    - status
  fields:
    status:
      allowed:
        - proposed_new_focus
        - continued_focus
        - reduced_focus
        - paused_focus
        - conflict_review_needed

active_next_action_item:
  type: object
  required:
    - action_id
    - project_ref
    - action_summary
    - action_status
    - source_refs
  fields:
    action_status:
      allowed:
        - ready_for_precap_consideration
        - blocked_by_operator_decision
        - blocked_by_missing_evidence
        - deferred
        - conflict_review_needed

blocker_item:
  type: object
  required:
    - blocker_id
    - blocker_summary
    - affected_project_refs
    - source_refs
    - resolution_needed
  fields:
    resolution_needed:
      allowed:
        - operator_decision
        - project_kb_manager_update
        - missing_evidence
        - conflict_resolution
        - no_action_required

unresolved_operator_decision:
  type: object
  required:
    - decision_id
    - decision_summary
    - options
    - source_refs
    - impact_if_unresolved
  fields:
    impact_if_unresolved:
      allowed:
        - blocks_next_precap
        - limits_next_precap_confidence
        - blocks_project_kb_write
        - informational_only

confidence_summary:
  type: object
  required:
    - level
    - rationale
    - limiting_factors
  fields:
    level:
      allowed:
        - high
        - medium
        - low
        - blocked
```

## Boundary Validation

```yaml
boundary_validation:
  compact_seed_only: true
  next_day_plan_not_created: true
  PreCapNextDay_schema_not_defined: true
  project_kb_manager_boundary_preserved: true
  durable_project_state_not_written: true
  ProjectStatus_schema_not_redefined: true
  flow_recap_schema_not_redefined: true
  usage_summary_schema_not_redefined: true
  unresolved_conflicts_preserved: true
  no_runtime_created: true
  no_scheduler_created: true
  no_agent_created: true
  no_calendar_write_created: true
```
