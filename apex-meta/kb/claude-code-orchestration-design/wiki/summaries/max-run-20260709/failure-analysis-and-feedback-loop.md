---
title: "Failure Analysis and Feedback Loop"
page_type: summary
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
  - source_path: apex-meta/kb/claude-code-orchestration-design/ingest-analysis/max-run-20260709/05-failure-analysis-and-operator-feedback.md
---

# Failure Analysis and Feedback Loop

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source: apex-meta/kb/claude-code-orchestration-design/ingest-analysis/max-run-20260709/05-failure-analysis-and-operator-feedback.md
    rationale: "Run-specific failure analysis."
    coverage: "Legacy output limits, empty payload manifest, postflight warnings."
  - rank: 2
    source: apex-meta/kb/claude-code-orchestration-design/log/max-update-run-gate-20260709.md
    rationale: "Historical gate artifact."
    coverage: "Why deterministic rerun was required before semantic rebuild."
```

## Macro / Meso / Micro

### Macro

The main failure pattern is layer collapse: treating old summaries, incomplete deterministic artifacts, or runtime-capable mechanisms as more authoritative than they are.

### Meso

The feedback loop is: expose the defect, write new parallel outputs, avoid overwriting old outputs, then run deterministic postflight before accepting query-ready closure.

### Micro

For this run, the source-payload manifest content is empty and must remain visible as a postflight requirement.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Old outputs are comparison material, not source truth for max-run pages."
    source_pointer: apex-meta/kb/claude-code-orchestration-design/ingest-analysis/max-run-20260709/05-failure-analysis-and-operator-feedback.md
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "What failed in the old KB outputs and how should the feedback loop work?"
    leads_to: apex-meta/kb/claude-code-orchestration-design/wiki/summaries/max-run-20260709/failure-analysis-and-feedback-loop.md
    rationale: "Failure and correction route."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Reopen postflight after index, retrieval, status, and lint commands run in terminal."
    source_pointer: .claude/skills/apex-kb/examples/lifecycle-runbook.md
    proposed_handling: revisit_source
```
