---
title: "Meta Detective Internal Modes"
page_type: entity
kb_slug: "old-apex-full-orchestration-agent-kb"
entity_slug: "meta-detective-internal-modes"
entity_type: "artifact"
source_refs:
  - source_id: "batch02-agent-roles-and-doctrine"
    source_path: "apex-meta/kb/old-apex-full-orchestration-agent-kb/ingest-analysis/batch02-agent-roles-and-doctrine.analysis.md"
    source_hash: "NA"
    source_pointer: "C006; internal mode entities"
    source_storage_mode: "copy_into_kb"
  - source_id: "batch04-reusable-patterns-and-migration"
    source_path: "apex-meta/kb/old-apex-full-orchestration-agent-kb/ingest-analysis/batch04-reusable-patterns-and-migration.analysis.md"
    source_hash: "NA"
    source_pointer: "anti-agent-sprawl-internal-modes"
    source_storage_mode: "copy_into_kb"
created_at: "2026-07-03T00:00:00Z"
updated_at: "2026-07-03T00:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - internal-mode-not-agent
  - anti-agent-sprawl-internal-modes
  - validator-executor-separation
review_flags:
  - "Do not promote every mode into a permanent agent by default."
---

# Meta Detective Internal Modes

## Identity

```yaml
entity:
  label: "Meta Detective Internal Modes"
  type: "artifact_family"
  aliases:
    - "internal validation lenses"
    - "Meta Detective appendix modes"
```

## Source-Grounded Summary

Meta Detective internal modes are validator lenses inside one adversarial validation role. They are not separate agents, separate KB roots, or runtime entities by default. Their reusable value is anti-sprawl: specialized validation behavior can be preserved as doctrine, workflow checks, or sub-processes without multiplying permanent agent identities.

```yaml
modes:
  - slug: evidence_source_verifier
    owns: [source_authority_classification, evidence_sufficiency_review, source_candidate_canon_status_check]
    not_owns: [strategy_choice, patching, KB_placement]
  - slug: contradiction_logic_auditor
    owns: [contradiction_detection, inference_jump_review, unsupported_claim_surfacing]
    not_owns: [rewriting_artifact, strategy_choice, patches]
  - slug: boundary_authority_guardian
    owns: [role_boundary_drift_detection, promotion_safety_pressure, validator_executor_separation]
    not_owns: [orchestration_control, KB_placement_ownership, structural_cleanup_execution]
  - slug: risk_failure_mode_red_teamer
    owns: [premortem_challenge, base_rate_challenge, reversibility_review, falsification_test_design]
    not_owns: [mitigation_execution, project_management, final_strategy]
  - slug: verdict_escalation_synthesizer
    owns: [verdict_synthesis, confidence_consolidation, evidence_gap_statement, escalation_recommendation]
    not_owns: [implementing_fix, applying_patch, promoting_KB_candidates]
```

## Known Relationships

```yaml
relationships:
  - "Belongs under Meta Detective doctrine rather than separate agent roots."
  - "Supports validation verdict packets and owner/validator routing."
  - "Maps to potential workflows, checklists, or subagents only when operator-approved."
```

## Evidence

```yaml
evidence:
  - source_id: batch02-agent-roles-and-doctrine
    source_pointer: "C006 and internal mode entities"
    supports: "Internal modes are lenses, not agents."
  - source_id: batch04-reusable-patterns-and-migration
    source_pointer: "C002"
    supports: "Anti-agent-sprawl pattern."
```

## Open Questions

```yaml
open_questions:
  - "Should any internal mode become a current Claude-native subagent, or should all remain wiki doctrine/checklists until a concrete need appears?"
```
