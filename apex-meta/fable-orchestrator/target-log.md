---
title: "Target Log"
purpose: "The overarching mission and its milestone breakdown. Update at the start of each work session, not mid-session."
created: 2026-07-11
---

```okf
document:
  id: fable-orchestrator-target-log
  title: Target Log
  status: active
  created_date: 2026-07-11
  repository: leela-spec/apexai-os-meta
  branch: main
  package_path: apex-meta/fable-orchestrator/

scope:
  owns:
    - overarching_target_statement
    - six_milestone_breakdown
    - current_target_pointer
    - session_log
  must_not_own:
    - user_stories_content
    - discovery_findings_content
    - build_execution
```

# Target Log

## Overarching target

Create the final orchestration system, merging the old Apex agent-swarm system and the new `apex-plan`/`apex-sync`/`apex-session` system into one coherent whole — where Fable itself evaluates the soundness, impact, resilience, and intent of each system's workflows and agents, supported by external research where the reasoning is heavy, verified by the operator at each milestone.

## Milestones

1. **Understand intent across every version.** The four versions in scope: `operator-research-orchestration-20260711` (the original operator-research KB that started this initiative), `old-apex-full-orchestration-agent-kb` (v1 — the compiled, do-not-delete role-doctrine corpus, cited as `source_doctrine` elsewhere in this system), `old-apex-full-orchestration-agent-kb-v2` (the 9-agent-roster / BUILD-VERIFY-LOCK iteration), and `apex-plan-sync-session-workflow-v2` (the current three-package `apex-plan`/`apex-sync`/`apex-session` system). For each: what it was trying to build, the biggest decisions it made, where it overlaps with the others, what patterns repeat across all four. Artifact: `discovery-notes.md`. Gate: operator verifies.
2. **Understand resilience best-practice — through `claude-code-orchestration-design`.** Concretely: read its mechanism-ladder page (`wiki/summaries/minimal-claude-orchestration-architecture.md` — smallest sufficient mechanism before escalating), its resilience page (`wiki/summaries/agent-skill-orchestration-resilient-workflows.md` — resilience is about *where the plan/state lives*, not which agent runs it), and its deterministic/LLM-split page (`wiki/summaries/apex-application-orchestration-patterns.md`). Extract the concrete resilience dimensions this KB uses (mechanism-ladder position, state-holding location, presence/absence of adversarial cross-check, role-vs-state permission separation, context-budget handling) so milestone 3 has something specific to score against. Where the KB itself is thin on a specific question, produce a prompt for an external model (per `fable-execution-best-practices.md`'s model-routing table) instead of guessing. Artifact: `discovery-notes.md` §4. Gate: operator verifies.
3. **Evaluate soundness/impact/resilience of what already exists — against milestone 2's dimensions, specifically.** "What exists": the old Apex v2's 9-agent roster + BUILD/VERIFY/LOCK state machine, and the current `apex-plan`/`apex-sync`/`apex-session` three-package boundary. How: score each system's *actual* mechanisms against each resilience dimension milestone 2 produced (not a general impression) — where does each system hold its state/plan, does either have an adversarial cross-check step, is permission modeled by role or by state, how is context budget handled — citing milestone 1's findings as evidence, not assumption. Output: a explicit per-dimension comparison, not a prose verdict. Gate: operator verifies.
4. **Resolve the 8 open architecture questions in `design-lock-qa.md`** — Q1 topology (single-agent/workflow/multi-agent), Q2 how the in-scope systems relate (merge/layer/supersede), Q3 skill-file granularity, Q4 how subagents get spawned/scoped, Q5 the shared state/handoff schema, Q6 where operator-approval gates live, Q7 drift-control mechanism, Q8 the fate of the old KB's 9-agent roster/state-machine. Each question lists its own candidate directions and blast radius in that file — milestones 1–3 supply the evidence to actually decide between them; the operator's noted starting hypotheses are explicitly marked there as things to verify, not locked answers.
5. **Draft the target architecture** — only after 1–4 are verified.
6. **Build it** — the actual construction, Codex for execution, per `build-plan.md`.

## Current target

- **`apex-meta/orchestration/`** — **the final orchestration system, assembled 2026-07-11** per `implementation-plan.md` (operator direction: no external calls, Fable builds directly). Milestones 1–5 done; milestone 6 = per-story adoption via real simulation records in `apex-meta/orchestration/simulations/` (first candidate: US-IDEA-01) plus the open build items in `apex-meta/orchestration/ARCHITECTURE.md` §7.
- `apex-meta/orchestration/user-stories/` — the 7 stories, moved into the system package as its regression suite.

## Log

Fable can enter logs for changes here

- **2026-07-11 (Fable session, direct-build run — organization switch):** Operator redirected: no external model calls anymore; Fable designs and builds the final system directly. Prior external-research returns (P1 role-vs-state, P2 adversarial-review) were critically ground-checked in `prompts/PromptAnswers/research-integration-note.md` — P1's minimal `authority.state` field adopted; P2's two-lens blind review adopted Claude-only (cross-family judge dropped per operator direction; no runtime external-model surface exists in the repo). Then wrote and executed `implementation-plan.md`: **milestone 5 built** — `apex-meta/orchestration/` package (00-START-HERE, ARCHITECTURE, GLOSSARY, schemas: handoff-packet/authority-state/review-verdict, workflows: orchestrator-run/detective-review, simulations scaffold), 7 agent definitions in `.claude/agents/`, user-stories moved via `git mv` with all path references updated; `ORCHESTRATION-SYSTEMS-INDEX.md` updated (§4 new package row, §5.3 glossary resolved). **Milestone 6 status:** assembled, not yet adopted — adoption gated on simulation records; open build items: authority-digest enforcement code in apex-session write path, registry materialization.

- **2026-07-11 (Fable session, orchestrator-worker fan-out run):** Ran PRC-MULTI-001 with three parallel internal research workers (one per source system + one on the reference KB) plus direct reads of `best-practice-report.md` and the full user-stories package. Produced: `evaluation-matrix.md` (milestone 2 dimensions grounded with citations + milestone 3 per-dimension scoring of old-apex-v2 vs. apex-plan/sync/session), `design-lock-answers.md` (milestone 4 — proposed, evidence-based answers to all 8 design-lock questions; every answer operator-gated), and `prompts/external-research-pack-20260711.md` (5 copy-out prompts: 4 thin-dimension research prompts for ChatGPT/Gemini per the routing table, 1 Perplexity repo-grounded adversarial verification of the evaluation matrix itself). Resolved with direct evidence: the v2 "Phase 1 only" framing was stale — Phase 2 wiki exists (index says 17 pages, 19 on disk, 6 placeholders); corrected `discovery-notes.md` §2 and `ORCHESTRATION-SYSTEMS-INDEX.md`. **Gates now pending:** operator verification of milestones 1–4 artifacts. Milestone 5 (architecture draft) deliberately NOT started — target-log rule: only after 1–4 are verified.