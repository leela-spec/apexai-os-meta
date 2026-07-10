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
updated_at: "2026-07-10T20:00:00Z"
confidence: "medium"
claim_label: "working_hypothesis"
status: "needs_review"
related_concepts: []
related_entities: []
review_flags: []
---

# Production Agent Roster Candidate Boundary

## Definition

This concept marks the boundary between recording a role as a candidate for the production agent roster and treating that role as accepted, running infrastructure. A candidate entry (owned scope, non-owned scope, evidence of recurrence, validation/audit need) is a review artifact, not a runtime agent definition. It exists to hold the compile plan's `agent_orchestration_index` question `smallest_useful_permanent_agent_set`. **This remains an open architectural question per the Phase 2 specialized index compile plan, not a settled Phase 1 claim** — Phase 1 material does not name a final roster, and the operator decision log explicitly keeps the full subagent roster in open-question status.

## Operating Rules

```yaml
rules:
  - "A proposed role enters the roster only as a candidate record (needs_review), never as an already-accepted production agent."
  - "A candidate record should capture: candidate role name, owned scope, non-owned scope, validation/audit need, and evidence of recurrence — not a runtime agent file."
  - "Do not infer a final roster size or membership from any single candidate record; smallest_useful_permanent_agent_set is an open compile-plan question, not a resolved count."
  - "Treat candidate-is-not-accepted-truth as the general rule this boundary specializes for the agent-roster case."
reads:
  - "candidate role name"
  - "owned scope"
  - "non-owned scope"
  - "validation or audit need"
  - "evidence of recurrence"
writes:
  - "candidate roster record"
  - "needs_review status"
token_efficiency: "Candidate records stay compact and provisional until a real roster decision is needed, avoiding premature detailed runtime specs for roles that may never be accepted."
drift_controls: "A candidate role is explicitly not accepted truth or a runtime agent definition until the (still-unresolved) readiness gate and roster-size questions are settled."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Primary source: names smallest_useful_permanent_agent_set as an open agent_orchestration_index question, meaning no roster size or membership is settled."
    coverage: "Frames why any candidate list must stay provisional rather than final."
  - source_id: "operator-phase1-review-decisions-20260702"
    rationale: "Explicitly places full_subagent_roster under write_as_boundary_or_open_question, and supplies the only directional candidate-evaluation criteria (Q004) presently available."
    coverage: "Section 3 phase2_implications; Q004_subagent_persistence criteria."
```

## Macro / Meso / Micro

### Macro

`agent_orchestration_index` names `smallest_useful_permanent_agent_set` directly alongside `when_adding_an_agent_improves_the_system` as open core questions — meaning Phase 1 does not establish how many, or which, roles should ultimately be persistent production agents. Any list of "candidate" roles compiled from Phase 1 material is therefore, by construction, a candidate list rather than a final roster.

### Meso

The operator decision log is explicit on this point at the representation level: its `phase2_implications` section places `full_subagent_roster` under `write_as_boundary_or_open_question`, in the same list as MCP server allowlisting and plugin packaging timing — items the operator has flagged as deliberately deferred rather than settled. Operator decision Q004's `persistent_when`/`ephemeral_when` criteria are the only concrete evaluation inputs offered, and they are candidate-evaluation criteria, not a roster.

### Micro

- Compile plan `agent_orchestration_index` core question `smallest_useful_permanent_agent_set` (compile plan lines ~61).
- `operator-phase1-review-decisions-20260702.md` section 3, `write_as_boundary_or_open_question` list including `full_subagent_roster` (lines 132-137).
- Same file, Q004 `persistent_when`/`ephemeral_when` (lines 74-84), usable as candidate-evaluation inputs only.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "agent_orchestration_index names smallest_useful_permanent_agent_set as an open core question, meaning no final roster size or membership is established by Phase 1."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md, agent_orchestration_index core_questions"
    confidence: "medium"
    claim_label: "working_hypothesis"
  - claim_id: C002
    claim: "The operator decision log explicitly places full_subagent_roster under write_as_boundary_or_open_question rather than write_as_doctrine, confirming candidate status (not acceptance) is the correct Phase 2 representation for any proposed agent role."
    source_pointer: "operator-phase1-review-decisions-20260702.md lines 132-137"
    confidence: "medium"
    claim_label: "working_hypothesis"
  - claim_id: C003
    claim: "Operator decision Q004's persistent_when/ephemeral_when criteria supply candidate-evaluation inputs (recurrence, stable scope, validation duty, security sensitivity) without resolving which specific roles clear the bar."
    source_pointer: "operator-phase1-review-decisions-20260702.md lines 74-84"
    confidence: "medium"
    claim_label: "working_hypothesis"
```

## Routes Here

```yaml
routes:
  - question: "Has a specific candidate role passed the staged readiness check yet?"
    leads_to: "claude-code-orchestration-design/concepts/production-agent-readiness-gate.md"
    rationale: "The readiness gate is the (equally open) check a candidate would need to pass to leave candidate status."
  - question: "What is the general rule that a candidate record is not accepted truth?"
    leads_to: "claude-code-orchestration-design/concepts/candidate-is-not-accepted-truth.md"
    rationale: "That page states the general claim-status rule this boundary specializes for the agent-roster case."
  - related_page: "claude-code-orchestration-design/concepts/persistent-agent-boundary.md"
    relation: "Persistent-agent-boundary states the general persistence question a roster candidate is being evaluated against."
```

## Evidence

```yaml
evidence:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "agent_orchestration_index core_questions, smallest_useful_permanent_agent_set"
    supports: "Definition and Macro section."
  - source_id: "operator-phase1-review-decisions-20260702"
    source_pointer: "section 3 phase2_implications, lines 132-137; Q004, lines 74-84"
    supports: "Meso and Micro sections: candidate-vs-accepted framing and evaluation inputs."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "This remains an open architectural question per the Phase 2 specialized index compile plan, not a settled Phase 1 claim: final roster membership and size are unresolved."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md, agent_orchestration_index"
    proposed_handling: "ask_operator"
  - id: U002
    description: "Canonical production-agent file layout (how an accepted, non-candidate agent should be represented once a roster decision is made) is not defined anywhere in Phase 1 material."
    source_pointer: "operator-phase1-review-decisions-20260702.md, section 3"
    proposed_handling: "planning_task_candidate"
```
