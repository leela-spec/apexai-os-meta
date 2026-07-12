---
title: "Discovery Notes"
purpose: >
  Durable, citable understanding of the target and its four source materials,
  built in parallel with apex-meta/orchestration/user-stories/user-stories.md (a separate, already-complete input, not something this file replaces). Recheck
  and update each section as milestone work in target-log.md progresses —
  do not treat any section here as final until the operator has verified it.
status: "seeded from a first research pass — not yet operator-verified"
created: "2026-07-11"
---

```okf
document:
  id: fable-orchestrator-discovery-notes
  title: Discovery Notes
  status: seeded_not_verified
  created_date: 2026-07-11
  repository: leela-spec/apexai-os-meta
  branch: main
  package_path: apex-meta/fable-orchestrator/

scope:
  owns:
    - source_understanding_per_kb
    - citations_to_raw_kb_pages
    - operator_open_items
  must_not_own:
    - user_stories_content
    - final_architecture_decisions
```

# Discovery Notes

## 0. Target / mission (from target-log.md)

Create the final orchestration system, merging the old Apex agent-swarm system
and the new `apex-plan`/`apex-sync`/`apex-session` system into one coherent
whole — where Fable itself evaluates the soundness, impact, resilience, and
intent of each system's workflows and agents, supported by external research
where the reasoning is heavy, verified by the operator at each milestone.

Six milestones (full detail, incl. named sources/dimensions/questions: `apex-meta/fable-orchestrator/target-log.md`):
1. Understand intent across every version — the four versions are `operator-research-orchestration-20260711`, `old-apex-full-orchestration-agent-kb` (v1), `old-apex-full-orchestration-agent-kb-v2`, `apex-plan-sync-session-workflow-v2`. **This file is the artifact for that.**
2. Understand resilience best-practice — through `claude-code-orchestration-design`'s mechanism-ladder, resilience, and deterministic/LLM-split pages; see §4 below for the extracted dimensions.
3. Evaluate soundness/impact/resilience of what exists — the old Apex v2 9-agent/BUILD-VERIFY-LOCK model and the current `apex-plan`/`apex-sync`/`apex-session` boundary, scored against milestone 2's dimensions specifically, not a general impression.
4. Resolve the 8 open architecture questions in `design-lock-qa.md` (Q1 topology, Q2 system relation, Q3 skill granularity, Q4 subagent spawning, Q5 shared state model, Q6 gate placement, Q7 drift control, Q8 old-KB roster fate).
5. Draft the target architecture.
6. Build it (Codex, per `build-plan.md`).

`apex-meta/orchestration/user-stories/` (7 complete stories, manifest, connection ledger) is **input material** for milestone 1 and later milestone 5 — not this initiative's final deliverable. Separate track from this file.

---

## 1. Old orchestration system — v1 (`old-apex-full-orchestration-agent-kb`)

**Status:** fully compiled, 59 commits, 18 wiki pages, do-not-delete, cited as `source_doctrine` by live skill specs.

**What it was:** a durable, source-preserving *role-doctrine architecture* for an agent swarm (formerly "OpenClaw") — valuable as a reusable knowledge-storage pattern, not as a live runtime spec to copy verbatim.
— `wiki/summaries/old-agent-kb-architecture.md`

**Core architecture:** five-file scaffold per role — `ESSENCE.md` (compact activation surface), `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md`, `LEARNING_QUEUE.md` (candidate-only, never auto-promoted).
— `AGENT_KB_INDEX.md`

**Roles:** `alfred` (intake/routing, no system control) · `meta_ops` (orchestration/sequencing, not validation) · `meta_strategy` (options/recommendations) · `meta_detective` (validation/challenge — does not implement fixes or mutate canon) · `special_ops__ai_handling_routing` (advisory routing) · `special_ops__hygiene_clean` (structural QA).
Meta Detective's five "modes" (evidence_source_verifier, contradiction_logic_auditor, boundary_authority_guardian, risk_failure_mode_red_teamer, verdict_escalation_synthesizer) are **lenses inside one role, not separate agents.**
— `wiki/entities/old-agent-roles.md`, `wiki/entities/meta-detective-internal-modes.md`

**Biggest design decisions:** compact `ESSENCE.md` files keep roles retrieval-sized; owner/validator separation prevents self-validation (`OKB-DOCTRINE-003`); candidate learning stays non-authoritative until reviewed; validation "modes" deliberately kept as lenses to avoid agent sprawl.

**Self-noted weaknesses (real tensions the KB records about itself):**
- Agent sprawl if the five-file scaffold is reused as literal current agents (`A01-T001`).
- Appendix/source sprawl risk without index-first retrieval (`A01-T002`).
- Execution-control conflation — old `meta_ops` held execution control; conflating with current semantic KB work risks unintended mutation (`A02-T001`, `A03-T001`).
- Mode-to-agent drift risk (`A02-T002`).
- Historical paths ≠ current authority — old paths are evidence, not live authority, without reopening raw sources (`A03-T002`).
- Overfitting risk to obsolete paths/implementations (`A04-T002`).
- Open questions still unresolved: `audit/semantic-open-questions.md` (`OKB-RERUN-Q001`–`Q004`) — which patterns should become live Apex skill text vs. wiki-only doctrine; whether validation modes should ever become separate current-system surfaces.

**Migration note:** `wiki/summaries/migration-to-claude-native-orchestration.md` + `wiki/concepts/migration-safety-patterns.md` (confidence: mixed) — all claims require reopening raw sources before promotion into the current system.

---

## 2. Old orchestration system — v2 (`old-apex-full-orchestration-agent-kb-v2`)

**Status correction (resolved 2026-07-11 with direct file evidence):** the "Phase 1 only, no Phase 2 wiki" framing was stale. `wiki/index.md` (auto-generated 2026-07-11T11:42:03Z) states "Compiled page count: 17", and 19 compiled page files actually exist on disk across audit/concepts/entities/summaries (the index undercounts by 2 — `explicit-handoff-continuity.md` and `role-state-permission-separation.md` exist but aren't enumerated; 6 "Untitled topic" placeholders remain). So: Phase 2 compilation is real but incomplete, alongside the three `ingest-analysis/phase1-*.md` files. `ORCHESTRATION-SYSTEMS-INDEX.md`'s row was corrected the same day. Remaining operator question is narrower: whether the 17-19 compiled pages are treated as authoritative or as needing an audit pass given the undercount/placeholders.

**What v2 changed vs. the original:** per the source's own "Self-check" section (`raw/other/managed/rules/AGENT_SWARM_INTERACTION_CANON.md`, ~L464-521) — **preserved** the hybrid semantic-role + operational-state model, six-role taxonomy, and three-state permission model; **tightened** `*_vNext` filename dependencies into final-system sibling paths; replaced `AGENT_INSTRUCTION_BLOCK_vNext.md` with a compact `managed/rules/AGENTS.base.md` anchor; pushed QA/escalation/promotion/file-grammar detail to sibling files instead of duplicating it; dropped advisory/transitional sections not tied to governing law. **Unresolved:** whether `PROMOTER` stays a role vs. becomes a governed mode; whether `VERIFIER`/`AUDITOR` should merge.

**The 9-agent roster** (`raw/other/managed/agents/AGENT_INDEX.md`, compiled at `wiki/entities/first-wave-agent-roster.md`):
`alfred` → `meta_ops` → `meta_strategy` → `meta_detective` → `special_ops__knowledge_bank` → `special_ops__informatics_design` → `special_ops__prompts_workflows` → `special_ops__ai_handling_routing` → `special_ops__hygiene_clean` — each with a named validator role (full mapping in the roster file). Domain masters explicitly excluded from this seed set.

**BUILD/VERIFY/LOCK mechanics** (`AGENT_SWARM_INTERACTION_CANON.md`, "Operational state model", ~L169-284): state is the actual permission layer (roles are only accountability). **BUILD** = bounded creation, no self-verification/truth mutation. **VERIFY** = review/reconciliation/promotion-proposal, no silent rewrites or unilateral mutation. **LOCK** = read-only/frozen unless a governing protocol lifts it. Transitions: `BUILD→VERIFY`, `VERIFY→BUILD` (loop-back), `VERIFY→LOCK` (escalation), `LOCK→BUILD` (explicit lift only). Forbidden: self-promotion from BUILD, disguised VERIFY rewrites, convenience LOCK overrides.
— `wiki/summaries/resilient-iterative-orchestration.md`, `wiki/concepts/macro-meso-micro-synthesis-loop.md`

**Why it stalled — evidence is weak, not conclusive:** no file states an explicit stall reason. Closest signal: `ingest-analysis/phase1-failure-evidence.md` catalogs recurring failure families (authority drift, self-review/role conflation, source-pointer loss, candidate-to-canon leakage) flagged high-impact in `wiki/audit/high-impact-conflict-register.md` — these read as the governance risks the system was designed against, not direct evidence of why ingestion paused (flagged `U-F02`).

---

## 3. apex-sync-session-plan (`apex-plan-sync-session-workflow-v2`)

**Purpose:** strict separation of concerns across the project-management lifecycle — proposing work, computing deterministic state, recording confirmed outcomes — so semantic reasoning, script-backed computation, and durable mutation never bleed into one another.

**Boundary:**
- **apex-plan** — proposal/planning layer. Proposes epics/tasks/dependencies/priority/due-date rationale/provisional focus. Produces an operator-reviewed `apex_plan_packet`. Must NOT run scripts, compute exact rankings, rebuild registries, or mutate state.
- **apex-sync** — deterministic computation layer, delegates to `scripts/apex_sync.py` (dry-run-first JSON). Produces next-action/blocker/registry/stale/drift/score/dependency reports. Only write exception: a narrow non-dry-run-authorized update to `apex-meta/registry/index.md`. Must NOT author plans, narrative, or handoff files.
- **apex-session** — confirmed-mutation layer. Creates the H6 handoff artifacts (`task_plan.md`, `findings.md`, `progress.md`, `next-session.md`); validates status changes before treating them as confirmed. Must NOT rank tasks, scan blockers, rebuild registries, or run scripts.
— `wiki/entities/apex-plan.md`, `wiki/entities/apex-sync.md`, `wiki/entities/apex-session.md`, `wiki/concepts/three-package-boundary.md`

**Handoff flow:** apex-plan → apex-sync (exact computation/dependency validation/blockers/registry/drift/scoring); apex-plan → apex-session (durable updates/status mutation/progress/findings/next-session context); apex-session → apex-plan (feeds context back, but does not compute focus/ranking itself — apex-sync stays the computation authority).

**Recorded gaps:** whether `apex_plan_packet`, `scripts/apex_sync.py`, and H6 artifacts each warrant dedicated concept pages; the KB is explicitly minimal (Phase 1 analysis + PASS report only) — no query outputs or deterministic reports yet; next step is index/lint/audit/status checks after Phase 2 compilation.

---

## 4. Claude orchestration design best practice (`claude-code-orchestration-design` + Fable's own synthesis)

**Core principles (raw KB):**
- **Mechanism ladder** — start with the smallest sufficient mechanism (plain Markdown/YAML → skills → workflows → ephemeral subagents → persistent agents → deterministic scripts/hooks → plugins/MCP), escalate only when the current rung can't carry the work safely/auditably/token-efficiently.
  — `wiki/summaries/minimal-claude-orchestration-architecture.md`
- **Resilience = who holds the plan**, not which agent runs it: subagents/skills keep the plan in Claude's turn-by-turn context (restarts on interruption); workflows externalize loop/state to a script (resumable).
  — `wiki/summaries/agent-skill-orchestration-resilient-workflows.md`
- **Deterministic/LLM split** — exact computation to deterministic code, ambiguity/synthesis to the LLM — mirrored in `apex-kb`'s own skill contract.
  — `wiki/summaries/apex-application-orchestration-patterns.md`
- **Small stable role set**, escalate to named persistent agents only for genuine durable identity/memory/ownership.
  — `handoff/agent-skill-system-research/best-practice-report.md` §3

**Failure modes warned against:** context collapse (state living only in-context, lost on crash/interruption); no adversarial cross-check (subagent chains lack independent review — "structurally complete, semantically ungrounded output" named as an already-observed failure); premature agent-system building; role proliferation without a state/permission layer; candidate-vs-canon leakage; context-budget exhaustion.

**Already applied to Fable** (`fable-orchestrator/fable-execution-best-practices.md`): mechanism-ladder discipline → model-routing table (Fable orchestrates; ChatGPT/Gemini/Perplexity do external reasoning; Codex does deterministic execution only, per `CODEX_EXECUTION_STANDARD.md`); adversarial-review principle → mandatory verification contract (every external-model claim grounded against real repo state before acting); context-budget-as-scarce-resource → write verified extracts to files immediately, keep only pointers in context; deliverable-over-process and delete-safety rules round out session discipline.

**Gaps between raw KB and what's synthesized:** most of the raw KB is still `not_started`/`llm_proposed`, not operator-reviewed; no page yet verifies whether Apex's *own* skills actually use workflow-layer resilience or still rely on the weaker subagent/skill layer (`U002`); `best-practice-report.md` flags an unresolved tension between role-based vs. state-based permission models across all three systems it reviewed; persistent-agent roster, plugin/MCP packaging, and a unified handoff schema remain explicitly deferred (`U001`–`U003`).

---

## Open items for the operator

1. ~~Resolve the v1/v2 "Phase 2 already compiled" discrepancy (§2)~~ **Resolved 2026-07-11** — the "Phase 1 only" framing was simply stale (see §2 status correction). Narrower remaining question: are v2's compiled pages authoritative as-is, or do the index undercount + 6 placeholder topics warrant an audit pass before citing them as settled?
2. Decide whether `PROMOTER`/`VERIFIER`/`AUDITOR` role questions (v1 and v2 both flag variants of this) should be folded into milestone 3's soundness evaluation or milestone 4's architecture questions.
3. Nothing here has been operator-verified yet — this is a first research pass, not a locked understanding.
