---
title: "Old Apex Full Orchestration Agent KB Wiki Index"
page_type: index
kb_slug: "old-apex-full-orchestration-agent-kb"
source_refs:
  - source_id: "phase1-completion-report"
    source_path: "apex-meta/kb/old-apex-full-orchestration-agent-kb/ingest-analysis/phase1-completion-report.md"
    source_hash: "NA"
    source_pointer: "proposed_phase2_targets"
    source_storage_mode: "copy_into_kb"
created_at: "2026-07-02T21:23:35Z"
updated_at: "2026-07-03T00:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Old Apex Full Orchestration Agent KB Wiki Index

## Scope

This wiki compiles the approved Phase 2 layer for `old-apex-full-orchestration-agent-kb` from the Phase 1 analysis files. The source corpus is the old managed agent KB mirrored under the KB root, with the original source root preserved in the manifest.

## Compiled Pages

```yaml
summaries:
  - summaries/old-agent-kb-architecture.md
  - summaries/old-agent-role-system.md
  - summaries/handoff-validation-and-risk-doctrine.md
  - summaries/reusable-old-agent-kb-patterns.md
  - summaries/migration-to-claude-native-orchestration.md
concepts:
  - concepts/agent-doctrine-and-promotion-patterns.md
  - concepts/validation-and-routing-guardrails.md
  - concepts/migration-safety-patterns.md
entities:
  - entities/old-agent-roles.md
  - entities/meta-detective-internal-modes.md
  - entities/reusable-artifact-families.md
audit:
  - ../audit/semantic-open-questions.md
report:
  - ../log/phase2-wiki-compile-report.md
```

## Retrieval Notes

Use this index first, then read the smallest sufficient page set. For role boundaries, start with `entities/old-agent-roles.md`. For validation or handoff doctrine, start with `summaries/handoff-validation-and-risk-doctrine.md` and `concepts/validation-and-routing-guardrails.md`. For migration decisions, start with `summaries/migration-to-claude-native-orchestration.md` and `concepts/migration-safety-patterns.md`.

## Source Discipline

The old OpenClaw-specific runtime paths and local Windows paths are historical source evidence, not current runtime authority. Current Apex or Claude-native implementation decisions require separate approval and verification.
