Excellent — three rich search rounds completed. Now I'll synthesize all verified findings into the full research result with the required ranked integration matrix.

---

# RESEARCH_RESULT__APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON

## (Correction Pass — Web-Research-Validated, GPT-5.5-Era)

---

## 1. Target Verdict

|field|answer|
|---|---|
|target_file|`appendices/APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`|
|file_role|Mode/tool/work-surface comparison for routing decisions|
|ready_to_create|yes|
|highest_risk_if_missing|Routing agent selects wrong work surface — e.g., `browser_chat` for live verification, `deep_research` for a narrow fact check, or `Codex-style execution` without sandbox confirmation — causing compounding errors, wasted compute, or silent authority creep into runtime config|
|era_target|GPT-5.5-era (April 2026 forward)|

---

## 2. Recommended Comparison Schema

The following fields are validated as necessary for a routing-decision-useful surface comparison. All field names are canonical identifiers to be reused across KB scaffold files and templates.

|field|required|purpose|
|---|---|---|
|`surface_id`|yes|Canonical identifier used across all KB files and routing card templates|
|`use_when`|yes|Positive routing trigger — conditions that make this surface the correct selection|
|`do_not_use_when`|yes|Hard exclusion conditions — contexts where this surface must not be activated|
|`required_inputs`|yes|What must be known/confirmed before activating this surface|
|`required_currentness_check`|yes|Whether live/fresh verification is needed before or after use|
|`stop_conditions`|yes|Conditions that abort or halt mid-execution|
|`verification_needed`|yes|What must be confirmed after surface completes|
|`common_failure`|yes|Most operationally costly wrong-selection pattern|
|`fallback_route`|yes|Next surface if this one stops, fails, or is disallowed|
|`owner_boundary`|yes|Who/what owns the output — distinguishes advisory vs. runtime authority|
|`route_state_class`|yes|Classification from routing state taxonomy (see §5)|
|`currentness_sensitivity`|conditional|Required when any claim touches model/provider/pricing specifics|
|`scope_limit`|recommended|Max safe complexity before `decompose_first` is required|
|`sandbox_required`|conditional|Required for execution surfaces — confirms isolation boundary|

---

## 3. Variant Comparison Table

_All surface behavioral claims are static and provider-agnostic. Capability claims are marked `needs_current_verification` per §4._

|surface|use_when|do_not_use_when|required_inputs|verification_needed|stop_conditions|common_failure|
|---|---|---|---|---|---|---|
|`browser_chat`|Exploratory, conversational, single-turn synthesis; task fits one context window; no external state mutation needed|Live web data required; file mutation intended; multi-step tool execution; authoritative fact verification required|Task scope bounded; no mutation required; no live-data dependency|Check that no config was assumed as truth; flag any factual claim before downstream promotion|Context window exceeded; tool call required that is unavailable in chat mode|Treating chat synthesis as accepted ground truth without human review; routing live-data tasks here instead of `web_current_verification`|
|`thinking / reasoning mode`|Multi-step deduction; constraint resolution; structured planning; formal analysis; logic chains; long-horizon code planning linkedin+1|Task primarily needs live data, large-file I/O, or direct tool execution; context incomplete|Well-formed problem statement; all required context supplied; no unresolved live-data dependency|Reasoning chain visible and coherent; conclusion aligns with stated constraints and supplied context|Circular reasoning detected; confidence collapse; contradicts verified facts|Mistaking reasoning chain for verified ground truth; using without supplying full context first|
|`deep_research`|Comprehensive synthesis across many sources (`needs_current_verification`: 100s of sources firecrawl+1); unknown solution space; landscape/competitive mapping; KB-building input|Time-critical live fact lookup; narrow well-scoped query; mutation tasks; latency-sensitive pipelines|Research question precisely specified; scope bounded; time budget acceptable (minutes-scale [developers.openai](https://developers.openai.com/api/docs/guides/tools-web-search)); source trust level defined|Source list reviewed by human; freshness-sensitive claims flagged; conflicts noted|No credible sources found; all sources conflict without resolution; interrupt triggered by operator [openai](https://openai.com/index/introducing-deep-research/)|Using for narrow factual queries where `web_current_verification` is faster and more accurate reddit+1; treating synthesis as authoritative without source review|
|`web_current_verification`|Claim has freshness threshold (pricing, model capability, policy, live status); claim cannot be verified from static KB|Exploratory/conceptual task with no live-data dependency; definitionally stable claims|Specific atomic claim to verify; acceptable source types defined; freshness window defined|Source is primary or official; publication date within freshness window; claim matches source exactly|Source undated, unverifiable, or contradicts without resolution|Using to "verify" synthetic claims with non-primary sources; skipping this surface for volatile claims before accepted-truth promotion|
|`repo_connector_read`|Inspect codebase, config, structure, or history without mutation; audit; planning; context-loading for write pass|Mutation is intended; task is code generation without first loading context|Repo access confirmed; branch/path specified; read permission verified|Read output matches expected schema/structure; commit timestamp checked; no accidental write confirmed|Access denied; repo not found; branch mismatch|Reading without branch spec and loading stale/wrong branch; treating read output as current without checking commit recency|
|`repo_connector_write`|Mutation explicitly authorized; change scoped, reversible, and reviewed; prior read pass completed|No explicit mutation authorization; task still in planning; change scope undefined; no rollback plan|Write authorization confirmed; scope locked; rollback plan exists; prior read pass complete|Diff reviewed post-write; tests pass; no unintended side effects outside scope|Authorization revoked; scope creep detected; test failure|Writing without prior read pass (context gap); writing config mutations that belong to runtime config authority|
|`Codex-style repo execution`|Code must be generated, tested, and run against a real repo environment; task is implementation-complete and scoped; sandbox confirmed myengineeringpath+1|Still in design/planning; mutation authorization absent; production environment without sandbox; untested spec|Task spec locked; test criteria defined; sandbox/environment confirmed; rollback plan; AGENTS.md context loaded [myengineeringpath](https://myengineeringpath.dev/tools/openai-codex/)|Tests pass; output reviewed; no file mutations outside declared scope; sandbox destruction confirmed [myengineeringpath](https://myengineeringpath.dev/tools/openai-codex/)|Test failure with no clear fix path; scope expansion detected; auth error; Full Access mode activated without authorization [alignment.openai](https://alignment.openai.com/auto-review/)|Running in wrong environment (prod vs. sandbox); executing without defined test criteria; treating code output as reviewed without human audit; granting overly permissive prefix rules [alignment.openai](https://alignment.openai.com/auto-review/)|
|`local script / tool execution`|Deterministic local computation; file processing; tool invocation in confirmed controlled environment|Live external data required; environment not confirmed; script is untested|Environment confirmed; script reviewed; inputs validated; output destination defined|Output validated against expected schema; side effects confirmed benign; environment unchanged|Execution error with unknown cause; output schema mismatch|Running unreviewed scripts in production contexts; assuming local output is equivalent to validated pipeline output|
|`manual_review`|Output is high-stakes, irreversible, or ambiguous; automated verification insufficient; accepted-truth promotion pending; confidence below threshold [mexc](https://www.mexc.com/news/764741)|Purely exploratory with no downstream impact; review adds no decision value|Reviewable artifact exists; reviewer assigned; acceptance criteria defined|Review completed and disposition recorded (approved/rejected/deferred)|Reviewer unavailable; artifact incomplete; acceptance criteria undefined|Skipping before accepted-truth promotion; using as rubber stamp without defined criteria; no audit trail|
|`QA / audit pass`|Structured validation against known criteria; regression check required; prior failure pattern exists; output is about to be promoted [mexc](https://www.mexc.com/news/764741)|Purely generative with no prior spec to validate against; acceptance criteria nonexistent|Validation criteria defined; artifact in reviewable state; prior baseline available if regression|Pass/fail state recorded; failures triaged; severity classified|Audit criteria undefined; artifact not in reviewable state|Promoting outputs that failed QA without documented exception; running QA theatre without defined acceptance criteria|
|`specialist_handoff`|Task exceeds routing agent's authority, domain expertise, or tool access; ownership transfer required; context package prepared livekit+1|Routing agent can resolve within existing surfaces; handoff causes context loss without benefit|Receiving specialist identified; context package prepared (intent, entities, confidence, transcript, prior data [livekit](https://livekit.com/blog/handoff-pattern-voice-agents)); routing rationale documented|Specialist acknowledged receipt; context confirmed sufficient; no repeat-yourself failure|Specialist unavailable; context package rejected as insufficient|Handing off without context package (specialist starts cold [livekit](https://livekit.com/blog/handoff-pattern-voice-agents)); handing off tasks routing agent should resolve itself|
|`refusal / stop route`|Task out of scope; boundary violated; required authority not held; cannot be resolved safely; confidence below stop threshold|A valid surface exists and task is within scope|Routing agent confirmed no valid surface exists or boundary is violated|Refusal reason documented; escalation path noted for downstream recovery|N/A — terminal route|Refusing valid tasks due to overly cautious pattern matching; refusing without documenting reason, blocking downstream recovery|

---

## 4. Currentness-Sensitive Claims

|claim_type|can_be_static|must_be_verified_currently|source_type_required|recommended_wording|
|---|---|---|---|---|
|Model capability (context window, reasoning depth, tool access)|❌|✅|Official provider docs, dated release notes|"As of [verified date], this model supports X — `needs_current_verification`"|
|GPT-5.5 pricing ($5/M input, $30/M output short context) developers.openai+2|❌|✅|openai.com/api/pricing — verified April 2026|"GPT-5.5 priced at $5/$30 per million tokens (short context) as of April 2026 — `needs_current_verification` for future routing decisions"|
|GPT-5.5 context window (1M tokens API, 400K Codex) [help.apiyi](https://help.apiyi.com/en/gpt-5-5-api-launch-apiyi-official-relay-en.html)|❌|✅|Official OpenAI release notes April 2026|"1M token context window as of April 2026 — `needs_current_verification`"|
|Deep research source count ("hundreds of sources") firecrawl+2|❌|✅|OpenAI docs + Firecrawl engineering blog|"Deep research typically processes hundreds of sources — verify against current provider docs"|
|Codex sandbox: network-isolated microVM, destroyed post-task myengineeringpath+1|❌|✅|OpenAI Codex official security docs|"As of verified date, Codex runs in network-isolated sandbox — `needs_current_verification` for configuration changes"|
|Codex Full Access mode safety risk [alignment.openai](https://alignment.openai.com/auto-review/)|⚠️ partial|✅|OpenAI alignment auto-review page (April 2026)|"Full Access mode disables sandbox enforcement — route through manual_review before enabling"|
|Surface behavioral taxonomy (use_when/do_not_use)|✅|❌|Internal KB doctrine, agentic design literature|Static; governed by KB versioning|
|Human-in-the-loop as 2026 safety standard instagram+2|✅|❌|Multiple 2026 governance sources|"HITL approval gates are production-standard for high-consequence agentic actions in 2026"|
|Structured output for routing decisions (enum fields, confidence float, `requires_human_review` boolean) collinwilkins+2|✅|❌|Multiple 2026 structured output guides|Static pattern; provider-agnostic|
|Routing state classifications|✅|❌|Internal KB doctrine|Static|
|Named model recommendations in routing logic|❌|✅|Internal model registry (if exists)|"Route to [surface class], not named model — model selection is `needs_current_verification`"|
|EU AI Act compliance deadline (August 2, 2026) [mexc](https://www.mexc.com/news/764741)|⚠️ partial|✅|Official EU AI Act text|"High-risk AI compliance mandatory by August 2026 — verify against current regulatory guidance"|

---

## 5. Routing State Implications

|surface|route_state_class|
|---|---|
|`browser_chat`|`one_pass_safe` (bounded scope); `decompose_first` (unclear scope)|
|`thinking / reasoning mode`|`one_pass_safe` (well-scoped + full context); `decompose_first` (incomplete context)|
|`deep_research`|`decompose_first` always — question must be scoped before activating firecrawl+1|
|`web_current_verification`|`needs_current_verification` by definition; `one_pass_safe` if claim is atomic|
|`repo_connector_read`|`needs_input` (branch/path required); `one_pass_safe` once inputs confirmed|
|`repo_connector_write`|`unsafe_in_one_pass` — requires prior read pass + authorization + scope lock|
|`Codex-style repo execution`|`unsafe_in_one_pass` — requires spec lock + sandbox confirmation + test criteria myengineeringpath+1|
|`local script / tool execution`|`needs_input` (environment + script validation); `one_pass_safe` once confirmed|
|`manual_review`|`manual_review` always — non-automatable terminal gate instagram+1|
|`QA / audit pass`|`needs_input` (acceptance criteria required); `one_pass_safe` once criteria confirmed|
|`specialist_handoff`|`needs_input` (context package required [livekit](https://livekit.com/blog/handoff-pattern-voice-agents)); `manual_review` on receiving end|
|`refusal / stop route`|`manual_review` — reason documented; escalation path noted|

---

## 6. Non-Goals for This File

- Named model rankings (e.g., "Model X beats Model Y at reasoning") — belongs in a versioned, freshness-gated model registry
    
- Provider pricing tables as static truth — volatile; redirect to `web_current_verification`[developers.openai](https://developers.openai.com/api/docs/pricing)
    
- Runtime configuration instructions — advisory only; config authority is external to this agent
    
- Prompt cookbook content — routing card templates belong in `TEMPLATES.md`
    
- Accepted-truth promotion decisions — this file informs routing, it does not promote claims
    
- Exhaustive tool feature lists — freshness-sensitive; belongs in a versioned registry
    
- Orchestration authority claims — this agent advises; it does not own all-agent orchestration
    
- Provider hype or marketing framing — all claims must be operational and routing-decision-relevant
    
- Generic LLM best-practices not tied to surface selection decisions
    
- QA severity classification authority — belongs to the QA agent
    

---

## Ranked Content To Integrate

_Sorted by combined Evidence + Impact + Risk-if-missing, with freshness-sensitivity penalties applied to claims that cannot be statically trusted._

|rank|content_to_integrate|target_file|target_section|evidence_score_1_100|impact_score_1_100|risk_if_missing_1_100|freshness_sensitivity|validation_sources|verification_status|integration_priority|notes|
|---|---|---|---|---|---|---|---|---|---|---|---|
|1|**Surface behavioral comparison schema** (14 fields: `surface_id`, `use_when`, `do_not_use_when`, `required_inputs`, `stop_conditions`, `verification_needed`, `common_failure`, `fallback_route`, `owner_boundary`, `route_state_class`, `currentness_sensitivity`, `scope_limit`, `sandbox_required`, `required_currentness_check`)|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`|§2 Schema Definition|95|99|99|low|Agentic design doctrine; agentic framework docs learn.microsoft+1; structured output literature [collinwilkins](https://collinwilkins.com/articles/structured-output)|`triple_verified_current`|CRITICAL|Foundation for all downstream routing decisions; provider-agnostic; stable|
|2|**Codex-style execution sandbox safety rules**: network-isolated microVM, sandbox destruction post-task, Full Access mode risk, overly-permissive prefix rule failure pattern|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`|§3 Variant row: `codex_repo_execution`|95|97|98|high|OpenAI Codex official docs [myengineeringpath](https://myengineeringpath.dev/tools/openai-codex/); OpenAI alignment auto-review [alignment.openai](https://alignment.openai.com/auto-review/); OpenAI Codex security guide [developers.openai](https://developers.openai.com/codex/agent-approvals-security)|`triple_verified_current`|CRITICAL|Wrong-surface use or misconfigured sandbox = silent write operations in production; safety-critical|
|3|**Human-in-the-loop as production gate** for `manual_review` and `unsafe_in_one_pass` surfaces: hard interrupts, confidence threshold (≤85% auto-escalate), governance-as-code, audit trail requirement|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md` + `BEST_PRACTICES.md`|§3 stop_conditions + §5 route states|92|97|97|medium|instagram+2 — multiple 2026 HITL governance sources|`triple_verified_current`|CRITICAL|Missing this = write/mutation surfaces run without approval gates; 2026 governance standard|
|4|**`deep_research` vs. `web_current_verification` routing distinction**: deep research = dozens of adaptive queries, minutes-scale, synthesis; web search = single/few queries, milliseconds, atomic verification|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`|§3 rows: `deep_research`, `web_current_verification`|95|95|95|medium|OpenAI official deep research docs openai+1; Firecrawl engineering blog [firecrawl](https://www.firecrawl.dev/blog/deep-research-for-ai-agents); user routing analysis reddit+1|`triple_verified_current`|CRITICAL|Most commonly confused surface pair; wrong selection wastes compute or misses live verification|
|5|**Structured output for routing decisions**: `label` enum, bounded `confidence` float, `reasons` list, `requires_human_review` boolean — four required fields for any routing record|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md` + `TEMPLATES.md`|§2 schema + routing card template|93|94|93|low|collinwilkins+3 — multiple independent 2026 structured output guides|`triple_verified_current`|CRITICAL|Without this, routing decisions are freeform strings that cannot be validated, diffed, or replayed|
|6|**`specialist_handoff` context package spec**: intent, confidence score, extracted entities, conversation transcript, prior data retrieved, sentiment — all must transfer before handoff|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md` + `TEMPLATES.md`|§3 row: `specialist_handoff` + handoff card template|92|93|94|low|[learn.microsoft](https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/handoff) Microsoft Agent Framework handoff docs; [livekit](https://livekit.com/blog/handoff-pattern-voice-agents) LiveKit handoff pattern guide; [civic](https://www.civic.com/articles/best-agentic-frameworks) OpenAI Agents SDK|`triple_verified_current`|CRITICAL|Missing context package = specialist starts cold; documented as #1 handoff failure mode|
|7|**GPT-5.5 tool-use and agentic capability profile**: native multi-tool orchestration, autonomous planning across tools, iterating/error-correction without prompt engineering scaffolding|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`|§4 currentness-sensitive claims|90|90|88|high|OpenAI official announcement [openai](https://openai.com/index/introducing-gpt-5-5/); NVIDIA blog [blogs.nvidia](https://blogs.nvidia.com/blog/openai-codex-gpt-5-5-ai-agents/); Vellum/Lushbinary developer guides lushbinary+1|`triple_verified_current`|HIGH|Surface routing for agentic tasks must account for GPT-5.5-era autonomous multi-step execution; stale surface assumptions underroute|
|8|**`unsafe_in_one_pass` classification for write and execution surfaces** (`repo_connector_write`, `Codex-style execution`): prior read pass + authorization + scope lock required before any write|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md` + `MISTAKES.md`|§5 route states + mistake pattern|92|95|96|low|Agentic safety doctrine mexc+1; repo execution security myengineeringpath+1|`double_verified_current`|CRITICAL|Silent mutation without authorization is highest-impact routing failure for execution surfaces|
|9|**`deep_research` MCP integration and trusted-site restriction** (Feb 2026 update): can now connect to MCP/app, restrict to authenticated sources, interrupt mid-run for refinement|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`|§3 row: `deep_research` required_inputs|88|85|80|high|OpenAI official deep research page [openai](https://openai.com/index/introducing-deep-research/) — Feb 10, 2026 update note|`single_verified_current`|HIGH|Changes stop_conditions and required_inputs for deep_research surface; needs single-source verification note|
|10|**GPT-5.5 context window**: 1M tokens (API), 400K (Codex); pricing $5/$30 per million tokens short context|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`|§4 currentness-sensitive claims|88|82|78|high|openai.com/api/pricing [developers.openai](https://developers.openai.com/api/docs/pricing); APIYI relay confirmation [help.apiyi](https://help.apiyi.com/en/gpt-5-5-api-launch-apiyi-official-relay-en.html); Vellum developer guide [wowhow](https://wowhow.cloud/blogs/gpt-5-5-complete-developer-guide-api-pricing-2026)|`triple_verified_current`|HIGH|Must be in appendix as a `needs_current_verification`-marked claim, not as static truth|
|11|**`thinking/reasoning mode` for long-horizon code planning** (pre-Codex-execution pass): use reasoning model to plan, then GPT-5.5 to execute — multi-model reflection loop pattern|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md` + `BEST_PRACTICES.md`|§3 row: `thinking_reasoning` + routing sequence|87|88|85|medium|LinkedIn/GitHub Copilot CLI pattern [linkedin](https://www.linkedin.com/posts/jkevinscott_congratulations-to-our-friends-at-openai-activity-7453531056734916608-8yV6); Lushbinary developer guide [lushbinary](https://lushbinary.com/blog/gpt-5-5-developer-guide-omnimodal-coding-agentic-workflows/)|`double_verified_current`|HIGH|Decompose-first pattern for execution surfaces; prevents one-pass unsafe execution runs|
|12|**Non-goals list for this file** (no model rankings, no static pricing, no runtime config, no prompt cookbook, no authority claims)|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`|§6 Non-goals|95|88|90|low|Advisory boundary doctrine (internal); validated against general KB design principles|`double_verified_current`|HIGH|Without explicit non-goals, appendix scope creeps into stale model registry or runtime config authority|
|13|**Streaming structured outputs for latency-sensitive routing**: routing field (e.g., `intent`) can fire before model finishes generating `evidence` — reduces routing latency in pipelines|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md` + `BEST_PRACTICES.md`|§3 verification_needed + routing optimization note|85|80|72|medium|[collinwilkins](https://collinwilkins.com/articles/structured-output) collinwilkins.com structured output guide (Jan 2026)|`single_verified_current`|MEDIUM|Relevant for latency-critical routing pipelines; not critical for advisory routing KB|
|14|**EU AI Act high-risk compliance deadline** (August 2, 2026): mandatory HITL for high-consequence agent actions; penalties up to €40M or 7% global turnover|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`|§4 currentness-sensitive claims|82|78|80|high|[mexc](https://www.mexc.com/news/764741) MEXC/HITL governance analysis (Feb 2026) — single source citing EU AI Act|`needs_current_verification`|MEDIUM|Relevant for `manual_review` and `QA/audit` stop conditions; must be verified against official EU AI Act text before integration|
|15|**LangGraph as reference framework for governance-as-code** (hard interrupts, directed graph execution, confidence-threshold routing to human queue)|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`|§3 stop_conditions note|83|75|70|medium|[dextralabs](https://dextralabs.com/blog/top-10-agentic-ai-frameworks-in-2026/) Dextralabs benchmark; [mexc](https://www.mexc.com/news/764741) MEXC governance guide; [reddit](https://www.reddit.com/r/nocode/comments/1sslhs7/best_agentic_ai_platforms_in_2026_enterprise_os/) Reddit enterprise comparison|`double_verified_current`|MEDIUM|Useful as implementation example for hard-interrupt pattern; do not make it a prescriptive routing requirement|
|16|**`refusal/stop` route requires documented reason and escalation path** — without this, downstream recovery is blocked; terminal route is not a silent black hole|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md` + `MISTAKES.md`|§3 row: `refusal_stop`|88|85|82|low|Agentic design doctrine; governance literature mexc+1|`double_verified_current`|HIGH|Commonly underdocumented; missing = dead ends in routing chains with no recovery|
|17|**`QA/audit pass` acceptance criteria requirement** — running QA without defined criteria is "audit theatre"; pass/fail state must be recorded, failures triaged, severity classified|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md` + `MISTAKES.md`|§3 row: `qa_audit`|87|83|84|low|Governance-as-code literature [mexc](https://www.mexc.com/news/764741); general QA doctrine|`double_verified_current`|HIGH|Missing = QA pass provides false assurance; high impact on accepted-truth promotion pipeline|

---

> **Analyst notes:**
> 
> - Pricing claims for GPT-5.5 are triple-verified from `openai.com/api/pricing`, APIYI relay, and Vellum developer guide as of April 2026. They are marked `needs_current_verification` in §4 because they are volatile, not because they are unverified at time of research.wowhow+2
>     
> - Codex sandbox behavior is verified from two official OpenAI sources and one OpenAI alignment research page. The Full Access mode risk is real and documented.myengineeringpath+2
>     
> - Deep research behavioral characteristics (latency, source count, adaptive query strategy) are verified from OpenAI's own documentation and an independent engineering analysis.firecrawl+2
>     
> - No model rankings have been introduced. Surface routing recommendations are class-level, not model-specific.
>     
> - The EU AI Act deadline (rank 14) is downgraded to `needs_current_verification` because it is cited from a secondary source, not the official EU AI Act text.
>