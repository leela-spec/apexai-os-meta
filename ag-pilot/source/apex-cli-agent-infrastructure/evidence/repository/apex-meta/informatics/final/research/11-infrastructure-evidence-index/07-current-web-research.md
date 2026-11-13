---
type: ResearchBrief
id: RESEARCH-INFRASTRUCTURE-CURRENT-WEB
title: Current web research and next-study agenda
description: Dated primary-source findings and unresolved research questions for CLI instructions, skills, agents, hooks, and shared infrastructure.
status: current
tags: [informatics, research, cli, hooks, skills, evidence]
---

# Current web research

Research checked on **2026-11-12**. This is a verified starting brief for the processing prompt, not the completed cross-CLI architecture study. Official pages describe available product behavior; they do not prove the installed workstation versions, account availability, or runtime configuration. Repository references in this package are root-relative; public vendor documentation retains ordinary web citations.

The [source register](apex-meta/informatics/final/research/11-infrastructure-evidence-index/web-research-sources.json) records 16 opened primary sources, retrieval dates, reviewed sections, and evidence limits. The two preprints received abstract-level review only. Re-open sources when executing the processing prompt.

## Findings that affect the next design

| Finding | Primary evidence | Implication for the study |
|---|---|---|
| Codex documents native pre-/post-tool hooks and model/context lifecycle events. Its tool-coverage table also identifies exclusions, including hosted tools and specialized paths. | [OpenAI hooks: Tool coverage and PreToolUse](https://learn.chatgpt.com/docs/hooks) | Revisit the historical git-only premise. Map exact tool coverage and failure behavior before treating hooks as complete enforcement. Installed behavior remains unverified. |
| Codex skills support explicit invocation and description-based implicit invocation. Invocation policy can disable implicit selection. | [Build skills: How ChatGPT and Codex use skills](https://learn.chatgpt.com/docs/build-skills) | Test discovery, invocation policy, and missed activation separately from correctness after activation. |
| Codex instruction discovery is hierarchical and includes override precedence and a combined byte budget. Custom agents have their own project/user configuration surfaces. | [AGENTS.md discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [Subagents: Custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents) | Reconcile actual loaded context and agent scope before proposing carrier copies or shared role files. |
| OpenAI's plugin architecture groups capabilities, while execution-environment support can differ by surface. | [Plugin architecture](https://developers.openai.com/plugins/concepts/plugins) | Evaluate packaging independently of whether installed scripts or lifecycle adapters execute in each host. |
| Claude Code documents event-specific hook inputs, outputs, decision controls, prompt events, and compaction events. | [Claude Code hook reference](https://code.claude.com/docs/en/hooks) | Build an event/payload/control matrix. Do not copy one event's blocking or injection response to another. |
| Claude Code separates manual/model skill invocation and supports isolated skill execution; subagents have their own loading and permission behavior. | [Claude Code skills](https://code.claude.com/docs/en/skills), [Claude Code subagents](https://code.claude.com/docs/en/sub-agents) | Test skill lifetime, child context, and inherited instructions. Description similarity alone cannot establish equivalent semantics. |
| Antigravity documents workspace, global, and plugin hooks, plus different App/CLI/IDE surfaces. Its hook reference includes model invocation events. | [Antigravity hooks](https://antigravity.google/docs/hooks) | Keep surface identity, configuration roots, event schemas, and context delivery distinct. Validate the installed product rather than infer behavior from the Antigravity name. |
| Antigravity documents native skills, custom subagents, and a Gemini CLI migration path. | [Agent skills](https://antigravity.google/docs/skills/), [Custom subagents](https://antigravity.google/docs/subagents/), [Gemini CLI migration](https://antigravity.google/docs/cli/gcli-migration/) | Check legacy versus current config, migrated capabilities, and agent definitions explicitly. A migration guide is not proof that this workstation migrated. |
| The Agent Skills specification defines the portable skill package and progressive loading conventions. MCP defines a separate tool/context connectivity protocol. | [Agent Skills specification](https://agentskills.io/specification), [MCP specification](https://modelcontextprotocol.io/specification/latest) | Separate package conformance, host routing, execution authority, and connectivity. Conformance to one does not imply the others. |

These implications are design inferences from the cited documentation. No hook was installed, no CLI was upgraded, and no live capability probe was run for this brief.

## Empirical research that can challenge the design

The July 2026 preprint [Do Context Files Help Coding Agents?](https://arxiv.org/abs/2607.27250) reports a controlled context-injection ablation on two agents and real repository tasks. Its abstract reports no measurable correctness improvement within the study's bounds. Treat it as a counterexample to universal claims that more persistent context improves outcomes. This run read the abstract and bibliographic record; the next study must inspect methods, released data, and task applicability before using the result quantitatively.

The September 2026 preprint [Scanning the Harness, version 3](https://arxiv.org/abs/2609.07360v3) studies configuration exposures and conformance in public agent setups. The authors distinguish repository-declaration findings from unmeasured runtime consequences. Use it to frame package review and version-specific permission semantics, not to infer that a particular Apex configuration is exploitable. This run read the abstract and revision record; full methodological appraisal remains to be done.

## Required deeper web research

The [processing prompt](apex-meta/informatics/final/research/11-infrastructure-evidence-index/PROCESSING-PROMPT.md) requires the receiving model to extend this brief in its own execution date context:

1. Re-open current official documentation and release notes for Codex, Claude Code, and Antigravity. Distinguish CLI, desktop, IDE, SDK, hosted, and headless execution.
2. Check instruction discovery, precedence, scoped rules, skill metadata, invocation policy, plugin distribution, custom agent definitions, hooks, permissions, and lifecycle/state recovery for each surface.
3. Examine secondary agents or CLIs actually present in repository evidence. Separate historically studied products from tools currently in use. Broaden the candidate landscape when a materially different mechanism could change the architecture decision.
4. Trace important capability claims to official schemas or code and versioned releases where accessible. Seek primary empirical studies that could falsify the proposed mechanism, including null results and failed replications.
5. Distinguish documented, repository-observed, runtime-measured, source-reported, inferred, and proposed claims. Record dates, versions, inaccessible evidence, disagreements, and implications for previous Apex decisions.

## Source discovery and stopping rule

Begin with the cited official pages and follow their current documentation indexes and release links. Search by the unresolved mechanism and platform, rather than by a preferred architecture. Use community material only to discover leads; verify capability claims in primary sources.

Continue until each material capability or proposed decision has suitable evidence or an explicit unresolved gap, each serious alternative has been evaluated, and recent contrary evidence has been considered. Do not stop because an arbitrary source count is reached. Do not call a search-result snippet a verified source.

## Limits and failure guards

Retrieval date is not a publication date. No exact installed version or latest release number is asserted here. Documentation URLs can redirect; record the resolved page and section when rechecking. Public vendor sources are different from private repository navigation. The processing program must use authenticated repository access for the latter and public web access for the former.
