---
title: "Source-Preserving KB Compile"
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
  - source_path: .claude/skills/apex-kb/references/kb-contract.md
  - source_path: .claude/skills/apex-kb/SKILL.md
---

# Source-Preserving KB Compile

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source: .claude/skills/apex-kb/references/kb-contract.md
    rationale: "Primary contract for canonical paths, source custody, and page requirements."
    coverage: "Raw sources, manifests, wiki pages, derived artifacts."
  - rank: 2
    source: .claude/skills/apex-kb/SKILL.md
    rationale: "Lifecycle owner contract."
    coverage: "Semantic compile and deterministic postflight ownership."
```

## Macro / Meso / Micro

### Macro

A source-preserving compile keeps original source custody separate from semantic summaries and rebuildable indexes.

### Meso

Raw files and manifests are canonical; wiki pages are source-backed compiled doctrine; search indexes and query packets are derived.

### Micro

This run records the empty source-payload manifest as a defect instead of pretending custody is fresh.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Generated pages must record source pointers and may not replace raw source custody."
    source_pointer: .claude/skills/apex-kb/references/kb-contract.md
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "How should source-preserving agent memory be structured?"
    leads_to: apex-meta/kb/claude-code-orchestration-design/wiki/concepts/max-run-20260709/source-preserving-kb-compile.md
    rationale: "Source custody and compile boundary."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Reopen if source-payload-manifest remains empty after terminal postflight."
    source_pointer: apex-meta/kb/claude-code-orchestration-design/manifests/source-payload-manifest.json
    proposed_handling: revisit_source
```
