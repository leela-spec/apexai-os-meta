# Model Usage Delta Contract

```yaml
model_usage_delta_contract:
  artifact_name: model_usage_delta_contract
  file_role: model_usage_log_reference_contract
  package_path: ".claude/skills/model-usage-log/"
  purpose: >
    Define the minimal advisory model_usage_delta artifact produced after a
    planned flow has execution evidence or explicit missing-usage evidence.
    This contract compares planned AI usage intent with actual observed or
    operator-supplied usage notes, then returns a non-blocking reuse-or-avoid
    signal for future planning.

  ownership:
    owns:
      - model_usage_delta
      - planned_vs_actual_usage_record
      - route_reuse_or_avoid_signal
      - usage_confidence_flags
      - missing_usage_data_degraded_behavior
    must_not_own:
      - routing_recommendation_packet_schema
      - AI_surface_inventory_schema
      - monthly_quota_map_schema
      - provider_pricing_truth
      - current_product_limit_truth_without_verification
      - prompt_packet_schema
      - flow_recap_packet_schema
      - project_status_delta_schema
      - status_merge_packet_schema
      - project_kb_schema
      - runtime_usage_metering
      - automated_quota_tracking

  global_rules:
    advisory_only: true
    non_blocking_for_FlowRecap: true
    non_blocking_for_StatusMerge: true
    actual_usage_evidence_may_be_missing: true
    missing_actual_usage_requires_low_confidence: true
    quota_or_pricing_claims_require_explicit_source: true
    route_schema_referenced_not_redefined: true
    flow_recap_schema_referenced_not_redefined: true
    no_runtime_metering_or_automation: true
```

## Source Inspection Register

```yaml
source_inspection_register:
  inspected:
    - path: ".claude/Claude.md"
      status: present
      relevance: >
        Declares ModelUsageLog as a missing skill with input artifact
        flow_recap_packet and output artifact model_usage_delta. Also defines
        the manual operator-gated loop and forbids automatic scheduling or
        unconfirmed state overwrites.
    - path: ".claude/skills/PrecapNextDay/references/usage-tracking-dependency-contract.md"
      status: present
      relevance: >
        Establishes PreCapNextDay usage planning boundaries, including no exact
        provider pricing or current product-limit claims without verification,
        and no actual usage delta before execution.
    - path: ".claude/skills/PrecapNextDay/references/flow-prompt-pack-contract.md"
      status: present
      relevance: >
        Confirms flow_prompt_pack owns routing_usage_summary and FlowRecap
        preparation references while not owning usage_delta, routing schemas, or
        quota maps.
    - path: ".claude/skills/AIRouting/ai-routing-and-usage-tracking-SKILL.md"
      status: present
      relevance: >
        Confirms AIRouting owns routing_decision, planned_usage_budget,
        usage_tracking_tags, and routing_recommendation_packet, and treats exact
        current pricing/product limits as volatile claims requiring verification.
    - path: ".claude/skills/AIRouting/ai-routing-and-usage-tracking-package-manifest.md"
      status: present_as_alternate_manifest_path
      relevance: >
        Confirms AIRouting package index and boundaries, including route and
        quota authority. The requested package-manifest.md path was not present.
    - path: "apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-skill-design/sources/operator-supplied/notes/Claude_Skill_Package_BestPractice_Handover.md"
      status: present
      relevance: >
        Confirms Claude package anatomy, SKILL.md section standards, frontmatter
        rules, supporting-file map format, and token-efficiency boundaries.
    - path: "apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-skill-design/sources/operator-supplied/notes/Claude_Skill_PromptFlow_Design_Guidance_v1.md"
      status: present
      relevance: >
        Confirms YAML indentation, Use-this-skill-when trigger phrasing,
        5-to-8-step procedure grain, failure-mode limits, and YAML completion
        gate requirements.

source_gap_register:
  inspected_or_resolved:
    - path: ".claude/skills/flow-recap/references/flow-recap-packet-contract.md"
      status: present
      handling: >
        ModelUsageLog references flow_recap_packet artifacts without redefining schema.
    - path: ".claude/skills/flow-recap/references/project-status-delta-contract.md"
      status: present
      handling: >
        ModelUsageLog may preserve project_status_delta refs when supplied, without redefining schema.
  alternate_path_notes:
    - path: ".claude/skills/AIRouting/package-manifest.md"
      status: alternate_path_inspected
      impact: >
        Requested manifest path is absent; alternate AIRouting manifest was
        inspected at ai-routing-and-usage-tracking-package-manifest.md.
      degraded_behavior: reference_alternate_manifest_path_when_needed
```

## Schema: model_usage_delta

```yaml
model_usage_delta:
  type: object
  required:
    - usage_delta_id
    - artifact_name
    - execution_day
    - source_flow_recap_refs
    - planned_usage_refs
    - actual_usage_evidence
    - model_or_surface_used
    - usage_purpose
    - planned_vs_actual_summary
    - route_reuse_or_avoid_signal
    - confidence
    - validation_status

  fields:
    usage_delta_id:
      type: string
      format: "model_usage_delta_<execution_day>_<flow_id_or_short_slug>"
      required: true

    artifact_name:
      type: string
      const: model_usage_delta
      required: true

    execution_day:
      type: string
      format: "YYYY-MM-DD"
      required: true

    source_flow_recap_refs:
      type: list
      item_type: object_ref
      required: true
      min_items: 0
      note: >
        References to flow_recap_packet or related recap evidence. This contract
        does not define the FlowRecap packet schema.

    planned_usage_refs:
      type: list
      item_type: object_ref
      required: true
      min_items: 0
      allowed_ref_examples:
        - routing_recommendation_packet
        - planned_usage_budget
        - flow_prompt_pack.routing_usage_summary
        - next_day_plan.usage_tracking_plan
      note: >
        References only. Routing and budget schemas are owned by AIRouting and
        PreCapNextDay dependency contracts.

    actual_usage_evidence:
      type: object
      required: true
      fields:
        evidence_status:
          type: string
          allowed:
            - explicit_operator_supplied
            - inferred_from_transcript
            - inferred_from_artifact_metadata
            - partial
            - missing
            - unknown
          required: true
        evidence_refs:
          type: list
          item_type: object_ref
          required: false
        evidence_notes:
          type: string
          required: false
        missing_evidence_reason:
          type: string
          required: false
          nullable: true
      rule: >
        When evidence_status is missing or unknown, produce the delta anyway in
        degraded advisory mode and set confidence to low or unknown.

    model_or_surface_used:
      type: object
      required: true
      fields:
        provider_or_surface_label:
          type: string
          required: false
          nullable: true
        stable_surface_class:
          type: string
          required: false
          nullable: true
        exact_model_name:
          type: string
          required: false
          nullable: true
        exact_model_name_source:
          type: string
          required: false
          nullable: true
        verification_status:
          type: string
          allowed:
            - verified_by_operator
            - verified_by_artifact
            - inferred
            - not_supplied
            - unknown
          required: true
      rule: >
        Do not claim exact model, pricing, quota, or remaining limit values
        unless an explicit source is supplied.

    usage_purpose:
      type: string
      required: true
      examples:
        - prompt_generation
        - code_agent_run
        - deep_research
        - review_or_audit
        - recap_or_summary
        - planning
        - unknown

    planned_vs_actual_summary:
      type: object
      required: true
      fields:
        planned_route_ref:
          type: object_ref
          required: false
        planned_usage_intent:
          type: string
          required: false
        actual_usage_observed:
          type: string
          required: false
        comparison:
          type: string
          allowed:
            - matched_plan
            - cheaper_or_lighter_than_planned
            - heavier_or_scarcer_than_planned
            - different_route_used
            - planned_but_not_executed
            - executed_without_plan
            - insufficient_data
          required: true
        operator_learning_note:
          type: string
          required: false

    route_reuse_or_avoid_signal:
      type: string
      allowed:
        - reuse_route
        - avoid_route
        - use_only_for_high_value_tasks
        - insufficient_data
        - operator_review_needed
      required: true

    route_signal_rationale:
      type: string
      required: false
      note: >
        Explain why the signal was selected without redefining routing decision
        fields or claiming provider truth.

    confidence:
      type: object
      required: true
      fields:
        level:
          type: string
          allowed:
            - high
            - medium
            - low
            - unknown
          required: true
        confidence_flags:
          type: list
          item_type: string
          allowed:
            - actual_usage_evidence_missing
            - planned_usage_ref_missing
            - exact_model_unknown
            - inferred_from_context_only
            - operator_supplied_but_unverified
            - source_refs_incomplete
            - quota_or_pricing_not_verified
          required: false
        review_note:
          type: string
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

## Planned vs Actual Usage Record Rules

```yaml
planned_vs_actual_usage_record_rules:
  allowed:
    - compare planned route intent to actual usage evidence when both exist
    - mark insufficient_data when either planned or actual side is missing
    - produce advisory learning signals for future PreCapNextDay context
    - preserve operator notes even when evidence is incomplete

  forbidden:
    - Do not calculate exact provider cost without an explicit source.
    - Do not infer remaining quotas from memory or unstated assumptions.
    - Do not mutate AI_surface_inventory or monthly_quota_map.
    - Do not overwrite AIRouting routing recommendations.
    - Do not block FlowRecap, StatusMerge, or next PreCapNextDay outputs.
    - Do not redefine flow_recap_packet, project_status_delta, prompt_packet, or routing_recommendation_packet schemas.
```

## Degraded Behavior

```yaml
missing_usage_data_degraded_behavior:
  actual_usage_evidence_missing:
    output_required: true
    required_signal: insufficient_data
    confidence_level: low
    validation_status: low_confidence_auto_generated
    required_note: "Actual usage evidence missing; output is advisory only."

  planned_usage_refs_missing:
    output_required: true
    allowed_signals:
      - insufficient_data
      - operator_review_needed
    confidence_level: low
    validation_status: operator_review_recommended

  exact_model_or_surface_unknown:
    output_required: true
    model_or_surface_used:
      provider_or_surface_label: null
      stable_surface_class: provider_unspecified
      exact_model_name: null
      verification_status: unknown
    forbidden_claims:
      - exact_model_name_if_not_supplied
      - exact_provider_pricing
      - current_product_limit_truth
      - remaining_quota
```

## Minimal Valid Object Skeleton

```yaml
model_usage_delta_minimal_skeleton:
  usage_delta_id: "model_usage_delta_<YYYY-MM-DD>_<flow_id>"
  artifact_name: model_usage_delta
  execution_day: "YYYY-MM-DD"
  source_flow_recap_refs: []
  planned_usage_refs: []
  actual_usage_evidence:
    evidence_status: missing
    evidence_notes: "No explicit usage evidence supplied."
  model_or_surface_used:
    provider_or_surface_label: null
    stable_surface_class: provider_unspecified
    exact_model_name: null
    exact_model_name_source: null
    verification_status: unknown
  usage_purpose: unknown
  planned_vs_actual_summary:
    comparison: insufficient_data
    actual_usage_observed: "Unknown."
  route_reuse_or_avoid_signal: insufficient_data
  confidence:
    level: low
    confidence_flags:
      - actual_usage_evidence_missing
      - exact_model_unknown
      - source_refs_incomplete
    review_note: "Advisory only; do not use as quota truth."
  validation_status: low_confidence_auto_generated
```
