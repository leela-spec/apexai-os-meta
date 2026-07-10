---
title: "Claude Code Workflows"
page_type: entity
kb_slug: "claude-code-orchestration-design"
entity_slug: "claude-code-workflows"
entity_type: "runtime_component"
source_refs:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "source scope; Claude Code control plane"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C001 through B04-C008; staged processes"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "claude-code-orchestration-design/concepts/deterministic-script-boundary.md"
review_flags:
  - "workflow is not a sharply separated Claude Code entity in the ingested sources; see Uncertainty"
---

# Claude Code Workflows

## Identity

```yaml
entity:
  label: "Claude Code workflows"
  type: "runtime_component"
  aliases:
    - "multi-stage processes"
    - "commands/workflows/ (external repo convention)"
```

## Source-Grounded Summary

This page is deliberately hedged: the ingested sources do not establish "workflow" as a distinct, sharply-bounded Claude Code mechanism the way skills, hooks, subagents, plugins, and MCP are. `.claude/` is documented as the project-level surface for settings, hooks, rules, skills, agents, workflows, output styles, and other project-specific extensions (B02-C010) — so "workflows" appears as one named folder/category inside the control plane, but Claude Code has also merged custom commands into skills for new work (B02-C001), and the skill/command convergence is itself flagged as an unresolved naming tension for Apex (B02-C016). Separately, Apex's own application patterns describe multi-stage processes — the PreCap/FlowRecap/APSU loop — as a sequence mapped into discrete Claude Code *skills* connected by artifact contracts, with the human-executed step remaining outside any skill file entirely (B04-C001, B04-C004). Bounded, stage-gated, artifact-centered execution is explicitly preferred over broad autonomy or one giant multi-phase prompt (B04-C008). Taken together, the evidence supports "workflow" as a *pattern* (an ordered, gated, multi-stage process) rather than as a first-class Claude Code runtime entity distinct from skills.

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    rationale: "Only primary-docs evidence that names 'workflows' as a category within the .claude/ directory; also the source of the skill/command convergence claim that bounds this page's honesty caveat."
    coverage: "B02-C001 skill/command convergence; B02-C010 .claude/ directory contents including workflows; B02-C016 contradiction on command/skill naming."
  - source_id: "phase1-batch04-apex-application-patterns"
    rationale: "Only source describing an actual multi-stage Apex process (PreCap/FlowRecap/APSU) and its explicit preference for stage-gated over broad-workflow execution."
    coverage: "B04-C001 loop-to-skill mapping; B04-C004 artifact-contract connection; B04-C008 bounded stage-gated execution preference."
```

## Macro / Meso / Micro

### Macro

There is no clean, single Claude Code "workflow" entity in the ingested corpus. What exists is (a) a `workflows` folder/category listed alongside skills and agents inside `.claude/` (B02-C010), and (b) a general pattern — seen in Apex's own multi-stage processes — of chaining discrete skills together via artifacts and gates rather than writing one large orchestration file (B04-C001, B04-C004, B04-C008). This page therefore documents "workflow" as a *pattern for composing skills*, not as a distinct runtime mechanism with its own contract the way hooks or subagents have.

### Meso

Two forces push toward treating workflows as a composition pattern rather than a separate mechanism. First, Claude Code's skill/command convergence (B02-C001) absorbed what used to be separate "command" files into the skill mechanism; anything that used to be called a multi-step "workflow command" is now, architecturally, a skill (or a set of skills). Second, Apex's own operational pattern for multi-stage work — the PreCap/FlowRecap/APSU loop — is explicitly implemented as a chain of discrete skills linked by artifact contracts, with bounded, stage-gated, artifact-centered execution favored over broad autonomy or large multi-phase prompts (B04-C001, B04-C002, B04-C008). Neither source describes a distinct "workflow" runtime object with its own frontmatter, lifecycle, or enforcement semantics comparable to hooks or subagents.

### Micro

Source pointers: `primary-code-claude-com-docs-en-claude-directory.md.md` lines 7-10 (`.claude/` contents including workflows), lines 30-39; `primary-code-claude-com-docs-en-skills.md.md` lines 11-22 (command/skill convergence); `Apex_Alfred_Skill_Definition_Guide.md` lines 5-18 (loop-to-skill mapping), lines 94-107 (artifact contracts); `BEST_PRACTICES_v_old.md` lines 74-92 (bounded stage-gated execution preferred).

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: ".claude/ is the project-level surface for settings, hooks, rules, skills, agents, workflows, output styles, and other project-specific extensions; CLAUDE.md is session guidance rather than an enforcement surface."
    source_pointer: "B02-C010; primary-code-claude-com-docs-en-claude-directory.md.md lines 7-10, 30-39, 101-141"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "Apex maps the PreCap/FlowRecap/APSU loop into discrete Claude skills, while OperatorExecutesPlannedFlow remains a human action with a documented output contract rather than a skill file — i.e. a multi-stage process implemented as chained skills, not as a distinct 'workflow' object."
    source_pointer: "B04-C001; Apex_Alfred_Skill_Definition_Guide.md lines 5-18"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "Bounded, stage-gated, artifact-centered execution is preferred over broad autonomy or giant multi-phase prompts in subscription-chat or handoff contexts."
    source_pointer: "B04-C008; BEST_PRACTICES_v_old.md lines 74-92"
    confidence: "high"
    claim_label: "source_backed_summary"
```

## Routes Here

```yaml
routes:
  - question: "When does a process need to become a multi-stage workflow instead of one skill?"
    leads_to: "claude-code-orchestration-design/summaries/claude-mechanism-decision-model.md"
    rationale: "The mechanism-decision model treats 'workflow' as a rung on the ladder even though the underlying Claude Code entity is unresolved; this page supplies the honesty caveat behind that rung."
  - related_page: "claude-code-orchestration-design/entities/claude-code-skills.md"
    relation: "Workflows and skills converge under B02-C001/B02-C016; the skills page is the more sharply defined entity that workflows compose from."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_pointer: "B02-C010"
    supports: "workflows named as a .claude/ directory category"
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_pointer: "B02-C001, B02-C016"
    supports: "skill/command convergence bounding workflow's distinctness"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "B04-C001, B04-C004, B04-C008"
    supports: "workflow as a chained-skill, artifact-gated composition pattern"
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "'Workflow' as a distinct Claude Code entity is not sharply separated from skills/commands in the ingested sources: Claude Code merged commands into skills (B02-C001), and B02-C016 flags this as an unresolved naming tension for Apex. This page should not be read as evidence of a first-class 'workflow' runtime object with its own contract."
    source_pointer: "B02-C001; B02-C016"
    proposed_handling: "revisit_source"
  - id: U002
    description: "Which Apex processes should be represented as Claude Code skills, which should be rules or reference skills, and which should remain human/operator actions only? (B04-Q002, open question)"
    source_pointer: "B04-Q002"
    proposed_handling: "planning_task_candidate"
  - id: U003
    description: "There is a tension between prompt/workflow artifact completeness and SKILL.md concision (B04-T001): Apex needs detailed contracts, but sources converge on keeping activation files compact and moving dense schemas into appendices."
    source_pointer: "B04-T001"
    proposed_handling: "leave_as_gap"
```
