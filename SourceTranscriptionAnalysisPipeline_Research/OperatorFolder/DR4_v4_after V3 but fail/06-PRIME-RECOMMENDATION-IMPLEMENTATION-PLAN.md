# Transcript-to-Knowledge — Prime Recommendation Implementation Plan

**Status:** READY FOR CLI IMPLEMENTATION  
**Date:** 2026-08-19  
**Repository:** `leela-spec/apexai-os-meta`  
**Branch:** `main` only  
**Executor:** Antigravity CLI directly  
**Optional relay:** OpenClaw only after/when it is already working; it must never block product implementation

## 0. Decision lock

Architecture selection is complete. Do **not** execute the old V3 discovery chain (`M00`–`M05`) before implementation and do **not** reopen candidate research unless a reversal trigger below is hit by real execution.

Selected production path:

```text
URL / local media / existing transcript
        |
        v
[yt-dlp for remote acquisition]
        |
        v
[FFmpeg only when normalization is actually required]
        |
        +--> trustworthy existing transcript ------------------+
        |                                                       |
        +--> ElevenLabs Scribe v2 ------------------------------+
              ASR + word times + speaker IDs                   |
                                                                v
                                                   canonical source package
                                                   source text + timing map
                                                                |
                                                                v
                                                   LangExtract 1.6.0
                                                   targeted multi-pass
                                                   exact source grounding
                                                                |
                                                                v
                                                   grounded evidence units
                                                                |
                                                                v
                                                   Gemini 3.7 Flash
                                                   full-source global synthesis
                                                                |
                                                                v
                                                   source-support gate
                                                                |
                                    +---------------------------+-------------------+
                                    |                                               |
                                    v                                               v
                              source knowledge                         optional external truth check
                                                                          Gemini + Search grounding
                                    |                                               |
                                    +---------------------------+-------------------+
                                                                v
                                                   deterministic compiler
                                                                |
                                                                v
                                           knowledge.md + knowledge.json
                                           evidence.jsonl + source.json
```

Conditional branch: for video where slides/charts/code/demonstrations contain material knowledge absent from speech, add a Gemini 3.7 Flash visual-evidence pass. Do not enable it by default.

### Prime component decisions

| Responsibility | Prime choice | Rule |
|---|---|---|
| Remote acquisition | `yt-dlp` | Reuse; do not replace. |
| Media normalization | FFmpeg | Run only when the next component cannot consume the source directly. |
| Existing transcript | Use it as source | Do not re-ASR a trustworthy transcript for architectural uniformity. |
| Hosted ASR | ElevenLabs Scribe v2 | Default when transcription is needed. |
| Hosted ASR fallback | Deepgram Nova-3 Multilingual | Use only after a real Scribe quality/operational failure. |
| Local ASR fallback | faster-whisper | Use when locality/privacy requires it or hosted ASR is unavailable. |
| Alignment/diarization | Scribe native | Do not add WhisperX unless a demonstrated gap remains. |
| Canonical custody | Thin deterministic adapter | Own only stable text/segment/time/hash mapping. |
| Long-source segmentation | LangExtract | No custom chunker. |
| Grounded extraction | LangExtract 1.6.0 + Gemini-family model | Multi-pass; exact source spans. |
| Global synthesis | Gemini 3.7 Flash | Full source when it fits; no recursive summary cascade by default. |
| Source support | Deterministic span checks + bounded semantic review | Keep exact evidence, semantic support, and external truth separate. |
| External verification | Gemini Search grounding | Optional and separate; never rewrite what the source said. |
| Final compilation | Tiny deterministic compiler | No semantic generation in compiler. |
| Recovery | Immutable stage outputs + tiny manifest | No workflow engine. |
| Product baseline | NotebookLM | Comparison baseline, not production dependency. |
| Delivery | Files first | Agent/OpenClaw skill only after CLI product works. |

## 1. Operating rules for the CLI AI

These rules outrank implementation elegance.

1. **TARGET dominates everything.** Optimize for the efficient, resilient, credible path to a useful source-grounded knowledge artifact.
2. **Reuse before build.** Before writing a new abstraction, actually inspect/try the existing repo implementation or selected external component that could own the responsibility.
3. **Product before infrastructure.** Until the first real vertical slice works, fix only execution blockers, product corruption, experiment invalidation, or material safety/data-loss risk.
4. **Two-strike rule.** Two corrective iterations on the same subsystem without product advancement => stop. Do not perform correction #3. Prefer configuration, replacement, or deletion.
5. **No sunk-cost reasoning.** Existing V1/V2/V2.1/V3 code gets no authority because it already exists.
6. **Every work unit must advance the product.** A unit must run something real, teach us something material about product quality, or move directly toward the target.
7. **Evidence proportionality.** Deterministic checks for deterministic claims; bounded human/source review for semantic quality. Do not build an evaluation platform.
8. **Stop on drift.** If work becomes mainly orchestration, schemas, provenance, wrappers, receipts, or test infrastructure, stop and return to the shortest product path.
9. **Minimalism.** Do only what the active work package requires. Do not add hypothetical guardrails, new frameworks, or extra abstractions.

### Executor and transport

Use **Antigravity CLI directly** for implementation. Do not make OpenClaw relay work a prerequisite. OpenClaw may later invoke the proven CLI mechanically, but implementing or repairing OpenClaw does not advance this product until the production CLI exists.

### Git

- Work directly on `main`.
- Start every work package with `git status -sb` and `git pull --ff-only origin main`.
- Do not create a branch unless the operator explicitly changes policy.
- Commit only accepted, product-advancing work.
- One work package may use multiple local iterations; it does not need one commit per micro-step.

### Context discipline

One work package = one fresh CLI AI context.

At the start of a package, read only:

1. `SourceTranscriptionAnalysisPipeline_Research/00-CURRENT-AUTHORITY.md`;
2. this implementation plan;
3. `SourceTranscriptionAnalysisPipeline_Research/v3-proven-infrastructure/CURRENT-WORK.md`;
4. files explicitly named by the active package;
5. current official docs for the component being integrated, when required.

Do not preload V1/V2/V2.1 history or the old V3 discovery modules.

## 2. Production surface: keep it deliberately small

The first production implementation should have **one user-facing Python CLI entrypoint**, not a new framework.

Preferred initial location:

```text
scripts/transcript_knowledge_prod/
  ttk_prod.py
  prompts/
    extraction.md
    synthesis.md
    support-review.md
  schemas/
    synthesis.schema.json
```

Start with one Python file for deterministic glue. Split it only when real implementation friction makes that simpler.

Do not extend `scripts/transcript_pipeline_v2/` into the production runner: that directory is a historical benchmark/adapter harness with obsolete semantic transport assumptions.

The existing `.claude/skills/transcript-to-knowledge/` implementation is a **reuse candidate**, not the new lifecycle authority. Reuse deterministic parsing/custody/hash/validation/compiler functions only when they directly fit the selected contract. Do not preserve its custom Map/Reduce lifecycle merely because it exists.

### One-command target

```powershell
py -3 scripts/transcript_knowledge_prod/ttk_prod.py run <URL-or-file-or-transcript> --output <job-dir>
```

Optional second command after the first vertical slice:

```powershell
py -3 scripts/transcript_knowledge_prod/ttk_prod.py status <job-dir>
```

Do not add a command family unless a real operator need appears.

### Required final artifacts

```text
<job>/
  manifest.json
  source/
    source.json
    source.txt
    transcript.json
    media-info.json          # when media/URL input exists
  evidence/
    evidence.jsonl
    extraction-review.html   # when LangExtract can produce it cheaply
    visual-evidence.json     # conditional
  synthesis/
    synthesis.json
    support-review.json
    external-verification.json  # conditional
  output/
    knowledge.json
    knowledge.md
```

The Markdown is the human product. JSON is the machine contract. No additional artifact is mandatory before a real need exists.

## 3. Work package P00 — Preflight + ruthless reuse audit

### Goal

Prove the selected external seams can execute and determine exactly which existing deterministic repo pieces are worth reusing. Do not implement the pipeline yet.

### Inspect

Only these existing code areas first:

```text
.claude/skills/transcript-to-knowledge/scripts/ttk.py
.claude/skills/transcript-to-knowledge/scripts/ttk_base.py
.claude/skills/transcript-to-knowledge/scripts/ttk_*.py
scripts/transcript_pipeline_v2/
```

### Actions

1. Confirm repo = `leela-spec/apexai-os-meta`, branch = `main`.
2. Confirm Python >= 3.10.
3. Confirm `yt-dlp`, `ffmpeg`, and `ffprobe` availability; install only if the active test needs them.
4. Confirm required credentials are available without printing them:
   - `ELEVENLABS_API_KEY`;
   - `GEMINI_API_KEY`.
5. In an isolated Python environment, install the selected libraries using their documented paths. Pin `langextract==1.6.0`; use the current official ElevenLabs and Google GenAI SDKs compatible with it.
6. Run a tiny Scribe v2 transcription probe on real short audio.
7. Run a tiny Gemini 3.7 Flash structured-output probe. If the model itself is not available through the current supported Gemini API, do **not** silently substitute the global synthesis model; stop with `BLOCKED_MODEL_AVAILABILITY` for bounded re-verification.
8. Run a tiny LangExtract grounded extraction on known text.
9. Specifically test LangExtract 1.6.0 with `gemini-3.7-flash`.
10. If only the LangExtract-to-3.7 pairing fails, use LangExtract's currently supported Gemini provider/model for extraction and keep Gemini 3.7 Flash for global synthesis. **Do not fork LangExtract.**
11. Audit existing TTK code against only three possible reuse roles:
    - transcript parsing/canonicalization;
    - hashing/segment/timestamp custody;
    - deterministic compilation/validation.
12. For each role, record `REUSE`, `LIGHT_ADAPT`, or `DO_NOT_REUSE` with one-sentence observed reason.

### Acceptance

P00 passes when all three selected semantic/provider boundaries can execute in a trivial real call (or the pre-authorized LangExtract model fallback is proven) and the reuse decision is concrete enough to start the vertical slice.

### Stop / replacement rule

- A credential/configuration error is not architecture evidence.
- Two failed corrections on the same integration seam without a successful call => `APPROACH_SUSPECT`; use the report's pre-authorized fallback rather than building a wrapper framework.

### Commit

Commit only the minimal dependency/configuration files and a short `P00` result if they are needed to reproduce the next package. Do not commit API keys or throwaway probe output.

## 4. Work package P01 — First real vertical slice: existing transcript -> useful knowledge

### Goal

Produce the first complete user-facing `knowledge.md` **before** adding acquisition, ASR orchestration, visual understanding, external verification, or elaborate recovery.

### Input

Use a real existing transcript from the target corpus if trustworthy. Prefer the German finance source when a usable transcript exists; otherwise use the compact technical English source already in the benchmark corpus.

### Implement only this path

```text
existing transcript
  -> canonical source package
  -> LangExtract multi-pass grounded evidence
  -> Gemini 3.7 Flash full-source synthesis
  -> deterministic compile
  -> knowledge.md + knowledge.json + evidence.jsonl + source.json
```

### Canonical source contract

Own only the fields needed downstream:

```yaml
source_id:
input_type:
source_uri_or_path:
source_sha256:
transcript_provider:
language:
segments:
  - segment_id:
    text:
    char_start:
    char_end:
    start_time: null_or_seconds
    end_time: null_or_seconds
    speaker: null_or_string
```

`source.txt` is immutable canonical evidence. Build it deterministically. Character offsets are against this exact file.

### LangExtract extraction

Do not create a custom chunker. Let LangExtract own chunking, parallelism, and repeated passes.

Use targeted high-recall passes for the semantic classes that matter to the product:

- thesis / central positions;
- factual/source claims and important numbers;
- mechanisms / causal explanations;
- procedures / actions;
- arguments / reasons;
- examples that explain an idea;
- qualifications / exceptions / caveats;
- corrections;
- contradictions / disagreements;
- uncertainty;
- predictions / opinions;
- definitions;
- entity relationships where actually useful.

Every grounded source unit must resolve to exact source text. Preserve LangExtract's native source position data rather than copying evidence through a new representation unless the final contract requires it.

### Gemini synthesis

Give Gemini 3.7 Flash:

1. the complete canonical source when it fits;
2. all grounded evidence units;
3. the final synthesis schema/instructions.

Require:

- global thesis and useful hierarchy;
- preservation of corrections/disagreements;
- preservation of caveats and uncertainty;
- no prediction/opinion -> fact conversion;
- evidence-unit references for substantive source assertions;
- a `missing_evidence_requests` field instead of unsupported invention.

Do not use search grounding in this source-only synthesis call.

### Compiler

Compiler may only render validated structured data. It may not generate or rewrite semantic content.

`knowledge.md` must be readable without JSON and include, when present in the source:

- central thesis/positions;
- major claims;
- mechanisms;
- procedures/actions;
- arguments/reasons;
- material examples;
- qualifications/exceptions;
- corrections/contradictions;
- uncertainty;
- predictions/opinions;
- source evidence references.

### Product inspection

Inspect the actual Markdown against the source, not just schema validity.

P01 passes only if the artifact is recognizably source-specific, useful to read, and materially richer than a generic summary.

### Forbidden in P01

- Scribe integration;
- yt-dlp integration;
- OpenClaw integration;
- visual branch;
- external truth verification;
- resume engine;
- DeepEval framework;
- vector DB / RAG / graph DB;
- new Map/Reduce framework;
- large test suite.

## 5. Work package P02 — Source-support gate + targeted repair

### Goal

Make the already-working artifact trustworthy without building a verification platform.

### Implement the three-way distinction

```text
EXACT EVIDENCE EXISTS
    !=
FINAL WORDING IS SEMANTICALLY SUPPORTED
    !=
CLAIM IS TRUE IN THE EXTERNAL WORLD
```

### Deterministic checks

For every evidence link:

- source ID exists;
- character interval is valid;
- exact text resolves to canonical `source.txt`;
- referenced evidence unit exists.

### Semantic support review

Run Gemini only for final normalized/synthesized claims whose wording goes beyond verbatim evidence.

Allowed result:

- `supported`;
- `partially_supported`;
- `unsupported`;
- `ambiguous`.

Major `unsupported` items do not remain as source-grounded final claims.

### Targeted repair queue

If synthesis identifies an important idea with missing/weak evidence, rerun a **targeted LangExtract pass for that idea only**, then rerun only affected synthesis/support work.

Do not rerun the whole raw-source extraction merely because one item needs repair.

### Acceptance

- zero unresolved unsupported major source-grounded claims;
- no invalid evidence intervals;
- corrections, contradictions, uncertainty, predictions and opinions remain correctly typed in a bounded manual inspection.

## 6. Work package P03 — Add real media input with Scribe v2

### Goal

Extend the proven semantic product to audio/video without changing the semantic architecture.

### Path

```text
local audio/video
  -> Scribe v2
  -> canonical source package
  -> existing P01/P02 semantic path
```

### Rules

1. Preserve the raw Scribe provider response before flattening.
2. Use word timestamps and speaker IDs when returned.
3. Generate `source.txt` deterministically from the persisted transcript representation.
4. Map each canonical segment to character bounds.
5. Map LangExtract evidence spans back to intersecting words/segments to derive time ranges.
6. Do not fuzzy-match evidence text to timestamps if deterministic segment/word overlap is available.
7. Keyterm prompting is conditional: use it only when a representative sample shows domain-name/term errors worth fixing.
8. Do not add WhisperX unless native Scribe timing/diarization demonstrably fails a product need.

### First ASR inspection

On the first representative EN and DE runs, inspect bounded early/middle/late slices with attention to:

- names;
- technical terms;
- numbers/percentages;
- corrections;
- speaker attribution when meaning depends on speaker.

Do not build a WER benchmark unless existing references make it genuinely useful.

### Fallback

If Scribe has repeated meaning-changing errors after one configuration/keyterm correction, run the same representative slice through **Deepgram Nova-3 Multilingual**. Do not redesign ASR.

Use faster-whisper only for locality/privacy/offline requirements or hosted-service unavailability.

### Acceptance

A real media source produces the same useful final knowledge package, with major evidence links resolving to both transcript text and time where timing is available.

## 7. Work package P04 — Add URL acquisition; FFmpeg only when needed

### Goal

Reach the user-facing one-command path from a supported URL without adding media infrastructure.

### Path

```text
URL
  -> yt-dlp metadata/media
  -> [FFmpeg only if Scribe/input compatibility requires it]
  -> P03
```

### Rules

- Reuse yt-dlp; no downloader abstraction beyond the few arguments the product needs.
- Persist source URL and basic media metadata.
- Preserve a manual/trustworthy transcript if one is supplied; do not replace it with ASR merely because the URL path supports ASR.
- Do not transcode by default.
- A site-specific yt-dlp extractor failure is an acquisition defect, not a reason to redesign the pipeline.

### Acceptance

The one user-facing command accepts one primary benchmark URL and produces the final artifact without manual file surgery.

## 8. Work package P05 — Add the smallest useful resumability

### Goal

Prevent expensive successful stages from rerunning after ordinary failures.

Add this **only now**, after the real path exists.

### Manifest scope

One `manifest.json` containing, per stage:

```yaml
stage:
status:
input_hash:
config_hash:
component_or_model:
version_if_observable:
output_paths:
completed_at:
error: null_or_short_string
```

### Skip rule

A stage may be reused only when its input/config hashes and expected outputs still match.

### No workflow engine

Do not add DocETL, Temporal, Airflow, a database, queue, daemon, or agent state machine for this responsibility.

### Required test

Interrupt one semantic stage on a real run and confirm rerunning the same command reuses completed acquisition/ASR/source artifacts and resumes from the first stale/failed stage.

## 9. Work package P06 — Conditional visual evidence

### Run only if

At least one real target video contains material knowledge in slides, charts, code, demonstrations, or other visuals that the transcript does not contain.

If not demonstrated, mark P06 `SKIPPED_NOT_NEEDED` and do no implementation.

### Implementation

Use Gemini 3.7 Flash directly on the relevant video/source portions to emit timestamped visual observations. Keep visual evidence separate from transcript evidence and label model inference explicitly.

Feed retained visual evidence into synthesis/support review; do not invent a second knowledge pipeline.

### Acceptance

A known visual-only fact/relationship from the chosen source appears in the final artifact with a resolvable time reference and is not mislabeled as spoken transcript evidence.

## 10. Work package P07 — Optional external factual verification

### Default

**Defer until the source-grounded product already passes.** This is not required to prove what the source said.

### Run only when

The operator/product requires external truth status for selected factual claims.

### Implementation

Use Gemini 3.7 Flash with Search grounding on selected factual claims only. Store the result separately:

```yaml
source_claim:
epistemic_status:
source_support:
external_verification:
  status: corroborated|contradicted|mixed|unverifiable
  explanation:
  evidence:
```

Never overwrite `source_claim` because the world check disagrees.

### Acceptance

External verification can be removed entirely without changing the source-grounded artifact's meaning or provenance.

## 11. Work package P08 — Three-source product proof + NotebookLM baseline

### Goal

Decide whether the selected production path actually deserves production status.

### Required sources

Use the current V3 primary corpus:

1. `P-h5WSQG1Sw` — long English science/interview;
2. `CygwqaNg2PY` — English technical finance;
3. `vFTuLylvYnA` — German finance.

Use the existing-transcript branch for one additional run only when needed to prove that input mode independently; do not grow the corpus casually.

### Before reading generated artifacts

Create a bounded must-find set of roughly 20–30 consequential items per long source only if that much source knowledge is genuinely present. Include representative:

- thesis/position;
- number;
- mechanism;
- procedure/action;
- argument;
- example;
- caveat;
- uncertainty;
- prediction/opinion;
- correction/disagreement when present.

This is a product review aid, not a benchmark platform.

### Inspect three dimensions

**Knowledge value**

- important material retained;
- mechanisms/procedures/reasons/examples survive;
- organization is useful rather than transcript dump or generic summary.

**Trust**

- every major source-grounded assertion resolves to evidence;
- unsupported synthesis is absent/labeled;
- prediction/opinion/fact status remains correct;
- corrections/disagreements are not flattened away.

**Operations**

- fresh run uses the intended source;
- failures are visible;
- rerun/resume does not require manual surgery;
- output is usable without the originating AI conversation.

### NotebookLM comparison

For the first two long sources, run the same source/transcript through NotebookLM as a whole-product reference baseline.

The production composition must at least hold its own on substantive recall/usefulness while winning the required automation + evidence-contract use case. If it is materially worse as a knowledge product, the pipeline has failed even if its schemas/tests pass.

### Release gate

Fail on any critical:

- unsupported major final claim;
- opinion/prediction converted to fact;
- missed correction/contradiction that changes meaning;
- unresolved major evidence reference;
- cross-source contamination;
- generic/source-interchangeable artifact;
- unusable German output.

A directional weighted-recall score may be recorded, but it must not override a catastrophic semantic failure.

## 12. Reversal triggers — architecture research is allowed only here

Reopen **only the affected decision**, and only after real execution proves one of these:

1. Scribe repeatedly causes meaning-changing EN/DE errors and the pre-authorized Deepgram fallback also fails.
2. LangExtract cannot reach acceptable important-unit recall or reliable grounding after documented configuration/multi-pass use.
3. Gemini 3.7 global synthesis repeatedly drops major corrections/contradictions/uncertainty or produces unsupported major conclusions despite the support gate.
4. A hosted component violates actual privacy/data-residency requirements and no pre-authorized alternative satisfies them.
5. Measured per-source cost materially violates the approved operating budget.
6. Windows deployment fails through documented installation paths plus one bounded workaround.
7. The implementation genuinely requires a large new workflow/orchestration subsystem instead of the thin glue described here.
8. Final artifacts are materially worse than NotebookLM on substantive knowledge quality.

Do **not** reopen architecture because of:

- a renamed API parameter;
- one downloader breakage;
- one malformed model response;
- a Python packaging issue;
- a Windows path bug;
- a single failed extraction pass;
- old TTK code not fitting the new contract.

## 13. Two-strike mechanics for the CLI AI

For each work package, keep the strike counter conceptually local to the subsystem being repaired.

```text
attempt 1 fails
  -> diagnose
  -> smallest documented/configuration repair

attempt 2 fails without advancing the product
  -> STOP
  -> do not repair again
  -> use selected fallback / simplify / emit APPROACH_SUSPECT
```

A strike is **not** every ordinary command error. It is a corrective iteration on the same approach that still fails to advance the product.

## 14. Definition of implementation complete

Implementation is complete only when one command can turn a real supported URL/media/transcript into a durable package where:

- `knowledge.md` is genuinely useful and source-specific;
- important claims, mechanisms, procedures, reasons, caveats, corrections, contradictions and uncertainty are retained when present;
- every major source-grounded item has resolvable evidence;
- time references resolve when the source provides timing;
- source support and external truth are distinct;
- EN and DE work on the real corpus;
- an interrupted run resumes without redoing successful expensive stages;
- no custom ASR, diarizer, chunker, semantic extraction framework, RAG system, workflow engine, benchmark platform or agent framework was invented.

## 15. Immediate next action

Start **P00 only** in a fresh Antigravity CLI context.

Bootstrap instruction:

> Work on `leela-spec/apexai-os-meta`, `main` only. Read `SourceTranscriptionAnalysisPipeline_Research/00-CURRENT-AUTHORITY.md`, `SourceTranscriptionAnalysisPipeline_Research/v3-proven-infrastructure/06-PRIME-RECOMMENDATION-IMPLEMENTATION-PLAN.md`, and `SourceTranscriptionAnalysisPipeline_Research/v3-proven-infrastructure/CURRENT-WORK.md`. Execute only the active work package. Reuse existing code before writing new code. Do not execute the old V3 M00-M05 discovery chain. Apply the two-strike rule. Commit accepted product-advancing work directly to `main`; otherwise stop with the concrete blocker or `APPROACH_SUSPECT`.
