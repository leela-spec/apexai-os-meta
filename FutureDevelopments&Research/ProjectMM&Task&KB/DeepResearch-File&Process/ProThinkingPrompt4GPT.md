# APEX PM/KB/PD — Execution Options Research
# Optimized for GPT o3 / 4o with extended thinking. Not deep research mode.

---

## Your role

You are a technical analyst, not a designer. Your job is to read real implementation 
files from public GitHub repositories, extract concrete evidence from those files, 
and report — per process — every viable implementation option you can substantiate 
with a file citation. Do not architect a system. Do not make recommendations. 
Discover and report options; stop there.

---

## Hard rules (read before starting)

R1. Every claim needs a direct file URL citation. Format: [exact URL].
R2. Use the browser tool to fetch each file. Do NOT construct raw.githubusercontent.com 
    URLs — many return 404. Use the GitHub web URL format:
    https://github.com/[owner]/[repo]/blob/[branch]/[path]
    Then fetch the rendered page or use:
    https://api.github.com/repos/[owner]/[repo]/contents/[path]
    to get base64-decoded file content.
R3. If a path returns 404 or empty content, try the repo root via:
    https://api.github.com/repos/[owner]/[repo]/contents/
    List what is actually there and report the correct path.
R4. If a file genuinely cannot be fetched after two attempts with different paths, 
    write exactly: "NOT FOUND — searched: [URL1], [URL2]" and continue.
R5. Never invent or infer file content. If you did not read it, say so.
R6. No filler prose. Tables over paragraphs throughout.

---

## Background (context only — do not analyse this)

Apex is a personal AI orchestration system running inside a GitHub repository. 
The AI engine is Claude, used via Claude Code (terminal agent reading SKILL.md 
instruction files from the repo). No SaaS. No external database. One solo operator. 
Apex needs to execute 20 processes across four domains: project management (PM), 
knowledge base management (KB), product management (PD), and process governance. 
Whether each process requires a Python/bash script or can run as a pure SKILL.md 
instruction file is the open question this research must answer, per process.

---

## Step 1 — Read these repositories

For each source below: fetch at minimum 2 non-README implementation files. 
Prioritise SKILL.md files, scripts, schema files, and example files.
Log every URL fetched and whether it succeeded or failed.

### Confirmed working paths (verified in prior research — fetch these first):

**S1 — CCPM** `github.com/automazeio/ccpm`
- https://github.com/automazeio/ccpm/blob/main/skill/ccpm/SKILL.md
- https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/structure.md
- https://github.com/automazeio/ccpm/blob/main/skill/ccpm/references/track.md
Extract: task frontmatter field names, status enum, dependency fields 
(depends_on / parallel / conflicts_with), script names mapped to user intents, 
the script-first execution rule.

**S2 — Backlog.md** `github.com/MrLesk/Backlog.md`
- https://github.com/MrLesk/Backlog.md/blob/main/backlog/tasks/BACK-200%20-%20Add-Claude-Code-integration-with-workflow-commands-during-init.md
- Find and fetch any schema definition file (try docs/, .backlog/, or src/)
Extract: complete YAML frontmatter field list, required vs optional, status enum.

**S3 — Task Master AI** `github.com/eyaltoledano/claude-task-master`
- https://github.com/eyaltoledano/claude-task-master/blob/main/docs/task-structure.md
- Find and fetch the next-task selection script (try scripts/ or src/commands/)
Extract: task JSON schema fields, dependency field names, priority scoring logic, 
next-task algorithm (exact logic, not description).

**S4 — GSD Core** — search GitHub for "GSD Core Claude agent STATE.md CONTEXT.md".
Try: `github.com/pHab/gsd` or search via 
https://api.github.com/search/repositories?q=GSD+Claude+STATE+CONTEXT
Fetch STATE.md and CONTEXT.md templates.
Extract: exact fields, session capture and restore mechanism.

**S5 — planning-with-files**
- https://github.com/mxyhi/ok-skills/blob/main/planning-with-files/SKILL.md
- https://github.com/OthmanAdi/planning-with-files/blob/master/docs/quickstart.md
Extract: the 2-action write rule, error persistence mechanism, progress log format 
(task_plan.md / findings.md / progress.md schema).

**S6 — OpenClaw** `github.com/openclaw/openclaw`
- Try: https://api.github.com/repos/openclaw/openclaw/contents/
- Fetch skills/taskflow/SKILL.md and any .lobster example file
Extract: flow lifecycle states, stateJson structure, Python/AI execution boundary.

**S7 — CrewAI skills** `github.com/crewAIInc/skills`
- Try: https://api.github.com/repos/crewAIInc/skills/contents/
- Fetch skills/design-task/SKILL.md and skills/getting-started/SKILL.md
Extract: task contract fields, guardrail definition, human review gate, 
output file pattern.

**S8 — llm-wiki**
- https://github.com/alirezarezvani/claude-skills/blob/main/engineering/llm-wiki/skills/llm-wiki/SKILL.md
- https://github.com/junbjnnn/llm-wiki (list contents, then fetch init-wiki.py or update-index.py)
Extract: file scanning logic, index structure, Python/Claude split boundary.

**S9 — kanban-skill** `github.com/mattjoyce/kanban-skill`
- https://api.github.com/repos/mattjoyce/kanban-skill/contents/
- Fetch SKILL.md and any example card .md file
Extract: YAML frontmatter fields, status/priority definitions, blockedby field, 
how dependencies gate lane transitions.

**S10 — pm-skills** — search: site:github.com "pm-skills" SKILL.md claude
Fetch any 2 SKILL.md files found.
Extract: PM lifecycle phases covered, trigger mechanism, output produced.

**S11 — swarmvault** — search GitHub: "swarmvault" claude skill
Try: https://api.github.com/search/repositories?q=swarmvault+claude
Fetch index build script or SKILL.md.
Extract: how documents compile into local wiki, Python/Claude split.

**S12 — Imprint** — search GitHub: "Imprint claude skill profile session"
Try: https://api.github.com/search/repositories?q=Imprint+claude+profile+session
Fetch profile template or SKILL.md.
Extract: session continuity mechanism, how profile persists across sessions.

**S13 — Hermes-agent** `github.com/NousResearch/hermes-agent`
- https://github.com/NousResearch/hermes-agent/blob/main/tools/skills_hub.py
- https://github.com/NousResearch/hermes-agent/blob/main/tools/skills_guard.py
Extract: SkillMeta fields, trust level system, source adapter structure, 
install/quarantine/audit flow.

**S14 — LangGraph** `github.com/langchain-ai/langgraph`
- Find one minimal stateful workflow example (try examples/ or docs/tutorials/)
This is a v2 escalation reference only.
Extract: minimum lines of code for a durable stateful workflow; complexity cost 
vs simple script.

**S15 — Pattern SKILLs** — For each pattern, search GitHub for the closest 
public Claude SKILL.md implementation and fetch one actual file:
- PRC-CORE-001 (intake→goal→artifact loop): search "goal artifact loop SKILL.md claude"
- TEMPLATE-KANBAN-001 (lanes + dependencies + review gates): search "kanban durable task graph SKILL.md"
- PRC-HANDOFF-001 (session handoff packet): search "agent handoff context packet SKILL.md"
- PRC-DATA-001 (CRISP-DM workflow): search "CRISP-DM agent workflow claude"
- PRC-VERIFY-001 (chain-of-verification gate): search "chain of verification SKILL.md claude"
- PRC-SCRUM-001 (sprint artifact loop): search "scrum sprint claude agent SKILL.md"
- PRC-RISK-001 (NIST AI RMF): search "NIST AI RMF claude agent workflow"

---

## Step 2 — Options table for each of the 20 processes

For every process, produce in this exact order:

**[ID] Process name**
What it does: [one sentence]

| Option | Source | Mechanism (cite file URL) | Token cost | Maintenance cost | Complexity | Needs script? | Portable? |
|--------|--------|--------------------------|------------|-----------------|------------|---------------|-----------|

Token cost: Low <500 tokens / Medium 500–2000 / High >2000  
Maintenance cost: Low = edit SKILL.md text only / Medium = edit script logic / High = refactor multiple files  
Needs script?: Yes only if the operation involves deterministic computation, 
file aggregation, or graph traversal Claude reasoning cannot reliably perform 
without errors. Be conservative — most operations do not need scripts.  
Portable?: Yes if no SaaS or external service required.

**Best option for solo operator, Claude Code, no SaaS:** [one sentence + exact file URL]

---

### The 20 processes:

**Project Management**
- PM1: Capture project — record name, goal, domain, state, success criteria
- PM2: Decompose project — break into epics, chunks, tasks with explicit splitting rules
- PM3: Assign dependencies — build depends_on and unlocks graph
- PM4: Compute next action — from state + dependency graph, determine what to do next
- PM5: Detect blockers — identify items that cannot proceed
- PM6: Update status — mark items complete after work finishes
- PM7: Detect stall — find items with no progress across multiple sessions
- PM8: Generate work registry — produce compact index of all project state

**Knowledge Base Management**
- KB1: Write session progress — capture what happened during a work session
- KB2: Extract state deltas — convert session narrative to structured field changes
- KB3: Maintain entity files — apply deltas to Markdown files without data loss
- KB4: Rebuild index — regenerate registry after state changes
- KB5: Detect drift — compare current state against last session snapshot
- KB6: Produce next-session context — generate handoff document for next Claude session

**Product Management**
- PD1: Score priority — assign numeric priority value
- PD2: Score urgency — assess time-sensitivity separately from priority
- PD3: Compute unlock depth — count items unblocked when this one completes
- PD4: Synthesize focus recommendation — ranked focus list with reasoning
- PD5: Validate with operator — human gate before any state mutation is written
- PD6: Feed planning layer — hand off ranked context to daily planning skill

---

## Step 3 — Sub-skill clustering

Answer three questions after completing all 20 process tables:

Q1. Which processes naturally cluster into the same skill (same trigger, same 
    files read/written, same execution context)? Name each cluster.

Q2. For each cluster: can it be pure SKILL.md with no scripts? Does it require 
    a script and in what language? Does an existing open-source SKILL.md from 
    the 15 sources serve as a base — and what must change?

Q3. Is there any process for which none of the 15 sources provides a viable 
    implementation pattern? If yes, name it and describe exactly what needs 
    to be built from scratch.

---

## Step 4 — Final summary table

One table. Every process on one row. No additional prose.

| Process ID | Process name | Best source | Mechanism | Needs script | Copy type | Priority rank |
|------------|--------------|-------------|-----------|--------------|-----------|---------------|

**Copy type definitions:**
- FULL: use the file or template as-is
- ADAPT: copy logic, rewrite format or language
- CONCEPT: rebuild from scratch using only the idea
- SKIP: not needed in v1 (add one-word reason)

**Priority rank:** PM4 = rank 1 (highest implementation fit), PM1 = rank 27.
Fill remaining ranks based on implementation readiness from your evidence.

---

## Output quality checklist (apply before finishing)

Before submitting your response, verify:
- [ ] Every claim cites an exact GitHub file URL (not a repo homepage)
- [ ] Every "NOT FOUND" entry lists the exact URLs searched
- [ ] No source is cited without having been fetched and read
- [ ] The Needs script? column is conservative (No unless computation is 
      genuinely unreliable without a script)
- [ ] Step 4 table is complete — all 20 rows present
- [ ] No architectural recommendations appear anywhere