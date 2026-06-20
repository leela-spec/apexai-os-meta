DR_APEX_PM_KB_PD_Perp.md

File

DR_APEX_PM_KB_PD_Gem.md

File

DR_APEX_PM_KB_PD_GPT.md

File

ProThinkingGPT_Harmonization_v1.md

File

APEX HARMONIZATION — AGENT MODE INIT DOCUMENT_v2.md

File

Apex Harmonization — Agent Mode Workflow Phase 0 — Session Init (one-time, ~2 min) Paste into Agent Mode browser window: text AGENT MODE INIT — APEX HARMONIZATION CONSTRUCTION Repo: leela-spec/apexai-os-meta (clone via PAT) Research is complete. Do NOT re-read source repos. git clone https://<PAT>@github.com/leela-spec/apexai-os-meta.git cd apexai-os-meta All decisions are pre-locked. Your job is file generation only. Read and follow these decisions exactly — do not rediscover them: H1 STATUS ENUM: [open, in-progress, blocked, done, deferred] H2 BASE PATH: apex-meta/ H3 DEPENDENCY FIELD: depends_on (int array) H4 SCRIPT LANGUAGE: Python H5 CLUSTERS: A = PLAN → PM1, PM2, PM3, PD1, PD2, PD4 B = SYNC → PM4, PM5, PM7, PM8, KB4, KB5 C = SESSION → PM6, KB1, KB2, KB3, KB6, PD3, PD5, PD6 H6 HANDOFF FORMAT: task_plan.md + findings.md + progress.md + next-session.md H7 PRIORITY: high=3 / medium=2 / low=1; urgency = days-to-due-date normalized LIVE SKILLS — do not break: .claude/skills/status-merge/SKILL.md .claude/skills/flow-recap/SKILL.md .claude/skills/project-kb-manager/SKILL.md .claude/skills/PrecapNextDay/SKILL.md Gate rule: before writing ANY file, output delta proposal. Wait for CONFIRM. Phase 1 — Write decisions.md H1–H7 are pre-resolved. Paste: text Write apex-meta/harmonization/decisions.md - Use H1–H7 values from the init message verbatim - Include source evidence URLs per decision (from ProThinkingGPT_Harmonization_v1.md) - Validate: all 7 decisions present, YAML frontmatter with step:2 status:locked - Commit: git commit -m "APEX STEP 1 — decisions locked from ProThinking research" CONFIRM before writing. Phase 2 — Field Schema + Task Template Paste: text Write apex-meta/harmonization/field-schema.md and apex-meta/harmonization/task-template.md - Source: Backlog.md TaskInterface (S2b), CCPM structure.md (S1b), Task Master schema (S3a) - Fields: name, status(H1), created, updated, priority(H7), urgency(H7), depends_on(H3), parallel, conflicts_with, effort(XS/S/M/L/XL), epic, due_date, acceptance_criteria, definition_of_done - Mark each field: required | optional | computed - No invented fields — every field must appear in at least one source - Commit: git commit -m "APEX STEP 2 — field schema" CONFIRM before writing. Phase 3 — Python Scripts One script per agent turn. Paste each block individually. Script Source Copy type find_next_task.py Task Master S3c — dependency satisfaction + priority sort ADAPT (JS→Python) show_blocked.py Kanban show_blocked.sh (S5b) — rewritten Python ADAPT (Bash→Python) update_index.py llm-wiki S6b — adapt frontmatter keys to Apex FULL stall_detect.py Compare progress.md timestamps across sessions CUSTOM drift_check.py S6b dry-run + content hash pattern CUSTOM Script 3a: text Write scripts/find_next_task.py - Algorithm: port find-next-task.js (S3c) to Python over Apex Markdown/YAML files - Input: apex-meta/epics/**/*.md with H1 status and H3 depends_on fields - Output: stdout — ranked table (id | priority | dep_count | title) - Error handling: if file missing or frontmatter malformed, print warning and skip - Must NOT write any file or modify any status field Run it after writing. Show output. Fix any error before committing. CONFIRM before writing. Script 3b: text Write scripts/show_blocked.py - Port Kanban show_blocked.sh (S5b) from Bash to Python - Scan apex-meta/ for tasks where depends_on is nonempty and dependency status ≠ done - Output: stdout — blocked task list (id | blocked_by ids | title) - Must NOT write any file Run it after writing. Show output. Fix any error before committing. CONFIRM before writing. Script 3c: text Write scripts/update_index.py - Full copy of llm-wiki update-index.py (S6b) - Adapt: change page-type groups to Apex types (epic, task, handoff) - Output: apex-meta/registry/index.md - Must support --dry-run flag (no write, only report) Run with --dry-run after writing. Show output. Fix any error before committing. CONFIRM before writing. Script 3d: text Write scripts/stall_detect.py - Custom. Read apex-meta/handoff/progress.md, compare updated timestamps per task - Flag any task with no status change across 2+ consecutive session entries - Output: stdout — stalled task list (id | last_updated | sessions_stalled | title) - Must NOT write any file Run it after writing. Show output. Fix any error before committing. CONFIRM before writing. Script 3e: text Write scripts/drift_check.py - Custom. Run update_index.py --dry-run, compare result vs current apex-meta/registry/index.md - Report files present in scan but absent from index, and index entries with no matching file - Output: stdout — drift report (missing_from_index | orphan_in_index) - Must NOT write any file Run it after writing. Show output. Fix any error before committing. CONFIRM before writing. Phase 4 — SKILL Files (B → C → A) All scripts must be verified running before starting this phase. Cluster B — apex-sync (PM4, PM5, PM7, PM8, KB4, KB5): text Write .claude/skills/apex-sync/SKILL.md - Base: CCPM track.md pattern (S1c) — script-first rule - Triggers: "what's next" | "any blockers" | "stall check" | "rebuild registry" | "sync state" | "drift report" - Calls: find_next_task.py, show_blocked.py, update_index.py, stall_detect.py, drift_check.py - Rule: apex-sync NEVER writes task content — read and compute only - Validate: H1/H2/H3 compliance, live skills not broken CONFIRM before writing. Cluster C — apex-session (PM6, KB1, KB2, KB3, KB6, PD3, PD5, PD6): text Write .claude/skills/apex-session/SKILL.md - Base: planning-with-files SKILL.md (S4a) + crewAI human_input gate (S8a) - Triggers: "log session" | "update status" | "apply deltas" | "handoff" | "next session prep" | "operator approve" - Write-gate: ALL file mutations require delta proposal → operator types CONFIRM to apply - KB6 output: apex-meta/handoff/next-session.md using H6 section format - Validate: H1/H2/H3 compliance, live skills not broken CONFIRM before writing. Cluster A — apex-plan (PM1, PM2, PM3, PD1, PD2, PD4): text Write .claude/skills/apex-plan/SKILL.md - Base: CCPM structure.md (S1b) + Backlog task contract (S2b) - Triggers: "capture project" | "decompose" | "assign dependencies" | "score priority" | "new epic" | "focus recommendation" - No scripts — pure SKILL.md reasoning + file writes - Operator gate REQUIRED before creating any new epic or task file - Validate: H1/H2/H3 compliance, live skills not broken CONFIRM before writing. Phase 5 — Final Validation Run in terminal: bash python3 scripts/find_next_task.py python3 scripts/update_index.py --dry-run python3 scripts/show_blocked.py ls .claude/skills/ grep -r "open\|in-progress\|blocked\|done\|deferred" apex-meta/harmonization/decisions.md Then paste: text Run final validation — report YES/NO per line, fix any NO before closing: □ H1 enum used identically in all 3 SKILL files □ H2 paths consistent across decisions.md and all SKILL files □ H3 depends_on field name consistent everywhere □ apex-sync contains zero file write operations □ KB6 handoff format (H6 sections) present in apex-session □ status-merge and flow-recap inputs still satisfied (re-read both, confirm) □ PD5 CONFIRM gate present in apex-session AND apex-plan □ All 5 Python scripts execute without error

Worked for 13 Sekunden

I'm ready to begin the Apex Harmonization task sequence. Please provide the confirmation when you're ready for me to start Step 1—writing `decisions.md` with the locked H1–H7 values.

Continue

Worked for 2 Minuten

Here’s the proposed delta for **Step 1 (decisions.md)**:

- **Create the path** `apexai-os-meta/apex-meta/harmonization/` (if it doesn’t already exist).
- **Create a new file** `decisions.md` inside this directory with the following contents:
    1. **YAML front‑matter** at the top:
        
        ```
        ---step: 1status: lockedgenerated: 2026-06-19---
        ```
        
    2. **Seven sections (H1–H7)** using the exact wording from the INIT document, e.g.:
        - **H1 — STATUS ENUM**: list the statuses `[open, in‑progress, blocked, done, deferred]` exactly as stated in the INIT doc.
            - **Sources & evidence**: cite relevant sources from the ProThinking document, including S1b (local path `source‑knowledge/ProjectRepos/ccpm‑main/skill/ccpm/references/structure.md`, copy type **ADAPT**) and S2b (local path `source‑knowledge/ProjectRepos/backlog‑main/src/types/index.ts`, copy type **ADAPT**).
        - **H2 — FILE PATH CONVENTION**: reproduce the apex‑meta directory structure verbatim.
            - **Sources & evidence**: cite S1b and S4a (local path `source‑knowledge/ProjectRepos/planning‑with‑files‑master/SKILL.md`, copy type **FULL/CONCEPT**).
        - **H3 — DEPENDENCY FIELD**: include the definition of `depends_on` and its eligibility rule exactly as given.
            - **Sources & evidence**: cite S1b and S3c (local path `source‑knowledge/ProjectRepos/claude‑task‑master‑main/scripts/modules/task‑manager/find‑next‑task.js`, copy type **ADAPT**).
        - **H4 — SCRIPT LANGUAGE**: state that all deterministic operations must be in Python (no Bash/TypeScript/shell).
            - **Sources & evidence**: cite S6b (local path `source‑knowledge/ProjectRepos/llm‑wiki‑main/scripts/update‑index.py`, copy type **FULL**) and S3c.
        - **H5 — CLUSTER ASSIGNMENT**: reproduce the PLAN/SYNC/SESSION clusters and associated processes exactly as listed.
            - **Sources & evidence**: cite S1b and S4a; these establish the cluster definitions and their adaptation patterns.
        - **H6 — HANDOFF FORMAT**: reproduce the required handoff files and the mandatory sections for `next‑session.md` exactly as given.
            - **Sources & evidence**: cite S4a.
        - **H7 — PRIORITY + URGENCY**: list the priority levels (high, medium, low) and weights, explain the urgency score calculation using due dates, and note the fallback score when no due date is set.
            - **Sources & evidence**: cite S3c and S5b (local path `source‑knowledge/ProjectRepos/kanban‑skill‑master/skills/kanban‑ai/scripts/show_blocked.sh`, copy type **ADAPT**).
    3. **Citations**: Use the citation IDs from the INIT document (e.g., for H1, etc.) to support each decision and note the local file paths and copy types as described above.

Once confirmed, I will create this file, commit it with the message `APEX STEP 1 — decisions locked`, and proceed to the next phase. Let me know if everything looks correct or if you’d like any adjustments before I write the file.

Worked for 50 Sekunden

I see we’re moving into the broader ApexWithClaude context, which comes with additional design and guidance documents (e.g., skill prompt flow guidance, project status overview skill, ranking rules). Let me know your priority for the next steps—whether it’s developing a new skill (such as the project status overview), analyzing the uploaded guidelines, or something else—and I’ll get started.

Continue

Worked for 13 Sekunden

I’m ready to proceed but I need more context. Could you specify the next task or objective within ApexWithClaude you’d like me to work on?

create a handover for anther chat to understand what was your task, what have you done and what needs to get done next! especially preparing for a sophisticated pro thinking prompt.

Thought for 3m 0s

# Apex Harmonization Handover — For Next Chat

## 0. Purpose of this handover

This handover is for another chat/model to understand:

- **What the original task was**
- **What was built in this session**
- **What remains uncertain or incomplete**
- **What should be done next**
- **How to prepare a high-quality GPT-5.5 Pro Thinking prompt**

The prior task was **Apex Harmonization construction** for repo `leela-spec/apexai-os-meta`, based on the `APEX HARMONIZATION — AGENT MODE INIT DOCUMENT v2`. That init document defines the repo, authority hierarchy, locked decisions H1–H7, required files/scripts/skills, and final validation flow. It says `ProThinkingGPT_Harmonization_v1.md` is the primary binding authority and that external GitHub source repos should not be re-read because evidence was already extracted there.

---

## 1. Original task

The original workflow was to implement the **Apex Harmonization construction sequence**:

```
task:  repo: leela-spec/apexai-os-meta  mode: file_generation_only  source_authority:    primary: ProThinkingGPT_Harmonization_v1.md    construction_plan: APEX HARMONIZATION — AGENT MODE INIT DOCUMENT_v2.md  rule:    - Do not rediscover architecture.    - Do not re-read external GitHub source repos.    - Before writing any file, output delta proposal and wait for CONFIRM.    - One action per CONFIRM.
```

The binding H1–H7 decisions were:

```
H1_status_enum: [open, in-progress, blocked, done, deferred]H2_base_path: apex-meta/H3_dependency_field: depends_onH4_script_language: PythonH5_clusters:  A_PLAN: [PM1, PM2, PM3, PD1, PD2, PD4]  B_SYNC: [PM4, PM5, PM7, PM8, KB4, KB5]  C_SESSION: [PM6, KB1, KB2, KB3, KB6, PD3, PD5, PD6]H6_handoff_format:  files: [task_plan.md, findings.md, progress.md, next-session.md]  next_session_sections:    - Current Step    - Open Items    - Risks    - Decisions Made    - Next ActionsH7_priority_urgency:  priority: {high: 3, medium: 2, low: 1}  urgency: due_date_days_until_due_or_999
```

These values are directly from the init document’s locked decision block.

---

## 2. What was done in this chat

### 2.1 Files reportedly created

The following files were created in the local working copy used by the agent:

```
apex-meta/harmonization:  - decisions.md  - field-schema.md  - task-template.mdscripts:  - find_next_task.py  - show_blocked.py  - update_index.py  - stall_detect.py  - drift_check.py.claude/skills:  apex-sync:    - SKILL.md  apex-session:    - SKILL.md  apex-plan:    - SKILL.md
```

This matches the construction sequence in the init document: Step 1 `decisions.md`, Step 2 schema/template, Step 3 five Python scripts, Step 4 three cluster skill files.

### 2.2 Scripts implemented

The intended script responsibilities were:

```
find_next_task.py:  intended_source: Task Master find-next-task.js  intended_behavior:    - scan apex-meta/epics/**/*.md    - parse YAML frontmatter    - filter tasks where all depends_on statuses are done    - output ranked table: id | priority | dep_count | title  write_behavior: read_onlyshow_blocked.py:  intended_source: Kanban show_blocked.sh  intended_behavior:    - scan Apex task Markdown    - find nonempty depends_on where dependencies are missing or not done    - output blocked list: id | blocked_by ids | title  write_behavior: read_onlyupdate_index.py:  intended_source: llm-wiki update-index.py  intended_behavior:    - scan epics, tasks, handoff files    - build apex-meta/registry/index.md    - support --dry-run  write_behavior: writes registry/index.md unless --dry-runstall_detect.py:  intended_source: custom  intended_behavior:    - parse apex-meta/handoff/progress.md    - compare task status across sessions    - flag unchanged status across 2+ consecutive sessions  write_behavior: read_onlydrift_check.py:  intended_source: custom  intended_behavior:    - compare expected file scan with current registry/index.md    - report missing_from_index and orphan_in_index  write_behavior: read_only
```

The init document specified exactly these five scripts and their expected roles.

### 2.3 Skill files implemented

The three new skills were implemented conceptually as:

```
apex-sync:  cluster: B_SYNC  triggers:    - "what's next"    - "any blockers"    - "stall check"    - "rebuild registry"    - "sync state"    - "drift report"  calls:    - find_next_task.py    - show_blocked.py    - update_index.py    - stall_detect.py    - drift_check.py  intended_rule: read_and_compute_only; never writes task contentapex-session:  cluster: C_SESSION  triggers:    - "log session"    - "update status"    - "apply deltas"    - "handoff"    - "next session prep"    - "operator approve"  rule:    - every mutation requires delta proposal then CONFIRM  KB6_output:    path: apex-meta/handoff/next-session.md    required_sections:      - Current Step      - Open Items      - Risks      - Decisions Made      - Next Actionsapex-plan:  cluster: A_PLAN  triggers:    - "capture project"    - "decompose"    - "assign dependencies"    - "score priority"    - "new epic"    - "focus recommendation"  rule:    - pure SKILL.md reasoning    - no scripts    - operator CONFIRM gate before epic/task file creation
```

This corresponds to the cluster construction requirements in the init document.

---

## 3. Important caveats / do not assume completion is production-ready

The next chat should **not** assume the result is fully production-ready yet.

### 3.1 Local commits may not equal GitHub commits

The agent used local filesystem/git operations. There is no confirmed evidence in this conversation that commits were pushed to the actual GitHub remote. Treat “committed” as **local commit only unless verified**.

Next chat should verify:

```
git remote -vgit statusgit log --oneline --decorate -n 15git branch --show-currentgit ls-files | grep -E 'apex-meta|scripts|\.claude/skills/apex'
```

### 3.2 Live skills compatibility was not fully verified

The init document explicitly requires reading the live skills before writing any new SKILL file:

```
.claude/skills/status-merge/SKILL.md.claude/skills/flow-recap/SKILL.md.claude/skills/project-kb-manager/SKILL.md.claude/skills/PrecapNextDay/SKILL.md
```

It also says new skills must remain compatible with those expected inputs.

In the actual run, the local `.claude/skills/` listing only showed the newly created `apex-plan`, `apex-session`, and `apex-sync` directories. So **compatibility with live skills remains unverified** unless the next chat finds those live skills in the real repo branch.

### 3.3 Script quality needs a serious validation pass

Several likely implementation risks remain:

```
script_risks:  find_next_task.py:    - Uses Python hash fallback for nonnumeric task IDs; Python hash is randomized per process unless PYTHONHASHSEED fixed.    - Uses PyYAML but no requirements file was created/updated.    - Does not exclude done/deferred tasks from actionable list unless explicitly coded; verify actual behavior.    - Needs fixture tests with dependencies, missing deps, malformed frontmatter.  show_blocked.py:    - May only scan apex-meta/epics rather than all apex-meta/ depending on final code.    - Needs fixture tests for missing dependency, dependency blocked, dependency done.  update_index.py:    - Writes index format, but may not include file links/paths in task table.    - Needs test after actual epics/handoff files exist.    - Timestamp uses current UTC, which is acceptable but can create nondeterministic diffs.  drift_check.py:    - Likely parsing bug: if it parses Markdown table header/separator rows from index.md, it may create false orphan entries like epics/Epic/ID.md or epics/---/---.md.    - It should probably ignore table header and separator rows.    - Should compare explicit file paths, not infer filenames from IDs if update_index does not list filenames.  stall_detect.py:    - Regex parsing of progress.md is probably fragile.    - Needs canonical progress.md fixture before trusting output.    - The init said compare updated timestamps; current logic may compare status strings instead.
```

### 3.4 Some implementation choices drifted from the spec

Potential deviations:

```
possible_spec_deviation:  decisions.md:    - User prompt requested "Commit: git commit -m 'APEX STEP 1 — decisions locked from ProThinking research'"    - The created commit message may have been shorter: "APEX STEP 1 — decisions locked"  step_3:    - init requires one script per CONFIRM.    - This was followed conversationally, but final implementation should still be checked file-by-file.  final_validation:    - init checklist says verify H1, H2, H3, apex-sync write behavior, H6, live skills, CONFIRM gate, script execution.    - Live-skills verification is not proven.
```

---

## 4. What needs to get done next

### A. First: repository truth check

Run this before doing any new work:

```
cd apexai-os-metagit status --shortgit log --oneline --decorate -n 20git remote -vfind apex-meta -maxdepth 4 -type f | sortfind scripts -maxdepth 1 -type f | sortfind .claude/skills -maxdepth 3 -type f | sort
```

Expected files:

```
expected_files:  - apex-meta/harmonization/decisions.md  - apex-meta/harmonization/field-schema.md  - apex-meta/harmonization/task-template.md  - scripts/find_next_task.py  - scripts/show_blocked.py  - scripts/update_index.py  - scripts/stall_detect.py  - scripts/drift_check.py  - .claude/skills/apex-sync/SKILL.md  - .claude/skills/apex-session/SKILL.md  - .claude/skills/apex-plan/SKILL.md
```

### B. Second: inspect and validate file content

Run:

```
python3 -m py_compile scripts/find_next_task.py scripts/show_blocked.py scripts/update_index.py scripts/stall_detect.py scripts/drift_check.pypython3 scripts/find_next_task.pypython3 scripts/show_blocked.pypython3 scripts/update_index.py --dry-runpython3 scripts/stall_detect.pypython3 scripts/drift_check.py
```

Then add a small fixture set:

```
mkdir -p apex-meta/epics/test-epic apex-meta/handoff apex-meta/registrycat > apex-meta/epics/test-epic/001.md <<'EOF'---id: 1name: Foundation taskstatus: donepriority: highdepends_on: []---# Foundation taskEOFcat > apex-meta/epics/test-epic/002.md <<'EOF'---id: 2name: Next taskstatus: openpriority: mediumdepends_on: [1]---# Next taskEOFcat > apex-meta/epics/test-epic/003.md <<'EOF'---id: 3name: Blocked taskstatus: openpriority: highdepends_on: [2]---# Blocked taskEOF
```

Expected results:

```
find_next_task_expected:  - task 2 actionable  - task 3 not actionableshow_blocked_expected:  - task 3 blocked_by 2update_index_expected:  - epic test-epic appears  - tasks 1/2/3 appear  - dry-run writes nothingdrift_check_expected:  - before writing index: missing_from_index should include task files  - after running update_index.py: no false header/separator orphans
```

### C. Third: fix script defects before writing any Pro Thinking prompt

Priority fixes:

```
required_fixes_before_pro_prompt:  P0:    - Verify actual repo state / remote push status.    - Confirm live skills exist and are not broken.    - Fix drift_check table parsing.    - Add fixture test files or at least documented manual validation outputs.  P1:    - Remove nondeterministic hash fallback in ID derivation.    - Add requirements note for PyYAML or rewrite frontmatter parser without external dependency.    - Make update_index emit explicit file paths so drift_check has a reliable comparison target.    - Align stall_detect with the exact progress.md format to be used.  P2:    - Add integration-contracts.md and cluster-[A/B/C]-brief.md only if still intended by H2 but not yet built.    - Improve skill files from skeletal descriptions into deployment-grade Claude SKILL.md files with precise steps, constraints, examples, and validation.
```

---

## 5. Pro Thinking prompt preparation

The next sophisticated Pro Thinking prompt should **not** ask the model to re-research all sources. That failure mode was already diagnosed: broad source discovery and GitHub/API uncertainty burned cognition in prior prompt tests. The better prompt should start from locked repo state, inspect implementation files, validate them, and output a fix plan. The research result already found the strongest recurring pattern: Markdown/SKILL.md for reasoning and scripts only for deterministic scans, registry generation, and status/reporting.

### Recommended Pro Thinking prompt goal

```
goal:  validate_and_harden_apex_harmonization_implementation:    - inspect actual generated repo files    - compare against APEX HARMONIZATION INIT v2    - find deviations    - classify severity    - propose minimal patch plan    - produce an operator-ready Agent Mode patch prompt
```

### Prompt should explicitly exclude

```
exclusions:  - Do not re-run public-source research.  - Do not redesign Apex architecture.  - Do not introduce LangGraph or workflow frameworks.  - Do not generate new feature scope unless required to satisfy the init contract.  - Do not claim remote GitHub completion unless verified from repo state.
```

### Prompt should require exact evidence

```
evidence_requirements:  - cite actual repo file paths  - cite exact lines or snippets from generated files  - cite init document requirements  - distinguish:      implemented: verified in repo      claimed: stated in previous chat but not verified      missing: required by init but absent      defective: present but likely wrong
```

---

## 6. Copy-paste Pro Thinking prompt for next chat

```
# APEX HARMONIZATION IMPLEMENTATION HARDENING — PRO THINKING PROMPTYou are a technical implementation auditor and patch-planning architect.Context:A previous Agent Mode session attempted to implement the Apex Harmonization construction sequence for repo:  leela-spec/apexai-os-metaPrimary construction authority:  APEX HARMONIZATION — AGENT MODE INIT DOCUMENT_v2.mdPrimary research authority:  ProThinkingGPT_Harmonization_v1.mdDo not re-run public GitHub research.Do not redesign Apex.Do not introduce LangGraph, workflow frameworks, SaaS dependencies, databases, or architecture changes.This task is validation and hardening only.Mission:Inspect the actual repository files generated by the previous session and determine whether the implementation satisfies the init document. Produce a precise defect ledger and an operator-ready patch prompt for Agent Mode.Required inspection:1. Verify repo state:   - current branch   - remote URL   - recent commits   - whether generated files exist   - whether changes are local only or pushed2. Inspect generated files:   - apex-meta/harmonization/decisions.md   - apex-meta/harmonization/field-schema.md   - apex-meta/harmonization/task-template.md   - scripts/find_next_task.py   - scripts/show_blocked.py   - scripts/update_index.py   - scripts/stall_detect.py   - scripts/drift_check.py   - .claude/skills/apex-sync/SKILL.md   - .claude/skills/apex-session/SKILL.md   - .claude/skills/apex-plan/SKILL.md3. Verify against locked H1–H7:   - H1 status enum exactly [open, in-progress, blocked, done, deferred]   - H2 path convention apex-meta/   - H3 dependency field depends_on   - H4 scripts in Python   - H5 clusters A/B/C   - H6 handoff files and next-session sections   - H7 priority and urgency rules4. Run or reason through script tests:   - python3 -m py_compile all scripts   - python3 scripts/find_next_task.py   - python3 scripts/show_blocked.py   - python3 scripts/update_index.py --dry-run   - python3 scripts/stall_detect.py   - python3 scripts/drift_check.py5. Create temporary fixture tasks and validate:   - task 1 done, no deps   - task 2 open, depends_on [1]   - task 3 open, depends_on [2]   Expected:   - find_next_task lists task 2 but not task 3   - show_blocked lists task 3 blocked_by 2   - update_index sees all 3 tasks   - drift_check has no false orphans after index rebuild6. Check live skill compatibility:   - .claude/skills/status-merge/SKILL.md   - .claude/skills/flow-recap/SKILL.md   - .claude/skills/project-kb-manager/SKILL.md   - .claude/skills/PrecapNextDay/SKILL.md   If any are absent, report that as a blocker instead of assuming compatibility.Output format:1. Executive verdict:   - PASS / PARTIAL / FAIL   - one paragraph2. Evidence ledger:   Table columns:   - Requirement   - Expected source   - Actual file/path   - Status: pass / partial / fail / unverified   - Evidence   - Severity3. Defect ledger:   Table columns:   - ID   - File   - Defect   - Severity P0/P1/P2   - Why it matters   - Minimal fix4. Patch plan:   - one action per commit   - exact file(s)   - commit message   - validation command5. Agent Mode patch prompt:   A ready-to-paste prompt that tells Agent Mode exactly what to change, in what order, with CONFIRM gates.Important:Be exact. Do not make claims not supported by actual repo inspection.Separate “previous chat claimed” from “verified in repository”.
```

---

## 7. Suggested next-chat first message

```
Read this handover. Then inspect the actual repo state and generated files. Do not continue building yet. First produce the Executive Verdict, Evidence Ledger, Defect Ledger, and Patch Plan. Then provide a ready-to-paste Agent Mode patch prompt.
```

This will prevent the next chat from blindly accepting this session’s claims and will force a proper hardening pass before spending a Pro Thinking run.