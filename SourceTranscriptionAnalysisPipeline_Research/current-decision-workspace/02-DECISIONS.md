# Operator Decisions — Transcript-to-Knowledge Current Workspace

**Status:** CURRENT OPERATOR DECISIONS  
**Date:** 2026-08-20

This file contains decisions actually verified by the operator. Recommendations elsewhere do not override it.

## D01 — Workflow sequencing

**Decision:** AI must not be required to remember or infer ordinary pipeline sequence/state. Deterministic code or a workflow runtime owns normal sequencing, state, retries, and resume.

**Clarification:** this does not prohibit autonomous CLI agents from performing a bounded semantic/implementation job when they provide enough value.

## D02 — External/API use

**Decision:** external API use is allowed only when it demonstrates significant value over local/subscription alternatives. API-first is not the default.

**Required evidence:** same-input comparison where practical; assess quality, reliability, implementation burden, recurring cost, privacy/dependency, and local alternative performance.

## D03 — Local Qwen

**Decision:** local Qwen must be tested separately for grounded extraction and final/global synthesis. Do not infer capability from parameter count or generic benchmarks.

## D04 — Hybrid local/external path

**Decision:** a hybrid is allowed. Example: local extraction can remain if it performs well while a materially stronger external model is used only for synthesis.

## D05 — Subscription CLI autonomy

**Decision:** autonomous subscription CLI agents are allowed (`Q5=C`).

**Constraint:** avoid them by default because repeated prior attempts have been unreliable. Use autonomy only when there is a large enough value gain and a reliable, battle-proven or empirically proven execution pattern. Do not reject CLI autonomy categorically; make it earn its role.

## D06 — Measure before remove

**Decision:** a mature reusable component that plausibly improves product value, reliability, efficiency, evidence quality, or removes fragile custom logic receives a bounded test before rejection.

## D07 — Stage/component count

**Decision:** do not optimize the number of stages as an objective. Merge/remove only when capability/value is not lost or an existing component absorbs the responsibility better.

## D08 — API promotion gate

**Decision:** an API should be compared against the best practical local/subscription option on the same or equivalent fixture before production promotion when that comparison is feasible.

## D09 — Resume after interruption

**Decision:** expensive completed work should be resumable after interruption/crash rather than routinely recomputed.

## D10 — Automatic fallback

**Decision:** automatic fallback paths are desirable where they are explicitly defined and reliable. They must not turn into an AI improvising a new architecture.

## D11 — Paid/external invocation gate

**Decision:** initially require explicit approval before a new paid/external semantic route is adopted or invoked as a production dependency. This can be revisited after measured value/cost is known.

## D12 — Unattended source run

**Decision:** once a run is approved and its policy is fixed, one source should be processable without routine human intervention.

## D13 — Failure stop rule

**Decision:** after two failed corrective iterations on the same semantic/technical approach without measurable product advancement, stop/escalate/replace rather than letting an AI invent repair #3.

## D14 — Concurrency

**Decision:** no requirement for multi-source concurrency is currently locked. Do not choose workflow infrastructure primarily for concurrency until needed.

## D15 — Output representation

**Decision:** Macro/Meso/Micro is **one option**, not a mandatory final output contract.

The output structure should be selected by product usefulness and may incorporate external information/software where useful. Do not constrain the product to Macro/Meso/Micro merely because prior TTK used it.

## D16 — Exact evidence/timestamps

**Decision:** exact claim-to-transcript/timestamp evidence is **configurable by use case**, not mandatory for every output.

Possible modes must remain visible in the matrix, for example:
- evidence-light / usefulness-first;
- source-grounded where claims need verification;
- strict traceability for high-trust use cases.

The architecture must not impose the maximum evidence burden on every run by default without demonstrating value.

## D17 — Non-factual provenance

**Decision:** out of scope for the current project. Preserve as future development only.

## D18 — Source support vs external truth

**Decision:** where either is used, keep them conceptually separate. "The source said X" and "X is externally true" are different questions.

## D19 — Visual-only video evidence

**Decision:** out of scope for the current project. Preserve as a future project; do not add a visual-analysis branch to current production architecture.

## D20 — Global synthesis comparison

**Decision:** provisional YES to testing the comparison, but the operator did not fully understand the original wording. Treat the experiment as approved in principle, not the architecture conclusion.

Plain meaning of the comparison to test:
1. final model receives the complete transcript only;
2. final model receives extracted evidence only;
3. final model receives both complete transcript and extracted evidence.

Purpose: determine whether extraction improves attention/recall without making extraction misses irreversible. No option is preselected by this decision.

## D21 — Qwen Round 4

**Decision:** Q21–Q29 are not operator questions. They are mandatory empirical tests to execute in the research/bake-off phase.

Required Qwen test areas:
- EN LangExtract/schema extraction;
- DE LangExtract/schema extraction;
- uncertainty/correction retention;
- bounded-source synthesis;
- long-source synthesis;
- identical-input comparison with strong external model;
- actual runtime on operator hardware;
- usable context/quantization on operator hardware;
- whether quality is sufficient to remove most external semantic calls.

## Locked anti-inference rules

- Do not equate local with reliable.
- Do not equate external/API with better.
- Do not equate a real component with a proven project integration.
- Do not equate schema PASS with product quality.
- Do not make Macro/Meso/Micro mandatory without a new operator decision.
- Do not make exact timestamp evidence mandatory without use-case justification.
- Do not pull visual evidence or non-factual provenance back into current scope.
- Do not interpret permission for CLI autonomy as a recommendation to use it by default.