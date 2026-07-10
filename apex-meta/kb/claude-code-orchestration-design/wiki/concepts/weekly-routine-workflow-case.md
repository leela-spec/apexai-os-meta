---
title: "Weekly Routine Workflow Case"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "weekly-routine-workflow-case"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 99-111; weekly_routine_case_index"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C001 through B04-C005; Apex loop and gates"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "medium"
claim_label: "working_hypothesis"
status: "active"
related_concepts:
  - "weekly-plan-packet"
  - "flow-recap-packet"
  - "status-merge-packet"
  - "ephemeral-subagent-boundary"
related_entities:
  - "precap-week"
  - "precap-next-day"
  - "flow-recap-skill"
  - "all-project-status-packet-update"
review_flags:
  - "most weekly_routine_case_index questions are Phase 2 synthesis, not answered by name in Batch 04"
  - "compile-plan section 7 explicitly lists final_weekly_routine_build as a Phase 2 non-goal"
---

# Weekly Routine Workflow Case

## Definition

The weekly routine workflow case is Apex's worked example of applying the KB's general orchestration model — plan, execute, recap, merge, reseed — to a recurring weekly and daily planning loop. It exists to answer the `weekly_routine_case_index` in full: which parts are generic orchestration stages versus specific to this routine, why the routine is a workflow rather than a single skill, which subprocedures could become skills, where ephemeral subagents help, and which steps remain operator-gated. It is a case study, not a specification: the compile plan explicitly lists `final_weekly_routine_build` as a Phase 2 non-goal.

## Operating Rules

```yaml
rules:
  - "Generic orchestration stages (planning, execution, recap/evidence capture, status merge, context reseed) are reusable across any recurring routine, not unique to the weekly cycle."
  - "The routine must remain a multi-stage workflow (PreCapWeek -> PreCapNextDay -> OperatorExecutesPlannedFlow -> FlowRecapSkill -> APSU) rather than a single monolithic skill, because each stage has a distinct owner and artifact contract, and at least one stage is a required human action."
  - "Bounded subprocedures with a clear artifact-in/artifact-out contract (e.g., recap digesting, status merging) are skill candidates; stages requiring judgment across the whole loop, or requiring human execution, are not."
  - "OperatorExecutesPlannedFlow remains explicitly a human action with a documented output contract, not a skill file (B04-C001) — the clearest operator-gated step in the loop."
  - "Other transitions (for example, promoting a recap into accepted status) should be gated per B04-C005's rule to pause for explicit approval when validation is required."
  - "Raw per-day flow evidence must be digested into compact recap packets before being merged into status, to prevent raw dumps from bloating future context."
  - "This page must stay a case-study/pattern reference; it must not become a specification for building the actual weekly routine (compile plan section 7, phase2_non_goals)."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch04-apex-application-patterns"
    rationale: "Supplies the actual PreCap/FlowRecap/APSU entity mapping and the generic skill-shape and operator-gate rules that this case study applies to a concrete loop."
    coverage: "B04-C001 through B04-C005; PreCapWeek, PreCapNextDay, FlowRecapSkill, and APSU entity roles."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Defines the full weekly_routine_case_index question set this page is organized to answer, and the explicit non-goal warning against building the routine itself."
    coverage: "weekly_routine_case_index core questions; section 3 corrected-compile-objective warning; section 7 phase2_non_goals."
```

## Macro / Meso / Micro

### Macro

The `weekly_routine_case_index` treats the Apex weekly/daily loop (PreCapWeek, PreCapNextDay, OperatorExecutesPlannedFlow, FlowRecapSkill, APSU) as a case study for the KB's general orchestration model. The compile plan (section 3) explicitly warns that this KB must compile abstract, source-grounded orchestration knowledge rather than a premature implementation of the weekly routine itself — so this page's purpose is to check the KB's layering and packet patterns against one concrete recurring process, not to build that process.

### Meso

B04-C001 establishes the actual stage mapping: the PreCap/FlowRecap/APSU loop is mapped to discrete Claude skills, with `OperatorExecutesPlannedFlow` deliberately left as a human action rather than a skill file. B04-C002 and B04-C003 supply the generic skill-shape rules (routing metadata plus a concise objective plus a numbered, artifact-focused procedure ending in a completion gate; descriptions that name exact input/output artifacts and a boundary clause) that any one stage in this loop should follow. B04-C004 supplies the generic artifact-contract rule connecting stages, and B04-C005 supplies the generic operator-gate rule. The stage-specific packet types this KB compiles separately — weekly plan packet, flow packet/flow recap packet, status merge packet, next-cycle context — are the Phase 2 pages that instantiate this general model onto the specific loop.

### Micro

Most of the weekly_routine_case_index's exact questions — why the routine is a workflow and not a single skill, which subprocedures could become skills, where ephemeral subagents help — are not answered by name in Batch 04. Batch 04 supplies the raw material (the PreCap/FlowRecap/APSU entities, the artifact-contract and operator-gate claims), but the specific reasoning about workflow-versus-skill boundaries and ephemeral-subagent placement for this case is Phase 2 synthesis, extending the KB's general `ephemeral-subagent-boundary` concept to this specific loop rather than citing a Batch 04 claim that names subagents for it.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Apex maps the PreCap/FlowRecap/APSU loop into discrete Claude skills, while OperatorExecutesPlannedFlow remains a human action with a documented output contract rather than a skill file."
    source_pointer: "B04-C001 (Apex_Alfred_Skill_Definition_Guide.md lines 5-18)"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "Skills are connected by artifact contracts (not direct calls), and skill files should separate routing metadata, objective, and a numbered, artifact-focused procedure ending in a completion gate."
    source_pointer: "B04-C002, B04-C004 (Apex_Alfred_Skill_Definition_Guide.md lines 21-43, 76-107)"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "Operator gates are first-class: any stage transition requiring validation should pause for explicit operator approval."
    source_pointer: "B04-C005 (Apex_Alfred_Skill_Definition_Guide.md lines 108-120)"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C004
    claim: "The routine should be treated as a multi-stage workflow rather than a single skill because its stages have distinct owners, artifact contracts, and at least one required human-execution step; this specific 'why a workflow' reasoning is a Phase 2 working hypothesis built from B04-C001/C004/C005, not a directly stated Batch 04 claim."
    source_pointer: "phase2-specialized-index-compile-plan-20260702 lines 99-104 (why_the_routine_is_a_workflow_not_a_single_skill)"
    confidence: "medium"
    claim_label: "working_hypothesis"
  - claim_id: C005
    claim: "Ephemeral subagents plausibly help at bounded, context-isolable subprocedures (for example, digesting one day's raw flow evidence) but this placement is inferred from the KB's general ephemeral-subagent-boundary concept and the compile plan's index question, not from a Batch 04 claim naming subagents for this loop."
    source_pointer: "phase2-specialized-index-compile-plan-20260702 lines 104-105 (where_ephemeral_subagents_help)"
    confidence: "medium"
    claim_label: "working_hypothesis"
```

## Routes Here

```yaml
routes:
  - question: "Is the weekly routine one skill or several, and why?"
    leads_to: "claude-code-orchestration-design/concepts/weekly-plan-packet.md"
    rationale: "Weekly-plan-packet is the first stage artifact in this case study's workflow chain."
  - related_page: "claude-code-orchestration-design/concepts/flow-recap-packet.md"
    relation: "The recap-stage artifact this case study's FlowRecapSkill produces."
  - related_page: "claude-code-orchestration-design/concepts/status-merge-packet.md"
    relation: "The merge-stage artifact this case study's APSU produces."
  - related_page: "claude-code-orchestration-design/concepts/ephemeral-subagent-boundary.md"
    relation: "The general boundary this case applies when asking where ephemeral subagents help."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "B04-C001"
    supports: "PreCap/FlowRecap/APSU loop mapping and OperatorExecutesPlannedFlow as a human action."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "B04-C002, B04-C003, B04-C004"
    supports: "Generic skill-shape and artifact-contract rules applied to each loop stage."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "B04-C005"
    supports: "Generic operator-gate rule applied to loop transitions."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "entities_extracted 'precap-week', 'precap-next-day', 'flow-recap-skill', 'all-project-status-packet-update'"
    supports: "The named stages of the loop this case study examines."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "lines 97-108"
    supports: "Full weekly_routine_case_index question set this page answers."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "section 3, section 7"
    supports: "Non-goal warning against treating this KB as the final weekly routine implementation."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Most weekly_routine_case_index questions (workflow-vs-skill reasoning, subprocedure-to-skill mapping, ephemeral-subagent placement) are Phase 2 synthesis from the index question framework rather than verbatim Phase 1 claims; treat conclusions here as working hypotheses pending a dedicated case-study review."
    source_pointer: "phase2-specialized-index-compile-plan-20260702 lines 97-108"
    proposed_handling: "revisit_source"
  - id: U002
    description: "The compile plan explicitly lists 'final_weekly_routine_build' as a Phase 2 non-goal; this page must stay a case-study/pattern reference, not a specification for building the actual routine."
    source_pointer: "phase2-specialized-index-compile-plan-20260702 section 7"
    proposed_handling: "leave_as_gap"
  - id: U003
    description: "Which Apex processes should become skills versus rules versus operator actions remains an open question that directly affects which subprocedures in this case become skills."
    source_pointer: "B04-Q002"
    proposed_handling: "revisit_source"
```
