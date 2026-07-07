---
title: "Route Boundary Rerun V2"
page_type: concept
kb_slug: "old-apex-full-orchestration-agent-kb"
concept_slug: "route-boundary-rerun-v2"
source_refs:
  - source_id: "phase1-rerun-batch03"
    source_path: "apex-meta/kb/old-apex-full-orchestration-agent-kb/ingest-analysis/batch03-handoffs-validation-and-risk.analysis.md"
    source_pointer: "claims A03-C005-A03-C009"
    source_storage_mode: "copy_into_kb"
  - source_id: "semantic-continuation-after-lint-closure"
    source_path: "apex-meta/kb/old-apex-full-orchestration-agent-kb/outputs/synthesis/apex-kb-semantic-continuation-after-lint-closure.md"
    source_pointer: "semantic meaning of lint-repo-execution-router"
    source_storage_mode: "copy_into_kb"
updated_at: "2026-07-07T09:00:00+02:00"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
canonical_replacement_for: "wiki/concepts/repo-execution-routing-safety.md"
---

# Route Boundary Rerun V2

## Adaptive Ranked Source Set

```yaml
ranked_source_set:
  tier_1:
    - source: "batch03-handoffs-validation-and-risk.analysis.md"
      supports: "route boundary synthesis"
    - source: "semantic-continuation-after-lint-closure.md"
      supports: "finalized boundary-check semantics"
  tier_2:
    - source: "special_ops__ai_handling_routing/ESSENCE.md"
      supports: "routing minimum and source authority"
```

## Macro Synthesis

Route-boundary safety prevents semantic conclusions from being mistaken for permission to change repository files. It keeps analysis, deterministic checks, and file updates in separate lanes.

## Meso Synthesis

A safe route boundary names task, non-task, target output, source authority, operation class, allowed actions, forbidden actions, checks, stop conditions, fallback, validator, and final report shape.

## Micro Synthesis

```yaml
key_claims:
  - id: RB2-001
    claim: "Semantic KB writing and repository file updates are different executor surfaces."
    source_pointer: ".claude/skills/apex-kb/SKILL.md / deterministic versus LLM ownership; batch03 A03-C009"
    confidence: high
    claim_label: source_backed_summary
  - id: RB2-002
    claim: "Route decisions require task, non-task, route surface, fallback, validator, and confidence."
    source_pointer: "special_ops__ai_handling_routing/ESSENCE.md / Minimal routing card"
    confidence: high
    claim_label: raw_source
  - id: RB2-003
    claim: "Unclear file-update routing should remain visible as a process finding rather than be silently cleaned from prose."
    source_pointer: "semantic-continuation-after-lint-closure.md / real_surface_findings"
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

Use this concept before drafting a Codex prompt, approving a patch flow, or deciding whether a KB output requires local execution.

## Uncertainty / Raw Source Triggers

Reopen live repo files and deterministic reports before applying this concept to current file changes.
