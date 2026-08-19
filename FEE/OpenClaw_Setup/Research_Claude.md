# Local LLM Context Sizing & Agentic Execution — Reality Check

Your architecture principle (local model as pure mechanical executor, no reasoning) is sound and the payload-transfer pattern is a known, named pattern. Below is the quantitative breakdown per question, with explicit uncertainty flags where the answer depends on backend/build specifics I cannot verify from your machine directly.

## 1. Deterministic Payload Transfer

This pattern has an established name: **context offloading / the "handle, not payload" pattern** (also called "pointer passing" or "reference-based tool results" in agent-framework literature). The rule: large tool outputs are written to durable storage (filesystem, object store, KV store) and the model receives only a compact handle — an id, byte count, hash/preview — never the blob itself. This is exactly how serious long-running coding and deep-research agents avoid drowning in tool output over hundreds of steps. [viralruparel](https://viralruparel.com/blog/tool-output-offloading-filesystem-agent-context)

Your OpenClaw runtime already implements a version of this natively: it derives a live tool-result char cap from the model's context window (16,000 chars below 100K tokens) and caps any single tool result at 30% of the context window regardless. So even without your own deterministic layer, OpenClaw would truncate — but truncation is not the same guarantee as never routing the payload through context at all, so your explicit deterministic layer is still the right call, not redundant.[2]

**Pitfalls with this pattern**, since the model never sees the payload:
- **Provenance verification**: the model can only trust the hash/byte-count receipt, not confirm semantic correctness. If the browser tool captures the wrong DOM region (e.g., a stale cached response, or a truncated stream mid-generation), a byte count and hash will look "successful" while being wrong. Mitigate with a deterministic completion signal (e.g., poll for a stop-generating UI state change, not just "text exists") before the capture tool fires.
- **Silent truncation**: if the deterministic capture tool itself has an internal length cap and the response exceeds it, the model receives a "successful" receipt for truncated data unless the tool explicitly flags truncation in the receipt.
- **Hash mismatch is your only integrity check** — make sure the orchestration layer diffs hash-of-capture against something (e.g., re-fetch and compare) at least occasionally, since the model itself cannot spot-check content.

## 2. Context Window Sizing — 32K Floor, Is It Enough?

Given your floor is fixed at 32K, the real question is whether the remaining (non-payload) work fits comfortably. Two independent, real-world data points bound this:

The single biggest context risk in your stack is **raw accessibility-tree snapshots**, not the prompt or schema. A measured example: a real ad-heavy page returned ~598,000 tokens as a raw A11y tree; even a moderate content page (Hacker News front page) cost ~16,000 tokens per snapshot. Your workflow calls for a snapshot on **every UI interaction step** (mode select, model select, reasoning-mode select, composer text verify, submit) — that's easily 4–6 snapshots per task before generation even starts. [docs.openclaw](https://docs.openclaw.ai/reference/token-use)

**Token budget per turn (rough, non-payload only):**

| Component | Est. tokens |
|---|---|
| System prompt (13,505 chars ≈ 3,400 tok) | ~3,400 |
| Browser tool schema (~3,600 chars) | ~900 |
| Skills text (~1,900 chars) | ~475 |
| Turn prompt to emit (300–2,000 words) | ~400–2,700 |
| Per A11y snapshot (unranked, real site) | 500–18,000+ (highly page-dependent) |
| Cron/media receipt fields (paths, byte counts) | ~50–150 per call |

If your pages are simple (HN-scale, ~16K tokens/snapshot) and you take 4 snapshots per task, that's ~64K tokens on snapshots **alone**, before system prompt or the prompt-to-emit — which already blows past 32K. If pages are ad-heavy (slickdeals-scale), 32K is exhausted by a **single** snapshot.

**Verdict: 32K has no comfortable headroom for raw accessibility-tree navigation against real-world pages.** This isn't a call to go below 32K — it's the opposite: you should either (a) go to 64K/128K, or (b) fix the actual bottleneck, which is the unranked A11y tree. A ranked-element snapshot approach (returning ~50 actionable elements instead of the full tree) cuts a 598K-token observation to ~1,300 tokens — a 99.8% reduction — and a 16K-token observation to ~587 tokens. That single change likely matters more than any context-window increase, and is cheaper (fewer prefill tokens = faster, not just fits-in-window). If you keep the raw A11y approach, 128K is the realistic floor for multi-site, multi-step navigation; 64K is workable only if you constrain the sites/pages the browser tool touches to low-complexity ones. The cron/media pipeline's own tokens (paths, byte counts, status fields) are trivial (~1–2K per run) and never the constraint. [docs.openclaw](https://docs.openclaw.ai/reference/token-use)

## 3. Qwen3-8B Specifics

Qwen3-8B natively supports **32,768 tokens**; RoPE/YaRN scaling is needed only beyond that, extending to a validated 131,072 tokens with YaRN. Qwen's own model card explicitly recommends **against** enabling YaRN if your typical context stays under 32,768 tokens, because static YaRN's constant scaling factor taxes every prompt — including short ones — even when scaling isn't needed. Since your floor is exactly 32K, you sit right at the boundary: staying at native 32K avoids YaRN's quality tax entirely; going to 64K/128K requires YaRN and should use dynamic/length-aware scaling rather than static, to avoid degrading short-prompt quality.[4][5][6]

Quality degradation at longer contexts for Q4_K_M specifically is not something I found direct benchmarked data on — flagging that as genuine uncertainty, not something to guess at. What is documented: quantization degradation and long-context degradation are two separate effects that compound, and Qwen3's official recommendation not to use YaRN below 32K is a proxy signal that beyond native range, expect measurable (not just theoretical) quality loss regardless of quant level.[6]

On model choice for pure mechanical tool execution: 2026 benchmarks put Qwen3 as one of the most reliable small-model families for tool-calling — it has the lowest rate of dropped/invalid tool calls among 8–10B local models in comparative testing, and BFCL scores for Qwen3-8B land around ~55. There are materially better *specialized* tool-callers at this size — Llama-3-Groq-8B-Tool-Use scores 89.06% on BFCL (fine-tuned specifically for function calling), and Qwen3.5-9B scores 66.1 BFCL v4 / 79.1 TAU2-bench vs Qwen3-8B's ~55. If your job is genuinely just mechanical tool execution with no need for the "thinking" mode, Qwen3.5-9B or Llama-3-Groq-8B-Tool-Use are worth benchmarking against Qwen3-8B directly on your actual tool schemas — don't take this as settled without testing on your hardware. [huggingface](https://huggingface.co/Qwen/Qwen3-8B)

## 4. KV Cache Memory — Correcting Your Estimate

Confirmed architecture: Qwen3-8B has **36 layers, 32 query heads / 8 KV heads (GQA, 4:1 grouping), head dimension 128**. Formula: KV cache bytes/token = 2 (K+V) × 36 layers × 8 KV heads × 128 head_dim × bytes_per_element.[4][10][11]

At fp16 (2 bytes/element): **144 KiB/token exactly** (0.1406 MiB/token) — your estimate is correct.

| Context | fp16 | q8_0 (~1.06 B/elem) | q4_0 (~0.56 B/elem) |
|---|---|---|---|
| 8K | 1.13 GiB | 0.60 GiB | 0.32 GiB |
| 16K | 2.25 GiB | 1.20 GiB | 0.63 GiB |
| 32K | 4.50 GiB | 2.39 GiB | 1.27 GiB |
| 64K | 9.00 GiB | 4.78 GiB | 2.53 GiB |
| 128K | 18.00 GiB | 9.56 GiB | 5.06 GiB |

Your 32K/64K fp16 estimates (~4.6 GiB / ~9.2 GiB) are correct within rounding — verified, not corrected. q8_0/q4_0 figures are approximate since exact block-scale overhead varies slightly by llama.cpp implementation version.

## 5. Hardware Fit on Arc 140V

Weights (~5 GiB Q4_K_M) + KV cache + compute buffers must all fit inside the **shared** memory pool, and this is where Windows adds a real constraint independent of your total 31.63 GB RAM. On Windows, the WDDM driver model allocates a **fixed shared-GPU-memory budget from system RAM**, separate from your total RAM — documented cases show a 96 GB-RAM machine capped at ~3.5 GB shared GPU memory by the driver, enforced identically for both Vulkan and other backends, not something llama.cpp can just override. This is a real, non-negotiable Windows/driver limit, and it is backend-independent (the cap is set by the driver, not by SYCL vs Vulkan vs OpenCL).[12]

Intel's own guidance for iGPU llama.cpp deployment says shared memory should be "more than 4.5 GB" for a 7B Q4 model and that up to roughly half of total host memory can be allocated to the iGPU on capable configurations  — but this is a general guideline, not a guarantee for your specific Lunar Lake/Arc 140V driver build. **I cannot verify your actual current WDDM shared-memory budget without you checking it directly**: run `dxdiag` → Display tab, or check Task Manager → Performance → GPU → "Shared GPU memory" to see your allocatable ceiling before assuming any context size fits. [webscraft](https://webscraft.org/blog/yaku-model-ollama-obrati-dlya-agenta-z-tool-calling-porivnyannya-i-benchmarki?lang=en)

Given ~5 GiB weights + compute buffers (typically 0.5–1.5 GiB overhead) + KV cache: at 32K fp16 KV (4.5 GiB) you're near ~10–11 GiB total — plausible if your shared-memory budget is generous, risky if it's capped low like the Radeon 890M example. **64K fp16 KV (9 GiB) pushes total to ~15 GiB**, at which point KV quantization becomes the safer path: `--cache-type-k q8_0 --cache-type-v q8_0` roughly halves KV cost (9 GiB → 4.78 GiB at 64K) with modest, generally acceptable quality loss; `q4_0` gets you further (2.53 GiB at 64K) but with more noticeable degradation, especially on long-range retrieval-style tasks. Check your actual WDDM allocation limit before locking in 64K.

## 6. Throughput on Arc 140V

I don't have a benchmark on the exact Arc 140V for Qwen3-8B Q4_K_M — flagging this explicitly rather than guessing. The closest verified data point is a direct Xe2 iGPU test (same Lunar Lake/Arc 140V class) showing SYCL FP32 far outpacing Vulkan on prompt processing: **SYCL ~180 t/s prefill vs Vulkan ~44 t/s** on a comparable small model. Separately, an Arc A770 (older, larger Xe HPG dGPU, not directly comparable but same SYCL/Vulkan gap pattern) showed SYCL prefill at 870–886 t/s vs Vulkan at 137–154 t/s for Llama-3.1-8B Q4_K_M, with generation throughput roughly comparable between backends (~16–33 t/s either way). Extrapolating cautiously to your Arc 140V: prefill will very likely favor SYCL by a large margin; generation speed differences are smaller and backend/version dependent — a newer Mesa/Vulkan report from mid-2026 shows Vulkan actually winning decode in some configurations after driver updates, so **this ranking is version-sensitive and needs re-testing on your exact driver stack**, not assumed fixed.[14][15][16]

For a 15,000–25,000 token prefill at Arc 140V-class throughput (guessing conservatively from the Xe2 data point, ~150–300 t/s prefill for an 8B Q4 model), expect roughly **50–150 seconds** for the prefill alone at that range, scaling roughly linearly with context — 32K prefill would be somewhat under double that, 64K somewhat under 4x, since prefill throughput can degrade at longer sequences due to attention cost growth. This is an estimate, not a measured number for your exact hardware — you should benchmark with `llama-bench` on your own build.

**Prompt caching absolutely helps your stable-prefix, growing-tail pattern.** llama.cpp's server has `cache_prompt: true` (default: on) which skips prefill for the matching leading prefix and only processes the new tail  [localaimaster](https://localaimaster.com/blog/best-ollama-models-tool-calling). For your multi-step agent loop with a large stable system prompt/tool schema and a growing conversation tail, this is exactly the right pattern. Flags to use: `--cache-reuse 256` (reuses cached KV via shifting even when shared text isn't a strict leading prefix), `--cache-ram -1` (removes the default 8192 MiB prompt-cache eviction cap, since your context history may exceed that), and `--slot-save-path` with the `/slots/{id}?action=save|restore` API if you want to persist a warmed cache across server restarts [18][17]. With `--parallel 1` you have exactly one cache slot, which is correct for a single sequential agent — don't add `-np` slots unless you start running concurrent independent tasks.

## 7. Backend Choice

**How to check your current backend**: run `llama-server.exe --version` or check the startup log — llama.cpp prints the active backend (e.g., "ggml_sycl_init" or "ggml_vulkan_init") in its console output at launch. If you built/downloaded a generic release binary, it's most likely the Vulkan backend, since that's the default cross-vendor build most prebuilt Windows releases ship; SYCL requires a build against Intel's oneAPI toolkit specifically.

Given the evidence: **SYCL has historically shown a large prefill advantage on Intel iGPUs/dGPUs** (180 t/s vs 44 t/s on Xe2; 870+ vs 137 t/s on Arc A770 ), making it the stronger default for your prefill-heavy, large-schema workflow. However, one mid-2026 report found Vulkan actually beating SYCL on decode throughput after Mesa driver updates, on a different Intel GPU (B70, larger MoE model)  — so backend performance ordering is genuinely shifting with driver/toolchain updates and **you should benchmark both on your exact machine with `llama-bench`** rather than trust either ranking as fixed for 2026. Intel's SYCL backend documentation also flags that large allocations (>4 GiB) on Level Zero need `GGML_SYCL_ENABLE_LEVEL_ZERO=1` (default-on) or the environment variable `UR_L0_ENABLE_RELAXED_ALLOCATION_LIMITS=1` — relevant if you go to 64K+ KV cache sizes on SYCL.[14][15][16][19]

On alternative runtimes: I don't have concrete 2026 benchmark data for IPEX-LLM or OpenVINO specifically against llama.cpp SYCL/Vulkan on Arc 140V — this is a real gap in what I can verify. Both are plausible alternatives worth testing since they're Intel-maintained and historically competitive on Intel silicon, but treat any recommendation here as a hypothesis to test, not a settled fact.

## 8. Reliability Reality Check

An 8B Q4 model doing pure mechanical execution (no reasoning) is realistic, but not risk-free. The evidence-based failure modes, ranked:

- **Tool-call JSON formatting**: even strong 8B tool-callers see meaningful failure rates as tool-schema complexity grows — BFCL data shows accuracy drops sharply from single-tool (~87–96% for frontier models, lower for 8B-class) to 20+ tool scenarios (~54–76%). Your browser tool schema alone has 54 properties — that's a large single-tool schema, and large schemas increase malformed-call risk even without multiple competing tools.[20]
- **UI-state misreads**: this is your highest practical risk given the accessibility-tree token cost problem in Q2 — if snapshots get truncated to fit context, the model may act on an incomplete view of the page and click the wrong element with high confidence.
- **Repetition/formatting drift over long tool-call chains** is a known weakness class for local 8B models specifically in multi-turn tool sequences, even when the underlying task is simple, because small models are more prone to subtle instruction drift across many turns than frontier models.[8]

Mitigations that matter more than model choice: keep tool schemas as small/decomposed as possible (split your 54-property browser tool into narrower single-purpose tools if feasible), use grammar-constrained decoding (xgrammar or GBNF) to force valid JSON structurally rather than relying on the model to get syntax right unassisted, and always verify inserted text deterministically before submit (which you're already doing) rather than trusting the model's self-report. [emergentmind](https://www.emergentmind.com/topics/qwen3-8b-decoder)

## 9a. Overnight Unattended Operation

I don't have manufacturer-specific thermal/battery data for the HP OmniBook X Flip 16 running sustained iGPU inference overnight — this needs direct measurement on your machine, not a general claim. What's structurally true regardless of specific numbers: sustained iGPU load keeps the SoC package out of low-power idle states, so a job running while otherwise idle draws continuous power at "active inference" levels for its full duration (likely tens of minutes to hours for Deep Research-class waits) rather than the near-zero idle draw of a sleeping laptop. If plugged in, this is a non-issue for daytime availability. If running on battery overnight unattended, expect meaningfully more battery drain than idle sleep — potentially fully draining the battery before morning depending on job length and battery capacity, which you should test empirically once with a single overnight run and check remaining charge, rather than assume.

## 9b. Day/Night Profile Setup

Yes — **two separate `llama-server.exe` launch configurations, swapped by Windows Task Scheduler**, is the standard and simplest pattern here; there isn't a more sophisticated well-known alternative for a single-model, single-node llama.cpp setup like yours. Concretely:

- **Daytime profile**: smaller `--ctx-size` (e.g., 32K or less if you decompose the browser tool schema per Q2/Q8), `--parallel 1`, possibly lower `--gpu-layers` if you want to reserve some iGPU headroom for foreground display/video work — launched as a scheduled task at a fixed time or on user logon.
- **Overnight profile**: larger `--ctx-size` (64K/128K if your WDDM budget from Q5 supports it), KV cache quantized (`--cache-type-k q8_0 --cache-type-v q8_0`) to fit the larger context, full `--gpu-layers 999` since nothing else competes for the GPU — launched by a Task Scheduler trigger just before your Cron/Automations job window, and a second task to kill/restart into the daytime profile each morning.

Practically: two `.bat` files (each invoking `llama-server.exe` with a distinct flag set and distinct port, or same port with a scheduled `taskkill` + relaunch), wired into Task Scheduler with time-based triggers. This is exactly the pattern you described — no better-known alternative exists for this single-server case; a more elaborate approach (e.g., a supervisor process that dynamically resizes context) exists in some MLOps/production setups but is over-engineering for a single-user local deployment.