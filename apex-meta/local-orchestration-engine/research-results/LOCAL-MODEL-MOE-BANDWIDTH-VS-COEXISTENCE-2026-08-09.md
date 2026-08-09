---
title: "MoE Bandwidth Finding vs. Coexistence Constraint — Bake-Off Sequencing Decision"
doc_type: operator_decision_note
initiative: local-orchestration-engine
created: 2026-08-09
authority: operator-session-2026-08-09
depends_on:
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md
  - apex-meta/local-orchestration-engine/architecture/04-decision-ledger.md
  - apex-meta/local-orchestration-engine/architecture/02-meso-module-design.md
  - apex-meta/local-orchestration-engine/DESIGN-LOCK-QA.md
  - apex-meta/local-orchestration-engine/research-results/LOCAL-MODEL-RESEARCH-F-SYNTHESIS-2026-08-09-CHATGPT-RESULT.md
  - apex-meta/local-orchestration-engine/research-results/LOCAL-MODEL-RESEARCH-F-SYNTHESIS-2026-08-09-PERPLEXITY-RESULT.md
status: "operator sequencing decision recorded; does not authorize production model selection; the ~7-8B practical center starts first and is tested before any larger/MoE candidate is revisited"
---

# MoE Bandwidth Finding vs. Coexistence Constraint — Bake-Off Sequencing Decision

## 1. What triggered this note

The operator ran (or re-ran) a hardware-aware model-selection tool, `whichllm`, after feeding it the machine's **real** measured GPU bandwidth (~136.5 GB/s) and exact device memory (16.5 GB, from Geekbench) for the Arc 140V. This is the same `whichllm` tool already referenced three times elsewhere in this repo (`DESIGN-LOCK-QA.md`, `architecture/02-meso-module-design.md`, `architecture/04-decision-ledger.md` decision D-S5) — it is not a new, unvetted source.

With real bandwidth plugged in, the ranking changed sharply from an earlier run that had no bandwidth number (`BW: N/A`) and could only rank on quality/fit, blind to speed:

| Rank | Model | Quant | Score | tok/s |
|---|---|---|---|---|
| 1 (was #3) | Gemma-4-26B-A4B-it | Q4_K_M | 80.6 | 22.8 |
| 2 | Qwen3-30B-A3B | Q3_K_M | 78.8 | 33.8 |
| 3 (was #1) | Qwen3.6-27B | Q3_K_M | 77.1 | 3.6 |

The reordering is driven by architecture: Gemma-4-26B-A4B-it and Qwen3-30B-A3B are **Mixture-of-Experts (MoE)** models with only ~3-4B *active* parameters per token, so on bandwidth-starved hardware they stream far less data per token than a dense model of similar total/quality class like Qwen3.6-27B, which crawls at 3.6 tok/s despite a comparable quality score. `whichllm` also switched several picks to lower quantization (Q4/Q3 instead of Q5/Q6) once it had the exact usable VRAM budget (15.7 GB after reserving 845 MB headroom) rather than assuming the full 16 GB.

## 2. Why the browser-agent research (Prompts A-F) missed this

Every one of this session's research prompts (ChatGPT and Perplexity, Prompts A through F) centered the operator's ~7-8B **dense**-model prior and screened larger candidates by **total** parameter count as a proxy for resource cost. Perplexity's own Prompt F packet rejected `Qwen3-Coder-30B-A3B-Instruct` with the reasoning "30B total parameters; not locally plausible on Arc 140V" — a total-parameter-count judgment, with no active-parameter/bandwidth math behind it. That heuristic is the gap: for MoE architectures, per-token throughput tracks **active** parameters, not total parameters, and none of the eight B-F agent packets computed that distinction quantitatively. This is a real evidence gap in the prior research, not a fabrication — it is recorded here so it isn't silently lost or contradicted by a later document, the same failure class already caught once this session in `MISTAKES.md` (MK-KB-010/011) for a different reason.

## 3. Why this doesn't automatically make the MoE picks the new answer

This repo already rejected a `whichllm` big-model pick once before, for a **different capability** (M5 narration/classification in the executor-platform work), in decision **D-S5** (`architecture/04-decision-ledger.md`):

> C. 27-32B (the `whichllm` pick) | **Rejected.** Would consume ~16GB — the entire GPU-addressable share of a *shared* 32GB pool — competing directly with several Chromium instances, for capability M5 never uses. Actively harmful, not merely wasteful.

That objection was about **VRAM footprint / coexistence**, not throughput. MoE architecture fixes the throughput problem (only active experts are read per token) but does **not** fix the footprint problem — all experts must still reside resident in VRAM for arbitrary per-token routing, since routing is decided dynamically. Rough-checking (INFERRED, not measured) the two new top picks against the stated 15.7 GB usable budget:

- Gemma-4-26B-A4B-it @ Q4_K_M: 26B params × ~4.5 bits/weight ≈ **14.6 GB** of weights alone, before KV cache.
- Qwen3-30B-A3B @ Q3_K_M: 30B params × ~3.75 bits/weight ≈ **14 GB** of weights alone, before KV cache.

Both would consume nearly the entire 15.7 GB ceiling — reproducing almost exactly the D-S5 objection (crowding out the "GPU-addressable share of a shared pool" that the browser fleet and other concurrent operations need), just via a faster model this time. So the MoE finding resolves the *speed* axis cleanly but does not, by itself, resolve the *coexistence* axis that is this project's actual hard requirement (`OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md`, LM-26: "laptop coexistence is a hard requirement").

**Unverified-model flag**: `Qwen3-30B-A3B` matches Alibaba's known, real Qwen3 MoE lineup and is treated as plausible. `Gemma-4-26B-A4B-it` has not been independently confirmed against this project's own fabrication-check ledger (`LOCAL-MODEL-CROSS-AGENT-COMPARISON-B-E-2026-08-09.md`, Section 5) — the prior research only verified Gemma 4 12B (dense) and Gemma 4 E2B/E4B (small NPU variants), not a 26B-A4B MoE variant. This does not mean it is wrong; it means it is not yet in the evidence trail as confirmed.

## 4. Operator decision — sequencing, not selection

**Decision: start with the ~7-8B dense practical-center candidates already recommended by both agents' Prompt F syntheses (Qwen3-8B primary, Qwen2.5-Coder-7B-Instruct as coding specialist — see `LOCAL-MODEL-CROSS-AGENT-COMPARISON-B-E-2026-08-09.md` Section 8A). Run the actual local APEX benchmark fixtures against that tier first. Only escalate toward larger candidates — including revisiting the MoE finding recorded above — if the 7-8B tier fails to perform as expected on those fixtures.**

Rationale, in the operator's own framing: the reason for not going bigger up front is not that a bigger/MoE model couldn't work — it's that the machine needs to run **other operations concurrently with the local model**, not have the local model alone occupy the shared GPU-addressable memory pool. That is the same coexistence constraint already locked in this initiative (LM-26, and D-S5's earlier rejection of `whichllm`'s previous big-model pick for an unrelated capability). Starting small and only escalating if the smaller tier underperforms is the direct, lower-risk way to honor that constraint while still leaving the door open to a faster MoE profile later if the evidence calls for it.

This is a **sequencing decision**, not a production model/runtime selection — it does not lock a final model, and it does not close off the MoE candidates. It sets the order of testing:

1. Run the already-recommended ~7-8B dense tier (Qwen3-8B, Qwen2.5-Coder-7B-Instruct, Qwen3.5-4B efficiency control) against real APEX CODE/WEEKLY/MA/INJECT/COEX fixtures, per the benchmark harness both agents designed in Prompt E.
2. If the 7-8B tier passes its hard gates and delivers acceptable execution quality within the coexistence envelope, that settles the near-term default — no need to spend the VRAM/coexistence budget on a larger model for capability the smaller tier already delivers.
3. If the 7-8B tier measurably underperforms (the existing Prompt F packets' own reversal-trigger language already anticipates this: "narration/execution quality measurably fails" is the named condition for reconsidering size), revisit this note's MoE finding as the next candidate to test — specifically Qwen3-30B-A3B, with its VRAM footprint and coexistence impact (COEX-01..06) measured explicitly rather than assumed, exactly like every other candidate in the benchmark portfolio.
4. Either way, `Gemma-4-26B-A4B-it` should go through the same real-primary-source verification the other candidates received (Section 5 of the B-E comparison) before being treated as a confirmed real model, not just a `whichllm` label.

## 5. Cross-references for future readers

- The candidate/evidence gap this note documents (MoE active-vs-total-parameter oversight) should be treated as a new row in future contradiction/evidence-freshness tables if this initiative's research is extended further.
- See `LOCAL-MODEL-CROSS-AGENT-COMPARISON-B-E-2026-08-09.md` Section 9 (Known limitations) for a pointer back to this note.
- See `architecture/04-decision-ledger.md` (D-S5) and `architecture/02-meso-module-design.md` for the pre-existing, unrelated-capability precedent this note builds on.
