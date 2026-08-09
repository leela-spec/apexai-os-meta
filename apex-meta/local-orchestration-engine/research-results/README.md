# research-results — Local Model & Platform Research Outputs

This folder holds the raw and synthesized outputs of the cross-agent research program for the Local Orchestration Engine initiative: platform research (Round 1/V2) and local-model research (Prompts A through G, run against ChatGPT, Perplexity, and — for Prompts A and G — Gemini).

**Nothing in this folder carries APEX authority on its own.** Every file below is either raw agent output or a same-session desk synthesis of raw agent output. No file here selects a production model or runtime; that decision remains gated on real local benchmark execution against the operator's own machine, per `../OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md`.

## Where to start

If you only read one file, read **`LOCAL-MODEL-CROSS-AGENT-COMPARISON-B-E-2026-08-09.md`** — it is the current synthesis, corroborated by both agents' Prompt F output, with a final first-bake-off recommendation (Section 8A). Read its top-of-file reading-order note first: the document was updated in two passes, and later sections (6A/7A/8A) supersede earlier ones (6/7/8) that describe a mid-session state where things had not yet succeeded.

Then read **`LOCAL-MODEL-MOE-BANDWIDTH-VS-COEXISTENCE-2026-08-09.md`** — it records a discussion that came after that synthesis was written, and the sequencing decision it produced. Summary: a hardware-aware calculator (`whichllm`) run with this machine's real GPU bandwidth showed that MoE (Mixture-of-Experts) models can be several times faster than dense models of similar total size — a distinction none of the agent research caught, because it screened large candidates by total parameter count rather than active parameter count. That finding is real, but it doesn't automatically overturn the ~7-8B recommendation: this repo already rejected a `whichllm` big-model pick once before (decision D-S5, for an unrelated capability) specifically because it would consume nearly the entire GPU-addressable share of the shared memory pool, competing with everything else that needs to run concurrently (the browser fleet, other operations) — and the same footprint problem applies to the new MoE picks, since MoE only reduces *per-token bandwidth*, not *resident memory footprint*. **The resulting decision: start with the already-recommended ~7-8B dense tier, run it against real APEX benchmark fixtures, and only escalate to a larger/MoE candidate if the 7-8B tier measurably underperforms.** This is a sequencing decision, not a final model selection — it keeps the door open to the MoE finding without spending the coexistence budget up front. **Read that file's Section 5 (added 2026-08-09)** — Research Prompt G sent the note's own inferred VRAM-footprint numbers back out for independent verification across all three agents (ChatGPT, Perplexity, and — for the first time successfully in this program — Gemini via Deep Research). All three confirmed both MoE models are real, found their actual GGUF file sizes larger (worse) than originally estimated, and unanimously reaffirmed the sequencing decision is unchanged.

## File index

### Cross-agent syntheses (read these first)

| File | What it is |
|---|---|
| `LOCAL-MODEL-CROSS-AGENT-COMPARISON-A-2026-08-08.md` | Round 1 synthesis — Prompt A (Local Model Research Landscape) across ChatGPT, Perplexity, and Gemini. |
| `LOCAL-MODEL-CROSS-AGENT-COMPARISON-B-E-2026-08-09.md` | Round 2 synthesis — Prompts B-F across ChatGPT and Perplexity. The current, authoritative comparison and first-bake-off recommendation. Read the top-of-file reading-order note before relying on any one section. |
| `LOCAL-MODEL-MOE-BANDWIDTH-VS-COEXISTENCE-2026-08-09.md` | Post-synthesis addendum recording the `whichllm` MoE-bandwidth finding, why it doesn't simply override the B-F recommendation, and the operator's sequencing decision (7-8B first, escalate only if needed). Section 5 (added 2026-08-09) records the Prompt G ranking-update verification results — see below. |

### Raw per-agent research results, by prompt

| Prompt | ChatGPT | Perplexity | Gemini |
|---|---|---|---|
| A — Local Model Landscape | `LOCAL-MODEL-RESEARCH-LANDSCAPE-2026-08-08-CHATGPT-RESULT.md` | `LOCAL-MODEL-RESEARCH-LANDSCAPE-2026-08-08-PERPLEXITY-RESULT.md` | `LOCAL-MODEL-RESEARCH-LANDSCAPE-2026-08-08-GEMINI-RESULT.md` |
| B — Bounded Coding | `LOCAL-MODEL-RESEARCH-B-CODING-2026-08-09-CHATGPT-RESULT.md` | `LOCAL-MODEL-RESEARCH-B-CODING-2026-08-09-PERPLEXITY-RESULT.md` | not run |
| C — Weekly + Multi-Agent | `LOCAL-MODEL-RESEARCH-C-WEEKLY-MULTI-AGENT-2026-08-09-CHATGPT-RESULT.md` | `LOCAL-MODEL-RESEARCH-C-WEEKLY-MULTI-AGENT-2026-08-09-PERPLEXITY-RESULT.md` | not run |
| D — Windows/Intel Runtime | `LOCAL-MODEL-RESEARCH-D-WINDOWS-INTEL-RUNTIME-2026-08-09-CHATGPT-RESULT.md` | `LOCAL-MODEL-RESEARCH-D-WINDOWS-INTEL-RUNTIME-2026-08-09-PERPLEXITY-RESULT.md` | not run |
| E — Benchmark Harness Design | `LOCAL-MODEL-RESEARCH-E-BENCHMARK-HARNESS-2026-08-09-CHATGPT-RESULT.md` (succeeded on the 5th attempt via ChatGPT's native GitHub connector; `...-CHATGPT-ATTEMPT-FAILED.md` is kept as the historical record of the four earlier failed attempts) | `LOCAL-MODEL-RESEARCH-E-BENCHMARK-HARNESS-2026-08-09-PERPLEXITY-RESULT.md` | not run |
| F — Cross-Research Synthesis | `LOCAL-MODEL-RESEARCH-F-SYNTHESIS-2026-08-09-CHATGPT-RESULT.md` | `LOCAL-MODEL-RESEARCH-F-SYNTHESIS-2026-08-09-PERPLEXITY-RESULT.md` | not run |
| G — Ranking Update from the MoE Bandwidth Finding | `LOCAL-MODEL-RESEARCH-G-RANKING-UPDATE-2026-08-09-CHATGPT-RESULT.md` | `LOCAL-MODEL-RESEARCH-G-RANKING-UPDATE-2026-08-09-PERPLEXITY-RESULT.md` | `LOCAL-MODEL-RESEARCH-G-RANKING-UPDATE-2026-08-09-GEMINI-RESULT.md` (via Deep Research — first successful Gemini run in this program) |

### Platform research (predates the local-model rounds; unrelated but same folder)

| File | What it is |
|---|---|
| `PLATFORM-RESEARCH-HERMES-2026-08-08-V2-RESULT.md` | Platform research result for the "Hermes" candidate, V2 round. |
| `PLATFORM-RESEARCH-ODYSSEUS-2026-08-08-V2-RESULT.md` | Platform research result for the "Odysseus" candidate, V2 round. |
| `PLATFORM-RESEARCH-OPENCLAW-2026-08-08-V2-RESULT.md` | Platform research result for the "OpenClaw" candidate, V2 round. |
| `PLATFORM-RESEARCH-SYNTHESIS-2026-08-08-V2-RESULT.md` | Cross-candidate synthesis of the three platform results above. |

## What has and hasn't been done

- **Done**: all seven local-model research prompts (A-G) executed on both ChatGPT and Perplexity (A and G also on Gemini); cross-agent synthesis and fabrication spot-checks; the MoE-bandwidth finding reconciled against the existing coexistence constraint (`LOCAL-MODEL-MOE-BANDWIDTH-VS-COEXISTENCE-2026-08-09.md`); that note's own inferred VRAM-footprint numbers sent back out for independent 3-agent verification via Prompt G, with all three agents confirming the real numbers are worse than estimated and unanimously reaffirming the existing sequencing decision.
- **Not done, and the actual next step**: real local APEX benchmark execution (the CODE/WEEKLY/MA/INJECT/COEX fixtures both agents designed in Prompt E) on the operator's own machine, against the ~7-8B tier first per the sequencing decision above. Nothing in this folder substitutes for that measurement — every recommendation here remains a hypothesis until it's run.

## Related files outside this folder

- `../OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md` — the binding authority for local-model behavior and the ~7-8B practical-center prior these prompts were built to test.
- `../LOCAL-MODEL-BENCHMARK-PORTFOLIO-2026-08-08.md` — the benchmark fixture/hard-gate spec both agents' Prompt E designs implement.
- `../research-prompts/` — the seven frozen prompt files (A-G) that were sent to each agent.
- `../architecture/04-decision-ledger.md` (decision D-S5) — the earlier, unrelated-capability precedent for rejecting a `whichllm` big-model pick on VRAM-footprint/coexistence grounds, which the MoE-bandwidth addendum above builds on.
- `../orchestration/agents/knowledge-bank/MISTAKES.md` (MK-KB-010, MK-KB-011) — browser-automation lessons learned while running this research (raw GitHub URL fetches are unreliable; long chat-UI responses can misread as truncated immediately after generation).
