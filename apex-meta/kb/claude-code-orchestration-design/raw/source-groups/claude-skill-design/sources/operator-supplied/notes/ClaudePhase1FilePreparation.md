## Section A: File-by-File Conversion Guide

Each of your seven file types maps to a specific Claude primitive. Below is the mapping, required format, and a minimal format example for each.

---

## A1 — Meta-Agent Essentials → `SOUL.md` (or `SOUL.draft.md`)

**What it is:** The identity layer. Role, responsibilities, and hard boundaries for a top-level agent.

**Keep:** Role definition, responsibility scope, behavioral constraints, tone/style rules.  
**Cut:** Any procedural steps (those go in SKILL.md), examples that are already in workflow files.  
**Add:** A `soul_id` field, a `version` field, and a `linked_skills` list pointing to associated SKILL.md files.

**Format example:**

text

`--- soul_id: SOUL-META-APEX version: 0.1 status: draft linked_skills:   - SKILL-FLOWRECAP-CORE  - SKILL-PRECAP-WEEK --- # [AgentName] — Soul Definition ## Role One sentence: what this agent IS. ## Responsibilities - Responsibility A - Responsibility B ## Hard Boundaries - Must not do X - Must not do Y ## Behavioral Defaults - Tone: ... - Output format preference: ...`

---

## A2 — Meta-Agent Templates → `SKILL.md` (or `SKILL.draft.md`)

**What it is:** Reusable instruction patterns are procedural — they become skill definitions, not soul definitions.

**Keep:** Step sequences, conditional logic ("if X then Y"), input/output descriptions.  
**Cut:** Role framing, agent backstory, anything that belongs in SOUL.md.  
**Add:** `skill_id`, `trigger` (what invokes this skill), `inputs`, `outputs`, explicit numbered steps.

**Format example:**

text

`--- skill_id: SKILL-TEMPLATE-[NAME] version: 0.1 status: draft trigger: "Operator invokes [SkillName] explicitly" inputs:   - raw_dump: string outputs:   - structured_recap: artifact --- # [SkillName] — Skill Definition ## Purpose One sentence. ## Steps 1. Step one — what Claude does 2. Step two — conditional: if [condition], then [action] 3. Step three — output produced ## Failure Modes - If input is missing X → request clarification before proceeding`

---

## A3 — Meta-Agent Mistakes → Append to `SOUL.md` under `## Known Failure Modes`

**What it is:** Mistakes files are not a separate primitive — they are an appendix section inside the SOUL they belong to.

**Keep:** The failure mode description and the correction behavior.  
**Cut:** Any framing prose, redundant headers.  
**Add:** Nothing new — just merge under the parent SOUL's `## Known Failure Modes` section.

**Format example (inside SOUL.md):**

text

`## Known Failure Modes ### FM-01: Over-scoping responses - Trigger: Operator gives an open-ended prompt - Default bad behavior: Claude generates full deliverable unprompted - Correction: Pause, confirm scope before producing output ### FM-02: Skipping recap validation - Trigger: FlowRecap invoked without prior raw dump - Correction: Surface missing input error immediately`

> **Assumption:** Each meta-agent has one mistakes file. If you have a single consolidated mistakes file across agents, split it by agent before merging.

---

## A4 — Sub-Agent Essentials → `SOUL.draft.md` (sub-agent variant)

Identical mapping to A1, but with a different `soul_id` prefix convention and a `parent_agent` field.

**Add:** `parent_agent` field linking back to the meta-agent this sub-agent serves.

**Format example (YAML block only):**

text

`--- soul_id: SOUL-SUB-[FUNCTION] version: 0.1 status: draft parent_agent: SOUL-META-APEX linked_skills:   - SKILL-[FUNCTION]-CORE ---`

> **[OPERATOR DECISION NEEDED: Do your sub-agents each have their own templates/mistakes files, or are those shared with the parent meta-agent? This determines whether sub-agents get their own SKILL.md files or inherit from meta-agent skills.]**

---

## A5 — Routine/Process Spec → `SKILL.md`

**What it is:** Your process specs (PreCapWeek, FlowRecap, APSU, etc.) are the closest thing you already have to SKILL.md files. These need the least conversion work.

**Keep:** The stage-by-stage breakdown, all conditional logic, input/output definitions.  
**Cut:** Background/rationale prose longer than 2 sentences (archive it, don't delete).  
**Add:** `skill_id`, `trigger`, `inputs`, `outputs`, `estimated_duration` (optional but useful), and a `## Failure Modes` section at the bottom.

**Format example:**

text

`--- skill_id: SKILL-FLOWRECAP-CORE version: 0.1 status: draft trigger: "End of active flow session, operator says 'run FlowRecap'" inputs:   - raw_dump: string (operator-provided)  - current_project_status: file ref → current.md outputs:   - flow_recap_artifact: structured markdown  - updated current.md estimated_duration: 8–12 min --- # FlowRecap — Skill Definition ## Purpose ... ## Pre-conditions - [ ] raw_dump provided - [ ] current.md loaded ## Steps 1. ...`

---

## A6 — Workflow Example → `examples/` folder, kept as-is with a YAML header added

**What it is:** Workflow examples (e.g., MasterOfArts) are **reference material**, not active primitives. Claude doesn't execute them — it reads them as context when needed.

**Keep:** Everything. These are gold.  
**Cut:** Nothing.  
**Add:** A YAML front-matter block with `type: example`, `references_skill`, and `project`.

**Format example:**

text

`--- type: example project: MasterOfArts references_skill: SKILL-FLOWRECAP-CORE status: reference --- # MasterOfArts — FlowRecap Workflow Example ## Context ... ## Session Log ...`

---

## A7 — Process Ranking File → `CLAUDE.md` (section: `## Build Priority`)

**What it is:** The ranking file is not a standalone primitive — its content belongs directly in CLAUDE.md so Claude sees it at every session start without being asked.

**Keep:** The ranked list, the reasoning per item (condensed to 1 line each).  
**Cut:** Any extended rationale paragraphs — move those to a `docs/` reference file.  
**Add:** Nothing. Just paste the condensed ranked list into CLAUDE.md under its own section.

---

## Section B: Naming and Structure Conventions

## File Naming Pattern

|File Type|Naming Pattern|Example|
|---|---|---|
|Meta-agent soul|`SOUL-META-[AGENTNAME].draft.md`|`SOUL-META-APEX.draft.md`|
|Sub-agent soul|`SOUL-SUB-[FUNCTION].draft.md`|`SOUL-SUB-RECAP.draft.md`|
|Skill/process|`SKILL-[PROCESSNAME]-CORE.draft.md`|`SKILL-FLOWRECAP-CORE.draft.md`|
|Workflow example|`EXAMPLE-[PROJECT]-[SKILL].md`|`EXAMPLE-MASTEROFARTS-FLOWRECAP.md`|
|YAML config|`[CONFIGNAME].config.yaml`|`ai-surfaces.config.yaml`|
|Artifact template|`TEMPLATE-[ARTIFACTNAME].md`|`TEMPLATE-RAWDUMP.md`|
|Project status|`current.md`|`current.md` (always this name)|

## Folder Structure (Logical Names Only — No Paths Yet)

text

`/souls          ← all SOUL.draft.md files /skills         ← all SKILL.draft.md files /examples       ← all workflow example files /config         ← all YAML config files /templates      ← all artifact templates /docs           ← archived rationale, process ranking extended notes /registry       ← consumed-recaps registry, session logs`

> **[OPERATOR DECISION NEEDED: Do you want sub-agent souls in a `/souls/sub-agents/` subfolder, or flat in `/souls/`? Flat is simpler for Claude to navigate in Phase 2; nested is cleaner for humans. Pick one now to avoid renaming later.]**

## Minimum YAML Front-Matter (Every File)

Every single file — without exception — must start with this block:

text

`--- id: [UNIQUE-ID] type: [soul | skill | example | config | template | registry] version: 0.1 status: draft last_updated: 2026-06-12 owner: AlexOG ---`

`status: draft` on everything at this stage. Do not mark anything `active` until Phase 2 validation confirms it works.

---

## Section C: Files to Create from Scratch

These do not exist in your knowledge base yet but Claude Code will need them immediately upon first session.

---

## C1 — `CLAUDE.md` (Root of repo)

**What it contains:** Global session rules — what Claude must do at the start of every session, what it must never do, how to navigate the repo, build priority order.

**Why Claude needs it before Phase 2:** This is the first file Claude reads. Without it, Claude has no context and will operate on defaults.

**Skeleton:**

text

``--- id: CLAUDE-GLOBAL type: config version: 0.1 status: draft last_updated: 2026-06-12 owner: AlexOG --- # Apex Orchestration — Global Session Rules ## On Session Start - Load current.md - Load [list specific SOUL files] - Do not load examples unless explicitly requested ## Hard Rules - Never output a deliverable without operator confirming scope - Always check pre-conditions before executing a skill - Flag missing inputs before proceeding ## Repo Navigation - /souls → agent identity definitions - /skills → executable skill definitions - /examples → reference only - /templates → operator fills these in during execution ## Build Priority [Paste condensed ranking list from your process ranking file here] ## Current Phase Phase 2 — Integration. Skills marked `status: draft` are in testing.``

---

## C2 — `ai-surfaces.config.yaml`

**What it contains:** Inventory of every AI tool/surface in your stack (Claude, NotebookLM, etc.) with what it's used for, what it can and cannot do, and how it connects to skills.

**Why Claude needs it:** Skills reference specific surfaces ("output this to NotebookLM"). Claude needs to know what each surface is before executing.

**Skeleton:**

text

`--- id: CONFIG-AI-SURFACES type: config version: 0.1 status: draft last_updated: 2026-06-12 owner: AlexOG --- surfaces:   - id: SURFACE-CLAUDE    name: Claude (Claude Code)    role: primary orchestrator    capabilities: []       # fill in    limitations: []        # fill in    connected_skills: []   # fill in after skills are named   - id: SURFACE-[NEXT]    name:    role:    capabilities: []    limitations: []    connected_skills: []`

---

## C3 — `TEMPLATE-RAWDUMP.md`

**What it contains:** The blank fill-in form the operator completes at the end of a flow session before running FlowRecap.

**Why Claude needs it:** FlowRecap's first step is validating the raw dump against this schema. Without a defined template, validation has no reference.

**Skeleton:**

text

`--- id: TEMPLATE-RAWDUMP type: template version: 0.1 status: draft last_updated: 2026-06-12 owner: AlexOG --- # Raw Flow Dump ## Session Date YYYY-MM-DD ## Project [Project name] ## Duration [Approximate session length] ## What Was Done [Freeform — operator fills this in] ## Decisions Made -  ## Blockers / Open Questions -  ## Next Immediate Action [One sentence]`

---

## C4 — `current.md`

**What it contains:** The live state of the current project — active sprint, last recap reference, next action, key decisions pending.

**Why Claude needs it:** Every skill that involves project continuity reads this file first. It is the state anchor.

**Skeleton:**

text

`--- id: CURRENT-STATUS type: registry version: 0.1 status: draft last_updated: 2026-06-12 owner: AlexOG --- # Current Project Status ## Active Project [Project name] ## Current Phase [Phase name / number] ## Last Recap [Recap ID or date — leave blank until first FlowRecap runs] ## Next Action [One sentence] ## Pending Decisions -  ## Blocked On -` 

---

## C5 — `consumed-recaps.registry.yaml`

**What it contains:** A log of every FlowRecap that has been produced, consumed, and archived. Prevents double-processing.

**Why Claude needs it:** Without this, Claude cannot know which recaps have already been integrated into project state.

**Skeleton:**

text

`--- id: REGISTRY-CONSUMED-RECAPS type: registry version: 0.1 status: draft last_updated: 2026-06-12 owner: AlexOG --- recaps: [] # Each entry will follow this shape once populated: # - recap_id: RECAP-YYYYMMDD-[PROJECT] #   date: YYYY-MM-DD #   project:  #   status: consumed   # or: produced | archived #   consumed_into: current.md`

---

## Section D: Consolidation Decisions

## When to Merge Two Files

Merge when:

- Two files describe **the same agent** but split across "essentials" and a structural appendix — combine into one SOUL.md
    
- Two process specs share **80%+ of their steps** and differ only by trigger condition — one SKILL.md with a conditional branch is cleaner
    
- A mistakes file has **fewer than 5 entries** — always merge into the parent SOUL's `## Known Failure Modes`
    

## When to Split One File

Split when:

- A single file contains **both identity content (who the agent is) and procedural content (what it does)** — split into SOUL.md + SKILL.md
    
- A routine spec covers **more than one distinct trigger condition** — each trigger gets its own SKILL.md
    
- A workflow example covers **more than one project** — one file per project
    

## When to Archive

Archive (move to `/docs`, add `status: archived`) when:

- The file contains valid background rationale but **no executable content**
    
- A file is a **previous version** superseded by a merged/split output
    
- Content is **accurate but not needed until Phase 3 or later** (check against your process ranking file — anything not in top-priority tier gets archived now)
    

## When to Make a Reference File

Make it a reference (keep in `/docs`, link from CLAUDE.md but don't auto-load) when:

- The file is **long** (>200 lines) and Claude only needs it occasionally
    
- It's a **workflow example** — never auto-load examples, always reference on demand
    
- It contains **extended reasoning** behind a decision — useful to have, not needed every session
    

---

## Section E: Preparation Order

Do these in sequence. Each step produces outputs the next step depends on.

1. **Establish naming conventions** — Decide the flat vs. nested folder question ([OPERATOR DECISION NEEDED] from Section B) and write your naming pattern on a sticky note. Every rename from here follows this pattern. Doing this first prevents renaming files twice.
    
2. **Audit all 30–40 files** — Go through each file and assign it one of: `soul`, `skill`, `example`, `config`, `template`, `archive`, or `merge-pending`. Use a simple spreadsheet or plain list. Do not rename yet.
    
3. **Execute all merge decisions** — Combine mistakes files into parent SOULs. Merge near-duplicate process specs. Do this before renaming so you're renaming final files, not intermediate ones.
    
4. **Execute all split decisions** — Separate any files that contain both identity + procedural content into SOUL + SKILL pairs.
    
5. **Add YAML front-matter to every file** — Go file by file, add the minimum metadata block from Section B. Set `status: draft` on everything. This is mechanical and fast once you're in a rhythm.
    
6. **Rename all files** — Using the naming pattern from Step 1, rename every file to its final name.
    
7. **Create the five scratch files from Section C** — In order: `CLAUDE.md` first (it references the others), then `current.md`, then `ai-surfaces.config.yaml`, then `TEMPLATE-RAWDUMP.md`, then `consumed-recaps.registry.yaml`.
    
8. **Populate `CLAUDE.md` Section: Build Priority** — Paste your condensed process ranking directly into CLAUDE.md now, while the ranking file is fresh in your head.
    
9. **Run the Ready-Check (Section F)** — If anything fails, fix it before opening Claude Code.
    

---

## Section F: Ready-Check

Run through this before opening Claude Code. Every box must be checked.

**Naming & Structure**

- Every file follows the naming pattern from Section B
    
- Every file has a YAML front-matter block with `id`, `type`, `version`, `status: draft`, `last_updated`, `owner`
    
- No two files share the same `id` value
    
- Folder structure matches the logical folders from Section B
    

**File Completeness**

- Every meta-agent has exactly one `SOUL-META-*.draft.md` file
    
- Every sub-agent has exactly one `SOUL-SUB-*.draft.md` file
    
- Every process spec (PreCapWeek, PreCapNextDay, FlowRecap, APSU, etc.) has exactly one `SKILL-*.draft.md` file
    
- Every mistakes file has been merged into its parent SOUL's `## Known Failure Modes` section and the standalone mistakes file is archived
    
- All workflow examples are in `/examples` with `type: example` in their YAML block
    

**Scratch Files Created**

- `CLAUDE.md` exists at repo root and contains: session rules, repo navigation map, build priority list, current phase
    
- `current.md` exists with all fields present (can be blank — just not missing)
    
- `ai-surfaces.config.yaml` exists with at least one surface entry (Claude itself)
    
- `TEMPLATE-RAWDUMP.md` exists with all sections present
    
- `consumed-recaps.registry.yaml` exists (empty `recaps: []` is fine)
    

**Consolidation Complete**

- No file contains both soul content (identity) and skill content (procedure) — these have been split
    
- All archived files are in `/docs` and marked `status: archived`
    
- Nothing in `/skills` has `status: archived` — archived skills leave the `/skills` folder
    

**Final Sanity**

- You can open any SOUL file and immediately identify the agent's role, responsibilities, and failure modes
    
- You can open any SKILL file and immediately identify the trigger, inputs, outputs, and numbered steps
    
- CLAUDE.md can be read cold (no context) and still make sense