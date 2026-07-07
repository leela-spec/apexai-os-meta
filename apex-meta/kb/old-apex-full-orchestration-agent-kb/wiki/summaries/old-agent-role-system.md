---
title: "Old Agent Role System"
page_type: summary
kb_slug: "old-apex-full-orchestration-agent-kb"
summary_slug: "old-agent-role-system"
source_refs:
  - source_id: "phase1-rerun-batch02"
    source_path: "apex-meta/kb/old-apex-full-orchestration-agent-kb/ingest-analysis/batch02-agent-roles-and-doctrine.analysis.md"
    source_pointer: "source_grounded_claims A02-C001-A02-C009"
    source_storage_mode: "copy_into_kb"
updated_at: "2026-07-06T22:45:00+02:00"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Old Agent Role System

## Adaptive Ranked Source Set

```yaml
ranked_source_set:
  tier_1:
    - source: "AGENT_KB_INDEX.md"
      supports: "role roster, owner-validator map, working-surface boundaries"
      reopen_raw_source_when: "mapping old roles to current Apex responsibilities"
    - source: "batch02-agent-roles-and-doctrine.analysis.md"
      supports: "rerun role claims, concepts, entities, tensions"
      reopen_raw_source_when: "checking claim-to-role alignment"
  tier_2:
    - source: "alfred/ESSENCE.md"
      supports: "intake boundary"
    - source: "meta_ops/ESSENCE.md"
      supports: "orchestration boundary"
    - source: "meta_strategy/ESSENCE.md"
      supports: "recommendation boundary"
    - source: "meta_detective/ESSENCE.md"
      supports: "validation boundary"
    - source: "special_ops__ai_handling_routing/ESSENCE.md"
      supports: "routing boundary"
    - source: "special_ops__hygiene_clean/ESSENCE.md"
      supports: "structural QA boundary"
```

## Macro Synthesis

The old role system is a boundary map. It is useful for designing role separation, but it is not a direct plan for current Apex roles.

## Meso Synthesis

The system separates intake, orchestration, strategy, validation, routing, structural QA, KB lifecycle, information architecture, and prompt/workflow design. Each lane includes both positive ownership and explicit non-ownership. The non-ownership fields are load-bearing because they prevent role drift.

## Micro Synthesis

```yaml
micro_claims:
  - claim_id: OKB-ROLE-001
    claim: "Alfred owns intake and route framing, but not later system control."
    source_pointer: "alfred/ESSENCE.md / Owns and Does not own"
    confidence: high
    claim_label: raw_source
  - claim_id: OKB-ROLE-002
    claim: "Meta Ops owns orchestration and sequencing, but not validation or direct canon mutation."
    source_pointer: "meta_ops/ESSENCE.md / Owns and Does not own"
    confidence: high
    claim_label: raw_source
  - claim_id: OKB-ROLE-003
    claim: "Meta Detective validates and challenges, but does not implement fixes or mutate accepted truth."
    source_pointer: "meta_detective/ESSENCE.md / Agent boundary and Core constraints"
    confidence: high
    claim_label: raw_source
  - claim_id: OKB-ROLE-004
    claim: "Internal modes are lenses inside Meta Detective, not separate agents."
    source_pointer: "meta_detective/APPENDIX_INTERNAL_MODES.md / Doctrine statement"
    confidence: high
    claim_label: raw_source
```

## Routes Here

Use this page for questions about role separation, old role names, whether a capability should be a role or checklist, or how owner/validator relationships were modeled.

## Uncertainty / Raw Source Triggers

Reopen raw role files before turning any old role into a current Apex skill, workflow, subagent, or other active surface. Role names remain historical evidence unless current authority is separately established.
