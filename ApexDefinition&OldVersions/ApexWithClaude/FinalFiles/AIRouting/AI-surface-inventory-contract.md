# AI Surface Inventory Contract

## Contract

```yaml
AI_surface_inventory_contract:
  artifact_name: AI_surface_inventory
  file_role: ai_routing_reference_contract
  purpose: >
    Define the canonical inventory structure for AI surfaces available to the
    operator. This file owns AI_surface_inventory records, abstract surface
    classes, capability classes, access modes, availability status, scarcity
    hints, and verification status. It does not own routing decisions, monthly
    quota maps, planned usage budgets, usage deltas, prompt schemas, workflow
    taxonomies, pricing claims, model rankings, or exact product limits.

  ownership:
    owns:
      - AI_surface_inventory
      - AI_surface_record
      - surface_class_taxonomy
      - capability_class_taxonomy
      - access_mode_taxonomy
      - availability_status_taxonomy
      - verification_status_taxonomy
      - scarcity_hint_fields
      - inventory_update_rules
    must_not_own:
      - routing_decision_schema
      - monthly_quota_map_schema
      - planned_usage_budget_schema
      - usage_delta_schema
      - routing_recommendation_packet_schema
      - prompt_packet_schema
      - workflow_stage_taxonomy
      - process_stage_taxonomy
      - exact_pricing
      - exact_product_limits
      - exact_model_rankings
      - benchmark_claims

  volatility_policy:
    stable_inventory_claims_allowed:
      - operator_declared_surface_names
      - abstract_surface_classes
      - access_modes
      - broad_capability_classes
      - broad_cost_or_scarcity_hints
      - operator_notes
    volatile_claims_require_current_verification:
      - exact_pricing
      - exact_usage_limits
      - exact_model_availability
      - exact_context_window
      - exact_benchmark_position
      - provider_product_status
    forbidden_without_verification:
      - current_best_model_ranking
      - exact_monthly_allowance
      - exact_API_price
      - exact_provider_limit
```

## Surface Class Taxonomy

```yaml
surface_class_taxonomy:
  allowed:
    frontier_subscription_chat:
      definition: "High-capability chat interface available through a subscription surface."
      typical_use: "Daily high-value reasoning, synthesis, critique, planning, and prompt design."

    frontier_subscription_agent:
      definition: "Subscription-based agentic execution surface with bounded tool or task capability."
      typical_use: "Multi-step bounded tasks, file navigation, structured execution, and iterative artifact work."

    frontier_deep_research:
      definition: "Research-oriented surface intended for source-grounded synthesis."
      typical_use: "Current information checks, source comparison, evidence-heavy planning, and uncertainty reduction."

    frontier_code_agent:
      definition: "Code-oriented agent or assistant surface for repository or file-generation work."
      typical_use: "Code review, file generation, implementation planning, and technical validation."

    long_context_subscription_chat:
      definition: "Subscription chat surface suited for large supplied context."
      typical_use: "Long document digestion, comparison, extraction, and context-preserving synthesis."

    supplemental_api:
      definition: "API-accessed model surface used as a supplement rather than default daily flow engine."
      typical_use: "Low-risk support generation, batch transformation, classification, and cost-sensitive helper tasks."

    low_cost_batch_api:
      definition: "Metered API surface optimized for inexpensive high-volume transformations."
      typical_use: "Bulk formatting, tagging, lightweight extraction, and repetitive low-reasoning work."

    local_or_offline_tool:
      definition: "Local tool, script, or offline utility that supports AI work without provider inference."
      typical_use: "Parsing, deterministic validation, file conversion, and mechanical checks."

    manual_operator_surface:
      definition: "Human-only operator action or decision surface."
      typical_use: "Approvals, account checks, subscription decisions, calendar commitments, and final priority choices."

    operator_defined:
      definition: "Operator-supplied surface class not yet covered by this taxonomy."
      typical_use: "Temporary extension pending contract update."
```

## Capability Class Taxonomy

```yaml
capability_class_taxonomy:
  allowed:
    - high_end_reasoning
    - source_grounded_research
    - long_context_digestion
    - code_file_generation
    - code_review_or_debugging
    - visual_or_multimodal_analysis
    - creative_generation
    - structured_synthesis
    - validation_and_critique
    - workflow_or_process_design
    - fast_batch_transformation
    - low_cost_supplemental_generation
    - deterministic_local_processing
    - operator_decision
    - operator_defined

access_mode_taxonomy:
  allowed:
    - chat_ui
    - deep_research_mode
    - agent_run_mode
    - code_agent_mode
    - api_call
    - local_tool
    - manual_operator_action
    - operator_defined

provider_family_taxonomy:
  allowed:
    - ChatGPT
    - Claude
    - Gemini
    - OpenRouter_later
    - local_tool
    - manual_operator
    - other_provider
    - provider_unspecified
    - operator_defined
```

## Status Taxonomies

```yaml
surface_status_taxonomies:
  availability_status:
    allowed:
      - available
      - unavailable
      - operator_subscription_missing
      - tool_unavailable
      - account_or_permission_unclear
      - deprecated_or_paused
      - unknown_requires_verification

  verification_status:
    allowed:
      - verified_current
      - operator_supplied_unverified
      - stale_requires_review
      - not_verified
      - volatile_claim_removed
      - blocked_by_missing_operator_decision

  cost_class_hint:
    allowed:
      - no_incremental_cost_subscription
      - scarce_subscription_quota
      - API_metered_low
      - API_metered_medium
      - API_metered_high
      - local_no_provider_cost
      - manual_operator_time
      - unknown_requires_verification

  scarcity_class:
    allowed:
      - abundant
      - limited
      - scarce
      - manual_only
      - unknown_requires_verification

  spend_policy:
    allowed:
      - use_freely_when_fit_is_good
      - use_deliberately_for_high_value_work
      - reserve_for_high_impact_high_risk_work
      - use_only_when_low_cost_surface_is_sufficient
      - avoid_until_verified
      - operator_decision_required
```

## Schema: AI_surface_inventory

```yaml
AI_surface_inventory:
  type: object
  required:
    - inventory_id
    - inventory_status
    - created_or_updated_at
    - surface_records
    - validation_status

  fields:
    inventory_id:
      type: string
      format: "AI_surface_inventory_<short_slug>"
      required: true

    inventory_status:
      type: string
      allowed:
        - draft
        - current
        - partial
        - stale_requires_review
        - blocked_by_missing_operator_decision
      required: true

    created_or_updated_at:
      type: string
      format: "YYYY-MM-DD"
      required: true

    inventory_scope:
      type: string
      allowed:
        - operator_personal_AI_surfaces
        - project_specific_AI_surfaces
        - subscription_and_API_surfaces
        - operator_defined
      required: false

    surface_records:
      type: list
      item_ref: AI_surface_record
      min_items: 1
      required: true

    global_assumptions:
      type: list
      item_type: string
      required: false

    verification_notes:
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

## Schema: AI_surface_record

```yaml
AI_surface_record:
  type: object
  required:
    - surface_id
    - surface_name
    - provider_family
    - surface_class
    - access_mode
    - capability_classes
    - cost_class_hint
    - scarcity_profile
    - availability_status
    - verification_status

  fields:
    surface_id:
      type: string
      format: "surface_<provider_or_tool>_<short_slug>"
      required: true

    surface_name:
      type: string
      required: true
      examples:
        - "ChatGPT subscription chat"
        - "Claude Code"
        - "Gemini long-context chat"
        - "OpenRouter API later"

    provider_family:
      type: string
      ref: provider_family_taxonomy.allowed
      required: true

    surface_class:
      type: string
      ref: surface_class_taxonomy.allowed
      required: true

    access_mode:
      type: string
      ref: access_mode_taxonomy.allowed
      required: true

    capability_classes:
      type: list
      item_ref: capability_class_taxonomy.allowed
      min_items: 1
      required: true

    best_fit_prompt_task_types:
      type: list
      item_type: string
      allowed:
        - research
        - synthesis
        - planning
        - coding
        - critique
        - file_generation
        - creative_generation
        - visual_briefing
        - long_context_digestion
        - validation
        - workflow_extraction
        - workflow_normalization
        - prompt_refinement
        - operator_defined
      required: false

    best_fit_work_modes:
      type: list
      item_type: string
      allowed:
        - planned_flow_session
        - supplemental_or_batch_execution
        - deep_research_session
        - agentic_file_work
        - coding_session
        - validation_pass
        - operator_defined
      required: false

    cost_class_hint:
      type: string
      ref: surface_status_taxonomies.cost_class_hint.allowed
      required: true

    scarcity_profile:
      type: object_ref
      ref: scarcity_profile
      required: true

    quota_link:
      type: object_ref
      ref: quota_link
      required: false

    routing_notes:
      type: list
      item_type: string
      required: false

    usage_capture_hints:
      type: list
      item_type: string
      required: false

    availability_status:
      type: string
      ref: surface_status_taxonomies.availability_status.allowed
      required: true

    verification_status:
      type: string
      ref: surface_status_taxonomies.verification_status.allowed
      required: true

    operator_notes:
      type: list
      item_type: string
      required: false
```

## Schema: scarcity_profile and quota_link

```yaml
scarcity_profile:
  type: object
  required:
    - monthly_quota_relevant
    - scarcity_class
    - spend_policy

  fields:
    monthly_quota_relevant:
      type: boolean
      required: true

    scarcity_class:
      type: string
      ref: surface_status_taxonomies.scarcity_class.allowed
      required: true

    spend_policy:
      type: string
      ref: surface_status_taxonomies.spend_policy.allowed
      required: true

    reset_cycle_known:
      type: boolean
      required: false

    exact_limit_known:
      type: boolean
      required: false

    exact_limit_value:
      type: string
      required: false
      rule: "Only include when verified_current; otherwise omit or set to unknown_requires_verification."

    review_note:
      type: string
      required: false

quota_link:
  type: object
  required:
    - monthly_quota_map_ref
    - planned_usage_budget_ref
    - usage_delta_ref

  fields:
    monthly_quota_map_ref:
      type: string
      nullable: true
      required: true
      rule: "Reference only; schema is owned by monthly-quota-map-contract.md."

    planned_usage_budget_ref:
      type: string
      nullable: true
      required: true
      rule: "Reference only; schema is owned by planned-usage-budget-contract.md."

    usage_delta_ref:
      type: string
      nullable: true
      required: true
      rule: "Reference only; schema is owned by usage-delta-contract.md."
```

## Inventory Update Rules

```yaml
inventory_update_rules:
  add_surface_when:
    - operator_names_new_AI_surface
    - new_subscription_or_tool_becomes_relevant
    - API_or_local_tool_is_added_for_supplemental_work
    - routing_decision_references_unknown_surface

  mark_stale_when:
    - exact_limit_or_pricing_may_have_changed
    - provider_availability_is_uncertain
    - operator_subscription_status_changed
    - surface_has_not_been_reviewed_recently_enough_for_current_routing

  remove_or_pause_surface_when:
    - operator_no_longer_has_access
    - surface_is_deprecated
    - surface_is_not_allowed_for_project_work
    - surface_was_added_as_temporary_test_only

  verification_rules:
    - "Do not infer current pricing, quota, model availability, or exact limits from memory."
    - "If a volatile claim matters for routing, require current verification before using it as decisive."
    - "If verification is missing, keep the surface usable only with verification_status: not_verified or stale_requires_review."
    - "Stable abstract classes may remain even when exact provider details are unknown."
```

## Validation Rules

```yaml
AI_surface_inventory_validation:
  required_checks:
    inventory_has_at_least_one_surface: true
    every_surface_has_unique_surface_id: true
    every_surface_has_surface_class: true
    every_surface_has_access_mode: true
    every_surface_has_capability_class: true
    every_surface_has_cost_class_hint: true
    every_surface_has_scarcity_profile: true
    every_surface_has_availability_status: true
    every_surface_has_verification_status: true
    volatile_claims_are_marked_or_removed: true
    routing_decision_schema_not_defined_here: true
    monthly_quota_schema_not_defined_here: true
    exact_model_ranking_not_claimed: true
    exact_pricing_not_claimed_without_verification: true

  operator_review_flags:
    - unknown_surface_access
    - stale_surface_claim
    - missing_cost_class_hint
    - missing_scarcity_profile
    - missing_quota_link_for_scarce_surface
    - volatile_claim_needs_verification
    - provider_or_tool_no_longer_available
    - operator_subscription_decision_needed
```

## Minimal Example

```yaml
minimal_AI_surface_inventory_example:
  inventory_id: AI_surface_inventory_operator_current
  inventory_status: partial
  created_or_updated_at: "YYYY-MM-DD"
  inventory_scope: operator_personal_AI_surfaces
  surface_records:
    - surface_id: surface_chatgpt_subscription_chat
      surface_name: "ChatGPT subscription chat"
      provider_family: ChatGPT
      surface_class: frontier_subscription_chat
      access_mode: chat_ui
      capability_classes:
        - high_end_reasoning
        - structured_synthesis
        - validation_and_critique
      best_fit_prompt_task_types:
        - synthesis
        - planning
        - critique
        - prompt_refinement
      best_fit_work_modes:
        - planned_flow_session
        - validation_pass
      cost_class_hint: scarce_subscription_quota
      scarcity_profile:
        monthly_quota_relevant: true
        scarcity_class: limited
        spend_policy: use_deliberately_for_high_value_work
        reset_cycle_known: false
        exact_limit_known: false
        review_note: "Exact current usage limits require verification before quota-sensitive routing."
      quota_link:
        monthly_quota_map_ref: null
        planned_usage_budget_ref: null
        usage_delta_ref: null
      routing_notes:
        - "Good default candidate for high-reasoning planned flow prompts when quota use is justified."
      usage_capture_hints:
        - "Capture provider_family, surface_class, task_type, and whether scarce quota was intentionally used."
      availability_status: unknown_requires_verification
      verification_status: operator_supplied_unverified

    - surface_id: surface_openrouter_api_later
      surface_name: "OpenRouter API later"
      provider_family: OpenRouter_later
      surface_class: supplemental_api
      access_mode: api_call
      capability_classes:
        - low_cost_supplemental_generation
        - fast_batch_transformation
      best_fit_prompt_task_types:
        - validation
        - workflow_extraction
        - workflow_normalization
      best_fit_work_modes:
        - supplemental_or_batch_execution
      cost_class_hint: API_metered_low
      scarcity_profile:
        monthly_quota_relevant: false
        scarcity_class: unknown_requires_verification
        spend_policy: avoid_until_verified
        reset_cycle_known: false
        exact_limit_known: false
        review_note: "Final model mapping is intentionally TODO."
      quota_link:
        monthly_quota_map_ref: null
        planned_usage_budget_ref: null
        usage_delta_ref: null
      routing_notes:
        - "Do not use as default daily flow reasoning engine."
        - "Keep as supplemental, low-reasoning, cost-sensitive candidate only."
      usage_capture_hints:
        - "Capture API use later through automated logs or manual usage_delta."
      availability_status: unknown_requires_verification
      verification_status: not_verified
  global_assumptions:
    - "Surface inventory is operator-maintained and may be partial."
  verification_notes:
    - "No exact pricing, model limits, or rankings are claimed in this inventory."
  operator_review_flags:
    - unknown_surface_access
    - missing_quota_link_for_scarce_surface
  validation_status: operator_review_recommended
```
