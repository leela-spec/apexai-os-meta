---
doc_type: design-lock-qa
initiative: local-orchestration-engine
created: 2026-07-28
authority: operator-session-2026-07-28
mode: living-document — resolve one round at a time, do not force all-at-once decisions
scope: >
  A laptop-local, non-reasoning orchestrator (small/mid local LLM) that sequences a workflow of
  prompts and tool calls, delegating actual reasoning to browser-driven AI subscription sessions
  and to worker codebases (candidates: Hermes, Odysseus, OpenClaw) running in a sandbox on this
  machine. Out of scope for now: whether this becomes a third APEX OS orchestration system (Q5).
---

# Local Orchestration Engine — Design Lock Q&A

Same format as `apex-meta/handoff/agent-skill-system-research/design-lock-qa.md`: each question
carries a starting hypothesis where one exists, candidate directions, what needs to be checked,
and the blast radius of the choice. Resolved questions record the actual decision plus its
follow-on obligations. Open questions are for the next round, not to be assumed shut.

---

## Resolved — 2026-07-28 session

### Q1. What are Hermes, Odysseus, and OpenClaw, concretely?
**Resolution: not yet decided — this is itself a research task, not a design question to
answer from the armchair.**

**What's actually known so far:** This KB's `MasterOfArts/OpenClaw/.../docs/hermes-docs/` is a
cached copy of docs from `hermes-agent.nousresearch.com` — i.e. "Hermes" most likely refers to
**Nous Research's Hermes agent framework** (messaging integrations: Slack/Telegram/WhatsApp/
Signal/Matrix/Mattermost/SMS/webhooks, plus kanban, memory providers, MCP, hooks, sessions, TUI).
"Odysseus" has no hits anywhere in the currently cloned repos — either it hasn't been imported
into this KB yet, it's known to the operator from outside this machine, or the name is
provisional. "OpenClaw" is the operator's own existing system, already substantial
(`MasterOfArts/OpenClaw/07_finalopenclawsystem/`).

**Update — 2026-07-28, later in session:** "Odysseus" confirmed as **odysseusai.dev / Odysseus
AI** — an open-source (AGPL-3.0), self-hosted AI agent workspace (built by PewDiePie) combining
chat with autonomous agents that have bash/file/web/memory tool access, a "deep research"
multi-step search-and-synthesis workflow feature, email/calendar/task integrations, ChromaDB
vector memory, and — notably — **pluggable local-model backends already built in** (Ollama,
vLLM, llama.cpp, OpenRouter), deployed via Docker Compose, local-first/privacy-first by design.

**This changes the shape of the question.** Odysseus AI isn't obviously just a "worker/executor"
alongside Hermes and OpenClaw — it may already **be** most of what Q3–Q10 are trying to design
from scratch: a local-LLM-backed agent orchestration engine with tool handling, memory, and
web access out of the box. The open question is no longer just "what is Odysseus" but
**"does adopting Odysseus AI as the base platform obsolete several of the open questions below
(Q7 model selection, Q9 sandbox model, Q10 workflow representation), or does it only supply the
worker layer while a separate local-LLM control-plane still sits on top of it?"**

**Required next action:** a scoped research pass (could be delegated to a Claude Code agent)
that (a) evaluates Odysseus AI's actual agent/orchestration internals against this document's
requirements (not just its marketing description above), (b) confirms what
`hermes-agent.nousresearch.com` actually is and whether it complements or duplicates Odysseus AI,
(c) inventories what already exists under `OpenClaw/07_finalopenclawsystem/` well enough to know
whether it's a working system, a design-doc corpus, or both, and how it would relate to Odysseus
AI if both are adopted.

**Blast radius:** Nothing else in this document can be locked with confidence until this
resolves — Q6 (operator boundary), Q7 (model selection), Q9 (sandbox model), Q10 (workflow
representation), and Q11 (handoff protocol) all depend on knowing whether Odysseus AI is the
platform or just one component.

---

### Q2. What does "browser chat subscription windows do the heavy reasoning" mean mechanically?
**Resolution: literal browser-UI automation.** A browser-automation layer drives the actual
web chat interfaces (claude.ai, chatgpt.com, gemini.google.com, etc.) as if a human were typing,
using the operator's existing paid subscriptions instead of metered API keys — to keep the
expensive multi-step reasoning inside flat-rate subscription cost.

**Blast radius:** Locks in Q4 (ToS/ban risk acceptance) and Q8 (automation tooling/provider
scope) as the concrete engineering consequences of this choice.

---

### Q3. What is the local LLM's job scope?
**Resolution: control-plane + light glue reasoning.** The local model is not a content
generator for the actual research/analysis deliverables — that stays delegated to the
subscription-chat reasoning backend. But it isn't purely mechanical routing either: it's allowed
to do small in-between reasoning the operator role itself needs (e.g. deciding what the next
step is, lightly summarizing a tool result before deciding, validating/repairing a malformed
handoff packet) without spending a subscription-chat round trip on every micro-decision.

**Blast radius:** Directly shapes Q7 (model selection — prioritize reliable instruction-following
and structured tool-calling over raw parameter count) and Q6 (operator boundary).

---

### Q4. ToS / account-suspension risk from automating subscription chat UIs
**Resolution: accept the risk, and engineer around detection** (human-like pacing, avoid
parallel hammering of the same account, build graceful degradation for logout/flag events —
not just "proceed and hope").

**Important asymmetry surfaced during this session, worth designing around rather than
flattening into one risk level:** Anthropic ships its own **officially sanctioned** browser
automation of claude.ai (the "Claude in Chrome" extension/tool family) — driving Claude's web
chat through that channel is a materially different risk profile than writing an unsanctioned
Playwright/Selenium script against chatgpt.com or gemini.google.com, which have no equivalent
official automation path. Treat "automate Claude" and "automate ChatGPT/Gemini/other" as two
different risk buckets, not one uniform "subscription-chat automation" bucket — the pacing/
detection-avoidance engineering effort should be concentrated on the providers that lack an
official channel.

**Blast radius:** Feeds directly into Q8 (automation tooling and provider scope) — the tooling
answer should probably differ per provider rather than being one universal scraper.

---

### Q5. Is this a third APEX OS orchestration system, or a separate standalone project?
**Resolution — 2026-07-28, via Q15: this specifically targets the existing Weekly Orchestrator,
not a new peer system and not a fully independent project.** The operator's answer to Q15
("the weekly orchestration should be handled by that llm agent flow") means this initiative is
meant to become (or become part of) the execution mechanism for the **already-live** Weekly
Orchestrator documented at `apex-meta/kb/Weekly-Orchestrator/00-START-HERE.md`, whose runtime
entrypoint today is `.claude/skills/weekly-orchestrator/SKILL.md` — a Claude-Code-native skill
running the locked loop `PrecapWeek -> PrecapNextDay -> execution and evidence capture ->
FlowRecap -> StatusMerge/Project KB update -> ProjectStatus -> next planning cycle`.

**This resolves the "peer system" framing but opens a sharper one — see new Q16.** The Weekly
Orchestrator's macro/meso/micro architecture is already locked and dry-run-verified
(`architecture/01-macro-architecture-decision.md` through `03-execution-trace-verification.md`).
Replacing or augmenting its runtime with a local-LLM + browser-automation + Odysseus/Hermes/
OpenClaw engine is a real architectural change to a live, finalized system — not a greenfield
build. Do not start implementation against this until Q16 is answered.

**Blast radius:** `ORCHESTRATION-SYSTEMS-INDEX.md` and the Weekly Orchestrator's own
`00-START-HERE.md`/architecture package will need updating once Q16 is resolved, since both
currently describe a purely Claude-Code-native runtime with no mention of a local-LLM/browser-
automation execution path.

---

### Q6. Operator boundary: what does the local LLM execute itself vs. only instruct?
**Resolution: not yet decided — explicitly deferred pending Q1.** The operator has not committed
to either "local LLM never touches tools directly, pure instruction/handoff-packet output" or
"local LLM owns cheap/safe tools directly, delegates only the risky/heavy ones."

**Blast radius:** This is one of the highest-leverage undecided questions in the whole document —
it determines the local LLM's tool-access surface, the shape of the sandbox (Q9), and how much
trust the browser-automation layer's *output* (which is untrusted web content once it leaves the
subscription chat) is allowed to carry into local execution. Do not default to "local LLM has
broad tool access" without deliberately revisiting this.

---

## Resolved — 2026-07-28 architecture pass

Q7–Q14 were all resolved in the architecture package created this session
(`architecture/01-macro-architecture-decision.md`, `02-meso-module-design.md`,
`03-micro-implementation-map.md`, `04-decision-ledger.md`). Each resolution below names its
authoritative decision ID; the ranked alternatives and reversal triggers live in
`04-decision-ledger.md` rather than being duplicated here.

| Q | Resolution | Authority |
|---|---|---|
| Q7 | **7–8B structured-output model**, not the ~27B `whichllm` pick. The local model's job (closed-enum classification + short narration) does not benefit from scale, and a 27B build would consume the entire GPU-addressable share of a *shared* 32GB pool, competing directly with the browser fleet. | D-S5 |
| Q8 | **Split by risk bucket:** Claude via its officially sanctioned automation channel; ChatGPT/Gemini via Playwright over a persistent real profile with conservative jittered pacing. Start with the Claude lane only. | D-S4, D-I5 |
| Q9 | **Targeted isolation, not blanket isolation.** Only the executor bridge (the sole component with shell access) runs containerized; the driver stays a host process with narrow filesystem scope, because it never executes untrusted content. The *primary* injection control is structural (frozen plan + quarantine), not isolation — isolation limits blast radius but does not protect integrity. | M7, D-M6 |
| Q10 | **No new workflow language.** `flow_prompt_pack` already *is* the work order; M1 compiles it into an immutable frozen plan. Rejected: bespoke DSL, LangGraph/Temporal, LLM-improvised sequencing. | D-M3, D-S1 |
| Q11 | **Turn-level protocol**, 4-method adapter interface, completion detection as a cheapest-first cascade (native signal → quiescence timer → LLM adjudication). Fresh session per flow; captures written verbatim to disk and referenced by path, never inlined. | M3, M4, D-S6 |
| Q12 | **Per-failure-class policy, not one generic retry.** `captcha_or_challenge` and `account_flagged` never retry; `rate_limited` opens a circuit and tries the declared `fallback_surface`; timeouts retry once. Halt is always resumable and always emits partial evidence. | M9, D-S9 |
| Q13 | **Serial per account, parallel across providers, capped at 2–3 browser sessions.** Per-account serialization is simultaneously the strongest detection-avoidance measure and a hardware necessity on a shared memory pool. MVP starts fully serial. | D-S9 |
| Q14 | **Append-only JSONL ledger + status line first; push notification later.** Hermes is the right eventual channel (its messaging integrations are its genuine strength) but building notification before the failure modes are empirically known is premature. | D-S7, M9 |

---

## Superseded question text (retained for reasoning provenance)

The original open-question framings below are kept because they record what was actually weighed.
They are **no longer open** — read the table above and `04-decision-ledger.md` for current truth.

### Q7. Local LLM selection
Given the resolved scope (Q3: control-plane + light glue reasoning, not raw content generation),
model choice should optimize for **reliable structured tool-calling and instruction-following**
over parameter count — a large general-purpose model is not obviously the right pick just
because it scores well on generic benchmarks. `whichllm`'s hardware-based top pick for this
laptop (a ~27B Qwen build) was computed before this scope was clarified and should be revisited
against this narrower job description, not treated as already decided.

**Candidate directions:**
- A. A small model specifically tuned for function-calling / agentic tool use (7–8B class).
- B. A mid-size model (13–14B class) if the "light glue reasoning" turns out to need more
  headroom than pure routing.
- C. Whatever model the eventual worker framework (Q1) ships or recommends by default — don't
  pick independently of that choice.

**Blast radius:** Coupled to Q1 — if Hermes (Nous Research) ends up in scope, note that Nous
Research also publishes their own "Hermes" model family, which may be a natural fit worth
checking specifically, not a coincidence to ignore.

---

### Q8. Browser automation tooling and provider scope
Which subscriptions are actually in scope (Claude Pro/Max? ChatGPT Plus/Pro/Team? Gemini
Advanced? others?), and by what mechanism per provider — given the Q4 asymmetry, this likely
isn't one universal answer.

**Candidate directions:**
- A. Claude via the official sanctioned extension/automation channel; other providers via
  Playwright/Selenium driving a real logged-in Chrome profile.
- B. One uniform automation approach (e.g. Playwright for everything, including Claude) for
  implementation simplicity, accepting the higher risk bucket for all providers uniformly.
- C. Start with a single provider end-to-end before adding others.

**Blast radius:** Determines the concrete engineering effort for Q4's detection-avoidance work,
and whether the system launches with one reasoning backend or several from day one (see Q13).

---

### Q9. Sandbox / execution isolation model
"Work in a kind of sandbox on this laptop" needs a concrete mechanism. This matters more than it
might look: content coming back from a browser-automated chat session is, from a security
standpoint, **untrusted web content** flowing back into a system that can execute local
commands — a real prompt-injection surface, not just a code-organization question.

**Candidate directions:**
- A. Full OS-level isolation — a separate Windows user account, or WSL2/a container per
  project, so a compromised or manipulated response can't reach the rest of the machine.
- B. Folder-scoped isolation only — each project confined to its own directory / git worktree,
  no deeper OS boundary, on the assumption that the operator boundary (Q6) already limits what
  gets executed from delegated content.
- C. No formal isolation — rely entirely on the operator boundary and human review of
  irreversible actions.

**Blast radius:** Directly coupled to Q6 — a "local LLM owns cheap tools directly" answer to Q6
raises the stakes of this choice considerably, since untrusted content would be closer to direct
execution.

---

### Q10. Workflow / state representation
How is "a flow of prompts" actually defined and persisted — as data the orchestrator reads, not
as something implicit in a conversation.

**Candidate directions:**
- A. Declarative step definitions (YAML/JSON), read and advanced by the orchestrator — closest
  in spirit to this KB's existing packet/handoff schema (role, status, target surface, next
  state, prerequisites).
- B. A code-defined DAG/graph via an existing orchestration library (e.g. LangGraph, Prefect,
  Temporal) rather than a bespoke file format.
- C. A bespoke queue/file-drop protocol invented specifically for this system.

**Blast radius:** Coupled to Q5 — if this ends up being a peer APEX OS system, reusing the
existing backbone's schema shape (rather than inventing a fourth shape in this KB) was the
explicit recommendation of prior research here.

---

### Q11. Handoff / session protocol with the worker layer
When the orchestrator hands a step to a worker (a subscription-chat tab, or Hermes/Odysseus/
OpenClaw), what's the actual contract?

**Open sub-questions:**
- Does it keep one persistent browser tab/conversation per project for multi-turn continuity,
  or open a fresh session per step?
- How does it detect a response is complete — DOM-level completion signal, polling with a
  timeout, or a fixed wait?
- What's the literal input/output shape passed across this boundary (plain text prompt/reply,
  or a structured packet with metadata)?

**Blast radius:** Fragile-by-nature (browser automation breaks in specific ways — see Q12) —
whatever protocol is chosen needs to be resilient to partial/garbled responses, not just the
happy path.

---

### Q12. Failure / recovery policy
Browser-driven subscription automation fails in known, specific ways: session expiry/logout,
page-layout changes breaking selectors, mid-conversation rate limiting, CAPTCHA challenges,
outright account flags. Each may warrant a different response, not one generic "retry" policy.

**Candidate directions:**
- A. Auto-retry N times per failure class, then pause the whole flow and notify the operator.
- B. Auto-retry, then fail over to a different provider/session if one is configured, only
  notifying the operator if all configured backends are exhausted.
- C. No auto-retry — halt and notify on first failure, on the reasoning that a human should look
  at anything unusual given the fragility and the ToS risk already accepted in Q4.

**Blast radius:** Interacts with Q13 (concurrency) — a fail-over policy only works if more than
one backend/session is actually configured.

---

### Q13. Concurrency
One active reasoning-backend session at a time, or multiple provider tabs/subscriptions running
in parallel across different work-steps or different projects?

**Blast radius:** Parallel sessions multiply both the Q4 ToS-risk surface and the Q12
fail-over options — this is a real trade-off, not free capacity.

---

### Q14. Observability
What visibility is wanted while this runs relatively unattended: a log file to tail, a live
status file/dashboard, OS-level notifications on step completion or failure, or direct visual
supervision of the browser window itself? Given the ToS risk already accepted (Q4) and the
inherent fragility (Q12), some form of "tell me when something needs me" signal seems necessary
regardless of which option is chosen — this question is really about the specific mechanism.

---

### Q15. MVP — first concrete end-to-end flow
**Resolution — 2026-07-28:** The MVP target is the **existing Weekly Orchestrator loop**
(`PrecapWeek -> PrecapNextDay -> execution and evidence capture -> FlowRecap -> StatusMerge ->
ProjectStatus`), not a new bespoke flow invented for this initiative. Role split as stated by the
operator:
- **Local LLM** = the engine — sequences the weekly loop's stages, holds state, decides what
  runs next (matches the already-resolved Q3 control-plane + light-glue-reasoning scope).
- **Hermes and/or Odysseus AI and/or OpenClaw** = the agents/executors that actually carry out
  each stage's work.
- **Web reasoning models** (browser-driven subscription chats) = do the actual reasoning
  *within* each stage: prompt design, verification, and prompt execution.

**Still missing before this is a real MVP spec, not just a role split:** which single stage of
the weekly loop gets built first (see Q16 — likely "execution and evidence capture," since that's
the one stage in the existing architecture explicitly about doing bounded work, not
planning/status bookkeeping), what a completed run of that one stage looks like concretely, and
where its output artifact lands relative to the existing `apex-meta/kb/Weekly-Orchestrator/`
package.

**Blast radius:** This grounds Q7–Q14 in a real target instead of the abstract — e.g. Q13
(concurrency) is likely moot for a single-stage MVP, and Q10 (workflow representation) should
default to whatever shape the existing weekly-loop stage contracts already use rather than
inventing a new one, pending Q16.

---

### Q16. Scope of the takeover: whole Weekly Orchestrator runtime, or one stage of its loop?
**Resolution — 2026-07-28: option B, and the exact extension point is now identified with
citation-level precision.** Re-reading the locked stage-dispatch trace
(`architecture/03-execution-trace-verification.md` §3) shows the loop's step 4 is **already**
exactly the seam this initiative needs:

```yaml
step: 4
name: execution
actor_today: operator (human)          # <- this is the seam this initiative replaces/augments
reads:
  - "artifacts/flow-packets/<YYYYMMDD>/"              # the flow packet
  - "artifacts/flow-packets/<YYYYMMDD>/prompt-packs/" # the prompt packs (already AI-authored, by
                                                       #   apex-precap-next-day via PromptEngineer/
                                                       #   AIRouting/Workflow&Processes)
writes: "raw notes, or a skip signal"
gate: G3 (capture)
```

Everything upstream of step 4 (`apex-precap-week`, `apex-precap-next-day` — which already
produces the prompt-packs this new engine would consume) and everything downstream
(`apex-evidence-normalize`, `apex-flow-recap`, `apex-status-merge`, `apex-project-status`, the
dual-blind review pair) stays exactly as locked. **This initiative's scope, precisely: replace
the human actor at step 4 only** — the local-LLM engine reads the existing flow packet +
prompt-packs artifacts, dispatches the actual work to Hermes/Odysseus AI/OpenClaw as
executors with browser-driven subscription-chat reasoning doing the prompt design/verification/
execution, and writes output in the same "raw notes" shape step 5 already expects.

**One commitment carried forward, not optional:** gate G3 must stay a real human checkpoint, not
be silently automated away. Given the standing risks already accepted in this document (Q4 ToS/
ban risk, Q12 browser-automation fragility), G3 becomes the point where the operator reviews what
the automated flow actually produced before it feeds into evidence-normalize and, eventually,
canon project-state writes via Apex Session (D-M4's single write path is unaffected by any of
this).

**Follow-up checked and closed, not open — `.claude/skills/raw-flow-dump-normalize/SKILL.md`
read in full on 2026-07-28.** No format mismatch exists: the skill's own contract is explicitly
built for heterogeneous, unstructured input ("messy operator execution notes, chat fragments,
artifact references, or skipped-flow signals"). A clean, machine-generated dump is strictly
*easier* to normalize than typical messy human notes, not harder — it should score higher on
`normalization_confidence`, and the `model_usage_notes` output field is a better fit for an
automated flow than a human (a human executing manually routinely forgets to log exactly which
model/tool was used at each step; this engine will know precisely).

The one real requirement, trivial to satisfy: the skill's failure modes name exactly three
fields that must be present to locate context — `flow_id`, `execution_day`,
`source_flow_packet_ref`. The engine already has all three in hand from reading the flow packet
at step 4; it only needs to carry them into its output rather than drop them. Keep straight (not
a blocker, just a shape to respect): `produced_outputs` is its own field, distinct from the
narrative dump text — if a flow's real deliverable is e.g. a research report, that report is a
`produced_outputs` artifact reference, not something to conflate with the raw-notes narrative.

**Superseded:** the "full replacement" (A) and "parallel/experimental track" (C) directions
originally posed above are dropped — B is a strictly smaller, already-defined extension point,
and there's no evidence in this KB motivating touching the seven other locked stages.

**Blast radius:** This resolves the single highest-leverage open question. Q7 (model
selection), Q9 (sandbox model), Q10 (workflow representation), and Q11 (handoff protocol) can now
all be answered against a concrete, narrow target — "replace one human-performed step in an
already-running pipeline" — instead of an abstract greenfield system.
