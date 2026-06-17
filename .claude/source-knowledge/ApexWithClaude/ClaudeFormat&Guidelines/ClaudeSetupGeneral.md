Good — the `apex-orchestration` repo doesn't exist yet , which confirms this is truly a pre-build planning session. I have your GitHub identity confirmed as `leela-spec` / AlexOG . Now let me work through the four steps as designed.

---

## Step 1 — What I Understand About Apex

**The system being built:**

- Apex is a human-gated planning-execution-recap loop, not an autonomous agent — the operator is the execution layer, Apex is the scaffolding around human work
    
- The loop is strictly ordered: `PreCapWeek → PreCapNextDay → Execute → FlowRecap → APSU → repeat` — sequence is architectural, not advisory
    
- Four fixed daily flows (F1–F4) map to four real projects/domains; each has three sprints; this is the daily atomic unit
    
- Five mandatory operator gates (G1–G5) mean the system can never "run away" — every stage transition requires explicit human sign-off
    
- The four profiles (alfred, metastrategist, metaoperations, metadetectivecontroller) are **identity/runtime boundaries** — they define _who is talking_, not _what procedure is running_
    
- Procedures are captured as skills, not profiles — this distinction is architecturally locked and must be preserved during integration
    

**The existing knowledge base:**

- 30–40 files organized as: meta-agents, sub-agents, routines/process specs, workflow examples, process ranking
    
- Files are structured with essentials/templates/mistakes/appendices — this is a pre-Claude format that has the right _content_ but wrong _shape_
    
- Files were designed before the operator understood Claude's native primitives (CLAUDE.md, SKILL.md, SOUL.md) — they need translation, not copying
    
- Workflow examples (like MasterOfArts) are concrete, project-specific — these are a different artifact class than the general skill/routine specs
    

**Key integration challenges:**

- Token budget is the primary constraint — 30–40 files cannot be ingested in one Claude Code session; batching strategy is critical
    
- Terminology mismatch: operator's file vocabulary (meta-agent, sub-agent, routine) must be cleanly mapped to Claude primitives before any build begins
    
- The "essentials/templates/mistakes/appendices" structure is a content container — each section may map to a _different_ Claude primitive, not all to the same one
    
- What's missing is as important as what exists — Claude needs certain files (CLAUDE.md root context, SOUL.md profiles) that may not exist yet in any form
    
- Phase 1 (operator preparation) is load-bearing — if files arrive at Claude Code unstructured, the integration will be token-wasteful and error-prone
    

---

## Step 2 — Translation Decisions

## Meta-agent definition (essentials + templates + mistakes + appendices)

**Maps to: `SOUL.md` (primary) + contribution to `CLAUDE.md`**

Reasoning: A meta-agent is an identity boundary with behavioral rules — that is exactly what `SOUL.md` handles in Claude's architecture. The "essentials" section → SOUL.md core directives. "Mistakes" → SOUL.md anti-patterns/constraints. "Templates" are not identity — they become standalone artifact templates or SKILL.md components. "Appendices" → likely CLAUDE.md footnotes or deferred reference files.

_However: I need to confirm whether you have one SOUL.md per profile or one combined SOUL.md. See Q4 in Step 3._

## Sub-agent definition (same structure)

**Maps to: SKILL.md (primary) + artifact templates as separate files**

Reasoning: Sub-agents in your system appear to be specialized functional procedures, not identity boundaries. A sub-agent that handles "flow recap" is a repeatable procedure, not a persona — it belongs in SKILL.md format. The "essentials" → SKILL.md procedure spec. "Templates" → separate `templates/` markdown files referenced by the skill. "Mistakes" → SKILL.md anti-patterns section. "Appendices" → inline or linked reference.

_Exception: If any sub-agent definition contains behavioral/identity content (voice, stance, persistent rules), that portion migrates to the owning profile's SOUL.md._

## Routine/process spec (PreCapNextDay, FlowRecap, APSU, etc.)

**Maps to: SKILL.md (one per named routine)**

Reasoning: These are the six skill candidates you already identified. Each is a repeatable, invocable procedure with defined inputs, outputs, and decision logic. SKILL.md is exactly the right home. Each SKILL.md should have: trigger condition, inputs required, step-by-step procedure, output format, operator gate(s) involved, error/edge cases.

The existing "process spec" documents become the source material — they are not copied verbatim but restructured into SKILL.md format during Phase 1 operator prep.

## Workflow example (MasterOfArts concrete example)

**Maps to: `examples/` directory — project-scoped reference files, not SKILL.md**

Reasoning: Workflow examples are neither identity definitions nor reusable procedures — they are grounding context. Claude Code benefits from having one reference example per project to calibrate the system against real data. These should live in `context/examples/` or `projects/[name]/example-run.md`. They are read-once orientation material for Claude, not invoked at runtime.

## Process ranking/prioritization file

**Maps to: Contribution to `CLAUDE.md` (root) — a `PRIORITIES.md` or `BUILD_ORDER.md` section**

Reasoning: Process ranking is operator-level meta-information about what to build and in what order. It belongs in the root CLAUDE.md so Claude Code sees it at project open. Alternatively, a standalone `PRIORITIES.md` file that CLAUDE.md references. This is not a SKILL.md (not a procedure) and not a SOUL.md (not identity). It is build-order governance.

---

## Step 3 — Clarifying Questions

## A. Questions about the existing files

**Q1.** Are your 30–40 files currently in one folder (flat), or already in some folder hierarchy? If hierarchical, what does that structure look like right now?

**Q2.** Do your existing files use a consistent internal header format (e.g. `## Essentials`, `## Templates`, `## Mistakes`, `## Appendices`)? Or does the heading structure vary file to file?

**Q3.** Are the "meta-agent" files one file per agent, or is one file potentially defining multiple agents? Same question for sub-agents.

**Q4.** For the four profiles (alfred, metastrategist, metaoperations, metadetectivecontroller) — do you have explicit files for each, or are profile definitions currently scattered inside other files (process specs, routines, etc.)?

**Q5.** Do any of your existing files contain project-specific content (e.g. MasterOfArts client data, Leela feature lists) mixed in with reusable procedure logic? Or is project-specific content already cleanly separated?

**Q6.** You mentioned "process ranking and prioritization" as a file type — is this a single file or multiple? Does it rank skills by build priority, by runtime frequency, or both?

**Q7.** Do you have any existing YAML files? If so, what are they currently used for — configs, state tracking, something else?

**Q8.** The "workflow examples" — are these actual past run records (historical), or illustrative examples written to explain the system (synthetic documentation)? This changes how they should be treated.

**Q9.** Do your files reference each other by name/ID (internal links or cross-references)? If so, will renaming files during Phase 1 break those references?

**Q10.** What is the approximate token count of your longest single file? I need to know if any individual file exceeds what Claude Code can ingest in one shot.

---

## B. Questions about Claude Code usage

**Q11.** How are you currently using Claude Code — are you running it in a local terminal via `claude` CLI, or through some other interface? This affects how CLAUDE.md is loaded and what file path conventions matter.

**Q12.** When you open a Claude Code session on the `apex-orchestration` repo, do you plan to give it a fresh context window each session (stateless), or do you expect Claude Code to maintain meaningful state between sessions via CLAUDE.md + project files alone?

**Q13.** Do you use `claude --continue` or resumable sessions, or do you start fresh each time? This determines how much "re-onboarding" content needs to be in CLAUDE.md.

**Q14.** Will Claude Code be the _only_ AI surface working in this repo, or will you also be running Hermes, API calls, or other Claude interfaces against the same files? This is critical for deciding what CLAUDE.md should assume about the runtime environment.

**Q15.** When you run a skill (e.g. FlowRecap), do you intend to invoke it by typing a command/trigger phrase to Claude Code directly, or by feeding it a structured prompt packet file? I need to understand the invocation model.

---

## C. Questions about repo setup

**Q16.** The repo `apex-orchestration` does not yet exist on GitHub under `leela-spec` . Do you want me to factor that into the plan — i.e., should repo creation be Step 0 of Phase 1? Or do you have a local repo already that isn't pushed?

**Q17.** Will this repo be private (it should be — it contains your planning state)? And will it ever have branches, or is `main` the single working branch for v0.1?

**Q18.** Where will your 30–40 existing files live before Phase 1 conversion? Are they on your local machine, in Notion, in another repo, in Google Drive? This determines the operator's preparation workflow.

**Q19.** Do you want `current.md` (the live project state file that APSU writes) to live at repo root, or inside a `projects/[name]/` folder? The location affects how Claude Code finds and updates it.

**Q20.** Will the artifact index (tracking what was produced in each flow) be a separate file, or embedded inside `current.md`? I need to understand the state model before designing the file structure.

---

## D. Questions about priorities

**Q21.** What is your personal definition of "the system is working" — what is the first real use-case you want to run end-to-end? Is it one full day (PreCapNextDay → 4 flows → APSU), or something smaller like a single FlowRecap?

**Q22.** Of the six skill candidates, which one would you run first in a real session? That skill should be built and tested first, regardless of the logical build order.

**Q23.** For v0.1 — do all four flows (F1–F4) need to work from day one, or can you ship with F3 (Apex/Hermes) working and the others as stubs?

**Q24.** You listed `prompt-and-ai-routing-planning` as a skill candidate — this sounds like it routes which AI surface to use for which prompt. Is this a skill Claude Code runs, or a meta-document the operator consults? If Claude Code runs it, what does "routing" produce — a recommendation, a file, a prompt template?

**Q25.** Is there a deadline or forcing function for getting Phase 1 done? Knowing whether you have 2 days or 2 weeks changes how aggressive the batching strategy should be.

---

## E. Other blocking questions

**Q26.** In the `rawflowdump` — what format does this take in practice? Is it a pasted transcript, a voice-to-text dump, bullet notes, or a structured form? This determines what the FlowRecap skill needs to handle as input.

**Q27.** You mention "model usage delta tracking" as a skill candidate. Is this tracking token costs, which model was used per task, both, or something else? And is this for personal awareness or for system optimization decisions?

**Q28.** The APSU produces `nextPreCapNextDayinputcontext` — is this a file written to the repo, or a prompt block constructed at runtime and handed directly to the next PreCapNextDay session? This is a key state-persistence question.

**Q29.** When you say "profiles are identity/runtime boundaries" — in Claude Code's actual execution, do you plan to enforce this by having separate CLAUDE.md files per profile directory, by using `--profile` flags, or by manually switching context prompts? I want to make sure the profile architecture maps to something technically real in your setup.

**Q30.** Is Hermes (referenced in F3) a separate Claude instance, a separate tool, or a subsystem of Apex? I want to be precise about what "F3 = Apex/Hermes" means for the repo structure — does Hermes have its own files, or is it a role Apex plays?

---

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