---
title: "Old Agent Roles"
page_type: entity
kb_slug: "old-apex-full-orchestration-agent-kb"
entity_slug: "old-agent-roles"
source_refs:
  - source_id: "phase1-rerun-batch02"
    source_path: "apex-meta/kb/old-apex-full-orchestration-agent-kb/ingest-analysis/batch02-agent-roles-and-doctrine.analysis.md"
    source_pointer: "entities_extracted"
    source_storage_mode: "copy_into_kb"
updated_at: "2026-07-06T22:45:00+02:00"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Old Agent Roles

## Adaptive Ranked Source Set

```yaml
ranked_source_set:
  tier_1:
    - source: "batch02-agent-roles-and-doctrine.analysis.md"
      supports: "role extraction and boundaries"
    - source: "AGENT_KB_INDEX.md"
      supports: "role roster and owner-validator table"
  tier_2:
    - source: "role ESSENCE files"
      supports: "individual owns / does-not-own boundaries"
```

## Macro Synthesis

The old roles are historical entities and reusable boundary examples. They are not automatically current Apex roles.

## Meso Synthesis

The role set separates intake, orchestration, strategy, validation, routing, structure, knowledge placement, information design, and prompt/workflow design.

## Micro Synthesis

```yaml
entities:
  alfred:
    role: "operator intake and route brief"
    source_pointer: "alfred/ESSENCE.md"
  meta_ops:
    role: "orchestration and sequencing"
    source_pointer: "meta_ops/ESSENCE.md"
  meta_strategy:
    role: "options and recommendation packets"
    source_pointer: "meta_strategy/ESSENCE.md"
  meta_detective:
    role: "validation and challenge"
    source_pointer: "meta_detective/ESSENCE.md"
  special_ops__ai_handling_routing:
    role: "advisory route selection"
    source_pointer: "special_ops__ai_handling_routing/ESSENCE.md"
  special_ops__hygiene_clean:
    role: "structural QA and closure evidence"
    source_pointer: "special_ops__hygiene_clean/ESSENCE.md"
```

## Routes Here

Use this entity page for role lookup, owner/validator questions, and historical role references.

## Uncertainty / Raw Source Triggers

Reopen raw role files before mapping any historical role to current Apex implementation.
