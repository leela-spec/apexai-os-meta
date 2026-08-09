---
title: "Local Model Research Result — Ranking Update from the MoE Bandwidth Finding — Perplexity"
doc_type: local_model_research_result
initiative: local-orchestration-engine
prompt: apex-meta/local-orchestration-engine/research-prompts/LOCAL-MODEL-RESEARCH-RANKING-UPDATE-2026-08-09.md
prompt_id: G
agent: perplexity
agent_model_label: "auto-select (model not hand-picked, to avoid biasing toward a Claude-family model)"
agent_mode: "Chunked multi-message submission within a single thread (Perplexity has no working GitHub connector on this account), search mode explicitly set to Suche/Search (not Vertiefte Recherche/Deep Research). Research Prompt G's text and the relevant excerpts of the prior MoE bandwidth-vs-coexistence note were split across 3 sequential messages (parts 1-2 explicitly instructed 'do NOT answer yet, just acknowledge receipt'; part 3 contained the execution contract and final instruction to execute)."
account_tier: "Pro"
run_id: R1-chunked
run_started: "2026-08-09"
run_duration_seconds: null
evidence_date: 2026-08-09
chat_url: "https://www.perplexity.ai/search/9d434eb1-2d8c-4dd7-be81-b0dbb2e68478"
bundle_sha256: null
retries: 0
interruptions: []
uncontrolled_variables:
  - "The chat's search-mode toggle was found pre-set to Vertiefte Recherche (Deep Research) rather than Suche (standard search) before typing began; cause unclear, possibly leftover UI state. Deep Research begins executing immediately on submission and would not have waited for the planned multi-part chunking, so the mode was explicitly switched to Suche before Part 1 was typed, preserving the proven chunked-submission technique used for the prior Prompt F run."
  - "Repeated 'CDP sendCommand Input.dispatchKeyEvent timed out after 30000ms' errors occurred at least 3 times across the 3-part submission. Per the established false-alarm-verification procedure, each occurrence was followed by a screenshot or get_page_text check confirming the full intended text was actually present in the composer despite the timeout error; no retries or data loss resulted."
  - "The final answer initially appeared truncated mid-sentence on a get_page_text read ('...and the conclusion that the first benchmark-not more landscape rese'). Per MK-KB-011, the page was reloaded (fresh navigation to the same conversation URL) and re-extracted; the reloaded, complete text confirmed the response was genuinely complete (ending cleanly at 'Overall confidence: 86/100' plus a normal sources/follow-ups footer). This was a rendering-lag false alarm, not real truncation, and no continuation message was sent."
status: "raw agent output; unverified; no APEX authority"
---

# Local Model Research Result — Ranking Update from the MoE Bandwidth Finding — Perplexity

> Operator note: this file is the verbatim (reformatted-for-markdown) output of Perplexity executing Research Prompt G (Ranking Update from the MoE Bandwidth Finding) after receiving Research Prompt G and relevant excerpts of the prior MoE bandwidth-vs-coexistence note via a 3-part chunked message submission (Perplexity has no working GitHub connector on this account), combined with Perplexity's own live web search to verify the two whichllm-flagged MoE candidates. This is raw agent output. It carries no APEX authority, has not been checked against local benchmark fixtures, and does not authorize any production model or runtime selection.

Prompt G — MoE Ranking Update

Executive verdict

No—the finding does not change the first-bake-off order. It adds two documented later-escalation candidates, especially Qwen3-30B-A3B, but both remain poor fits for the machine's 15.7 GB usable GPU-memory budget once weights, KV cache, runtime allocations, and coexistence requirements are included.

The central correction is important: MoE sparsity reduces compute and bandwidth per generated token, but does not reduce resident weight memory proportionally. D-S5 therefore still applies.

Model verification

Candidate: Gemma-4-26B-A4B-it — Verification verdict: CONFIRMED WITH CAVEATS — Evidence: Google's official model card identifies it as a Gemma 4 MoE model with 25.2B total parameters, 3.8B active parameters, 128 total experts, 8 active experts plus one shared expert, and a 256K context window. (huggingface)

Candidate: Qwen3-30B-A3B — Verification verdict: CONFIRMED — Evidence: Alibaba/Qwen's primary model card identifies 30.5B total parameters, 3.3B active parameters, 128 experts, 8 activated experts, and 32,768-token native context. The official GGUF card also documents Q3/Q4/Q5/Q6/Q8 quantizations and llama.cpp usage. (huggingface)

The caveat on Gemma is not that the model appears fabricated—it is now independently confirmed through Google's model card—but that the exact Q4_K_M artifact used in the whichllm result is a third-party GGUF conversion, not an official Google-distributed GGUF. The available conversion listing reports approximately 17.04 GB for the standard Q4_K_M file. (huggingface)

Recomputed memory impact

The following uses actual published GGUF file sizes where available. The KV figures are planning allowances, not measurements on the APEX machine. Approximately 0.5 GB is used for a 4K-token KV cache and no less than 0.5 GB is reserved beyond that for allocator/runtime overhead; actual usage depends on backend, context length, flash-attention mode, and offload configuration.

- Gemma-4-26B-A4B-it Q4_K_M: Published GGUF file size ~17.04 GB, 4K KV allowance ~0.5 GB, Weights + KV ~17.54 GB, Remaining from 15.7 GB: −1.84 GB. Coexistence verdict: Does not fit fully in usable VRAM; offload required.
- Qwen3-30B-A3B Q3_K_M: Published GGUF file size ~14.1 GB, 4K KV allowance ~0.5 GB, Weights + KV ~14.6 GB, Remaining from 15.7 GB: ~1.1 GB. Coexistence verdict: Technically marginal before runtime overhead.
- Qwen3-30B-A3B Q3_K_M plus conservative runtime reserve: Weights + KV ~15.1 GB, Remaining from 15.7 GB: ~0.6 GB. Coexistence verdict: Fails the coexistence margin in practice.

The Qwen3 file-size evidence is approximately 14.1 GB for the Q3_K_M artifact, correcting the internal estimate only slightly. The Gemma estimate of approximately 14.6 GB was materially optimistic for the standard Q4_K_M file: the currently listed artifact is about 17.04 GB, with another listing reporting approximately 16.8 GB. (huggingface)

Qwen3's architecture makes its KV estimate comparatively favorable: the official card reports 48 layers and four KV heads, so its KV cache is not proportional to the full 30.5B parameter count. However, that does not solve the weight-footprint problem. Gemma's sliding-window attention may also reduce long-context pressure, but its Q4 file already exceeds the entire 15.7 GB budget before KV cache.

Updated ranking (throughput ranking from the new whichllm run)

1. Gemma-4-26B-A4B-it — MoE, 25.2B total / 3.8B active — Q4_K_M — score 80.6 — 22.8 tok/s — Memory status: Fails 15.7 GB fully resident.
2. Qwen3-30B-A3B — MoE, 30.5B total / 3.3B active — Q3_K_M — score 78.8 — 33.8 tok/s — Memory status: Marginal weights-only; poor coexistence.
3. Qwen3.6-27B — Dense — Q3_K_M — score 77.1 — 3.6 tok/s — Memory status: Slow and memory-heavy.
Existing bake-off tier: Qwen3-8B, Ministral 3 8B, Qwen2.5-Coder-7B, controls, and one 12–14B challenger — Mostly dense — As previously specified — To be measured locally — Designed for coexistence.

The MoE result is a valid throughput-ranking update, not a replacement of the resource-aware bake-off recommendation. The prior ledger decision D-S5 explicitly rejected the 27–32B class because it would consume roughly the entire GPU-addressable share of a shared 32 GB pool and compete with Chromium, not because it was too slow. The repository's searchable ledger records D-S5's decision as the structured 7–8B path, with the larger model rejected because of shared-pool memory pressure. (huggingface)

Recommendation decision

Decision: retain the existing first-bake-off order.

- Keep Qwen3-8B as the primary first candidate.
- Keep Ministral 3 8B Instruct 2512 as the main challenger.
- Keep the coding and efficiency controls already specified.
- Add Qwen3-30B-A3B as the preferred later MoE escalation candidate.
- Add Gemma-4-26B-A4B-it as a conditional later escalation candidate, subject to confirming a backend-compatible quantization that fits with an acceptable coexistence margin.
- Do not select either MoE model as a production model through this packet.

Qwen3-30B-A3B is the stronger escalation candidate because its published Q3 file is smaller and the reported whichllm throughput is higher. Gemma has the stronger reported score but its standard Q4 file is already larger than the usable VRAM budget.

Minimum promotion gate

The smallest concrete local result that would justify promoting an MoE candidate ahead of the 7–8B tier is a same-harness, same-prompt comparison showing all of the following:

1. On a fixed 40–50-item APEX task set covering orchestration, structured output, tool-use planning, and the M5 capability, the MoE candidate achieves at least the Qwen3-8B pass rate plus 5 percentage points.
2. It completes three repeated runs with zero out-of-memory events.
3. Its measured peak GPU allocation stays at or below 15.0 GB, leaving at least 0.7 GB of the 15.7 GB usable budget for fluctuation.
4. Its median generation throughput is at least 20 tok/s under the selected backend, while preserving the required output format and tool-call correctness.
5. It does not materially degrade coexistence: Chromium and the rest of the normal APEX software stack remain responsive during the test.

For Qwen3-30B-A3B, this would require validating that the apparent 33.8 tok/s whichllm estimate survives real local execution without unacceptable offload or browser contention. For Gemma, the standard Q4_K_M artifact would first need either partial offload acceptance or a smaller compatible quantization; otherwise it cannot meet the memory gate.

Evidence and confidence

Search-grounded: model existence, official parameter/active-parameter counts, expert counts, context limits, official Qwen quantization support, and third-party GGUF file sizes. (huggingface, multiple sources)

Internal/project-grounded: the whichllm scores and throughput values, the 15.7 GB usable budget, measured approximately 136.5 GB/s bandwidth, the existing shortlist, the D-S5 rationale, and the conclusion that the first benchmark—not more landscape research—is the next decision point. The D-S5 repository lookup was performed against leela-spec/apexai-os-meta; a differently named public APEX OS repository surfaced during discovery did not contain the cited ledger.

Inferred rather than measured: the 0.5 GB KV-cache allowance, the 0.5 GB runtime reserve, and the resulting coexistence margin. These must be verified with the actual OpenVINO/llama.cpp/Ollama configurations.

Overall confidence: 86/100. Confidence is high that both model families are real and that MoE throughput exposes a legitimate ranking gap. Confidence is lower on exact runtime memory because GGUF conversion, backend allocator behavior, context length, and GPU offload policy can change the measured footprint.

> Operator note: the original response cited 32 web sources inline; these are not individually reproduced in this file. See the live conversation at the chat_url above for the full source list.
