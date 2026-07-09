---
title: "Old Output Comparison Policy"
page_type: concept
kb_slug: claude-code-orchestration-design
run_id: max-run-20260709
status: new_parallel_compile
source_policy: source_preserving
legacy_output_policy: old_pages_for_comparison_only
confidence: high
claim_label: source_backed_summary
source_refs:
  - source_path: apex-meta/kb/claude-code-orchestration-design/wiki/index.md
  - source_path: apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-completion-report.md
---

# Old Output Comparison Policy

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source: apex-meta/kb/claude-code-orchestration-design/wiki/index.md
    rationale: "Lists legacy compiled pages and old compile state."
    coverage: "Old page inventory and LLM summary."
  - rank: 2
    source: apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-completion-report.md
    rationale: "Legacy Phase 1 comparison source."
    coverage: "Old batches, source coverage, concepts, and entities."
```

## Macro / Meso / Micro

### Macro

Old outputs are historical compiled artifacts, not raw source truth.

### Meso

Use them to compare coverage and discover concepts, but do not overwrite them during the max-run compile.

### Micro

All max-run outputs live under versioned folders so an operator can compare before deletion or promotion.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Old wiki pages must not be overwritten by this max-run compile."
    source_pointer: user prompt plus apex-meta/kb/claude-code-orchestration-design/wiki/index.md
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "How should old wiki outputs be compared to new max-run outputs?"
    leads_to: apex-meta/kb/claude-code-orchestration-design/wiki/concepts/max-run-20260709/old-output-comparison-policy.md
    rationale: "Comparison and promotion route."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Reopen before deleting, moving, or promoting old pages."
    source_pointer: apex-meta/kb/claude-code-orchestration-design/wiki/index.md
    proposed_handling: ask_operator
```
