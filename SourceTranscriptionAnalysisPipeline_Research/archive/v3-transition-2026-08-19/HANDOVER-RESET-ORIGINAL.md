# HANDOVER — RESET TO PROVEN TRANSCRIPT-TO-KNOWLEDGE INFRASTRUCTURE RESEARCH

**Date:** 2026-08-19  
**Repository:** `leela-spec/apexai-os-meta`  
**Branch policy:** `main` only  
**Status:** `RESET_REQUIRED`  
**Purpose:** Give the next AI a truthful restart point after the current implementation/orchestration attempt failed to deliver a working end-to-end pipeline.

---

# 0. Read this first

The current transcript-pipeline effort has gone in the wrong direction.

The operator's original goal was **not** to spend days inventing and debugging a new orchestration protocol, handoff schema, evidence framework, or bespoke transcript architecture.

The original goal was:

> **Research and reuse already-proven infrastructure from the internet — especially existing open-source projects, transcript-processing tools, benchmark methods, and evaluation frameworks — and use the smallest amount of custom integration necessary to produce a reliable transcript-to-knowledge system.**

The operator explicitly wanted to avoid designing a novel pipeline from scratch when this is a problem that many existing projects and users have already solved in practice.

The present V2.1 attempt did not satisfy that goal. It became a custom staged implementation plus a human-mediated AI orchestration protocol. The result was repeated correction loops over bookkeeping and provenance before even reaching real source acquisition.

**Do not continue that process as the default next step.**

This handover is a reset mandate.

The next AI should first rediscover the real problem, research what already works, run the best existing candidates, and only then decide what — if anything — needs to be built.

---

# 1. Original user goal

The original user goal, stated before the failed V2.1 implementation effort, was to build a **reliable, deterministic transcript-to-knowledge system** by researching and reusing proven infrastructure.

The desired system takes a source such as:

- video;
- audio;
- SRT/VTT;
- transcript JSON;
- plain-text transcript;
- other common transcript formats;

and produces a structured, auditable, source-faithful knowledge artifact.

The desired output should preserve the actual information in the source rather than merely generate a loose summary.

Important desired output properties include:

- chapter-level organization;
- timestamp/source anchors;
- atomic claims;
- procedures and steps;
- warnings and caveats;
- examples;
- decisions and recommendations made in the source;
- important named tools/entities/concepts;
- explicit uncertainty/ambiguity;
- navigable structure/indexes;
- coverage/completeness evidence;
- traceability back to the transcript;
- an independent verifier/evaluator that can compare the produced knowledge artifact against the source transcript.

The knowledge artifact must be **source-faithful**. It must not silently invent facts or silently replace the speaker's meaning with external knowledge.

If external factual verification is later useful, it should be clearly separated from the source-grounded artifact rather than contaminating source fidelity.

The system should eventually support multilingual material. English and German are important benchmark cases already present in this project.

---

# 2. Non-functional priorities from the operator

These priorities are central. Do not trade them away for architectural elegance.

## 2.1 Resilience

The pipeline should work repeatedly on real inputs and fail clearly when it cannot.

A simple proven tool that succeeds reliably is better than a sophisticated architecture with many fragile stages.

## 2.2 Simplicity

Prefer the smallest system that satisfies the real product requirement.

Do not introduce a custom framework merely because it makes the architecture look systematic.

## 2.3 Token efficiency

Large transcripts and supporting context should not repeatedly be pushed through expensive reasoning contexts unnecessarily.

Use deterministic preprocessing, indexing, chunking, file references, retrieval, and other mechanical operations where they genuinely reduce cost/complexity.

Do not use deterministic scripts for semantic judgments they cannot reliably make.

## 2.4 Deterministic scripts where they add real value

Good deterministic responsibilities include examples such as:

- media acquisition;
- format conversion;
- hashing;
- transcript parsing;
- timestamp normalization;
- chunk/window generation;
- schema validation;
- source-reference validation;
- coverage measurement;
- output assembly;
- test execution;
- resume/invalidation when this is proven necessary.

Semantic interpretation should use a component that is actually good at semantic interpretation.

## 2.5 Reuse before invention

Use this preference order:

1. a proven end-to-end project that already solves most of the use case;
2. a maintained proven project with a small adapter/fork;
3. a composition of a few proven components with clear boundaries;
4. custom implementation only for a gap that has been demonstrated by running the existing options.

**Do not jump directly to #4.**

## 2.6 Real evaluation

The operator does not want subjective "looks good" evaluation.

Use real benchmark sources and explicit evaluation methods.

The system should be judged on the actual knowledge product, not on the amount of framework, tests, receipts, or architecture documentation surrounding it.

---

# 3. What the operator was trying to avoid

The operator previously stated that the existing APEX KB approach had been unreliable and effectively never worked well enough.

That was one of the reasons this research effort was started in the first place.

The intent was to look outside the existing implementation and answer:

> **What is already out there that actually works for this use case, and how do those systems do each step?**

The research was supposed to think outside the existing APEX design and evaluate available approaches in detail.

The next AI must therefore resist the temptation to treat the current repository architecture as the answer merely because it already exists.

---

# 4. What happened instead

## 4.1 V1

An earlier custom transcript pipeline implementation was found to be unreliable and was archived under:

`SourceTranscriptionAnalysisPipeline_Research/archive/transcript-pipeline-v1-2026-08-18/`

Known bad behavior in that lineage included semantic heuristics/custom agents being treated as if they were real strong semantic workers, simulated/fake provider paths, reuse of historical artifacts while presenting runs as fresh, and other evidence/product-integrity problems.

The archived V1 material may be useful as failure evidence, but it must **not** be treated as the architecture to revive.

## 4.2 V2/V2.1 research and architecture

The next attempt created a large V2/V2.1 research/bake-off architecture under:

`SourceTranscriptionAnalysisPipeline_Research/v2-reuse-bakeoff/`

Some research in that folder may remain useful as historical evidence about individual components.

However, the implementation strategy became a bespoke fourteen/fifteen-stage orchestration process (`S00` through `S14`) with a separate execution-AI session and orchestrator approval after each stage.

## 4.3 Human became the message bus

The protocol required roughly:

`ChatGPT orchestrator -> operator copy/paste -> CLI execution AI -> operator copy/paste -> ChatGPT review -> repeat`

for every small stage and every repair.

This turned minor implementation defects into multi-agent/human round trips.

## 4.4 S00 consumed repeated repair cycles

The first stage only initialized a run. It did not download audio, transcribe anything, or create knowledge.

Yet it required repeated commits/corrections involving:

- optional-field defaults;
- request serialization;
- repository/branch checks;
- hash newline semantics;
- premature/fabricated PASS recording;
- exact test-command evidence;
- unrelated dirty-path classification;
- repository-wide versus stage-owned `git diff --check` behavior;
- immutable `start_head` provenance;
- re-finalization behavior.

Relevant commit sequence:

- `31cb1db67df9840c20871fa728bfaf3b7fdae68b` — initial V2.1 run initialization;
- `6729342bb81db24ad46cf7813f31589cdecc9344` — evidence/hash/acceptance repair;
- `10a7f8df018eadb3395295aadbe0f283e7f593af` — execution-exact acceptance evidence;
- `580b8e7eab5b11894b088244e55dfb3391ae2c17` — diff-check ownership classification;
- `ae83ac0f99b679e877fce39613cc1d739d638c27` — immutable start-head provenance repair.

The final S00 run is:

`artifacts/transcript_pipeline_v2/runs/ttk_20260819_095347_CygwqaNg2PY_069f8a/`

This reached an internally accepted S00 state, but that should **not** be mistaken for meaningful pipeline progress.

At this point in the failed orchestration attempt:

- no fresh source audio had been acquired by V2.1;
- no V2.1 ASR had run;
- no canonical transcript had been produced;
- no semantic extraction had run;
- no Map/Reduce product had been produced;
- no final knowledge artifact existed;
- no end-to-end V2.1 pipeline had been demonstrated.

The operator reports losing roughly another 1.5 days to this process without getting the pipeline finished.

That operational outcome is itself important evidence: **the process is not acceptable.**

---

# 5. Why the current approach is considered failed

The issue is not merely that some code had bugs.

The approach failed at the workflow/design level.

## 5.1 It optimized bookkeeping before product proof

Large effort went into proving initialization metadata while the central product — source -> transcript -> useful knowledge — had not yet been demonstrated.

## 5.2 Too many semantic rules were encoded in prompts

Things such as PASS semantics, ownership, provenance, exact evidence, and stage boundaries repeatedly depended on an AI correctly interpreting long instructions.

Where possible, such invariants should instead be mechanically enforced by a small test/validator, or omitted until they are actually needed.

## 5.3 Every repair required an external round trip

The execution AI was prevented from simply performing normal software-development iteration inside one bounded task.

Instead of:

`implement -> test -> debug -> repair -> rerun`

inside one session, the system repeatedly did:

`implement -> push -> human transfer -> review -> human transfer -> repair -> push -> ...`

## 5.4 The architecture became the project

The actual goal was a working transcript-to-knowledge pipeline.

The project drifted toward building an orchestration/evidence architecture around a pipeline that still did not exist end to end.

## 5.5 It ignored the original reuse-first intent

Most importantly, the original request was to research existing proven solutions before building a new system.

The next AI must correct this error at the root rather than continue polishing the custom V2.1 pipeline.

---

# 6. RESET DECISION — what NOT to do next

The next AI must **not** begin by executing `S01`.

Do not treat the existing `S00 -> S14` module sequence as the required next implementation path.

Do not begin another correction cycle on the current handoff/evidence machinery.

Do not build a new downloader abstraction, semantic orchestration framework, state framework, receipt framework, resume engine, evidence ledger, agent router, or custom knowledge framework before researching existing alternatives.

Do not spend the next session choosing between ChatGPT/OpenClaw/Codex orchestration topologies before proving the underlying transcript-to-knowledge product.

Orchestration is secondary. The pipeline/product comes first.

Do not assume the answer must reuse the current `scripts/transcript_pipeline_v2/` implementation.

Do not assume a solution is good merely because it has already consumed implementation effort.

Treat sunk cost as sunk cost.

---

# 7. New mission for the next AI

## Mission

**Find the best already-proven existing infrastructure for this transcript-to-knowledge use case, verify it with real evidence, run the strongest candidates, and recommend the smallest reliable architecture built primarily from those proven systems.**

This is a research-and-bake-off task first.

It is **not** an implementation-from-scratch task.

---

# 8. Research order

Research from the outside in.

## Phase A — find complete or near-complete systems first

Search broadly across the current internet and GitHub for maintained systems that already perform substantial parts of:

`video/audio -> transcript -> structured notes/knowledge -> source-grounded artifact`

Relevant search spaces include, but are not limited to:

- YouTube/video-to-notes projects;
- podcast-to-notes/knowledge projects;
- lecture/transcript knowledge extraction projects;
- meeting/transcript knowledge-base systems;
- transcript-to-Markdown/wiki systems;
- transcript ingestion pipelines for RAG/knowledge bases;
- source-grounded summarization/extraction systems;
- knowledge-graph/document extraction systems where transcript provenance is preserved;
- mature ingestion frameworks with transcript/audio loaders and structured extraction;
- open-source research assistants with auditable source references;
- existing transcript-processing skills/tools that can be run locally or through a simple CLI.

Do not narrow the search prematurely to components already selected in V2.1.

The correct answer may be an existing project we have not considered at all.

## Phase B — only then inspect proven components

If no near-complete system meets the requirement, identify the smallest composition of proven components needed for:

1. source acquisition;
2. transcription/diarization/alignment where required;
3. transcript normalization/chunking;
4. semantic extraction/synthesis;
5. provenance/grounding;
6. final knowledge artifact generation;
7. coverage/factuality/source-faithfulness evaluation.

Again: prefer components with demonstrated real-world use over speculative architectural fit.

## Phase C — identify evaluation infrastructure

Search specifically for existing evaluation approaches/frameworks for:

- transcript summarization coverage;
- factual consistency/faithfulness;
- information extraction completeness;
- citation/source grounding;
- long-document summarization;
- structured extraction quality;
- ASR quality where relevant;
- regression testing of generated knowledge artifacts.

Do not invent a large bespoke evaluation framework until existing benchmark methods have been investigated.

---

# 9. Evidence required for every serious candidate

Do not produce a list of names based on search snippets.

For every shortlisted project/component, collect evidence such as:

- canonical repository/project URL;
- what exact problem it solves;
- whether it is maintained now;
- release/version activity;
- contributor/activity signals;
- adoption/community signals where meaningful;
- documentation quality;
- installation path;
- supported operating systems;
- Windows viability where relevant to this project;
- required hardware;
- supported input types;
- supported languages;
- actual output format;
- source/timestamp/citation support;
- test suite;
- example outputs;
- real issue history/failure modes;
- dependency burden;
- licensing;
- local versus hosted execution;
- API-key/provider dependencies;
- token/cost implications;
- whether semantic model choice can be swapped;
- how much custom glue would be required;
- whether it can resume/retry without complexity;
- whether it has actually been used end to end by others.

GitHub stars alone are not proof.

A project with a reproducible working example is stronger evidence than a project with an impressive README but no runnable path.

---

# 10. Mandatory real bake-off before architecture design

The next AI must not stop at literature/repository research.

After identifying the strongest candidates, run the most promising options on real material wherever feasible.

Use the existing benchmark corpus in this repository rather than inventing a new benchmark unless there is a strong reason.

At minimum, test candidates against representative English and German material once the candidate set is narrow enough.

The current first vertical-slice source was:

`https://www.youtube.com/watch?v=CygwqaNg2PY`

but do not let historical artifacts for that source contaminate a claimed fresh run.

For each runnable candidate, preserve:

- exact version/commit;
- actual command/config;
- runtime/install blockers;
- produced transcript/knowledge artifact;
- enough evidence to compare quality;
- concrete failure modes.

A candidate that cannot be made to run should be recorded as blocked/failed — not silently replaced by a custom implementation.

---

# 11. Product-first evaluation

The primary question is:

> **Did this produce a trustworthy, useful, source-specific knowledge artifact from the real source?**

Evaluation should prioritize:

1. source faithfulness;
2. coverage/completeness;
3. preservation of important procedures, claims, warnings, examples, decisions, and caveats;
4. timestamp/source traceability;
5. structure/navigability;
6. explicit ambiguity/uncertainty;
7. resistance to hallucination/contamination;
8. multilingual behavior;
9. reproducibility/resilience;
10. simplicity/maintenance burden;
11. token/runtime/cost efficiency.

Do not award a system points merely for producing more receipts, schemas, stages, or tests.

Those are means, not the product.

---

# 12. Reuse decision rule

After real research and bake-off, choose the architecture by this rule:

### Option 1 — adopt an existing end-to-end project

Choose this if one project already satisfies most of the product requirement and can be adapted lightly.

### Option 2 — fork/extend one proven project

Choose this if one strong project is close and the missing behavior is small and well-defined.

### Option 3 — compose a small number of proven components

Choose this if no single project is sufficient but a simple 2-4 component pipeline clearly works.

### Option 4 — custom implementation

Use this only for gaps demonstrated by the bake-off.

Every custom component must answer:

> What existing solution was tested, what exactly failed, and why is this custom code the smallest justified repair?

If that cannot be answered, do not build it.

---

# 13. What may still be useful from the current repository

The current repository is still valuable as:

- a record of failed approaches;
- a benchmark corpus;
- previous evaluation observations;
- prior research leads;
- a source of explicit user requirements;
- a source of anti-patterns to avoid.

Useful historical areas may include:

- `SourceTranscriptionAnalysisPipeline_Research/HANDOVER_MULTI_PIPELINE_EVALUATION.md`
- `SourceTranscriptionAnalysisPipeline_Research/PROCESS_STEP_COMPARISON_MATRIX.md`
- `SourceTranscriptionAnalysisPipeline_Research/POST_REPAIR_EVALUATION_REPORT.md`
- `SourceTranscriptionAnalysisPipeline_Research/v2-reuse-bakeoff/`
- `SourceTranscriptionAnalysisPipeline_Research/archive/transcript-pipeline-v1-2026-08-18/`
- existing benchmark artifacts under `artifacts/`

But use these as **historical input**, not as unquestioned architecture authority.

The next AI should explicitly distinguish:

- requirements worth preserving;
- evidence worth preserving;
- implementation ideas worth retesting;
- machinery that existed only because the failed custom architecture needed it.

---

# 14. Anti-patterns the next AI must avoid

## Do not over-engineer before first real success

A first useful vertical slice should be allowed to be simple.

## Do not make every pipeline step an AI handoff

Normal software iteration belongs inside one execution workflow.

## Do not invent fake semantic substitutes

Heuristics, templates, or internal agents must not masquerade as a strong semantic model.

## Do not simulate freshness

Historical audio/transcripts cannot be copied and called a fresh run.

## Do not equate schema correctness with product correctness

A perfectly valid JSON/YAML handoff around a poor knowledge artifact is still failure.

## Do not optimize provenance bookkeeping beyond its product value

Hashing and provenance are useful where they protect reproducibility, but they must not consume more engineering effort than the actual source-to-knowledge product.

## Do not let tests prove only the wrapper

Tests should establish that the actual user-facing pipeline works.

## Do not keep repairing a failing architecture because it is already built

Re-evaluate from existing proven systems.

---

# 15. Required next-AI deliverables — BEFORE implementation

The next AI should first produce a research decision package, not code.

At minimum:

## A. Problem restatement

A concise source-to-product definition independent of current V2.1 internals.

## B. Landscape map

A broad set of credible existing projects/frameworks/tools grouped by how much of the end-to-end problem they already solve.

Aim for enough breadth to avoid local-search bias; approximately 10-20 credible candidates is reasonable if the ecosystem supports it.

## C. Evidence-backed shortlist

Select the strongest 3-5 candidate architectures/projects based on evidence, not preference.

## D. Real bake-off plan and execution

Run the most promising candidates/components on representative source material.

Do not merely propose that someone else should test them later.

## E. Comparison matrix

Compare at least:

- real product quality;
- source fidelity;
- coverage;
- timestamp/provenance support;
- multilingual behavior;
- installation/runtime reliability;
- Windows compatibility where relevant;
- complexity;
- token/cost efficiency;
- customization required;
- maintenance risk;
- license/community maturity.

## F. Recommendation

Recommend one primary path and one fallback.

The recommendation must identify exactly what is reused unchanged, what is configured, what is adapted, and what genuinely must be custom.

## G. Operator decisions

Only after the evidence is assembled, surface a short list of decisions that genuinely require operator preference/authority.

Do not ask the operator to decide technical questions that the research can answer objectively.

---

# 16. Implementation only after the research gate

Do not resume implementation until the research package answers:

1. What existing systems were found?
2. Which were actually run?
3. Which produced the best real knowledge artifact?
4. Which failed, and why?
5. What exact gap remains that existing infrastructure does not solve?
6. What is the smallest integration needed?

Only then should implementation begin.

When implementation does begin, prefer a normal software-development loop:

`implement -> run -> inspect product -> test -> repair -> rerun`

inside one bounded executor workflow.

Do not require operator copy/paste between two AIs for every small failure.

Independent review can happen at meaningful product checkpoints rather than after every internal step.

---

# 17. Orchestration is deliberately deferred

There was a later discussion about three orchestration options:

1. repair the current human-mediated ChatGPT <-> CLI pattern;
2. use OpenClaw as a control-plane/middleman;
3. let Codex own more of the implementation workflow.

Do **not** make choosing or implementing that orchestration the next project.

First prove the transcript-to-knowledge pipeline using existing infrastructure.

Once a working pipeline exists, automation/orchestration can be selected based on a real workload instead of being designed in the abstract.

---

# 18. Current repository state at this handover

At the time this reset handover was authored, the latest observed `main` commit before the handover itself was:

`ae83ac0f99b679e877fce39613cc1d739d638c27`

with message:

`fix(transcript): preserve immutable S00 start-head provenance`

That commit should be understood as the endpoint of the failed S00 orchestration loop, not as evidence that the end-to-end transcript pipeline works.

No V2.1 S01 acquisition had been accepted/executed as part of this orchestration attempt at the time of reset.

---

# 19. Definition of success for the restart

The restart succeeds when we can point to a real source and say:

1. a proven/reused system acquired or consumed the source;
2. a real transcript was produced/loaded;
3. the system created a high-value structured knowledge artifact;
4. the artifact can be traced back to source timestamps/text;
5. important source information is demonstrably retained;
6. hallucination/source contamination is controlled;
7. the process can be rerun without fragile manual surgery;
8. the architecture is materially simpler because it reused existing work;
9. benchmark evidence justifies the selected system;
10. custom code exists only where proven existing infrastructure left a real gap.

A successful orchestration framework without this product is not success.

A successful S00/S01/Sxx handoff without this product is not success.

A large research document without actually running the shortlisted systems is not success.

---

# 20. Immediate instruction to the next AI

**STOP implementing the current custom pipeline.**

Start with current web/GitHub research.

Find what people already use successfully for this exact or adjacent use case.

Investigate complete solutions first.

Verify claims against primary repositories/documentation and real runnable evidence.

Run the strongest candidates.

Compare their actual outputs.

Then recommend the simplest proven path.

The operator wanted a working transcript-to-knowledge pipeline, not another architecture project.
