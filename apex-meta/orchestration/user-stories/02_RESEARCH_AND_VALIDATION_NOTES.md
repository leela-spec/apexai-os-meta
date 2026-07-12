# APEX Orchestration User Stories — Research and Validation Notes

## 1. Research scope and snapshot

```yaml
research_scope:
  repository: leela-spec/apexai-os-meta
  branch: main
  read_snapshot: f4c81bf7fe5ad00b9bab6b83026071a7bb96d884
  accessed_on: 2026-07-11
  repository_mode: read_only
  web_research_mode: targeted_primary_sources_after_macro_skeletons
  governing_attachment_status: unavailable_in_accessible_attachments_and_not_found_in_repository_search
  governing_fallback: operator_request_decisions_treated_as_baseline
```

The web pass was performed after all seven macro skeletons existed. It was used to improve specific workflow decisions—parallelization, evaluator separation, context handling, human approval, deterministic support, and recovery—not to introduce additional APEX layers.

## 2. Relevant current web-research improvements

### W-A1 — Anthropic, “Building effective agents”

- **Source:** `https://www.anthropic.com/engineering/building-effective-agents`
- **Published:** 2024-12-19; accessed 2026-07-11.
- **Relevant findings:** successful implementations tend to use simple, composable patterns; prompt chaining may include intermediate gates; independent subtasks can run in parallel; orchestrator-workers fit dynamic decomposition; evaluator-optimizer loops fit work with clear criteria; agents need environmental ground truth, checkpoints, stopping conditions, and human review.
- **Translation into stories:**
  - all stories start with the smallest adequate agent/skill/tool set;
  - MEDIA, OFFER, WORKSHOP, and COMP parallelize only independent branches;
  - Detective is independent of the creator;
  - iteration has explicit pass criteria and stop conditions;
  - complexity is added only when it changes workflow quality.

### W-A2 — Anthropic, “Effective context engineering for AI agents”

- **Source:** `https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents`
- **Published:** 2025-09-29; accessed 2026-07-11.
- **Relevant findings:** context is finite; effective context is the smallest high-signal set; tools should be clear and minimally overlapping; just-in-time retrieval uses paths and lightweight references; structured note-taking supports long-horizon coherence; focused subagents isolate verbose work and return condensed results.
- **Translation into stories:**
  - each worker gets a bounded source slice and compact packet;
  - durable source maps, asset registers, obligation registers, and session packets replace corpus dumping;
  - workers return distilled artifacts and uncertainty rather than full internal work logs;
  - specialists activate only where their distinctive contribution justifies context and coordination cost.

### W-A3 — Anthropic, “Equipping agents for the real world with Agent Skills”

- **Source:** `https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills`
- **Accessed:** 2026-07-11.
- **Relevant findings:** skills use progressive disclosure; linked files are loaded only as needed; deterministic code is preferable for repeatable operations such as extraction or sorting; skills should be evaluated and refined incrementally.
- **Translation into stories:**
  - skills support an accountable agent instead of becoming a parallel authority;
  - detailed references remain behind compact entrypoints;
  - deterministic status, dependency, consistency, and evidence checks sit under Meta Ops;
  - learning from pilots or failures remains candidate-only until reviewed and accepted.

### W-O1 — OpenAI, “A practical guide to building agents”

- **Source:** `https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/`
- **Accessed:** 2026-07-11.
- **Relevant findings:** begin incrementally; maximize a single accountable system before multiplying agents; multi-agent systems add overhead; manager patterns retain central workflow control; runs need exit conditions; human intervention is appropriate when failure thresholds are exceeded or actions are high-risk, sensitive, irreversible, or high-stakes; risk-rate tools and combine model and deterministic guardrails.
- **Translation into stories:**
  - durable core agents stay few; most production work is temporary and bounded;
  - Meta Ops remains the integration spine rather than allowing peer workers to take control;
  - operator gates are concentrated at release, spending, implementation, durable mutation, external submission, and safety/compliance points;
  - retries and repair loops have stop conditions and escalate rather than continue indefinitely.

### W-O2 — OpenAI, “Safety in building agents”

- **Source:** `https://developers.openai.com/api/docs/guides/agent-builder-safety`
- **Accessed:** 2026-07-11.
- **Relevant findings:** structured outputs constrain downstream data flow; tool approvals should remain on; evals and trace grading help locate failures; isolation and structured fields reduce, but do not eliminate, risk.
- **Translation into stories:**
  - handoffs use explicit fields rather than free-form context dumping;
  - LEELA separates practice, boundary, requirements, and implementation artifacts;
  - COMP uses typed obligation/status/evidence records;
  - public and high-risk actions remain reviewable and operator-approved.

### W-MCP1 — Model Context Protocol Specification 2025-11-25

- **Source:** `https://modelcontextprotocol.io/specification/2025-11-25`
- **Status:** latest specification shown on access date.
- **Relevant findings:** separates resources, prompts, and tools; supports stateful connections, progress, cancellation, errors, and logging; requires user consent and control over data access and actions; roots bound filesystem access.
- **Translation into stories:**
  - source data, reusable procedures, and executable actions remain conceptually distinct;
  - external actions and tool use have visible approval and scope boundaries;
  - long workflows need progress, stop, error, and audit evidence;
  - no story requires MCP itself as a mandatory implementation mechanism.

### W-N1 — NIST AI Risk Management Framework and Generative AI Profile

- **Sources:**
  - `https://www.nist.gov/itl/ai-risk-management-framework`
  - `https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence`
- **Accessed:** 2026-07-11.
- **Relevant findings:** trustworthiness and risk management apply across design, development, use, and evaluation; organizations should preserve evidence and align controls to risks and goals.
- **Translation into stories:**
  - WORKSHOP and COMP use lifecycle controls, not one-time review;
  - LEELA checks privacy, autonomy, and human-value boundaries before implementation;
  - recurring state and reopen triggers are explicit.

### W-M1 — Microsoft HAX Guidelines for Human-AI Interaction

- **Source:** `https://www.microsoft.com/en-us/haxtoolkit/ai-guidelines/`
- **Accessed:** 2026-07-11.
- **Relevant findings:** human-AI design must cover initial use, ongoing interaction, situations in which the AI is wrong, and adaptation over time.
- **Translation into stories:**
  - every operator-facing flow exposes uncertainty, correction, hold, and override paths;
  - accepted corrections are recorded separately from speculative learning;
  - recovery behavior is designed alongside the ideal path.

## 3. Major workflow interpretations

```okf
interpretations:
  four_role_control_plane:
    conclusion: "Alfred, Meta Strategy, Meta Ops, and Meta Detective are durable accountabilities, not a requirement that all four act on every low-impact item."
    effect: "IDEA omits Strategy by default; all public, directional, implementation, safety, or compliance milestones include Strategy alignment."

  specialist_agents:
    conclusion: "Historical specialists are represented as bounded lanes or temporary workers backed by skills and scoped knowledge."
    effect: "Knowledge Bank, Informatics Design, and Prompts & Workflows never inherit orchestration or independent final authority."

  plan_sync_session:
    conclusion: "Plan, Sync, and Session are Meta Ops support capabilities."
    effect: "Plan proposes, Sync computes, and Session records an approved state delta; none becomes a peer orchestrator."

  dual_review:
    conclusion: "Validity and strategic alignment answer different questions and must not be collapsed."
    effect: "Detective passes evidence/scope/safety; Strategy then assesses objective, leverage, timing, audience, and intended outcome."

  correction_ownership:
    conclusion: "The repair owner is determined by the defect, not by who detected it."
    effect: "Strategy repairs promises; creators repair content; Ops repairs dependencies and integration; implementers repair implementations; professionals resolve their domain questions."

  deterministic_model_split:
    conclusion: "Model judgment handles ambiguity and synthesis; deterministic support handles exact state, dependencies, coverage, versions, tests, and evidence retrieval."
    effect: "No deterministic pass silently authorizes a semantic decision or durable mutation."

  durable_state:
    conclusion: "Files, evidence links, verdicts, and state deltas are the system of record."
    effect: "Every multi-session story names continuity artifacts and requires fetch-back before closure."

  macro_meso_micro:
    conclusion: "Macro is not a one-time introduction; micro results must roll upward through validity and alignment review."
    effect: "Pilot, release, implementation, launch, and compliance evidence can change the macro direction through an explicit operator decision."
```

## 4. Cross-story validation record

| Validation question | Result | Evidence in primary artifact |
|---|---|---|
| Exactly seven fixed stories present | Pass | Seven `story_id` values from `US-SEQ-01` through `US-COMP-01` |
| Each describes real intended work | Pass | Each macro names a project, starting material, deliverable, and completion condition |
| Each workflow is materially distinct | Pass | Method/pilot, media fan-out, product translation, embodied workshop, knowledge intake, commercial launch, compliance operations |
| Agent interplay is visible | Pass | Every meso flow includes handoffs, integration, review, repair, revalidation, and continuation |
| Important work is independently validated | Pass | Meta Detective is never the creator of the reviewed candidate |
| Strategy and validity are separated | Pass | Important milestones use Detective first, then Strategy alignment |
| Failed checks have named repair routes | Pass | Each micro block contains defect-specific owner and correction examples |
| Operator gates are consequential | Pass | Gates occur at direction, pilot, release, durable mutation, implementation, launch, external action, or professional boundary |
| Low-impact work is not over-governed | Pass | IDEA uses a compact flow and activates Strategy conditionally |
| Work proceeds in small batches | Pass | One session, one pilot episode, one use-case slice, one workshop format, one idea, one demand test, bounded obligation lanes |
| Safe parallelism is used | Pass | MEDIA, WORKSHOP, OFFER, and COMP fan out only after shared constraints are stable |
| Passed work is preserved | Pass | Repair rules reopen affected assets or components, not the entire project |
| Durable continuity is explicit | Pass | Every story names continuity artifacts; Session records accepted deltas |
| Candidate and accepted state are separated | Pass | IDEA, learning loops, requirements, source interpretations, and compliance status use candidate/accepted states |
| Meta Strategy does not execute | Pass | Strategy frames, aligns, and recommends; execution remains with Ops/workers/humans |
| Meta Ops does not self-validate | Pass | Ops integrates and computes reports; Detective validates important candidates |
| Meta Detective does not implement | Pass | Detective issues verdicts and repair maps only |
| Specialists do not take over orchestration | Pass | All specialist returns fan back to Meta Ops |
| Skills do not erase accountability | Pass | Shared context explicitly binds skills to invoking agents |
| Professional authority remains human | Pass | WORKSHOP and COMP include qualified human reviews and hold conditions |
| Stories guide Fable without specifying runtime | Pass | Section 7 lists required capabilities and excludes file-layout/framework prescriptions |

## 5. Consequential assumptions

1. **Governing attachment unavailable.** The named “User Stories — Decision and Definition Log” was not available in `/mnt/data`, did not appear through uploaded-file search, and did not surface in repository search. The detailed operator request was treated as the validated baseline. If the missing log contains additional locked decisions, this portfolio requires a reconciliation pass.
2. **Morning Routine content boundary.** The repository supports Morning Routine as a project and a three-video planning candidate but does not expose the complete mature practice content in the inspected sources. The story therefore defines the orchestration around source material without inventing episode substance.
3. **Dance Fusion evidence boundary.** The repository verifies Dance Fusion as a portfolio concept and verifies demand-first offer/media/workshop workflows. It does not verify audience, price, venue, or offer claims. Those remain explicit operator decisions and research hypotheses.
4. **Sequencing and Leela confidence.** The repository marks the Sequencing-to-Leela workflow as inferred and medium confidence. The stories keep Leela implications downstream of coaching-method evidence and require a separate product gate.
5. **External professionals.** “Qualified reviewer” means a person with the credentials, jurisdictional competence, and engagement terms appropriate to the specific question. APEX tracks the handoff and evidence; it does not determine professional qualification by assertion.
6. **Current law and product rules.** The compliance story is an orchestration blueprint, not a statement of current German, EU, or other legal requirements. Runtime execution must retrieve current official sources and professional advice for the actual jurisdiction and activity.

## 6. Unresolved implementation boundaries

These are deliberately left for Fable or later implementation work; they are not converted into hidden story assumptions.

- Exact persisted schema for macro, meso, micro, verdict, approval, state-delta, and evidence records.
- Exact naming and packaging of the shared handoff contract.
- Whether Plan, Sync, and Session remain three skill folders or become one Meta Ops package with internal modes.
- Which state computations are scripts, hooks, native repository operations, or MCP-backed tools.
- Exact model selection and context budget for Strategy, Ops, Detective, specialists, and temporary workers.
- How operator approval is represented in the UI and how write-side tools enforce it.
- How external professional identities, responses, confidentiality, and evidence retention are managed.
- Whether Codex implementation returns through GitHub pull requests, local patches, worktrees, or another reviewed execution surface.
- Numeric retry limits, timeout policies, and packet-size limits; stories require explicit limits but do not prescribe their values.
- Production source locations for the complete Morning Routine, Sequencing, Peaceful Warrior / Superhero, Dance Fusion, and compliance materials.

## 7. Final interpretation

The portfolio supports one decisive conclusion:

> **APEX should not behave like a crowd of autonomous agents. It should behave like one operator-controlled project system in which a small set of durable accountabilities routes bounded work, preserves state, separates creation from validation, repairs defects at their source, and repeatedly reconnects detailed execution to the macro objective.**
