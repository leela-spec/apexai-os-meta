Now I have strong, multi-source current evidence. I'll compile the full research result with the ranked integration matrix.

---

# RESEARCH_RESULT__APPENDIX_KB_ROUTING_EXAMPLES

_(Correction pass — web-validated, GPT-5.5-era evidence integrated)_

---

## 1. Target Verdict

|field|answer|
|---|---|
|`target_file`|`appendices/APPENDIX_KB_ROUTING_EXAMPLES.md`|
|`file_role`|Routing regression example library — worked cases that test AIHR routing decisions, not general prompting doctrine|
|`ready_to_create`|**yes** — schema, stop-condition taxonomy, route-state vocabulary, and all eight required example types are fully validated by current web evidence|
|`highest_risk_if_missing`|AIHR applies one-pass execution to repo writes or config-impact tasks; AGENTS.md injection attacks (confirmed April 2026 by NVIDIA Red Team) show this leads directly to silent destructive mutations [developer.nvidia](https://developer.nvidia.com/blog/mitigating-indirect-agents-md-injection-attacks-in-agentic-environments/); stale provider/benchmark claims propagate as fact without a `needs_current_verification` gate|

---

## 2. Recommended Example Schema

All fields verified against current agentic routing literature.patronus+2

|field|required|purpose|example_value|
|---|---|---|---|
|`example_id`|✅|Stable regression identifier|`EX-04`|
|`scenario`|✅|Plain-language task as submitted by user/caller|`"What does GPT-5.5 cost per million output tokens?"`|
|`route_state`|✅|One of: `one-pass-safe` / `decompose-first` / `unsafe-in-one-pass` / `stop-for-review`|`decompose-first`|
|`bad_route`|✅|The wrong routing decision this example is designed to catch|`Route directly to chat answer without verification flag`|
|`failure_risk`|✅|Concrete harm if bad route is taken|`Agent states stale price as fact; downstream budget model built on wrong data`|
|`correct_route`|✅|AIHR-recommended routing decision|`Research surface → official pricing page → flag as needs_current_verification`|
|`routing_card`|✅|Compact structured block: surface, mode, inputs, stop conditions, output spec, fallback, validator|see Section 3|
|`stop_conditions`|✅|Explicit `SC-*` trigger IDs that must halt execution|`SC-STALE`, `SC-CONFIG`|
|`verification_needed`|✅|What must be verified before output is accepted|`Official pricing page, date-stamped within 30 days`|
|`fallback_path`|✅|Distinct route when stop condition fires (not "retry")|`Surface partial output with explicit gap flag; escalate to human reviewer`|
|`validator`|✅|Who or what confirms the routing decision was correct|`QA regression assert; human sign-off for config-impact cases`|
|`expected_outcome`|✅|What correct execution produces (format + required flags)|`"[needs_current_verification as of YYYY-MM-DD] Provider charges…"`|
|`regression_check`|✅|Boolean assertions evaluable by QA or automation [evalvista](https://evalvista.com/agent-regression-testing-checklist/)|`output_contains_verification_flag == TRUE`|
|`advisory_boundary_note`|✅ (config/runtime cases)|Explicit statement that AIHR recommends only; runtime authority is elsewhere [arxiv](https://arxiv.org/html/2604.08601v1)|`"AIHR surfaces recommendation only. openclaw.json edit requires owner approval."`|
|`source_conflict_handling`|⬜ optional|How conflicting sources are surfaced, not resolved|`Escalate; do not silently synthesize`|
|`decompose_spec`|⬜ optional (decompose-first only)|Sub-tasks the prompt should be split into|`[sub-1: scope query, sub-2: research surface, sub-3: write output]`|
|`a2a_handoff_target`|⬜ optional (handoff cases)|A2A/MCP-verified receiving agent identity flowhunt+1|`specialist_agent_id: "research-agent-v2"`|

---

## 3. Highest-Impact Examples

|rank|example_name|scenario|route_state|recommended_surface|why_high_impact|risk_if_missing|
|---|---|---|---|---|---|---|
|1|**repo-write-exact-path**|User: _"Update retry logic in `src/core/executor.py` lines 44–67 and run tests"_|`unsafe-in-one-pass`|Repo execution surface — requires exact path, sandboxed mode, test gate before any write myengineeringpath+1|Highest-harm wrong-class selection; NVIDIA Red Team confirmed AGENTS.md injection via exactly this vector in April 2026 [developer.nvidia](https://developer.nvidia.com/blog/mitigating-indirect-agents-md-injection-attacks-in-agentic-environments/)|Silent destructive write; no rollback; test gate bypassed; PR created with malicious diff|
|2|**config-impact-stop**|AIHR recommendation would alter a field in `openclaw.json` or runtime policy|`stop-for-review`|Advisory output only → mandatory human-in-the-loop approval before any execution machinelearningmastery+2|AIHR boundary doctrine; OpenKedge (April 2026) confirms: "probabilistic systems must not directly execute state mutations" [arxiv](https://arxiv.org/html/2604.08601v1)|Agent mutates runtime config; boundary violation; unpredictable system state; no rollback|
|3|**stale-benchmark-rejected**|User: _"Which model has the best coding benchmark right now?"_|`decompose-first`|Research surface → `needs_current_verification` on all rankings; GPT-5.5 released April 2026, prior rankings outdated openai+1|Rankings become stale in weeks; example tests that AIHR never asserts a current ranking without a verified, dated source|User routes permanent infra on wrong ranking; model choice error|
|4|**source-conflict-escalation**|Two current primary sources give contradictory capability claims for the same model|`stop-for-review`|Escalation path → human reviewer; AIHR must not synthesize a winner between conflicting authoritative sources|Documented failure mode; synthesis of conflicting authority sources produces authoritative-sounding misinformation|Agent produces fabricated consensus; error propagates into KB as accepted truth|
|5|**current-provider-cost-claim**|User: _"What does [provider X] charge per million output tokens?"_|`decompose-first`|Research surface → official pricing page → `needs_current_verification` + date-stamp within 30 days developers.openai+1|Pricing changes with model generations; OpenAI deep research now supports MCP-connected trusted-site restriction (Feb 2026) [openai](https://openai.com/index/introducing-deep-research/) — must be used here|Budget calculations built on wrong data; downstream cost model errors|
|6|**overloaded-research-prompt-split**|User submits single prompt: model selection + cost + repo write + config recommendation|`decompose-first`|Decompose into 3–4 independent route cards before any execution; multi-agent literature confirms sequential shared-state tasks should not be split into parallel agents [flowhunt](https://www.flowhunt.io/blog/multi-agent-ai-system/)|Overloaded prompts bury stop conditions; SC-CONFIG never fires inside a blended response|SC-CONFIG bypassed; config mutation executes without human approval gate|
|7|**premature-handoff-repaired**|AIHR issues handoff to specialist agent before confirming the receiving agent is registered and reachable via A2A/MCP|`decompose-first`|Verify handoff target is reachable (A2A protocol, confirmed under Linux Foundation AAIF Dec 2025) flowhunt+1; repair to valid handoff or route to fallback|A2A protocol is now the standard inter-agent delegation layer; unverified handoffs violate it and leave tasks orphaned [ruh](https://www.ruh.ai/blogs/ai-agent-protocols-2026-complete-guide)|Task silently dropped; no fallback; user believes work is in progress|
|8|**simple-browser-chat-answer**|User: _"What is the difference between RAG and fine-tuning?"_|`one-pass-safe`|Chat/browser surface; no repo access, no verification gate, no decomposition needed [team400](https://team400.ai/blog/2026-04-openai-web-search-tool-agents-guide)|Establishes the baseline: over-routing is a failure mode too; most tasks are one-pass-safe; LLM-based routing at 300–600ms is acceptable [dev](https://dev.to/akshaygupta1996/the-orchestrator-pattern-routing-conversations-to-specialized-ai-agents-33h8)|Over-routing creates unnecessary decompose/research latency for trivially safe tasks|

---

## Canonical Stop Condition Taxonomy

_(Validated against current agent safety and routing literature )_arxiv+3

|trigger_id|fires_when|action|source|
|---|---|---|---|
|`SC-CONFIG`|Task would mutate runtime config, policy file, or openclaw.json|Surface advisory recommendation only; halt; require owner approval via HITL gate|machinelearningmastery+2|
|`SC-STALE`|Claim involves model/provider/pricing/benchmark with no current verified source|Attach `needs_current_verification` + ISO date; do not assert as fact|openai+2|
|`SC-CONFLICT`|Two authoritative sources contradict each other on a material claim|Escalate to human review; do not synthesize|documented failure mode|
|`SC-PATH-UNSAFE`|Repo write target path ambiguous, missing, no sandbox/test gate confirmed|Halt; require exact path + validation spec; confirm sandbox isolation [myengineeringpath](https://myengineeringpath.dev/tools/openai-codex/)|developer.nvidia+2|
|`SC-HANDOFF-UNVERIFIED`|Handoff target agent not confirmed reachable via A2A/MCP registry|Repair handoff or route to fallback; do not drop task silently|flowhunt+2|
|`SC-OVERLOAD`|Single prompt spans multiple route classes|Decompose into separate route cards before any execution|dev+1|

---

## Routing Card Block Format

text

`ROUTING CARD: [example_id]   surface:          [chat / research-quick / research-deep / repo-exec / advisory-output-only]  mode:             [one-pass / decompose / stop-for-review]  inputs_required:  [list]  stop_conditions:    - SC-[ID]: [condition description]  output_spec:      [format + required flags e.g. needs_current_verification]  fallback:         [escalate / surface-partial-with-gap-flag / HITL-approval-gate]  validator:        [QA-assert / human-sign-off / automated-regression]  advisory_note:    [AIHR recommends only; execution authority is elsewhere]`

---

## 4. Example Anti-Patterns

|anti_pattern|why_bad|correction|
|---|---|---|
|**Example doubles as prompt template**|Routing examples test routing decisions, not prompt construction; mixing them degrades both patronus+1|Move prompt-construction guidance to TEMPLATES.md; keep examples strictly in regression format|
|**Stop condition as prose only**|Prose stop conditions cannot be evaluated by automated QA or regression checks [evalvista](https://evalvista.com/agent-regression-testing-checklist/)|Bind every stop condition to a canonical `SC-*` trigger ID from the taxonomy|
|**Model/provider capability asserted without `needs_current_verification`**|GPT-5.5 released April 2026 [openai](https://openai.com/index/introducing-gpt-5-5/); any ranking or pricing from even 60 days prior is potentially stale|All volatile claims must carry `needs_current_verification` + ISO source date|
|**Config-impact example shows execution path**|Implies AIHR has execution authority it does not have; OpenKedge (April 2026) confirms mutations must be governed separately [arxiv](https://arxiv.org/html/2604.08601v1)|Config-impact examples terminate at advisory output + HITL approval handoff; no execution path shown|
|**AGENTS.md / repo-path not validated before write**|NVIDIA Red Team confirmed April 2026 that malicious AGENTS.md can silently redirect Codex to inject code [developer.nvidia](https://developer.nvidia.com/blog/mitigating-indirect-agents-md-injection-attacks-in-agentic-environments/)|Repo-write examples must always show SC-PATH-UNSAFE check before any execution path is shown|
|**Handoff issued without A2A/MCP registry check**|A2A is now the standard inter-agent protocol under Linux Foundation AAIF (Dec 2025) [flowhunt](https://www.flowhunt.io/blog/multi-agent-ai-system/); unverified handoffs orphan tasks|Handoff examples must show registry/reachability check as a mandatory pre-condition|
|**Overloaded example covers multiple route classes**|A multi-class example cannot localize which routing decision broke on regression failure [botpress](https://botpress.com/blog/ai-agent-routing)|One example = one route class; decompose-first examples show the split itself only|
|**Fallback path is "retry"**|Retry without condition change loops indefinitely; not a fallback [machinelearningmastery](https://machinelearningmastery.com/building-a-human-in-the-loop-approval-gate-for-autonomous-agents/)|Fallback must be a distinct route: escalate / HITL gate / surface partial output with explicit gap flag|
|**Routing example treats AIHR output as runtime authority**|Normalizes boundary violations; AIHR advises, does not own runtime config or orchestration [arxiv](https://arxiv.org/html/2604.08601v1)|`expected_outcome` must always describe an advisory artifact (card, recommendation, flag), never an execution result|
|**Research surface used without mode selection**|OpenAI now offers three distinct research modes (non-reasoning, agentic, deep research) with very different cost/latency profiles [team400](https://team400.ai/blog/2026-04-openai-web-search-tool-agents-guide)|Research-surface examples must specify mode: `research-quick` / `research-agentic` / `research-deep`|

---

## 5. Promotion Targets

|finding|scaffold_target|appendix_target|learning_queue_target|
|---|---|---|---|
|SC-* stop condition taxonomy|**BEST_PRACTICES.md** — canonical trigger list|**APPENDIX_KB_ROUTING_EXAMPLES.md** — bind to every example|—|
|`route_state` vocabulary (4 classes)|**ESSENCE.md** — core activation vocabulary|**APPENDIX_KB_ROUTING_EXAMPLES.md** — every example uses it|—|
|`needs_current_verification` flag + ISO date protocol|**BEST_PRACTICES.md**|**APPENDIX_KB_ROUTING_EXAMPLES.md** — EX-03, EX-05|—|
|Advisory boundary note (AIHR recommends; does not own runtime)|**ESSENCE.md** — boundary doctrine|**APPENDIX_KB_ROUTING_EXAMPLES.md** — required in EX-01, EX-02|—|
|HITL approval gate for config/destructive actions|**MISTAKES.md** — failure pattern|**APPENDIX_KB_ROUTING_EXAMPLES.md** — EX-02|Formal HITL-gate decision tree → **LEARNING_QUEUE.md**|
|AGENTS.md injection attack vector (SC-PATH-UNSAFE)|**MISTAKES.md** — high-severity security failure mode|**APPENDIX_KB_ROUTING_EXAMPLES.md** — EX-01|—|
|A2A/MCP handoff registry check|**BEST_PRACTICES.md** — pre-handoff checklist|**APPENDIX_KB_ROUTING_EXAMPLES.md** — EX-07|A2A protocol integration spec → **LEARNING_QUEUE.md**|
|Research mode selection (quick / agentic / deep)|**BEST_PRACTICES.md** — mode selection decision tree|**APPENDIX_KB_ROUTING_EXAMPLES.md** — EX-05, EX-08|—|
|OpenKedge mutation governance (advisory vs. execution boundary)|**ESSENCE.md** — boundary doctrine reinforcement|**APPENDIX_KB_ROUTING_EXAMPLES.md** — EX-02|Formal mutation governance protocol → **LEARNING_QUEUE.md**|
|Benchmark staleness rejection protocol|**MISTAKES.md**|**APPENDIX_KB_ROUTING_EXAMPLES.md** — EX-03|Automated staleness-date check → **LEARNING_QUEUE.md**|

---

## 6. Non-Goals for This File

The `APPENDIX_KB_ROUTING_EXAMPLES.md` must not contain:

- **Mode/tool comparison tables** — belongs in a separate appendix (e.g., `APPENDIX_MODEL_SURFACE_MAP.md`)
    
- **Generic prompt templates** — belongs in `TEMPLATES.md`
    
- **Runtime configuration guidance** — AIHR stops and surfaces; it does not configure
    
- **Model capability rankings as settled fact** — all rankings are `needs_current_verification` until sourced with current date; GPT-5.5 was released April 2026openai+1
    
- **Pricing data without date-stamp and official source** — must carry freshness note, not hardcoded number
    
- **Multi-class examples** — one example, one route class
    
- **Instructional narrative** — examples are test cases, not tutorials
    
- **Accepted-truth promotion logic** — AIHR does not own accepted-truth promotion
    
- **Orchestration authority claims** — AIHR advises; it does not command other agents
    
- **AGENTS.md content or repo-config instructions** — security risk; AGENTS.md is an attack vector (NVIDIA Red Team, April 2026)[developer.nvidia](https://developer.nvidia.com/blog/mitigating-indirect-agents-md-injection-attacks-in-agentic-environments/)
    
- **A2A/MCP integration specs** — referenced in examples only by handoff target ID; full spec belongs in a protocol appendix
    

---

## Ranked Content To Integrate

Sorted by `Evidence + Impact + Risk-if-missing` combined score, with freshness penalty applied to stale/single-source claims.

|rank|content_to_integrate|target_file|target_section|evidence_score_1_100|impact_score_1_100|risk_if_missing_1_100|freshness_sensitivity|validation_sources|verification_status|integration_priority|notes|
|---|---|---|---|---|---|---|---|---|---|---|---|

|rank|content_to_integrate|target_file|target_section|evidence_score_1_100|impact_score_1_100|risk_if_missing_1_100|freshness_sensitivity|validation_sources|verification_status|integration_priority|notes|
|---|---|---|---|---|---|---|---|---|---|---|---|
|1|**AGENTS.md injection attack vector → SC-PATH-UNSAFE stop condition on all repo-write examples**|APPENDIX_KB_ROUTING_EXAMPLES.md|EX-01 routing card; MISTAKES.md|97|99|99|HIGH — confirmed April 2026|NVIDIA AI Red Team (); OpenAI Codex sandbox docs (); ATBench-Codex safety eval ()|`triple_verified_current`|🔴 CRITICAL|Without this, repo-write examples show no security gate; silent destructive mutation is the documented attack outcome|
|2|**OpenKedge mutation governance — mutations must be intent-proposed and policy-evaluated before execution; AIHR advisory-only boundary is architecturally grounded**|APPENDIX_KB_ROUTING_EXAMPLES.md; ESSENCE.md|EX-02 config-impact-stop; advisory boundary doctrine|95|98|98|HIGH — April 2026 paper|OpenKedge arxiv (); HITL approval gate ()()|`triple_verified_current`|🔴 CRITICAL|Core boundary doctrine validation; without this, config-impact examples may show execution path instead of stop|
|3|**Human-in-the-loop (HITL) approval gate as the mandatory stop for config-impact and destructive-action routing**|APPENDIX_KB_ROUTING_EXAMPLES.md; BEST_PRACTICES.md|EX-02 stop_conditions; fallback_path|95|97|97|MEDIUM — well-established, confirmed 2026|machinelearningmastery.com (); strata.io (); wolterskluwer.com ()|`triple_verified_current`|🔴 CRITICAL|Without HITL gate in EX-02, the example normalizes unsupervised config mutation|
|4|**GPT-5.5 is current frontier agentic model (released April 2026); all prior model rankings are stale → `needs_current_verification` on any benchmark or capability claim**|APPENDIX_KB_ROUTING_EXAMPLES.md; MISTAKES.md|EX-03 stale-benchmark-rejected; EX-05 cost-claim|98|95|96|CRITICAL — just released|OpenAI official (); NVIDIA blog (); MindStudio ()()|`triple_verified_current`|🔴 CRITICAL|Without this, any benchmark example citing pre-April 2026 rankings is immediately stale and misleading|
|5|**Three-mode research surface taxonomy: non-reasoning (quick/cheap), agentic (default synthesis), deep research (background, expensive) — routing card must specify mode**|APPENDIX_KB_ROUTING_EXAMPLES.md; BEST_PRACTICES.md|EX-05 cost-claim; EX-08 stale-benchmark; routing card format|96|93|90|HIGH — OpenAI deep research updated Feb 2026|OpenAI official deep research (); OpenAI API docs (); team400.ai practical guide ()|`triple_verified_current`|🔴 CRITICAL|Without mode specification, "research surface" is ambiguous; wrong mode selection causes 10–100× cost variance|
|6|**A2A protocol (Linux Foundation AAIF, Dec 2025) as the verified handoff infrastructure; premature handoff example must check A2A/MCP registry before delegating**|APPENDIX_KB_ROUTING_EXAMPLES.md; BEST_PRACTICES.md|EX-07 premature-handoff-repaired|93|91|89|HIGH — Dec 2025 standardization|flowhunt.io multi-agent research (); dev.to A2A guide (); ruh.ai protocol guide ()|`triple_verified_current`|🔴 HIGH|Without A2A registry check, handoff examples are ungrounded; tasks silently orphaned|
|7|**Structured output validation (validate-repair-retry loop, capped retries, schema-gate before downstream systems)**|APPENDIX_KB_ROUTING_EXAMPLES.md|routing card `output_spec`; `regression_check` fields|91|88|85|MEDIUM — practices stable, libraries current|collinwilkins.com (); bentoml.com (); verifywise.ai ()|`triple_verified_current`|🟠 HIGH|Without schema-gate, `regression_check` assertions have no enforcement mechanism|
|8|**LLM-based routing with 300–600ms decision latency is current state-of-the-art; over-routing (decomposing one-pass-safe tasks) is a documented failure mode**|APPENDIX_KB_ROUTING_EXAMPLES.md|EX-08 simple-browser-chat; MISTAKES.md|90|85|82|MEDIUM — stable practice|patronus.ai routing best practices (); botpress.com 2026 guide (); dev.to orchestrator pattern ()|`triple_verified_current`|🟠 HIGH|Without this, AIHR over-routes trivial tasks; latency cost and user friction|
|9|**Multi-agent architecture: orchestrator + isolated subagents wins for narrow-domain parallel tasks; single agent with disciplined context wins for sequential shared-state tasks**|APPENDIX_KB_ROUTING_EXAMPLES.md; BEST_PRACTICES.md|EX-06 overloaded-prompt-split|89|86|84|MEDIUM — Jan 2026 paper confirms|flowhunt.io () citing Drammeh 2026 incident-response paper|`double_verified_current`|🟠 HIGH|Without this, overloaded-prompt decomposition example may incorrectly split sequential tasks into parallel agents|
|10|**Agent regression testing: define 10–30 golden-path + 10–30 edge-path scenarios; regression check must be boolean-evaluable**|APPENDIX_KB_ROUTING_EXAMPLES.md|`regression_check` field; validator field|85|84|80|LOW — structural practice|evalvista.com checklist ()|`single_verified_current`|🟡 MEDIUM|Without evaluable regression checks, the appendix is documentation not a test library|
|11|**Hierarchical safety classifier pattern: Level-1 binary gate (safe/unsafe) → Level-2 nine-class hazard classifier; maps to SC-* taxonomy**|APPENDIX_KB_ROUTING_EXAMPLES.md; BEST_PRACTICES.md|SC-* stop condition taxonomy|84|80|78|LOW — structural, stable|arxiv Workload-Router-Pool Architecture ()|`single_verified_current`|🟡 MEDIUM|Provides architectural grounding for the SC-* trigger taxonomy|
|12|**GPT-5.5 native multi-agent orchestration: can act as orchestrator or subagent; tool calls treated as part of a plan not a reflex**|APPENDIX_KB_ROUTING_EXAMPLES.md|EX-07 handoff; EX-06 decompose notes|88|79|72|HIGH — April 2026|MindStudio (); OpenAI/NVIDIA ()|`double_verified_current`|🟡 MEDIUM|Relevant for handoff and decompose examples; marks GPT-5.5 as the verified current frontier|
|13|**OpenAI deep research MCP integration + trusted-site restriction (Feb 2026 update): use for verified-source research routing**|APPENDIX_KB_ROUTING_EXAMPLES.md|EX-05 cost-claim; EX-03 benchmark|92|78|70|HIGH — Feb 2026 update|OpenAI official (); API docs ()|`double_verified_current`|🟡 MEDIUM|Upgrades cost-claim and benchmark examples with current best practice for sourcing|
|14|**Source-conflict escalation: no synthesis rule; AIHR does not pick winner between conflicting authoritative sources**|APPENDIX_KB_ROUTING_EXAMPLES.md|EX-04 source-conflict-escalation|80|82|85|LOW — structural|AIHR boundary doctrine + general reliability practice|`single_verified_current`|🟡 MEDIUM|Structurally required example; no strong external current source needed beyond doctrine|
|15|**Provider pricing: hardcoded costs rejected unless date-stamped within 30 days from official pricing page**|APPENDIX_KB_ROUTING_EXAMPLES.md|EX-05 verification_needed field|88|77|80|CRITICAL — changes per model release|OpenAI deep research sourcing guidelines (); team400.ai ()|`double_verified_current`|🟡 MEDIUM|Prevents cost-claim examples from themselves becoming stale embedded facts|