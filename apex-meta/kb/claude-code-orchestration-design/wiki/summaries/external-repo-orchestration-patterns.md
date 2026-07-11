---
title: "External Practitioner Repo Orchestration Patterns"
page_type: summary
kb_slug: "claude-code-orchestration-design"
summary_slug: "external-repo-orchestration-patterns"
source_refs:
  - source_id: "orchestration-agents-repo-research"
    source_path: "raw/source-groups/claude-orchestration-agents/raw/notes/OrchestrationAgentsInCC_RepoResearch_CC.md"
    source_hash: "NA"
    source_pointer: "lines 91-108 (BMAD-METHOD, Aider, personal-os candidate profiles), lines 127-149 (confirmed repo structures)"
    source_storage_mode: "pointer_only"
  - source_id: "aider-modes-doc"
    source_path: "raw/source-groups/claude-orchestration-agents/raw/repos/first-batch-to-read-only/Aider-AI__aider/aider/website/docs/usage/modes.md"
    source_hash: "NA"
    source_pointer: "lines 1-15, architect/editor two-model chat mode"
    source_storage_mode: "pointer_only"
created_at: "2026-07-11T00:00:00Z"
updated_at: "2026-07-11T00:00:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "owner-validator-split"
  - "deterministic-script-boundary"
related_entities:
  - "bmad-method"
  - "aider"
  - "swe-agent"
review_flags:
  - "This page deliberately translates practitioner-repo mechanics into named design patterns rather than treating any repo's runtime spec as directly reusable, per this KB's own handover instruction (claude-code-orchestration-design-orchestrator-targeting handover, area 6). A separate handover reference to a cross-KB precedent document for this same rule could not be verified to exist in this repo and is not cited here -- see U003."
---

# External Practitioner Repo Orchestration Patterns

## Core Summary

Three downloaded practitioner repos each demonstrate one orchestration pattern clearly enough to be worth extracting as a named, general design lesson: BMAD-METHOD's **orchestrator-routes-to-specialized-agents** structure, Aider's **atomic-commit-per-change + two-model architect/editor split**, and personal-os's **bash-first setup with a single Markdown entry point**. This page states each pattern in general form and cites the concrete repo evidence it's drawn from, deliberately stopping short of treating any repo's exact file layout as a spec to reproduce verbatim -- consistent with the precedent already established elsewhere in this repo (`apex-meta/handoff/agent-skill-system-research/best-practice-report.md` decision 5) that external repo patterns are evidence to translate, not runtime specs to revive.

## What This Adds

```yaml
adds:
  - "BMAD-METHOD's confirmed orchestrator-plus-role-agents-plus-workflow-templates structure as a named orchestrator-routing pattern."
  - "Aider's confirmed atomic-commit-per-action and architect/editor two-model split as named execution-discipline and routing patterns."
  - "personal-os's confirmed bash-first setup.sh + single Markdown entry point (AGENTS.md) as a named low-overhead bootstrap pattern."
clarifies:
  - "These are patterns extracted and renamed for general applicability, not the repos' own terminology -- distinct from the canonical Anthropic workflow-pattern naming covered in wiki/summaries/named-orchestration-workflow-patterns.md."
limits:
  - "Does not cover SWE-agent's ACI (agent-computer interface) pattern in depth despite it being ranked in the same research pass; flagged as a follow-up in Uncertainty below."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source_id: "orchestration-agents-repo-research"
    rationale: "A pre-existing operator/LLM research pass (P1-P3 tier practitioner survey) that already confirmed real repo_structure_observed layouts for BMAD-METHOD and personal-os and rated Aider's Git-commit discipline directly, rather than this page inferring structure from raw repo files independently."
    coverage: "Ranked candidate table across 12 repos, detailed profiles for the top 6 (BMAD-METHOD, Aider, personal-os, SWE-agent among them), and confirmed repo_structure_observed trees."
  - rank: 2
    source_id: "aider-modes-doc"
    rationale: "Primary-source confirmation, directly from the Aider repo's own docs, of the architect/editor two-model split referenced in the research pass -- corroborates rather than merely repeats the secondary research note."
    coverage: "Aider's code/ask/architect/help chat-mode definitions and the architect-mode two-model mechanic."
```

## Macro / Meso / Micro

### Macro

Across independently maintained practitioner repos, the same handful of structural ideas keep reappearing under different names: a thin coordinating layer that routes to specialized workers, a discipline of small reversible units of change, and a low-ceremony single entry point for a human or agent to start from. None of these require adopting a repo's full framework -- each is separable and independently adoptable. This page states each as a general pattern rather than a literal file-tree port, consistent with this KB's own operating instruction to translate external-repo evidence rather than revive it as a runtime spec.

### Meso

**Orchestrator-routes-to-specialized-agents** (BMAD-METHOD): the repo's confirmed structure is `bmad-core/agents/` containing `bmad-orchestrator.md`, `analyst.md`, `architect.md`, `dev.md`, `qa.md`, `pm.md`, alongside `bmad-core/tasks/`, `templates/` (including `story-template.md`, `epic-template.md`), and `workflows/` (`create-story.md`, `dev-story.md`, `code-review.md`), with a `.claude/agents/` directory holding Claude-Code-specific subagent versions (research note lines 131-133). The research explicitly frames the transferable lesson, not the file-for-file copy: "pattern: bmad-orchestrator.md routes tasks to specialized agents... how_apex_could_use: apex-orchestrator.md routes to KB/Sync/Plan/Session agents" (lines 95). **Atomic commit + two-model routing** (Aider): the research notes "Every action = Git commit (atomic, reversible)... how_apex_could_use: Apex session executor commits per task step; rollback on failure" (line 101), which is independently corroborated by Aider's own docs describing `architect` mode where "An architect model will propose changes and an editor model will translate that proposal into specific file edits" (aider modes.md line 11) -- a real two-model routing split, not a research paraphrase. **Bash-first bootstrap** (personal-os): confirmed structure is `GOALS.md` (generated), `AGENTS.md` (Claude Code entry point), `setup.sh`, `workspace/`, `templates/` (research note lines 148-149), with the transferable lesson stated as "Bash-first, LLM-assisted second... how_apex_could_use: Deterministic sync/init scripts; LLM only for reasoning tasks" (line 107).

### Micro

The research pass itself already applies the "translate, don't copy" discipline this page follows: every `copyable_patterns` entry it records is paired with a `how_apex_could_use` reframing rather than a literal file-path port, e.g. BMAD's `dist/teams/` bundled configs become "Apex dist/ with pre-bundled agent team for project type" (line 95), and personal-os's `AGENTS.md` entry point becomes "APEX.md = central orchestration entry" (line 107). The research's own risk flags corroborate why literal porting would be unsound in at least one case: personal-os is explicitly flagged `[low_maturity, unverified_file_tree]` with "structure unverified beyond README" (line 107) -- evidence should be weighted by how directly it was confirmed, and this page inherits that same caution rather than treating all three repos' structures as equally solid.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "BMAD-METHOD's confirmed structure separates a single orchestrator agent file from role-specific agent files (analyst, architect, dev, qa, pm), task/workflow/template directories, and a bundled-team-config directory -- an orchestrator-routes-to-specialized-agents pattern, not a monolithic agent."
    source_pointer: "OrchestrationAgentsInCC_RepoResearch_CC.md lines 131-133"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages: []
  - claim_id: C002
    claim: "Aider commits every LLM-driven change as a discrete, atomic Git commit, and its architect chat mode splits work across two models -- one that proposes changes and a separate one that translates the proposal into specific file edits."
    source_pointer: "OrchestrationAgentsInCC_RepoResearch_CC.md line 101; aider docs/usage/modes.md line 11"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages: []
  - claim_id: C003
    claim: "personal-os's confirmed structure is a bash-first setup.sh that generates GOALS.md and points to a single Markdown entry point (AGENTS.md) for Claude Code, deliberately minimizing LLM calls for routine setup."
    source_pointer: "OrchestrationAgentsInCC_RepoResearch_CC.md lines 107, 148-149"
    confidence: "medium"
    claim_label: "source_backed_summary"
    used_in_pages: []
  - claim_id: C004
    claim: "The research pass itself flags personal-os's structure as low-maturity and unverified beyond its README, meaning this repo's patterns should be weighted with lower confidence than BMAD-METHOD's or Aider's, which were more directly confirmed."
    source_pointer: "OrchestrationAgentsInCC_RepoResearch_CC.md line 107 (risk_flags: [low_maturity, unverified_file_tree])"
    confidence: "medium"
    claim_label: "source_backed_summary"
    used_in_pages: []
```

## Routes Here

```yaml
routes:
  - question: "What can I actually learn from BMAD-METHOD, Aider, or personal-os without adopting their whole framework?"
    leads_to: "wiki/summaries/external-repo-orchestration-patterns.md"
    rationale: "Direct extraction of transferable patterns with confidence levels attached per repo."
  - question: "Is there a real example of a two-model propose/apply routing split?"
    leads_to: "wiki/summaries/external-repo-orchestration-patterns.md"
    rationale: "Aider's architect/editor split is a concrete, corroborated instance."
  - related_page: "wiki/summaries/apex-application-orchestration-patterns.md"
    relation: "Continues the how_apex_could_use reframing from this page into Apex's actual KB/Sync/Plan/Session subsystems."
  - related_page: "wiki/summaries/named-orchestration-workflow-patterns.md"
    relation: "Complementary page classifying workflow shapes by the canonical Anthropic-adjacent vocabulary rather than by source repo."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "SWE-agent's ACI (agent-computer interface) pattern -- issue-to-fix-to-validate loop with structured tool calls -- was ranked in the same research pass (final_score noted, 'Study ACI + validation') but not covered in depth on this page; a follow-up page or extension could cover it directly from princeton-nlp/SWE-agent's own docs rather than only the secondary research note."
    source_pointer: "OrchestrationAgentsInCC_RepoResearch_CC.md line 68"
    proposed_handling: "planning_task_candidate"
  - id: U002
    description: "Star counts, 'last_updated,' and license fields in the research note were not independently reverified against the live repos for this page; treat them as the research pass's snapshot rather than currently-verified facts."
    proposed_handling: "leave_as_gap"
  - id: U003
    description: "A prior handover document for this KB referenced a cross-KB precedent file (apex-meta/handoff/agent-skill-system-research/best-practice-report.md, 'decision 5') for the translate-not-copy rule applied on this page. That file does not exist anywhere in this repo as of this writing -- it was not cited in this page's frontmatter or body, and the rule here is grounded only in this KB's own handover text, not in that unverifiable cross-reference."
    proposed_handling: "ask_operator"
```
