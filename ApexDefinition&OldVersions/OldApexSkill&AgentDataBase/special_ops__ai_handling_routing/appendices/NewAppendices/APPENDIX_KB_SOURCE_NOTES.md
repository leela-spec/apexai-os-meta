## class: source_notes  
role: EVIDENCE_DATABASE  
surface: agent_kb_appendix  
quality: reliable  
scope: agent  
purpose: source-authority notes database for AI Handling Routing KB  
dependencies: ESSENCE.md | APPENDIX_KB_SOURCE_MANIFEST.md | APPENDIX_KB_INFORMATION_RANKING_LEDGER.md | APPENDIX_KB_CANDIDATE_LEDGER.md | APPENDIX_KB_CROSS_AGENT_GAP_TRANSFER_ANALYSIS.md  
status: active_appendix  
owner: special_ops__ai_handling_routing  
validator: meta_ops

# APPENDIX_KB_SOURCE_NOTES

## Purpose

This file defines source-authority rules for `special_ops__ai_handling_routing` (`AIHR`).

AIHR uses this appendix to decide:

|decision_area|this_file_defines|this_file_does_not_define|
|---|---|---|
|Source authority|What each source can decide|Whether the source content is promoted as accepted truth|
|Source limits|What each source cannot decide|Runtime behavior or provider policy|
|Freshness|How stale a claim can become before re-verification|Live provider data itself|
|Source-tier trust|Which source tier wins inside a claim domain|A universal ranking across all domains|
|Routing use|How AIHR may cite or depend on each source|Permission to mutate repos, config, registries, credentials, or tools|
|Conflict handling|When to escalate source disagreement|Authority for AIHR to synthesize conflicting truth|

## Authority Boundary

|boundary_id|rule|allowed_aihr_action|forbidden_aihr_action|status|
|---|---|---|---|---|
|`SN-BND-001`|Source notes do not promote claims.|Mark source use as `cite-as-authority`, `corroborate-only`, `background-context`, `candidate-only`, or `do-not-cite-live`.|Promote any claim to `accepted_in_kb_base`.|accepted|
|`SN-BND-002`|Source notes do not replace the source manifest.|Reference source identity, authority, freshness, and usage posture.|Duplicate full manifest coverage, ownership, or inventory content.|accepted|
|`SN-BND-003`|Source notes are not a provider/model registry.|Flag provider/model claims as volatile and route to current verification.|Hardcode live model rankings, provider rosters, model IDs, pricing, quotas, or API availability as permanent doctrine.|accepted|
|`SN-BND-004`|Source notes do not authorize runtime config changes.|Emit advisory stop/escalation guidance when runtime authority is implicated.|Mutate `openclaw.json`, provider settings, model registries, API keys, credentials, MCP grants, or account permissions.|accepted|
|`SN-BND-005`|Source notes only control evidence usage and freshness posture.|Decide source tier, freshness gate, and conflict response.|Execute repo writes, approve QA severity, orchestrate all agents, or finalize truth promotion.|accepted|
|`SN-BND-006`|Candidate evidence remains candidate evidence.|Use candidate sources only with explicit caveat.|Treat `LEARNING_QUEUE.md`, candidate ledgers, or research-result files as settled routing doctrine.|accepted|

## Status Vocabulary

|status|meaning|allowed_action|forbidden_action|
|---|---|---|---|
|`active`|Source record is usable under its declared authority scope and freshness rule.|Use according to `routing_use`.|Use outside `authority_scope`.|
|`candidate`|Source record or content is proposed but not promoted.|Cite as candidate-only or background context.|Use as accepted routing authority.|
|`needs_validation`|Source record exists but has unresolved verification, scope, or freshness questions.|Surface flag and route to validation.|Suppress uncertainty.|
|`needs_current_verification`|Claim is volatile or stale relative to its freshness window.|Verify against an allowed current source before routing on it.|Route as if current.|
|`stale`|Freshness window has expired.|Use only as historical/background context unless re-verified.|Cite for current decisions.|
|`deprecated`|Source is superseded or no longer recommended.|Retain for audit trail.|Use for active routing.|
|`superseded`|Source has a replacement source record.|Follow `superseded_by`.|Continue using the old record.|
|`under_review`|Source is being evaluated for authority, conflict, or promotion.|Escalate to reviewer or use with caveat.|Promote or cite as settled authority.|
|`runtime_authority_not_granted`|Requested action exceeds AIHR authority.|Stop and route to owning authority.|Execute or approve mutation.|

## Source-Note Schema

|field|required|purpose|allowed_values_or_format|
|---|---|---|---|
|`source_id`|yes|Stable machine-readable primary key.|`SRC-AIHR-###`|
|`source_name`|yes|Human-readable source label.|Free text, preferably under 100 characters|
|`source_type`|yes|Classifies the source for authority and freshness routing.|Enum from `Source Type Taxonomy`|
|`source_path_or_url`|yes|Canonical source location.|Repo-relative path, uploaded filename, or official URL placeholder|
|`authority_scope`|yes|Claims this source may decide or support.|Comma-separated domain list|
|`not_authoritative_for`|yes|Claims this source must not decide.|Non-empty comma-separated exclusion list|
|`freshness_sensitivity`|yes|How quickly claims from this source decay.|`critical`, `high`, `medium`, `low`, `static`, `historical`, `candidate-only`|
|`currentness_requirement`|yes|Maximum acceptable claim age or trigger.|`same-day`, `7-day`, `30-day`, `60-day`, `quarterly`, `annual`, `event-triggered`, `indefinite`, `not-current-authority`|
|`last_verified`|yes|Last date this source record was checked for this appendix.|ISO date `YYYY-MM-DD`; use `unknown` only for unverified inherited records|
|`review_due`|yes|Expiry date or trigger for re-verification.|ISO date, `on_model_release`, `on_provider_change`, `on_process_change`, `on_repo_update`, `not-applicable`|
|`routing_use`|yes|How AIHR may use this source in routing output.|`cite-as-authority`, `corroborate-only`, `background-context`, `candidate-only`, `do-not-cite-live`, `administrative-index-only`|
|`known_gap`|yes|Limitation that must travel with the record.|Free text or `none`|
|`source_tier`|yes|Trust tier for conflict resolution inside declared scope.|`T1-official`, `T2-repo-doctrine`, `T3-project-evidence`, `T4-external-research`, `T5-user-local`, `T6-candidate`, `T7-historical`|
|`status`|yes|Lifecycle state of the source record.|Enum from `Status Vocabulary`|
|`scaffold_refs`|optional|Scaffold files that depend on or cite this source.|Comma-separated filenames|
|`appendix_refs`|optional|Appendix files that depend on or cite this source.|Comma-separated filenames|
|`superseded_by`|conditional|Replacement source record if superseded.|`SRC-AIHR-###` or `none`|
|`notes`|optional|Short provenance or audit note.|Free text; no runtime secrets|

## Source Type Taxonomy

|source_type|authoritative_for|not_authoritative_for|freshness_window|allowed_use|
|---|---|---|---|---|
|`official_provider_docs`|Model IDs, API surfaces, official capability flags, context-window statements, modality support, official tool availability.|Pricing, real-world reliability, local routing doctrine, AIHR authority boundaries, accepted-truth promotion.|`30-day` or `event-triggered` on provider release.|`cite-as-authority` for provider capability only; model-specific claims still require `needs_current_verification` if stale.|
|`official_pricing_docs`|Token pricing, billing units, current price tiers, quota-plan pricing when official.|Model capability, model quality, safety, local policy, provider roadmap.|`same-day` for cost-optimized routing.|`cite-as-authority` for cost only when checked in current run or same day.|
|`official_release_notes`|New model/tool launches, behavior changes, breaking changes, version milestones.|Full current availability, pricing, local routing suitability, real-world reliability.|`event-triggered`; re-check on provider release.|`cite-as-authority` for release event claims; corroborate current status with provider docs if routing depends on it.|
|`official_deprecations_page`|EOL dates, migration deadlines, shutdown notices, retired model or tool status.|Successor model suitability, pricing, local routing doctrine.|`event-triggered`; re-check before routing to any named model or provider surface.|`cite-as-authority` for deprecation/EOL gates.|
|`repo_local_scaffold`|AIHR accepted compact doctrine, boundaries, route states, source-authority checks, stop/escalation posture, scaffold reading path.|Runtime config, model registry truth, provider policy, live pricing, API keys, credentials, MCP grants, QA severity, accepted-truth promotion beyond declared scope.|`static`; re-check on repo update.|`cite-as-authority` for AIHR process doctrine.|
|`repo_local_appendix`|Deep AIHR evidence, ledgers, anti-drift records, source manifest entries, candidate provenance, appendix-local schemas.|Live provider state, current pricing, final runtime authority, provider policy.|`quarterly` unless claim category is volatile.|`cite-as-authority` for internal evidence only; `corroborate-only` for provider/model claims.|
|`failure_postmortem`|Observed failure modes, drift classes, destructive-edit patterns, source-authority mistakes, recovery lessons.|Current model performance, current provider capability, current pricing, universal benchmark truth.|`historical`; no expiry for observed event, but interpretation may need review.|`background-context` for risk detection; supports `MISTAKES.md` entries.|
|`process_doctrine`|Execution discipline, patch discipline, repo path discipline, stop conditions, bounded-operation rules, validation/report shape.|Current provider capability, pricing, model rankings, runtime authorization, provider policy.|`static` or `on_process_change`.|`cite-as-authority` for process rules.|
|`external_research_summary`|Comparative analysis, candidate patterns, benchmark commentary, market/tool landscape as of research date.|Sole authority for routing decisions, official provider truth, local doctrine, runtime authority.|`60-day` for model/tool claims; `quarterly` for structural patterns.|`corroborate-only`; never sole authority for active routing.|
|`user_uploaded_runbook`|User-specific workflow constraints, local deployment assumptions, task-local preferences, project-local tool expectations.|Universal AIHR doctrine, live provider truth, runtime permission, cross-user policy.|`event-triggered` when user uploads a newer version.|`cite-as-authority` inside user/task scope only; escalate conflicts with repo-local doctrine.|
|`candidate_ledger`|Proposed improvements, unpromoted candidate rules, deferred design options.|Accepted routing doctrine, live provider truth, current model selection, mandatory behavior.|`candidate-only`; review per KB cycle.|`candidate-only`; blocked from direct routing authority.|
|`source_manifest`|Source inventory, coverage, duplication notes, plausibility gaps, source status overview.|Object-level claims from the sources themselves, live model/provider facts, routing execution.|`quarterly` or on source-index update.|`administrative-index-only`; use to find sources, not to replace them.|

## Currentness Policy

|claim_category|verification_window|trigger_conditions|action_if_stale|
|---|---|---|---|
|Model IDs / availability|`30-day` plus `event-triggered` on provider release/deprecation.|Named model, provider roster, endpoint availability, model-family routing, model-surface compatibility.|Mark `needs_current_verification`; verify against `official_provider_docs` and, where relevant, `official_deprecations_page` before recommending.|
|Pricing / token cost|`same-day` for cost-optimized routing; otherwise cite as stale estimate only if explicitly labeled.|Cost comparison, budget routing, token-price claim, provider tier claim.|Mark `needs_current_verification`; route to `official_pricing_docs`; do not optimize on stale price.|
|Context window / modality|`30-day` plus re-check on model or endpoint change.|Context-limit claim, multimodal capability, tool capability, API surface capability.|Re-verify against `official_provider_docs`; if not verified, route by surface class rather than named model.|
|Deprecation / EOL dates|`event-triggered`; check before named-model routing.|Any model/tool nearing retirement, migration target, provider deprecation announcement.|Hard stop for named routing until checked against `official_deprecations_page` or `official_release_notes`.|
|API surface / endpoint structure|`30-day` plus provider changelog trigger.|API endpoint names, Responses/Chat/Codex/API surface distinctions, tool-calling availability.|Re-verify against provider docs; avoid endpoint-specific recommendation if stale.|
|Agentic tool surfaces|`event-triggered` on tool release, CLI/IDE extension change, MCP server change, or repo-execution surface change.|Codex-like execution, repo connector, MCP, browser automation, deep research, local script execution.|Mark `needs_current_verification`; verify tool surface and permission boundary before recommending.|
|Agent boundary doctrine|`quarterly` or `on_process_change`.|Advisory-vs-runtime boundary, config-impact stop, accepted-truth promotion boundary, QA severity boundary.|Use repo-local scaffold as authority; if conflict appears, escalate to `meta_ops`.|
|Failure / postmortem evidence|Historical event persists; interpretation review `annual` or on repeated failure.|Citing a failure pattern, drift cause, destructive rewrite incident, source-authority substitution.|Use as historical evidence only; do not infer current model behavior from it.|
|Stable process doctrine|`annual` or `on_process_change`.|Patch discipline, stop-on-ambiguity, one-file-at-a-time, validation/report shape.|Re-check process doctrine file if a new process pack is uploaded or repo doctrine changes.|
|External research summaries|`60-day` for model/tool/provider claims; `quarterly` for structural patterns.|Benchmark claims, provider comparisons, agentic-tool trends, route-surface performance.|Downgrade to `corroborate-only`; require official or repo-local source before routing.|
|Candidate ledger entries|Per KB review cycle.|Candidate rule, unpromoted improvement, future template, deferred surface.|Keep `candidate-only`; do not use for active route unless promoted.|

## Source Records

|source_id|source_name|source_type|authority_scope|not_authoritative_for|freshness_sensitivity|currentness_requirement|routing_use|known_gap|status|
|---|---|---|---|---|---|---|---|---|---|
|`SRC-AIHR-001`|`ESSENCE.md`|`repo_local_scaffold`|AIHR compact boundary doctrine, owns/does-not-own, fast route states, minimal routing card, reading map|runtime_config, openclaw_json, provider_policy, model_registry, live_pricing, QA_severity, accepted_truth_promotion|static|on_repo_update|cite-as-authority|Compression-only; evidence lives in appendices|active|
|`SRC-AIHR-002`|`BEST_PRACTICES.md`|`repo_local_scaffold`|Accepted compact practices, source-authority routing checks, manual review stop practices, reading path|runtime_config, provider_policy, live_model_truth, pricing, model_registry|static|on_repo_update|cite-as-authority|Compact; not full evidence database|active|
|`SRC-AIHR-003`|`MISTAKES.md`|`repo_local_scaffold`|Accepted failure patterns, source-authority substitution, verification theater, stale model/provider claims, config-authority overreach|live_provider_status, pricing, benchmark rankings, runtime permission|static|on_repo_update|cite-as-authority|Pattern catalog only; evidence detail in appendix|active|
|`SRC-AIHR-004`|`TEMPLATES.md`|`repo_local_scaffold`|Routing card shapes, source-authority card shapes, handoff card structure, stop-card structure|prompt cookbook bodies, model rankings, provider pricing, runtime config paths|static|on_repo_update|cite-as-authority|Templates are structural, not executable authority|active|
|`SRC-AIHR-005`|`LEARNING_QUEUE.md`|`candidate_ledger`|Future improvements, deferred candidates, unpromoted ideas|active routing doctrine, accepted truth, current provider claims, runtime authority|candidate-only|per_review_cycle|candidate-only|Candidate-only by design|active|
|`SRC-AIHR-006`|`PROMPTFLOW_KB_BASE_BUILD.md`|`process_doctrine`|KB build sequence, target lock, repo boundary, scaffold/appendix architecture, non-targets|live provider claims, runtime config mutation, accepted truth outside KB build|low|on_process_change|cite-as-authority|Build-process authority, not routing-output authority|active|
|`SRC-AIHR-007`|`APPENDIX_KB_SOURCE_MANIFEST.md`|`source_manifest`|Source inventory, coverage, duplication, plausibility gaps, source list|object-level claim truth, live provider state, pricing, model ranking|medium|quarterly|administrative-index-only|Manifest may point to stale records if not audited|active|
|`SRC-AIHR-008`|`APPENDIX_KB_INFORMATION_RANKING_LEDGER.md`|`repo_local_appendix`|Ranked information units, target scaffold placement, excluded unstable/provider claims|live provider truth, current pricing, runtime authority|medium|quarterly|cite-as-authority|Ranking may age as KB evolves|active|
|`SRC-AIHR-009`|`APPENDIX_KB_CANDIDATE_LEDGER.md`|`candidate_ledger`|Candidate provenance, proposed items, unpromoted evidence|accepted routing doctrine, active route decisions, provider truth|candidate-only|per_review_cycle|candidate-only|Must not leak into accepted routing|active|
|`SRC-AIHR-010`|`APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`|`repo_local_appendix`|Drift evidence, failure evidence, anti-drift patterns|current model performance, live pricing, provider availability|historical|annual|background-context|Historical failure evidence needs interpretation|active|
|`SRC-AIHR-011`|`APPENDIX_KB_CROSS_AGENT_GAP_TRANSFER_ANALYSIS.md`|`repo_local_appendix`|Cross-agent gaps, handoff risks, transfer analysis|all-agent orchestration authority, runtime agent registry, provider policy|medium|quarterly|corroborate-only|Dependency listed; current file availability must be checked before use|needs_validation|
|`SRC-AIHR-012`|`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`|`repo_local_appendix`|Mode/tool/work-surface comparison, route-state implications, surface fit|live provider pricing, current model rankings, runtime tool permissions|high|30-day|corroborate-only|Provider-specific rows must carry currentness flags|needs_validation|
|`SRC-AIHR-013`|`APPENDIX_KB_ROUTING_EXAMPLES.md`|`repo_local_appendix`|Routing regression examples, bad-route/correct-route patterns, stop-condition examples|generic prompt templates, runtime config, live provider truth|medium|quarterly|cite-as-authority|Examples test routing; they do not execute routes|needs_validation|
|`SRC-AIHR-014`|`APPENDIX_KB_MACHINE_READABLE_INDEX.md`|`repo_local_appendix`|Enums, route-state index, card fields, stop-condition classes, appendix/scaffold maps|source content truth, runtime configuration, provider live facts|medium|quarterly|administrative-index-only|Indexes authority; does not replace authority|needs_validation|
|`SRC-AIHR-015`|`APPENDIX_KB_SOURCE_NOTES.md`|`repo_local_appendix`|Source authority, freshness policy, conflict handling, source-record schema|source manifest inventory, provider registry, runtime config, truth promotion|static|on_repo_update|cite-as-authority|This file governs evidence use only|active|
|`SRC-AIHR-016`|`RESEARCH_RESULT__APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`|`external_research_summary`|Candidate schema and content for mode/tool comparison appendix|accepted doctrine, current provider truth, pricing, final surface ranking|high|60-day|corroborate-only|Research result; language may include volatile model-era claims|candidate|
|`SRC-AIHR-017`|`RESEARCH_RESULT__APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON_gem.md`|`external_research_summary`|Alternate candidate schema and comparison ideas|accepted doctrine, live provider truth, final routing table|high|60-day|corroborate-only|Variant research; reconcile before promotion|candidate|
|`SRC-AIHR-018`|`RESEARCH_RESULT__APPENDIX_KB_ROUTING_EXAMPLES.md`|`external_research_summary`|Candidate routing examples, stop-condition taxonomy, regression checks|accepted doctrine, live provider truth, runtime execution|high|60-day|corroborate-only|Contains volatile 2026 references; verify before using current claims|candidate|
|`SRC-AIHR-019`|`RESEARCH_RESULT__APPENDIX_KB_MACHINE_READABLE_INDEX.md`|`external_research_summary`|Candidate enum sets, field registries, machine-readable index sections|accepted enum authority, live provider truth, runtime schema generation|medium|60-day|corroborate-only|Candidate index material only|candidate|
|`SRC-AIHR-020`|`RESEARCH_RESULT__APPENDIX_KB_MACHINE_READABLE_INDEX_Gem.md`|`external_research_summary`|Alternate candidate index sections and enum ideas|accepted enum authority, live provider truth, runtime schema generation|medium|60-day|corroborate-only|Variant research; contains simulated/volatile references|candidate|
|`SRC-AIHR-021`|`RESEARCH_RESULT__APPENDIX_KB_SOURCE_NOTES.md`|`external_research_summary`|Candidate source-note schema, currentness policy, high-risk mistakes, ranked integrations|accepted doctrine, live provider truth, pricing, runtime authority|high|60-day|corroborate-only|Source-notes research; normalize before promotion|candidate|
|`SRC-AIHR-022`|`APPENDIX_KB_SOURCE_NOTES_RESEARCH.md`|`external_research_summary`|Earlier source-note research, schema options, source taxonomy, currentness windows|accepted doctrine, live provider truth, pricing, final routing authority|high|60-day|corroborate-only|Earlier variant; lower authority than corrected source-notes research|candidate|
|`SRC-AIHR-023`|`RESEARCH_RESULT__TEMPLATES_PATCH_CANDIDATES.md`|`external_research_summary`|Candidate routing-card fields, template ownership, stop-card and currentness-card recommendations|accepted template doctrine, live provider truth, runtime config|high|60-day|corroborate-only|Contains volatile model/tool references|candidate|
|`SRC-AIHR-024`|`aihr_templates_research_v1.md`|`external_research_summary`|Alternate template candidate research|accepted template doctrine, current provider truth, runtime config|high|60-day|corroborate-only|Variant may conflict with corrected research; use cautiously|candidate|
|`SRC-AIHR-025`|`RESEARCH_RESULT__ESSENCE_PATCH_CANDIDATES.md`|`external_research_summary`|Candidate ESSENCE patches, status vocabulary, read-budget profiles|accepted ESSENCE doctrine, provider truth, runtime authority|medium|60-day|corroborate-only|Candidate-only; do not treat as landed scaffold|candidate|
|`SRC-AIHR-026`|`ESSENCE_patch_candidates_ranked_integration_matrix.md`|`external_research_summary`|Ranked ESSENCE integration matrix, currentness/freshness recommendations|accepted ESSENCE doctrine, live provider truth, model pricing|high|60-day|corroborate-only|Contains volatile GPT-era claims; verify before reuse|candidate|
|`SRC-AIHR-027`|`OpenClaw Model Routing.md`|`user_uploaded_runbook`|User-local OpenClaw routing assumptions, two-agent specialization pattern, OpenAI-only setup constraints|universal AIHR doctrine, live model availability, provider pricing, runtime permission to edit config|high|event-triggered|background-context|Contains specific model names and pricing; require current verification before routing|needs_current_verification|
|`SRC-AIHR-028`|`AI_Useage.md`|`user_uploaded_runbook`|User-local AI usage/process assumptions if directly relevant|accepted AIHR doctrine, provider truth, runtime authority|medium|event-triggered|background-context|Filename typo preserved; content must be checked before use|needs_validation|
|`SRC-AIHR-029`|`AI_Handling_Process_Gem.md`|`process_doctrine`|Anti-drift process design, work-state decomposition, patch discipline, source scoping, preflight risk labeling|current provider truth, live model performance, runtime authority|low|on_process_change|corroborate-only|Contains numeric success-rate claims; treat as process research, not measured AIHR truth|active|
|`SRC-AIHR-030`|`CODEX_GIT_EXECUTION_ESSENCE.md`|`process_doctrine`|Bounded repo execution, authority stack, operation modes, stop conditions, out-of-mode improvement capture|AIHR runtime execution permission, provider truth, live model/tool capability|static|on_process_change|cite-as-authority|Applies when routing to repo execution; AIHR remains advisory|active|
|`SRC-AIHR-031`|`CODEX_RESILIENT_MIGRATION_PROCESS.md`|`process_doctrine`|Migration discipline, exact root lock, closed target set, content preservation, stop-on-ambiguity|current model truth, provider pricing, runtime authority|static|on_process_change|cite-as-authority|Use for repo-migration risk classification only|active|
|`SRC-AIHR-032`|`CODEX_EXECUTION_INSTRUCTION_RELIABLE_REPRODUCED.md`|`process_doctrine`|Reliable bounded execution instruction, path discipline, preservation rules, patch validation|live provider truth, runtime permission, accepted AIHR route result|static|on_process_change|corroborate-only|Duplicate/variant doctrine; prefer compact essence when conflict exists|active|
|`SRC-AIHR-033`|`Improvement_Capture_Rule.md`|`process_doctrine`|Out-of-mode improvement capture, detection vs execution separation|provider truth, routing surface performance, runtime authority|static|on_process_change|corroborate-only|Use to prevent silent scope creep in patch recommendations|active|
|`SRC-AIHR-034`|`INFORMATION_DESIGN_CANON_GPT.md`|`process_doctrine`|Information design canon: chunks, labels, structure, inspectability|AIHR routing doctrine, provider truth, runtime authority|low|annual|corroborate-only|Structural writing support only|active|
|`SRC-AIHR-035`|`TERMINOLOGY_GPT.md`|`process_doctrine`|Information-design vocabulary, terminology consistency|AIHR route-state authority, provider truth, runtime authority|low|annual|corroborate-only|Structural vocabulary support only|active|
|`SRC-AIHR-036`|`FILE_TAXONOMY_GPT.md`|`process_doctrine`|File-class taxonomy, function-typed Markdown files|AIHR source authority, live model truth, runtime authority|low|annual|corroborate-only|Use for appendix/scaffold type shaping|active|
|`SRC-AIHR-037`|`AUDIT_CHECKLIST_GPT.md`|`process_doctrine`|Markdown governance audit checks and severity-style checklist structure|QA severity authority, AIHR accepted doctrine, provider truth|low|annual|corroborate-only|Does not grant QA severity authority|active|
|`SRC-AIHR-038`|`FILE_TAXONOMY_Perp.md`|`process_doctrine`|Alternate file taxonomy candidate|accepted file taxonomy, AIHR routing doctrine, provider truth|low|annual|corroborate-only|Variant; reconcile before promotion|candidate|
|`SRC-AIHR-039`|`SYSTEM_AUDIT.md`|`failure_postmortem`|Cross-file audit strengths, inconsistencies, deploy-blocker pattern examples|current model performance, provider truth, live routing authority|historical|annual|background-context|Duplicate filenames may exist; inspect exact file before citing|active|
|`SRC-AIHR-040`|`KB_SYSTEM_RELIABILITY_AUDIT_V1 (2).txt`|`failure_postmortem`|System reliability audit evidence if available|current provider truth, active doctrine unless promoted|historical|annual|background-context|Availability must be confirmed before use|needs_validation|
|`SRC-AIHR-041`|`prob - prompt design & process failure.md`|`failure_postmortem`|Destructive rewrite and process-failure evidence, manual-check burden, guardrail needs|current model performance, provider truth, active doctrine|historical|annual|background-context|User frustration context; use respectfully and boundedly|active|
|`SRC-AIHR-042`|`Promptflow.md`|`process_doctrine`|Prompt-flow decomposition, artifact-by-artifact generation, evidence-only source constraints|AIHR routing doctrine, live provider truth, runtime authority|low|on_process_change|corroborate-only|Supports one-file-at-a-time generation pattern|active|
|`SRC-AIHR-043`|`AI_Handling_Process_Gem.md`|`process_doctrine`|Resilience ranking, anti-drift guardrails, source scoping, checkpoint verification|measured success rates, current provider truth, runtime authority|medium|annual|corroborate-only|Use qualitative process rules; numeric claims need validation|active|
|`SRC-AIHR-044`|`official_provider_docs`|`official_provider_docs`|Current official provider model/tool/API capability claims|AIHR doctrine, local route authority, pricing, real-world reliability|high|30-day|cite-as-authority|Placeholder source type; concrete provider URL must be supplied during current verification|needs_current_verification|
|`SRC-AIHR-045`|`official_pricing_docs`|`official_pricing_docs`|Current official provider pricing claims|AIHR doctrine, model capability, safety, reliability|critical|same-day|cite-as-authority|Placeholder source type; concrete provider pricing page must be checked in current run|needs_current_verification|
|`SRC-AIHR-046`|`official_release_notes`|`official_release_notes`|Provider release and breaking-change claims|pricing, local suitability, accepted AIHR doctrine|high|event-triggered|cite-as-authority|Placeholder source type; concrete release note required|needs_current_verification|
|`SRC-AIHR-047`|`official_deprecations_page`|`official_deprecations_page`|Provider EOL/deprecation routing gates|successor suitability, cost, local policy|high|event-triggered|cite-as-authority|Placeholder source type; concrete deprecations page required|needs_current_verification|

## High-Risk Source-Authority Mistakes

|mistake|consequence|prevention_rule|target_file_for_rule|
|---|---|---|---|
|Omitting `not_authoritative_for`.|Source scope creeps silently; pricing docs decide capabilities or research summaries decide doctrine.|Every source record must carry a non-empty `not_authoritative_for`; validation fails if absent.|`APPENDIX_KB_SOURCE_NOTES.md`|
|Treating local appendices as live provider truth.|Cached appendix content routes to stale or unavailable models/tools.|Local appendices are authoritative only for internal evidence/schema; provider/model facts require current official verification.|`ESSENCE.md`, `BEST_PRACTICES.md`, `APPENDIX_KB_SOURCE_NOTES.md`|
|Treating candidate ledger as accepted truth.|Unreviewed suggestions enter active routing and create unstable doctrine.|`candidate_ledger` and research-result files must use `routing_use=candidate-only` or `corroborate-only`.|`LEARNING_QUEUE.md`, `APPENDIX_KB_CANDIDATE_LEDGER.md`, `APPENDIX_KB_SOURCE_NOTES.md`|
|Using pricing docs for capabilities.|Cost source wrongly decides model/tool suitability, context window, modality, or safety.|`official_pricing_docs` authority is limited to cost and billing units.|`APPENDIX_KB_SOURCE_NOTES.md`|
|Using failure evidence for current model performance.|Historical incident becomes false current benchmark or unfair model judgment.|`failure_postmortem` supports risk detection only; current performance requires current eval/source verification.|`MISTAKES.md`, `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`|
|Using official docs for real-world reliability without corroboration.|Theoretical capabilities are routed as operational reliability guarantees.|Official docs decide declared capability; real-world reliability requires benchmarks, postmortems, tests, or audit evidence.|`BEST_PRACTICES.md`, `APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`|
|Treating research summaries as primary authority.|Candidate or synthesized research overrides direct sources and produces hallucinated confidence.|`external_research_summary` is always `corroborate-only` unless promoted by KB workflow.|`APPENDIX_KB_SOURCE_NOTES.md`, `APPENDIX_KB_CANDIDATE_LEDGER.md`|
|Using model IDs without surface-scope qualification.|Same model/provider name is recommended for the wrong surface, API, IDE, CLI, or tool path.|Any named model/tool claim must include surface scope or be marked `needs_current_verification`.|`TEMPLATES.md`, `APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`|
|Missing `review_due` for volatile sources.|Stale sources remain `active` indefinitely.|Every `critical`, `high`, or `medium` freshness source must declare `review_due`.|`APPENDIX_KB_SOURCE_NOTES.md`, `LEARNING_QUEUE.md`|
|Letting user-local runbooks override repo-local doctrine silently.|Task-local assumptions become universal AIHR rules.|`user_uploaded_runbook` authority is bounded to user/task scope; conflicts with repo-local scaffold escalate.|`APPENDIX_KB_SOURCE_NOTES.md`, `BEST_PRACTICES.md`|
|Treating source notes as a source manifest.|Inventory duplicates drift and agents read the wrong database.|Source notes define authority/freshness; manifest defines coverage/inventory. Cross-reference rather than duplicate full content.|`APPENDIX_KB_SOURCE_MANIFEST.md`, `APPENDIX_KB_SOURCE_NOTES.md`|
|Hardcoding provider pricing or model rankings in source records.|Volatile current claims become permanent doctrine.|Source records point to source type and verification requirement; they do not reproduce volatile tables.|`APPENDIX_KB_SOURCE_NOTES.md`|

## Conflict Handling

|conflict_type|example|required_response|may_aihr_decide|escalation|
|---|---|---|---|---|
|`provider_vs_repo_boundary`|Official provider docs say an API supports config mutation; AIHR doctrine says AIHR cannot mutate config.|Split domains: provider docs may decide capability; repo scaffold decides AIHR authority. Stop if action would mutate runtime state.|yes, only to enforce AIHR boundary|`meta_ops` or runtime/config owner|
|`provider_capability_conflict`|Two official or near-official sources disagree about model availability or capability.|Mark `needs_current_verification`; cite neither as settled until current official source is verified.|no|provider-current verification route; human reviewer if still conflicting|
|`pricing_conflict`|Pricing page and cached appendix disagree.|Official current pricing doc wins if checked same day; cached appendix becomes stale/background only.|yes, if official same-day source exists|provider-current verification route|
|`deprecation_conflict`|Release note implies availability, deprecations page lists shutdown.|Deprecations page controls EOL gate; block named-model routing until resolved.|yes, for stop decision only|manual review if provider sources remain inconsistent|
|`repo_scaffold_vs_appendix`|Appendix candidate recommends a route state not in scaffold.|Scaffold wins for accepted behavior; appendix item remains candidate unless promoted.|yes|`meta_ops` KB promotion review|
|`research_summary_vs_direct_source`|Research result says a model is best; official docs only confirm existence.|Direct source decides existence; research summary can only corroborate or raise candidate note.|yes, to downgrade research authority|current verification or benchmark-review route|
|`candidate_vs_accepted`|Candidate ledger proposes changing stop condition behavior.|Accepted scaffold remains active; candidate is not used for routing.|yes|KB review / candidate promotion process|
|`failure_postmortem_vs_current_eval`|Historical failure suggests a tool is unreliable; current audited test passes.|Treat postmortem as risk signal, not current performance truth. Require current validation artifact for routing.|partially|QA/audit reviewer|
|`user_runbook_vs_repo_doctrine`|User runbook requests direct config edits; AIHR scaffold forbids runtime mutation.|Repo doctrine controls AIHR boundary; user runbook informs task scope only. Stop and escalate.|yes, for refusal/stop|user + runtime/config owner|
|`manifest_vs_source_record`|Manifest lists source as present; source note marks it stale.|Manifest confirms existence; source note controls freshness/use.|yes|source-manifest maintenance if mismatch persists|
|`source_notes_vs_live_web`|Source note says 30-day window; live provider page changed today.|Live verified official source controls current claim; update source note later through KB process.|no for source mutation; yes for currentness flag|KB patch proposal / `meta_ops`|
|`template_vs_source_authority`|Template field allows `selected_surface`; source note says source is `candidate-only`.|Source authority controls evidence use; template controls shape only.|yes|template/schema review if recurring|

## Ranked Content To Integrate

|rank|content_to_integrate|target_file|target_section|evidence_score_1_100|impact_score_1_100|risk_if_missing_1_100|freshness_sensitivity|verification_status|integration_priority|notes|
|--:|---|---|---|--:|--:|--:|---|---|---|---|
|1|`official_pricing_docs` must use `currentness_requirement=same-day` for cost-optimized routing; cached appendix pricing must not drive active cost routing.|`APPENDIX_KB_SOURCE_NOTES.md`|Currentness Policy + Source Type Taxonomy|97|99|99|critical|needs_current_verification|P0|Keep pricing as source pointer and verification rule, not inline price table.|
|2|`official_deprecations_page` must be a distinct source type from release notes and must gate named-model routing.|`APPENDIX_KB_SOURCE_NOTES.md`|Source Type Taxonomy + Currentness Policy|99|98|99|high|needs_current_verification|P0|EOL/deprecation mistakes are live routing failures.|
|3|Named model/tool IDs must carry surface-scope qualifiers or be marked `needs_current_verification`.|`APPENDIX_KB_SOURCE_NOTES.md`|Source Records + Currentness Policy|96|97|98|high|needs_current_verification|P0|Avoids API/ChatGPT/Codex/MCP surface mismatch.|
|4|`not_authoritative_for` is mandatory for every source record.|`APPENDIX_KB_SOURCE_NOTES.md`|Source-Note Schema + Validation Checklist|95|96|97|static|accepted|P0|Highest leverage anti-scope-creep field.|
|5|Freshness windows must be explicit system contracts through `currentness_requirement`, `last_verified`, and `review_due`.|`APPENDIX_KB_SOURCE_NOTES.md`|Source-Note Schema + Currentness Policy|95|95|96|static|accepted|P0|Prevents stale active records.|
|6|Repo-local scaffold must declare that it is not authoritative for runtime config, provider policy, model registry, `openclaw.json`, or credentials.|`APPENDIX_KB_SOURCE_NOTES.md`|Source Records|85|92|91|static|accepted|P1|Enforces advisory boundary inside source database.|
|7|`external_research_summary` must be `corroborate-only` and cannot be sole authority for active routing.|`APPENDIX_KB_SOURCE_NOTES.md`|Source Type Taxonomy + High-Risk Mistakes|88|87|85|medium|accepted|P1|Blocks candidate research from becoming hidden doctrine.|
|8|Source conflict resolution must be claim-domain-specific, not a single universal tier order.|`APPENDIX_KB_SOURCE_NOTES.md`|Conflict Handling|85|90|88|low|accepted|P1|Provider docs win for provider claims; repo doctrine wins for AIHR boundary.|
|9|User-uploaded runbooks are bounded to user/task scope and cannot silently override repo-local AIHR doctrine.|`APPENDIX_KB_SOURCE_NOTES.md`|Source Type Taxonomy + Conflict Handling|80|80|79|low|accepted|P2|Preserves user context without universalizing it.|
|10|Failure/postmortem evidence is historical risk evidence, not current model-performance truth.|`APPENDIX_KB_SOURCE_NOTES.md`|High-Risk Source-Authority Mistakes|82|84|86|historical|accepted|P1|Prevents overfitting current routes to old failures.|
|11|Source notes must not duplicate the source manifest.|`APPENDIX_KB_SOURCE_NOTES.md`|Authority Boundary + Validation Checklist|84|80|82|low|accepted|P1|Prevents split inventory truth.|
|12|Provider/model/tool current claims in research results must remain `needs_current_verification` until verified in current run.|`APPENDIX_KB_SOURCE_NOTES.md`|Currentness Policy + Source Records|92|88|90|high|needs_current_verification|P0|Avoids stale GPT-era or provider-era assumptions.|
|13|Candidate ledger and learning queue records must be blocked from `cite-as-authority`.|`APPENDIX_KB_SOURCE_NOTES.md`|Source Records + Validation Checklist|90|88|92|candidate-only|accepted|P0|Separates future ideas from accepted doctrine.|
|14|Source records for process doctrine may support repo-execution routing, but do not grant execution authority.|`APPENDIX_KB_SOURCE_NOTES.md`|Source Records + Authority Boundary|88|90|91|static|accepted|P1|Prevents Codex/process docs from becoming permission grants.|
|15|Every volatile source record must carry `review_due`; missing review date downgrades to `needs_validation`.|`APPENDIX_KB_SOURCE_NOTES.md`|Validation Checklist|88|85|86|medium|accepted|P1|Mechanical freshness audit gate.|

## Validation Checklist

|check_id|validation_check|pass_condition|fail_condition|required_action|
|---|---|---|---|---|
|`SN-VAL-001`|Every source record has `authority_scope`.|Field is non-empty and claim-domain-specific.|Empty, vague, or universal authority.|Mark source `needs_validation`.|
|`SN-VAL-002`|Every source record has `not_authoritative_for`.|Field is non-empty and includes at least one meaningful exclusion.|Empty or says `none` without justification.|Reject record until exclusions are added.|
|`SN-VAL-003`|Volatile claims have currentness rules.|`freshness_sensitivity`, `currentness_requirement`, `last_verified`, and `review_due` are present.|Any freshness field missing for volatile source.|Mark `needs_current_verification`.|
|`SN-VAL-004`|Source manifest is not duplicated as full content.|Source notes contain authority/freshness/use posture only.|Full inventory, detailed source excerpts, or manifest replacement appears.|Move inventory detail to manifest.|
|`SN-VAL-005`|No provider/model ranking is promoted.|Rankings are absent or marked `needs_current_verification` / `corroborate-only`.|Ranking appears as accepted doctrine.|Downgrade or remove ranking.|
|`SN-VAL-006`|No runtime authority is implied.|Runtime/config/provider/account actions are marked outside AIHR scope.|Source note implies AIHR may mutate config, keys, provider accounts, registries, or MCP grants.|Replace with stop/escalation language.|
|`SN-VAL-007`|Candidate sources are marked candidate-only or corroborate-only.|`candidate_ledger` = `candidate-only`; research summaries = `corroborate-only`.|Candidate source has `cite-as-authority`.|Reject record or change routing use.|
|`SN-VAL-008`|Repo-local scaffold records include boundary exclusions.|Exclusions include runtime config, model registry, provider policy, `openclaw.json`, and credentials.|Boundary exclusions missing.|Update source record.|
|`SN-VAL-009`|Source conflict rules are domain-specific.|Conflict handling distinguishes provider claims from AIHR doctrine.|Single universal source hierarchy used for all conflicts.|Rewrite conflict rule.|
|`SN-VAL-010`|Historical failure sources are not current-performance sources.|Failure records use `background-context` or risk-evidence language.|Failure source cited as current benchmark truth.|Downgrade and request current verification.|
|`SN-VAL-011`|User-uploaded sources are scope-bounded.|Record states user/task scope and conflict escalation rule.|User-local source becomes universal doctrine.|Mark `needs_validation`.|
|`SN-VAL-012`|Source records avoid secrets and config values.|No API keys, credentials, provider account settings, MCP grant details, or runtime config values.|Any secret/config value appears.|Remove immediately and escalate.|

## Final Recommendation

|usage_context|required_aihr_use_of_this_appendix|output_requirement|
|---|---|---|
|Routine routing|Check whether the source behind the recommendation is authoritative for the relevant claim domain.|Include source-authority posture when material.|
|Model/provider/tool recommendation|Treat model IDs, pricing, capabilities, context windows, deprecations, and provider policies as volatile.|Mark `needs_current_verification` unless verified in the current run against allowed current sources.|
|Source conflict|Apply claim-domain conflict rules; do not synthesize a false consensus.|Stop or escalate when authoritative sources conflict materially.|
|Repo-execution routing|Use process doctrine and failure evidence to classify risk, but do not infer execution permission.|Recommend route, stop condition, validator, and manual review gate when needed.|
|Patch creation|Use this appendix to decide what evidence can support a patch; keep candidate and accepted content separate.|Patch must preserve advisory boundary and avoid promoting volatile claims.|
|Audit|Validate source records against schema, freshness windows, and `not_authoritative_for` exclusions.|Downgrade stale or under-scoped records to `needs_validation` or `needs_current_verification`.|
|Future KB maintenance|Keep source notes as authority/freshness database; keep inventory in source manifest and candidates in candidate ledger.|Do not create sidecar YAML/JSON; maintain machine-readable Markdown tables only.|