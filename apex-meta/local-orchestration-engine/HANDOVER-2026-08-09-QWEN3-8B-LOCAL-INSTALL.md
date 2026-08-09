---
title: "Handover — Install Qwen3-8B (Primary Generalist) for the First Local-Model Bake-Off"
doc_type: handover
initiative: local-orchestration-engine
created: 2026-08-09
authority: operator-session-2026-08-09
status: "ready for execution by a local coding agent (Claude Code) with real install permissions on the operator's Windows machine"
repo: leela-spec/apexai-os-meta
branch_policy: "WORK DIRECTLY ON main ONLY. Do not create branches unless the operator explicitly asks for one."
reads_first:
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md
  - apex-meta/local-orchestration-engine/LOCAL-MODEL-BENCHMARK-PORTFOLIO-2026-08-08.md
  - apex-meta/local-orchestration-engine/research-results/LOCAL-MODEL-CROSS-AGENT-COMPARISON-B-E-2026-08-09.md
  - apex-meta/local-orchestration-engine/research-results/LOCAL-MODEL-MOE-BANDWIDTH-VS-COEXISTENCE-2026-08-09.md
  - apex-meta/local-orchestration-engine/research-results/README.md
---

# Handover — Install Qwen3-8B for the First Local-Model Bake-Off

## 0. Mission, and what this is NOT

Install **Qwen3-8B** — the primary ~7-8B generalist candidate — on the operator's machine, in both of the two runtime configurations the cross-agent research converged on, so it is ready to be run against the actual APEX benchmark fixtures in a later session.

**This is an install-and-verify task. It is not a model selection.** Per `OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md` (LM-28, LM-30), no model enters production or the planner's routing registry until it has been run against the real APEX CODE/WEEKLY/MA/INJECT/COEX fixtures and certified. Installing Qwen3-8B now is preparation for that bake-off, not a substitute for it. Do not write anything into this repo that describes Qwen3-8B as "selected," "the local model," or "in production." The correct framing throughout is "installed candidate, pending benchmark."

Two other models belong in the same first bake-off (Qwen2.5-Coder-7B-Instruct as coding specialist, Qwen3.5-4B as the efficiency control) but are **out of scope for this handover** — install Qwen3-8B first, verify it end-to-end, and stop. A follow-up handover will cover the other two once this one is confirmed working, so problems are isolated to one model at a time.

## 1. Machine profile (do not deviate without checking)

```yaml
machine_profile: "HP OmniBook X Flip / Core Ultra 7 258V / ~31.6 GB RAM / Arc 140V / Windows 11"
usable_gpu_vram_gb: 15.7   # shared GPU-addressable pool; must leave headroom for the browser fleet per LM-26
measured_gpu_bandwidth_gbps: 136.5
```

Qwen3-8B at Q4_K_M/INT4 needs roughly 5-6 GB resident (weights + KV cache at 32K context + runtime overhead) — comfortably inside the 15.7 GB budget with room to spare for coexistence. If actual measured resident usage comes in materially higher than ~7 GB, stop and report it rather than proceeding — that would itself be a useful early data point, not a failure to hide.

## 2. Why two runtime configurations, not one

Research Prompt D (Windows/Intel runtime) had both agents independently converge on the same pairing: **OpenVINO GenAI is the primary runtime** for the Arc 140V GPU path, with **llama.cpp (Vulkan or SYCL backend) as a mandatory independent comparator** — not optional, because runtime choice measurably affects throughput, memory behavior, and structured-output reliability, and the benchmark portfolio's "size-class comparison discipline" (Section 10 of the portfolio doc) requires comparable, reproducible configuration identities. NPU was deprioritized by both agents for this model class (OVMS documents an 8K max-prompt limit on NPU, versus APEX's ~32K context target). Ollama is documented as a lifecycle/API convenience layer only — useful later for serving, not the Intel performance reference — so it is not required for this install pass.

Install both of the following. Do not skip one to save time; the whole point of the comparator is that it isn't assumed to match.

### Configuration A — OpenVINO GenAI (primary)

```yaml
config_id: "CFG-8B-OPENVINO-01"
model_artifact: "OpenVINO/Qwen3-8B-int4-ov"   # pre-converted OpenVINO IR, confirmed real and referenced in Intel's own OVMS quickstart
parameter_class: "8B"
quantization: "INT4"
runtime: "OpenVINO GenAI"
runtime_version: "2026.3.0 (or latest 2026.3.x patch — pin the exact build actually installed)"
backend: "GPU (Arc 140V)"
context_limit: 32768
```

### Configuration B — llama.cpp (independent comparator)

```yaml
config_id: "CFG-8B-VULKAN-01"
model_artifact: "Qwen3-8B-Instruct GGUF, Q4_K_M quantization"   # use an established, reputable GGUF build (e.g. Qwen's own or a well-known community quantizer); record the exact HF repo + file + SHA256 actually downloaded
parameter_class: "8B"
quantization: "Q4_K_M"
runtime: "llama.cpp"
runtime_version: "b10331 or later (record exact build/commit actually installed)"
backend: "Vulkan"   # SYCL is an acceptable alternative if Vulkan setup fails; record which was actually used
context_limit: 32768
```

## 3. Where to put things

No model-storage location has been locked anywhere in this repo yet — this is a new, small operational decision this handover is making, not a pre-existing rule. Use:

```text
C:\LocalModels\qwen3-8b\openvino-int4\      <- Configuration A files
C:\LocalModels\qwen3-8b\gguf-q4km\          <- Configuration B files
C:\LocalModels\runtimes\openvino\           <- OpenVINO GenAI / toolkit install
C:\LocalModels\runtimes\llama.cpp\          <- llama.cpp binaries
```

Keep this outside `C:\GitDev\apexai-os-meta` — model weights and runtime binaries are multi-gigabyte and must never be committed to the repo. If a different location makes more sense on the actual machine (existing drive layout, space constraints), use it and record the actual paths used in the deliverable log (Section 6) instead of guessing here.

Before starting, check available free disk space and confirm at least ~15 GB free (OpenVINO toolkit + IR model + llama.cpp + GGUF + working room). If space is tight, report it and ask before proceeding rather than filling the disk.

## 4. Install steps — Configuration A (OpenVINO GenAI)

1. Install/confirm Python (3.10-3.12 range; record the exact version used) and create a dedicated virtual environment for this work rather than installing into a shared/global environment.
2. Install the OpenVINO GenAI package set (`pip install openvino openvino-genai` or the current equivalent per OpenVINO's own 2026.3 documentation — check current install instructions rather than assuming a specific pip incantation, since packaging details drift between releases).
3. Download the pre-converted model artifact `OpenVINO/Qwen3-8B-int4-ov` from Hugging Face into `C:\LocalModels\qwen3-8b\openvino-int4\`.
4. Confirm GPU device visibility to OpenVINO (there is typically a device-enumeration call/CLI in the OpenVINO GenAI package — use it to confirm the Arc 140V GPU is detected as a usable device, not just falling back to CPU).
5. Run a minimal smoke test: load the model on the GPU device, generate a short completion for a simple fixed prompt (e.g. "Say hello and name yourself in one sentence."), and confirm it returns coherent text without error.

## 5. Install steps — Configuration B (llama.cpp)

1. Obtain a llama.cpp build with Vulkan backend support for Windows (prebuilt release binary is acceptable and preferred over building from source unless a prebuilt isn't available for this exact configuration; if you build from source, record the exact commit and build flags used).
2. Place the runtime under `C:\LocalModels\runtimes\llama.cpp\`.
3. Download a Qwen3-8B-Instruct GGUF at Q4_K_M quantization into `C:\LocalModels\qwen3-8b\gguf-q4km\` from a reputable source — prefer Qwen's own official GGUF release if one exists; otherwise a well-established community quantizer (e.g. an unsloth/bartowski-style repo), and record the exact Hugging Face repo, filename, and file size/SHA256 actually downloaded so the artifact is traceable later, matching this whole research program's evidence-grounding discipline.
4. Run a minimal smoke test via llama.cpp's CLI or server mode with the Vulkan backend selected, same fixed prompt as Configuration A, and confirm coherent output. If Vulkan fails to initialize, fall back to SYCL and record that substitution explicitly rather than silently succeeding on a different backend than requested.

## 6. Required deliverable — install log written back to the repo

After both configurations are installed and smoke-tested, create one new file:

```text
apex-meta/local-orchestration-engine/research-results/LOCAL-MODEL-INSTALL-LOG-2026-08-09-QWEN3-8B.md
```

Follow the YAML-frontmatter convention used by every other file in that folder (see any `*-RESULT.md` file for the pattern: `title`, `doc_type`, `initiative`, `created`, `status`). Set `doc_type: local_model_install_log`. The body must record, for each configuration actually installed:

- exact software versions installed (OpenVINO/OpenVINO GenAI version, Python version, llama.cpp build/commit, GPU driver version if checked);
- exact model artifact identity (Hugging Face repo, file(s), size, SHA256 if computed);
- exact install paths actually used, if different from Section 3 above;
- the smoke-test prompt used and the actual output returned, verbatim, for both configurations;
- measured resident memory at idle-loaded state for each configuration (GPU VRAM for Configuration A, RAM/VRAM split for Configuration B depending on backend) — this is a real number to capture now, not to infer;
- any deviation from this handover's instructions (different backend, different quant, different path) and why;
- any errors encountered and how they were resolved, or left unresolved with a clear note if something could not be completed;
- explicit final status per configuration: `INSTALLED_AND_VERIFIED`, `INSTALLED_WITH_ISSUES` (describe), or `FAILED` (describe and stop rather than forcing a workaround that hides the failure).

Do **not** add any pass/fail judgment about whether Qwen3-8B is a good model, whether it should be selected, or how it compares to the other candidates — that requires the actual benchmark fixtures, which is future work, not this handover.

Also update `apex-meta/local-orchestration-engine/research-results/README.md`: add one row/line pointing to the new install-log file, and add one sentence to "What has and hasn't been done" noting that Qwen3-8B is now installed in both runtime configurations, pending real benchmark execution.

## 7. Things this handover explicitly does NOT authorize

Do not:

- install or benchmark Qwen2.5-Coder-7B-Instruct or Qwen3.5-4B in this pass (separate handover);
- install either MoE candidate (Gemma-4-26B-A4B-it, Qwen3-30B-A3B) — both are documented escalation-only candidates per the MoE bandwidth note, not part of the first bake-off;
- run any of the actual CODE/WEEKLY/MA/INJECT/COEX benchmark fixtures — this handover stops at "installed and smoke-tested," not "certified";
- wire this model into any live orchestration path, planner, or routing registry;
- change any locked decision in `OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md`;
- create a git branch — work directly on `main` per the branch policy above.

## 8. Definition of done

- [ ] Configuration A (OpenVINO GenAI) installed, GPU-device-confirmed, smoke test passed.
- [ ] Configuration B (llama.cpp/Vulkan or SYCL) installed, smoke test passed.
- [ ] Resident memory measured and recorded for both.
- [ ] `LOCAL-MODEL-INSTALL-LOG-2026-08-09-QWEN3-8B.md` written with all required fields from Section 6.
- [ ] `research-results/README.md` updated to reference the new log.
- [ ] Changes committed directly to `main` with a clear commit message; pushed if the environment permits direct push, or handed off via the same git-bundle workaround used earlier this session if it does not.
- [ ] No claim of model selection, certification, or production status appears anywhere in the new content.
