---
title: "Local Model Research Result — Ranking Update from the MoE Bandwidth Finding — ChatGPT"
doc_type: local_model_research_result
initiative: local-orchestration-engine
prompt: apex-meta/local-orchestration-engine/research-prompts/LOCAL-MODEL-RESEARCH-RANKING-UPDATE-2026-08-09.md
prompt_id: G
agent: chatgpt
agent_model_label: "auto-select (model not hand-picked, to avoid biasing toward a Claude-family model)"
agent_mode: "GitHub connector (native ChatGPT Connector), reading Research Prompt G and the MoE bandwidth-vs-coexistence note directly from the repository at head commit de6f188f, plus live web search to verify both new whichllm-flagged MoE candidates against primary sources"
account_tier: "Business workspace"
run_id: R1-connector
run_started: "2026-08-09"
run_duration_seconds: null
evidence_date: 2026-08-09
chat_url: "https://chatgpt.com/c/6a7880e9-d148-83eb-9f82-86a3fc391484"
bundle_sha256: null
retries: 2
interruptions: []
uncontrolled_variables:
  - "The prompt text was typed into ChatGPT's composer as one flowing paragraph using inline (1)/(2)/(3)/(4) numbering rather than a line-broken numbered list. An earlier attempt that used literal newlines inside the typed prompt was submitted prematurely (ChatGPT's composer sends on a bare Enter keypress), truncating the intended prompt after only its first paragraph; that generation was stopped and a fresh chat was started for this run."
  - "The first fully-typed retry of this run was attempted before the task file (LOCAL-MODEL-RESEARCH-RANKING-UPDATE-2026-08-09.md) had actually been pushed to GitHub. ChatGPT's connector correctly and honestly reported that the file returned 404 Not Found via the GitHub repository-contents API at the connector-visible head commit (7b4cb3cc), explicitly stating this was not a connector/permissions failure. This was a real self-inflicted gap, not a model error; the file was committed (de6f188f) and pushed via the operator's local git client using a git-bundle handoff from the sandbox, verified landed on origin/main via a read-only git fetch, and this run was then executed against the corrected, live commit."
  - "A second in-run composer glitch occurred when retyping the corrected prompt: a page-text/screenshot check showed the composer contained only a stray dash sequence instead of the intended text, likely due to focus loss from unrelated browser tabs that had appeared around this time. The composer was cleared with Ctrl+A/Delete, the full prompt was retyped, and the complete text was verified present via get_page_text before sending."
  - "This packet explicitly defines its own evidence-class taxonomy (REPO-GROUNDED / LIVE-SEARCH-GROUNDED / DERIVED / INTERNAL-BASELINE) at the top of the response and states that internal-baseline knowledge was not relied upon to verify either candidate; this is agent-authored methodology, not an APEX-imposed constraint, but it is preserved verbatim here for traceability."
status: "raw agent output; unverified; no APEX authority"
---

# Local Model Research Result — Ranking Update from the MoE Bandwidth Finding — ChatGPT

> Operator note: this file is the verbatim (reformatted-for-markdown) output of ChatGPT executing Research Prompt G (Ranking Update from the MoE Bandwidth Finding) after reading Research Prompt G and the prior MoE bandwidth-vs-coexistence note directly from the GitHub repository via ChatGPT's native GitHub connector, combined with live web search to verify the two whichllm-flagged MoE candidates (Gemma-4-26B-A4B-it, Qwen3-30B-A3B) against primary sources. This is raw agent output. It carries no APEX authority, has not been checked against local benchmark fixtures, and does not authorize any production model or runtime selection.

Research Prompt G — Ranking Update from the MoE Bandwidth Finding

Evidence date: 2026-08-09
Repository baseline: leela-spec/apexai-os-meta, main, prompt introduced at operator-provided head de6f188f.

0. Evidence boundary and baseline

This packet distinguishes three evidence classes throughout:

REPO-GROUNDED: claims taken directly from the APEX repository through the GitHub connector. These include the current first-bake-off sequence, the 15.7 GB usable-device-memory premise, LM-23/25/26, D-S5, benchmark task classes, and the whichllm result supplied by the operator.

LIVE/SEARCH-GROUNDED: claims independently checked against current first-party model cards/configurations, official technical documentation, live Hugging Face artifact repositories, and current whichllm documentation. These are explicitly cited below.

DERIVED: arithmetic or ranking judgments computed in this packet from those sources. These are labeled as calculations/inferences rather than measurements.

INTERNAL-BASELINE KNOWLEDGE: none is relied upon for verification of either candidate. Where the previous APEX packet itself contains a research-stage expectation, it is treated as repository baseline rather than silently promoted to current external fact.

The governing APEX requirements remain unchanged: ~32K reliably usable working context is the target; reliability takes priority over raw token throughput; and laptop coexistence with browser sessions, IDE/terminals, tests, and occasional CLI agents is a hard requirement. Production model/runtime selection remains benchmark-gated.

The current first-bake-off recommendation in Section 8A remains: Qwen3-8B (primary practical-center candidate), Qwen2.5-Coder-7B-Instruct (coding specialist comparator), Qwen3.5-4B (efficiency control). Section 8A explicitly leaves the ~7–8B hypothesis at PARTIAL / UNRESOLVED, pending actual local APEX execution.

The MoE sequencing note subsequently recorded whichllm's ranking of Gemma-4-26B-A4B-it Q4_K_M at 22.8 tok/s and Qwen3-30B-A3B Q3_K_M at 33.8 tok/s, but marked its memory arithmetic as inferred and retained the earlier sequencing decision: test ~7–8B first, then escalate only if it underperforms.

One correction is necessary before using those throughput numbers: current whichllm documentation calls this field estimated_tok_per_sec and describes its speed model as bandwidth-based. Thus 22.8 and 33.8 tok/s are hardware-informed estimates using measured bandwidth, not measured local inference results from these exact model/runtime configurations. (GitHub)

1. Candidate verification

1.1 Gemma-4-26B-A4B-it — Verdict: CONFIRMED-WITH-CAVEATS

The exact model is real. Google publishes the instruction-tuned checkpoint as google/gemma-4-26B-A4B-it, and its official Gemma 4 documentation identifies the 26B A4B variant as the family's MoE model. (Hugging Face)

Architecture: exact checkpoint google/gemma-4-26B-A4B-it; total parameters 25.2B; active parameters/token 3.8B; transformer layers 30; routed experts 128; routed experts selected/token 8; shared experts 1; routing: token-level top-8 routed-expert selection plus shared expert; context 256K; modalities text + image; vision encoder ~550M parameters.

Google's model card reports 25.2B total parameters, 3.8B active, "8 active / 128 total and 1 shared." The official checkpoint configuration independently exposes num_experts: 128 and top_k_experts: 8. (Google AI for Developers)

This corrects the earlier APEX rough shorthand of "26B / ~4B active"; that shorthand was directionally right, but the verified values are 25.2B total / 3.8B active.

Q4_K_M availability: Confirmed. A live Hugging Face GGUF repository contains gemma-4-26B-A4B-it-q4_k_m.gguf, usable through llama.cpp/Ollama-compatible tooling. Hugging Face reports the remote file at 16.8 GB.

That is materially larger than the operator note's inferred 14.6 GB weight estimate. The difference is unsurprising: Q4_K_M is not literally four bits multiplied by parameter count; GGUF contains quantization metadata and uses mixed block quantization, and this Gemma checkpoint also contains architecture components beyond a simplistic scalar parameter×bit calculation.

Google itself separately publishes an approximate 14.4 GB Q4_0 loading figure for Gemma 4 26B A4B and explicitly warns that inference memory depends on runtime/environment and that KV/context memory is additional. That Q4_0 estimate is therefore not the actual Q4_K_M GGUF artifact size requested here and should not replace the observed 16.8 GB file.

Caveat: The model itself is first-party confirmed. The exact Q4_K_M artifact used for the footprint computation is a third-party quantization, not Google's canonical BF16 checkpoint. The artifact is nevertheless directly verifiable as an existing downloadable GGUF. Hence CONFIRMED-WITH-CAVEATS, not UNVERIFIED.

2. Qwen3-30B-A3B — Verdict: CONFIRMED-WITH-CAVEATS

The exact model is real. Qwen publishes Qwen/Qwen3-30B-A3B, and its official release describes it as the smaller of Qwen3's two original MoE models.

Architecture: exact checkpoint Qwen/Qwen3-30B-A3B; total parameters 30.5B; active parameters/token 3.3B; non-embedding parameters 29.9B; layers 48; experts 128; experts selected/token 8; routing: normalized token-level top-8 expert routing; attention heads Q/KV 32/4; head dimension 128; native context 32,768 on original card (extended configurations exist).

The first-party Qwen model card reports 30.5B total / 3.3B activated, 128 experts, eight activated experts, and 48 layers. Its first-party configuration records num_experts: 128, num_experts_per_tok: 8, and norm_topk_prob: true.

This therefore confirms the architectural premise behind whichllm: bandwidth demand during generation tracks a ~3.3B-active MoE computation rather than a dense 30.5B computation, even though all expert weights remain resident. Qwen's own release gives the same 128/8 expert structure.

Q3_K_M availability: Confirmed, but not in Qwen's first-party GGUF repository. Qwen's own current GGUF repo exposes Q4_K_M and larger GGUFs; its Q4_K_M file is approximately 18.6 GB. Multiple independent Hugging Face quant repositories provide the requested Q3_K_M build: tensorblock/Qwen_Qwen3-30B-A3B-GGUF lists 14.712 GB for Q3_K_M; another live Q3_K_M artifact reports approximately 14.7 GB; a separate layer-wise Q3_K_M build is displayed by Hugging Face as 13.5 GB, demonstrating that nominally identical quant labels do not guarantee byte-identical artifacts.

Reconciliation: for APEX coexistence planning, this packet uses the directly tabulated 14.712 GB build rather than selecting the smallest observed third-party artifact to manufacture a fit.

Caveat: The underlying Qwen model is first-party confirmed. The exact Q3_K_M representation is available only through third-party GGUF builds in the sources found here, and actual file size varies by conversion/build. Hence CONFIRMED-WITH-CAVEATS.

3. Verification summary

Gemma-4-26B-A4B-it: real (Google), 25.2B/3.8B, 128 routed top-8 + 1 shared, requested quant exists (Q4_K_M), verified size used 16.8 GB, verdict CONFIRMED-WITH-CAVEATS.
Qwen3-30B-A3B: real (Qwen), 30.5B/3.3B, 128 top-8, requested quant exists (Q3_K_M third-party), verified size used 14.712 GB, verdict CONFIRMED-WITH-CAVEATS.

The unverified-model concern in the earlier MoE note is therefore resolved: neither candidate is fabricated.

4. VRAM-footprint recomputation

Method: resident approximation = actual GGUF artifact size + 32K text KV-cache allowance. This remains deliberately optimistic, because it does not add runtime allocation, compute buffers, driver allocations, multimodal buffers, or other application/device consumers. A candidate that already exceeds 15.7 GB under this calculation cannot reasonably be described as coexistence-safe. There is also a GB/GiB convention ambiguity between tools, producing a few-percent uncertainty that does not change either verdict.

Qwen3-30B-A3B KV cache: official config gives 48 layers, 4 KV heads, head dimension 128, no sliding-window cache, KV caching enabled. Assuming standard FP16/BF16-equivalent two-byte KV elements: bytes/token = K+V × 48 layers × 4 KV heads × 128 dimensions × 2 bytes = 98,304 bytes/token. At 32,768 tokens: 98,304 × 32,768 ≈ 3.22 GB (≈3.00 GiB). Even at only ~8K context, the same cache is roughly 0.81 GB, yielding about 15.52 GB combined before runtime buffers — leaving only ~0.18 GB against the nominal 15.7 GB ceiling even at 8K.

Gemma-4-26B-A4B-it KV cache: Google's config is unusually favorable — 30 layers (25 sliding-attention layers with a 1,024-token window, 5 full-attention layers), 8 local KV heads at head dimension 256, 2 global KV heads at global head dimension 512. Conservative text-only 32K calculation: sliding layers ≈0.21 GB, full-attention layers ≈0.67 GB, total text KV ≈0.88 GB. This is much more KV-efficient at 32K than Qwen3-30B-A3B. However, it does not rescue the candidate: the Q4_K_M weights alone are already 16.8 GB, exceeding the entire 15.7 GB usable budget before a single KV-cache token or runtime buffer is allocated.

Recomputed VRAM-footprint table:
- Gemma-4-26B-A4B-it Q4_K_M: actual file size 16.80 GB, 32K KV allowance ~0.88 GB, approx. minimum resident total ~17.68 GB, headroom vs 15.7 GB: −1.98 GB. Coexistence verdict: FAIL / no full-resident fit.
- Qwen3-30B-A3B Q3_K_M: actual file size 14.712 GB, 32K KV allowance ~3.22 GB, approx. minimum resident total ~17.93 GB, headroom vs 15.7 GB: −2.23 GB. Coexistence verdict: FAIL at 32K.

The Gemma file size is live-artifact-grounded. The Qwen Q3_K_M figure is live-artifact-grounded and chosen conservatively from the verified Q3 builds. The KV figures are derived from the respective first-party configurations.

Consequence for LM-26: Neither candidate leaves meaningful headroom for concurrent Chromium/browser-fleet processes at APEX's ~32K working-context target. Gemma is the clearer rejection: its requested Q4_K_M artifact exceeds the stated GPU-addressable budget with weights alone. Qwen is superficially closer, but the distinction is not operationally useful: the verified 14.712 GB Q3_K_M build leaves <1 GB before KV; at 32K it exceeds the ceiling by roughly 2.23 GB; and at ~8K it has only ~0.18 GB nominal headroom before runtime allocations. That reproduces the substantive D-S5 problem. D-S5 rejected 27–32B as a default because a large resident model competes with the browser fleet in a shared-memory machine, and its explicit reversal trigger is measurable failure of the smaller tier's execution/narration quality. The MoE architecture fixes the bandwidth/computation axis; it does not fix the resident-memory/coexistence axis.

5. Throughput reconciliation

Correct evidence classification: the supplied whichllm figures (Gemma-4-26B-A4B-it Q4_K_M 22.8 tok/s, Qwen3-30B-A3B Q3_K_M 33.8 tok/s, dense ~27B comparator 3.6 tok/s) come from the repository's operator run. But whichllm itself exposes that field as estimated_tok_per_sec; its speed estimate uses device-memory bandwidth and MoE active parameters. Therefore this packet does not call 22.8 or 33.8 measured model throughput — they are predictions informed by the operator's measured ~136.5 GB/s bandwidth.

~7–8B comparison: A current OpenVINO first-party benchmark table for Core Ultra 7 258V reports Qwen3-8B INT4-MIXED generation results around 20.1–21.5 tok/s (examples: 21.51, 21.37, 21.32, 20.37, 20.08), independently supporting the previous APEX research's ~21 tok/s reference for the 7–8B tier.

Using ~21 tok/s as an approximate comparison point: Qwen3-8B INT4 OpenVINO ~20–21.5 tok/s (baseline, measured external reference); Gemma-4-26B-A4B Q4_K_M 22.8 tok/s (~1.06–1.13×, whichllm estimate not local measurement); Qwen3-30B-A3B Q3_K_M 33.8 tok/s (~1.57–1.68×, whichllm estimate not local measurement); ~27B dense Q3 3.6 tok/s (~0.17×). The comparison is not a controlled benchmark — valid only as a plausibility comparison.

Interpretation: Gemma-4-26B-A4B's projected speed advantage over an already ~20–21 tok/s Qwen3-8B path is small — no obvious APEX reason to sacrifice coexistence merely to move from roughly low-20s tok/s to another low-20s value. Qwen3-30B-A3B's projected ~34 tok/s is a real architectural signal worth preserving — if locally reproduced, it could be substantially faster than Qwen3-8B despite vastly larger total capacity, exactly the active-vs-total-parameter evidence gap Prompt G was intended to expose. But the resulting speed advantage does not address the memory failure.

6. Which APEX task classes would actually benefit?

APEX explicitly says to optimize successful bounded jobs per wall time/intervention/escalation, not raw tokens/sec. The benchmark portfolio covers CODE, WEEKLY, MA, INJECT, context, and COEX workloads.

CODE: the potentially material MoE value is quality/capability at usable decode speed, not speed alone. A 25–30B-total MoE could become useful for CODE-03 (tiny inferred fixes where the 7–8B model repeatedly misdiagnoses the defect), CODE-04 (ambiguous-bug classification if the larger MoE reduces false "I can fix this" behavior and correctly escalates), CODE-05 (bounded cross-repo tasks if larger-capacity reasoning materially improves provenance/scope correctness). However, any gain matters only if it reduces incorrect actions, CLI escalation, or human intervention — generating a bounded patch a few seconds faster is not sufficient by itself.

WEEKLY: most WEEKLY fixtures are closed-state execution, browser recovery, evidence capture, and resumability rather than open-ended reasoning. A move from ~21 to ~34 tok/s has limited value if browser/network/UI latency dominates. An MoE profile becomes interesting only if the 7–8B tier materially fails semantic UI recovery, state classification, or conditional-follow-up selection.

MA: MA-01 through MA-05 could benefit from a stronger model if the 7–8B tier exhibits repeated classification, bounded-materialization, or escalation-destination errors. Again, quality gain is the trigger, not tok/s alone.

INJECT/authority safety: there is no permissible trade of safety for speed. A configuration that generates faster but increases injection-following, authority-promotion attempts, scope drift, or missed escalation is worse under the locked benchmark law. Successful unauthorized actions must remain zero.

COEX: this is where both current MoE configurations lose most decisively. The benchmark portfolio requires model+browser, model+three subscription sessions, model+IDE/terminals, model+tests, and model+occasional Claude Code/Codex coexistence. At the requested quantizations, neither model currently has a credible full-resident 32K memory envelope for these tests.

7. Updated ranking

Two rankings must not be conflated: a throughput/capability escalation ranking (where MoE matters) and the APEX first-bake-off ranking (where coexistence is a hard gate).

Hardware-informed throughput ranking: 1) Qwen3-30B-A3B (30.5B/3.3B active, 128→8, Q3_K_M, 14.712 GB, 33.8 tok/s est., ~17.93 GB @32K) — best named MoE escalation candidate, fails current coexistence envelope. 2) Gemma-4-26B-A4B-it (25.2B/3.8B active, 128→8+shared, Q4_K_M, 16.8 GB, 22.8 tok/s est., ~17.68 GB @32K) — real and fast, but weights alone exceed budget. 3) dense ~27B whichllm candidate (Q3_K_M, not reverified by Prompt G, 3.6 tok/s) — throughput and coexistence both unattractive. This preserves the whichllm architectural finding (Qwen3-30B-A3B remains a serious later candidate) without turning it into the APEX execution order.

Updated APEX bake-off ranking: 1) Qwen3-8B (primary ~7–8B generalist) — UNCHANGED. 2) Qwen2.5-Coder-7B-Instruct (coding specialist) — UNCHANGED. 3) Qwen3.5-4B (efficiency control) — UNCHANGED. 4/escalation) Qwen3-30B-A3B Q3_K_M MoE (higher-capability escalation experiment) — NEWLY VERIFIED / retain for later testing. 5/secondary escalation) Gemma-4-26B-A4B-it Q4_K_M (alternate MoE escalation experiment) — NEWLY VERIFIED but lower priority.

Qwen3-30B-A3B ranks ahead of Gemma as the MoE escalation candidate because: its active parameter count is slightly lower (3.3B vs 3.8B); whichllm projects a substantially higher generation rate (33.8 vs 22.8 tok/s); its requested Q3_K_M weight artifact is smaller (14.712 vs 16.8 GB); although neither passes 32K coexistence, Qwen is at least capable of approaching the device ceiling at short context, whereas Gemma's Q4_K_M weights alone exceed it. That is an escalation ranking, not production selection.

8. Explicit answer: does Prompt G change the first bake-off? No.

changes_first_bakeoff_recommendation = false.

The MoE finding is valid and important, but it does not justify changing the first-bake-off order. The core reason is now stronger than in the preliminary operator note: Gemma's real Q4_K_M file is 16.8 GB, already larger than the 15.7 GB usable budget. Qwen3-30B-A3B's verified Q3_K_M artifact is ~14.7 GB; its ~32K KV requirement pushes the minimum approximation to ~17.9 GB. Runtime and concurrent-process allocations are omitted from those totals, so these are optimistic lower bounds. LM-26 makes laptop coexistence a hard requirement; LM-25 explicitly says not to optimize for raw token throughput. D-S5 already establishes the relevant precedent: a larger model is reopened when the smaller tier's execution quality measurably fails, not merely when a larger model can generate faster. Therefore the operator sequencing decision in the MoE note survives reconciliation.

Current recommendation — FIRST BAKE-OFF: 1. Qwen3-8B, 2. Qwen2.5-Coder-7B-Instruct, 3. Qwen3.5-4B efficiency control. ESCALATE ONLY IF REQUIRED BY APEX RESULTS: 4. Qwen3-30B-A3B Q3_K_M, 5. Gemma-4-26B-A4B-it Q4_K_M. This remains bake-off sequencing only — it selects neither a production model nor a production runtime.

9. D-S5 precedent check

D-S5 states: local-model size ranking 7–8B first, 13–14B second, 27–32B third; deciding criterion is competition with the browser fleet in the shared 32 GB pool; reversal trigger is measurable narration-quality failure at 7–8B. Prompt G does not falsify the deciding criterion — it falsifies only an implicit secondary assumption that a ~30B candidate must also be slow. Corrected logic: large total parameters → large resident footprint (still true); small active parameter subset → potentially fast decode (new/important); large resident footprint → poor coexistence (still true). Thus the MoE candidates survive the speed objection but still fail the D-S5 coexistence objection at the investigated quantizations. D-S5 therefore remains applicable.

10. Reversal trigger

The reversal trigger should be narrower and more operational than "a bigger model benchmarks better." Promote Qwen3-30B-A3B ahead of the ~7–8B profile for a specific APEX task class if one minimal repeated matched test demonstrates all of: (1) the best certified ~7–8B configuration materially fails that task class in repeated trials (at least 2 of 3 identical-version trials produce an incorrect final outcome, missed mandatory escalation, or CLI/human escalation caused by insufficient model reasoning); (2) Qwen3-30B-A3B passes all 3 corresponding trials with correct final outcomes and no additional authority/safety failure; (3) successful unauthorized actions remain zero; (4) the MoE configuration passes the relevant COEX scenario while loaded (typically COEX-04 for browser+IDE/terminal work or COEX-05 for browser+repo tests) without making the laptop operationally unusable. The result must be for the complete model+quant+runtime+harness configuration, not an abstract model comparison. This is a profile-specific promotion trigger, not a demand that the MoE become a global default — matching APEX's planner-routing architecture. If the MoE wins quality but fails COEX, it has not met the reversal trigger. If it wins speed but the 7–8B model already performs the task correctly, it has not met the reversal trigger.

11. Preserved disagreements and unresolved evidence

whichllm throughput wording: the repository note speaks of the bandwidth-fed result as a throughput finding, but current whichllm documentation exposes the value as an estimate, not a locally measured benchmark. Resolution: retain the finding as a strong candidate-generation signal, but require real APEX local throughput measurements before treating 22.8/33.8 tok/s as observed performance.

Qwen Q3_K_M file size: live builds disagree (~14.712 GB, ~14.7 GB, ~13.5 GB in a separate layer-wise build). Resolution: do not average them — quantized artifacts are distinct binaries. This packet uses 14.712 GB for the named footprint scenario and requires the exact SHA/configuration to be recorded in a real bake-off.

Gemma Q4 sizing: Google documents ~14.4 GB for its generic Q4_0 memory-planning estimate, while the verified requested Q4_K_M GGUF is 16.8 GB. Resolution: use the actual Q4_K_M artifact size for Prompt G — they are different representations.

KV cache/runtime implementation: the KV figures above are architecture-derived allowances, not GPU-profiler measurements. Different runtimes can quantize/offload KV, use differing allocation strategies, or place some memory in system RAM. Resolution: this uncertainty cannot rescue Gemma because its Q4_K_M artifact already exceeds 15.7 GB. It could conceivably change the exact Qwen boundary, but not establish coexistence safety without COEX measurement.

Partial GPU offload: a runtime could place part of either model in ordinary system memory, reducing GPU-resident pressure. That is not evidence that the configuration meets APEX's latency/coexistence requirement. On a unified-memory Arc 140V system, both the model and Chromium/IDE/test workload ultimately contend for the same physical-memory and bandwidth resources; the real result must therefore come from COEX-01..06 measurement rather than a "model starts successfully" test.

12. Final research judgment

Verification result: both new whichllm candidates are real, current models. Neither should remain marked unverified. Architecture result: the active-parameter finding is genuine — Qwen3-30B-A3B is a 30.5B-total/3.3B-active 128→8 MoE; Gemma-4-26B-A4B-it is a 25.2B-total/3.8B-active MoE with 128 routed experts, top-8 selection, and a shared expert. Throughput result: the MoE architecture closes the conceptual gap in A–F — it plausibly allows large-total-capacity models to decode at small-active-model speeds; Qwen3-30B-A3B is therefore a legitimate later challenger rather than something that should be rejected merely because "30B must be slow." Memory result: the operator note's rough memory numbers were optimistic — the verified Gemma Q4_K_M is 16.8 GB before KV; Qwen Q3_K_M is about 14.7 GB and becomes ~17.9 GB at APEX's ~32K context under a standard KV assumption; neither leaves the requested coexistence envelope. Ranking result: the first bake-off therefore does not change. Escalation result: Qwen3-30B-A3B should be retained by name as the first MoE escalation candidate if the ~7–8B tier materially fails an APEX task class; Gemma-4-26B-A4B-it becomes a verified secondary MoE challenger rather than an unverified label. Production decision: none — actual model/runtime certification remains gated on local APEX fixtures and COEX measurement, exactly as required by the operator lock.

```yaml
ranking_update:
  evidence_date: "2026-08-09"
  moe_candidates_verified:
    - model: "google/gemma-4-26B-A4B-it"
      verdict: "CONFIRMED_WITH_CAVEATS"
      total_params_b: 25.2
      active_params_b: 3.8
      primary_source: "Google AI for Developers Gemma 4 model card / google/gemma-4-26B-A4B-it"
    - model: "Qwen/Qwen3-30B-A3B"
      verdict: "CONFIRMED_WITH_CAVEATS"
      total_params_b: 30.5
      active_params_b: 3.3
      primary_source: "Qwen/Qwen3-30B-A3B model card, config, and Qwen3 official release"
  vram_footprint_recompute:
    - model: "google/gemma-4-26B-A4B-it"
      quant: "Q4_K_M"
      file_size_gb: 16.8
      kv_cache_allowance_gb: 0.88
      total_gb: 17.68
      headroom_vs_15_7gb: -1.98
    - model: "Qwen/Qwen3-30B-A3B"
      quant: "Q3_K_M"
      file_size_gb: 14.712
      kv_cache_allowance_gb: 3.22
      total_gb: 17.932
      headroom_vs_15_7gb: -2.232
  changes_first_bakeoff_recommendation: false
  first_bakeoff_recommendation_current:
    - "Qwen3-8B — primary practical-center generalist"
    - "Qwen2.5-Coder-7B-Instruct — coding specialist comparator"
    - "Qwen3.5-4B — efficiency control"
  escalation_candidates:
    - "Qwen3-30B-A3B Q3_K_M — first MoE escalation candidate if the 7-8B tier materially underperforms and the exact configuration passes COEX"
    - "Gemma-4-26B-A4B-it Q4_K_M — secondary MoE escalation candidate; current verified artifact exceeds the 15.7 GB budget on weights alone"
  reversal_trigger: "On the same versioned APEX task-class fixture, the best 7-8B configuration fails materially in at least 2 of 3 repeated trials while Qwen3-30B-A3B passes all 3 with zero successful unauthorized actions, and the MoE configuration simultaneously passes the corresponding COEX-04/COEX-05 coexistence test without making the laptop operationally unusable."
  unresolved_questions:
    - "Actual local decode throughput of the exact Gemma-4-26B-A4B-it Q4_K_M configuration on the operator machine; 22.8 tok/s is a whichllm estimate, not a measured local result."
    - "Actual local decode throughput of the exact Qwen3-30B-A3B Q3_K_M configuration on the operator machine; 33.8 tok/s is a whichllm estimate, not a measured local result."
    - "Exact runtime-specific GPU/system-memory split, compute-buffer overhead, and KV-cache implementation for each candidate."
    - "Whether any lower-footprint Qwen3-30B-A3B representation retains sufficient APEX execution quality while creating a genuine COEX-safe envelope."
    - "Whether partial offload can preserve acceptable latency and browser/IDE/test responsiveness under COEX-01..06."
    - "Which exact Q3_K_M artifact and SHA should become the canonical Qwen3-30B-A3B benchmark input, because independently produced Q3_K_M files differ in size."
  overall_confidence_0_to_100: 91
```
