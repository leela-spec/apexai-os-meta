I'll pick up where the previous session left off. It was mid-way through integrating the ground-checked findings into `design-lock-answers.md`. Let me check the current state.

Ran a command, found files

The `research-integration-note.md` wasn't actually written (the session was cut off before it completed). Let me look at the fable-orchestrator folder and the design-lock-answers file to see exactly where things stand.

Ran a command, read a file

The design-lock-answers.md on disk is the committed version — the previous session's intended edits (research-integration-note.md + Q7/Q8 flips) were never persisted before the cutoff. Before I re-do them, let me verify the two ground-check findings myself rather than trust the truncated narrative, and see what the external research prompts currently assume.

Ran a command, searched code, read 2 files

I've now verified both hinge findings myself against the actual repo (not the truncated narrative). Here's where things actually stand.

**Ground-check results:**

1. **P1's target surface is real.** `mutation-gate-rules.md` confirms apex-session has exactly one gated write path: `operator_validation ∈ {confirmed, rejected, needs_revision, not_requested}`, with `never_do: silently_mutate_repo_files`. P1's premise (bolt the role-vs-state invariant onto this single gate) is architecturally sound.
2. **P2 hits a hard wall.** The only `openai`/`gemini` matches in the repo are copy-paste _prompt-style contracts_ (`PromptEngineer/provider-style-contract-gemini.md`) and _routing contracts_ (`AIRouting/`) — **not a runtime surface**. There is no MCP server or external-model call the orchestrator can invoke. So if P2 comes back recommending a "different-model-family judge" (its most likely verdict), that recommendation is **not executable in this repo today** — it would require net-new trusted infrastructure.

The committed `design-lock-answers.md` and `external-research-pack` are internally coherent, but **P2 as written doesn't tell the researcher this constraint** — so it can return an unusable recommendation. That's the real gap.

Let me confirm one more thing before I propose the edit — whether the Q7 glossary target already exists (the CLAUDE.md now references `apex-meta/GLOSSARY.md`):

Checked glossary and arch doc existence

`apex-meta/GLOSSARY.md` **already exists** — committed in 26ed183e. That's important: Q7's proposed decision (create a glossary) is no longer a proposal, it's been _built_ in the main line, along with the finalized Weekly-Orchestrator architecture. Part of the fable-orchestrator "proposed answers" have already been overtaken by committed reality.

Also, there's a **third PromptAnswers file the previous session never read** — `Role-vs-state permission separation_WithRepoAccess.md` (a P1 re-run with repo access). Evaluating returned answers was the core task, so let me read it.

ReadRole-vs-state permission separation_WithRepoAccess.md

contoniue with full permissons. remember the target: finalized the orhcestration system * this would mean all agents and contracts are defined, the skilll pacages from the previous old apex are moved into their domain for them to have the information, the rich insturctions (best practice, essence, template,s mistakes / failures and appendixes got checked, evaluate and dterministically moved. * apex synch and plan are integrated into the meta ops agents * but most imporrntatnly that system is tested, running, evaualte and optimized for the kb insight from claude orchestration design i see nothing of that has happend. reread this folder: C:\GitDev\apexai-os-meta\apex-meta\fable-orchestrator and actually finish the job fully

Fable orchestrator: full build to finish

Reading the whole folder first, as instructed.

Read 11 files, ran a command, used 9 tools

P01 and P02 are already applied in the committed files. Let me check the 8 agent files (P03–P10).

Read 3 files

Wave 1 appears fully applied already — the patch plan's "no patch applied" status line is stale. Let me verify all wave gates directly rather than reading every file.

Searched code, read a file

Usage limit reached

continue

Searched code, read a file, edited a file, used 3 tools

P26 done. Now P27 — reflow the squashed contract blocks in PromptEngineer/SKILL.md into parseable YAML:

EditedSKILL.md+70-2

The `supporting_files` block has the identical defect (same G09 class) — reflowing it too:

Edited a file, ran a command

Wave 3 gate passes. Committing, then Wave 4:

Ran 3 commands, read a file, edited 2 files, used 2 tools

Unexpected: ~20 files show as modified that I never touched. Let me inspect before anything else.

Ran 4 commands, read 2 files, used 2 tools

The script runs live against 8 real task files. Writing the two meta-ops agent definitions in the established idiom:

Created 2 files, edited 3 files

Now the handoff schema needs the two new packet types, and the meso file map needs the scope update:

Failed to edithandoff-schema.md

The concurrent session touched handoff-schema again. Re-reading:

Read 2 files, ran a command, edited 2 files

Integration surface complete. Now the behavioral gate — dispatching both new agents live, in parallel (real script, real task files):

Ran 3 agents, edited a file, ran 2 commands, used 2 tools

The five-file scaffold exists for 8+ roles. Checking the full role list and appendix surfaces, then I'll fan out one evaluation worker per role:

Ran a command, ran 9 agents

All 9 migration workers are running in parallel. While they work, verifying the review wiring and glossary stay consistent with the new packet types:

ReadGLOSSARY.md

Glossary is already consistent — the new packet types fall under the existing `packet` definition and `meta_ops` accountability; no edit needed.

The 9 migration workers are running. When they complete I'll: verify each written doctrine file (spot-check citations against sources), wire the doctrine references into the consuming agent definitions, aggregate the kept/dropped evaluation tables into a migration ledger in the architecture KB, commit — then run the full-loop test (Task 7).

Background task completedAgent "Migrate alfred doctrine" finished· 1m 21s

Alfred migration done — honest result: only 3 items survived (most of the alfred scaffold was empty-state markers, already covered by current contracts). The two new meta-ops agents also just registered live in the session. Waiting on the remaining 8 workers.

Checked doctrine files written so far

Two doctrine files down. Waiting on the remaining workers before verification and wiring.

Background tasks2 completed

meta_ops done (2 kept, 13 dropped — correctly caught that old meta_ops execution-control doctrine is superseded by the locked architecture). 7 workers remaining.

Found tools

meta_strategy done (7 kept, 7 dropped). 6 workers remaining — holding until all return before verification, wiring, and the ledger.

Background task completedAgent "Migrate knowledge_bank doctrine" finished· 1m 46s

knowledge_bank done (8 kept, 23 dropped — correctly deferred to apex-kb's deterministic ownership). 5 remaining.

Background task completedAgent "Migrate meta_detective doctrine" finished· 2m 18s

meta_detective done (17 kept — the richest surviving doctrine, as expected; verification moves from the five internal modes mapped onto the two lenses). 4 remaining.

Background task completedAgent "Migrate ai_handling_routing doctrine" finished· 2m 22s

ai_handling_routing done (28 kept, 17 dropped — stale provider ceilings correctly excluded). 3 remaining.

Background task completedAgent "Migrate prompts_workflows doctrine" finished· 2m 13s

prompts_workflows done (25 kept across the two domains). 2 remaining — informatics_design and hygiene_clean.

Background task completedAgent "Migrate hygiene_clean doctrine" finished· 2m 1s

hygiene_clean done (17 kept, 21 dropped). 1 remaining — informatics_design.

Background task completedAgent "Migrate informatics_design doctrine" finished· 2m 35s

All 9 migration workers complete — 124 items kept, ~130 dropped with cited reasons. Now verifying the written files before wiring:

Linted all 10 doctrine files

Two files lack source citations. Inspecting them:

Read 2 files

Content is strong — only the source-basis lines use shorthand instead of the resolvable repo path. Fixing both:

Edited 2 files

Doctrine files verified. Now wiring them into their consumers — orchestrator references, the two reviewers, and precap-week first:

Edited 4 files, read a file

Now wiring the four skill-package doctrine files into their skills' navigation:

Searched code, read 3 files, edited 4 files

All wiring complete. Now the migration ledger:

Created a file, ran a command, ran an agent, used 2 tools

G1 pass. **Stage 2 — G2 next-day plan** (autonomous-override: G1 ceremony skipped per handoff-schema rule, noted in dispatch):

Ran an agent

Failed to run agentFable 5G2: dispatch apex-precap-next-day

Background task failedAgent terminated early due to an API error: You've hit your session limit · resets 5:50pm (E