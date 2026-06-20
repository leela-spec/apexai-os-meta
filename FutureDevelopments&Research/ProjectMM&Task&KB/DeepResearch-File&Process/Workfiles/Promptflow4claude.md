━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APEX HARMONIZATION — STEP 1 HANDOVER PACKET
For: new Perplexity chat with GitHub MCP access
Repo: leela-spec/apexai-os-meta (private)
Branch: main (SHA prefix: 4dceaa89)
Created: 2026-06-19
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## MISSION
Build the Apex personal AI orchestration system.
Apex = solo operator + Claude Sonnet 4.6 (via Perplexity with GitHub MCP).
No Claude Code. No SaaS. No external DB.
Everything lives in leela-spec/apexai-os-meta.
The EXISTING .claude/ directory in the repo is NOT the target system — ignore it.
The NEW system is to be built from scratch using the source repos as evidence base.

## DESIGN AUTHORITY
Two deep research reports exist in the repo — these are the canonical design documents:
- source-knowledge/DR_Harmonization_Perp.md
- source-knowledge/DR_APEX_PM_KB_PD_Perp.md
READ THESE FIRST before doing anything else. They define the 20 processes, 
4 domains (PM/KB/PD/PG), and harmonization goals.

## CURRENT STEP STATUS

### STEP 1 — Baseline Audit
STATUS: ~60% COMPLETE. Read-only. No files written yet.

#### COMPLETED READS (confirmed from real files):

FILE 1: source-knowledge/ProjectRepos/ccpm-main/skill/ccpm/references/structure.md
- status enum: open (single value at task creation)
- YAML frontmatter: name, status, created (ISO8601 full), updated (ISO8601 full),
  github (unset at creation), depends_on (int array), parallel (bool), conflicts_with (array)
- dependency field: depends_on → array of task numbers
- script-first rule: NO — structure.md is LLM-driven
- files written: .claude/epics/<name>/001.md, 002.md …; appends to epic.md
- trigger: "break an epic into actionable tasks"

FILE 2: source-knowledge/ProjectRepos/ccpm-main/skill/ccpm/references/track.md
- status enum: NONE (reads, does not define)
- script-first rule: YES — "All tracking operations have a corresponding bash script.
  Run the script; do not reconstruct the output manually."
- trigger: "what's our status", "standup", "what's next", "what's blocked", "validate"
- script language: Bash (bash references/scripts/<script>.sh)
- known scripts: next.sh, blocked.sh, standup.sh, status.sh, validate.sh,
  epic-list.sh, epic-show.sh, epic-status.sh, prd-list.sh, prd-status.sh,
  in-progress.sh, search.sh

FILE 3: source-knowledge/ProjectRepos/backlog-main/Backlog.md-main/backlog/config.yml
- status enum: ["To Do", "In Progress", "Done"]
- YAML frontmatter: project_name, default_status, statuses (array), labels (array),
  definition_of_done (array), date_format (yyyy-mm-dd hh:mm), task_prefix ("back")
- dependency field: NONE in config (in task files — not yet read)
- script-first rule: NO — TypeScript CLI tool
- files written: backlog/tasks/<prefix>-NNN - <title>.md
- directories: tasks/, completed/, archive/, drafts/, milestones/, decisions/, docs/
- trigger: NONE (CLI: backlog task create, backlog task list)

#### PARTIAL CONFLICT TABLE (from 3 files read):

| Field concept      | CCPM                              | Backlog                     | Conflict? |
|--------------------|-----------------------------------|-----------------------------|-----------|
| Status enum        | open                              | To Do / In Progress / Done  | YES       |
| Dependency field   | depends_on: [] (int array)        | not in config               | PARTIAL   |
| Date format        | ISO8601 full timestamp            | yyyy-mm-dd hh:mm            | YES       |
| Task ID format     | 001.md / 002.md (seq numbers)     | back-NNN - title.md         | YES       |
| Parallel flag      | parallel: boolean                 | NONE                        | YES       |
| Script language    | Bash                              | TypeScript CLI              | YES       |
| File base path     | .claude/epics/<name>/             | backlog/tasks/              | YES       |

#### STILL UNREAD (5 sources — MUST complete before Step 1 is done):

| # | Exact path to explore first    | Target files                          | Processes covered           |
|---|--------------------------------|---------------------------------------|-----------------------------|
| 1 | source-knowledge/ProjectRepos/claude-task-master-main/.taskmaster/ | tasks.json or schema file | PM4, PD1, PD2, PD3 — priority/urgency/dependency fields |
| 2 | source-knowledge/ProjectRepos/llm-wiki-main/        | SKILL.md + index/init script          | KB1, KB3, KB4, KB6          |
| 3 | source-knowledge/ProjectRepos/llm-wiki-skill-main/  | SKILL.md                              | KB skill pattern            |
| 4 | source-knowledge/ProjectRepos/gsd-core-next/        | STATE.md + CONTEXT.md                 | KB5, KB6 — session model    |
| 5 | source-knowledge/ProjectRepos/planning-with-files-master/ | SKILL.md                        | KB2, KB3 — 2-action write rule |

NOTE on claude-task-master: This is a large TypeScript monorepo (mcp-server, packages/, apps/, src/).
The schema lives under .taskmaster/ — start there, not in src/. The CLAUDE.md file (7.6kb) is
also worth reading as it documents the AI interface contract.

#### CONFIRMED ABSENT from ProjectRepos/:
- crewAI-main → EXISTS ✅ (not yet read)
- Any "kanban-skill", "swarmvault", "Imprint", "hermes-agent" → NOT present in ProjectRepos
  These were sourced from public GitHub in the prior deep research pass.

## CONFIRMED REPO STRUCTURE

source-knowledge/ProjectRepos/
├── backlog-main/              ✅ read
├── ccpm-main/                 ✅ read  
├── claude-task-master-main/   ⬜ .taskmaster/ not yet read
├── crewAI-main/               ⬜ not yet read
├── gsd-core-next/             ⬜ not yet read
├── llm-wiki-main/             ⬜ not yet read
├── llm-wiki-skill-main/       ⬜ not yet read
├── llm-wiki/                  ⬜ not yet read
└── planning-with-files-master/ ⬜ not yet read

## THE 20 PROCESSES TO COVER

Domain PM — Project Management:
PM1: Capture project (name, goal, domain, state, success criteria)
PM2: Decompose project (epics → chunks → tasks, explicit splitting rules)
PM3: Assign dependencies (depends-on / unlocks graph)
PM4: Compute next action (from state + DAG)
PM5: Detect blockers
PM6: Update status
PM7: Detect stall (items not progressed across sessions)
PM8: Generate work registry (compact index of all project state)

Domain KB — Knowledge Base Management:
KB1: Write session progress
KB2: Extract state deltas (narrative → structured field changes)
KB3: Maintain entity files (apply deltas without data loss)
KB4: Rebuild index
KB5: Detect drift (current state vs last session)
KB6: Produce next-session context (handoff document)

Domain PD — Product Management:
PD1: Score priority (numeric)
PD2: Score urgency (time-sensitivity, separate from priority)
PD3: Compute unlock depth (items unblocked when this completes)
PD4: Synthesize focus recommendation (ranked list + reasoning)
PD5: Validate with operator (human gate before state mutation)
PD6: Feed planning layer (hand off ranked context to daily planning skill)

## WHAT TO DO IN THE NEW CHAT

### STEP 1 COMPLETION (do this first):

1. Read source-knowledge/DR_Harmonization_Perp.md and
   source-knowledge/DR_APEX_PM_KB_PD_Perp.md to get full design authority context.
   (These may be large — read directory first to confirm exact filenames.)

2. Explore and read from each of the 5 unread sources listed above.
   For each: list the directory first, identify the 1-2 most relevant files, read them.
   Extract ONLY: field names, status enums, dependency logic, script language,
   session model, write rules. Do not read READMEs.

3. Extend the conflict table with every new field/enum/convention found.
   Flag every conflict with: Field | Source A value | Source B value | Conflict type.

4. OUTPUT: Final completed Step 1 = full conflict table + complete field inventory
   from all 9 repos. Chat only. No files written.

### STEP 2 (after Step 1 is fully done):

For each of the 20 processes, produce the options table as specified in the original
research prompt (PromptFlow Step 2). One row per viable implementation found.
Columns: Option | Source | Mechanism | Token cost | Maintenance cost | Complexity |
         Requires script? | Portable without SaaS?

Use conservative judgment on "Requires script?" — only Yes if deterministic computation,
file aggregation, or graph traversal that Claude cannot reliably do without errors.

### STEP 3: Sub-skill grouping
### STEP 4: Final summary table (all 20 processes, one row each)

These follow the same spec as the original research prompt (reproduced below).

## EXECUTION RULES
- Read actual implementation files, not READMEs
- Cite exact file URL (GitHub path) for every claim
- If a file returns 404, list the directory first and find the correct path
- Chat output only until explicitly told to write files
- Tables over prose throughout
- No filler, no architecture recommendations
- When two sources conflict on the same field, report BOTH and explain the tradeoff
- Token budget: Perplexity Sonnet 4.6 with GitHub MCP — max 3 tool calls per response turn,
  batch reads where possible (explore dir → identify files → read 2 at once)

## ORIGINAL RESEARCH SPEC (Step 2 columns — exact)

Option | Source | Mechanism | Token cost per run | Maintenance cost | Complexity |
Requires a script? | Portable without SaaS?

Token cost: Low = <500 tokens | Medium = 500–2000 | High = >2000
Maintenance cost: Low = edit text in SKILL.md only | Medium = edit script logic |
                  High = refactor multiple files
Script required: Yes ONLY if operation involves deterministic computation,
                 file aggregation, or graph traversal Claude cannot handle reliably.

Best option for solo operator, Claude Sonnet 4.6, no SaaS: one sentence + evidence URL.

Step 4 columns:
Process ID | Process name | Best source | Mechanism | Needs script |
Copy type | Priority rank

Copy type: FULL / ADAPT / CONCEPT / SKIP (one word + reason)
Priority rank: PM4 = rank 1 (highest fit), PM1 = rank 27

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
END HANDOVER PACKET
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━