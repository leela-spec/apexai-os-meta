# 09 — Primary Orchestration Selection Handover

Status: **NEXT DECISION PASS — selection, not architecture design**  
Date: **2026-08-22**  
Primary question: **Which existing orchestration ecosystem should Master of Arts actually install and use?**

## 0. Operator correction / reason for this handover

The previous work repeatedly drifted from **select an existing system** into **design a custom system around tools**. That is now explicitly forbidden.

The next AI is not being asked to invent the Master of Arts knowledge architecture, project hierarchy, memory synchronization protocol, agent taxonomy, custom workflow runtime, or custom RAG stack.

The next AI must instead determine which existing orchestration ecosystem already provides the closest complete operating model and how Master of Arts would use that system **natively** with the files/projects that already exist.

The decision must end with:

1. **one recommended primary orchestration ecosystem**;
2. **one direct challenger**;
3. a bounded explanation of why the winner is better for the actual Master of Arts workflows;
4. a native installation/use blueprint for both;
5. a short list of unavoidable project-specific configuration only;
6. no implementation until the operator approves the selection.

Current evidence makes **Hermes Agent** the leading candidate and **OpenClaw** the strongest direct challenger. This is a starting prior, not a locked verdict.

---

## 1. Non-negotiable decision law

### REUSE_FIRST

Order of preference:

1. existing orchestration ecosystem with native feature;
2. officially supported plugin/module/skill pack;
3. established portable Agent Skills package used through documented support;
4. small configuration/adaptation using the selected ecosystem's own extension mechanism;
5. custom code/system only if absolutely unavoidable and limited to a small adapter.

### CUSTOM_LIMIT

Target: **90–95% upstream/existing system; maximum 5–10% Master of Arts-specific connection/configuration.**

If a proposed architecture requires us to create the core hierarchy, memory model, task runtime, agent protocol, retrieval engine, synchronization system, or workflow language ourselves, reject it.

### NO_PARALLEL_SYSTEMS

Do not casually combine:

- Hermes Kanban + GitHub Projects + OpenClaw Workboard;
- Hermes memory + OpenClaw memory + custom shared memory synchronization;
- several different workflow engines for the same task state;
- several separate canonical knowledge databases.

One responsibility should have one primary owner wherever possible.

### INSTALL_BEFORE_INVENT

The question is not:

> "What theoretically perfect architecture could an AI design?"

The question is:

> "What existing system can we install, point at the Master of Arts estate, configure through documented mechanisms, and start using?"

---

## 2. Authoritative Master of Arts truths

Read these first:

1. `Orchestration/03-SCOPE-LOCK.md`
2. `Orchestration/07-INTEGRATED-AGENT-OPERATING-MODEL.md`
3. `Orchestration/08-CROSS-AI-INTEGRATED-AGENT-RESEARCH-PROMPT.md`
4. all independent reports under `Orchestration/research-runs/`
5. `Master Of Arts Meta` / current project-source material if accessible

Do **not** treat old OpenClaw/Apex custom orchestration designs as trusted architecture. They are historical evidence and failure context only unless a current upstream system independently validates the same mechanism.

### BUSINESS_SCOPE

Master of Arts is not one software project. It includes:

- workshops and workshop families;
- coaching/method development;
- research and synthesis;
- content, website and social media;
- products/offers/pricing/market tests;
- business administration and legal/financial operations;
- live project execution;
- future translation into Leela use cases.

### EXISTING_PROJECT_ESTATE

The repository already contains diverse project/domain folders and substantial loose source material. The selected system must work with this reality.

Do not begin by reorganizing the repo into a new AI-designed taxonomy.

The system must explain how existing project files become usable context/knowledge with minimal migration.

### MACRO_MESO_MICRO_REQUIREMENT

The operator needs project management and knowledge context at three scales:

- **Macro:** Master of Arts as the whole organization/portfolio.
- **Meso:** a project/program/family, e.g. an Awakenings workshop family or another major project domain.
- **Micro:** one concrete execution project, e.g. create, publish and advertise one specific workshop.

The selected orchestration must demonstrate how it natively represents or handles those levels.

Do not invent a hierarchy if the candidate already has boards/projects/workspaces/parents/subtasks/dependencies/nested context or equivalent native concepts.

### SHARED_SPECIALISTS_REQUIREMENT

Do **not** assume one bespoke agent per project.

Preferred model:

- reusable specialist role, e.g. Marketing Executive;
- reusable skill/method package;
- shared organization-level knowledge where relevant;
- project-specific knowledge/context loaded for the current project;
- micro-project execution context loaded only for the current job.

The same marketing/research/workshop/operations specialist should ideally work across several projects without copying its role definition.

The next AI must verify whether each candidate actually supports this pattern natively or through documented Agent Skills/project-context mechanisms.

---

## 3. The central unresolved design question

Do **not** answer this from abstract reasoning. Answer it from official candidate behavior.

### QUESTION

How does the selected orchestration let one reusable specialist agent operate across many isolated projects while receiving:

1. organization-wide context;
2. project/program-specific knowledge;
3. concrete micro-project context;
4. the same reusable skill library;
5. durable task/workflow state;
6. accumulated learning that can be reused without creating runtime-memory drift?

### REQUIRED_WALKTHROUGH

Use one concrete example:

> `Marketing Executive` creates launch content for a specific Awakenings workshop.

Show exactly:

- where the Marketing Executive definition lives;
- where the marketing skills live;
- where general Master of Arts brand/business knowledge lives;
- where Awakenings-specific knowledge lives;
- where the specific workshop brief/assets live;
- what the runtime automatically loads;
- what it retrieves only on demand;
- where work state is stored;
- how review works;
- what happens after the task is complete;
- what learning, if any, becomes reusable for the next project;
- which parts are native vs configured vs custom.

Repeat the same walkthrough for both finalists.

If the candidate cannot demonstrate this without a custom subsystem, score it down heavily.

---

## 4. Candidate A — Hermes Agent: facts that must be verified and completed

Use **current official Hermes documentation/repository only** for load-bearing claims.

Official evidence already established as of 2026-08-22:

### HERMES_KANBAN

Official docs describe a durable multi-agent board shared across Hermes profiles, stored in `~/.hermes/kanban.db`, with:

- named profiles/workers;
- durable tasks;
- dependencies;
- request-review / request-changes;
- blocking/unblocking;
- comments and attachments;
- retries/attempt history;
- handoff metadata;
- automatic dispatch/decomposition options.

Source: `https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban`

Research task: determine whether native board/project/workspace semantics are sufficient for Master of Arts macro/meso/micro management or whether another canonical PM system would be required.

### HERMES_SKILLS

Official docs state that Hermes supports the open Agent Skills format and can scan external shared skill directories.

Source: `https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/`

Important current behavior: external skill directories are **not automatically write-protected**. If writable, Hermes skill-management operations can modify them.

Research task:

- identify the safest official configuration for a pinned/reviewed organization skill library;
- determine which upstream skill packs can be installed unchanged;
- distinguish company-approved skills from Hermes agent-created skills.

### HERMES_LEARNING

Official Curator docs show Hermes has a learning/maintenance loop for agent-created skills with:

- usage telemetry;
- active/stale/archive lifecycle;
- audit ledger;
- backups;
- rollback;
- no automatic purge by default.

Source: `https://hermes-agent.nousresearch.com/docs/user-guide/features/curator`

Research task: explain exactly how Hermes learning can improve reusable capabilities without allowing one runtime to silently corrupt shared Master of Arts skills or project truth.

Do not design a new synchronization mechanism. Use only Hermes-supported boundaries/configuration and ordinary repo review where needed.

### HERMES_KNOWLEDGE

This remains the biggest load-bearing question.

Determine from official docs exactly how Hermes handles:

- root/project context files;
- nested project context;
- long-term memory;
- local project files;
- on-demand retrieval/search;
- project workspace assignment from Kanban;
- per-profile vs shared knowledge;
- isolation between unrelated projects;
- what survives sessions;
- what is automatically injected vs retrieved.

Do not assume QMD, RAG, MCP, OKF, or a custom knowledge folder is required. First map Hermes' **native** mechanism completely.

If an external knowledge component is genuinely required, prove the gap before recommending one.

---

## 5. Candidate B — OpenClaw: facts that must be verified and completed

Use **current official OpenClaw documentation/repository only** for load-bearing claims.

### OPENCLAW_WORKBOARD

Official docs describe Workboard as a bundled optional Kanban-style board with durable SQLite state, agents, linked runs/sessions, dependencies, attempts, comments, proof/artifact refs, review/blocked states and dispatch.

Official docs also explicitly state:

> Workboard is intentionally small and is not a replacement for GitHub Issues, Linear, Jira or other team project-management systems.

Source: `https://docs.openclaw.ai/plugins/workboard`

Research task: determine whether that limitation makes OpenClaw unsuitable as the **single** Master of Arts control plane or whether its intended workspace/project model handles our needs elsewhere.

### OPENCLAW_MEMORY

Official docs state that OpenClaw writes durable memory as plain Markdown in each agent workspace and also provides a built-in retrieval index.

Sources:

- `https://docs.openclaw.ai/concepts/memory`
- `https://docs.openclaw.ai/concepts/memory-builtin`

Current builtin memory includes keyword and vector/hybrid retrieval, deterministic ranking and per-agent SQLite indexing.

Research task:

- determine whether this creates too much per-agent/project duplication for Master of Arts;
- determine how one reusable specialist works across several project contexts;
- determine what is canonical vs per-agent memory;
- determine whether the memory advantage materially outweighs Workboard/control-plane limitations.

### OPENCLAW_SKILLS

Official docs support installing skills from ClawHub, Git repositories, local directories and external skills references.

Source: `https://docs.openclaw.ai/skills`

Do not assume ClawHub packages are trusted merely because they are listed. Prefer pinned Git/local skills with inspectable source for production comparison.

Research task: verify whether the same approved skill library can be reused by OpenClaw and other Agent-Skills-compatible runtimes without rewriting it.

---

## 6. Tool glossary — mandatory explanation standard

The next AI may mention supporting tools only after it can complete this fact card.

For **every named tool/service/component**, report:

```text
NAME:
WHAT_IT_IS:
WHO_MAKES_IT:
ROLE_IN_OUR_SYSTEM:
MANDATORY_OR_OPTIONAL:
INSTALLATION:
RUNS_LOCAL_OR_REMOTE:
DATA_SENT_EXTERNALLY:
API_REQUIRED:
PAID_OR_FREE:
LICENSE_IF_RELEVANT:
INPUTS:
OUTPUTS:
SECURITY_BOUNDARY:
WHY_WE_NEED_IT:
WHAT_BREAKS_IF_REMOVED:
OFFICIAL_SOURCE:
```

No tool may be recommended based on a name plus one-line description.

### QMD — current verified orientation only

- **What:** open-source on-device search engine for Markdown notes/docs/knowledge bases.
- **Maker/repo:** `tobi/qmd`.
- **Install:** Node/Bun package, e.g. `npm install -g @tobilu/qmd`.
- **Core execution:** local; BM25, vectors and reranking run locally through local models.
- **API:** no external API is required for core local use.
- **MCP:** optional interface; QMD can work directly from CLI without MCP.
- **Cost/license:** software is MIT licensed; no software fee in the repository license.
- **Input:** directories/collections of Markdown/text-like files.
- **Output:** ranked search results, files/passages/JSON; local search index.
- **Current role:** **not selected**. It is an optional search component only if the winning orchestration proves it lacks sufficient native retrieval.
- Official sources: `https://github.com/tobi/qmd`, `https://github.com/tobi/qmd/blob/main/README.md`.

### Docling — current verified orientation only

- **What:** open-source document conversion/parsing toolkit.
- **Origin/license:** IBM copyright; MIT license in the current official repository.
- **Install:** Python package, e.g. `pip install docling`.
- **Runs:** macOS/Linux/Windows; core processing can run locally.
- **API:** no external hosted API is required for normal local installation/use.
- **Cost:** no software fee for the MIT-licensed core.
- **Input:** documents such as PDF/DOCX/PPTX and other supported formats.
- **Output:** structured representations such as Markdown/JSON depending on workflow.
- **Current role:** **not selected**. Use only if the winner demonstrably needs conversion of existing binary project documents for native ingestion/search.
- Official sources: `https://docling-project.github.io/docling/`, `https://github.com/docling-project/docling`.

### MCP — current verified orientation only

- **What:** Model Context Protocol, an open communication protocol between an AI client and a tool/server. It is not a database and not a hosted company service by itself.
- **Standard transports:** local `stdio` and networked Streamable HTTP.
- **Local mode:** the AI client can launch an MCP server as a local subprocess; no network transfer is inherent in that mode.
- **Remote mode:** HTTP means network communication and requires proper authentication/origin/security controls.
- **Cost:** the protocol itself has no fee; the software/service behind an MCP server may have costs.
- **Current role:** **not selected**. Use only when the winning orchestration or selected tool requires MCP for an integration.
- Official source: `https://modelcontextprotocol.io/specification/`

Do not promote QMD, Docling or MCP into architectural requirements merely because they are technically useful.

---

## 7. Knowledge-base decision requirements

The operator is not asking for a new abstract KB ontology.

The repository already contains knowledge/source material. The next decision is:

> **How does the chosen existing orchestration natively turn the existing project estate into usable, isolated and reusable context for specialist agents?**

For each finalist answer:

### KB_1_PROJECT_SCOPE

Can a project/program have its own bounded context/knowledge without creating an entirely separate agent organization?

### KB_2_SHARED_AGENT

Can the same specialist profile/agent work in multiple projects and automatically or explicitly receive different project context?

### KB_3_HIERARCHY

How are organization → program/project → concrete execution contexts represented natively?

### KB_4_RETRIEVAL

What happens when the project contains too many files to load into context?

Use candidate-native retrieval first. Only then identify an upstream external component if required.

### KB_5_RAW_FILES

How does the system handle the files already present in Master of Arts?

Distinguish:

- Markdown/text;
- PDF/DOCX/PPTX;
- images/media;
- links/web sources;
- generated artifacts.

Do not invent ingestion pipelines. State native support, official plugin/integration, or verified gap.

### KB_6_CANONICAL_TRUTH

Where is authoritative project knowledge stored?

Do not accept a solution where canonical truth is scattered across hidden chat memory plus several runtime databases with no human-readable source.

### KB_7_LEARNING

How can successful work improve future work?

Distinguish:

- project knowledge learned from one project;
- organization-wide knowledge;
- reusable procedural skill;
- temporary runtime/session memory.

The candidate must already have a documented learning/memory/skill lifecycle or the recommendation must clearly state the gap.

No custom cross-runtime memory synchronization system may be proposed.

---

## 8. Shared agent/skill model requirements

The operator prefers **shared specialist capabilities**, not one bespoke agent per project.

Test these real specialist examples:

- Marketing Executive;
- Research Strategist;
- Source/Evidence Reviewer;
- Workshop Designer;
- Content Writer/Repurposer;
- Operations/Admin specialist;
- Project/Portfolio Controller.

For each finalist identify:

1. whether a prebuilt role/skill exists;
2. who maintains it;
3. license/commercial usability;
4. how it is installed;
5. whether the same files can be consumed by Hermes, Claude/Codex or OpenClaw;
6. whether the orchestration routes work to the specialist automatically or requires manual selection;
7. whether the specialist can switch projects without duplicating its definition;
8. what project knowledge it receives;
9. whether its learning is private, shared, reviewed, or automatically mutating.

Do not write missing roles as part of this research.

Use `MISSING` when no verified upstream option exists.

---

## 9. Cost / privacy / execution constraints

### SUBSCRIPTION_FIRST

Prefer already-paid subscription or local-model execution.

Do not make OpenRouter or another pay-per-token aggregation layer a core requirement.

External API execution may be listed for completeness but should only become part of the recommendation if it creates a material capability unavailable through subscription/local paths.

### DATA_EGRESS

For each semantic execution path show:

- which provider receives the prompt/project data;
- whether files leave the local machine/repository;
- whether embeddings/search are local or remote;
- whether the feature can operate locally;
- what credentials are required.

### COMMERCIAL_LICENSE

Any third-party skill pack intended for production must have commercially compatible licensing or explicit permission.

Do not silently use non-commercial packages.

---

## 10. Required head-to-head user stories

Run the same user stories as architecture walkthroughs using **native documented behavior only**.

### US1 — CROSS_PROJECT_MARKETING_EXECUTIVE

Scenario:

- reusable Marketing Executive exists once;
- it first works on Awakenings;
- later it works on another Master of Arts project;
- same specialist/method, different project knowledge;
- operator should not copy/paste context or clone the agent.

Show exact state/context/skill flow.

### US2 — WORKSHOP_FAMILY_TO_ONE_WORKSHOP

Scenario:

- macro portfolio contains Master of Arts;
- meso project is an Awakenings family/program;
- micro project is one specific workshop launch;
- workshop knowledge and previous learnings should be available at the correct level;
- the concrete workshop keeps its own brief/assets/tasks/results.

Show native project/task/workspace hierarchy and knowledge scoping.

### US3 — RESEARCH_TO_WORKSHOP_TO_CONTENT

Flow:

`research question → existing project knowledge → research → source review → synthesis → workshop design → review → CEO decision → content derivation → durable outputs → reusable learning`

Measure how much of this exists upstream.

### US4 — WEEKLY_CEO_CONTROL

Flow:

`read portfolio → identify blockers/dependencies/stale work → continue routine work → surface only consequential decisions → persist decision → resume execution`

The CEO should not need to reconstruct state from agent chatter.

### US5 — LEARNING_WITHOUT_DRIFT

After a successful workshop/content/research workflow:

- a project-specific learning is retained for that project;
- a genuinely reusable method can become a shared skill;
- one runtime's private memory does not silently become company-wide truth;
- another executor can reuse the approved shared capability.

Use only candidate-native mechanisms plus ordinary repository review/configuration.

### US6 — INTERRUPT_AND_RESUME

Stop the runtime mid-work and restart it.

Show what persists natively and what must be reconstructed manually.

---

## 11. MCDA for the final decision

Do not produce another huge landscape ranking unless a clearly superior out-of-box candidate appears.

Score **Hermes** and **OpenClaw** deeply. Keep **one out-of-box wildcard slot** only for a system that current official evidence shows already solves more of the complete operating loop with less customization.

Recommended dimensions:

| Dimension | Weight |
|---|---:|
| Existing end-to-end operating loop | 18 |
| Project-local + hierarchical knowledge/context | 16 |
| Shared reusable agents/skills across projects | 15 |
| Durable orchestration / handoff / resume / review | 14 |
| Learning without runtime-memory fragmentation | 10 |
| Subscription/local executor fit and privacy | 10 |
| Non-software Master of Arts workflow fit | 8 |
| Operator visibility / CEO control | 5 |
| Installation/operations simplicity | 4 |

Hard-gate before scoring:

- existing and maintained;
- no custom orchestration core;
- no mandatory external API aggregator;
- durable state survives sessions;
- supports shared reusable specialist capabilities;
- project context can be isolated/scoped;
- commercially usable production path;
- auditable permissions/actions;
- real non-software fit.

Perform sensitivity checks for:

1. knowledge-first;
2. autonomy-first;
3. simplicity/privacy-first.

Do not treat a 1–2 point desk-score difference as decisive when an unresolved implementation fact can reverse it.

---

## 12. Required output of the next AI

Produce **one decision-ready report**, not another architecture corpus.

### SECTION_A — EXECUTIVE_DECISION

Maximum one page:

- recommended primary orchestration;
- runner-up;
- confidence;
- top three reasons;
- top three risks;
- exact unresolved points before installation.

### SECTION_B — PLAIN_LANGUAGE_SYSTEM_MAPS

For each finalist show:

```text
Master of Arts
  → projects
    → knowledge
    → tasks
    → shared agents
    → shared skills
    → executor/model
    → review
    → learning
```

Explain every component in non-technical language.

### SECTION_C — ACTUAL_MASTER_OF_ARTS_WALKTHROUGHS

Use US1–US6.

Do not substitute generic software examples.

### SECTION_D — NATIVE_VS_ADDED

For every component mark:

- `NATIVE`
- `OFFICIAL_PLUGIN`
- `ESTABLISHED_PORTABLE_SKILL`
- `SMALL_CONFIGURATION`
- `CUSTOM`
- `MISSING`

The selected system should have almost no `CUSTOM` in load-bearing layers.

### SECTION_E — TOOL_FACT_CARDS

Use the mandatory glossary schema from §6 for every external tool mentioned.

### SECTION_F — MCDA_AND_SWITCHING_CONDITIONS

Show scores plus:

> Hermes loses if ...

> OpenClaw loses if ...

### SECTION_G — NATIVE_INSTALLATION_BLUEPRINT

Use only verified official installation/configuration commands.

Show:

1. install core system;
2. authenticate executor/subscription/local model;
3. point system at MasterOfArts repo;
4. install/enable approved existing skills;
5. create/import native project/board/workspace state;
6. show how an existing project folder becomes usable;
7. show how the same specialist changes project context;
8. show recovery/review/learning.

Do **not** execute installation during this research pass.

### SECTION_H — FINAL_OPERATOR_DECISION

End with exactly:

```text
RECOMMENDED_PRIMARY:
RUNNER_UP:
WHY_PRIMARY_WINS:
CUSTOM_PERCENT_ESTIMATE:
MANDATORY_EXTERNAL_SERVICES:
INCREMENTAL_MONTHLY_COST:
PRIVATE_DATA_EGRESS:
FIRST_NATIVE_WORKFLOW_TO_RUN:
DO_NOT_BUILD:
REMAINING_OPERATOR_DECISION:
```

---

## 13. Explicit anti-drift rules

- Do not design a custom Master of Arts knowledge-base engine.
- Do not revive the previous OpenClaw/Apex custom agent-KB architecture.
- Do not assume `AGENTS.md` hierarchy alone is the orchestration system.
- Do not choose QMD, Docling, MCP, OKF, GitHub Projects or another component before proving the chosen orchestration needs it.
- Do not create a new agent for each project unless the selected upstream system itself requires/benefits from that model and proves the value.
- Do not synchronize Hermes/OpenClaw/Claude/Codex private memories.
- Do not treat runtime memory as company truth.
- Do not create dozens of custom role prompts.
- Do not introduce a second project-management SSOT without a proven native gap.
- Do not use OpenRouter or another external aggregation API by default.
- Do not recommend non-commercial skill packages for commercial production.
- Do not score marketing claims as capabilities.
- Do not use stars as evidence that a workflow works.
- Do not create a small custom pilot architecture that cannot scale to the complete target.
- Do use real Master of Arts projects and user stories to test the **existing system as shipped**.
- Do prefer one installed coherent ecosystem over a theoretically elegant composition.

---

## 14. Completion gate

The research is incomplete unless all answers are YES:

- Did I recommend one primary orchestration ecosystem and one direct challenger?
- Did I use only current official sources for load-bearing runtime behavior?
- Did I explain exactly how existing Master of Arts project files become usable context/knowledge?
- Did I show organization → project/program → concrete execution context using candidate-native mechanisms?
- Did I show one reusable specialist working across multiple projects without cloning the agent?
- Did I verify how shared skills are installed and whether they are portable?
- Did I verify how the candidate learns and how that learning is prevented from silently corrupting company truth?
- Did I separate runtime memory from durable organizational knowledge?
- Did I explain every external tool in plain operational language including install/cost/local-vs-remote/data egress?
- Did I avoid introducing QMD, Docling, MCP or another component unless a proven gap required it?
- Did I verify subscription/local execution and identify every external data path?
- Did I keep custom work within the 5–10% ceiling?
- Did I use actual Master of Arts non-software user stories?
- Did I provide native verified install/use blueprints without executing them?
- Did I stop before implementation so the operator can choose?

If any answer is NO, fix the research before presenting a decision.
