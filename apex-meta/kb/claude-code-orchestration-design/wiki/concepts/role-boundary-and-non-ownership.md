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
updated_at: "2026-07-10T20:00:00Z"
confidence: "medium"
claim_label: "working_hypothesis"
status: "active"
related_concepts:
  - "workflow-boundary"
  - "skill-boundary"
  - "owner-validator-split"
related_entities: []
review_flags: []
---

# Role Boundary and Non-Ownership

## Definition

Role boundary and non-ownership is the practice of stating, for any Apex role (skill, agent, workflow stage, verifier), both what it owns and what it explicitly must not own, before it executes. The concrete, directly-sourced instance of this is the prompt/workflow lane's boundary in B04-C006: it owns reusable prompt structures, workflow-stage patterns, bounded execution sequences, promptflow skeletons, handoff templates, source-authority wording, and out-of-mode improvement capture; it does not own orchestration authority, model/config routing authority, KB placement authority, QA severity, promotion approval, or config mutation. This page generalizes that lane-specific framing into an Apex-wide pattern, following the `agent_orchestration_index` core question `what_every_agent_owns_and_must_not_own` — that generalization is a working hypothesis, since no B04 claim states the non-ownership rule for roles in general, only for the prompt/workflow lane specifically.

## Operating Rules

```yaml
rules:
  - "Before a role executes, its skill/agent/workflow definition should state an explicit owns list and an explicit does-not-own list."
  - "Non-owned authority (orchestration, config mutation, promotion approval, QA severity, KB placement) must route to the role that does own it rather than being assumed or absorbed."
  - "A skill description functions as a routing key and should name exact input artifacts, exact output artifacts, and a boundary/non-purpose clause."
  - "A role that finds itself needing authority it does not own should stop and hand off, not quietly expand its own scope."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch04-apex-application-patterns"
    rationale: "Primary and most specific source: B04-C006 is a direct, explicit owns/does-not-own list for the prompt/workflow lane; B04-C003 supplies the parallel skill-level boundary/non-purpose clause requirement."
    coverage: "Claims B04-C003 (skill descriptions as routing keys with boundary/non-purpose clause) and B04-C006 (prompt/workflow lane owns/does-not-own list)."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Supplies the agent_orchestration_index question that motivates generalizing the lane-specific boundary into an Apex-wide role pattern."
    coverage: "agent_orchestration_index core_questions, lines 63-64, especially what_every_agent_owns_and_must_not_own."
```

## Macro / Meso / Micro

### Macro

The compile plan's `agent_orchestration_index` treats "what every agent owns and must not own" as a structural question for the whole orchestration system, alongside how build/validation/routing/authority are separated. Role boundary and non-ownership is the general name for the answer this KB gives to that question, built by generalizing a pattern that Phase 1 observed concretely in one lane.

### Meso

The only place in the ingested batch-04 corpus where an owns/does-not-own list is stated explicitly and in full is the prompt/workflow lane (B04-C006): it owns reusable prompt structures, workflow-stage patterns, bounded execution sequences, promptflow skeletons, handoff templates, source-authority wording, and out-of-mode improvement capture, and it explicitly does not own orchestration authority, model/config routing authority, KB placement authority, QA severity, promotion approval, or config mutation. B04-C003 supplies the parallel mechanism at the skill level: skill descriptions function as routing keys and should name exact input artifacts, exact output artifacts, and a boundary/non-purpose clause. Treating these two as instances of one general Apex pattern — rather than two unrelated local rules — is the interpretive step this page takes.

### Micro

`ESSENCE.md` lines 11-33 is the direct source for the prompt/workflow lane's owns/does-not-own list (B04-C006). `Apex_Alfred_Skill_Definition_Guide.md` lines 44-67 is the direct source for the skill-description boundary/non-purpose clause (B04-C003). The compile plan's `agent_orchestration_index` (lines 63-64) is where the generalized question `what_every_agent_owns_and_must_not_own` appears, alongside `how_build_validation_routing_and_authority_are_separated`.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "The prompt/workflow lane owns reusable prompt structures, workflow-stage patterns, bounded execution sequences, promptflow skeletons, handoff templates, source-authority wording, and out-of-mode improvement capture; it does not own orchestration authority, model/config routing authority, KB placement authority, QA severity, promotion approval, or config mutation."
    source_pointer: "phase1-batch04-apex-application-patterns claim B04-C006"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "Apex skill descriptions function as routing keys and should name exact input artifacts, exact output artifacts, and a boundary/non-purpose clause."
    source_pointer: "phase1-batch04-apex-application-patterns claim B04-C003"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "The owns/does-not-own boundary observed for the prompt/workflow lane generalizes to every Apex agent, skill, or workflow role, per the agent_orchestration_index's what_every_agent_owns_and_must_not_own core question; this generalization is inferred from the index framing, not stated for roles in general by any single B04 claim."
    source_pointer: "phase2-specialized-index-compile-plan-20260702 lines 63-64"
    confidence: "medium"
    claim_label: "working_hypothesis"
```

## Routes Here

```yaml
routes:
  - question: "What must every agent or skill explicitly not own, so it doesn't quietly expand into adjacent authority?"
    leads_to: "claude-code-orchestration-design/concepts/role-boundary-and-non-ownership.md"
    rationale: "Direct match to the agent_orchestration_index's what_every_agent_owns_and_must_not_own question."
  - related_page: "claude-code-orchestration-design/concepts/workflow-boundary.md"
    relation: "Sibling application of the same owns/does-not-own pattern at the workflow-stage level."
  - related_page: "claude-code-orchestration-design/concepts/skill-boundary.md"
    relation: "Sibling application of the same pattern at the individual-skill level, grounded in B04-C003's boundary/non-purpose clause."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C006"
    supports: "Definition and Meso section: the concrete owns/does-not-own list."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C003"
    supports: "Operating Rules and Meso section: skill-level boundary/non-purpose clause."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "agent_orchestration_index core_questions, lines 63-64"
    supports: "Macro section and Key Claim C003: generalization to all Apex roles."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Only the prompt/workflow lane has a fully explicit owns/does-not-own list in the ingested B04 corpus; generalizing this to 'every Apex role' is a working hypothesis driven by the agent_orchestration_index question rather than a directly quoted claim covering all roles. Confidence and claim_label are set to medium/working_hypothesis to reflect this."
    source_pointer: "phase1-batch04-apex-application-patterns claim B04-C006; phase2-specialized-index-compile-plan-20260702 lines 63-64"
    proposed_handling: "revisit_source"
  - id: U002
    description: "The specific roster of Apex roles (which agents/skills exist and what each one's owns/does-not-own list should say) is deferred beyond this compile pass."
    source_pointer: "phase2-specialized-index-compile-plan-20260702 phase2_non_goals, lines 199-211"
    proposed_handling: "leave_as_gap"
```
