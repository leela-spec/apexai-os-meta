---
title: "External Research Pack — 2026-07-11 (v2, deep-research-grade)"
purpose: >
  Deep-research prompts for the two architecture questions where an external frontier model
  can actually change the build, plus one optional low-value prompt and one lean repo-grounded
  verification prompt. Rewritten from v1: v1's four prompts were confirmatory best-practice
  lookups (they could not overturn any design-lock answer, which per decisions.md D2 makes them
  ceremony). v2 keeps only research that can flip a decision, and makes those prompts adversarial,
  context-loaded, and artifact-producing.
created: 2026-07-11
supersedes: "the v1 prompt set previously in this file"
execution_target: >
  Written for GPT-5.6 in HIGH-REASONING / deep-research mode (long-horizon, tool-using web
  research with browsing). P1 and P2 are the real deep-research runs — expect 20-60 min each and
  a multi-page cited report. P3 is optional/low-value (skip unless P1/P2 surface a reason to run
  it). P4 is a lean verification pass, not deep research — run on Perplexity (GitHub connector),
  not GPT.
grounding_after_return: >
  Every returned claim is cross-checked against real repo state before it touches a design-lock
  answer (fable-execution-best-practices.md §4). Verified extracts written to file immediately;
  only a pointer + one-line verdict kept in session context (§5).
decision_change_criterion: >
  Each deep prompt below states, explicitly, the finding that would FLIP our current answer. If a
  prompt comes back unable to meet that bar, the current answer stands and the research cost was
  the price of confidence — not a reason to soften the answer to match a vague result.
---

# How to run this pack

| Prompt | Model / mode | Value | What it can change |
|---|---|---|---|
| **P1** — role-vs-state permission | GPT-5.6, high-reasoning deep research | **High** | Q8 state-machine decision; Q6 gate schema; whether we add a state layer at all |
| **P2** — adversarial-review wiring | GPT-5.6, high-reasoning deep research | **High** | The one component we must build from scratch (D3 hole); Q8 Detective translation |
| **P3** — gates + persistent agents (combined) | GPT-5.6, medium reasoning | **Low / optional** | Confirmation only — skip unless P1/P2 expose a gap |
| **P4** — matrix verification | Perplexity (GitHub connector) | Utility | Catches any citation error in `evaluation-matrix.md` before it propagates |

Honest note to the operator: P1 and P2 are worth your time because they attack the two decisions with the weakest in-repo evidence and the highest build cost. P3 is included for completeness but I expect it to return "your current approach is standard" — run it only if you want the paper trail. P4 is cheap insurance, not research.

---

# P1 — Role-vs-state permission separation (DEEP)

**Paste into GPT-5.6, high-reasoning deep-research mode.**

```
ROLE
You are a principal architect reviewing an agent-orchestration system's permission model. You
have designed permission/authorization layers for both multi-agent LLM systems and traditional
workflow engines, and you are known for arguing against unnecessary state machines as often as
for them. Treat this as an adversarial design review: your job is to find where our current
decision breaks, not to ratify it.

THE DECISION UNDER REVIEW
We are merging two orchestration systems into one, to run inside Claude Code (skills + ephemeral,
tool-scoped subagents; all durable state lives in Markdown files with YAML frontmatter; git-backed).

  - System A (older) makes this its central invariant, verbatim: "Roles remain the semantic
    accountability layer. Operational states are the real permission layer. No role label may be
    used as compliance theater for permissions the current state does not grant." It implements
    this as a three-state machine per work item — BUILD (bounded creation, no self-verification),
    VERIFY (review/reconciliation/promotion-proposal, no silent rewrites), LOCK (read-only unless a
    governing protocol lifts it) — with defined transitions (BUILD->VERIFY, VERIFY->BUILD,
    VERIFY->LOCK, LOCK->BUILD-by-explicit-lift). CRITICALLY: this state machine was fully specified
    in prose and NEVER actually mechanized/executed. It is unproven design law.

  - System B (current, live) has NO state machine. It uses role-based capability partitioning:
    three skills each hard-forbid the others' capabilities (a planning skill cannot mutate state;
    a compute skill cannot author plans; only a session skill may write confirmed mutations), plus
    ONE state-shaped gate on the single write path — a required field operator_validation ∈
    {confirmed, rejected, needs_revision, not_requested}, no_implicit_apply, and dry-run-first
    script writes. This is real, running, file-backed.

OUR CURRENT ANSWER (the thing you must try to break)
Adopt B's mechanized role-partitioning + single write-path gate; do NOT revive A's full
BUILD/VERIFY/LOCK state machine; keep A's invariant ("role is accountability, state is
permission") as a design rule applied ONLY at mutation surfaces via the gate field. Rationale:
don't add a general state machine unless a concrete failure is observed that the role boundary +
write gate don't already prevent.

TASK (single objective)
Determine whether role-based capability partitioning plus a single state-gated write path is
genuinely sufficient, OR whether a first-class operational-state layer (per work item, not just at
the write path) prevents a class of real, documented failures that role-partitioning cannot.
Research the actual state of the art (2024-2026), don't reason from first principles alone.

WHAT TO SURVEY (name concrete systems/papers, don't hand-wave "best practice")
  - How real multi-agent frameworks model permission/authority (survey specifically: AutoGen/AG2,
    LangGraph's state model, CrewAI roles, OpenAI Swarm/Agents SDK handoffs, Anthropic's own agent
    guidance). For each: is authority carried by role identity, by graph/workflow state, by both,
    or by neither — and what failure did that choice cause or prevent?
  - The security/authorization literature on RBAC vs. ABAC vs. state/lifecycle-based access
    control, mapped onto agent systems: where does role-only authorization provably fail (privilege
    that should depend on artifact lifecycle, not actor identity)?
  - Documented failure modes in LLM agent systems that a lifecycle-state layer specifically
    catches: self-approval, premature promotion of candidate to canon, an actor acting on stale
    authority, "structurally complete but ungrounded" output passing because no state forbade it.

ADVERSARIAL REQUIREMENT
Construct the strongest concrete scenario in which OUR CURRENT ANSWER fails — a specific sequence
of agent actions on a real-shaped artifact where role-partitioning + a single write gate lets
through something a BUILD/VERIFY/LOCK layer would have blocked. If you cannot construct one that
survives scrutiny, say so plainly and explain why the simpler design holds.

DELIVERABLE (return exactly this)
  1. A decision table: [permission model | authority carried by | failure class it prevents |
     failure class it CANNOT prevent | real system/paper exhibiting this | adoption cost in a
     file-based Claude Code system]. Min 6 rows spanning role-only, state-only, and hybrid.
  2. Your single strongest break-scenario against our current answer (or an explicit "no valid
     break found" with reasoning).
  3. A recommendation in one of exactly three verdicts: (a) current answer holds — role-partition
     + single write gate is sufficient; (b) add a minimal state field to every work item (not a
     full machine) — specify the exact field, allowed values, and transition rule; (c) a full
     lifecycle state layer is warranted — specify it and justify the added concept against its cost.
  4. If (b) or (c): the exact YAML field(s) and the ONE enforcement surface (schema check, git hook,
     or mandatory review step) that makes it real rather than prose.

DECISION-CHANGE BAR (be honest about whether you cleared it)
Flip us off verdict (a) ONLY if you produced a concrete, plausible failure scenario that
role-partition + write-gate cannot prevent AND that a lightweight state field genuinely would.
Generic "state machines add rigor" is NOT sufficient — System A's state machine was never even
run, so untested rigor is exactly what we're trying not to import.

SOURCE RIGOR
Inline citations/links on every factual claim and every named-system behavior. Distinguish "the
framework documents this" from "practitioners report this" from "I am inferring this." Uncited
behavioral claims about named systems will be discarded on our end.
```

---

# P2 — Adversarial-review wiring for an orchestrator-worker system (DEEP)

**Paste into GPT-5.6, high-reasoning deep-research mode.**

```
ROLE
You are an LLM-evaluation researcher who specializes in LLM-as-judge reliability and multi-agent
review. You have published on why naive "have another model check it" fails (sycophancy,
rubber-stamping, correlated blind spots) and on what actually makes independent review trustworthy.
You are skeptical of adversarial-review theater that produces a PASS stamp without real scrutiny.

WHY THIS MATTERS TO US (the stakes)
We are building an orchestration system where, today, there is provably ZERO adversarial cross-
check: a grep across all runtime skills returns no independent-review step. Our own reference
research names the resulting failure — "structurally complete, semantically ungrounded output" —
as ALREADY OBSERVED in this project, not hypothetical. We are about to build the missing reviewer
("Detective") and we will live with whatever wiring you help us get right. This is the single
component we cannot copy from either source system; both lack it in runnable form.

THE CONSTRAINTS WE MUST BUILD WITHIN
  - Runtime: Claude Code. The reviewer is an ephemeral, context-isolated subagent with a scoped
    tool allowlist and a precise description; it is spawned per consequential output, not standing.
  - The reviewer issues criterion-level verdicts (pass / revise / hold / needs_input / escalate),
    NAMES the owner of each defect, may NOT implement any fix, and re-reviews the corrected
    ARTIFACT (not the correction claim) on the next pass.
  - Two review lenses are deliberately separated: independent validity review (evidence,
    contradiction, plausibility, safety, scope, drift) vs. strategic-alignment review (does it
    still serve the macro goal). We want to know if that separation should be two subagents, two
    passes of one, or something else.
  - Work products are structured packets (sources, assumptions, uncertainties, changed claims,
    stop conditions). Reviewer input and output are both files on disk.

TASK (single objective)
Design the concrete wiring for a trustworthy independent-review step in this orchestrator-worker
system, grounded in current (2024-2026) evidence on what makes LLM-vs-LLM review reliable vs.
theater — and specify the exact failure modes we must engineer against and how.

WHAT TO SURVEY (concrete, cited)
  - LLM-as-judge reliability findings: measured rates and drivers of sycophancy, self-preference
    bias (a model favoring its own or similar-style output), position/verbosity bias, and
    calibration failure. Which of these survive when the judge is a DIFFERENT model vs. the same
    model in a different role?
  - Multi-agent review/debate patterns and whether they actually improve correctness over a single
    critical pass, or mostly increase confidence without accuracy (cite the studies that found
    both results — do not cherry-pick the optimistic ones).
  - Concrete anti-rubber-stamp mechanisms that have evidence behind them: forcing the reviewer to
    argue the artifact is WRONG before it may pass it; requiring criterion-by-criterion verdicts
    with cited evidence per criterion; independent-then-aggregate vs. sequential review; using a
    different model family for the judge; withholding the author's reasoning from the reviewer.

ADVERSARIAL REQUIREMENT
Take our sketch above and show how it FAILS as described — the specific way an isolated Claude
subagent reviewing another Claude subagent's packet will rubber-stamp or share a blind spot — then
fix the wiring to close that hole. We would rather you break our sketch now than discover it after
we build it.

DELIVERABLE (return exactly this)
  1. A numbered wiring spec (<= 12 steps), each step with explicit inputs -> outputs and WHICH
     artifact/file it reads and writes. Make clear where the two lenses (validity vs. alignment)
     are separated and why you wired them that way.
  2. The reviewer's input-packet schema and verdict-output schema, both as YAML, with a field
     whose job is specifically to prevent an evidence-free PASS.
  3. A failure-mode table: [failure mode | why it happens in same-family LLM review | the specific
     mechanism in your wiring that mitigates it | residual risk that remains | citation]. Cover at
     minimum sycophancy, self-preference, correlated blind spot, and rubber-stamp-under-time.
  4. One explicit recommendation on the model question: same model different role, different model
     family, or majority vote across N — with the evidence for your choice and the token/latency
     cost we're accepting.

DECISION-CHANGE BAR
If the evidence shows same-family LLM review is unreliable enough to be theater, say so directly —
that would change our plan from "one Detective subagent" to "different-model judge" or "N-of-M
independent verdicts," and we need to know that BEFORE we build, not after.

SOURCE RIGOR
Inline citations on every measured claim (bias rates, "debate helps/doesn't help" results). Flag
where the literature disagrees rather than resolving it artificially. Distinguish lab-benchmark
findings from production-practitioner reports.
```

---

# P3 — Operator gates + persistent-agent escalation (OPTIONAL, low value)

**Only run if P1 or P2 surfaces a reason to. Medium reasoning is enough; this is confirmatory.**

```
ROLE
You are an agentic-systems reviewer. Two quick questions; we already have working answers and
mainly want to know if current practice contradicts them.

CONTEXT
(1) Our operator-approval gate is a single reusable primitive: a required YAML field
operator_validation ∈ {confirmed, rejected, needs_revision, not_requested} plus a required literal
confirmation phrase for phase transitions, applied risk-weighted (full gate only for consequential
outputs: direction change, public release, durable-knowledge promotion, spend, external action,
safety exposure) — NOT a global autonomous-mode toggle.
(2) We keep durable roles as ephemeral, tool-scoped subagent definitions invoked per-run with no
standing memory beyond files on disk. We are NOT giving any role persistent cross-session memory
yet.

TASK
For each: does current (2025-2026) practice broadly support it, and is there a specific documented
failure our approach would walk into? For persistent agents, give a <=8-item checklist for deciding
when a role should be promoted from ephemeral to persistent (durable identity/memory), and the
costs (state drift, stale memory, permission creep) with citations.

DELIVERABLE
(1) Two short verdicts: "supported / supported-with-caveat / contradicted," each with the single
strongest citation. (2) The persistent-agent promotion checklist. (3) <=150-word recommendation.
Keep it tight — if the answer is "your approach is standard," say exactly that and stop.
```

---

# P4 — Evaluation-matrix verification (Perplexity, GitHub connector — NOT deep research)

**Paste into Perplexity with the GitHub connector enabled. Lean fact-check, run before trusting the matrix downstream.**

```
Use your GitHub connector on repository leela-spec/apexai-os-meta, branch
claude/fable-orchestrator-setup-9pc5pu.

Act as an adversarial fact-checker. Verify or refute each claim in the file
apex-meta/fable-orchestrator/evaluation-matrix.md, section "2. Per-dimension scoring", against the
actual files it cites. Check specifically:
  1. .claude/skills/apex-plan/SKILL.md, apex-sync/SKILL.md, apex-session/SKILL.md — do the quoted
     field names (operator_validation, no_implicit_apply, script_policy.scripts_allowed, the
     requested_operator_action enum), boundaries, and cited line ranges actually appear?
  2. scripts/apex_sync.py — standard-library-only? dry-run default true? registry the only write path?
  3. apex-meta/kb/old-apex-full-orchestration-agent-kb-v2/raw/other/managed/rules/
     AGENT_SWARM_INTERACTION_CANON.md — does the verbatim permission-layer quote ("Roles remain the
     semantic accountability layer...") appear, and do cited line ranges match?
  4. Does apex-meta/registry/index.md exist in the repo, or not?
  5. Does .../old-apex-full-orchestration-agent-kb-v2/wiki/index.md state "Compiled page count: 17",
     and how many compiled page files actually exist under that wiki/?

Output: one table row per numbered item plus one row per additional material claim you check —
[claim | verified / refuted / partial | exact file path + what you found]. Do not summarize the
matrix; audit it. Flag anything you could not access rather than guessing.
```
