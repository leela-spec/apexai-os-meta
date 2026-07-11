---
title: "Fable Build Plan — Finalized Input"
purpose: "The plan Fable executes to build the final multi-agent/subagent orchestration system, verified against both indexed best practice and real usage — not theory-first. Written by a prior scoping session for Fable to pick up and run; not something the scoping session itself executes."
created: 2026-07-11
status: finalized_input — Fable starts at phase 0 in §2 and locks decisions.md itself using §1 as defaults, subject to whatever the operator has told Fable directly
depends_on:
  - apex-meta/fable-orchestrator/process-blueprint-qa.md
  - apex-meta/fable-orchestrator/fable-execution-best-practices.md
  - apex-meta/ORCHESTRATION-SYSTEMS-INDEX.md
---

# Fable Build Plan — Recommendation

## The core execution principle you asked for

**Every design decision in this build must clear two checks before it's accepted, and both checks must be concrete, not argued in the abstract:**

1. **Best-practice check** — does the `claude-code-orchestration-design` KB (or another indexed source) actually support this pattern? Cite the real page/claim, don't reason from memory.
2. **Real-use check** — does it survive an actual user story run as a simulation, against real repo content? Not "in principle it should work" — actually try it and record what happened.

A design decision that passes #1 but has never been tried against #2 is a hypothesis, not a verified pattern. **Do not build on unverified hypotheses.** This is now the standing execution discipline for this whole initiative — see §4 for the concrete mechanics, and §5 for a worked example that isn't hypothetical.

## 1. Default answers to `process-blueprint-qa.md` (Fable locks these in phase 0)

Accept the RECOMMENDED option on all 8 questions in that file as the default, unless the operator has told Fable otherwise directly:

```yaml
Q1: B  # adopt the subset mapped to Fable/external-model/Codex split, not the whole file verbatim
Q2: accept mapping table as shown
Q3: B  # apex-plan/sync/session stays as-is; this initiative gets only a lightweight supplementary list
Q4: B  # reuse existing CLAUDE.md constraints as the risk gate, no new framework
Q5: B  # Fable verifies external-model output itself, grounded against real repo state
Q6: B  # diverge/converge + systems-engineering framing is a one-time architecture-reconciliation phase, not a standing process
Q7: B  # split "supervisor tool-calling" out as already-covered by Fable's direct tool/Codex use
Q8: B  # lightweight decisions.md + plain task list, not a full Kanban apparatus
```

Fable writes these into `decisions.md` as locked at the start of phase 0, then proceeds — this is a fast default lock, not a stopping point (see `fable-execution-best-practices.md` §6 on not letting a decision round substitute for the actual work).

## 2. Ordered phases

```yaml
phase_0_scope_lock:
  output: decisions.md (process-blueprint-qa.md answers locked)
  gate: operator confirms §1 above (or edits it)

phase_1_user_stories:
  goal: >
    Write concrete user stories describing what the FINISHED orchestration system must let
    someone actually do — not abstract capability lists. Each story becomes a target query /
    acceptance test, not just documentation.
  examples_of_shape:
    - "As the operator, when I hand Fable a messy multi-KB reconciliation task, I want a single
       decision document that resolves every named conflict and cites real KB pages, not invented
       justification."
    - "As a future orchestrator agent, when I need to decide subagent-vs-inline-work, I want the
       claude-code-orchestration-design KB to give me a real, source-cited answer."
    - "As Fable, when I need external deep research, I want a repeatable prompt shape per model
       (fable-execution-best-practices.md §3) that reliably produces a usable, citable result."
  output: apex-meta/fable-orchestrator/user-stories.md (one file, plain list, grows over time)
  note: >
    This directly satisfies the still-open OD2 from orchestrator-education-targeting-handover.md
    (query-eval-pack.json has zero target queries) — these stories ARE those target queries,
    generalized beyond just the one KB.

phase_2_best_practice_check:
  goal: For each user story, find the real page/claim in an indexed KB that should answer it.
  fail_condition: >
    If no indexed source answers a story, that's a real gap — either the story is out of scope,
    or claude-code-orchestration-design needs a new page (see orchestrator-education-targeting-handover.md).
    Do not invent an answer to fill the gap.

phase_3_workflow_plus_simulation:
  goal: >
    For each user story that passes phase 2, draft the actual workflow (the concrete sequence of
    Fable/external-model/Codex steps) and RUN it once as a simulation against real content —
    not a walkthrough on paper. Record what actually happened, including failures.
  output: one simulation record per story (see §5 for the worked example and its shape)
  gate: a workflow is not "adopted" until its simulation record exists and passed, or failed with
        a documented fix.

phase_4_build:
  goal: Implement the actual skills/subagents/scaffolding, using verified workflows as spec.
  method: small batches, Codex for pure execution steps (apex-meta/CODEX_EXECUTION_STANDARD.md),
          Fable for everything requiring judgment.

phase_5_regression:
  goal: >
    Re-run the phase-1 user stories periodically as regression checks whenever the KB, skills, or
    orchestration scaffolding change. Treat them as living acceptance tests, not one-off proof.
```

## 3. Why this ordering (not architecture-first)

The temptation in a build like this is to spend the whole session designing the target architecture in the abstract (which is what `agent-skill-system-research/design-lock-qa.md` and `process-blueprint-qa.md` already did plenty of) and never check whether any of it actually holds up against a real question. You explicitly asked for the opposite: concrete user stories and simulations as the core principle, so architecture decisions get tested against reality early and often, not validated by argument alone.

## 4. What counts as a "simulation" (concrete definition, not vague)

```yaml
simulation_definition:
  is: "An actual attempt to satisfy the user story using real repo content, with the real result recorded — pass, partial, or fail, honestly."
  is_not:
    - a hypothetical walkthrough ("Fable would read X, then Y, then...")
    - a design doc describing how the workflow should work in principle
    - an argument that a pattern "should" work because it matches best practice
  minimum_record_shape:
    - the user story being tested
    - the actual steps taken (real tool calls, real files read)
    - the actual result (quote or cite it)
    - verdict: pass / partial / fail, with the reason
```

## 5. Worked example — already run once, during scoping, as proof this discipline is achievable

This example was executed once already (by the session that wrote this plan) to prove phase 2/3's discipline actually works on real KB content before handing the plan to Fable — it is not something Fable needs to redo, just the bar every one of Fable's own phase-1 stories must clear.

**User story:** "As a future orchestrator agent, when I need to decide subagent-vs-inline-work for a given task, I want `claude-code-orchestration-design` to give me a real, source-cited answer."

**Best-practice check (phase 2):** Searched the KB for subagent-related pages; found `wiki/summaries/agent-vs-subagent-vs-skill.md` — ranked as the KB's own top source match for this exact topic (231 keyword hits, highest in the corpus per its own `topic-source-rankings.json`).

**Simulation (phase 3) — actually read the page and checked it against the story:**

```yaml
result:
  does_it_answer_the_story: yes
  evidence:
    - "Use the main conversation over a subagent when the task needs frequent back-and-forth...
       or when latency matters, since subagents start fresh and may need time to gather context."
    - "Use a subagent... when the task produces verbose output you don't want polluting your main
       context, when you want to enforce specific tool restrictions, or when the work is
       self-contained and can return a short summary."
  source_grounding: "Real quotes with line-number pointers into raw/source-groups/.../sub-agents.md,
                     not paraphrase from training data."
  honesty_check: "Page itself flags two unresolved uncertainty triggers (U001, U002) instead of
                  overclaiming completeness — a good sign, not a defect."
verdict: PASS
```

**What this proves:** the KB's authoring pass from 2026-07-10 produced at least one page that survives a real simulation, not just a structural lint check. This is the bar every other user story in phase 1 needs to clear — and the honest record above is the shape every future simulation record should take.

## 6. Where Fable starts

Phase 0 in §2: lock `decisions.md` from §1's defaults, then move directly into phase 1 (writing the first real batch of user stories) in the same session — per `fable-execution-best-practices.md` §6, a decision-lock step is a fast preamble, not a stopping point.
