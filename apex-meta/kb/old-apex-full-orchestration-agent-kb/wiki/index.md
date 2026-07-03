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
  - source_id: "semantic-continuation-after-lint-closure"
    source_path: "apex-meta/kb/old-apex-full-orchestration-agent-kb/outputs/synthesis/apex-kb-semantic-continuation-after-lint-closure.md"
    source_hash: "NA"
    source_pointer: "wiki_pages_to_create_or_update; deterministic_post_llm_commands"
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

The index now also registers the semantic continuation layer created after deterministic lint closure for execution routing and historical path authority safety.

## Compiled Pages

```yaml
summaries:
  - summaries/old-agent-kb-architecture.md
  - summaries/old-agent-role-system.md
  - summaries/handoff-validation-and-risk-doctrine.md
  - summaries/reusable-old-agent-kb-patterns.md
  - summaries/migration-to-claude-native-orchestration.md
  - summaries/deterministic-execution-safety-after-lint-closure.md
concepts:
  - concepts/agent-doctrine-and-promotion-patterns.md
  - concepts/validation-and-routing-guardrails.md
  - concepts/migration-safety-patterns.md
  - concepts/repo-execution-routing-safety.md
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

Use this index first, then read the smallest sufficient page set. For role boundaries, start with `entities/old-agent-roles.md`. For validation or handoff doctrine, start with `summaries/handoff-validation-and-risk-doctrine.md`, `concepts/validation-and-routing-guardrails.md`, and `concepts/repo-execution-routing-safety.md`. For migration decisions, start with `summaries/migration-to-claude-native-orchestration.md` and `concepts/migration-safety-patterns.md`. For deterministic execution safety after lint closure, start with `summaries/deterministic-execution-safety-after-lint-closure.md`.

## Source Discipline

The old OpenClaw-specific runtime paths, local Windows paths, and historical runtime references are historical source evidence, not current runtime authority. Current Apex or Claude-native implementation decisions require separate approval and verification. Real-surface lint findings are preserved as visible audit signals and are not silently resolved by wiki index inclusion.

<!-- BEGIN AUTO-GENERATED INDEX -->

Generated: `2026-07-03T00:00:00Z`

Compiled page count: `13`

## Concept Pages

- [Agent Doctrine and Promotion Patterns](concepts/agent-doctrine-and-promotion-patterns.md) - `active` / `high`
- [Migration Safety Patterns](concepts/migration-safety-patterns.md) - `active` / `mixed`
- [Repo Execution Routing Safety](concepts/repo-execution-routing-safety.md) - `active` / `high`
- [Validation and Routing Guardrails](concepts/validation-and-routing-guardrails.md) - `active` / `high`

## Entity Pages

- [Meta Detective Internal Modes](entities/meta-detective-internal-modes.md) - `active` / `high`
- [Old Agent Roles](entities/old-agent-roles.md) - `active` / `high`
- [Reusable Artifact Families](entities/reusable-artifact-families.md) - `active` / `high`

## Summary Pages

- [Deterministic Execution Safety After Lint Closure](summaries/deterministic-execution-safety-after-lint-closure.md) - `active` / `high`
- [Handoff, Validation, and Risk Doctrine](summaries/handoff-validation-and-risk-doctrine.md) - `active` / `high`
- [Migration to Claude-Native Orchestration](summaries/migration-to-claude-native-orchestration.md) - `active` / `mixed`
- [Old Agent KB Architecture](summaries/old-agent-kb-architecture.md) - `active` / `high`
- [Old Agent Role System](summaries/old-agent-role-system.md) - `active` / `high`
- [Reusable Old Agent KB Patterns](summaries/reusable-old-agent-kb-patterns.md) - `active` / `high`

<!-- END AUTO-GENERATED INDEX -->
