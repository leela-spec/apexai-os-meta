# Semantic Open Questions — old-apex-full-orchestration-agent-kb

```yaml
page_type: audit_item
kb_slug: old-apex-full-orchestration-agent-kb
created_at: "2026-07-03T00:00:00Z"
updated_at: "2026-07-03T00:00:00Z"
status: active
confidence: mixed
claim_label: operator_question
source_refs:
  - source_id: phase1-completion-report
    source_path: apex-meta/kb/old-apex-full-orchestration-agent-kb/ingest-analysis/phase1-completion-report.md
    source_pointer: unresolved_questions
  - source_id: batch04-reusable-patterns-and-migration
    source_path: apex-meta/kb/old-apex-full-orchestration-agent-kb/ingest-analysis/batch04-reusable-patterns-and-migration.analysis.md
    source_pointer: contradictions_or_tensions
```

## Audit Items

```yaml
audit_items:
  - id: OAQ-001
    question: "Should Phase 2 preserve old role names as entities only, or also compile generalized Claude-native concepts that abstract away OpenClaw naming?"
    current_handling: "Preserved old roles as historical entities and grouped generalized concepts into concept-family pages."
    status: active
    source_pointer: "phase1-completion-report.md / unresolved_questions"

  - id: OAQ-002
    question: "How should mixed EVD/IMP/RSK score conventions be handled?"
    current_handling: "Recorded as unresolved contradiction; did not normalize 1-100 and 1-5 score scales."
    status: active
    source_pointer: "batch04-reusable-patterns-and-migration.analysis.md / T002"

  - id: OAQ-003
    question: "Which old agent KB roots should receive full source-specific expansion beyond the sampled/high-signal pass?"
    current_handling: "Phase 2 compiled compact wiki pages; deeper root-by-root expansion remains future work."
    status: active
    source_pointer: "phase1-completion-report.md / unresolved_questions"

  - id: OAQ-004
    question: "Should Meta Detective internal modes become Claude Code subagents, skill checklists, workflows, or remain wiki doctrine only?"
    current_handling: "Preserved as internal-mode entity page and migration question; no subagent creation."
    status: active
    source_pointer: "phase1-completion-report.md / unresolved_questions; batch04 migration_notes"

  - id: OAQ-005
    question: "How should old OpenClaw runtime/config references be marked to prevent accidental current-runtime authority?"
    current_handling: "Marked old runtime paths and config authority as historical evidence and non-binding carry-forward."
    status: active
    source_pointer: "batch04-reusable-patterns-and-migration.analysis.md / T004 and deprecated list"

  - id: OAQ-006
    question: "Which patterns should become skills, workflows, deterministic checks, operator gates, or subagents/internal modes?"
    current_handling: "Recorded migration classification without implementation."
    status: active
    source_pointer: "batch04-reusable-patterns-and-migration.analysis.md / migration_notes"
```

## Closure Rule

Do not close any audit item by inference. Closure requires a later source-backed decision or explicit operator decision recorded in the KB.
