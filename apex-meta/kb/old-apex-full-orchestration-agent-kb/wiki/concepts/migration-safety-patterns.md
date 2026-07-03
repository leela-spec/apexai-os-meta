---
title: "Migration Safety Patterns"
page_type: concept
kb_slug: "old-apex-full-orchestration-agent-kb"
concept_slug: "migration-safety-patterns"
source_refs:
  - source_id: "batch04-reusable-patterns-and-migration"
    source_path: "apex-meta/kb/old-apex-full-orchestration-agent-kb/ingest-analysis/batch04-reusable-patterns-and-migration.analysis.md"
    source_hash: "NA"
    source_pointer: "contradictions_or_tensions; migration_notes"
    source_storage_mode: "copy_into_kb"
  - source_id: "batch03-handoffs-validation-and-risk"
    source_path: "apex-meta/kb/old-apex-full-orchestration-agent-kb/ingest-analysis/batch03-handoffs-validation-and-risk.analysis.md"
    source_hash: "NA"
    source_pointer: "repo execution and current verification claims"
    source_storage_mode: "copy_into_kb"
created_at: "2026-07-03T00:00:00Z"
updated_at: "2026-07-03T00:00:00Z"
confidence: "mixed"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - repo-write-preflight-contract
  - exact-span-before-rewrite
  - current-verification-warning
  - constant-frame-control
  - path-drift
related_entities:
  - old-openclaw-agent-kb-system
review_flags:
  - "Implementation targets are not resolved by this page."
---

# Migration Safety Patterns

## Definition

A set of guardrails for carrying old Apex/OpenClaw agent KB doctrine into current Apex/Claude-native work without accidentally importing stale runtime authority, brittle local paths, overgrown agent rosters, unverified provider claims, or config mutation authority.

## Operating Rules

```yaml
rules:
  - "Preserve old role and path material as historical source evidence unless separately promoted."
  - "Do not treat old OpenClaw-specific runtime paths as current repo/runtime authority."
  - "Do not create separate permanent agents for every Meta Detective internal mode by default."
  - "Do not treat learning queue material as runtime truth."
  - "Mark current model/provider/cost/performance claims as needing current verification unless checked in the current run."
  - "Prefer deterministic scripts or lint checks for pointer integrity, stale-state, frontmatter/status vocabulary, source manifest validation, and forbidden write path detection."
```

## Relationships

```yaml
related_concepts:
  - repo-write-preflight-contract
  - current-verification-warning
  - anti-agent-sprawl-internal-modes
related_entities:
  - old-openclaw-agent-kb-system
  - reusable-scaffold-files
```

## Evidence

```yaml
evidence:
  - source_id: batch04-reusable-patterns-and-migration
    source_pointer: "T001"
    supports: "Old role taxonomy is evidence, not automatic current permanent agent set."
  - source_id: batch04-reusable-patterns-and-migration
    source_pointer: "T004"
    supports: "Old OpenClaw paths are historical, not current runtime authority."
  - source_id: batch04-reusable-patterns-and-migration
    source_pointer: "migration_notes / should_be_deprecated_or_not_carried_forward_as_binding"
    supports: "Non-binding carry-forward list."
  - source_id: batch03-handoffs-validation-and-risk
    source_pointer: "C011"
    supports: "Manual/governance review for config/provider/model-policy authority."
```

## Contradictions and Open Questions

```yaml
contradictions:
  - "Old EVD/IMP/RSK score conventions differ between Meta Detective and AI Handling Routing."
open_questions:
  - "Which migration targets should become skills, workflows, subagents/internal modes, deterministic checks, or operator gates?"
```
