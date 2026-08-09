---
title: "Local Model Research Prompt — Ranking Update (MoE Bandwidth Finding)"
doc_type: research_prompt
initiative: local-orchestration-engine
created: 2026-08-09
prompt_standard: apex-meta/SmallSkills/ProThinkingPrompt/01_PRO_THINKING_PROMPT_DESIGN_STANDARD.md
authority:
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md
  - apex-meta/local-orchestration-engine/LOCAL-MODEL-BENCHMARK-PORTFOLIO-2026-08-08.md
  - apex-meta/local-orchestration-engine/research-results/LOCAL-MODEL-CROSS-AGENT-COMPARISON-B-E-2026-08-09.md
  - apex-meta/local-orchestration-engine/research-results/LOCAL-MODEL-MOE-BANDWIDTH-VS-COEXISTENCE-2026-08-09.md
---

# Research Prompt G — Ranking Update from the MoE Bandwidth Finding

## Why this prompt exists

Prompts A-F (already completed by this research program) screened local-model candidates by **total parameter count** as a proxy for resource cost, and converged on a ~7-8B dense practical center. After that synthesis was written, a hardware-aware selection tool (`whichllm`), re-run with this machine's **measured** GPU bandwidth (~136.5 GB/s) and usable VRAM (15.7 GB), ranked two Mixture-of-Experts (MoE) candidates above the previous ~27B dense pick on throughput:

| Rank | Model | Quant | Score | tok/s |
|---|---|---|---|---|
| 1 | Gemma-4-26B-A4B-it | Q4_K_M | 80.6 | 22.8 |
| 2 | Qwen3-30B-A3B | Q3_K_M | 78.8 | 33.8 |
| 3 | Qwen3.6-27B (dense) | Q3_K_M | 77.1 | 3.6 |

This is a real evidence gap in the A-F research (it never computed active-vs-total parameter throughput for MoE architectures), not a fabrication. It does not automatically overturn the ~7-8B recommendation, because the prior rejection of large `whichllm` picks (decision D-S5, `architecture/04-decision-ledger.md`) was about **VRAM footprint / coexistence**, not throughput — and MoE architecture does not reduce resident memory footprint, only per-token bandwidth cost.

## Target

Produce a **ranking-update packet**: verify the two new MoE candidates as real, current, primary-sourced models; recompute their footprint/coexistence impact against this machine's actual 15.7 GB usable budget; and state plainly whether this finding changes the first-bake-off recommendation already on record (Qwen3-8B primary + Qwen2.5-Coder-7B-Instruct specialist), or whether it only adds a documented escalation candidate for later.

This is a **ranking update**, not a production model/runtime selection. No packet may select a production model. That remains gated on real local benchmark execution (`OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md`).

## Inputs provided

1. The full B-F cross-agent comparison and its Section 8A first-bake-off recommendation.
2. The MoE-bandwidth-vs-coexistence operator decision note (Section 3's VRAM-footprint math is marked INFERRED/estimate — verify or correct it).
3. The `whichllm` re-run table above.

## Required verification (do this first, before any ranking judgment)

For **both** `Gemma-4-26B-A4B-it` and `Qwen3-30B-A3B`:

- Confirm the model exists, under that exact name/variant, from a primary source (model card, official release notes, or the maintaining organization's own announcement) — not a secondary blog post or the `whichllm` label alone.
- State its real architecture: total parameters, active parameters per token, number of experts, and expert-routing scheme, from a primary source.
- State whether `Q4_K_M` / `Q3_K_M` quantized builds of it are actually available (e.g. on Hugging Face / Ollama / a named GGUF repo), and their actual file size in GB.
- Flag explicitly if a model cannot be verified as real — do not silently drop it or silently assume it is real.

## Required reconciliation

- Recompute (do not just accept the operator note's estimate) each verified MoE candidate's approximate resident VRAM footprint at its actual quantization and file size, including a reasonable KV-cache allowance, against the stated 15.7 GB usable budget.
- State explicitly whether that footprint leaves meaningful headroom for concurrent Chromium/browser-fleet processes (the coexistence requirement, `OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md` LM-26) or would consume nearly the full budget the way the earlier ~27B dense pick did (D-S5).
- Compare each MoE candidate's *measured-real* throughput advantage against the ~7-8B tier's expected throughput, and state what APEX task classes (if any) would actually benefit from the MoE tier's speed given APEX's own latency/quality requirements — not benchmark speed for its own sake.
- Preserve disagreement rather than averaging it away if evidence conflicts.

## Required deliverables

1. Verification verdict for each MoE candidate (CONFIRMED / CONFIRMED-WITH-CAVEATS / UNVERIFIED), with primary-source citations.
2. Recomputed VRAM-footprint table (model, quant, file size, KV-cache allowance, total, headroom against 15.7 GB).
3. Updated ranking table reflecting verified figures (not the operator note's estimates).
4. Explicit answer: does this finding change the recommended first-bake-off order (Qwen3-8B primary, Qwen2.5-Coder-7B-Instruct specialist, Qwen3.5-4B efficiency control), or does it only add a named escalation candidate to test *if* the 7-8B tier underperforms?
5. Reversal trigger: name the smallest concrete local-benchmark result that would justify promoting an MoE candidate ahead of the 7-8B tier.
6. YAML:

```yaml
ranking_update:
  evidence_date: null
  moe_candidates_verified:
    - model: null
      verdict: null  # CONFIRMED | CONFIRMED_WITH_CAVEATS | UNVERIFIED
      total_params_b: null
      active_params_b: null
      primary_source: null
  vram_footprint_recompute:
    - model: null
      quant: null
      file_size_gb: null
      kv_cache_allowance_gb: null
      total_gb: null
      headroom_vs_15_7gb: null
  changes_first_bakeoff_recommendation: null  # true | false
  first_bakeoff_recommendation_current: []
  escalation_candidates: []
  reversal_trigger: null
  unresolved_questions: []
  overall_confidence_0_to_100: null
```

## Essential boundaries

- Do not select a production model or runtime.
- Do not treat `whichllm`'s label as sufficient evidence that a model exists — verify independently.
- Do not silently assume MoE architecture solves the coexistence constraint; footprint and throughput are separate axes.
- State which parts of your answer are search/tool-grounded versus internal-baseline knowledge, explicitly.

## Success condition

The run succeeds when the operator can see, with verified (not estimated) numbers, whether either MoE candidate is real and coexistence-safe on this machine, and whether that changes the order of the first bake-off or simply adds a documented later candidate.
