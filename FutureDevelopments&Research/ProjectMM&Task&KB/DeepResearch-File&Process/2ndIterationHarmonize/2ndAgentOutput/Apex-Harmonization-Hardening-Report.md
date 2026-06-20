# Apex Harmonization Hardening Report

## 0. Verdict

PARTIAL – The initial scaffold (decisions, field schema, task template, scripts and skill stubs) exists in the repository, but missing live dependencies and several script defects prevent the system from being production‑ready.

## 1. Authority basis

|Source|Role|Status|
|---|---|---|
|ProThinkingGPT_Harmonization_v1.md|Primary authority defining the 20‑process option table and the evidence matrix used to derive H1–H7 and the high‑priority source list|Present and referenced![](https://chatgpt.com/backend-api/estuary/content?id=file_00000000a4447243b976e91800fb60c8&ts=494964&p=fs&cid=1&sig=60091a6da30975b78158373b61ccaf93a02792010c9a19f87246b02bf3c2eb37&v=0)|
|APEX HARMONIZATION — AGENT MODE INIT DOCUMENT v2.md|Establishes construction sequence, guardrails, locked decisions (H1–H7), and source mapping|Present and referenced![](https://chatgpt.com/backend-api/estuary/content?id=file_00000000a4447243b976e91800fb60c8&ts=494964&p=fs&cid=1&sig=60091a6da30975b78158373b61ccaf93a02792010c9a19f87246b02bf3c2eb37&v=0)|
|HandoverAfterFirstWorkflow.md|Describes what was built in the first workflow, expected script behaviour, and known caveats|Present and referenced![](https://chatgpt.com/backend-api/estuary/content?id=file_00000000a4447243b976e91800fb60c8&ts=494964&p=fs&cid=1&sig=60091a6da30975b78158373b61ccaf93a02792010c9a19f87246b02bf3c2eb37&v=0)|
|2ndAgentWorkflow.md (Agent Workflow Prompt + Operator Guidance)|Restates the mission, locked decisions, guardrails and phased execution steps for this session|Present and referenced![](https://chatgpt.com/backend-api/estuary/content?id=file_00000000a4447243b976e91800fb60c8&ts=494964&p=fs&cid=1&sig=60091a6da30975b78158373b61ccaf93a02792010c9a19f87246b02bf3c2eb37&v=0)|
|Status Update — Apex Harmonization After First Workflow|Intended to provide a status report after the first workflow|**Missing** – rely on the handover document for context|

## 2. Verified repo scaffold

|Path|Exists|SHA|Role|Status|
|---|---|---|---|---|
|apex-meta/harmonization/decisions.md|YES|fa2e06a10f…|Locks the H1–H7 decisions and records source IDs and copy types|Matches H1–H7 values; needs update only if decisions change|
|apex-meta/harmonization/field-schema.md|YES|8938e22d46…|Defines canonical task fields and their types|Covers core fields but may need additions (effort, epic) in later iterations|
|apex-meta/harmonization/task-template.md|YES|4882b45908…|Provides a markdown task template with front‑matter and body sections|Matches the schema; further examples could be added|
|scripts/find_next_task.py|YES|581b70e3cf…|Filters tasks by dependency satisfaction and ranks by priority/dependency count/ID|Contains nondeterministic hash fallback and includes done/deferred tasks; needs hardening|
|scripts/show_blocked.py|YES|8c99d195b3…|Reports tasks whose dependencies are missing or not done|Needs to distinguish missing vs. incomplete dependencies and produce deterministic ordering|
|scripts/update_index.py|YES|f887a2a4be…|Builds apex‑meta/registry/index.md from epics and handoff files|Lacks explicit file paths in the table and may not support full dry‑run semantics|
|scripts/stall_detect.py|YES|db2529d306…|Detects stalled tasks based on progress logs|Progress log format unclear; parsing logic may be fragile|
|scripts/drift_check.py|YES|fb0cf8ad71…|Compares file scan with registry index to detect missing/orphan files|Parses table header rows as tasks and infers file names from IDs instead of using explicit paths|
|.claude/skills/apex-plan/SKILL.md|YES|dbfbc5a78a…|Stub skill for cluster A (planning)|Lacks YAML front‑matter, exact inputs/outputs, numbered procedure, and validation behaviour|
|.claude/skills/apex-sync/SKILL.md|YES|e15e9ca4a2…|Stub skill for cluster B (sync) calling scripts|Needs proper skill structure with triggers, boundaries, supporting files, and validation|
|.claude/skills/apex-session/SKILL.md|YES|a926dcdea6…|Stub skill for cluster C (session) controlling mutations|Needs full skill contract with confirmation gate and handoff behaviour|
|.claude/skills/project-kb-manager/SKILL.md|YES|6e7b52425e…|Unrelated KB manager skill from the repo|Not part of harmonization but available for reference|

## 3. Missing or unverified expected files

|Expected path|Status|Impact|Decision needed|
|---|---|---|---|
|.claude/skills/status-merge/SKILL.md|Missing|Live skill expected by the init document; compatibility cannot be verified|Provide or confirm correct path or treat as blocker|
|.claude/skills/flow-recap/SKILL.md|Missing|Required to ensure new skills remain compatible with flow recap inputs|Provide or confirm correct path or treat as blocker|
|.claude/skills/PrecapNextDay/SKILL.md|Missing|Handover document references PrecapNextDay system; compatibility unknown|Provide or confirm correct path or treat as blocker|
|Status Update — Apex Harmonization After First Workflow|Missing|Could contain status information about the first workflow’s results|Proceed without it or locate alternative summary|

## 4. Defect ledger

|ID|Severity|File|Defect|Evidence|Minimal fix|Blocks next step?|
|---|---|---|---|---|---|---|
|D1|High|scripts/find_next_task.py|Uses Python’s built‑in `hash()` fallback for task ID when non‑numeric, leading to nondeterministic ordering; includes tasks with status `done` and `deferred` in the actionable set|Observed in script code; inconsistent rankings and includes completed tasks|Remove hash fallback; derive ID from filename or front‑matter; exclude `done` and `deferred` statuses; require deterministic sort|Yes – ranking must be deterministic before validation|
|D2|High|scripts/show_blocked.py|Does not distinguish between missing dependencies and dependencies not yet done; output ordering may depend on Python hash|Identified by comparing with Kanban `show_blocked.sh` expectations|Parse dependencies, check existence vs status separately; sort deterministically by task ID|Yes|
|D3|Medium|scripts/update_index.py|Does not include explicit file paths in the index; may not honour `--dry-run` correctly; sorts tasks by Python hash of ID|Based on initial script review and Handover guidance|Include relative file path for each task; ensure `--dry-run` writes nothing; use deterministic sort (e.g., by updated date then ID)|Yes|
|D4|High|scripts/drift_check.py|Parses Markdown table header/separator rows as tasks; infers file names from ID rather than using explicit paths|Caused false orphan entries when scanning index|Skip header/separator rows; parse explicit path column when available; do not infer filenames|Yes|
|D5|Medium|scripts/stall_detect.py|Lacks clear specification of `progress.md` format; regex may fail if format changes|Observed from script code; no schema defined|Define expected `progress.md` structure; implement deterministic parsing and detection of unchanged tasks across sessions|Yes|
|D6|Medium|.claude/skills/apex-plan/SKILL.md|Missing YAML front‑matter, trigger descriptions, inputs/outputs, boundaries, supporting file references, procedure and validation|Stub file only; not deployable|Upgrade to full SKILL.md according to skill specification|No – can be addressed after script hardening|
|D7|Medium|.claude/skills/apex-sync/SKILL.md|Lacks full skill structure and boundaries; no YAML front‑matter; triggers not clearly enumerated|Stub file; cannot enforce read‑only behaviour yet|Redraft with proper triggers, calls to hardened scripts, boundaries and validation|No|
|D8|Medium|.claude/skills/apex-session/SKILL.md|Stub lacking detailed session control, confirmation gate, and handoff section management|Not ready for operator use|Add front‑matter, triggers, procedure, and delta proposal logic; ensure H6 handoff sections|No|

## 5. H1–H7 compliance

|Decision|Verified?|Evidence|Defects|
|---|---|---|---|
|**H1 – Status enum:** `open`, `in‑progress`, `blocked`, `done`, `deferred`|YES|decisions.md lists these values; no other status values found|None|
|**H2 – Base path:** `apex-meta/`|YES|All scaffold files are under `apex-meta/` and `scripts/` as specified|None|
|**H3 – Dependency field:** `depends_on`|PARTIAL|field‑schema.md uses `depends_on`; scripts parse this field|`parallel` and `conflicts_with` fields appear in schema but are not used by scripts; verifying their handling in scripts remains TBD|
|**H4 – Script language:** Python only|YES|All scripts are Python files|None|
|**H5 – Clusters:** A_PLAN, B_SYNC, C_SESSION|PARTIAL|Skill stubs exist for each cluster, but they lack full structure and enforcement of script policies|Need to upgrade skills to enforce script policies and operator gates|
|**H6 – Handoff format:** `task_plan.md`, `findings.md`, `progress.md`, `next‑session.md`|NO|Handoff directory exists but is empty; scripts for handoff management (apex‑session) incomplete|Need to implement apex‑session behaviour and ensure files and sections are created|
|**H7 – Priority/urgency weights:** priority high=3, medium=2, low=1; urgency = days until due or 999|PARTIAL|`find_next_task.py` sorts by priority but uses Python hash for ID; urgency is not currently computed|Must incorporate due‑date into next‑task ranking and remove hash fallback|

## 6. Script validation plan

|Script|Static check|Runtime check|Fixture check|Expected result|
|---|---|---|---|---|
|**find_next_task.py**|Review code for deterministic sorting, proper exclusion of `done`/`deferred`, correct dependency evaluation|Run script against sample tasks; ensure consistent output across runs|Use fixture tasks (IDs 1–3 with dependencies and statuses)|Task 2 is actionable and appears top; Task 3 does not appear|
|**show_blocked.py**|Confirm detection of missing vs non‑done dependencies; deterministic ordering|Run script on fixture tasks; verify blocked output|Fixture tasks where task 3 depends on task 2|Output lists task 3 blocked by 2|
|**update_index.py**|Ensure file paths included and `--dry-run` option works|Run with dry‑run on fixture directory; confirm no file written|Use fixture tasks and handoff files|Index lists each task and epic with correct relative paths|
|**drift_check.py**|Ensure header/separator lines ignored; explicit path column read|Run on fixture index to ensure no false orphan entries|Use fixture index with explicit paths|Reports no drift after index rebuild|
|**stall_detect.py**|Confirm progress log format handled; parsing deterministic|Run with sample progress logs and sessions|Create fixture progress.md with sequential session entries|Identify stalled tasks correctly|

## 7. Skill upgrade readiness

|Skill|Current status|Missing pieces|Upgrade priority|
|---|---|---|---|
|**apex-plan**|Scaffold stub with basic description|Needs YAML front‑matter, trigger mapping, input/output definitions, boundaries, numbered procedure, completion gate and failure modes|Medium – upgrade after script hardening|
|**apex-sync**|Scaffold stub referencing scripts|Needs front‑matter, enumeration of triggers (`what’s next`, `any blockers`, `stall check`, `rebuild registry`, `sync state`, `drift report`), call sequence, boundaries (read‑only), numbered procedure, validation|High – must be upgraded after script fixes to ensure safe sync operations|
|**apex-session**|Scaffold stub with minimal content|Needs front‑matter, triggers (`log session`, `update status`, etc.), operator confirmation gate, handoff file creation, delta proposal logic, session recovery, validation|High – essential for controlling mutations and handoff behaviour|

## 8. Next action sequence

|Order|Action|Target path|Requires CONFIRM|Validation|
|---|---|---|---|---|
|1|Create **validation-fixtures.md** documenting fixture file tree and test scenarios|apex-meta/harmonization/validation-fixtures.md|YES|File exists with sections: purpose, fixture tree, fixture tasks, expected script behaviour, no‑write validation|
|2|Harden **scripts/find_next_task.py** to remove nondeterministic hashing and exclude completed/deferred tasks|scripts/find_next_task.py|YES|Fetch current SHA; generate full replacement; verify with fixture; ensure deterministic output|
|3|Harden **scripts/show_blocked.py** to distinguish missing vs incomplete dependencies and sort deterministically|scripts/show_blocked.py|YES|Full replacement; test on fixture tasks|
|4|Harden **scripts/update_index.py** to include explicit file paths, honour dry‑run, and sort deterministically|scripts/update_index.py|YES|Full replacement; verify no file created during dry‑run|
|5|Harden **scripts/drift_check.py** to read explicit paths and skip header rows|scripts/drift_check.py|YES|Full replacement; test with fixture index|
|6|Harden **scripts/stall_detect.py** after defining progress.md format and deterministic parsing|scripts/stall_detect.py|YES|Full replacement; verify with fixture progress logs|
|7|Create **skill-upgrade-plan.md** summarising current skills and specifying upgrade tasks for apex-sync, apex-session, and apex-plan|apex-meta/harmonization/skill-upgrade-plan.md|YES|Document upgrade requirements and sequence; finalised after script hardening|
|8|Upgrade **apex-sync/SKILL.md** with proper structure, triggers, calls, boundaries, procedure, and validation|.claude/skills/apex-sync/SKILL.md|YES|Full replacement; verify compatibility with live skills and H1–H7|
|9|Upgrade **apex-session/SKILL.md** with operator gate and handoff management|.claude/skills/apex-session/SKILL.md|YES|Full replacement; verify handoff files and sections|
|10|Upgrade **apex-plan/SKILL.md** to full planning skill spec|.claude/skills/apex-plan/SKILL.md|YES|Full replacement; ensure no script calls and operator gate for file creation|
|11|Perform final validation and produce final report summarising compliance with H1–H7, script behaviour, skill readiness, and remaining blockers|apex-meta/harmonization/final-validation.md (optional)||