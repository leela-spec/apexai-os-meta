# Phase 2 Complete — URL/Label → Local Repo Path Map v0.1

I continued from the **saved Phase 1 project resource** and reopened the real project/repo files. Phase 1 explicitly handed off to **Phase 2 — URL / label → local mirrored path map**, with rules to avoid public GitHub/web, treat public URLs only as identities, resolve sources under `source-knowledge/ProjectRepos/`, and record path drift.

## 1. Authority basis reloaded

**Source ledger authority:** `ProThinkingGPT_Harmonization_v1.md` defines S1a–S9b and what each source is used for.

**Local-path lockfile:** `APEX HARMONIZATION — AGENT MODE INIT DOCUMENT_v2.md` says local files must be read before adapting and provides expected local paths for S1a, S1b, S1c, S2b, S3c, S4a, S5b, S6b, S6a, and S8a.

---

## 2. Frozen source map

|ID|Source identity|Expected / resolved local repo path|Phase 2 status|Notes|
|---|---|---|---|---|
|**S1a**|CCPM `SKILL.md`|`source-knowledge/ProjectRepos/ccpm-main/skill/ccpm/SKILL.md`|**RESOLVED**|Expected by lockfile; fetched successfully. Defines CCPM as spec-driven project management and PRD → Epic → Issues → agents → shipped code.|
|**S1b**|CCPM `structure.md`|`source-knowledge/ProjectRepos/ccpm-main/skill/ccpm/references/structure.md`|**RESOLVED**|Expected by lockfile; fetched successfully. It explicitly converts an epic into numbered task files with dependency/parallel metadata.|
|**S1c**|CCPM `track.md`|`source-knowledge/ProjectRepos/ccpm-main/skill/ccpm/references/track.md`|**RESOLVED**|Expected by lockfile; fetched successfully. It contains the script-first tracking rule, but original source is Bash-oriented and must be adapted to Python.|
|**S2a**|Backlog example task|`source-knowledge/ProjectRepos/backlog-main/Backlog.md-main/backlog/tasks/back-200 - Add-Claude-Code-integration-with-workflow-commands-during-init.md`|**RESOLVED / NESTED**|Not listed in the init local-path subset, but ProThinking requires it. Fetched successfully at nested `Backlog.md-main` path.|
|**S2b**|Backlog `types/index.ts`|Corrected: `source-knowledge/ProjectRepos/backlog-main/Backlog.md-main/src/types/index.ts`|**RESOLVED WITH PATH DRIFT**|Lockfile path omits `Backlog.md-main`; direct lockfile path failed, nested path succeeds.|
|**S2c**|Backlog parser|`source-knowledge/ProjectRepos/backlog-main/Backlog.md-main/src/markdown/parser.ts`|**RESOLVED / NESTED**|Fetched successfully at nested path. Parser imports task types and structured-section managers.|
|**S3a**|Task Master task schema|`source-knowledge/ProjectRepos/claude-task-master-main/docs/task-structure.md`|**RESOLVED**|Fetched successfully; defines `tasks.json` task fields.|
|**S3b**|Task Master manager module|`source-knowledge/ProjectRepos/claude-task-master-main/scripts/modules/task-manager.js`|**RESOLVED**|Fetched successfully; re-exports `findNextTask`.|
|**S3c**|Task Master `find-next-task.js`|`source-knowledge/ProjectRepos/claude-task-master-main/scripts/modules/task-manager/find-next-task.js`|**RESOLVED**|Expected by lockfile; fetched successfully. It returns eligible next work items and exposes status/priority fields.|
|**S4a**|planning-with-files `SKILL.md`|Corrected: `source-knowledge/ProjectRepos/planning-with-files-master/.kiro/skills/planning-with-files/SKILL.md`|**RESOLVED WITH PATH DRIFT**|Lockfile expected root `SKILL.md`; direct root path failed. Correct `.kiro/skills/...` path fetched successfully.|
|**S4b**|planning-with-files quickstart|`source-knowledge/ProjectRepos/planning-with-files-master/docs/quickstart.md`|**RESOLVED**|Fetched successfully.|
|**S5a**|Kanban `SKILL.md`|Expected family: `source-knowledge/ProjectRepos/kanban-skill-master/skills/kanban-ai/SKILL.md`|**SOURCE_PATH_MISSING**|ProThinking requires Kanban skill/card evidence, but the expected `kanban-skill-master` local path did not resolve in this pass.|
|**S5b**|Kanban `show_blocked.sh`|Expected: `source-knowledge/ProjectRepos/kanban-skill-master/skills/kanban-ai/scripts/show_blocked.sh`|**SOURCE_PATH_MISSING**|Lockfile path did not resolve; record as missing before Phase 3.|
|**S5c**|Kanban `list_all_cards.sh`|Expected sibling of S5b|**SOURCE_PATH_MISSING**|ProThinking requires it, but no verified local path found in this pass.|
|**S6a**|llm-wiki `SKILL.md`|Corrected substitute: `source-knowledge/ProjectRepos/llm-wiki-skill-main/llm-wiki/SKILL.md`|**RESOLVED WITH PATH DRIFT**|Lockfile points to `llm-wiki-main/`; actual resolved skill is under `llm-wiki-skill-main`.|
|**S6b**|llm-wiki `update-index.py`|Expected: `source-knowledge/ProjectRepos/llm-wiki-main/scripts/update-index.py`|**SOURCE_PATH_MISSING / SUBSTITUTE WEAK**|Expected exact file did not resolve. A nearby llm-wiki Python script exists (`scaffold.py`), but it bootstraps structure; it is not equivalent to `update-index.py`.|
|**S7a**|OpenClaw taskflow|Expected identity: `openclaw/openclaw/skills/taskflow/SKILL.md`|**SOURCE_PATH_MISSING**|ProThinking lists it, but no verified local mirror path was found in this pass.|
|**S8a**|CrewAI `design-task/SKILL.md`|Expected missing; substitute: `source-knowledge/ProjectRepos/crewAI-main/lib/crewai/src/crewai/task.py`|**RESOLVED WITH SUBSTITUTE**|Lockfile expected `crewAI-main/skills/design-task/SKILL.md`; that path did not resolve. `task.py` contains the task contract fields: `description`, `expected_output`, `context`, `output_file`, structured outputs, and tools.|
|**S8b**|CrewAI getting-started skill|Expected identity: `crewAIInc/skills/getting-started/SKILL.md`|**SOURCE_PATH_MISSING**|ProThinking requires this for YAML/config and handoff evidence, but no verified local path was found in this pass.|
|**S9a**|Hermes `skills_hub.py`|Expected identity: `NousResearch/hermes-agent/tools/skills_hub.py`|**SOURCE_PATH_MISSING**|Governance-only source; no verified local mirror path found in this pass.|
|**S9b**|Hermes `skills_guard.py`|Expected identity: `NousResearch/hermes-agent/tools/skills_guard.py`|**SOURCE_PATH_MISSING**|Governance-only source; no verified local mirror path found in this pass.|

---

## 3. PM2 control sample verdict

**PM2 control sample: PASS WITH ONE SUBSTITUTE**

|Required PM2 source family|Status|Evidence|
|---|---|---|
|**CCPM decomposition**|**PASS**|`structure.md` resolves and states it converts epics into numbered task files with dependency and parallelization metadata.|
|**Backlog task/subtask schema**|**PASS WITH PATH DRIFT**|Correct path is nested under `Backlog.md-main`; fetched `types/index.ts` successfully.|
|**CrewAI task-contract/operator-gate evidence**|**PASS WITH SUBSTITUTE**|Expected skill path missing; local `task.py` supplies task-contract fields including `description`, `expected_output`, `context`, and `output_file`.|

**Control-sample interpretation:** PM2 can proceed into Phase 3 mechanism extraction, but CrewAI must be recorded as **substitute-source evidence**, not as the originally named `design-task/SKILL.md`.

---

## 4. Path drift ledger

|Drift ID|Source|Expected path|Resolved path / outcome|Severity|
|---|---|---|---|---|
|**D1**|S2b Backlog types|`source-knowledge/ProjectRepos/backlog-main/src/types/index.ts`|`source-knowledge/ProjectRepos/backlog-main/Backlog.md-main/src/types/index.ts`|**P1 — corrected path required**|
|**D2**|S4a planning-with-files|`source-knowledge/ProjectRepos/planning-with-files-master/SKILL.md`|`source-knowledge/ProjectRepos/planning-with-files-master/.kiro/skills/planning-with-files/SKILL.md`|**P1 — corrected path required**|
|**D3**|S5a/S5b/S5c Kanban|`kanban-skill-master/...`|Not found in repo connector tests|**P0 for PM5/PD2 unless substitute found**|
|**D4**|S6b llm-wiki update-index|`llm-wiki-main/scripts/update-index.py`|Not found; only weak llm-wiki script substitute identified|**P0 for PM8/KB4/KB5 until resolved**|
|**D5**|S6a llm-wiki skill|`llm-wiki-main/ find SKILL.md`|`llm-wiki-skill-main/llm-wiki/SKILL.md`|**P1 — corrected path required**|
|**D6**|S8a CrewAI design-task|`crewAI-main/skills/design-task/SKILL.md`|`crewAI-main/lib/crewai/src/crewai/task.py`|**P1 — substitute accepted for contract fields, not skill format**|
|**D7**|S7a OpenClaw|not locally specified in lockfile|no verified local mirror path found|**P2 — concept source only**|
|**D8**|S9a/S9b Hermes governance|not locally specified in lockfile|no verified local mirror path found|**P2 — governance-only, not core PM/KB/PD**|

---

## 5. Phase 2 verdict

**PHASE_2_PARTIAL_PASS_WITH_PATH_DRIFT**

Resolved enough to proceed into **Phase 3 — File-read ledger**, but not enough to claim all source identities are locally mirrored.

### Ready for Phase 3 immediately

- S1a/S1b/S1c
- S2a/S2b/S2c
- S3a/S3b/S3c
- S4a/S4b
- S6a
- S8a substitute

### Must be handled as missing or unresolved in Phase 3

- S5a/S5b/S5c Kanban
- S6b exact `update-index.py`
- S7a OpenClaw
- S8b CrewAI getting-started
- S9a/S9b Hermes governance

### Next phase entry condition

Phase 3 can begin with a **file-read ledger for resolved paths only**, while missing sources are carried as `SOURCE_PATH_MISSING` until a repo-local path is proven.