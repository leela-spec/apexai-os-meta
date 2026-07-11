## class: comparison  
role: ROUTING_REFERENCE  
surface: agent_kb_appendix  
quality: reliable  
scope: agent  
purpose: mode, tool, and work-surface comparison for AI Handling Routing decisions  
dependencies: ESSENCE.md | BEST_PRACTICES.md | MISTAKES.md | TEMPLATES.md | APPENDIX_KB_SOURCE_NOTES.md | APPENDIX_KB_ROUTING_EXAMPLES.md  
status: active_appendix  
owner: special_ops__ai_handling_routing  
validator: meta_ops

# APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON

## Purpose

This appendix defines a provider-agnostic comparison surface for AIHR routing decisions.

AIHR uses this file to compare work-surface classes before recommending a route for:

- AI mode selection
- work-surface selection
- currentness verification
- source-authority routing
- repo read/write routing
- repo execution routing
- specialist handoff
- fallback routing
- manual review
- stop/escalation routing

This file is a routing reference. It is not a model leaderboard, provider registry, pricing table, execution policy, or runtime configuration source.

## Authority Boundary

|boundary_id|rule|status|enforcement|
|---|---|---|---|
|`AB-01`|AIHR compares surfaces for advisory routing only.|`accepted_in_kb_base`|Route output must remain a recommendation, card, warning, or stop signal.|
|`AB-02`|AIHR does not rank providers or named models as accepted truth.|`accepted_in_kb_base`|Named provider/model claims must be marked `needs_current_verification`.|
|`AB-03`|AIHR does not own model registry truth.|`accepted_in_kb_base`|Route to a surface class unless a verified model registry is explicitly supplied.|
|`AB-04`|AIHR does not own pricing truth.|`accepted_in_kb_base`|Cost/pricing claims require `web_current_verification` or source-authority lookup.|
|`AB-05`|AIHR does not authorize execution.|`accepted_in_kb_base`|Execution surfaces require owner authorization, scope lock, and validation gates.|
|`AB-06`|AIHR does not mutate runtime config, provider settings, API keys, credentials, MCP grants, or `openclaw.json`.|`accepted_in_kb_base`|Any such request triggers `refusal_stop_route` or `manual_review`.|
|`AB-07`|Specific model/provider/cost/capability claims require current verification before use as routing basis.|`accepted_in_kb_base`|Volatile claim state defaults to `needs_current_verification`.|
|`AB-08`|Candidate research may inform this appendix but does not become accepted doctrine until promoted.|`accepted_in_kb_base`|Candidate rows must remain marked `candidate`, `needs_validation`, or `deferred`.|

## Comparison Schema

|field|required|purpose|allowed_values_or_format|
|---|---|---|---|
|`surface_id`|yes|Stable identifier for a compared work surface.|snake_case string; one row per surface.|
|`surface_class`|yes|Human-readable class name for the surface.|`chat`, `reasoning`, `research`, `verification`, `repo_read`, `repo_write`, `repo_execution`, `local_execution`, `review`, `audit`, `handoff`, `stop`.|
|`use_when`|yes|Positive routing conditions.|Compact semicolon-separated conditions.|
|`do_not_use_when`|yes|Hard exclusion conditions.|Compact semicolon-separated conditions.|
|`required_inputs`|yes|Inputs that must be present before routing.|Named requirements; use `none` only for truly safe cases.|
|`required_currentness_check`|yes|Whether fresh verification is required.|`none`, `before_route`, `after_route`, `before_and_after_route`, `claim_dependent`.|
|`stop_conditions`|yes|Conditions that must halt or reroute.|`SC-*` identifiers or concise stop phrases.|
|`verification_needed`|yes|Required validation after the surface is used.|`none`, `source_check`, `diff_review`, `test_run`, `human_approval`, `qa_assert`, `handoff_ack`, `reason_logged`.|
|`common_failure`|yes|Primary failure if wrongfully selected.|One concise failure mode.|
|`fallback_route`|yes|Next route when unavailable, unsafe, or failed.|Another `surface_id` or `manual_review` / `refusal_stop_route`.|
|`owner_boundary`|yes|Authority owner for the output or action.|`aihr_advisory`, `source_authority`, `repo_owner`, `runtime_owner`, `qa_owner`, `specialist_owner`, `human_reviewer`, `terminal_stop`.|
|`route_state_class`|yes|Default routing state.|`one_pass_safe`, `decompose_first`, `unsafe_in_one_pass`, `needs_current_verification`, `needs_input`, `manual_review`, `refuse_or_stop`.|
|`currentness_sensitivity`|yes|Claim decay risk.|`static`, `low`, `medium`, `high`, `claim_dependent`.|
|`scope_limit`|yes|Maximum safe scope before decomposition.|`single_turn`, `bounded_multi_step`, `atomic_claim`, `read_only_scope`, `locked_write_scope`, `locked_execution_scope`, `criteria_bound`, `terminal`.|
|`sandbox_required`|yes|Whether isolation is required.|`no`, `yes`, `execution_only`, `tool_dependent`, `not_applicable`.|

## Variant Comparison Table

|surface|use_when|do_not_use_when|required_inputs|verification_needed|stop_conditions|common_failure|fallback_route|owner_boundary|
|---|---|---|---|---|---|---|---|---|
|`browser_chat`|Simple advisory answer; low-risk synthesis; no live/current claim; no external mutation; no repo operation.|Current fact needed; source citation required; repo/file write needed; execution needed; high-stakes decision; ambiguous multi-surface request.|Task statement; no volatile claim; no mutation request.|Reasonableness check; mark factual uncertainty if any claim may be volatile.|`SC-STALE`, `SC-OVERLOAD`, `SC-AUTHORITY`, `SC-HIGH_RISK`.|Chat output treated as accepted truth.|`web_current_verification` for volatile claims; `deep_research` for broad research; `manual_review` for high risk.|`aihr_advisory`|
|`thinking_reasoning_mode`|Multi-step reasoning; constraint solving; route planning; architecture tradeoff analysis; decomposition before execution.|Live/current data is the core need; factual verification is required; repo state must be inspected; task is simple enough for direct answer.|Complete problem statement; known constraints; known authority boundary; explicit output form.|Constraint-fit check; contradiction check; route receipt or decision rationale.|`SC-CONFLICT`, `SC-INCOMPLETE_CONTEXT`, `SC-CIRCULAR_REASONING`, `SC-AUTHORITY`.|Reasoning chain mistaken for evidence or source truth.|`web_current_verification` for factual claims; `repo_connector_read` for repo facts; `manual_review` for unresolved authority.|`aihr_advisory`|
|`deep_research`|Broad synthesis; many-source landscape scan; unclear external evidence space; appendix/source-note research; comparative evidence gathering.|Atomic fact lookup; narrow current check; repo-internal question; latency-sensitive answer; execution task.|Research question; scope bounds; source-quality requirements; freshness window; acceptance format.|Source review; conflict log; freshness flags; source-authority classification.|`SC-SOURCE_CONFLICT`, `SC-NO_CREDIBLE_SOURCE`, `SC-SCOPE_CREEP`, `SC-LATENCY`.|Expensive research used where atomic verification would suffice.|`web_current_verification` for narrow claim; `manual_review` for unresolved conflicts; `source_authority_route` if available.|`source_authority`|
|`web_current_verification`|Atomic volatile claim; model/provider/pricing/policy/capability check; date-sensitive fact; current availability/status.|Broad synthesis; stable doctrine; purely internal repo question; no currentness dependency.|Exact claim; acceptable source types; freshness window; required date stamp.|Primary-source match; date check; conflict check; `needs_current_verification` cleared or retained.|`SC-STALE`, `SC-SOURCE_CONFLICT`, `SC-UNVERIFIABLE`, `SC-NON_PRIMARY_SOURCE`.|Weak source treated as current authority.|`deep_research` for broader source search; `manual_review` for conflict; `refusal_stop_route` if unverifiable and required.|`source_authority`|
|`repo_connector_read`|Inspect repo structure, files, issues, PRs, history, or config without mutation; gather context before write/execution.|Mutation requested; tests must be run; local environment required; target repo/path unknown.|Repo selection; branch or commit if relevant; exact path/query; read permission.|Path/branch confirmation; no-write confirmation; source recency check.|`SC-PATH_UNSAFE`, `SC-ACCESS_DENIED`, `SC-BRANCH_UNKNOWN`, `SC-STALE_REPO_CONTEXT`.|Wrong branch or stale file read as current.|`needs_input` for missing path; `repo_connector_write` only after explicit authorization; `manual_review` for ambiguity.|`repo_owner`|
|`repo_connector_write`|Explicitly authorized repo mutation; scoped and reversible change; prior read pass completed; review path available.|No explicit authorization; ambiguous path; broad rewrite; runtime config mutation; missing rollback; no review gate.|Prior read result; exact file path; authorized operation class; rollback plan; diff review expectation.|Diff review; scope check; no unintended files; tests or static checks where applicable.|`SC-PATH_UNSAFE`, `SC-AUTHORITY`, `SC-SCOPE_CREEP`, `SC-TEST_FAIL`, `SC-RUNTIME_CONFIG`.|Write performed without context, review, or authorization.|`repo_connector_read` if context missing; `manual_review` if high risk; `refusal_stop_route` for forbidden mutation.|`repo_owner`|
|`codex_style_repo_execution`|Implement/test in repo environment; multi-file code task; execution required; sandbox confirmed; task spec locked.|Still planning; no sandbox; no test criteria; no authorization; production environment risk; runtime config mutation.|Locked task spec; exact repo/path scope; sandbox/environment confirmation; test command/criteria; rollback plan.|Test run; diff review; scope audit; sandbox boundary confirmation; human review if high consequence.|`SC-SANDBOX_MISSING`, `SC-TEST_CRITERIA_MISSING`, `SC-SCOPE_CREEP`, `SC-FULL_ACCESS_UNAPPROVED`, `SC-TEST_FAIL`.|Code execution treated as safe without sandbox or tests.|`thinking_reasoning_mode` for planning; `repo_connector_read` for context; `manual_review` for high-risk execution.|`repo_owner`|
|`local_script_tool_execution`|Deterministic local computation; file conversion; data processing; repeatable validation; controlled tool use.|Subjective judgment; live web needed; untrusted script; production side effects; unknown environment.|Input files; script/tool definition; expected output schema; environment constraints; side-effect boundary.|Output schema check; side-effect check; reproducibility check; error capture.|`SC-ENV_UNKNOWN`, `SC-SCRIPT_UNTRUSTED`, `SC-OUTPUT_SCHEMA_FAIL`, `SC-SIDE_EFFECT_RISK`.|Tool output treated as semantically validated when only mechanically produced.|`manual_review` for interpretation; `web_current_verification` for live data; `refusal_stop_route` for unsafe script.|`aihr_advisory`|
|`manual_review`|High-stakes decision; irreversible action; authority ambiguity; accepted-truth promotion; low confidence; human judgment required.|No downstream impact; clear low-risk answer; no artifact to review; no defined reviewer role.|Reviewable artifact; reviewer role; acceptance criteria; resume condition.|Human approval/rejection/defer recorded; reason logged.|`SC-REVIEWER_UNDEFINED`, `SC-CRITERIA_MISSING`, `SC-ARTIFACT_INCOMPLETE`.|Rubber-stamp review with no criteria or audit trail.|`qa_audit_pass` if criteria can be formalized; `refusal_stop_route` if authority absent.|`human_reviewer`|
|`qa_audit_pass`|Validate against known checklist; regression check; artifact promotion gate; failure-mode check.|No acceptance criteria; no baseline; purely generative task; QA severity authority required but absent.|Artifact; checklist or criteria; expected state; severity owner if severity classification is needed.|Pass/fail log; finding list; unresolved issues; escalation if blocked.|`SC-CRITERIA_MISSING`, `SC-BASELINE_MISSING`, `SC-QA_AUTHORITY`, `SC-UNREVIEWABLE_ARTIFACT`.|Audit theater: pass/fail declared without criteria.|`manual_review` for judgment; `thinking_reasoning_mode` to define criteria; `refusal_stop_route` if QA authority missing.|`qa_owner`|
|`specialist_handoff`|Task exceeds AIHR authority, domain competence, or tool access; named specialist is required; context transfer needed.|AIHR can resolve directly; no receiving agent; no context package; handoff would drop state.|Receiving specialist; handoff reason; context package; return contract; fallback path.|Handoff acknowledgment; context sufficiency check; return contract acceptance.|`SC-HANDOFF_UNVERIFIED`, `SC-CONTEXT_PACKAGE_MISSING`, `SC-RETURN_CONTRACT_MISSING`.|Cold handoff that forces specialist to rediscover context.|`manual_review` if no specialist; `browser_chat` if AIHR can answer; `refusal_stop_route` if no valid owner.|`specialist_owner`|
|`refusal_stop_route`|Request violates boundary; required authority absent; unsafe or unverifiable dependency blocks route; no valid fallback.|Valid safe route exists; missing information can be requested; refusal is only based on uncertainty not boundary.|Boundary or blocker reason; attempted safe route class; escalation path if any.|Reason documented; allowed alternative or owner path identified if available.|terminal route|Over-refusal without documenting recoverable path.|`manual_review` if owner can decide; `needs_input` if missing input is recoverable.|`terminal_stop`|

## Route-State Implications

|surface|default_route_state|when_to_escalate|unsafe_in_one_pass_trigger|
|---|---|---|---|
|`browser_chat`|`one_pass_safe`|Escalate when current data, source authority, high-stakes impact, or multi-surface scope appears.|User asks for live/current facts, repo changes, or accepted-truth promotion.|
|`thinking_reasoning_mode`|`decompose_first`|Escalate when reasoning depends on external facts, missing context, or authority boundary.|Reasoning output would be used as factual verification or execution approval.|
|`deep_research`|`decompose_first`|Escalate when sources conflict, scope expands, or result would become accepted truth.|Research is asked to execute, mutate, or decide authority.|
|`web_current_verification`|`needs_current_verification`|Escalate when primary sources conflict, are unavailable, or claim cannot be verified.|Volatile claim is routed without date/source verification.|
|`repo_connector_read`|`needs_input`|Escalate when repo/path/branch access is ambiguous.|Read output would be treated as write authorization.|
|`repo_connector_write`|`unsafe_in_one_pass`|Escalate when path, authorization, rollback, or review gate is missing.|Any write is attempted without prior read, scope lock, and explicit authorization.|
|`codex_style_repo_execution`|`unsafe_in_one_pass`|Escalate when sandbox, tests, task spec, or approval is missing.|Execution starts in uncontrolled environment or without test criteria.|
|`local_script_tool_execution`|`needs_input`|Escalate when script trust, environment, or side effects are unclear.|Unreviewed script runs against valuable files or external systems.|
|`manual_review`|`manual_review`|Escalate to owning authority when reviewer role or acceptance criteria are missing.|Review is used as permission without a defined reviewer or resume condition.|
|`qa_audit_pass`|`needs_input`|Escalate when criteria are absent or QA severity authority is required.|QA declares pass/fail without criteria or baseline.|
|`specialist_handoff`|`needs_input`|Escalate when specialist target, context package, or return contract is absent.|Handoff occurs without confirmed receiver or context transfer.|
|`refusal_stop_route`|`refuse_or_stop`|Escalate only if an owning human/agent can resolve the boundary or missing authority.|Stop is bypassed to preserve task momentum.|

## Currentness-Sensitive Claims

|claim_type|can_be_static|must_be_verified_currently|source_type_required|recommended_wording|
|---|---|---|---|---|
|model capability|no|yes|`official_provider_docs` or approved model registry|`needs_current_verification`: verify capability against current provider/model registry before routing on it.|
|pricing|no|yes|`official_pricing_docs`|`needs_current_verification`: verify price at decision time; do not store static price as doctrine.|
|context window|no|yes|`official_provider_docs` or approved model registry|`needs_current_verification`: verify context limit and effective usable limit before routing.|
|named model recommendation|no|yes|approved model registry plus current source note|Prefer surface class. Named model is `needs_current_verification` unless registry-supplied.|
|provider policy|no|yes|`official_provider_docs`, provider policy page, or approved source note|`needs_current_verification`: provider policy may change; cite current source before use.|
|deep research capability|partial|yes for provider/tool specifics|official product/tool docs|Surface behavior is static; provider-specific capability is `needs_current_verification`.|
|Codex/repo execution capability|partial|yes for sandbox/tool specifics|official product/tool docs or repo-local execution doctrine|Surface behavior is static; concrete execution environment is `needs_current_verification`.|
|surface behavioral taxonomy|yes|no|repo-local doctrine|Stable within KB version; update only through KB review.|
|human-in-the-loop standard|yes|claim_dependent|governance doctrine or approved safety source|Human approval is required for high-risk/irreversible actions; thresholds remain policy-owned.|
|structured routing output pattern|yes|no|repo-local templates and schema doctrine|Use structured routing fields; do not output freeform route decisions for high-risk surfaces.|

## Wrong-Surface Failure Matrix

|wrong_route|likely_failure|prevention_rule|correct_surface|
|---|---|---|---|
|`browser_chat` for live verification|Stale or hallucinated current fact becomes accepted truth.|Any volatile claim triggers `web_current_verification`.|`web_current_verification`|
|`deep_research` for narrow fact lookup|Unnecessary latency, cost, and synthesis noise.|Atomic claim gets atomic verification, not broad synthesis.|`web_current_verification`|
|`repo_connector_write` without read/context|Wrong file, wrong branch, or hidden dependency changed.|Write requires prior `repo_connector_read`, exact path, and scope lock.|`repo_connector_read` then `repo_connector_write`|
|`codex_style_repo_execution` without sandbox/test|Unreviewed code or destructive side effects.|Execution requires sandbox, test criteria, and post-run diff/test review.|`codex_style_repo_execution` with gates or `manual_review`|
|`manual_review` used as rubber stamp|Human gate adds latency but no safety.|Manual review requires reviewer role, artifact, criteria, and resume condition.|`qa_audit_pass` or valid `manual_review`|
|`specialist_handoff` without context package|Specialist starts cold; context loss; repeated discovery work.|Handoff requires context package and return contract.|`specialist_handoff` with context package|
|`thinking_reasoning_mode` used as fact verification|Plausible reasoning replaces source truth.|Reasoning may plan; source truth requires verification.|`web_current_verification` or `repo_connector_read`|
|`local_script_tool_execution` for subjective analysis|Tool output falsely appears deterministic or authoritative.|Use scripts only for deterministic computation/transformation.|`thinking_reasoning_mode` or `manual_review`|
|`repo_connector_read` for current provider capability|Internal repo context substitutes for live provider truth.|Provider/model capability claims need current source-authority check.|`web_current_verification`|
|`qa_audit_pass` without criteria|Audit theater; unverifiable pass/fail result.|QA pass requires checklist, baseline, or explicit acceptance criteria.|`thinking_reasoning_mode` to define criteria, then `qa_audit_pass`|
|`refusal_stop_route` for recoverable missing input|Valid work is blocked unnecessarily.|Stop only when boundary/authority/safety blocks route; otherwise request needed input.|`needs_input` route state with target surface|
|`repo_connector_write` for runtime config mutation|AIHR crosses advisory boundary into runtime authority.|Runtime config mutation triggers stop/manual review; AIHR may only recommend.|`manual_review` or `refusal_stop_route`|

## Ranked Content To Integrate

|rank|content_to_integrate|target_file|target_section|evidence_score_1_100|impact_score_1_100|risk_if_missing_1_100|freshness_sensitivity|verification_status|integration_priority|notes|
|---|---|---|---|---|---|---|---|---|---|---|
|1|Surface behavioral comparison schema with required fields for use, exclusion, inputs, verification, stop conditions, fallback, and owner boundary.|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`|`Comparison Schema`|95|99|99|low|`accepted_in_kb_base`|P0|Provider-agnostic; foundation for machine-readable routing.|
|2|Advisory authority boundary for all surface recommendations.|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`|`Authority Boundary`|97|99|98|low|`accepted_in_kb_base`|P0|Prevents AIHR from becoming runtime/config actor.|
|3|Write/execution surfaces classified as `unsafe_in_one_pass`.|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`|`Route-State Implications`|92|95|96|low|`accepted_in_kb_base`|P0|Repo write and execution require read/context, authorization, tests, and review.|
|4|Distinction between `deep_research` and `web_current_verification`.|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`|`Variant Comparison Table`|95|95|95|medium|`accepted_in_kb_base`|P0|Prevents both under-verification and over-research.|
|5|Currentness gate for model/provider/pricing/context/capability claims.|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`|`Currentness-Sensitive Claims`|98|95|96|high|`accepted_in_kb_base`|P0|Volatile claims cannot be routed from memory or static appendix content.|
|6|Specialist handoff requires context package and return contract.|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`|`Variant Comparison Table`|92|93|94|low|`accepted_in_kb_base`|P0|Prevents cold handoff and orphaned work.|
|7|Manual review requires reviewer role, artifact, criteria, and resume condition.|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`|`Variant Comparison Table`|92|97|97|medium|`accepted_in_kb_base`|P0|Prevents rubber-stamp or dead-end review.|
|8|Structured routing output pattern: selected surface must be singular and auditable.|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`|`Comparison Schema`|93|94|93|low|`accepted_in_kb_base`|P1|Aligns appendix with routing-card templates.|
|9|Wrong-surface failure matrix for common routing mistakes.|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`|`Wrong-Surface Failure Matrix`|90|94|95|low|`accepted_in_kb_base`|P1|Operationalizes MISTAKES-style regression prevention.|
|10|Currentness-sensitive deep research and repo execution capability claims stay gated.|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`|`Currentness-Sensitive Claims`|88|85|88|high|`needs_current_verification`|P1|Do not freeze tool/provider features into permanent doctrine.|
|11|Local script/tool execution constrained to deterministic tasks with environment and output validation.|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`|`Variant Comparison Table`|86|88|84|low|`accepted_in_kb_base`|P1|Prevents subjective or unsafe work being treated as deterministic tooling.|
|12|QA/audit pass requires explicit criteria and cannot assign QA severity unless authority exists.|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`|`Variant Comparison Table`|88|90|89|low|`accepted_in_kb_base`|P1|Preserves QA ownership boundary.|
|13|Named model recommendations must route through model registry or current verification.|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`|`Currentness-Sensitive Claims`|90|90|92|high|`accepted_in_kb_base`|P1|Keeps appendix from becoming stale model leaderboard.|
|14|Non-goals list for provider leaderboard, static price table, runtime config, prompt cookbook, and sidecar authority.|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`|`Non-Goals`|95|88|90|low|`accepted_in_kb_base`|P1|Prevents appendix scope creep.|
|15|Candidate provider/tool details may be mentioned only as `needs_current_verification` or deferred to source notes.|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`|`Currentness-Sensitive Claims`|85|82|80|high|`candidate`|P2|Useful only when paired with fresh source-authority evidence.|

## Non-Goals

|non_goal|exclusion_rule|correct_home|
|---|---|---|
|Provider leaderboard|Do not rank providers or named models as permanent truth.|Model registry or current source-authority file.|
|Static price table|Do not store token prices or subscription prices as doctrine.|`web_current_verification` or source notes.|
|Model registry|Do not define current model IDs, availability, limits, or provider-specific capability flags.|Runtime/model registry owner.|
|Runtime config|Do not instruct edits to `openclaw.json`, provider configs, API keys, credentials, MCP permissions, or deployment settings.|Runtime config owner.|
|Prompt cookbook|Do not include system prompts, personas, style prompts, or execution prompts.|Prompt/template owner outside this appendix.|
|Sidecar authority|Do not create YAML/JSON sidecars or imply generated sidecars are source of truth.|Markdown authority; generated artifacts only if separately approved.|
|Accepted-truth promotion|Do not promote candidate research into accepted doctrine.|KB promotion workflow.|
|QA severity authority|Do not assign severity levels as AIHR-owned truth.|QA owner.|
|All-agent orchestration authority|Do not claim AIHR controls receiving agents or global orchestration.|Orchestration owner.|
|Provider policy interpretation|Do not reinterpret provider policy beyond verified source statements.|Provider docs and policy owner.|

## Validation Checklist

|check_id|validation_check|pass_condition|failure_status|
|---|---|---|---|
|`VC-01`|Every surface has `use_when` conditions.|No blank `use_when` cells.|`needs_validation`|
|`VC-02`|Every surface has `do_not_use_when` conditions.|No blank `do_not_use_when` cells.|`needs_validation`|
|`VC-03`|Every execution surface has verification needed.|`repo_connector_write`, `codex_style_repo_execution`, and `local_script_tool_execution` include review/test/output validation.|`needs_validation`|
|`VC-04`|Every volatile claim is marked.|Model, provider, pricing, context, capability, and policy claims use `needs_current_verification` unless verified by approved current source.|`needs_current_verification`|
|`VC-05`|No current model claim is promoted to accepted doctrine.|Named model specifics are absent or explicitly currentness-gated.|`blocked`|
|`VC-06`|No runtime authority is implied.|No instruction authorizes config mutation, provider settings, credentials, MCP grants, or execution.|`blocked`|
|`VC-07`|Provider-specific content stays currentness-gated.|Provider/tool capability details are marked `claim_dependent` or `needs_current_verification`.|`needs_current_verification`|
|`VC-08`|Write/execution surfaces are not one-pass safe.|`repo_connector_write` and `codex_style_repo_execution` are `unsafe_in_one_pass`.|`blocked`|
|`VC-09`|Manual review is not a rubber stamp.|Manual review requires artifact, reviewer, criteria, and resume condition.|`needs_validation`|
|`VC-10`|Specialist handoff has context transfer.|Handoff requires receiving specialist, context package, and return contract.|`needs_validation`|
|`VC-11`|QA/audit pass has criteria.|QA/audit pass requires checklist, baseline, or acceptance criteria.|`needs_validation`|
|`VC-12`|Refusal/stop route documents reason.|Stop route includes blocker reason and escalation path if available.|`needs_validation`|
|`VC-13`|Candidate research remains candidate unless promoted.|Candidate inputs are not written as accepted facts.|`blocked`|
|`VC-14`|Appendix remains provider-agnostic.|Surface classes are stable; provider/model specifics are absent or gated.|`needs_validation`|

## Final Recommendation

AIHR should use this appendix as the surface-selection reference after the compact scaffold files establish mission, boundary, and route-card format.

Recommended load pattern:

|routing_context|load_policy|reason|
|---|---|---|
|Simple low-risk advisory task|Do not load this appendix by default.|`ESSENCE.md` and `BEST_PRACTICES.md` should be sufficient.|
|Surface ambiguity|Load this appendix.|The comparison table resolves wrong-surface risk.|
|Volatile model/provider/pricing/capability claim|Load this appendix plus `APPENDIX_KB_SOURCE_NOTES.md`; route to `web_current_verification`.|Static appendix content cannot prove currentness.|
|Repo write or execution task|Load this appendix plus repo-execution doctrine and routing examples.|Write/execution surfaces are `unsafe_in_one_pass`.|
|Handoff task|Load this appendix plus `TEMPLATES.md`.|Handoff requires context package and return contract.|
|Promotion or audit task|Load this appendix plus `APPENDIX_KB_ROUTING_EXAMPLES.md` and QA criteria.|Surface routing must be regression-checkable.|

Volatile parts review cadence:

|content_type|review_cadence|default_status_if_stale|
|---|---|---|
|Surface behavioral taxonomy|On KB revision or quarterly review.|`accepted_in_kb_base` until superseded.|
|Model/provider/tool capability references|Before each routing use.|`needs_current_verification`|
|Pricing/cost references|Before each routing use.|`needs_current_verification`|
|Context-window/provider-limit references|Before each routing use.|`needs_current_verification`|
|Repo execution safety assumptions|On tool/process change or quarterly review.|`needs_validation` if environment changed.|
|Manual review/HITL governance thresholds|On policy change or quarterly review.|`needs_validation` if threshold owner changed.|
|Candidate research-derived rows|Each KB promotion cycle.|`candidate` or `deferred`|

Final rule:

AIHR may recommend a surface from this appendix. AIHR must not convert that recommendation into execution authority, runtime mutation, accepted-truth promotion, provider policy, model registry truth, or QA severity authority.