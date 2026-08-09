---
title: "Local Model Research Result — Ranking Update from the MoE Bandwidth Finding — Gemini"
doc_type: local_model_research_result
initiative: local-orchestration-engine
prompt: apex-meta/local-orchestration-engine/research-prompts/LOCAL-MODEL-RESEARCH-RANKING-UPDATE-2026-08-09.md
prompt_id: G
agent: gemini
agent_model_label: "auto-select via Gemini Deep Research (model not hand-picked, to avoid biasing toward a Claude-family model)"
agent_mode: "Gemini Deep Research (accessed via + -> More tools -> Deep Research in the message composer; already available on the account's existing Google AI Pro plan, no upgrade required). The full Research Prompt G text plus relevant excerpts of the prior MoE bandwidth-vs-coexistence note were submitted in a single message (Deep Research requires the complete prompt up front, unlike the chunked-submission technique used for Perplexity). Gemini generated a research plan, which was approved via the explicit 'Start research' button, then ran asynchronously to completion."
account_tier: "Google AI Pro"
run_id: R1-deepresearch
run_started: "2026-08-09"
run_duration_seconds: null
evidence_date: 2026-08-09
chat_url: "https://gemini.google.com/app/b7e8ac42ceb016e3"
bundle_sha256: null
retries: 0
interruptions: []
uncontrolled_variables:
  - "This is the first successful Gemini run in this research program. A prior (Round 1, earlier session segment) Gemini attempt failed because it disclosed a search-tool outage and produced ungrounded output; that failure mode was fixed for this run by using Deep Research mode specifically (rather than a standard Gemini chat), which requires and performs extensive live web search, and by confirming beforehand via live browser inspection that Deep Research was already available on the account's existing Pro plan with no user action needed."
  - "While Deep Research ran asynchronously ('I'm on it... you can leave this chat'), several unrelated/stray browser tabs appeared during the session: a 'Manage your Google One membership' tab (confirmed via get_page_text to show the account is already on the Google AI Pro plan with 5 TB storage, consistent with Deep Research already being available — read as an incidental UI upsell, not a real blocker), a tab showing 'Error 403 (Forbidden)!!1' for an unrelated Gemini pageId, and an old unused Perplexity tab left over from an earlier session segment that drifted on its own to an onboarding/org-create URL. All three were closed as noise; none affected the Deep Research task, which was independently confirmed still running via the chat-history sidebar and resumed at the same conversation URL."
  - "This report opens with an agent-authored 'Epistemological Framework and Live Grounding Declaration' section explicitly asserting exclusive reliance on live web search over internal training knowledge, and stating the analysis would formally halt rather than present ungrounded information as current. This is agent-authored methodology (produced in direct response to the prompt's verification requirements and the known Round-1 failure mode), not an APEX-imposed constraint, but it is preserved verbatim here for traceability."
  - "The full source list (30 sources cited directly, ~45 additional sources read but not directly cited) was not reproduced in the extracted raw text and remains available only in the live Gemini conversation at the chat_url above."
status: "raw agent output; unverified; no APEX authority"
---

# Local Model Research Result — Ranking Update from the MoE Bandwidth Finding — Gemini

> Operator note: this file is the verbatim (reformatted-for-markdown) output of Gemini executing Research Prompt G (Ranking Update from the MoE Bandwidth Finding) via Gemini Deep Research, after being given Research Prompt G's text and relevant excerpts of the prior MoE bandwidth-vs-coexistence note in a single submission, followed by explicit approval of Gemini's generated research plan. This is raw agent output. It carries no APEX authority, has not been checked against local benchmark fixtures, and does not authorize any production model or runtime selection.

APEX OS Local-Model Selection: Exhaustive Hardware Bake-Off Re-Evaluation for Mixture-of-Experts Candidates

Epistemological Framework and Live Grounding Declaration

To satisfy the strict epistemological requirements of this research program, it is explicitly affirmed that this analysis relies entirely and exclusively on live web search and real-time data retrieval provided through the current research context, rather than static or historical internal training knowledge. The verification of the existence of the specific Mixture-of-Experts (MoE) models, their architectural parameters, the availability of quantized formats, and their physical storage constraints are derived from real-time community repositories, official technical reports, and hardware testing logs current as of August 2026. If live search capabilities were unavailable, this assessment would formally halt rather than present ungrounded, potentially deprecated information as current. The data utilized herein represents the empirical, verifiable state of the open-weight machine learning ecosystem at the time of calculation, ensuring that the hardware strategy is founded upon absolute physical realities rather than theoretical projections.

Executive Summary and Strategic Bake-Off Positioning

This technical assessment investigates whether the recent emergence of high-throughput Mixture-of-Experts (MoE) architectures—specifically Google DeepMind's Gemma-4-26B-A4B-it and Alibaba Cloud's Qwen3-30B-A3B—justifies a reordering of the APEX OS local-model hardware bake-off schedule. The defining operational constraint of the APEX OS environment is a shared 32GB GPU memory pool, of which exactly 15.7 GB of usable VRAM is allocated to the local LLM. The remaining VRAM is aggressively reserved to host a concurrently running fleet of hardware-accelerated Chromium browser processes.

A prior phase of this research program established that a 7-8B dense tier—featuring Qwen3-8B as the primary generalist and Qwen2.5-Coder-7B-Instruct as the coding specialist—must be tested first to guarantee sufficient memory headroom, fundamentally blocking a ~27B dense candidate due to VRAM exhaustion. However, subsequent evaluations utilizing the whichllm hardware-aware ranking tool placed the Gemma-4-26B-A4B-it and Qwen3-30B-A3B MoE models above the 27B dense models, citing vastly superior inference throughput on bandwidth-limited hardware.

The core inquiry is whether the sparse activation patterns of these MoE models translate to a reduced resident memory footprint, allowing them to fit within the 15.7 GB budget while retaining their speed advantages. Based on an exhaustive calculation of physical file sizes, backend overheads, and the immutable requirement that all MoE routing experts must reside in VRAM to prevent catastrophic PCIe transfer latencies, this report concludes that the MoE candidates do not fit within the APEX OS memory constraints.

The final strategic recommendation remains completely unchanged: the project must bake off the ~7-8B dense tier first. The MoE candidates evaluated herein do not alter the current testing order; they are merely added to the decision ledger as documented contingency candidates, strictly reserved for scenarios where the hardware budget is physically expanded or where the deployment environment abandons the browser coexistence requirement.

The Diagnostic Imperative: Mixture-of-Experts vs. Bandwidth Limitations

To understand why the whichllm utility ranked these highly parameterized models so favorably, one must dissect the relationship between memory bandwidth, parameter count, and inference throughput. The utility is engineered to bypass static parameter-count heuristics, instead merging benchmark intelligence from independent leaderboards (such as LiveBench and Artificial Analysis) and projecting performance against the host machine's measured specifications.

For the APEX OS hardware profile, the measured GPU memory bandwidth is approximately 136.5 GB/s. In a standard dense model like the previously rejected Qwen3.6-27B, every single parameter must be loaded from VRAM into the GPU's streaming multiprocessors for every generated token. If the dense 27B model is quantized to 4-bit precision, its weight footprint is roughly 15.6 GB. Consequently, the maximum theoretical decode speed is strictly bound by the physical time required to move 15.6 GB of data across a 136.5 GB/s bus, yielding a theoretical ceiling of approximately 8.7 tokens per second, which degrades to roughly 3.6 tokens per second when factoring in real-world compute overheads and scheduler inefficiencies.

The Mixture-of-Experts architecture subverts this bottleneck. While an MoE model may contain 25 billion to 30 billion total parameters, it employs a routing layer that dynamically directs each token to a specialized subset of neural network components, known as experts. Therefore, the model only "activates" a few billion parameters during any given forward pass. When whichllm evaluates an MoE model, it calculates the bandwidth requirement based on the active parameter count rather than the total parameter count. Fetching only 3 to 4 billion active parameters (roughly 1.8 GB to 2.2 GB of data at 4-bit precision) across a 136.5 GB/s bus yields a theoretical ceiling of over 60 tokens per second. This mathematical reality is what propelled the MoE models to the top of the throughput rankings. However, this throughput calculation assumes that the entire model is already resident in VRAM, an assumption that proves fatal in the APEX OS environment.

Primary Source Verification: Gemma-4-26B-A4B-it

Verification of official model cards and repository announcements confirms that Gemma-4-26B-A4B-it is a legitimate, publicly available, open-weight multimodal model engineered by Google DeepMind — the high-end server-grade configuration within the Gemma 4 family, distinct from the edge-optimized E2B and E4B variants.

Verified specification: Model family Gemma 4 (Google DeepMind); Architecture type Mixture-of-Experts (MoE); Total parameters 25.2 billion; Active parameters 3.8 billion (per token); Expert configuration 128 total experts, top-8 routing, +1 shared expert; Layer count 30 layers (25 sliding-window, 5 full-attention); Maximum context 256,144 tokens.

The nomenclature "26B" is a categorical identifier, but precise technical documentation establishes the true total parameter count at 25.2 billion. The "A4B" designation reflects its active parameter footprint — the model engages only 3.8 billion parameters per token during text generation.

Sparsity is achieved through a highly aggressive 128-expert routing setup: for each token the router dynamically selects the 8 most relevant experts, plus one additional "always-on" shared expert that processes every token regardless of routing, ensuring foundational semantic grammar and systemic logic are never bypassed. The model also uses a "Hybrid Alternating Attention" mechanism — interleaving local sliding-window attention (1,024-token window) with global full-context attention layers at a 5:1 ratio, an 8:1 Grouped Query Attention structure on global layers, unified Key/Value tensors (K=V), and Proportional Rotary Position Embeddings (p-RoPE) rotating only 25% of vector dimensions — all aimed at compressing KV-cache memory at its 256K context scale.

Primary Source Verification: Qwen3-30B-A3B

Concurrent verification confirms that Qwen3-30B-A3B is an active, highly capable open-weight MoE model developed by Alibaba Cloud, documented extensively in the Qwen3 Technical Report — a hyper-efficient mid-tier solution providing near-frontier reasoning at a fraction of the compute cost of dense predecessors.

Verified specification: Model family Qwen 3 (Alibaba Cloud); Architecture type MoE; Total parameters 30.5 billion; Active parameters 3.3 billion (per token); Expert configuration 128 total experts, top-8 routing; Layer count 48 layers; Attention mechanism Grouped Query Attention (32 query heads, 4 KV heads).

The true total parameter count is 30.5 billion with an extremely sparse activation strategy engaging only 3.3 billion parameters per token — a 9.2:1 sparsity ratio, mirroring the compute overhead of a sub-4B dense model. A defining characteristic of the Qwen3 instruction-tuned series is dual operational modality: a non-thinking mode for rapid conversational responses and a thinking mode for complex multi-step reasoning, allowing dynamic compute-budget allocation by task complexity.

Empirical Quantization Verification: GGUF Availability and Physical Imprint

To evaluate viability against the 15.7 GB usable VRAM budget, models must be evaluated in optimized quantized GGUF formats for the llama.cpp inference engine, not native 16-bit precision.

Gemma-4-26B-A4B-it at Q4_K_M: Q4_K_M builds absolutely exist and are actively distributed by established quantization groups including the LM Studio Community team. The exact physical file size is verified at 16.8 GB. Alternative experimental formats exist (NVFP4 compressed-tensors at 15.3 GB; abliterated Q4_K_S variants at roughly 15.0 GB), but the APEX OS deployment pipeline relies on the standard llama.cpp GGUF backend, so the 16.8 GB figure is the immutable physical baseline that must be accommodated.

Qwen3-30B-A3B at Q3_K_M: Q3_K_M builds are heavily documented and widely available through authoritative repositories such as Bartowski and Unsloth. File size fluctuates marginally by block-wise optimization and calibration; repositories cite values between 14.08 GB and 14.7 GB. To adhere to strict capacity planning, the maximum reported size of 14.7 GB is used for all boundary calculations.

Summary table: Gemma-4-26B-A4B-it Q4_K_M — 16.8 GB weights only. Qwen3-30B-A3B Q3_K_M — 14.7 GB weights only. Reference: Qwen3-8B Q4_K_M — 5.03 GB.

Resident VRAM Footprint Modeling and APEX OS Coexistence

VRAM consumption is not solely determined by weight file size. Total VRAM requirement = Weights + Backend overhead + KV cache + OS/background overhead. Comprehensive benchmarking establishes backend compute-buffer/driver-context overhead at a reliable ~0.75 GB on consumer hardware, before a single model weight is loaded.

Analysis of Gemma-4-26B-A4B-it: the verified Q4_K_M weight is 16.8 GB; adding 0.75 GB backend cost yields a baseline load footprint of 17.55 GB — already ~2 GB over the 15.7 GB maximum usable VRAM budget before a single token is ingested or KV cache allocated. Gemma-4-26B-A4B-it physically cannot be loaded into the APEX OS shared memory pool.

Analysis of Qwen3-30B-A3B: the maximum verified weight is 14.7 GB; adding 0.75 GB backend overhead yields a baseline footprint of 15.45 GB. This technically fits within 15.7 GB but leaves a precarious margin of exactly 0.25 GB (250 MB) for KV cache plus coexistence overhead. Even with Qwen3's efficient 32:4 GQA ratio, an 8,000–32,000 token context window requires 0.6–1.9 GB of VRAM for KV cache — the moment a conversation starts, KV cache allocation breaches the 15.7 GB ceiling. Additionally, APEX OS requires "meaningful headroom" for concurrently running Chromium processes, which use the GPU pool for dynamic EGL/WebGL textures, compositing layers, and surface buffers — a single rich-media tab or sudden UI repaint can trigger a VRAM spike of several hundred MB. Executing the LLM with zero remaining headroom guarantees memory collisions: OOM-killed processes, crashed browser fleet, or severe PCIe swap-thrashing halting system responsiveness.

The MoE Memory Wall and PCIe Latency Penalties

A pervasive misunderstanding is that MoE's sparse active-parameter count implies proportionately sparse VRAM requirement — this is physically false. The MoE routing mechanism must execute at inference time: the router analyzes each token's hidden state and dispatches it to the top-8 of 128 experts, but since the system cannot predict which experts will be needed until the token is processed, all 128 experts' weights must be continuously resident and instantly accessible in VRAM.

The Failure of CPU Offloading: when a model's size exceeds available VRAM, engines like llama.cpp (via flags such as --n-cpu-moe) load as many layers as possible into VRAM and store excess expert weights in system RAM. If the router selects an expert in system RAM, either an activation-transfer or a weight-swap ("expert thrashing") must occur across the PCIe bus, up to two orders of magnitude slower than direct VRAM access. Because routing decisions change unpredictably token-by-token, this triggers constant non-sequential memory transfers. A model capable of 60 tok/s fully resident in VRAM can plummet to 1–3 tok/s under partial CPU offloading.

This physical reality entirely invalidates the initial whichllm throughput ranking for the APEX OS environment: whichllm's ranking assumed full VRAM residency, which neither MoE model can achieve within the 15.7 GB constraint without triggering fatal OS instability — so their theoretical throughput advantage is permanently inaccessible on this specific machine profile.

Final Strategic Recommendation and Ledger Update

The primary directive remains completely unchanged: the project must bake off the ~7-8B dense tier first.

Qwen3-8B and Qwen2.5-Coder-7B-Instruct at Q4_K_M occupy approximately 5.03 GB. VRAM calculation: Weights 5.03 GB + Backend 0.75 GB + KV cache (32K context) ~0.98 GB = Total resident footprint ~6.76 GB. Subtracting from the 15.7 GB usable limit leaves roughly 8.94 GB of unallocated VRAM — a massive, stable buffer allowing the browser fleet to allocate/deallocate graphical memory, spawn rendering threads, and process WebGL textures without starving the LLM, triggering OOM, or forcing PCIe swap-thrashing.

The MoE candidates, Gemma-4-26B-A4B-it and Qwen3-30B-A3B, are advanced architectural achievements that successfully decouple parameter scale from compute cost — but they cannot bypass the physical laws of memory storage capacity. These findings do not warrant eliminating these models from consideration, but strictly relegate them to documented contingency candidates: to be tested only if the 7-8B dense tier critically underperforms in reasoning or coding tasks, and only if project maintainers are willing to confront a binary ultimatum — tolerate severe latency degradation (sub-3 tok/s) via CPU offloading, or physically upgrade the host hardware to expand the usable VRAM pool to a minimum of 24 GB.

> Operator note: the original response cites 30 sources used directly (Hugging Face model cards/GGUF repos, the arXiv Qwen3 Technical Report, Jetson AI Lab, ApX Machine Learning, llama.cpp VRAM guides, MoE-offloading engineering sources, etc.), plus roughly 45 additional sources read but not directly cited. The full source list is not reproduced here; it remains available in the live Gemini conversation at the chat_url above.
