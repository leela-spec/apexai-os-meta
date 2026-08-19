# Correction: local-executor viability assumption — high impact

**Flagging this prominently because it contradicts an assumption baked into prior FEE research and planning** (`OpenClaw Local Executor — Operator Decision Lock.md`, `OpenClaw Local Executor — Installation and Implementation Plan.md`, and the various OpenClaw setup research reports). Read this before trusting those documents' framing that a local model on this laptop is a viable executor for real agentic browser/tool workflows.

## The assumption that needs correcting

Prior research and planning treated "run a local 8B model as the bounded executor, escalate to cloud only when needed" as a workable default, with hardware/context/backend tuning framed as *optimization* to do later, not as a gating question. Repeated live testing today shows that framing was too optimistic on two independent axes — not one.

## What today's evidence actually showed

1. **Model capability**: Qwen3-8B (Q4_K_M, local) could not reliably self-correct from tool-call schema errors — it repeated identical wrong tool calls 4-6 times with zero adaptation, then fabricated a plausible-sounding answer once fully blocked, across multiple independent test runs. The exact same task, same skill instructions, same browser, run with a cloud model (`gpt-4o-mini`) succeeded cleanly — it read each error and fixed the specific thing wrong on the very next call, every time. This was tested with the local model's own thinking/reasoning mode both off and on; thinking-on did not get a clean test because of finding #2 below.

2. **Hardware/driver stability**: the local inference server (`llama-server`, Vulkan backend, Intel Arc 140V iGPU) crashed with a Vulkan `ErrorDeviceLost` fault **four separate times in one session**, reproducibly on the second inference turn of any session as context grows. Root-caused to a known, unresolved upstream Intel Arc/Vulkan driver bug (`KHR_coopmat`, matching GitHub issue #20554 on this exact GPU model, closed `not_planned` — no fix ever shipped). A workaround exists (`GGML_VK_DISABLE_COOPMAT=1`) but costs ~30-35% generation throughput, bringing sustained speed to ~5 tokens/sec.

Neither of these is a configuration mistake that got fixed today — the first is a base-model capability limit, and the second is an unresolved third-party driver bug outside this project's control. Both were previously undocumented as *live-tested facts*; they were absent from, or optimistically assumed away in, the planning documents that treated this hardware/model combination as executor-ready.

## Why this is high impact

The FEE local-executor initiative's core premise — a local model bounded-executing real multi-step browser/tool workflows, unattended, on this laptop — is not currently supported by evidence. What *is* supported:
- The **harness** (OpenClaw, the browser-automation plumbing, the managed-browser-profile approach) works correctly. Every plumbing-level bug found today (browser-policy plugin's now-removed live tab-check, action/schema issues) was fixed and confirmed working.
- The **cloud-model path** (OpenAI API key, `gpt-4o-mini`/`gpt-4.1-nano`/`gpt-5-nano`) works end-to-end today, verified against a real Perplexity session with a real page navigation and real captured answer.
- The **local-model path** does not currently work reliably for this class of task, for two independent, non-trivial-to-fix reasons.

## Recommended correction to project assumptions

- Treat local-model execution as **not yet proven**, not as a working default with optimization pending. Don't plan future FEE workflows assuming Qwen3-8B-on-this-laptop will handle them.
- Treat the **cloud-model path as the current working baseline** for anything that needs to actually run today, with local-model substitution as a to-be-revisited goal, not a near-term default.
- Before revisiting local-model viability: (a) test with the SYCL backend instead of Vulkan (may fix both the driver crash *and* restore throughput — untested as of this writing), and (b) retest tool-schema self-correction specifically with thinking mode on, which never got a clean run today due to the GPU crash blocking it.

## Supporting evidence (same-day)

- `FEE/OpenClaw_Setup/OPERATOR-HANDOVER-2026-08-11.md` — full model-comparison transcript analysis (Qwen vs GPT-4o-mini).
- `FEE/GPU_Failure/ANALYSIS-AND-PLAN-2026-08-11.md` — GPU crash root cause, confirmed workaround, and its cost.
- `FEE/GPU_Failure/Claude.md`, `FEE/GPU_Failure/Gem.md` — source research reports.
