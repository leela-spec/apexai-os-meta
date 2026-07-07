---
title: "Migration Safety Patterns"
page_type: concept
kb_slug: "old-apex-full-orchestration-agent-kb"
concept_slug: "migration-safety-patterns"
source_refs:
  - source_id: "phase1-rerun-batch04"
    source_path: "apex-meta/kb/old-apex-full-orchestration-agent-kb/ingest-analysis/batch04-reusable-patterns-and-migration.analysis.md"
    source_pointer: "claims A04-C001-A04-C007; tensions"
    source_storage_mode: "copy_into_kb"
updated_at: "2026-07-06T22:45:00+02:00"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Migration Safety Patterns

## Adaptive Ranked Source Set

```yaml
ranked_source_set:
  tier_1:
    - source: "batch04-reusable-patterns-and-migration.analysis.md"
      supports: "migration patterns and historical evidence boundaries"
    - source: "semantic-continuation-after-lint-closure.md"
      supports: "old-path evidence discipline"
```

## Macro Synthesis

Migration safety means preserving reusable doctrine without importing old implementation assumptions. The safe unit is a verified pattern, not an old path or role name.

## Meso Synthesis

Migration requires three classifications: reusable pattern, historical evidence, and current authority. Only the third can guide active changes, and it requires current verification.

## Micro Synthesis

```yaml
key_claims:
  - claim_id: OKB-MIGSAFE-001
    claim: "The old role taxonomy is useful evidence but not automatically the current permanent role set."
    source_pointer: "batch04 / contradiction A04-T001"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: OKB-MIGSAFE-002
    claim: "Old paths are evidence until current authority is independently established."
    source_pointer: "semantic continuation report / historical path authority safety"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: OKB-MIGSAFE-003
    claim: "Reusable patterns include compact doctrine scaffolds, route contracts, evidence-based closure, and internal-mode containment."
    source_pointer: "batch04 / concepts_extracted"
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

Use this concept for deciding what to preserve, what to rewrite, what to verify, and what to leave historical.

## Uncertainty / Raw Source Triggers

Reopen raw sources and current repo files before converting a historical pattern into a current implementation.
