---
title: "Old Agent Roles"
page_type: entity
kb_slug: "old-apex-full-orchestration-agent-kb"
entity_slug: "old-agent-roles"
entity_type: "artifact"
source_refs:
  - source_id: "batch02-agent-roles-and-doctrine"
    source_path: "apex-meta/kb/old-apex-full-orchestration-agent-kb/ingest-analysis/batch02-agent-roles-and-doctrine.analysis.md"
    source_hash: "NA"
    source_pointer: "entities_or_roles_extracted"
    source_storage_mode: "copy_into_kb"
created_at: "2026-07-03T00:00:00Z"
updated_at: "2026-07-03T00:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - persistent-agent-role
  - negative-ownership-boundary
  - validator-like-role
  - specialist-lane
review_flags:
  - "Historical role set only; not current runtime authorization."
---

# Old Agent Roles

## Identity

```yaml
entity:
  label: "Old Agent Roles"
  type: "artifact_family"
  aliases:
    - "first-wave agent role set"
    - "managed agent KB roles"
```

## Source-Grounded Summary

The old managed agent KB identifies a first-wave role system with intake, orchestration, strategy, adversarial validation, structural QA, routing, KB lifecycle, information design, and prompt/workflow lanes. The roles are source-backed as historical doctrine entities and should not be read as current runtime authorization.

```yaml
roles:
  - slug: alfred
    classification: [persistent, routing_like, intake_like]
    owns: [operator_intake, constraint_capture, bounded_handoff_framing]
    not_owns: [execution_control, final_strategy, adversarial_validation, config_mutation]
  - slug: meta_ops
    classification: [persistent, executor_like, orchestration_like]
    owns: [orchestration, specialist_activation, sequencing, bounded_synthesis, execution_control]
    not_owns: [final_strategy, adversarial_validation, direct_canon_mutation, config_authority]
  - slug: meta_strategy
    classification: [persistent, strategy_like, recommendation_like]
    owns: [option_framing, scenario_comparison, timing_analysis, leverage_analysis, recommendation_packets]
    not_owns: [execution_control, implementation, direct_promotion, config_authority]
  - slug: meta_detective
    classification: [persistent, validator_like, adversarial_reviewer]
    owns: [source_authority_challenge, contradiction_surfacing, assumption_pressure, drift_challenge, risk_review, verdict_packets]
    not_owns: [execution, patch_application, direct_promotion, self_validation_as_final_approval]
  - slug: special_ops__knowledge_bank
    classification: [persistent, specialist_like, kb_lifecycle_like]
    owns: [source_manifesting, candidate_ledgering, appendix_architecture, KB_lifecycle_routing]
    not_owns: [final_strategy, promotion_approval, config_mutation]
  - slug: special_ops__informatics_design
    classification: [persistent, specialist_like, structure_like]
    owns: [taxonomy, terminology_stability, chunking, retrieval_clarity]
    not_owns: [domain_truth_validation, promotion_approval, orchestration_control]
  - slug: special_ops__hygiene_clean
    classification: [persistent, validator_like, structural_QA_like]
    owns: [structural_QA, pointer_integrity, stale_state_checks, closure_safety]
    not_owns: [truth_mutation, promotion_approval, strategy_authority]
  - slug: special_ops__prompts_workflows
    classification: [persistent, specialist_like, workflow_like]
    owns: [prompt_structures, workflow_stage_patterns, handoff_templates, anti_drift_promptflows]
    not_owns: [orchestration_authority, model_config_routing, KB_placement, promotion_approval]
  - slug: special_ops__ai_handling_routing
    classification: [persistent, specialist_like, routing_like]
    owns: [advisory_model_tool_posture, source_authority_checks, handoff_readiness]
    not_owns: [runtime_config_mutation, provider_policy_authority, all_agent_orchestration, final_approval]
```

## Known Relationships

```yaml
relationships:
  - "Meta Ops validates/receives orchestration and execution-control implications."
  - "Meta Detective validates/challenges strategy, evidence, contradiction, drift, and risk."
  - "Hygiene Clean owns structural QA and closure safety boundaries."
  - "Special Ops specialist lanes provide bounded capability surfaces, not global authority."
```

## Evidence

```yaml
evidence:
  - source_id: batch02-agent-roles-and-doctrine
    source_pointer: "C001 and entities_or_roles_extracted"
    supports: "Indexed first-wave role set and extracted role boundaries."
```

## Open Questions

```yaml
open_questions:
  - "Which old roles are still useful as current skills, workflows, or subagents?"
```
