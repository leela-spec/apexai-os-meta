# 06 — What the Alternatives Actually Do: Verified User Stories + Executor Matrix

Status: **explanatory decision artifact; no implementation authorized**  
Evidence checked: **2026-08-21**

## 0. Why the earlier comparison was confusing

The researched systems are **not interchangeable products**. They occupy different layers:

| Layer | What it owns | Researched examples |
|---|---|---|
| Portfolio/project state | What exists, priority, status, dependencies, ownership | GitHub Issues/Projects, Beads, Task Master |
| Workflow/process controller | Which step happens next, gates, loops, fan-out/fan-in, resume | Spec Kit Workflows, Gas City, Ruflo Workflows |
| Skill/method library | How an AI should perform a recurring task | Agent Skills, Superpowers, BMAD skills/bundles, OpenClaw/Hermes skills |
| Agent runtime/executor | Actually invokes models/tools, delegates work, browses, writes files | ChatGPT/Claude/Codex/Antigravity; Hermes; OpenClaw; Ruflo around supported agents |
| Knowledge/memory/retrieval | Stores/searches reusable knowledge across sessions | Ruflo AgentDB/RAG; Hermes built-in/external memory; repo documents for the other systems |
| Durable artifact repository | Final research papers, workshop docs, SOPs, decisions, sources | Git/GitHub repository |

**Critical principle:** the orchestration framework does not create high-quality research by itself. An AI executor creates the research/workshop/content. The framework controls the process, provides context, records state, forces review/gates, and makes the work resumable.

## 1. Evidence notation

- **N — Native / verified:** directly documented or shipped example.
- **A — Adaptation:** verified generic mechanism, but applying it to Master of Arts is our proposed adaptation; not an official MoA/non-software case study.
- **C — Component:** useful at this step, but does not own it end-to-end.
- **—:** no meaningful capability found in current official evidence.

This prevents a generic capability from being presented as a proven Master of Arts use case.

---

# 2. Concrete user stories — what your day would look like

## US1 — GitHub Spec Kit + GitHub Issues/Projects

### Story

**You:** “I want a research-backed 90-minute women’s self-defense workshop. I want three alternative structures, evidence, an operations check, then I decide which one becomes the workshop.”

### What would happen

1. A Spec Kit workflow is started from a durable workflow definition.
2. A prompt step asks an AI executor (for example Codex/Claude/Antigravity) to create the bounded research/design artifact.
3. A **human gate** pauses the workflow so you approve/reject the research framing.
4. A plan step turns the approved framing into a workshop structure.
5. Optional fan-out steps can ask separate AI runs to examine evidence, pedagogy, operations, risk, or content reuse; fan-in collects their results.
6. Another human gate pauses before the workshop becomes accepted work.
7. Tasks can be materialized into GitHub Issues with dependency-aware IDs for portfolio tracking.
8. If the run fails or is interrupted, Spec Kit persists `state.json`, inputs, and a JSONL log and can resume the run.
9. The resulting workshop/research documents live in Git/GitHub.

### Verified basis

Spec Kit officially ships workflow steps for commands, arbitrary AI prompts, shell commands, human gates, conditionals, loops and fan-out/fan-in, with persisted state and resume. It supports Claude Code, Codex CLI and Antigravity integrations. It also ships a `taskstoissues` path that turns tasks into GitHub Issues. A community catalog entry demonstrates that Spec Kit has been adapted beyond code to long-form fiction writing with story bibles, scene tasks and quality gates.

### What Spec Kit does **not** solve

It is **not a semantic knowledge base**. It can keep durable project principles, research/artifact files and workflow logs in the repository, but semantic retrieval across all MoA source documents would still come from the executing agent or a separate proven retrieval/KB layer.

### Sources

- https://github.com/github/spec-kit/blob/main/docs/reference/workflows.md
- https://github.com/github/spec-kit/blob/main/docs/reference/integrations.md
- https://github.com/github/spec-kit/blob/main/templates/commands/taskstoissues.md
- https://github.com/github/spec-kit/blob/main/docs/community/presets.md

---

## US2 — GitHub Issues/Projects + portable Agent Skills

### Story

**You:** “Show me everything active in Master of Arts, what is blocked, what needs my decision, and what the AI team should do next.”

### What would happen

1. Master of Arts work lives as Issues/sub-issues and Project items.
2. Each project can carry fields such as status, priority, horizon, visibility, domain, reviewer, CEO decision state, due date, etc.
3. Parent/sub-issue relationships break a large workshop/research project into smaller pieces.
4. Issue dependencies mark work as blocked by/ blocking other work.
5. A web or CLI AI with GitHub access reads the same issues and repository artifacts.
6. Reusable Agent Skills (`SKILL.md`) tell compatible AIs *how* to perform recurring MoA tasks such as “research synthesis” or “workshop review.”
7. GitHub Actions/scripts can perform deterministic checks and automation.
8. You see the same canonical work state the agents see.

### Verified basis

GitHub Projects provides table, board and roadmap views, custom fields, charts, templates and automation. GitHub Issues supports multi-level sub-issues and explicit blocking dependencies, including machine-readable CLI/JSON access. Agent Skills is an open `SKILL.md` format with scripts/references/assets and progressive disclosure.

### What it does **not** solve

GitHub does not itself orchestrate AI reasoning steps or provide a semantic KB. Without another workflow layer, an AI/human must decide when to invoke research, review, synthesis and approval steps.

### Sources

- https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects
- https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-issue-dependencies
- https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/browsing-sub-issues
- https://agentskills.io/specification

---

## US3 — Beads

### Story

**You:** “I have 40 pieces of work across research, website, coaching, workshops and admin. I do not want agents to keep asking what to do. They should pick work that is actually unblocked, claim it, finish it, and expose new dependencies.”

### What would happen

1. Work is stored in the Beads/Dolt issue graph.
2. Dependencies connect tasks; graph links can express relationships such as related/supersedes/duplicates.
3. An agent asks `bd ready --json` for work with no open blockers.
4. It atomically claims a task with `bd update <id> --claim`.
5. If it discovers new work, it creates and links that work to its parent/discovery source.
6. It closes completed work with an audit trail.
7. Older closed work can be compacted/summarized to reduce agent context load.
8. Beads’ shipped examples include a multiple-persona architect/implementer/reviewer workflow.

### Verified basis

Beads documents ready-work detection, atomic claiming, dependency tracking, JSON output, graph links, semantic compaction and examples for architect/implementer/reviewer separation.

### What it does **not** solve

Beads is primarily an **agent work graph**, not a business knowledge library or a finished CEO methodology. Its official positioning/examples are coding-agent focused. Master of Arts usage would be an adaptation, and browser-only agents cannot naturally manipulate the local Dolt graph without a bridge.

### Sources

- https://github.com/gastownhall/beads
- https://github.com/gastownhall/beads/blob/main/examples/README.md

---

## US4 — Gas City

### Story

**Hypothetical MoA adaptation, not a verified non-software deployment:** “Run a whole workshop-production factory: requirements → plan → review → decomposition → several specialist agents → final audit.”

### What the verified system does

Gas City packages multi-agent workflows as formulas/packs. Its official packs already encode processes such as:

- requirements → plan → review → decompose → implement → three-lane review;
- BMAD PRD → architecture → epics/stories → readiness gate → implementation → audits;
- Superpowers brainstorming → written-spec approval → task execution → compliance/quality review.

### MoA value if adaptation proves viable

The same orchestration mechanics could theoretically map “implementation” to “produce research/workshop/content artifact” and specialist lanes to MoA reviewer roles.

### Why this is not yet a recommendation

Official scope is **multi-agent coding workflows/software factories**. We found no verified Master-of-Arts-like business workflow. Using it for MoA therefore requires a domain adaptation that must be piloted rather than assumed.

### Sources

- https://github.com/gastownhall/gascity-packs
- https://github.com/gastownhall/gascity

---

## US5 — Superpowers

### Story

**Process-pattern adaptation:** “Before an AI writes a workshop, force it to clarify the idea, write a design, get that design independently reviewed, create an explicit plan, execute in bounded tasks, then get an independent final review.”

### What the verified system does

Superpowers ships a disciplined software-development sequence:

- brainstorming/design;
- written plans;
- fresh subagent per task;
- spec-compliance review;
- quality review;
- verification before completion.

It also contains document-review loops for checking completeness, coverage, consistency, clarity and over-engineering before implementation.

### MoA value

The **review discipline and fresh-context reviewer pattern** are highly reusable. A MoA workshop/research skill could borrow that approach.

### What it does **not** solve

Superpowers does not provide the canonical portfolio project database or a general MoA knowledge base. Its shipped methodology is explicitly software development. Treat it as a proven **process/skill donor**, not the business operating system.

### Sources

- https://github.com/obra/superpowers
- https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/SKILL.md
- https://github.com/obra/superpowers/blob/main/docs/superpowers/specs/2026-01-22-document-review-system-design.md

---

## US6 — BMAD Method

### Story

**You:** “I want to sit in ChatGPT and work through market research, an offer concept, and a product/workshop brief without paying API tokens, then hand the polished artifact to the repo/CLI executor.”

### What would happen

1. Install/use a supported BMAD Web Bundle as a ChatGPT Custom GPT or Gemini Gem.
2. The bundle conducts conversational discovery and maintains the artifact during the session.
3. Current official bundles include Brainstorming, Product Brief, PRFAQ, PRD, UX and Market & Industry Research.
4. Deep Research-capable bundles can draft a research brief and ingest the resulting research report.
5. Export/paste the finished artifact into the repository.
6. A CLI-side BMAD or other executor continues from the artifact.

### Verified basis

This web-subscription handoff is an official BMAD workflow, explicitly intended to do planning/research in web subscriptions and implementation in an IDE/CLI.

### What it does **not** solve

BMAD is still fundamentally an AI-driven software-development methodology. Its web bundles are highly relevant to MoA research/planning, but there is no verified whole-business portfolio state, client/admin system or general KB layer.

### Sources

- https://docs.bmad-method.org/explanation/web-bundles/
- https://github.com/bmad-code-org/BMAD-METHOD

---

## US7 — OpenSpec

### Story

**Adaptation:** “Before changing a major MoA method or creating a new workshop, create a durable ‘change package’: why, requirements, design, tasks; approve it; execute it; archive the complete decision trail.”

### What the verified system does

OpenSpec’s default schema is:

`proposal → specs → design → tasks → apply → archive`

Its examples show complete change folders and an archive step that preserves the context after implementation.

### MoA value

This is strong for **decision/change traceability**. A workshop redesign or method change could use the same artifact lifecycle.

### What it does **not** solve

Its official product is spec-driven development for AI coding assistants. It does not provide continuous portfolio orchestration, multi-agent assignment or a general knowledge base.

### Sources

- https://github.com/Fission-AI/OpenSpec/blob/main/docs/examples.md
- https://github.com/Fission-AI/OpenSpec/blob/main/schemas/spec-driven/schema.yaml

---

## US8 — Task Master

### Story

**Adaptation:** “Take a large written project brief and turn it into explicit tasks/subtasks with dependencies and priority, then always tell the AI what the next unblocked task is.”

### What the verified system does

1. Parse a PRD into `tasks.json`.
2. Generate task files.
3. Store status, dependencies, priority and test strategy.
4. Expand complex tasks into subtasks.
5. Determine the next task based on dependencies/status.
6. Perform AI-powered research with project context.
7. Claude Code can be used as a provider without a separate API key.

### MoA value

The PRD-to-task and “next work” model is easy to understand and useful for bounded projects.

### What it does **not** solve

Official usage is development/PRD oriented. It lacks a strong verified CEO-gate/reviewer methodology, portfolio-wide knowledge system and non-software business examples.

### Sources

- https://github.com/eyaltoledano/claude-task-master
- https://github.com/eyaltoledano/claude-task-master/blob/main/apps/docs/capabilities/index.mdx
- https://github.com/eyaltoledano/claude-task-master/blob/main/docs/examples/claude-code-usage.md

---

## US9 — Ruflo

### Story

**You:** “Research three aspects of a topic in parallel, have specialists work independently, retrieve what we learned from previous work, combine the results, pause for my approval, then continue the workflow later.”

### What the verified system can do

1. Run persisted workflows with create/run/pause/resume/cancel lifecycle.
2. Use conditions, parallel steps, pipelines and approval gates.
3. Coordinate multiple agent roles/swarms.
4. Store/search semantic memory in AgentDB with HNSW vector search.
5. Use a RAG-memory plugin and a knowledge-graph plugin.
6. Search memory before work and store successful patterns afterwards.
7. Codex integration explicitly treats Ruflo as coordination/ledger and Codex as the executor.

### MoA value

Of the researched candidates, Ruflo has the **strongest verified integrated technical story for orchestration + semantic memory/RAG**.

### Why it still scored poorly for MoA core

The official product and agent catalog remain heavily software-engineering oriented, and the full install has a very large surface: MCP server, hooks, daemon, many agents/tools, vector-memory components, etc. Its memory is also not automatically the simple GitHub-visible canonical business SSOT. This is a capability-rich but high-complexity option.

### Sources

- https://github.com/ruvnet/ruflo/blob/main/plugins/ruflo-workflows/README.md
- https://github.com/ruvnet/ruflo/blob/main/plugins/ruflo-rag-memory/README.md
- https://github.com/ruvnet/ruflo/blob/main/AGENTS.md

---

## US10 — Hermes Agent

### Story

**You:** “Research an MoA question using web tools, delegate independent subtopics, produce a synthesis file, remember key conclusions, and every Monday run a new research/update check using the relevant skill.”

### What the verified system can do

1. Use web/browser/file/terminal tools.
2. Delegate reasoning-heavy subtasks to isolated child agents; only their summaries return to the parent context.
3. Store bounded persistent memory in `MEMORY.md`/`USER.md`.
4. Optionally connect one of several external memory providers for semantic/cross-session memory.
5. Load Agent-Skills-compatible skills progressively.
6. Run scheduled jobs with attached skills; jobs can run AI tasks or deterministic no-agent scripts.
7. Discover project context from files such as `AGENTS.md`/`CLAUDE.md`.

### MoA value

Hermes can be an **actual executor/runtime** for research, recurring scans, file work and delegation. Its skills + schedules are directly relevant to producing outputs.

### What it does **not** solve

Its built-in memory is agent memory, not a canonical portfolio/project database. Delegated subagent work is not durable across parent interruption. It still benefits from GitHub/Spec Kit/another project-state layer for the MoA operating system.

### Sources

- https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/overview.md
- https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/delegation.md
- https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/cron.md
- https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/memory-providers.md

---

## US11 — OpenClaw

### Story

**You:** “Keep the main chat as orchestrator, send three isolated research tasks to subagents, let them return evidence, use a project skill to synthesize the workshop, and run a recurring weekly portfolio/research job.”

### What the verified system can do

1. Spawn isolated or forked sub-agent sessions for parallel research/long tasks.
2. Track sub-agent runs as background tasks and announce results back to the requester.
3. Use persistent sessions and cross-session tools.
4. Run persisted automations/schedules with run history.
5. Load project/workspace `SKILL.md` skills, including Agent-Skills-style project skills.
6. Apply tool policies/sandbox restrictions to subagents.

### MoA value

OpenClaw can be an **executor/orchestration runtime around the actual AI agents**, especially for parallel work and recurring operations.

### What it does **not** solve

The verified sources reviewed here do not establish OpenClaw as a canonical business portfolio/task graph or semantic document KB. Its session state and scheduled work should therefore not replace the repo/project SSOT.

### Sources

- https://docs.openclaw.ai/tools/subagents
- https://docs.openclaw.ai/automation/cron-jobs
- https://docs.openclaw.ai/tools/skills
- https://docs.openclaw.ai/concepts/session-tool

---

# 3. The big executor/value matrix

**Read each cell as:** what this system contributes at that process step. `N` means directly verified; `A` means MoA adaptation of a generic mechanism; `C` means supporting component only.

| MoA step / process / output | Spec Kit + GitHub | GitHub + Agent Skills | Beads | Gas City | Superpowers | BMAD | OpenSpec | Task Master | Ruflo | Hermes | OpenClaw |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **1. Establish durable MoA principles / governance** | **N/C:** constitution + repo artifacts; workflow gates | **N:** repo SSOT + fields/policies; Skills carry method rules | **C:** issues/memories can reference rules | **C:** config/packs | **C:** skills enforce process | **N/C:** structured method/workflow artifacts | **N/C:** proposals/specs preserve decisions | **C:** PRD/rules | **C:** policy/memory possible | **N/C:** project context files + skills/memory | **N/C:** project skills/context/policies |
| **2. Capture a new idea / research question** | **N:** workflow input/prompt → artifact | **N:** issue/draft/project item | **N:** create bead | **N:** formula/work item | **C:** brainstorming skill | **N:** brainstorming/research web bundle | **N:** `explore`/proposal | **N:** add task/PRD | **N:** workflow/task/memory entry | **N:** normal agent task/todo | **N:** session/task/subagent prompt |
| **3. Turn vague idea into explicit requirements** | **N:** specify/clarify-style artifact flow | **A:** AI uses issue + skill template | **A:** description/acceptance criteria in issue graph | **N for code / A for MoA:** methodology pack | **N:** brainstorming → written design (software) | **N:** product brief/PRD/research bundles | **N:** proposal/specs | **N:** PRD parsing | **N/A:** workflow agents can refine | **A:** executor + skill | **A:** executor + project skill |
| **4. Break work into tasks** | **N:** generated `tasks.md`; can materialize Issues | **N/A:** sub-issues manually or by AI | **N:** dependencies + child work | **N:** formulas/decomposition | **N:** written plan/task chunks | **N:** stories/workflows in core BMad | **N:** `tasks.md` | **N:** `tasks.json` + subtasks | **N:** task orchestration/workflows | **A:** in-session todo/delegation | **A:** background tasks/subagents; not portfolio task graph |
| **5. Model dependencies / blockers** | **N/C:** tasks dependencies + GitHub issue dependencies | **N:** blocking dependencies + hierarchy | **N:** core graph capability | **N:** formula DAG/Beads | **C:** plan order, not portfolio graph | **C:** story/process dependencies | **C:** task order/checklist | **N:** dependency graph + next task | **N:** workflow/state dependencies | **C:** delegation only | **C:** child/task relationships; not business DAG |
| **6. Decide what is ready next** | **A/N:** workflow state + GitHub blocked status; no Beads-style transitive ready command | **A:** filters/dependencies; AI/human prioritizes | **N:** `bd ready` | **N:** runtime/formula readiness | **C:** execute approved plan | **C:** workflow phase logic | **C:** pending checklist | **N:** `next_task()` | **N:** workflow router/task state | **A:** orchestrator decides | **A:** orchestrator decides from sessions/tasks |
| **7. Claim/assign work without collisions** | **C:** GitHub assignees/issue ownership | **N:** assignees/project owner | **N:** atomic claim | **N:** agent work allocation | **C:** fresh subagent per task | **C:** agent roles | **—/C:** no agent-claim core | **C:** status/assignment patterns | **N:** agent/task assignment | **C:** parent delegates child | **N/C:** spawned run owned by parent; not portfolio claim |
| **8. Run multiple specialists in parallel** | **N:** workflow fan-out/fan-in | **A:** several AI sessions/issues, no native AI fan-out | **A/N:** multi-agent examples + ready/claim | **N:** core multi-agent formulas | **N:** subagent-driven development | **N/C:** role workflows; web bundles mainly interactive | **—:** not orchestration focus | **—/C:** task parallelism not orchestration core | **N:** swarms + parallel workflow steps | **N:** batch delegation | **N:** parallel sub-agents/background tasks |
| **9. Perform web/deep research** | **C:** prompt step calls chosen AI; Spec Kit itself does not research | **C:** executor does research | **C:** executor does research | **C:** agents do research if equipped | **C:** executing AI does research | **N:** Market & Industry Research web bundle; Deep Research handoff | **C:** executor does research | **N/C:** AI-powered `research` command, dev-project oriented | **C:** executor/tool does research | **N:** web/browser tools + delegated research | **N/C:** subagents designed for research if tool profile provides web |
| **10. Preserve raw sources / documents** | **N/C:** keep artifacts/sources in Git repo | **N:** repo is natural source store | **C:** link/reference sources; not doc store | **C:** underlying repo/Beads | **—/C:** repo outside framework | **C:** exported artifacts to repo | **N/C:** change artifacts/spec archive | **C:** `.taskmaster/docs`/task files | **C:** AgentDB may store knowledge, but repo still better for canonical source docs | **N/C:** project files + memory | **N/C:** project files/sessions |
| **11. Semantic KB retrieval across MoA corpus** | **—:** no native semantic KB verified | **—:** GitHub project features are not semantic RAG | **C:** semantic compaction/memory; not a document RAG KB | **C:** inherits Beads/other components, not core doc KB | **—** | **—/C:** bundle context, not persistent semantic KB | **—** | **C:** research with project context, not general semantic KB | **N:** RAG memory / AgentDB / knowledge-graph plugins | **N:** optional external memory providers; built-in bounded memory | **—/C:** session search/context files; no semantic MoA KB established in sources checked |
| **12. Retrieve only relevant method/SOP context** | **N/C:** integration commands + workflow/preset files; normal repo context | **N:** Agent Skills progressive disclosure + focused references | **N/C:** `bd prime`, compact state/memories | **N/C:** packs/skills/formula context | **N:** skill activation | **N:** skill/bundle protocol | **C:** schema/artifact context | **C:** task context | **N:** memory search + workflow/skills | **N:** Agent Skills + memory/context references | **N:** workspace/project skills + isolated subagent context |
| **13. Produce a grounded research memo** | **A:** AI prompt creates artifact; workflow governs gates/review | **A:** AI executor writes repo document under issue/skill | **A:** agent writes output; Beads tracks work | **A:** formula specialists can produce artifact, non-code unproven | **A:** process/review pattern can govern document | **N/A:** official research bundle produces research artifact; MoA topic is domain input | **A:** proposal/design artifacts are change-focused, not research memo | **A:** research command + task output | **A:** research agents + memory can create file | **N:** research/delegation/file tools can produce artifact | **N/A:** subagents can research; main agent synthesizes/writes artifact |
| **14. Convert research into workshop skeleton** | **A:** workflow prompt → plan artifact → CEO gate | **A:** workshop skill + issue + AI executor | **A:** dependent task from research output | **A:** replace software build stages with workshop stages; unproven | **A:** brainstorming/design/review pattern | **A:** product/brief workflow can inform offer design; workshop-specific adaptation | **A:** proposal/spec/design/tasks analogy | **A:** workshop brief parsed as PRD | **A:** workflow agents can transform outputs | **A/N:** agent + skill writes workshop file | **A/N:** agent/subagents + skill write workshop file |
| **15. Independent expert/reviewer challenge** | **N:** separate prompt/agent steps + gates/fan-out possible | **A:** separate reviewer issue/AI/PR review | **N:** shipped multiple-persona architect/implementer/reviewer example | **N:** review lanes in official packs | **N:** spec + quality reviewers; document-review loops | **N/C:** specialized agent/workflow reviews in BMad | **C:** user reviews artifacts before apply | **C:** no strong reviewer topology | **N:** reviewer agents/swarm workflows | **N:** fresh isolated delegated reviewers possible | **N:** isolated subagents are natural independent reviewers |
| **16. CEO approval before consequential action** | **N:** explicit workflow `gate` pause/resume | **N/A:** issue/project status + required human action; workflow semantics are configured | **N:** gates documented | **N:** readiness/approval gates in packs | **N:** human checkpoints in execution modes | **N:** interactive planning/workflow approvals | **N/C:** artifacts explicitly reviewed before apply, but not general runtime gate | **C:** user can control status, no strong native gate found | **N:** approval gates in workflow plugin | **A:** main agent can stop/ask; cron/delegation not generic CEO-gate engine | **A:** parent/user/session controls; not a generic workflow gate primitive |
| **17. Execute approved output work** | **N:** command/prompt/shell steps execute through chosen integration | **A:** AI executor acts on issue; Actions/scripts mechanical work | **A:** claimed agent does work | **N:** runtime dispatches agents | **N:** execution skills dispatch tasks | **N:** core BMad continues into implementation (software) | **N:** `apply` executes change tasks | **N:** AI implements selected task | **N:** Codex/Claude/etc. executors do real work under Ruflo coordination | **N:** Hermes uses tools/files/browser/delegates | **N:** OpenClaw agents/subagents/tools execute work |
| **18. Deterministic checks / scripts** | **N:** shell steps + scripts + JSON outcomes | **N:** Actions/scripts/CLI | **N:** CLI/JSON/hooks | **N:** hooks/formulas/services | **N:** verification commands/scripts in skills | **C/N:** workflow checks, especially software/test modules | **N/C:** CLI validates/tracks task artifacts | **N/C:** dependency validation, generated structured data | **N:** hooks/workflows/MCP tools | **N:** `execute_code`; cron can run no-agent scripts | **N:** automations/command payloads + tools |
| **19. Create derivative content from one concept** | **A:** fan-out prompt step over output types | **A:** content skill + sub-issues + several AI tasks | **A:** create linked child tasks | **A:** fan-out formula; non-code unproven | **A:** skills can govern process if authored | **A:** planning/creative suites can support ideation, not dedicated content repurposing proof | **A:** separate changes/tasks | **A:** expand tasks | **A:** parallel agents can generate derivatives | **A/N:** delegate multiple content tasks, write files | **A/N:** spawn isolated subagents per derivative |
| **20. Store final research/workshop/content output** | **N/C:** repository artifacts | **N:** Git/GitHub canonical artifact | **C:** Beads tracks state, output should still live in repo | **C:** repo output | **C:** repo output | **C:** export artifact into repo | **N:** change/spec archive in repo | **N/C:** task files + project files | **C:** memory plus repository; memory alone should not be canonical artifact | **N:** file tools can write repo/local files | **N:** agent tools/project workspace files |
| **21. Know portfolio status next week** | **N/C:** workflow run status + GitHub Project/Issues | **N:** Project views/status/roadmap | **N:** work graph/status | **N:** city/formula/task status | **—/C:** no portfolio state | **C:** workflow artifacts, not portfolio PM | **—/C:** change folders, no whole portfolio view | **N/C:** task lists/tags, project-local | **N:** task/workflow/memory status but more technical | **C:** session/todo/cron; no CEO portfolio board | **C/N:** sessions/background tasks/automation history; no canonical business board |
| **22. Weekly recurring operating review** | **A/N:** workflow can be rerun; scheduling would need external scheduler/CI | **N/A:** Actions/scheduler + Project view + AI summary | **A:** external scheduler runs Beads queries | **N:** services/controller can run ongoing work | **—** | **—/C:** not portfolio scheduler | **—** | **—/C:** no strong scheduler core | **N:** background workers/workflows possible | **N:** cron with skills, fresh sessions, delivery | **N:** persisted automations + run history |
| **23. Resume after interruption/failure** | **N:** persisted state + exact top-level step resume | **N:** durable issue/project state; agent restarts from issue/artifacts | **N:** durable work graph | **N:** durable formula/task state | **C:** plan files durable; active session execution less so | **C:** artifacts durable; workflow runtime varies | **N/C:** pending task checklist/change archive | **N:** task state durable | **N:** persisted workflow lifecycle | **C:** cron durable; delegated child work itself is not durable if parent/process interrupted | **N/C:** automation state durable; subagent task handoffs tracked; session mechanics more complex |
| **24. Cross-agent handoff (ChatGPT ↔ CLI AI)** | **N/C:** repo artifacts common; explicit integrations for many CLIs; ChatGPT reads repo rather than local CLI state | **N:** GitHub/repo is naturally common boundary; Agent Skills open format | **C:** CLI agents can share Beads; web-only access weaker | **C:** runtime-local; repo artifacts are handoff | **N/C:** Agent Skills-style files portable to many coding agents | **N:** official web bundle → repo/IDE handoff | **N/C:** files portable across supported assistants | **N/C:** broad editor/CLI integrations; web handoff weaker | **C/N:** Codex/Claude integration, but memory runtime is local/server-side | **C:** repo files portable; Hermes memory/runtime is Hermes-specific | **C:** repo files/skills portable; OpenClaw session state is runtime-specific |
| **25. Learn from previous successful work** | **C:** reuse workflows/presets + repo decisions; no learned semantic memory | **C:** repo history + reusable skills; AI must retrieve it | **N:** persistent memories + compaction/graph history | **C/N:** Beads plus packs | **C:** encode proven process in skills | **C:** reuse workflows/templates | **C:** archived specs/changes | **C:** task history/research context | **N:** semantic memory + pattern store/recall | **N:** persistent memory/external providers + session search | **C:** session transcript search/skills; no verified semantic knowledge memory in this comparison |
| **26. Keep public/private/sensitive work separated** | **A:** repo paths/workflows plus Git permissions; no domain-native privacy model | **N/A:** GitHub permissions/repos + fields/labels/process conventions | **A:** separate repos/graphs/labels; no MoA visibility model | **A:** runtime/config isolation | **—/C:** process only | **—/C:** artifact process only | **—/C:** repository permissions outside OpenSpec | **—/C:** project files outside system | **N/C:** security/policy features exist, but MoA visibility ontology would be configuration | **N/C:** profiles/toolsets/project context; source/document ACL needs underlying storage | **N/C:** tool policies/sandbox/session isolation; document ACL needs underlying storage |
| **27. Human-facing transparency** | **N:** Markdown artifacts + GitHub Issues; workflow state is JSON/files | **N:** strongest human-readable project UI | **C:** CLI/Dolt graph; optional monitor UI | **C:** technical runtime | **N/C:** human-readable skills/plans | **N:** conversational web bundles + artifacts | **N:** Markdown change packages | **N/C:** tasks files/CLI | **C:** technical dashboards/CLI/memory | **N:** conversational agent, files, scheduled results | **N:** Control UI/session tree + chat, but portfolio view is not GitHub Project-like |
| **28. Main risk for MoA** | Non-software terminology + **no semantic KB** | Too much orchestration remains implicit/manual | Extra Dolt state + coding-agent defaults + web visibility | Too complex + coding-factory assumptions | Great method, **not PM/KB/runtime** | Great planning/research bundles, **not whole-business OS** | Change-control only, coding-centric | PRD/task-centric and dev-oriented | Huge operational surface + software bias + opaque/non-repo memory | Runtime/memory strong, but no canonical portfolio SSOT | Runtime/parallelism strong, but no canonical portfolio/semantic KB |
| **29. Best role in MoA if used** | **Primary workflow controller + GitHub handoff** | **Canonical portfolio state/control baseline** | **Specialist agent task graph if GitHub proves insufficient** | Advanced multi-agent factory only if a pilot justifies complexity | **Borrow review/process skills** | **Web-subscription research/planning skill layer** | **Borrow rigorous change-package pattern** | **Bounded project decomposition tool** | **Candidate integrated runtime + semantic memory if complexity is accepted** | **Execution/research/scheduled-agent runtime** | **Execution/parallel-agent/scheduling runtime** |

---

# 4. One end-to-end Master of Arts scenario

Scenario: **Create a research-backed workshop on “surrender under pressure” and turn it into a workshop, research note and public content.**

| Stage | Human CEO | AI executor | Project/workflow control | Knowledge/KB | Durable output |
|---|---|---|---|---|---|
| 1. Intent | State goal, boundaries, audience, public/private rules | Clarify ambiguity | Spec Kit workflow or GitHub issue records objective | Existing MoA canon is referenced | Project brief |
| 2. Research framing | Approve scope/questions | Draft research plan | Gate prevents premature execution | Retrieve relevant sources/previous work | Research plan |
| 3. Evidence collection | Usually no intervention | Web AI / Hermes / OpenClaw delegates collect sources | Tasks/fan-out record separate lanes | KB/repo stores or links sources | Source/evidence set |
| 4. Synthesis | Review only if consequential | Research agent writes grounded synthesis | Workflow waits for completion/review | Retrieval supplies prior concepts + new evidence | Research memo |
| 5. Independent challenge | Inspect flagged conflicts | Reviewer agent checks evidence, contradictions, missing sources | Reviewer lane / issue / gate | Same source set available to reviewer | Review report |
| 6. CEO decision | Choose framing / reject / request revision | Implement chosen revision | Explicit gate records choice | Decision linked to evidence | Approved research conclusion |
| 7. Workshop skeleton | Decide business constraints | Workshop-design agent creates rough 90-min structure | New dependent task/workflow stage | Research memo + workshop SOP/skill | Workshop skeleton |
| 8. Specialist reviews | See only escalations | Pedagogy, safety, operations, brand reviewers challenge independently | Fan-out/fan-in or separate review tasks | Each reviewer gets only needed context | Review package |
| 9. Workshop finalization | Approve launch/test | Executor consolidates corrections | Gate before “ready” | Canon/source links preserved | Workshop v1 |
| 10. Content derivatives | Approve public/private boundary | Content agents create article, video outline, shorts | Fan-out tasks | Approved research/workshop as source | Content package |
| 11. Publish/store | Approve external release if needed | Agent/files/scripts package outputs | Project state moves to done/published | Canonical artifacts stored in repo | Published assets + archive |
| 12. Learn | Decide which findings become canonical | Agent summarizes learnings | Close project + create follow-up work | KB/memory receives validated learnings, not raw chatter | Updated method/knowledge + next tasks |
| 13. Weekly revisit | Review exceptions/decisions | Scheduled agent checks stale/blocked/changed work | GitHub review or Hermes/OpenClaw/Ruflo schedule | Retrieves recent changes | CEO operating brief |

This scenario exposes the system boundary clearly:

- **GitHub/Beads/Task Master** answer “what work exists and what is next?”
- **Spec Kit/Gas City/Ruflo Workflows** answer “what process step runs next and where do we stop for approval?”
- **BMAD/Superpowers/Agent Skills** answer “how should the AI perform this kind of work?”
- **Hermes/OpenClaw/Ruflo + ChatGPT/Codex/Claude/etc.** answer “which AI actually does the work and uses tools?”
- **Ruflo memory/Hermes memory or a separate KB** answer “what relevant knowledge should the agent retrieve from the past?”
- **Git/GitHub files** answer “where is the canonical human- and machine-readable artifact?”

---

# 5. The most important correction to the MCDA

The previous MCDA over-compressed **project orchestration** and **knowledge infrastructure** into one score.

The evidence now shows that the leading project-control candidates do **not** by themselves provide the semantic knowledge system required by the Master of Arts description:

- Spec Kit: excellent workflow/artifact control; no native semantic MoA corpus retrieval.
- GitHub Projects: excellent visible portfolio state; no native semantic RAG.
- Beads: excellent task graph + compact agent memory; not a full document/research KB.
- Ruflo: strongest integrated semantic memory/RAG of the researched set, but high operational complexity and software-engineering bias.
- Hermes: useful persistent/external memory and executor features, but not a canonical project/portfolio SSOT.
- OpenClaw: strong runtime/session/subagent/scheduling capabilities; no verified semantic MoA KB established in the sources checked.

Therefore a final architecture decision should explicitly evaluate **four independent responsibilities**:

| Responsibility | Question |
|---|---|
| Portfolio SSOT | Where do projects, tasks, priorities, dependencies and CEO decisions live? |
| Workflow engine | What reliably advances work through research → review → approval → output? |
| Knowledge system | Where do source documents, concepts, validated learnings and retrieval live? |
| AI executors + skills | Which subscribed/local AIs actually do the work, and which proven skills tell them how? |

A candidate should not be credited for a responsibility it does not own.

---

# 6. Verified source index

## Spec Kit
- https://github.com/github/spec-kit/blob/main/docs/reference/workflows.md
- https://github.com/github/spec-kit/blob/main/docs/reference/integrations.md
- https://github.com/github/spec-kit/blob/main/templates/commands/taskstoissues.md
- https://github.com/github/spec-kit/blob/main/docs/community/presets.md

## GitHub + Agent Skills
- https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects
- https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-issue-dependencies
- https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/browsing-sub-issues
- https://agentskills.io/specification

## Beads
- https://github.com/gastownhall/beads
- https://github.com/gastownhall/beads/blob/main/examples/README.md

## Gas City
- https://github.com/gastownhall/gascity
- https://github.com/gastownhall/gascity-packs

## Superpowers
- https://github.com/obra/superpowers
- https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/SKILL.md
- https://github.com/obra/superpowers/blob/main/docs/superpowers/specs/2026-01-22-document-review-system-design.md

## BMAD
- https://docs.bmad-method.org/explanation/web-bundles/
- https://github.com/bmad-code-org/BMAD-METHOD

## OpenSpec
- https://github.com/Fission-AI/OpenSpec/blob/main/docs/examples.md
- https://github.com/Fission-AI/OpenSpec/blob/main/schemas/spec-driven/schema.yaml

## Task Master
- https://github.com/eyaltoledano/claude-task-master
- https://github.com/eyaltoledano/claude-task-master/blob/main/apps/docs/capabilities/index.mdx

## Ruflo
- https://github.com/ruvnet/ruflo/blob/main/plugins/ruflo-workflows/README.md
- https://github.com/ruvnet/ruflo/blob/main/plugins/ruflo-rag-memory/README.md
- https://github.com/ruvnet/ruflo/blob/main/AGENTS.md

## Hermes
- https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/overview.md
- https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/delegation.md
- https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/cron.md
- https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/memory-providers.md

## OpenClaw
- https://docs.openclaw.ai/tools/subagents
- https://docs.openclaw.ai/automation/cron-jobs
- https://docs.openclaw.ai/tools/skills
- https://docs.openclaw.ai/concepts/session-tool
