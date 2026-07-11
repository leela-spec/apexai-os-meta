---
title: "Named Orchestration Workflow Patterns"
page_type: summary
kb_slug: "claude-code-orchestration-design"
summary_slug: "named-orchestration-workflow-patterns"
source_refs:
  - source_id: "anthropic-engineering-index"
    source_path: "raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/secondary-anthropic-com-engineering.md"
    source_hash: "NA"
    source_pointer: "line 10, 'Building effective agents' entry (Dec 19, 2024) in the Anthropic Engineering blog index"
    source_storage_mode: "pointer_only"
  - source_id: "shanraisshan-workflow-concepts-command"
    source_path: "raw/source-groups/claude-orchestration-agents/raw/repos/first-batch-to-clone/shanraisshan__claude-code-best-practice/.claude/commands/workflows/best-practice/workflow-concepts.md"
    source_hash: "NA"
    source_pointer: "full file, Phase 0 through Phase 2 (parallel fan-out, then merge)"
    source_storage_mode: "pointer_only"
  - source_id: "aider-modes-doc"
    source_path: "raw/source-groups/claude-orchestration-agents/raw/repos/first-batch-to-read-only/Aider-AI__aider/aider/website/docs/usage/modes.md"
    source_hash: "NA"
    source_pointer: "lines 1-15, architect mode description"
    source_storage_mode: "pointer_only"
  - source_id: "anthropics-skill-creator-skill-md"
    source_path: "raw/source-groups/_source-acquisitions/skill-best-practices-official-2026-06-23/raw/repo-extracts/anthropics-skills__skills__skill-creator__SKILL.md"
    source_hash: "NA"
    source_pointer: "lines 10-20, draft-test-evaluate-rewrite-repeat loop"
    source_storage_mode: "pointer_only"
created_at: "2026-07-11T00:00:00Z"
updated_at: "2026-07-11T00:00:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "needs_review"
related_concepts:
  - "workflow-boundary"
  - "owner-validator-split"
related_entities:
  - "claude-code-workflows"
  - "aider"
  - "bmad-method"
review_flags:
  - "The canonical 5-pattern taxonomy (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer) comes from Anthropic's 'Building Effective Agents' article. Only the article's title/URL are present in this corpus (an index-page link, not its body text) -- see uncertainty trigger U001. That taxonomy section is marked working_hypothesis; the concrete practitioner examples below it are source_backed_summary."
---

# Named Orchestration Workflow Patterns

## Core Summary

An orchestration "workflow" is a fixed, code-defined sequence of LLM calls and tool invocations (as opposed to an open-ended agent loop that decides its own steps). This page names the recurring shapes such workflows take and grounds each in a concrete example actually present in this KB's raw corpus, rather than restating a taxonomy from memory as if it were quoted from a source this KB has fully ingested.

## What This Adds

```yaml
adds:
  - "Three named patterns evidenced directly in the downloaded practitioner corpus: fan-out/merge (parallelization), model-routing (routing/orchestrator-workers), and draft-eval-rewrite (evaluator-optimizer)."
  - "An explicit, honest flag that the canonical 5-pattern taxonomy's origin article is only present in this corpus as an index-page title/link, not as ingested body text."
clarifies:
  - "'Workflow' here means fixed, orchestrator-defined control flow -- distinct from an agent given a goal and tools that decides its own loop."
limits:
  - "Does not attempt to reconstruct the full 'Building Effective Agents' article from memory; treat the taxonomy naming as working_hypothesis pending real ingestion of that article's text."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source_id: "shanraisshan-workflow-concepts-command"
    rationale: "A real, complete, working orchestration command from a downloaded practitioner repo (P1-P3 tier) -- concrete fan-out/merge workflow, not a description of one."
    coverage: "Full parallel-launch-then-merge workflow: two subagents spawned in the same message, waited on, cross-referenced, and synthesized into one report."
  - rank: 2
    source_id: "aider-modes-doc"
    rationale: "Concrete, real two-model routing pattern (architect proposes, editor applies) from a mature, widely-used external coding agent -- direct practitioner evidence for the routing/orchestrator-workers shape."
    coverage: "Aider's architect/code/ask/help chat-mode split and the recommended ask-then-code routing workflow."
  - rank: 3
    source_id: "anthropics-skill-creator-skill-md"
    rationale: "Official Anthropic (P0) skill whose own documented process is itself a draft-evaluate-rewrite loop -- direct evidence for the evaluator-optimizer shape from a first-party source."
    coverage: "Skill-creator's stated iteration loop: draft, test prompts, evaluate qualitatively/quantitatively, rewrite, repeat, expand test set."
  - rank: 4
    source_id: "anthropic-engineering-index"
    rationale: "Only source in this corpus that names the origin article for the canonical 5-pattern taxonomy; present as a title/link only, not ingested body content, hence ranked last and marked working_hypothesis."
    coverage: "Confirms the article 'Building effective agents' (Dec 19, 2024) exists and is the likely origin of the standard workflow-pattern vocabulary; provides no body text to cite from."
```

## Macro / Meso / Micro

### Macro

Two different kinds of workflow-shape claims sit on this page, and they carry different confidence. The **concrete practitioner shapes** -- fan-out/merge, model-routing, and draft-eval-rewrite -- are directly evidenced in this corpus by real, working configurations from downloaded repos and an official Anthropic skill. The **canonical naming scheme** (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer) is well-known practitioner vocabulary whose likely origin article is referenced in this corpus only by title and URL, not by ingested text -- so this page treats that specific naming/definitions as `working_hypothesis` rather than claiming it is source-backed from this KB's own corpus.

### Meso

The clearest fan-out/merge example is a real Claude Code slash command: it "launch[es] two research agents in parallel, wait[s] for their results, merge[s] findings, and present[s] a unified report," spawning both agents "using the Task tool **in the same message** (parallel launch)" and later instructing the coordinator to "cross-reference the two... flag any contradictions between the two for the user to resolve" (shanraisshan workflow-concepts.md, Phase 0 and Phase 2). This is parallelization plus a merge/synthesis step -- the orchestrator-workers shape in miniature: one coordinating prompt, two independently-scoped workers, one merge step. A distinct routing shape appears in Aider: its `architect` chat mode has "An architect model... propose changes and an editor model... translate that proposal into specific file edits" (aider modes.md line 11), and the doc recommends bouncing between `/ask` (discussion, no edits) and `/code` (execution) modes depending on task phase -- a human- or task-driven router choosing which specialized mode/model handles a given turn. The evaluator-optimizer shape appears first-party in Anthropic's own skill-creator: "Write a draft of the skill... run claude-with-access-to-the-skill on [test prompts]... help the user evaluate the results both qualitatively and quantitatively... Rewrite the skill based on feedback... Repeat until you're satisfied. Expand the test set and try again at larger scale" (skill-creator SKILL.md lines 12-20) -- a literal draft/evaluate/rewrite/repeat loop with an explicit scale-up step at the end.

### Micro

None of the three examples above use the words "orchestrator-workers," "routing," or "evaluator-optimizer" -- those are this page's own classification of what each concrete pattern *is*, applied by the author of this page, not quoted terminology. Only the Anthropic engineering blog index (a page of article titles/links, not full articles) confirms that "Building effective agents" (Dec 19, 2024) is a real, existing Anthropic publication likely to be the origin of that standard vocabulary (secondary-anthropic-com-engineering.md line 10) -- but its body text was never fetched into this corpus (network access is forbidden under this KB's operating policy), so this page cannot cite specific pattern definitions from it and does not attempt to reproduce them from training-data memory as if they were sourced here.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "A real Claude Code workflow command spawns two subagents in parallel in a single message, waits for both, then merges and cross-references their findings into one report -- a concrete fan-out/merge (parallelization + orchestrator-workers) shape."
    source_pointer: "shanraisshan__claude-code-best-practice workflow-concepts.md, Phase 0 and Phase 2"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages: []
  - claim_id: C002
    claim: "Aider's architect chat mode routes a task through two distinct models -- an architect model that proposes changes and a separate editor model that translates the proposal into specific file edits -- and separately recommends routing between ask mode (discussion) and code mode (execution) by task phase."
    source_pointer: "Aider-AI/aider docs/usage/modes.md lines 1-15"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages: []
  - claim_id: C003
    claim: "Anthropic's own skill-creator skill documents its process as draft, test-prompt generation, qualitative/quantitative evaluation, rewrite based on feedback, repeat, then expand the test set at larger scale -- a first-party evaluator-optimizer loop."
    source_pointer: "anthropics-skills skill-creator SKILL.md lines 10-20"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages: []
  - claim_id: C004
    claim: "The standard 'prompt chaining / routing / parallelization / orchestrator-workers / evaluator-optimizer' naming scheme for agent workflows likely originates in Anthropic's 'Building effective agents' article (Dec 19, 2024), but this corpus contains only that article's title and URL, not its ingested body text."
    source_pointer: "secondary-anthropic-com-engineering.md line 10"
    confidence: "low"
    claim_label: "working_hypothesis"
    used_in_pages: []
```

## Routes Here

```yaml
routes:
  - question: "What does a real fan-out-then-merge multi-agent workflow look like in practice?"
    leads_to: "wiki/summaries/named-orchestration-workflow-patterns.md"
    rationale: "Cites a complete, real parallel-launch-and-merge command rather than a paraphrase."
  - question: "How do practitioner tools route a task between different models or modes?"
    leads_to: "wiki/summaries/named-orchestration-workflow-patterns.md"
    rationale: "Aider's architect/editor and ask/code routing is concrete, corpus-grounded evidence."
  - related_page: "wiki/concepts/workflow-boundary.md"
    relation: "Companion concept defining what counts as a fixed workflow vs an open agent loop in this KB's own terms."
  - related_page: "wiki/summaries/external-repo-orchestration-patterns.md"
    relation: "Broader practitioner-repo synthesis; this page's Aider/BMAD-adjacent evidence is a workflow-specific slice of that wider survey."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Anthropic's 'Building effective agents' article -- the likely origin of the standard workflow-pattern taxonomy this page uses for classification -- is present in this corpus only as a title/URL in an index page, not as ingested body text. The specific named-pattern definitions in this page's Macro/Meso sections are this page's own classification applied to real evidence, not quotes from that article."
    source_pointer: "secondary-anthropic-com-engineering.md line 10"
    proposed_handling: "revisit_source"
  - id: U002
    description: "BMAD-METHOD's own workflow/routing mechanisms (party-mode, subagent routing referenced in bmad-party-mode/references/mode-subagent.md) were located during ranking but not read in depth for this page; a follow-up pass could add a fourth concrete example."
    proposed_handling: "planning_task_candidate"
```
