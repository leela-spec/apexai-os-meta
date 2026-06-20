━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APEX HARMONIZATION — AGENT MODE INIT DOCUMENT v2
GPT-5 Agent Mode | ApexWithClaude Project
Repo: leela-spec/apexai-os-meta (branch: main)
Date: 2026-06-19
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

╔══════════════════════════════════════════════╗
║  AUTHORITY HIERARCHY — read this first       ║
╚══════════════════════════════════════════════╝

Tier 1 — PRIMARY (binding, overrides everything):
  ProThinkingGPT_Harmonization_v1.md  ← in this Project
  This file contains the full 20-process option table,
  evidence matrix, all source URLs, copy types, and
  the final "best option" verdict for every process.
  When in doubt about any implementation decision: consult this first.

Tier 2 — DESIGN CONTEXT (background, do not re-execute):
  DR_APEX_PM_KB_PD_Perp.md   ← defines the 20 processes, 4 domains (PM/KB/PD/PG),
                                 and Apex system goals
  DR_APEX_PM_KB_PD_GPT.md    ← alternative analysis, use only if ProThinking has a gap
  DR_APEX_PM_KB_PD_Gem.md    ← third analysis pass, low priority
  DR_Harmonization_Perp.md   ← full harmonization deep research (117k chars),
                                 contains the conflict table and field inventory
  These files define WHY. ProThinking defines WHAT and HOW.

Tier 3 — REPO CONTENT (what you will build into):
  leela-spec/apexai-os-meta  ← clone this, work inside it

Rule: Do NOT re-read external GitHub source repos.
      All source evidence is already extracted in ProThinkingGPT_Harmonization_v1.md.

╔══════════════════════════════════════════════╗
║  STEP 0 — SESSION SETUP                      ║
╚══════════════════════════════════════════════╝

Run in terminal:
  git clone https://<PAT>@github.com/leela-spec/apexai-os-meta.git
  cd apexai-os-meta

Confirm these local paths exist before writing anything:
  ls source-knowledge/ProjectRepos/ccpm-main/skill/ccpm/references/
  ls source-knowledge/ProjectRepos/planning-with-files-master/
  ls source-knowledge/ProjectRepos/llm-wiki-main/scripts/
  cat .claude/skills/status-merge/SKILL.md
  cat .claude/skills/flow-recap/SKILL.md
  cat .claude/skills/project-kb-manager/SKILL.md
  cat .claude/skills/PrecapNextDay/SKILL.md

Gate rule: before writing ANY file — output delta proposal, wait for CONFIRM.
One file or script per agent turn. No batching writes.

╔══════════════════════════════════════════════╗
║  LOCKED DECISIONS H1–H7                      ║
╚══════════════════════════════════════════════╝
Source authority: ProThinkingGPT_Harmonization_v1.md
These are FINAL. Do not rediscover, re-evaluate, or override.

H1 — STATUS ENUM
  [open, in-progress, blocked, done, deferred]
  Evidence: CCPM structure.md + Backlog.md types/index.ts

H2 — FILE PATH CONVENTION
  apex-meta/
  ├── harmonization/        ← decisions.md, field-schema.md, task-template.md,
  │                            integration-contracts.md, cluster-[A/B/C]-brief.md
  ├── epics/<slug>/         ← 001.md, 002.md … (task files)
  ├── handoff/              ← task_plan.md, findings.md, progress.md, next-session.md
  └── registry/             ← index.md (auto-generated, never edit manually)
  scripts/                  ← all Python scripts
  .claude/skills/           ← apex-plan/, apex-sync/, apex-session/
  Evidence: CCPM structure.md + planning-with-files SKILL.md

H3 — DEPENDENCY FIELD
  Field: depends_on   Type: int array   Example: depends_on: [1, 3]
  Eligibility rule: task is actionable only if ALL ids in depends_on have status=done
  Evidence: CCPM structure.md + Task Master find-next-task.js

H4 — SCRIPT LANGUAGE
  Python — for ALL deterministic operations
  No Bash. No TypeScript. No shell scripts.
  Evidence: llm-wiki update-index.py + Task Master find-next-task.js (ported)

H5 — CLUSTER ASSIGNMENT
  A — PLAN    (pure SKILL.md, no scripts, operator gate before any write)
              PM1, PM2, PM3, PD1, PD2, PD4
  B — SYNC    (SKILL.md + read-only Python scripts, never writes task content)
              PM4, PM5, PM7, PM8, KB4, KB5
  C — SESSION (SKILL.md + write-gate scripts, ALL mutations need CONFIRM)
              PM6, KB1, KB2, KB3, KB6, PD3, PD5, PD6

H6 — HANDOFF FORMAT
  Files: task_plan.md + findings.md + progress.md + next-session.md
  Location: apex-meta/handoff/
  next-session.md required sections:
    ## Current Step | ## Open Items | ## Risks | ## Decisions Made | ## Next Actions
  Evidence: planning-with-files SKILL.md + quickstart.md

H7 — PRIORITY + URGENCY
  priority field:  high | medium | low   (weights: high=3, medium=2, low=1)
  urgency field:   due_date (ISO8601)
  urgency score:   (due_date − today).days  →  lower = more urgent; None = 999
  Evidence: Task Master find-next-task.js + Kanban SKILL.md

╔══════════════════════════════════════════════╗
║  SOURCE INDEX — copy types + local paths     ║
╚══════════════════════════════════════════════╝
All evidence pre-extracted in ProThinkingGPT_Harmonization_v1.md.
Read local files ONLY for exact file content before adapting.
Do NOT fetch from GitHub.

S1a  CCPM SKILL.md
     Local: source-knowledge/ProjectRepos/ccpm-main/skill/ccpm/SKILL.md
     Use for: SKILL.md structure pattern, trigger format, 5-phase lifecycle
     Copy type: ADAPT

S1b  CCPM structure.md
     Local: source-knowledge/ProjectRepos/ccpm-main/skill/ccpm/references/structure.md
     Use for: PM2 decomposition, PM3 dependency fields
     Copy type: ADAPT (field names → Apex H3 naming)

S1c  CCPM track.md
     Local: source-knowledge/ProjectRepos/ccpm-main/skill/ccpm/references/track.md
     Use for: Cluster B SKILL (apex-sync) — script-first trigger pattern
     Copy type: ADAPT (Bash refs → Python refs)

S2b  Backlog types.ts
     Local: source-knowledge/ProjectRepos/backlog-main/src/types/index.ts
     Use for: canonical task field set for field-schema.md + task-template.md
     Copy type: ADAPT (TypeScript interface → YAML frontmatter)

S3c  Task Master find-next-task.js
     Local: source-knowledge/ProjectRepos/claude-task-master-main/scripts/modules/task-manager/find-next-task.js
     Use for: scripts/find_next_task.py algorithm
     Copy type: ADAPT (JS → Python, JSON task schema → Apex YAML frontmatter)

S4a  planning-with-files SKILL.md
     Local: source-knowledge/ProjectRepos/planning-with-files-master/SKILL.md
     Use for: KB1 (FULL copy → adapt field names), KB6 (FULL copy), apex-session base
     Copy type: KB1=FULL, KB6=FULL, PM7=CONCEPT

S5b  Kanban show_blocked.sh
     Local: source-knowledge/ProjectRepos/kanban-skill-master/skills/kanban-ai/scripts/show_blocked.sh
     Use for: scripts/show_blocked.py
     Copy type: ADAPT (Bash grep/sed → Python frontmatter parser)

S6b  llm-wiki update-index.py
     Local: source-knowledge/ProjectRepos/llm-wiki-main/scripts/update-index.py
     Use for: scripts/update_index.py (KB4, PM8)
     Copy type: FULL (change page-type groups to Apex H2 paths only)

S6a  llm-wiki SKILL.md
     Local: source-knowledge/ProjectRepos/llm-wiki-main/  (find SKILL.md)
     Use for: KB3 entity maintenance pattern, raw/ vs wiki/ separation rule
     Copy type: ADAPT

S8a  crewAI design-task SKILL.md
     Local: source-knowledge/ProjectRepos/crewAI-main/skills/design-task/SKILL.md
     Use for: PD5 operator gate pattern
     Copy type: ADAPT (replace human_input=True → explicit CONFIRM keyword gate)

╔══════════════════════════════════════════════╗
║  LIVE SKILLS — DO NOT BREAK                  ║
╚══════════════════════════════════════════════╝
Read these before writing any SKILL file.
Any new SKILL must remain compatible with their expected inputs.

  .claude/skills/status-merge/SKILL.md      ← reads H1 status values
  .claude/skills/flow-recap/SKILL.md        ← reads task files at H2 paths
  .claude/skills/project-kb-manager/SKILL.md
  .claude/skills/PrecapNextDay/SKILL.md

For each new SKILL file written, verify:
  □ Uses identical H1 enum values
  □ Reads/writes only H2 paths
  □ Uses H3 depends_on field name

╔══════════════════════════════════════════════╗
║  CONSTRUCTION SEQUENCE                       ║
╚══════════════════════════════════════════════╝
One action per CONFIRM. Do not proceed to next until current is committed.

STEP 1 — decisions.md                                    [CONFIRM gate]
  Write: apex-meta/harmonization/decisions.md
  Content: H1–H7 verbatim from this document
  Add per decision: source ID (S1a–S8a) + local file path + copy type
  Frontmatter: step: 1  status: locked  generated: 2026-06-19
  git commit -m "APEX STEP 1 — decisions locked"

STEP 2 — field-schema.md + task-template.md              [CONFIRM gate]
  Source: S2b (field list) + S1b (dependency fields) + S3a (Task Master schema)
  Fields: name, status(H1), created, updated, priority(H7), urgency(H7),
          depends_on(H3), parallel, conflicts_with, effort(XS/S/M/L/XL),
          epic, due_date, acceptance_criteria, definition_of_done
  Mark each: required | optional | computed
  No invented fields. Every field must appear in at least one source.
  git commit -m "APEX STEP 2 — field schema"

STEP 3 — Python scripts (one per CONFIRM, run + verify after each)
  3a. scripts/find_next_task.py
      Port S3c (JS→Python). Input: apex-meta/epics/**/*.md
      Output: ranked stdout table (id | priority | dep_count | title)
      Must NOT write any file.
      Run after writing. If error → fix before committing.

  3b. scripts/show_blocked.py
      Port S5b (Bash→Python). Scan apex-meta/ for nonempty depends_on
      where dependency task status ≠ done.
      Output: blocked task list (id | blocked_by ids | title)

  3c. scripts/update_index.py
      Copy S6b. Adapt: page-type groups → Apex types (epic, task, handoff).
      Must support --dry-run flag.
      Output: apex-meta/registry/index.md

  3d. scripts/stall_detect.py
      Custom. Compare updated timestamps in progress.md across sessions.
      Flag any task with no updated change in >2 sessions.

  3e. scripts/drift_check.py
      Custom. Run update_index.py --dry-run, compare vs current index.md.
      Report any files present in scan but missing from index.

STEP 4 — SKILL files (one cluster per CONFIRM)
  4a. .claude/skills/apex-sync/SKILL.md        [Cluster B]
      Base: S1c (CCPM track.md pattern — script-first)
      Triggers: "what's next" | "any blockers" | "stall check" |
                "rebuild registry" | "sync state" | "drift report"
      Calls: find_next_task.py, show_blocked.py, update_index.py,
             stall_detect.py, drift_check.py
      Rule: apex-sync NEVER writes task content. Read + compute only.

  4b. .claude/skills/apex-session/SKILL.md     [Cluster C]
      Base: S4a (planning-with-files) + S8a (crewAI CONFIRM gate)
      Triggers: "log session" | "update status" | "apply deltas" |
                "handoff" | "next session prep" | "operator approve"
      Write-gate: ALL mutations → show delta proposal → wait for CONFIRM
      KB6 output: apex-meta/handoff/next-session.md (H6 sections)

  4c. .claude/skills/apex-plan/SKILL.md        [Cluster A]
      Base: S1b (CCPM structure.md) + S2b (Backlog task contract)
      Triggers: "capture project" | "decompose" | "assign dependencies" |
                "score priority" | "new epic" | "focus recommendation"
      No scripts. Pure SKILL.md reasoning + file writes.
      Operator gate REQUIRED before creating any new epic or task file.

╔══════════════════════════════════════════════╗
║  FINAL VALIDATION                            ║
╚══════════════════════════════════════════════╝
Run after all files committed:
  python3 scripts/find_next_task.py
  python3 scripts/update_index.py --dry-run
  python3 scripts/show_blocked.py
  ls .claude/skills/
  grep -r "in-progress\|open\|blocked\|done\|deferred" \
       apex-meta/harmonization/decisions.md

Checklist — report YES/NO per line, fix any NO before closing:
  □ H1 enum identical in all 3 SKILL files
  □ H2 paths consistent in decisions.md and all SKILLs
  □ H3 depends_on field name consistent everywhere
  □ apex-sync contains zero file write operations
  □ KB6 handoff format (H6 sections) present in apex-session
  □ PD5 CONFIRM gate present in apex-session AND apex-plan
  □ status-merge and flow-recap still compatible (re-read them, confirm)
  □ All 3 Python scripts execute without error on empty apex-meta/

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
END INIT DOCUMENT v2
Estimated turns: ~12–15 (one CONFIRM per action)
Start: wait for operator CONFIRM before Step 1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━