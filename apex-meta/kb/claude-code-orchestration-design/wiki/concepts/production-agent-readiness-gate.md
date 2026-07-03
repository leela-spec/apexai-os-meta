---
title: "Production Agent Readiness Gate"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "production-agent-readiness-gate"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "agent_orchestration_index: when adding an agent improves system vs creates overhead"
    source_storage_mode: "pointer_only"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "Q004 persistent_when: repeated domain role, stable validation/audit role, security-sensitive repo executor"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T14:30:00Z"
updated_at: "2026-07-02T14:30:00Z"
confidence: "medium"
claim_label: "behavioral_inference"
status: "needs_review"
---

# Production Agent Readiness Gate

```yaml
pattern: "A role moves toward production-agent status only if it passes recurrence, boundary, validation, and overhead checks."
used_when:
  - "A candidate role is proposed for persistent production use."
not_used_when:
  - "The candidate can remain a skill, workflow stage, or ephemeral subagent."
reads:
  - "recurrence evidence"
  - "stable owned scope"
  - "non-owned scope"
  - "validation or audit duty"
  - "security sensitivity"
  - "coordination overhead"
writes:
  - "ready, defer, reject, or keep_ephemeral recommendation"
  - "operator review requirement"
token_efficiency:
  - "Readiness gate prevents broad permanent-agent sprawl."
drift_controls:
  - "A permanent agent is deferred if its doctrine would conflict with existing roles or lack a validator."
unresolved_or_deferred:
  - "Exact scoring thresholds."
  - "Final gate owner."
```
