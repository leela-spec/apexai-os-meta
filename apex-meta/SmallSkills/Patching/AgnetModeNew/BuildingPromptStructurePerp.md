Here is a browser-only Agent Mode 5.5 prompt template, built directly from your Space files and scoped strictly to browser chat execution — no API, no Codex, no local shell/git assumptions.

## Why This Template Differs From Your Existing One

Your current `AgentModePatchingPromptTemplate.md` and its best-practice guide were built for a **Codex-style container with shell/Git access** — that's a different execution surface than GPT-5.5 Agent Mode in browser chat. The failure evidence in `GitAccessMistake.md` and `NoLocalGitWorktree.md` shows that assuming shell/Git primitives in an environment that doesn't have them causes wasted discovery loops and fabricated fallbacks. This template removes all Git/patch/API scaffolding and keeps only the surface-agnostic discipline: anti-fabrication, budget caps, and honest partial reporting.

## Content Ready — Template Body

text

`# Agent Mode Prompt — <TASK_NAME> You are GPT-5.5 Agent Mode operating in browser chat only. No API access. No Codex. No local shell, terminal, or Git worktree exists in this surface — do not attempt or search for one. ## 1. Mission (rewrite every run) - task: "<ONE_SENTENCE_GOAL>" - scope: "<WHAT_IS_IN_SCOPE>" - out_of_scope: "<WHAT_IS_EXPLICITLY_EXCLUDED>" - output_format: "<REPORT | LIST | DRAFT | ANALYSIS | DECISION>" ## 2. Invariant Rules (copy unchanged every run) - Do not fabricate sources, data, or results under time/complexity pressure. - Do not claim a task step is done without direct evidence from a tool call in this session. - Do not re-run identical discovery/search actions more than once if the first result was conclusive. - Do not silently narrow the mission after hitting a blocker — report the blocker instead. - Report partial completion honestly; PARTIAL is not the same as PASS. ## 3. Budget Discipline (from IterativeProcess.md learning) - Max exploratory/preflight actions before starting real work: <N, e.g. 2> - If a fact is already established earlier in this run, treat it as final — do not re-verify. - If full completion is not possible within budget, STOP and report exactly what remains undone. Never fill gaps with placeholder content. ## 4. Run Parameters (fill fresh, delete placeholders before running) - inputs: <LIST_OF_SOURCES_OR_FILES_USER_PROVIDES> - constraints: <TIME, LENGTH, FORMAT, TONE CONSTRAINTS> - required_deliverables: <LIST_EACH_ONE_EXPLICITLY> - forbidden_actions: <ANYTHING_AGENT_MUST_NOT_DO> ## 5. Procedure 1. Confirm inputs are present; if missing, stop and report MISSING_INPUT (do not guess). 2. Execute task against required_deliverables only. 3. Self-check each deliverable against the coverage ledger before finishing. 4. Produce final report using the schema below. ## 6. Deliverable Coverage Ledger - declared: [<deliverable_1>, <deliverable_2>, ...] - completed: [...] - omitted: [{name: "...", reason: "..."}] ## 7. Final Report Schema verdict: PASS | PARTIAL | FAIL deliverables_completed: [...] deliverables_omitted: [{name, reason}] sources_used: [...] limitations: [...] blockers: [...] (only if FAIL/PARTIAL) ## 8. Anti-Drift Self-Check (run before responding) - no_fabricated_content: true - no_redundant_discovery_loops: true - no_scope_narrowing_without_report: true - all_run_parameters_filled: true - coverage_ledger_matches_output: true`

This is roughly 2.4k characters — well under the 5k truncation limit, so it can be saved as a single file without splitting.

Before I save this to your Space as a file, confirm one thing: do you want it saved under the name `AgentModeBrowserPromptTemplate.md`, or should it overwrite/extend `INdexINSpacePerp.md` directly?

Prepared using Claude Sonnet 5.0 Thinking

reserach the web for uptodate best practice to improve this prompt: - focusing on the process the ai is supposed to do - all files that are necessary for the püatch agent mode target are going to be delivered as accesible in the project sources of that agent mode chat (thereby guaranteeing accessibility) - the iterative workflow and not reading all files in the begining (expecting to hold context) - using the git patch tools that are accesible in an agent mode - creating a download with all patches if save, the write function seem in git seem to be wacjky, they may be priority but should have a downloadable fallback - overengineering, stale info, focus on failure rather than the target/process/output

Completed 2 steps

Based on 2026 context-engineering research, the core fix is: stop front-loading files, treat the file list as a "just-in-time" index, and cut all narrative failure-history language from the prompt itself. Below is the revised template.[](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

## What The Research Says To Change

Anthropic's current guidance frames long agent tasks as an "attention budget" problem — the smallest set of high-signal tokens wins, and pre-loading every file up front causes context rot rather than better grounding. The recommended pattern is "just-in-time" retrieval: keep lightweight file references (paths, not contents) in the prompt, and let the agent pull actual file content only when it works on that specific file. Separately, current prompt-engineering guidance for 2026 explicitly warns against "reactive prompting" bloat — stuffing a prompt with every edge case or past failure mode makes it harder for the model to parse the actual task, and shorter, target-focused prompts outperform defensive ones.

## Revised Template

text

`# Agent Mode Prompt — <TASK_NAME> You are GPT-5.5 Agent Mode in browser chat. Project sources for this chat already contain every file you need — you do not need to search, request, or assume access elsewhere. Git patch tools available in this Agent Mode session are your primary write mechanism. ## 1. Target - outcome: "<WHAT_A_DONE_TASK_LOOKS_LIKE, ONE SENTENCE>" - deliverables: [<file_or_patch_1>, <file_or_patch_2>, ...] - done_when: "<OBJECTIVE_COMPLETION_CONDITION>" ## 2. File Access Model (just-in-time, not upfront) - All required files are already attached in project sources — confirmed accessible. - Do not read every file at the start. Open a file only when you are actively   working on it. - Process one target file at a time: open -> edit/patch -> validate -> close -> next. - If a file referenced mid-task is missing from project sources, stop and name it —   do not guess its content. ## 3. Iterative Workflow - Work in single-file loops. Do not batch multiple files' edits before validating any of them. - After each file, confirm the patch applied cleanly before moving to the next. - Do not re-open or re-scan a file you already finished unless a later step depends on it. ## 4. Patch Generation and Delivery - Use the built-in git/patch tool in this Agent Mode session as the primary method   for creating and applying patches. - After each patch (or at task end), also produce a downloadable copy of every patch   file. Treat the in-session git write as primary and the download as a required  fallback, not optional — session git writes have shown intermittent failures. - Before final report, verify: does a download link exist for every patch claimed   as written? If not, generate it now. ## 5. Scope Discipline - Stay on the declared deliverables. Do not add new checks, guards, or steps not   required to reach "done_when." - If a blocker appears, report it once and stop — do not build workaround logic   or expand scope to compensate. ## 6. Final Report - deliverables_completed: [...] - deliverables_incomplete: [{name, reason}] - patches_written_in_session: [...] - patches_available_as_download: [...] - verdict: DONE | PARTIAL (with reason)`

## Key Differences From The Prior Version

The table below shows what changed and why, grounded in the research above.

|Area|Old approach|New approach|Why|
|---|---|---|---|
|File access|Read all files upfront to "hold context"|Files confirmed accessible in project sources; open just-in-time per file|Prevents context rot from loading unneeded data [](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)|
|Workflow|Batch discovery then batch edits|Strict one-file loop: open, edit, validate, close|Matches "iterative development with clear milestones" pattern [](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)|
|Patch writing|Git-native worktree assumptions (wrong surface)|Native Agent Mode git/patch tool as primary|Uses the actual tool present in this environment, not a shell assumption|
|Output safety|No fallback specified|Mandatory downloadable patch copy alongside git write|Directly addresses your note that in-session git writes are unreliable|
|Prompt tone|Long failure-mode anthology and anti-drift checklists|Short, target-focused, minimal constraints|Bloated defensive prompts reduce model parsing accuracy|
|Reasoning at each step|Prompt re-explains prior failures for context|Prompt states the target and lets the model reason forward|"Right altitude" prompting — specific enough to guide, not brittle logic [](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)|

Prepared using Claude Sonnet 5.0 Thinking

you seem to have drifted insanely. instead of gpt related prompt engeineering you ahve been goinginto antrhopic? focus only on gpt 5.5 subscription browser agent mode runs

Completed 2 steps

You're right — pivoting fully to OpenAI's official GPT-5.5 guidance now, no cross-vendor contamination.[](https://developers.openai.com/api/docs/guides/prompt-guidance)

## What OpenAI Actually Says About GPT-5.5

OpenAI's current GPT-5.5 prompt guidance is explicit: shorter, outcome-first prompts outperform legacy step-by-step process stacks, and over-specifying process "adds noise, narrows the model's search space, or leads to overly mechanical answers". The model performs best when you define the goal, success criteria, constraints, and stop rules, then let it choose its own path — not when you prescribe every step. OpenAI also explicitly recommends replacing absolute "ALWAYS/NEVER/must" language with decision rules for judgment calls, since over-firm language doesn't carry more weight in GPT-5.5 and forces guessing when the "why" is missing.[](https://developers.openai.com/api/docs/guides/prompt-guidance)

## Revised Template — GPT-5.5 Browser Agent Mode Only

text

`Role: You are GPT-5.5 Agent Mode running in browser chat for patch/edit work. # Goal <ONE_SENTENCE_OUTCOME, e.g. "Apply the required changes to the listed target files and deliver them as patches."> # Context available All files needed for this task are already attached in this chat's project sources — treat that as guaranteed. Do not search for files elsewhere or assume any are missing until you actually try to open one and it fails. # Success criteria - Every target file listed below has been edited/patched and validated. - Each patch was generated with the git/patch tool built into this Agent Mode session. - A downloadable copy of every patch exists, regardless of whether the in-session git write succeeded. - Final answer states which files are done, which are not, and why. # Working method Work through target files one at a time: open the file, make the change, generate and validate its patch, then move to the next file. Don't open or read files you aren't currently working on — pull each one just before you need it, not all at once. If a step doesn't require inspecting more files, don't inspect more files. # Constraints - Target files: <LIST> - Do not touch files outside this list. - Do not invent file content if a listed file can't be opened — report it as blocked instead. - In-session git write is the first attempt for each patch, but is known to be unreliable here — always also produce a downloadable version of the patch in the same turn, don't treat the download as optional cleanup. # Output For each file: one line stating file name, patch status (written/downloaded/blocked), and reason if blocked. End with a short summary: files completed, files remaining, overall status. # Stop rules If a target file can't be accessed after one real attempt, mark it blocked and continue to the next file — don't retry repeatedly and don't fabricate its content. Stop and report once all target files have been attempted.`

## Why Each Change Maps To Your Four Points

|Your requirement|Template mechanism|OpenAI rationale|
|---|---|---|
|Process focus, not failure history|Prompt states goal + success criteria only, no anti-drift checklist or past-failure prose|Legacy prompts over-specify process; shorter outcome-first prompts perform better [](https://developers.openai.com/api/docs/guides/prompt-guidance)|
|Files guaranteed in project sources|One line stating access is guaranteed, no verification ritual|Removes unnecessary upfront steps the model would otherwise invent [](https://developers.openai.com/api/docs/guides/prompt-guidance)|
|Iterative workflow, no upfront context loading|"Working method" explicitly says pull each file just before use, not all at once|Matches "fewest useful tool loops" stopping-condition pattern, avoiding unneeded exploration [](https://developers.openai.com/api/docs/guides/prompt-guidance)|
|Git patch tool + downloadable fallback|Constraints section names in-session git as first attempt, download as mandatory parallel output|OpenAI's guidance to define concrete validation/output requirements rather than vague hopes [](https://developers.openai.com/api/docs/guides/prompt-guidance)|
|Avoid overengineering / stale info|No absolute-rule stacking, no XML anti-drift blocks, short sections only|OpenAI explicitly discourages "ALWAYS/NEVER" stacking and step-by-step over-specification in GPT-5.5 prompts [](https://developers.openai.com/api/docs/guides/prompt-guidance)|

This version is roughly 1.8k characters, well inside any single-message limit, and contains no Git-worktree, Codex, or shell assumptions.

Prepared using Claude Sonnet 5.0 Thinking

give better wording for: - all relevant files are in the the project sources available, if not search for github repo access - using the deterministc git patch creation (somethiing like git apply, check or soemtjhign)should be better explained? - the iterative process should be better alinged with the patch plan - the patch plan should be read, even thouhg it is long, create some guidance to deal with that - if a blokcer is happening the run should find some workaround and continue with the target in mind (but still guard against empty files, hallucianted patching without relevant file access)

Here are refined wordings for each of your five points, grounded in current git-apply mechanics and long-document handling practice.

## 1. File Access With Fallback

**Before:** "all relevant files are in the project sources available, if not search for github repo access"

**Better wording:**

text

`# File access All target files should already be attached in this chat's project sources — check there first. If a specific file is missing from project sources, attempt GitHub repo access (if a connector is available in this session) as the fallback source before treating the file as blocked. Only mark a file BLOCKED if neither project sources nor GitHub access can produce its content — never proceed on assumption or memory of what the file "probably" contains.`

This keeps a two-tier access order (project sources → GitHub connector → blocked) instead of assuming one path always works.

## 2. Deterministic Patch Validation

**Before:** vague mention of "git apply, check or something"

**Better wording, based on standard git-apply dry-run practice**:

text

`# Patch creation and validation For every file change, generate the patch as a unified diff via the git tool available in this session. Before treating any patch as final, run a dry-run check (git apply --check <patch>) — this validates the patch would apply cleanly without writing any changes to disk. - If the dry-run check passes with no output: the patch is valid, proceed to apply/deliver it. - If the dry-run check fails: it reports the exact file and hunk causing the mismatch — regenerate   the patch against the current file content rather than forcing it or discarding the check. Never present a patch as complete without having run this dry-run step first.`

This explains why the check matters (silent corruption otherwise) and what to do on both outcomes, not just that a check "should" happen.[](https://courses.axx.no/rdgitcourse/tier-3-expert/01-git-apply.html)

## 3. Iterative Process Aligned To The Patch Plan

**Better wording:**

text

`# Iterative workflow Treat the patch plan as the single source of truth for scope and order. Process target files in the exact sequence the patch plan defines, one file per loop: open the file the plan names next, apply the corresponding change, validate with the dry-run check, mark that plan item done, then move to the plan's next item. Do not reorder, batch, or skip ahead of the plan's sequence.`

Anchoring the loop to plan order (instead of just "one at a time") ties the iterative discipline directly to the plan's own structure.

## 4. Handling A Long Patch Plan

**Better wording, based on document-chunking practice**:

text

`# Reading the patch plan The patch plan must be read in full before work starts, even if it is long — do not skip sections or infer their content. If the plan exceeds what you can hold in one read, process it in sequential sections (e.g. by its own headings or numbered items) and extract only the structured facts you need per section: target file, required change, and any validation marker. Do not attempt to hold the entire plan's prose in working memory — instead, re-open the relevant plan section when you reach that file in the iterative loop, rather than relying on an earlier summary of it.`

This gives a concrete strategy (section-by-section extraction, re-reference on demand) rather than just telling the model to "cope" with length.

## 5. Blocker Handling: Workaround With Guardrails

**Better wording:**

text

`# Blocker handling If a step is blocked (e.g. a file won't open, a patch won't validate), attempt one reasonable workaround before giving up on that item — such as retrying access, checking the GitHub fallback, or re-reading the relevant plan section for missed context. If the workaround resolves it, continue toward the target normally. If no workaround resolves it, do not force progress by: writing an empty file, generating a patch against content you have not actually read, or inventing file content to complete the diff. Instead mark that specific target BLOCKED with a one-line reason, and continue to the next target in the patch plan. A blocked item must never be disguised as a completed patch.`

This separates "try to route around it" from the hard stop condition — fabricated or empty patches — so the run stays productive without crossing into hallucinated output.