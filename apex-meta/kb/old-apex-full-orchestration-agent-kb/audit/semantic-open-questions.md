# Semantic Open Questions — old-apex-full-orchestration-agent-kb

```yaml
page_type: audit_item
kb_slug: old-apex-full-orchestration-agent-kb
updated_at: "2026-07-06T22:45:00+02:00"
status: active
confidence: mixed
claim_label: operator_question
source_refs:
  - source_id: phase1-rerun-completion-report
    source_path: apex-meta/kb/old-apex-full-orchestration-agent-kb/ingest-analysis/phase1-rerun-completion-report.md
    source_pointer: core_findings; limitation_notes
  - source_id: batch04-reusable-patterns-and-migration
    source_path: apex-meta/kb/old-apex-full-orchestration-agent-kb/ingest-analysis/batch04-reusable-patterns-and-migration.analysis.md
    source_pointer: open_questions; contradictions_or_tensions
  - source_id: semantic-continuation-after-lint-closure
    source_path: apex-meta/kb/old-apex-full-orchestration-agent-kb/outputs/synthesis/apex-kb-semantic-continuation-after-lint-closure.md
    source_pointer: audit_open_questions_to_preserve
```

## Open Questions

```yaml
open_questions:
  - id: OKB-RERUN-Q001
    question: "Which reusable old-agent patterns should become current Apex skill text, deterministic lint, workflow templates, or wiki doctrine only?"
    source_pointer: "batch04 / open_questions A04-Q001"
    status: open
    blocker: false
  - id: OKB-RERUN-Q002
    question: "Which old path references need later deterministic cleanup, and which should remain explicit source evidence?"
    source_pointer: "batch04 / open_questions A04-Q002"
    status: open
    blocker: false
  - id: OKB-RERUN-Q003
    question: "Which recorded real-surface findings from finalized lint reports require semantic wiki edits versus later deterministic cleanup?"
    source_pointer: "batch03 / open_questions A03-Q001; semantic continuation report / audit open questions"
    status: open
    blocker: false
  - id: OKB-RERUN-Q004
    question: "Should internal validation modes stay wiki doctrine, become checklists, or later become separate current-system surfaces?"
    source_pointer: "batch02 / open_questions A02-Q002"
    status: open
    blocker: false
```

## Connector Write Limitations Observed

```yaml
connector_write_limitations:
  - path: wiki/summaries/deterministic-execution-safety-after-lint-closure.md
    status: update_blocked_by_connector_safety_layer
    semantic_status: prior_page_still_exists
  - path: wiki/concepts/repo-execution-routing-safety.md
    status: update_blocked_by_connector_safety_layer
    semantic_status: prior_page_still_exists
  - path: wiki/entities/meta-detective-internal-modes.md
    status: update_blocked_by_connector_safety_layer
    semantic_status: prior_page_still_exists
```

## Postflight Requirement

Deterministic postflight remains required from a local/Codex-capable environment. This connector run replaced semantic pages but did not run Python index, retrieval, lint, audit, or status commands.
