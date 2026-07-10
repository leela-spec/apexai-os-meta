---
title: "Agent vs Subagent vs Skill"
page_type: summary
kb_slug: "claude-code-orchestration-design"
summary_slug: "agent-vs-subagent-vs-skill"
source_refs:
  - source_id: "claude-code-sub-agents-doc"
    source_path: "raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-sub-agents.md.md"
    source_hash: "68e6bee3a7cf8fd5"
    source_pointer: "lines 655-794, Work with subagents / Choose between subagents and main conversation"
    source_storage_mode: "pointer_only"
  - source_id: "claude-code-skills-doc"
    source_path: "raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-skills.md.md"
    source_hash: "d3680aaafea31f59"
    source_pointer: "lines 5-45, Extend Claude with skills / Bundled skills"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "14412344bddf7838"
    source_pointer: "claims B02-C008 through B02-C010"
    source_storage_mode: "pointer_only"
created_at: "2026-07-10T21:00:00Z"
updated_at: "2026-07-10T21:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Agent vs Subagent vs Skill

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source_id: "claude-code-sub-agents-doc"
    rationale: "Deterministic term-frequency ranking (topic-source-rankings.json) placed this file first for the topic's exact keyword set, with 231 keyword hits -- the highest of any raw file in the corpus."
    coverage: "Subagent invocation patterns, delegation model, decision criteria for subagent vs main conversation vs skill."
  - rank: 2
    source_id: "claude-code-skills-doc"
    rationale: "Second-ranked deterministic hit for skill-specific keywords; defines what a skill is and how it differs structurally from a subagent."
    coverage: "Skill definition, discovery, and invocation model."
```

## Macro / Meso / Micro

### Macro

Claude Code exposes three distinct mechanisms for delegating or structuring work, and they solve different problems rather than being interchangeable tiers of the same thing. A **subagent** is a separate, context-isolated worker with its own system prompt, tool restrictions, and model; a **skill** is a reusable instruction package (`SKILL.md`) that runs inside the *current* conversation's context, not a separate one; the **main conversation** is the default, unrestricted execution surface with no isolation and no reusable packaging. The choice is about where context isolation and reuse actually pay off, not about capability -- all three can call tools and reason.

### Meso

The source doc states the decision directly rather than leaving it inferred: use the **main conversation** when a task needs frequent back-and-forth, when multiple phases share significant context (planning, implementation, testing together), or when latency matters, since subagents "start fresh and may need time to gather context." Use a **subagent** when the task produces verbose output you don't want polluting your main context, when you want to enforce specific tool restrictions or permissions, or when the work is self-contained and can return a short summary. The doc explicitly redirects a third case away from subagents: "Consider Skills instead when you want reusable prompts or workflows that run in the main conversation context rather than isolated subagent context" -- i.e., a skill is the right choice specifically when isolation is *not* wanted but repeatability is.

### Micro

Concretely, subagents are invoked three ways that escalate in strength: naming the subagent in a natural-language prompt (Claude decides whether to delegate), an explicit `@`-mention (guarantees that specific subagent runs), or passing `--agent` with a subagent name on the CLI, or the equivalent `agent` setting (the entire session adopts that subagent's system prompt, tools, and model for its duration) (sub-agents doc lines 663-720). Skills, by contrast, are triggered by matching a `description` field in `SKILL.md` frontmatter against the request, or invoked directly with `/skill-name` (skills doc lines 9, 45-59) -- there is no equivalent of context isolation or a separate system prompt; the skill's instructions are read into the *same* conversation. This is the structural fact that explains most of the "when to use which" guidance: a subagent's isolation is a feature when you want to keep verbose output or a separate persona out of the main thread, and a limitation when the task needs the shared context a skill or the main conversation already has.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Use the main conversation over a subagent when the task needs frequent back-and-forth, when planning/implementation/testing phases share significant context, or when latency matters, because a subagent starts fresh and may need time to gather context."
    source_pointer: "primary-code-claude-com-docs-en-sub-agents.md.md lines 772-789"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "Use a subagent over the main conversation when the task produces verbose output that would pollute the main context, when specific tool restrictions/permissions must be enforced, or when the work is self-contained and can return a short summary."
    source_pointer: "primary-code-claude-com-docs-en-sub-agents.md.md lines 781-786"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "A skill is the right choice specifically when reusability is wanted but subagent-style context isolation is not -- skills execute inside the current conversation's context rather than a separate one."
    source_pointer: "primary-code-claude-com-docs-en-sub-agents.md.md line 787; primary-code-claude-com-docs-en-skills.md.md lines 9-45"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C004
    claim: "Subagents can be invoked with three escalating patterns -- natural-language name (Claude decides), explicit @-mention (guarantees that subagent), or --agent/session-wide setting (whole session adopts its system prompt, tools, and model) -- while skills are triggered by frontmatter description matching or direct /skill-name invocation, with no equivalent of a separate system prompt or context isolation."
    source_pointer: "primary-code-claude-com-docs-en-sub-agents.md.md lines 663-720; primary-code-claude-com-docs-en-skills.md.md lines 9, 45-59"
    confidence: "high"
    claim_label: "source_backed_summary"
```

## Routes Here

```yaml
routes:
  - question: "Should I use a subagent, a skill, or just the main conversation for this task?"
    leads_to: "wiki/summaries/agent-vs-subagent-vs-skill.md"
    rationale: "Direct decision criteria from the primary Claude Code documentation, not a generic restatement."
  - question: "Why does Claude Code have both skills and subagents when both can run instructions?"
    leads_to: "wiki/summaries/agent-vs-subagent-vs-skill.md"
    rationale: "Explains the structural difference (context isolation vs shared context) that the naming alone doesn't convey."
  - related_page: "wiki/entities/claude-code-subagents.md"
    relation: "Narrow entity page for subagents specifically; this summary covers the comparative decision."
  - related_page: "wiki/entities/claude-code-skills.md"
    relation: "Narrow entity page for skills specifically."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "This page synthesizes the documented decision criteria for Claude Code generally; it does not verify whether Apex's own skill packages (e.g. apex-kb) follow this guidance consistently in practice."
    proposed_handling: "revisit_source"
  - id: U002
    description: "Persistent agents (--agent flag, session-wide) and nested subagent spawning (v2.1.172+) are documented but not cross-checked against this KB's own persistent-agent-boundary and ephemeral-subagent-boundary concept pages for consistency."
    source_pointer: "primary-code-claude-com-docs-en-sub-agents.md.md lines 688-721, 791-794"
    proposed_handling: "audit_item"
