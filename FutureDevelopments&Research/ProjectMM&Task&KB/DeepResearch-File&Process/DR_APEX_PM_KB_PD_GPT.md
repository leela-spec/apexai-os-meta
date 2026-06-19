# APEX Execution Options Research

## Scope and method

This report does **not** propose an architecture and does **not** decide what to build. It compares execution patterns already present in public implementations that are closest to the Apex processes you listed, with emphasis on **Claude Code / file-first / no-SaaS / solo operator** fit. The strongest recurring pattern across the usable sources is: **use markdown files and SKILL.md conventions for capture, decomposition, state mutation, handoff, and synthesis; use scripts only for deterministic scans, registry generation, and low-token status/reporting; reserve workflow engines for escalation only.** That conclusion is supported most directly by CCPM’s “script-first rule” for deterministic operations, its task frontmatter/dependency conventions, llm-wiki’s index-first and surgical-edit rules, CrewAI’s task design and stateful Flow patterns, and OpenClaw’s explicit separation between durable flow state and business logic. 

The highest-confidence sources actually read at implementation-file level were: **S1 CCPM**, **S2 Backlog.md**, **S6 OpenClaw**, **S7 crewAI skills**, **S8 llm-wiki-plugin**, **S13 hermes-agent**, and **S14 LangGraph**. S9 was only partially retrievable at file level during this research window; S3, S4, S5, S10, S11, and S12 were not confidently retrievable as implementation-file sources from the queries/paths attempted, so they are treated as **not confirmed** rather than inferred. 

## Source coverage and closest reusable patterns

| Source                   | Status                      | Files read                                                                                                                                             | What it contributes                                                                                                                       |
| ------------------------ | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| S1 CCPM                  | Confirmed                   | `skill/ccpm/SKILL.md`, `skill/ccpm/references/structure.md`, `skill/ccpm/references/track.md`                                                          | File-first PM flow; task frontmatter; dependency metadata; script-first status/next/blockers/validation.                                  |
| S2 Backlog.md            | Confirmed                   | example task file `backlog/tasks/back-200 - Add-Claude-Code-integration-with-workflow-commands-during-init.md`; source tree under `src/` and `src/ui/` | Frontmatter-backed task records; task dependency field; CLI/UI around markdown backlog.                                                   |
| S3 task-master           | Not confirmed               | public implementation files not confidently identified                                                                                                 | Treated as unavailable in this report.                                                                                                    |
| S4 GSD Core              | Not confirmed               | public implementation files not confidently identified                                                                                                 | Treated as unavailable in this report.                                                                                                    |
| S5 planning-with-files   | Not confirmed               | public implementation files not confidently identified                                                                                                 | Treated as unavailable in this report.                                                                                                    |
| S6 OpenClaw              | Confirmed                   | `skills/taskflow/SKILL.md`, `skills/model-usage/scripts/model_usage.py`, `skills/taskflow/examples/inbox-triage.lobster`                               | Durable taskflow state, explicit waits/blocked states, example multi-step job DSL, Python script pattern for deterministic summarization. |
| S7 crewAI skills         | Confirmed                   | `skills/design-task/SKILL.md`, `skills/getting-started/SKILL.md`                                                                                       | Strong task design discipline; explicit context dependencies; structured outputs; optional Flow with persistence and human feedback.      |
| S8 llm-wiki-plugin       | Confirmed                   | `skills/llm-wiki/SKILL.md`, `skills/llm-wiki/scripts/wiki_search.py`, `skills/llm-wiki/scripts/init_wiki.py`                                           | KB pattern: `SCHEMA.md`, `index.md`, `log.md`, surgical updates, BM25 fallback, template/bootstrap scripts, optional graph layer.         |
| S9 kanban-skill          | Partially confirmed         | repository structure + example card format only                                                                                                        | Markdown cards with YAML frontmatter, `blocked_by`, and board/blocked helper scripts.                                                     |
| S10 pm-skills            | Not confirmed               | public implementation files not confidently identified                                                                                                 | Treated as unavailable in this report.                                                                                                    |
| S11 swarmvault           | Not confirmed               | public implementation files not confidently identified                                                                                                 | Treated as unavailable in this report.                                                                                                    |
| S12 Imprint              | Not confirmed               | public implementation files not confidently identified                                                                                                 | Treated as unavailable in this report.                                                                                                    |
| S13 hermes-agent         | Confirmed                   | `tools/skills_hub.py`                                                                                                                                  | Skill registry, trust levels, repo taps, caching, grouping sidecar, fetch/inspect pattern.                                                |
| S14 LangGraph            | Confirmed                   | repo root, `examples/plan-and-execute/plan-and-execute.ipynb` path, examples tree                                                                      | Escalation-only stateful workflow framework with durable execution and human-in-the-loop; materially higher complexity cost.              |
| S15 private PRC patterns | Closest public matches only | matched to public sources below                                                                                                                        | See grouping section.                                                                                                                     |

## Project management execution options

### Capture project

**ID: PM1**

**What this process does:** Creates the initial project record: name, goal, domain, current state, and success criteria.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Requires Python?|Portable?|
|---|---|---|---|---|---|---|---|
|A|S2 Backlog.md|Create one markdown task/project file with YAML/frontmatter fields|Low|Low|Low|No|Yes|
|B|S1 CCPM|SKILL-guided PRD/epic capture in files before execution|Med|Low|Low|No|Yes|
|C|S7 crewAI|Structured task description + expected_output model|Med|Med|Med|Yes|No|

**Best option for solo operator, no SaaS, Claude Code environment:** **Option A.** The lightest-fit pattern is a single markdown record with explicit fields, because it is cheap, portable, and does not introduce framework coupling. 

**Evidence:** Backlog example task file exposes a simple fielded record with `id`, `title`, `status`, `created_date`, `updated_date`, `dependencies`, and `priority`, showing the practical viability of file-first structured capture; exact file URL: `https://github.com/MrLesk/Backlog.md/blob/main/backlog/tasks/back-200%20-%20Add-Claude-Code-integration-with-workflow-commands-during-init.md`. CCPM’s skill description explicitly starts from “PRD → Epic”; exact file URL: `https://github.com/automazeio/ccpm/blob/main/skill/ccpm/SKILL.md`. 

### Decompose project

**ID: PM2**

**What this process does:** Breaks a project into epics, chunks, and tasks with explicit splitting rules.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Requires Python?|Portable?|
|---|---|---|---|---|---|---|---|
|A|S1 CCPM|Skill-guided epic decomposition into numbered task files with metadata|Med|Low|Low|No|Yes|
|B|S7 crewAI|“One task = one objective” task design discipline|Med|Med|Med|Yes|No|
|C|S14 LangGraph|Stateful planner/executor workflow|High|High|High|Yes|No|

**Best option for solo operator, no SaaS, Claude Code environment:** **Option A.** CCPM already encodes decomposition rules, parallelization thresholds, and task-file format without requiring a runtime beyond files and Claude. 

**Evidence:** CCPM `structure.md` says this phase “converts a technical epic into concrete, numbered task files with dependency and parallelization metadata,” and specifies a frontmatter-backed task format with `depends_on`, `parallel`, and `conflicts_with`; exact file URL: `https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md`. crewAI’s design guide says “One task = one objective”; exact file URL: `https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md`. 

### Assign dependencies

**ID: PM3**

**What this process does:** Maintains the dependency graph between tasks: what depends on what, and what gets unlocked.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Requires Python?|Portable?|
|---|---|---|---|---|---|---|---|
|A|S1 CCPM|Store `depends_on` and `conflicts_with` in task frontmatter|Low|Low|Low|No|Yes|
|B|S2 Backlog.md|Simple `dependencies` field in markdown task file|Low|Low|Low|No|Yes|
|C|S7 crewAI|Use task `context=[...]` for explicit non-linear dependency flow|Med|Med|Med|Yes|No|

**Best option for solo operator, no SaaS, Claude Code environment:** **Option A.** CCPM’s dependency metadata is the cleanest public implementation because it covers both prerequisite order and file-conflict parallelism. 

**Evidence:** CCPM specifies `depends_on`, `parallel`, and `conflicts_with`, and says circular dependencies are an error; exact file URL: `https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md`. Backlog’s example task includes a `dependencies` list; exact file URL: `https://github.com/MrLesk/Backlog.md/blob/main/backlog/tasks/back-200%20-%20Add-Claude-Code-integration-with-workflow-commands-during-init.md`. 

### Compute next action

**ID: PM4**

**What this process does:** Determines the next executable task from current state plus dependency state.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Requires Python?|Portable?|
|---|---|---|---|---|---|---|---|
|A|S1 CCPM|Run deterministic `next.sh` against project files|Low|Med|Med|No|Yes|
|B|S9 kanban-skill|Infer next movable card from `blocked_by` and status fields|Low|Low|Low|No|Yes|
|C|S7 crewAI|Ask an LLM/agent to reason over loaded state|Med|Med|Med|Yes|No|

**Best option for solo operator, no SaaS, Claude Code environment:** **Option A.** This is one of the clearest cases where a deterministic script is preferable for repeatability and token minimization, even though a pure SKILL approach is still possible. 

**Evidence:** CCPM `track.md` maps “what should I work on next” to `bash references/scripts/next.sh` and says it “Shows highest-priority open tasks with no blocking dependencies”; exact file URL: `https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/track.md`. 

### Detect blockers

**ID: PM5**

**What this process does:** Identifies tasks that cannot proceed and why.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Requires Python?|Portable?|
|---|---|---|---|---|---|---|---|
|A|S1 CCPM|Deterministic `blocked.sh` report|Low|Med|Med|No|Yes|
|B|S9 kanban-skill|Read `blocked_by` frontmatter and block movement to active work|Low|Low|Low|No|Yes|
|C|S6 OpenClaw|Durable flow state includes explicit waiting/blocked states|Med|Med|Med|No|Partial|

**Best option for solo operator, no SaaS, Claude Code environment:** **Option A.** The CCPM pattern is the cleanest low-token implementation and already names the user-facing trigger. 

**Evidence:** CCPM `track.md` maps “what’s blocked” to `bash references/scripts/blocked.sh`; exact file URL: `https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/track.md`. Kanban’s rules say a card cannot move to `doing` until all cards in `blocked_by` are `done`; exact source page with example card and fields: `https://github.com/mattjoyce/kanban-skill`. 

### Update status

**ID: PM6**

**What this process does:** Mutates task/project state after work completes.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Requires Python?|Portable?|
|---|---|---|---|---|---|---|---|
|A|S2 Backlog.md|Edit markdown/frontmatter fields directly|Low|Low|Low|No|Yes|
|B|S9 kanban-skill|Change `status`, preserve narrative/history in card markdown|Low|Low|Low|No|Yes|
|C|S6 OpenClaw|Update durable flow state (`currentStep`, `stateJson`, revision-safe mutations)|Med|Med|Med|No|Partial|

**Best option for solo operator, no SaaS, Claude Code environment:** **Option A.** Direct frontmatter mutation is sufficient and keeps state obvious to both human and model. 

**Evidence:** Backlog example task exposes `status` and `updated_date` as first-class mutable fields; exact file URL: `https://github.com/MrLesk/Backlog.md/blob/main/backlog/tasks/back-200%20-%20Add-Claude-Code-integration-with-workflow-commands-during-init.md`. Kanban’s rules explicitly rely on markdown status changes; source page: `https://github.com/mattjoyce/kanban-skill`. 

### Detect stall

**ID: PM7**

**What this process does:** Flags tasks or projects that are no longer progressing.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Requires Python?|Portable?|
|---|---|---|---|---|---|---|---|
|A|S8 llm-wiki|Use stale `updated` date / lint-style heuristics|Low|Med|Med|No|Yes|
|B|S1 CCPM|Infer from standup/status/in-progress outputs|Low|Med|Med|No|Yes|
|C|S14 LangGraph|Detect stalled states via workflow state machine|High|High|High|Yes|No|

**Best option for solo operator, no SaaS, Claude Code environment:** **Option A.** Staleness heuristics over markdown timestamps/logs are a reasonable lightweight implementation pattern; no retrieved source provided a more direct public “stall detector” for Claude skills. 

**Evidence:** llm-wiki requires frontmatter `updated` on every page and its bundled linter checks for “stale `updated` dates”; exact file URL: `https://github.com/praneybehl/llm-wiki-plugin/blob/main/skills/llm-wiki/SKILL.md`. The bootstrap script preserves `SCHEMA.md`, `index.md`, and `log.md`, which gives a basis for stall heuristics; exact file URL: `https://github.com/praneybehl/llm-wiki-plugin/blob/main/skills/llm-wiki/scripts/init_wiki.py`. 

### Generate work registry

**ID: PM8**

**What this process does:** Produces one compact index of all current project state.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Requires Python?|Portable?|
|---|---|---|---|---|---|---|---|
|A|S8 llm-wiki|Maintain `index.md` / sharded indexes as project registry|Low|Low|Low|No|Yes|
|B|S1 CCPM|Script-generated status/epic views|Low|Med|Med|No|Yes|
|C|S13 hermes-agent|Registry/index build with metadata cache and grouping sidecar|Med|Med|Med|Yes|Partial|

**Best option for solo operator, no SaaS, Claude Code environment:** **Option A.** llm-wiki’s `index.md` pattern is the clearest compact registry pattern and is explicitly optimized to be cheap to read. 

**Evidence:** llm-wiki defines `index.md` as “entry point: catalog of all pages with one-line summaries,” says to read it first, and recommends sharding once size grows; exact file URL: `https://github.com/praneybehl/llm-wiki-plugin/blob/main/skills/llm-wiki/SKILL.md`. 

## Knowledge base management execution options

### Write session progress

**ID: KB1**

**What this process does:** Records what happened in a work session.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Requires Python?|Portable?|
|---|---|---|---|---|---|---|---|
|A|S8 llm-wiki|Append a dated line to `log.md`|Low|Low|Low|No|Yes|
|B|S1 CCPM|Reuse standup/status-style progress summaries|Low|Low|Low|No|Yes|
|C|S6 OpenClaw|Persist flow state and owner context across steps|Med|Med|Med|No|Partial|

**Best option:** **Option A.** Append-only chronological logging is the most robust low-friction pattern. 

**Evidence:** llm-wiki requires `log.md` as an “append-only chronological log of ingests/queries/lints”; exact file URL: `https://github.com/praneybehl/llm-wiki-plugin/blob/main/skills/llm-wiki/SKILL.md`. 

### Extract state deltas

**ID: KB2**

**What this process does:** Converts session narrative into structured state changes.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Requires Python?|Portable?|
|---|---|---|---|---|---|---|---|
|A|S7 crewAI|Use structured expected output / Pydantic-style extraction schema|Med|Med|Med|Yes|No|
|B|Pure SKILL pattern, closest in S8 llm-wiki|Claude extracts deltas and applies surgical edits|Med|Low|Low|No|Yes|
|C|S14 LangGraph|State object updated step by step|High|High|High|Yes|No|

**Best option:** **Option B.** Extraction is not mathematically impossible in pure reasoning, so a SKILL-backed structured delta pass is sufficient for solo use. 

**Evidence:** crewAI exposes structured output (`output_pydantic` / `output_json`) as the main downstream-parsing mechanism; exact file URL: `https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md`. llm-wiki mandates surgical edits instead of rewrites; exact file URL: `https://github.com/praneybehl/llm-wiki-plugin/blob/main/skills/llm-wiki/SKILL.md`. 

### Maintain entity files

**ID: KB3**

**What this process does:** Safely applies deltas to markdown entity/state files.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Requires Python?|Portable?|
|---|---|---|---|---|---|---|---|
|A|S8 llm-wiki|`str_replace`/section edits to touched files only|Low|Low|Low|No|Yes|
|B|S2 Backlog.md|Update single-file task records in place|Low|Low|Low|No|Yes|
|C|S6 OpenClaw|Revision-safe state mutation in flow|Med|Med|Med|No|Partial|

**Best option:** **Option A.** This is the strongest public pattern for safe markdown mutation. 

**Evidence:** llm-wiki says “Surgical edits, not rewrites” and warns that full rewrites are slow, token-expensive, and risk losing nuance; exact file URL: `https://github.com/praneybehl/llm-wiki-plugin/blob/main/skills/llm-wiki/SKILL.md`. 

### Rebuild index

**ID: KB4**

**What this process does:** Regenerates the compact registry after files change.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Requires Python?|Portable?|
|---|---|---|---|---|---|---|---|
|A|S8 llm-wiki|Maintain/rebuild `index.md` and optional shard files|Low|Low|Low|No|Yes|
|B|S8 llm-wiki scripts|Bootstrap or rebuild from templates/scripts|Low|Med|Med|Yes|Yes|
|C|S13 hermes-agent|Cached metadata index with grouping sidecar|Med|Med|Med|Yes|Partial|

**Best option:** **Option A** for small-to-medium scale; **Option B** becomes more attractive once the registry is large enough that manual maintenance becomes noisy. 

**Evidence:** llm-wiki explicitly treats `index.md` as the cheap registry layer, introduces sharding thresholds, and bootstraps `index.md` from template files; exact file URLs: `https://github.com/praneybehl/llm-wiki-plugin/blob/main/skills/llm-wiki/SKILL.md` and `https://github.com/praneybehl/llm-wiki-plugin/blob/main/skills/llm-wiki/scripts/init_wiki.py`. 

### Detect drift

**ID: KB5**

**What this process does:** Finds divergence between current knowledge-state and the previous session or source of truth.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Requires Python?|Portable?|
|---|---|---|---|---|---|---|---|
|A|S8 llm-wiki|Compare `updated`, `sources`, `log.md`, backlinks, and lint output|Low|Med|Med|No|Yes|
|B|S1 CCPM|Run validation for orphaned/missing/integrity issues|Low|Med|Med|No|Yes|
|C|S14 LangGraph|Persisted workflow state drift detection|High|High|High|Yes|No|

**Best option:** **Option A.** The combination of metadata, log, and lint-style checks is sufficient for KB drift without introducing a database. 

**Evidence:** llm-wiki requires `sources` and `updated` in frontmatter and ships structural lint; exact file URL: `https://github.com/praneybehl/llm-wiki-plugin/blob/main/skills/llm-wiki/SKILL.md`. CCPM validation checks “frontmatter consistency, orphaned files, missing GitHub links, dependency integrity”; exact file URL: `https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/track.md`. 

### Produce next-session context

**ID: KB6**

**What this process does:** Produces a self-contained handoff packet for the next session.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Requires Python?|Portable?|
|---|---|---|---|---|---|---|---|
|A|S8 llm-wiki|Synthesize from index, candidate pages, backlinks, and synthesis notes|Med|Low|Low|No|Yes|
|B|S1 CCPM|Standup/status packet from project files|Low|Med|Med|No|Yes|
|C|S6 OpenClaw|Durable job/owner context with persisted state|Med|Med|Med|No|Partial|

**Best option:** **Option A.** llm-wiki is the closest public implementation to “self-contained context packet with guardrails between sessions.” 

**Evidence:** llm-wiki’s query workflow reads the index first, then candidate pages, then synthesizes an answer and can file it back into `wiki/synthesis/`; exact file URL: `https://github.com/praneybehl/llm-wiki-plugin/blob/main/skills/llm-wiki/SKILL.md`. 

## Product management execution options

### Score priority

**ID: PD1**

**What this process does:** Assigns a comparative priority value to work items.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Requires Python?|Portable?|
|---|---|---|---|---|---|---|---|
|A|S7 crewAI|Rubric-driven scoring task with explicit output schema|Med|Med|Med|Yes|No|
|B|S2 Backlog.md|Persist priority field in markdown record|Low|Low|Low|No|Yes|
|C|Pure SKILL pattern, closest in S1/S8|Claude applies written rubric against compact registry|Med|Low|Low|No|Yes|

**Best option:** **Option C.** Priority scoring is reasoning-heavy but not computationally impossible, so a pure SKILL rubric over a compact registry is sufficient. 

**Evidence:** Backlog example shows `priority` as a first-class task field; exact file URL: `https://github.com/MrLesk/Backlog.md/blob/main/backlog/tasks/back-200%20-%20Add-Claude-Code-integration-with-workflow-commands-during-init.md`. crewAI emphasizes explicit success criteria and structured outputs; exact file URL: `https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md`. 

### Score urgency

**ID: PD2**

**What this process does:** Separates time-sensitivity from general priority.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Requires Python?|Portable?|
|---|---|---|---|---|---|---|---|
|A|S2 Backlog.md / S9 kanban-skill|Use date-like fields plus rubric to assign urgency separately|Low|Low|Low|No|Yes|
|B|S7 crewAI|Make urgency its own output field/task|Med|Med|Med|Yes|No|
|C|Script-assisted date scan, closest in S8/S1|Deterministic sort by due/update metadata, then human/LLM interpretation|Low|Med|Med|No|Yes|

**Best option:** **Option A.** No confirmed source offered a dedicated urgency algorithm, but the public markdown-field patterns are sufficient to model urgency separately from priority. 

**Evidence:** Backlog example stores `priority`; kanban-skill stores `due_date`; exact source pages: `https://github.com/MrLesk/Backlog.md/blob/main/backlog/tasks/back-200%20-%20Add-Claude-Code-integration-with-workflow-commands-during-init.md` and `https://github.com/mattjoyce/kanban-skill`. 

### Compute unlock depth

**ID: PD3**

**What this process does:** Calculates how many downstream items become available when a given item completes.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Requires Python?|Portable?|
|---|---|---|---|---|---|---|---|
|A|S1 CCPM|Reason over `depends_on` graph in markdown|Med|Low|Low|No|Yes|
|B|S8 llm-wiki graph layer|Use optional graph extract/query scripts for exact traversal|Low|Med|Med|Yes|Yes|
|C|S14 LangGraph|Encode full dependency graph in a workflow runtime|High|High|High|Yes|No|

**Best option:** **Option B** if exact unlock counts matter repeatedly; **Option A** is viable for small graphs. 

**Evidence:** CCPM encodes dependencies explicitly in `depends_on`; exact file URL: `https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md`. llm-wiki exposes optional graph extract/query scripts (`wiki_graph_extract.py`, `wiki_graph_query.py`); exact file URL: `https://github.com/praneybehl/llm-wiki-plugin/blob/main/skills/llm-wiki/SKILL.md`. 

### Synthesize focus recommendation

**ID: PD4**

**What this process does:** Produces a ranked focus list with reasoning.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Requires Python?|Portable?|
|---|---|---|---|---|---|---|---|
|A|Pure SKILL over S1/S8 registry|Claude reasons over next/blockers/index/log and writes ranked recommendation|Med|Low|Low|No|Yes|
|B|S7 crewAI|Dedicated synthesis task with explicit output format|Med|Med|Med|Yes|No|
|C|S14 LangGraph|Route/scored decision graph|High|High|High|Yes|No|

**Best option:** **Option A.** Focus recommendation is explanation-heavy and benefits from Claude’s reasoning more than from a workflow engine. 

**Evidence:** CCPM already exposes “what’s next” and “what’s blocked,” while llm-wiki provides the cheap index-first registry layer; exact file URLs: `https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/track.md` and `https://github.com/praneybehl/llm-wiki-plugin/blob/main/skills/llm-wiki/SKILL.md`. 

### Validate with operator

**ID: PD5**

**What this process does:** Inserts a human gate before mutating planning state.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Requires Python?|Portable?|
|---|---|---|---|---|---|---|---|
|A|S7 crewAI|Built-in human feedback / approval branch|Med|Med|Med|Yes|No|
|B|S8 llm-wiki|Explicit approval before memory-file or schema mutations|Low|Low|Low|No|Yes|
|C|S1 CCPM|Confirm destructive/recreation actions before proceeding|Low|Low|Low|No|Yes|

**Best option:** **Option B.** For Claude Code solo work, a simple explicit confirmation gate is sufficient and less coupled than a framework-level human-feedback abstraction. 

**Evidence:** llm-wiki says “Never write to the memory file without the user’s approval,” and its upgrade flow never overwrites `SCHEMA.md`; exact file URLs: `https://github.com/praneybehl/llm-wiki-plugin/blob/main/skills/llm-wiki/SKILL.md` and `https://github.com/praneybehl/llm-wiki-plugin/blob/main/skills/llm-wiki/scripts/init_wiki.py`. crewAI has `@human_feedback`; exact file URL: `https://github.com/crewAIInc/skills/blob/main/skills/getting-started/SKILL.md`. 

### Feed planning layer

**ID: PD6**

**What this process does:** Produces a structured handoff for a downstream planning step such as a daily planning ritual.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Requires Python?|Portable?|
|---|---|---|---|---|---|---|---|
|A|S1 CCPM|Use status/standup/next report as downstream packet|Low|Med|Med|No|Yes|
|B|S8 llm-wiki|File synthesized recommendation into `wiki/synthesis/`|Med|Low|Low|No|Yes|
|C|S6 OpenClaw|Durable multi-step taskflow handing output from one step to another|Med|Med|Med|No|Partial|

**Best option:** **Option A.** CCPM already packages the exact kinds of outputs a downstream planning layer would consume. 

**Evidence:** CCPM standup/status scripts explicitly output completed work, in-progress work, blockers, and next priority; exact file URL: `https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/track.md`. 

## Sub-skill groupings, closest public matches, and final summary

### Natural sub-skill groupings

The strongest natural grouping is **Project registry and routing**: PM1, PM6, PM8, KB1, KB6, PD6. These all operate on the same compact state files and handoff artifacts, and their best public analogs are CCPM’s status/standup scripts and llm-wiki’s `SCHEMA.md`/`index.md`/`log.md` pattern. 

A second grouping is **Decomposition and dependency management**: PM2, PM3, PM4, PM5, PD3. These share task files plus dependency metadata; CCPM is the clearest reusable base because it already stores `depends_on`, `parallel`, and `conflicts_with` and already ships next/blocker scripts. 

A third grouping is **Knowledge mutation and integrity**: KB2, KB3, KB4, KB5. These share the same file set and are best matched by llm-wiki’s surgical-edit, index-first, lint, and bootstrap patterns. 

A fourth grouping is **Product scoring and operator gating**: PD1, PD2, PD4, PD5. These are reasoning-heavy and best matched by pure SKILL patterns plus optional structured-output conventions from crewAI. 

### Per-group fit

|Sub-skill group|Pure SKILL.md possible?|Script required?|Reusable open-source base|What would need to change|
|---|---|---|---|---|
|Project registry and routing|Yes|No|S8 llm-wiki + S1 CCPM|Replace research/wiki nouns with project/session/planning nouns|
|Decomposition and dependency management|Yes|No, but helpful for next/blockers|S1 CCPM|Swap GitHub-issue assumptions for local repo state where needed|
|Knowledge mutation and integrity|Yes|No, but helpful for lint/index rebuild|S8 llm-wiki|Narrow wiki conventions into Apex KB entity/state conventions|
|Product scoring and operator gating|Yes|No|S7 crewAI design-task + S8 approval patterns|Replace crew/runtime coupling with Claude-native prompt forms|

### Closest public matches for the private PRC patterns

|Private pattern|Closest public implementation|Why|
|---|---|---|
|PRC-CORE-001|S7 crewAI design-task + S1 CCPM|intake/goal/source/skeleton/fill/verify maps closely to explicit task design plus CCPM’s phase structure|
|TEMPLATE-KANBAN-001|S9 kanban-skill + S1 CCPM structure|lanes + dependencies + review gates align with markdown cards plus dependency metadata|
|PRC-HANDOFF-001|S8 llm-wiki synthesis/index/log|closest public “self-contained context packet” pattern|
|PRC-DATA-001|S7 crewAI Flow, weakly S14 LangGraph|staged stateful workflow, but no direct Claude-skill CRISP-DM implementation was confirmed|
|PRC-VERIFY-001|S1 CCPM validate + S8 lint + S7 human gate|closest public chain-of-verification equivalents|
|PRC-SCRUM-001|S1 CCPM track/status/standup|plan/execute/review loop is closest here|
|PRC-RISK-001|No strong direct match; closest is S13 hermes-agent trust/governance metadata|governance/risk framing exists, but not as an Apex-ready workflow skill|

### Processes with no strong public implementation pattern

The clearest gaps are **PM7 Detect stall**, **PD2 Score urgency as a distinct construct**, and **PRC-RISK-001-style governance**. Public sources provide adjacent patterns — stale-date linting, due-date fields, trust-level metadata — but no clean off-the-shelf implementation was confirmed for these exact behaviors in a Claude-skill-first repo workflow. 

### Final summary table

|Process|Best source|Mechanism|Needs script?|Copy type|Rank|
|---|---|---|---|---|---|
|PM1|S2 Backlog.md|YAML/frontmatter capture file|No|ADAPT|6|
|PM2|S1 CCPM|Epic → numbered task files|No|ADAPT|2|
|PM3|S1 CCPM|`depends_on` / `conflicts_with` metadata|No|FULL|1|
|PM4|S1 CCPM|Deterministic `next.sh`|No|ADAPT|3|
|PM5|S1 CCPM|Deterministic blocker report|No|ADAPT|4|
|PM6|S2 Backlog.md|Direct frontmatter mutation|No|FULL|10|
|PM7|S8 llm-wiki|Stale-date / lint heuristic|No|CONCEPT|17|
|PM8|S8 llm-wiki|`index.md` registry|No|ADAPT|5|
|KB1|S8 llm-wiki|Append-only `log.md`|No|FULL|7|
|KB2|S8 llm-wiki + S7 crewAI|Structured delta extraction|No|ADAPT|14|
|KB3|S8 llm-wiki|Surgical file edits|No|FULL|8|
|KB4|S8 llm-wiki|Index rebuild/sharding|No|ADAPT|9|
|KB5|S8 llm-wiki|Drift via metadata/log/lint|No|CONCEPT|18|
|KB6|S8 llm-wiki|Synthesis/handoff packet|No|ADAPT|11|
|PD1|S7 crewAI + file-first rubric|Explicit scoring rubric|No|ADAPT|15|
|PD2|S2/S9 field pattern|Separate urgency field/rubric|No|CONCEPT|19|
|PD3|S1 CCPM + S8 graph option|Dependency graph traversal|No|ADAPT|12|
|PD4|S1/S8 pure synthesis|Ranked focus reasoning|No|ADAPT|13|
|PD5|S8 approval gate|Human confirmation before mutation|No|FULL|16|
|PD6|S1 CCPM|Status/standup/next handoff|No|ADAPT|20|

### Open questions and limitations

Several requested sources were **not confidently retrievable as implementation files** during this research window: **S3 task-master, S4 GSD Core, S5 planning-with-files, S10 pm-skills, S11 swarmvault, S12 Imprint**. S9 kanban-skill was only partially retrievable at file level. Because of that, this report is strongest where it relies on S1, S6, S7, S8, S13, and S14, and weaker where it would have benefited from additional corroboration. This report therefore supports **execution-option decisions**, but it should not be read as proof that no better public implementation exists for the missing sources.