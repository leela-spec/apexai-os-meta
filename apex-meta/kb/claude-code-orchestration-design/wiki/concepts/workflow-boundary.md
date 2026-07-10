---
title: "Workflow Boundary"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "workflow-boundary"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 112-123; process becomes workflow"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C001 through B04-C008; stage-gated workflow"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "medium"
claim_label: "behavioral_inference"
status: "active"
related_concepts: []
related_entities: []
review_flags: []
---

# Workflow Boundary

## Definition

A "workflow" in this KB names an orchestration-level design category, not a native Claude Code file type: it is a multi-stage, gated chain of skills and artifacts where each stage has its own reads, writes, and completion gate, as opposed to a single skill that can safely produce one bounded artifact end to end. Claude Code itself treats commands and skills as the same underlying mechanism (`phase1-batch02-claude-code-orchestration-surface.md`, claim B02-C001), so "workflow" is the compiled-KB's name for a pattern of chaining several such mechanisms together, not a distinct primitive Claude Code ships. This concept answers the compile plan's `claude_mechanism_mapping_index` question `when_a_process_becomes_a_workflow` and grounds the `weekly_routine_case_index` question `why_the_routine_is_a_workflow_not_a_single_skill`.

## Operating Rules

```yaml
rules:
  - "Use a workflow when a process spans multiple ordered stages with stage-specific reads and writes, and no single skill can safely own the whole span."
  - "Do not use a workflow when one concise skill can produce the needed artifact end-to-end without an intervening gate."
  - "Each stage should read only its own input packet/prior-stage artifact and emit one bounded output artifact, not replay full process history."
  - "An explicit gate sits between stages so a downstream stage cannot start from an unapproved or incomplete upstream artifact."
reads:
  - "stage inputs and prior-stage artifacts"
writes:
  - "stage outputs and handoff packets"
token_efficiency: "Each stage reads only its own packet and emits a bounded artifact, instead of every stage re-reading the full prior history."
drift_controls: "Gates prevent stage collapse (skipping ahead) and prevent premature use of an artifact that has not been approved."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Names the exact core questions this concept answers: when_a_process_becomes_a_workflow (claude_mechanism_mapping_index) and why_the_routine_is_a_workflow_not_a_single_skill (weekly_routine_case_index)."
    coverage: "Defines the specialized-index questions a workflow-boundary page must resolve; does not itself resolve them."
  - source_id: "phase1-batch04-apex-application-patterns"
    rationale: "Supplies the concrete evidence pattern of a multi-stage loop mapped into gated, artifact-connected skills."
    coverage: "Claims B04-C001 (loop mapped to discrete skills), B04-C004 (artifact-contract connections), B04-C005 (operator gates), B04-C008 (bounded stage-gated execution preferred)."
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    rationale: "Establishes that Claude Code has no separate native 'workflow' file type, which is why this KB treats 'workflow' as a design-level category rather than a platform primitive."
    coverage: "Claims B02-C001 (commands/skills convergence) and B02-C016 (naming tension between legacy commands/ and skills)."
```

## Macro / Meso / Micro

### Macro

Claude Code does not expose a distinct "workflow" primitive separate from skills and commands; it treats custom commands and skills as the same underlying mechanism, with skills adding supporting files, frontmatter, and automatic loading (B02-C001). Because of this, "workflow" in this KB is a compiled design-level label for a recognizable pattern — several skills or stages chained together with gates — rather than a thing Claude Code ships. This is exactly the distinction the compile plan's `claude_mechanism_mapping_index` raises with `when_a_process_becomes_a_workflow`, and it is the same distinction the `weekly_routine_case_index` raises when it asks why a recurring routine counts as a workflow rather than a single skill.

### Meso

The apex-application-patterns batch gives the concrete shape of that pattern. Apex maps the PreCap/FlowRecap/APSU loop into discrete Claude skills, while the operator-only step (`OperatorExecutesPlannedFlow`) stays a human action with a documented output contract rather than a skill file (B04-C001). Those skills are connected by artifact contracts rather than direct calls — one skill writes an artifact to a canonical slot and a downstream skill reads it (B04-C004) — and operator gates are a first-class design rule: skills must pause for explicit approval before downstream use when validation is required (B04-C005). Bounded, stage-gated, artifact-centered execution is preferred over broad autonomy or one giant multi-phase prompt (B04-C008). Put together, this is the operational definition of a workflow: several distinct, gated stages, not one skill trying to absorb the whole process.

### Micro

- B04-C001: PreCap/FlowRecap/APSU loop mapped to discrete skills; `OperatorExecutesPlannedFlow` remains human, not a skill file.
- B04-C004: skills connected by artifact contracts (write-to-slot / read-from-slot), not direct calls.
- B04-C005: operator gates pause downstream use pending explicit approval.
- B04-C008: bounded, stage-gated, artifact-centered execution preferred over broad autonomy.
- B02-C001: Claude Code treats commands and skills as the same underlying mechanism — there is no native "workflow" file kind to point to instead.
- B02-C016: legacy `commands/` files still work but are not recommended as first-class long-term architecture, which is part of why "workflow" must be defined at the KB design level rather than borrowed from a single Claude Code file type.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "A workflow denotes a multi-stage, gated chain of skills/artifacts rather than a distinct Claude Code file mechanism; Claude Code itself treats skills and commands as the same underlying mechanism."
    source_pointer: "phase1-batch02-claude-code-orchestration-surface.md, claim B02-C001"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "Apex's recurring loops are represented as workflows because each stage is a distinct skill connected by artifact contracts and operator gates, not a single skill call."
    source_pointer: "phase1-batch04-apex-application-patterns.md, claims B04-C001, B04-C004, B04-C005"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "Bounded, stage-gated, artifact-centered execution is the preferred shape for a workflow over broad autonomy or one large multi-phase prompt."
    source_pointer: "phase1-batch04-apex-application-patterns.md, claim B04-C008"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C004
    claim: "The compile plan's weekly_routine_case_index still lists 'why the routine is a workflow not a single skill' as an open core question to be answered by Phase 2 synthesis, not as a claim Phase 1 already closed."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md, weekly_routine_case_index core_questions"
    confidence: "medium"
    claim_label: "working_hypothesis"
```

## Routes Here

```yaml
routes:
  - question: "Why is the weekly routine a workflow instead of one skill?"
    leads_to: "claude-code-orchestration-design/concepts/weekly-routine-workflow-case.md"
    rationale: "That page applies this general workflow-boundary pattern to the specific recurring-routine case study."
  - question: "When should a procedure be a skill instead of a multi-stage workflow?"
    leads_to: "claude-code-orchestration-design/concepts/skill-boundary.md"
    rationale: "Skill-boundary is the complementary concept: the smaller-grain decision that workflow-boundary sits above."
  - related_page: "claude-code-orchestration-design/concepts/mechanism-ladder.md"
    relation: "Mechanism-ladder places workflow among the other mechanism choices (skill, subagent, script, hook) this concept helps distinguish."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_pointer: "claim B02-C001"
    supports: "Claim that Claude Code has no separate native workflow primitive."
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_pointer: "claim B02-C016"
    supports: "Naming tension between legacy commands/ and skills that motivates a KB-level 'workflow' label."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claims B04-C001, B04-C004, B04-C005, B04-C008"
    supports: "Concrete evidence pattern of a workflow as gated, artifact-connected skill stages."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "claude_mechanism_mapping_index: when_a_process_becomes_a_workflow; weekly_routine_case_index: why_the_routine_is_a_workflow_not_a_single_skill"
    supports: "Frames the exact open questions this concept must answer."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Whether 'workflow' should ever become an actual first-class Claude Code artifact type, versus remaining a KB-level design category layered over skills/commands, is unresolved."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md, claude_mechanism_mapping_index"
    proposed_handling: "revisit_source"
  - id: U002
    description: "The weekly_routine_case_index's own question 'why_the_routine_is_a_workflow_not_a_single_skill' remains listed as a core question in the compile plan rather than a fully answered claim; this page states the general pattern but does not close that specific case."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md, weekly_routine_case_index core_questions"
    proposed_handling: "planning_task_candidate"
```
