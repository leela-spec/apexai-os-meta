---
doc_type: design-lock-qa
task_id: fable-orchestrator-process-blueprint
version: 1
created: 2026-07-11
source_reviewed: apex-meta/kb/old-apex-full-orchestration-agent-kb-v2/OperatorResearch/ProcessRanking_GPT&MasterOA.md
instructions: >
  Answer by picking or editing an option per question. Every question has a RECOMMENDED
  default. This Q&A must be answered and locked into decisions.md before the actual
  Fable-led orchestration build begins — see README.md sequencing.
---

# Process Blueprint Q&A — Which Processes From `ProcessRanking_GPT&MasterOA.md` to Reuse

## Context: why this file, despite the domain mismatch

`ProcessRanking_GPT&MasterOA.md` ranks 20 process/methodology patterns (Double Diamond, Scrum, NIST AI RMF, ReAct, CRISP-DM, Kanban, orchestrator-worker fan-out, chain-of-verification, etc.) for a completely different domain — personal "Master of Arts" workflows: workshops, Leela use-cases, self-employment setup, martial-arts content. **None of its worked examples apply here.** What's reusable is the abstract process taxonomy and its ranking logic (coverage, complementarity, fit-to-execution-mechanism, evidence/maturity, risk control) — those criteria are domain-agnostic and map cleanly onto "build the final Claude Code multi-agent orchestration system." This Q&A re-ranks the same 10 top processes against *this* build's actual needs.

## Q1. Adopt the file's "minimal complete process library" build order as the blueprint skeleton?

**Options:**
- A. Adopt it near-verbatim, just retranslating each process's *examples* (not its mechanism) to this repo's domain.
- B. **RECOMMENDED** — Adopt the subset that maps directly onto the stated Fable/external-model/Codex split (see Q2), treat the rest as optional/situational rather than mandatory build order.
- C. Discard this file; design the blueprint from scratch using only Anthropic's own orchestration guidance (already synthesized in `apex-meta/handoff/agent-skill-system-research/best-practice-report.md`).

**Rationale:** The file's own top-3 (`PRC-CORE-001` goal-to-verified-artifact loop, `TEMPLATE-KANBAN-001` durable multi-agent task graph, `PRC-MULTI-001` orchestrator-worker fan-out/fan-in) map almost exactly onto what this build already needs: a per-task backbone, a way to track the massive multi-system reconciliation work, and the exact Fable→{ChatGPT/Gemini/Perplexity/Codex} split the operator described. But several ranked-highly processes (Scrum sprints, CRISP-DM, Double Diamond) were ranked for a *team* doing *recurring creative/business* work — this build is one Fable session doing a *bounded* architecture-and-build task, so blind full adoption would add process for its own sake (explicitly against this repo's own anti-overengineering norm — see `apex-meta/handoff/agent-skill-system-research-run` handover's own `ANTI-OVERENGINEERING` clause).

**Blast radius:** Sets how much of this file's 10-process/20-process structure survives translation vs. gets dropped. Determines the shape of every other answer below.

---

## Q2. Map the file's top processes onto the Fable/external-model/Codex roles — confirm or correct this mapping

| ProcessRanking process | Proposed role in the Fable build | Confirm / edit |
|---|---|---|
| `PRC-MULTI-001` Orchestrator-Worker Fan-Out/Fan-In | **Core mechanism.** This *is* the Fable → {ChatGPT deep research, Gemini deep research, Perplexity+GitHub, Codex execution} pattern, generalized. | — |
| `PRC-HANDOFF-001` Handoff With Guardrails | **Core mechanism.** Governs the prompt-out/result-in packet shape between Fable and each external model (see `fable-execution-best-practices.md`). | — |
| `PRC-CORE-001` Goal-to-Verified-Artifact Loop | **Per-task backbone.** Applies inside each individual reconciliation/build task Fable runs. | — |
| `PRC-VERIFY-001` Chain-of-Verification Gate | **Mandatory**, arguably more important here than in the original file's domain — every external-model output is un-trusted input until Fable checks it against the repo's real state (this repo's KBs already carry hard-won lessons about proxy-objective failure and shell/thin-content false-positives — see `Apex-KB-Semantic-Quality-Realization-Handover.md`). | — |
| `TEMPLATE-KANBAN-001` Durable Multi-Agent Task Graph | **Optional, scoped down.** A full Kanban board is built for distributed human teams; a single-session Fable run needs a lighter durable task list (see Q8), not necessarily the full lanes/dependencies/review-gate apparatus. | — |
| `PRC-RISK-001` Govern-Map-Measure-Manage | **Reuse existing gate, don't rebuild.** This repo already has an operator-gate/constraint model (`.claude/CLAUDE.md` constraints, `apex-kb`'s failure-behavior contract). Map this process onto *that*, don't invent a parallel risk framework. | — |
| `PRC-DATA-001` CRISP-DM Evidence/Data Flow | **Situational.** Relevant only for the KB-reconciliation sub-phase (structuring the merged, messy corpus), not for the build as a whole. | — |
| `PRC-DIV-001` Diverge-Converge Diamond | **Situational.** Useful specifically for the "many systems, need one design" architecture-reconciliation decision phase; not a standing process. | — |
| `PRC-SYS-001` Systems Engineering Flow | **Situational.** Useful for designing the target orchestration system itself (requirements → architecture → implementation → verification); overlaps with `PRC-CORE-001` for this build's scale — likely redundant, drop unless a gap shows up. | — |
| `PRC-SCRUM-001` Sprint Artifact Loop | **Drop for this build.** Designed for recurring human-team cycles; this is a single continuous Fable-led effort, not a sprint cadence. | — |

**Recommended default:** accept the mapping as shown; edit only the rows marked situational/drop if the operator disagrees.

**Blast radius:** This table *is* the blueprint. Everything in `fable-execution-best-practices.md` assumes this mapping.

---

## Q3. Does `TEMPLATE-KANBAN-001` (durable multi-agent task graph) replace or run alongside the existing `apex-plan`/`apex-sync`/`apex-session` three-package boundary?

**Options:**
- A. Replace — build a new Kanban-style graph specifically for this initiative, independent of apex-plan/sync/session.
- B. **RECOMMENDED** — Run alongside, scoped down: use apex-plan/apex-sync/apex-session as-is for anything that already fits their contract (task capture, dependency proposals, gated mutation); only add a lightweight supplementary task list *inside this folder* (`decisions.md` + a running log) for orchestration-specific work that doesn't fit those three packages' scope (e.g., cross-KB reconciliation, external-model prompt tracking).
- C. Ignore Kanban/task-graph structure entirely; treat this as informal session-to-session continuity via handoff docs only.

**Rationale:** This repo already has a validated three-package planning boundary (`apex-plan-sync-session-workflow-v2` KB, synthesized in `agent-skill-system-research/best-practice-report.md`). Building a second, parallel task-graph system risks exactly the kind of duplicated-boundary problem that report's decision 1 already warned against.

**Blast radius:** Determines whether this initiative gets its own tracking artifact or feeds into the existing apex-plan/session surfaces.

---

## Q4. Where does `PRC-RISK-001` (govern/map/measure/manage) actually plug in?

**Options:**
- A. New standing risk-review step before every Fable decision.
- B. **RECOMMENDED** — No new step; treat the existing `.claude/CLAUDE.md` constraints (operator confirmation before batch-writes, no destructive/irreversible actions without approval, gated mutation per `apex-sync`/`apex-session`) as this build's risk-gate, and only add anything new if a real gap is found during the run.
- C. Skip entirely — treat this build as low-risk since it's KB/wiki content, not production code.

**Rationale:** This build *does* do real file-moving and reconciliation across a "massive" corpus per the operator's own framing — not risk-free — but the repo's existing constraint set already covers the relevant risk surface (irreversible ops, batch-writes, shared state). Adding a second risk framework on top would be the overengineering pattern this task's own prior work explicitly warned against.

**Blast radius:** Low — this just confirms "reuse what exists" rather than inventing new governance.

---

## Q5. Who runs the Chain-of-Verification pass on external-model output?

**Options:**
- A. The operator manually judges each ChatGPT/Gemini/Perplexity response before pasting it back to Fable.
- B. **RECOMMENDED** — Fable runs the verification pass itself once results are pasted back in: cross-check claims against the actual repo state (files, KBs, existing decisions) before acting on them, exactly the discipline already proven to work in the 2026-07-10 KB authoring pass (real claim grounding, explicit confidence downgrades, no inventing detail to sound complete).
- C. No formal verification — trust external-model output as-is once relayed.

**Rationale:** Fable has direct repo access and the external models don't (except Perplexity's GitHub connector) — Fable is the only party positioned to actually check a claim against ground truth. Requiring the operator to verify manually every time defeats the point of outsourcing reasoning to save the operator's own effort, not just Fable's tokens.

**Blast radius:** Sets a hard requirement into `fable-execution-best-practices.md`: every external-model result gets a grounding check before being acted on, not just relayed into a file.

---

## Q6. Scope of `PRC-DIV-001` / `PRC-SYS-001` — architecture-reconciliation phase only, or standing process?

**Options:**
- A. Standing process — run diverge/converge and systems-engineering framing on every sub-task.
- B. **RECOMMENDED** — Scoped to one specific phase: reconciling the multiple existing orchestration KBs/systems (per `ORCHESTRATION-SYSTEMS-INDEX.md` §5's open overlaps) into one target architecture. Once that architecture is decided, later sub-tasks use `PRC-CORE-001` only.
- C. Skip both; go straight from "many systems" to "final system" without an explicit divergence/framing step.

**Rationale:** The actual hard problem stated by the operator is architectural reconciliation across systems that "should be compatible" but currently aren't reconciled — that's exactly a diverge/converge + systems-engineering-shaped problem, but only once, not repeatedly.

**Blast radius:** Confirms there's one explicit "decide the target architecture" phase before build work starts, not an ongoing methodology applied to every task.

---

## Q7. Confirm the file's own "deliberately not prioritize now" list still applies here

The file explicitly deprioritizes: Tree-of-Thoughts search (token-expensive), Group Chat Review (noisy), Chain-of-Draft (less important than correctness here), Supervisor Tool-Calling (absorbed by the orchestrator-worker pattern already adopted), Plan-and-Solve (absorbed by `PRC-CORE-001`).

**Options:**
- A. Confirm all five stay deprioritized for this build too.
- B. Re-examine Supervisor Tool-Calling specifically — it's arguably closer to what Fable does when calling Codex/deterministic tools directly (vs. the human-relayed ChatGPT/Gemini/Perplexity loop), so it may deserve separate treatment rather than blanket deprioritization.
- **RECOMMENDED**: B — split it: keep the other four deprioritized as originally reasoned, but treat "supervisor tool-calling" as already covered by Fable's direct tool use inside Claude Code (Bash, file edits, Codex handover) rather than deprioritizing it as a gap.

**Rationale:** The original reasoning ("worker-as-tool orchestration... Kanban/delegation more urgent") was written before this build's specific human-relayed vs. direct-tool-call split existed. Worth one explicit look rather than blanket-inheriting the old verdict.

**Blast radius:** Small — affects only how `fable-execution-best-practices.md` frames Fable's own direct tool/Codex calls vs. the human-relayed external-model loop.

---

## Q8. How lightweight should the "durable task graph" for this initiative actually be?

**Options:**
- A. Full Kanban implementation: lanes, dependencies, review gates, per-task packets, synthesis step — as `TEMPLATE-KANBAN-001` describes it for a multi-profile human team.
- B. **RECOMMENDED** — A single running `decisions.md` (locked answers) plus a plain markdown task list inside `apex-meta/fable-orchestrator/` (open items, in-progress, done) — durable enough to survive a session break, light enough not to become its own maintenance burden.
- C. No durable artifact at all — rely on chat-session continuity only.

**Rationale:** `TEMPLATE-KANBAN-001` was designed for coordinating multiple human profiles across days/weeks. This build is one Fable session (possibly resumed) coordinating itself plus prompted-out external models — a full Kanban apparatus is more process than the actual coordination need.

**Blast radius:** Sets the concrete artifact shape for tracking this initiative's own progress, separate from any apex-plan/session task tracking (per Q3).
