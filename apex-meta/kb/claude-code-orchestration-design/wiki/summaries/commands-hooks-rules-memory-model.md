---
title: "Commands, Hooks, Rules, and Memory Interaction Model"
page_type: summary
kb_slug: "claude-code-orchestration-design"
summary_slug: "commands-hooks-rules-memory-model"
source_refs:
  - source_id: "claude-code-hooks-doc"
    source_path: "raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-hooks.md.md"
    source_hash: "NA"
    source_pointer: "lines 15-58 (lifecycle/cadence + event table), 533-575 (hooks in skills/agents, /hooks menu), 1047-1080 (InstructionsLoaded, CLAUDE.md/rules memory scopes), 1145-1195 (UserPromptExpansion, slash-command hook path)"
    source_storage_mode: "pointer_only"
  - source_id: "shanraisshan-hooks-readme"
    source_path: "raw/source-groups/claude-orchestration-agents/raw/repos/first-batch-to-clone/shanraisshan__claude-code-best-practice/.claude/hooks/HOOKS-README.md"
    source_hash: "NA"
    source_pointer: "lines 1-34, full 30-event table with per-event input fields and the experimental agent-teams flag note"
    source_storage_mode: "pointer_only"
created_at: "2026-07-11T00:00:00Z"
updated_at: "2026-07-11T00:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "hook-vs-skill-instruction"
  - "mcp-config-boundary"
related_entities:
  - "claude-code-hooks"
  - "claude-code-skills"
review_flags: []
---

# Commands, Hooks, Rules, and Memory Interaction Model

## Core Summary

Slash commands, hooks, `CLAUDE.md`/rules files, and memory are four distinct surfaces that intersect at specific, named lifecycle events rather than being layers of one system. The official hooks reference documents the exact event names where each surface's activity becomes observable or interceptable to the others: a slash command's expansion is its own hookable event (`UserPromptExpansion`), a rules/memory file's load is its own hookable event (`InstructionsLoaded`), and a hook itself can live inside a skill or subagent's frontmatter rather than only in global settings.

## What This Adds

```yaml
adds:
  - "The exact event where a typed slash command becomes interceptable (UserPromptExpansion) and why it exists separately from PreToolUse on the Skill tool."
  - "The exact event and field set for CLAUDE.md / .claude/rules/*.md loading (InstructionsLoaded), including its four memory_type scopes and five load_reason values."
  - "That hooks are not only a settings.json construct: skills and subagents can define their own scoped hooks directly in frontmatter."
clarifies:
  - "Three hook cadences exist -- once per session, once per turn, and once per tool call -- and rules/memory loading is a fourth, separate, asynchronous, non-blocking cadence."
limits:
  - "Does not cover MCP-specific hook/trust mechanics in depth; see wiki/summaries/mcp-configuration-and-trust-boundary.md for that boundary."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source_id: "claude-code-hooks-doc"
    rationale: "Deterministic term-frequency ranking (topic-source-rankings.json, topic commands-hooks-rules-memory-model) placed this file first with 623 keyword hits, by far the highest in the corpus for this topic's keyword set, and it is the official primary-source hooks reference."
    coverage: "Complete hook lifecycle, all ~30 hook events with firing conditions, hook configuration/matcher/handler fields, hooks defined in skill/subagent frontmatter, the /hooks inspection menu, and CLAUDE.md/rules memory-loading semantics via InstructionsLoaded."
  - rank: 2
    source_id: "shanraisshan-hooks-readme"
    rationale: "Second-ranked practitioner corpus file (207 keyword hits); an independently-written condensed table of the same 30 hook events that corroborates the official doc's event count and per-event field list, and adds the experimental-flag detail for agent-team-only events."
    coverage: "Numbered 30-event summary table (event name, firing condition, per-event input fields) plus a note that TeammateIdle/TaskCreated/TaskCompleted require CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1."
```

## Macro / Meso / Micro

### Macro

These four surfaces do not stack in a fixed order; they interleave around the same per-turn loop, and each has exactly one or two named events where it becomes visible to a hook. A slash command becomes hookable the moment it *expands* into a prompt, not when a resulting tool call fires. A `CLAUDE.md` or rules file becomes hookable the moment it *loads* into context, whether at session start or lazily mid-session. Hooks themselves are not confined to `settings.json` -- a skill or subagent can carry its own hooks, scoped to that component's lifetime and cleaned up when it finishes. Understanding the interaction model means knowing which of these four named events a given design concern actually belongs to, rather than assuming "hooks" is one undifferentiated interception point.

### Meso

Hook events fall into three cadences: "once per session (`SessionStart`, `SessionEnd`), once per turn (`UserPromptSubmit`, `Stop`, `StopFailure`), and on every tool call inside the agentic loop (`PreToolUse`, `PostToolUse`)" (lines 15-20). Rules/memory loading is effectively a fourth, orthogonal cadence: `InstructionsLoaded` "fires when a CLAUDE.md or .claude/rules/*.md file is loaded into context... at session start for eagerly-loaded files and again later when files are lazily loaded, for example when Claude accesses a subdirectory that contains a nested CLAUDE.md or when conditional rules with paths: frontmatter match" (lines 1047-1050) -- and unlike most hooks, it "does not support blocking or decision control... runs asynchronously for observability purposes" (lines 1049-1050, 1078-1080). Slash commands have their own separate hookable seam, `UserPromptExpansion`, specifically because `PreToolUse` cannot see them: "a PreToolUse hook matching the Skill tool fires only when Claude calls the tool, but typing /skillname directly bypasses PreToolUse. UserPromptExpansion fires on that direct path" (lines 1148-1150) -- and this event can block the command outright (`decision: block`) or inject `additionalContext`, unlike the read-only `InstructionsLoaded` event. Hooks are also not exclusively a global-settings mechanism: "hooks can be defined directly in skills and subagents using frontmatter. These hooks are scoped to the component's lifecycle and only run when that component is active... cleaned up when it finishes" (lines 533-540).

### Micro

`InstructionsLoaded`'s input schema names four memory scopes via `memory_type`: `"User"`, `"Project"`, `"Local"`, or `"Managed"` (line 1058), and five `load_reason` values: `"session_start"`, `"nested_traversal"`, `"path_glob_match"` (conditional rules matched via `paths:` frontmatter), `"include"`, or `"compact"` (re-load after context compaction) (line 1059). `UserPromptExpansion`'s input schema names `expansion_type` as either `"slash_command"` (skill and custom commands) or `"mcp_prompt"` (MCP server prompts), plus `command_name`, `command_args`, and `command_source` (lines 1156, JSON example at 1160-1170). The `/hooks` menu itself surfaces where a given hook was defined across all four+ surfaces at once, labeling each by source: `User` (`~/.claude/settings.json`), `Project` (`.claude/settings.json`), `Local` (`.claude/settings.local.json`), `Plugin` (a plugin's `hooks/hooks.json`), `Session` (registered in memory for the current session), or `Built-in` (registered internally) (lines 558-573) -- meaning a skill- or subagent-scoped hook (added at lines 533-556) is a distinct, real configuration surface separate from all of these settings-file locations, even though the menu's listed sources don't enumerate it by name.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Hook events fall into three cadences -- once per session, once per turn, and once per tool call inside the agentic loop -- while CLAUDE.md/rules loading (InstructionsLoaded) is a separate, asynchronous, non-blocking, observability-only cadence that cannot block or modify loading."
    source_pointer: "primary-code-claude-com-docs-en-hooks.md.md lines 15-20, 1047-1050, 1078-1080"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages: []
  - claim_id: C002
    claim: "A typed slash command bypasses PreToolUse entirely (which only fires when Claude itself calls the Skill tool); UserPromptExpansion is the separate, dedicated hook event for intercepting direct /skillname invocation, and it can block the expansion or inject additionalContext."
    source_pointer: "primary-code-claude-com-docs-en-hooks.md.md lines 1145-1150, 1172-1193"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages: []
  - claim_id: C003
    claim: "InstructionsLoaded reports four memory scopes (User, Project, Local, Managed) and five load reasons (session_start, nested_traversal, path_glob_match, include, compact) for every CLAUDE.md or .claude/rules/*.md file loaded into context."
    source_pointer: "primary-code-claude-com-docs-en-hooks.md.md lines 1058-1059"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages: []
  - claim_id: C004
    claim: "Hooks are not confined to settings.json: skills and subagents can define their own hooks directly in YAML frontmatter, scoped to that component's active lifetime and cleaned up when it finishes."
    source_pointer: "primary-code-claude-com-docs-en-hooks.md.md lines 533-540, 550-556"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages: []
  - claim_id: C005
    claim: "Claude Code exposes 30 named hook events in total; three of them (TeammateIdle, TaskCreated, TaskCompleted) only fire under the experimental agent-teams feature, gated behind the CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 environment variable."
    source_pointer: "HOOKS-README.md lines 4-34 (numbered table), note below the table"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages: []
```

## Routes Here

```yaml
routes:
  - question: "How do I intercept or block a specific slash command before it runs?"
    leads_to: "wiki/summaries/commands-hooks-rules-memory-model.md"
    rationale: "Direct coverage of UserPromptExpansion, the dedicated slash-command hook event."
  - question: "How can I get notified or audit-log whenever a CLAUDE.md or rules file loads?"
    leads_to: "wiki/summaries/commands-hooks-rules-memory-model.md"
    rationale: "Direct coverage of InstructionsLoaded and its memory_type/load_reason schema."
  - question: "Can a skill or subagent have its own hooks instead of putting everything in settings.json?"
    leads_to: "wiki/summaries/commands-hooks-rules-memory-model.md"
    rationale: "Covers component-scoped hooks defined in skill/subagent frontmatter."
  - related_page: "wiki/concepts/hook-vs-skill-instruction.md"
    relation: "Companion concept on the boundary between hook-enforced behavior and skill-instructed behavior."
  - related_page: "wiki/entities/claude-code-hooks.md"
    relation: "Narrow entity page for the hooks mechanism itself."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "This page does not enumerate all ~30 hook events in the lifecycle diagram (line 21 lists many more: PermissionRequest, TeammateIdle, WorktreeCreate/Remove, PreCompact/PostCompact, Elicitation, etc.); it focuses on the four events most relevant to the commands/hooks/rules/memory interaction question. A fuller event-by-event page would be a natural extension of wiki/entities/claude-code-hooks.md."
    source_pointer: "primary-code-claude-com-docs-en-hooks.md.md lines 21, 40-58"
    proposed_handling: "leave_as_gap"
  - id: U002
    description: "The /hooks menu's listed source labels (User/Project/Local/Plugin/Session/Built-in) do not explicitly include a label for skill- or subagent-frontmatter-defined hooks; whether these show under one of the existing labels or are simply not surfaced in that menu is not stated in the source and was not verified interactively."
    source_pointer: "primary-code-claude-com-docs-en-hooks.md.md lines 558-573 vs 533-556"
    proposed_handling: "revisit_source"
```
