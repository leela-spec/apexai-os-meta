---
title: "Old Agent KB Architecture"
page_type: summary
kb_slug: "old-apex-full-orchestration-agent-kb"
summary_slug: "old-agent-kb-architecture"
source_refs:
  - source_id: "batch01-agent-kb-architecture"
    source_path: "apex-meta/kb/old-apex-full-orchestration-agent-kb/ingest-analysis/batch01-agent-kb-architecture.analysis.md"
    source_hash: "NA"
    source_pointer: "source_grounded_claims C001-C010"
    source_storage_mode: "copy_into_kb"
created_at: "2026-07-03T00:00:00Z"
updated_at: "2026-07-03T00:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - five-file-agent-kb-scaffold
  - compact-essence-activation-surface
  - candidate-only-learning-queue
  - owner-validator-agent-kb-model
  - scaffold-appendix-split
related_entities:
  - reusable-scaffold-files
  - old-openclaw-agent-kb-system
review_flags: []
---

# Old Agent KB Architecture

## Core Summary

The old Apex managed agent KB is a durable role-doctrine architecture. It uses a root index to map first-wave agent KB roots, and each durable agent root follows a five-file scaffold: `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md`, and `LEARNING_QUEUE.md`.

The architecture separates compact activation surfaces from deeper evidence surfaces. `ESSENCE.md` carries accepted compact role boundaries and activation doctrine, while appendices or supporting files carry detailed evidence, rankings, candidate ledgers, examples, and QA traces. `LEARNING_QUEUE.md` is explicitly candidate-only and is not runtime truth until validated and promoted.

## What This Adds

```yaml
adds:
  - "A reusable doctrine scaffold for durable role behavior across sessions."
  - "A clear source/candidate/canon/runtime-truth separation pattern."
  - "A compact-surface plus appendix-detail architecture for retrieval-safe KB design."
clarifies:
  - "Old local source paths are preserved as historical custody evidence, not current runtime authority."
  - "Phase 0 navigation hints are not semantic authority rankings."
limits:
  - "This page does not claim the old role roster should become the current Claude-native agent roster."
```

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "The old agent KB has an explicit root index mapping first-wave agents to KB roots."
    source_pointer: "batch01-agent-kb-architecture.analysis.md / C001"
    confidence: high
    claim_label: raw_source
    used_in_pages: [entities/old-agent-roles.md]
  - claim_id: C002
    claim: "Each agent KB root follows the five-file scaffold."
    source_pointer: "batch01-agent-kb-architecture.analysis.md / C002"
    confidence: high
    claim_label: raw_source
    used_in_pages: [concepts/agent-doctrine-and-promotion-patterns.md]
  - claim_id: C003
    claim: "Learning queues are candidate-only and never runtime truth."
    source_pointer: "batch01-agent-kb-architecture.analysis.md / C003"
    confidence: high
    claim_label: raw_source
    used_in_pages: [concepts/agent-doctrine-and-promotion-patterns.md]
  - claim_id: C008
    claim: "Source material, candidate material, accepted doctrine, and runtime truth are intentionally separated."
    source_pointer: "batch01-agent-kb-architecture.analysis.md / C008"
    confidence: high
    claim_label: source_backed_summary
    used_in_pages: [concepts/agent-doctrine-and-promotion-patterns.md]
```

## Contradictions

```yaml
contradictions: []
```

## Open Questions

```yaml
open_questions:
  - "Which old agent KB roots should receive full source-specific expansion beyond the high-signal Phase 1 pass?"
```
