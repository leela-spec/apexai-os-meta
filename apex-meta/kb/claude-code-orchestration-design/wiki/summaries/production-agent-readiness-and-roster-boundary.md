---
title: "Production Agent Readiness and Roster Boundary"
page_type: summary
kb_slug: "claude-code-orchestration-design"
summary_slug: "production-agent-readiness-and-roster-boundary"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "agent_orchestration_index: smallest useful permanent agent set, when adding agent improves system, coordination overhead"
    source_storage_mode: "pointer_only"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "Q004 persistent_when/ephemeral_when and phase2_implications full_subagent_roster"
    source_storage_mode: "pointer_only"
  - source_id: "wiki/concepts/persistent-agent-boundary"
    source_path: "apex-meta/kb/claude-code-orchestration-design/wiki/concepts/persistent-agent-boundary.md"
    source_hash: "9ea40726e54acf3ef264d61784200743078cb557"
    source_pointer: "existing partial coverage: final agent roster outside S6"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T14:30:00Z"
updated_at: "2026-07-02T14:30:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "needs_review"
---

# Production Agent Readiness and Roster Boundary

```yaml
extension_package: "production_agent_readiness_and_roster_boundary"
pattern: >
  Production agents should be treated as a small validated roster, not as every
  useful subtask made permanent. The current S6 compile can define readiness and
  boundary criteria, but it must not declare a final production roster.
used_when:
  - "A repeated domain role appears to require durable doctrine, stable validation, or audit responsibility."
  - "A future implementation asks whether a role should graduate from skill/workflow/subagent to production agent."
not_used_when:
  - "The work is exploratory, temporary, easily expressed as a skill, or not validated."
reads:
  - "role recurrence evidence"
  - "authority boundary"
  - "validation or audit requirement"
  - "coordination-overhead risk"
writes:
  - "candidate roster item"
  - "readiness gate result"
  - "deferred decision record"
token_efficiency:
  - "Keep candidate roles as short records until they meet readiness criteria."
drift_controls:
  - "No production agent is accepted without owner boundary, non-ownership, source_refs, validation gates, and operator acceptance."
unresolved_or_deferred:
  - "Final production agent roster."
  - "Agent-specific KB folder convention."
  - "Verifier loop implementation."
```

This page extends `persistent-agent-boundary.md` and `persistent-agent-vs-ephemeral-subagent.md` without editing them.
