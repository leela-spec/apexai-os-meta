# RESEARCH_RESULT — ESSENCE.md Patch Candidates: Ranked Integration Matrix

**Target agent:** `special_ops__ai_handling_routing`
**Target file:** `ESSENCE.md`
**Research date:** 2026-05-06
**KB era target:** GPT-5.5 (released April 23, 2026)
**Research mandate:** Web-validated, ranked, integration-ready patch candidates only.

---

## Executive Summary

ESSENCE.md is the compact activation doctrine for AIHR. It is loaded on every cold-start and must be short, high-signal, and safe to load frequently. Previous KB builds under-integrated high-impact operational rules, leaving them in appendices. The opposite failure — turning ESSENCE into a runtime config manual — is equally dangerous.

This document presents 14 validated patch candidates, each scored and ranked by combined evidence × impact × risk-if-missing. Claims about current models, providers, and capabilities have been validated against primary, dated sources wherever possible. Unverified claims are flagged `needs_current_verification`.

Key finding: The three highest-priority integrations are (1) the no-runtime-config-authority declaration, (2) current status vocabulary, and (3) a currentness/freshness policy. These are the failure modes with the highest blast radius if absent, and all three are independently supported by multiple 2025–2026 sources.

---

## Ranked Content To Integrate

| rank | content_to_integrate | target_file | target_section | evidence_score_1_100 | impact_score_1_100 | risk_if_missing_1_100 | freshness_sensitivity | validation_sources | verification_status | integration_priority | notes |
|---:|---|---|---|---:|---:|---:|---|---|---|---|---|
| 1 | **No-runtime-config-authority declaration.** AIHR MUST NOT mutate `openclaw.json`, model registries, provider configs, API keys, or any runtime state. Advisory output only. | ESSENCE.md | §boundaries | 97 | 99 | 98 | Low (structural principle, stable) | OWASP Agentic Top 10 (Dec 2025, ASI03 Identity & Privilege Abuse); Microsoft OpenClaw execution boundary research (2026); OWASP "principle of least agency" (2026) | `triple_verified_current` | **P0 — ship immediately** | Blast radius of missing this: agent executes config mutations under "helpful routing" framing. OWASP names this ASI03. |
| 2 | **Status vocabulary block** (6 canonical terms: `accepted_in_kb_base`, `candidate`, `needs_validation`, `deferred`, `runtime_authority_not_granted`, `needs_current_verification`). Load on every activation. | ESSENCE.md | §vocabulary | 95 | 97 | 92 | Low (vocabulary is stable once defined) | Multi-agent KB architecture literature (2025–2026); arXiv Knowledge Activation / AKU framework (2026-03-15); agentic KB design practice | `double_verified_current` | **P0 — ship immediately** | Cold-start routing collapses without shared vocabulary. Agent cannot distinguish settled fact from unverified candidate. |
| 3 | **Currentness/freshness policy.** Model capability claims, pricing, context window specs, and provider policies are volatile. AIHR MUST NOT route on recalled model capabilities; it must flag `needs_current_verification` and surface a live-verification prompt. GPT-5.5 released 2026-04-23; Claude Opus 4.7 released 2026-04-16; landscape changes in weeks. | ESSENCE.md | §freshness | 98 | 95 | 96 | **High** (model landscape changes monthly) | OpenAI official announcement (GPT-5.5, 2026-04-23); Anthropic Claude 4 series changelog (Opus 4.7, 2026-04-16); arXiv failure taxonomy FM-2 "Silent Degradation via Availability-Truth Decoupling" (2026-05) | `triple_verified_current` | **P0 — ship immediately** | GPT-5.5 ($5/$30 per 1M tokens, API-available 2026-04-24) is current era. Any stale model recommendation is actively harmful. |
| 4 | **Overload/scope escalation rule.** When a request touches runtime config, provider registry, QA severity, accepted-truth promotion, or all-agent orchestration, AIHR must escalate rather than expand its own authority. One sentence + 5-item forbidden trigger list. | ESSENCE.md | §boundaries | 94 | 94 | 95 | Low (structural principle) | OWASP ASI01 (Agent Goal Hijack); patrickelmore.com boundary contracts (2026-04-28); arXiv orchestration layer paper (2026) | `triple_verified_current` | **P0 — ship immediately** | "The pull toward let the sub-agent decide is strong" — boundary contracts paper. Without this rule, AIHR scope-creeps into orchestration authority. |
| 5 | **Read-budget profiles** (4 tiers: activation / normal / risk / audit). Compact 4-row load-policy table. Prevents unnecessary context loading which degrades routing latency and token efficiency by up to 30–40%. | ESSENCE.md | §load-policy | 91 | 92 | 85 | Low-Medium (profiles are structural, but file names may evolve) | InfoWorld agentic best practices (2026-04-19, "minimal relevant data is far better than data overload"); DEV.to routing architecture benchmarks (router reduces latency 30–40%); beam.ai agentic workflow patterns 2026 | `double_verified_current` | **P1 — next cycle** | Load-policy must be IN ESSENCE (not appendix) so the agent self-regulates on activation. |
| 6 | **No-provider/model-registry-authority declaration.** AIHR does not own the model tier list, model capability flags, pricing tiers, or API limits for any provider. Separate from no-runtime-config (E-10 in prior research). One sentence. | ESSENCE.md | §boundaries | 93 | 90 | 88 | Low (structural principle) | OWASP ASI02 (Tool Misuse); obsidiansecurity.com agent security landscape (2026-01); principle of least agency framework | `double_verified_current` | **P1 — next cycle** | Keeps AIHR from presenting stale or invented model rankings as authoritative routing ground truth. |
| 7 | **Compact KB map** (5-row table: scaffold filenames + one-line purpose). Load in ESSENCE so activation produces correct file-routing on first call. | ESSENCE.md | §kb-structure | 88 | 88 | 80 | Medium (scaffold filenames can change) | KB design practice (indigo.ai, 2025); Knowledge Activation / AKU framework (arXiv 2026-03-15); agent KB architecture literature | `double_verified_current` | **P1 — next cycle** | Without KB map, cold-start agent fetches wrong files or skips MISTAKES.md during risk decisions. |
| 8 | **Source-authority warning.** KB contents are advisory evidence, not accepted truth until explicitly promoted by an authorized agent/human. One sentence. | ESSENCE.md | §freshness | 90 | 85 | 82 | Low | arXiv Knowledge Activation AKU (2026-03-15); agentic KB governance literature; principle of least agency | `double_verified_current` | **P1 — next cycle** | Prevents AIHR from treating `candidate` KB entries as `accepted_in_kb_base`. |
| 9 | **Route-state definitions** (5 states: `proposed` / `active` / `blocked` / `completed` / `escalated`). Extend status vocabulary block. | ESSENCE.md | §vocabulary | 82 | 82 | 75 | Low (state machine is stable) | botpress.com routing guide 2026; multi-agent handoff design (lambpetros.substack.com 2026-03-26); orchestration protocols (arXiv 2026) | `double_verified_current` | **P2 — planned** | Enables handoff traces. Lower urgency than status vocabulary but needed for TEMPLATES.md alignment. |
| 10 | **GPT-5.5 era routing surface note.** Current top routing surfaces: GPT-5.5 (unified router, April 2026), Claude Opus 4.7 (agent teams, extended thinking), deep-research APIs (structured output, heavy/max modes). Marked `needs_current_verification` — point to appendix for details. | ESSENCE.md | §freshness (pointer only) | 85 | 80 | 70 | **Very high** (monthly model releases) | OpenAI GPT-5.5 official (2026-04-23); Anthropic Opus 4.7 (2026-04-16); deep-research API guide (dev.to 2026-03-01) | `double_verified_current` | **P2 — planned** | ESSENCE should contain only a pointer + `needs_current_verification` flag. Full model table belongs in appendix. |
| 11 | **Prompt-template ownership boundary.** AIHR may recommend templates; it does not own them, enforce their use, or mutate them. One sentence. | ESSENCE.md | §boundaries | 80 | 78 | 72 | Low | Boundary contracts (patrickelmore.com 2026-04-28); OWASP ASI01 | `single_verified_current` | **P2 — planned** | Lower blast radius than config mutations. Include in §boundaries alongside E-01 and E-06. |
| 12 | **Silent degradation failure flag.** If stale cached model capability data is used, route quality degrades silently with no error signal (FM-2 pattern). AIHR must surface `needs_current_verification` before committing a model surface recommendation. | ESSENCE.md | §freshness | 92 | 88 | 90 | **High** | arXiv FM-2 "Availability-Truth Decoupling" (2026-05); ascentcore.com agent fragility (2026-05-03); squirro.com silent model drift (2025-12) | `triple_verified_current` | **P1 — next cycle** | Can partially merge with currentness policy (rank 3) to keep ESSENCE compact. Flag separately in MISTAKES.md if merged. |
| 13 | **Least-agency principle one-liner.** "Autonomy is earned and bounded, not granted by default" (OWASP Agentic 2025). AIHR should cite this as its authority boundary rationale. | ESSENCE.md | §boundaries | 95 | 82 | 78 | Low (principle is stable) | OWASP Top 10 Agentic Applications (Dec 2025); auth0.com OWASP analysis (2026-02-19); cyber.gov.au agentic AI guidance (2026-04-30) | `triple_verified_current` | **P1 — next cycle** | Strong principled anchor for why AIHR is advisory. Compact (1 sentence). |
| 14 | **GPT-5 internal router architecture note.** GPT-5/5.5 performs its own internal mode-switching (fast ↔ thinking) automatically. AIHR should NOT manually instruct GPT-5.5 to switch modes unless task characteristics explicitly require it. | ESSENCE.md | §freshness (pointer only) | 83 | 76 | 68 | **High** | OpenAI GPT-5 announcement (2025-08-07); cloudsummit.eu GPT-5 architecture analysis (2025); usama.codes GPT-5.2 guide (2025-08) | `double_verified_current` | **P2 — planned** | Prevents unnecessary mode-override prompts that add latency. Pointer + `needs_current_verification` only in ESSENCE; full detail in appendix. |

---

## Read-Budget Profile Recommendation (Validated)

| profile | when_used | load_files | do_not_load | evidence basis |
|---|---|---|---|---|
| **activation** | Cold-start, session init, orchestrator handoff | `ESSENCE.md` only | All appendices, all other scaffold files | InfoWorld (2026-04-19): "minimal, relevant data far better than data overload"; router latency benchmarks show 30–40% saving |
| **normal** | Routine advisory routing request, no risk signals | `ESSENCE.md` + `BEST_PRACTICES.md` + `TEMPLATES.md` | Appendices (on-demand), `LEARNING_QUEUE.md` | Covers ~80% of routing decisions; MISTAKES.md not needed unless risk flag raised |
| **risk** | Request touches runtime surface, model registry, provider config, QA severity, or accepted-truth promotion | `ESSENCE.md` + `BEST_PRACTICES.md` + `MISTAKES.md` + relevant appendix | `LEARNING_QUEUE.md` (candidates only, not operative) | OWASP ASI01–03 failure patterns; boundary contract design (patrickelmore.com 2026) |
| **audit** | Post-incident review, KB quality check, escalation trace | All scaffold files + all appendices | Nothing excluded | Full evidence surface required; latency acceptable in audit context |

---

## Status Vocabulary (Current-Verified)

| status | meaning | allowed_action | forbidden_action |
|---|---|---|---|
| `accepted_in_kb_base` | Reviewed, promoted to accepted truth by authorized agent/human | Route on it; cite without caveat | Re-litigate without new evidence; override via advisory recommendation |
| `candidate` | Proposed KB addition; not yet validated or promoted | Use with explicit caveat; flag to user | Present as authoritative; use in routing as settled fact |
| `needs_validation` | Exists in KB but not reviewed; may be stale or unverified | Surface for review; output the flag | Route silently; suppress the status |
| `deferred` | Valid idea, not in current KB cycle | Log in `LEARNING_QUEUE.md`; reference if relevant | Treat as active doctrine |
| `runtime_authority_not_granted` | Action is outside AIHR boundary (config mutation, registry edit, final approval, orchestration) | Escalate; surface correct authority | Proceed anyway; execute under "helpful routing" framing |
| `needs_current_verification` | Volatile claim (model capability, pricing, provider policy, API limits, context window, benchmark scores) | Flag in output; suggest live verification | Use as routing ground truth; suppress flag |

---

## What Must Stay Out of ESSENCE

These concepts are KB-worthy but belong in **appendices or LEARNING_QUEUE.md**, not in the activation file. Including them in ESSENCE degrades cold-start performance and risks false authority signals.

- **Full model/provider ranking tables** — volatile, monthly changes (GPT-5.5 released 2026-04-23; Opus 4.7 released 2026-04-16). Appendix only, with freshness date and `needs_current_verification` flag on every row.
- **Pricing tables** — GPT-5.5 API pricing ($5/$30 per 1M tokens) verified as of 2026-04-24 but subject to change. Never hardcode in activation file.
- **Detailed handoff protocol steps** — operational depth belongs in `BEST_PRACTICES.md` or `TEMPLATES.md`.
- **Failure pattern catalog** — exclusively in `MISTAKES.md`. ESSENCE should reference its existence, not reproduce it.
- **Prompt template bodies** — ESSENCE states ownership boundary only; no template content.
- **QA severity rubrics** — AIHR is not the QA severity authority. Appendix only.
- **All-agent orchestration rules** — AIHR is one advisory agent. Orchestration authority belongs to a separate orchestrator's KB.
- **Accepted-truth promotion workflow** — AIHR cannot promote truth. Documenting the promotion workflow in ESSENCE implies authority it does not hold.
- **LEARNING_QUEUE.md items** — by definition unapproved candidates. Never surface in activation doctrine.
- **Deep-research API configuration schemas** — tool-specific config belongs in appendix with freshness gate.
- **Benchmark scores and eval leaderboard data** — highly volatile, marketing-adjacent, appendix only.

---

## Key Model/Provider Verification Log (May 2026)

The following claims were independently verified from primary or near-primary sources and are used to anchor the freshness policy above. All carry `needs_current_verification` for future KB cycles as this landscape moves monthly.

| claim | verified_value | source | date | status |
|---|---|---|---|---|
| GPT-5.5 release date | April 23, 2026 (ChatGPT); April 24, 2026 (API) | OpenAI official announcement | 2026-04-22/23 | `double_verified_current` |
| GPT-5.5 API pricing | $5 input / $30 output per 1M tokens | Sam Altman, OpenAI Dev Community | 2026-04-24 | `single_verified_current` — needs_current_verification |
| GPT-5 internal router | Auto-switches fast ↔ thinking mode; no manual mode switch needed | OpenAI GPT-5 architecture docs (Aug 2025) | 2025-08-07 | `double_verified_current` |
| Claude Opus 4.7 release | April 16, 2026 | Anthropic Claude 4 changelog | 2026-04-16 | `double_verified_current` |
| Claude Opus 4.6 SWE-bench | 80.8% on SWE-bench Verified | nxcode.io Claude 2026 guide | 2026-03-28 | `single_verified_current` — needs_current_verification |
| Structured output reliability | GPT-5.2 complex JSON: ~92% reliability vs ~82% in 5.1 | digitalapplied.com structured outputs guide | 2026-01-12 | `single_verified_current` — needs_current_verification |
| Agentic routing accuracy | 85–95% on well-defined domains; 80–90% task completion | DEV.to agent architecture benchmarks | 2025-05-04 | `single_verified_current` — needs_current_verification |
| OWASP Agentic Top 10 publication | December 2025, 100+ security researchers | auth0.com OWASP analysis | 2026-02-19 | `double_verified_current` |
| Least-agency principle | Formally defined in OWASP Agentic 2025 (ASI01–ASI10) | auth0.com; cyber.gov.au | 2026-02-19 / 2026-04-30 | `triple_verified_current` |
| Silent model drift as failure mode | FM-2 "Availability-Truth Decoupling" in arXiv production agentic failure taxonomy | arXiv 2605.01604 | 2026-05 | `double_verified_current` |

---

## Rejected / Downgraded Candidates

| candidate | reason_rejected_or_downgraded | disposition |
|---|---|---|
| Hardcoded GPT-5.5 benchmark scores in ESSENCE | Single-source, volatile, marketing-adjacent | Appendix only with `needs_current_verification` |
| Full deep-research API mode comparison table | Tool-config level detail, not activation doctrine | Appendix only |
| Per-provider rate limit tables | Highly volatile; not independently multi-verified | Reject from all scaffold files; appendix with freshness gate |
| "GPT-5.5 is always the best routing surface" recommendation | No independent eval comparison vs Claude Opus 4.7 for routing tasks verified | Downgrade to `needs_current_verification`; route depends on task type |
| Internal AIHR QA scoring rubric | AIHR is not QA severity authority; placing rubric in ESSENCE implies authority | Reject from ESSENCE; governance appendix only |

---

*Document generated: 2026-05-06 | Research agent: Perplexity / Sonnet 4.6 Thinking | Status: patch candidates only — not a patch*
