---
title: "Handoff Stop Conditions"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "handoff-stop-conditions"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 82-85; mandatory stop conditions and refs replacing full context"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C013, B04-C014, B04-C017; stop and closure proof"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Handoff Stop Conditions

```yaml
pattern: "A handoff must state when the receiver should stop rather than infer missing context."
used_when:
  - "Missing source, authority, target, validation, or permission would make continuation invalid."
not_used_when:
  - "The next action is deterministic and fully specified."
reads:
  - "blocking assumptions"
  - "required approvals"
  - "source availability"
writes:
  - "stop or clarify marker"
  - "blocked handoff status"
token_efficiency:
  - "A stop marker prevents long speculative continuation."
drift_controls:
  - "No silent fill-in of missing source or operator authority."
unresolved_or_deferred:
  - "Exact machine enum can be standardized later."
```
