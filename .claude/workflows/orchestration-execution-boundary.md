# Orchestration Execution Boundary Workflow

```yaml
workflow_name: orchestration-execution-boundary
source_doctrine:
  - apex-meta/kb/old-apex-full-orchestration-agent-kb/wiki/summaries/old-agent-role-system.md
  - apex-meta/kb/old-apex-full-orchestration-agent-kb/wiki/entities/old-agent-roles.md
  - apex-meta/kb/old-apex-full-orchestration-agent-kb/outputs/synthesis/old-agent-kb-migration-decision-packet.md
purpose: >
  Convert the reusable parts of old Alfred and Meta Ops into a Claude-native
  workflow boundary without recreating them as permanent agents.
```

## Use when

Use this workflow when a task needs intake, route selection, execution framing, validator handoff, or approval routing.

## Boundary model

```yaml
workflow_roles:
  intake:
    owns: [operator_intent_capture, constraints, source_hierarchy, output_shape]
    does_not_own: [deep_execution, final_validation]
  route:
    owns: [target_surface_selection, owner_selection, allowed_and_forbidden_actions]
    does_not_own: [repo_mutation_without_contract, final_approval]
  execute:
    owns: [implementation_inside_allowed_surface, artifact_creation, stated_postflight]
    does_not_own: [validating_own_high_risk_work_as_final]
  validate:
    owns: [source_authority_review, contradiction_detection, risks, verdict_packet]
    does_not_own: [patching_reviewed_fix, self_approval]
  approve:
    owns: [operator_decision, authority_promotion, phase_gate_release]
    does_not_own: [silent_normalization_of_open_decisions]
```

## Procedure

1. Capture the operator request as a single mission.
2. Identify affected surfaces: KB, skill, workflow, script, repo file, runtime config, or operator doctrine.
3. Assign the task lane: intake, route, execute, validate, approve, or stop.
4. Declare what the lane owns and does not own.
5. If execution is allowed, define exact target paths, allowed writes, forbidden writes, and postflight checks.
6. If validation is needed, use `source-authority-and-verdict-packet` and keep validator/executor separation explicit.
7. Preserve operator decisions rather than resolving them implicitly.

## Stop conditions

```yaml
stop_conditions:
  - target_surface_is_ambiguous
  - repo_write_paths_are_not_exact
  - validator_is_expected_to_apply_and_final_approve_own_fix
  - old_role_name_is_being_promoted_to_current_agent_without_decision
  - advisory_route_is_being_treated_as_execution_authority
  - runtime_config_or_provider_policy_change_lacks_operator_authority
```

## Completion criteria

```yaml
completion_criteria:
  - task_lane_is_explicit
  - owns_and_does_not_own_are_explicit
  - execution_paths_are_exact_when_repo_writes_are_involved
  - validation_route_is_separate_for_high_risk_work
  - next_owner_or_operator_gate_is_visible
```
