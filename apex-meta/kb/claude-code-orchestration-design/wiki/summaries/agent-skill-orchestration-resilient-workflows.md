---
title: "Agent and Skill Orchestration for Resilient Workflows"
page_type: summary
kb_slug: "claude-code-orchestration-design"
summary_slug: "agent-skill-orchestration-resilient-workflows"
source_refs:
  - source_id: "claude-code-workflows-doc"
    source_path: "raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-workflows.md.md"
    source_hash: "99e9a815d2ad3038"
    source_pointer: "lines 19-68, When to use a workflow / Run a bundled workflow"
    source_storage_mode: "pointer_only"
  - source_id: "claude-code-sub-agents-doc"
    source_path: "raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/primary-code-claude-com-docs-en-sub-agents.md.md"
    source_hash: "68e6bee3a7cf8fd5"
    source_pointer: "lines 738-794, Common patterns / Choose between subagents and main conversation"
    source_storage_mode: "pointer_only"
created_at: "2026-07-10T21:00:00Z"
updated_at: "2026-07-10T21:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Agent and Skill Orchestration for Resilient Workflows

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source_id: "claude-code-sub-agents-doc"
    rationale: "Highest deterministic keyword-hit ranking for this topic (236 hits, topic-source-rankings.json) -- primary doc for delegation and isolation mechanics."
    coverage: "Subagent isolation, chaining, parallel research pattern, nested subagent spawning."
  - rank: 2
    source_id: "claude-code-workflows-doc"
    rationale: "Third-ranked deterministic hit; the only source that names resumability and adversarial cross-checking as structural properties of one mechanism (workflows) and not others."
    coverage: "Comparison table across subagents/skills/agent teams/workflows; resilience-relevant properties (resumability, review patterns)."
```

## Macro / Meso / Micro

### Macro

Resilience in Claude Code orchestration is not a separate feature bolted onto agents and skills -- it falls directly out of which of four mechanisms holds the plan: subagents, skills, agent teams, or workflows. The source doc frames this as one question with four answers: "who decides what runs next." When Claude itself is the orchestrator (subagents, skills, agent teams), a crash, an interrupted turn, or a context-window limit is a real failure mode, because the plan lives only in Claude's turn-by-turn reasoning. When a workflow script holds the loop and the intermediate state, the run survives interruption and can resume in the same session -- resilience is a property of *where the plan lives*, not of which agent is doing the work.

### Meso

The comparison table in the workflows doc makes the resilience-relevant differences explicit rather than leaving them to be inferred: subagents and skills both restart the turn on interruption, because their state lives in Claude's context window; agent teams keep running because teammates are independent peer sessions coordinating through a shared task list; workflows are resumable in the same session because a script, not Claude's live reasoning, holds the loop and its variables. Scale follows the same axis -- subagents and skills handle "a few delegated tasks per turn," agent teams "a handful of long-running peers," and workflows "dozens to hundreds of agents per run" -- because only a script can hold that much concurrent state without it collapsing into a single context window.

### Micro

Concretely, a workflow gets resilience properties a subagent chain cannot: it can run independent agents that adversarially review each other's findings before anything is reported, or draft a plan from several angles and weigh them against each other, "so you get a more trustworthy result than a single pass" (workflows doc lines 34). This is the same adversarial-verification pattern this KB's own quality-gate redesign uses (a claim survives only if independent checks agree) applied to orchestration itself, not just to content validation. At the subagent layer, the closest equivalent to resilience is a narrower pattern: isolating high-volume, verbose operations so a single failure or large output doesn't consume the main thread's context (sub-agents doc lines 740-747), and chaining subagents so each step's failure is visible before the next step runs rather than compounding silently (sub-agents doc lines 764-770). Neither restart-safety nor adversarial cross-checking is available at that layer -- both are properties the workflows doc attributes specifically to moving the plan into a script.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "The four Claude Code orchestration mechanisms (subagents, skills, agent teams, workflows) differ primarily in who holds the plan -- Claude turn-by-turn for the first three, a script for workflows -- and this single distinction determines their resilience properties, not their capability."
    source_pointer: "primary-code-claude-com-docs-en-workflows.md.md lines 21-32"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "Subagents and skills both restart the interrupted turn on failure because their state lives in Claude's context window; workflows are resumable in the same session because a script holds the loop and its variables instead."
    source_pointer: "primary-code-claude-com-docs-en-workflows.md.md lines 23-30 (comparison table)"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "Workflows can apply a repeatable quality pattern that subagent chains cannot on their own: independent agents adversarially reviewing each other's findings, or drafting from multiple angles and weighing them, before anything is reported."
    source_pointer: "primary-code-claude-com-docs-en-workflows.md.md lines 34"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C004
    claim: "At the subagent layer, the closest available resilience patterns are isolating high-volume/verbose operations and chaining subagents so a step's failure surfaces before the next step runs -- narrower than a workflow's restart-safety or adversarial review, but achievable without a script."
    source_pointer: "primary-code-claude-com-docs-en-sub-agents.md.md lines 740-770"
    confidence: "high"
    claim_label: "source_backed_summary"
```

## Routes Here

```yaml
routes:
  - question: "How do I build a resilient multi-agent workflow in Claude Code, and what actually makes it resilient?"
    leads_to: "wiki/summaries/agent-skill-orchestration-resilient-workflows.md"
    rationale: "Names the specific structural property (who holds the plan) that determines resilience, not a generic list of features."
  - question: "Why would I use a workflow instead of just chaining subagents?"
    leads_to: "wiki/summaries/agent-skill-orchestration-resilient-workflows.md"
    rationale: "Direct comparison table plus the specific resumability and adversarial-review properties workflows add."
  - related_page: "wiki/summaries/agent-vs-subagent-vs-skill.md"
    relation: "Covers the subagent/skill/main-conversation decision in depth; this page extends that comparison to workflows and agent teams specifically for resilience."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Agent teams (the third mechanism in the comparison table) are named but not detailed in the two bounded sources used here; their specific resilience properties beyond 'teammates keep running' are not verified against a primary agent-teams doc in this pass."
    source_pointer: "primary-code-claude-com-docs-en-workflows.md.md lines 23-30"
    proposed_handling: "revisit_source"
  - id: U002
    description: "This page does not verify whether Apex's own skills (apex-kb, apex-plan, etc.) currently use any workflow-layer resilience pattern, or whether they rely entirely on the less resilient subagent/skill layer described here."
    proposed_handling: "audit_item"
