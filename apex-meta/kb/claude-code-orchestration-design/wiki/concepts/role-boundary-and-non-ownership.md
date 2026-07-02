---
title: "Role Boundary and Non-Ownership"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "role-boundary-and-non-ownership"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 65-66; role ownership and authority separation"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C006 through B04-C007; owns and does-not-own boundaries"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Role Boundary and Non-Ownership

```yaml
pattern: "Each role states what it owns and what it must not own before execution."
used_when:
  - "A skill, agent, verifier, or workflow stage could expand into adjacent authority."
not_used_when:
  - "A simple static page has no execution authority."
reads:
  - "role description"
  - "input artifact contract"
  - "non-goals"
writes:
  - "bounded output"
  - "handoff or stop condition"
token_efficiency:
  - "Non-ownership removes unnecessary context and prevents adjacent-lane research."
drift_controls:
  - "Boundary clauses prevent one agent from becoming the whole system."
unresolved_or_deferred:
  - "Specific role roster is deferred beyond S6."
```
