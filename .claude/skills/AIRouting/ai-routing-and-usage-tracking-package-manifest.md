# FILE: .claude/skills/ai-routing-and-usage-tracking/package-manifest.md

```markdown id="ar10mf"
# AI Routing and Usage Tracking Package Manifest

```yaml
package_manifest:
  package_name: ai-routing-and-usage-tracking
  package_path: ".claude/skills/ai-routing-and-usage-tracking/"
  primary_output: routing_recommendation_packet
  package_role: ai_surface_routing_usage_budget_and_feedback_index

  package_file_index:
    - path: ".claude/skills/ai-routing-and-usage-tracking/SKILL.md"
      purpose: "Skill entrypoint for AI routing, usage budgeting, routing recommendations, and usage feedback."
      read_when: [skill_invocation, entrypoint_review]
    - path: ".claude/skills/ai-routing-and-usage-tracking/references/AI-surface-inventory-contract.md"
      purpose: "Defines stable AI surface inventory fields without volatile provider claims."
      read_when: [inventory_available, checking_surface_fit]
    - path: ".claude/skills/ai-routing-and-usage-tracking/references/monthly-quota-map-contract.md"
      purpose: "Defines quota, scarcity, cycle, and operator-maintained limit fields."
      read_when: [quota_context_available, scarcity_check_needed]
    - path: ".claude/skills/ai-routing-and-usage-tracking/references/routing-decision-contract.md"
      purpose: "Defines one routing decision for a prompt or task."
      read_when: [creating_routing_decision, validating_route]
    - path: ".claude/skills/ai-routing-and-usage-tracking/references/planned-usage-budget-contract.md"
      purpose: "Defines planned usage allocation across prompts, flows, and scarce modes."
      read_when: [planning_usage_budget, next_day_influence_needed]
    - path: ".claude/skills/ai-routing-and-usage-tracking/references/usage-delta-contract.md"
      purpose: "Defines actual versus planned usage capture and feedback signals."
      read_when: [capturing_usage_delta, flow_recap_usage_feedback]
    - path: ".claude/skills/ai-routing-and-usage-tracking/references/routing-recommendation-packet-contract.md"
      purpose: "Defines advisory routing recommendations and tradeoff options."
      read_when: [creating_recommendation_packet, operator_tradeoff_needed]
    - path: ".claude/skills/ai-routing-and-usage-tracking/references/cost-class-and-scarcity-rules.md"
      purpose: "Defines cost classes, scarcity classes, and high-end reasoning trigger rules."
      read_when: [classifying_cost_or_scarcity, high_end_reasoning_check]
    - path: ".claude/skills/ai-routing-and-usage-tracking/examples/starter-usage-routing-example.md"
      purpose: "Shows one compact usage-routing example without adding schema authority."
      read_when: [operator_requests_example, first_manual_test]
    - path: ".claude/skills/ai-routing-and-usage-tracking/package-manifest.md"
      purpose: "Indexes package files, dependencies, boundaries, and acceptance checks."
      read_when: [package_review, file_inventory_check]

  dependency_map:
    consumes_from_prompt_engineering:
      - prompt_task_type
      - expected_output_type
      - provider_target
      - prompt_quality_review
    returns_to_prompt_engineering:
      - routing_decision
      - provider_rationale
      - quota_rationale
      - usage_tracking_tags
    interfaces_with_workflow_process_design:
      - task_complexity
      - workflow_value
      - risk_level
      - expected_output_type
    feeds_PreCapNextDay:
      - routing_recommendation_packet
      - planned_usage_budget
      - next_day_influence

  package_boundaries:
    must_do:
      - recommend_AI_surface_and_usage_class
      - plan_budget_and_scarcity_use
      - capture_actual_usage_delta
      - surface_operator_tradeoffs
      - influence_next_day_planning
    must_not_do:
      - execute_prompts
      - create_project_plans
      - create_calendar_events
      - finalize_OpenRouter_model_mapping
      - override_operator_choice
      - duplicate_prompt_or_workflow_schemas

  acceptance_checks:
    all_10_files_indexed: true
    manifest_is_index_only: true
    schema_definitions_not_duplicated: true
    volatile_provider_claims_excluded: true
    package_interfaces_are_explicit: true
```
```

---

# VALIDATION - FILE-SPECIFIC CHECKS

- [ ] Manifest indexes all 10 `ai-routing-and-usage-tracking` package files.
- [ ] Manifest stays lightweight and index-only.
- [ ] Manifest uses `path`, `purpose`, and `read_when` for file index entries.
- [ ] Manifest does not duplicate reference schemas.
- [ ] Manifest shows package interfaces only, not implementation logic.
- [ ] Manifest does not finalize OpenRouter model mapping.

---

# NEXT PROMPT

Paste this next:
> Prompt WPD1:
> Create exactly one file.
>
> # FILE: .claude/skills/workflow-process-design/SKILL.md
>
> File type: SKILL.md entrypoint.
> Schema ownership: references only; do not define full reference schemas here.
> Context carry-forward:
> - all generated prompt-engineering files
> - all generated ai-routing-and-usage-tracking files
> - shared convergence layer: next_day_plan / flow_prompt_pack / prompt_execution_packet
>
> Structure constraints:
> - Use exact SKILL.md section order: frontmatter, H1, Skill Contract, Supporting Files, Procedure, Failure Modes, Output Requirements, Completion Gate.
> - Frontmatter only has name and description.
> - Description begins with "Use this skill when".
> - Supporting files must use YAML path/read_when.
> - Procedure must be 5-8 steps.
> - Failure modes must be YAML and no more than 8.
> - Completion Gate must be YAML booleans.
>
> Content constraints:
> - Package name: workflow-process-design.
> - Primary output: workflow_process_validation_summary.
> - Role: classify workflow stages, process stages, sprint structures, expected output types, workflow records, and prompt-to-workflow alignment.
> - Must interface with prompt-engineering and ai-routing-and-usage-tracking.
> - Must not generate provider-specific prompt rules, route models or quotas, execute project work, create final daily plans, override operator decisions, or create new permanent agents.
>
> File-specific checks:
> - [ ] Description starts with "Use this skill when".
> - [ ] Skill boundaries separate workflow/process authority from prompt and routing authority.
> - [ ] Supporting file list uses read_when conditions.
> - [ ] Procedure is compact and action-grained.

## Promoted Operator Templates

```yaml
operator_templates:
  - artifact_id: J12
    path: .claude/skills/AIRouting/ai-routing-card-template.md
    purpose: Operator-facing presentation template
    read_when: operator_requests_template
```
