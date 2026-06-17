## Step 4 — Preliminary Integration Plan

## Phase 1 — Preparation (operator does before opening Claude Code)

1. **Audit existing files** — list all 30–40 files by name, note their type (meta-agent / sub-agent / routine / example / ranking), and flag any that are project-specific vs. reusable. Output: a simple spreadsheet or markdown table. [PENDING: Q1, Q3]
    
2. **Classify each file** against the translation map from Step 2 — assign each file a target Claude primitive: SOUL.md, SKILL.md, CLAUDE.md contribution, template file, example file, or discard. [PENDING: Q2, Q4, Q5]
    
3. **Separate mixed-content files** — any file that contains both identity content (→ SOUL.md) and procedure content (→ SKILL.md) must be split before Phase 2. This is a manual operator task. [PENDING: Q5]
    
4. **Standardize headers in all SKILL.md candidates** — each should have: `## Purpose`, `## Trigger`, `## Inputs Required`, `## Steps`, `## Output Format`, `## Operator Gate`, `## Anti-Patterns`. This is the SKILL.md schema to converge on. [PENDING: Q2]
    
5. **Standardize headers in all SOUL.md candidates** — each should have: `## Identity`, `## Core Directives`, `## Voice and Stance`, `## Constraints`, `## Anti-Patterns`. [PENDING: Q4]
    
6. **Write the root CLAUDE.md** — this is new content the operator must draft. It should contain: what Apex is (1 paragraph), the core loop definition, the four profiles (named, not detailed), the six skills (named, not detailed), locked architecture decisions, build priorities. This is the file Claude Code reads first in every session. [PENDING: Q12, Q13]
    
7. **Create the repo** — initialize `apex-orchestration` as a private GitHub repo under `leela-spec`, push a skeleton with just `CLAUDE.md` and `README.md` before any other files are added. [PENDING: Q16, Q17]
    
8. **Stage files into batches** — group the prepared files into 4–5 logical batches for Phase 2, ordered by dependency. Batch 1 = foundational (CLAUDE.md + profiles). Batch 2 = core skills (FlowRecap + APSU). Batch 3 = planning skills (PreCapNextDay + PreCapWeek). Batch 4 = routing + logging skills. Batch 5 = examples + templates. [PENDING: Q10, Q21, Q22]
    

---

## Phase 2 — Integration Batching Strategy (Claude Code sessions)

**Session 1 — Foundation:**  
Feed: root CLAUDE.md + all four SOUL.md profile files. Instruction to Claude Code: _"Read these files and confirm you understand the four profiles, the core loop, and the locked architecture decisions. Do not build anything yet. Confirm your understanding in bullet points."_ Claude Code writes nothing — this is an orientation session.

**Session 2 — First skill build:** [PENDING: Q22]  
Feed: SOUL.md files (already loaded in CLAUDE.md memory) + the single highest-priority SKILL.md candidate. Instruction: _"Build this skill into the repo at `skills/[name].md`. Use the SKILL.md schema from CLAUDE.md. Confirm the file was written."_

**Session 3 — Core loop skills:**  
Feed: FlowRecap SKILL.md + APSU SKILL.md + any relevant artifact templates. Build both skills. Operator validates output against spec.

**Session 4 — Planning skills:**  
Feed: PreCapNextDay SKILL.md + PreCapWeek SKILL.md. Build both. [PENDING: Q19, Q20]

**Session 5 — Routing, logging, examples:**  
Feed: remaining skill candidates + example files + project state templates. [PENDING: Q24, Q27]

**Between-session continuity rule:** CLAUDE.md must be updated after each session to reflect what was built. Claude Code should not rely on session memory — every session starts from CLAUDE.md + file tree. [PENDING: Q12, Q13]

---

## Phase 3 — Test Protocol

**Test 1 — Smoke test (single skill invocation):**  
Invoke FlowRecap (or whichever skill was built first) with a synthetic `rawflowdump` — a short fake flow execution note. Expected output: a valid `flowrecappacket` markdown file with all required sections populated. Failure signal: missing sections, wrong format, operator gate not surfaced. [PENDING: Q26]

**Test 2 — PreCapNextDay run:**  
Feed a synthetic `weeklyplanpacket` + a synthetic `current.md` state file. Expected output: a `nextdayplan` with four flow packets (F1–F4) and sprint breakdowns. Failure signal: fewer than four flows, missing sprint structure, skill producing prose instead of structured output.

**Test 3 — APSU merge:**  
Feed three FlowRecap outputs (one real from Test 1, two synthetic). Expected output: updated `current.md` per project. Failure signal: state delta not captured, conflicts not surfaced, `nextPreCapNextDayinputcontext` not produced. [PENDING: Q28]

**Test 4 — Full day simulation:**  
Run the complete loop: PreCapNextDay → execute one real flow → FlowRecap → APSU. This is the minimum viable end-to-end test. Failure signals: any gate being skipped, any output being prose when structured format is required, state from APSU not feeding cleanly into the next PreCapNextDay. [PENDING: Q21, Q23]

**What "working" looks like:** Operator can run one complete day (four flows) through the system, with all five gates triggering, and APSU produces a `current.md` that accurately reflects what happened. [PENDING: Q21]

---

**Output A (integration plan) and Output B (question list) are above.** The plan has 30 questions pending — Q1, Q2, Q10, Q12, Q16, Q17, Q18, Q21, Q22, Q26, Q28, and Q30 are the ones that would most change the Phase 1 and Phase 2 sequencing if answered differently. I'd suggest answering those twelve first if you want to move fast, and I can refine the plan in one pass before we open Claude Code.

One thing I want to flag explicitly: **Q29 (profile enforcement mechanism) and Q14 (multi-surface usage) are architecturally load-bearing** — if Hermes or another Claude interface will also touch this repo, the CLAUDE.md design and profile boundary enforcement strategy changes significantly. Worth flagging before anything else is locked.