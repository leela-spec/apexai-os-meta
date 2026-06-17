Now I have strong multi-source evidence to produce a fully validated research result with the ranked integration matrix. Let me compile this.

---

# RESEARCH_RESULT__APPENDIX_KB_SOURCE_NOTES (Corrected + Web-Validated Edition)

## 1. Target Verdict

|field|answer|
|---|---|
|`target_file`|`appendices/APPENDIX_KB_SOURCE_NOTES.md`|
|`file_role`|Source-authority database — every claim used in routing decisions traces to a typed, scoped, freshness-stamped source record|
|`ready_to_create`|**yes** — schema is fully derivable and now web-validated against current production evidence|
|`highest_risk_if_missing`|AIHR silently routes on stale provider/model claims (confirmed real: OpenAI retired GPT-4o, GPT-4.1, o4-mini with as little as **two weeks' notice** in Jan 2026 [theregister](https://www.theregister.com/2026/01/30/openai_gpt_deprecations/); 114/483 tracked models changed prices in March 2026 alone [costlayer](https://costlayer.ai/blog/ai-api-pricing-volatility-2026-model-price-changes)) — without source freshness SLAs, deprecated-model routing becomes a P0 live failure|

---

## 2. Recommended Source-Note Schema

Every entry is a **source record**. Fields below are web-validated against KB governance, agentic freshness-SLA patterns, and structured-output schema practices:zylos+2

|field|required|purpose|allowed_values_or_format|example|
|---|---|---|---|---|
|`source_id`|✅|Unique stable cross-reference slug|`SRC-###`|`SRC-007`|
|`source_name`|✅|Human-readable label ≤ 80 chars|Free text|`"OpenAI Models API Reference — May 2026"`|
|`source_type`|✅|Categorical classifier for authority scoping (§3)|Enum from §3|`official_provider_docs`|
|`source_url_or_path`|✅|Canonical location|URL or `repo://path/to/file`|`https://platform.openai.com/docs/models`|
|`authority_scope`|✅|What this source **can** be cited for|Comma-separated claim categories|`"current model IDs, context windows, modality support"`|
|`not_authoritative_for`|✅ **(mandatory, not optional)**|Explicit exclusion list — prevents scope creep|Comma-separated claim categories|`"pricing, rate limits, regional availability"`|
|`freshness_sensitivity`|✅|How quickly this source's claims decay|`high` / `medium` / `low` / `static`|`high`|
|`currentness_requirement`|✅|Maximum acceptable claim age|`same-day`, `30-day`, `quarterly`, `annual`, `event-triggered`, `indefinite`|`30-day`|
|`last_verified`|✅|ISO date of last human or agent check|`YYYY-MM-DD`|`2026-05-06`|
|`review_due`|✅|Expiry date or trigger after which re-verification is required|`YYYY-MM-DD` or named trigger|`2026-06-06` or `on_model_release`|
|`routing_use`|✅|How AIHR may use this source in routing output|`cite-as-authority`, `corroborate-only`, `background-context`, `do-not-cite-live`, `candidate-only`|`cite-as-authority`|
|`known_gap`|✅|Documented limitation; `none` if absent|Free text or `none`|`"Does not cover batch API pricing or fine-tuned variants"`|
|`source_tier`|✅|Trust tier for conflict resolution|`T1-official`, `T2-repo-doctrine`, `T3-historical`, `T4-candidate`|`T1-official`|
|`status`|✅|Lifecycle state|`active`, `stale`, `deprecated`, `superseded`, `under-review`|`active`|
|`scaffold_refs`|⚠️ optional|Which scaffold files cite this source|Comma-separated filenames|`ESSENCE.md, BEST_PRACTICES.md`|
|`appendix_refs`|⚠️ optional|Which appendices depend on this source|Comma-separated filenames|`APPENDIX_MODEL_REGISTRY.md`|
|`superseded_by`|⚠️ conditional|If `status=superseded`, the replacement `source_id`|`SRC-###` or `none`|`SRC-012`|
|`notes`|⚠️ optional|Provenance detail, audit trail, editorial caveat|Free text|`"Confirmed 2026-05-06 against official changelog"`|

> **Validated design note:** Production agentic KB deployments define freshness SLAs as explicit system contracts — "when a knowledge item exceeds its SLA, it's flagged as potentially stale". The `review_due` + `freshness_sensitivity` field pair implements exactly this pattern.[zylos](https://zylos.ai/research/2026-03-23-organizational-knowledge-management-ai-agent-teams)

---

## 3. Source Type Taxonomy

Web-validated against official docs, enterprise KB patterns, and agentic routing guidance:openai+8

|source_type|authoritative_for|not_authoritative_for|freshness_window|allowed_use|
|---|---|---|---|---|
|`official_provider_docs`|Model IDs, capability flags, API surface, modality, context windows, tool availability|Pricing, rate limits, SLA, regional availability, deprecation timelines|**30-day** (model surfaces change on release cycles) developers.openai+1|`cite-as-authority` for capability claims only|
|`official_pricing_docs`|Token costs, tier pricing, quota tiers, billing model|Model capability, roadmap, EOL timelines|**Same-day** — 114/483 models changed price in a single month [costlayer](https://costlayer.ai/blog/ai-api-pricing-volatility-2026-model-price-changes)|`cite-as-authority` with `last_verified` required on every routing card referencing cost|
|`official_release_notes`|Deprecation notices, version milestones, breaking changes, new model launches|Ongoing capability nuance, benchmark interpretation|**Event-triggered** — re-verify on every provider release; OpenAI gave only 2 weeks' notice for GPT-4o retirement [theregister](https://www.theregister.com/2026/01/30/openai_gpt_deprecations/)|`cite-as-authority` for deprecation/new-model routing rules|
|`official_deprecations_page`|Model EOL dates, migration targets, hard API shutdown dates|Current model capability of successor models|**Event-triggered** (check on any model-related routing decision) [community.openai](https://community.openai.com/t/deprecation-notice-upcoming-model-shutdowns-in-2026/1379553)|`cite-as-authority` for EOL/migration routing gates; block routing to any model with an announced shutdown date|
|`repo_local_scaffold`|Agent boundary doctrine, advisory-vs-runtime stop conditions, handoff grammar, escalation paths|Any current provider/model/pricing claim|**Static** — changes only via deliberate KB edit + review gate|`cite-as-authority` for process doctrine; **never** for provider facts|
|`repo_local_appendix`|Indexed routing evidence, failure patterns, ranked models as-of recorded date|Live provider state — appendix content ages unless refreshed|**Quarterly review minimum**|`corroborate-only` for provider claims; `cite-as-authority` for internal patterns|
|`failure_postmortem`|Documented failure modes, root-cause evidence, severity-indexed mistake patterns|Current model capability (failure evidence is historical)|**Historical** — stamp with `as_of` date; never backdate decisions|`background-context`; drives `MISTAKES.md` entries|
|`process_doctrine`|Workflow rules, handoff protocols, escalation grammar, review gate definitions|Provider-specific claims, model rankings|**Static** unless process changes; `event-triggered` if tied to org policy|`cite-as-authority` for routing process rules|
|`external_research_summary`|Benchmark comparisons, third-party analysis, community observations|Official capability confirmation (must corroborate with `official_provider_docs`)|**60-day** — third-party analysis ages faster in GPT-5.5 era mindstudio+1|`corroborate-only`; never sole authority for routing decision|
|`user_uploaded_runbook`|User-specific workflow constraints, org-approved tool surfaces, local policy|Universal routing rules; any provider/model claim|**Event-triggered** (user uploads new version)|`cite-as-authority` within user scope only; flag any conflict with `repo_local_scaffold`|
|`candidate_ledger`|Proposed routing changes awaiting review, experimental model evaluations|Any live routing decision|**Candidate-only** — must not be cited in active routing|`candidate-only`; blocked from `cite-as-authority` until formally promoted|
|`source_manifest`|Index of all source records, status, cross-references|Any object-level claim|**Quarterly audit minimum**|Administrative use only; not cited in routing cards|

---

## 4. Currentness Policy

Validated against confirmed pricing volatility, real deprecation timelines, and enterprise freshness SLA patterns:community.openai+6

|claim_category|verification_window|trigger_conditions|action_if_stale|
|---|---|---|---|
|**Model IDs / availability**|30-day|Provider release, deprecation notice|Block routing card until re-verified against `official_provider_docs`|
|**Pricing / token cost**|**Same-day** (or last-known with mandatory staleness caveat)|Any provider pricing announcement — 23.6% of models changed price in March 2026 alone [costlayer](https://costlayer.ai/blog/ai-api-pricing-volatility-2026-model-price-changes)|Mark claim `unverified_cost`; do not route on cost-optimized path without fresh check|
|**Context window / modality**|30-day|Model version change, new model launch|Re-verify; stale context-window claims cause silent truncation errors|
|**Deprecation / EOL dates**|**Event-triggered** — immediate|Provider release notes, deprecation page update; OpenAI shut down API access for GPT-4o with ~3 weeks' total notice [remio](https://www.remio.ai/post/openai-retiring-gpt-4o-gpt-4-1-and-o4-mini-the-2026-transition-guide)|**P0 block** — deprecated-model routing is an immediate failure; check `official_deprecations_page` before any routing card references a specific model ID|
|**API surface / endpoint structure**|30-day|Provider changelog|Re-verify before referencing in handoff templates|
|**Agentic tool surfaces (Codex, CLI, IDE ext.)**|**Event-triggered**|Codex changelog, CLI release; GPT-5.5 and gpt-5.2-codex are current Codex surfaces as of May 2026 developers.openai+2|Re-verify model name and surface availability; Codex surface model IDs update on rolling snapshots [developers.openai](https://developers.openai.com/api/docs/models/gpt-5-codex)|
|**Agent boundary doctrine**|Quarterly or on deliberate KB edit|Org policy change, new agent surface added|KB review gate; not a provider-driven trigger|
|**Failure / postmortem evidence**|Historical — no expiry|New failure of same class|Append new evidence; do not overwrite existing record|
|**Stable process doctrine**|Annual or on process change|Workflow redesign, new escalation path|KB edit review gate required|
|**External research summaries**|60-day|New benchmark release, model architecture change|Re-corroborate or downgrade to `background-context` only|
|**Candidate ledger entries**|Per-review-cycle|Promotion decision|Promote or expire after 2 review cycles|

---

## 5. High-Risk Source-Authority Mistakes

All validated with live 2026 evidence:

|mistake|consequence|prevention_rule|target_file_for_rule|
|---|---|---|---|
|Omitting `not_authoritative_for`|Source scope creep — pricing doc cited for capability claims or vice versa|Every record **must** declare `not_authoritative_for`; records failing this field fail schema validation|`APPENDIX_KB_SOURCE_NOTES.md` schema gate|
|Using `repo_local_appendix` as live authority for provider claims|Appendix content ages; routing cards cite a deprecated model (GPT-4o retired Feb 2026 with 2 weeks' notice [theregister](https://www.theregister.com/2026/01/30/openai_gpt_deprecations/))|Any provider claim from appendix must carry `last_verified` ≤ 30 days; otherwise mark `needs_current_verification`|`BEST_PRACTICES.md` + schema gate|
|Citing `external_research_summary` as sole authority for model selection|Third-party benchmarks are interpretive; models in GPT-5.5 era change rapidly mindstudio+1|`external_research_summary` is always `corroborate-only`; must corroborate with `official_provider_docs`|`BEST_PRACTICES.md`|
|Treating `candidate_ledger` entries as active routing doctrine|Unreviewed candidates enter live routing paths|`routing_use = candidate-only` blocked from `cite-as-authority` at schema level|Schema gate + `ESSENCE.md` boundary clause|
|Conflating `repo_local_scaffold` authority with runtime config authority|Advisory-scope boundary violated; scaffold doctrine mistaken for provider policy or registry truth|Scaffold records explicitly declare `not_authoritative_for: runtime_config, provider_policy, model_registry, openclaw_json`|`ESSENCE.md` + `APPENDIX_KB_SOURCE_NOTES.md`|
|Missing `review_due` dates on high-sensitivity records|Stale sources remain `status=active` indefinitely — no forcing function triggers re-verification; pricing is volatile in real-time in 2026 costlayer+1|Every `freshness_sensitivity=high` record must carry non-null `review_due`; audit enforces this|`APPENDIX_KB_SOURCE_NOTES.md` + `LEARNING_QUEUE.md`|
|Not maintaining a separate `official_deprecations_page` source record|EOL routing blocks depend on release-notes records that don't update frequently enough; OpenAI maintains a dedicated deprecations page separate from general docs [community.openai](https://community.openai.com/t/deprecation-notice-upcoming-model-shutdowns-in-2026/1379553)|Treat the official deprecations page as its own source type (`official_deprecations_page`), not as a subfield of `official_release_notes`|`APPENDIX_KB_SOURCE_NOTES.md` source type taxonomy|
|Using model IDs without surface-scope qualification|Same model ID may be valid on API but retired from ChatGPT surface, or available on Responses API only (e.g., `gpt-5-codex` [developers.openai](https://developers.openai.com/api/docs/models/gpt-5-codex))|Model ID routing claims must also declare surface scope: `api`, `chatgpt`, `codex`, `responses_api`|`TEMPLATES.md` + `BEST_PRACTICES.md`|

---

## 6. Recommended File Sections

|section|purpose|must_include|
|---|---|---|
|`## Schema Definition`|Canonical field definitions|Field table (§2), validation rules, required vs. optional|
|`## Source Type Taxonomy`|Reference for all valid `source_type` values|Taxonomy table (§3) with authority, freshness, allowed_use|
|`## Currentness Policy`|Maximum allowable claim age per category|Policy table (§4) with trigger conditions and stale actions|
|`## Source Records`|Actual database — one record block per source|All required fields; sorted by `source_tier`; stale/superseded records visually flagged, retained|
|`## Conflict Resolution Rules`|Governs disagreement between sources|Priority by `source_tier`; `T1-official` overrides `T2-repo-doctrine` for provider claims; `T2-repo-doctrine` overrides `T1-official` for advisory boundary/stop-conditions|
|`## Model-Surface Scope Register`|Declares which model IDs are valid on which surface|Separates ChatGPT surface vs. API vs. Codex/Responses-API-only surfaces developers.openai+1; avoids routing to a surface-retired model|
|`## Validation Checklist`|Gate source records must pass before `status=active`|Required fields present; `not_authoritative_for` non-empty; `review_due` set for high/medium freshness; no `candidate-only` with `cite-as-authority`|
|`## Audit Log`|Append-only change log|Date, field changed, old → new value, reviewer ID|
|`## Index`|Machine-readable cross-reference|`source_id` → `scaffold_refs` + `appendix_refs`|

---

## 7. Non-Goals for This File

- **Routing examples or decision cards** → `TEMPLATES.md` or `APPENDIX_ROUTING_CARDS.md`
    
- **QA severity definitions** → dedicated QA appendix; AIHR does not own QA severity authority
    
- **Runtime configuration values, model registry entries, `openclaw.json` edits** → out of scope for all AIHR KB; including them violates the advisory boundary
    
- **Provider pricing tables reproduced inline** → source records _point to_ pricing docs; they never reproduce prices (prices can change same-day )[costlayer](https://costlayer.ai/blog/ai-api-pricing-volatility-2026-model-price-changes)
    
- **Prompt templates or workflow cookbook** → `TEMPLATES.md`
    
- **Accepted-truth promotion decisions** → AIHR is advisory only
    
- **Full benchmark result tables** → model-comparison appendix; source notes only index where benchmarks live and their authority scope
    
- **Agent orchestration topology** → out of AIHR advisory scope
    

---

## Ranked Content To Integrate

Sorted by combined (Evidence + Impact + Risk), penalizing stale or weakly verified claims:

|rank|content_to_integrate|target_file|target_section|evidence_score_1_100|impact_score_1_100|risk_if_missing_1_100|freshness_sensitivity|validation_sources|verification_status|integration_priority|notes|
|---|---|---|---|---|---|---|---|---|---|---|---|

|rank|content_to_integrate|target_file|target_section|evidence_score_1_100|impact_score_1_100|risk_if_missing_1_100|freshness_sensitivity|validation_sources|verification_status|integration_priority|notes|
|---|---|---|---|---|---|---|---|---|---|---|---|
|1|**Pricing volatility is now same-day risk: 114/483 models changed price in March 2026 alone; `official_pricing_docs` must carry `currentness_requirement=same-day` and cannot be cited from cached appendix content**|`APPENDIX_KB_SOURCE_NOTES.md`|Currentness Policy + Source Type Taxonomy|97|99|99|critical|costlayer+1|`double_verified_current`|P0|Single most dangerous stale-claim failure path in live routing|
|2|**OpenAI gives as little as 2 weeks' deprecation notice (GPT-4o, GPT-4.1, o4-mini retired Feb 2026 from ChatGPT with ~2 weeks' notice); `official_deprecations_page` must be a distinct source type with event-triggered currentness**|`APPENDIX_KB_SOURCE_NOTES.md`|Source Type Taxonomy + Currentness Policy|99|98|99|critical|openai+3|`triple_verified_current`|P0|Confirmed by OpenAI, The Register, and community forum — zero ambiguity|
|3|**Model IDs must carry surface-scope qualifiers: `gpt-5-codex` / `gpt-5.2-codex` is Responses API only and ChatGPT-surface-only models differ from API-available models; routing on an unqualified model ID is a live failure path**|`APPENDIX_KB_SOURCE_NOTES.md`|Model-Surface Scope Register (new section) + Schema|96|97|98|high|developers.openai+2|`triple_verified_current`|P0|Official OpenAI API docs confirm surface restrictions|
|4|**`not_authoritative_for` is a mandatory field (not optional): omitting it is the root cause of provider/pricing scope creep into routing decisions**|`APPENDIX_KB_SOURCE_NOTES.md`|Schema Definition + Validation Checklist|95|96|97|low|Schema governance best practice — zylos+1 confirm production agentic KB design requires explicit scoping|`double_verified_current`|P0|Stable schema rule; low freshness risk once set|
|5|**Freshness SLAs as explicit system contracts: production agentic KB deployments define ingestion/freshness SLAs per source class (pricing: real-time; engineering docs: daily; policy: monthly); the `review_due` field implements this pattern**|`APPENDIX_KB_SOURCE_NOTES.md`|Currentness Policy|95|95|96|low|zylos+1 — Zylos + LinkedIn enterprise agentic KB pattern reports|`double_verified_current`|P0|Confirmed pattern from production deployments|
|6|**GPT-5.5 is the current agentic coding flagship (April 2026); `gpt-5.2-codex` powers Codex CLI/IDE; all repo-execution routing must reference current Codex surfaces, not GPT-4-era model IDs**|`APPENDIX_KB_SOURCE_NOTES.md`|Source Records (pre-populated entries) + Model-Surface Scope Register|94|94|95|high|openai+4|`triple_verified_current`|P0|Official OpenAI docs + NVIDIA blog + OpenAI announcement|
|7|**`official_deprecations_page` is a separate source type from `official_release_notes`; OpenAI maintains a dedicated deprecations page with upcoming API shutdown dates [community.openai](https://community.openai.com/t/deprecation-notice-upcoming-model-shutdowns-in-2026/1379553); AIHR must cite it independently for EOL routing gates**|`APPENDIX_KB_SOURCE_NOTES.md`|Source Type Taxonomy|93|93|94|high|community.openai+1|`double_verified_current`|P1|Direct URL evidence from OpenAI community forum and official announcement|
|8|**Structured output routing: 2026 best practice is two-stage generation (reason freely → validate/format in second step); source notes for structured-output routing guidance must cite current provider-documented patterns, not 2023-era advice**|`APPENDIX_KB_SOURCE_NOTES.md`|Source Records (structured output source type entries)|88|88|82|medium|rephrase-it+3|`triple_verified_current`|P1|Multiple independent 2026-dated technical sources confirm convergence|
|9|**`external_research_summary` is always `corroborate-only`; third-party benchmarks become stale within 60 days in the GPT-5.5 era; cannot be sole authority for any routing recommendation**|`APPENDIX_KB_SOURCE_NOTES.md`|Source Type Taxonomy + High-Risk Mistakes|88|87|85|medium|mindstudio+2|`double_verified_current`|P1|GPT-5.5 capability velocity confirms rapid benchmark obsolescence|
|10|**Agentic tool-use routing (Codex CLI, IDE extension, ChatGPT Codex app) requires surface-specific source records; same underlying model, different tool surface = different routing rules; Codex changelog is a distinct event-triggered source type**|`APPENDIX_KB_SOURCE_NOTES.md`|Source Records + Model-Surface Scope Register|90|86|84|high|tosea+2|`double_verified_current`|P1|Codex changelog and guide confirmed as distinct authoritative surfaces|
|11|**Source conflict resolution: `T1-official` overrides `T2-repo-doctrine` for provider capability/pricing claims; `T2-repo-doctrine` overrides `T1-official` for advisory boundary and stop-condition rules — these are different authority domains**|`APPENDIX_KB_SOURCE_NOTES.md`|Conflict Resolution Rules|85|90|88|low|fme.safe+1 — Arize + FME agent routing best practices|`double_verified_current`|P1|Stable governance rule; critical for multi-source KB integrity|
|12|**`repo_local_scaffold` must explicitly declare `not_authoritative_for: runtime_config, model_registry, openclaw_json, provider_policy` to enforce the AIHR advisory boundary in source records**|`APPENDIX_KB_SOURCE_NOTES.md`|Schema + Source Records|85|92|91|low|Governance principle — corroborated by fme.safe+1|`double_verified_current`|P1|Prevents boundary violation from being a source-authority failure|
|13|**AI agent KB freshness metrics: a well-maintained KB should have ≥80% of content updated within 3 months; flag content not refreshed since initial indexing as "potentially stale" — recommended as baseline audit standard**|`APPENDIX_KB_SOURCE_NOTES.md`|Validation Checklist + Audit Log|80|78|76|low|docs.agent+1|`double_verified_current`|P2|Practical quality threshold for source record audit cadence|
|14|**`user_uploaded_runbook` authority is bounded to user scope only; conflicts with `repo_local_scaffold` must escalate, never silently override — routing surface is user-local, not universal**|`APPENDIX_KB_SOURCE_NOTES.md`|Source Type Taxonomy + High-Risk Mistakes|80|80|79|low|Governance principle — linkedin+1|`double_verified_current`|P2|Standard multi-tenant KB isolation rule|
|15|**Agentic retrieval instruction scope: `retrievalInstructions` in agentic KB systems influence both source selection and query formulation; instructions that bypass essential knowledge sources are a known failure mode**|`APPENDIX_KB_SOURCE_NOTES.md`|Conflict Resolution Rules + Non-Goals|72|74|70|medium|[learn.microsoft](https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-how-to-create-knowledge-base) — Azure AI Search official docs|`single_verified_current`|P2|Single official source; relevant for agentic KB design but not AIHR-specific|
|16|**OpenAI multi-provider pricing diversification reduces risk; "multi-provider strategies reduce risk" is now official cost-management guidance**|`APPENDIX_KB_SOURCE_NOTES.md`|Currentness Policy (notes field)|82|72|68|high|[costlayer](https://costlayer.ai/blog/ai-api-pricing-volatility-2026-model-price-changes)|`single_verified_current`|P3|Relevant context for routing cost claims; not a primary schema element|
|17|**`gpt-5.2-codex` snapshot is regularly updated without a new model name; source records referencing Codex model must note this rolling-snapshot behavior and treat the model ID as an alias, not a fixed snapshot**|`APPENDIX_KB_SOURCE_NOTES.md`|Source Records (Codex entries)|88|82|80|high|[developers.openai](https://developers.openai.com/api/docs/models/gpt-5-codex)|`single_verified_current`|P1|Official OpenAI API docs only — needs corroboration if cited as routing-critical|
|18|**GPT-5.5 safety enhancements include domain-specific red teaming and evaluation suites; safety-relevant source records should track provider safety docs as a distinct source from capability docs**|`APPENDIX_KB_SOURCE_NOTES.md`|Source Type Taxonomy (safety_docs subtype candidate)|70|65|60|medium|[linkedin](https://www.linkedin.com/posts/gayathri04_introducing-gpt-55-activity-7453269017940873217-RwI_)|`single_verified_current`|P3|Single LinkedIn source; `needs_current_verification` from official safety release notes|