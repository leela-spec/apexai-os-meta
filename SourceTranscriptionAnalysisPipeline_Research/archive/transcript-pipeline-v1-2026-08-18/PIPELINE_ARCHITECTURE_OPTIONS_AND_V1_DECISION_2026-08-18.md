# Transcript → Knowledge Pipeline — Architecture Options, Decision Matrix, and V1 Recommendation

**Date:** 2026-08-18  
**Status:** decision/implementation input — V1 selected, alternatives retained  
**Repository:** `leela-spec/apexai-os-meta`  
**Target:** a resilient, high-value, resumable audio/video → trustworthy knowledge pipeline, invoked automatically by APEX/OpenClaw.

---

## 0. Purpose and decision discipline

This document is the handover-quality architecture analysis for the transcript-to-knowledge pipeline. It deliberately preserves:

- operator decisions and constraints;
- current-repository evidence;
- external research findings;
- options considered at every stage;
- reasons for selecting or rejecting options;
- measurable V1 targets;
- fallback upgrades if a chosen component fails.

It is designed so that a future CLI AI can continue from repository state without reconstructing intent from a chat transcript.

**Anti-overengineering rule:** every dependency or extra stage must solve a demonstrated problem. Do not add a framework because it is interesting. A component enters V1 only if it is necessary for the product or materially replaces fragile custom logic.

**Reuse-before-invention rule:** prefer mature external software for mechanical problems, but do not replace a working local deterministic TTK capability unless the external option wins a measured comparison.

**Important terminology:**

- **Local process** does not imply **local intelligence**. Claude Code, Gemini CLI, and Codex CLI are locally invoked processes backed by strong remote models.
- **Local Qwen** is a local-inference model. It is not authorized as the semantic worker in this pipeline.
- **Deterministic** means code/rules whose result is mechanically reproducible for the same inputs. ASR and LLM inference are not deterministic in this sense.

---

# 1. Operator decision lock

The following decisions are authoritative for V1 unless explicitly changed by the operator.

| ID | Decision | Locked choice |
|---|---|---|
| D01 | Product goal | **B:** high-value, trustworthy knowledge artifact. High-quality ASR is required because it enables B, but transcript text is not the final product. |
| D02 | Success | High insight recall + strong grounding + useful compression, not merely a polished summary. |
| D03 | Artifact audience | Canonical machine-readable knowledge + compiled human-readable views. |
| D04 | Macro/Meso/Micro | Preferred current representation, but not sacred. A demonstrably better representation may replace it. |
| D05 | Semantic intelligence | Strong subscription CLI AIs may be invoked automatically. |
| D06 | Semantic worker priority | Use a strong CLI AI for semantic reasoning; do not force reasoning onto a weak local model. |
| D07 | Qwen role | **No role in this pipeline for V1.** Future workflows may benchmark it for very simple bounded classification/routing, never assume semantic competence. |
| D08 | Semantic passes | Keep calls minimal; additional passes are justified only by measured value. |
| D09 | Cost model | Existing subscriptions are acceptable resources. Avoid unnecessary incremental API spend. |
| D10 | Subscription quota | Quality takes priority; using subscription quota for long sources is acceptable. |
| D11 | Token efficiency | High priority. A deterministic/local tool that materially reduces semantic token usage may justify additional setup. |
| D12 | Paid APIs | Undesirable, not forbidden. Keep strong paid options visible as benchmark/fallback/escalation choices with their value made explicit. |
| D13 | Invocation | **APEX/OpenClaw automatic invocation** is the normal target. |
| D14 | Human interaction | Zero routine human interaction after start. Stop only for real unresolved failures/authority boundaries. |
| D15 | CLI invocation | The pipeline may launch strong CLI AIs headlessly. |
| D16 | Parallelism | Allowed if provider limits and correctness allow it; not required for V1. |
| D17 | Recovery | Resume from validated state; never restart successful work without need. |
| D31 | External dependencies | Adopt when they materially improve quality, reliability, token/cost efficiency, or eliminate meaningful custom code. |
| D32 | Architecture selection | Benchmark working alternatives where the decision is consequential. |
| D34 | Duplicate capability | Reject a new dependency that merely duplicates a working TTK feature unless it clearly wins. |
| D35 | Micro exact evidence | **Mandatory for factual claims**. Non-factual semantic objects still need source provenance, but do not require a forced verbatim quote merely to satisfy a quota. |
| D36 | Macro/Meso synthesis | May be non-verbatim synthesis when traceably derived from lower-level evidence. |
| D37 | Uncertainty | Preserve important contradictions, caveats, corrections, and uncertainty. |
| D38 | Low-confidence insights | Preserve potentially valuable items with uncertainty labels rather than silently flattening/dropping them. |
| D39 | Compression | Adaptive to information density; no fixed 90–95% target. |
| D40 | Ontology | Keep protocols, mechanisms, arguments, anecdotes, etc. distinct where semantically useful. |
| D41 | Regression corpus | The existing four benchmark sources remain the initial cross-domain corpus. |
| D42 | Selection evidence | Actual output quality outranks architecture elegance. |
| D43 | Human gold set | Minimal targeted manual gold data is acceptable when it prevents repeated guessing. |
| D45 | Fail-closed semantics | If a required semantic AI stage did not actually execute and validate, the pipeline is incomplete. |
| D48 | External verification | Selectively verify important/checkworthy **factual** claims, not every statement. |

---

# 2. Current repository reality

## 2.1 What is already strong and should be preserved

The current `.claude/skills/transcript-to-knowledge/SKILL.md` already states the desired architecture:

- transcript is immutable evidence;
- deterministic code owns custody, segmentation, validation, routing, resumability, deduplication warnings, compilation;
- the active reasoning model owns semantic interpretation;
- Map reads bounded windows once;
- processing windows are not semantic chapters;
- context-only segments are not evidence;
- Reduce sees the validated compact evidence ledger;
- source support is separate from external truth;
- selective external fact verification exists;
- completion derives from files and hashes, not chat state.

This is the strongest existing core and should remain the architecture anchor.

## 2.2 What is currently wrong

The current `execute_ttk_lifecycle.py` convenience executor violates that skill contract. It uses regular expressions and hand-written lexical markers to:

- split sentence-like fragments;
- infer `fact`, `prediction`, `recommendation`, etc.;
- infer proper-noun entities;
- generate thematic labels;
- group windows mechanically into a fixed number of Meso chapters;
- stamp `source_support: SUPPORTED`;
- generate generic Macro text.

This is exactly the failure class the architecture was intended to prevent: **structurally valid, source-adjacent output that has not actually been semantically interpreted**.

Therefore V1 should replace the pseudo-semantic code path with a real CLI semantic worker. It should not rewrite the TTK custody/validator/compiler stack.

## 2.3 Latest benchmark truth state

The latest committed receipt at the time of this analysis (`artifacts/benchmark_runs/20260818-185245/receipt.json`) correctly reports `all_passed: false`; only one source is fully complete because Pipeline 2 remains `SYNTHESIS_PENDING` for three sources. The receipt also records a dirty working tree and a prior commit SHA, so future receipts must continue improving execution provenance.

---

# 3. External research findings that materially affect the design

Only primary/official sources are used below for technical capability claims.

## 3.1 Strong CLI semantic workers already expose automation primitives

### Claude Code

Official Claude Code documentation supports:

- non-interactive `claude -p` execution;
- JSON / streaming JSON output;
- **`--json-schema` validated structured output**;
- `--max-turns` and budget controls;
- explicit tool availability/permission restrictions;
- built-in `WebSearch` and `WebFetch` tools.

Sources:
- https://code.claude.com/docs/en/cli-usage
- https://code.claude.com/docs/en/headless
- https://code.claude.com/docs/en/tools-reference
- https://code.claude.com/docs/en/agent-sdk/permissions

Important cost note: Anthropic documents that from 2026-06-15, `claude -p` / Agent SDK usage on subscription plans draws from a separate monthly Agent SDK credit. This is acceptable under D09/D10 but must be measured rather than called “free.”

### Gemini CLI

Official Gemini CLI documentation supports:

- headless mode with `-p`;
- JSON and streaming JSON output;
- token/latency statistics in headless responses;
- standard exit codes;
- PowerShell automation examples;
- built-in Google web search and web fetch tools.

Sources:
- https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/headless.md
- https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/tutorials/automation.md
- https://github.com/google-gemini/gemini-cli/blob/main/docs/reference/tools.md

The current official headless docs do not expose a direct strict JSON-Schema output flag equivalent to Claude/Codex. Prompted JSON + deterministic validation/retry remains possible.

### Codex CLI

The official OpenAI Codex repository currently exposes:

- `codex exec` non-interactive execution;
- `--output-schema FILE` for strict JSON-schema final response shape;
- `--json` JSONL event output;
- output-last-message file support;
- hosted web-search capability in the current runtime/configuration.

Sources:
- https://github.com/openai/codex/blob/main/codex-rs/exec/src/cli.rs
- https://github.com/openai/codex/blob/main/codex-rs/exec/tests/suite/output_schema.rs
- https://github.com/openai/codex/blob/main/codex-rs/app-server/README.md

**Implication:** we do not need Instructor merely to obtain schema-shaped output in V1. Two already-available CLI workers provide schema constraints directly.

## 3.2 ASR options

### faster-whisper

The current engine already supports:

- word timestamps;
- Silero VAD;
- hotwords/hint phrases;
- language detection;
- average log probability;
- no-speech probability;
- compression-ratio diagnostics;
- hallucination-silence threshold;
- repetition controls.

Source: https://github.com/SYSTRAN/faster-whisper/blob/master/faster_whisper/transcribe.py

This means the smallest V1 improvement is to use the existing engine correctly and benchmark model/configuration quality before replacing it.

### NVIDIA Parakeet TDT 0.6B v3

NVIDIA’s model card describes a 600M multilingual ASR model supporting 25 European languages including English and German, automatic punctuation/capitalization, and word/segment timestamps. NeMo documentation exposes timestamp output for Parakeet models.

Sources:
- https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3
- https://github.com/NVIDIA-NeMo/Speech/blob/main/docs/source/asr/intro.rst

This is the most valuable **ASR challenger**, especially because German domain vocabulary is a demonstrated weakness. It is not V1 default because NeMo adds a heavier dependency/runtime stack and current issue history shows timestamp/dependency friction in some configurations.

### WhisperX

WhisperX adds forced alignment and pyannote diarization on top of faster-whisper, giving accurate word timestamps and speaker labels.

Source: https://github.com/m-bain/whisperX

It is an upgrade only if timestamp or speaker separation proves materially necessary. Adding it by default would increase dependency complexity without fixing the current primary semantic failure.

### OpenVINO GenAI Whisper

OpenVINO GenAI provides a local Whisper speech-recognition pipeline and supports CPU/GPU device selection; its Whisper examples expose word timestamps and hotwords. This is particularly relevant to the Intel Lunar Lake/Arc machine.

Sources:
- https://github.com/openvinotoolkit/openvino.genai
- https://github.com/openvinotoolkit/openvino.genai/blob/master/samples/js/whisper_speech_recognition/README.md

This is a future performance challenger if CPU faster-whisper is too slow at the model size required for quality.

### whisper.cpp

whisper.cpp supports Vulkan acceleration, but Windows Intel-GPU paths currently involve build/runtime caveats. It is therefore not the first implementation choice on this machine.

Source: https://github.com/ggml-org/whisper.cpp/blob/master/README.md

## 3.3 Optional extraction/orchestration libraries

### Google LangExtract

LangExtract provides exact source-location grounding, long-document chunking/parallel passes, structured extraction, and model flexibility.

Source: https://github.com/google/langextract

**V1 conclusion:** valuable challenger, but not needed yet. TTK already has canonical segment IDs, exact quotes, processing windows, and deterministic validators. Inserting LangExtract before proving a gap would duplicate custody/extraction infrastructure and would still require an LLM provider adapter.

### Instructor

Instructor provides Pydantic-based structured LLM output, validation, and automatic retry across many providers.

Source: https://github.com/567-labs/instructor

**V1 conclusion:** do not add. Claude and Codex CLIs already support schema-constrained output, and TTK already has deterministic validation. Instructor becomes useful only if the worker later moves to a provider without native schema support or if validation/retry plumbing grows materially.

### Berkeley DocETL

DocETL is a declarative/agentic LLM Map-Reduce data-processing system with parallel operators and pipeline optimization.

Source: https://github.com/ucbepic/docetl

**V1 conclusion:** do not add. TTK already contains the transcript-specific Map → validate → Reduce → verify → compile state machine and provenance rules. DocETL is the leading fallback if our custom semantic dispatch loop itself becomes burdensome or inaccurate, but it should not replace transcript custody now.

### GLiNER2 / NuExtract

GLiNER2 is a CPU-first local structured-information-extraction model; NuExtract 2.0 supports schema-driven fields including `verbatim-string`.

Sources:
- https://github.com/fastino-ai/GLiNER2
- https://huggingface.co/numind/NuExtract-2.0-2B

**V1 conclusion:** not semantic authorities. Benchmark later only if Map token usage becomes the dominant cost and a cheap pre-extractor can remove substantial work without reducing insight recall.

### DeepEval

DeepEval provides LLM-based faithfulness/relevancy evaluation.

Source: https://github.com/confident-ai/deepeval

**V1 conclusion:** evaluation option, not runtime dependency. First establish deterministic correctness plus direct cross-model/human output review. Add DeepEval only if repeated semantic regression evaluation becomes painful enough to justify it.

## 3.4 Product/baseline comparators

Fabric and Open Notebook remain useful baselines, not trust cores:

- Fabric can quickly extract/summarize YouTube transcripts through reusable prompt patterns.
- Open Notebook provides an existing notebook/knowledge UX and local/cloud provider integrations.

Sources:
- https://github.com/fail-open/fabric
- https://github.com/lfnovo/open-notebook

They should be used to answer “is our operator artifact actually better?” rather than inserted into V1 architecture.

---

# 4. End-to-end pipeline — step/options/value matrix

The word **all** below means all materially plausible/researched options for this project, not every package on the internet.

| Step | Valuable target | Options considered | V1 choice | Why V1 | Future upgrade if V1 fails |
|---|---|---|---|---|---|
| **0. Trigger** | APEX/OpenClaw can start one durable run without operator ceremony | APEX/OpenClaw → script; manual PowerShell; Qwen executor; workflow framework (Prefect/Dagster/Temporal) | **APEX/OpenClaw → one local runner** | Existing orchestrator already exists; no reason to add another | If OpenClaw dispatch proves unreliable, add a tiny scheduled/service wrapper—not a new workflow platform first |
| **1. Source acquisition** | Reproducible source file + metadata | existing P1 downloader; yt-dlp + ffmpeg; browser download; external transcript-only services | **Reuse existing P1/yt-dlp+ffmpeg path** | Mechanical, mature, already working | Add alternate extractor only for unsupported sources |
| **2. ASR** | Accurate EN/DE transcript with timestamps + confidence/evidence telemetry | faster-whisper base/small/medium/large-v3; Parakeet v3; OpenVINO Whisper; WhisperX ASR; whisper.cpp; paid ASR APIs | **faster-whisper, calibrated model/config** | Already installed; rich evidence telemetry; smallest change | Parakeet for EN/DE quality; OpenVINO for Intel acceleration; paid ASR as optional difficult-source escalation |
| **3. ASR quality control** | Detect obvious weak segments without inventing corrections | no QA; confidence/logprob/VAD diagnostics; second-ASR disagreement; AI text cleanup; manual review | **Deterministic ASR diagnostics; no semantic text repair** | Cheap and safe; AI cannot recover unheard audio | Re-transcribe flagged clips with stronger ASR/hotwords; second engine disagreement check |
| **4. Canonical transcript custody** | Immutable source identity, stable IDs, timestamps, resume | TTK init; custom database; LangExtract char spans; vector DB | **TTK init/canonical transcript** | Already purpose-built and tested | Only change if TTK ingestion loses required word-level evidence |
| **5. Processing windows** | Every source segment reaches semantic worker once as core evidence; bounded context | TTK lexical/pause windows; fixed token chunks; semchunk; Chonkie; LangExtract chunking; DocETL split/gather | **TTK windows + context halo** | Already preserves source IDs, hashes, context-only semantics | Benchmark semantic chunkers only if Map quality shows boundary failures |
| **6. Semantic Map** | One high-value semantic pass/window capturing themes, arguments, mechanisms, protocols, useful claims, uncertainty | Claude CLI; Codex CLI; Gemini CLI; browser subscription AI; direct paid APIs; Qwen; heuristic Python; LangExtract+model; DocETL map | **Claude Code `-p` with JSON Schema, no tools** | Strong model, headless, native schema output, minimal integration; Qwen/heuristics explicitly rejected | First challenger Codex `exec --output-schema`; Gemini if quota/provider constraints; LangExtract only if evidence-span failures remain |
| **7. Map validation** | Reject malformed/stale/unsupported provenance before reduction | TTK validator; Pydantic/Instructor; LLM reviewer; JSON Schema alone | **TTK deterministic validator** | Existing contract is stronger than mere JSON shape | Add Pydantic only if schema maintenance becomes painful |
| **8. Reduce / synthesis** | Meaningful global thesis, semantic modules, refined Micro claims; all important Map evidence represented | Claude CLI; Codex CLI; Gemini CLI; browser AI; DocETL reduce; heuristic Python | **same Claude CLI semantic worker, strict Reduce schema** | Minimal provider surface; compact evidence ledger controls tokens | Codex challenger; DocETL only if orchestration/tuning becomes a real problem |
| **9. Source-support validation** | Separate “speaker said/supports this” from “true in world” | strong AI judgment + deterministic refs; NLI model; quote-exists shortcut; heuristic classification | **semantic worker judges support; deterministic code verifies cited source objects/quotes** | Entailment is semantic; provenance is mechanical | Add multilingual NLI as advisory regression check only if support errors recur |
| **10. External verification routing** | Research only consequential factual claims | verify everything; checkworthiness queue; none; manual | **TTK checkworthiness queue, factual only** | Matches operator decision; controls search/token cost | Tune threshold based on observed queue size/value |
| **11. External verification execution** | Primary-source evidence and explicit CONFIRMED/CONTRADICTED/MIXED/UNVERIFIED | Claude WebSearch/WebFetch; Gemini Google Search; Codex web search; OpenClaw browser subscription AI; SearxNG; paid research APIs | **same Claude CLI in a separate web-enabled verification mode** | One provider adapter; built-in search; tightly scoped queue | Gemini/Codex browser/search fallback; OpenClaw browser for subscription UIs; paid API only if clearly valuable |
| **12. Knowledge compilation** | Stable machine JSON + concise human wiki with resolvable provenance | TTK compiler; P2 renderer; Open Notebook; Obsidian-specific custom exporter | **TTK compiler** | Already purpose-built | Add alternate views/exporters after canonical artifact is trustworthy |
| **13. Final validation** | “Complete” means every required stage actually happened and output is current | TTK `validate --complete`; benchmark receipt; AI self-review; DeepEval | **TTK complete validation + truthful receipt** | Deterministic completion is essential | Add independent semantic regression judge/DeepEval after V1 quality baseline |
| **14. Resume/receipt** | One failed window/research item reruns locally; exact provenance of run | TTK hashes/status; chat memory; workflow DB; Temporal | **TTK file/hash state + run receipt** | Existing and transparent | Add DB/service only if concurrent scale creates a demonstrated need |
| **15. Operator delivery** | Useful knowledge, not artifact sprawl | TTK wiki; single report; Open Notebook; Obsidian; Apex KB ingest | **TTK wiki + canonical JSON; integration downstream later** | First prove content quality | Add Open Notebook/Obsidian/Apex ingest after compiler output passes quality gate |

---

# 5. Focused option comparison matrices

## 5.1 Semantic worker comparison

| Option | Headless | Strict schema | Web research | Strength for nuanced synthesis | Integration complexity | Incremental cost posture | V1 verdict |
|---|---:|---:|---:|---:|---:|---|---|
| **Claude Code CLI** | Yes | **Yes (`--json-schema`)** | Yes | High | Low | Subscription Agent-SDK credit; measure usage | **Default V1** |
| **Codex CLI** | Yes | **Yes (`--output-schema`)** | Yes | High | Low | ChatGPT-plan/API context dependent; measure usage | **First challenger/fallback** |
| **Gemini CLI** | Yes | JSON wrapper, deterministic validator needed | **Yes** | High | Low–medium | Subscription/quota dependent | Fallback/challenger |
| Browser subscription AI through OpenClaw | Automatable but UI-coupled | Weak/indirect | Yes | High | Medium/high | Existing subscriptions | Recovery/fallback, not normal Map path |
| Direct paid model API | Yes | Usually yes | provider-dependent | High | Medium | Incremental paid usage | Optional escalation/benchmark |
| Qwen3-8B local | Yes | Can be constrained syntactically | No useful semantic trust | **Insufficient by operator decision/evidence** | Already installed | local compute | **Reject semantic role** |
| Heuristic Python | Yes | Deterministic shape | No | **Not semantic** | Low | Free | **Reject semantic role** |

### V1 semantic worker decision

Use **Claude Code CLI** for the first integrated test because the current official CLI provides the exact automation primitives we need: non-interactive input, structured JSON, strict JSON Schema, turn/budget controls, and optional WebSearch. Do not build a multi-provider router first.

Implement the worker boundary so the command invocation is isolated in one adapter file. If Claude quota/cost/quality fails, replace that adapter with Codex without changing the TTK lifecycle.

## 5.2 ASR comparison

| Option | Local | EN+DE | Word timestamps | Confidence/diagnostics | Install burden | Current-project evidence | V1 verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| **faster-whisper** | Yes | Yes | Yes | **Rich** | Already installed | Current base path works but has domain-word errors | **Keep, calibrate model/config** |
| **Parakeet TDT 0.6B v3** | Yes | **Yes** | Yes | Different telemetry | Medium/high (NeMo) | Not yet benchmarked here | Best challenger |
| WhisperX | Yes | Yes | **Forced alignment** | plus diarization | High | Not needed for current root failure | Add only if alignment/speaker need measured |
| OpenVINO GenAI Whisper | Yes | Yes | Yes | model-dependent | Medium | Intel stack already used elsewhere on machine | Performance challenger |
| whisper.cpp Vulkan/SYCL | Yes | Yes | Yes | model-dependent | Medium/high on Windows Intel | No local project benchmark | Not first |
| Paid ASR API | No | typically yes | provider-dependent | provider-dependent | Low integration, external cost/privacy | None needed yet | Optional oracle/escalation |

### V1 ASR decision

Do not swap engines before a small calibration. Keep faster-whisper and run difficult English/German slices through `base`, `small`, and `medium` using the same evidence-rich settings. Choose the **smallest model that clears the quality gate**; this is more robust than hard-coding “medium” or “large” based on assumptions. Parakeet is the next challenger if the German/domain-term gate fails.

## 5.3 Extraction/orchestration framework comparison

| Option | Solves a demonstrated missing V1 need? | Duplicates TTK? | Adds model/provider coupling? | V1 decision |
|---|---:|---:|---:|---|
| **TTK existing lifecycle** | Yes | — | No | **Keep** |
| LangExtract | Not yet | High overlap on grounding/chunking | Yes | Test only if quote/span mapping becomes unreliable |
| Instructor | Not with Claude/Codex schema output | Moderate on validation/retry | Yes | Do not add V1 |
| DocETL | Not while TTK lifecycle is small | High on Map/Reduce orchestration | Yes | Benchmark only if TTK orchestration becomes a real burden |
| GLiNER2 | Possible future token reduction | No, but adds prepass | Local model | Future benchmark if token cost is proven bottleneck |
| NuExtract | Possible future token reduction | No, but adds prepass | Local model | Future challenger after GLiNER2 |
| DeepEval | Evaluation only | No | requires judge model | Post-V1 regression option |
| Prefect/Dagster/Temporal | No current need | Replaces existing file-state lifecycle | No | Reject until concurrency/service scale justifies it |

---

# 6. Recommended V1 architecture

```text
APEX / OpenClaw
      |
      v
local deterministic runner
      |
      +--> acquire/extract source (existing P1 / yt-dlp + ffmpeg)
      |
      +--> faster-whisper ASR
      |      - calibrated model
      |      - Silero VAD
      |      - word timestamps
      |      - confidence/logprob/no-speech/compression telemetry
      |      - optional source-specific hotwords
      |
      +--> TTK init
      |      - immutable source SHA
      |      - canonical segment IDs
      |      - bounded Map windows
      |      - context halo
      |
      +--> LOOP each pending Map packet
      |      |
      |      +--> Claude CLI semantic worker
      |      |      - packet text only
      |      |      - NO shell/write/web tools
      |      |      - strict Map JSON Schema
      |      |
      |      +--> TTK deterministic validation
      |             - packet hash
      |             - core-only provenance
      |             - required exact quote evidence for factual claims
      |             - schema/enums/references
      |
      +--> TTK make-reduce
      |
      +--> Claude CLI Reduce worker
      |      - compact validated evidence ledger only
      |      - NO raw full transcript
      |      - strict Reduce JSON Schema
      |
      +--> TTK deterministic Reduce validation
      |
      +--> TTK make-verify (important/checkworthy factual claims only)
      |      |
      |      +--> Claude CLI verification mode
      |             - WebSearch/WebFetch enabled
      |             - primary/official sources preferred
      |             - explicit UNVERIFIED when evidence insufficient
      |
      +--> TTK compile
      |
      +--> TTK validate --complete
      |
      +--> truthful run receipt
             - exact git commit + dirty state
             - source SHA
             - ASR config/model
             - CLI provider/model/usage where observable
             - packet counts and validation states
             - verification counts
             - final artifact paths/hashes
```

## What is deliberately absent from V1

- Qwen;
- Ollama;
- LangExtract;
- Instructor;
- DocETL;
- GLiNER2;
- NuExtract;
- DeepEval as a runtime dependency;
- vector database;
- graph database;
- new workflow engine;
- custom diarization;
- browser UI automation for ordinary Map/Reduce;
- paid APIs in the normal path.

This absence is intentional, not a research omission.

---

# 7. Semantic evidence policy for V1

The current TTK contract requires a verbatim quote for every candidate claim. Operator decision D35 changes that requirement.

Recommended V1 rule:

| Semantic object | Required source provenance | Exact verbatim quote required? |
|---|---|---:|
| `fact` | source segment IDs | **Yes** |
| `estimate` / explicit numerical factual assertion | source segment IDs | **Yes** |
| `opinion` | source segment IDs | No |
| `prediction` | source segment IDs | No |
| `recommendation` | source segment IDs | No |
| `decision` | source segment IDs | No |
| `anecdote` | source segment IDs | No (quote optional) |
| `definition` | source segment IDs | Prefer quote; not a hard V1 gate unless treated as factual |
| `mechanism` | source segment IDs | Quote optional; source-support judgment required |
| `hypothesis` | source segment IDs | No |
| Meso synthesis | claim refs and/or source segment IDs | No |
| Macro synthesis | Meso/claim lineage | No |

**Do not confuse quote existence with semantic support.** Deterministic code can prove that a quote exists at a source location. The semantic worker must judge whether that evidence supports the formulated proposition.

**Do not confuse source support with external truth.** A transcript-grounded factual claim may later be externally contradicted.

---

# 8. Valuable target and failure trigger at every stage

| Stage | Minimum valuable target | Failure means | Next action |
|---|---|---|---|
| Acquisition | source captured + metadata + stable file | download/extraction unavailable | retry source adapter or alternate extractor |
| ASR | readable transcript; domain terms/figures acceptable; word/segment timing available | quality gate fails on gold slices | increase faster-whisper model/config; then Parakeet challenger |
| Custody | source SHA + stable segments + 100% source representation | parse/custody mismatch | fix importer; do not proceed semantic |
| Windowing | bounded packets, every segment core-covered exactly as intended | uncovered/duplicate invalid core coverage | fix deterministic TTK only |
| Map | useful semantics, not raw sentence dumping; factual claims grounded | schema/grounding invalid OR semantic artifact clearly low-value | retry same packet once; then provider/prompt diagnosis |
| Map validation | all packets valid and current | one packet invalid | rerun only that packet |
| Reduce | meaningful Macro/Meso/Micro; important Map evidence represented | generic headings, fixed template, missing major themes | repair Reduce prompt/provider; do not “validate” generic output as success |
| Verification routing | bounded queue of important factual claims | queue explodes or misses central facts | tune checkworthiness policy |
| External verification | primary evidence where feasible; explicit UNVERIFIED otherwise | fabricated/weak citations | invalidate only verification result, keep source claim |
| Compile | machine JSON + human wiki resolves all refs | stale/missing refs | deterministic compiler fix |
| Complete receipt | truthfully reports every required stage | any required semantic stage absent/stale | `all_passed=false` / incomplete |

---

# 9. V1 evaluation strategy — staged to avoid wasting work

## Gate A — semantic pipeline repair first

Use the **existing four transcripts** so ASR does not obscure whether the semantic architecture works.

Run genuine CLI Map + Reduce over:

1. Huberman/Adolphs — long English science interview (`P-h5WSQG1Sw`)
2. Elliott Prechter — technical finance (`CygwqaNg2PY`)
3. Markus Koch — German finance (`vFTuLylvYnA`)
4. Market Cycles — technical procedure (`oZIsMX6WgFs`)

Acceptance:

- every Map packet was actually produced by the CLI semantic worker;
- no heuristic semantic generator ran;
- all TTK validators pass;
- factual exact-quote rules pass;
- Reduce produces real semantic Meso modules rather than fixed time quartiles;
- no generic template Macro;
- the four outputs are visibly more useful than the current pseudo-semantic artifacts;
- receipt truthfully distinguishes complete/incomplete.

If this gate fails, **do not add LangExtract/DocETL/etc. automatically**. First determine whether the failure is prompt/schema/provider versus orchestration.

## Gate B — ASR calibration

Create a small manually checked slice set from the four videos, biased toward:

- proper nouns;
- numbers/percentages;
- Elliott Wave terminology;
- German finance terms;
- dense scientific terminology.

Run faster-whisper `base`, `small`, `medium` with equivalent VAD/timestamp settings. Compare exact gold text/domain-term accuracy and processing time.

Select the smallest model that passes. If no tested faster-whisper model passes acceptably, benchmark Parakeet v3 before inventing text repair.

## Gate C — fresh end-to-end runs

After A and B pass:

1. Run the shorter German source fresh end-to-end.
2. Run one shorter English technical source fresh end-to-end.
3. If both pass, run the long Huberman source and Market Cycles.

This staged sequence catches architecture failure cheaply.

---

# 10. Future upgrade map by observed failure

| Observed failure | First response | Second response | Do **not** do first |
|---|---|---|---|
| German/proper-noun ASR errors | larger/calibrated faster-whisper + hotwords | Parakeet v3 | AI rewrite of transcript |
| Word timestamp alignment poor | WhisperX alignment | alternative ASR timestamp engine | custom aligner |
| Speaker attribution required | WhisperX/pyannote | other proven diarizer | custom clustering |
| CLI output schema flaky | retry + validator | Codex strict schema / Instructor | redesign whole pipeline |
| Exact span mapping insufficient | improve TTK segment/word mapping | LangExtract benchmark | vector DB |
| Map token cost too high | reduce packet redundancy / tune window size | GLiNER2/NuExtract pre-extraction benchmark | weaker Qwen semantic worker |
| Map insight recall poor | prompt/examples/provider challenger | LangExtract multi-pass or DocETL comparison | add more deterministic heuristics |
| Reduce loses themes | improve evidence ledger + Reduce prompt | DocETL Reduce/gather benchmark | fixed chapter templates |
| Source-support errors | stronger semantic prompt/provider | multilingual NLI advisory check | infer support from quote existence |
| External verification expensive | raise checkworthiness threshold | alternate CLI/browser subscription AI | verify everything |
| Operator wiki not useful | compare Fabric/Open Notebook views | add alternate compiler views | change trust/custody core |
| Resume/orchestration fragile | fix TTK state/runner | only then consider workflow framework | add Temporal/Prefect immediately |

---

# 11. Architecture choice summary

## Keep

- existing P1 source acquisition path;
- faster-whisper as first ASR engine;
- evidence-rich ASR JSON;
- TTK canonical custody;
- TTK window/packet/hash lifecycle;
- TTK deterministic validators;
- TTK selective verification queue;
- TTK compiler;
- file/hash-based resumability.

## Replace

- heuristic pseudo-semantic Map generation in `execute_ttk_lifecycle.py`;
- heuristic claim typing;
- heuristic entity extraction as semantic authority;
- fixed mechanical Meso grouping;
- automatic `source_support: SUPPORTED` stamping;
- generic Macro template generation.

## Add only

- **one small CLI semantic-worker adapter**;
- **one deterministic pipeline runner** that follows TTK `next` state and calls the worker;
- exact run receipts with provider/model/usage metadata;
- a small ASR calibration fixture/gold slice set.

## Defer

Everything else until a measured failure names the missing capability.

---

# 12. Decision rationale in one sentence

**V1 is intentionally boring:** reuse the already-correct TTK evidence/state machine, keep the already-working local ASR stack while calibrating quality, replace only the fake semantic executor with one strong schema-constrained subscription CLI worker, and measure the four real sources before adding any other framework.
