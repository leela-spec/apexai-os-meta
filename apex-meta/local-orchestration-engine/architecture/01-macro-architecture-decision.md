---
title: "Flow Execution Engine — Macro Architecture Decision"
purpose: >
  Locked macro topology for the local-LLM execution layer: what combines, what each
  AI tier is for, where the engine attaches to Weekly Orchestrator and Multi-Agent
  Orchestration, and the trust boundary that governs every downstream choice.
created: 2026-07-28
status: "proposal — candidate; not operator-confirmed, no runtime built"
decided_against:
  - .claude/skills/weekly-orchestrator/SKILL.md (live contract)
  - .claude/skills/weekly-orchestrator/references/handoff-schema.md
  - apex-meta/kb/Weekly-Orchestrator/architecture/01-macro-architecture-decision.md (locked)
  - apex-meta/kb/Weekly-Orchestrator/architecture/03-execution-trace-verification.md (locked trace)
  - apex-meta/orchestration/ARCHITECTURE.md (live Multi-Agent architecture)
  - apex-meta/orchestration/GLOSSARY.md (terminology authority)
  - .claude/skills/PrecapNextDay/references/flow-prompt-pack-contract.md
  - .claude/skills/AIRouting/SKILL.md
  - .claude/skills/raw-flow-dump-normalize/references/raw-flow-dump-contract.md
---

# Flow Execution Engine — Macro Architecture Decision

## Naming (D-M0)

Decision: this system is the **Flow Execution Engine (FEE)**. It is **not** an orchestrator
and must not be called one.

`apex-meta/orchestration/GLOSSARY.md` pins **orchestration run** to "one explicitly started,
bounded execution of a named orchestration system." APEX OS has exactly two orchestration
systems. FEE adds a third *execution substrate*, not a third orchestration system — the Weekly
Orchestrator remains the orchestrator; FEE is the machinery that performs one of its stages.
Calling it "local orchestration engine" would manufacture precisely the term-drift the glossary
exists to prevent.

`local-orchestration-engine/` (this folder) is therefore a **former working name, not the live
system name** — handled exactly as `apex-meta/fable-orchestrator/` was for Multi-Agent
Orchestration. Folder rename is optional and deferred; churn is not worth it.

---

## The strategic core (D-M1)

Decision: **the three AI tiers are allocated by scarcity/capability asymmetry, not by
preference.** This is the single decision every other one derives from.

| Tier | Cost shape | Reasoning | Structure | Latency | Reliability | Risk |
|---|---|---|---|---|---|---|
| Browser subscription chat | flat-rate, effectively unbounded | highest | none guaranteed | slow (UI-speed) | fragile | ToS/ban |
| Claude Code CLI | metered, genuinely scarce | high | excellent (typed tools) | fast | high | none |
| Local LLM | electricity only, unbounded | **low** | good if constrained | fast | high | none |

The allocation rule that follows:

```yaml
allocation_rule:
  scarce_and_smart_claude_code: design, verification, gates, doctrine, anything consequential
  unbounded_and_smart_browser:  reasoning VOLUME — research, drafting, analysis, critique
  unbounded_and_dumb_local:     mechanical VOLUME — sequencing, dispatch, capture, classification
  never_local:                  any judgement whose wrongness is expensive or hard to detect
```

**Why this ranks first among alternatives:**

- **A. (chosen) Scarcity-asymmetry allocation.** Each tier does only what it is uniquely best
  at; the scarce resource is never spent on work an unbounded resource can do. Directly extends
  `AIRouting`'s existing `cost_policy: subscription_frontier_models_mean_cost_is_not_primary_constraint`
  and its already-written prohibition: *"Do not use API frontier models as the default daily
  workflow engine"* (`PrecapNextDay/SKILL.md` boundaries). The repo already decided this;
  FEE implements it.
- **B. Local-LLM-first ("run everything locally, escalate on failure").** Rejected: a low-reasoning
  model producing *plausible-but-wrong* analysis is the expensive failure mode, because detecting
  it costs a reasoning-tier review pass — so the "saving" is negative. The repo names this class
  of failure explicitly (`ARCHITECTURE.md` §4 "plausible-but-wrong artifacts").
- **C. Claude-Code-first (spawn subagents for flow work).** Rejected: burns the one genuinely
  scarce resource on the highest-volume work. This is the status-quo cost problem FEE exists to fix.
- **D. API-first (OpenRouter/metered API for flow work).** Rejected twice over: `AIRouting` forbids
  finalizing an OpenRouter map (`final_model_map_drift` failure mode) and `PrecapNextDay` forbids
  API frontier models as the daily engine. Metered API converts a solved flat-rate cost into an
  unbounded variable cost.

---

## What actually combines (D-M2)

Decision: **four systems, three of which already exist and must not be modified.**

```
┌─ APEX OS ─────────────────────────────────────────────────────────────────┐
│                                                                           │
│  Weekly Orchestrator  ◄── FEE attaches HERE, at step 4 only               │
│  (Claude Code native, G1–G5, files-as-state)                              │
│      1 locate → 2 precap-week(G1) → 3 precap-next-day(G2)                 │
│           → 4 EXECUTION(G3) ◄══════════════╗                              │
│           → 5 normalize → 6 recap(G4) → 7 merge(G5) → 8 review            │
│           → 9 durable write → 10 overview → 11 next cycle                 │
│                                             ║                             │
│  Multi-Agent Orchestration                  ║  handoff packet only,       │
│  (operator-triggered, Alfred/MetaOps/…)  ◄──╫─ never auto-activation      │
│                                             ║                             │
│  Plan-Sync-Session Backbone                 ║  read-only from FEE         │
│  (apex-plan / apex-sync / apex-session)  ◄──╝                             │
└───────────────────────────────────────────────────────────────────────────┘
                                              ║
┌─ FEE (new, local, non-Claude-Code) ──────────╨────────────────────────────┐
│  deterministic driver  +  local LLM adjudicator  +  browser adapters      │
│                        +  executor bridge (Odysseus AI / Hermes / OpenClaw)│
└───────────────────────────────────────────────────────────────────────────┘
```

Step 4 of the locked trace is *already* the seam, verbatim:
`actor: operator (human) · reads: flow packet + prompt packs · writes: raw notes / skip signal ·
gate: G3`. FEE replaces the **actor** at that one step. Nothing upstream or downstream changes.

---

## The engine consumes an existing contract; it does not invent one (D-M3)

Decision: **`flow_prompt_pack` IS the execution work order. FEE defines no new workflow
language.**

This is the highest-leverage finding of this design pass. `PrecapNextDay` already emits, per flow,
a machine-readable pack containing everything a browser executor needs:

```yaml
already_present_in_flow_prompt_pack:
  sprint_prompt_sequences:            # ordered S1/S2/S3, with sprint_role and sprint_status
    start_prompt_ref:
      provider_target: ChatGPT | Claude | Gemini | OpenRouter_later | provider_unspecified
      final_copy_paste_prompt_ref: <path>     # "copy-paste-ready" per prompt_placement_rules
      prompt_task_type: <taxonomy value>
    follow_up_prompt_refs: [0..6]     # bounded_follow_up_count
  routing_usage_summary:
    primary_surface_class: subscription_frontier_chat | subscription_frontier_reasoning |
                           deep_research_surface | agent_run_surface | code_agent_surface |
                           long_context_surface | supplemental_api_low_cost | provider_unspecified
  light_capture_hints:
    suggested_operator_notes: [...]   # what to save, what to flag
  FlowRecap_preparation:
    raw_flow_dump_connection: use_flow_packet_raw_flow_dump_template | ...
```

A per-sprint ordered prompt list, each with a named provider, a copy-paste-ready body, bounded
follow-ups, and explicit capture instructions **is a browser automation script in declarative
form**. It was authored for a human executor; a machine executor reads it identically.

**Alternatives ranked:**

- **A. (chosen) Consume `flow_prompt_pack` as-is.** Zero new schema, zero drift, upstream
  `PromptEngineer`/`AIRouting`/`Workflow&Processes` keep full ownership of their domains, and the
  engine inherits the existing degraded-mode semantics (`generation_mode: degraded_generic_prompt_mode`,
  `pack_status: low_confidence_auto_generated`) for free. `prompt_packets_are_referenced_not_redefined`
  is honoured by construction.
- **B. New declarative workflow DSL (YAML step definitions).** Rejected: duplicates a contract
  that already exists and is already validated, creating a second source of truth for prompt
  sequencing — the exact "per-skill invented packet shapes" the GLOSSARY names as the thing
  `packet` disambiguates.
- **C. Code-defined DAG via LangGraph/Prefect/Temporal.** Rejected: heavy dependency for a graph
  that is already fully described by data, and it would hide the plan inside code where the repo's
  invariant #1 ("state lives in files") requires it on disk.
- **D. Let the local LLM improvise the sequence from the flow packet.** Rejected outright — see D-M5;
  it hands sequencing authority to the least reliable component and opens the injection surface.

Consequence: `flow_prompt_pack` gains **one** new consumer. FEE needs exactly one additive change
to upstream contracts, specified in `02-meso-module-design.md` (D-S3): a new surface class for the
local model. Nothing else upstream moves.

---

## Deterministic-first, LLM-at-the-edges (D-M4)

Decision: **the control plane is a deterministic state machine. The local LLM is called only for
narrow, typed adjudications it cannot escape.**

The repo's own mechanism ladder governs this: *"escalate only when the lower rung demonstrably
cannot carry the work"* (`Weekly-Orchestrator/architecture/01`, claim C001), and its deterministic
precedent is `scripts/apex_sync.py` — "stdlib-only, dry-run-first."

Work split, measured against what actually requires inference:

```yaml
rung_1_deterministic_python:        # ~80% of step-4 decisions
  - read + freeze the execution plan from flow_prompt_pack
  - select provider adapter from provider_target / primary_surface_class
  - sequence sprints and prompts in declared order
  - enforce pacing, quota, retry counts, timeouts
  - append to the run ledger; write evidence files
  - emit the evidence bundle
rung_2_local_llm_typed_adjudication:   # ~15%, each call returns a closed enum + fields
  - turn_complete | truncated | refused | rate_limited | off_topic | error
  - follow_up_needed: bool  (only ever selecting from the pack's declared follow-ups)
  - operator_summary narrative (prose, clearly labelled as engine-generated)
  - evidence_source classification into the raw-flow-dump enum
rung_3_reasoning_tier:                 # ~5% of decisions, 100% of the CONTENT
  - browser subscription chats: the actual research/analysis/drafting
  - Claude Code: prompt design (upstream), review (downstream), gates (operator)
```

**Alternatives ranked:**

- **A. (chosen) Deterministic driver + typed local-LLM adjudication.** Highest resilience per unit
  of complexity: every failure is attributable to a named rung, the plan is inspectable before any
  browser opens, and a killed process resumes from the ledger. Matches repo doctrine exactly.
- **B. Local LLM as an agent loop (ReAct-style, tools exposed, model decides next action).**
  Rejected: this is the industry-default shape and the wrong one here. It (i) gives a low-reasoning
  model unbounded action selection, (ii) makes every run non-reproducible, (iii) converts browser
  output into action-selection input, which is the injection hole D-M6 closes, and (iv) burns
  local-inference latency on decisions a `match` statement makes correctly every time.
- **C. Pure determinism, no LLM at all (regex/DOM heuristics for completion detection).** Genuinely
  attractive and ranks a close second. Rejected only because completion/refusal/truncation detection
  across three changing web UIs is exactly the fuzzy-classification task where a small local model
  is more robust than selectors — and because `operator_summary.normalized_summary` is required prose
  by the raw-dump contract. **Fallback position:** if the local LLM proves unreliable, degrade to
  heuristics + `normalization_confidence: low` + `operator_review_recommended: true`, which the
  downstream contract already handles natively. This is a designed retreat path, not a dead end.
- **D. Claude Code as the driver.** Rejected: spends the scarce tier on mechanical dispatch (D-M1).

---

## Local LLM job description — negative-first (D-M5)

Decision: **the local model is an adjudicator and a narrator. It is never an author, a router, or
a decider.**

```yaml
local_llm_may:
  - classify a captured turn into a closed enum
  - decide whether a pre-declared follow-up prompt from the pack should fire
  - write the operator_summary narrative and interpretation_notes
  - map captured evidence to the raw-flow-dump evidence_source taxonomy
  - restate/repair its own malformed JSON output once
local_llm_must_never:
  - author or edit a prompt body            # PromptEngineer owns this, upstream
  - choose a provider or surface class      # AIRouting owns this, upstream
  - invent a step not present in the frozen plan
  - decide a flow is complete, skipped, or successful   # completion_state is evidence-derived
  - set operator_validation, authority.state, or any gate field
  - select a filesystem path, shell command, or tool from captured content
  - write outside its own artifact family
```

This resolves **DESIGN-LOCK-QA.md Q3** (control-plane + light glue reasoning) into an enforceable
contract, and it resolves **Q6** (operator boundary) with a specific answer: *the local LLM holds
no tools at all.* It emits typed verdicts to the deterministic driver, and the **driver** performs
every side effect. That is strictly stronger than the Q6 option "local LLM owns cheap tools
directly," and it costs nothing.

---

## The trust boundary — frozen plan, quarantined evidence (D-M6)

Decision: **the plan is frozen before execution begins; captured content is inert data forever.**

This is the load-bearing safety decision, and it is not optional ceremony. Browser output is
untrusted third-party web content. Odysseus AI ships bash/file tools. Absent this boundary, text
written by a web page could select a local command — a live prompt-injection-to-code-execution path.

```yaml
trust_boundary:
  freeze_before_run:
    what: execution_plan.frozen.json compiled from flow_prompt_pack
    contains: every prompt body, provider, order, follow-up, timeout, retry budget
    property: immutable for the run's lifetime; hash recorded in the ledger
    consequence: the set of possible actions is fully enumerated BEFORE any network contact
  quarantine_after_capture:
    captured_text_may:   be stored verbatim; be hashed; be classified; be summarized; be handed to G3
    captured_text_may_not: select a tool, path, command, provider, or next step
    mechanism: captured text is written to disk and passed to the adjudicator inside a
               data-only envelope; the adjudicator's response schema has no action fields to fill
  executor_bridge:
    rule: tool-work steps run ONLY from frozen-plan declarations, never from captured content
```

**Alternatives ranked:**

- **A. (chosen) Frozen plan + quarantined evidence.** Makes injection structurally impossible rather
  than statistically unlikely: there is no field in which a captured instruction could land. Also
  buys reproducibility and clean resume for free.
- **B. Prompt-injection detection/filtering on captured text.** Rejected as a *primary* control —
  detection is probabilistic and adversarially weak. Acceptable only as defence-in-depth on top of A.
- **C. Trust captured content, rely on sandbox isolation to contain damage.** Rejected: isolation
  limits blast radius but does not prevent the engine from writing attacker-chosen content into the
  evidence bundle that feeds — through normalize → recap → merge → session — toward canon project
  state. Containment is not integrity.

---

## Where the human stays (D-M7)

Decision: **G3 remains a real human gate. FEE changes who *performs* step 4, never who *approves* it.**

`handoff-schema.md` sets `G3: {stage: operator_execution, packet: raw_flow_dump_or_skip_marker,
required: always}`. Required always. Automating the actor while silently inheriting the approval
would violate the live contract and remove the only human checkpoint between untrusted web content
and the canon write path.

What changes for the operator: G3 stops being "do the work, then write notes" and becomes "review
what the engine produced." That is a large real gain in leverage without any loss of control — and
it is the correct place for the human, because it is the first point where a wrong result is cheap
to catch and expensive to miss.

Autonomous runs are already covered by the existing contract and need no new mechanism:
`operator_absent_in_autonomous_run` → produce packets with `operator_validation: not_requested`,
batch-present gates at run end, never fabricate confirmation, never apply canon writes.

---

## Relationship to Multi-Agent Orchestration (D-M8)

Decision: **FEE never activates Multi-Agent Orchestration. It can only produce a handoff packet the
operator may choose to route.**

Repo law is explicit and unambiguous (`orchestration/00-START-HERE.md`, `ARCHITECTURE.md` §Scope,
GLOSSARY **cross-system transfer**): no automatic cross-activation; transfer requires explicit
operator instruction, an explicit handoff packet, or a confirmed durable-artifact reference; the
receiving system still requires its own activation condition.

So the bridge is one-directional and inert:

```yaml
escalation_path:
  trigger: a flow's output meets the GLOSSARY definition of consequential
           (durable mutation, public output, spend, safety-relevant instruction, doctrine change)
  fee_action: emit a handoff packet with authority.state = candidate, and STOP
  fee_must_not: invoke Alfred, Meta Ops, or any .claude/agents/ definition
  operator_action: may route that packet into a Multi-Agent Orchestration run — or not
```

### Second integration point, deliberately ranked lower

Multi-Agent Orchestration spawns **bounded domain workers**, each a Claude Code subagent consuming
the scarce tier. FEE could serve those workers over browser subscriptions instead — a real cost
unlock (a 20-worker research fan-out is the exact shape that hurts).

**Ranked: defer.** Reason: `ARCHITECTURE.md` §7.3 makes per-story adoption evidence-gated
(`simulations/` record required before a workflow counts as adopted), and Multi-Agent Orchestration
is operator-triggered and rarer than the daily weekly loop. Build and prove the step-4 seam first;
this reuses the same modules later with no rework, because the Surface Broker (M2) is already
provider-agnostic. Cheap to add, expensive to debug in parallel with the primary integration.

### A previously-closed decision this design reopens

`ARCHITECTURE.md` §4 records a real limitation with an explicit escalation path:

> both lenses are Claude-family … Escalation path if simulations show plausible-but-wrong artifacts
> passing: different-family judge — an operator trust-boundary decision, currently out of scope
> (no external calls, operator direction 2026-07-11).

FEE's browser adapters would make a **different-family judge** (Gemini or ChatGPT via browser) newly
cheap — it would close the recorded limitation using flat-rate subscriptions rather than metered API.

**Ranked: flag, do not build.** It requires the operator to revisit the 2026-07-11 "no external
calls" direction, and the review path is the most safety-critical surface in APEX OS — the last
place to introduce a fragile, ToS-risky, injection-exposed component. Recorded here as a genuine
opportunity with a named precondition (operator re-authorization + a simulation showing the
Claude-family limitation actually biting), not as a build item.

---

## Worker platform selection (D-M9)

Decision: **provisional — Odysseus AI as the executor for tool-work steps, NOT as the orchestration
engine. Confirmation is gated on the DESIGN-LOCK-QA.md Q1 research pass.**

Assessed against what FEE actually needs:

| Candidate | What it offers | Fit |
|---|---|---|
| **Odysseus AI** (odysseusai.dev, AGPL-3.0) | self-hosted agent workspace; bash/file/web/memory tools; deep-research multi-step synthesis; pluggable local backends (Ollama, vLLM, llama.cpp, OpenRouter); ChromaDB memory; Docker Compose | **Strong as executor.** Docker Compose is a ready-made answer to the D-M?/Q9 sandbox question; pluggable local backends match D-M5; bash/file tools cover tool-work steps. **Weak as orchestrator** — its agent loop is exactly shape B rejected in D-M4. |
| **Hermes** (Nous Research) | messaging integrations (Slack/Telegram/WhatsApp/Signal/Matrix/SMS/webhooks), kanban, memory providers, MCP, hooks, sessions, TUI | **Fit is observability/notification (Q14), not execution.** Its strength is operator reach — the "tell me when something needs me" channel D-M?/Q14 needs. Do not adopt it as the execution core. |
| **OpenClaw** (operator's own, `MasterOfArts/OpenClaw/07_finalopenclawsystem/`) | large existing system + doc corpus, already in the operator's KB | **Unknown maturity — must be inventoried before any dependency.** Highest strategic value if it is a working system (no new dependency, operator owns it); zero value if it is a design corpus. This is the single most important unknown in Q1. |

**Ranked recommendation:** adopt **Odysseus AI as executor**, **Hermes as notification channel
only**, and **inventory OpenClaw before deciding whether it replaces either.** Explicitly reject
"adopt Odysseus AI as the orchestration engine" — its autonomous agent loop is the D-M4 alternative-B
shape, and handing it the driver role would forfeit the frozen-plan boundary (D-M6) that makes the
whole design safe.

---

## Rejected macro alternatives (with reasons)

| Rejected | Why |
|---|---|
| FEE replaces the whole Weekly Orchestrator runtime | Seven of eight stages are locked and dry-run-verified with passing behavioral tests (T1–T4). Only step 4 has a human actor to replace. No evidence motivates touching the rest. |
| FEE as a third APEX OS orchestration system | GLOSSARY pins "orchestration system" to two; FEE is a substrate for one stage of one of them. Adding a third would require peer status in `ORCHESTRATION-SYSTEMS-INDEX.md` it has not earned. |
| Local LLM holds tools directly | D-M5/D-M6: strictly weaker than a toolless adjudicator, for no benefit. |
| New workflow DSL / state schema | D-M3: `flow_prompt_pack` + `handoff_envelope` already cover it; a new shape is drift. |
| Metered API (OpenRouter) for flow reasoning | Forbidden by two live contracts (`AIRouting` `final_model_map_drift`; `PrecapNextDay` "no API frontier models as the default daily workflow engine"). |
| Automating away G3 | `handoff-schema.md` `required: always`; removes the only human checkpoint before the canon path. |
| FEE calling `apex-session` or writing `state/` | `Weekly-Orchestrator/architecture/01` D-M4: single write path, main thread only, post-G5. FEE writes only its own artifact family. |
| Uniform browser-automation treatment across providers | DESIGN-LOCK-QA.md Q4: Claude has an officially sanctioned automation channel; ChatGPT/Gemini do not. One risk bucket would either over-engineer Claude or under-protect the others. |

---

## Open macro dependencies

1. **Q1 research pass** (Odysseus AI internals, Hermes fit, OpenClaw inventory) gates D-M9
   confirmation. Everything else in this file stands independent of it.
2. **Operator confirmation of this file** — it is `authority.state: candidate` per repo law and
   must not be treated as decided.
3. **One additive upstream change** (a local-model surface class in `AIRouting`) is specified in
   `02-meso-module-design.md` D-S3 and requires its own operator gate before any contract edit.
