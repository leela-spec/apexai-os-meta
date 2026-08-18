# Transcript-to-Knowledge v2 — Research Source Ledger

The implementation was derived from primary papers, official project documentation/repositories, and working open-source transcript pipelines. A source appearing here does **not** mean its full architecture was adopted.

| Source | What was inspected | What v2 borrows | What v2 rejects/defers |
|---|---|---|---|
| Lost in the Middle — https://arxiv.org/abs/2307.03172 | long-context utilization/position sensitivity | do not rely on context-window size as reliability guarantee | one-shot long transcript as baseline |
| TextTiling — https://aclanthology.org/J97-1003/ | deterministic lexical cohesion segmentation | cheap lexical boundary signal | treating lexical cuts as semantic chapter truth |
| FActScore — https://arxiv.org/abs/2305.14251 | atomic factual precision evaluation | self-contained factual proposition concept | atomize all transcript content |
| SAFE / LongFact — https://arxiv.org/abs/2403.18802 and https://github.com/google-deepmind/long-form-factuality | search-augmented individual fact evaluation | evidence-bearing external verdicts | search every statement by default |
| Decomposition Dilemmas — https://aclanthology.org/2025.naacl-long.320/ | decomposition error/noise tradeoff | keep decomposition bounded/useful | assume more atomic decomposition always improves verification |
| FaStFACT — https://arxiv.org/abs/2510.12839 | chunk-level extraction + pre-verification + document evidence | extract claims during chunk pass; selective verification | fixed all-claim search pipelines |
| MiniCheck — https://aclanthology.org/2024.emnlp-main.499/ | efficient document-grounded fact checking | optional local source-support second check | hard dependency in core |
| RAPTOR — https://arxiv.org/abs/2401.18059 | recursive abstraction for retrieval | lower-level evidence before higher-level synthesis | recursive tree for single transcript core |
| Chain of Density — https://arxiv.org/abs/2309.04269 | density/readability summary refinement | optional final Macro QA heuristic | repeated default generations |
| Microsoft GraphRAG — https://microsoft.github.io/graphrag/ | TextUnits, graph extraction, claims, communities, caching/output model | structured intermediates/source refs; optional downstream index inspiration | graph-first core; default claim extraction; vector/Parquet stack |
| lattifai `lai-summarize` — https://github.com/lattifai/lattifai-skills | prepare -> agent writes -> deterministic validate; verbatim quote checking | agent-session semantic work surrounded by scripts | hidden API requirement |
| silverstein/minutes — https://github.com/silverstein/minutes | Markdown meeting pipeline, pluggable semantic engines, provenance/dedup/dry-run, map-reduce for long transcripts | simple durable files, optional agent CLI, provenance, graceful fallback | a complex mandatory KB service |
| OpenVINO GenAI Whisper — https://docs.openvino.ai/2026/api/genai_api/_autosummary/openvino_genai.WhisperPipeline.html | Whisper CPU/GPU/NPU API, word timestamps | optional Intel-friendly upstream ASR candidate | core dependency |
| OpenVINO long-audio issue — https://github.com/openvinotoolkit/openvino.genai/issues/3501 | memory scaling on long audio | manually chunk long audio if using backend | assume backend handles arbitrary duration efficiently |
| OpenVINO Lunar Lake NPU issue — https://github.com/openvinotoolkit/openvino.genai/issues/4222 | current NPU failure on Lunar Lake | benchmark device routes | NPU as default without local validation |

## Research synthesis rule

A pattern was promoted into v2 only when it met all of these:

1. directly improves the transcript→knowledge mission;
2. has clear failure behavior;
3. can be locally validated or bounded;
4. does not add more infrastructure than the failure it solves;
5. keeps source provenance inspectable;
6. does not force repeated raw-context/model calls without measured value.
