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
updated_at: "2026-07-10T20:00:00Z"
confidence: "medium"
claim_label: "working_hypothesis"
status: "needs_review"
related_concepts: []
related_entities: []
review_flags: []
---

# Persistent Agent Boundary

## Definition

The persistent agent boundary is the (currently unresolved) line separating a role that justifies a durable, persistent Claude Code agent from a role that should stay ephemeral (a one-off subagent), or should not be an agent at all and instead remain a skill, workflow stage, or script. This concept exists to hold the compile plan's `agent_orchestration_index` question `persistent_agent_vs_ephemeral_subagent_vs_skill_vs_workflow_vs_script`. **This remains an open architectural question per the Phase 2 specialized index compile plan, not a settled Phase 1 claim.** Phase 1 supplies directional operator guidance (below), not a closed rule.

## Operating Rules

```yaml
rules:
  - "Treat persistence as directional guidance, not a closed rule, until agent_orchestration_index questions (smallest_useful_permanent_agent_set, coordination overhead, redundancy tolerance) are resolved."
  - "Candidate persistent_when signals: a repeated domain role, a stable validation/audit role, or a security-sensitive repo executor with explicit constraints."
  - "Candidate ephemeral_when signals: one-off source scouting, temporary comparison reading, or broad exploration."
  - "Do not treat any name in this cluster of pages as a final, accepted production-agent roster; the compile plan explicitly excludes final_named_agent_implementation from Phase 2."
reads:
  - "agent doctrine"
  - "activation seed"
  - "role-specific KB"
writes:
  - "bounded outputs"
  - "review candidates (not final roster entries)"
token_efficiency: "A persistent role's value is only realized if it is stable enough to amortize its own setup cost across repeated use; this remains to be validated per role."
drift_controls: "Non-ownership clauses and owner/validator separation are the guardrails proposed against role expansion, but their sufficiency is not yet demonstrated by Phase 1 evidence alone."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Primary source: lists persistent_agent_vs_ephemeral_subagent_vs_skill_vs_workflow_vs_script and smallest_useful_permanent_agent_set as open core questions of agent_orchestration_index, unresolved by Phase 1."
    coverage: "Defines the exact open question this page names; does not answer it."
  - source_id: "operator-phase1-review-decisions-20260702"
    rationale: "Gives the only concrete, though explicitly provisional, criteria available: persistent_when / ephemeral_when signals from operator decision Q004."
    coverage: "Q004_subagent_persistence decision and criteria lists; section 1 explicitly frames these as compile-policy direction, not a finished orchestration system."
```

## Macro / Meso / Micro

### Macro

The `agent_orchestration_index` frames persistence as an open cluster of questions rather than a settled design: what is an agent in this system, when is persistent agent status warranted versus ephemeral subagent/skill/workflow/script status, what is the smallest useful permanent agent set, and when does adding an agent help versus create coordination overhead. None of these are marked resolved in the compile plan; they are listed as `core_questions` for Phase 2 synthesis to work through, explicitly separate from any final agent build (the compile plan's non-goals list excludes `final_named_agent_implementation`).

### Meso

The one piece of concrete, source-grounded direction available is operator decision Q004, which gives directional (not final) criteria: persistent status is favored for a repeated domain role, a stable validation/audit role, or a security-sensitive repo executor with explicit constraints, while ephemeral status is favored for one-off scouting, temporary comparison reading, or broad exploration. Critically, the operator decision log states plainly that "these decisions do not mean Apex is building the final orchestration system now" — they are Phase 2 compile-policy direction telling the wiki compiler how to represent the knowledge, not a resolved production boundary.

### Micro

- Compile plan `agent_orchestration_index` core questions: `persistent_agent_vs_ephemeral_subagent_vs_skill_vs_workflow_vs_script`, `smallest_useful_permanent_agent_set`, `when_adding_an_agent_improves_the_system`, `when_adding_an_agent_creates_coordination_overhead` (compile plan lines ~57-64).
- Operator decision Q004 (`operator-phase1-review-decisions-20260702.md` lines 74-84): `persistent_when` = repeated domain role, stable validation/audit role, security-sensitive repo executor with explicit constraints; `ephemeral_when` = one-off source scouting, temporary comparison reading, broad exploration.
- Same file, section 1 (lines 13-17): explicit statement that these are Phase 2 compile-policy decisions, not a built orchestration system.
- Compile plan section 7 `phase2_non_goals`: `final_named_agent_implementation` excluded.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "agent_orchestration_index treats persistent_agent_vs_ephemeral_subagent_vs_skill_vs_workflow_vs_script and smallest_useful_permanent_agent_set as open core questions for Phase 2 synthesis, not settled Phase 1 findings."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md, agent_orchestration_index core_questions, lines 57-69"
    confidence: "medium"
    claim_label: "working_hypothesis"
  - claim_id: C002
    claim: "Operator decision Q004 gives directional (not final) criteria: persistent status fits a repeated domain role, a stable validation/audit role, or a security-sensitive repo executor with explicit constraints; ephemeral status fits one-off scouting, temporary comparison reading, or broad exploration."
    source_pointer: "operator-phase1-review-decisions-20260702.md lines 74-84"
    confidence: "medium"
    claim_label: "working_hypothesis"
  - claim_id: C003
    claim: "The compile plan explicitly excludes final_named_agent_implementation from Phase 2 scope, so no persistent-agent boundary drawn from this KB should be treated as final production doctrine at this stage."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md, section 7 phase2_non_goals, lines 199-211"
    confidence: "medium"
    claim_label: "working_hypothesis"
```

Only three claims are offered here, and all are framed as working hypotheses rather than settled facts: the underlying compile-plan questions this page answers are explicitly open, so a longer list of "confident" claims would misrepresent the source material.

## Routes Here

```yaml
routes:
  - question: "Has a candidate role cleared the bar for persistent production status?"
    leads_to: "claude-code-orchestration-design/concepts/production-agent-readiness-gate.md"
    rationale: "Production-agent-readiness-gate operationalizes this boundary into a staged check, equally unresolved."
  - question: "What distinguishes a persistent agent from a one-off subagent in general?"
    leads_to: "claude-code-orchestration-design/concepts/persistent-agent-vs-ephemeral-subagent.md"
    rationale: "That page covers the same distinction from the mechanism-selection angle (claude_mechanism_mapping_index) rather than the roster angle (agent_orchestration_index)."
  - related_page: "claude-code-orchestration-design/concepts/ephemeral-subagent-boundary.md"
    relation: "Describes the ephemeral side of the same unresolved boundary."
```

## Evidence

```yaml
evidence:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "agent_orchestration_index core_questions, lines 57-69"
    supports: "Definition and Macro section: the boundary is an open question, not a settled claim."
  - source_id: "operator-phase1-review-decisions-20260702"
    source_pointer: "Q004_subagent_persistence, lines 74-84; section 1, lines 13-17"
    supports: "Meso and Micro sections: directional criteria and the explicit non-final framing."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "This remains an open architectural question per the Phase 2 specialized index compile plan, not a settled Phase 1 claim: the exact line between persistent agent, ephemeral subagent, skill, workflow, and script is listed as a core_question of agent_orchestration_index and has not been closed."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md, agent_orchestration_index core_questions"
    proposed_handling: "ask_operator"
  - id: U002
    description: "smallest_useful_permanent_agent_set and when_adding_an_agent_creates_coordination_overhead remain unresolved; Q004's criteria are directional inputs, not a final scoring rule."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md, agent_orchestration_index core_questions"
    proposed_handling: "planning_task_candidate"
```
