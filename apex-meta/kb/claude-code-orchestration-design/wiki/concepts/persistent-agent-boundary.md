---
title: "Persistent Agent Boundary"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "persistent-agent-boundary"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 57-70; persistent agent questions"
    source_storage_mode: "pointer_only"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "lines 76-87; persistent subagent policy"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "medium"
claim_label: "behavioral_inference"
status: "active"
---

# Persistent Agent Boundary

```yaml
pattern: "A persistent agent is justified only for a repeated, stable domain role with clear validation or audit responsibility."
used_when:
  - "The role needs durable doctrine, tools, and review criteria."
not_used_when:
  - "The work is exploratory, temporary, or easily expressed as a skill."
reads:
  - "agent doctrine"
  - "activation seed"
  - "role-specific KB"
writes:
  - "bounded outputs"
  - "review candidates"
token_efficiency:
  - "Persistent roles reduce repeated setup only when they are stable."
drift_controls:
  - "Non-ownership clauses and verifier separation prevent role expansion."
unresolved_or_deferred:
  - "Final agent roster is outside S6."
```
