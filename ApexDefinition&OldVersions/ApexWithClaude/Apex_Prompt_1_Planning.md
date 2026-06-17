# Apex Orchestration System — Integration Planning Session
## Claude Sonnet Extended Thinking | Prompt 1 of 2 | Planning Only

---

You are Claude in extended thinking mode. You are being brought into a planning session for a personal AI orchestration system called **Apex**. The operator (AlexOG) has already done extensive design work. Your job in this session is **not to build anything**. Your job is to:

1. Read and deeply understand the system as designed
2. Understand the existing knowledge base (files) that need to be integrated
3. Ask the operator clarifying questions to resolve ambiguities
4. Produce a structured integration plan — how this system should be built inside a Claude Code repo

You will produce two outputs at the end:
- **Output A:** A structured integration plan (phases, sequence, decisions)
- **Output B:** A prioritized list of clarifying questions you still need answered before Phase 1 begins

Do not write files. Do not propose file trees yet. Do not execute anything.

---

## PART 1 — THE SYSTEM BEING BUILT

The operator has designed a personal AI orchestration layer called **Apex**. It lives inside one GitHub repo: `apex-orchestration`. It is built and maintained using **Claude Code** (Claude running with local filesystem access).

### What Apex does
Apex is a planning-execution-recap-state loop. It does not execute work automatically. The operator does the actual work. Apex:
- Creates structured plans (weekly → daily → per-flow)
- The operator executes those plans manually
- Apex converts execution evidence into durable project state
- That state seeds the next planning cycle

### The core loop (fixed, do not reorder):
```
PreCapWeek → PreCapNextDay → OperatorExecutesPlannedFlow → FlowRecap → APSU → next PreCapNextDay
```

**PreCapWeek:** Defines weekly direction from project state + operator intent → produces `weeklyplanpacket`

**PreCapNextDay:** Converts weekly plan + current project state → produces `nextdayplan` with four fixed flow packets (F1–F4) and prompt packets per sprint

**Fixed daily flows:**
- F1 = Leela (app dev)
- F2 = MasterOfArts (coaching business)
- F3 = Apex/Hermes (orchestration buildout)
- F4 = Residual (recovery, overflow, cross-project)

Each flow has three sprints: S1 (first work), S2 (second work), S3 (recap/digest)

**OperatorExecutesPlannedFlow:** Human work layer — operator executes one flow, produces a `rawflowdump` or `skippedflowmarker`

**FlowRecap:** Converts flow packet + raw dump → structured `flowrecappacket` with project status delta, artifact index, model usage delta, next step proposal

**APSU (All-Project Status Update):** Merges all flow recaps into canonical project state → produces updated `current.md` per project + `nextPreCapNextDayinputcontext`

### Operator gates (all mandatory):
- G1: Operator approves weekly plan before PreCapNextDay
- G2: Operator approves next day plan before executing any flow
- G3: Operator marks flow done/partial/skipped/blocked after execution
- G4: Operator validates next step + status delta during FlowRecap
- G5: Operator reviews APSU output only if conflicts or high-impact changes detected

### The four profiles (durable identity boundaries, not workflow names):
| Profile | Role |
|---|---|
| alfred | Operator-facing interface, intake, daily/weekly review surface, human gate |
| metastrategist | Strategy, prioritization, leverage, long-horizon direction |
| metaoperations | Process orchestration, routing, artifact creation, build coordination |
| metadetectivecontroller | Verification, drift detection, quality control, safety gates |

### The six skill candidates (repeatable procedures → become SKILL.md files):
- `flow-recap` — converts flow packet + raw dump into recap packet
- `precap-next-day` — turns weekly plan + status into daily flow plan
- `status-merge` — merges flow recaps into canonical project status (APSU)
- `precap-week` — defines weekly direction from project state + intent
- `prompt-and-ai-routing-planning` — AI surface routing decisions per prompt
- `model-usage-log` — lightweight model/surface usage delta tracking

### Locked architecture decisions (do not reopen):
- Profiles are identity/runtime boundaries — not names for every function
- Most repeatable procedures become skills, not profiles
- GitHub is the single source of truth — all artifacts are markdown/YAML files
- APSU does NOT auto-trigger PreCapNextDay in v0.1 — operator starts it manually
- No cron or Kanban automation in v0.1 — manual invocation only

### Deprecated models (never revive):
- DayExecution as standalone process
- FlowExecution as standalone process
- DayExecutionController as standalone process
- RecapDay as required project-state loop stage
- Storing large structured artifacts in MEMORY.md
- Creating many profiles for every workflow

---

## PART 2 — THE EXISTING KNOWLEDGE BASE

The operator has **30–40 existing markdown and YAML files** that define this system. These files are organized like a skill/agent database with the following structure:

**Meta-agents** (top-level agent definitions):
- Each has: essentials, templates, mistakes, appendices

**Sub-agents** (specialized function agents):
- Same structure: essentials, templates, mistakes, appendices

**Routines and process specs** (the core loop stages defined in detail)

**Workflow examples** (concrete examples of how the system runs for specific projects, e.g. MasterOfArts)

**Process ranking and prioritization** (which skills/routines to build first)

These files were designed before the operator fully understood Claude's native infrastructure. They contain the right logic and content, but:
- They are not yet in Claude's preferred format (CLAUDE.md, SKILL.md, SOUL.md)
- Some concepts use different terminology than Claude uses natively
- They are information-dense and need to be digested, not copied verbatim

**Your job with these files:**
- Understand what content belongs where in Claude's architecture
- Identify which files map to which Claude primitives (CLAUDE.md rules, SKILL.md procedures, SOUL.md profile definitions, YAML configs, artifact templates)
- Identify what is missing that Claude needs but the files don't provide
- Tell the operator exactly how to prepare these files for efficient integration

---

## PART 3 — THE THREE INTEGRATION PHASES

### Phase 1 — Preparation (operator does this BEFORE opening Claude Code)
The operator prepares the existing 30–40 files so that when Claude Code opens the repo, it can integrate them efficiently without wasting tokens on interpretation or reformatting.

Questions to resolve in this session:
- What format should each file type be converted into?
- What is the minimum Claude needs to understand each agent/profile?
- What is the minimum Claude needs to understand each skill/routine?
- What naming conventions, header structures, and YAML schemas should be standardized?
- Which files should be combined? Which should stay separate?
- What new files does the operator need to create that don't exist yet?

### Phase 2 — Integration (Claude Code builds the repo from prepared files)
Claude Code reads the prepared files and converts them into the Apex repo structure. The key challenge here is token efficiency — 30–40 files cannot all be fed at once.

Questions to resolve in this session:
- What is the optimal batching sequence for feeding files to Claude Code?
- Which files must Claude read first (foundational context)?
- Which files can be deferred to later sessions?
- How should the operator instruct Claude Code at the start of each batch session?
- What does Claude need to remember between sessions (what goes in CLAUDE.md)?

### Phase 3 — Testing (operator runs simulation sessions)
After the repo is built, the operator runs test sessions to verify the system works.

Questions to resolve in this session:
- What is the minimum viable test — what does "working" look like?
- How does the operator test a PreCapNextDay run?
- How does the operator test a FlowRecap run?
- What failure signals indicate something was built incorrectly?

---

## PART 4 — YOUR TASK IN THIS SESSION

Read everything above carefully. Then do the following in order:

### Step 1: Reflect and summarize
In 10–15 bullet points, tell the operator what you understand about:
- The system being built
- The existing knowledge base structure
- The key challenge of integration

### Step 2: Identify translation decisions
For each of the following, state your recommended mapping — what Claude primitive does it become, and why:
- A meta-agent definition (essentials + templates + mistakes + appendices)
- A sub-agent definition (same structure)
- A routine/process spec (e.g. PreCapNextDay, FlowRecap)
- A workflow example (e.g. MasterOfArts concrete example)
- A process ranking/prioritization file

### Step 3: Ask your clarifying questions
Ask every question you need answered to produce a precise integration plan. Organize questions by category:
- Questions about the existing files (structure, naming, content)
- Questions about Claude Code usage (how the operator works with it daily)
- Questions about repo setup (paths, branches, local vs remote)
- Questions about priorities (what must work first, what can wait)
- Questions about anything else blocking you

Do not hold back questions. It is better to ask 20 questions now than to build the wrong thing.

### Step 4: Draft the integration plan
Based on what you know so far (before questions are answered), draft a preliminary integration plan with:
- Phase 1 preparation steps (ordered list)
- Phase 2 batching strategy (how to feed files to Claude Code)
- Phase 3 test protocol (what to run and what to look for)

Mark anything in the plan as [PENDING: question X] where it depends on a question you asked in Step 3.

---

## PART 5 — RULES FOR THIS SESSION

- Do not build files
- Do not propose a final file tree yet
- Do not make assumptions about file content — ask instead
- Do not revive deprecated models (see Part 1)
- If you are unsure about how Claude Code works vs how Hermes/another runtime works, say so explicitly — do not assume
- Treat the operator's existing files as authoritative on *content*, but not on *format* — the format is your domain
- The goal of this session is a plan and a question list, not a scaffold
