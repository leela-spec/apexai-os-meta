# Apex Orchestration System — Phase 1 Preparation Guide
## Claude Sonnet Extended Thinking | Prompt 2 of 2 | Operator Preparation

---

You are Claude in extended thinking mode. The operator (AlexOG) has already run a planning session (Prompt 1) and received your integration plan and clarifying questions. This session has one job: **tell the operator exactly how to prepare their existing 30–40 files before opening Claude Code for the first time.**

The operator should leave this session with a concrete checklist: what to rename, what format each file should be in, what to add, what to remove, and what new files to create from scratch. After completing this checklist, the operator will be ready to open Claude Code and begin Phase 2 (integration).

---

## PART 1 — CONTEXT (read, do not repeat back)

The operator has a knowledge base organized as a skill/agent database:

**Meta-agents:** Top-level agent definitions, each with:
- Essentials (role, responsibilities, boundaries)
- Templates (reusable instruction patterns)
- Mistakes (known failure modes and corrections)
- Appendices (supporting references)

**Sub-agents:** Same structure as meta-agents but scoped to specific functions

**Routines/Process specs:** Detailed definitions of the core loop stages (PreCapWeek, PreCapNextDay, FlowRecap, APSU, etc.)

**Workflow examples:** Concrete examples of how processes run for specific projects (e.g. MasterOfArts)

**Process ranking:** Priority ordering of which skills/routines to build first

These files are in markdown (mostly) and YAML (occasionally). They are logically organized but not yet formatted for Claude Code integration. They contain the right content but need to be translated into Claude's native primitives.

**Claude's native primitives (what content maps into):**
- `CLAUDE.md` — persistent instructions Claude reads at every session start
- `SKILL.md` (or `SKILL.draft.md`) — step-by-step procedure definitions for repeatable skills
- `SOUL.md` (or `SOUL.draft.md`) — profile identity definitions (role, boundaries, behavior)
- `YAML config files` — structured data (AI surface inventory, artifact schemas, ID schemas)
- `Artifact templates` — blank fill-in structures the operator uses during execution (e.g. raw dump template)
- `README.md` — navigation and orientation files per folder

---

## PART 2 — YOUR TASK

Produce a **complete preparation checklist** for the operator. Structure it as follows:

### Section A: File-by-file conversion guide
For each file type in the operator's knowledge base, specify:
1. What Claude primitive it maps to
2. The exact format it should be in (headers, YAML blocks, section names)
3. What to keep, what to cut, what to add
4. A minimal example of the converted format (5–10 lines is enough — show structure, not full content)

Cover all five file types:
- Meta-agent essentials → maps to: ?
- Meta-agent templates → maps to: ?
- Meta-agent mistakes → maps to: ?
- Sub-agent essentials → maps to: ?
- Routine/process spec → maps to: ?
- Workflow example → maps to: ?
- Process ranking file → maps to: ?

### Section B: Naming and structure conventions
Tell the operator exactly:
- What to name each file (naming pattern)
- What folder it goes in (logical folder name — not absolute path yet)
- What the top YAML block of every file must contain (minimum metadata)
- What status field to use (`status: draft` for everything at this stage)

### Section C: What to create from scratch
List the files that do NOT exist in the operator's knowledge base yet but that Claude Code will need during Phase 2. For each:
- File name
- What it contains
- Why Claude needs it before integration begins
- A skeleton (headers + empty fields) the operator can fill in

These will likely include:
- The CLAUDE.md for the repo (global session rules)
- The AI surface inventory config
- The raw flow dump template
- The initial project status packet (current.md)
- The consumed-recaps registry

### Section D: Consolidation decisions
Some of the operator's 30–40 files probably overlap or can be merged. Give the operator a decision framework:
- When to merge two files into one
- When to split one file into two
- When to archive a file (content is valid but not needed in Phase 2)
- When a file should become a reference (linked from CLAUDE.md but not loaded every session)

### Section E: Preparation order
Give the operator a numbered sequence for doing all of this preparation work. What do they do first, second, third? Sequence it to minimize rework — if deciding on naming conventions first prevents having to rename everything later, put that first.

### Section F: Ready-check
Give the operator a simple yes/no checklist they can run through before opening Claude Code. If all boxes are checked, they are ready for Phase 2. If any box is unchecked, they are not ready.

---

## PART 3 — RULES FOR THIS SESSION

- Be concrete — no vague guidance like "organize your files clearly"
- Every recommendation must be actionable by the operator alone, without needing to open Claude Code first
- Show format examples, not just descriptions
- If you need to make an assumption about the operator's files, state the assumption explicitly
- Do not propose the full repo file tree — that is Phase 2's job
- Do not start building files — this session is preparation only
- Flag anything that requires a decision from the operator (use [OPERATOR DECISION NEEDED: ...])
