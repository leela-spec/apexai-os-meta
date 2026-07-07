---
title: "Old Apex Full Orchestration Agent KB Wiki Index Rerun V2"
page_type: index
kb_slug: "old-apex-full-orchestration-agent-kb"
source_refs:
  - source_id: "phase1-rerun-completion-report"
    source_path: "apex-meta/kb/old-apex-full-orchestration-agent-kb/ingest-analysis/phase1-rerun-completion-report.md"
    source_pointer: "proposed_phase2_file_set"
    source_storage_mode: "copy_into_kb"
  - source_id: "phase2-rerun-compile-report"
    source_path: "apex-meta/kb/old-apex-full-orchestration-agent-kb/log/phase2-rerun-compile-report.md"
    source_pointer: "files_replaced; blocked_updates"
    source_storage_mode: "copy_into_kb"
updated_at: "2026-07-07T09:00:00+02:00"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
canonical_replacement_for: "wiki/index.md"
---

# Old Apex Full Orchestration Agent KB Wiki Index Rerun V2

## Scope

This index routes the semantic rerun layer for `old-apex-full-orchestration-agent-kb`. It includes the canonical pages already replaced and the `*-rerun-v2.md` pages created as connector-safe replacements for previously blocked overwrite targets.

Historical old-source paths remain source evidence only. Current Apex implementation decisions require current repo verification and deterministic postflight.

## Rerun Status

```yaml
semantic_rerun_status:
  deterministic_baseline_verified: true
  phase1_replaced: true
  phase2_replaced_with_workarounds: true
  canonical_index_overwrite_blocked: true
  postflight_required: true
```

## Route-by-Question Map

| Question | Start here | Then read |
|---|---|---|
| What is the old KB architecture? | `summaries/old-agent-kb-architecture.md` | `concepts/agent-doctrine-and-promotion-patterns.md` |
| What were the old roles? | `summaries/old-agent-role-system.md` | `entities/old-agent-roles.md` |
| How should handoffs be validated? | `summaries/handoff-validation-and-risk-doctrine.md` | `concepts/validation-and-routing-guardrails.md` |
| Which old patterns are reusable? | `summaries/reusable-old-agent-kb-patterns.md` | `entities/reusable-artifact-families.md` |
| What is safe to migrate? | `summaries/migration-to-claude-native-orchestration.md` | `concepts/migration-safety-patterns.md` |
| How should route boundaries be handled? | `summaries/deterministic-safety-rerun-v2.md` | `concepts/route-boundary-rerun-v2.md` |
| How should validation lenses be treated? | `entities/validation-lenses-rerun-v2.md` | `summaries/handoff-validation-and-risk-doctrine.md` |
| What remains open? | `../audit/semantic-open-questions.md` | `../log/phase2-rerun-compile-report.md` |

## Canonical Replacement Map

```yaml
manual_swap_map:
  - new_file: wiki/summaries/deterministic-safety-rerun-v2.md
    canonical_target: wiki/summaries/deterministic-execution-safety-after-lint-closure.md
  - new_file: wiki/concepts/route-boundary-rerun-v2.md
    canonical_target: wiki/concepts/repo-execution-routing-safety.md
  - new_file: wiki/entities/validation-lenses-rerun-v2.md
    canonical_target: wiki/entities/meta-detective-internal-modes.md
  - new_file: wiki/index-rerun-v2.md
    canonical_target: wiki/index.md
```

## Compiled Page Set

```yaml
summaries:
  - summaries/old-agent-kb-architecture.md
  - summaries/old-agent-role-system.md
  - summaries/handoff-validation-and-risk-doctrine.md
  - summaries/reusable-old-agent-kb-patterns.md
  - summaries/migration-to-claude-native-orchestration.md
  - summaries/deterministic-safety-rerun-v2.md
concepts:
  - concepts/agent-doctrine-and-promotion-patterns.md
  - concepts/validation-and-routing-guardrails.md
  - concepts/migration-safety-patterns.md
  - concepts/route-boundary-rerun-v2.md
entities:
  - entities/old-agent-roles.md
  - entities/validation-lenses-rerun-v2.md
  - entities/reusable-artifact-families.md
audit:
  - ../audit/semantic-open-questions.md
reports:
  - ../ingest-analysis/phase1-rerun-completion-report.md
  - ../log/phase2-rerun-compile-report.md
  - ../log/codex-semantic-rerun-postflight-prompt.md
```

## Source Discipline

Use this index first, then the smallest sufficient page set, then raw sources only when a claim must be verified, promoted, or applied to current Apex files.
