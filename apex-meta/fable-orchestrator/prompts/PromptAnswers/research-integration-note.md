---
title: "External Research — Critical Integration Note"
purpose: >
  Orchestrator's honest assessment of the two deep-research answers returned for the
  external research pack (P1 role-vs-state permission, P2 adversarial-review wiring),
  ground-checked against real repo state, with the verified findings folded into
  design-lock-answers.md and the residual gaps named.
created: 2026-07-11
status: "drafted — feeds the Q6/Q7/Q8 updates in design-lock-answers.md; operator-gated"
---

# External Research — Critical Integration Note

## 0. Did we get what we wanted? (the honest answer)

**Mostly yes — more than the copy-paste framing suggested — but with one recommendation that the repo cannot currently support and a grounding weakness that must be corrected before any of it locks.**

The two prompts each carried an explicit *decision-change bar* ("only report if you can flip a build decision"). **Both cleared their bar.** That is the opposite of the earlier v1 ceremony problem — these two returns are decision-capable:

- **P1** produced a concrete break-scenario that our current Q6/Q7 answer genuinely does not cover, and lands on a *minimal* fix (one artifact-state field) rather than reviving the full state machine. It moves Q7/Q8.
- **P2** produced a concrete reason the single-Detective translation in Q8 is insufficient for consequential outputs, and specifies a buildable alternative. It moves Q8's Detective step.

So the initiative's stated purpose for these two prompts — "research that can change a high-cost build decision" — was met.

**The valid criticism (operator's, and correct):** the answers argue mostly from *generic framework surveys* (CrewAI, LangGraph, AutoGen, OpenAI Swarm/Agents SDK) and *web citations*, with only thin repo grounding (a few `fileciteN` markers). They reason about "a file-based Claude Code system" in the abstract rather than about **our** systems by name. That is a research-hygiene weakness: the recommendations are generically argued, so they must be ground-checked against our actual files before being trusted — which is what §2–§3 below do, and why the re-run prompts (v3) are rewritten to name the systems, folders, and KB explicitly.

## 1. What each answer actually recommends (compressed)

| Prompt | Verdict | Decision it moves |
|---|---|---|
| **P1 — role-vs-state permission** | Add a minimal per-artifact `authority.state ∈ {candidate, verified, invalidated}` field with a `basis_digest` binding the review to the exact content+evidence version; enforce it in the *existing* apex-session write path. **Do NOT restore BUILD/VERIFY/LOCK.** | Q7 (drift control was "glossary + nothing else") and Q8 (state-machine invariant was called "already provided by the package boundary + gate"). |
| **P2 — adversarial-review wiring** | A single same-family Claude "Detective" is **not** sufficient independent validity review for consequential outputs (shared training priors → self/family preference, correlated blind spots). Split into a **validity** lens (ideally a *different model family*, read-only, blind, criterion-level falsification) and a **strategic-alignment** lens (fresh Claude subagent is fine), run blind + in parallel, aggregate **deterministically** (no majority vote, no LLM aggregator), reviewer may never fix its own finding. | Q8's `meta_detective → one workflow step` translation. |

## 2. Ground-check against real repo state

### P1 — verified, and the target surface exists
- **Claim:** there is one exclusive mutation surface to bolt the check onto.
  **Verified:** `.claude/skills/apex-session/SKILL.md` L196–198, L236–240 — `status_mutation_record` + `operator_validation: confirmed` gate + `silent_repo_mutation_allowed: false`. P1's "enforce inside the existing write script" is architecturally coherent with what already exists (EM D6).
- **Claim:** role-boundary + `operator_validation` cannot answer "was the *artifact this mutation relies on* independently reviewed and still current?"
  **Assessment: correct, and it is a real gap in our design.** `operator_validation` authorizes the *mutation*; nothing in the three-package boundary attaches authority to an *input artifact's lifecycle version*. This is exactly the v2 candidate-vs-canon invariant (EM D4 left column) that our Q8 claimed was "already provided" — P1 shows it is only *partly* provided (the proposal≠computed≠confirmed axis is covered; the reviewed-and-current axis is not).
- **Net:** P1 clears the Q8 decision-change bar. Adopt a *minimal* artifact-authority field — not the full machine. This is consistent with, and sharpens, Q8-B "translate, don't revive": the invariant survives as one enforced field, not a state engine.

### P2 — verified as a real weakness, but its headline fix is currently unbuildable here
- **Claim:** same-family review shares priors; a fresh Claude subagent gives context isolation, not epistemic independence.
  **Assessment: sound, and it matches our own after-action evidence** (fable-execution-best-practices §7 / the "same-context subagents re-derive rather than independently verify" lesson the answer cites as `file0`).
- **Claim / headline fix:** use a **different model family** for the validity judge, exposed via **MCP or an API wrapper**.
  **Ground-check: no such surface exists in this repo.** A grep across `.claude/` and `scripts/` finds *zero* runtime external-model tools. The only OpenAI/Gemini references are (a) illustrative code in `prompt-engineering-patterns`, (b) `AIRouting`/`PromptEngineer` *copy-paste routing contracts* (which provider a human should paste a prompt into), and (c) an offline `deterministic-markdown-patcher/agents/openai.yaml`. **None is an in-run tool the orchestrator can call.** So P2's headline recommendation requires building net-new trusted infrastructure (external-judge wrapper + credentials inside the trust boundary) that the current system deliberately does not have — the whole three-package system is standard-library-only and offline (EM D1).
- **Net:** P2 clears the bar on the *diagnosis* (single same-family Detective is insufficient) and on the *buildable-without-MCP* parts (blind packets, hidden author reasoning, criterion-level falsification with mandatory strongest-wrong-case, evidence-bearing PASS gate, deterministic aggregation, reviewer-can't-fix-own-finding, re-review only after a new hashed version). Those we adopt now. The *cross-family judge* is recorded as a **deferred escalation**, not a v1 build item, because it breaks the offline/stdlib property and needs a trust-boundary decision the operator has not made.

## 3. What actually changes in design-lock-answers.md

1. **Q7 (drift control):** widen from "glossary + nothing else" to "glossary + one minimal artifact-authority field." The glossary pins *terminology* drift; the `authority.state` field pins *artifact-currency* drift — a different failure class P1 made concrete.
2. **Q8 (state machine row):** correct the claim that the package boundary "already provides" the candidate/canon invariant. It provides the proposal≠computed≠confirmed axis only. Add the minimal `authority.state` field (candidate/verified/invalidated + basis_digest) enforced in the apex-session write path as the translated-not-revived form of the v2 invariant.
3. **Q8 (meta_detective row):** replace "one workflow step (one subagent)" with the two-lens design (validity + alignment, blind + parallel, deterministic aggregation, reviewer can't fix). Record cross-family validity judge as a deferred escalation dependent on an operator MCP/trust-boundary decision.

## 4. Residual gaps / what these answers did NOT settle
- **Whether the cross-family judge is worth building at all.** P2 argues it is necessary for "consequential validity"; our repo's design ethos is offline/stdlib/no-external-trust-surface. This is a genuine operator trade-off (independence vs. attack surface + dependency), not a settled fact.
- **`basis_digest` scope.** P1 says "canonicalized content + hashes of declared evidence + dependency refs." For our Markdown+frontmatter work items that is implementable in `scripts/apex_sync.py` (stdlib hashlib), but the exact canonicalization rule is a milestone-5 detail, not decided here.
- **Neither answer was repo-bound.** Their framework surveys are context, not evidence about our system. The v3 prompts fix this for any re-run; the findings above are trustworthy only to the extent §2's ground-check confirmed them against real files.
