# 1. The Skill File

**Path:** `~/.hermes/skills/apex-process/goal-skeleton-fill-verify-revise-learn/SKILL.md`

 name: goal-skeleton-fill-verify-revise-learn  description: "Create any structured artifact reliably: define the goal contract, build the skeleton first, fill content, verify against acceptance criteria, revise, and capture learning. Use for guides, decision memos, process definitions, prompt packs, research syntheses, skill drafts, implementation plans, Kanban graph specs, and briefing packets."  version: 1.0.0  author: Apex Process  license: MIT  platforms: [linux, macos, windows]  metadata:    hermes:      tags: [process, artifact-creation, verification, planning, synthesis, structured-output, skeleton-first]      category: apex-process      related_skills: [plan, requesting-code-review, subagent-driven-development, kanban-orchestrator]  ---    # Goal → Skeleton → Fill → Verify → Revise → Learn    A six-phase process for creating reliable structured artifacts from messy user requests. It forces goal clarity before structure, structure before content, and verification before delivery.    **Core principle:** Never fill content until the skeleton is coherent. Never deliver until verification passes or a block is explicit.    ## When to Use    - User requests a structured artifact: guide, decision memo, process definition, prompt pack, research synthesis, skill draft, implementation plan, Kanban graph spec, briefing packet, or similar  - The artifact has multiple sections, audiences, or constraints that need to be resolved before writing  - Quality and correctness matter more than speed  - The request is ambiguous, underspecified, or contains conflicting constraints    ## Do Not Use For    - Simple one-section responses — answer directly  - Conversational replies or quick lookups  - Code implementation tasks — use the `plan` skill instead  - Real-time or streaming outputs    ## Required Inputs    Before starting, identify:    | Input | Required | Notes |  |---|---|---|  | User goal | Yes | What they want to exist when done |  | Artifact type | Yes | Guide / memo / plan / spec / briefing / synthesis / other |  | Audience | Yes | Who reads it and what they already know |  | Scope | Yes | What is in and out |  | Constraints | Yes | Length, format, tone, sources, deadlines |  | Success criteria | Yes | How to know the artifact is done |  | Sources | If applicable | Documents, data, prior work to draw from |    If any required input is missing, ask one targeted question before proceeding. Do not guess at scope or success criteria.    ## Quick Reference
```

Phase 1 → Goal Contract Define what done looks like before writing anything  
Phase 2 → Skeleton First Structure before content; validate before filling  
Phase 3 → Fill One section at a time; assumptions visible  
Phase 4 → Verify Self-check + acceptance criteria check; structured verdict  
Phase 5 → Revise Fix defects in priority order; max 2 cycles by default  
Phase 6 → Learn Capture reusable patterns and failure modes

```
  
## Procedure  
  
### Phase 1 — Goal Contract  
  
Before writing anything, make the goal explicit and bounded.  
  
Produce a goal contract with these fields:  
  
```

Goal Contract  
─────────────  
User goal: [What the user wants to exist]  
Artifact type: [Guide / memo / plan / spec / briefing / synthesis / other]  
Audience: [Who reads it; what they already know]  
Scope: [What is included]  
Non-scope: [What is explicitly excluded]  
Constraints: [Length, format, tone, sources, deadlines]  
Source requirements: [Documents or data needed; mark MISSING if not yet available]  
Success criteria: [Specific, verifiable conditions for done — list each one]  
Ambiguity assumptions: [Decisions made without asking; flag for user review]  
Stop conditions: [What would cause a block: missing source, conflicting constraint, user decision needed]

```
  
**Decision rule:** If success criteria cannot be stated specifically, ask one clarifying question. Do not proceed to Phase 2 with vague criteria.  
  
**Ambiguity rule:** For minor ambiguities, make a reasonable assumption and mark it visibly with `[Assumption: ...]`. For blocking ambiguities — missing source, contradictory constraints, unclear audience — stop and ask.  
  
---  
  
### Phase 2 — Skeleton First  
  
Build the artifact's structure before writing any content.  
  
Produce a skeleton with these fields:  
  
```

Skeleton  
────────  
Artifact title: [Working title]  
Section list:

- Section name: [Name]  
    Function: [What this section does for the reader]  
    Required inputs: [What must be known or sourced to fill this section]  
    Planned output: [What the filled section will contain]  
    Acceptance criteria: [How to know this section is complete and correct]

Missing inputs: [Sources or decisions not yet available]  
Risks: [Sections that may be hard to fill correctly]  
Unresolved questions: [Open items that could change the structure]

```
  
**Coherence check — do not proceed to Phase 3 until all pass:**  
  
- [ ] Every section has a clear, distinct function (no orphan sections, no duplicates)  
- [ ] Sections are in a logical order for the audience  
- [ ] All required inputs are either available or explicitly marked MISSING  
- [ ] Success criteria exist for each section  
- [ ] The skeleton as a whole satisfies the goal contract's success criteria  
  
**Rule:** If a section's required inputs are MISSING, mark it as a placeholder and note the block. Do not fill it with guesses.  
  
---  
  
### Phase 3 — Fill  
  
Fill one section at a time. Preserve the section's stated function.  
  
**Fill rules:**  
  
1. Fill sections in order unless a dependency requires otherwise  
2. Keep evidence, decisions, open questions, and instructions in separate blocks — do not mix them in one paragraph  
3. Make assumptions visible: prefix with `[Assumption: ...]`  
4. Keep unresolved issues visible: prefix with `[Open: ...]`  
5. Preserve source boundaries: note where each claim comes from  
6. Do not expand scope beyond what the skeleton defines for this section  
  
**Per-section fill checklist:**  
- [ ] Section function is preserved (not drifted from the skeleton)  
- [ ] All claims are grounded in available sources or marked as assumptions  
- [ ] No content from other sections has leaked in  
- [ ] Open items are visible, not buried  
  
---  
  
### Phase 4 — Verify  
  
After filling all sections, run a structured verification pass.  
  
Produce a verification record:  
  
```

Verification Record  
───────────────────  
Self-check:

- [ ]  Artifact matches the goal contract (scope, audience, constraints)
- [ ]  All sections filled or explicitly blocked with reason
- [ ]  No internal contradictions between sections
- [ ]  Assumptions are visible and reasonable
- [ ]  Open items are listed, not hidden

Acceptance criteria check:  
[List each success criterion from Phase 1 and mark PASS / FAIL / PARTIAL]

Missing input check:  
[List any sources or decisions that were unavailable; note impact on quality]

Contradiction check:  
[List any claims that conflict with each other or with the sources]

Source grounding check:  
[List any claims not grounded in available sources]

Completeness check:  
[List any sections that are thin, vague, or placeholder-only]

Independent review needed:  
[YES / NO — if YES, describe what the reviewer should check]

Verdict:  
[ ] PASS — all critical acceptance criteria pass; no blocking contradictions  
[ ] REVISE — fixable gaps exist; list them in Required fixes below  
[ ] BLOCK — missing user decision, missing source, or contradiction that cannot  
be resolved without input; state exactly what is needed

Required fixes (if REVISE):  
[Ordered list of defects, critical first]

```
  
**Verdict decision rules:**  
  
| Verdict | Condition | Action |  
|---|---|---|  
| PASS | All critical acceptance criteria pass; no blocking contradictions | Proceed to Phase 6 (skip Phase 5) |  
| REVISE | Fixable gaps exist; no blocking unknowns | Proceed to Phase 5 |  
| BLOCK | Missing user decision, missing source, or contradiction that cannot be resolved without input | Stop; state exactly what is needed; do not guess |  
  
---  
  
### Phase 5 — Revise  
  
Run a targeted revision cycle. Default maximum: **2 cycles**.  
  
**Each revision cycle:**  
  
1. List all defects from the verification record  
2. Prioritize: critical defects first (those that cause FAIL on acceptance criteria), then important, then minor  
3. If the structure is wrong: patch the skeleton first, then re-fill affected sections  
4. If the content is wrong: patch the content directly  
5. Re-run Phase 4 verification after each cycle  
  
**Stop conditions:**  
- Artifact passes verification → proceed to Phase 6  
- A user decision is needed → block with exact question  
- Maximum cycles reached → deliver with an explicit list of remaining open items; do not silently omit them  
  
**Rule:** Do not silently drop defects. If a defect cannot be fixed without user input, surface it explicitly.  
  
---  
  
### Phase 6 — Learn  
  
After delivery (PASS or BLOCK), produce a learning capture.  
  
```

Learning Capture  
────────────────  
Reusable pattern: [What worked well that should be repeated]  
Failure mode seen: [What went wrong or nearly wrong]  
Future skill candidate: [If a reusable sub-process emerged, name it]  
Memory candidate: [A fact or preference worth saving to MEMORY.md]  
Open question: [Something unresolved that future work should address]  
Do not save: [Anything sensitive, ephemeral, or task-specific that should not persist]

```
  
**Rule:** This is a candidate only. Do not write to memory or create a skill unless the user explicitly asks. Surface the learning capture as a visible section in your response.  
  
---  
  
## Output Format  
  
The artifact is the primary deliverable. Deliver it as a clean document, not embedded in process commentary.  
  
After the artifact, append:  
  
```

─── Process Summary ───────────────────────────────────────  
Verification: [PASS / REVISE / BLOCK]  
Cycles used: [N of max 2]  
Open items: [List or "none"]  
Assumptions: [List or "none"]  
Learning capture: [Inline or "see above"]  
───────────────────────────────────────────────────────────

```
  
---  
  
## Verification  
  
The skill is working correctly when:  
  
- [ ] Phase 1 produces a goal contract with specific, verifiable success criteria  
- [ ] Phase 2 produces a skeleton that passes the coherence check before any content is written  
- [ ] Phase 3 fills sections without mixing evidence, decisions, and instructions  
- [ ] Phase 4 produces a structured verification record with an explicit PASS / REVISE / BLOCK verdict  
- [ ] Phase 5 fixes defects in priority order and re-verifies  
- [ ] Phase 6 produces a learning capture that is surfaced but not automatically saved  
- [ ] The final artifact is delivered as a clean document with a process summary appended  
  
---  
  
## Pitfalls  
  
**Skipping the goal contract.** Starting to write before success criteria are defined produces artifacts that satisfy the wrong goal. The goal contract is not optional.  
  
**Filling before the skeleton is coherent.** Writing content into a broken structure means the content will need to be rewritten when the structure is fixed. Always pass the coherence check first.  
  
**Mixing evidence, decisions, and instructions in one block.** This makes verification impossible. Keep them in separate labeled blocks within each section.  
  
**Hiding assumptions.** Unmarked assumptions become invisible errors. Every assumption must be prefixed `[Assumption: ...]`.  
  
**Silently dropping defects.** If a defect cannot be fixed, surface it explicitly. Never deliver an artifact with hidden known problems.  
  
**Treating BLOCK as failure.** A BLOCK is correct behavior when a user decision or missing source is genuinely needed. State exactly what is needed and stop.  
  
**Running more than 2 revision cycles without escalating.** If the artifact has not passed after 2 cycles, the problem is likely structural (wrong skeleton) or requires user input. Escalate rather than iterate indefinitely.  
  
**Saving the learning capture automatically.** The learning capture is a candidate. Do not write to memory or create a skill without explicit user instruction.  
  
---  
  
## Examples  
  
### Example 1 — Decision memo  
  
**User request:** "Write a decision memo on whether to use Kanban or a simple todo list for our team's workflow."  
  
**Phase 1 (abbreviated):**  
```

User goal: Decision memo for team lead to choose between Kanban and todo list  
Artifact type: Decision memo  
Audience: Team lead; knows both tools; needs a recommendation with rationale  
Scope: Kanban vs todo list for a 3-person async team  
Non-scope: Other tools; implementation details; cost analysis  
Success criteria: Memo states a clear recommendation with 3 supporting reasons and 1 risk  
Ambiguity assumptions: [Assumption: team is 3 people, async, no dedicated PM]

```
  
**Phase 2 (abbreviated):**  
```

Sections:

1. Problem statement — why a decision is needed now
2. Options — Kanban and todo list with key characteristics
3. Evaluation — comparison on 3 criteria relevant to a 3-person async team
4. Recommendation — one option with rationale
5. Risks and mitigations — top risk of the recommended option

```
  
**Phase 4 verdict:** REVISE — evaluation criteria were too generic for the stated audience.  
**Phase 5:** Replaced generic criteria with team-size-specific ones. Re-verified: PASS.  
  
---  
  
### Example 2 — Skill draft  
  
**User request:** "Draft a Hermes skill for running weekly reviews."  
  
**Phase 1 (abbreviated):**  
```

User goal: A SKILL.md file for weekly review ritual  
Artifact type: Hermes skill (SKILL.md)  
Audience: Hermes agent; must follow Hermes skill conventions  
Scope: Weekly review procedure only; no daily planning  
Success criteria: Valid frontmatter; When to Use; Procedure with ≥5 concrete steps;  
Pitfalls; Verification; output format defined  
Source requirements: Hermes skill format conventions [AVAILABLE via creating-skills.md]

```
  
**Phase 2 (abbreviated):**  
```

Sections: frontmatter / title / intro / When to Use / Do Not Use For /  
Procedure / Output Format / Pitfalls / Verification  
Missing inputs: none

````
  
**Phase 4 verdict:** REVISE — procedure steps lacked concrete trigger conditions.  
**Phase 5:** Added explicit trigger wording and output format. Re-verified: PASS.  
  
---  
  
## Related Hermes Translations  
  
**As a single-session skill (default):** Load this skill and run all six phases in one session. No Kanban or cron needed. Suitable for most artifacts.  
  
**As a Kanban graph (for multi-profile or durable artifacts):**  
```python  
t1 = kanban_create(title="goal-contract", assignee="<planner-profile>",  
     body="Run Phase 1 of goal-skeleton-fill-verify-revise-learn. Output: goal contract.")  
t2 = kanban_create(title="skeleton", assignee="<planner-profile>",  
     body="Run Phase 2. Input: goal contract from T1. Output: coherent skeleton.", parents=[t1])  
t3 = kanban_create(title="fill", assignee="<writer-profile>",  
     body="Run Phase 3. Input: skeleton from T2. Output: filled artifact.", parents=[t2])  
t4 = kanban_create(title="verify", assignee="<reviewer-profile>",  
     body="Run Phase 4. Input: filled artifact from T3. Output: verification record.", parents=[t3])  
t5 = kanban_create(title="revise", assignee="<writer-profile>",  
     body="Run Phase 5. Input: verification record from T4. Max 2 cycles.", parents=[t4])  
t6 = kanban_create(title="learn", assignee="<planner-profile>",  
     body="Run Phase 6. Input: final artifact from T5. Output: learning capture.", parents=[t5])  
````

Use this shape when the artifact is large, requires specialist profiles, or must survive a session restart.

**As a delegate_task chain (for short synchronous artifacts):**  
Use `delegate_task` for Phases 3 and 4 when the parent agent orchestrates but does not write. Pass the goal contract and skeleton as context to each child.

**As a cron-triggered artifact (for recurring artifacts):**  
Wrap Phase 1 in a self-contained cron prompt that includes the goal contract inline. Cron sessions are stateless — all context must be in the prompt.

---

# 2. Adaptation Report

## What was adapted from `research-paper-writing`

- **Phase 0.4 "Identify the Contribution"** (What / Why / So What, lines 140–148) → generalized into the Goal Contract's `user goal`, `success criteria`, and `ambiguity assumptions` fields. The three-question structure (What / Why / So What) is preserved but renamed for non-research artifacts.
- **Context management table** (lines 786–799: "load one section's context at a time") → adapted into Phase 3 Fill rule 6 ("do not expand scope beyond what the skeleton defines for this section").
- **Two-pass refinement pattern** (lines 871–890) → adapted into Phase 5's revision cycle structure: fix structure first, then content; re-verify after each cycle.
- **Autoreason failure modes table** (lines 764–772) → adapted into the Pitfalls section: "running more than 2 revision cycles without escalating" maps directly to the "no convergence" failure mode.
- **Session startup protocol** (lines 2219–2227) → adapted into Phase 6 Learning Capture: the protocol's "report status" step became the learning capture's `memory candidate` and `open question` fields. SKILL.md:140-148 SKILL.md:871-890 SKILL.md:764-772

## What was adapted from `plan`

- **Plan document structure** (lines 115–180) → adapted into the Skeleton format. The `Objective / Files / Steps / Verification` per-task structure became `Function / Required inputs / Planned output / Acceptance criteria` per-section.
- **Writing Process 6 steps** (lines 182–244) → adapted into Phase 2's coherence check. The "Review the Plan" checklist (lines 235–244) became the skeleton coherence check.
- **Execution handoff** (lines 314–325) → adapted into the Related Hermes Translations section's Kanban graph and delegate_task patterns.
- **Save location pattern** (lines 44–51) → not copied directly, but the Output Format section follows the same "deliver as a clean document" principle. SKILL.md:115-133 SKILL.md:235-244

## What was adapted from `requesting-code-review`

- **Fail-closed reviewer pattern** (lines 125–173) → adapted into Phase 4's `independent review needed` field and the BLOCK verdict. The principle "reviewer gets ONLY the artifact, no shared context" is preserved.
- **Auto-fix loop cap** (lines 194–226: "maximum 2 fix-and-reverify cycles") → directly adopted as Phase 5's default maximum of 2 cycles.
- **Structured verdict format** (lines 184–192: PASS / FAIL / escalate) → adapted into Phase 4's PASS / REVISE / BLOCK decision table.
- **Self-review checklist** (lines 112–123) → adapted into Phase 4's self-check block, generalized from code-specific items to artifact-agnostic ones. SKILL.md:125-173 SKILL.md:194-226

## What was adapted from `subagent-driven-development`

- **Spec compliance FIRST, quality SECOND ordering** (line 216) → adapted into Phase 5's priority rule: "critical defects first (those that cause FAIL on acceptance criteria), then important, then minor."
- **Red Flags section** (lines 204–217) → adapted into the Pitfalls section. "Skip reviews" → "Skipping the goal contract." "Accept close enough on spec compliance" → "Silently dropping defects."
- **Per-task workflow** (lines 56–157) → adapted into Phase 3's fill rules. The "fresh context per task" principle became "fill one section at a time." SKILL.md:204-217

## What was adapted from `kanban-orchestrator` / `kanban-worker`

- **Structured handoff shapes** (`kanban-worker` lines 34–101) → adapted into the Output Format's process summary block. The `summary + metadata` pattern became `Verification / Cycles used / Open items / Assumptions`.
- **Human-in-the-loop block pattern** (`kanban-worker` lines 129–143) → adapted into Phase 4's BLOCK verdict. The "one sentence naming the specific decision you need" rule is preserved.
- **Goal-mode cards** (`kanban-orchestrator` lines 182–204) → referenced in the Related Hermes Translations Kanban graph as an option for Phase 5 (revise card with `goal_mode=True`).
- **Decomposition playbook Step 2** (`kanban-orchestrator` lines 64–83) → adapted into Phase 2's coherence check: "sketch the task graph before creating anything" became "produce a skeleton before filling." SKILL.md:34-101 SKILL.md:129-143

## What was deliberately not copied

- **Git-specific steps** from `requesting-code-review` (diff, static scan patterns, `[verified]` commit prefix, test frameworks) — this skill is not code-specific.
- **TDD cycle instructions** from `plan` and `subagent-driven-development` — not applicable to non-code artifacts.
- **LaTeX quality checklist** from `research-paper-writing` (lines 893–908) — ML-paper-specific.
- **Autoreason loop** from `research-paper-writing/references/autoreason-methodology.md` — too compute-intensive (6 model calls per pass) for a general-purpose skill. Referenced as a future split-out (`diverge-synthesize`).
- **Code-specific task granularity** ("2-5 min per task") from `plan` — not meaningful for document artifacts.
- **`environments: [kanban]`** frontmatter field from `kanban-orchestrator` and `kanban-worker` — this skill is not kanban-specific; the Kanban translation is optional.

## Why this skill should be one skill instead of five skills

The six phases are tightly coupled: each phase's output is the next phase's required input. The goal contract feeds the skeleton. The skeleton feeds the fill. The fill feeds the verification. The verification record feeds the revision. Splitting them into separate skills would require the user to manually chain them, pass context between sessions, and remember which phase they are in. The skill is designed to be loaded once and run end-to-end in a single session. The Related Hermes Translations section shows how to decompose it into Kanban tasks when multi-profile execution is genuinely needed — but that is an optional translation, not the default.

## Where this skill may need to split later

- **`skeleton-first-artifact`** — Phase 2 alone, for users who only need structure generation without the full loop.
- **`goal-recheck-validation`** — Phase 4 alone, for users who have an existing artifact and only need a verification pass.
- **`diverge-synthesize`** — an optional Phase 3 variant using the Autoreason loop (Critic → Author B → Synthesizer → Judge Panel) for high-stakes artifacts where quality justifies 6+ model calls per iteration.
- **`source-constraint-map`** — a pre-Phase 1 step for complex research artifacts where sources must be inventoried and mapped to claims before the goal contract can be written.

---

# 3. API-Call Analysis

**Counting rules applied:**

- One `chat/completions` (or equivalent) request = one model/API call.
- One Hermes tool invocation = one tool call (not itself a model call unless it spawns an agent).
- `skill_view` = one tool call; the agent needs one additional model turn after reading the skill content.
- `delegate_task` = one tool call from the parent; the spawned child agent's model calls are counted separately.
- Background review = reported separately; it fires in a daemon thread after the turn, not as part of the explicit process.

|Mode|Assumptions|Model/API calls|Tool calls|Notes|
|---|---|---|---|---|
|Simple no-tool run|All 6 phases in one agent turn; no file I/O; artifact is short|1–2|0–1|Agent reasons through all phases; may call `write_file` once to save artifact|
|With `skill_view` load|Agent loads skill before starting|2–4|1 (`skill_view`) + 0–2|`skill_view` is a tool call; agent needs 1 more model turn after reading skill content|
|With one verification pass|Phase 4 runs as a separate reasoning step; agent reads source files|2–5|0–4 (`read_file` calls for sources)|Verification may require reading source documents|
|With one revision cycle|Phase 5 adds one more reasoning step after Phase 4|3–7|0–6 (`read_file` + `write_file`)|Revision re-verifies; 2 model turns minimum for revise + re-verify|
|With independent reviewer via `delegate_task`|Phase 4 dispatches a reviewer subagent|2–4 (parent) + 1–3 (reviewer child)|1 (`delegate_task`) + 2–6 (reviewer's tool calls)|Reviewer gets artifact + acceptance criteria; returns structured verdict|
|With Kanban translation|6 Kanban cards, each executed by a separate worker|1–3 per card × 6 = 6–18|3–8 per card × 6 = 18–48|Each card is a separate agent run; dispatcher overhead is not a model call|

```
api_call_estimate:    minimum: 1    typical: 3–6    upper_bound: "18+ (with Kanban translation and independent reviewer)"    unknowns:      - "Number of model calls per phase depends on artifact complexity and whether         the agent needs to read source files — inspect agent/conversation_loop.py"      - "Whether background review fires after the turn (1–3 additional calls in a         daemon thread, separate from the explicit process) — inspect         agent/background_review.py spawn_background_review_thread() call sites"      - "Whether the user asks for an independent reviewer via delegate_task         (adds 1–3 calls per reviewer invocation)"      - "Whether the Kanban translation is used (multiplies calls by number of cards         and number of revision cycles)"    files_to_check_for_exact_count:      - "agent/conversation_loop.py — when model calls happen vs. tool calls"      - "tools/delegate_tool.py lines 250–600 — _run_single_child() for child agent lifecycle"      - "agent/background_review.py — spawn_background_review_thread() call sites"      - "hermes_cli/goals.py — run_kanban_goal_loop() if goal_mode=True is used on Phase 5 card"
```

---

# 4. Blocking Questions

None that prevent authoring the skill as specified. Three notes worth confirming before first use:

**1. Category name.** The frontmatter uses `category: apex-process`. This is a custom category not present in any bundled skill. It will work — Hermes does not validate category values — but it will appear as its own category in `skills_list()`. If you prefer to nest under an existing category like `productivity` or `workflow`, change the `category` field. The install path (`~/.hermes/skills/apex-process/`) is independent of the frontmatter `category` field.

**2. `related_skills` references.** The skill references `plan`, `requesting-code-review`, `subagent-driven-development`, and `kanban-orchestrator`. All four exist in the repo at their expected paths. No phantom references.

**3. No `requires_toolsets` declared.** The skill runs as pure procedural reasoning and does not require any toolset. If the user wants the agent to save the artifact to disk during Phase 3 or Phase 6, the `file` toolset must be active in the session — but this is a session-level concern, not a skill-level constraint. Do not add `requires_toolsets: [file]` unless you want the skill to be hidden in sessions without file tools.