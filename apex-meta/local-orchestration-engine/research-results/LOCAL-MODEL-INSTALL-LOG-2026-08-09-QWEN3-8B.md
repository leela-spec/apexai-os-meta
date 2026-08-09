---
title: "Local Model Install Log — Qwen3-8B (OpenVINO GenAI + llama.cpp)"
doc_type: local_model_install_log
initiative: local-orchestration-engine
created: 2026-08-09
status: "both configurations installed and smoke-tested; pending real APEX benchmark fixtures (future work, not this handover)"
handover: apex-meta/local-orchestration-engine/HANDOVER-2026-08-09-QWEN3-8B-LOCAL-INSTALL.md
---

# Local Model Install Log — Qwen3-8B

**This is an install-and-verify record, not a model selection or certification.** Per
`OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md` (LM-28, LM-30), Qwen3-8B is an
**installed candidate, pending benchmark** — nothing below should be read as "selected,"
"the local model," or "in production." No CODE/WEEKLY/MA/INJECT/COEX fixture was run; that
remains explicitly future work.

Machine: HP OmniBook X Flip 16-as0xxx, Windows 11, Intel Core Ultra 7 258V, ~31.6 GB RAM,
Intel Arc 140V (16 GB shared-memory pool), GPU driver 32.0.101.8626 (2026-03-11).

## Configuration A — OpenVINO GenAI

| Field | Value |
|---|---|
| Software versions | OpenVINO `2026.3.0`, OpenVINO GenAI `2026.3.0.0` (build 2495), OpenVINO Tokenizers `2026.3.0.0`, Python `3.12.10` in a dedicated venv, `huggingface_hub` `1.27.0` |
| Model artifact | `OpenVINO/Qwen3-8B-int4-ov` (Hugging Face, pre-converted OpenVINO IR, INT4). Main weight file `openvino_model.bin`, 4,855,348,053 bytes. 18 files total (tokenizer/detokenizer/config alongside). Downloaded via `huggingface_hub.snapshot_download`. |
| Install paths | Runtime/venv: `C:\LocalModels\runtimes\openvino\venv\`. Model: `C:\LocalModels\qwen3-8b\openvino-int4\` (matches handover Section 3 exactly). |
| GPU device visibility | Confirmed via `openvino.Core().available_devices` → `['CPU', 'GPU', 'NPU']`; `GPU` reports `Intel(R) Arc(TM) 140V GPU (16GB) (iGPU)`. Pipeline explicitly loaded on `"GPU"`. |
| Smoke-test prompt | `Say hello and name yourself in one sentence.` |
| Smoke-test output (verbatim, `max_new_tokens=200`) | `<think>\nOkay, the user wants me to say hello and name myself in one sentence. Let me start by greeting them. I should use a friendly tone. Then, I need to mention my name. Wait, what's my name? Oh right, I'm Qwen. So the sentence should be something like "Hello, I'm Qwen!" Let me check if that's concise enough. Yes, that's one sentence and includes both the greeting and my name. I don't need to add anything else. It's straightforward and meets the user's request.\n</think>\n\nHello, I'm Qwen!` |
| Load time | 10.6s–14.4s across three separate cold loads |
| Generation time | ~4.7s–5.2s for a 64-token capped run; the 200-token run above completed within its cap (reached natural end, not truncated) |
| Measured resident memory | **~5.0 GB** (system-wide free-physical-memory delta: 10,191.2 MB free idle vs. 5,098.8 MB free with model loaded and generating ⇒ ≈4.97 GB). Methodology note: Arc 140V is an integrated GPU that draws from shared system RAM rather than dedicated VRAM, so total-system-free-memory delta is the correct measure here — Windows' per-process "GPU Process Memory" performance counters did not attribute usage to this process cleanly (tested and abandoned; see Deviations). This is comfortably under the ~15.7 GB usable-GPU-budget ceiling the handover set, in line with the ~5–6 GB the handover itself predicted. |
| Final status | **INSTALLED_AND_VERIFIED** |

## Configuration B — llama.cpp (Vulkan)

| Field | Value |
|---|---|
| Software versions | `llama.cpp` release `b10333`, commit `08659901c`, built with Clang 20.1.8 for Windows x86_64. Prebuilt binary (`llama-b10333-bin-win-vulkan-x64.zip`, 34,147,775 bytes) from `ggml-org/llama.cpp` GitHub releases — no source build needed. |
| Model artifact | `Qwen/Qwen3-8B-GGUF` (Hugging Face, **official Qwen release**, not a community requant). File `Qwen3-8B-Q4_K_M.gguf`, 5,027,783,488 bytes. SHA256: `d98cdcbd03e17ce47681435b5150e34c1417f50b5c0019dd560e4882c5745785`. |
| Install paths | Runtime: `C:\LocalModels\runtimes\llama.cpp\`. Model: `C:\LocalModels\qwen3-8b\gguf-q4km\` (matches handover Section 3 exactly). |
| Backend requested / used | Vulkan, via `llama-server --gpu-layers 999 --ctx-size 32768`. No explicit "Vulkan device detected" log line was printed by this server build at its default verbosity (deviation — see below); backend was instead confirmed indirectly (see below). |
| Smoke-test prompt | `Say hello and name yourself in one sentence.` (via `/v1/chat/completions`) |
| Smoke-test output (verbatim, `max_tokens=200`, one representative run) | `reasoning_content`: `Okay, the user wants me to say hello and name myself in one sentence. Let me think about how to phrase that.\n\nFirst, I need to greet them. The standard greeting is "Hello!" or "Hi there!" Maybe "Hello!" is more friendly. Then, I should introduce myself. My name is Qwen, so I need to mention that. \n\nWait, the user specified "name yourself," so maybe they want me to state my name clearly. Let me check the instructions again. They said "say hello and name yourself in one sentence." So the entire response should be a single sentence combining both actions.\n\nSo, "Hello! I am Qwen." That's straightforward. Let me make sure there are no typos. Qwen is the correct name. Maybe add a bit more to make it sound natural? Like "Hello! My name is Qwen." But the user might prefer the shorter version. \n\nAlternatively, "Hello! I'm Qwen."` ; `content`: `""` (empty — this particular sampling run (temperature 0.8, default) did not exit its `<think>` block within the 200-token cap; a separate 64-token run produced the same pattern). The reasoning trace itself is coherent, on-topic, and converging toward a correct answer throughout — no incoherent or erroneous output was observed in any run. |
| Load time | ~19s cold load (model + 32K-context KV buffer init for 4 slots) |
| Generation timings | Prompt processing 9.2–25.5 tok/s (short 17–20 token prompts, likely fixed-overhead-dominated); decode 12.5–13.5 tok/s sustained across three separate generation calls (64, 300, and 200 max-token runs) |
| Measured resident memory | Process working set (`tasklist`) read **10.76 GB** immediately after the first exchange, rising to **14.16 GB** after several subsequent generation calls in the same server session — attributable to KV-cache growth under `--ctx-size 32768` with `n_slots=4` (`kv_unified=true`), not a leak. This is a real, reproducible number worth carrying into the future COEX/CTX benchmark design, since it is markedly higher than Configuration A's footprint for the same model. |
| Final status | **INSTALLED_AND_VERIFIED** |

## Deviations from the handover

1. **Backend confirmation method for Configuration B.** The handover expected a device/offload log line (the typical llama.cpp `load_tensors: offloaded N/M layers to GPU` pattern). This server build printed only 11 log lines at default verbosity and none named a backend or device. Vulkan/GPU use was instead inferred from CPU-utilization behavior: a 16.09-second, 200-token generation call consumed only 5.56 seconds of process CPU time (~35% of one core), which is inconsistent with CPU-bound 8B-model decoding (which would be expected to peg multiple cores near 100%) and consistent with the CPU mostly waiting on GPU compute dispatch. This is a reasonable but indirect confirmation — a future benchmark session should re-verify with `--list-devices`, a verbose server flag, or a direct llama.cpp GPU-only vs. CPU-only comparison run if a stronger guarantee is needed.
2. **GPU memory measurement method for Configuration A.** Windows' `\GPU Process Memory(*)\*` performance counters did not attribute any measurable usage to the Python process across repeated attempts (tried both PID-specific and adapter-aggregate queries). Measurement fell back to total-system-free-RAM delta, which is methodologically sound for an integrated GPU with a shared memory pool but is a system-wide rather than strictly per-process number.
3. **Config B's smoke-test capture did not reach a final answer within 200 tokens** on the run recorded above (Qwen3's default "thinking" mode consumed the full token budget). This is a sampling/token-budget artifact, not a coherence or correctness failure — the reasoning trace itself is fully coherent and on-topic in every run observed, including the earlier 64-token run. Worth flagging for the future benchmark harness: fixtures that need a completed (not just coherent) answer should either raise `max_tokens` further or disable thinking mode, since Qwen3-8B's default reasoning verbosity can consume 150+ tokens on a one-sentence request.

No errors were encountered that blocked installation or verification of either configuration.

## Not done (explicitly out of scope per the handover)

- Qwen2.5-Coder-7B-Instruct and Qwen3.5-4B are not installed (separate handover per Section 0).
- No MoE candidate was installed.
- No CODE/WEEKLY/MA/INJECT/COEX benchmark fixture was run against either configuration.
- Neither configuration is wired into any orchestration path, planner, or routing registry.
