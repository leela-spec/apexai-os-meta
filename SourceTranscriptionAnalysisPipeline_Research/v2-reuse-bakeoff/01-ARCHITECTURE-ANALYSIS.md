---
title: "Transcript→Knowledge V2 — Reuse Architecture Analysis"
doc_type: architecture_analysis
created: 2026-08-18
status: benchmark_driven_candidate_architecture
machine_plan: 02-IMPLEMENTATION-PLAN.yaml
benchmark_spec: 03-BENCHMARK-AND-TEST-SPEC.yaml
component_registry: 04-COMPONENT-REGISTRY.yaml
---

# 1. Executive architecture decision

The V2 target is **not** a single pre-selected pipeline and **not** a dependency pile.

It is a controlled architecture bake-off around one trustworthy spine:

```text
APEX/OpenClaw trigger
  -> source acquisition
  -> ASR reference + challenger
  -> optional alignment/diarization
  -> TTK canonical custody / windows / hashes
  -> Map extraction paths benchmarked on identical packets
  -> deterministic TTK validation
  -> local advisory support checks
  -> Reduce orchestration paths benchmarked on identical evidence ledgers
  -> selective factual external verification
  -> TTK compiler
  -> benchmark + regression suite
  -> evidence-based component promotion
```

The design law is:

> **Use code for exact operations; use specialized reusable models/software for narrow solved problems; use strong general AI only for irreducible semantic reasoning; keep a component only if measured value justifies its complexity.**

This directly corrects two prior failure modes:

1. **Over-invention:** building custom semantic, extraction, evaluation, alignment, or orchestration logic where mature software already exists.
2. **Over-correction:** removing mature reusable candidates merely to make a diagram look simpler before testing whether they solve real quality/cost/reliability problems.

# 2. Product target by layer

| Layer | Valuable outcome | Non-goal |
|---|---|---|
| Source acquisition | reproducible audio/video + metadata | custom downloader framework |
| ASR | words/timestamps/confidence good enough that downstream knowledge is trustworthy | ASR speed as an isolated vanity metric |
| Alignment/speakers | reliable `who said what/when` only where the source requires it | mandatory diarization for single-speaker media |
| Custody | immutable source identity, stable segments, packet hashes, resume | generic RAG storage |
| Map | high-recall reusable semantic evidence cards | sentence dumping or forced quotas |
| Grounding | factual claims trace to exact source evidence | quote existence mistaken for semantic support |
| Reduce | useful global thesis, real semantic modules, refined claims | fixed time buckets / generic chapter templates |
| External verification | research only consequential factual claims | verifying every sentence |
| Compilation | stable machine representation + useful human view | UI-first architecture |
| Benchmark | select architecture from evidence, not taste | one-off subjective review |

# 3. Hardware / operating envelope

Target machine:

```yaml
os: Windows 11 Home
cpu: Intel Core Ultra 7 258V
cores: 8
ram_gb: 31.63
gpu: Intel Arc 140V integrated
gpu_opencl_reported_memory_gb: 16.5
```

Implications:

- CPU-first local tools such as GLiNER2 are realistic candidates.
- Heavy CUDA-only assumptions are invalid; every local model/runtime must have an actual Windows/Intel execution path.
- Shared-memory iGPU behavior must be measured locally.
- Multiple large Torch/ASR environments should be isolated to avoid dependency collisions and simultaneous memory pressure.
- Qwen is not needed for this pipeline; deterministic scripts or OpenClaw dispatch the workflow.

# 4. Full stage/options matrix

## S0 — Trigger / orchestration

| Option | Value | Cost/risk | Lane | V2 action |
|---|---|---|---|---|
| Existing APEX/OpenClaw dispatch | already selected orchestration plane; can launch local commands/CLI AIs | depends on existing runtime state | **Core** | integrate only after standalone pipeline works |
| Local PowerShell/Python runner | simplest reproducible runner, easy test/resume | small custom adapter | **Core implementation seam** | build thin runner over TTK state |
| Qwen dispatcher | unnecessary AI in a deterministic control role | known reliability limits; adds context/failure surface | Reject for this pipeline | do not implement |
| Prefect/Dagster/Temporal | mature orchestration | new service/state model duplicates current TTK needs | Future only | add only if concurrency/file-state limitations are observed |

**First iteration:** thin deterministic runner, later invoked by APEX/OpenClaw.

---

## S1 — Source acquisition

| Option | Value | Cost/risk | Lane | V2 action |
|---|---|---|---|---|
| Existing P1 downloader + yt-dlp/ffmpeg | mature, already working | low | **Core** | retain |
| Direct browser download | useful for blocked sources | brittle/manual | Fallback | only when normal extractor fails |
| Transcript-only source | cheap | loses acoustic evidence and ASR benchmarking | Input mode | support, but not benchmark substitute |

**First iteration:** retain existing acquisition path; do not rewrite.

---

## S2 — ASR

| Option | Strength | Weakness | Lane | Test |
|---|---|---|---|---|
| faster-whisper base/small/medium/large-v3 | existing stack; word timestamps; probabilities; VAD; hotwords; diagnostics | current `base` artifacts show domain-name errors | **Primary reference** | benchmark at least base/small/medium on gold slices |
| NVIDIA Parakeet TDT 0.6B v3 | 600M multilingual model; official model supports EN/DE and word/segment timestamps | heavier NeMo/Transformers stack; Windows Intel viability must be proven | **Challenger** | install isolated, run same slices |
| OpenVINO GenAI Whisper | Intel-local runtime, relevant hardware fit | separate model/runtime conversion complexity | Challenger if speed is a problem | test after quality selection |
| WhisperX transcription backend | faster-whisper plus downstream alignment | extra dependencies; not needed solely for ASR | Conditional | use for speaker/alignment test |
| whisper.cpp | mature local runtime | Windows Intel acceleration path may need tuning | Secondary challenger | only if existing engines fail needs |
| Hosted ASR / Voxtral-style API | potentially strong quality; low install burden | cost/privacy/network | Post-Trial-1 oracle/escalation | do not run in Trial 1; retain as a documented later option only |

**Official/primary evidence:**
- faster-whisper: https://github.com/SYSTRAN/faster-whisper
- Parakeet: https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3
- OpenVINO GenAI: https://github.com/openvinotoolkit/openvino.genai

**First iteration:** do not select by intuition. Produce an ASR scorecard and promote the smallest/fastest local engine/config clearing the quality gate.

---

## S3 — Alignment and diarization

| Option | Value | Cost/risk | Lane | V2 action |
|---|---|---|---|---|
| faster-whisper timestamps only | zero extra stage | may be insufficient for speaker-level provenance | Primary default | use for single-speaker or if speaker attribution does not matter |
| WhisperX alignment | forced alignment and word timestamps; language-specific aligners include English/German | Torch/models/install overhead | **Conditional** | benchmark on Huberman/Adolphs |
| WhisperX + pyannote diarization | maps words/segments to speaker IDs | diarization is probabilistic; overlap/identity naming still imperfect; HF model access may be needed | **Conditional** | enable only for multi-speaker sources where value is demonstrated |
| Custom diarization/alignment | none | reinvents solved problem | Reject | never first choice |

Primary evidence: https://github.com/m-bain/whisperX

**Promotion rule:** make WhisperX conditional production dependency only if speaker/timestamp evaluation demonstrates a meaningful provenance gain.

---

## S4 — Canonical evidence custody

| Option | Value | Cost/risk | Lane | V2 action |
|---|---|---|---|---|
| Existing TTK | transcript-specific source SHA, stable segment IDs, context-only halo, packet hashes, stale detection, compile lineage | current importer may need richer word evidence | **Core** | retain and extend only where benchmark exposes a gap |
| LangExtract source locations | precise char-span grounding inside extraction workflow | LLM-dependent; not a full custody/state system | Challenger capability | map spans back into TTK, do not replace TTK custody initially |
| Database/vector store | query/retrieval features | new state/infra; not needed for compilation trust | Deferred | no V2 production dependency |

**First iteration:** TTK remains canonical custody authority.

---

## S5 — Processing windows/chunking

| Option | Value | Cost/risk | Lane | V2 action |
|---|---|---|---|---|
| TTK lexical/pause windows + context halo | stable evidence IDs and explicit core/context boundary | may split semantically awkwardly | **Primary** | retain as common benchmark input |
| LangExtract long-doc chunking/multipass | built for high-recall extraction | would change comparison inputs if used indiscriminately | Challenger inside LangExtract lane | test after direct TTK packet reference |
| semchunk / Chonkie | mature generic chunkers | no TTK custody semantics automatically | Secondary | benchmark only if boundary failure is observed |
| DocETL split/gather | integrated LLM ETL flow | duplicates current packet mechanism if used too early | Challenger orchestration | use only in DocETL experiment |

**First iteration:** identical TTK windows are the controlled input for Map route comparisons.

---

## S6 — Cheap local pre-extraction

| Option | Value | Cost/risk | Lane | V2 action |
|---|---|---|---|---|
| none | no dependency or bias | strong AI spends tokens on entities/basic structure | Reference | benchmark |
| **GLiNER2** | 205M CPU-first local extraction/classification/entities/relations; no API required | may add noisy hints or English/German variance | **Primary challenger** | install and compare direct-CLI vs GLiNER2-assisted Map |
| NuExtract 2.x | schema-driven multilingual extraction; verbatim fields | larger model/runtime burden | Secondary challenger | run only if GLiNER2 misses the role |
| regex/heuristics | cheap | semantic misclassification already caused failures | Reject as authority | may be used only for deterministic formatting, never semantic truth |

Primary evidence: https://github.com/fastino-ai/GLiNER2

**Promotion rule:** GLiNER2 survives only if it materially reduces strong-AI tokens or improves entity/structured recall without harming semantic output.

---

## S7 — Grounded Map extraction

### Route A — direct strong CLI

```text
TTK packet -> Claude/Codex/Antigravity subscription CLI -> TTK Map result -> TTK validator
```

Pros:
- minimal layers;
- Claude and Codex support strict output schema;
- strongest semantic model sees source directly.

Cons:
- source-span mapping still relies on TTK quote/segment contracts;
- custom prompts/retry adapter remain ours.

### Route B — LangExtract + strong worker backend

```text
TTK packet -> LangExtract -> provider plugin -> strong semantic backend -> exact source-located extraction -> TTK translation/validation
```

LangExtract provides:
- exact source locations;
- structured extraction;
- long-document strategies;
- multiple passes;
- provider plugin system.

Primary evidence:
- https://github.com/google/langextract
- https://github.com/google/langextract/blob/main/examples/custom_provider_plugin/README.md

The provider plugin is a supported extension mechanism. A CLI-backed provider is therefore a legitimate experiment rather than a core fork.

### Route C — GLiNER2-assisted direct CLI

```text
TTK packet -> GLiNER2 hints + packet -> strong CLI -> TTK Map result
```

### Route D — NuExtract-assisted

Run only if C does not satisfy the cheap pre-extraction role.

**V2 action:** benchmark A, B and C on the **same representative windows** before production selection.

---

## S8 — Structured output / retry layer

| Option | Value | Cost/risk | Lane | V2 action |
|---|---|---|---|---|
| Claude `--json-schema` | native strict schema, headless JSON | Claude-specific | Primary for Claude lane | use in reference route |
| Codex `--output-schema` | native strict JSON schema | Codex-specific | Challenger/fallback | benchmark or use when Claude lane unavailable |
| Gemini headless JSON | structured wrapper + usage stats | no equivalent strict schema flag documented in current reference; deterministic post-validation needed | Fallback/challenger | support after core route |
| Instructor/Pydantic | provider-agnostic schema/retry | extra adapter layer; may not wrap subscription CLI directly without custom transport | **Conditional challenger** | add only if native schema + TTK retry plumbing becomes duplicated/fragile |

Primary evidence:
- Claude: https://code.claude.com/docs/en/cli-usage
- Codex: https://github.com/openai/codex/blob/main/codex-rs/exec/src/cli.rs
- Gemini: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/headless.md
- Instructor: https://github.com/567-labs/instructor

**Decision:** Instructor is no longer excluded; it has a defined promotion trigger.

---

## S9 — Map deterministic validation

| Option | Value | Lane | V2 action |
|---|---|---|---|
| TTK validator | packet hash, refs, core coverage, quotes, schemas | **Core authority** | retain |
| JSON Schema only | shape only | Supporting | not sufficient |
| LLM self-review | semantic review | Auxiliary | never replace deterministic invariants |
| LangExtract exact source locations | stronger extraction provenance | Challenger signal | translate to TTK refs and validate |

**Key rule:** exact quote/span existence proves provenance, not proposition entailment.

---

## S10 — Source-support advisory checks

| Option | Value | Limitation | Lane | V2 action |
|---|---|---|---|---|
| strong semantic worker judgment | nuanced entailment/context | costs semantic tokens; can still err | **Authority** | required |
| multilingual mDeBERTa NLI | cheap local entailment/neutral/contradiction signal across languages | model is not final semantic authority | **Advisory challenger** | benchmark against gold support pairs |
| Vectara HHEM | local factual-consistency score, useful English comparator | language/generalization limits | **English advisory/eval** | compare on English set |
| quote-exists shortcut | cheap | logically invalid | Reject | never infer `SUPPORTED` from quote existence alone |

Primary evidence:
- mDeBERTa model: https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli
- HHEM: https://huggingface.co/vectara/hallucination_evaluation_model

**Promotion rule:** advisory models may trigger review/retry but must not silently override semantic support without a validated policy.

---

## S11 — Reduce / global synthesis

### Route A — TTK evidence ledger + direct strong CLI Reduce

Strengths:
- compact input;
- preserves TTK lineage;
- minimal orchestration.

### Route B — DocETL Map/Reduce/Gather

DocETL provides:
- map/reduce/filter/split/gather/extract operators;
- parallel orchestration;
- caching;
- automatic optimization capable of rewriting prompts/operations and replacing subtasks with code.

Primary evidence: https://github.com/ucbepic/docetl

Risks:
- generic ETL semantics may duplicate TTK state;
- provider/API integration may be easier than subscription-CLI integration;
- optimizer makes attribution harder if enabled too early.

**Trial 1 experiment:** fixed DocETL pipeline first; optimizer **off** during the initial comparison. Use the same validated Map evidence set where feasible. Any strong-AI call must execute through an allowed locally invoked subscription CLI. If DocETL cannot be connected to Claude Code, Codex, or Antigravity without API-key/pay-as-you-go transport or disproportionate adapter work, mark the DocETL experiment `BLOCKED_FOR_TRIAL1` rather than using an API. Enable optimization only as a second experiment after baseline attribution exists.

**Promotion rule:** DocETL must improve semantic recall/quality or materially reduce custom orchestration/tuning burden enough to justify the dependency/provider route.

---

## S12 — External verification

| Option | Value | Lane | V2 action |
|---|---|---|---|
| Claude Code web tools | same semantic worker, bounded queue | Trial-1 primary candidate | use only through authenticated subscription CLI transport |
| Codex web search | strong alternative | Trial-1 challenger | use only through authenticated ChatGPT-plan CLI transport |
| Antigravity CLI research/tooling if its headless smoke test passes | subscription/account-backed local CLI alternative | Trial-1 challenger | fail closed if current CLI cannot be captured safely/non-interactively |
| OpenClaw/browser subscription AIs | reuses logged-in browser sessions | Post-Trial-1 fallback | retain as later option; do not use in the first trial |
| paid research APIs | direct programmatic interface | Post-Trial-1 optional escalation | do not use in Trial 1; retain documented cost/value option |
| verify everything | maximal research | massive cost/noise | Reject | checkworthy factual claims only |

TTK `make-verify` remains the deterministic routing authority.

---

## S13 — Compilation / operator view

| Option | Role | Lane | V2 action |
|---|---|---|---|
| TTK compiler | canonical machine+wiki output | **Core** | retain |
| Fabric | mature `extract_wisdom`/transcript baseline | **Baseline** | run for operator-quality comparison |
| Open Notebook | existing knowledge/research UX | **Product comparator/downstream view** | test after canonical knowledge is stable |
| yt-distill / transcript digest tools | close external implementation baseline | Baseline | run where installation is straightforward |

Do not let UI selection dictate evidence architecture.

---

## S14 — Evaluation

| Evaluation type | Tool/options | Authority |
|---|---|---|
| exact provenance | TTK deterministic validators | hard gate |
| ASR accuracy | manually labeled difficult slices + deterministic WER/term metrics | hard comparison evidence |
| factual support | human-labeled claim/evidence pairs; NLI/HHEM model scores | human gold is reference; advisory model is comparator |
| semantic faithfulness | targeted human review + DeepEval/G-Eval-style metrics | semantic evidence, not sole hard gate |
| insight recall | gold insight checklist per source/window | primary semantic quality metric |
| operator usefulness | blind/rubric review vs Fabric/Open Notebook/current artifact | product metric |
| token/quota | CLI-reported usage where available | efficiency metric |
| runtime/RAM | measured process data | efficiency/feasibility metric |
| implementation complexity | changed LOC, adapter count, dependency count, recovery surface | decision input |

DeepEval primary source: https://github.com/confident-ai/deepeval

Important current caveat: DeepEval issue history includes multilingual evaluation limitations in some built-in English prompts. Do not blindly use English-only semantic metrics to score the German source; the benchmark spec therefore keeps human/gold and deterministic metrics primary for multilingual comparison.

# 5. Recommended first bake-off architecture

This is the **reference experiment**, not the final production freeze:

```text
source
  -> existing acquisition
  -> faster-whisper reference ASR
  -> optional WhisperX on multi-speaker test
  -> TTK canonical custody/windows
  -> three controlled Map lanes:
       A. direct strong CLI
       B. LangExtract + custom strong-worker provider
       C. GLiNER2-assisted direct strong CLI
  -> TTK deterministic validation
  -> mDeBERTa advisory on factual claim/evidence pairs
  -> HHEM advisory on English subset
  -> two Reduce lanes:
       R1. direct strong CLI Reduce
       R2. fixed DocETL Reduce/orchestration challenger
  -> TTK selective factual verification
  -> TTK compiler
  -> Fabric/Open Notebook/external baselines
  -> benchmark scorecard
```

## Why this is not over-engineering

The candidates are **not all in every run**. Each has one explicit hypothesis:

| Candidate | Hypothesis being tested |
|---|---|
| Parakeet | local ASR can beat faster-whisper on German/domain terms without unacceptable runtime burden |
| WhisperX | speaker/timestamp provenance improves enough on interviews to justify conditional dependency |
| LangExtract | exact source grounding and extraction structure improve Map reliability/recall or eliminate enough custom grounding code |
| GLiNER2 | cheap local pre-extraction reduces strong-AI tokens or improves structured recall |
| NuExtract | only needed if GLiNER2 role fails |
| Instructor | native schema/retry paths prove too provider-specific or fragile |
| mDeBERTa | cheap multilingual support warnings catch real semantic-support mistakes |
| HHEM | adds useful independent English factual-consistency signal |
| DocETL | mature Map/Reduce orchestration improves semantic quality/cost/maintenance over our dispatcher |
| DeepEval | repeatable semantic regression metrics reduce subjective re-review burden |
| Fabric/Open Notebook | our final artifact is actually more useful than simple existing solutions |

A candidate that does not deliver on its hypothesis is rejected with a receipt, not retained for theoretical elegance.

# 6. Promotion / rejection decision algorithm

For every candidate, record:

```yaml
candidate_decision:
  id: component_id
  hypothesis: string
  benchmark_cases: []
  hard_gates:
    install: PASS|FAIL|UNMEASURED
    correctness: PASS|FAIL|UNMEASURED
    provenance: PASS|FAIL|UNMEASURED
  measured_delta:
    insight_recall: number_or_UNMEASURED
    grounding: number_or_UNMEASURED
    factual_support_accuracy: number_or_UNMEASURED
    token_use: number_or_UNMEASURED
    runtime_seconds: number_or_UNMEASURED
    peak_memory: number_or_UNMEASURED
    code_deleted_or_avoided: number_or_UNMEASURED
    maintenance_surface: LOW|MEDIUM|HIGH|UNMEASURED
  verdict: PROMOTE|CONDITIONAL|KEEP_AS_CHALLENGER|REJECT|BLOCKED
  rationale: string
  reversal_trigger: string
```

### Default decision law

- Hard correctness/provenance failure => **REJECT/BLOCKED**, regardless of speed.
- Material quality gain with modest isolated complexity => **PROMOTE/CONDITIONAL**.
- Similar quality but material token/runtime/code reduction => **PROMOTE/CONDITIONAL**.
- Similar quality/cost with more complexity => **REJECT**.
- Unclear due to insufficient sample => **KEEP_AS_CHALLENGER / UNMEASURED**, not fabricated precision.

# 7. First plausible production compositions after evidence

These are examples, not pre-decisions.

### Composition A — grounded extraction wins

```text
faster-whisper or Parakeet
 -> conditional WhisperX
 -> TTK
 -> LangExtract + strong CLI provider
 -> TTK validation
 -> mDeBERTa warning layer
 -> strong CLI Reduce
 -> selective verification
 -> TTK compile
```

### Composition B — cheap pre-extraction wins

```text
chosen ASR
 -> TTK
 -> GLiNER2
 -> strong CLI Map
 -> TTK validation
 -> mDeBERTa/HHEM warnings
 -> strong CLI Reduce
 -> TTK compile
```

### Composition C — mature orchestration wins

```text
chosen ASR
 -> TTK custody
 -> DocETL semantic Map/Reduce using chosen provider
 -> TTK provenance/coverage validation adapter
 -> selective verification
 -> TTK compiler
```

### Composition D — simplest route wins empirically

```text
chosen ASR
 -> TTK
 -> direct strong CLI Map/Reduce
 -> TTK validation
 -> selective verification
 -> TTK compiler
```

Composition D is acceptable **only if it wins or ties the benchmark after complexity is included**. Simplicity is a scored benefit, not a pre-benchmark veto against reusable software.

# 8. Things deliberately not in the current bake-off

- vector databases;
- GraphRAG;
- LlamaIndex/Haystack full RAG architecture;
- a new scheduler/workflow service;
- custom speaker diarization;
- custom forced alignment;
- custom semantic heuristic classifiers as final authority;
- Qwen semantic reasoning;
- a custom UI before output quality is proven.

These can be revisited only with a named observed capability gap.

# 9. External primary-source reference set

```yaml
references:
  faster_whisper: https://github.com/SYSTRAN/faster-whisper
  whisperx: https://github.com/m-bain/whisperX
  parakeet: https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3
  langextract: https://github.com/google/langextract
  langextract_custom_provider: https://github.com/google/langextract/blob/main/examples/custom_provider_plugin/README.md
  gliner2: https://github.com/fastino-ai/GLiNER2
  nuextract: https://huggingface.co/numind/NuExtract-2.0-2B
  docetl: https://github.com/ucbepic/docetl
  instructor: https://github.com/567-labs/instructor
  mdeberta_nli: https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli
  hhem: https://huggingface.co/vectara/hallucination_evaluation_model
  deepeval: https://github.com/confident-ai/deepeval
  fabric: https://github.com/danielmiessler/Fabric
  open_notebook: https://github.com/lfnovo/open-notebook
  claude_headless: https://code.claude.com/docs/en/headless
  claude_cli: https://code.claude.com/docs/en/cli-usage
  codex_cli: https://github.com/openai/codex/blob/main/codex-rs/exec/src/cli.rs
  gemini_headless: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/headless.md
```

# 10. What the implementation plan must prove

The next AI's goal is **not “install packages.”** It must produce enough working evidence to answer:

1. Which ASR configuration should be the first production choice on this exact laptop and source mix?
2. Does WhisperX materially improve speaker/timing provenance enough to be a conditional stage?
3. Does LangExtract improve source-grounded Map extraction enough to justify an adapter?
4. Does GLiNER2 reduce tokens or improve structured recall enough to keep?
5. Is NuExtract worth testing after GLiNER2?
6. Do mDeBERTa/HHEM catch meaningful support/factual-consistency errors?
7. Does DocETL beat or simplify the direct TTK semantic orchestration?
8. Is Instructor actually needed after native CLI schema support and TTK validation are measured?
9. Does the chosen final artifact beat simple Fabric/Open Notebook baselines for operator value?
10. Can the entire selected route resume, validate, and fail closed without chat memory?

The exact tasks and evidence outputs are defined in `02-IMPLEMENTATION-PLAN.yaml` and `03-BENCHMARK-AND-TEST-SPEC.yaml`.
