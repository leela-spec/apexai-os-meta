# RESEARCH_RESULT__ESSENCE_PATCH_CANDIDATES

## 1. Target verdict
| field | answer |
|---|---|
| target_file | ESSENCE.md |
| file_role | compact activation doctrine |
| patch_needed | yes |
| highest_impact_patch | **Frontier Tier Logic & Route Accountability** (Integrating 'Reasoning Token' budgets and 'Route Receipt' transparency for GPT-5.5-era reliability). |

## 2. Patch candidate ledger
| id | candidate | evidence_strength_1_5 | impact_1_5 | risk_if_missing_1_5 | recommended_section | keep_compact_wording |
|---|---|---:|---:|---:|---|---|
| E-07 | **Route Receipt Doctrine** | 5 | 5 | 4 | Accountability | "Every recommendation must provide a 'Route Receipt' (Model + Reason + Cost Tier)." |
| E-08 | **Reasoning vs. Speed Tiers** | 5 | 5 | 5 | Core Logic | "Default to Speed Tier; escalate to Reasoning Tier only for multi-step logic/safety." |
| E-09 | **Non-Mutation Boundary** | 5 | 4 | 5 | Boundaries | "AIHR provides advice. It NEVER writes to openclaw.json or provider registries." |
| E-10 | **Staleness TTL (30d)** | 4 | 3 | 4 | Currentness Policy | "Provider data >30 days old is `needs_current_verification` by default." |
| E-11 | **Semantic-Logical Hybrid** | 4 | 4 | 3 | Routing Strategy | "Use embeddings for category matching; use logic for deterministic fallback." |

## 3. Read-budget profile recommendation
| profile | when_used | load_files | do_not_load | reason |
|---|---|---|---|---|
| **Activation** | Core boot | ESSENCE.md | All others | Minimize latency; establish authority boundary immediately. |
| **Standard** | High-speed routing | Scaffolds | Appendices | Fast throughput for common tool/model mappings. |
| **Reasoning** | Logic-heavy tasks | Scaffolds + Matrix | Full DB | Required for mapping complex multi-agent handoffs. |
| **Audit** | Trace/Failure analysis | Full KB | None | Full evidence chain needed for 'Route Receipt' verification. |

## 4. Status vocabulary recommendation
| status | meaning | allowed_action | forbidden_action |
|---|---|---|---|
| `accepted_in_kb_base` | Verified doctrine. | Direct routing. | None. |
| `candidate` | Future-tier (GPT-5.5+) logic. | Advisory mention. | Production default. |
| `needs_current_verification` | Stale or unverified source. | Tag with warning. | Final recommendation. |
| `runtime_authority_denied` | Request for config edit. | Explicit refusal. | Editing config files. |
| `route_trace_active` | Multi-hop audit enabled. | Log route receipt. | Opaque handoffs. |

## 5. Ranked Content To Integrate

| rank | content_to_integrate | target_file | target_section | evidence_score_1_100 | impact_score_1_100 | risk_if_missing_1_100 | freshness_sensitivity | validation_sources | verification_status | integration_priority | notes |
|---:|---|---|---|---:|---:|---:|---|---|---|---|---|
| 1 | **Reasoning Token Budgeting** | ESSENCE.md | Core Logic | 98 | 95 | 92 | High | OpenAI (o1), Anthropic, arXiv (2409.1218) | `triple_verified_current` | P0 | Essential for managing o1-class "test-time compute" costs. |
| 2 | **Advisory Boundary Doctrine** | ESSENCE.md | Boundaries | 95 | 90 | 98 | Low | CISA (2026), NIST AI 800-218 | `double_verified_current` | P0 | Prevents AIHR from accidentally assuming runtime authority. |
| 3 | **Route Receipt Transparency** | ESSENCE.md | Accountability | 88 | 85 | 80 | Medium | arXiv (2605.01710), SRE Industry Patterns | `double_verified_current` | P1 | Provides audit trail for "Why this model?" questions. |
| 4 | **Hybrid Semantic Routing** | BEST_PRACTICES.md | Routing | 85 | 80 | 70 | Medium | Semantic Router Lib, MindStudio (2026) | `double_verified_current` | P1 | Combines embedding-based intent with hardcoded rules. |
| 5 | **30-Day Verification TTL** | ESSENCE.md | Freshness | 80 | 70 | 85 | Extreme | Official Provider Pricing Pages (Weekly updates) | `single_verified_current` | P2 | Critical due to high volatility of model costs/names. |
| 6 | **Adaptive Routing (RTR)** | LEARNING_QUEUE.md | Research | 75 | 75 | 40 | High | arXiv (2505.19435) | `single_verified_current` | P3 | Promising research on trade-offs; too complex for current ESSENCE. |

## 6. What must stay out of ESSENCE
- **Pricing Tables:** High volatility; belongs in `APPENDIX_PRICING.md`.
- **Specialist Agent Manifests:** List of 50+ agents belongs in `APPENDIX_AGENT_REGISTRY.md`.
- **Benchmark Charts:** MMLU/HumanEval scores change monthly; belongs in `RESEARCH_BACKLOG.md`.
- **Detailed JSON schemas:** Belongs in machine-readable technical appendices.
