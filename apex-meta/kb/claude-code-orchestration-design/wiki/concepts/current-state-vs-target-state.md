---
title: "Current State vs Target State"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "current-state-vs-target-state"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 72-85; current_state_vs_target_state"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C007 and B04-C011; state frames and target locks"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Current State vs Target State

```yaml
pattern: "Execution starts by naming what is true now and what acceptable completion looks like."
used_when:
  - "A handoff or task could drift because the starting state or target is implicit."
not_used_when:
  - "The page is only a static glossary item."
reads:
  - "current files or state packet"
  - "operator target"
  - "source authority"
writes:
  - "state frame"
  - "task or handoff packet"
token_efficiency:
  - "A short state frame replaces long recap prose."
drift_controls:
  - "Target lock prevents silent scope expansion."
unresolved_or_deferred:
  - "No runtime state packet is created by this S6 page."
```
