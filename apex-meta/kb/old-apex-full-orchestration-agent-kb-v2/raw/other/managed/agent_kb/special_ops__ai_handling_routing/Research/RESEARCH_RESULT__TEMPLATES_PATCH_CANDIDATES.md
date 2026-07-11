This is excellent — three rounds of fresh, high-quality primary sources. Now I'll synthesize the full ranked integration matrix.

---

# RESEARCH_RESULT__TEMPLATES_PATCH_CANDIDATES

_(Web-validated edition — May 2026)_

---

## 1. Target Verdict

|field|answer|
|---|---|
|target_file|TEMPLATES.md|
|file_role|Reusable structural routing/handoff/verification cards — not prompts|
|patch_needed|**yes — high urgency**|
|highest_impact_patch|Add mandatory universal field schema (`card_type`, `advisory_only_flag`, `confidence_level`, `escalation_path`) to all route cards, grounded in 2026 agent reliability and HITL research|
|second_impact_patch|Add `manual_review_stop_card` with `resume_condition` + `irreversibility_score` gate, sourced from confidence-threshold and agent security evidence|
|third_impact_patch|Add `currentness_verification_card` with `volatility_tier` + `needs_current_verification` flag for all model/provider/pricing claims|
|lowest_priority|`fallback_path_card` — defer to LEARNING_QUEUE if scaffolding is already overloaded|

---

## 2. Template Ownership Boundary

|template_type|owner|AIHR_allowed_content|prompts_workflows_allowed_content|boundary_risk|
|---|---|---|---|---|
|routing_card|AIHR|Route signal, selected surface (singular), rejected surfaces, confidence level, escalation path|Full prompt text, instruction payloads, persona config|**HIGH** — AIHR must carry only structure, never instructions botpress+1|
|specialist_handoff_card|AIHR|Trigger condition, target_agent_id, context_payload schema, return_contract|Receiving agent's internal instructions, task prompts|MEDIUM — handoff metadata is routing; agent instructions are not agentic-design+1|
|currentness_verification_card|AIHR|Claim volatility tier, `needs_current_verification` flag, `last_verified_date`, source_type|Source crawl/retrieval logic, re-verification pipelines|LOW — AIHR raises the flag; does not resolve it [deploymentsafety.openai](https://deploymentsafety.openai.com/gpt-5-5)|
|source_authority_card|AIHR|Tier label (primary/secondary/unverified), use_limit, provenance note|Source discovery, ranking algorithms|LOW|
|repo_execution_vs_chat_route_card|AIHR|Execution surface selector, `reversibility_flag`, `irreversibility_score`, risk_level|Tool invocation logic, repo credentials, sandbox config|**CRITICAL** — AIHR selects surface; GPT-5.5/Codex sandbox config belongs to runtime, not AIHR [deploymentsafety.openai](https://deploymentsafety.openai.com/gpt-5-3-codex/cyber-safeguards)|
|manual_review_stop_card|AIHR|Stop trigger, reason code, reviewer_role, resume_condition, `human_approval_required` flag|Reviewer workflows, SLA, ticketing system integration|HIGH — AIHR raises stop; owns no downstream process zylos+1|
|overloaded_task_decomposition_card|AIHR|Decomposition signal, subtask_ids[], orchestration_route|Subtask execution logic, resource allocation|MEDIUM — AIHR proposes decomposition; does not orchestrate execution [dev](https://dev.to/akshaygupta1996/the-orchestrator-pattern-routing-conversations-to-specialized-ai-agents-33h8)|
|fallback_path_card|AIHR|Failed route, fallback surface, `degraded_mode_flag`, retry_eligible|Retry logic, circuit-breaker implementation|MEDIUM|
|prompt cookbook entries|**prompts_workflows**|None|All|**CRITICAL** — must never enter TEMPLATES.md|
|openclaw.json / model registry mutations|**runtime config**|Reference by logical name only, never config paths|None — AIHR advisory only|**CRITICAL**|
|MCP server config / OAuth setup|**runtime config**|Logical surface reference only (e.g., `surface: mcp_tool`)|MCP server configuration, OAuth 2.1/PKCE setup|HIGH — MCP is now a de facto routing surface; its config is not AIHR's modelcontextprotocol+1|

---

## 3. Template Chooser Candidates

|choose_when|template_name|required_inputs|stop_conditions|validator|
|---|---|---|---|---|
|Task requires assigning a model, surface, or agent|`routing_card`|task_signal, confidence_level, available_surfaces[], escalation_path|ambiguous_task_type; confidence < domain threshold|Single surface named in `selected_surface`; `rejected_surfaces[]` populated botpress+1|
|Routing destination is a different specialist agent with its own KB|`specialist_handoff_card`|source_agent, target_agent_id, context_payload, return_contract|target_agent unresolvable; context_payload schema missing|target_agent_id resolvable in registry; return_contract defined agentic-design+1|
|Any claim involves model version, pricing, capability, or provider policy|`currentness_verification_card`|claim_text, volatility_tier, last_verified_date, verification_source_type|source_type = unverified AND `needs_current_verification` absent|Claim flagged OR verified — never silently passed through [deploymentsafety.openai](https://deploymentsafety.openai.com/gpt-5-5)|
|Source provenance is secondary, indirect, or single-sourced|`source_authority_card`|source_id, tier_label, use_limit|tier = unverified AND use_limit not set|Tier assigned before claim surfaces downstream|
|Task involves code execution, repo write, tool invocation, or any irreversible action|`repo_execution_vs_chat_route_card`|task_type, reversibility_flag, irreversibility_score, risk_level, execution_surface|risk_level = HIGH AND no human_approval_flag; irreversibility_score ≥ threshold|Single surface selected; HIGH-risk ops routed to manual-review stop first deploymentsafety.openai+1|
|Task outcome requires config authority, approval, human judgment, or crosses safety threshold|`manual_review_stop_card`|stop_trigger, reason_code, reviewer_role, resume_condition, human_approval_required|reviewer_role undefined; resume_condition missing|Stop logged; routing fully halted until resume_condition met zylos+1|
|Task contains >1 independent routing problem or exceeds single-agent scope|`overloaded_task_decomposition_card`|task_description, decomposition_signal, subtask_ids[], orchestration_route|subtask_ids empty; orchestration_route undefined|Each subtask maps to exactly one routing card [botpress](https://botpress.com/blog/ai-agent-routing)|
|Primary route fails or no surface resolves|`fallback_path_card`|failed_route, fallback_surface, degraded_mode_flag, retry_eligible|degraded_mode AND fallback_surface = none|Fallback surface named OR escalated to manual_review_stop_card [zylos](https://zylos.ai/research/2026-01-30-ai-agent-human-handoff)|

---

## 4. Template Field Recommendations

|template|field|required|why|failure_if_missing|
|---|---|---|---|---|
|ALL cards|`card_type`|✅|Machine-readable identity for indexing and QA|Cards become undifferentiated; QA cannot audit [arxiv](https://arxiv.org/abs/2602.16666)|
|ALL cards|`advisory_only_flag: true`|✅|Enforces AIHR boundary; prevents cards being read as runtime authority|Boundary drift — AIHR treated as config actor|
|ALL cards|`task_signal`|✅|Routing trigger — card cannot fire without it|Wrong-task or no-fire|
|ALL cards|`confidence_level`|✅|2026 evidence shows 80–95% thresholds vary by risk domain; must be explicit|Silent misroutes at low confidence [zylos](https://zylos.ai/research/2026-01-30-ai-agent-human-handoff)|
|ALL cards|`escalation_path`|✅|Every card must define failure destination|Dead-end routing, no recovery|
|routing_card|`selected_surface`|✅|Exactly one surface must be named|Dual-routing ambiguity [botpress](https://botpress.com/blog/ai-agent-routing)|
|routing_card|`rejected_surfaces[]`|recommended|Enables QA audit of routing decision|Routing decision unauditable [arize](https://arize.com/blog/best-practices-for-building-an-ai-agent-router/)|
|currentness_verification_card|`volatility_tier`|✅|Model/pricing claims change on weeks-to-months cycles|Stale claim treated as accepted truth [deploymentsafety.openai](https://deploymentsafety.openai.com/gpt-5-5)|
|currentness_verification_card|`last_verified_date`|✅|Required for freshness audit; GPT-5.5 released April 22 2026|Unverifiable claim age [deploymentsafety.openai](https://deploymentsafety.openai.com/gpt-5-5)|
|currentness_verification_card|`needs_current_verification`|✅ (if unverified)|Explicit flag for downstream agents and QA|Unverified claim propagates as primary|
|manual_review_stop_card|`stop_trigger`|✅|Exact condition halting routing|Routing proceeds past a hard stop|
|manual_review_stop_card|`reviewer_role`|✅|Who must resolve the stop|Stop raised with no owner|
|manual_review_stop_card|`resume_condition`|✅|When routing may continue; prevents permanent deadlock|Routing deadlock [zylos](https://zylos.ai/research/2026-01-30-ai-agent-human-handoff)|
|manual_review_stop_card|`human_approval_required`|✅|MCP 2026 spec mandates human-in-the-loop for high-risk actions|Unsafe autonomous action on irreversible ops [linkedin](https://www.linkedin.com/pulse/model-context-protocol-2026-year-ai-infrastructure-standardize-4yetc)|
|specialist_handoff_card|`return_contract`|✅|Receiving agent must know what to return; context-preserving handoffs are non-negotiable in 2026|Cold handoff; orchestration cannot resume agentic-design+1|
|specialist_handoff_card|`context_payload`|✅|Customers/agents must never re-derive context from scratch|Stateless handoff; quality collapse [learn.microsoft](https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/handoff)|
|repo_execution_vs_chat_route_card|`reversibility_flag`|✅|Irreversible ops require elevated caution; Codex runs sandboxed by default|Destructive ops routed without risk classification [deploymentsafety.openai](https://deploymentsafety.openai.com/gpt-5-3-codex/cyber-safeguards)|
|repo_execution_vs_chat_route_card|`irreversibility_score`|✅|Action consequence scoring is 2026 best practice for repo agents|High-irreversibility actions bypass verification gates [agentmarketcap](https://agentmarketcap.ai/blog/2026/04/09/agent-confidence-calibration-knowing-when-to-ask)|
|repo_execution_vs_chat_route_card|`risk_level`|✅|HIGH must trigger manual_review_stop_card|Unsafe execution [beam](https://beam.ai/agentic-insights/ai-agent-security-in-2026-the-risks-most-enterprises-still-ignore)|
|overloaded_task_decomposition_card|`decomposition_signal`|✅|Must articulate WHY the task was split|Arbitrary decomposition; subtasks misalign with intent|
|overloaded_task_decomposition_card|`subtask_ids[]`|✅|Each must map to one routing card|Orphaned subtasks [botpress](https://botpress.com/blog/ai-agent-routing)|
|fallback_path_card|`degraded_mode_flag`|✅|Distinguishes graceful degradation from failure; 2026 HITL research validates this as a design pattern|Degraded output surfaces as authoritative [zylos](https://zylos.ai/research/2026-01-30-ai-agent-human-handoff)|
|source_authority_card|`tier_label`|✅|primary / secondary / unverified classification|Source authority collapse|
|source_authority_card|`use_limit`|✅|Caps how far unverified sources propagate|Unverified source used as KB foundation|

---

## 5. Anti-Patterns

|anti_pattern|why_bad|prevention|
|---|---|---|
|Embedding full prompt text inside a routing card|Collapses routing card into prompt cookbook; TEMPLATES.md becomes an instruction payload|Cards hold only structural fields; prompt text lives in prompts_workflows [botpress](https://botpress.com/blog/ai-agent-routing)|
|Missing `advisory_only_flag` on every card|Cards get interpreted as runtime config authority|Mandate `advisory_only_flag: true` as universal required field|
|Routing card with no `confidence_level`|2026 research: most agent failures trace to uncalibrated confidence, not wrong routing logic per se|Confidence level is a required field; block card if absent zylos+1|
|`manual_review_stop_card` without `resume_condition`|Permanent routing deadlock|resume_condition is required; card is structurally invalid without it [zylos](https://zylos.ai/research/2026-01-30-ai-agent-human-handoff)|
|AIHR card referencing openclaw.json or MCP server config paths directly|AIHR becomes a config actor, not an advisor; violates boundary|Cards reference surfaces by logical name only; never config paths [modelcontextprotocol](https://modelcontextprotocol.io/development/roadmap)|
|Hardcoding model names, pricing, or provider tiers in template examples|GPT-5.5 was released April 22 2026; model lineage changed within weeks|Use placeholder tokens (`{{model_tier}}`); annotate `needs_current_verification` [deploymentsafety.openai](https://deploymentsafety.openai.com/gpt-5-5)|
|Dual surface selection in a single routing card|Executor picks arbitrarily; ambiguity compounds downstream|`selected_surface` is singular; enforce at card validation [botpress](https://botpress.com/blog/ai-agent-routing)|
|`specialist_handoff_card` without `return_contract`|Handoff with no expected output; orchestration cannot resume|return_contract is required [agentic-design](https://agentic-design.ai/patterns/multi-agent/handoff-orchestration)|
|Treating `overloaded_task_decomposition_card` as optional|Multi-problem tasks silently route to one surface; other problems vanish|Trigger decomposition card whenever two independent routing decisions are present in one task|
|Routing HIGH-risk / irreversible repo ops without `irreversibility_score` gate|2026 Codex safety model: sandboxing + consequence scoring are complementary — scoring is the AIHR layer|Require `irreversibility_score` on all repo-execution cards; gate HIGH scores to manual review deploymentsafety.openai+1|
|Omitting MCP as a valid routing surface in surface enumeration|MCP is the 2026 de facto standard for tool integration; ignoring it creates surface gaps|Add `mcp_tool` as a first-class surface option in routing card enumerations modelcontextprotocol+1|

---

## 6. What Must Stay Out of TEMPLATES.md

**→ Belongs in appendices:**

- Model capability rankings and tier comparisons (volatile; `needs_current_verification`)[deploymentsafety.openai](https://deploymentsafety.openai.com/gpt-5-5)
    
- Confidence threshold tables by domain (80–95% range by risk level) — evidence, not structure[zylos](https://zylos.ai/research/2026-01-30-ai-agent-human-handoff)
    
- Populated example routing cards (filled instances) — evidence, not templates
    
- MCP server capability discovery / `.well-known` metadata[modelcontextprotocol](https://modelcontextprotocol.io/development/roadmap)
    
- Provider pricing tables (weeks-to-months volatility)
    
- Agent registry / surface registry indexes
    
- Reliability metric definitions (consistency, robustness, predictability, safety)[arxiv](https://arxiv.org/abs/2602.16666)
    
- Security audit requirements (RBAC, just-in-time permissions, immutable audit trails)[beam](https://beam.ai/agentic-insights/ai-agent-security-in-2026-the-risks-most-enterprises-still-ignore)
    

**→ Belongs in prompts_workflows:**

- Full instruction text for any agent
    
- Prompt templates, persona configs, system message payloads
    
- Retrieval pipeline logic, MCP OAuth 2.1/PKCE setup[linkedin](https://www.linkedin.com/pulse/model-context-protocol-2026-year-ai-infrastructure-standardize-4yetc)
    
- Tool invocation sequences, API call patterns
    
- Retry logic and circuit-breaker implementations
    
- Structured output JSON schema definitions (enforcement logic belongs to runtime)openrouter+1
    

**→ Belongs in LEARNING_QUEUE.md:**

- `cost_budget_gate_card` — promising but unvalidated in AIHR context
    
- `confidence_calibration_card` — trajectory-level uncertainty is emerging researchagentmarketcap+1
    
- `streaming_structured_output_routing` — streaming partial JSON enabling early routing-logic fire is a 2026 technique worth evaluating[collinwilkins](https://collinwilkins.com/articles/structured-output)
    
- MCP Server Cards as routing surface discovery mechanism[modelcontextprotocol](https://modelcontextprotocol.io/development/roadmap)
    

**→ Must never appear anywhere in TEMPLATES.md:**

- openclaw.json paths or mutations
    
- Provider policy text verbatim
    
- Model registry change instructions
    
- Any claim asserting runtime config authority
    
- MCP server config, OAuth credentials, sandbox policy (belongs to deployment safety layer)[deploymentsafety.openai](https://deploymentsafety.openai.com/gpt-5-3-codex/cyber-safeguards)
    

---

## Ranked Content To Integrate

|rank|content_to_integrate|target_file|target_section|evidence_score_1_100|impact_score_1_100|risk_if_missing_1_100|freshness_sensitivity|validation_sources|verification_status|integration_priority|notes|
|---|---|---|---|---|---|---|---|---|---|---|---|

|rank|content_to_integrate|target_file|target_section|evidence_score_1_100|impact_score_1_100|risk_if_missing_1_100|freshness_sensitivity|validation_sources|verification_status|integration_priority|notes|
|---|---|---|---|---|---|---|---|---|---|---|---|
|1|Universal required fields for ALL route cards: `card_type`, `advisory_only_flag`, `confidence_level`, `escalation_path`, `task_signal`|TEMPLATES.md|Template field schema|92|98|97|low|arxiv+2|`triple_verified_current`|**P0 — integrate immediately**|Without these, no card is structurally valid; confidence_level grounded in 2026 HITL research|
|2|`manual_review_stop_card` with `stop_trigger`, `reviewer_role`, `resume_condition`, `human_approval_required`|TEMPLATES.md|Manual-review card|91|96|96|medium|zylos+2|`triple_verified_current`|**P0 — integrate immediately**|MCP 2026 spec mandates human-in-the-loop for high-risk actions; `resume_condition` prevents deadlock|
|3|`repo_execution_vs_chat_route_card` with `reversibility_flag`, `irreversibility_score`, `risk_level`; HIGH-risk gates to manual-review stop|TEMPLATES.md|Repo-execution card|90|95|95|medium|deploymentsafety.openai+2|`triple_verified_current`|**P0 — integrate immediately**|GPT-5.5/Codex sandboxing is runtime; AIHR's layer is the `irreversibility_score` gate|
|4|`specialist_handoff_card` with mandatory `return_contract` + `context_payload`; context preservation non-negotiable per 2026 patterns|TEMPLATES.md|Specialist-handoff card|89|94|93|low|agentic-design+2|`triple_verified_current`|**P0**|2026 handoff pattern evidence: context loss is top failure mode|
|5|`currentness_verification_card` with `volatility_tier`, `last_verified_date`, `needs_current_verification` for model/provider/pricing claims|TEMPLATES.md|Currentness card|88|93|94|**high**|deploymentsafety.openai+2|`triple_verified_current`|**P0**|GPT-5.5 launched April 22 2026; model claims stale within weeks|
|6|`choose_template_when` decision table (8-row routing chooser)|TEMPLATES.md|Chooser table|87|92|88|low|botpress+2|`double_verified_current`|**P1**|Prevents wrong-template selection at point of use|
|7|`routing_card` with singular `selected_surface`, `rejected_surfaces[]`, and `advisory_only_flag`|TEMPLATES.md|Routing card|87|91|88|low|botpress+2|`triple_verified_current`|**P1**|LLM-based routing is state-of-the-art; advisory flag enforces AIHR boundary|
|8|MCP as first-class routing surface (`mcp_tool`) in surface enumeration|TEMPLATES.md|Routing card / surface enum|85|88|86|**high**|modelcontextprotocol+2|`double_verified_current`|**P1**|MCP is 2026 de facto standard; omitting it creates routing surface gap|
|9|`overloaded_task_decomposition_card` with `decomposition_signal` and `subtask_ids[]`|TEMPLATES.md|Decomposition card|83|87|85|low|botpress+1|`double_verified_current`|**P1**|Multi-problem tasks silently misroute without this card|
|10|Template ownership boundary table (AIHR vs prompts_workflows vs runtime)|TEMPLATES.md|Ownership section|84|89|90|low|deploymentsafety.openai+2|`triple_verified_current`|**P1**|Boundary violations are the most dangerous failure mode for an advisory agent|
|11|`source_authority_card` with `tier_label` (primary/secondary/unverified) and `use_limit`|TEMPLATES.md|Source authority card|80|82|82|low|—|`single_verified_current`|**P2**|Prevents unverified sources from propagating as KB foundations|
|12|Confidence threshold ranges (80–95% by domain) in appendix with reference from TEMPLATES.md `confidence_level` field|APPENDIX|Confidence thresholds|88|85|83|medium|zylos+1|`double_verified_current`|**P1 for appendix**|Evidence-based numbers; must not be hardcoded in templates — reference only|
|13|Agent reliability dimensions (consistency, robustness, predictability, safety) as stop-card reasoning vocabulary|APPENDIX|Reliability evidence|86|80|78|low|[arxiv](https://arxiv.org/abs/2602.16666)|`single_verified_current`|**P2 for appendix**|arXiv Feb 2026 peer-reviewed; 14-model study; informs stop-card trigger language|
|14|`fallback_path_card` with `degraded_mode_flag`, `retry_eligible`, graceful-degradation semantics|TEMPLATES.md|Fallback card|80|80|75|low|[zylos](https://zylos.ai/research/2026-01-30-ai-agent-human-handoff)|`single_verified_current`|**P2**|Important but lower urgency; can be added after P0/P1 cards stabilize|
|15|`streaming_structured_output_routing` note — early-fire routing on partial JSON stream|LEARNING_QUEUE.md|Future candidates|72|70|40|**high**|[collinwilkins](https://collinwilkins.com/articles/structured-output)|`single_verified_current`|**P3 — LEARNING_QUEUE**|2026 emerging pattern; not yet stable enough for scaffold|
|16|MCP Server Cards as surface-discovery routing mechanism|LEARNING_QUEUE.md|Future candidates|70|68|38|**high**|[modelcontextprotocol](https://modelcontextprotocol.io/development/roadmap)|`single_verified_current`|**P3 — LEARNING_QUEUE**|Roadmap item; not yet released|
|17|`confidence_calibration_card` for trajectory-level uncertainty|LEARNING_QUEUE.md|Future candidates|68|72|55|medium|zylos+1|`single_verified_current`|**P3 — LEARNING_QUEUE**|Promising; needs operational validation before scaffold inclusion|
|18|Hardcoded provider pricing or model tier tables|—|**REJECT**|10|—|—|**extreme**|[deploymentsafety.openai](https://deploymentsafety.openai.com/gpt-5-5)|`reject_stale_or_unverified`|**REJECT**|Model lineage changed within weeks of GPT-5.5 launch; stale by definition|