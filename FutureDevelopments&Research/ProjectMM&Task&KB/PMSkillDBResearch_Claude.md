Here is the full architecture session output.

---

## Step 1 — Hermes: What It Actually Is

**NousResearch/Hermes** is a fine-tuned LLM series (Hermes 2, 3, etc.) with strong function-calling and tool-use. It is **not** a skill community. There is no "Hermes skill ecosystem" for PM in the sense Marco referenced. The `NousResearch/hermes-agent` repo is a Claude Code-compatible agent runtime — its [`tools/skills_hub.py`](https://github.com/NousResearch/hermes-agent) is a **skill registry infrastructure layer** (GitHub source adapters, ClawHub adapter, skills.sh adapter, trust scoring, quarantine logic). It is the plumbing for fetching and installing skills, not a PM skill library itself.

**What Hermes-agent actually provides relevant to Apex:**

- `SKILL.md` + YAML frontmatter as the canonical skill entrypoint format
    
- `GitHubSource`, `SkillsShSource`, `ClawHubSource` adapters — you can tap any repo
    
- `HubLockFile` for provenance tracking of installed skills
    
- Trust levels: `builtin` → `trusted` → `community`
    
- This is infrastructure Apex can leverage to install skills from external taps, not a PM pattern source
    

---

## Step 2 — Actual Skill Communities Found

The [awesomeclaude.ai](https://awesomeclaude.ai/awesome-claude-skills) directory indexes **169 community skills across 13 categories**, actively maintained as of 2026. This is the primary living skill community. [skills.sh](https://skills.sh/) catalogs **69,000+ skills** across all AI coding tools. Both are searchable. Here are the candidates directly relevant to Apex PM architecture:

## Candidate Evaluation Table

|Candidate|Stars|What Python Does|What Claude/AI Does|State Files|Portable?|Fit|
|---|---|---|---|---|---|---|
|**kanban-skill**|15|File read/write; YAML frontmatter updates on `.md` card files|None (pure instruction skill)|`.md` per card with `status/priority/dependencies` YAML|✅ Yes|Medium — file schema is directly usable|
|**pm-skills**|292|24 PM skills, MCP server support, templates|Claude executes templates|Markdown templates per phase|✅ Yes|Medium — lifecycle phases match Apex|
|**Product-Manager-Skills**|5,100|None — pure prompt skills|PRD, roadmap, prioritization reasoning|Markdown docs|✅ Yes|Low — no Python layer|
|**ship-learn-next**|432|None — tracks iteration feedback|Claude synthesizes what to build/learn next|Feedback loop files|✅ Yes|Medium — session continuity concept|
|**swarmvault**|552|Compiles docs into local markdown wiki + search index|Knowledge graph construction|Local markdown wiki|✅ Yes|High — file-based KB pattern|
|**blueprint (JuliusBrussee)**|1,000|None|Spec → blueprint → build plan|Markdown spec files|✅ Yes|Medium — planning layer only|
|**Imprint**|95|None — portable profile|Memory, planning, review, debugging habits|Profile `.md`|✅ Yes|High — session continuity pattern|
|**llm-wiki**|51|Sharded indexes, Python file ops|Search and synthesis|Sharded markdown index|✅ Yes|**Highest** — KB manager pattern, Python + Claude split|

**Winner for architectural import: `llm-wiki` ([praneybehl/llm-wiki-plugin](https://github.com/praneybehl/llm-wiki-plugin)) + `kanban-skill` ([mattjoyce/kanban-skill](https://github.com/mattjoyce/kanban-skill)).**

- `llm-wiki`: Python builds/maintains sharded markdown index; Claude queries and synthesizes. This is **the closest existing pattern** to project-kb-manager. It solves the KB-build/search split cleanly.
    
- `kanban-skill`: YAML frontmatter on `.md` files per task entity — directly importable as the task/chunk file schema for Apex.
    

**Why these were missed in prior research:** Prior research targeted dedicated PM SaaS-wrappers and Node.js tools. The `llm-wiki` pattern lives in the Claude Code skill community, not the PM tooling ecosystem. It was not indexed under PM — it's categorized under Learning & Knowledge.

---

## Step 3 — Apex Python/Claude Split

Based on `llm-wiki` (sharded index build = Python; synthesis = Claude) and `kanban-skill` (YAML frontmatter state = file-native):

## Operation Decision Table

|Operation|Layer|Source Pattern|Why This Layer|
|---|---|---|---|
|Read all `.claude/kb/projects/*.md`|Python|llm-wiki index build|Deterministic; no reasoning needed|
|Parse YAML frontmatter fields|Python|kanban-skill schema|Deterministic; structured data|
|Generate `registry.md` index from project files|Python|llm-wiki sharded index|File aggregation = deterministic|
|Compute `unlock_depth` score from `depends_on/unlocks`|Python|Task Master AI dependency scoring|Graph traversal = deterministic|
|Check stall condition (same `next_action` 3+ sessions)|Python|GSD Core STATE.md diff|String comparison = deterministic|
|Write progress log entries (append-only)|Python|planning-with-files 2-action rule|File mutation = must be deterministic|
|Update `status`/`priority` fields (explicit values)|Python|kanban-skill YAML writer|Explicit value = no AI tokens justified|
|Output structured data packet to Claude|Python|llm-wiki → synthesis handoff|Boundary: Python produces, Claude consumes|
|Synthesize `next_action` from milestone + progress log|Claude|llm-wiki synthesis layer|Requires context + narrative reasoning|
|Rank projects using `priority_score` + operator context|Claude|pm-skills prioritization templates|Multi-variable judgment = AI justified|
|Merge FlowRecap narrative into project state deltas|Claude|GSD Core FlowRecap pattern|Unstructured text → structured delta|
|Detect implicit blockers from FlowRecap text|Claude|planning-with-files error persistence|Natural language inference required|
|Generate focus recommendation with reasoning|Claude|Product-Manager-Skills frameworks|Operator-facing synthesis = AI justified|
|Write `next-precap-context.md` output file|Claude → Python|GSD Core CONTEXT.md pattern|Claude generates content; Python writes file|

**Import spec summary:**

- From `kanban-skill`: YAML frontmatter schema (`status`, `priority`, `depends_on`, `due_date` fields)
    
- From `llm-wiki`: Python index-build pattern (scan files → build sharded registry → hand structured packet to Claude)
    
- From `GSD Core`: `STATE.md` / `CONTEXT.md` artifacts as session continuity files
    
- From `Task Master AI`: dependency scoring concept (unlock_depth as integer)
    
- From `planning-with-files`: 2-action write rule, error persistence in progress log
    
- From `Hermes-agent skills_hub.py`: SKILL.md + YAML frontmatter as entrypoint standard (already aligned)
    

---

## Step 4 — First Test Run Design

**Input state:** Apex orchestration system. M1 complete. M2 in progress. M3–M8 pending.

**Test run sequence:**

**Step 1 — Python reads and computes:**

text

`python kb_scan.py --project apex → Reads: .claude/kb/projects/apex.md → Parses: YAML frontmatter (current_milestone: M2, status: in_progress) → Reads: progress_log (last 5 entries) → Computes: unlock_depth(M2) = 3 (M3, M4, M5 unlock when M2 completes) → Checks: stall? No (last 3 sessions show different next_action values) → Outputs: structured_packet.json`

**Step 2 — Python outputs structured packet:**

json

`{   "project": "apex-orchestration",  "current_milestone": "M2",  "milestone_label": "project-kb-manager skill: Python/Claude split",  "unlock_depth": 3,  "stall": false,  "progress_log_tail": [    "2026-06-16: defined YAML frontmatter schema",    "2026-06-17: wrote Python index builder scaffold",    "2026-06-18: architecture session — import spec in progress"  ],  "next_milestones": ["M3: PrecapNextDay integration", "M4: FlowRecap merge logic"],  "blockers_explicit": [] }`

**Step 3 — Claude synthesizes (token-justified reasoning):**  
Input: structured_packet.json + operator context ("solo operator, morning flow")

**Step 4 — Mock operator output (readable in 30 seconds):**

text

`━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ APEX KB MANAGER — FOCUS SIGNAL Session: 2026-06-18 | Project: apex-orchestration ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ CURRENT  M2 — project-kb-manager Python/Claude split STATUS   in_progress | unlock_depth: 3 | stall: NO NEXT ACTION   → Finalize SKILL.md entrypoint and write first Python    kb_scan.py (reads registry, outputs structured_packet.json).  → Estimated: 1 focused flow session. WHY NOW   M2 is the highest unlock: completing it unblocks M3 (Precap  integration), M4 (FlowRecap merge), and M5 (multi-project  scaffold). No other project is competing for this slot. IMPLICIT RISK DETECTED   None from last 3 FlowRecap sessions. Architecture session  today replaces one flow slot — adjust PrecapNextDay signal. PRECAP SIGNAL FOR TOMORROW   Ranked input for PrecapNextDay:  1. apex / M2 — kb_scan.py implementation [HIGH]  2. apex / M2 — SKILL.md entrypoint draft [MEDIUM]  3. apex / M3 — PrecapNextDay integration spec [LOW/BLOCKED] ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━`

**Step 5 — Operator validates:**

- Is the next_action correct? → Yes/No → if No, operator corrects and Python appends to progress log.
    
- Is the Precap signal ranked correctly? → feeds directly into PrecapNextDay.
    

---

The first test run will show Marco: **a 30-second readable panel with current milestone, unlock_depth, next action with reasoning, implicit risk flag, and a ranked Precap signal — all computed from real project files, no manual input required.**