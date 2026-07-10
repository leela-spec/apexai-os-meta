---
title: "Mechanism Ladder"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "mechanism-ladder"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 112-123; mechanism mapping questions"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "claim B02-C014; layered control plane"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "hook-vs-skill-instruction"
  - "persistent-agent-vs-ephemeral-subagent"
  - "mcp-decision-model"
  - "plugin-deferment-rule"
related_entities: []
review_flags:
  - "The specific 'least powerful mechanism first' ordering is a working-hypothesis synthesis of B02-C014, not a verbatim source claim; see Uncertainty."
---

# Mechanism Ladder

## Definition

The mechanism ladder is the ordering principle that Apex should select the least powerful, least persistent, least trust-costly Claude Code mechanism that safely satisfies a given need, escalating only when a lighter mechanism is insufficient — from static artifacts and skills, through workflows and ephemeral subagents, up to persistent agents, scripts, hooks, plugins, and finally MCP. It generalizes the layered-control-plane interpretation of Claude Code's orchestration surface into a selection procedure for new work.

## Operating Rules

```yaml
rules:
  - "When choosing between artifact, skill, workflow, subagent, agent, script, hook, plugin, or MCP, select the lightest mechanism that safely satisfies the requirement rather than defaulting to the most powerful one available."
  - "Prefer static artifacts and skills over heavier persistent systems (agents, plugins, MCP) when the task is a one-off or a simple repeatable procedure."
  - "Escalate up the ladder only when a documented gap exists: e.g., a boundary needs deterministic enforcement (see hook-vs-skill-instruction), a role must persist across many tasks (see persistent-agent-vs-ephemeral-subagent), or the capability requires live external access (see mcp-decision-model)."
  - "Do not treat this page as mandating a final implementation surface; the final mechanism selection for any specific Apex capability is decided after KB compile and validation, not by this page alone."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    rationale: "B02-C014 is the primary interpretive claim establishing the layered control plane (guidance, procedures, enforcement, isolation, external tools, distribution) that this page reframes as an ordered selection ladder."
    coverage: "Layered control-plane interpretation spanning CLAUDE.md/rules, skills, hooks/settings, subagents, MCP, and plugins."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "The mechanism-mapping questions in this planning log are the direct compile-policy source for treating mechanism selection as an explicit, indexed decision rather than an implicit default."
    coverage: "Mechanism mapping questions used to route a given need to the appropriate Claude Code mechanism."
```

## Macro / Meso / Micro

### Macro

Claude Code offers many mechanisms for extending or constraining agent behavior, and each one carries a different cost profile: skills are cheap and easy to author but only guide behavior; hooks are more work to write but enforce deterministically; subagents isolate context but add coordination overhead; plugins and MCP add distribution and external-trust surface. The mechanism ladder names the discipline of matching the mechanism's cost to the actual requirement, so Apex does not reach for a persistent agent, a plugin, or an MCP server when a skill or a static artifact would do.

### Meso

In practice the ladder tracks the layered control plane described in B02-C014: `CLAUDE.md` and rules sit at the lightest, always-on guidance layer; skills sit above that as repeatable, invocable procedures; hooks and settings form the enforcement layer for boundaries that must hold regardless of model compliance; subagents add context isolation for exploratory or specialized work; plugins bundle multiple mechanisms for distribution; and MCP sits at the top as the mechanism for genuine external tool/data connectivity. Related concept pages operationalize specific rungs of this ladder: `hook-vs-skill-instruction` covers the guidance-vs-enforcement step, `persistent-agent-vs-ephemeral-subagent` covers the isolation/persistence step, `plugin-deferment-rule` and `mcp-decision-model` cover the distribution and external-connectivity steps.

### Micro

B02-C014 (label: interpretation, confidence: high) states: "Claude Code orchestration should be modeled as a layered control plane: CLAUDE.md and rules for always-on/path-scoped guidance; skills for repeatable procedures; hooks/settings for enforcement; subagents for context isolation; MCP for external tool surfaces; plugins for distributable bundles" (`phase1-batch02-claude-code-orchestration-surface.md` claim B02-C014). The `phase2-specialized-index-compile-plan-20260702.md` mechanism-mapping questions (lines 112-123) provide the compile-time routing logic referenced here, though that log was not part of the two source files re-read in full for this compile pass and its exact wording should be reopened if this page is challenged.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Claude Code orchestration should be modeled as a layered control plane: CLAUDE.md/rules for guidance, skills for repeatable procedures, hooks/settings for enforcement, subagents for context isolation, MCP for external tool surfaces, and plugins for distributable bundles."
    source_pointer: "phase1-batch02-claude-code-orchestration-surface.md claim B02-C014"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "Apex should reserve hooks and permissions for hard gates rather than relying on lighter guidance mechanisms, which implies a cost-ordering among mechanisms (guidance is cheaper but weaker; hooks are costlier but deterministic)."
    source_pointer: "phase1-batch02-claude-code-orchestration-surface.md claim B02-C015"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "The final implementation surface (which specific mechanism is used for a given Apex capability) is decided after KB compile and validation, not fixed by this concept page."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md lines 112-123 (mechanism mapping questions)"
    confidence: "medium"
    claim_label: "source_backed_summary"
```

## Routes Here

```yaml
routes:
  - question: "What Claude Code mechanism should we use for this new capability — skill, subagent, hook, plugin, or MCP?"
    leads_to: "claude-code-orchestration-design/concepts/mechanism-ladder.md"
    rationale: "This page is the general routing point for mechanism selection before drilling into a specific rung's concept page."
  - related_page: "claude-code-orchestration-design/concepts/hook-vs-skill-instruction.md"
    relation: "Specializes the guidance-vs-enforcement rung of the ladder."
  - related_page: "claude-code-orchestration-design/concepts/persistent-agent-vs-ephemeral-subagent.md"
    relation: "Specializes the context-isolation/persistence rung of the ladder."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_pointer: "B02-C014, B02-C015"
    supports: "Layered control-plane framing and the guidance-vs-enforcement cost distinction underlying the ladder ordering."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "lines 112-123 mechanism mapping questions"
    supports: "Compile-policy basis for treating mechanism selection as an explicit, indexed decision."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Working hypothesis: the specific 'ladder' ordering (artifact/skill before workflow/subagent before agent/script before hook/plugin/MCP) is a synthesized generalization of B02-C014's layered control plane, not a verbatim claim in the batch file. Treat the exact rung order as inferential rather than a directly source-stated sequence."
    source_pointer: "phase1-batch02-claude-code-orchestration-surface.md claim B02-C014"
    proposed_handling: "ask_operator"
  - id: U002
    description: "The mechanism-mapping questions in the referenced planning log (lines 112-123) were not re-read in full during this compile pass; verify exact wording if this page's routing logic is challenged."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md lines 112-123"
    proposed_handling: "revisit_source"
  - id: U003
    description: "Final implementation surface per capability remains undecided; this page should not be read as pre-committing Apex to a specific mechanism for any named capability."
    source_pointer: "operator-phase1-review-decisions-20260702.md phase2_implications.avoid_in_phase2"
    proposed_handling: "leave_as_gap"
```
