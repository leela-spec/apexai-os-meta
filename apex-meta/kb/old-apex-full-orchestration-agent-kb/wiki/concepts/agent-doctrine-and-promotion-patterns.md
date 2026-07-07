---
title: "Agent Doctrine and Promotion Patterns"
page_type: concept
kb_slug: "old-apex-full-orchestration-agent-kb"
concept_slug: "agent-doctrine-and-promotion-patterns"
source_refs:
  - source_id: "phase1-rerun-batch01"
    source_path: "apex-meta/kb/old-apex-full-orchestration-agent-kb/ingest-analysis/batch01-agent-kb-architecture.analysis.md"
    source_pointer: "concepts_extracted; source_grounded_claims"
    source_storage_mode: "copy_into_kb"
  - source_id: "phase1-rerun-batch04"
    source_path: "apex-meta/kb/old-apex-full-orchestration-agent-kb/ingest-analysis/batch04-reusable-patterns-and-migration.analysis.md"
    source_pointer: "concepts_extracted"
    source_storage_mode: "copy_into_kb"
updated_at: "2026-07-06T22:45:00+02:00"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Agent Doctrine and Promotion Patterns

## Adaptive Ranked Source Set

```yaml
ranked_source_set:
  tier_1:
    - source: "batch01-agent-kb-architecture.analysis.md"
      supports: "five-file scaffold, compact ESSENCE, candidate-only learning"
    - source: "batch04-reusable-patterns-and-migration.analysis.md"
      supports: "migration-safe reuse and promotion boundaries"
  tier_2:
    - source: "AGENT_KB_INDEX.md"
      supports: "scaffold convention"
    - source: "Hygiene Clean ESSENCE"
      supports: "candidate/truth vocabulary"
```

## Macro Synthesis

Agent doctrine becomes reliable when role knowledge is compact, source-preserving, and promotion-gated. The old KB pattern prevents useful notes from becoming accepted doctrine without review.

## Meso Synthesis

The pattern has four parts: compact role surface, supporting practice/mistake/template files, candidate-only learning queue, and owner-validator separation.

## Micro Synthesis

```yaml
key_claims:
  - claim_id: OKB-DOCTRINE-001
    claim: "The five-file scaffold is a reusable doctrine pattern."
    source_pointer: "AGENT_KB_INDEX.md / Scaffold convention"
    confidence: high
    claim_label: raw_source
  - claim_id: OKB-DOCTRINE-002
    claim: "Candidate learning does not become accepted truth by storage location."
    source_pointer: "AGENT_KB_INDEX.md / LEARNING_QUEUE convention"
    confidence: high
    claim_label: raw_source
  - claim_id: OKB-DOCTRINE-003
    claim: "Owner-validator separation prevents self-validation."
    source_pointer: "AGENT_KB_INDEX.md / Agent KB root map"
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

Use this concept for candidate promotion, doctrine packaging, reusable skill scaffolds, and role-memory design.

## Uncertainty / Raw Source Triggers

Reopen raw scaffold files before creating a new package standard or treating a candidate item as accepted doctrine.
