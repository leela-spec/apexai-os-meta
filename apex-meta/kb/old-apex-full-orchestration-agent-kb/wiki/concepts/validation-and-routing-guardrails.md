---
title: "Validation and Routing Guardrails"
page_type: concept
kb_slug: "old-apex-full-orchestration-agent-kb"
concept_slug: "validation-and-routing-guardrails"
source_refs:
  - source_id: "phase1-rerun-batch03"
    source_path: "apex-meta/kb/old-apex-full-orchestration-agent-kb/ingest-analysis/batch03-handoffs-validation-and-risk.analysis.md"
    source_pointer: "claims A03-C001-A03-C009"
    source_storage_mode: "copy_into_kb"
updated_at: "2026-07-06T22:45:00+02:00"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Validation and Routing Guardrails

## Adaptive Ranked Source Set

```yaml
ranked_source_set:
  tier_1:
    - source: "batch03-handoffs-validation-and-risk.analysis.md"
      supports: "validation and routing synthesis"
    - source: "meta_detective/APPENDIX_INTERNAL_MODES.md"
      supports: "mode selection, verdict, confidence, standard flow"
  tier_2:
    - source: "AI Handling Routing ESSENCE"
      supports: "routing minimum"
    - source: "Hygiene Clean ESSENCE"
      supports: "closure evidence and mode lock"
```

## Macro Synthesis

Validation and routing guardrails make outputs trustworthy by forcing evidence, verdict, owner, and stop-condition clarity before a task moves to another surface.

## Meso Synthesis

The guardrail chain is: classify source authority, select a validation mode, produce a bounded verdict, then route the next action to the right owner.

## Micro Synthesis

```yaml
key_claims:
  - claim_id: OKB-GUARD-001
    claim: "Validation outputs should name evidence checked, evidence gap, stop condition, next owner, and next validator."
    source_pointer: "meta_detective/APPENDIX_INTERNAL_MODES.md / Standard validation flow"
    confidence: high
    claim_label: raw_source
  - claim_id: OKB-GUARD-002
    claim: "Routing decisions need task, non-task, output, source authority, route surface, fallback, validator, and confidence."
    source_pointer: "AI Handling Routing ESSENCE / Minimal routing card"
    confidence: high
    claim_label: raw_source
  - claim_id: OKB-GUARD-003
    claim: "Closure requires evidence, not silence or later cleanup."
    source_pointer: "Hygiene Clean ESSENCE / Operating doctrine"
    confidence: high
    claim_label: raw_source
```

## Routes Here

Use this concept for handoff review, output trust checks, routing cards, validation packets, and ambiguity resolution.

## Uncertainty / Raw Source Triggers

Reopen raw validation files when a verdict affects file edits, acceptance status, or current implementation authority.
