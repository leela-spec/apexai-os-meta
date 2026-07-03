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
  - source_id: "semantic-continuation-after-lint-closure"
    source_path: "apex-meta/kb/old-apex-full-orchestration-agent-kb/outputs/synthesis/apex-kb-semantic-continuation-after-lint-closure.md"
    source_hash: "NA"
    source_pointer: "semantic meaning of lint-historical-path-authority; audit/open questions to preserve"
    source_storage_mode: "copy_into_kb"
  - source_id: "historical-path-authority-lint-implementation-report"
    source_path: "apex-meta/kb/old-apex-full-orchestration-agent-kb/outputs/synthesis/historical-path-authority-lint-implementation-report.md"
    source_hash: "NA"
    source_pointer: "verdict; command_added; validation; notes"
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
  - repo-execution-routing-safety
related_entities:
  - old-openclaw-agent-kb-system
review_flags:
  - "Implementation targets are not resolved by this page."
  - "Historical paths remain source evidence unless promoted by a recorded current decision."
---

# Migration Safety Patterns

## Definition

A set of guardrails for carrying old Apex/OpenClaw agent KB doctrine into current Apex/Claude-native work without accidentally importing stale runtime authority, brittle local paths, overgrown agent rosters, unverified provider claims, or config mutation authority.

After deterministic lint closure, this concept also includes historical path authority safety: historical OpenClaw paths, local Windows paths, and old runtime references may remain in the KB as source-trace evidence, but they must not be treated as current repo/runtime/config authority unless a later source-backed operator or implementation decision explicitly promotes them.

## Operating Rules

```yaml
rules:
  - "Preserve old role and path material as historical source evidence unless separately promoted."
  - "Do not treat old OpenClaw-specific runtime paths as current repo/runtime authority."
  - "Do not treat local Windows paths or old runtime references as active execution paths."
  - "Distinguish historical source evidence from current runtime authority in wiki pages, summaries, handovers, and audit items."
  - "Do not create separate permanent agents for every Meta Detective internal mode by default."
  - "Do not treat learning queue material as runtime truth."
  - "Mark current model/provider/cost/performance claims as needing current verification unless checked in the current run."
  - "Prefer deterministic scripts or lint checks for pointer integrity, stale-state, frontmatter/status vocabulary, source manifest validation, forbidden write path detection, and historical path authority checks."
```

## Why Historical-Path-Authority Lint Exists

```yaml
historical_path_authority_lint:
  purpose: >-
    Detect cases where a historical path, old OpenClaw runtime reference, or local
    Windows path is written as if it were current Apex repo/runtime/config authority.
  preserves:
    - old source custody
    - migration traceability
    - source provenance
  prevents:
    - stale authority drift
    - accidental execution against old paths
    - silent normalization of historical assumptions into current implementation doctrine
  semantic_status: "source_backed_summary"
```

## Relationships

```yaml
related_concepts:
  - repo-write-preflight-contract
  - current-verification-warning
  - anti-agent-sprawl-internal-modes
  - repo-execution-routing-safety
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
  - source_id: semantic-continuation-after-lint-closure
    source_pointer: "semantic_meaning / historical_path_authority_safety"
    supports: "Old paths can be preserved as source evidence but must not be treated as current authority unless promoted and verified."
  - source_id: historical-path-authority-lint-implementation-report
    source_pointer: "validation"
    supports: "The historical path authority lint command has validated command/help/fixture/JSON behavior."
```

## Contradictions and Open Questions

```yaml
contradictions:
  - "Old EVD/IMP/RSK score conventions differ between Meta Detective and AI Handling Routing."
open_questions:
  - "Which migration targets should become skills, workflows, subagents/internal modes, deterministic checks, or operator gates?"
  - "Which of the 18 historical wiki surface findings are stale-authority risks versus acceptable historical source references?"
  - "Which source-authority build surfaces should be promoted into active Apex KB process doctrine versus retained as current Claude-native implementation evidence?"
```
