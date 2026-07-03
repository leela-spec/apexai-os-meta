# Apex KB Knowledge Promotion Rules

```yaml
artifact_name: apex_kb_knowledge_promotion_rules
package_path: .claude/skills/apex-kb/references/knowledge-promotion-rules.md
source_doctrine:
  - apex-meta/kb/old-apex-full-orchestration-agent-kb/wiki/summaries/old-agent-kb-architecture.md
  - apex-meta/kb/old-apex-full-orchestration-agent-kb/wiki/concepts/agent-doctrine-and-promotion-patterns.md
  - apex-meta/kb/old-apex-full-orchestration-agent-kb/wiki/entities/reusable-artifact-families.md
  - apex-meta/kb/old-apex-full-orchestration-agent-kb/outputs/synthesis/old-agent-kb-migration-decision-packet.md
purpose: >
  Prevent source, candidate, accepted doctrine, and runtime truth from collapsing
  into one layer. Learning queues and candidate notes are never runtime truth
  until promoted through owner/validator or operator gate.
```

## State model

```yaml
knowledge_states:
  raw_source:
    meaning: "Preserved source or durable pointer with source path/hash or no-hash reason."
    may_drive_runtime: false
  candidate:
    meaning: "Possible lesson, pattern, claim, or artifact not yet validated."
    may_drive_runtime: false
  reviewed_candidate:
    meaning: "Candidate checked for source support, contradiction, and target-surface fit."
    may_drive_runtime: false
  accepted_doctrine:
    meaning: "Source-backed or operator-approved guidance stored in wiki, reference, workflow, or skill form."
    may_drive_runtime: true_if_target_surface_authorizes_it
  runtime_truth:
    meaning: "Current active instruction, script behavior, config, or repo source of truth."
    may_drive_runtime: true
  deprecated:
    meaning: "Rejected, superseded, or historical material preserved for traceability."
    may_drive_runtime: false
```

## Promotion gate

```yaml
promotion_gate:
  required_for:
    - candidate_to_accepted_doctrine
    - accepted_doctrine_to_runtime_truth
    - old_role_name_to_current_agent_or_skill
    - old_runtime_path_to_current_target_path
    - score_scale_normalization
  requires:
    - source_refs_or_operator_decision
    - owner_route
    - validator_route_for_medium_or_high_risk
    - target_form
    - negative_ownership_boundary
    - rollback_or_deprecation_path
```

## Operator decisions that must not be inferred

- Whether old role names remain historical entities or become generalized Claude-native concepts.
- Whether mixed EVD/IMP/RSK score scales should be normalized.
- Whether any Meta Detective internal mode should become a subagent.
- Which migration patterns become skills, workflows, deterministic checks, or operator gates.

## Completion criteria

```yaml
completion_criteria:
  - candidate_material_is_labeled
  - accepted_doctrine_has_source_or_operator_decision
  - runtime_truth_change_has_explicit_target_surface
  - medium_or_high_risk_promotion_has_validator_route
  - unresolved_operator_decisions_remain_visible
```
