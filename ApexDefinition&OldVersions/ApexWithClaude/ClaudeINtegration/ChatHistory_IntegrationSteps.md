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

Prepared using Claude Sonnet 4.6 Thinking

So I just got, uh, Claude subscription, and I want to now create the files and the skill databases only. Uh, please. Completely, eliminate any understanding of the agents. Um, Claude is working differently, so we are only going to focus on the skill. Um, Skill database, um. Development. And. I. Now need a. Guide. Lines on how to do that. So I already defined a lot of different. Skills and templates and organization. Ahead of the integration. I know I want to. Um. Use. That Already predefined workflows and stuff like that for only creating the. Um. Apex orchestration. So. All the. Flows and sprints are only going to focus on that for now. And we will add the other projects later. Um, yeah, this is it. How do I now. Do the first steps? As a little reminder, I will create a new. Repo that is only going to host the Apex orchestration system where Claude is going to live in. And, um, this is going to be the project I want Claude to have access to that repo and work in it locally. And. Uh, I want to create that. Um, exact— Um. I want to create that exact, um, Yeah, workflow system just for that project. So give me a step-by-step system. On how I'm now feeding Claude with that goal and what you need to know. So I ask a lot of questions to really—really nail your understanding, and thereby your. Guidance. Um, at best, let's start with the questions and answers first. And, uh, then you create your step-by-ste

I have full context from your space files — the validated skill package best practices, defect inventories, and your prior audit cycles. I know exactly what you've already built and where the gaps are. Now let me run the question battery before giving you the step-by-step.

---

## What I Understand Right Now (State Check)

From your files, you have already:

- A complete best-practice spec for SKILL.md format[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/0b371272-4664-4703-a065-aa8efa6db970/Claude_Skill_Package_BestPractice_Handover.md?AWSAccessKeyId=ASIA2F3EMEYE3SI3KZE7&Signature=yAPMP4t97Qzz2PZ4cth7cDLXWMA%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIDM8XIPDfI8Z869g%2FHR1OBfChO3zPzxs0aqMPZyBagsQAiEAwfVPPKiSf9xCOHxNSaEkXHo85RaQYqX2eFK06x3qN3Qq%2FAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDIQjvKZ1gl7dHb5%2BaCrQBFK1NrYjKCDbq5PmziXL5frN1tFc9S%2BnmcUB33je8%2FiCn23zVdL46ZgxqJX%2F7J2DdfGOhEhDGL5nEycEsX69Hmo%2FDvXUm0%2BKe1Pmqnmg9kHSGcmCKjvtEqardmBIgfBi3MQjTegPf%2BsjCo7LX3eU0FcI%2B1Hl4nLkY3buuPZpmB2wBO7O5D2erWXXiNXdnujGsjF55LZA%2FaxEXja3Gfd41lMIYLQ6%2FWpvbj6islRUt16qwRsC6hTc%2FTF9vHuJ7pcZts0m3DH9Pzdhmz5lbUl%2BL9XEARd0bS48wR803UEW5tpj3IoyYZb618dTdcPAbeODfyaRfuAk2ca6qHimP1%2FpdwTcEC7oqCulNoTgCfBZiMf3MAP3fLnqDbvL8SJEOHsTR7KmUZ2KN9%2Fmb4LJrsRYm5Kz8qVWj7xl95zgKOLGzKyrGkmarsmrNq17dsAFHBOuF3ClmVcDzz%2F5hc6oqBDXotZHnROW5enmbzkBhJeFl2sgiw6GuMx%2B4q9QQ6f3dbDLSLDKzXYs4Q2FO1N6iFo5cWA5vrIJTqIeFZ9bIgbqpBgYgPzqOqrB8jTs9MWaJeTK9ECts5%2FJYleeW6TgQh6XEC1pxNrjr%2FfifbTmuYfd6rjInBG27WQEx9JVFihN185cpSGrdGAXqf0LwA6zua3WPuOeO2J0Zazki0vh2mYK%2BK4PufLnWsPBrnDJ3JGoKOYzGRFnTaSR7FsU9zEMzbe7hnVe%2BDWUh1dNHd5BxuGBHuUYWQBwug0muUIQwX5WzMAWHQ2a4fxH4%2F0Crg9lCtxitNUwlefK0QY6mAEUDOJ3UWGiWpNQzYLSMLtyfkhHaWS%2FnKmXnfYIdxRb6qlreMNrlE0lGOGSMU7iJ2%2BAVfMUDpkkJj8SESzwdeQIq7a%2BGlYrtyLkkfM1oXxCrf5FtvwUcZ3JLFn%2FP7TwUBKKMINipEfZa9Fk2ozt%2BTrc%2FuZRliw3VE%2F%2BJcxz1UH48bdINwUNU6iwo%2BgZpdcsv6nq3FNTmPKsPA%3D%3D&Expires=1781711208)
    
- A validated prompt flow design guide for generating skill packages[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/96a9f696-553a-479a-b4e3-8ac0ee0e8234/Claude_Skill_PromptFlow_Design_Guidance_v1.md?AWSAccessKeyId=ASIA2F3EMEYE3SI3KZE7&Signature=BR5AAro%2BRpOZr6XkVsm9eEuawQA%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIDM8XIPDfI8Z869g%2FHR1OBfChO3zPzxs0aqMPZyBagsQAiEAwfVPPKiSf9xCOHxNSaEkXHo85RaQYqX2eFK06x3qN3Qq%2FAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDIQjvKZ1gl7dHb5%2BaCrQBFK1NrYjKCDbq5PmziXL5frN1tFc9S%2BnmcUB33je8%2FiCn23zVdL46ZgxqJX%2F7J2DdfGOhEhDGL5nEycEsX69Hmo%2FDvXUm0%2BKe1Pmqnmg9kHSGcmCKjvtEqardmBIgfBi3MQjTegPf%2BsjCo7LX3eU0FcI%2B1Hl4nLkY3buuPZpmB2wBO7O5D2erWXXiNXdnujGsjF55LZA%2FaxEXja3Gfd41lMIYLQ6%2FWpvbj6islRUt16qwRsC6hTc%2FTF9vHuJ7pcZts0m3DH9Pzdhmz5lbUl%2BL9XEARd0bS48wR803UEW5tpj3IoyYZb618dTdcPAbeODfyaRfuAk2ca6qHimP1%2FpdwTcEC7oqCulNoTgCfBZiMf3MAP3fLnqDbvL8SJEOHsTR7KmUZ2KN9%2Fmb4LJrsRYm5Kz8qVWj7xl95zgKOLGzKyrGkmarsmrNq17dsAFHBOuF3ClmVcDzz%2F5hc6oqBDXotZHnROW5enmbzkBhJeFl2sgiw6GuMx%2B4q9QQ6f3dbDLSLDKzXYs4Q2FO1N6iFo5cWA5vrIJTqIeFZ9bIgbqpBgYgPzqOqrB8jTs9MWaJeTK9ECts5%2FJYleeW6TgQh6XEC1pxNrjr%2FfifbTmuYfd6rjInBG27WQEx9JVFihN185cpSGrdGAXqf0LwA6zua3WPuOeO2J0Zazki0vh2mYK%2BK4PufLnWsPBrnDJ3JGoKOYzGRFnTaSR7FsU9zEMzbe7hnVe%2BDWUh1dNHd5BxuGBHuUYWQBwug0muUIQwX5WzMAWHQ2a4fxH4%2F0Crg9lCtxitNUwlefK0QY6mAEUDOJ3UWGiWpNQzYLSMLtyfkhHaWS%2FnKmXnfYIdxRb6qlreMNrlE0lGOGSMU7iJ2%2BAVfMUDpkkJj8SESzwdeQIq7a%2BGlYrtyLkkfM1oXxCrf5FtvwUcZ3JLFn%2FP7TwUBKKMINipEfZa9Fk2ozt%2BTrc%2FuZRliw3VE%2F%2BJcxz1UH48bdINwUNU6iwo%2BgZpdcsv6nq3FNTmPKsPA%3D%3D&Expires=1781711208)
    
- A full audit cycle on `project-status-overview` (v1→v3, scores 6.0→9.3 avg)
    
- All 15 defect patterns documented with fixes[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/96a9f696-553a-479a-b4e3-8ac0ee0e8234/Claude_Skill_PromptFlow_Design_Guidance_v1.md?AWSAccessKeyId=ASIA2F3EMEYE3SI3KZE7&Signature=BR5AAro%2BRpOZr6XkVsm9eEuawQA%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIDM8XIPDfI8Z869g%2FHR1OBfChO3zPzxs0aqMPZyBagsQAiEAwfVPPKiSf9xCOHxNSaEkXHo85RaQYqX2eFK06x3qN3Qq%2FAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDIQjvKZ1gl7dHb5%2BaCrQBFK1NrYjKCDbq5PmziXL5frN1tFc9S%2BnmcUB33je8%2FiCn23zVdL46ZgxqJX%2F7J2DdfGOhEhDGL5nEycEsX69Hmo%2FDvXUm0%2BKe1Pmqnmg9kHSGcmCKjvtEqardmBIgfBi3MQjTegPf%2BsjCo7LX3eU0FcI%2B1Hl4nLkY3buuPZpmB2wBO7O5D2erWXXiNXdnujGsjF55LZA%2FaxEXja3Gfd41lMIYLQ6%2FWpvbj6islRUt16qwRsC6hTc%2FTF9vHuJ7pcZts0m3DH9Pzdhmz5lbUl%2BL9XEARd0bS48wR803UEW5tpj3IoyYZb618dTdcPAbeODfyaRfuAk2ca6qHimP1%2FpdwTcEC7oqCulNoTgCfBZiMf3MAP3fLnqDbvL8SJEOHsTR7KmUZ2KN9%2Fmb4LJrsRYm5Kz8qVWj7xl95zgKOLGzKyrGkmarsmrNq17dsAFHBOuF3ClmVcDzz%2F5hc6oqBDXotZHnROW5enmbzkBhJeFl2sgiw6GuMx%2B4q9QQ6f3dbDLSLDKzXYs4Q2FO1N6iFo5cWA5vrIJTqIeFZ9bIgbqpBgYgPzqOqrB8jTs9MWaJeTK9ECts5%2FJYleeW6TgQh6XEC1pxNrjr%2FfifbTmuYfd6rjInBG27WQEx9JVFihN185cpSGrdGAXqf0LwA6zua3WPuOeO2J0Zazki0vh2mYK%2BK4PufLnWsPBrnDJ3JGoKOYzGRFnTaSR7FsU9zEMzbe7hnVe%2BDWUh1dNHd5BxuGBHuUYWQBwug0muUIQwX5WzMAWHQ2a4fxH4%2F0Crg9lCtxitNUwlefK0QY6mAEUDOJ3UWGiWpNQzYLSMLtyfkhHaWS%2FnKmXnfYIdxRb6qlreMNrlE0lGOGSMU7iJ2%2BAVfMUDpkkJj8SESzwdeQIq7a%2BGlYrtyLkkfM1oXxCrf5FtvwUcZ3JLFn%2FP7TwUBKKMINipEfZa9Fk2ozt%2BTrc%2FuZRliw3VE%2F%2BJcxz1UH48bdINwUNU6iwo%2BgZpdcsv6nq3FNTmPKsPA%3D%3D&Expires=1781711208)
    

**What's now changing:** Agent model dropped. Scope narrowed to Apex/F3 only. Goal is building the skill database inside a new Claude Code repo, with Claude as the local operator inside that repo.

---

## Clarifying Questions — Answer These First

**Group A — Scope of the skill database**

**Q1.** How many skills have you pre-defined for Apex/F3? Give me a count and the names if you have them. This determines batching sequence.

**Q2.** For each skill — do you already have the content written (procedure logic, inputs, outputs) in your existing files, or do you only have names/descriptions? I need to know if Phase 1 is "convert existing content" or "generate from scratch."

**Q3.** Does "skill database" mean only the `.claude/skills/` packages (SKILL.md + references + templates), or does it also include a CLAUDE.md that indexes and activates them? The root CLAUDE.md is load-bearing — without it, Claude Code won't know the skills exist.

**Group B — Repo and Claude Code setup**

**Q4.** Have you created the `apex-orchestration` repo yet, or is that Step 0? And is it local-only first, or GitHub-first?

**Q5.** Are you running Claude Code via `claude` CLI in terminal on your local machine, or through the Claude.ai Projects + files interface? This changes how CLAUDE.md is loaded and how skills are invoked.

**Q6.** Will you invoke skills by typing a trigger phrase to Claude Code directly (e.g. _"run flow-recap"_), or by feeding it a structured input file? The invocation model determines what the CLAUDE.md routing section needs to say.

**Group C — Your existing files**

**Q7.** The 30–40 files from the previous session — are they on your local machine now, in Notion, or somewhere else? And have any of them already been converted to SKILL.md format, or are they all still in the old essentials/templates/mistakes/appendices structure?

**Q8.** Do any of your pre-defined skills overlap with the `project-status-overview` skill you already built and audited? For example, does "status-merge" or "APSU" overlap with what that skill does? I want to avoid rebuilding something you already have at v3 quality.

**Group D — Generation workflow**

**Q9.** For the new Apex skills — do you want to use the same GPT-driven prompt flow (from `Claude_Skill_PromptFlow_Design_Guidance_v1.md`) to _generate_ each skill package, and then commit them to the repo? Or will you generate them directly inside Claude Code? These are two different workflows with different token economics.

**Q10.** What is your definition of "done" for the skill database? Is it: all skills exist as files in the repo? Or: Claude Code can successfully invoke at least one skill end-to-end in a test session?

---

Once you answer these — especially Q1, Q3, Q5, and Q9 — I'll give you the exact ordered step-by-step with no ambiguity. The questions I already have answers for (SKILL.md format rules, defect patterns, quality thresholds) won't slow us down at all since those are already validated in your files.

Prepared using Claude Sonnet 4.6 Thinking

So first of all, I— You. Said a quote-code repo. What I want to be precise about: I will create a repo in GitHub to work on the orchestration system. I want a. Claude. To be connected to that and. Work on that on. The local clone of that repo. I hope you understood that. Question one: I think 6 to 7. There are— All. Kinds of different skills— It's basically the flow that I already described. I'll attach a document for you to understand what it is: Q2. Yes, it's basically all already written. Defined. Sometimes the templates and outputs are missing, but we have both a. Huge flow description with a lot of details, as also already. Pre-defined. Files. That have been created as a. Claude best practice. Q3, the skill database is most. The individual skills, not the full Claude MD file. Q4, yes, the Apex orchestration repo exists. And it is a local and. Online GitHub, so— I would say it's— Local, local-first, but sometimes it's online, sometimes it's local. It's both, I would say. Q5. I don't know. Tell me what is best. Q6. Yes, I will use Trigger Phrases. Q7. They are also already in the repo, as a reference. Q8. No, they don't overlap. Project status overview is one of those skills. Q9. Yes, I would like to use the GPT to generate what Claude code needs, so Claude code can concentrate. On the verification, the integration, um. And the actual running of the system. Thereby, uh, splitting the token, uh, resources. Q10. Um, that. We. Go through the skills and actually use it. So, um, I want the whole system that I have attached so executing each step, getting verified outputs and use it to orchestrate my work in a test run, then reiterating

WeeklyRoutine_Overview_Marco-Meso.md

All answers received. Full context digested. I now have everything I need. Here is the complete step-by-step system.

---

## State of Play — What's Confirmed

|Item|Status|
|---|---|
|Repo `apex-orchestration`|Exists, local + GitHub|
|Skills|6–7, all from the loop in [](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/03ecdb33-7d3d-474f-aece-ac901e7e661d/WeeklyRoutine_Overview_Marco-Meso.md?AWSAccessKeyId=ASIA2F3EMEYEXXGFC65M&Signature=F5m3B%2BVbGySJJcPsE5q%2FuHJfjio%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIE1RIJ9CxumCqnjm2JBl7%2BVGHm5%2B1Wzf%2ByC9Em3bPY%2B9AiEAvCnEuU6uF%2FO6dzGWuIrqVsPo1v8yDyalcrj65cZ4Rv4q%2FAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDKdRMHEc2HeNhB2HvCrQBBNu3dP8YcC7J98GPOKs%2BhCuP6p6xxYCoXO%2BRGpoShV3jN%2BeUvGAeA6YJTfguG76PleJ5PsyoorhEj7TLe2sVvZgcNsKPXLdnza4Uok%2BmH91lsWIq%2BptHJpA6bfLdDEPgZnib5JIvW%2Bfe7HI46BtBMfeNIep6vfaV4Ifix04X7x353hvgMIN6oRPFipPXXCtk605FMt%2BVUVk29i4RAs1uzOEyuaH3AlcT8wJz9sJF2QdPIjAndnQLPe7t3%2B8QYHi%2FgNjXlINHx28M0ZoruTsZS7Lj8vwVyB%2Bnw5zpA6hsit7gF9kT04DR3EoqCXzLXByOsI0iXLMpwim1TfutG9vrfyujoN%2B82IJ%2FyBI8xaXS%2FE%2FjDqLb8FPcfjnXVaTvnWRqbQCymKEs4NU%2BVkP4Xa0%2BBX0hBR80wBLX0KKNF4yICjb6k0%2BdNPww%2Bj2RmXRT1NhzLFCzCu6NOvTukHE5YH%2BEgtW6LrifCnW0qp9evZtHZwU%2Bb1zcRAxOEQkAJH6kC7Bo1fbidl4fQCfWrNPb9OCgQB%2BHha6k8AulykywIPKNfXWZnyGy2EgFax3XUmnwxHz0ymJgSOCseDf6KReFa4x513wUhONeTn5ydszAdGPoClknaa5DTxZhSXWYwFrev%2BLC1QW79ShGDNg7JxR%2FhgivzRZOH0GfXnCzj9iNZ7a6NvMrs4vUk9hYC5ZZbiybLLpH8EexPoRbbSGenRLbX9eMlnIfgAnT5z0Q2OLXhpOxwovItv0Jh7o6Hf2074V518WhCK35otABcpp5GSh1EZSY6swxefK0QY6mAGtfaRVl4bVW0nyLdB2mO0dyz%2F69aZgyJHHVh2nH4R%2FuO3UL%2B0lR7tCzdcmqFqOAuYY4dXpkKoSUt1%2BRoOTe3zAOsP%2BWwU4fMTe0fWZAhioyjF2J%2FxtbTwSX%2FvkEf%2BDfcloQIH1T8rjsSaKnVy9%2B6RkIHFCaNlt8tVk2BYgaZxeWM7z65lVB4ObtU1X0LiFUlwc9hTxnD1Pjg%3D%3D&Expires=1781711256)|
|Content ready|Yes — logic written, some templates/outputs missing|
|Existing files in repo|Yes — as reference material already|
|`project-status-overview`|Already built (v3), no overlap|
|Invocation model|Trigger phrases to Claude Code|
|Generation split|GPT generates SKILL packages → Claude Code integrates + runs|
|Done =|Full test run of the loop, iterated until it works|

---

## The 6–7 Skills — Confirmed Inventory

From, these are your skill packages to build:[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/03ecdb33-7d3d-474f-aece-ac901e7e661d/WeeklyRoutine_Overview_Marco-Meso.md?AWSAccessKeyId=ASIA2F3EMEYEXXGFC65M&Signature=F5m3B%2BVbGySJJcPsE5q%2FuHJfjio%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIE1RIJ9CxumCqnjm2JBl7%2BVGHm5%2B1Wzf%2ByC9Em3bPY%2B9AiEAvCnEuU6uF%2FO6dzGWuIrqVsPo1v8yDyalcrj65cZ4Rv4q%2FAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDKdRMHEc2HeNhB2HvCrQBBNu3dP8YcC7J98GPOKs%2BhCuP6p6xxYCoXO%2BRGpoShV3jN%2BeUvGAeA6YJTfguG76PleJ5PsyoorhEj7TLe2sVvZgcNsKPXLdnza4Uok%2BmH91lsWIq%2BptHJpA6bfLdDEPgZnib5JIvW%2Bfe7HI46BtBMfeNIep6vfaV4Ifix04X7x353hvgMIN6oRPFipPXXCtk605FMt%2BVUVk29i4RAs1uzOEyuaH3AlcT8wJz9sJF2QdPIjAndnQLPe7t3%2B8QYHi%2FgNjXlINHx28M0ZoruTsZS7Lj8vwVyB%2Bnw5zpA6hsit7gF9kT04DR3EoqCXzLXByOsI0iXLMpwim1TfutG9vrfyujoN%2B82IJ%2FyBI8xaXS%2FE%2FjDqLb8FPcfjnXVaTvnWRqbQCymKEs4NU%2BVkP4Xa0%2BBX0hBR80wBLX0KKNF4yICjb6k0%2BdNPww%2Bj2RmXRT1NhzLFCzCu6NOvTukHE5YH%2BEgtW6LrifCnW0qp9evZtHZwU%2Bb1zcRAxOEQkAJH6kC7Bo1fbidl4fQCfWrNPb9OCgQB%2BHha6k8AulykywIPKNfXWZnyGy2EgFax3XUmnwxHz0ymJgSOCseDf6KReFa4x513wUhONeTn5ydszAdGPoClknaa5DTxZhSXWYwFrev%2BLC1QW79ShGDNg7JxR%2FhgivzRZOH0GfXnCzj9iNZ7a6NvMrs4vUk9hYC5ZZbiybLLpH8EexPoRbbSGenRLbX9eMlnIfgAnT5z0Q2OLXhpOxwovItv0Jh7o6Hf2074V518WhCK35otABcpp5GSh1EZSY6swxefK0QY6mAGtfaRVl4bVW0nyLdB2mO0dyz%2F69aZgyJHHVh2nH4R%2FuO3UL%2B0lR7tCzdcmqFqOAuYY4dXpkKoSUt1%2BRoOTe3zAOsP%2BWwU4fMTe0fWZAhioyjF2J%2FxtbTwSX%2FvkEf%2BDfcloQIH1T8rjsSaKnVy9%2B6RkIHFCaNlt8tVk2BYgaZxeWM7z65lVB4ObtU1X0LiFUlwc9hTxnD1Pjg%3D%3D&Expires=1781711256)

|#|Skill name (kebab-case)|Loop stage|
|---|---|---|
|1|`precap-week`|Stage 1|
|2|`precap-next-day`|Stage 2|
|3|`raw-flow-dump-normalize`|Stage 4|
|4|`flow-recap`|Stage 5|
|5|`model-usage-log`|Stage 6|
|6|`status-merge`|Stage 7 (APSU)|
|+1|`project-status-overview`|Already built at v3 ✅|

**Note:** Stage 3 (OperatorExecutesPlannedFlow) is human-only — no skill needed, only a RawFlowDump template.

---

## Recommended Claude Code Setup (Q5 Answer)

Use **Claude Code via CLI** (`claude` in terminal, pointed at your local clone of `apex-orchestration`). This is optimal because:

- CLAUDE.md is auto-loaded at project open — Claude always has full context[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/0b371272-4664-4703-a065-aa8efa6db970/Claude_Skill_Package_BestPractice_Handover.md?AWSAccessKeyId=ASIA2F3EMEYEXXGFC65M&Signature=Ifwu19ES0nlcg9pYVmUm6mUVUEk%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIE1RIJ9CxumCqnjm2JBl7%2BVGHm5%2B1Wzf%2ByC9Em3bPY%2B9AiEAvCnEuU6uF%2FO6dzGWuIrqVsPo1v8yDyalcrj65cZ4Rv4q%2FAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDKdRMHEc2HeNhB2HvCrQBBNu3dP8YcC7J98GPOKs%2BhCuP6p6xxYCoXO%2BRGpoShV3jN%2BeUvGAeA6YJTfguG76PleJ5PsyoorhEj7TLe2sVvZgcNsKPXLdnza4Uok%2BmH91lsWIq%2BptHJpA6bfLdDEPgZnib5JIvW%2Bfe7HI46BtBMfeNIep6vfaV4Ifix04X7x353hvgMIN6oRPFipPXXCtk605FMt%2BVUVk29i4RAs1uzOEyuaH3AlcT8wJz9sJF2QdPIjAndnQLPe7t3%2B8QYHi%2FgNjXlINHx28M0ZoruTsZS7Lj8vwVyB%2Bnw5zpA6hsit7gF9kT04DR3EoqCXzLXByOsI0iXLMpwim1TfutG9vrfyujoN%2B82IJ%2FyBI8xaXS%2FE%2FjDqLb8FPcfjnXVaTvnWRqbQCymKEs4NU%2BVkP4Xa0%2BBX0hBR80wBLX0KKNF4yICjb6k0%2BdNPww%2Bj2RmXRT1NhzLFCzCu6NOvTukHE5YH%2BEgtW6LrifCnW0qp9evZtHZwU%2Bb1zcRAxOEQkAJH6kC7Bo1fbidl4fQCfWrNPb9OCgQB%2BHha6k8AulykywIPKNfXWZnyGy2EgFax3XUmnwxHz0ymJgSOCseDf6KReFa4x513wUhONeTn5ydszAdGPoClknaa5DTxZhSXWYwFrev%2BLC1QW79ShGDNg7JxR%2FhgivzRZOH0GfXnCzj9iNZ7a6NvMrs4vUk9hYC5ZZbiybLLpH8EexPoRbbSGenRLbX9eMlnIfgAnT5z0Q2OLXhpOxwovItv0Jh7o6Hf2074V518WhCK35otABcpp5GSh1EZSY6swxefK0QY6mAGtfaRVl4bVW0nyLdB2mO0dyz%2F69aZgyJHHVh2nH4R%2FuO3UL%2B0lR7tCzdcmqFqOAuYY4dXpkKoSUt1%2BRoOTe3zAOsP%2BWwU4fMTe0fWZAhioyjF2J%2FxtbTwSX%2FvkEf%2BDfcloQIH1T8rjsSaKnVy9%2B6RkIHFCaNlt8tVk2BYgaZxeWM7z65lVB4ObtU1X0LiFUlwc9hTxnD1Pjg%3D%3D&Expires=1781711256)
    
- Trigger phrases work natively in the CLI chat interface
    
- You edit files locally, push to GitHub when stable
    
- Claude Code reads/writes files directly — no copy-paste overhead
    

Setup: `cd ~/path/to/apex-orchestration && claude`

---

## Step-by-Step System

## Phase 0 — Repo Scaffolding (One-Time, Do Once Before Anything Else)

**Step 0.1 — Create CLAUDE.md at repo root**

This is the single most important file. Claude reads it on every session open. It must contain:

- What Apex is (2 sentences)
    
- The 6-stage loop (compressed YAML, copy from `compressed_meso_chain`)[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/03ecdb33-7d3d-474f-aece-ac901e7e661d/WeeklyRoutine_Overview_Marco-Meso.md?AWSAccessKeyId=ASIA2F3EMEYEXXGFC65M&Signature=F5m3B%2BVbGySJJcPsE5q%2FuHJfjio%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIE1RIJ9CxumCqnjm2JBl7%2BVGHm5%2B1Wzf%2ByC9Em3bPY%2B9AiEAvCnEuU6uF%2FO6dzGWuIrqVsPo1v8yDyalcrj65cZ4Rv4q%2FAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDKdRMHEc2HeNhB2HvCrQBBNu3dP8YcC7J98GPOKs%2BhCuP6p6xxYCoXO%2BRGpoShV3jN%2BeUvGAeA6YJTfguG76PleJ5PsyoorhEj7TLe2sVvZgcNsKPXLdnza4Uok%2BmH91lsWIq%2BptHJpA6bfLdDEPgZnib5JIvW%2Bfe7HI46BtBMfeNIep6vfaV4Ifix04X7x353hvgMIN6oRPFipPXXCtk605FMt%2BVUVk29i4RAs1uzOEyuaH3AlcT8wJz9sJF2QdPIjAndnQLPe7t3%2B8QYHi%2FgNjXlINHx28M0ZoruTsZS7Lj8vwVyB%2Bnw5zpA6hsit7gF9kT04DR3EoqCXzLXByOsI0iXLMpwim1TfutG9vrfyujoN%2B82IJ%2FyBI8xaXS%2FE%2FjDqLb8FPcfjnXVaTvnWRqbQCymKEs4NU%2BVkP4Xa0%2BBX0hBR80wBLX0KKNF4yICjb6k0%2BdNPww%2Bj2RmXRT1NhzLFCzCu6NOvTukHE5YH%2BEgtW6LrifCnW0qp9evZtHZwU%2Bb1zcRAxOEQkAJH6kC7Bo1fbidl4fQCfWrNPb9OCgQB%2BHha6k8AulykywIPKNfXWZnyGy2EgFax3XUmnwxHz0ymJgSOCseDf6KReFa4x513wUhONeTn5ydszAdGPoClknaa5DTxZhSXWYwFrev%2BLC1QW79ShGDNg7JxR%2FhgivzRZOH0GfXnCzj9iNZ7a6NvMrs4vUk9hYC5ZZbiybLLpH8EexPoRbbSGenRLbX9eMlnIfgAnT5z0Q2OLXhpOxwovItv0Jh7o6Hf2074V518WhCK35otABcpp5GSh1EZSY6swxefK0QY6mAGtfaRVl4bVW0nyLdB2mO0dyz%2F69aZgyJHHVh2nH4R%2FuO3UL%2B0lR7tCzdcmqFqOAuYY4dXpkKoSUt1%2BRoOTe3zAOsP%2BWwU4fMTe0fWZAhioyjF2J%2FxtbTwSX%2FvkEf%2BDfcloQIH1T8rjsSaKnVy9%2B6RkIHFCaNlt8tVk2BYgaZxeWM7z65lVB4ObtU1X0LiFUlwc9hTxnD1Pjg%3D%3D&Expires=1781711256)
    
- Skill index: each skill name + trigger phrase + file path
    
- Operator gate list (G1–G5)
    
- What Claude Code is allowed to do in this repo (write skill files, read reference files, run skills on request — nothing else)
    
- The invocation pattern: `"run [skill-name]"` → Claude loads `.claude/skills/[skill-name]/SKILL.md` and executes
    

Do not write this yet. This is what you'll give GPT to generate in Phase 1.

**Step 0.2 — Create repo folder structure** (manually, takes 2 minutes)

text

`apex-orchestration/   CLAUDE.md  .claude/    skills/      precap-week/      precap-next-day/      raw-flow-dump-normalize/      flow-recap/      model-usage-log/      status-merge/    templates/      raw-flow-dump-template.md      skipped-flow-marker-template.md  state/    apex-project-status.md        ← APSU writes here    consumed-recap-registry.md    ← APSU dedup log  artifacts/    [weekly-plan-packets/]    [next-day-plans/]    [flow-recap-packets/]  reference/    WeeklyRoutine_Overview_Marco-Meso.md   ← already exists, move here`

**Step 0.3 — Commit skeleton to GitHub**

Push empty folders (with `.gitkeep` files) + CLAUDE.md stub. This becomes the base. Every skill package you add is one commit per package.

---

## Phase 1 — GPT Generates Each Skill Package (Per Skill, Repeat 6x)

This is the token-split strategy: GPT does the generation work, Claude Code does the verification and runtime work.[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/96a9f696-553a-479a-b4e3-8ac0ee0e8234/Claude_Skill_PromptFlow_Design_Guidance_v1.md?AWSAccessKeyId=ASIA2F3EMEYEXXGFC65M&Signature=ShsCnGbbcp3no9IJfLNGPfRRVJQ%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIE1RIJ9CxumCqnjm2JBl7%2BVGHm5%2B1Wzf%2ByC9Em3bPY%2B9AiEAvCnEuU6uF%2FO6dzGWuIrqVsPo1v8yDyalcrj65cZ4Rv4q%2FAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDKdRMHEc2HeNhB2HvCrQBBNu3dP8YcC7J98GPOKs%2BhCuP6p6xxYCoXO%2BRGpoShV3jN%2BeUvGAeA6YJTfguG76PleJ5PsyoorhEj7TLe2sVvZgcNsKPXLdnza4Uok%2BmH91lsWIq%2BptHJpA6bfLdDEPgZnib5JIvW%2Bfe7HI46BtBMfeNIep6vfaV4Ifix04X7x353hvgMIN6oRPFipPXXCtk605FMt%2BVUVk29i4RAs1uzOEyuaH3AlcT8wJz9sJF2QdPIjAndnQLPe7t3%2B8QYHi%2FgNjXlINHx28M0ZoruTsZS7Lj8vwVyB%2Bnw5zpA6hsit7gF9kT04DR3EoqCXzLXByOsI0iXLMpwim1TfutG9vrfyujoN%2B82IJ%2FyBI8xaXS%2FE%2FjDqLb8FPcfjnXVaTvnWRqbQCymKEs4NU%2BVkP4Xa0%2BBX0hBR80wBLX0KKNF4yICjb6k0%2BdNPww%2Bj2RmXRT1NhzLFCzCu6NOvTukHE5YH%2BEgtW6LrifCnW0qp9evZtHZwU%2Bb1zcRAxOEQkAJH6kC7Bo1fbidl4fQCfWrNPb9OCgQB%2BHha6k8AulykywIPKNfXWZnyGy2EgFax3XUmnwxHz0ymJgSOCseDf6KReFa4x513wUhONeTn5ydszAdGPoClknaa5DTxZhSXWYwFrev%2BLC1QW79ShGDNg7JxR%2FhgivzRZOH0GfXnCzj9iNZ7a6NvMrs4vUk9hYC5ZZbiybLLpH8EexPoRbbSGenRLbX9eMlnIfgAnT5z0Q2OLXhpOxwovItv0Jh7o6Hf2074V518WhCK35otABcpp5GSh1EZSY6swxefK0QY6mAGtfaRVl4bVW0nyLdB2mO0dyz%2F69aZgyJHHVh2nH4R%2FuO3UL%2B0lR7tCzdcmqFqOAuYY4dXpkKoSUt1%2BRoOTe3zAOsP%2BWwU4fMTe0fWZAhioyjF2J%2FxtbTwSX%2FvkEf%2BDfcloQIH1T8rjsSaKnVy9%2B6RkIHFCaNlt8tVk2BYgaZxeWM7z65lVB4ObtU1X0LiFUlwc9hTxnD1Pjg%3D%3D&Expires=1781711256)

**For each skill, follow this exact sequence:**

**Step 1.1 — Feed GPT the binding decisions block**

Before GPT writes any file, give it:

text

`binding_decisions:   skill_name: [skill-name]  trigger_phrase: "run [skill-name]"  primary_input: [from file:7 inputs YAML for this stage]  primary_output: [from file:7 outputs YAML for this stage]  operator_gate: [G1–G5 relevant gate]  source_content: [paste the relevant stage section from WeeklyRoutine_Overview_Marco-Meso.md]  canonical_key_names:    [define here — align with existing keys from file:7]`

**Step 1.2 — Run GPT Prompt Flow (start at Prompt 1, never Prompt 0)**[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/96a9f696-553a-479a-b4e3-8ac0ee0e8234/Claude_Skill_PromptFlow_Design_Guidance_v1.md?AWSAccessKeyId=ASIA2F3EMEYEXXGFC65M&Signature=ShsCnGbbcp3no9IJfLNGPfRRVJQ%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIE1RIJ9CxumCqnjm2JBl7%2BVGHm5%2B1Wzf%2ByC9Em3bPY%2B9AiEAvCnEuU6uF%2FO6dzGWuIrqVsPo1v8yDyalcrj65cZ4Rv4q%2FAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDKdRMHEc2HeNhB2HvCrQBBNu3dP8YcC7J98GPOKs%2BhCuP6p6xxYCoXO%2BRGpoShV3jN%2BeUvGAeA6YJTfguG76PleJ5PsyoorhEj7TLe2sVvZgcNsKPXLdnza4Uok%2BmH91lsWIq%2BptHJpA6bfLdDEPgZnib5JIvW%2Bfe7HI46BtBMfeNIep6vfaV4Ifix04X7x353hvgMIN6oRPFipPXXCtk605FMt%2BVUVk29i4RAs1uzOEyuaH3AlcT8wJz9sJF2QdPIjAndnQLPe7t3%2B8QYHi%2FgNjXlINHx28M0ZoruTsZS7Lj8vwVyB%2Bnw5zpA6hsit7gF9kT04DR3EoqCXzLXByOsI0iXLMpwim1TfutG9vrfyujoN%2B82IJ%2FyBI8xaXS%2FE%2FjDqLb8FPcfjnXVaTvnWRqbQCymKEs4NU%2BVkP4Xa0%2BBX0hBR80wBLX0KKNF4yICjb6k0%2BdNPww%2Bj2RmXRT1NhzLFCzCu6NOvTukHE5YH%2BEgtW6LrifCnW0qp9evZtHZwU%2Bb1zcRAxOEQkAJH6kC7Bo1fbidl4fQCfWrNPb9OCgQB%2BHha6k8AulykywIPKNfXWZnyGy2EgFax3XUmnwxHz0ymJgSOCseDf6KReFa4x513wUhONeTn5ydszAdGPoClknaa5DTxZhSXWYwFrev%2BLC1QW79ShGDNg7JxR%2FhgivzRZOH0GfXnCzj9iNZ7a6NvMrs4vUk9hYC5ZZbiybLLpH8EexPoRbbSGenRLbX9eMlnIfgAnT5z0Q2OLXhpOxwovItv0Jh7o6Hf2074V518WhCK35otABcpp5GSh1EZSY6swxefK0QY6mAGtfaRVl4bVW0nyLdB2mO0dyz%2F69aZgyJHHVh2nH4R%2FuO3UL%2B0lR7tCzdcmqFqOAuYY4dXpkKoSUt1%2BRoOTe3zAOsP%2BWwU4fMTe0fWZAhioyjF2J%2FxtbTwSX%2FvkEf%2BDfcloQIH1T8rjsSaKnVy9%2B6RkIHFCaNlt8tVk2BYgaZxeWM7z65lVB4ObtU1X0LiFUlwc9hTxnD1Pjg%3D%3D&Expires=1781711256)

GPT generates in this order per package:

1. `SKILL.md` — entrypoint, trigger phrase, 5–8 step procedure
    
2. `references/[skill]-contract.md` — output schema, field contracts
    
3. `references/[skill]-validation-rules.md` — ranking, failure modes (full)
    
4. `templates/[skill]-output-template.md` — blank copy-paste output
    
5. `examples/[skill]-example.md` — filled synthetic example
    
6. `package-manifest.md` — index only, under 60 lines
    

**Step 1.3 — Run pre-acceptance checklist on each file**[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/0b371272-4664-4703-a065-aa8efa6db970/Claude_Skill_Package_BestPractice_Handover.md?AWSAccessKeyId=ASIA2F3EMEYEXXGFC65M&Signature=Ifwu19ES0nlcg9pYVmUm6mUVUEk%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIE1RIJ9CxumCqnjm2JBl7%2BVGHm5%2B1Wzf%2ByC9Em3bPY%2B9AiEAvCnEuU6uF%2FO6dzGWuIrqVsPo1v8yDyalcrj65cZ4Rv4q%2FAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDKdRMHEc2HeNhB2HvCrQBBNu3dP8YcC7J98GPOKs%2BhCuP6p6xxYCoXO%2BRGpoShV3jN%2BeUvGAeA6YJTfguG76PleJ5PsyoorhEj7TLe2sVvZgcNsKPXLdnza4Uok%2BmH91lsWIq%2BptHJpA6bfLdDEPgZnib5JIvW%2Bfe7HI46BtBMfeNIep6vfaV4Ifix04X7x353hvgMIN6oRPFipPXXCtk605FMt%2BVUVk29i4RAs1uzOEyuaH3AlcT8wJz9sJF2QdPIjAndnQLPe7t3%2B8QYHi%2FgNjXlINHx28M0ZoruTsZS7Lj8vwVyB%2Bnw5zpA6hsit7gF9kT04DR3EoqCXzLXByOsI0iXLMpwim1TfutG9vrfyujoN%2B82IJ%2FyBI8xaXS%2FE%2FjDqLb8FPcfjnXVaTvnWRqbQCymKEs4NU%2BVkP4Xa0%2BBX0hBR80wBLX0KKNF4yICjb6k0%2BdNPww%2Bj2RmXRT1NhzLFCzCu6NOvTukHE5YH%2BEgtW6LrifCnW0qp9evZtHZwU%2Bb1zcRAxOEQkAJH6kC7Bo1fbidl4fQCfWrNPb9OCgQB%2BHha6k8AulykywIPKNfXWZnyGy2EgFax3XUmnwxHz0ymJgSOCseDf6KReFa4x513wUhONeTn5ydszAdGPoClknaa5DTxZhSXWYwFrev%2BLC1QW79ShGDNg7JxR%2FhgivzRZOH0GfXnCzj9iNZ7a6NvMrs4vUk9hYC5ZZbiybLLpH8EexPoRbbSGenRLbX9eMlnIfgAnT5z0Q2OLXhpOxwovItv0Jh7o6Hf2074V518WhCK35otABcpp5GSh1EZSY6swxefK0QY6mAGtfaRVl4bVW0nyLdB2mO0dyz%2F69aZgyJHHVh2nH4R%2FuO3UL%2B0lR7tCzdcmqFqOAuYY4dXpkKoSUt1%2BRoOTe3zAOsP%2BWwU4fMTe0fWZAhioyjF2J%2FxtbTwSX%2FvkEf%2BDfcloQIH1T8rjsSaKnVy9%2B6RkIHFCaNlt8tVk2BYgaZxeWM7z65lVB4ObtU1X0LiFUlwc9hTxnD1Pjg%3D%3D&Expires=1781711256)

Before accepting any GPT output, check the top-5 most frequent defects from your audit history:[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/7dfafa97-1b4d-4110-80bb-8cf041b562fa/FB_Claude.md?AWSAccessKeyId=ASIA2F3EMEYEXXGFC65M&Signature=qBf4JovkiTo8cZoHR%2BKJ8ZYh%2B7Y%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIE1RIJ9CxumCqnjm2JBl7%2BVGHm5%2B1Wzf%2ByC9Em3bPY%2B9AiEAvCnEuU6uF%2FO6dzGWuIrqVsPo1v8yDyalcrj65cZ4Rv4q%2FAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDKdRMHEc2HeNhB2HvCrQBBNu3dP8YcC7J98GPOKs%2BhCuP6p6xxYCoXO%2BRGpoShV3jN%2BeUvGAeA6YJTfguG76PleJ5PsyoorhEj7TLe2sVvZgcNsKPXLdnza4Uok%2BmH91lsWIq%2BptHJpA6bfLdDEPgZnib5JIvW%2Bfe7HI46BtBMfeNIep6vfaV4Ifix04X7x353hvgMIN6oRPFipPXXCtk605FMt%2BVUVk29i4RAs1uzOEyuaH3AlcT8wJz9sJF2QdPIjAndnQLPe7t3%2B8QYHi%2FgNjXlINHx28M0ZoruTsZS7Lj8vwVyB%2Bnw5zpA6hsit7gF9kT04DR3EoqCXzLXByOsI0iXLMpwim1TfutG9vrfyujoN%2B82IJ%2FyBI8xaXS%2FE%2FjDqLb8FPcfjnXVaTvnWRqbQCymKEs4NU%2BVkP4Xa0%2BBX0hBR80wBLX0KKNF4yICjb6k0%2BdNPww%2Bj2RmXRT1NhzLFCzCu6NOvTukHE5YH%2BEgtW6LrifCnW0qp9evZtHZwU%2Bb1zcRAxOEQkAJH6kC7Bo1fbidl4fQCfWrNPb9OCgQB%2BHha6k8AulykywIPKNfXWZnyGy2EgFax3XUmnwxHz0ymJgSOCseDf6KReFa4x513wUhONeTn5ydszAdGPoClknaa5DTxZhSXWYwFrev%2BLC1QW79ShGDNg7JxR%2FhgivzRZOH0GfXnCzj9iNZ7a6NvMrs4vUk9hYC5ZZbiybLLpH8EexPoRbbSGenRLbX9eMlnIfgAnT5z0Q2OLXhpOxwovItv0Jh7o6Hf2074V518WhCK35otABcpp5GSh1EZSY6swxefK0QY6mAGtfaRVl4bVW0nyLdB2mO0dyz%2F69aZgyJHHVh2nH4R%2FuO3UL%2B0lR7tCzdcmqFqOAuYY4dXpkKoSUt1%2BRoOTe3zAOsP%2BWwU4fMTe0fWZAhioyjF2J%2FxtbTwSX%2FvkEf%2BDfcloQIH1T8rjsSaKnVy9%2B6RkIHFCaNlt8tVk2BYgaZxeWM7z65lVB4ObtU1X0LiFUlwc9hTxnD1Pjg%3D%3D&Expires=1781711256)

- `description` starts with `"Use this skill when"` ✓
    
- All YAML blocks have 2-space indentation (not collapsed) ✓
    
- Numeric constraints use `type/min/max` not string labels ✓
    
- No schema defined in more than one file ✓
    
- `supporting_files` is a YAML block with `read_when` conditions ✓
    

**Step 1.4 — Save files to repo** under `.claude/skills/[skill-name]/`

Commit after each skill package passes the checklist. One commit per package.

---

## Phase 2 — Claude Code Integration (One Session Per Batch)

**Recommended skill build order** (dependency chain from ):[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/03ecdb33-7d3d-474f-aece-ac901e7e661d/WeeklyRoutine_Overview_Marco-Meso.md?AWSAccessKeyId=ASIA2F3EMEYEXXGFC65M&Signature=F5m3B%2BVbGySJJcPsE5q%2FuHJfjio%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIE1RIJ9CxumCqnjm2JBl7%2BVGHm5%2B1Wzf%2ByC9Em3bPY%2B9AiEAvCnEuU6uF%2FO6dzGWuIrqVsPo1v8yDyalcrj65cZ4Rv4q%2FAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDKdRMHEc2HeNhB2HvCrQBBNu3dP8YcC7J98GPOKs%2BhCuP6p6xxYCoXO%2BRGpoShV3jN%2BeUvGAeA6YJTfguG76PleJ5PsyoorhEj7TLe2sVvZgcNsKPXLdnza4Uok%2BmH91lsWIq%2BptHJpA6bfLdDEPgZnib5JIvW%2Bfe7HI46BtBMfeNIep6vfaV4Ifix04X7x353hvgMIN6oRPFipPXXCtk605FMt%2BVUVk29i4RAs1uzOEyuaH3AlcT8wJz9sJF2QdPIjAndnQLPe7t3%2B8QYHi%2FgNjXlINHx28M0ZoruTsZS7Lj8vwVyB%2Bnw5zpA6hsit7gF9kT04DR3EoqCXzLXByOsI0iXLMpwim1TfutG9vrfyujoN%2B82IJ%2FyBI8xaXS%2FE%2FjDqLb8FPcfjnXVaTvnWRqbQCymKEs4NU%2BVkP4Xa0%2BBX0hBR80wBLX0KKNF4yICjb6k0%2BdNPww%2Bj2RmXRT1NhzLFCzCu6NOvTukHE5YH%2BEgtW6LrifCnW0qp9evZtHZwU%2Bb1zcRAxOEQkAJH6kC7Bo1fbidl4fQCfWrNPb9OCgQB%2BHha6k8AulykywIPKNfXWZnyGy2EgFax3XUmnwxHz0ymJgSOCseDf6KReFa4x513wUhONeTn5ydszAdGPoClknaa5DTxZhSXWYwFrev%2BLC1QW79ShGDNg7JxR%2FhgivzRZOH0GfXnCzj9iNZ7a6NvMrs4vUk9hYC5ZZbiybLLpH8EexPoRbbSGenRLbX9eMlnIfgAnT5z0Q2OLXhpOxwovItv0Jh7o6Hf2074V518WhCK35otABcpp5GSh1EZSY6swxefK0QY6mAGtfaRVl4bVW0nyLdB2mO0dyz%2F69aZgyJHHVh2nH4R%2FuO3UL%2B0lR7tCzdcmqFqOAuYY4dXpkKoSUt1%2BRoOTe3zAOsP%2BWwU4fMTe0fWZAhioyjF2J%2FxtbTwSX%2FvkEf%2BDfcloQIH1T8rjsSaKnVy9%2B6RkIHFCaNlt8tVk2BYgaZxeWM7z65lVB4ObtU1X0LiFUlwc9hTxnD1Pjg%3D%3D&Expires=1781711256)

|Order|Skill|Why first|
|---|---|---|
|1|`flow-recap`|Most atomic, tests the dump→memory path|
|2|`raw-flow-dump-normalize`|Gate input for flow-recap|
|3|`status-merge`|Reads flow-recap output — needs it stable first|
|4|`precap-next-day`|Reads status-merge output|
|5|`precap-week`|Reads precap-next-day upstream|
|6|`model-usage-log`|Non-blocking, add last|

**Claude Code session instruction template** (use at start of every session):

text

`Read CLAUDE.md first. Then read .claude/skills/[skill-name]/SKILL.md. Confirm your understanding of: trigger phrase, inputs, outputs, operator gate. Do not execute anything yet. Confirm in bullet points.`

After confirmation: `"run [skill-name]"` with a synthetic input → verify output against contract.

---

## Phase 3 — Test Run (End-to-End Loop)

**Minimum viable test sequence:**

1. `run precap-week` → synthetic project state input → get `weekly_plan_packet`
    
2. Operator approves (G1)
    
3. `run precap-next-day` → feed `weekly_plan_packet` → get `next_day_plan` + 4 flow packets
    
4. Operator approves (G2)
    
5. Simulate F3 execution manually → write a `raw_flow_dump` by hand
    
6. Operator marks flow done (G3)
    
7. `run raw-flow-dump-normalize` → normalize the dump
    
8. `run flow-recap` → get `flow_recap_packet`
    
9. Operator validates next step (G4)
    
10. `run status-merge` → get updated `apex-project-status.md`
    
11. Operator reviews if conflicts (G5)
    

**Done signal:** `apex-project-status.md` correctly reflects what happened in step 5. All 5 gates fired. No skill produced prose where structured output was required.

**Iterate:** If any output fails the gate, identify which SKILL.md section produced the defect, fix it (via GPT re-gen of that file only), re-run from that step.

---

## Two Remaining Questions Before You Start

**Q-A.** For CLAUDE.md — do you want me to generate the full CLAUDE.md now (content ready, you paste it into the repo), or do you want to run it through GPT in Phase 1 alongside the skill packages?

**Q-B.** The `raw-flow-dump-normalize` stage — is this a standalone invocable skill (you type `run raw-flow-dump-normalize`), or is it a sub-step that `flow-recap` handles internally? Your file describes it as its own stage (Stage 4) with its own normalization rule, so I'd lean toward standalone — but confirm before I lock the skill count at 6 vs 7.[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/03ecdb33-7d3d-474f-aece-ac901e7e661d/WeeklyRoutine_Overview_Marco-Meso.md?AWSAccessKeyId=ASIA2F3EMEYEXXGFC65M&Signature=F5m3B%2BVbGySJJcPsE5q%2FuHJfjio%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIE1RIJ9CxumCqnjm2JBl7%2BVGHm5%2B1Wzf%2ByC9Em3bPY%2B9AiEAvCnEuU6uF%2FO6dzGWuIrqVsPo1v8yDyalcrj65cZ4Rv4q%2FAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDKdRMHEc2HeNhB2HvCrQBBNu3dP8YcC7J98GPOKs%2BhCuP6p6xxYCoXO%2BRGpoShV3jN%2BeUvGAeA6YJTfguG76PleJ5PsyoorhEj7TLe2sVvZgcNsKPXLdnza4Uok%2BmH91lsWIq%2BptHJpA6bfLdDEPgZnib5JIvW%2Bfe7HI46BtBMfeNIep6vfaV4Ifix04X7x353hvgMIN6oRPFipPXXCtk605FMt%2BVUVk29i4RAs1uzOEyuaH3AlcT8wJz9sJF2QdPIjAndnQLPe7t3%2B8QYHi%2FgNjXlINHx28M0ZoruTsZS7Lj8vwVyB%2Bnw5zpA6hsit7gF9kT04DR3EoqCXzLXByOsI0iXLMpwim1TfutG9vrfyujoN%2B82IJ%2FyBI8xaXS%2FE%2FjDqLb8FPcfjnXVaTvnWRqbQCymKEs4NU%2BVkP4Xa0%2BBX0hBR80wBLX0KKNF4yICjb6k0%2BdNPww%2Bj2RmXRT1NhzLFCzCu6NOvTukHE5YH%2BEgtW6LrifCnW0qp9evZtHZwU%2Bb1zcRAxOEQkAJH6kC7Bo1fbidl4fQCfWrNPb9OCgQB%2BHha6k8AulykywIPKNfXWZnyGy2EgFax3XUmnwxHz0ymJgSOCseDf6KReFa4x513wUhONeTn5ydszAdGPoClknaa5DTxZhSXWYwFrev%2BLC1QW79ShGDNg7JxR%2FhgivzRZOH0GfXnCzj9iNZ7a6NvMrs4vUk9hYC5ZZbiybLLpH8EexPoRbbSGenRLbX9eMlnIfgAnT5z0Q2OLXhpOxwovItv0Jh7o6Hf2074V518WhCK35otABcpp5GSh1EZSY6swxefK0QY6mAGtfaRVl4bVW0nyLdB2mO0dyz%2F69aZgyJHHVh2nH4R%2FuO3UL%2B0lR7tCzdcmqFqOAuYY4dXpkKoSUt1%2BRoOTe3zAOsP%2BWwU4fMTe0fWZAhioyjF2J%2FxtbTwSX%2FvkEf%2BDfcloQIH1T8rjsSaKnVy9%2B6RkIHFCaNlt8tVk2BYgaZxeWM7z65lVB4ObtU1X0LiFUlwc9hTxnD1Pjg%3D%3D&Expires=1781711256)

Prepared using Claude Sonnet 4.6 Thinking

Uh, you are, uh, master AI orchest. Rate. Uh, in Claude. Task? I. Want a step-by-step plan on how to develop. My skill database. And orchestration layer only for the project of defining Apex— Orchestration. System. Only with Claude, no Hermes, no Open Claw, and. I want to use a. External GPT and Claude— Uh. Frontier. Models. To not waste tokens and let— Uh. Claude code do only the integration and. Um. Actual out test outputs. Um, for that, I want you to read. The. Repo and tell me what to do next. Um, I think next—uh, the next most important thing for me to do is define the. Uh, templates of the pre-cap next day, because they are still missing. Then. Fulfill the skill database of Flow Recap. And. Then fill. The. Uh, repo. With. Actual project content. I wonder where all of my research. Uh. That I already did. Needs to be placed and how it's actually getting transformed into. Uh. Token efficient machine readable. Um. Best. Practice workflows. Uh, you can ask as many questions as you need to create that step-by-step. Step. System. Uh, for me, the most important thing is that we build it step-by-step and. That. We use the other frontier models as much as possible to not waste tokens inside of the Claude subscription.

Completed 3 steps

Good — full picture now. Let me map what exists vs. what's needed before giving you the questions.

---

## Repo State Audit

## `.claude/skills/` — 6 folders present

|Folder name|Maps to which skill|Status unknown|
|---|---|---|
|`PrecapNextDay`|`precap-next-day`|Need to inspect|
|`PrecapWeek`|`precap-week`|Need to inspect|
|`ProjectStatus`|`project-status-overview`|Likely v3 ✅|
|`AIRouting`|Not in our 7-skill list|❓ extra or legacy|
|`PromptEngineer`|Not in our 7-skill list|❓ extra or legacy|
|`Workflow&Processes`|Not in our 7-skill list|❓ extra or legacy|

**Missing from skills folder:** `flow-recap`, `raw-flow-dump-normalize`, `status-merge`, `model-usage-log`

## `ApexDefinition&OldVersions/` — 3 subfolders

|Folder|Purpose|
|---|---|
|`ApexDefiniton`|Architecture definitions|
|`ApexWithClaude`|Claude-specific design docs|
|`OldApexSkill&AgentDataBase`|Legacy skill/agent database|

This maps exactly to `source-knowledge/` — it's already in the right place structurally, just needs renaming/reorganizing later (non-urgent) .

---

## Clarifying Questions — Answer These, Then I Build the Plan

## Group 1 — Skill Package Contents (Critical)

**Q1.** Inside `PrecapNextDay/` and `PrecapWeek/` — are there actual SKILL.md files inside, or are these empty folders? (You can check on GitHub directly or tell me to read them.)

**Q2.** The three extra skill folders — `AIRouting`, `PromptEngineer`, `Workflow&Processes` — are these active skills you want to keep, convert, or delete? Or are they legacy and belong in `ApexDefinition&OldVersions/`?

**Q3.** You said PrecapNextDay templates are still missing. Do you mean: (a) the SKILL.md exists but the `templates/` subfolder inside the package is empty, or (b) the entire PrecapNextDay skill package is incomplete/missing content?

## Group 2 — FlowRecap Status

**Q4.** For `flow-recap` — does any version of this skill exist anywhere in the repo (even as a draft or old format file), or does it need to be built from scratch using the meso loop definition in ?[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/03ecdb33-7d3d-474f-aece-ac901e7e661d/WeeklyRoutine_Overview_Marco-Meso.md?AWSAccessKeyId=ASIA2F3EMEYE4SD3KGQX&Signature=9XtucKO3eP3MoxeizKSoElAue1g%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCdhhM%2BDCB3EjsLq5i%2FgLyEYYnwSyt5Q0AVQSFZaN3H2QIgJP6xC0PDa5lGEUFJ%2ByHg%2BxHH7oOIg1YP8zTRGFxkKmAq%2FAQIkf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDPETfbQyF%2FWdD1YsiirQBHRULDZUBFbYzbtI4j7bqyB96cEKB%2BJY%2B52t5RIYvnTdBoTCK56CznjYzD66%2FDi0%2BYga5ZG4ZaCCur2jv%2FSQNhNTobiIZ721HXzY2ZcjUcqn804chIkeizWF1fSPVihezcwwqGiNlZtMZQMpygVMQWST7qEMeR1Rsh3uunbDORLG3jQnAxYftyRYM7PHh353t9924EYbbwQ73QwaLNqfkc7GPCI5rHOHM1g%2Bp%2BjeFCD%2BilYhzkKEURZVEvtPBY%2BqUkIunDoK3HRjKb09C19gvN4HCFGn9vkX4AVgitO7FKIsUzezFRRZubU8U7uyLVh4Tw8HFvp1hM18NyaDiww26LcrDLLt0YmTvva8wHWHEx%2BFlEFpqkgatqJ4C80A4NUBGZtlKRoyE6aniUYRtbWeyoS%2B7vOUAdFaMiT9Qq%2FDP2wdwxgO7gdf7djNeUs3CCKXvidy72mGtoKE1NhN8CKpiNaNOkixCP9o7MJPLY%2FrQuNPAICCcerjwq%2FQmlfD3kDkNK%2BY92hE%2FSOnKqKqi%2FCzeQFijZrawcrw%2FeorJA4XdDGcBk3TNU2mewSpCjtIcQMTxN3VeIT5vdDsiDis1z0Ud43AyEudYWw8i2KsX65s5n5EoDvNMXKX3p4eCOv2G1KpJ8fpECBUWthrZ3LPPjr3pKgqX%2BABsP1Ejd9PmBgYVPkztvbjSzUQslh63tFoVBToh6I6qnkm7FY%2FNrBNVmgjvRgZx8IRKjr2PiRtWz201lhKijFYDNk8P2%2BXfX%2BaLhljIi4Hz78mfc5blYOdE%2FNzccAwwvzK0QY6mAEA9YNsZc7QU8w%2BT0JWnggNeXUM8N45W3JyhARPO%2BSrjz05lob90psJldu9TkiJKkL6b6PMp97aaq3Cdy1OeCkberTLRlTUq%2BHvBJmg0pWivfqFBUJA0YuRh3L4bVcKeMnUdCWplo4MOBd1kJoNnLo518po8wOKFp1BH12%2BRlw4afJ%2FRcIMwQDgLkkyvk1qNO0XJsyK8APqTA%3D%3D&Expires=1781713941)

**Q5.** Same question for `status-merge` (APSU) and `raw-flow-dump-normalize` — scratch builds or partial drafts exist somewhere?

## Group 3 — Research Content Placement

**Q6.** The research you already did — what format is it in right now? Options:

- Notion pages
    
- Markdown files already in the repo (which folder?)
    
- Local files not yet pushed to GitHub
    
- Mixed
    

**Q7.** Does `ApexDefinition&OldVersions/ApexWithClaude/` contain the Claude-specific architecture decisions that should become the source material for CLAUDE.md generation? Or is that folder something else?

## Group 4 — Token Split Workflow Confirmation

**Q8.** Confirm the split model you want:

- **GPT (frontier, external):** generates all SKILL.md packages, templates, reference files, CLAUDE.md — from source material
    
- **Claude Code (local):** integration only — reads generated files, validates structure, runs test invocations, writes to `state/` and `artifacts/`
    
- **This Perplexity Space:** planning, audit, prompt design, step-by-step coordination
    

Is that correct, or do you want Claude Code to also do some generation?

**Q9.** Is there a `CLAUDE.md` file at repo root yet? I didn't see one in the root listing — confirm.

---

Answer these 9 questions and I build you the exact ordered execution plan with no gaps.

Prepared using Claude Sonnet 4.6 Thinking

Uh, Q1, all skills have actual skill files. Q2. They are actual— Very central skills— Q3. Uh, yes, the skill MD file exists, but the templates do not. Um, and shouldn't you be able to see all that through a repro access? Uh, I'm confused why you ask for things you could answer yourself. Q4. Uh, we. Do not have a skill for that yet. We need to define it. Uh, so this is a core to-do, most likely. Q5. Same. As Q4. Q6. Uh, it's mostly markdown files and it's in the, uh. Apex old definition and versions folder. Uh, yes, validated. Q8 validated. Um, Q9, uh. I already— I'm. Already designing a. Claude file, but it's not ready yet. Uh, it is also a to-do.

Full picture. I have everything I need now. Here is the complete diagnosis and step-by-step plan.

---

## Repo Diagnosis — What Actually Exists

## `PrecapNextDay/` — Heavily populated but structurally broken

|File|Problem|
|---|---|
|`Skill_precap-next-day.md`|✅ SKILL.md exists|
|`Audit_SKILL.md_pecap-next-day.md`|⚠️ Audit file sitting loose in package root — belongs outside or deleted|
|`TEmplates/` folder|⚠️ Exists but empty (your Q3 confirmed) — templates missing|
|`FirstIteration/` folder|⚠️ Legacy draft folder sitting inside active package — wrong location|
|`daily-plan-output-contract (2).md`|⚠️ Filename has `(2)` and spaces — naming defect, not canonical|
|`flow-prompt-pack-contract (2).md`|⚠️ Same issue|
|`usage-tracking-dependency-contract (2).md`|⚠️ Same issue|
|`input-intake-and-resilience-contract (2).md`|⚠️ Same issue|
|`validation-checklist.md`|⚠️ Standalone checklist file — should be embedded in reference file, not loose|
|`PreCap Next Day — Example Operator Output.md`|✅ Example exists — good|
|`calendar-event-write-contract.md`|✅ Contract file|
|`flow-packet-contract.md`|✅ Contract file|
|`prompt-engineering-dependency-contract.md`|✅ Contract file|
|`precap-next-day-package-manifest.md`|✅ Manifest exists|

**Core problems:** (a) `TEmplates/` is empty, (b) `(2)` filenames = copy artifacts that were never cleaned, (c) `FirstIteration/` and `Audit_` file pollute the active package, (d) no `references/` subfolder structure — all contracts are flat at root level.[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/0b371272-4664-4703-a065-aa8efa6db970/Claude_Skill_Package_BestPractice_Handover.md?AWSAccessKeyId=ASIA2F3EMEYE6737QX7A&Signature=brEYObb6lkz%2Br4RuF1BJGbJqj40%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIFBH6js1sEue%2F0NAB7SBrWPn6SeeehUSrX3vxYonGEw6AiEAz9OHBtx0PP9cpRuFwnnCwwG1sPd6CyiYuoFg2L%2BrbC0q%2FAQIkf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDE9bWg%2FMeiyjcVhTbirQBHiwk%2BJ1Op6%2FBbKo17YfLN1pdiB6bPAP3K%2B%2BZksEru6LxaeFoMNKci5pEK7%2B5Agr%2BW1hpATSx5VoI%2FtYJlioNwAvYI8ilAdAIhvSQSNnXcOVkT%2BCWaCVt73zbRLAaORL4DmEvwvnVD5ucNijH0fA%2F0SAwnO%2F6k%2FqP%2F9lqdKxPIRveyW5Na7guu5lt06f5x3pgWhEivwZQRNnlM8bC216rNuvrvJtNsirUMzEMAG5UKP37lo6qPdY5HyU%2BFXCcAGpBms5z68PuIvdJHqkWmSksDwQxbHJVQYRabMzNT1Jf4p1SswU6NyoH05usW4CXw7WFLJSnyDZP%2BnrR7gVLgIzsYmGRRm%2BU4xNHz%2F3pRdWRxE5dztX%2FUAEHk1dL4VkME0qzWiD4F7W9y01Ul7%2F0A6EpN62JOpwUSlA39FIPjtx5eiUgkqR2KVFbPNS2htVLUc2VdrWMdYoP1jesGWca20k%2F5sojJCRzqJKpCqNWp7UAVhXm1G4I7%2Bv3xYTktD3l3mTasKPDxFCepnZTLfdjx0nAl1rfuO0r2AqQPkqcprDI3V4TomH546mJyMOaoDa4R%2FUrgYRpHvzzNzmfXNIf9ADHLQxfjlLNrmxwjqz%2BnYuiyd%2BYJdGeLrXs5KbEcPmBZhblZI8z6WEjUHfc2RZN%2FCfQo3t5UeHPBugrond0FhQ%2Fb7zqZi3Y5zamS29hOKNdgK5SLok4CoAORknVS0kgaZ%2F%2FlNzC6wOCQ3bgQfQ7s0Hmm1mwIfUCw4oVlJxLvt4wlUNQCf0NZe%2FLA0sZcZvANrpNhwwzYzL0QY6mAG6qtk0VBBOY0TFdfZbhilF7PKZW1wYO8OzCe8npel8rZZUFTKJXfQf%2BRQndhkfwb4omGnY6IttabBqRxvFv1TYJbH0bAswaxotKVI%2FQjBu2aqmE68FnIAlff%2F8hXDOw6Z3kQUD359nq9B7giyif%2BPUmjJw6JZ8NbDojbrN9FGDKNYM%2FJHrZQ%2BAC0vmqfVOK1Ia4nuOdOsz5A%3D%3D&Expires=1781716000)

---

## Step-by-Step Execution Plan

## Token split model applied throughout:

- **GPT** = generates file content from source material
    
- **Claude Code** = integration, validation, test runs
    
- **This space** = planning, audit coordination, prompt design
    

---

## Phase 0 — Repo Cleanup (You do manually, 20 min, no AI needed)

**Step 0.1 — Fix `PrecapNextDay/` folder hygiene**

- Move `FirstIteration/` → `ApexDefinition&OldVersions/OldApexSkill&AgentDataBase/PrecapNextDay-v1/`
    
- Move `Audit_SKILL.md_pecap-next-day.md` → same archive location
    
- Rename all `(2)` files: remove the `(2)` suffix — e.g. `daily-plan-output-contract.md`
    
- Create `references/` subfolder inside `PrecapNextDay/` — move all `*-contract.md` and `validation-checklist.md` into it
    
- Result: clean package structure matching best practice[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/0b371272-4664-4703-a065-aa8efa6db970/Claude_Skill_Package_BestPractice_Handover.md?AWSAccessKeyId=ASIA2F3EMEYE6737QX7A&Signature=brEYObb6lkz%2Br4RuF1BJGbJqj40%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIFBH6js1sEue%2F0NAB7SBrWPn6SeeehUSrX3vxYonGEw6AiEAz9OHBtx0PP9cpRuFwnnCwwG1sPd6CyiYuoFg2L%2BrbC0q%2FAQIkf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDE9bWg%2FMeiyjcVhTbirQBHiwk%2BJ1Op6%2FBbKo17YfLN1pdiB6bPAP3K%2B%2BZksEru6LxaeFoMNKci5pEK7%2B5Agr%2BW1hpATSx5VoI%2FtYJlioNwAvYI8ilAdAIhvSQSNnXcOVkT%2BCWaCVt73zbRLAaORL4DmEvwvnVD5ucNijH0fA%2F0SAwnO%2F6k%2FqP%2F9lqdKxPIRveyW5Na7guu5lt06f5x3pgWhEivwZQRNnlM8bC216rNuvrvJtNsirUMzEMAG5UKP37lo6qPdY5HyU%2BFXCcAGpBms5z68PuIvdJHqkWmSksDwQxbHJVQYRabMzNT1Jf4p1SswU6NyoH05usW4CXw7WFLJSnyDZP%2BnrR7gVLgIzsYmGRRm%2BU4xNHz%2F3pRdWRxE5dztX%2FUAEHk1dL4VkME0qzWiD4F7W9y01Ul7%2F0A6EpN62JOpwUSlA39FIPjtx5eiUgkqR2KVFbPNS2htVLUc2VdrWMdYoP1jesGWca20k%2F5sojJCRzqJKpCqNWp7UAVhXm1G4I7%2Bv3xYTktD3l3mTasKPDxFCepnZTLfdjx0nAl1rfuO0r2AqQPkqcprDI3V4TomH546mJyMOaoDa4R%2FUrgYRpHvzzNzmfXNIf9ADHLQxfjlLNrmxwjqz%2BnYuiyd%2BYJdGeLrXs5KbEcPmBZhblZI8z6WEjUHfc2RZN%2FCfQo3t5UeHPBugrond0FhQ%2Fb7zqZi3Y5zamS29hOKNdgK5SLok4CoAORknVS0kgaZ%2F%2FlNzC6wOCQ3bgQfQ7s0Hmm1mwIfUCw4oVlJxLvt4wlUNQCf0NZe%2FLA0sZcZvANrpNhwwzYzL0QY6mAG6qtk0VBBOY0TFdfZbhilF7PKZW1wYO8OzCe8npel8rZZUFTKJXfQf%2BRQndhkfwb4omGnY6IttabBqRxvFv1TYJbH0bAswaxotKVI%2FQjBu2aqmE68FnIAlff%2F8hXDOw6Z3kQUD359nq9B7giyif%2BPUmjJw6JZ8NbDojbrN9FGDKNYM%2FJHrZQ%2BAC0vmqfVOK1Ia4nuOdOsz5A%3D%3D&Expires=1781716000)
    

**Step 0.2 — Create missing top-level folders**

text

`state/   apex-project-status.md         (empty stub)  consumed-recap-registry.md     (empty stub) artifacts/   weekly-plans/  next-day-plans/  flow-packets/  flow-recap-packets/ source-knowledge/   design-docs/                   (move WeeklyRoutine_Overview here if not already)  skill-conversion-queue/    flow-recap/    status-merge/    raw-flow-dump-normalize/`

**Step 0.3 — Rename `TEmplates/` → `templates/`** (capitalisation + typo fix)

---

## Phase 1 — CLAUDE.md (GPT generates, you paste into repo)

**Step 1.1** — In this space: answer the 10 Part-1 questions from the previous CLAUDE.md session (most answers already known — takes 5 min)

**Step 1.2** — Feed GPT: Part-1 answers + Part-2 prompt (from previous session) + `WeeklyRoutine_Overview_Marco-Meso.md`

**Step 1.3** — GPT outputs `CLAUDE.md` → you run pre-acceptance checklist → commit to repo root[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/0b371272-4664-4703-a065-aa8efa6db970/Claude_Skill_Package_BestPractice_Handover.md?AWSAccessKeyId=ASIA2F3EMEYE6737QX7A&Signature=brEYObb6lkz%2Br4RuF1BJGbJqj40%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIFBH6js1sEue%2F0NAB7SBrWPn6SeeehUSrX3vxYonGEw6AiEAz9OHBtx0PP9cpRuFwnnCwwG1sPd6CyiYuoFg2L%2BrbC0q%2FAQIkf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDE9bWg%2FMeiyjcVhTbirQBHiwk%2BJ1Op6%2FBbKo17YfLN1pdiB6bPAP3K%2B%2BZksEru6LxaeFoMNKci5pEK7%2B5Agr%2BW1hpATSx5VoI%2FtYJlioNwAvYI8ilAdAIhvSQSNnXcOVkT%2BCWaCVt73zbRLAaORL4DmEvwvnVD5ucNijH0fA%2F0SAwnO%2F6k%2FqP%2F9lqdKxPIRveyW5Na7guu5lt06f5x3pgWhEivwZQRNnlM8bC216rNuvrvJtNsirUMzEMAG5UKP37lo6qPdY5HyU%2BFXCcAGpBms5z68PuIvdJHqkWmSksDwQxbHJVQYRabMzNT1Jf4p1SswU6NyoH05usW4CXw7WFLJSnyDZP%2BnrR7gVLgIzsYmGRRm%2BU4xNHz%2F3pRdWRxE5dztX%2FUAEHk1dL4VkME0qzWiD4F7W9y01Ul7%2F0A6EpN62JOpwUSlA39FIPjtx5eiUgkqR2KVFbPNS2htVLUc2VdrWMdYoP1jesGWca20k%2F5sojJCRzqJKpCqNWp7UAVhXm1G4I7%2Bv3xYTktD3l3mTasKPDxFCepnZTLfdjx0nAl1rfuO0r2AqQPkqcprDI3V4TomH546mJyMOaoDa4R%2FUrgYRpHvzzNzmfXNIf9ADHLQxfjlLNrmxwjqz%2BnYuiyd%2BYJdGeLrXs5KbEcPmBZhblZI8z6WEjUHfc2RZN%2FCfQo3t5UeHPBugrond0FhQ%2Fb7zqZi3Y5zamS29hOKNdgK5SLok4CoAORknVS0kgaZ%2F%2FlNzC6wOCQ3bgQfQ7s0Hmm1mwIfUCw4oVlJxLvt4wlUNQCf0NZe%2FLA0sZcZvANrpNhwwzYzL0QY6mAG6qtk0VBBOY0TFdfZbhilF7PKZW1wYO8OzCe8npel8rZZUFTKJXfQf%2BRQndhkfwb4omGnY6IttabBqRxvFv1TYJbH0bAswaxotKVI%2FQjBu2aqmE68FnIAlff%2F8hXDOw6Z3kQUD359nq9B7giyif%2BPUmjJw6JZ8NbDojbrN9FGDKNYM%2FJHrZQ%2BAC0vmqfVOK1Ia4nuOdOsz5A%3D%3D&Expires=1781716000)

**Blocker if skipped:** Claude Code has no session context and cannot route skills correctly.

---

## Phase 2 — PrecapNextDay Templates (GPT generates)

This is your stated top priority. After Phase 0 cleanup, the package has SKILL.md + contracts but empty `templates/` folder.

**Step 2.1** — Feed GPT:

- `Skill_precap-next-day.md` (SKILL.md)
    
- `daily-plan-output-contract.md`
    
- `flow-packet-contract.md`
    
- `PreCap Next Day — Example Operator Output.md` (as reference)
    
- Binding instruction: _"Generate the blank operator-facing output template for PrecapNextDay. One template per output artifact: (1) next_day_plan, (2) flow_packet. Follow canonical template rules from."_[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/0b371272-4664-4703-a065-aa8efa6db970/Claude_Skill_Package_BestPractice_Handover.md?AWSAccessKeyId=ASIA2F3EMEYE6737QX7A&Signature=brEYObb6lkz%2Br4RuF1BJGbJqj40%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIFBH6js1sEue%2F0NAB7SBrWPn6SeeehUSrX3vxYonGEw6AiEAz9OHBtx0PP9cpRuFwnnCwwG1sPd6CyiYuoFg2L%2BrbC0q%2FAQIkf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDE9bWg%2FMeiyjcVhTbirQBHiwk%2BJ1Op6%2FBbKo17YfLN1pdiB6bPAP3K%2B%2BZksEru6LxaeFoMNKci5pEK7%2B5Agr%2BW1hpATSx5VoI%2FtYJlioNwAvYI8ilAdAIhvSQSNnXcOVkT%2BCWaCVt73zbRLAaORL4DmEvwvnVD5ucNijH0fA%2F0SAwnO%2F6k%2FqP%2F9lqdKxPIRveyW5Na7guu5lt06f5x3pgWhEivwZQRNnlM8bC216rNuvrvJtNsirUMzEMAG5UKP37lo6qPdY5HyU%2BFXCcAGpBms5z68PuIvdJHqkWmSksDwQxbHJVQYRabMzNT1Jf4p1SswU6NyoH05usW4CXw7WFLJSnyDZP%2BnrR7gVLgIzsYmGRRm%2BU4xNHz%2F3pRdWRxE5dztX%2FUAEHk1dL4VkME0qzWiD4F7W9y01Ul7%2F0A6EpN62JOpwUSlA39FIPjtx5eiUgkqR2KVFbPNS2htVLUc2VdrWMdYoP1jesGWca20k%2F5sojJCRzqJKpCqNWp7UAVhXm1G4I7%2Bv3xYTktD3l3mTasKPDxFCepnZTLfdjx0nAl1rfuO0r2AqQPkqcprDI3V4TomH546mJyMOaoDa4R%2FUrgYRpHvzzNzmfXNIf9ADHLQxfjlLNrmxwjqz%2BnYuiyd%2BYJdGeLrXs5KbEcPmBZhblZI8z6WEjUHfc2RZN%2FCfQo3t5UeHPBugrond0FhQ%2Fb7zqZi3Y5zamS29hOKNdgK5SLok4CoAORknVS0kgaZ%2F%2FlNzC6wOCQ3bgQfQ7s0Hmm1mwIfUCw4oVlJxLvt4wlUNQCf0NZe%2FLA0sZcZvANrpNhwwzYzL0QY6mAG6qtk0VBBOY0TFdfZbhilF7PKZW1wYO8OzCe8npel8rZZUFTKJXfQf%2BRQndhkfwb4omGnY6IttabBqRxvFv1TYJbH0bAswaxotKVI%2FQjBu2aqmE68FnIAlff%2F8hXDOw6Z3kQUD359nq9B7giyif%2BPUmjJw6JZ8NbDojbrN9FGDKNYM%2FJHrZQ%2BAC0vmqfVOK1Ia4nuOdOsz5A%3D%3D&Expires=1781716000)
    

**Step 2.2** — GPT outputs 2 template files → pre-acceptance check → commit to `PrecapNextDay/templates/`

---

## Phase 3 — FlowRecap Skill Package (GPT generates from scratch)

Highest-value missing skill — the loop cannot complete without it.

**Step 3.1** — Place source material in `source-knowledge/skill-conversion-queue/flow-recap/`:

- Copy Stage 5 section from `WeeklyRoutine_Overview_Marco-Meso.md`
    
- Copy any FlowRecap-related files from `ApexDefinition&OldVersions/`
    

**Step 3.2** — Feed GPT the full 7-prompt skill generation flow with `flow-recap` as the target skill and Stage 5 meso definition as source[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/96a9f696-553a-479a-b4e3-8ac0ee0e8234/Claude_Skill_PromptFlow_Design_Guidance_v1.md?AWSAccessKeyId=ASIA2F3EMEYE6737QX7A&Signature=LQOaRwiO7pzVZ5sJa64IUK4VVRI%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIFBH6js1sEue%2F0NAB7SBrWPn6SeeehUSrX3vxYonGEw6AiEAz9OHBtx0PP9cpRuFwnnCwwG1sPd6CyiYuoFg2L%2BrbC0q%2FAQIkf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDE9bWg%2FMeiyjcVhTbirQBHiwk%2BJ1Op6%2FBbKo17YfLN1pdiB6bPAP3K%2B%2BZksEru6LxaeFoMNKci5pEK7%2B5Agr%2BW1hpATSx5VoI%2FtYJlioNwAvYI8ilAdAIhvSQSNnXcOVkT%2BCWaCVt73zbRLAaORL4DmEvwvnVD5ucNijH0fA%2F0SAwnO%2F6k%2FqP%2F9lqdKxPIRveyW5Na7guu5lt06f5x3pgWhEivwZQRNnlM8bC216rNuvrvJtNsirUMzEMAG5UKP37lo6qPdY5HyU%2BFXCcAGpBms5z68PuIvdJHqkWmSksDwQxbHJVQYRabMzNT1Jf4p1SswU6NyoH05usW4CXw7WFLJSnyDZP%2BnrR7gVLgIzsYmGRRm%2BU4xNHz%2F3pRdWRxE5dztX%2FUAEHk1dL4VkME0qzWiD4F7W9y01Ul7%2F0A6EpN62JOpwUSlA39FIPjtx5eiUgkqR2KVFbPNS2htVLUc2VdrWMdYoP1jesGWca20k%2F5sojJCRzqJKpCqNWp7UAVhXm1G4I7%2Bv3xYTktD3l3mTasKPDxFCepnZTLfdjx0nAl1rfuO0r2AqQPkqcprDI3V4TomH546mJyMOaoDa4R%2FUrgYRpHvzzNzmfXNIf9ADHLQxfjlLNrmxwjqz%2BnYuiyd%2BYJdGeLrXs5KbEcPmBZhblZI8z6WEjUHfc2RZN%2FCfQo3t5UeHPBugrond0FhQ%2Fb7zqZi3Y5zamS29hOKNdgK5SLok4CoAORknVS0kgaZ%2F%2FlNzC6wOCQ3bgQfQ7s0Hmm1mwIfUCw4oVlJxLvt4wlUNQCf0NZe%2FLA0sZcZvANrpNhwwzYzL0QY6mAG6qtk0VBBOY0TFdfZbhilF7PKZW1wYO8OzCe8npel8rZZUFTKJXfQf%2BRQndhkfwb4omGnY6IttabBqRxvFv1TYJbH0bAswaxotKVI%2FQjBu2aqmE68FnIAlff%2F8hXDOw6Z3kQUD359nq9B7giyif%2BPUmjJw6JZ8NbDojbrN9FGDKNYM%2FJHrZQ%2BAC0vmqfVOK1Ia4nuOdOsz5A%3D%3D&Expires=1781716000)

**Step 3.3** — GPT generates all 6 files: SKILL.md, contract, rules, template, example, manifest

**Step 3.4** — Audit each file: MR/TE/RS ≥ 8 on all three before accepting[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/0b371272-4664-4703-a065-aa8efa6db970/Claude_Skill_Package_BestPractice_Handover.md?AWSAccessKeyId=ASIA2F3EMEYE6737QX7A&Signature=brEYObb6lkz%2Br4RuF1BJGbJqj40%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIFBH6js1sEue%2F0NAB7SBrWPn6SeeehUSrX3vxYonGEw6AiEAz9OHBtx0PP9cpRuFwnnCwwG1sPd6CyiYuoFg2L%2BrbC0q%2FAQIkf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDE9bWg%2FMeiyjcVhTbirQBHiwk%2BJ1Op6%2FBbKo17YfLN1pdiB6bPAP3K%2B%2BZksEru6LxaeFoMNKci5pEK7%2B5Agr%2BW1hpATSx5VoI%2FtYJlioNwAvYI8ilAdAIhvSQSNnXcOVkT%2BCWaCVt73zbRLAaORL4DmEvwvnVD5ucNijH0fA%2F0SAwnO%2F6k%2FqP%2F9lqdKxPIRveyW5Na7guu5lt06f5x3pgWhEivwZQRNnlM8bC216rNuvrvJtNsirUMzEMAG5UKP37lo6qPdY5HyU%2BFXCcAGpBms5z68PuIvdJHqkWmSksDwQxbHJVQYRabMzNT1Jf4p1SswU6NyoH05usW4CXw7WFLJSnyDZP%2BnrR7gVLgIzsYmGRRm%2BU4xNHz%2F3pRdWRxE5dztX%2FUAEHk1dL4VkME0qzWiD4F7W9y01Ul7%2F0A6EpN62JOpwUSlA39FIPjtx5eiUgkqR2KVFbPNS2htVLUc2VdrWMdYoP1jesGWca20k%2F5sojJCRzqJKpCqNWp7UAVhXm1G4I7%2Bv3xYTktD3l3mTasKPDxFCepnZTLfdjx0nAl1rfuO0r2AqQPkqcprDI3V4TomH546mJyMOaoDa4R%2FUrgYRpHvzzNzmfXNIf9ADHLQxfjlLNrmxwjqz%2BnYuiyd%2BYJdGeLrXs5KbEcPmBZhblZI8z6WEjUHfc2RZN%2FCfQo3t5UeHPBugrond0FhQ%2Fb7zqZi3Y5zamS29hOKNdgK5SLok4CoAORknVS0kgaZ%2F%2FlNzC6wOCQ3bgQfQ7s0Hmm1mwIfUCw4oVlJxLvt4wlUNQCf0NZe%2FLA0sZcZvANrpNhwwzYzL0QY6mAG6qtk0VBBOY0TFdfZbhilF7PKZW1wYO8OzCe8npel8rZZUFTKJXfQf%2BRQndhkfwb4omGnY6IttabBqRxvFv1TYJbH0bAswaxotKVI%2FQjBu2aqmE68FnIAlff%2F8hXDOw6Z3kQUD359nq9B7giyif%2BPUmjJw6JZ8NbDojbrN9FGDKNYM%2FJHrZQ%2BAC0vmqfVOK1Ia4nuOdOsz5A%3D%3D&Expires=1781716000)

**Step 3.5** — Commit validated package to `.claude/skills/flow-recap/`

---

## Phase 4 — StatusMerge + RawFlowDump Skills (same process as Phase 3)

Run in this order — StatusMerge depends on FlowRecap output being stable first:

1. `raw-flow-dump-normalize` — Stage 4 from as source[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/03ecdb33-7d3d-474f-aece-ac901e7e661d/WeeklyRoutine_Overview_Marco-Meso.md?AWSAccessKeyId=ASIA2F3EMEYE6737QX7A&Signature=YOgn9ekJlC5KKLMwyDOelYdl2uQ%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIFBH6js1sEue%2F0NAB7SBrWPn6SeeehUSrX3vxYonGEw6AiEAz9OHBtx0PP9cpRuFwnnCwwG1sPd6CyiYuoFg2L%2BrbC0q%2FAQIkf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDE9bWg%2FMeiyjcVhTbirQBHiwk%2BJ1Op6%2FBbKo17YfLN1pdiB6bPAP3K%2B%2BZksEru6LxaeFoMNKci5pEK7%2B5Agr%2BW1hpATSx5VoI%2FtYJlioNwAvYI8ilAdAIhvSQSNnXcOVkT%2BCWaCVt73zbRLAaORL4DmEvwvnVD5ucNijH0fA%2F0SAwnO%2F6k%2FqP%2F9lqdKxPIRveyW5Na7guu5lt06f5x3pgWhEivwZQRNnlM8bC216rNuvrvJtNsirUMzEMAG5UKP37lo6qPdY5HyU%2BFXCcAGpBms5z68PuIvdJHqkWmSksDwQxbHJVQYRabMzNT1Jf4p1SswU6NyoH05usW4CXw7WFLJSnyDZP%2BnrR7gVLgIzsYmGRRm%2BU4xNHz%2F3pRdWRxE5dztX%2FUAEHk1dL4VkME0qzWiD4F7W9y01Ul7%2F0A6EpN62JOpwUSlA39FIPjtx5eiUgkqR2KVFbPNS2htVLUc2VdrWMdYoP1jesGWca20k%2F5sojJCRzqJKpCqNWp7UAVhXm1G4I7%2Bv3xYTktD3l3mTasKPDxFCepnZTLfdjx0nAl1rfuO0r2AqQPkqcprDI3V4TomH546mJyMOaoDa4R%2FUrgYRpHvzzNzmfXNIf9ADHLQxfjlLNrmxwjqz%2BnYuiyd%2BYJdGeLrXs5KbEcPmBZhblZI8z6WEjUHfc2RZN%2FCfQo3t5UeHPBugrond0FhQ%2Fb7zqZi3Y5zamS29hOKNdgK5SLok4CoAORknVS0kgaZ%2F%2FlNzC6wOCQ3bgQfQ7s0Hmm1mwIfUCw4oVlJxLvt4wlUNQCf0NZe%2FLA0sZcZvANrpNhwwzYzL0QY6mAG6qtk0VBBOY0TFdfZbhilF7PKZW1wYO8OzCe8npel8rZZUFTKJXfQf%2BRQndhkfwb4omGnY6IttabBqRxvFv1TYJbH0bAswaxotKVI%2FQjBu2aqmE68FnIAlff%2F8hXDOw6Z3kQUD359nq9B7giyif%2BPUmjJw6JZ8NbDojbrN9FGDKNYM%2FJHrZQ%2BAC0vmqfVOK1Ia4nuOdOsz5A%3D%3D&Expires=1781716000)
    
2. `status-merge` — Stage 7 (APSU) from as source[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/03ecdb33-7d3d-474f-aece-ac901e7e661d/WeeklyRoutine_Overview_Marco-Meso.md?AWSAccessKeyId=ASIA2F3EMEYE6737QX7A&Signature=YOgn9ekJlC5KKLMwyDOelYdl2uQ%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIFBH6js1sEue%2F0NAB7SBrWPn6SeeehUSrX3vxYonGEw6AiEAz9OHBtx0PP9cpRuFwnnCwwG1sPd6CyiYuoFg2L%2BrbC0q%2FAQIkf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDE9bWg%2FMeiyjcVhTbirQBHiwk%2BJ1Op6%2FBbKo17YfLN1pdiB6bPAP3K%2B%2BZksEru6LxaeFoMNKci5pEK7%2B5Agr%2BW1hpATSx5VoI%2FtYJlioNwAvYI8ilAdAIhvSQSNnXcOVkT%2BCWaCVt73zbRLAaORL4DmEvwvnVD5ucNijH0fA%2F0SAwnO%2F6k%2FqP%2F9lqdKxPIRveyW5Na7guu5lt06f5x3pgWhEivwZQRNnlM8bC216rNuvrvJtNsirUMzEMAG5UKP37lo6qPdY5HyU%2BFXCcAGpBms5z68PuIvdJHqkWmSksDwQxbHJVQYRabMzNT1Jf4p1SswU6NyoH05usW4CXw7WFLJSnyDZP%2BnrR7gVLgIzsYmGRRm%2BU4xNHz%2F3pRdWRxE5dztX%2FUAEHk1dL4VkME0qzWiD4F7W9y01Ul7%2F0A6EpN62JOpwUSlA39FIPjtx5eiUgkqR2KVFbPNS2htVLUc2VdrWMdYoP1jesGWca20k%2F5sojJCRzqJKpCqNWp7UAVhXm1G4I7%2Bv3xYTktD3l3mTasKPDxFCepnZTLfdjx0nAl1rfuO0r2AqQPkqcprDI3V4TomH546mJyMOaoDa4R%2FUrgYRpHvzzNzmfXNIf9ADHLQxfjlLNrmxwjqz%2BnYuiyd%2BYJdGeLrXs5KbEcPmBZhblZI8z6WEjUHfc2RZN%2FCfQo3t5UeHPBugrond0FhQ%2Fb7zqZi3Y5zamS29hOKNdgK5SLok4CoAORknVS0kgaZ%2F%2FlNzC6wOCQ3bgQfQ7s0Hmm1mwIfUCw4oVlJxLvt4wlUNQCf0NZe%2FLA0sZcZvANrpNhwwzYzL0QY6mAG6qtk0VBBOY0TFdfZbhilF7PKZW1wYO8OzCe8npel8rZZUFTKJXfQf%2BRQndhkfwb4omGnY6IttabBqRxvFv1TYJbH0bAswaxotKVI%2FQjBu2aqmE68FnIAlff%2F8hXDOw6Z3kQUD359nq9B7giyif%2BPUmjJw6JZ8NbDojbrN9FGDKNYM%2FJHrZQ%2BAC0vmqfVOK1Ia4nuOdOsz5A%3D%3D&Expires=1781716000)
    

Each follows the identical Phase 3 workflow. Two separate GPT sessions, one skill per session.

---

## Phase 5 — First Project Content (Actual State Files)

Once CLAUDE.md and at least `flow-recap` + `status-merge` are validated:

**Step 5.1** — Create `state/apex-project-status.md` with real current Apex project state (you write this manually or dictate to GPT to format)

**Step 5.2** — Run first test: `run precap-next-day` in Claude Code → validate output against contract

**Step 5.3** — Iterate on any skill that produces wrong output — fix SKILL.md only (not the contract), re-run

---

## Priority Order — What to Do Right Now

|Order|Task|Who does it|Time|
|---|---|---|---|
|1|Phase 0 folder cleanup|You (manual)|20 min|
|2|CLAUDE.md generation|GPT + you review|30 min|
|3|PrecapNextDay templates|GPT|20 min|
|4|FlowRecap full package|GPT (7-prompt flow)|45 min|
|5|StatusMerge package|GPT (7-prompt flow)|45 min|
|6|RawFlowDump package|GPT (7-prompt flow)|30 min|
|7|First real state content|You + Claude Code test|30 min|

**Start with Phase 0.** Everything else depends on a clean repo structure. The `(2)` filename artifacts and the `FirstIteration/` folder inside the active package will confuse Claude Code on every invocation until they are removed.

Prepared using Claude Sonnet 4.6 Thinking

Explain the step 0.1 in more detail. I have no idea this why you do these things. It sounds very random. Other. Wise explain to me why you have that logic so I can understand. What the. What things to look out for also

Good question. Every action in Step 0.1 has a specific reason rooted in how Claude Code loads and parses files. Here is the logic behind each one.

---

## Why Step 0.1 — The Core Problem

Claude Code reads your `.claude/skills/PrecapNextDay/` folder **as the active, executable package**. It has no concept of "this file is old" or "this file is a draft." Every file it finds in that folder is treated as valid skill content. Dirty folders = confused Claude.[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/0b371272-4664-4703-a065-aa8efa6db970/Claude_Skill_Package_BestPractice_Handover.md?AWSAccessKeyId=ASIA2F3EMEYE5P6UNRCY&Signature=YyeJAgSxI5sahWAfrKnyLGU2tLw%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIC%2FieDkybYInM0Hn1l%2B5XRn6FFM5TDKBivu7s9bMUTWzAiBXTaajjUt50qotX%2BtUUflnSW%2FTyp%2BzT0oyVeBNaKQweir8BAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIMd%2FSLdbgA54bEGX09KtAEQaiyB7VZxSgrz19qb%2Fo2eNYqBKi7CmGFz9Rfc4RZMxC2qRu%2Bgu4Cnyeu3%2FQbNFx4z80isxe4ygjunpQsnph534k92dPm7R0uYqK%2BuDcvjlB%2Bac3W%2Bt9Mcb%2FubzbEQNM9BpNcqENj6U4cIytnXVqGc5%2F%2B6PqtAxk3d2wOpj%2FHbJY6rjaF76TGJVlIzIOyuTq%2BX2hMbk7X3ik%2F%2B7smyr7Jl%2BLlDlrrtjPiyy9JvYViAeTzDs%2Fw14CtWmyW4bqiJyzhZVyUQYGygJXPoXglFJ0z12wJ4hvE0s3tXo6n8tg5FMR5l%2FvIlUlmlVL4JQskAUvSf0iyjvIqcd1PsSNHL24%2F4uSe5M5st9EfMLh%2BO6fL46P79GbbKrEozPeAuNWCTX1%2BL%2Fpgg6F0lBqsaAo5Lajxo7iVW7FupjIyUoqYm84AGEI1dcZwfZiZOc%2BskIDkOYm%2FqRWSGkKK2x%2FiDV0e%2B0wqgGe5XLnbKHM7Cuf%2FkEN6C6yRkuuuXJSVBFmPIVir%2BspStUydfhTxPuVI1PkxXwIImznL0itJ6ggxANSwSOi3UxDe%2BjTVUO89pTzaAs4HnZS2taax4mk0fXWtJ8hEbZNkAAIPLYF1VAxW9LleajF37WzEe0%2BAGiuLg9RBpYe3gpRWt037uIwUyTWLRY8jeubB5tpiI6JxGM9h%2FXUIfK5TjMFgLSwsnZ2mtplY89O8X6Q1ADegfWhVeaWVXnRc16HP8e2tjAXUh7Kabe3YJN5266WIZsULc%2B3DdLnktLAeiG9tw46NxIcFFnVsjjYAYJazKzDSpsvRBjqZAej2YAVP0%2BgI32%2BwKChdLsYmbM1tcoypSkWEa9ctyhTlvt1N818rvw3vB60Jk%2BPgC%2Fv6O01gJWnL619%2BQ6hWdIKCj4uq4ZarfZW%2FCq3PirHIq4zqyOXl2huno7agxIUCnEHkcYKcMc9qQkahkOw0bQWn3xSC6%2FoINBz0s4v4MsaoFHZC5g1CboZpFYIp4siw7b0kHi31uVQYtA%3D%3D&Expires=1781719333)

---

## Each Action Explained

## 1. Move `FirstIteration/` out of the package

**What it is:** A subfolder containing the first draft of the skill before it was revised.

**Why it's dangerous:** Claude Code sees a subfolder inside the package and may attempt to load files from it as reference material — especially if any file inside has a similar name to an active contract file. Two versions of the same schema in the same package = Claude picks one arbitrarily, often the wrong one.[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/0b371272-4664-4703-a065-aa8efa6db970/Claude_Skill_Package_BestPractice_Handover.md?AWSAccessKeyId=ASIA2F3EMEYE5P6UNRCY&Signature=YyeJAgSxI5sahWAfrKnyLGU2tLw%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIC%2FieDkybYInM0Hn1l%2B5XRn6FFM5TDKBivu7s9bMUTWzAiBXTaajjUt50qotX%2BtUUflnSW%2FTyp%2BzT0oyVeBNaKQweir8BAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIMd%2FSLdbgA54bEGX09KtAEQaiyB7VZxSgrz19qb%2Fo2eNYqBKi7CmGFz9Rfc4RZMxC2qRu%2Bgu4Cnyeu3%2FQbNFx4z80isxe4ygjunpQsnph534k92dPm7R0uYqK%2BuDcvjlB%2Bac3W%2Bt9Mcb%2FubzbEQNM9BpNcqENj6U4cIytnXVqGc5%2F%2B6PqtAxk3d2wOpj%2FHbJY6rjaF76TGJVlIzIOyuTq%2BX2hMbk7X3ik%2F%2B7smyr7Jl%2BLlDlrrtjPiyy9JvYViAeTzDs%2Fw14CtWmyW4bqiJyzhZVyUQYGygJXPoXglFJ0z12wJ4hvE0s3tXo6n8tg5FMR5l%2FvIlUlmlVL4JQskAUvSf0iyjvIqcd1PsSNHL24%2F4uSe5M5st9EfMLh%2BO6fL46P79GbbKrEozPeAuNWCTX1%2BL%2Fpgg6F0lBqsaAo5Lajxo7iVW7FupjIyUoqYm84AGEI1dcZwfZiZOc%2BskIDkOYm%2FqRWSGkKK2x%2FiDV0e%2B0wqgGe5XLnbKHM7Cuf%2FkEN6C6yRkuuuXJSVBFmPIVir%2BspStUydfhTxPuVI1PkxXwIImznL0itJ6ggxANSwSOi3UxDe%2BjTVUO89pTzaAs4HnZS2taax4mk0fXWtJ8hEbZNkAAIPLYF1VAxW9LleajF37WzEe0%2BAGiuLg9RBpYe3gpRWt037uIwUyTWLRY8jeubB5tpiI6JxGM9h%2FXUIfK5TjMFgLSwsnZ2mtplY89O8X6Q1ADegfWhVeaWVXnRc16HP8e2tjAXUh7Kabe3YJN5266WIZsULc%2B3DdLnktLAeiG9tw46NxIcFFnVsjjYAYJazKzDSpsvRBjqZAej2YAVP0%2BgI32%2BwKChdLsYmbM1tcoypSkWEa9ctyhTlvt1N818rvw3vB60Jk%2BPgC%2Fv6O01gJWnL619%2BQ6hWdIKCj4uq4ZarfZW%2FCq3PirHIq4zqyOXl2huno7agxIUCnEHkcYKcMc9qQkahkOw0bQWn3xSC6%2FoINBz0s4v4MsaoFHZC5g1CboZpFYIp4siw7b0kHi31uVQYtA%3D%3D&Expires=1781719333)

**Rule:** Only the current validated version of a file belongs in `.claude/skills/[skill]/`. All prior iterations go to `ApexDefinition&OldVersions/` — that is exactly what that folder is for .

---

## 2. Move `Audit_SKILL.md_pecap-next-day.md` out

**What it is:** The audit feedback document from the review cycle — scores, defect notes, what was wrong with v1.

**Why it's dangerous:** It contains descriptions of broken patterns and wrong formats. If Claude Code reads it during a skill invocation (which it may, since it's in the package root), it could treat the _defect descriptions_ as instructions. It's essentially a file that says "here are wrong ways to do things" — the last thing you want Claude ingesting mid-execution.

**Rule:** Audit files are process artifacts, not skill files. They are forbidden inside the package.[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/0b371272-4664-4703-a065-aa8efa6db970/Claude_Skill_Package_BestPractice_Handover.md?AWSAccessKeyId=ASIA2F3EMEYE5P6UNRCY&Signature=YyeJAgSxI5sahWAfrKnyLGU2tLw%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIC%2FieDkybYInM0Hn1l%2B5XRn6FFM5TDKBivu7s9bMUTWzAiBXTaajjUt50qotX%2BtUUflnSW%2FTyp%2BzT0oyVeBNaKQweir8BAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIMd%2FSLdbgA54bEGX09KtAEQaiyB7VZxSgrz19qb%2Fo2eNYqBKi7CmGFz9Rfc4RZMxC2qRu%2Bgu4Cnyeu3%2FQbNFx4z80isxe4ygjunpQsnph534k92dPm7R0uYqK%2BuDcvjlB%2Bac3W%2Bt9Mcb%2FubzbEQNM9BpNcqENj6U4cIytnXVqGc5%2F%2B6PqtAxk3d2wOpj%2FHbJY6rjaF76TGJVlIzIOyuTq%2BX2hMbk7X3ik%2F%2B7smyr7Jl%2BLlDlrrtjPiyy9JvYViAeTzDs%2Fw14CtWmyW4bqiJyzhZVyUQYGygJXPoXglFJ0z12wJ4hvE0s3tXo6n8tg5FMR5l%2FvIlUlmlVL4JQskAUvSf0iyjvIqcd1PsSNHL24%2F4uSe5M5st9EfMLh%2BO6fL46P79GbbKrEozPeAuNWCTX1%2BL%2Fpgg6F0lBqsaAo5Lajxo7iVW7FupjIyUoqYm84AGEI1dcZwfZiZOc%2BskIDkOYm%2FqRWSGkKK2x%2FiDV0e%2B0wqgGe5XLnbKHM7Cuf%2FkEN6C6yRkuuuXJSVBFmPIVir%2BspStUydfhTxPuVI1PkxXwIImznL0itJ6ggxANSwSOi3UxDe%2BjTVUO89pTzaAs4HnZS2taax4mk0fXWtJ8hEbZNkAAIPLYF1VAxW9LleajF37WzEe0%2BAGiuLg9RBpYe3gpRWt037uIwUyTWLRY8jeubB5tpiI6JxGM9h%2FXUIfK5TjMFgLSwsnZ2mtplY89O8X6Q1ADegfWhVeaWVXnRc16HP8e2tjAXUh7Kabe3YJN5266WIZsULc%2B3DdLnktLAeiG9tw46NxIcFFnVsjjYAYJazKzDSpsvRBjqZAej2YAVP0%2BgI32%2BwKChdLsYmbM1tcoypSkWEa9ctyhTlvt1N818rvw3vB60Jk%2BPgC%2Fv6O01gJWnL619%2BQ6hWdIKCj4uq4ZarfZW%2FCq3PirHIq4zqyOXl2huno7agxIUCnEHkcYKcMc9qQkahkOw0bQWn3xSC6%2FoINBz0s4v4MsaoFHZC5g1CboZpFYIp4siw7b0kHi31uVQYtA%3D%3D&Expires=1781719333)

---

## 3. Rename `(2)` files

**What they are:** `daily-plan-output-contract (2).md`, `flow-prompt-pack-contract (2).md`, etc. The `(2)` suffix means these are copy artifacts — macOS or Windows added it automatically when you duplicated or re-downloaded a file that already existed .

**Why it's dangerous:** Two files exist for the same contract — the original (possibly deleted, possibly still there) and the `(2)` copy. Claude Code resolves file references by exact path. If your `SKILL.md` references `daily-plan-output-contract.md` but the file is actually named `daily-plan-output-contract (2).md`, Claude gets a file-not-found error and either halts or silently skips loading the contract. Your validation rules never get applied.[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/96a9f696-553a-479a-b4e3-8ac0ee0e8234/Claude_Skill_PromptFlow_Design_Guidance_v1.md?AWSAccessKeyId=ASIA2F3EMEYE5P6UNRCY&Signature=4083InblpNR5ZXoF7iqDpy6OMaw%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIC%2FieDkybYInM0Hn1l%2B5XRn6FFM5TDKBivu7s9bMUTWzAiBXTaajjUt50qotX%2BtUUflnSW%2FTyp%2BzT0oyVeBNaKQweir8BAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIMd%2FSLdbgA54bEGX09KtAEQaiyB7VZxSgrz19qb%2Fo2eNYqBKi7CmGFz9Rfc4RZMxC2qRu%2Bgu4Cnyeu3%2FQbNFx4z80isxe4ygjunpQsnph534k92dPm7R0uYqK%2BuDcvjlB%2Bac3W%2Bt9Mcb%2FubzbEQNM9BpNcqENj6U4cIytnXVqGc5%2F%2B6PqtAxk3d2wOpj%2FHbJY6rjaF76TGJVlIzIOyuTq%2BX2hMbk7X3ik%2F%2B7smyr7Jl%2BLlDlrrtjPiyy9JvYViAeTzDs%2Fw14CtWmyW4bqiJyzhZVyUQYGygJXPoXglFJ0z12wJ4hvE0s3tXo6n8tg5FMR5l%2FvIlUlmlVL4JQskAUvSf0iyjvIqcd1PsSNHL24%2F4uSe5M5st9EfMLh%2BO6fL46P79GbbKrEozPeAuNWCTX1%2BL%2Fpgg6F0lBqsaAo5Lajxo7iVW7FupjIyUoqYm84AGEI1dcZwfZiZOc%2BskIDkOYm%2FqRWSGkKK2x%2FiDV0e%2B0wqgGe5XLnbKHM7Cuf%2FkEN6C6yRkuuuXJSVBFmPIVir%2BspStUydfhTxPuVI1PkxXwIImznL0itJ6ggxANSwSOi3UxDe%2BjTVUO89pTzaAs4HnZS2taax4mk0fXWtJ8hEbZNkAAIPLYF1VAxW9LleajF37WzEe0%2BAGiuLg9RBpYe3gpRWt037uIwUyTWLRY8jeubB5tpiI6JxGM9h%2FXUIfK5TjMFgLSwsnZ2mtplY89O8X6Q1ADegfWhVeaWVXnRc16HP8e2tjAXUh7Kabe3YJN5266WIZsULc%2B3DdLnktLAeiG9tw46NxIcFFnVsjjYAYJazKzDSpsvRBjqZAej2YAVP0%2BgI32%2BwKChdLsYmbM1tcoypSkWEa9ctyhTlvt1N818rvw3vB60Jk%2BPgC%2Fv6O01gJWnL619%2BQ6hWdIKCj4uq4ZarfZW%2FCq3PirHIq4zqyOXl2huno7agxIUCnEHkcYKcMc9qQkahkOw0bQWn3xSC6%2FoINBz0s4v4MsaoFHZC5g1CboZpFYIp4siw7b0kHi31uVQYtA%3D%3D&Expires=1781719333)

**Rule:** Every filename must match exactly what `SKILL.md`'s `supporting_files` block references. No spaces, no `(2)`, no version suffixes in active package files.

---

## 4. Create `references/` subfolder and move contracts into it

**What the contracts are:** `daily-plan-output-contract.md`, `flow-packet-contract.md`, `calendar-event-write-contract.md`, etc. — the schema and validation files.

**Why flat root is wrong:** Currently all contracts sit at the same level as `SKILL.md`. The canonical package structure is:[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/0b371272-4664-4703-a065-aa8efa6db970/Claude_Skill_Package_BestPractice_Handover.md?AWSAccessKeyId=ASIA2F3EMEYE5P6UNRCY&Signature=YyeJAgSxI5sahWAfrKnyLGU2tLw%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIC%2FieDkybYInM0Hn1l%2B5XRn6FFM5TDKBivu7s9bMUTWzAiBXTaajjUt50qotX%2BtUUflnSW%2FTyp%2BzT0oyVeBNaKQweir8BAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIMd%2FSLdbgA54bEGX09KtAEQaiyB7VZxSgrz19qb%2Fo2eNYqBKi7CmGFz9Rfc4RZMxC2qRu%2Bgu4Cnyeu3%2FQbNFx4z80isxe4ygjunpQsnph534k92dPm7R0uYqK%2BuDcvjlB%2Bac3W%2Bt9Mcb%2FubzbEQNM9BpNcqENj6U4cIytnXVqGc5%2F%2B6PqtAxk3d2wOpj%2FHbJY6rjaF76TGJVlIzIOyuTq%2BX2hMbk7X3ik%2F%2B7smyr7Jl%2BLlDlrrtjPiyy9JvYViAeTzDs%2Fw14CtWmyW4bqiJyzhZVyUQYGygJXPoXglFJ0z12wJ4hvE0s3tXo6n8tg5FMR5l%2FvIlUlmlVL4JQskAUvSf0iyjvIqcd1PsSNHL24%2F4uSe5M5st9EfMLh%2BO6fL46P79GbbKrEozPeAuNWCTX1%2BL%2Fpgg6F0lBqsaAo5Lajxo7iVW7FupjIyUoqYm84AGEI1dcZwfZiZOc%2BskIDkOYm%2FqRWSGkKK2x%2FiDV0e%2B0wqgGe5XLnbKHM7Cuf%2FkEN6C6yRkuuuXJSVBFmPIVir%2BspStUydfhTxPuVI1PkxXwIImznL0itJ6ggxANSwSOi3UxDe%2BjTVUO89pTzaAs4HnZS2taax4mk0fXWtJ8hEbZNkAAIPLYF1VAxW9LleajF37WzEe0%2BAGiuLg9RBpYe3gpRWt037uIwUyTWLRY8jeubB5tpiI6JxGM9h%2FXUIfK5TjMFgLSwsnZ2mtplY89O8X6Q1ADegfWhVeaWVXnRc16HP8e2tjAXUh7Kabe3YJN5266WIZsULc%2B3DdLnktLAeiG9tw46NxIcFFnVsjjYAYJazKzDSpsvRBjqZAej2YAVP0%2BgI32%2BwKChdLsYmbM1tcoypSkWEa9ctyhTlvt1N818rvw3vB60Jk%2BPgC%2Fv6O01gJWnL619%2BQ6hWdIKCj4uq4ZarfZW%2FCq3PirHIq4zqyOXl2huno7agxIUCnEHkcYKcMc9qQkahkOw0bQWn3xSC6%2FoINBz0s4v4MsaoFHZC5g1CboZpFYIp4siw7b0kHi31uVQYtA%3D%3D&Expires=1781719333)

text

`PrecapNextDay/   SKILL.md              ← entrypoint  references/           ← schemas and rules live here    daily-plan-output-contract.md    flow-packet-contract.md    ...  templates/            ← blank output templates  examples/             ← filled examples  package-manifest.md   ← index`

When everything is flat at root level, Claude has no structural signal about what type of file each one is. It loads them all on every invocation rather than lazy-loading only what's needed. This burns tokens on every single skill run. The `references/` subfolder + `readwhen` conditions in SKILL.md is what enables Claude to load _only the contract it needs, only when it needs it_.[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/0b371272-4664-4703-a065-aa8efa6db970/Claude_Skill_Package_BestPractice_Handover.md?AWSAccessKeyId=ASIA2F3EMEYE5P6UNRCY&Signature=YyeJAgSxI5sahWAfrKnyLGU2tLw%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIC%2FieDkybYInM0Hn1l%2B5XRn6FFM5TDKBivu7s9bMUTWzAiBXTaajjUt50qotX%2BtUUflnSW%2FTyp%2BzT0oyVeBNaKQweir8BAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIMd%2FSLdbgA54bEGX09KtAEQaiyB7VZxSgrz19qb%2Fo2eNYqBKi7CmGFz9Rfc4RZMxC2qRu%2Bgu4Cnyeu3%2FQbNFx4z80isxe4ygjunpQsnph534k92dPm7R0uYqK%2BuDcvjlB%2Bac3W%2Bt9Mcb%2FubzbEQNM9BpNcqENj6U4cIytnXVqGc5%2F%2B6PqtAxk3d2wOpj%2FHbJY6rjaF76TGJVlIzIOyuTq%2BX2hMbk7X3ik%2F%2B7smyr7Jl%2BLlDlrrtjPiyy9JvYViAeTzDs%2Fw14CtWmyW4bqiJyzhZVyUQYGygJXPoXglFJ0z12wJ4hvE0s3tXo6n8tg5FMR5l%2FvIlUlmlVL4JQskAUvSf0iyjvIqcd1PsSNHL24%2F4uSe5M5st9EfMLh%2BO6fL46P79GbbKrEozPeAuNWCTX1%2BL%2Fpgg6F0lBqsaAo5Lajxo7iVW7FupjIyUoqYm84AGEI1dcZwfZiZOc%2BskIDkOYm%2FqRWSGkKK2x%2FiDV0e%2B0wqgGe5XLnbKHM7Cuf%2FkEN6C6yRkuuuXJSVBFmPIVir%2BspStUydfhTxPuVI1PkxXwIImznL0itJ6ggxANSwSOi3UxDe%2BjTVUO89pTzaAs4HnZS2taax4mk0fXWtJ8hEbZNkAAIPLYF1VAxW9LleajF37WzEe0%2BAGiuLg9RBpYe3gpRWt037uIwUyTWLRY8jeubB5tpiI6JxGM9h%2FXUIfK5TjMFgLSwsnZ2mtplY89O8X6Q1ADegfWhVeaWVXnRc16HP8e2tjAXUh7Kabe3YJN5266WIZsULc%2B3DdLnktLAeiG9tw46NxIcFFnVsjjYAYJazKzDSpsvRBjqZAej2YAVP0%2BgI32%2BwKChdLsYmbM1tcoypSkWEa9ctyhTlvt1N818rvw3vB60Jk%2BPgC%2Fv6O01gJWnL619%2BQ6hWdIKCj4uq4ZarfZW%2FCq3PirHIq4zqyOXl2huno7agxIUCnEHkcYKcMc9qQkahkOw0bQWn3xSC6%2FoINBz0s4v4MsaoFHZC5g1CboZpFYIp4siw7b0kHi31uVQYtA%3D%3D&Expires=1781719333)

---

## 5. Rename `TEmplates/` → `templates/`

**Why:** Path references in `SKILL.md` and `package-manifest.md` are case-sensitive on Linux/macOS file systems and in GitHub. If your SKILL.md says `templates/next-day-plan-template.md` but the folder is named `TEmplates/`, Claude Code throws a file-not-found error. The typo + capitalisation inconsistency will silently break template loading every time.[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/96a9f696-553a-479a-b4e3-8ac0ee0e8234/Claude_Skill_PromptFlow_Design_Guidance_v1.md?AWSAccessKeyId=ASIA2F3EMEYE5P6UNRCY&Signature=4083InblpNR5ZXoF7iqDpy6OMaw%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIC%2FieDkybYInM0Hn1l%2B5XRn6FFM5TDKBivu7s9bMUTWzAiBXTaajjUt50qotX%2BtUUflnSW%2FTyp%2BzT0oyVeBNaKQweir8BAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIMd%2FSLdbgA54bEGX09KtAEQaiyB7VZxSgrz19qb%2Fo2eNYqBKi7CmGFz9Rfc4RZMxC2qRu%2Bgu4Cnyeu3%2FQbNFx4z80isxe4ygjunpQsnph534k92dPm7R0uYqK%2BuDcvjlB%2Bac3W%2Bt9Mcb%2FubzbEQNM9BpNcqENj6U4cIytnXVqGc5%2F%2B6PqtAxk3d2wOpj%2FHbJY6rjaF76TGJVlIzIOyuTq%2BX2hMbk7X3ik%2F%2B7smyr7Jl%2BLlDlrrtjPiyy9JvYViAeTzDs%2Fw14CtWmyW4bqiJyzhZVyUQYGygJXPoXglFJ0z12wJ4hvE0s3tXo6n8tg5FMR5l%2FvIlUlmlVL4JQskAUvSf0iyjvIqcd1PsSNHL24%2F4uSe5M5st9EfMLh%2BO6fL46P79GbbKrEozPeAuNWCTX1%2BL%2Fpgg6F0lBqsaAo5Lajxo7iVW7FupjIyUoqYm84AGEI1dcZwfZiZOc%2BskIDkOYm%2FqRWSGkKK2x%2FiDV0e%2B0wqgGe5XLnbKHM7Cuf%2FkEN6C6yRkuuuXJSVBFmPIVir%2BspStUydfhTxPuVI1PkxXwIImznL0itJ6ggxANSwSOi3UxDe%2BjTVUO89pTzaAs4HnZS2taax4mk0fXWtJ8hEbZNkAAIPLYF1VAxW9LleajF37WzEe0%2BAGiuLg9RBpYe3gpRWt037uIwUyTWLRY8jeubB5tpiI6JxGM9h%2FXUIfK5TjMFgLSwsnZ2mtplY89O8X6Q1ADegfWhVeaWVXnRc16HP8e2tjAXUh7Kabe3YJN5266WIZsULc%2B3DdLnktLAeiG9tw46NxIcFFnVsjjYAYJazKzDSpsvRBjqZAej2YAVP0%2BgI32%2BwKChdLsYmbM1tcoypSkWEa9ctyhTlvt1N818rvw3vB60Jk%2BPgC%2Fv6O01gJWnL619%2BQ6hWdIKCj4uq4ZarfZW%2FCq3PirHIq4zqyOXl2huno7agxIUCnEHkcYKcMc9qQkahkOw0bQWn3xSC6%2FoINBz0s4v4MsaoFHZC5g1CboZpFYIp4siw7b0kHi31uVQYtA%3D%3D&Expires=1781719333)

---

## What to Look Out For in General

These are the patterns that create the same class of problem across any skill folder:

- **Extra files at package root** that aren't SKILL.md, package-manifest.md, or a direct subfolder → move or delete
    
- **Duplicate filenames** with `(2)`, `_copy`, `_old`, `_v1` suffixes → exactly one file per role, archived or deleted otherwise
    
- **Mismatched filenames** between what `SKILL.md` references in `supporting_files` and what actually exists on disk → always check the SKILL.md path references match the actual filenames exactly
    
- **Nested iteration folders** (`FirstIteration/`, `v1/`, `drafts/`) inside active packages → always archive to `ApexDefinition&OldVersions/`
    
- **Audit/feedback/review files** inside active packages → process artifacts only, never live skill content