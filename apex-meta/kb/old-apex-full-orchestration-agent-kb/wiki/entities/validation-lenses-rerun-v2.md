---
title: "Validation Lenses Rerun V2"
page_type: entity
kb_slug: "old-apex-full-orchestration-agent-kb"
entity_slug: "validation-lenses-rerun-v2"
source_refs:
  - source_id: "phase1-rerun-batch02"
    source_path: "apex-meta/kb/old-apex-full-orchestration-agent-kb/ingest-analysis/batch02-agent-roles-and-doctrine.analysis.md"
    source_pointer: "entities_extracted"
    source_storage_mode: "copy_into_kb"
  - source_id: "accepted-validation-appendix"
    source_path: "apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/meta_detective/APPENDIX_INTERNAL_MODES.md"
    source_pointer: "Status; Mode map; Standard validation flow"
    source_storage_mode: "copy_into_kb"
updated_at: "2026-07-07T09:00:00+02:00"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
canonical_replacement_for: "wiki/entities/meta-detective-internal-modes.md"
---

# Validation Lenses Rerun V2

## Adaptive Ranked Source Set

```yaml
ranked_source_set:
  tier_1:
    - source: "meta_detective/APPENDIX_INTERNAL_MODES.md"
      supports: "accepted validation lens doctrine"
    - source: "batch02-agent-roles-and-doctrine.analysis.md"
      supports: "entity extraction and role classification"
```

## Macro Synthesis

The validation lenses are accepted doctrine inside one historical validation role. They are not a separate current role set by default.

## Meso Synthesis

The lenses cover source review, logic review, boundary review, risk review, and verdict synthesis. The reusable pattern is specialization without expanding every lens into a permanent role.

## Micro Synthesis

```yaml
validation_lenses:
  source_review:
    purpose: "source authority and evidence sufficiency"
  logic_review:
    purpose: "contradictions and unsupported conclusions"
  boundary_review:
    purpose: "role drift and authority confusion"
  risk_review:
    purpose: "failure scenario and stop-condition pressure"
  verdict_synthesis:
    purpose: "combine findings into one bounded verdict"
```

## Routes Here

Use this page when deciding whether a validation capability should remain a checklist, become wiki doctrine, or be considered for later implementation.

## Uncertainty / Raw Source Triggers

Reopen the accepted appendix before changing the status of any validation lens.
