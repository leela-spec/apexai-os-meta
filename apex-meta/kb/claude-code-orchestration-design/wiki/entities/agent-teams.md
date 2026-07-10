---
title: "Agent Teams"
page_type: entity
kb_slug: "claude-code-orchestration-design"
entity_slug: "agent-teams"
entity_type: "runtime_component"
source_refs:
  - source_id: "claude-code-agent-teams-doc"
    source_path: "raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-agent-teams.md.md"
    source_pointer: "lines 21-60, When to use agent teams / Compare with subagents / Enable agent teams"
    source_storage_mode: "pointer_only"
  - source_id: "apex-kb-skill-md"
    source_path: ".claude/skills/apex-kb/SKILL.md"
    source_pointer: "execution_surface_policy block"
    source_storage_mode: "pointer_only"
created_at: "2026-07-10T22:00:00Z"
updated_at: "2026-07-10T22:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Agent Teams

## Identity

```yaml
entity:
  label: "Agent Teams"
  type: "runtime_component"
  aliases: ["teammates", "team of Claude Code sessions"]
```

## Source-Grounded Summary

Agent teams are a Claude Code mechanism, disabled by default and enabled via `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`, where multiple independent Claude sessions ("teammates") coordinate through a shared task list and communicate with each other directly -- structurally different from a subagent, whose only communication path is reporting a result back to the spawning agent.

**Project-specific delta:** this KB's own `apex-kb` skill entrypoint (`.claude/skills/apex-kb/SKILL.md`, `execution_surface_policy`) currently defaults *all* semantic work to a single assistant/chat LLM, and reserves external terminal/Agent/Codex surfaces for deterministic execution only, requiring `semantic_delegation_requires: explicit_operator_override` before any semantic work leaves that single assistant. Agent teams' entire value proposition -- teammates independently interpreting and challenging each other's findings -- is exactly the kind of distributed semantic work this skill's policy currently keeps inside one assistant by default. No Apex skill in this KB is currently documented as using agent teams; this is not evidence they shouldn't, only that no such usage has been extracted from the corpus yet (see Uncertainty below).

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source_id: "claude-code-agent-teams-doc"
    rationale: "Deterministic term-frequency ranking (manifests/phase0/topic-source-rankings.json, computed from this page's registry keywords) placed this file first with 142 keyword hits, by far the highest in the corpus for this topic."
    coverage: "What agent teams are, when to use them, how they differ from subagents, how to enable them."
  - rank: 2
    source_id: "apex-kb-skill-md"
    rationale: "Not part of the deterministic ranking (this is Apex's own skill file, not a raw source) -- included directly because it supplies the project-specific delta this page's contract requires."
    coverage: "The execution_surface_policy that currently keeps all default semantic work inside a single assistant, in tension with agent teams' distributed-teammate model."
```

## Macro / Meso / Micro

### Macro

An agent team is a set of independent Claude Code sessions that coordinate through a shared task list and talk to each other directly, rather than reporting results up to a single controller. This makes it structurally different from a subagent (which never talks to other subagents) and from a skill (which runs inside one session's context, not several).

### Meso

The primary doc frames the choice as a communication question, not a capability question: use a subagent when workers only need to report a result back; use an agent team when workers need to "share findings, challenge each other, and coordinate on their own" (lines 34-50). It names four strongest use cases -- parallel research/review, independently-owned new modules, competing-hypothesis debugging, and cross-layer coordination -- and one explicit cost: agent teams "add coordination overhead and use significantly more tokens than a single session," recommending a single session or subagents instead for sequential, same-file, or highly-dependent work (line 30).

### Micro

Agent teams are disabled by default; enabling requires setting `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` in the shell environment or `settings.json` (lines 54-60). The comparison table (lines 42-48) is exact: subagents have their own context window but results return to the caller; agent teams' teammates have a fully independent context window and message each other directly; subagents are coordinated entirely by the main agent, agent teams self-coordinate via a shared task list; token cost is lower for subagents (summarized results only) and higher for agent teams (each teammate is a separate Claude instance).

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Agent teams differ from subagents specifically in communication topology: subagents only report results back to the spawning agent, while agent-team teammates message each other directly and self-coordinate through a shared task list."
    source_pointer: "primary-code-claude-com-docs-en-agent-teams.md.md lines 32-48"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "Agent teams are recommended specifically for research/review, independently-owned new modules, competing-hypothesis debugging, and cross-layer coordination -- not for sequential tasks, same-file edits, or highly-dependent work, where a single session or subagents are named as more effective."
    source_pointer: "primary-code-claude-com-docs-en-agent-teams.md.md lines 23-30"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "Agent teams are disabled by default and require CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 to enable."
    source_pointer: "primary-code-claude-com-docs-en-agent-teams.md.md lines 54-60"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C004
    claim: "This KB's own apex-kb skill currently defaults all semantic work to a single assistant/chat LLM by policy, requiring explicit operator override before any semantic delegation -- a structural tension with agent teams' distributed-teammate model that this KB has not yet resolved or even directly discussed."
    source_pointer: ".claude/skills/apex-kb/SKILL.md execution_surface_policy block"
    confidence: "medium"
    claim_label: "behavioral_inference"
```

## Routes Here

```yaml
routes:
  - question: "Should Apex skills use agent teams for parallel or collaborative work?"
    leads_to: "wiki/entities/agent-teams.md"
    rationale: "Names the specific policy tension (single-assistant default vs distributed teammates) rather than a generic description of the feature."
  - question: "What's the actual difference between an agent team and a subagent?"
    leads_to: "wiki/entities/agent-teams.md"
    rationale: "Exact comparison table from the primary source, not a paraphrase."
  - related_page: "wiki/entities/claude-code-subagents.md"
    relation: "Direct comparison point named by the primary source itself."
  - related_page: "wiki/summaries/agent-vs-subagent-vs-skill.md"
    relation: "Covers the subagent/skill/main-conversation decision; agent teams are the fourth mechanism in the same underlying comparison table (workflows doc)."
```

## Evidence

```yaml
evidence:
  - source_id: "claude-code-agent-teams-doc"
    source_pointer: "lines 21-60"
    supports: "Definition, use cases, subagent comparison, enable mechanism."
  - source_id: "apex-kb-skill-md"
    source_pointer: "execution_surface_policy block"
    supports: "The project-specific delta claim (C004)."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "No source in this corpus documents any Apex skill actually attempting or rejecting agent-team usage -- C004 is a structural inference from comparing two policies, not a claim that this tension has been discussed or decided by an operator."
    source_pointer: ".claude/skills/apex-kb/SKILL.md execution_surface_policy block"
    proposed_handling: "ask_operator"
  - id: U002
    description: "Two secondary raw sources (a repo example and an internal claude-code-best-practice implementation doc) reference agent teams but were not read in full for this page; only the primary official doc was read line-by-line."
    source_pointer: "manifests/phase0/topic-source-rankings.json agent-teams ranked_sources ranks 2-3"
    proposed_handling: "revisit_source"
```
