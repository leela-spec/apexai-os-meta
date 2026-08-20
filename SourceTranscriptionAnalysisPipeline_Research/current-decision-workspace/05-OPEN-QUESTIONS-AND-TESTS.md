# Open Questions and Mandatory Tests

**Status:** CURRENT OPEN WORK  
**Date:** 2026-08-20

This file separates genuine operator decisions from empirical questions. Do not ask the operator questions that can be answered by running a bounded experiment.

## A. Workflow / orchestration

### A1 — Plain Python vs LangGraph

**Question:** do the actual production requirements justify LangGraph over a simple deterministic runner?

**Already known requirements:**
- expensive-stage resume;
- unattended approved source run;
- explicit fallback paths are desirable;
- two-strike stop instead of AI improvisation;
- no current concurrency requirement.

**Test:** implement or simulate the smallest representative workflow in both forms and compare:
- state persistence;
- failure recovery;
- fallback clarity;
- code surface;
- custom state plumbing removed;
- operational complexity.

**Decision rule:** LangGraph wins only if it materially reduces custom recovery/state logic or improves reliability enough to justify the dependency.

### A2 — Autonomous subscription CLI value

**Question:** can Claude/Codex/Antigravity autonomy be made reliable enough to earn a production role?

**Operator decision:** autonomy is permitted, but avoid by default unless value is large.

**Required evidence:** use an existing/battle-proven invocation pattern where possible; measure completion, hangs, permission/input waits, retries, output capture, state recovery, and actual product gain. Do not build a large custom adapter just to prove an agent can be used.

## B. ASR

### B1 — Best practical transcript path

Run representative difficult EN and DE clips through:
1. existing trustworthy transcript if available;
2. faster-whisper current calibrated setup;
3. Parakeet if install/runtime is practical;
4. one strong hosted challenger only if the potential value justifies the external test.

Measure manually:
- names/domain terms;
- numbers/percentages;
- German terms;
- speaker/timestamp utility;
- runtime/reliability;
- integration burden.

Do not select from vendor WER claims alone.

## C. Local Qwen — mandatory tests, not operator questions

### C1 — EN LangExtract extraction

Run local Qwen through LangExtract on four representative English windows using a fixed schema.

Measure:
- required-field completion;
- important insight recall;
- unsupported extraction;
- exact/source-span grounding;
- retries/failures;
- runtime.

### C2 — DE LangExtract extraction

Same test on four difficult German windows.

### C3 — nuance/correction retention

Fixtures must include:
- uncertainty;
- later correction;
- disagreement;
- forecast vs fact;
- causal mechanism.

Check whether Qwen flattens these distinctions.

### C4 — bounded-source synthesis

Use one complete 20–40 minute source. Compare local Qwen output with a strong external reference on the exact same input/contract.

### C5 — long-source synthesis

Use the long interview. Measure omission, coherence, important-insight retention, contradictions, generic boilerplate, runtime, and context failures.

### C6 — external-model delta

Blind-score local Qwen vs strong external model on identical fixtures. Determine which semantic jobs actually show a material quality gap.

### C7 — actual hardware runtime

Record:
- exact Qwen model/revision;
- runtime stack (Ollama/llama.cpp/etc.);
- quantization;
- context setting;
- RAM/device memory observed;
- tokens/sec or elapsed time;
- failure/stability state.

The known machine is Windows 11, Intel Core Ultra 7 258V, ~31.6 GB RAM, Intel Arc 140V integrated GPU. Do not infer performance from generic hardware tables.

### C8 — context/quantization envelope

Determine the largest context/quantization combination that remains operationally useful and stable on this machine.

### C9 — local semantic coverage decision

From C1–C8, decide which jobs can be local:
- extraction;
- support review;
- bounded synthesis;
- global synthesis.

Do not turn one result into a blanket "Qwen works/doesn't work" conclusion.

## D. LangExtract

### D1 — Local vs external provider comparison

Same transcript packets, same schema, same examples:
- LangExtract + local Qwen/Ollama;
- LangExtract + one strong supported external provider.

Measure model delta while keeping framework/process constant.

### D2 — LangExtract native long-doc vs TTK windows

Run the same source through:
- LangExtract's native long-document process;
- pre-windowed TTK transport into LangExtract.

Measure boundary loss, insight recall, runtime, duplicate/merge behavior, and implementation burden.

### D3 — custom CLI provider only if justified

Before building a Claude/Codex/Antigravity LangExtract adapter, search for a maintained existing provider/bridge. If none exists, require explicit evidence that subscription economics/value justify custom glue over local or native API provider paths.

## E. Synthesis input strategy — D20 experiment

The operator provisionally approved this comparison but requested clearer meaning.

Use one complete source and the same synthesis model/contract for all lanes:

1. **Full transcript only** — model sees original source text.
2. **Evidence only** — model sees only extracted evidence objects/cards.
3. **Full transcript + evidence** — model sees both.

**What this tests:** whether extraction improves recall/attention enough to help the final product, and whether evidence-only processing loses important material when extraction misses something.

Measure:
- important insight recall;
- false/unsupported claims;
- corrections/uncertainty retained;
- structure/coherence;
- generic boilerplate;
- reading efficiency;
- token/runtime cost.

No lane is preselected.

## F. Output product definition

### F1 — Output representation bake-off

Macro/Meso/Micro is no longer mandatory.

Compare at least 2–3 concrete artifact forms on one source, for example:
- Macro/Meso/Micro knowledge set;
- structured source report/article/wiki;
- compact executive + detailed evidence artifact;
- another near-complete existing system's product form.

The test question is: **which form lets the operator recover the valuable content of the source most effectively for the intended downstream use?**

The exact downstream use still needs to be made concrete through scenarios rather than assumed.

### F2 — Evidence modes

Define and test at least three modes:
- usefulness-first/no strict claim anchors;
- source-grounded important claims;
- strict high-trust quote/timestamp traceability.

Determine incremental value vs complexity/token/output burden. This follows the operator decision that exact evidence is optional by use case.

## G. API/external value threshold

### G1 — Significant value definition

Do not set a purely theoretical numeric threshold yet. Use same-fixture comparisons and record:
- important-insight gain/loss;
- faithfulness;
- nuance/correction handling;
- reliability;
- runtime;
- recurring cost;
- privacy/dependency;
- custom integration eliminated.

Then make the operator decision with actual deltas. Example logic: a tiny quality gain does not justify a major external dependency; a large product-quality or reliability gain may.

## H. Product baselines

Run the strongest practical existing near-complete systems/baselines on the same representative source before freezing custom composition. Candidates already identified include Fabric, Open Notebook, NotebookLM, and any current maintained transcript/video-to-knowledge system found in fresh research.

Purpose: prove our composition adds actual product value rather than merely more machinery.

## I. Deferred / not current questions

Do **not** spend current project effort on:
- visual-only evidence branch;
- non-factual provenance policy.

See `07-FUTURE-DEVELOPMENT.md`.