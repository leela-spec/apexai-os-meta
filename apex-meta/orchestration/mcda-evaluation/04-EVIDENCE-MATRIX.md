# 04 — Evidence Matrix: Master of Arts Orchestration

Status: **desk evidence complete / pilots not yet run**  
Evidence date: **2026-08-21**  
Decision profile: **Balanced**

## 1. Evaluation rule

This matrix applies the scope in `03-SCOPE-LOCK.md` and the gates in `00-MCDA-CHARTER.md`.

**Whole-system first:** evaluate an established system in its native/upstream-supported form before inventing a composition. A second layer is allowed only for a demonstrated load-bearing gap. Upstream-supported integrations count as part of the system path; homemade synchronization glue does not.

Evidence grades:

- **A** — official docs/repository plus direct feature evidence and/or pilot;
- **B** — official docs/examples support the claim, but not yet tested against Master of Arts;
- **C** — credible inference from a generic mechanism, with no direct MoA/non-software proof;
- **D** — speculation; cannot support a winner.

## 2. Current maturity snapshot

Current GitHub repository metadata checked 2026-08-21:

| Project | Current adoption signal | Activity signal | Relevance |
|---|---:|---|---|
| GitHub Spec Kit | ~130.7k stars | pushed 2026-08-21 | strongest current spec/workflow candidate |
| Superpowers | ~275.5k stars | pushed 2026-08-19 | very strong skill/process donor, software-centric |
| Ruflo | ~68.6k stars | pushed 2026-08-21 | powerful agent meta-harness, high complexity |
| OpenSpec | ~65.8k stars | pushed 2026-08-21 | mature/lightweight spec layer, software-centric |
| BMAD Method | ~52.1k stars | pushed 2026-08-21 | mature role/workflow methodology, software-centric |
| Task Master | ~28.0k stars | last push observed 2026-04-28 | strong AI task manager, dev-oriented |
| Beads | ~26.5k stars | pushed 2026-08-21 | strongest specialized durable agent task graph |
| Gas City | ~1.15k stars | pushed 2026-08-21 | new but active orchestration-builder SDK |

Popularity does **not** override hard-gate failure.

## 3. Source register

### GitHub Spec Kit

Official/current sources:

- https://github.github.com/spec-kit/
- https://github.com/github/spec-kit/blob/main/docs/index.md
- https://github.com/github/spec-kit/blob/main/docs/reference/workflows.md
- https://github.com/github/spec-kit/blob/main/docs/reference/integrations.md
- https://github.com/github/spec-kit/blob/main/templates/commands/taskstoissues.md
- https://github.com/github/spec-kit/blob/main/workflows/ARCHITECTURE.md

Direct evidence:

- explicitly describes itself as an intent-driven harness for the SDLC **or any business process**;
- current docs show 35+ integrations and skills-based integrations for Claude Code, Codex CLI and Antigravity;
- workflow engine supports commands, prompts, shell steps, gates, conditionals, loops, fan-out/fan-in;
- workflow run state persists under `.specify/workflows/runs/<run_id>/` as `state.json`, `inputs.json`, `log.jsonl` and a workflow copy;
- runs can resume from paused/failed state;
- `--json` provides machine-readable outcomes;
- project overlays preserve local changes across workflow updates;
- built-in `taskstoissues` converts dependency-ordered tasks into GitHub Issues and avoids duplicates;
- community catalog includes non-software presets such as Fiction Book Writing, providing evidence that the system is not intrinsically limited to code outputs;
- official docs warn that community workflows/extensions are independently maintained and must be reviewed before installation.

Important limitation:

- the default mental model and built-in SDD cycle remain software-oriented;
- no direct native ChatGPT-web integration was found. Repo-connected ChatGPT can still read GitHub state/artifacts, but does not execute the local `specify` CLI itself;
- workflow state gives strong run-level durability but is not by itself a portfolio issue graph. The built-in GitHub-Issues bridge materially reduces this gap.

### Beads

Official/current sources:

- https://github.com/gastownhall/beads
- https://github.com/gastownhall/beads/blob/main/README.md
- https://github.com/gastownhall/beads/blob/main/docs/index.md
- https://github.com/gastownhall/beads/blob/main/docs/reference/faq.md
- https://github.com/gastownhall/beads/blob/main/examples/README.md

Direct evidence:

- Dolt-backed distributed graph issue tracker for AI agents;
- durable dependency graph with `blocks`, `parent-child`, `related`, `discovered-from`, etc.;
- atomic claiming, priorities, history, ready-work detection and JSON output;
- formulas/molecules provide reusable workflow graphs;
- gates support asynchronous coordination;
- direct setup support for Codex, Claude and other agents plus generic `AGENTS.md` guidance;
- compaction/memory decay summarizes older closed work to reduce context burden;
- graph links and persistent memories are first-class;
- examples include multiple-persona architect/implementer/reviewer flows;
- state sync uses Dolt, not ordinary Git issue files.

Important limitation:

- official positioning is still explicitly **coding-agent** oriented;
- non-software business fit is inferred from the generic issue/graph model rather than demonstrated by official business workflows;
- browser/web AI with only ordinary GitHub repository access cannot naturally inspect the live Dolt work graph the same way a local `bd` client can;
- introduces another state substrate and operational concept (Dolt) alongside Git/GitHub.

### GitHub Issues + Projects + portable Agent Skills — control

Official/current sources:

- https://docs.github.com/en/issues/tracking-your-work-with-issues/learning-about-issues/about-issues
- https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects
- https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-issue-dependencies
- https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/browsing-sub-issues
- https://agentskills.io/specification
- https://openai.com/academy/skills/

Direct evidence:

- Issues explicitly support ideas, feedback, tasks, bugs and general work;
- sub-issues provide hierarchy and issue dependencies model blocking relations;
- Projects provides table/board/roadmap views, filters, charts, custom fields, templates and built-in automation;
- GitHub APIs, CLI and Actions provide deterministic machine access and automation;
- state is directly visible to web users and repo-connected agents;
- project/issue state is durable, auditable and permissioned;
- Agent Skills is an open `SKILL.md`-based format; skills are portable/versionable and use progressive disclosure; compatible agents include OpenAI Codex and Claude Code, while ChatGPT supports reusable skills in the same open format.

Important limitation:

- GitHub does not itself provide an AI-agent workflow runtime comparable to Spec Kit workflows or Gas City formulas;
- no native `ready` transitive dependency computation/atomic agent claim equivalent to Beads was found;
- maker/reviewer/CEO-gate semantics must be represented through existing issue fields/statuses, PR/document review and/or Actions rather than a dedicated generic workflow gate primitive;
- skill discovery is supplied by the Agent Skills ecosystem/clients, not by GitHub Projects itself.

### Gas City

Official/current sources:

- https://github.com/gastownhall/gascity
- https://github.com/gastownhall/gascity/blob/main/README.md
- https://github.com/gastownhall/gascity-packs
- https://github.com/gastownhall/gascity/blob/main/engdocs/architecture/formulas.md

Direct evidence:

- declarative `city.toml` configuration;
- multiple runtime providers;
- Beads-backed work tracking, formulas, molecules, waits and mail;
- controller/supervisor reconciliation loop;
- reusable packs and pinned imports;
- official pack repository adapts established methods such as BMAD, Superpowers, gstack and Compound Engineering into Gas City formulas;
- strong fan-out/fan-in, review and automation capabilities.

Hard limitation for MoA:

- official description is an **orchestration-builder SDK for multi-agent coding workflows** and docs frame it as a platform for software factories;
- no official non-software operating-business examples were found;
- it is young (created 2026-02) and substantially more operationally complex than Spec Kit/GitHub control.

### Superpowers

Official/current sources:

- https://github.com/obra/superpowers
- https://github.com/obra/superpowers/blob/main/README.md
- current skills such as `executing-plans`, `verification-before-completion`, subagent-driven development and review flows.

Direct evidence:

- exceptionally strong reusable skills/process discipline;
- explicit brainstorming → plan → execution → verification/review flow;
- maker/reviewer separation and evidence-before-completion practices;
- broad coding-agent support and an Agent Skills-compatible structure.

Hard limitation for MoA:

- official identity is an **agentic skills framework & software development methodology**;
- no durable portfolio task/state substrate is provided as the core product;
- no evidence that the shipped methodology covers admin/client/research/workshop portfolio management without authoring a new method layer.

Use in later architecture: excellent **skill/process donor**, not production portfolio core.

### BMAD Method

Official/current sources:

- https://github.com/bmad-code-org/BMAD-METHOD
- https://github.com/bmad-code-org/BMAD-METHOD/blob/main/README.md
- https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/index.md

Direct evidence:

- 34+ structured workflows, specialized roles, scale-adaptive planning and a builder for custom agents/workflows;
- strong human-in-the-loop planning orientation;
- official web bundles package selected skills for ChatGPT Custom GPTs and Gemini Gems, including brainstorming, product brief, PRFAQ, PRD, UX, market and industry research;
- high adoption and active maintenance.

Hard limitation for MoA:

- core BMad Method is explicitly an AI-driven **software development** framework;
- non-code web bundles cover useful planning/research tasks but not a durable whole-business operating system for client/admin/workshop/content/project state;
- using BMad Builder to create a complete MoA method would move too much responsibility back to us unless an existing proven module already owns that domain.

Use in later architecture: potential **method/role donor**, especially for planning and web-subscription work.

### OpenSpec

Official/current sources:

- https://github.com/Fission-AI/OpenSpec
- current README/docs.

Direct evidence:

- lightweight structured change folders with proposals/specs/design/tasks;
- 20–25+ agent integrations;
- no API keys required;
- very strong intent/change auditability with a simpler footprint than many alternatives.

Hard limitation for MoA:

- official scope is explicitly **spec-driven development for AI coding assistants**;
- not a continuous portfolio orchestration runtime/task graph;
- no direct evidence for administration/client delivery/workshop operating cycles.

Use in later architecture: spec/change-control donor if a selected core lacks this capability.

### Task Master

Official/current sources:

- https://github.com/eyaltoledano/claude-task-master
- current README/model docs.

Direct evidence:

- AI-powered hierarchical task management and PRD decomposition;
- supports Claude Code and Codex CLI provider modes that can use subscription/OAuth instead of a separate API key;
- machine-readable task/status structures and broad editor integration.

Correction to initial screen:

- **G10 does not automatically fail**: current Task Master supports Claude Code and Codex CLI modes without separate metered API keys.

Hard limitation for MoA:

- product is still centered on AI-driven development/PRD implementation;
- no strong evidence for generic CEO approval gates or non-software business workflows;
- not promoted over the stronger domain-neutral GitHub control.

### Ruflo

Official/current sources:

- https://github.com/ruvnet/ruflo
- current README/wiki/plugin docs.

Direct evidence:

- powerful multi-agent harness with swarms, 60–100+ agent types, hundreds of MCP tools, memory/RAG, recurring workers, security plugins and Claude Code/Codex support;
- persistent/self-learning memory and reusable workflow plugins;
- high adoption and active development.

Hard limitation for MoA:

- production positioning and marketplace are still centered on continuous software engineering/coding workflows;
- full installation creates a large operational surface (MCP server, hooks, daemon, memory/vector components, large tool/agent catalog);
- canonical memory/state is not naturally the simple repo-visible portfolio SSOT required for web-agent interoperability;
- materially violates the simplicity bias unless a future pilot proves capabilities unavailable from simpler systems.

### Hermes Agent / OpenClaw

Official/current sources checked:

- Hermes skills/tools/memory/delegation docs in `NousResearch/hermes-agent`;
- OpenClaw AgentSkills-compatible workspace skills docs.

Direct evidence:

- both are capable runtime/agent shells with skills, memory, tool execution and delegation/automation features;
- Hermes supports open Agent Skills, progressive disclosure, persistent memory, delegation and cron;
- OpenClaw supports AgentSkills-compatible workspace/project skills.

Hard limitation for the portfolio-core decision:

- their principal value is **agent runtime/execution**, not a repo-visible portfolio project/task SSOT with issue hierarchy/dependencies/CEO project views;
- they can remain execution clients around the selected orchestration/project system, but should not become the sole project truth.

## 4. Hard-gate outcome

Legend: **PASS**, **PASS-C** = passes provisionally but requires MoA pilot, **FAIL**, **N/A** = not scored because an earlier load-bearing gate fails.

| Candidate | G1 | G2 | G3 durable state | G4 cross-agent | G5 CEO gates | G6 deterministic | G7 resume | G8 review | G9 non-software | G10 no mandatory API | Outcome |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Spec Kit + built-in GitHub Issues bridge** | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS-C | PASS | **SURVIVES** |
| **GitHub Issues/Projects + Agent Skills control** | PASS | PASS | PASS | PASS | PASS-C | PASS | PASS | PASS-C | PASS | PASS | **SURVIVES** |
| **Beads** | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS-C | PASS | **SURVIVES** |
| Gas City | PASS | PASS-C | PASS | PASS | PASS | PASS | PASS | PASS | **FAIL** | PASS | eliminate as core |
| Superpowers | PASS | PASS | **FAIL as portfolio state core** | PASS | PASS | PASS | PASS-C | PASS | **FAIL** | PASS | donor only |
| BMAD Method | PASS | PASS | PASS-C | PASS | PASS | PASS-C | PASS-C | PASS | **FAIL** | PASS | donor only |
| OpenSpec | PASS | PASS | PASS | PASS | PASS-C | PASS | **FAIL as continuous orchestration core** | PASS-C | **FAIL** | PASS | donor only |
| Task Master | PASS | PASS | PASS | PASS | PASS-C | PASS-C | PASS | PASS-C | **FAIL** | PASS | eliminate as core |
| Ruflo | PASS | PASS | PASS-C | PASS | PASS-C | PASS | PASS | PASS | **FAIL** | PASS-C | eliminate as core |
| Hermes/OpenClaw runtime | PASS | PASS | **FAIL as portfolio SSOT** | PASS-C | PASS-C | PASS | PASS | PASS-C | PASS-C | PASS-C | runtime/reference |

## 5. Why the three survivors are meaningfully different

### Spec Kit + built-in GitHub Issues bridge

**Owns:** process/workflow execution, artifacts, resumable state, human gates, reusable workflows/presets/extensions, cross-agent CLI integration, task-to-Issue materialization.

**Open question:** whether one upstream-configured Spec Kit process can stay natural across admin/coaching/research/workshop/content work without too much software vocabulary.

### GitHub-native control

**Owns:** canonical portfolio work state, human visibility, issue hierarchy/dependencies, project fields/views, APIs, permissions, durable review/history.

**Open question:** whether lack of a dedicated agent workflow engine creates too much repeated orchestration/prompting.

### Beads

**Owns:** the best agent-native dependency/task graph, ready work, claims, graph links, durable compact state, formulas and memory compaction.

**Open question:** whether Dolt and coding-centric defaults create unnecessary complexity and weaker web-agent visibility compared with GitHub Issues.

## 6. Composition rule after evidence pass

The earlier hypothesis `Spec Kit + Beads + Agent Skills` is **not** automatically advanced.

Spec Kit now has more native capability than the initial screen assumed, including:

- workflow engine;
- persisted resumable state;
- human gates;
- multi-agent integrations;
- extensions/presets/bundles;
- built-in GitHub task materialization.

Therefore the next test is:

> **Can Spec Kit + GitHub's native state pass the MoA pilots without Beads?**

Only if a pilot demonstrates a real gap in ready-work computation, claims, dependency graph semantics or context compaction should Beads be added. This prevents duplicate task truth.
