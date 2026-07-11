---
title: "Apex KB as Source-Preserving Agent Memory"
page_type: summary
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
  - source_path: .claude/skills/apex-kb/SKILL.md
  - source_path: .claude/skills/apex-kb/references/kb-contract.md
---

# Apex KB as Source-Preserving Agent Memory

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source: .claude/skills/apex-kb/SKILL.md
    rationale: "Defines Apex KB lifecycle and ownership."
    coverage: "Canonical paths, semantic compile, boundaries."
  - rank: 2
    source: .claude/skills/apex-kb/references/kb-contract.md
    rationale: "Defines data, source custody, and page value contract."
    coverage: "Canonical/derived split, page frontmatter, Phase 2 required sections."
```

## Macro / Meso / Micro

### Macro

Apex KB is durable agent memory only when it preserves source custody and separates raw sources, semantic pages, and rebuildable indexes.

### Meso

Raw sources and manifests remain canonical. Wiki pages summarize and route. Derived search artifacts are rebuilt after page changes and cannot become source truth.

### Micro

The max-run output path structure preserves old outputs and makes comparison explicit before replacement.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Apex KB memory must remain source-preserving, not chat-memory-only."
    source_pointer: .claude/skills/apex-kb/references/kb-contract.md
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "How should source-preserving agent memory be structured?"
    leads_to: apex-meta/kb/claude-code-orchestration-design/wiki/summaries/max-run-20260709/apex-kb-as-source-preserving-agent-memory.md
    rationale: "Memory architecture route."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Reopen source custody while the committed source-payload manifest is empty."
    source_pointer: apex-meta/kb/claude-code-orchestration-design/manifests/source-payload-manifest.json
    proposed_handling: revisit_source
```
