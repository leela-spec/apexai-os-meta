---
title: "Phase 2 Value Contract"
page_type: concept
kb_slug: claude-code-orchestration-design
run_id: max-run-20260709
status: new_parallel_compile
source_policy: source_preserving
legacy_output_policy: old_pages_for_comparison_only
confidence: high
claim_label: source_backed_summary
source_refs:
  - source_path: .claude/skills/apex-kb/references/kb-contract.md
  - source_path: .claude/skills/apex-kb/templates/wiki-page-templates.md
---

# Phase 2 Value Contract

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source: .claude/skills/apex-kb/references/kb-contract.md
    rationale: "Defines required Phase 2 page sections."
    coverage: "Adaptive Ranked Source Set, Macro / Meso / Micro, Key Claims, Routes Here, Reopen Triggers."
  - rank: 2
    source: .claude/skills/apex-kb/templates/wiki-page-templates.md
    rationale: "Defines reusable page templates."
    coverage: "Summary, concept, entity frontmatter and section shape."
```

## Macro / Meso / Micro

### Macro

The value contract ensures compiled wiki pages are useful routing artifacts, not shell pages.

### Meso

Each page needs adaptive source ranking, layered synthesis, source-backed claims, query routes, and visible uncertainty/reopen triggers.

### Micro

This max-run intentionally writes smaller pages, but every Phase 2 page includes the mandatory headings.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Phase 2 summary, concept, and entity pages must include the five required value sections."
    source_pointer: .claude/skills/apex-kb/references/kb-contract.md
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "What sections must new Apex KB Phase 2 pages contain?"
    leads_to: apex-meta/kb/claude-code-orchestration-design/wiki/concepts/max-run-20260709/phase2-value-contract.md
    rationale: "Page contract route."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Reopen if deterministic lint reports missing value sections after postflight."
    source_pointer: .claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md
    proposed_handling: revisit_source
```
