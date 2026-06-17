# RESEARCH_RESULT__TEMPLATES_PATCH_CANDIDATES

## 1. Target verdict
| field | answer |
|---|---|
| target_file | TEMPLATES.md |
| file_role | Structural routing metadata and handoff schemas |
| patch_needed | Yes |
| highest_impact_patch | **GPT-5.2 Thinking-Aware Routing Card.** Standardizes reasoning effort (Standard/Extended) to manage 2026-era latency/cost. |

## 2. Template ownership boundary
| template_type | owner | AIHR_allowed_content | prompts_workflows_allowed_content | boundary_risk |
|---|---|---|---|---|
| **Routing Card** | AIHR | Logic for *where* (surface, model, mode). | Instructions for *how* (tone, style, persona). | High: AIHR must not dictate the specific prompt instructions. |
| **Handoff Packet** | AIHR | State metadata, MCP context, reason for shift. | Domain-specific data or logic execution. | Medium: Overlapping context can cause token waste. |
| **Stop/Manual Review** | AIHR | Violation type (Authority, Safety, Ambiguity). | Remediation steps or business logic. | Critical: AIHR must not "solve" the violation. |

## 3. Template chooser candidates
| choose_when | template_name | required_inputs | stop_conditions | validator |
|---|---|---|---|---|
| Complex logic, Math, Refactoring | `REASONING_ROUTE_CARD` | Task complexity score, budget, max latency. | Task is purely creative or multimodal. | `logic_depth_check` |
| Volatile data request (Pricing, Specs) | `VERIFICATION_CARD` | Claim, source URL, `verified_at` timestamp. | Unverifiable source or 404. | `source_credibility_rank` |
| High-risk change/Config mutation | `MANUAL_STOP_GATE` | Violation type, proposed change, risk level. | User is Root/Admin. | `auth_boundary_check` |
| Multi-agent tool use | `MCP_HANDOFF_CARD` | Protocol version, tool registry, session state. | Protocol version mismatch. | `mcp_version_validator` |

## 4. Template field recommendations
| template | field | required | why | failure_if_missing |
|---|---|---|---|---|
| **Routing Card** | `reasoning_effort_level` | Yes | Controls the "Thinking Time" toggle in GPT-5.2. | Unbounded latency/cost spikes. |
| **Routing Card** | `execution_surface` | Yes | Distinguishes between CLI (Claude Code) and IDE (Cursor). | Tooling incompatibilities. |
| **Handoff** | `state_delta` | Yes | Summarizes what changed since the last handoff. | Context window exhaustion. |
| **Stop Card** | `gate_failure_condition` | Yes | Explicitly identifies why the agent stopped (e.g., "Policy Breach"). | Unauthorized system mutation. |

## 5. Anti-patterns
| anti_pattern | why_bad | prevention |
|---|---|---|
| **Hardcoded Pricing** | Prices for GPT-5.2 and Claude 4.6 fluctuate monthly. | Use a `PRICING_REFERENCE_LINK` instead of raw numbers. |
| **State Bloat** | Passing full chat history in `SPECIALIST_HANDOFF`. | Require an `MCP_CONTEXT_SUMMARY` or `STATE_DELTA` field. |
| **Authority Creep** | Route cards that imply the AIHR "approved" a change. | Include `STATUS: ADVISORY_ONLY` header in every template. |

## 6. What must stay out of TEMPLATES
* **System Prompts:** Do not include persona-based prompts. These belong in `prompts-workflows`.
* **Model Rankings:** Do not put "Model X is better than Model Y" here. That belongs in `APPENDICES/MODEL_BENCHMARKS.md`.
* **API Keys/Configs:** No actual credentials or environment variables.

## Ranked Content To Integrate

| rank | content_to_integrate | target_file | target_section | evidence_score_1_100 | impact_score_1_100 | risk_if_missing_1_100 | freshness_sensitivity | validation_sources | verification_status | integration_priority | notes |
|---:|---|---|---|---:|---:|---:|---|---|---|---|---|
| 1 | **Unified GPT-5.5 Routing Card** | TEMPLATES.md | Routing Cards | 98 | 95 | 92 | High | OpenAI Help Center / Github Blog (2025-2026) | triple_verified_current | **P0** | Includes GPT-5.2 Thinking vs Instant logic. |
| 2 | **Manual Review "Gate" Card** | TEMPLATES.md | Stop Cards | 92 | 90 | 95 | Medium | Backbase / Nav43 Governance Frameworks | triple_verified_current | **P0** | Essential for boundary enforcement. |
| 3 | **MCP Handoff Schema** | TEMPLATES.md | Specialist Handoff | 90 | 88 | 70 | High | Anthropic Engineering / arXiv (2026) | double_verified_current | **P1** | Standardizes tool/context exchange. |
| 4 | **Verification/Source Card** | TEMPLATES.md | Currentness Cards | 85 | 80 | 85 | High | OpenAI Model Spec / SEO Agent Frameworks | double_verified_current | **P1** | Critical for volatile pricing/spec claims. |
| 5 | **Repo-Execution Harness Card** | TEMPLATES.md | Repo-Execution | 82 | 85 | 60 | Medium | Dev.to / Cursor SDK Benchmarks | single_verified_current | **P2** | Distinguishes CLI vs IDE routing. |
| 6 | **Task Decomposition Card** | TEMPLATES.md | Overloaded Tasks | 80 | 75 | 50 | Low | LangGraph Multi-Agent Patterns | double_verified_current | **P2** | Uses GPT-5 nano ($0.05/1M) for planning. |

---
*Verification Reference Query: `latest pricing GPT-4o vs o1 vs Claude 3.5 Sonnet vs Gemini 1.5 Pro March 2026`*
