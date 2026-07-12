---
title: "Design Lock Answers — Milestone 4 (proposed)"
purpose: >
  Evidence-based proposed answers to the 8 open architecture questions in
  apex-meta/handoff/agent-skill-system-research/design-lock-qa.md, decided from
  milestones 1-3's findings (discovery-notes.md, evaluation-matrix.md), the user-stories
  package, and the best-practice report — not from pre-picked defaults.
created: 2026-07-11
status: "proposed — every answer here is operator-gated; milestone 5 (architecture draft) must not start until the operator verifies milestones 1-4 including this file"
---

```okf
document:
  id: fable-orchestrator-design-lock-answers
  title: Design Lock Answers
  status: proposed_not_locked
  created_date: 2026-07-11
  repository: leela-spec/apexai-os-meta
  package_path: apex-meta/fable-orchestrator/

scope:
  owns:
    - proposed_answers_q1_q8_with_evidence
    - external_research_dependencies_per_answer
  must_not_own:
    - milestone_5_architecture_draft
    - build_execution
```

# Design Lock Answers (proposed)

Evidence keys used below:
- **EM** = `evaluation-matrix.md` (milestone 2 dimensions + milestone 3 scoring, all file-cited)
- **DN** = `discovery-notes.md` (milestone 1 source understanding)
- **US** = `apex-meta/orchestration/user-stories/user-stories.md` (esp. §3 shared context, §6 coverage matrix, §7 "Implications for Fable")
- **BPR** = `apex-meta/handoff/agent-skill-system-research/best-practice-report.md`

---

## Q1. Topology → **B, with durable *accountabilities*, not always-on agents** (operator hypothesis partially confirmed, partially corrected)

**Answer:** Fixed workflow backbone with ephemeral, task-scoped subagents (direction B). The four durable accountabilities from the user stories — Alfred, Meta Strategy, Meta Ops, Meta Detective — are kept as **durable role definitions** (subagent definitions with scoped tools and precise descriptions, invoked per-run), not as always-on named agents holding independent state.

**Evidence:**
- The reference KB's persistent-agent rung is explicitly deferred/underspecified (U001: "do not invent final agent list without operator confirmation") and its escalation criteria for persistent agents were never answered — EM §1 D1, thin-dimension flag.
- US §7.3 requires routing to the four accountabilities "**without creating unnecessary durable agents**"; US domain workers are defined as "temporary, context-isolated workers" — exactly the ephemeral subagent model.
- BPR decision 5: subagents strictly ephemeral/tool-scoped; "named persistent agent" reserved for genuine durable identity/memory/ownership.
- Resilience evidence (EM D2): who-holds-the-plan determines resilience; a workflow backbone with script/file-held state is the resilient rung, and the three-package system already holds state in files (EM D2, right column).

**Where the operator hypothesis stands:** "multi-agent with plan/sync/session under a meta-ops-style agent" is confirmed as an *accountability structure* (see Q2) but corrected as a *runtime mechanism*: Meta Ops is a workflow-and-role surface, not a persistent stateful agent. If a genuine persistent-identity need emerges (e.g., cross-session Detective memory), that's an escalation decided then — pending the external research prompt on persistent-agent criteria (`prompts/`).

---

## Q2. System relation → **B: layer them** (operator hypothesis confirmed)

**Answer:** The three-package system supplies the state-mutation backbone; the four accountabilities sit on top as the who-proposes/who-validates layer; the old Apex KB is mined for translated patterns, not revived.

**Evidence:**
- US §3 already encodes this exactly: `apex_plan`/`apex_sync`/`apex_session` are listed as **`meta_ops_support_capabilities`** — components under Meta Ops accountability, not peer systems. US §7.9 restates it as a required capability.
- BPR decision 1 (top decision): plan-sync-session's proposal → deterministic-compute → gated-mutation split is the canonical boundary; the role control plane folds in on top, "not a competing boundary."
- EM verdict: the systems are complementary opposites — v2 wins on theory (D3, D4), three-package wins on mechanism (D1, D2, D5, D6). Layering keeps each system's winning half.

---

## Q3. Skill granularity → **B: Anthropic's rule** (already the de facto standard)

**Answer:** Keep `SKILL.md` to "decide whether + how to start"; push detail into referenced files; split when unwieldy or covering mutually-exclusive contexts. No mechanical line cap (C rejected: a hard cap is exactly the defensive-process layer decision D2 eliminates; A rejected: the repo already outgrew "notice problems later").

**Evidence:** The live skills already implement B and it demonstrably works: compact ~8–11 KB SKILL.md contracts, `references/` behind explicit `read_when` tables, templates on demand, size-tier variants (EM D5 right column). BPR decision 4 says adopt it since none of the three KBs address granularity at all (BPR §2 row "Progressive disclosure": not addressed × 3).

---

## Q4. Subagent spawning/scoping → **B: named definition only for repeated worker types; one-off calls otherwise; narrow tool allowlists always**

**Answer:** Define a named subagent only when the same worker type recurs with the same instructions (the four accountabilities qualify immediately; specialist lanes — Knowledge Bank, Informatics Design, Prompts & Workflows — qualify as they recur across stories). Everything else is a one-off task-scoped call. Every subagent gets an explicit narrow tool allowlist and a precise description.

**Evidence:**
- Reference KB decision criteria (EM §1 D1): subagent when output is verbose / tool restrictions must be enforced / work is self-contained returning a short summary; skill when reusability without isolation; main conversation when phases share context.
- US domain-worker rule: workers "receive only the source slice, acceptance criteria, allowed tools, and stop condition needed for that deliverable" — that IS the scoping contract, verbatim.
- Q8's translation (below) maps the 9-agent roster onto this: 4 accountabilities + 3 specialist lanes as named definitions, the rest one-off workers.

---

## Q5. Shared state/handoff schema → **B: one shared handoff schema, built from v2's most complete version**

**Answer:** One schema reused by every packet type (`apex_plan_packet`, apex-sync reports, H6 artifacts, worker returns), replacing per-packet invented shapes. Proposed field union (to be locked at milestone 5, not here):
`role/accountability · lifecycle_stage (proposal | computed | confirmed) · status · target_surface · next_state · prerequisites · expected_action · sources/evidence · uncertainties · unresolved_risk · stop_condition · operator_validation`.

**Evidence:**
- v2's handoff law is the most complete in scope: role + state + target surface + next state + prerequisites + expected action + unresolved risk; "handoff continuity may not depend on hidden reasoning alone"; "silent continuation from an unclear handoff is invalid" (EM D2 left column, canon L349–376).
- BPR decision 6 recommends exactly this generalization; BPR §2 flags apex-session's H6 schema as less specified than v2's — so the union fills a real gap, not a stylistic one.
- US §7.4 requires artifact contracts with "sources, assumptions, uncertainties, changed claims, evidence, and stop conditions" — the added fields map 1:1.

---

## Q6. Operator-gate placement → **B: one reusable gate primitive, taken verbatim from apex-session's implemented mechanism**

**Answer:** A single gate primitive — required `operator_validation` field (values `confirmed | rejected | needs_revision | not_requested`) plus, for phase transitions, a required literal confirmation phrase — reused by every workflow that mutates durable state. Risk-weighted application per US §2's milestone rule (full loop only for consequential outputs), which answers decision D2's anti-ceremony concern: one primitive, applied where consequence lives, not everywhere.

**Evidence:**
- apex-session's gate is the **only concrete implemented mechanism** among all systems in scope (EM D6): field values, gate statuses, `requested_operator_action` enum, `no_implicit_apply: true`, 3-step confirm chain. v2's VERIFY/LOCK gates are prose; the reference KB has essentially nothing in-run (EM §1 D6).
- BPR decision 7: consolidate to plan-sync-session's mechanism "since it's the only one with an actual mechanism rather than a described concept."
- C (autonomous-mode toggle) is rejected on direct evidence: US §6 governance checks require "operator_gates_are_consequential_not_constant" and stronger control for public/safety/compliance/mutation — a global toggle can't express that.

---

## Q7. Drift control → **B: one project-level glossary file** (plus nothing else)

**Answer:** A single glossary file pinning canonical meaning for already-drifted terms — minimally: *role* vs. *state* (unit of permission), *agent* (ephemeral subagent vs. persistent identity vs. accountability), *candidate* vs. *canon/accepted*, *packet* (and the Q5 schema as its one shape), *workflow* vs. *skill*, *validation* vs. *approval* (v2: "validation ≠ approval"). Location proposal: `apex-meta/GLOSSARY.md`, referenced from `ORCHESTRATION-SYSTEMS-INDEX.md`.

**Evidence:** ORCHESTRATION-SYSTEMS-INDEX §5.3 already names the drifted terms and notes no glossary exists. A (operator notices) already failed once — the "Phase 1 only" stale index row this session corrected is literally review-based drift control not working. C (periodic drift-detection skill) is the defensive-process layer D2 eliminates, and blast radius here is officially small — the cheapest sufficient mechanism wins on the reference KB's own ladder rule.

---

## Q8. Fate of the 9-agent roster + BUILD/VERIFY/LOCK → **B: translate, don't revive** (with a concrete translation map)

**Answer:** No literal roster revival, no literal state machine. The translation, concretely:

| v2 element | Fate in the unified system | Grounds |
|---|---|---|
| 9-agent roster | **4 durable accountabilities** (Alfred, Meta Strategy, Meta Ops, Meta Detective) + **3 specialist lanes** (Knowledge Bank, Informatics Design, Prompts & Workflows) + ephemeral domain workers — the mapping the user stories already use | US §3; BPR decision 3 (cap permanent roles, push the rest to skills/subagents) |
| BUILD/VERIFY/LOCK state machine | **Not implemented as a state machine.** Its invariant survives translated: the three-package boundary + Q6 gate primitive already provide proposal ≠ computed ≠ confirmed separation; BPR decision 2's default ("don't add a new state machine unless a concrete failure is observed that the package boundary doesn't prevent") is adopted | EM D4 both columns; BPR §3.2 |
| Role-vs-state permission invariant | **Kept as design law** for any new mutation surface: "no role label may be used as compliance theater for permissions the current state does not grant" — enforced through the Q6 state-field gate, not through role identity | EM D4 left column (canon L240–251, RS01–RS04) |
| meta_detective adversarial validation | **Translated into a mandatory workflow step** for consequential outputs: independent validity review, separated from strategic-alignment review, reviewer cannot implement fixes, criterion-level verdicts with named defect owners | EM D3 (the three-package system's one genuine hole); US milestone loop + §7.6–7.7; reference KB C003 (adversarial review is a workflow-rung capability) |
| Handoff record law | **Becomes the Q5 shared schema** | EM D2; BPR decision 6 |
| Candidate-vs-canon separation / LEARNING_QUEUE | **Kept as rule**: candidate learning never auto-promotes; US §7.15 restates it | DN §1; US §6 candidate-only learning row |
| ESSENCE.md compaction / index-first retrieval | Already realized as compact SKILL.md + `read_when` references — no new mechanism needed | EM D5 both columns |
| The v2 KB itself | Historical evidence, kept intact (its own wiki self-flags "translate, not runtime spec", U-RS01/U-RS02); v1 KB stays per the standing do-not-delete resolution | DN §1–2; ORCHESTRATION-SYSTEMS-INDEX §1 |

C (discard entirely) is rejected on the evaluation evidence: v2 holds the two strongest ideas in scope (D3, D4) and both are missing from the live system.

---

## Consistency check (Q1/Q4/Q8 coupling)

The three coupled questions resolve to one coherent picture: durable **accountabilities** as named, tool-scoped, ephemeral-invocation subagent definitions (Q1-B, Q4-B), the roster translated rather than revived (Q8-B), the three-package system as the mutation backbone under Meta Ops (Q2-B), one handoff schema (Q5-B) carrying one gate primitive (Q6-B), with drift pinned by a glossary (Q7-B). No answer contradicts another; all match decision D1 (this produces the final system — nothing above is deferred as a v1 excuse) and D2 (no defensive process layers added — the only added control surfaces are the Detective review step and the gate primitive, both target-focused and already operator-mandated by the user stories).

## External-research dependencies (do not block the gate, sharpen it)

See `prompts/external-research-pack-20260711.md` (v2). Only two questions get a real deep-research run, because only two can actually flip a decision: **P1 role-vs-state permission** (could move Q8 from "no state machine" to "minimal state field" if it produces a concrete failure the role-boundary + write-gate can't prevent) and **P2 adversarial-review wiring** (could move Q8's Detective translation from "one subagent" to "different-model / N-of-M judge" if same-family LLM review proves unreliable — this is the one component we build from scratch). Both are framed adversarially, to break the B-answer rather than confirm it, with an explicit decision-change bar. The former v1 prompts on operator-gate patterns and persistent-agent escalation were confirmatory (they could not overturn Q6/Q1, which already rest on the only implemented mechanism in scope and on a deferred question) — folded into one optional P3, safe to skip. P4 is a lean Perplexity verification of the evaluation matrix's own citations, not research.

## Operator gate

- [ ] Operator verifies milestones 1–3 artifacts (`discovery-notes.md`, `evaluation-matrix.md`).
- [ ] Operator confirms or amends each Q1–Q8 answer above.
- [ ] Only then: milestone 5 (target-architecture draft) begins.
