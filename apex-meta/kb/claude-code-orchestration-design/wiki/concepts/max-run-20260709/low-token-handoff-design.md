---
title: "Low-Token Handoff Design"
page_type: concept
kb_slug: claude-code-orchestration-design
run_id: max-run-20260709
status: needs_review
created_at: "2026-07-09"
updated_at: "2026-07-11"
source_policy: source_preserving
legacy_output_policy: old_pages_for_comparison_only
confidence: high
claim_label: source_backed_summary
source_refs:
  - source_path: apex-meta/kb/claude-code-orchestration-design/ingest-analysis/max-run-20260709/03-orchestration-workflows-and-agent-boundaries.md
  - source_path: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-skills.md.md
---

# Low-Token Handoff Design

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source: apex-meta/kb/claude-code-orchestration-design/ingest-analysis/max-run-20260709/03-orchestration-workflows-and-agent-boundaries.md
    rationale: "Run-specific source-sprawl and small-corpus decision evidence."
    coverage: "Selective source use, small curated agent sets, and workflow boundaries."
  - rank: 2
    source: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-skills.md.md
    rationale: "Progressive disclosure evidence."
    coverage: "Skills load supporting files only when needed."
```

## Macro / Meso / Micro

### Macro

Low-token handoff design routes agents to compact, source-backed pages before raw source dumps.

### Meso

The pattern is: index first, summary/concept/entity page second, raw source only when uncertainty or implementation requires it.

### Micro

This max-run keeps old outputs for comparison and writes smaller value-contract pages under versioned folders.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Apex should prefer compact routed evidence packets over broad source sprawl."
    source_pointer: apex-meta/kb/claude-code-orchestration-design/ingest-analysis/max-run-20260709/03-orchestration-workflows-and-agent-boundaries.md
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "How do we keep Claude orchestration handoffs small?"
    leads_to: apex-meta/kb/claude-code-orchestration-design/wiki/concepts/max-run-20260709/low-token-handoff-design.md
    rationale: "Token and routing design concept."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Reopen raw sources when compact pages cannot answer a routing or implementation question."
    source_pointer: apex-meta/kb/claude-code-orchestration-design/manifests/phase0/source-priority-candidates.md
    proposed_handling: revisit_source
```
