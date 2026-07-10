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
updated_at: "2026-07-10T20:00:00Z"
confidence: "medium"
claim_label: "working_hypothesis"
status: "needs_review"
related_concepts:
  - "persistent-agent-boundary"
  - "persistent-agent-vs-ephemeral-subagent"
  - "production-agent-readiness-gate"
  - "production-agent-roster-candidate-boundary"
related_entities: []
review_flags:
  - "roster question intentionally left unresolved; do not upgrade confidence without new operator decision"
---

# Production Agent Readiness and Roster Boundary

## Core Summary

**This page is explicitly about an OPEN question in this KB, not a resolved
doctrine.** The compile plan's `agent_orchestration_index` (lines 55-68)
lists, as unanswered core questions, "smallest useful permanent agent set,"
"when adding an agent improves the system," and "when adding an agent
creates coordination overhead." None of these are answered by this compile.
The Phase 1 operator review decision log confirms this boundary directly: in
`phase2_implications`, `full_subagent_roster` is listed under
`write_as_boundary_or_open_question`, not under `write_as_doctrine`
(`operator-phase1-review-decisions-20260702.md` section 3), and the compile
plan's `phase2_non_goals` explicitly forbid `final_named_agent_implementation`
and `production_runtime_setup` (compile plan section 7).

One narrower piece *is* settled: operator decision Q004 validated general
readiness criteria for when a subagent should be persistent versus ephemeral.
Persistent is justified when a role shows repeated domain recurrence, a
stable validation or audit responsibility, or is a security-sensitive repo
executor with explicit constraints. Ephemeral is appropriate for one-off
source scouting, temporary comparison reading, or broad exploration
(`operator-phase1-review-decisions-20260702.md` Q004). That is a decision
about *how to judge readiness*, not a decision about *which named agents pass
the judgment* — the roster itself remains open.

## What This Adds

```yaml
adds:
  - "Validated persistent_when / ephemeral_when readiness criteria (Q004), usable as a gate for any future candidate role."
  - "An explicit, source-cited statement that the production agent roster is deferred, not decided, so future readers do not mistake this page for a roster."
clarifies:
  - "Distinction between 'criteria for readiness' (settled, medium-high confidence) and 'the actual roster of production agents' (open, not addressed here)."
limits:
  - "Names no production agent. Resolves no coordination-overhead threshold. Does not define the smallest useful permanent agent set."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "operator-phase1-review-decisions-20260702"
    rationale: "Only source with an actual operator decision (Q004) plus the explicit boundary classification (full_subagent_roster as open question, not doctrine)."
    coverage: "Q004 readiness criteria; phase2_implications write_as_doctrine vs write_as_boundary_or_open_question split."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Source of the unanswered agent_orchestration_index questions this page is scoped to, and of the explicit phase2_non_goals that forbid resolving them here."
    coverage: "agent_orchestration_index core_questions; phase2_non_goals section 7."
  - source_id: "wiki/concepts/persistent-agent-boundary"
    rationale: "Prior partial KB coverage already places the final agent roster outside this compile step; this page extends, not replaces, that boundary."
    coverage: "Existing concept-level statement that the final roster is out of S6 scope."
```

## Macro / Meso / Micro

### Macro

The `agent_orchestration_index` is one of the compile plan's six specialized
indexes (section 4), and it is the one most directly about *which agents
should exist*. At the macro level, the corpus supports building a
**decision procedure** for agent readiness, but not a **decision** about any
specific roster. The operator review reinforces this split explicitly by
sorting `full_subagent_roster` into the boundary/open-question bucket rather
than the doctrine bucket.

### Meso

Two things move at different speeds here. Readiness *criteria* moved to
"validated" status in the Phase 1 operator review (Q004) and can be treated
as source-backed doctrine with medium-high confidence. The *roster* — which
concrete recurring roles graduate from skill/workflow/subagent into a
persistent production agent — has not moved at all; it stays exactly where
Phase 1 left it: an open question requiring further operator input, likely
after real usage evidence accumulates (recurrence, validation need,
coordination-overhead observations).

### Micro

- Compile plan lines 58-68: `agent_orchestration_index` core questions,
  unanswered by this compile.
- `operator-phase1-review-decisions-20260702.md` Q004 (lines 74-84):
  persistent_when / ephemeral_when criteria, answer status "validated."
- `operator-phase1-review-decisions-20260702.md` section 3 (lines 132-138):
  `full_subagent_roster` listed under `write_as_boundary_or_open_question`.
- Compile plan section 7 (lines 199-211): `phase2_non_goals` including
  `final_named_agent_implementation` and `production_runtime_setup`.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: >
      Operator decision Q004 validated general persistent-vs-ephemeral
      readiness criteria for subagents: persistent when a role shows repeated
      domain recurrence, a stable validation/audit responsibility, or is a
      security-sensitive repo executor with explicit constraints; ephemeral
      for one-off source scouting, temporary comparison reading, or broad
      exploration.
    source_pointer: "operator-phase1-review-decisions-20260702.md Q004"
    confidence: high
    claim_label: source_backed_summary
    used_in_pages: []
  - claim_id: C002
    claim: >
      The full subagent/production-agent roster is explicitly classified as
      an open question/boundary item, not as Phase 2 doctrine, in the
      operator's Phase 1 review.
    source_pointer: "operator-phase1-review-decisions-20260702.md phase2_implications, write_as_boundary_or_open_question"
    confidence: high
    claim_label: source_backed_summary
    used_in_pages: []
  - claim_id: C003
    claim: >
      A candidate role should be tracked as a short, deferred record and
      checked against the Q004 readiness criteria over time, rather than
      being declared a production agent directly from this KB compile.
    source_pointer: "synthesis of agent_orchestration_index core questions, operator decision Q004, and phase2_non_goals"
    confidence: medium
    claim_label: working_hypothesis
    used_in_pages: []
  - claim_id: C004
    claim: >
      Phase 2 of this KB compile must not produce a final named production
      agent roster or an operational agent implementation.
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md section 7, phase2_non_goals"
    confidence: high
    claim_label: source_backed_summary
    used_in_pages: []
```

## Routes Here

```yaml
routes:
  - question: "Which Apex subprocesses should become permanent agents versus skills or ephemeral subagents?"
    leads_to: "claude-code-orchestration-design/wiki/concepts/persistent-agent-vs-ephemeral-subagent.md"
    rationale: "That concept page holds the general persistent-vs-ephemeral distinction this summary applies to the unresolved roster question."
  - related_page: "claude-code-orchestration-design/wiki/concepts/production-agent-readiness-gate.md"
    relation: "The readiness-gate criteria summarized here (Q004) are detailed further in that concept page."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: >
      The smallest useful permanent agent set is an open
      agent_orchestration_index question with no resolved answer in this KB.
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md agent_orchestration_index core_questions, lines 58-60"
    proposed_handling: ask_operator
  - id: U002
    description: >
      The full subagent/production-agent roster is explicitly deferred per
      the operator decision log and must not be treated as settled by any
      future reader of this page.
    source_pointer: "operator-phase1-review-decisions-20260702.md phase2_implications"
    proposed_handling: planning_task_candidate
  - id: U003
    description: >
      When adding an agent creates coordination overhead versus improves the
      system is an unresolved general criterion; no threshold or heuristic
      has been established beyond the Q004 persistent/ephemeral distinction.
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md agent_orchestration_index core_questions"
    proposed_handling: revisit_source
```

This page extends `persistent-agent-boundary.md` and
`persistent-agent-vs-ephemeral-subagent.md` without editing them, and it
should not be read as declaring a final production agent roster.
