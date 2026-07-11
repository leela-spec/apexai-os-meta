---
title: "Apex KB"
page_type: entity
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

# Apex KB

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source: .claude/skills/apex-kb/SKILL.md
    rationale: "Primary skill entrypoint."
    coverage: "Lifecycle, ownership, semantic policy, boundary."
  - rank: 2
    source: .claude/skills/apex-kb/references/kb-contract.md
    rationale: "Primary KB data contract."
    coverage: "Canonical paths, source custody, page contract."
```

## Macro / Meso / Micro

### Macro

Apex KB is the durable source-preserving knowledge base compiler used for this run.

### Meso

It stores raw sources, manifests, Phase 1 analysis, Phase 2 wiki pages, logs, and derived retrieval/query artifacts while keeping planning/runtime systems out of scope.

### Micro

This max-run wrote parallel outputs under versioned folders and left old outputs intact.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Apex KB owns source-preserving semantic compile, not Apex Plan/Sync/Session mutation."
    source_pointer: .claude/skills/apex-kb/SKILL.md
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "What is Apex KB's role in Claude orchestration memory?"
    leads_to: apex-meta/kb/claude-code-orchestration-design/wiki/entities/max-run-20260709/apex-kb.md
    rationale: "Apex KB entity route."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Reopen if any future request tries to mutate Apex Plan, Sync, Session, PreCap, FlowRecap, or APSU from the KB."
    source_pointer: .claude/skills/apex-kb/SKILL.md
    proposed_handling: ask_operator
```
