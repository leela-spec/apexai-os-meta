## class: qa_plan  
role: AUDIT  
surface: agent_kb_appendix  
quality: reliable  
scope: agent  
purpose: durable QA, readiness, closure-state, and next-research plan for AI Handling Routing KB  
dependencies: ESSENCE.md | BEST_PRACTICES.md | MISTAKES.md | TEMPLATES.md | LEARNING_QUEUE.md | APPENDIX_KB_CROSS_AGENT_GAP_TRANSFER_ANALYSIS.md | APPENDIX_KB_SOURCE_MANIFEST.md | APPENDIX_KB_INFORMATION_RANKING_LEDGER.md | APPENDIX_KB_CANDIDATE_LEDGER.md | APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md  
status: active_appendix  
owner: special_ops__ai_handling_routing  
validator: meta_ops

# APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN

## Purpose

This appendix is the durable QA, readiness, closure-state, and next-research control surface for the `special_ops__ai_handling_routing` KB.

It exists to answer four operational questions:

|question_id|question|required_output|
|---|---|---|
|`Q-READY`|Is the AIHR KB operationally ready for advisory routing use?|`QA Status` + `Functional Readiness Matrix`|
|`Q-GAP`|Which gaps still block safe finalization?|`Blocking QA Rules` + `Missing Database Candidates`|
|`Q-RESEARCH`|Which research lanes are high-impact enough to run next?|`Research Backlog` + `Next Patch Candidates`|
|`Q-CLOSURE`|Which content is accepted, candidate, validation-gated, deferred, or authority-denied?|`Closure State` + `Do-Not-Promote Findings`|

This file is not a prompt. It is an appendix-level QA control table set.

## Authority Boundary

This file is advisory and audit-oriented only.

|boundary_id|denied_authority|required_handling|
|---|---|---|
|`AB-RUNTIME-CONFIG`|runtime config mutation|stop; route to owning runtime authority|
|`AB-PROVIDER-POLICY`|provider policy definition or override|mark provider claim `needs_current_verification`; route to current official source|
|`AB-MODEL-REGISTRY`|model registry truth, model availability truth, model tier truth|mark as `needs_current_verification`; do not hardcode permanent doctrine|
|`AB-ORCHESTRATION`|all-agent orchestration authority|recommend handoff or escalation only|
|`AB-QA-SEVERITY`|QA severity authority|surface QA-relevant evidence only; do not assign final severity|
|`AB-TRUTH-PROMOTION`|accepted-truth promotion|keep item `candidate` or `needs_validation` until authorized promotion|
|`AB-OPENCLAW-JSON`|direct edits to `openclaw.json`|stop; output advisory-only route card|
|`AB-CREDENTIALS`|API keys, credentials, MCP permission grants, provider account settings|stop; route to security/runtime owner|

## QA Status

|area|status|evidence_basis|blocker|next_action|
|---|---|---|---|---|
|scaffold readiness|`needs_validation`|ESSENCE/BEST_PRACTICES/MISTAKES/TEMPLATES/LEARNING_QUEUE scaffold architecture exists as required activation surface set|current scaffold contents must be checked against latest candidate ledgers before finalization|run scaffold audit pass using this appendix and existing candidate matrices|
|appendix readiness|`needs_validation`|appendices are defined as deeper database/evidence surfaces; multiple appendix research results are available|not all appendix candidates are confirmed as created, promoted, or cross-linked|create or validate missing appendix files in priority order|
|source-authority readiness|`candidate`|source-note research defines source records, authority scopes, freshness windows, and conflict handling|source database may not yet exist as accepted appendix|create/validate `APPENDIX_KB_SOURCE_NOTES.md` or equivalent source-authority appendix|
|routing-example readiness|`candidate`|routing-example research defines example schema, stop conditions, route states, and regression checks|worked examples may remain research-only|create/validate routing example appendix before using examples as regression authority|
|mode/tool comparison readiness|`candidate`|mode/tool comparison research defines surface schemas, use/avoid conditions, verification needs, and fallback routes|current model/provider specifics are volatile|keep specific model/provider/tool claims validation-gated; promote only stable surface-class logic|
|machine-readable index readiness|`candidate`|index research defines route states, card fields, stop classes, authority boundaries, and sidecar policy|index may not yet be accepted as Markdown authority|create/validate Markdown-first machine-readable index before sidecar generation|
|currentness verification readiness|`needs_current_verification`|freshness research identifies provider/model/pricing/tool claims as volatile|no static KB claim can serve as current provider truth|require current verification route for every volatile claim|
|prompt-template boundary readiness|`needs_validation`|template research distinguishes route cards from prompt cookbook entries|TEMPLATES.md may still need universal field schema and ownership boundary patch|patch TEMPLATES.md with advisory-only card fields; keep prompt bodies out|
|runtime-authority boundary readiness|`accepted_in_kb_base`|AIHR mission and boundary doctrine deny runtime config, provider policy, model registry, credentials, and accepted-truth authority|no blocker for advisory boundary; blocker fires only if downstream use treats AIHR as executor|preserve boundary in every route card, example, and appendix|

## Functional Readiness Matrix

|function|ready_state|required_files|current_gap|risk_if_used_now|acceptance_condition|
|---|---|---|---|---|---|
|simple route recommendation|`needs_validation`|`ESSENCE.md`, `BEST_PRACTICES.md`, `TEMPLATES.md`|route-card schema and accepted status vocabulary must be confirmed|over-routing or under-routing simple tasks|simple advisory route card includes `selected_surface`, `confidence_level`, `advisory_only_flag`, and fallback|
|current model/provider/cost claim handling|`needs_current_verification`|`ESSENCE.md`, `BEST_PRACTICES.md`, source-authority appendix, currentness appendix/index|no static claim may be treated as current truth|stale model, pricing, context, or provider-policy claims become routing doctrine|every volatile claim carries `needs_current_verification`, `last_verified_date`, and source type|
|repo execution routing|`needs_validation`|`BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md`, routing examples appendix|exact repo path/mode/test/sandbox gates must be explicit|destructive mutation, path drift, AGENTS-style instruction injection, unreviewed diff|route card requires exact path, operation mode, validation command, rollback/review path, and manual review trigger|
|config-impact stop routing|`accepted_in_kb_base`|`ESSENCE.md`, `MISTAKES.md`, `TEMPLATES.md`|stop card must be represented consistently in templates|AIHR may be misread as allowed to edit runtime config|any config-impact task emits advisory stop card; no execution path included|
|specialist handoff routing|`needs_validation`|`BEST_PRACTICES.md`, `TEMPLATES.md`, machine-readable index|receiving agent identity and return contract may be undefined|cold handoff, context loss, orphaned task|handoff card includes target, context payload, reason, return contract, and fallback|
|source conflict escalation|`candidate`|source-authority appendix, `BEST_PRACTICES.md`, routing examples appendix|source conflict report may not exist|synthesized false consensus between conflicting authorities|conflict route emits stop/escalation card; no silent synthesis|
|overloaded prompt decomposition|`needs_validation`|`BEST_PRACTICES.md`, `TEMPLATES.md`, routing examples appendix|decomposition card may not be canonical|one route surface handles mixed task classes; stop conditions vanish|decomposition card splits independent route classes before any recommendation|
|candidate-to-accepted separation|`needs_validation`|`ESSENCE.md`, `LEARNING_QUEUE.md`, candidate ledger, machine-readable index|promotion workflow authority sits outside AIHR|candidate evidence becomes accepted truth by proximity|every candidate item has status, owner, promotion condition, and forbidden action|

## Blocking QA Rules

|rule_id|blocker|fires_when|required_response|owning_surface|
|---|---|---|---|---|
|`BQR-001`|no static provider/model/cost claims without current verification|output would assert model availability, pricing, context, provider policy, benchmark, tool capability, or deprecation state as current without fresh source|mark `needs_current_verification`; route to current verification; do not assert as accepted truth|source-authority appendix + currentness verification card|
|`BQR-002`|no runtime config authority|task asks AIHR to edit, approve, or finalize runtime config, provider account settings, credentials, MCP permissions, or `openclaw.json`|emit advisory stop card; identify owning authority; halt execution path|ESSENCE.md + manual review stop card|
|`BQR-003`|no candidate promotion by AIHR|candidate, research, or learning-queue item is treated as accepted routing doctrine|label `candidate` or `needs_validation`; require authorized promotion workflow|LEARNING_QUEUE.md + candidate ledger|
|`BQR-004`|no prompt cookbook ownership|route card, template, or appendix includes prompt body, persona instruction, or agent system message payload|move to prompts/workflows owner; keep AIHR structural fields only|TEMPLATES.md|
|`BQR-005`|no repo execution without exact path/mode/validation|repo write, code execution, tool invocation, migration, or test task lacks exact path, mode, sandbox/review status, validation command, or rollback plan|stop; require exact route card fields before routing|BEST_PRACTICES.md + MISTAKES.md + repo execution route card|
|`BQR-006`|no appendix sidecar replacing Markdown authority|YAML/JSON sidecar is proposed as primary authority or is hand-authored independently|reject as authority; require Markdown-first source and generated derivative only after acceptance|machine-readable index appendix|
|`BQR-007`|no source with undefined authority scope|source record lacks `authority_scope`, `not_authoritative_for`, freshness rule, or status|block use as evidence; send to source-authority appendix backlog|source-authority appendix|
|`BQR-008`|no one-pass execution for mixed route classes|task spans more than one independent route class, e.g. model choice + cost claim + repo write + config recommendation|decompose into route cards; block one-pass answer|BEST_PRACTICES.md + overloaded task decomposition card|

## Missing Database Candidates

|candidate_id|missing_database|why_needed|target_file_or_future_file|priority|promotion_condition|
|---|---|---|---|---|---|
|`MDB-001`|source notes|needed to distinguish official provider facts, repo doctrine, research notes, postmortems, and user-uploaded constraints|`APPENDIX_KB_SOURCE_NOTES.md`|P0|schema validated; required fields present; freshness windows assigned; conflict rules defined|
|`MDB-002`|routing examples|needed to regression-test AIHR route decisions against known wrong routes|`APPENDIX_KB_ROUTING_EXAMPLES.md`|P0|examples cover repo write, config stop, stale benchmark, source conflict, cost claim, overloaded task, handoff, simple route|
|`MDB-003`|mode/tool comparison|needed to choose chat, reasoning, research, repo, local script, manual review, QA, or handoff surface|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`|P0|each surface has use/avoid conditions, required inputs, stop conditions, verification, fallback, and boundary|
|`MDB-004`|machine-readable route index|needed to normalize enums, card fields, stop classes, confidence values, and boundary fences|`APPENDIX_KB_MACHINE_READABLE_INDEX.md`|P0|Markdown-first tables accepted; sidecar policy denies hand-authored derivatives|
|`MDB-005`|current model/provider matrix|needed only as future validation-gated lookup for current provider/model/cost/tool claims|`APPENDIX_KB_CURRENT_MODEL_PROVIDER_MATRIX.md` or future equivalent|P1|every row has source type, verified date, review due, volatility tier, and `needs_current_verification` expiry behavior|
|`MDB-006`|source conflict report|needed if material authoritative sources conflict on provider, model, tool, or process claims|`APPENDIX_KB_SOURCE_CONFLICT_REPORT.md` if conflicts exist|P1 conditional|at least one material conflict confirmed; conflict cannot be resolved by authority-scope rules alone|

## Research Backlog

|backlog_id|research_question|why_high_impact|source_type_required|freshness_window|target_destination|status|
|---|---|---|---|---|---|---|
|`RB-001`|Which source types are authoritative for provider capability, pricing, deprecation, context, and tool-surface claims?|prevents stale or wrong source authority from becoming routing truth|official provider docs, official pricing docs, official deprecation pages, repo-local doctrine|provider facts: 7–30 days; doctrine: static until edited|`APPENDIX_KB_SOURCE_NOTES.md`|`candidate`|
|`RB-002`|Which route examples best catch AIHR boundary failures?|examples become regression tests for silent destructive mutation and stale-claim propagation|repo failure postmortems, current agent safety research, AIHR doctrine|30–90 days depending on risk class|`APPENDIX_KB_ROUTING_EXAMPLES.md`|`candidate`|
|`RB-003`|Which surface classes are stable enough for mode/tool comparison without hardcoding provider-specific claims?|prevents false permanence in tool/model routing|current tool docs, repo-local doctrine, process research|30 days for tools; static for surface taxonomy|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`|`needs_current_verification`|
|`RB-004`|Which routing-card fields are mandatory across all AIHR cards?|makes route output auditable and machine-readable|template research, structured output schema guidance, internal KB rules|90 days or on schema change|`TEMPLATES.md` + machine-readable index|`needs_validation`|
|`RB-005`|Which candidate items should remain in LEARNING_QUEUE rather than scaffold?|prevents scaffold bloat and premature doctrine|candidate ledger, failure evidence, patch matrices|per KB review cycle|`LEARNING_QUEUE.md`|`candidate`|
|`RB-006`|What is the minimum attach pack per task type?|avoids context overload and under-loaded risky decisions|ESSENCE patch matrix, scaffold map, appendix map|static until file set changes|this appendix + ESSENCE load policy|`needs_validation`|
|`RB-007`|Which current model/provider/tool/cost claims are still unverified or single-source?|prevents currentness hallucination|official primary sources plus independent corroboration where needed|same-day to 30 days|currentness appendix or source notes|`needs_current_verification`|
|`RB-008`|What source conflict handling rule should apply when repo doctrine conflicts with provider docs?|prevents false synthesis between different authority domains|repo-local scaffold, official provider docs, source-authority research|static for authority rule; current for provider claim|source-authority appendix|`needs_validation`|

## Recommended Attach Pack

|task_type|minimum_attach_pack|optional_attach_pack|do_not_load_by_default|reason|
|---|---|---|---|---|
|activation|`ESSENCE.md`|none|all appendices, `LEARNING_QUEUE.md`|cold start should load boundary, mission, status vocabulary, and high-level routing doctrine only|
|normal routing|`ESSENCE.md` + `BEST_PRACTICES.md` + `TEMPLATES.md`|relevant appendix if route card needs evidence|full appendix set, candidate ledgers|standard routing needs card structure and practice rules, not full research database|
|risky routing|`ESSENCE.md` + `BEST_PRACTICES.md` + `MISTAKES.md` + relevant route appendix|source-authority appendix, machine-readable index|unrelated appendices, candidate-only items|risk signals require failure patterns, stop conditions, and boundary checks|
|source conflict|`ESSENCE.md` + source-authority appendix + relevant source records|source conflict report if created|unrelated mode/tool examples|conflict must be handled by authority-scope rules, not synthesized by prose|
|appendix patching|target appendix + `ESSENCE.md` + `TEMPLATES.md` + source/candidate ledgers|research result for that appendix|unrelated model/provider matrices unless patch touches current claims|patching requires target-specific context and boundary rules; avoid context bloat|
|audit pass|all scaffold files + all appendices + candidate/source ledgers|research notes and postmortems|none|audit requires full evidence surface and can tolerate higher context load|

## Next Patch Candidates

|rank|patch_candidate|target_file|patch_mode|reason|risk|required_validation|
|--:|---|---|---|---|---|---|
|1|Add no-runtime-config-authority declaration and overload/scope escalation triggers|`ESSENCE.md`|`CONTENT_DRAFT`|highest blast-radius boundary rule; prevents advisory-to-executor drift|runtime mutation or config authority hallucination|audit against denied-authority list; verify no config procedure added|
|2|Add status vocabulary: `accepted_in_kb_base`, `candidate`, `needs_validation`, `deferred`, `runtime_authority_not_granted`, `needs_current_verification`|`ESSENCE.md`|`CONTENT_DRAFT`|core machine-readable status language needed across KB|candidate content promoted silently|verify exact allowed status values; no synonyms introduced|
|3|Add currentness/freshness rule for model/provider/tool/pricing/capability claims|`ESSENCE.md` or `BEST_PRACTICES.md`|`CONTENT_DRAFT`|volatile claims must fail closed unless verified|stale provider/model claim becomes routing truth|test with sample volatile claim; output must include `needs_current_verification`|
|4|Add universal routing-card field schema|`TEMPLATES.md`|`CONTENT_DRAFT`|route cards need `card_type`, `advisory_only_flag`, `confidence_level`, `selected_surface`, and `escalation_path`|unparseable or authority-ambiguous cards|validate each template has required fields|
|5|Add manual-review stop card with resume condition|`TEMPLATES.md`|`CONTENT_DRAFT`|high-risk and authority-crossing tasks need explicit halt/resume semantics|deadlock or unsafe continuation|verify `stop_trigger`, `reviewer_role`, `resume_condition`, `human_approval_required`|
|6|Add repo execution vs chat route card|`TEMPLATES.md`|`CONTENT_DRAFT`|repo execution needs exact path, reversibility, risk, validation, and review|destructive write or wrong surface|validate exact-path/mode/test/review fields|
|7|Create source-authority appendix|`APPENDIX_KB_SOURCE_NOTES.md`|`CREATE`|currentness and authority-scoped evidence require database surface|source misuse and stale claims|validate source schema, freshness windows, conflict rules|
|8|Create routing examples appendix|`APPENDIX_KB_ROUTING_EXAMPLES.md`|`CREATE`|examples become regression tests for bad routes|untested boundary and stale-claim behavior|verify all required example types present|
|9|Create mode/tool comparison appendix|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`|`CREATE`|AIHR needs stable surface-class comparison|wrong surface routing|validate each surface row has use/avoid/input/stop/verification/fallback|
|10|Create machine-readable route index|`APPENDIX_KB_MACHINE_READABLE_INDEX.md`|`CREATE`|enums and field registries need fast lookup|hallucinated enums, sidecar split-truth|verify Markdown-first tables and sidecar denial policy|

## Closure State

|closure_item|state|evidence|remaining_gap|owner|
|---|---|---|---|---|
|AIHR advisory mission|`accepted_in_kb_base`|target prompt defines AIHR as advisory routing agent|none for mission statement|special_ops__ai_handling_routing|
|runtime config mutation denial|`accepted_in_kb_base`|target prompt denies runtime config, provider policy, registry, credentials, and `openclaw.json` authority|must be reflected in every scaffold/template/example|special_ops__ai_handling_routing|
|status vocabulary|`needs_validation`|ESSENCE patch research proposes canonical statuses|must be promoted into scaffold and index|meta_ops|
|currentness handling|`needs_current_verification`|research identifies model/provider/tool/cost claims as volatile|requires source-authority database and current verification cards|meta_ops|
|source-authority database|`candidate`|source-notes research provides schema and currentness policy|needs target appendix creation/validation|special_ops__ai_handling_routing|
|routing examples database|`candidate`|routing-example research provides schema and high-impact examples|needs target appendix creation/validation|special_ops__ai_handling_routing|
|mode/tool comparison database|`candidate`|mode/tool research provides comparison schema|model/tool specifics must remain currentness-gated|special_ops__ai_handling_routing|
|machine-readable route index|`candidate`|index research provides enums, sidecar policy, registries|must be created Markdown-first and validated|special_ops__ai_handling_routing|
|prompt-template boundary|`needs_validation`|template research separates AIHR cards from prompt cookbook and runtime config|TEMPLATES.md patch required|special_ops__ai_handling_routing|
|repo execution routing|`needs_validation`|Codex/process research defines exact path/mode/validation controls|route card and examples required|special_ops__ai_handling_routing|
|accepted-truth promotion|`runtime_authority_not_granted`|AIHR boundary denies promotion authority|must route to owning promotion workflow|meta_ops|
|provider/model registry truth|`runtime_authority_not_granted`|AIHR boundary denies model registry authority|must route to registry owner/current official source|provider/model registry owner|
|QA severity authority|`runtime_authority_not_granted`|AIHR boundary denies QA severity authority|AIHR may provide evidence only|QA owner|
|future model/provider matrix|`deferred`|useful but volatile and not required for core advisory boundary|create only after source-authority appendix exists|meta_ops|

## Do-Not-Promote Findings

|finding_id|finding|reason_to_keep_out_of_accepted_truth|permitted_destination|
|---|---|---|---|
|`DNP-001`|specific provider/model rankings|rankings and capabilities are volatile; AIHR does not own registry truth|validation-gated model/provider matrix|
|`DNP-002`|specific provider pricing values|pricing changes require current official verification; stale costs create budget errors|source-authority appendix with same-day/current verification|
|`DNP-003`|benchmark scores as routing doctrine|benchmarks are point-in-time and task-dependent|appendix evidence only with `needs_current_verification`|
|`DNP-004`|prompt bodies inside AIHR templates|prompt cookbook content is outside AIHR ownership|prompts/workflows owner|
|`DNP-005`|runtime config examples that imply edit authority|AIHR may recommend route/stop only; cannot mutate config|runtime owner documentation|
|`DNP-006`|MCP server permission grants or provider account settings|credentials and permission grants are outside AIHR authority|security/runtime owner|
|`DNP-007`|hand-authored YAML/JSON sidecars as primary truth|sidecars create split-truth unless generated from accepted Markdown authority|generated derivative only after Markdown acceptance|
|`DNP-008`|unverified external research summaries as primary authority|third-party research can corroborate but not own provider truth or repo doctrine|source notes as `corroborate-only`|
|`DNP-009`|future A2A/MCP roadmap features as current capability|roadmap items are not present capability|LEARNING_QUEUE.md|
|`DNP-010`|AIHR-owned QA severity rubric|QA severity authority is explicitly outside AIHR|QA-owned appendix or QA agent KB|

## Ranked Content To Integrate

|rank|content_to_integrate|target_file|target_section|evidence_score_1_100|impact_score_1_100|risk_if_missing_1_100|freshness_sensitivity|verification_status|integration_priority|notes|
|--:|---|---|---|--:|--:|--:|---|---|---|---|
|1|No-runtime-config-authority declaration covering `openclaw.json`, provider configs, model registries, API keys, MCP permissions, and runtime state|`ESSENCE.md`|Authority Boundary|97|99|98|low|`accepted_in_kb_base`|P0|structural boundary is stable and already mandated by AIHR mission|
|2|Canonical status vocabulary: `accepted_in_kb_base`, `candidate`, `needs_validation`, `deferred`, `runtime_authority_not_granted`, `needs_current_verification`|`ESSENCE.md` + machine-readable index|Vocabulary / status registry|95|97|92|low|`needs_validation`|P0|use exact values; do not introduce synonyms|
|3|Currentness/freshness policy for model/provider/tool/pricing/context/benchmark claims|`ESSENCE.md` + `BEST_PRACTICES.md`|Currentness|98|95|96|high|`needs_current_verification`|P0|never hardcode volatile claims as permanent doctrine|
|4|Authority-boundary fence table mapping denied action to owner and stop condition|machine-readable index appendix|`authority_boundary_fence`|95|98|99|low|`candidate`|P0|prevents advisory agent from becoming executor|
|5|Stop-condition taxonomy including config, stale claim, source conflict, unsafe path, handoff unverified, and task overload|`BEST_PRACTICES.md` + routing examples appendix|Stop Conditions|94|97|98|low|`needs_validation`|P0|stop conditions must be executable, not prose-only|
|6|Universal routing-card schema with `advisory_only_flag`, `confidence_level`, `selected_surface`, `rejected_surfaces`, and `escalation_path`|`TEMPLATES.md`|Routing Cards|93|94|93|low|`needs_validation`|P0|required before cards can be audited consistently|
|7|Manual-review stop card with `stop_trigger`, `reviewer_role`, `resume_condition`, and `human_approval_required`|`TEMPLATES.md`|Manual Review Stop Card|90|95|96|low|`candidate`|P0|prevents both unsafe continuation and permanent deadlock|
|8|Repo execution vs chat route card with exact path, operation mode, reversibility, risk, validation, and review gates|`TEMPLATES.md`|Repo Execution Card|90|95|95|medium|`candidate`|P0|repo execution must not be one-pass chat advice|
|9|Source-note schema with `authority_scope`, `not_authoritative_for`, freshness, currentness, review due, tier, and status|`APPENDIX_KB_SOURCE_NOTES.md`|Schema Definition|92|94|95|medium|`candidate`|P0|source records without authority scope are blocked|
|10|Routing example schema with route state, bad route, failure risk, correct route, stop conditions, fallback, validator, regression check|`APPENDIX_KB_ROUTING_EXAMPLES.md`|Example Schema|92|93|94|medium|`candidate`|P0|examples must test routing decisions, not become prompt templates|
|11|Mode/tool surface comparison with use/avoid, required inputs, stop conditions, verification, fallback, and owner boundary|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`|Variant Comparison Table|90|92|91|medium|`candidate`|P0|surface classes can be stable; specific models remain verification-gated|
|12|Markdown-first machine-readable index; sidecars generated only after Markdown acceptance|`APPENDIX_KB_MACHINE_READABLE_INDEX.md`|Sidecar Policy / Registry Tables|88|92|91|low|`candidate`|P1|no sidecar may replace Markdown authority|
|13|Recommended attach-pack profiles: activation, normal, risk, audit, source conflict, appendix patching|`ESSENCE.md` + this appendix|Load Policy|91|92|85|low|`needs_validation`|P1|prevents both under-loaded risk and context bloat|
|14|Overloaded task decomposition card with decomposition signal and subtask IDs|`TEMPLATES.md`|Decomposition Card|83|87|85|low|`candidate`|P1|mixed route classes must not execute one-pass|
|15|Source conflict escalation rule by authority domain|source-authority appendix + `BEST_PRACTICES.md`|Conflict Resolution|85|90|88|low|`candidate`|P1|provider docs own provider facts; repo doctrine owns AIHR boundaries|
|16|Learning queue separation rule for promising but unvalidated routing ideas|`LEARNING_QUEUE.md` + machine-readable index|Candidate Registry|90|93|95|low|`needs_validation`|P1|prevents research notes from becoming live routing doctrine|

## Validation Checklist

|check_id|validation_check|pass_condition|fail_condition|
|---|---|---|---|
|`VC-001`|target path correct|target path is `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__ai_handling_routing/appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md`|any other path is named as target|
|`VC-002`|only target file created|this appendix is the only created artifact for this run|scaffold, sidecar, config, or unrelated appendix is modified|
|`VC-003`|no scaffold edited|scaffold files are referenced as dependencies/targets only|final content claims scaffold was patched|
|`VC-004`|no sidecar created|no YAML/JSON sidecar is created or authorized as primary truth|sidecar is described as authority|
|`VC-005`|all status values machine-distinguishable|closure state uses only allowed values|closure state contains unapproved status synonyms|
|`VC-006`|all current provider/model claims flagged|any volatile claim category is marked `needs_current_verification` or omitted|volatile claim is asserted as permanent doctrine|
|`VC-007`|all blocking rules executable|each blocker has fire condition, required response, and owning surface|blocker is prose-only or lacks trigger|
|`VC-008`|no candidate promoted to accepted truth|research/candidate items remain `candidate` or `needs_validation` until promotion|candidate wording implies accepted doctrine|
|`VC-009`|authority boundary preserved|file denies runtime/config/provider/registry/QA/promotion authority|file implies AIHR can execute or approve changes|
|`VC-010`|table schemas stable|required columns are present exactly in each required section|required table missing or schema changed|
|`VC-011`|final recommendation bounded|final section states how future patch passes use this appendix|final section instructs runtime mutation or broad orchestration|
|`VC-012`|no prompt output contamination|file content is actual appendix Markdown|file describes itself as a prompt or instructions for another agent|

## Final Recommendation

Future AIHR patch passes should use this appendix as the QA gate before promoting scaffold or appendix changes.

|use_case|required_action|
|---|---|
|before scaffold patch|check `Blocking QA Rules`, `Closure State`, and `Next Patch Candidates`|
|before appendix creation|check `Missing Database Candidates`, target-file priority, and promotion condition|
|before using research as doctrine|check `Do-Not-Promote Findings` and candidate/accepted separation|
|before provider/model/tool/cost routing|require `needs_current_verification` unless a fresh authority source is attached|
|before repo/config/high-risk routing|emit advisory route or stop card; do not execute|
|before finalization|all P0 candidates must be either accepted through owning workflow, explicitly deferred, or blocked with owner and reason|