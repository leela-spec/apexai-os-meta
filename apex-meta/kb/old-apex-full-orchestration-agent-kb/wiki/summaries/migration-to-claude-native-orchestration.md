---
title: "Migration to Claude-Native Orchestration"
page_type: summary
kb_slug: "old-apex-full-orchestration-agent-kb"
summary_slug: "migration-to-claude-native-orchestration"
source_refs:
  - source_id: "batch04-reusable-patterns-and-migration"
    source_path: "apex-meta/kb/old-apex-full-orchestration-agent-kb/ingest-analysis/batch04-reusable-patterns-and-migration.analysis.md"
    source_hash: "NA"
    source_pointer: "contradictions_or_tensions; migration_notes; proposed_phase2_targets"
    source_storage_mode: "copy_into_kb"
created_at: "2026-07-03T00:00:00Z"
updated_at: "2026-07-03T00:00:00Z"
confidence: "mixed"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - migration-safety-patterns
  - repo-write-preflight-contract
  - exact-span-before-rewrite
  - current-verification-warning
  - constant-frame-control
related_entities:
  - old-openclaw-agent-kb-system
  - reusable-scaffold-files
review_flags:
  - "Historical source pattern, not binding current runtime."
  - "Implementation target remains an operator decision."
---

# Migration to Claude-Native Orchestration

## Core Summary

Phase 2 preserves the old system as a source pattern and doctrine corpus, not as binding current runtime architecture. The old agent taxonomy is useful evidence, but it should not automatically become the current Apex/Claude-native permanent agent set.

Reusable migration targets include skills for source-authority checks, phase-gated KB promotion, repo write preflight/postflight discipline, and verdict packet generation. Workflow candidates include target-first bounded promptflows, constant frame control, Phase 1 to operator gate to Phase 2 wiki compile, and failure-pattern to countermeasure capture loops. Deterministic scripts or lint checks are better fits for pointer integrity, stale-state checks, frontmatter/status vocabulary, source manifest validation, and forbidden write path detection.

Deprecated or non-binding carry-forward items include old OpenClaw-specific runtime paths, runtime config authority inside advisory lanes, separate permanent agents for every internal mode, learning queue material as runtime truth, legacy local Windows paths as repo authority, and unverified current model/provider/cost claims.

## What This Adds

```yaml
adds:
  - "A migration classification layer for reusable patterns."
  - "A non-binding historical-source warning for old OpenClaw runtime paths."
  - "A split between skills, workflows, subagents/internal modes, deterministic checks, and operator gates."
clarifies:
  - "Current implementation requires separate approval and should not be inferred from Phase 2 wiki synthesis."
limits:
  - "Phase 2 compiles doctrine and migration options; it does not mutate runtime config, provider policy, model registry, or active agent surfaces."
```

## Key Claims

```yaml
key_claims:
  - claim_id: T001
    claim: "The old role taxonomy is useful evidence but should not automatically become the current Apex/Claude-native permanent agent set."
    source_pointer: "batch04-reusable-patterns-and-migration.analysis.md / T001"
    confidence: medium
    claim_label: working_hypothesis
    used_in_pages: [audit/semantic-open-questions.md]
  - claim_id: T004
    claim: "Old OpenClaw paths should not be treated as current runtime authority."
    source_pointer: "batch04-reusable-patterns-and-migration.analysis.md / T004"
    confidence: high
    claim_label: source_backed_summary
    used_in_pages: [concepts/migration-safety-patterns.md]
  - claim_id: MN001
    claim: "Several old patterns map to skills, workflows, subagents/internal modes, deterministic checks, or operator gates."
    source_pointer: "batch04-reusable-patterns-and-migration.analysis.md / migration_notes"
    confidence: high
    claim_label: source_backed_summary
    used_in_pages: [audit/semantic-open-questions.md]
```

## Contradictions

```yaml
contradictions:
  - "Meta Detective uses 1-100 EVD/IMP/RSK scores, while AI Handling Routing examples use 1-5 scores. These scales should not be silently merged."
```

## Open Questions

```yaml
open_questions:
  - "Which patterns should be implemented as skills versus workflows versus deterministic scripts?"
  - "Should internal validation modes remain wiki doctrine or become Claude-native subagents only for narrow, high-value cases?"
```
