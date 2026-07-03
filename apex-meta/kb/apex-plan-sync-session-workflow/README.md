# Apex Plan Sync Session Workflow KB

```yaml
kb_slug: apex-plan-sync-session-workflow
kb_root: apex-meta/kb/apex-plan-sync-session-workflow/
status: phase1_ingest_analysis_created
source_storage_mode: pointer_only
primary_source_roots:
  - .claude/skills/apex-plan/
  - .claude/skills/apex-sync/
  - .claude/skills/apex-session/
phase2_allowed: false
required_phrase: approve ingest
```

## Purpose

This KB captures the source-grounded lifecycle ingest for the workflow boundary between `apex-plan`, `apex-sync`, and `apex-session`.

The source corpus is the three Claude skill folders visible in the repository. The Phase 1 output focuses on:

- the ownership split between planning, deterministic sync, and session mutation/handoff;
- the handoff interfaces between the three skills;
- the recurring invariants shared by all three packages;
- the risks created when planning, computation, and mutation are collapsed;
- proposed Phase 2 wiki targets, blocked until explicit operator approval.

## Current lifecycle state

```yaml
lifecycle_state:
  scaffold: complete_minimal
  source_intake: pointer_only_manifest_created
  deterministic_corpus_intelligence: source_scope_report_created
  ingest_phase_1_analysis: complete
  operator_gate: pending
  ingest_phase_2_wiki_compile: blocked
  deterministic_index_validation: not_run
  local_retrieval: not_run
  query_packet_generation: not_run
  lint_audit_maintenance: not_run
```

## Important boundary

No wiki pages were created because the current operator turn did not contain the exact Apex KB Phase 2 approval phrase.
