## 1. Source Ledger

|Source ID|File URL|Fetch status|Evidence extracted|Limitations|Used for|
|---|---|--:|---|---|---|
|S1a|[[https://github.com/automazeio/ccpm/blob/main/skill/ccpm/SKILL.md](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/SKILL.md)]|OK|PRD→epic→tasks lifecycle; phase routing; script-first rule; status/blocked/next scripts. ([GitHub](https://raw.githubusercontent.com/automazeio/ccpm/main/skill/ccpm/SKILL.md "raw.githubusercontent.com"))|Raw render collapsed, but GitHub blob and raw were read.|PM2, PM4, PM5, PM6, PM8|
|S1b|[[https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md)]|OK|Task file frontmatter: `name`, `status`, `created`, `updated`, `github`, `depends_on`, `parallel`, `conflicts_with`; dependency rules; circular dependency error. ([GitHub](https://raw.githubusercontent.com/automazeio/ccpm/main/skill/ccpm/references/structure.md "(parallel: true/false)<br>- [ ] 002.md - <Title> (parallel: true/false)<br>Total tasks: N<br>Parallel tasks: N<br>Sequential tasks: N<br>Estimated total effort: N hours<br>```<br>**After completion**: Confirm \"✅ Created N tasks for epic: <name>\" and suggest: \"Ready to push to GitHub? Say: sync the <name> epic\"<br>---<br>## Dependency Rules<br>- `depends_on` lists task numbers that must complete before this task can start.<br>- `parallel: true` means the task can run concurrently with others it doesn't conflict with.<br>- `conflicts_with` lists tasks that touch the same files — these cannot run in parallel.<br>- Circular dependencies are an error — check before finalizing."))|Raw render collapsed but readable.|PM2, PM3, PM8|
|S1c|[[https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/track.md](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/track.md)]|OK|Tracking is script-first; status, standup, search, in-progress, next, blocked, validate scripts. ([GitHub](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/track.md "ccpm/skill/ccpm/references/track.md at main · automazeio/ccpm · GitHub"))|Script bodies not fetched, only skill reference.|PM4, PM5, PM6, PM8|
|S2a|[[https://github.com/MrLesk/Backlog.md/blob/main/backlog/tasks/back-200%20-%20Add-Claude-Code-integration-with-workflow-commands-during-init.md](https://github.com/MrLesk/Backlog.md/blob/main/backlog/tasks/back-200%20-%20Add-Claude-Code-integration-with-workflow-commands-during-init.md)]|OK|Concrete Markdown task fields: id, title, status, dependencies, priority, labels, acceptance criteria. ([GitHub](https://github.com/MrLesk/Backlog.md/blob/main/backlog/tasks/back-200%20-%20Add-Claude-Code-integration-with-workflow-commands-during-init.md "Backlog.md/backlog/tasks/back-200 - Add-Claude-Code-integration-with-workflow-commands-during-init.md at main · MrLesk/Backlog.md · GitHub"))|One sample task only.|PM1, PM6, PM8, PD5|
|S2b|[[https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts](https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts)]|OK|Type definitions for Task, TaskCreateInput, TaskUpdateInput, priority, dependencies, acceptance criteria, definition-of-done, status callback. ([GitHub](https://raw.githubusercontent.com/MrLesk/Backlog.md/main/src/types/index.ts "raw.githubusercontent.com"))|Raw line collapsed, but complete interface content readable.|PM1, PM6, PM8, PD5|
|S3a|[[https://github.com/eyaltoledano/claude-task-master/blob/main/docs/task-structure.md](https://github.com/eyaltoledano/claude-task-master/blob/main/docs/task-structure.md)]|OK|JSON task schema; status enum; dependency array; priority enum; `next` command behavior; complexity scoring. ([GitHub](https://github.com/eyaltoledano/claude-task-master/blob/main/docs/task-structure.md "claude-task-master/docs/task-structure.md at main · eyaltoledano/claude-task-master · GitHub"))|Docs plus schema, not all commands.|PM3, PM4, PD1, PD3, PD4|
|S3b|[[https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js)]|OK|Next-task algorithm: completed-ID set, eligible subtasks, dependency satisfaction, priority sort, dependency-count tie-break, fallback to top-level tasks. ([GitHub](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js "claude-task-master/scripts/modules/task-manager/find-next-task.js at main · eyaltoledano/claude-task-master · GitHub"))|Good algorithmic evidence.|PM4, PD3, PD4|
|S4a|[[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)]|OK|`task_plan.md`, `findings.md`, `progress.md`; session restore; error logging; 2-action persistence rule; context recovery scripts. ([GitHub](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md "ok-skills/planning-with-files/SKILL.md at main · mxyhi/ok-skills · GitHub"))|Hook details not fully extracted.|KB1, KB2, KB5, KB6, PD6|
|S4b|[[https://github.com/OthmanAdi/planning-with-files/blob/master/docs/quickstart.md](https://github.com/OthmanAdi/planning-with-files/blob/master/docs/quickstart.md)]|OK|Five-step quickstart; three planning files; phase status updates; research findings; progress logs; error capture. ([GitHub](https://github.com/OthmanAdi/planning-with-files/blob/master/docs/quickstart.md "planning-with-files/docs/quickstart.md at master · OthmanAdi/planning-with-files · GitHub"))|Documentation pattern, not implementation code.|KB1, KB2, PD6|
|S5a|[[https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md](https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md)]|OK|Markdown card frontmatter: `id`, `status`, `priority`, `blocked_by`, `assignee`, `due_date`, tags; lane model; narrative append policy. ([GitHub](https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md "kanban-skill/skills/kanban-ai/SKILL.md at master · mattjoyce/kanban-skill · GitHub"))|No helper script fetched.|PM3, PM5, PM6, PM7|
|S6a|[[https://github.com/alirezarezvani/claude-skills/blob/main/engineering/llm-wiki/skills/llm-wiki/SKILL.md](https://github.com/alirezarezvani/claude-skills/blob/main/engineering/llm-wiki/skills/llm-wiki/SKILL.md)]|OK|Persistent wiki/second-brain skill; source ingestion; entity/concept pages; cross-reference maintenance; compounding Markdown KB. ([GitHub](https://github.com/alirezarezvani/claude-skills/blob/main/engineering/llm-wiki/skills/llm-wiki/SKILL.md "claude-skills/engineering/llm-wiki/skills/llm-wiki/SKILL.md at main · alirezarezvani/claude-skills · GitHub"))|General skill, not Apex-specific.|KB3, KB5|
|S6b|[[https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py](https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py)]|OK|Python index rebuild: scans Markdown, parses frontmatter, groups by type, sorts by updated date, generates index. ([GitHub](https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py "llm-wiki/scripts/update-index.py at main · junbjnnn/llm-wiki · GitHub"))|Enough for index rebuild; ingest.py not fetched.|KB4, PM8|
|S7a|[[https://github.com/openclaw/openclaw/blob/main/skills/taskflow/SKILL.md](https://github.com/openclaw/openclaw/blob/main/skills/taskflow/SKILL.md)]|OK|Durable TaskFlow lifecycle; `stateJson`, `waitJson`, child task linkage, wait/resume/finish/fail/cancel, revision checks. ([GitHub](https://github.com/openclaw/openclaw/blob/main/skills/taskflow/SKILL.md "openclaw/skills/taskflow/SKILL.md at main · openclaw/openclaw · GitHub"))|Escalation reference only.|PM7, KB6, PD6|
|S8a|[[https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md](https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md)]|OK|Task description + expected_output; task dependency context; output formats; guardrails; human input. ([GitHub](https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md "skills/skills/design-task/SKILL.md at main · crewAIInc/skills · GitHub"))|CrewAI-specific, used as contract pattern only.|PD5, KB2, PD4|
|S8b|[[https://github.com/crewAIInc/skills/blob/main/skills/getting-started/SKILL.md](https://github.com/crewAIInc/skills/blob/main/skills/getting-started/SKILL.md)]|OK|Architecture abstraction choice, scaffold-first rule, YAML task/agent configuration. ([GitHub](https://github.com/crewAIInc/skills/blob/main/skills/getting-started/SKILL.md "skills/skills/getting-started/SKILL.md at main · crewAIInc/skills · GitHub"))|Heavy CrewAI coupling.|PD5|
|S9a|[[https://github.com/NousResearch/hermes-agent/blob/main/tools/skills_hub.py](https://github.com/NousResearch/hermes-agent/blob/main/tools/skills_hub.py)]|OK|Skill metadata model; source adapters; GitHub Contents API; hub lock file; provenance; quarantine; audit log; cache. ([GitHub](https://github.com/NousResearch/hermes-agent/blob/main/tools/skills_hub.py "hermes-agent/tools/skills_hub.py at main · NousResearch/hermes-agent · GitHub"))|Governance support only.|PD5 optional|
|S9b|[[https://github.com/NousResearch/hermes-agent/blob/main/tools/skills_guard.py](https://github.com/NousResearch/hermes-agent/blob/main/tools/skills_guard.py)]|OK|Trust levels, trusted repos, scan verdicts, install policy, community-skill blocking rules. ([GitHub](https://github.com/NousResearch/hermes-agent/blob/main/tools/skills_guard.py "hermes-agent/tools/skills_guard.py at main · NousResearch/hermes-agent · GitHub"))|Security/governance only.|PD5 optional|
|S10a|[[https://github.com/langchain-ai/langgraph/blob/main/libs/langgraph/README.md](https://github.com/langchain-ai/langgraph/blob/main/libs/langgraph/README.md)]|OK|Stateful orchestration framework; durable execution, human-in-loop, persistence, memory; high-complexity escalation reference. ([GitHub](https://github.com/langchain-ai/langgraph/blob/main/libs/langgraph/README.md "langgraph/libs/langgraph/README.md at main · langchain-ai/langgraph · GitHub"))|README, not minimal code example.|Escalation only|
|S10b|[[https://github.com/langchain-ai/langgraph/blob/main/libs/langgraph/langgraph/graph/state.py](https://github.com/langchain-ai/langgraph/blob/main/libs/langgraph/langgraph/graph/state.py)]|PARTIAL|StateGraph class source fetched; confirms stateful graph implementation file exists. ([GitHub](https://github.com/langchain-ai/langgraph/blob/main/libs/langgraph/langgraph/graph/state.py "langgraph/libs/langgraph/langgraph/graph/state.py at main · langchain-ai/langgraph · GitHub"))|Code lines not useful in rendered extraction. Do not use for detailed API claims.|Escalation only|

---

## 2. Evidence Matrix

|Evidence category|Best supporting source(s)|Concrete mechanism|Script boundary|
|---|---|---|---|
|Markdown/YAML task contract|S1b, S2a, S5a|Frontmatter task/card files with status, dependency, priority fields.|No|
|JSON task schema|S3a|`tasks.json` with id, title, status, dependencies, priority, details, subtasks.|No|
|Dependency graph|S1b, S3a, S5a|`depends_on`, `dependencies`, `blocked_by`, `conflicts_with`.|Yes for exact graph validation|
|Blocker detection|S1c, S5a|`blocked.sh` style query; `blocked_by` card semantics.|Yes if cross-file|
|Next-action computation|S3b, S1c|`findNextTask` dependency+priority sort; `next.sh`.|Yes|
|Status update|S2b, S5a|`TaskUpdateInput.status`; card lane status.|Maybe|
|Stall detection|S5a, S7a|Narrative timestamps + durable state/wait lifecycle.|Yes|
|Work registry/index|S6b, S1c|Scan Markdown/frontmatter and rebuild index/status summary.|Yes|
|Session progress capture|S4a, S4b|`progress.md` and `task_plan.md` phase logs.|No|
|State delta extraction|S4a, S8a|Extract findings/progress into structured expected_output.|No|
|Entity file maintenance|S6a|Persistent Obsidian-style entity/concept pages.|Maybe|
|Index rebuild|S6b|Python scans pages, parses frontmatter, groups/sorts, writes index.|Yes|
|Drift detection|S4a, S7a, S9b|Plan attestation/hash; revision-checked state; trust scan.|Yes|
|Next-session handoff|S4a, S7a|Restore context from files; persisted `stateJson`/wait metadata.|Maybe|
|Priority scoring|S3a, S3b|high/medium/low priority and sort values.|Yes for exact ranking|
|Urgency scoring|No substantiated source|No exact separate urgency model found.|Custom|
|Unlock-depth scoring|S1b, S3b|Dependency graph can derive downstream unlock count.|Yes|
|Focus recommendation|S3b, S1c|Next-task selection and status scripts.|Yes|
|Human validation gate|S8a, S9b|Human input/guardrails; trust-aware install policy.|No|
|Planning-layer handoff|S4a, S7a|Planning files and durable state bag.|No/Maybe|
|Stateful workflow escalation|S7a, S10a|TaskFlow state lifecycle; LangGraph durable orchestration.|Yes|

---

## 3. Process Option Tables

### PM1 Capture project

What it does: Records project name, goal, domain, state, and success criteria.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|---|---|---|---|---|
|Markdown task/project contract|S2b [[https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts](https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts)]|Adapt `TaskCreateInput` fields into `project_capture` frontmatter/body.|Low|Low|Low|No|Yes|

Best option for solo operator, Claude Code, no SaaS: Use Backlog.md’s typed Markdown task-field model as a compact project-capture contract: [[https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts](https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts)]

### PM2 Decompose project

What it does: Breaks a project into epics, chunks, and tasks with explicit splitting rules.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|---|---|---|---|---|
|CCPM epic decomposition|S1b [[https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md)]|Analyze epic, split by task type, size, parallelism, numbered task files.|Medium|Low|Medium|No|Yes|

Best option for solo operator, Claude Code, no SaaS: Use CCPM `structure.md` as the decomposition pattern: [[https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md)]

### PM3 Assign dependencies

What it does: Builds `depends_on` and `unlocks` graph between work items.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|---|---|---|---|---|
|Dependency frontmatter|S1b [[https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md)]|Use `depends_on`, `parallel`, `conflicts_with`; derive `unlocks` by reverse lookup.|Medium|Medium|High|Yes|Yes|

Best option for solo operator, Claude Code, no SaaS: Use CCPM’s dependency fields and add a small reverse-index script for `unlocks`: [[https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md)]

### PM4 Compute next action

What it does: Determines the next executable task from state and dependency graph.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|---|---|---|---|---|
|Deterministic next-task algorithm|S3b [[https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js)]|Filter pending/in-progress items with satisfied dependencies; sort by priority, dependency count, id.|Low|Medium|High|Yes|Yes|

Best option for solo operator, Claude Code, no SaaS: Copy the Task Master next-task algorithm concept into a small Python script: [[https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js)]

### PM5 Detect blockers

What it does: Identifies items that cannot proceed.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|---|---|---|---|---|
|Blocked-by card semantics|S5a [[https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md](https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md)]|`blocked_by` list prevents lane transition until blocker IDs are done.|Low|Medium|High|Yes|Yes|

Best option for solo operator, Claude Code, no SaaS: Use Kanban `blocked_by` plus deterministic scan: [[https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md](https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md)]

### PM6 Update status

What it does: Marks items complete or updates state after work finishes.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|---|---|---|---|---|
|Task/card status mutation|S2b [[https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts](https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts)]|`TaskUpdateInput.status`; preserve acceptance criteria and final summary.|Low|Low|Medium|Maybe|Yes|

Best option for solo operator, Claude Code, no SaaS: Use Backlog.md’s status-update input model and keep Markdown mutation operator-reviewed: [[https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts](https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts)]

### PM7 Detect stall

What it does: Finds work items with no progress across multiple sessions.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|---|---|---|---|---|
|Narrative timestamp scan|S5a [[https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md](https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md)]|Append dated narrative entries; detect stale cards by missing recent narrative/status change.|Medium|Medium|High|Yes|Yes|

Best option for solo operator, Claude Code, no SaaS: Use Kanban narrative logs plus a stale-item scanner: [[https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md](https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md)]

### PM8 Generate work registry

What it does: Produces compact index of all project state.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|---|---|---|---|---|
|Markdown/frontmatter index rebuild|S6b [[https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py](https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py)]|Scan `.md`, parse frontmatter, group/sort, generate index file.|Low|Medium|High|Yes|Yes|

Best option for solo operator, Claude Code, no SaaS: Adapt `update-index.py` into an Apex registry rebuild script: [[https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py](https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py)]

---

### KB1 Write session progress

What it does: Captures what happened during a work session.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|---|---|---|---|---|
|Progress file log|S4a [[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)]|Use `progress.md` for session log, test results, actions, errors.|Low|Low|Low|No|Yes|

Best option for solo operator, Claude Code, no SaaS: Use planning-with-files `progress.md`: [[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)]

### KB2 Extract state deltas

What it does: Converts session narrative into structured field changes.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|---|---|---|---|---|
|Expected-output contract|S8a [[https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md](https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md)]|Define exact expected output for deltas; validate before mutation.|Medium|Low|Medium|No|Yes|

Best option for solo operator, Claude Code, no SaaS: Use CrewAI task-contract discipline for delta packets: [[https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md](https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md)]

### KB3 Maintain entity files

What it does: Applies deltas to Markdown entity files without data loss.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|---|---|---|---|---|
|Persistent wiki maintenance|S6a [[https://github.com/alirezarezvani/claude-skills/blob/main/engineering/llm-wiki/skills/llm-wiki/SKILL.md](https://github.com/alirezarezvani/claude-skills/blob/main/engineering/llm-wiki/skills/llm-wiki/SKILL.md)]|Maintain interlinked Markdown pages incrementally, preserving cross-references.|Medium|Low|Medium|Maybe|Yes|

Best option for solo operator, Claude Code, no SaaS: Use llm-wiki entity/concept page maintenance as the closest public pattern: [[https://github.com/alirezarezvani/claude-skills/blob/main/engineering/llm-wiki/skills/llm-wiki/SKILL.md](https://github.com/alirezarezvani/claude-skills/blob/main/engineering/llm-wiki/skills/llm-wiki/SKILL.md)]

### KB4 Rebuild index

What it does: Regenerates registry after state changes.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|---|---|---|---|---|
|Python index rebuild|S6b [[https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py](https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py)]|Scan Markdown, parse frontmatter, group pages by type, write index.|Low|Medium|High|Yes|Yes|

Best option for solo operator, Claude Code, no SaaS: Copy the scan/group/write pattern from llm-wiki: [[https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py](https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py)]

### KB5 Detect drift

What it does: Compares current state against last session snapshot.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|---|---|---|---|---|
|Plan attestation / hash check|S4a [[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)]|SHA-256 attestation detects tampered/diverged plan file.|Low|Medium|High|Yes|Yes|

Best option for solo operator, Claude Code, no SaaS: Adapt planning-with-files hash attestation for snapshot drift detection: [[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)]

### KB6 Produce next-session context

What it does: Generates handoff document for next Claude session.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|---|---|---|---|---|
|Restore context from planning files|S4a [[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)]|Read `task_plan.md`, `progress.md`, `findings.md` before continuing.|Low|Low|Medium|No|Yes|

Best option for solo operator, Claude Code, no SaaS: Use planning-with-files restore loop as next-session handoff: [[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)]

---

### PD1 Score priority

What it does: Assigns numeric or ordinal priority value.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|---|---|---|---|---|
|Priority enum + sort value|S3b [[https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js)]|Map high/medium/low to 3/2/1 and sort deterministically.|Low|Medium|Medium|Yes|Yes|

Best option for solo operator, Claude Code, no SaaS: Use Task Master priority-value mapping, extend to Apex numeric scale if needed: [[https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js)]

### PD2 Score urgency

What it does: Assesses time-sensitivity separately from priority.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|---|---|---|---|---|
|No substantiated public pattern found|No substantiated source|None fetched with separate urgency model distinct from priority/due date.|Low|Low|Medium|No|Yes|

Best option for solo operator, Claude Code, no SaaS: No direct public pattern found; implement as a small Apex-specific Markdown/YAML field contract, not copied from a source.

### PD3 Compute unlock depth

What it does: Counts items unblocked when this one completes.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|---|---|---|---|---|
|Reverse dependency graph|S1b [[https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md)]|Derive reverse edges from `depends_on` arrays; count reachable descendants.|Low|Medium|High|Yes|Yes|

Best option for solo operator, Claude Code, no SaaS: Use CCPM dependency arrays and add reverse graph traversal: [[https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md)]

### PD4 Synthesize focus recommendation

What it does: Produces ranked focus list with reasoning.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|---|---|---|---|---|
|Next-task plus explanation|S3b [[https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js)]|Deterministic eligibility/ranking; LLM adds concise reasoning.|Medium|Medium|High|Yes|Yes|

Best option for solo operator, Claude Code, no SaaS: Use deterministic candidate ordering from Task Master and let Claude explain the final ranked list: [[https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js)]

### PD5 Validate with operator

What it does: Requires human gate before any state mutation is written.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|---|---|---|---|---|
|Human input / guardrail gate|S8a [[https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md](https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md)]|Expected output and guardrail pattern; human input before finalizing.|Low|Low|Low|No|Yes|

Best option for solo operator, Claude Code, no SaaS: Use CrewAI’s human-input/guardrail pattern as a Markdown operator gate: [[https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md](https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md)]

### PD6 Feed planning layer

What it does: Hands ranked context to daily planning skill.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|---|---|---|---|---|
|Planning file handoff|S4a [[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)]|Persist plan/progress/findings as readable context for next planning invocation.|Low|Low|Medium|No|Yes|

Best option for solo operator, Claude Code, no SaaS: Use planning-with-files as the handoff substrate for PreCap-style daily planning: [[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)]

---

## 4. Sub-skill Clustering

### Q1. Natural clusters

|Cluster|Processes|Shared trigger|Shared files read|Shared files written|Shared execution context|
|---|---|---|---|---|---|
|Intake + capture|PM1, KB1|New project/session material appears|raw notes, prior progress|project capture, progress log|Pure Claude Skill|
|Decomposition + dependency graph|PM2, PM3, PD3|Project needs breakdown or dependency analysis|project capture, tasks|task files, dependency map|Skill + Python graph helper|
|Execution state + blockers|PM5, PM6, PM7|Work item state changes|task/card files, narrative logs|updated status, blocker/stall report|Skill + scan helper|
|Next action + focus|PM4, PD1, PD2, PD4|Operator asks what to do next|registry, dependency map, scores|ranked focus packet|Python ranking + Claude reasoning|
|KB maintenance|KB2, KB3, KB4, KB5|Session recap/state update|progress, entity files, snapshot|deltas, entity pages, index, drift report|Skill + Python index/drift helper|
|Handoff/planning|KB6, PD5, PD6, PM8|Planning layer needs compact context|registry, progress, focus packet|next-session context, operator validation|Pure Skill; scripts optional|

### Q2. Implementation type per cluster

|Cluster|Pure SKILL.md?|Script required?|Script language|Best source base|Required adaptation|
|---|--:|--:|---|---|---|
|Intake + capture|Yes|No|None|S2b, S4a|Convert task fields into Apex project/session fields|
|Decomposition + dependency graph|Partial|Yes|Python|S1b, S3b|Add `unlocks` reverse graph and circular validation|
|Execution state + blockers|Partial|Yes|Python|S5a, S1c|Scan cards/tasks for blocked/stale status|
|Next action + focus|No|Yes|Python|S3b|Extend priority sort with urgency/unlock-depth|
|KB maintenance|Partial|Yes|Python|S6a, S6b, S4a|Add Apex entity schema and drift snapshot format|
|Handoff/planning|Yes|Maybe|Python optional|S4a, S7a|Keep v1 Markdown handoff; escalate only if long-running state is needed|

### Q3. Gaps

|Process|Gap|Closest source|What must be built from scratch|
|---|---|---|---|
|PD2|No fetched source separates urgency from priority as an independent scoring dimension.|S3b|Apex urgency field contract and scoring rule.|
|PM7|Stall detection is not directly implemented in fetched files.|S5a|Stale-progress scan over timestamps/status/narrative.|
|KB5|Drift detection source is attestation/tamper detection, not semantic state drift.|S4a|Snapshot comparison between last validated state and current state.|

---

## 5. Final Summary Table

|Process ID|Process name|Best source|Mechanism|Needs script|Copy type|Priority rank|
|---|---|---|---|---|---|--:|
|PM4|Compute next action|[[https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js)]|Dependency-satisfied candidate filter + priority sort|Yes|ADAPT|1|
|PM8|Generate work registry|[[https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py](https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py)]|Markdown/frontmatter scan and index rebuild|Yes|ADAPT|2|
|PM3|Assign dependencies|[[https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md)]|`depends_on`, `parallel`, `conflicts_with` graph|Yes|ADAPT|3|
|PM5|Detect blockers|[[https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md](https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md)]|`blocked_by` semantics|Yes|ADAPT|4|
|PD4|Synthesize focus recommendation|[[https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js)]|Deterministic ranked candidates plus explanation|Yes|ADAPT|5|
|PD3|Compute unlock depth|[[https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md)]|Reverse dependency traversal|Yes|ADAPT|6|
|KB4|Rebuild index|[[https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py](https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py)]|Python index regeneration|Yes|ADAPT|7|
|KB5|Detect drift|[[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)]|Snapshot/hash comparison|Yes|CONCEPT|8|
|PM6|Update status|[[https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts](https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts)]|Typed status update fields|Maybe|ADAPT|9|
|PD1|Score priority|[[https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js)]|Priority values for sorting|Yes|ADAPT|10|
|PM7|Detect stall|[[https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md](https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md)]|Narrative timestamps and stale scan|Yes|CONCEPT|11|
|KB3|Maintain entity files|[[https://github.com/alirezarezvani/claude-skills/blob/main/engineering/llm-wiki/skills/llm-wiki/SKILL.md](https://github.com/alirezarezvani/claude-skills/blob/main/engineering/llm-wiki/skills/llm-wiki/SKILL.md)]|Persistent entity/concept page maintenance|Maybe|CONCEPT|12|
|KB6|Produce next-session context|[[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)]|Read plan/progress/findings on resume|No|FULL|13|
|PD6|Feed planning layer|[[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)]|File-based handoff into next planning loop|No|FULL|14|
|KB1|Write session progress|[[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)]|`progress.md` session log|No|FULL|15|
|KB2|Extract state deltas|[[https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md](https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md)]|Expected-output contract for deltas|No|ADAPT|16|
|PM2|Decompose project|[[https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md)]|Epic-to-task decomposition rules|No|ADAPT|17|
|PD5|Validate with operator|[[https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md](https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md)]|Human-input/guardrail gate|No|ADAPT|18|
|PD2|Score urgency|No substantiated source|custom|No|CONCEPT|19|
|PM1|Capture project|[[https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts](https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts)]|Compact typed Markdown capture contract|No|ADAPT|27|