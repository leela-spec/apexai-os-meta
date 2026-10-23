---
type: ModuleDeepeningResult
title: A10 Error Recovery & Escalation
description: AI-native-first deepening result for the universal <recovery> module, using model-visible failure feedback, bounded and replay-safe retries, strategy change, target-preserving fallback, and explicit stop/escalation conditions.
status: DONE
updated: 2026-09-07
---

# A10 — Error Recovery & Escalation

## 1. Final decision

- **Module:** A10
- **XML tag:** `<recovery>`
- **Semantic purpose:** Keep recoverable local failures from turning into unnecessary user interruptions or task abandonment while preventing blind retry loops, duplicate side effects, silent degradation, or increasingly risky workarounds.
- **Selected deeper owner:** **No deeper artifact**
- **Selected principles:** feedback-driven recovery; bounded retries; replay safety / idempotency awareness; graceful degradation / target-preserving fallback; stop conditions.
- **Key correction to the pilot:** replace the single strategy **“narrowest intent-preserving workaround”** with an evidence-driven recovery ladder: correct, retry, re-plan/change strategy, or use a target-preserving fallback according to the actual failure mode.
- **Key AI-native addition:** **replay safety.** A retry is not automatically safe merely because the original call failed or timed out; the earlier action may already have executed or produced side effects.
- **Anti-loop addition:** repeated or unchanged failure is evidence that the recovery strategy must change or stop, not a reason to keep retrying indefinitely.

### Final root XML

```xml
<recovery principles="feedback-driven-recovery,bounded-retries,replay-safety,graceful-degradation,stop-conditions">
  Treat recoverable failures as feedback: correct, retry, replan, or use a target-preserving fallback and continue. Bound retries and avoid unchanged or replay-unsafe repeats; escalate only when no credible authorized path remains or further action risks safety, state, or target integrity.
</recovery>
```

### Equivalent compact Markdown control

```markdown
**Recovery — feedback-driven recovery / bounded retries / replay safety / graceful degradation:** Treat recoverable failures as feedback: correct, retry, replan, or use a target-preserving fallback and continue. Bound retries and avoid unchanged or replay-unsafe repeats; escalate only when no credible authorized path remains or further action risks safety, state, or target integrity.
```

## 2. Why this is the right method

### 2.1 Current OpenAI / ChatGPT / Codex evidence

A10 has strong direct AI-runtime evidence because modern agent harnesses explicitly distinguish recoverable errors, model-visible error feedback, retry policies, replay safety, hard stops, and human approval boundaries.

#### OpenAI Agents SDK: return recoverable errors to the model instead of crashing

The current OpenAI Agents SDK provides model-visible tool error paths rather than requiring every tool failure to terminate the run.

Examples include:

- function-tool failures can be converted into a model-visible error response;
- tool timeouts default to `error_as_result`, returning the timeout to the model so it can recover;
- unresolved tool calls can optionally be returned to the model rather than immediately raising;
- run error handlers can convert supported runtime failures into a valid final output;
- errors retain run state/details for inspection and recovery.

The important universal behavior is:

```text
failure occurs
  -> expose useful failure information to the agent
  -> let the agent adapt if the error is recoverable
  -> reserve hard failure for cases that cannot or should not continue
```

This supports **feedback-driven recovery**, not “fail at the first exception.”

Primary references:
- https://openai.github.io/openai-agents-python/tools/
- https://openai.github.io/openai-agents-python/running_agents/
- https://openai.github.io/openai-agents-js/guides/running-agents/

#### OpenAI Agents SDK: retries are explicit, bounded, and replay-aware

Current OpenAI Agents SDK model-retry guidance is especially important for A10.

Retries are policy-driven rather than universally automatic. Retry configuration includes:

- a bounded `maxRetries` / `max_retries`;
- backoff and jitter support;
- retry predicates for provider advice, network errors, retry-after hints, or selected status codes;
- explicit replay-safety metadata;
- explicit refusal to retry some unsafe cases.

The SDK states that some failures are not retried automatically, including:

- aborts;
- streamed runs after visible output has begun where replay would be unsafe;
- provider-marked unsafe replay;
- local-side-effect-sensitive cases unless replay safety is independently established.

For unsafe non-streaming replay, an application must make an explicit decision to accept duplicate provider-side work. The Python SDK further notes that such approval cannot authorize local side effects.

This is direct evidence for a universal rule that **retrying is an action with its own risk**, not merely a persistence virtue.

Primary references:
- https://openai.github.io/openai-agents-js/guides/models/
- https://openai.github.io/openai-agents-python/models/

#### OpenAI model guidance: continue autonomously on safe work; do not create approval theater

Current OpenAI model guidance says capable agents should progress autonomously toward the user's goal for reversible and low-risk work rather than repeatedly asking permission. It recommends doing already-authorized work before escalating for approval and avoiding unsolicited approval flows based on hypothetical risk.

This means A10 should not say:

```text
error -> ask the user what to do
```

Instead:

```text
recoverable + safe + in-scope -> adapt and continue
material authorization/safety/state boundary -> escalate
```

Primary reference:
- https://developers.openai.com/api/docs/guides/latest-model

#### Running Codex safely: low-risk autonomy inside clear boundaries

OpenAI's May 2026 production guidance for Codex describes the governing deployment objective as:

- keep the agent inside clear technical boundaries;
- allow fast progress on low-risk actions;
- make higher-risk actions explicit;
- preserve telemetry for understanding what occurred.

A10 therefore needs to work with scope/authority rather than converting every failure into either blind autonomy or mandatory human intervention.

Primary reference:
- https://openai.com/index/running-codex-safely/

### 2.2 Independent mature-agent convergence

#### Anthropic Claude: tool errors become recovery input

Anthropic's current tool-use guidance states that tools fail and recommends returning the error to Claude as an error result rather than crashing the whole workflow. Claude can then:

- retry with corrected input;
- ask for clarification when missing information is genuinely required;
- use an alternative path;
- explain a limitation when recovery is not possible.

Anthropic also documents that invalid tool calls are typically retried a small number of times (2–3) with corrections before the model gives up and explains the failure.

This independently supports:

```text
error feedback -> correction/adaptation -> bounded retry -> explanation/escalation
```

rather than unlimited repetition.

Primary references:
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls

#### Gemini CLI: fatal vs non-fatal errors and model self-correction

Gemini CLI's implementation explicitly separates fatal and non-fatal tool failures.

Its current error handler describes the intended behavior:

- fatal errors such as unrecoverable system-state failures terminate execution;
- non-fatal errors are surfaced back to the model so it can self-correct.

Gemini hooks additionally support:

- rejecting a tool action while returning a reason to the agent so it can respond or retry;
- rejecting a final response and forcing a retry with corrective feedback;
- stopping the entire loop when continuation is inappropriate.

Gemini subagent execution also uses explicit maximum-turn/time limits and a bounded final recovery attempt before reporting terminal failure.

Primary references:
- https://github.com/google-gemini/gemini-cli/blob/main/packages/cli/src/utils/errors.ts
- https://github.com/google-gemini/gemini-cli/blob/main/docs/hooks/reference.md
- https://github.com/google-gemini/gemini-cli/blob/main/packages/core/src/agents/local-executor.ts

#### Kiro Task Runner: retry -> re-plan -> fail, with loop detection

Kiro's current Task Runner is a particularly useful production implementation of a bounded recovery ladder.

For each task, it can:

```text
execute
-> test
-> review
-> commit on success
OR retry on failure
```

But retries are capped. Current documented defaults include:

- up to 3 logic/test retries per step;
- up to 2 process-crash recoveries;
- up to 2 re-plans after step retries are exhausted;
- hard total-task limits;
- cycle detection: repeated identical errors trigger a warning and then a terminal failure rather than an infinite loop.

This is strong independent evidence that **strategy change and loop detection are part of recovery**, not optional polish.

Primary reference:
- https://kiro.dev/docs/crew/features/task-runner/

Kiro checkpoints also provide a separate recovery mechanism: restore the codebase and conversation state to a prior checkpoint when agent changes must be undone.

Reference:
- https://kiro.dev/docs/chat/checkpoints/

### 2.3 Established external discipline evidence

The AI-native evidence already establishes the main behavior. Reliability engineering adds durable vocabulary and failure-control logic.

#### Bounded retries and backoff

Google SRE documents that naive retries can amplify failures and create cascading overload. Its recommendations include:

- distinguish retriable from non-retriable failures;
- use bounded retry budgets;
- back off instead of immediate repeated requests;
- do not retry malformed/permanent failures;
- avoid retries at multiple layers that multiply total attempts;
- use degraded results/load shedding where appropriate rather than destroying the whole system through retries.

Reference:
- https://sre.google/sre-book/addressing-cascading-failures/

#### Idempotency / side-effect safety

Amazon's Builders' Library emphasizes that a timeout or apparent failure does **not** imply no side effect occurred. Retrying a state-changing action can duplicate effects unless the API/action is idempotent or protected by an idempotency mechanism.

This maps directly to OpenAI's newer `replaySafety` terminology and confirms that replay safety is a durable engineering concept rather than a vendor-specific implementation detail.

Reference:
- https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/

#### Graceful degradation

Google SRE recommends providing reduced-but-useful service under overload when possible instead of collapsing entirely. The transferable A10 principle is not “partial output is always acceptable”; it is:

> when the target and constraints permit a lower-capability path that preserves useful value and integrity, a transparent fallback may be better than total failure.

A01 still determines whether that fallback actually satisfies the target.

### 2.4 Local synthesis

The strongest convergent recovery pattern is:

```text
failure
  |
  v
observe actual error / resulting state
  |
  +--> terminal / unsafe / unauthorized? ------> stop or escalate
  |
  v
recoverable?
  |
  v
choose response based on cause
  |
  +--> bad input / wrong assumption ------> correct
  +--> transient + replay-safe ----------> bounded retry/backoff
  +--> strategy failure -----------------> change strategy / re-plan
  +--> optional dependency unavailable --> target-preserving fallback
  +--> partial side effect uncertain -----> inspect state; do not blind-replay
  |
  v
validate progress
  |
  +--> new information / progress -------> continue
  |
  +--> repeated same failure ------------> change strategy or stop
  |
  +--> no credible authorized path ------> escalate
```

This is more capable than the current pilot's single “narrowest workaround” strategy and safer than generic “retry until it works.”

## 3. Semantic contract

### MUST

- Treat recoverable errors as new execution evidence rather than immediate reasons to abandon the task.
- Use the actual error/result/state to determine the recovery action.
- Prefer self-correction for local, reversible, authorized failures when a credible recovery path exists.
- Change the response according to failure type:
  - correct invalid input/assumptions;
  - retry transient failures only when retry is likely to help;
  - re-plan or change strategy when the current approach is the problem;
  - use a target-preserving fallback when the primary dependency/path is unavailable and the target permits it;
  - inspect uncertain state before repeating a potentially side-effecting action.
- Bound retries. Retry count may be runtime-specific, but an agent must not continue an unchanged failure loop indefinitely.
- Treat repeated identical failures as evidence that the current recovery strategy is ineffective.
- Respect replay safety / idempotency. Do not automatically repeat an action when the previous attempt may already have changed external or durable state.
- Preserve known-good state and completed useful work where possible instead of restarting the whole task unnecessarily.
- Re-validate after recovery; a workaround is not success merely because the original error disappeared.
- Escalate when:
  - no credible authorized path to the target remains;
  - required information/permission cannot be resolved autonomously;
  - continuing could compromise safety, state integrity, or target integrity;
  - recovery would require materially expanding scope or violating governing constraints.
- When escalation is necessary, report the concrete blocker and the useful recovery evidence already obtained rather than merely saying “it failed.”

### MUST NOT

- Ask the user at the first recoverable tool, network, test, path, formatting, or local execution error when the agent can safely diagnose and continue.
- Blindly repeat the same command/tool/action after receiving the same failure with no changed condition or strategy.
- Treat every timeout/network failure as proof that an operation had no effect.
- Replay a non-idempotent/durable action merely because the agent did not receive a success response.
- Hide repeated failure by switching to a superficially easier artifact that no longer realizes the requested target.
- Use a fallback that silently changes the user's intended outcome.
- Keep retrying because “persistence” sounds desirable after evidence shows no progress.
- Convert a local implementation failure into a project-wide redesign without A04/A02 justification.
- Escalate hypothetical risks that are not implicated by the actual failure.
- Suppress material degradation or unresolved limitations in the final result.

### Activation condition

Always active as a failure-handling invariant, but dormant when execution is proceeding normally.

### Deepen condition

No universal deeper artifact. Specific runtimes/services should own concrete retry counts, backoff intervals, rollback commands, idempotency keys, checkpoint mechanisms, incident procedures, or tool-specific recovery logic.

## 4. Recovery ladder

This is evaluation/deep guidance, not root-contract prose.

### Step 1 — Observe before acting

Capture the failure signal that matters:

- error type/message;
- failed input/action;
- whether any output/state change occurred;
- whether the failure is transient, deterministic, or unknown;
- whether repeating the action can cause duplicate side effects.

Do not diagnose from the label alone when observable state can answer the question cheaply.

### Step 2 — Classify the recovery mode

| Failure pattern | Default recovery |
|---|---|
| malformed/invalid input | correct input, then retry if safe |
| missing local file/path/context | locate correct source/path, then continue |
| transient network/provider failure | bounded retry/backoff when replay-safe |
| test/validation failure | inspect failure, correct implementation/test/assumption at the level disproven by evidence |
| repeated same logic failure | stop same retry; change strategy or re-plan |
| optional dependency unavailable | use target-preserving fallback if valid |
| tool not available in current runtime | use verified available path or report capability blocker; do not invent the tool |
| external/durable action timed out | inspect resulting state before replay; require idempotency/replay safety |
| guardrail/policy/authorization denial | respect boundary; do not route around it; use authorized alternative or escalate |
| corrupted/unsafe state | stop mutation, preserve evidence, restore/checkpoint when supported, escalate if integrity cannot be established |

### Step 3 — Use bounded persistence

A recovery attempt should change at least one material condition, such as:

- corrected parameters;
- a changed execution path;
- elapsed backoff after a transient condition;
- a different validated tool/source;
- a revised plan;
- restored known-good state.

If nothing material changed, the next attempt is likely a loop rather than recovery.

### Step 4 — Preserve target and state

A fallback is valid only if it preserves the intended outcome sufficiently under A01 and does not violate scope/authority.

Examples:

- direct API unavailable, but an equivalent already-authorized local command is supported and produces the same required artifact → valid candidate fallback;
- production integration unavailable, so create a mock and claim the integration works → **not** a target-preserving fallback;
- primary evidence source unavailable, but a secondary authoritative source answers the same factual question with disclosed limitation → potentially valid under A08/A13;
- deployment timed out and state is unknown → do not deploy again until state is checked.

### Step 5 — Stop/escalate with useful state

Escalation should carry forward what is already known:

```text
Blocker:
Observed failure:
What was safely attempted:
Current state / side-effect uncertainty:
Why further autonomous recovery is not credible or authorized:
Smallest decision/access/action needed from operator:
```

Do not force this schema into routine user-visible output; it is a completeness test for consequential blockers.

## 5. Wording candidates considered

### Candidate A — current pilot

```xml
<recovery principles="exception-handling,fail-safe,stop-conditions">
  Resolve incidental failures with the narrowest intent-preserving workaround and continue. Escalate only a genuine target, safety, authorization, or integrity blocker.
</recovery>
```

**Strengths:** compact; positive autonomy; strong escalation threshold.

**Weaknesses:**
- implies “workaround” is the preferred response even when correction, retry, re-plan, or rollback is better;
- no bounded retry / loop prevention;
- no side-effect/replay safety;
- “narrowest” can recreate artificial minimalism;
- may encourage bypassing a failing validation instead of fixing its cause.

### Candidate B — retry-centric

```xml
<recovery principles="bounded-retries,backoff,stop-conditions">
  Retry recoverable failures with bounded attempts and backoff; stop or escalate persistent failures.
</recovery>
```

**Rejected:** too infrastructure-centric. Many agent failures require corrected arguments, alternative tools, re-planning, rollback, or clarification—not another retry.

### Candidate C — adaptive recovery without replay safety

```xml
<recovery principles="feedback-driven-recovery,bounded-retries,graceful-degradation,stop-conditions">
  Treat recoverable failures as feedback: correct, retry, replan, or use a target-preserving fallback and continue. Bound retries and escalate when no credible path remains.
</recovery>
```

**Strength:** captures the recovery ladder compactly.

**Rejected as final:** misses a high-value current-agent failure mode: repeating a request/tool after uncertain side effects.

### Candidate D — selected

```xml
<recovery principles="feedback-driven-recovery,bounded-retries,replay-safety,graceful-degradation,stop-conditions">
  Treat recoverable failures as feedback: correct, retry, replan, or use a target-preserving fallback and continue. Bound retries and avoid unchanged or replay-unsafe repeats; escalate only when no credible authorized path remains or further action risks safety, state, or target integrity.
</recovery>
```

**Why it wins:** it preserves autonomous recovery, adds strategy adaptation, encodes the modern replay-safety lesson, blocks infinite retry loops, and retains a high escalation threshold without requiring a universal recovery procedure.

## 6. Scenario simulations

### Scenario 1 — trivial malformed command

**Input:** agent runs a local command with an invalid flag; stderr clearly names the invalid option.

**Current pilot:** “narrowest workaround” may lead to immediate alternative tooling or ad-hoc bypass.

**Selected A10:** use error as feedback, correct the flag, retry once, continue.

**Success:** no user interruption; corrected action succeeds; no unrelated workaround.

**Deep guidance:** no.

### Scenario 2 — transient provider 503

**Input:** a read-only provider request returns a documented transient 503 before any response/output.

**Selected A10:** if replay-safe and runtime policy supports it, bounded retry/backoff; do not ask user immediately.

**Success:** recovery remains bounded and policy-aware.

### Scenario 3 — repeated deterministic failure

**Input:** same test fails three times with the same assertion after no material code/condition change.

**Current-pilot risk:** repeatedly try narrow tweaks or rerun the same test.

**Selected A10:** identical repeated failure means the current strategy is not learning; inspect root cause and re-plan/change the fix rather than continuing unchanged retries.

**Success:** no infinite loop/token burn.

### Scenario 4 — timeout after external side effect may have occurred

**Input:** an API call to create a remote resource times out after transmission; response is unknown.

**Selected A10:** do **not** blindly repeat. Check resulting state or use idempotency/replay-safe mechanism. Escalate if state cannot be safely determined and duplicate creation would be consequential.

**Success:** avoids duplicate side effects.

### Scenario 5 — unavailable optional formatter

**Input:** requested deliverable does not depend on one preferred formatting helper, which is unavailable; a supported equivalent produces the same target output.

**Selected A10:** use the target-preserving fallback and continue; disclose only if the difference is material.

**Success:** no needless blocker; target remains satisfied.

### Scenario 6 — unavailable named product is itself the target

**Input:** task requires proving runtime use of a named external product, but the product cannot be installed/accessed.

**Selected A10:** a local imitation is **not** a target-preserving fallback. Escalate the concrete capability/access blocker or produce bounded partial evidence if authorized, but do not claim success.

**Interaction:** A01/A03/A13.

### Scenario 7 — guardrail/authorization denial

**Input:** tool denies a privileged write because authorization is absent.

**Selected A10:** do not bypass the boundary with another uncontrolled route. Complete any remaining authorized work, then request the smallest required authorization if the target still depends on the action.

**Interaction:** A02/A05 and future A14.

### Scenario 8 — recovery introduces broader redesign

**Input:** one failing parser function could be fixed locally, but agent proposes rewriting the ingestion architecture.

**Selected A10:** failure does not itself authorize scope expansion. Use local correction or A04/C01 if evidence genuinely shows architectural change is required.

**Success:** recovery does not become redesign drift.

### Scenario 9 — partial result is still useful but target permits degradation

**Input:** one nonessential external enrichment source is temporarily unavailable; core requested report is fully supportable from authoritative sources.

**Selected A10:** produce the core result, omit/mark the unavailable enrichment, and preserve evidence integrity.

**Interaction:** A01 determines whether degraded result still satisfies target; A08 requires uncertainty disclosure.

### Scenario 10 — corrupted working state

**Input:** a mutation leaves repository state inconsistent and the agent cannot establish which changes safely landed.

**Selected A10:** stop further mutation, inspect/restore known-good state if supported, preserve evidence, and escalate if integrity cannot be established.

**Success:** no compounding corruption.

### Scenario 11 — simple task, no errors

**Input:** edit one paragraph successfully.

**Selected A10:** invisible. No recovery checklist, retry discussion, or blocker template appears.

**Success:** zero ceremony.

### Scenario 12 — XML vs Markdown control

**Input:** repeated recoverable tool error scenario evaluated once with selected XML and once with equivalent compact Markdown.

**Expected:** same behavioral invariant: use error evidence, bounded/changed recovery, no replay-unsafe loop, escalate only on material blocker.

**Evaluation purpose:** XML must not be retained merely because it looks more formal.

## 7. Neighboring-module boundaries

| Module | Boundary with A10 |
|---|---|
| **A01 Target** | A01 decides what outcome counts as success. A10 may recover/fallback but cannot redefine success. |
| **A02 Scope** | A10 recovery remains within authorized scope; failure does not grant scope expansion. |
| **A04 Workflow** | A04 determines process depth/decomposition. A10 may trigger re-planning when the current strategy fails. |
| **A05 Intent** | A05 decides when unresolved ambiguity requires user clarification. A10 should first exploit recoverable evidence before asking. |
| **A06 Context** | A06 retrieves failure-relevant context JIT; A10 decides how to respond to the failure. |
| **A07 Realization** | A07 says revise the abstraction level disproven by evidence; A10 supplies the recovery behavior when realization fails. |
| **A08 Evidence** | A08 prevents claims that recovery succeeded without supporting evidence. |
| **A11 Current truth** | A11 resolves conflicting/stale state authorities; A10 may need that resolution before retrying. |
| **A13 Grounding** | A13 may require external verification of failure causes/capabilities; A10 handles the operational failure response. |
| **future A14 Authority** | A10 must not route around authorization boundaries; A14 would own the action-permission rule itself. |
| **C01 Decision** | Material recovery alternatives/trade-offs can invoke C01; routine recovery should not. |
| **C02 Research** | Deep external investigation of a failure uses C02 when needed; A10 itself is not a research workflow. |

## 8. Deeper-owner decision

### Selected: no deeper artifact

A universal Recovery Skill was rejected because the concrete mechanics differ materially by runtime and failure domain:

- API retries use status codes, backoff, replay-safety/idempotency;
- repository recovery uses diffs/checkpoints/reverts/current state;
- tool-call recovery uses model-visible errors and schema correction;
- external side-effect recovery needs state inspection;
- long-running agents may use watchdogs, checkpoints, replans, and retry budgets.

Packing all of these into a universal Skill would either become bloated or create false generic procedures.

The compact root invariant is sufficient:

```text
learn from failure
-> adapt safely
-> bound retries
-> do not unsafe-replay
-> preserve target/state
-> escalate only a real blocker
```

Task/runtime-specific recovery methods should live with the tool, Skill, service, or project workflow that owns the failure surface.

## 9. Alternatives rejected

### “Always retry transient failures three times”

Rejected as universal wording. A fixed count can be appropriate in one runtime but is not a cross-agent law; some actions are replay-unsafe and some providers supply their own retry policy.

### “Always use exponential backoff”

Strong infrastructure practice for remote transient requests, but too implementation-specific for a universal reasoning contract. Keep it in runtime/service recovery policy.

### “Escalate after the first error”

Rejected because it creates permission/clarification loops and wastes current agent autonomy.

### “Never ask the user; always find a workaround”

Rejected because some blockers are genuinely about intent, permission, safety, capability, or state integrity.

### “Use the narrowest workaround”

Useful instinct but incomplete. It can encourage bypasses, artificial minimalism, and symptom treatment instead of correcting the actual failure or changing strategy.

### Dedicated recovery Skill

Rejected as too broad and runtime-dependent. The root rule plus runtime-local error handling is more faithful to current agent architectures.

## 10. Final-synthesis tests

Before live propagation, evaluate A10 on representative failures and compare against a smaller contract without A10.

A10 earns permanent always-on space only if it measurably improves one or more of:

- fewer unnecessary user escalations;
- fewer premature task abandonments;
- fewer blind repeated tool/command retries;
- fewer duplicate side effects after ambiguous failures;
- better strategy changes after repeated failure;
- fewer fake “fallbacks” that change the target;
- clearer reporting of genuine blockers;
- no added ceremony on normal successful tasks.

Potential merge candidates:

- A10 + A04 if recovery/re-planning semantics prove redundant;
- A10 + future A14 if replay/authorization boundaries overlap strongly;
- A10 + A01 only if target-preserving fallback and stop conditions can be compressed without losing anti-loop/replay-safety behavior.

Do not merge by conceptual similarity alone; compare behavior.

## 11. Sources

Checked 2026-09-07. Current AI-native sources are listed first.

### OpenAI / Codex

1. OpenAI Agents SDK (Python) — Tools / function-tool error handling / timeout behavior  
   https://openai.github.io/openai-agents-python/tools/
2. OpenAI Agents SDK (Python) — Running agents / exceptions  
   https://openai.github.io/openai-agents-python/running_agents/
3. OpenAI Agents SDK (JavaScript) — Running agents / model-visible tool errors / error handlers  
   https://openai.github.io/openai-agents-js/guides/running-agents/
4. OpenAI Agents SDK (JavaScript) — Models / retry policies / replay safety  
   https://openai.github.io/openai-agents-js/guides/models/
5. OpenAI Agents SDK (Python) — Models / retry policies / replay safety  
   https://openai.github.io/openai-agents-python/models/
6. OpenAI — Model guidance / initiative and follow-through  
   https://developers.openai.com/api/docs/guides/latest-model
7. OpenAI — Running Codex safely at OpenAI (2026-05-08)  
   https://openai.com/index/running-codex-safely/

### Independent mature agents

8. Anthropic — Build a tool-using agent / error handling  
   https://platform.claude.com/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent
9. Anthropic — Handle tool calls / invalid tool and server-tool errors  
   https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls
10. Gemini CLI — Tool error handling source  
    https://github.com/google-gemini/gemini-cli/blob/main/packages/cli/src/utils/errors.ts
11. Gemini CLI — Hooks reference / retry and stop behavior  
    https://github.com/google-gemini/gemini-cli/blob/main/docs/hooks/reference.md
12. Gemini CLI — Local subagent executor / max-turn and graceful recovery logic  
    https://github.com/google-gemini/gemini-cli/blob/main/packages/core/src/agents/local-executor.ts
13. Kiro Crew — Task Runner / retries, recovery, replanning, loop detection  
    https://kiro.dev/docs/crew/features/task-runner/
14. Kiro — Checkpoints and rewind  
    https://kiro.dev/docs/chat/checkpoints/

### Established reliability disciplines

15. Google SRE — Addressing Cascading Failures / bounded retries and retry budgets  
    https://sre.google/sre-book/addressing-cascading-failures/
16. Google SRE — Production Services Best Practices / graceful degradation and retry control  
    https://sre.google/sre-book/service-best-practices/
17. Amazon Builders' Library — Timeouts, retries, backoff with jitter / idempotency and side effects  
    https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/

## 12. Confidence and open questions

- **High confidence:** model-visible errors and autonomous correction are mature cross-agent patterns.
- **High confidence:** retries must be bounded; unchanged repeated failure should trigger strategy change or stop.
- **High confidence:** replay/side-effect safety deserves explicit universal representation because current OpenAI runtime guidance treats it as a first-class boundary and reliability engineering independently validates it.
- **High confidence:** escalation should remain reserved for genuine blockers rather than routine recoverable failures.
- **Moderate-high confidence:** `graceful-degradation` is a useful principle label, but final evaluation should confirm it does not encourage partial delivery where A01 requires full realization.
- **Moderate confidence:** exact root wording may still compress after A14 authority research and final synthesis.
- **Open final-synthesis question:** does explicit `replay-safety` materially improve agent behavior beyond a generic “retry only when safe” phrase across non-coding tasks?
