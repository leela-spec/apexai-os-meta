---
title: "Agent and Subagent Design Patterns"
page_type: summary
kb_slug: "claude-code-orchestration-design"
summary_slug: "agent-subagent-design-patterns"
source_refs:
  - source_id: "claude-code-sub-agents-doc"
    source_path: "raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-sub-agents.md.md"
    source_hash: "68e6bee3a7cf8fd5"
    source_pointer: "lines 307-400 (tool/MCP/nested-spawn scoping), 722-795 (foreground/background, chain, parallel, choose-vs-main-conversation)"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "14412344bddf7838"
    source_pointer: "claims B02-C008, B02-C009"
    source_storage_mode: "pointer_only"
created_at: "2026-07-11T00:00:00Z"
updated_at: "2026-07-11T00:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "persistent-agent-vs-ephemeral-subagent"
  - "ephemeral-subagent-boundary"
  - "mechanism-ladder"
related_entities:
  - "claude-code-subagents"
review_flags: []
---

# Agent and Subagent Design Patterns

## Core Summary

Claude Code's subagent mechanism gives a designer four independent levers over any delegated task: **tool scope** (what it can touch), **MCP scope** (what external servers it can reach), **spawn scope** (whether it can create further subagents, and which ones), and **execution mode** (foreground, background, or nested). This page covers the mechanics of those levers, grounded directly in the primary subagent documentation. It intentionally does not re-cover the persistent-vs-ephemeral *identity* decision (see `persistent-agent-vs-ephemeral-subagent.md`) or the subagent-vs-skill-vs-main-conversation *routing* decision (see `agent-vs-subagent-vs-skill.md`) — this page is about how to configure a subagent once you've decided to use one.

## What This Adds

```yaml
adds:
  - "Concrete tool-scoping mechanics: allowlist (tools) vs denylist (disallowedTools), precedence rule, and MCP server-level patterns."
  - "Nested subagent spawning (v2.1.172+) and the Agent(agent_type) allowlist syntax for restricting which subagents a coordinator can create."
  - "Execution-mode design space: foreground (blocking) vs background (concurrent) vs worktree isolation vs nested."
clarifies:
  - "Tool restriction and context isolation are separate, independently configurable mechanisms, not one setting."
limits:
  - "Does not cover the persistent/ephemeral identity boundary or the subagent-vs-skill routing decision; see the related concept pages for those."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source_id: "claude-code-sub-agents-doc"
    rationale: "Deterministic term-frequency ranking (topic-source-rankings.json, topic agent-subagent-design-patterns) placed this file first with 241 keyword hits, the highest in the corpus for this topic's keyword set."
    coverage: "Full subagent configuration surface: frontmatter fields, tool/MCP/spawn scoping, permission modes, hooks, foreground/background, nested subagents, common design patterns."
  - rank: 2
    source_id: "phase1-batch02-claude-code-orchestration-surface"
    rationale: "Second-ranked Phase 1 analysis; supplies the condensed claim form (B02-C008/C009) already used elsewhere in this KB, useful for cross-referencing without re-deriving."
    coverage: "Subagent context-isolation mechanism and built-in Explore/Plan/general-purpose subagent scope."
```

## Macro / Meso / Micro

### Macro

A subagent is not a single on/off switch for "isolation" — it is a bundle of independently configurable scopes. Designing a good subagent means deciding, separately, what tools it can call, what MCP servers it can reach, whether it can spawn further subagents (and which ones), and whether it runs blocking in the foreground, concurrently in the background, or with its own git worktree. Getting these levers right is what turns "delegate this to a subagent" from a vague instruction into a bounded, auditable unit of work.

### Meso

**Tool scope** is set with `tools` (allowlist) or `disallowedTools` (denylist); if both are set, `disallowedTools` is applied first and `tools` is resolved against what remains, so a tool listed in both ends up removed (lines 321-345). Both fields also accept MCP server-level patterns (`mcp__servername` or `mcp__servername__*`, granting/removing every tool from that server), and `disallowedTools` additionally accepts `mcp__*` to strip every MCP tool regardless of server (lines 345-352). **Spawn scope** governs whether a subagent (or a `--agent`-launched main thread) can create further subagents: `Agent(worker, researcher)` in `tools` is an allowlist restricting spawning to exactly those types; bare `Agent` allows spawning any type; omitting `Agent` from `tools` blocks spawning entirely (lines 353-372). This same field enables **nested subagents** (v2.1.172+): a subagent that itself lists `Agent` in its tools can spawn its own subagents, useful when a delegated task splits into parallel subtasks whose intermediate output should never reach the main conversation — only the top-level subagent's summary returns upward (lines 786-795). **Execution mode** is a third independent axis: foreground subagents block the main conversation and pass permission prompts through directly; background subagents run concurrently, and as of v2.1.186 their permission prompts surface in the main session naming the asking subagent rather than auto-denying (lines 722-733). `isolation: worktree` adds a fourth, orthogonal option — a temporary git worktree branched from the default branch, auto-cleaned if the subagent makes no changes (source doc line 262-264, cited via the related `agent-vs-subagent-vs-skill.md` page's source set).

### Micro

Three named design patterns recur in the source doc's "Common patterns" section (lines 738-780): **isolate high-volume operations** (delegate verbose output like test runs or log processing to a subagent so only a summary returns, keeping main context small); **run parallel research** (spawn multiple subagents simultaneously for independent investigations — "Research the authentication, database, and API modules in parallel using separate subagents" — with an explicit warning that many detailed returns can still consume significant context, and a pointer to Agent Teams for sustained parallelism beyond one context window); and **chain subagents** (sequential multi-step workflows where each subagent's output becomes the next one's input, e.g. "Use the code-reviewer subagent to find performance issues, then use the optimizer subagent to fix them"). The doc's own main-conversation-vs-subagent criteria (lines 772-787) are the load-bearing decision rule referenced by, but not re-derived in, `agent-vs-subagent-vs-skill.md`.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Tool scoping supports both an allowlist (tools) and denylist (disallowedTools); when both are set, disallowedTools is applied first and tools is resolved against the remainder, so a tool named in both fields is removed."
    source_pointer: "primary-code-claude-com-docs-en-sub-agents.md.md lines 321-345"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages: []
  - claim_id: C002
    claim: "Spawn scope for subagents/coordinators is set via the Agent tool entry in `tools`: Agent(type1, type2) allowlists exactly those subagent types, bare Agent allows any type, and omitting Agent blocks spawning entirely."
    source_pointer: "primary-code-claude-com-docs-en-sub-agents.md.md lines 353-372"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages: []
  - claim_id: C003
    claim: "As of Claude Code v2.1.172, a subagent can spawn its own nested subagents, useful when a delegated task itself splits into parallel subtasks whose intermediate output should not reach the main conversation."
    source_pointer: "primary-code-claude-com-docs-en-sub-agents.md.md lines 786-795"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages: []
  - claim_id: C004
    claim: "Background subagents run concurrently with the main conversation; as of v2.1.186 their permission prompts surface in the main session naming the requesting subagent, rather than auto-denying as in earlier versions."
    source_pointer: "primary-code-claude-com-docs-en-sub-agents.md.md lines 722-733"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages: []
  - claim_id: C005
    claim: "Three named common patterns for subagent use are: isolating high-volume/verbose operations, running parallel independent research across multiple subagents, and chaining subagents sequentially so one's output feeds the next's input."
    source_pointer: "primary-code-claude-com-docs-en-sub-agents.md.md lines 738-780"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages: []
```

## Routes Here

```yaml
routes:
  - question: "How do I restrict what tools or MCP servers a subagent can use?"
    leads_to: "wiki/summaries/agent-subagent-design-patterns.md"
    rationale: "Direct mechanics of tools/disallowedTools and MCP server-level patterns."
  - question: "Can a subagent spawn its own subagents, and can I limit that?"
    leads_to: "wiki/summaries/agent-subagent-design-patterns.md"
    rationale: "Covers nested subagent spawning and the Agent(agent_type) allowlist."
  - question: "Should this be one subagent, several parallel subagents, or a chain?"
    leads_to: "wiki/summaries/agent-subagent-design-patterns.md"
    rationale: "Covers the three named common patterns directly from the source doc."
  - related_page: "wiki/summaries/agent-vs-subagent-vs-skill.md"
    relation: "Covers the prior decision of whether to use a subagent at all, vs skill or main conversation; this page assumes that decision is already made."
  - related_page: "wiki/concepts/persistent-agent-vs-ephemeral-subagent.md"
    relation: "Covers whether a subagent role should be a persistent, versioned project artifact vs a one-off delegation; orthogonal to the scoping mechanics here."
  - related_page: "wiki/entities/claude-code-subagents.md"
    relation: "Narrow entity page for the subagent mechanism itself."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Agent Teams (referenced at line 762 for 'sustained parallelism beyond one context window') is a distinct, more heavyweight mechanism than parallel subagents; this page does not cover its design surface in depth. See wiki/entities/agent-teams.md."
    source_pointer: "primary-code-claude-com-docs-en-sub-agents.md.md line 762"
    proposed_handling: "revisit_source"
  - id: U002
    description: "The Agent SDK subagents doc (primary-code-claude-com-docs-en-agent-sdk-subagents.md.md, 87 keyword hits, second-ranked before this KB's Phase 1 analysis file) covers the programmatic/SDK equivalent of these same scoping mechanics and was not read for this page; a future pass should confirm whether SDK-level scoping differs from the CLI/file-based frontmatter described here."
    proposed_handling: "revisit_source"
```
