---
title: "Weekly Routine as Orchestration Case Study"
page_type: summary
kb_slug: "claude-code-orchestration-design"
summary_slug: "weekly-routine-as-orchestration-case-study"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 99-111; weekly_routine_case_index questions"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C001 through B04-C019; entities extracted"
    source_storage_mode: "pointer_only"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "lines 100-122; prompt pack and HALT/CLARIFY decisions"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "weekly-routine-workflow-case"
  - "weekly-plan-packet"
  - "next-day-plan"
  - "flow-recap-packet"
  - "status-merge-packet"
related_entities:
  - "precap-week"
  - "precap-next-day"
  - "flow-recap-skill"
  - "all-project-status-packet-update"
review_flags: []
---

# Weekly Routine as Orchestration Case Study

## Core Summary

The weekly routine is treated in this KB as a **case study** for whether the
general orchestration model holds up under a recurring, multi-stage,
operator-gated workflow — not as the final implementation target. The
compile plan's `weekly_routine_case_index` (lines 99-111) frames the routine
around nine questions: which parts are generic orchestration stages, which
parts are specific to the weekly routine, why the routine is a workflow and
not a single skill, which subprocedures could be skills, where ephemeral
subagents help, which steps remain operator-gated, what each stage reads and
writes, canonical state versus temporary execution evidence, and how raw
dumps are prevented from bloating future context.

Batch 04's entities give the routine its concrete stage names. `PreCapWeek`
is the weekly strategic planning skill in the Apex orchestration loop;
`PreCapNextDay` is the daily executable planning skill that consumes weekly
direction and project state; `FlowRecapSkill` is the digest skill that
converts raw flow execution evidence into structured recap memory; and
`AllProjectStatusPacketUpdate` (APSU) is the status-merge process that
consumes flow recap packets and updates project status
(`phase1-batch04-apex-application-patterns.md` section 5, all confidence
medium). Claim B04-C001 places these stages in sequence and explicitly
excludes the human execution step: Apex maps the PreCap/FlowRecap/APSU loop
into discrete Claude skills, while `OperatorExecutesPlannedFlow` remains a
human action with a documented output contract rather than a skill file
(`Apex_Alfred_Skill_Definition_Guide.md` lines 5-18). This directly answers
"why the routine is a workflow, not a single skill": at least one stage is
not a skill at all, and the surrounding stages are separately triggerable
skills chained by artifact contracts (B04-C004), not steps inside one
monolithic skill body.

Operator decisions reinforce two doctrine points that shape how this case
study is compiled. Q007 validated one-prompt-pack-file-per-flow, with the
flow packet as the planning artifact and the prompt pack as the execution
artifact, the flow packet pointing to the prompt pack, and execution prompt
packs kept out of Apex KB wiki pages
(`operator-phase1-review-decisions-20260702.md` Q007). Q008 validated an
Apex-wide minimal core for HALT, CLARIFY, file-output proof, task-closure
proof, and fetch-back validation, with promptflow examples and flow-pack
conventions as local extensions (`operator-phase1-review-decisions-20260702.md`
Q008). Both bound what "how raw dumps are prevented from bloating future
context" and "what each stage reads and writes" can mean for this routine.

## What This Adds

```yaml
adds:
  - "Names the weekly-routine stages explicitly (PreCapWeek, PreCapNextDay, OperatorExecutesPlannedFlow, FlowRecapSkill, APSU) and orders them against the weekly_routine_case_index question set."
  - "Grounds 'why a workflow, not a single skill' directly in B04-C001 (a human-only stage exists) and B04-C004 (artifact-contract chaining between skills)."
  - "Ties the routine's token-economy behavior to two already-validated operator decisions (Q007 prompt-pack filing, Q008 HALT/CLARIFY/file-output core) rather than inventing new conventions."
clarifies:
  - "The routine is evidence for the general orchestration model, not a runtime spec to build from this KB compile."
limits:
  - "Does not fix the exact filesystem path for prompt packs (B04-Q001 remains open) or state a final list of which subprocedures become skills versus stay as workflow steps."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch04-apex-application-patterns"
    rationale: "Only source with the concrete weekly-routine stage entities (PreCapWeek, PreCapNextDay, FlowRecapSkill, APSU) and the claims describing their sequencing and artifact contracts."
    coverage: "Claims B04-C001 through B04-C019; entities precap-week, precap-next-day, flow-recap-skill, all-project-status-packet-update; concept apex-artifact-contract-handoff."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Source of the weekly_routine_case_index question set this page is structured to answer, and of the explicit instruction to treat the routine as a case study rather than a build target."
    coverage: "weekly_routine_case_index core_questions, lines 99-111; corrected_compile_objective section 3."
  - source_id: "operator-phase1-review-decisions-20260702"
    rationale: "Supplies the two operator decisions (Q007, Q008) that directly bound how the routine's artifacts and control signals should be represented."
    coverage: "Q007 prompt-pack-per-flow decision; Q008 Apex-wide HALT/CLARIFY/file-output/task-closure core."
```

## Macro / Meso / Micro

### Macro

The compile plan lists `M006_weekly_routine_as_case_study` as a cross-index
master question answered jointly by `weekly_routine_case_index`,
`project_execution_index`, and `agent_orchestration_index` (compile plan
lines 170-175). At the macro level, the routine is used to test whether the
KB's general claims about skills, artifact contracts, operator gates, and
state safety survive contact with a real recurring multi-stage process,
without letting that one process become the KB's definition of orchestration.

### Meso

Medium-level pattern across the stages: `PreCapWeek` produces a weekly plan
packet (canonical-ish, longer-lived state); `PreCapNextDay` reads that packet
plus current project state to produce a next-day plan and, per Q007, a
per-flow prompt-pack pointer; `OperatorExecutesPlannedFlow` is a human action
producing raw flow execution evidence (not a skill, per B04-C001);
`FlowRecapSkill` digests that raw evidence into a structured flow recap
packet, discarding raw dump bulk from future context; `APSU` merges the flow
recap packet into project status. Each transition is an artifact-contract
handoff (B04-C004), and B04-C005's operator-gate rule applies at whichever
stage boundaries require explicit approval before the next stage may consume
the artifact.

### Micro

- B04-C001: `Apex_Alfred_Skill_Definition_Guide.md` lines 5-18 — PreCap/
  FlowRecap/APSU loop mapped to skills; `OperatorExecutesPlannedFlow` stays a
  human action with a documented output contract.
- Entities (all confidence medium): `precap-week`, `precap-next-day`,
  `flow-recap-skill`, `all-project-status-packet-update`
  (`phase1-batch04-apex-application-patterns.md` section 5).
- Operator decision Q007: one-prompt-pack-file-per-flow; flow packet points
  to prompt pack; prompt packs excluded from KB wiki pages
  (`operator-phase1-review-decisions-20260702.md` lines 98-105).
- Operator decision Q008: Apex-wide minimal HALT/CLARIFY/file-output/
  task-closure/fetch-back core, with promptflow and flow-pack conventions as
  local extensions (`operator-phase1-review-decisions-20260702.md` lines
  107-119).
- Open question B04-Q001: canonical filesystem slot for per-flow prompt-pack
  artifacts remains unresolved in Claude-native Apex (`ESSENCE.md` lines
  15-24; `PROMPTFLOW_KB_BASE_BUILD.md` lines 54-64).

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: >
      Apex maps the PreCap/FlowRecap/APSU loop into discrete Claude skills,
      while OperatorExecutesPlannedFlow remains a human action with a
      documented output contract rather than a skill file.
    source_pointer: "phase1-batch04-apex-application-patterns.md claim B04-C001"
    confidence: high
    claim_label: source_backed_summary
    used_in_pages: []
  - claim_id: C002
    claim: >
      Apex skills, including the weekly-routine stages, are connected by
      artifact contracts rather than direct calls: one skill writes an
      artifact to a canonical/logical slot and downstream skills read that
      artifact.
    source_pointer: "phase1-batch04-apex-application-patterns.md claim B04-C004"
    confidence: high
    claim_label: source_backed_summary
    used_in_pages: []
  - claim_id: C003
    claim: >
      Apex uses one prompt-pack file per flow, with the flow packet as the
      planning artifact pointing to the prompt pack as the execution
      artifact; execution prompt packs are not placed inside Apex KB wiki
      pages.
    source_pointer: "operator-phase1-review-decisions-20260702.md Q007"
    confidence: high
    claim_label: source_backed_summary
    used_in_pages: []
  - claim_id: C004
    claim: >
      The weekly routine's stage sequence (PreCapWeek to PreCapNextDay to
      human execution to FlowRecapSkill to APSU) is a workflow rather than a
      single skill because it contains a non-skill human stage and multiple
      artifact-contract-chained skill stages, not because of any single
      documented "workflow" declaration in the sources.
    source_pointer: "synthesis of B04-C001 and B04-C004 against weekly_routine_case_index question 'why_the_routine_is_a_workflow_not_a_single_skill'"
    confidence: medium
    claim_label: working_hypothesis
    used_in_pages: []
```

## Routes Here

```yaml
routes:
  - question: "What is the general artifact-contract handoff pattern this routine is an instance of?"
    leads_to: "claude-code-orchestration-design/wiki/summaries/agent-handoff-and-contract-system.md"
    rationale: "The handoff-and-contract summary explains the general pattern that each weekly-routine stage transition instantiates."
  - related_page: "claude-code-orchestration-design/wiki/summaries/project-execution-state-safety-model.md"
    relation: "The routine's stage sequence is a concrete case of the planning / read-side computation / gated write-side mutation separation that page describes generally."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: >
      The canonical Apex filesystem slot for per-flow prompt-pack artifacts
      in the Claude-native version is unresolved; current evidence supports
      separate prompt-pack artifacts but no final path has been confirmed.
    source_pointer: "phase1-batch04-apex-application-patterns.md open question B04-Q001"
    proposed_handling: ask_operator
  - id: U002
    description: >
      Which Apex processes should be represented as Claude Code skills,
      which should be rules/reference skills, and which should remain
      human/operator-only actions is still open beyond the PreCap/FlowRecap/
      APSU mapping already established.
    source_pointer: "phase1-batch04-apex-application-patterns.md open question B04-Q002"
    proposed_handling: ask_operator
  - id: U003
    description: >
      Old OpenCLAW/MasterOfArts promptflow structures underlying some of
      this routine's source material use legacy paths and repo boundaries
      that must not be copied as current Apex runtime paths; only the
      process pattern is reusable.
    source_pointer: "phase1-batch04-apex-application-patterns.md tension B04-T003"
    proposed_handling: revisit_source
  - id: U004
    description: >
      Exact runtime paths, scheduler behavior, and process implementation
      for the weekly routine remain outside this compile step; this page is
      a pattern case, not an instruction to build PreCap, FlowRecap, APSU, or
      schedulers.
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md section 7, phase2_non_goals"
    proposed_handling: leave_as_gap
```
