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
  - source_id: semantic-continuation-after-lint-closure
    source_path: apex-meta/kb/old-apex-full-orchestration-agent-kb/outputs/synthesis/apex-kb-semantic-continuation-after-lint-closure.md
    source_pointer: audit_open_questions_to_preserve
  - source_id: final-combined-lint-audit-status-postflight-report
    source_path: apex-meta/kb/old-apex-full-orchestration-agent-kb/outputs/synthesis/final-combined-lint-audit-status-postflight-report.md
    source_pointer: real_surface_checks; notes
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

  - id: OAQ-007
    question: "Which of the 39 repo-execution-router synthesis-surface findings require semantic wiki edits versus later deterministic cleanup?"
    current_handling: "Recorded as real-surface lint findings, visible but non-blocking; not auto-fixed in this semantic compile pass."
    status: active
    source_pointer: "final-combined-lint-audit-status-postflight-report.md / real_surface_checks / router_synthesis_surface_findings"

  - id: OAQ-008
    question: "Which of the 18 historical wiki surface findings are stale-authority risks versus acceptable historical source references?"
    current_handling: "Recorded as real-surface lint findings, visible but non-blocking; migration-safety-patterns now clarifies historical evidence versus current authority."
    status: active
    source_pointer: "final-combined-lint-audit-status-postflight-report.md / real_surface_checks / historical_wiki_surface_findings"

  - id: OAQ-009
    question: "Should deterministic execution safety be represented as a standalone summary page only, or also as a cross-linked concept family in a future pass?"
    current_handling: "Created a retrieval-first summary page and a repo-execution-routing-safety concept page; broader concept-family expansion remains open."
    status: active
    source_pointer: "apex-kb-semantic-continuation-after-lint-closure.md / audit_open_questions_to_preserve / AQ-003"

  - id: OAQ-010
    question: "Which source-authority build surfaces should be promoted into active Apex KB process doctrine versus retained as current Claude-native implementation evidence?"
    current_handling: "Not resolved in this semantic compile pass; promotion requires later source-backed or operator decision."
    status: active
    source_pointer: "apex-kb-semantic-continuation-after-lint-closure.md / audit_open_questions_to_preserve / AQ-004"

  - id: OAQ-011
    question: "Are there remaining old OpenClaw-specific runtime assumptions embedded in current wiki language that should be relabeled as historical evidence?"
    current_handling: "Not closed; historical-path-authority lint findings remain visible evidence for later review."
    status: active
    source_pointer: "apex-kb-semantic-continuation-after-lint-closure.md / audit_open_questions_to_preserve / AQ-005"
```

## Closure Rule

Do not close any audit item by inference. Closure requires a later source-backed decision or explicit operator decision recorded in the KB.
