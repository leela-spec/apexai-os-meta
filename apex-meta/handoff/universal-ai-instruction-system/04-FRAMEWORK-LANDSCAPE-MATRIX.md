---
type: ResearchMatrix
title: Universal Agent Instruction Framework Landscape
status: corrected_research_authority
created: 2026-09-04
supersedes: preliminary framework conclusions in 00-ARCHITECTURE-DECISION.md
---

# Universal Agent Instruction Framework Landscape

## Research target

Find existing, proven approaches for this exact target:

> Give an AI agent a very small always-loaded set of behavioral principles. Keep the surface token-efficient. Let the agent load deeper methods, references, examples, or procedures only when the active task needs them.

The always-loaded rules may be written compactly inside `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, a custom-instruction field, or equivalent. XML is evaluated as an internal structuring syntax inside those files, not as a separate storage system.

## Executive finding

This target **already exists as a convergent design pattern across major agent systems**.

The strongest common architecture is:

```text
L0 — small always-on agent constitution / map
  ↓
L1 — conditional rules or skill metadata
  ↓ when relevant
L2 — focused method / SKILL.md / workflow
  ↓ when needed
L3 — references / examples / scripts / evidence
```

No single vendor owns this pattern. It appears independently in Agent Skills, Claude Code, Cursor, Windsurf, Kiro, Gemini CLI, GitHub Copilot, OpenHands, Factory Droid, Cline, Spec Kit, BMAD, and OpenAI's own Codex repository practice.

## Framework matrix

| # | Framework / product | Always-on surface | Conditional / scoped surface | Deep / procedural surface | Trigger mechanism | Token-efficiency pattern | Cross-agent portability | XML fit | Evidence maturity | Fit to Apex target |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | **AGENTS.md open standard** | Root `AGENTS.md`; nested files by directory | Nested `AGENTS.md` scope | Ordinary repo docs referenced by path | Directory hierarchy / nearest file | Root can remain small; nested scope reduces irrelevant instructions | **Very high for coding agents**; 60k+ OSS projects and broad client support | Allowed as text inside Markdown; no parser semantics | **Very high** | **Excellent L0 carrier** |
| 2 | **Agent Skills open standard** | Only skill `name` + `description` metadata (~100 tokens per skill) | Skill selected by model relevance | Full `SKILL.md` then `references/`, `scripts/`, assets | Semantic match on description; user invocation varies by client | **Explicit 3-level progressive disclosure** | **High and growing** across compatible clients | XML not needed in metadata; body unrestricted Markdown | **Very high** | **Best L1→L3 model** |
| 3 | **Claude Code** | `CLAUDE.md`, user/org managed instructions | `.claude/rules/` path-scoped rules | Skills for task-specific procedures; references inside skills | Hierarchy, file paths, task relevance | Docs explicitly say keep universal facts in CLAUDE.md; move multi-step or narrow procedure to skills/path rules | Medium across vendors; concepts portable, filenames not | **Strong**: Anthropic explicitly recommends XML tags for complex prompts | **Very high** | **Excellent reference implementation** |
| 4 | **Cursor** | User/team/project Rules or `AGENTS.md` | Rules: Always Apply / Apply Intelligently / Specific Files / Manual | Skills for specialized knowledge/procedures | Model relevance, glob, manual, always | Official guidance: rules should be short/specific and point to examples rather than copy them | Medium-high; supports AGENTS.md and skills | Works as text; Markdown is native | **High** | **Excellent activation model** |
| 5 | **Windsurf Cascade** | Global rules or root `AGENTS.md` | `always_on`, `glob`, `model_decision`, `manual` rules | Skills + Workflows + references | Model decision, glob, manual mention | `model_decision` exposes only description until relevant; skills expose only name/description before invocation | Medium-high; supports AGENTS.md + Agent Skills | **Explicitly documented as effective for grouping related rules** | **High** | **Closest direct match to proposed XML + progressive disclosure** |
| 6 | **Kiro Steering** | Global/workspace steering; project foundation files; AGENTS.md | `always`, `fileMatch`, `auto`, `manual` inclusion | Skills/resources/custom agents | File match, model relevance, manual | Auto inclusion lets only description guide relevance before full context | Medium; AGENTS/Skills increase portability | Plain Markdown native; XML usable but not required | **High** | **Excellent rule-routing reference** |
| 7 | **Gemini CLI** | Global + workspace `GEMINI.md` | Subdirectory JIT context discovered when files are accessed | Other project docs; manual `@file` inclusion | Hierarchical discovery + JIT directory access | JIT context files load only when the agent enters relevant areas | Medium-high; configurable to use `AGENTS.md` | Google prompt guidance supports XML-like delimiters and `##` | **High** | **Excellent hierarchy/JIT reference** |
| 8 | **GitHub Copilot** | personal/repository instructions or AGENTS.md | `.github/instructions/*.instructions.md` with `applyTo` | Prompt files / skills depending surface | Scope hierarchy + file glob + manual prompt | Path-specific instructions explicitly avoid overloading repository-wide context | **High** across GitHub surfaces; also consumes AGENTS/CLAUDE/GEMINI in CLI/cloud agent | Text-compatible; Markdown native | **Very high** | **Excellent scoping reference** |
| 9 | **OpenHands** | Root `AGENTS.md` recommended | Keyword-triggered skills; AgentSkills model invocation | Full Agent Skills resources | Keyword or semantic/model trigger | Explicit distinction: permanent context vs triggered/on-demand skills | High concept portability; supports AGENTS + AgentSkills | Text-compatible | **High** | **Excellent trigger reference** |
| 10 | **Factory Droid** | `AGENTS.md` | Folder/project/user Skills | `SKILL.md` + supporting files | Semantic skill selection / user slash | Official guidance: use skills when too specific for always-on AGENTS.md; only descriptions are exposed until invocation | High via AGENTS + AgentSkills-compatible locations | Text-compatible | **High** | **Excellent separation of AGENTS vs Skills** |
| 11 | **Cline** | Global/workspace `.clinerules` | Toggleable modular rule files | Workflows + hooks + rules | Manual toggle; workspace/global scope | Explicit modularization; rule content only present when enabled | Medium; supports several foreign rules formats | XML usable as text; not native schema | **Medium-high** | Good modular rules pattern; weaker automatic semantic routing than Skills |
| 12 | **Devin** | `AGENTS.md` | Nested AGENTS/path context | Repo docs and product workflows | Directory scope | Lightweight predictable agent context | High via AGENTS | Text-compatible | **High** | Strong corroboration, limited conditional framework |
| 13 | **OpenAI Codex harness practice** | Short `AGENTS.md` (~100 lines in published case study) | Nested AGENTS + task-specific docs | Structured `docs/`, exec plans, references | Agent navigates map to source of truth | **Published lesson: give a map, not a 1,000-page manual** | High for coding agents | OpenAI's Codex system prompt itself uses XML-like tagged sections | **Very high empirical production evidence** | **Best evidence for short-root-map architecture** |
| 14 | **GitHub Spec Kit** | Project constitution = persistent guiding principles | Feature spec/plan/tasks | Command/skill workflows, references, convergence | Explicit workflow phase / command | Constitution is small principle layer; detailed requirements live in feature artifacts | Medium; software-development focused | Format is Markdown; XML irrelevant | **High** | Useful model for named principles/constitution, too heavy as universal runtime |
| 15 | **BMAD Method** | Small verified project context block in AGENTS.md | Named agents + skill descriptions/customization | Many Agent Skills/workflows/templates | Skill/agent activation | Current BMAD explicitly curates minimum non-derivable context and uses skills for depth | Medium-high where Agent Skills supported | Text-compatible | **Medium-high** | Useful integration example; full methodology is too large for universal L0 |

## Source-backed notes

### AGENTS.md

The open standard describes itself as a README for agents and reports use across more than 60,000 open-source projects. It is stewarded by the Agentic AI Foundation under the Linux Foundation. Supported clients include Codex, Cursor, Devin, Gemini CLI, GitHub Copilot, Windsurf, Aider, goose, OpenHands-compatible ecosystems, and others.

Primary sources:

- https://agents.md/
- https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation

### Agent Skills

The specification formalizes exactly three loading levels:

1. name + description metadata at startup;
2. full `SKILL.md` only after activation;
3. reference/scripts/assets only as required.

It recommends focused references and shallow reference depth.

Primary source:

- https://agentskills.io/specification
- https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills

### Claude Code

Claude's current documentation explicitly separates:

- facts/rules that belong in every session → `CLAUDE.md`;
- path-specific instructions → `.claude/rules/`;
- task-specific or multi-step procedures → Skills.

It also says more specific and concise instructions are followed more consistently.

Primary source:

- https://code.claude.com/docs/en/memory

### Cursor

Cursor provides four rule activation modes: always, intelligent/relevance, specific files, manual. Its official guidance says good rules are short, specific, and point to examples instead of copying them.

Primary source:

- https://cursor.com/docs/rules
- https://cursor.com/learn/customizing-agents

### Windsurf

Windsurf currently provides the most direct confirmation of the proposed architecture. Rules can be `always_on`, `glob`, `model_decision`, or `manual`. In `model_decision` mode, only the description is present in the system prompt and the full rule is read only if Cascade judges it relevant. Its docs separately distinguish Rules, AGENTS.md, Workflows, Skills, and Memories.

Its rule best-practice documentation also explicitly says XML tags can effectively group related rules.

Primary sources:

- https://docs.windsurf.com/windsurf/cascade/memories
- https://docs.windsurf.com/windsurf/cascade/skills
- https://docs.windsurf.com/windsurf/cascade/workflows

### Kiro

Kiro Steering supports global/workspace scope plus `always`, `fileMatch`, `auto`, and `manual` inclusion. Auto inclusion uses a small name/description routing surface. Kiro also consumes AGENTS.md and Agent Skills.

Primary source:

- https://kiro.dev/docs/steering/

### Gemini CLI

Gemini has global, workspace, and JIT subdirectory context. Subdirectory `GEMINI.md` files are discovered when tools access files in that area. `@file` imports are different: imports expand content into context, so they should not be used for deep references if the goal is token-saving JIT reads.

Primary source:

- https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/gemini-md.md

### GitHub Copilot

Copilot distinguishes repo-wide instructions, path-specific `applyTo` instructions, agent files, and task-specific prompt files. GitHub explicitly frames path-specific instructions as a way to avoid overloading the repo-wide surface.

Primary source:

- https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions
- https://docs.github.com/en/copilot/concepts/prompting/response-customization

### OpenHands

OpenHands explicitly recommends `AGENTS.md` for permanent context and Agent Skills for progressive disclosure. It also extends skills with keyword triggers.

Primary source:

- https://docs.openhands.dev/overview/skills
- https://docs.openhands.dev/overview/skills/keyword

### Factory Droid

Factory states directly: use `AGENTS.md` for always-on repository instructions; use Skills when guidance is too specific for always-on AGENTS.md and reusable enough to package. Skills progressively disclose only name/description until invocation.

Primary source:

- https://docs.factory.ai/harness/skills

### OpenAI production practice

OpenAI's published 2026 harness-engineering case study says the team tried one large AGENTS.md and found it failed because it crowded out task context, made everything look equally important, rotted, and was hard to verify. They replaced it with a short AGENTS.md (roughly 100 lines) functioning as a map to structured repository knowledge.

Primary source:

- https://openai.com/index/harness-engineering/

## What this matrix says about the Apex target

The target is not a new framework. The closest established composition is:

```text
AGENTS.md-style always-on constitution
+
Agent Skills-style semantic progressive disclosure
+
Cursor/Windsurf/Kiro-style conditional rule activation
+
OpenAI-style repository map to sources of truth
```

The innovation should be limited to **which operator-specific principles belong in L0 and how they are worded**, not a new loading architecture.
