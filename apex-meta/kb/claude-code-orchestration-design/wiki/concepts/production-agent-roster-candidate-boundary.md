---
title: "Production Agent Roster Candidate Boundary"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "production-agent-roster-candidate-boundary"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "agent_orchestration_index: smallest_useful_permanent_agent_set and when adding agent improves system"
    source_storage_mode: "pointer_only"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "Q004 persistent_when and phase2_implications full_subagent_roster"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T14:30:00Z"
updated_at: "2026-07-02T14:30:00Z"
confidence: "medium"
claim_label: "behavioral_inference"
status: "needs_review"
---

# Production Agent Roster Candidate Boundary

```yaml
pattern: "A possible production agent enters the roster as a candidate, not as accepted infrastructure."
used_when:
  - "A repeated role looks durable enough to evaluate for production status."
not_used_when:
  - "The role is one-off, exploratory, or can be handled by a skill/workflow."
reads:
  - "candidate role name"
  - "owned scope"
  - "non-owned scope"
  - "validation or audit need"
  - "evidence of recurrence"
writes:
  - "candidate roster record"
  - "needs_review status"
token_efficiency:
  - "Candidate records stay compact until a real roster decision is needed."
drift_controls:
  - "Candidate role is not accepted truth or runtime agent definition."
unresolved_or_deferred:
  - "Final roster."
  - "Canonical production-agent file layout."
```
