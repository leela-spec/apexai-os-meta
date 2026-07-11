# model-usage-log Package Manifest

```yaml
package_manifest:
  package_name: model-usage-log
  package_path: ".claude/skills/model-usage-log/"
  package_type: claude_skill_minimal_interface_package
  status: interface_package_present
  primary_role: >
    Capture compact post-execution model/surface usage deltas and roll them up
    into advisory usage summaries for future APEX planning.

  scope:
    owns:
      - model_usage_delta
      - usage_summary
      - planned_vs_actual_usage_record
      - route_reuse_or_avoid_signal
      - missing_usage_data_degraded_behavior
    references_without_owning:
      - FlowRecap packet outputs
      - PreCapNextDay usage context
      - AIRouting recommendations and planned usage budgets
      - operator usage notes
    explicitly_does_not_own:
      - routing_recommendation_packet
      - routing_decision
      - planned_usage_budget
      - AI_surface_inventory
      - monthly_quota_map
      - provider pricing truth
      - current provider or product limit truth
      - project_status_delta
      - status merge packet
      - calendar events
      - runtime metering
      - automation or cron execution

  artifact_flow:
    upstream_sources:
      - flow_recap_packet_or_raw_flow_dump
      - planned_usage_budget_or_routing_recommendation_packet
      - flow_prompt_pack
      - operator_usage_note
    package_outputs:
      - model_usage_delta
      - usage_summary
    downstream_consumers:
      - PreCapNextDay
      - FlowRecap review
      - AIRouting review context
      - operator planning review

  validation_policy:
    advisory_only: true
    non_blocking_for_FlowRecap: true
    non_blocking_for_StatusMerge: true
    non_blocking_for_PreCapNextDay: true
    missing_usage_evidence_allowed: true
    missing_usage_evidence_degrades_confidence: true
    quota_or_pricing_claims_require_explicit_source: true
    exact_model_claims_require_operator_or_artifact_evidence: true
```

## Package Files

```yaml
files:
  - path: ".claude/skills/model-usage-log/SKILL.md"
    role: skill_entrypoint
    status: created
    required: true
    notes: >
      Minimal invocation contract and procedure. Must keep package advisory and
      non-blocking.

  - path: ".claude/skills/model-usage-log/references/model-usage-delta-contract.md"
    role: reference_contract
    status: created
    required: true
    provides:
      - model_usage_delta_schema
      - planned_vs_actual_usage_record_rules
      - missing_usage_data_degraded_behavior
      - route_reuse_or_avoid_signal_values

  - path: ".claude/skills/model-usage-log/references/usage-summary-contract.md"
    role: reference_contract
    status: created
    required: true
    provides:
      - usage_summary_schema
      - route_signal_rollup_rules
      - usage_summary_degraded_behavior
      - next_PreCapNextDay_usage_context_shape

  - path: ".claude/skills/model-usage-log/templates/model-usage-delta-template.md"
    role: operator_template
    status: created
    required: true
    provides:
      - copy_paste_model_usage_delta_skeleton
      - degraded_behavior_block
      - confidence_block

  - path: ".claude/skills/model-usage-log/examples/apex-minimal-model-usage-example.md"
    role: example
    status: created
    required: true
    provides:
      - synthetic_usage_candidate
      - sample_low_confidence_model_usage_delta
      - sample_mini_usage_summary
```

## Source Inspection Register

```yaml
source_inspection_register:
  inspected_sources:
    - path: ".claude/Claude.md"
      relevance: apex_package_index_and_global_forbidden_actions
      status: inspected
    - path: ".claude/skills/PrecapNextDay/references/usage-tracking-dependency-contract.md"
      relevance: PreCapNextDay_usage_boundary
      status: inspected
    - path: ".claude/skills/PrecapNextDay/references/flow-prompt-pack-contract.md"
      relevance: flow_prompt_pack_boundary
      status: inspected
    - path: ".claude/skills/AIRouting/ai-routing-and-usage-tracking-SKILL.md"
      relevance: AIRouting_boundary
      status: inspected
    - path: ".claude/skills/AIRouting/ai-routing-and-usage-tracking-package-manifest.md"
      relevance: AIRouting_manifest_and_usage_delta_reference
      status: inspected
    - path: "apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-skill-design/sources/operator-supplied/notes/Claude_Skill_Package_BestPractice_Handover.md"
      relevance: claude_skill_package_structure
      status: inspected
    - path: "apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-skill-design/sources/operator-supplied/notes/Claude_Skill_PromptFlow_Design_Guidance_v1.md"
      relevance: promptflow_and_skill_design_guidance
      status: inspected

  source_gaps:
    - expected_path: ".claude/skills/flow-recap/references/flow-recap-packet-contract.md"
      status: present
      package_behavior: reference_flow_recap_artifact_names_without_redefining_schema
      resolution: resolved_by_live_main_inspection
    - expected_path: ".claude/skills/flow-recap/references/project-status-delta-contract.md"
      status: present
      package_behavior: do_not_define_project_status_delta
      resolution: resolved_by_live_main_inspection
    - expected_path: ".claude/skills/AIRouting/package-manifest.md"
      status: alternate_path_inspected
      alternate_inspected: ".claude/skills/AIRouting/ai-routing-and-usage-tracking-package-manifest.md"
```

## Invocation Fit

```yaml
invoke_when:
  - FlowRecap or operator notes include actual model/surface usage evidence.
  - A planned usage budget exists and post-execution actual usage should be compared against it.
  - The operator wants a compact route reuse or avoid signal for future planning.
  - Usage evidence is missing but the absence itself should be recorded as low-confidence learning.

avoid_when:
  - The task is to choose a model before execution.
  - The task is to define or update quota maps.
  - The task is to claim current provider pricing or current product limits.
  - The task is to execute prompts, automate runs, schedule work, or mutate project status.
  - The task belongs to AIRouting, FlowRecap, PreCapNextDay, ProjectStatus, or project-kb-manager.
```

## Completion Gates

```yaml
completion_gates:
  entrypoint_exists:
    path: ".claude/skills/model-usage-log/SKILL.md"
    required_before_package_complete: true
    current_status: present
  model_usage_delta_contract_exists: true
  usage_summary_contract_exists: true
  model_usage_delta_template_exists: true
  minimal_example_exists: true
  package_manifest_exists: true
  package_remains_minimal: true
  no_external_runtime_added: true
  no_quota_or_pricing_truth_claims_added: true
  no_project_management_schema_replacement: true
```


## Promoted Operator Templates

```yaml
operator_templates:
  - artifact_id: J8
    path: .claude/skills/model-usage-log/templates/usage-learning-card-template.md
    purpose: Retained Step 4 operator template
    read_when: operator_requests_template
```
