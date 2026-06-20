# Source Ledger

|Source ID|File URL|Fetch status|Evidence extracted|Limitations|Used for|
|---|---|--:|---|---|---|
|S1a|[[https://github.com/automazeio/ccpm/blob/main/skill/ccpm/SKILL.md](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/SKILL.md)]|OK|`SKILL.md` command workflow for PRD/project/epic/task flow; five-phase lifecycle; script-first rule for deterministic status, next, blocker, validation, and tracking commands.|File is an instruction entrypoint, not the script implementations themselves.|PM2, PM3, PM4, PM5, PM6, PM8, PD4|
|S1b|[[https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md)]|OK|Epic-to-task decomposition; task frontmatter; dependency fields `depends_on`, `parallel`, `conflicts_with`; dependency validation and circular dependency warning.|Supports dependency structure; not a full project database schema.|PM2, PM3, PM4, PM5, PM8, PD3|
|S1c|[[https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/track.md](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/track.md)]|OK|Script-first tracking pattern; status, standup, next, blocked, and validate scripts; fallback behavior when scripts fail.|Script names and expected behavior extracted; individual bash script files were not separately fetched.|PM4, PM5, PM6, PM8, KB5, PD4|
|S2a|[[https://github.com/MrLesk/Backlog.md/blob/main/backlog/tasks/back-200%20-%20Add-Claude-Code-integration-with-workflow-commands-during-init.md](https://github.com/MrLesk/Backlog.md/blob/main/backlog/tasks/back-200%20-%20Add-Claude-Code-integration-with-workflow-commands-during-init.md)]|OK|Real Markdown task file with YAML fields: `id`, `title`, `status`, `assignee`, `created_date`, `updated_date`, `labels`, `dependencies`, `priority`; acceptance criteria.|Single example task; schema completion comes from S2b/S2c.|PM1, PM6, PM8, PD5|
|S2b|[[https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts](https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts)]|OK|Task interfaces for create/update fields, status, priority, dependencies, references, acceptance criteria, definition-of-done, parent task, subtasks, branch, ordinal, source, status-change hook.|TypeScript contract only; persistence implementation not fully mapped.|PM1, PM6, PM8, KB2, PD5|
|S2c|[[https://github.com/MrLesk/Backlog.md/blob/main/src/markdown/parser.ts](https://github.com/MrLesk/Backlog.md/blob/main/src/markdown/parser.ts)]|OK|Markdown parser maps frontmatter/body sections into task objects; validates priority values; extracts acceptance criteria, DoD, dates, labels, dependencies, subtasks, and update fields.|Parser evidence supports extraction/update mechanics, not planning policy.|PM1, PM6, KB2, PD5|
|S3a|[[https://github.com/eyaltoledano/claude-task-master/blob/main/docs/task-structure.md](https://github.com/eyaltoledano/claude-task-master/blob/main/docs/task-structure.md)]|OK|JSON task schema; valid statuses and priorities; dependency model; next-task selection documented as pending/in-progress with satisfied dependencies, then priority, dependency count, ID.|Next-task algorithm is documented here; exact implementation is S3c.|PM3, PM4, PD1, PD3, PD4|
|S3b|[[https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager.js](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager.js)]|OK|Module boundary exporting `findNextTask` and related task-manager functions.|Thin re-export / aggregation file; substantive algorithm is S3c.|PM4, PD4|
|S3c|[[https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js)]|OK|Deterministic next-task algorithm: builds completed-ID set, filters eligible subtasks/tasks by status and dependency satisfaction, sorts by priority, dependency count, and ID.|Does not compute reverse unlock depth; only uses dependency count in ordering.|PM3, PM4, PM5, PD1, PD3, PD4|
|S4a|[[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)]|OK|File-based planning loop with `task_plan.md`, `findings.md`, `progress.md`; session recovery; re-read before decisions; progress/error persistence; helper scripts for session init/catchup/completion/attestation.|Instruction package references helper scripts; not all helper scripts were fetched.|PM7, KB1, KB2, KB5, KB6, PD6|
|S4b|[[https://github.com/OthmanAdi/planning-with-files/blob/master/docs/quickstart.md](https://github.com/OthmanAdi/planning-with-files/blob/master/docs/quickstart.md)]|OK|Quickstart for creating and updating `task_plan.md`, `findings.md`, `progress.md`; isolated plan directories; handoff file; completion verification; re-read rule.|Quickstart documentation rather than code.|KB1, KB2, KB5, KB6, PD6|
|S5a|[[https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md](https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md)]|OK|Card YAML fields; lanes/statuses; `priority`; `blocked_by`; due date; transition rule requiring blockers done before moving to doing; helper script list.|Card helper script internals only fetched for S5b/S5c.|PM3, PM5, PM6, PM7, PD2|
|S5b|[[https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/scripts/show_blocked.sh](https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/scripts/show_blocked.sh)]|OK|Bash blocker listing: scans Markdown cards, extracts `blocked_by`, `id`, `status`, title, and prints blocked cards.|Simple grep/sed parser; no YAML parser.|PM5|
|S5c|[[https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/scripts/list_all_cards.sh](https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/scripts/list_all_cards.sh)]|OK|Bash registry export: scans Markdown cards and emits pipe-delimited `id|status|blocked_by|
|S6a|[[https://github.com/alirezarezvani/claude-skills/blob/main/engineering/llm-wiki/skills/llm-wiki/SKILL.md](https://github.com/alirezarezvani/claude-skills/blob/main/engineering/llm-wiki/skills/llm-wiki/SKILL.md)]|OK|Knowledge-base pattern: immutable `raw/`, LLM-owned `wiki/`, `index.md`, `log.md`, `entities/`, `concepts/`, `sources/`, comparisons, synthesis; ingest/query/lint operations; iron rule not to edit raw source.|High-level skill file; detailed reference files not fetched.|KB3, KB4, KB5, PM8|
|S6b|[[https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py](https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py)]|OK|Python index rebuild: scans wiki Markdown recursively, parses frontmatter, groups by type, sorts by updated date, generates `index.md`, supports `--dry-run`.|Depends on local config helpers not fully fetched.|PM8, KB4, KB5|
|S7a|[[https://github.com/openclaw/openclaw/blob/main/skills/taskflow/SKILL.md](https://github.com/openclaw/openclaw/blob/main/skills/taskflow/SKILL.md)]|OK|Durable task state pattern: flow identity, owner session, `currentStep`, `stateJson`, `waitJson`, linked child tasks, waiting/resume/finish/fail/cancel states, revision checks.|Used only as local persisted-state evidence; no external runtime adoption implied.|PM7, KB6, PD6|
|S8a|[[https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md](https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md)]|OK|Task contract fields: `description`, `expected_output`, `agent`, `context`, `output_pydantic`, `output_json`, `output_file`, `human_input`, guardrails, callbacks, variable interpolation, task checklist.|Framework-specific examples adapted only as file-contract / review-gate evidence.|KB2, PD4, PD5|
|S8b|[[https://github.com/crewAIInc/skills/blob/main/skills/getting-started/SKILL.md](https://github.com/crewAIInc/skills/blob/main/skills/getting-started/SKILL.md)]|OK|YAML config pattern using `agents.yaml` and `tasks.yaml`; `expected_output`; `output_file`; explicit context dependencies; human feedback example; scaffold/write pattern.|Used only for task-contract and handoff evidence, not runtime selection.|KB2, PD5, PD6|
|S9a|[[https://github.com/NousResearch/hermes-agent/blob/main/tools/skills_hub.py](https://github.com/NousResearch/hermes-agent/blob/main/tools/skills_hub.py)]|OK|Skill metadata model; source adapter interface; GitHub source adapter; trust level fields; lock file/provenance; quarantine, audit log, taps, index cache; safe install path validation.|Governance support only; not core PM/KB/PD process implementation.|PD5, governance|
|S9b|[[https://github.com/NousResearch/hermes-agent/blob/main/tools/skills_guard.py](https://github.com/NousResearch/hermes-agent/blob/main/tools/skills_guard.py)]|OK|Trust-aware static scan: trusted/community/builtin levels; install policy; `ScanResult`; findings; threat pattern scan; install allow/block/confirm logic; content hash.|Security scanner, not Apex state process logic.|PD5, governance|

# Evidence Matrix

|Evidence category|Best supporting source(s)|Concrete mechanism|Script boundary|
|---|---|---|---|
|Markdown/YAML task contract|[[https://github.com/MrLesk/Backlog.md/blob/main/backlog/tasks/back-200%20-%20Add-Claude-Code-integration-with-workflow-commands-during-init.md](https://github.com/MrLesk/Backlog.md/blob/main/backlog/tasks/back-200%20-%20Add-Claude-Code-integration-with-workflow-commands-during-init.md)]; [[https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts](https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts)]; [[https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md](https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md)]|YAML frontmatter or typed task fields for title, status, priority, dependencies, dates, acceptance criteria, done criteria, blocked-by, lane/status.|No for writing one task/card; Maybe when enforcing typed parsing or bulk updates.|
|JSON task schema|[[https://github.com/eyaltoledano/claude-task-master/blob/main/docs/task-structure.md](https://github.com/eyaltoledano/claude-task-master/blob/main/docs/task-structure.md)]|`tasks.json` schema with id/title/description/status/dependencies/priority/details/test strategy/subtasks.|No for contract authoring; Yes for machine validation or traversal.|
|Dependency graph|[[https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md)]; [[https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js)]; [[https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts](https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts)]|`depends_on`, `parallel`, `conflicts_with`, dependencies arrays, satisfied-dependency filtering.|Yes for dependency resolution/traversal.|
|Blocker detection|[[https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md](https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md)]; [[https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/scripts/show_blocked.sh](https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/scripts/show_blocked.sh)]; [[https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/track.md](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/track.md)]|`blocked_by` field; transition rule blocks moving to doing until blockers done; script lists blocked cards; CCPM has blocked-status command.|Yes for exact multi-file blocker detection.|
|Next-action computation|[[https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js)]; [[https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/track.md](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/track.md)]|Eligible item = pending/in-progress and dependencies satisfied; sorted by priority, dependency count, ID; `next.sh` style tracking command.|Yes.|
|Status update|[[https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts](https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts)]; [[https://github.com/MrLesk/Backlog.md/blob/main/src/markdown/parser.ts](https://github.com/MrLesk/Backlog.md/blob/main/src/markdown/parser.ts)]; [[https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md](https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md)]|`TaskUpdateInput`; parser maps frontmatter/body; card move semantics across backlog/todo/doing/done/archive.|No for single-file state mutation; Maybe for batch propagation.|
|Stall detection|[[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)]; [[https://github.com/openclaw/openclaw/blob/main/skills/taskflow/SKILL.md](https://github.com/openclaw/openclaw/blob/main/skills/taskflow/SKILL.md)]|Progress log plus session catchup; persisted `currentStep`, `stateJson`, `waitJson`, `lastEventAt`-style child task timestamps.|Yes for stale-state detection across sessions.|
|Work registry/index|[[https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/track.md](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/track.md)]; [[https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/scripts/list_all_cards.sh](https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/scripts/list_all_cards.sh)]; [[https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py](https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py)]|Status/standup scripts; card export; recursive Markdown scan and index generation.|Yes for exact multi-file registry.|
|Session progress capture|[[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)]; [[https://github.com/OthmanAdi/planning-with-files/blob/master/docs/quickstart.md](https://github.com/OthmanAdi/planning-with-files/blob/master/docs/quickstart.md)]|`progress.md` captures work phases, errors, commands, outcomes; re-read-before-decide loop.|No.|
|State delta extraction|[[https://github.com/OthmanAdi/planning-with-files/blob/master/docs/quickstart.md](https://github.com/OthmanAdi/planning-with-files/blob/master/docs/quickstart.md)]; [[https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md](https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md)]|Narrative session notes become findings, progress notes, expected-output-shaped structured results.|No.|
|Entity file maintenance|[[https://github.com/alirezarezvani/claude-skills/blob/main/engineering/llm-wiki/skills/llm-wiki/SKILL.md](https://github.com/alirezarezvani/claude-skills/blob/main/engineering/llm-wiki/skills/llm-wiki/SKILL.md)]|Immutable raw source plus LLM-owned wiki pages under entities/concepts/sources; ingest updates 10–15 relevant pages and cross-references.|No for one file; Maybe for multi-file patch validation.|
|Index rebuild|[[https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py](https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py)]|Recursively scan Markdown files, parse frontmatter, group by type, sort by updated date, write `index.md`; dry-run supported.|Yes.|
|Drift detection|[[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)]; [[https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py](https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py)]; [[https://github.com/NousResearch/hermes-agent/blob/main/tools/skills_guard.py](https://github.com/NousResearch/hermes-agent/blob/main/tools/skills_guard.py)]|Session catchup, file attestation/hash-style integrity, index regeneration, content hash for file bundles.|Yes for exact drift comparison.|
|Next-session handoff|[[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)]; [[https://github.com/OthmanAdi/planning-with-files/blob/master/docs/quickstart.md](https://github.com/OthmanAdi/planning-with-files/blob/master/docs/quickstart.md)]; [[https://github.com/openclaw/openclaw/blob/main/skills/taskflow/SKILL.md](https://github.com/openclaw/openclaw/blob/main/skills/taskflow/SKILL.md)]|Read `task_plan.md`, `findings.md`, `progress.md`; write handoff file; persisted `currentStep/stateJson/waitJson` for resume.|No for handoff writing; Maybe for automatic context assembly.|
|Priority scoring|[[https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js)]; [[https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts](https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts)]|Priority enum/high-medium-low; deterministic priority weights high=3, medium=2, low=1.|Yes for deterministic scoring/ranking; No for manual assignment.|
|Urgency scoring|[[https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md](https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md)]|`due_date` field supports time-sensitivity; no fetched source provides numeric urgency scoring separate from priority.|Yes if converting dates to numeric urgency; otherwise No for recording date.|
|Unlock-depth scoring|[[https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js)]; [[https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md)]|Dependency arrays and satisfied-dependency traversal are present; exact reverse unlock-depth count is not implemented in fetched files.|Yes.|
|Focus recommendation|[[https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js)]; [[https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/track.md](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/track.md)]; [[https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md](https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md)]|Next-task algorithm plus expected-output task design can produce ranked focus list with rationale.|Yes for deterministic rank; No for narrative rationale.|
|Human validation gate|[[https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md](https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md)]; [[https://github.com/crewAIInc/skills/blob/main/skills/getting-started/SKILL.md](https://github.com/crewAIInc/skills/blob/main/skills/getting-started/SKILL.md)]; [[https://github.com/NousResearch/hermes-agent/blob/main/tools/skills_guard.py](https://github.com/NousResearch/hermes-agent/blob/main/tools/skills_guard.py)]|`human_input=True` pauses before finalizing; human feedback emits approved/needs_revision; trust scanner can block or require confirmation.|No for operator review gate; Yes only for automated scan/guard.|
|Planning-layer handoff|[[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)]; [[https://github.com/OthmanAdi/planning-with-files/blob/master/docs/quickstart.md](https://github.com/OthmanAdi/planning-with-files/blob/master/docs/quickstart.md)]; [[https://github.com/openclaw/openclaw/blob/main/skills/taskflow/SKILL.md](https://github.com/openclaw/openclaw/blob/main/skills/taskflow/SKILL.md)]|`task_plan.md` plus handoff file; current step/state/wait bags preserve context; planning files are read before decision.|No for writing handoff; Maybe for automatic context pack assembly.|

# Process Option Tables for all 20 processes

### PM1 Capture project

What it does: Records project name, goal, domain, current state, and success criteria as structured local files.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|--:|--:|--:|---|---|
|Markdown task/project contract|[[https://github.com/MrLesk/Backlog.md/blob/main/backlog/tasks/back-200%20-%20Add-Claude-Code-integration-with-workflow-commands-during-init.md](https://github.com/MrLesk/Backlog.md/blob/main/backlog/tasks/back-200%20-%20Add-Claude-Code-integration-with-workflow-commands-during-init.md)]; [[https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts](https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts)]|Use Backlog-style frontmatter/task fields plus `description`, acceptance criteria, DoD, dependencies, and priority as the capture container.|Low|Low|Low|No|Yes|
|Planning file intake|[[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)]|Start a `task_plan.md` and `findings.md` for the project; capture goal/state/success criteria in plan sections.|Low|Low|Low|No|Yes|
|Structured output task contract|[[https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md](https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md)]|Define `description` and `expected_output` for project capture; optionally write result to an output file.|Low|Low|Low|No|Yes|

Best option for solo operator, Claude Code, no SaaS: Backlog-style Markdown frontmatter is the closest low-cost capture pattern because it already stores status, priority, dependencies, acceptance criteria, and done criteria in local Markdown files [[https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts](https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts)].

### PM2 Decompose project

What it does: Breaks a project into epics, chunks, and tasks with explicit splitting rules.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|--:|--:|--:|---|---|
|CCPM PRD/epic/task decomposition|[[https://github.com/automazeio/ccpm/blob/main/skill/ccpm/SKILL.md](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/SKILL.md)]; [[https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md)]|Follow Plan → Structure flow; convert project/PRD intent into numbered task files with parallelization and splitting rules.|Medium|Low|Medium|No|Yes|
|Focused task contract|[[https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md](https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md)]|Enforce one objective per task and explicit expected output, then chain tasks through context dependencies.|Low|Low|Low|No|Yes|
|Backlog parent/subtask model|[[https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts](https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts)]|Use `parentTaskId`, `subtasks`, ordinal, priority, dependencies, and acceptance criteria to represent decomposition.|Medium|Low|Medium|No|Yes|

Best option for solo operator, Claude Code, no SaaS: CCPM’s Structure phase is the best-supported decomposition pattern because it directly converts epics into numbered task files with dependency and parallel metadata [[https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md)].

### PM3 Assign dependencies

What it does: Builds `depends_on` and `unlocks` relationships between tasks.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|--:|--:|--:|---|---|
|CCPM dependency fields|[[https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md)]|Use `depends_on`, `parallel`, and `conflicts_with`; validate against circular dependencies and invalid references.|Medium|Medium|High|Yes|Yes|
|Task Master dependency arrays|[[https://github.com/eyaltoledano/claude-task-master/blob/main/docs/task-structure.md](https://github.com/eyaltoledano/claude-task-master/blob/main/docs/task-structure.md)]; [[https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js)]|Store dependencies as ID arrays; traverse completed IDs to test eligibility.|Medium|Medium|High|Yes|Yes|
|Kanban `blocked_by` contract|[[https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md](https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md)]|Model dependency as blocker relation; prevent lane transition until blocking cards are done.|Low|Low|Medium|Maybe|Yes|

Best option for solo operator, Claude Code, no SaaS: CCPM’s `depends_on`/`parallel`/`conflicts_with` fields give the closest local-file dependency model, with script validation needed for exact graph checks [[https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md)].

### PM4 Compute next action

What it does: Determines the next executable action from current state and dependency satisfaction.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|--:|--:|--:|---|---|
|Task Master next-task algorithm|[[https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js)]|Filter pending/in-progress tasks and subtasks by satisfied dependencies; sort by priority, dependency count, and ID.|Low|Medium|High|Yes|Yes|
|CCPM next command|[[https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/track.md](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/track.md)]|Script-first `next.sh` pattern selects next work instead of relying on LLM guesswork.|Low|Medium|High|Yes|Yes|
|Planning files re-read loop|[[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)]|Re-read `task_plan.md`, `findings.md`, and `progress.md` before deciding; use plan state to propose next step.|Medium|Low|Medium|No|Yes|

Best option for solo operator, Claude Code, no SaaS: Task Master’s `find-next-task.js` is the strongest exact implementation because it already performs dependency satisfaction and priority sorting locally [[https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js)].

### PM5 Detect blockers

What it does: Identifies items that cannot proceed because dependencies, blockers, or prerequisites are unresolved.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|--:|--:|--:|---|---|
|Kanban blocked-card script|[[https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/scripts/show_blocked.sh](https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/scripts/show_blocked.sh)]; [[https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md](https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md)]|Scan Markdown cards for nonempty `blocked_by` and print blocked cards with blocker IDs.|Low|Medium|Medium|Yes|Yes|
|CCPM blocked command|[[https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/track.md](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/track.md)]|Script-first `blocked.sh` pattern reports blocked tasks across local project files.|Low|Medium|Medium|Yes|Yes|
|Task Master dependency eligibility|[[https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js)]|Treat unsatisfied dependencies as non-eligible tasks; inverse of next-action computation.|Low|Medium|High|Yes|Yes|

Best option for solo operator, Claude Code, no SaaS: The Kanban `blocked_by` plus `show_blocked.sh` pattern is the simplest substantiated blocker detector for local Markdown files [[https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/scripts/show_blocked.sh](https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/scripts/show_blocked.sh)].

### PM6 Update status

What it does: Marks items complete, active, blocked, archived, or otherwise updated after work finishes.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|--:|--:|--:|---|---|
|Backlog task update fields|[[https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts](https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts)]; [[https://github.com/MrLesk/Backlog.md/blob/main/src/markdown/parser.ts](https://github.com/MrLesk/Backlog.md/blob/main/src/markdown/parser.ts)]|Use `TaskUpdateInput` and parser-backed Markdown updates for status, priority, dependencies, acceptance criteria, and final summary.|Low|Medium|Medium|Maybe|Yes|
|Kanban lane movement|[[https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md](https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md)]|Move card between backlog/todo/doing/done/archive; verify blockers before moving to doing.|Low|Low|Low|No|Yes|
|CCPM status scripts|[[https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/track.md](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/track.md)]|Script-first status/progress commands update and report task state.|Low|Medium|Medium|Maybe|Yes|

Best option for solo operator, Claude Code, no SaaS: Backlog’s `TaskUpdateInput` plus Markdown parser is the best status-update fit when updates must preserve structured task fields [[https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts](https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts)].

### PM7 Detect stall

What it does: Finds items with no meaningful progress across multiple sessions.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|--:|--:|--:|---|---|
|Planning progress/catchup|[[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)]; [[https://github.com/OthmanAdi/planning-with-files/blob/master/docs/quickstart.md](https://github.com/OthmanAdi/planning-with-files/blob/master/docs/quickstart.md)]|Compare `progress.md` entries, plan phase changes, and catchup state across sessions.|Medium|Medium|High|Yes|Yes|
|Persisted step/state bag|[[https://github.com/openclaw/openclaw/blob/main/skills/taskflow/SKILL.md](https://github.com/openclaw/openclaw/blob/main/skills/taskflow/SKILL.md)]|Track `currentStep`, `stateJson`, `waitJson`, waiting/blocked state, and child task linkage for resumption.|Medium|Medium|High|Yes|Yes|
|Kanban unchanged-lane check|[[https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md](https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md)]|Use card status, due date, narrative, and blocked state as stale-work evidence.|Low|Medium|Medium|Yes|Yes|

Best option for solo operator, Claude Code, no SaaS: Planning-with-files gives the closest local-session stall substrate because it persists plan, findings, progress, errors, and session catchup artifacts [[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)].

### PM8 Generate work registry

What it does: Produces a compact index of all project state.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|--:|--:|--:|---|---|
|Wiki index rebuild|[[https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py](https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py)]; [[https://github.com/alirezarezvani/claude-skills/blob/main/engineering/llm-wiki/skills/llm-wiki/SKILL.md](https://github.com/alirezarezvani/claude-skills/blob/main/engineering/llm-wiki/skills/llm-wiki/SKILL.md)]|Recursively scan Markdown files, parse frontmatter, group by type, sort by updated date, and generate `index.md`.|Low|Medium|High|Yes|Yes|
|Kanban all-cards export|[[https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/scripts/list_all_cards.sh](https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/scripts/list_all_cards.sh)]|Emit compact pipe-delimited registry from Markdown cards: `id|status|blocked_by|title`, sorted by ID.|Low|Medium|
|CCPM status/standup scripts|[[https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/track.md](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/track.md)]|Script-first status and standup summaries over local PM files.|Low|Medium|Medium|Yes|Yes|

Best option for solo operator, Claude Code, no SaaS: `update-index.py` is the most reusable registry pattern because it already scans local Markdown, parses frontmatter, groups entries, and writes an index [[https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py](https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py)].

### KB1 Write session progress

What it does: Captures what happened during a work session.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|--:|--:|--:|---|---|
|Planning `progress.md`|[[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)]; [[https://github.com/OthmanAdi/planning-with-files/blob/master/docs/quickstart.md](https://github.com/OthmanAdi/planning-with-files/blob/master/docs/quickstart.md)]|Append phase work, commands, outcomes, errors, and completion notes to `progress.md`.|Low|Low|Low|No|Yes|
|Kanban narrative append|[[https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md](https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md)]|Append `## Narrative` notes to card without erasing durable context or outcome.|Low|Low|Low|No|Yes|
|Wiki log pattern|[[https://github.com/alirezarezvani/claude-skills/blob/main/engineering/llm-wiki/skills/llm-wiki/SKILL.md](https://github.com/alirezarezvani/claude-skills/blob/main/engineering/llm-wiki/skills/llm-wiki/SKILL.md)]|Append timeline entry to `wiki/log.md` during ingest/update.|Low|Low|Low|No|Yes|

Best option for solo operator, Claude Code, no SaaS: Planning-with-files `progress.md` is the direct session-progress pattern with explicit update-after-work behavior [[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)].

### KB2 Extract state deltas

What it does: Converts session narrative into structured field changes.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|--:|--:|--:|---|---|
|Planning findings/progress split|[[https://github.com/OthmanAdi/planning-with-files/blob/master/docs/quickstart.md](https://github.com/OthmanAdi/planning-with-files/blob/master/docs/quickstart.md)]; [[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)]|Extract decisions, errors, risks, and work outcomes from narrative into `findings.md` and `progress.md`.|Medium|Low|Medium|No|Yes|
|Backlog parser-backed fields|[[https://github.com/MrLesk/Backlog.md/blob/main/src/markdown/parser.ts](https://github.com/MrLesk/Backlog.md/blob/main/src/markdown/parser.ts)]; [[https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts](https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts)]|Map Markdown body sections and frontmatter into structured task properties.|Low|Medium|Medium|Maybe|Yes|
|Expected-output contract|[[https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md](https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md)]|Use `expected_output` to force the delta into a typed/structured result shape before downstream write.|Low|Low|Low|No|Yes|

Best option for solo operator, Claude Code, no SaaS: Planning-with-files is the best pure-instruction fit because it explicitly separates findings, progress, and errors without requiring custom code [[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)].

### KB3 Maintain entity files

What it does: Applies deltas to Markdown entity files without losing existing data.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|--:|--:|--:|---|---|
|LLM-owned wiki pages|[[https://github.com/alirezarezvani/claude-skills/blob/main/engineering/llm-wiki/skills/llm-wiki/SKILL.md](https://github.com/alirezarezvani/claude-skills/blob/main/engineering/llm-wiki/skills/llm-wiki/SKILL.md)]|Keep immutable raw files separate from LLM-owned `wiki/entities`, `wiki/concepts`, and `wiki/sources`; update pages and cross-references incrementally.|Medium|Low|Medium|No|Yes|
|Kanban narrative preservation|[[https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md](https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md)]|Append narrative without deleting existing card data; preserve durable source material and outcome.|Low|Low|Low|No|Yes|
|Backlog parser and update contract|[[https://github.com/MrLesk/Backlog.md/blob/main/src/markdown/parser.ts](https://github.com/MrLesk/Backlog.md/blob/main/src/markdown/parser.ts)]; [[https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts](https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts)]|Parse known fields and update structured task sections without treating the whole file as freeform text.|Medium|Medium|Medium|Maybe|Yes|

Best option for solo operator, Claude Code, no SaaS: The LLM Wiki source/wiki split is the strongest Markdown entity-maintenance pattern because it explicitly separates immutable input from maintained knowledge pages [[https://github.com/alirezarezvani/claude-skills/blob/main/engineering/llm-wiki/skills/llm-wiki/SKILL.md](https://github.com/alirezarezvani/claude-skills/blob/main/engineering/llm-wiki/skills/llm-wiki/SKILL.md)].

### KB4 Rebuild index

What it does: Regenerates the registry after state changes.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|--:|--:|--:|---|---|
|Python frontmatter index rebuild|[[https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py](https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py)]|Scan all Markdown pages, parse frontmatter, group by type, sort by updated date, write `index.md`, or dry-run.|Low|Medium|High|Yes|Yes|
|Kanban compact card export|[[https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/scripts/list_all_cards.sh](https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/scripts/list_all_cards.sh)]|Scan card files and emit sorted pipe-delimited index.|Low|Medium|Medium|Yes|Yes|
|CCPM status summary|[[https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/track.md](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/track.md)]|Use status/standup scripts to compute current work summary from local files.|Low|Medium|Medium|Yes|Yes|

Best option for solo operator, Claude Code, no SaaS: `update-index.py` is the clearest reusable rebuild mechanism for Markdown knowledge/project registries [[https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py](https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py)].

### KB5 Detect drift

What it does: Compares current state against the last session snapshot.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|--:|--:|--:|---|---|
|Planning session catchup and attestation|[[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)]|Re-read planning files, use catchup behavior, and apply hash/attestation-style checks before continuing.|Medium|Medium|High|Yes|Yes|
|Index dry-run comparison|[[https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py](https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py)]|Regenerate index in `--dry-run`, compare generated registry against stored index.|Low|Medium|High|Yes|Yes|
|Content hash pattern|[[https://github.com/NousResearch/hermes-agent/blob/main/tools/skills_guard.py](https://github.com/NousResearch/hermes-agent/blob/main/tools/skills_guard.py)]|Compute content hash across files to detect changes or integrity drift.|Low|Medium|High|Yes|Yes|

Best option for solo operator, Claude Code, no SaaS: The safest drift fit is a small Python comparator modeled on `update-index.py` dry-run generation and content-hash checking [[https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py](https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py)].

### KB6 Produce next-session context

What it does: Generates a handoff document for the next Claude session.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|--:|--:|--:|---|---|
|Planning handoff files|[[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)]; [[https://github.com/OthmanAdi/planning-with-files/blob/master/docs/quickstart.md](https://github.com/OthmanAdi/planning-with-files/blob/master/docs/quickstart.md)]|Read plan/findings/progress; write long-running-topic handoff with details, risk, rollback, and PR links.|Medium|Low|Medium|No|Yes|
|Persisted state bag|[[https://github.com/openclaw/openclaw/blob/main/skills/taskflow/SKILL.md](https://github.com/openclaw/openclaw/blob/main/skills/taskflow/SKILL.md)]|Store minimal `currentStep`, `stateJson`, and `waitJson` needed to resume.|Low|Low|Medium|No|Yes|
|Wiki index-first context|[[https://github.com/alirezarezvani/claude-skills/blob/main/engineering/llm-wiki/skills/llm-wiki/SKILL.md](https://github.com/alirezarezvani/claude-skills/blob/main/engineering/llm-wiki/skills/llm-wiki/SKILL.md)]|Query flow reads `index.md` first, then drills into relevant pages; good answers are filed back.|Medium|Low|Medium|No|Yes|

Best option for solo operator, Claude Code, no SaaS: Planning-with-files is the best handoff source because it already defines session restore through plan/findings/progress plus explicit handoff files [[https://github.com/OthmanAdi/planning-with-files/blob/master/docs/quickstart.md](https://github.com/OthmanAdi/planning-with-files/blob/master/docs/quickstart.md)].

### PD1 Score priority

What it does: Assigns a priority value to tasks or project items.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|--:|--:|--:|---|---|
|Task Master priority weights|[[https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js)]|Map `high`, `medium`, `low` to numeric weights 3/2/1 for sorting.|Low|Medium|Medium|Yes|Yes|
|Backlog priority enum|[[https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts](https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts)]; [[https://github.com/MrLesk/Backlog.md/blob/main/src/markdown/parser.ts](https://github.com/MrLesk/Backlog.md/blob/main/src/markdown/parser.ts)]|Store validated `priority` as high/medium/low in task contract.|Low|Low|Low|No|Yes|
|Expected-output scoring field|[[https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md](https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md)]|Require priority score/rationale in expected output; operator validates before write.|Low|Low|Low|No|Yes|

Best option for solo operator, Claude Code, no SaaS: Task Master’s priority weighting is the closest deterministic priority scoring pattern, but Apex numeric scale would be an adapted mapping [[https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js)].

### PD2 Score urgency

What it does: Assesses time-sensitivity separately from priority.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|--:|--:|--:|---|---|
|Kanban due-date field|[[https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md](https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md)]|Store `due_date` separately from `priority`, then compute urgency from date distance.|Low|Medium|Medium|Yes|Yes|
|Backlog date fields|[[https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts](https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts)]|Use created/updated dates and optional fields as time context; no explicit urgency scorer.|Low|Low|Low|No|Yes|
|Expected-output urgency assessment|[[https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md](https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md)]|Include time-sensitivity score and rationale in expected output for operator review.|Low|Low|Low|No|Yes|

Best option for solo operator, Claude Code, no SaaS: Kanban’s `due_date` field is the closest substantiated urgency substrate, but numeric urgency scoring must be added as local logic [[https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md](https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md)].

### PD3 Compute unlock depth

What it does: Counts how many downstream items become unblocked when one item completes.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|--:|--:|--:|---|---|
|Task Master dependency traversal base|[[https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js)]|Reuse completed-ID/dependency-satisfaction traversal and invert dependency edges to count downstream unlocks.|Low|Medium|High|Yes|Yes|
|CCPM dependency fields|[[https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md)]|Use `depends_on` relations as graph edges; build reverse dependency count.|Low|Medium|High|Yes|Yes|
|Kanban blocked-by inversion|[[https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md](https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md)]|Count cards whose `blocked_by` contains the completed card ID.|Low|Medium|High|Yes|Yes|

Best option for solo operator, Claude Code, no SaaS: Task Master provides the strongest traversal base, but unlock-depth itself is a custom reverse-dependency computation [[https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js)].

### PD4 Synthesize focus recommendation

What it does: Produces a ranked focus list with reasoning.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|--:|--:|--:|---|---|
|Task Master next-task ranking|[[https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js)]; [[https://github.com/eyaltoledano/claude-task-master/blob/main/docs/task-structure.md](https://github.com/eyaltoledano/claude-task-master/blob/main/docs/task-structure.md)]|Rank eligible tasks by dependency satisfaction, priority, dependency count, and ID; add reasoning text separately.|Medium|Medium|High|Yes|Yes|
|CCPM next/status scripts|[[https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/track.md](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/track.md)]|Use status/next/blocked scripts as deterministic substrate, then synthesize rationale.|Medium|Medium|High|Yes|Yes|
|Structured recommendation task|[[https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md](https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md)]|Define expected output as prioritized list with rationale, estimated effort, and expected impact.|Low|Low|Medium|No|Yes|

Best option for solo operator, Claude Code, no SaaS: Combine Task Master’s deterministic ranking substrate with a structured recommendation output, with rank computed by script and rationale drafted by instruction [[https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js)].

### PD5 Validate with operator

What it does: Adds a human gate before any state mutation is written.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|--:|--:|--:|---|---|
|Human review task gate|[[https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md](https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md)]|`human_input=True` pauses for human feedback before marking task complete.|Low|Low|Low|No|Yes|
|Human feedback approval branch|[[https://github.com/crewAIInc/skills/blob/main/skills/getting-started/SKILL.md](https://github.com/crewAIInc/skills/blob/main/skills/getting-started/SKILL.md)]|Human feedback step emits approved/needs_revision before publishing or revising.|Low|Low|Medium|No|Yes|
|Trust/guard confirmation|[[https://github.com/NousResearch/hermes-agent/blob/main/tools/skills_guard.py](https://github.com/NousResearch/hermes-agent/blob/main/tools/skills_guard.py)]; [[https://github.com/NousResearch/hermes-agent/blob/main/tools/skills_hub.py](https://github.com/NousResearch/hermes-agent/blob/main/tools/skills_hub.py)]|Scan result and install policy can allow, block, or require confirmation before installing/mutating skill state.|Low|Medium|Medium|Maybe|Yes|

Best option for solo operator, Claude Code, no SaaS: CrewAI’s `human_input=True` is the cleanest public pattern for pausing before finalization, adapted as an operator validation gate [[https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md](https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md)].

### PD6 Feed planning layer

What it does: Hands ranked context to a daily planning skill or planning layer.

|Option|Source|Mechanism|Token cost|Maintenance cost|Complexity|Needs script?|Portable?|
|---|---|---|--:|--:|--:|---|---|
|Planning file handoff|[[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)]; [[https://github.com/OthmanAdi/planning-with-files/blob/master/docs/quickstart.md](https://github.com/OthmanAdi/planning-with-files/blob/master/docs/quickstart.md)]|Write/read `task_plan.md`, `findings.md`, `progress.md`, and handoff file before next decision.|Medium|Low|Medium|No|Yes|
|Persisted resume state|[[https://github.com/openclaw/openclaw/blob/main/skills/taskflow/SKILL.md](https://github.com/openclaw/openclaw/blob/main/skills/taskflow/SKILL.md)]|Store `currentStep`, `stateJson`, and `waitJson` as compact context for resuming the next step.|Low|Low|Medium|No|Yes|
|Structured output file|[[https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md](https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md)]|Use `output_file` plus expected-output contract to write a ranked planning input artifact.|Low|Low|Low|No|Yes|

Best option for solo operator, Claude Code, no SaaS: Planning-with-files is the strongest handoff fit because the next decision loop explicitly reads plan/findings/progress before proceeding [[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)].

# Sub-skill Clustering

### Q1. Natural clusters

|Cluster|Processes|Shared trigger|Shared files read|Shared files written|Shared execution context|
|---|---|---|---|---|---|
|Intake and task contract|PM1, PM6, KB2, PD5|New project/task, status mutation, or operator-reviewed delta|Existing task/project Markdown, previous status, session narrative|Task/project Markdown, updated frontmatter, review flags|Claude Code local file edit with operator review|
|Decomposition and dependency engine|PM2, PM3, PM4, PM5, PD3, PD4|Need to split work, assign dependencies, find next action, or detect blockers|Task registry, dependency fields, blocker fields, statuses, priorities|Task files, dependency fields, next-action/focus output, blocker report|Claude Code plus small deterministic Python/bash scripts|
|Session memory and handoff|PM7, KB1, KB5, KB6, PD6|End/start of session, resumed work, stale context, daily planning handoff|`task_plan.md`, `findings.md`, `progress.md`, handoff files, snapshots|`progress.md`, `findings.md`, next-session context, drift/stall flags|Pure `SKILL.md` for capture/handoff; script for stale/drift comparison|
|Knowledge entity maintenance|KB3, KB4, PM8|State changed, entity page changed, registry/index needs refresh|Raw/source Markdown, entity/concept/source pages, frontmatter|Updated entity pages, `index.md`, log/registry|Markdown update workflow plus Python index rebuild|
|Product scoring and recommendation|PD1, PD2, PD3, PD4, PD6|Need ranked focus context for planning|Priority, due date, dependency graph, blockers, status, progress|Numeric scores, ranked focus list, planning handoff artifact|Python for scoring/ranking; instruction layer for rationale|
|Governance and validation|PD5, KB5|Before mutation/install or after suspected drift|Proposed mutation, scan result, existing files, hashes/snapshots|Approval/needs-revision/block flags, audit note|Operator gate plus optional deterministic guard script|

### Q2. Implementation type per cluster

|Cluster|Pure SKILL.md?|Script required?|Script language|Best source base|Required adaptation|
|---|--:|--:|---|---|---|
|Intake and task contract|Yes|No|None|[[https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts](https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts)]|Convert task fields into Apex project/task/status contract.|
|Decomposition and dependency engine|Partial|Yes|Python|[[https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js)]|Rewrite traversal over Apex Markdown/YAML files; add reverse unlock count.|
|Session memory and handoff|Yes|Only for stall/drift|Python|[[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)]|Rename planning files and fields to Apex PM/KB/PD artifacts.|
|Knowledge entity maintenance|Partial|Yes for index rebuild|Python|[[https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py](https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py)]|Change page types and frontmatter keys to Apex entity/project status fields.|
|Product scoring and recommendation|Partial|Yes|Python|[[https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js)]|Add priority/urgency/unlock-depth scoring and produce ranked focus artifact.|
|Governance and validation|Yes for operator gate|Maybe for guard/hash|Python|[[https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md](https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md)]; [[https://github.com/NousResearch/hermes-agent/blob/main/tools/skills_guard.py](https://github.com/NousResearch/hermes-agent/blob/main/tools/skills_guard.py)]|Replace framework-specific `human_input=True` with explicit Claude Code operator checkpoint; optionally add scan/hash guard.|

### Q3. Gaps

|Process|Gap|Closest source|What must be built from scratch|
|---|---|---|---|
|PM7|No fetched source provides exact Apex “no progress across multiple sessions” stale detector.|[[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)]|Snapshot comparator that checks unchanged status/progress across session timestamps.|
|KB5|No fetched source directly compares Apex current state against last session snapshot.|[[https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py](https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py)]; [[https://github.com/NousResearch/hermes-agent/blob/main/tools/skills_guard.py](https://github.com/NousResearch/hermes-agent/blob/main/tools/skills_guard.py)]|Drift script that regenerates registry, hashes state, and compares against prior snapshot.|
|PD1|Numeric Apex priority scoring is not directly implemented; sources provide enum/ordinal priority.|[[https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js)]|Mapping from Apex priority scale to deterministic score.|
|PD2|No fetched source has separate numeric urgency scoring; only due-date fields exist.|[[https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md](https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md)]|Date-to-urgency scoring function and no-deadline policy.|
|PD3|No fetched source computes reverse unlock depth exactly.|[[https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js)]|Reverse dependency traversal and count of newly unblocked items.|

# Final Summary Table

|Process ID|Process name|Best source|Mechanism|Needs script|Copy type|Priority rank|
|---|---|---|---|---|---|--:|
|PM1|Capture project|[[https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts](https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts)]|Markdown/frontmatter project-task capture contract with status, priority, dependencies, criteria|No|ADAPT|27|
|PM2|Decompose project|[[https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md)]|Epic-to-task decomposition with task files and split/parallel metadata|No|ADAPT|9|
|PM3|Assign dependencies|[[https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md](https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md)]|`depends_on`, `parallel`, `conflicts_with` dependency fields plus validation|Yes|ADAPT|5|
|PM4|Compute next action|[[https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js)]|Filter eligible tasks by dependency satisfaction and sort by priority/dependency count/ID|Yes|ADAPT|1|
|PM5|Detect blockers|[[https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/scripts/show_blocked.sh](https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/scripts/show_blocked.sh)]|Scan local Markdown cards for nonempty `blocked_by`|Yes|FULL|2|
|PM6|Update status|[[https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts](https://github.com/MrLesk/Backlog.md/blob/main/src/types/index.ts)]|`TaskUpdateInput` plus structured status/frontmatter fields|Maybe|ADAPT|6|
|PM7|Detect stall|[[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)]|Compare progress/session artifacts across sessions; custom stale detector needed|Yes|CONCEPT|15|
|PM8|Generate work registry|[[https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py](https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py)]|Scan Markdown frontmatter and regenerate compact index|Yes|ADAPT|3|
|KB1|Write session progress|[[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)]|Write `progress.md` with session actions, errors, findings, outcomes|No|FULL|7|
|KB2|Extract state deltas|[[https://github.com/OthmanAdi/planning-with-files/blob/master/docs/quickstart.md](https://github.com/OthmanAdi/planning-with-files/blob/master/docs/quickstart.md)]|Convert narrative into findings/progress/delta sections|No|ADAPT|18|
|KB3|Maintain entity files|[[https://github.com/alirezarezvani/claude-skills/blob/main/engineering/llm-wiki/skills/llm-wiki/SKILL.md](https://github.com/alirezarezvani/claude-skills/blob/main/engineering/llm-wiki/skills/llm-wiki/SKILL.md)]|Maintain LLM-owned entity/concept/source Markdown while preserving immutable raw input|Maybe|ADAPT|10|
|KB4|Rebuild index|[[https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py](https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py)]|Recursively scan wiki pages and regenerate `index.md`|Yes|FULL|4|
|KB5|Detect drift|[[https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py](https://github.com/junbjnnn/llm-wiki/blob/main/scripts/update-index.py)]|Regenerate state/index and compare against prior snapshot|Yes|CONCEPT|14|
|KB6|Produce next-session context|[[https://github.com/OthmanAdi/planning-with-files/blob/master/docs/quickstart.md](https://github.com/OthmanAdi/planning-with-files/blob/master/docs/quickstart.md)]|Read plan/findings/progress and write handoff context|No|FULL|8|
|PD1|Score priority|[[https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js)]|Priority weighting adapted from high/medium/low to Apex numeric score|Yes|ADAPT|17|
|PD2|Score urgency|[[https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md](https://github.com/mattjoyce/kanban-skill/blob/master/skills/kanban-ai/SKILL.md)]|Use due date as urgency substrate; numeric urgency rule must be added|Yes|CONCEPT|19|
|PD3|Compute unlock depth|[[https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js)]|Reverse dependency traversal over existing dependency arrays|Yes|CONCEPT|16|
|PD4|Synthesize focus recommendation|[[https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js](https://github.com/eyaltoledano/claude-task-master/blob/main/scripts/modules/task-manager/find-next-task.js)]|Deterministic eligible-task ranking plus rationale output|Yes|ADAPT|11|
|PD5|Validate with operator|[[https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md](https://github.com/crewAIInc/skills/blob/main/skills/design-task/SKILL.md)]|Human review gate before finalizing state mutation|No|ADAPT|12|
|PD6|Feed planning layer|[[https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md](https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md)]|Handoff ranked context through planning files read by next session|No|FULL|13|