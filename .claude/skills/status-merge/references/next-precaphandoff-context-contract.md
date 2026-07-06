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
        The core loop places next_PreCapNextDay after APSU/StatusMerge and
        requires manual operator trigger and validation. The repo behavior rules
        forbid auto-triggering skills and unconfirmed state overwrite.
    - path: .claude/skills/status-merge/references/status-merge-packet-contract.md
      status: created_in_this_package
      relevant_finding: >
        status_merge_packet owns next_PreCapNextDay_input_context as a compact
        planning seed while keeping durable project writes proposal-gated and
        project-kb-manager-boundary-safe.
    - path: .claude/skills/PrecapNextDay/Skill_precap-next-day.md
      status: inspected
      relevant_finding: >
        PreCapNextDay produces next_day_plan-centered planning artifacts, treats
        missing inputs as confidence/review signals, and must not execute work,
        run FlowRecap, or merge status.
    - path: .claude/skills/project-kb-manager/SKILL.md
      status: inspected
      relevant_finding: >
        project-kb-manager is the compact durable project KB authority for
        project status, milestone state, FlowRecap consumption, and
        PreCapNextDay context.
    - path: .claude/skills/project-kb-manager/references/apex-orchestration-state-packet-contract.md
      status: inspected
      relevant_finding: >
        apex_orchestration_state_packet provides weekly and next-day planning
        views but must not become a weekly plan, next-day plan, FlowRecap output,
        or status merge.
    - path: .claude/skills/project-kb-manager/templates/apex-orchestration-state-packet-template.md
      status: inspected
      relevant_finding: >
        Operator-facing planning handoffs should use compact cards, source
        status, missing-input markers, and confidence notes rather than exposing
        full durable project data.
    - path: .claude/skills/model-usage-log/references/model-usage-delta-contract.md
      status: inspected
      relevant_finding: >
        Usage artifacts are advisory and non-blocking; exact quota, pricing, or
        product-limit claims require explicit evidence.

  source_gap_register:
    - path: .claude/skills/model-usage-log/references/usage-summary-contract.md
      status: missing
      handling: >
        Keep usage_summary_ref optional/opaque. Do not define usage_summary
        schema in this handoff contract.
    - path: .claude/skills/flow-recap/references/project-status-delta-contract.md
      status: missing
      handling: >
        Do not infer project_status_delta schema. Carry only evidence-backed
        accepted/deferred/conflicting delta summaries from status_merge_packet.
```

## Schema: next_PreCapNextDay_input_context

```yaml
next_PreCapNextDay_input_context:
  type: object
  role: compact_seed_for_next_daily_planning
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
      format: next_PreCapNextDay_input_context_<YYYY_MM_DD>_<short_slug>
      required: true

    created_or_updated_at:
      type: string
      format: YYYY-MM-DD
      required: true

    source_status_merge_packet_ref:
      type: object_ref
      ref: status_merge_packet
      required: true
      note: Reference only. status_merge_packet schema is owned by status-merge.

    updated_project_focus:
      type: object_ref
      ref: updated_project_focus_view
      required: true
      note: Compact planning view only; not current_project_status_overview.

    active_next_actions:
      type: list
      item_ref: active_next_action_seed
      required: true
      min_items: 0
      max_items: 12

    blockers:
      type: list
      item_ref: blocker_seed
      required: true
      min_items: 0
      max_items: 12

    unresolved_operator_decisions:
      type: list
      item_ref: unresolved_operator_decision_seed
      required: true
      min_items: 0
      max_items: 12

    usage_summary_ref:
      type: object_ref_or_null
      ref: usage_summary
      required: true
      nullable: true
      note: >
        Opaque optional reference. usage_summary_schema is not owned here and may
        be missing until model-usage-log provides a usage-summary contract.

    evidence_refs:
      type: list
      item_type: object_ref
      required: true
      min_items: 0
      note: Preserve refs used to justify focus, actions, blockers, and decisions.

    confidence:
      type: string
      allowed:
        - high
        - medium
        - low
        - unknown
      required: true

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

## Supporting Object Sketches

```yaml
updated_project_focus_view:
  type: object
  required:
    - focus_status
    - focus_summary
    - project_refs
    - change_basis
  fields:
    focus_status:
      type: string
      allowed:
        - updated_from_accepted_deltas
        - unchanged
        - partial
        - blocked_by_conflict
        - unknown
    focus_summary:
      type: string
      required: true
      note: One compact paragraph or card-ready sentence for PreCapNextDay.
    project_refs:
      type: list
      item_type: object_ref
      required: true
    change_basis:
      type: string
      allowed:
        - accepted_delta_candidates
        - operator_review
        - previous_state_only
        - conflict_review_only
        - insufficient_evidence

active_next_action_seed:
  type: object
  required:
    - action_id
    - action_summary
    - source_refs
    - suggested_owner
    - planning_relevance
    - readiness
  fields:
    suggested_owner:
      type: string
      allowed:
        - operator
        - PreCapNextDay
        - project-kb-manager
        - ProjectStatus
        - status-merge
        - unknown
    planning_relevance:
      type: string
      allowed:
        - candidate_for_next_flow
        - supporting_context
        - followup_after_operator_decision
        - blocked
    readiness:
      type: string
      allowed:
        - ready
        - needs_operator_decision
        - needs_evidence
        - blocked
        - deferred

blocker_seed:
  type: object
  required:
    - blocker_id
    - blocker_summary
    - affected_refs
    - severity
    - proposed_unblock_path
  fields:
    severity:
      type: string
      allowed:
        - high
        - medium
        - low
        - unknown

unresolved_operator_decision_seed:
  type: object
  required:
    - decision_id
    - decision_summary
    - options
    - needed_before
    - evidence_refs
  fields:
    needed_before:
      type: string
      allowed:
        - next_PreCapNextDay
        - project_kb_manager_write
        - ProjectStatus_refresh
        - future_weekly_plan
        - not_blocking
```

## Validation Rules

```yaml
next_precap_handoff_context_validation_rules:
  required_checks:
    context_id_matches_format: true
    source_status_merge_packet_ref_present: true
    updated_project_focus_present: true
    active_next_actions_list_present: true
    blockers_list_present: true
    unresolved_operator_decisions_list_present: true
    usage_summary_ref_present_or_null_with_gap_flag: true
    evidence_refs_present: true
    confidence_allowed_value: true
    validation_status_allowed_value: true

  boundary_checks:
    does_not_create_next_day_plan: true
    does_not_define_flow_packet_or_prompt_pack: true
    does_not_mutate_project_kb: true
    does_not_redefine_current_project_status_overview: true
    does_not_create_calendar_write: true
    does_not_auto_trigger_PreCapNextDay: true
    unresolved_conflicts_are_operator_review_flags: true

  warning_conditions:
    - confidence_low_or_unknown
    - evidence_refs_empty
    - usage_summary_ref_null
    - active_next_actions_empty
    - unresolved_operator_decisions_nonempty
    - source_status_merge_packet_validation_not_valid

  blocking_conditions:
    - source_status_merge_packet_ref_missing
    - updated_project_focus_blocked_by_conflict
    - missing_state_owner_required_for_next_planning
    - context_attempts_to_create_next_day_plan
    - context_attempts_to_write_project_kb_directly
```

## Non-Goals

```yaml
non_goals:
  - Do not create a next_day_plan.
  - Do not create flow_packet or flow_prompt_pack artifacts.
  - Do not mutate project KB records or consumed recap registries.
  - Do not redefine usage_summary, model_usage_delta, or project_status_delta schemas.
  - Do not create calendar_event_write_request or calendar events.
  - Do not auto-trigger PreCapNextDay, PreCapWeek, FlowRecap, project-kb-manager, or runtime execution.
```
