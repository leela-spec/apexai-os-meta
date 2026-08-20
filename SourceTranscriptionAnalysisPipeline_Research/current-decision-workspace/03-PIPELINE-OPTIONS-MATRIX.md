# Pipeline Options Matrix — Current Decision Workspace

**Status:** LIVE COMPARISON MATRIX  
**Date:** 2026-08-20  
**Rule:** component reality, architecture fit, and project proof are separate evidence levels.

## Rating notation

- **Value V1–V5:** expected product leverage if it works.
- **Evidence E4:** mature/publicly proven component or standard practice.
- **Evidence E3:** real, maintained, documented; exact project role not yet proven.
- **Evidence E2:** real but new/vendor-heavy/limited production evidence.
- **Evidence E1:** project-specific architectural hypothesis/custom integration.
- **Risk R1–R5:** integration/operational risk.

`E3/1` means the component is E3 but the proposed integration pattern is only E1.

## Matrix

| Responsibility | Option A | Option B | Option C | Option D | Current recommendation |
|---|---|---|---|---|---|
| **Workflow / orchestration** | Plain deterministic Python runner — `V5 E4 R1` | **LangGraph** state/checkpoints/branches — `V4-5 E4/3 R2-3` | Autonomous subscription CLI controller — `V3-5 E4/1 R4-5` | OpenClaw as process supervisor — `V2-3 E3/2 R3` | Start from explicit deterministic workflow requirements; benchmark LangGraph if resume/fallback branching materially helps. CLI autonomy allowed but high-bar. |
| **Source acquisition** | **yt-dlp + FFmpeg** — `V5 E4 R1` | local media/transcript input — `V5 E4 R1` | browser/manual fallback — `V2 E3 R3` | turnkey product ingestion — `V2 E3 R2-3` | yt-dlp/FFmpeg/local input. No custom acquisition system. |
| **Transcript choice / ASR** | existing trustworthy transcript — `V5 E4 R1` | **faster-whisper** local — `V5 E4/2 R2` | **Parakeet TDT 0.6B v3** local challenger — `V4 E3/2 R3-4` | hosted Scribe v2 / Nova-3 — `V5 E3/2 R2` | Benchmark local reference against hosted quality only if hosted route could earn its dependency/cost. Do not assume local or hosted winner. |
| **Alignment / speakers** | no extra stage — `V4 E4 R1` | WhisperX + pyannote — `V3-4 E3 R3-4` | hosted ASR built-in diarization — `V3-4 E3 R2` | custom solution — `V1 E1 R5` | Conditional only when speaker/timing quality materially affects product. |
| **Canonical source / custody** | reuse TTK custody functions — `V4-5 E1-2 R2-3` | thin canonical source package — `V5 E4/2 R1-2` | database/vector-store ownership — `V1-2 E4/1 R4` | no durable source representation — `V1 R4` | Preserve only demonstrated invariants: stable source identity, transcript/timing when available, hashes/state needed for resume/traceability. Exact evidence burden is configurable. |
| **Long-text extraction transport** | TTK 700–1500-word windows — `V3-4 E1 R3` | **LangExtract native chunking/parallel/multipass** — `V5 E3/3 R2` | generic chunker — `V2-3 E3 R2` | full-context direct model — `V3-5 E3 R1-3` | If LangExtract wins extraction, prefer its built-in long-doc process unless a measured gap justifies external windowing. |
| **Grounded extraction** | direct model/CLI prompts — `V4 E4/2 R2-4` | **LangExtract + local Ollama/Qwen** — `V5 E3/3 R2-3` | **LangExtract + Gemini API** — `V5 E3/3 R2` | LangExtract + custom CLI provider — `V4-5 E3/1 R4` | Mandatory comparison of local Qwen path vs strong external path. Native provider paths preferred over custom adapter unless adapter earns large value. |
| **Cheap pre-extraction** | none — `V4 E4 R1` | GLiNER2 — `V2-3 E3/1 R2-3` | NuExtract — `V2-3 E3/1 R3-4` | custom regex/heuristics — `V1 E1 R4` | Optional. Test only if it plausibly reduces expensive semantic work or improves recall. |
| **Structured output / retries** | provider-native schema + deterministic validation — `V5 E4 R1-2` | Instructor/Pydantic — `V3-4 E3 R2-3` | LangExtract structured extraction — `V4 E3 R2` | custom parser/retry framework — `V1 E1 R4` | Native first; Instructor only when measured brittleness/value justifies it. |
| **Evidence / provenance strictness** | evidence-light usefulness-first — `V4 R1` | source-grounded claims where useful — `V5 E4/2 R2` | strict exact quote/time evidence — `V5 for high-trust use, R3` | universal strict evidence — `V2-4 R4` | **Configurable by use case.** Do not impose strict traceability on every output. |
| **Semantic source-support check** | none beyond synthesis — `V2-4 R1` | bounded strong-model review — `V4-5 E3/2 R2` | mDeBERTa/HHEM advisory — `V2-3 E3/1 R2-3` | custom support classifier — `V1 E1 R4` | Select based on target evidence mode. Specialist models advisory only unless benchmark proves more. |
| **Global synthesis input** | full transcript only | evidence only | **full transcript + evidence** | hierarchical section synthesis | All three primary forms must be tested on the same real source (D20); no preselected winner. |
| **Global synthesis model** | local Qwen 8B | subscription CLI model | external API long-context model | hybrid local extraction + external synthesis | Mandatory local-vs-external identical-input comparison. API/CLI earns role through significant measured value. |
| **Autonomous semantic/CLI worker** | no autonomy; exact calls only | bounded autonomous module | broad autonomous pipeline execution | API direct call | **Autonomy allowed but avoid-by-default.** Use only when value is large and execution pattern proves reliable. |
| **External factual verification** | none | selective checkworthy claims | verify everything | future research service | Keep optional/selective where the product actually needs external truth. Do not conflate with source support. |
| **Output representation** | Macro/Meso/Micro | structured article/wiki | source-grounded report | task-specific artifact / mixed representation | **Open. Macro/Meso/Micro is only one candidate.** Choose by product usefulness, not prior architecture inheritance. |
| **Compiler/output rendering** | reuse TTK compiler pieces | small deterministic renderer/templates | Fabric/Open Notebook as final product | free-form AI output | Deterministic compilation when a canonical artifact is needed; reuse selectively. |
| **Evaluation** | human must-find / artifact review | NotebookLM/Fabric/Open Notebook baselines | DeepEval auxiliary | internal PASS receipts | Product artifact quality outranks internal PASS. Use real-source comparisons and human/product baselines. |
| **Resume/recovery** | tiny stage manifest/hashes | **LangGraph checkpoint state** | TTK packet/result state | workflow engine/Temporal-class system | Requirement is locked; implementation remains open. Use the smallest proven option that satisfies actual failure/fallback scenarios. |
| **Visual-only evidence** | transcript only | video/image analysis branch | multimodal model | specialist video system | **OUT OF CURRENT SCOPE.** Future project only. |
| **Non-factual provenance policy** | minimal | strict provenance | mixed by type | external knowledge attribution | **OUT OF CURRENT SCOPE.** Future development. |

## Production dependency inventory

### Fully local-capable components

- yt-dlp
- FFmpeg
- faster-whisper
- Parakeet TDT (runtime feasibility still to benchmark on this machine)
- WhisperX inference after model setup
- TTK code
- LangExtract library
- LangExtract + Ollama/local Qwen
- LangGraph
- GLiNER2
- NuExtract
- mDeBERTa
- HHEM
- Instructor library
- DocETL framework with a compatible local model/provider path
- local deterministic compiler/evaluation code

### External/cloud/account-backed candidates

- Gemini provider/API
- OpenAI provider/API
- ElevenLabs Scribe v2
- Deepgram Nova-3
- Claude Code CLI / Codex CLI / Antigravity CLI semantic inference
- NotebookLM
- web factual verification

External options remain visible because they may provide enough value to justify use; they are not production defaults merely because they are easier or stronger in general benchmarks.

## Explicit anti-hallucination rule

Before an option is promoted, record:

```text
Existing implementation actually verified:
Exact capability verified:
Integration path actually supported:
Project fixture actually run:
Observed gain:
Observed failure/risk:
Remaining custom code:
```

If these fields cannot be filled honestly, the option is still research/hypothesis.