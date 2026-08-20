# Scenario Simulations

**Status:** CURRENT SCENARIO SET  
**Date:** 2026-08-20

These scenarios are used to test what actually changes product quality, reliability, cost, locality, and implementation complexity. They are not architecture decisions.

## S1 — Fully local / simple controller

```text
Python runner
  -> yt-dlp/FFmpeg
  -> local ASR
  -> LangExtract + local Qwen
  -> local Qwen synthesis
  -> deterministic compile
```

**Strengths:** no recurring API dependency; private/local; low external operational risk.  
**Unknowns:** Qwen extraction quality, global synthesis quality, long-context feasibility, runtime.  
**Key test:** can this meet product quality without external semantic calls?

## S2 — Fully local / durable workflow

```text
LangGraph
  -> local acquisition/ASR
  -> LangExtract + local Qwen
  -> local synthesis
  -> validation/compile
```

**Difference from S1:** workflow state/checkpoints/fallbacks are owned by LangGraph rather than custom/minimal Python state.

**Key test:** does LangGraph materially improve recovery/reliability or mostly add framework overhead?

## S3 — Local extraction + strong external synthesis

```text
local controller
  -> local ASR
  -> LangExtract + local Qwen
  -> strong external/subscription synthesis
  -> deterministic compile
```

**Hypothesis:** narrow grounded extraction may be feasible locally while final long-context synthesis benefits materially from a stronger model.

**Key test:** does the external model produce a large enough synthesis gain to justify dependency while most semantic volume remains local?

## S4 — Native cloud semantic path

```text
controller
  -> transcript
  -> LangExtract + supported cloud provider
  -> strong long-context cloud synthesis
  -> deterministic compile
```

**Strengths:** low custom semantic integration burden; likely strong quality ceiling.  
**Costs/risks:** paid API, credentials, cloud dependency, privacy considerations.

**Role:** quality/reliability challenger, not assumed production default.

## S5 — Subscription CLI semantic worker

```text
controller
  -> transcript/evidence packet
  -> Claude/Codex/Antigravity CLI
  -> result validation
  -> compile
```

**Operator position:** autonomy is allowed, including `Q5=C`, but repeated real attempts have been unreliable. Avoid this path unless it demonstrates substantial value and can use a reliable execution pattern.

**Key test:** can bounded or autonomous CLI execution run repeatedly without hangs, permission/input ambiguity, state loss, or improvised architecture?

## S6 — Autonomous CLI owns broad pipeline execution

```text
operator/controller launches agent
  -> agent decides/executes multiple semantic and mechanical steps
  -> agent repairs failures
  -> final artifact
```

**Potential value:** maximum reuse of subscription-agent intelligence and reduced hand-coded orchestration.  
**Observed risk:** prior project attempts repeatedly failed/drifted.  
**Promotion bar:** exceptionally high. Must outperform deterministic workflow alternatives materially and demonstrate repeatable execution. Permission to consider this is not a recommendation.

## S7 — Evidence-light useful artifact

```text
source
  -> transcript
  -> semantic extraction/synthesis
  -> useful artifact
```

No universal exact quote/timestamp requirement.

**Use case:** personal learning, low-stakes knowledge distillation, situations where source traceability is not worth the output/integration burden.

**Question:** how much simpler/better is the artifact when evidence machinery is reduced?

## S8 — Source-grounded artifact

Important factual/technical claims link to source passages/timestamps where practical.

**Use case:** reviewable knowledge, technical research, later source reopening.

**Question:** what grounding level gives useful trust without overwhelming the artifact?

## S9 — Strict high-trust artifact

Claims requiring trust carry exact evidence/time and stronger support checks.

**Use case:** high-consequence research/audit contexts.

**Question:** what incremental quality/trust is gained and what complexity/cost is added? This is explicitly not the default for every source.

## S10 — Full transcript only synthesis

Final semantic model reads the full source and produces the artifact directly.

**Risk:** important details may receive little attention; grounding structure may be weaker.  
**Benefit:** no extraction bottleneck; minimum semantic architecture.

## S11 — Evidence-only synthesis

Extraction creates a compact evidence ledger; synthesis reads only that ledger.

**Benefit:** compact/focused.  
**Risk:** extraction omissions are irreversible at synthesis time.

## S12 — Full transcript + evidence synthesis

Final model sees original source plus extracted evidence.

**Hypothesis:** evidence guides attention while the raw source provides recovery from extraction misses.

**Cost:** more context/tokens.  
**Status:** approved comparison, not approved winner.

## S13 — Existing near-complete product

Run a maintained existing product/system on the representative source with minimal adaptation.

**Question:** can it already meet enough of the target that custom composition is unnecessary or much smaller?

**Decision consequence:** if yes, adopt/fork/lightly adapt rather than continuing component architecture work.

## Scenario scorecard

Every scenario that reaches a real run should record:

| Dimension | Meaning |
|---|---|
| Product usefulness | Can the operator recover the source's valuable content efficiently? |
| Important-insight recall | Does it retain the information that matters? |
| Faithfulness | Does it distort or invent source meaning? |
| Nuance | Does it retain caveats, uncertainty, corrections, disagreements? |
| EN/DE quality | Does it work across required languages? |
| Reliability | Does it complete repeatably without manual surgery? |
| Resume/recovery | Can expensive progress survive failure? |
| Proven-state | Are components/integration paths established or custom hypotheses? |
| Locality/privacy | What leaves the local machine? |
| Recurring cost | API/subscription marginal cost. |
| Runtime | Actual elapsed performance on operator hardware. |
| Integration burden | Custom code/config/dependencies required. |
| Operator reading efficiency | How much effort is required to get the value from output? |

Do not use a composite score to hide a hard product failure. Preserve the underlying dimensions.