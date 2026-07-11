<!--
DOCUMENT TYPE: Research Result — NOT a patch, NOT an authority file
TARGET FILE: appendices/APPENDIX_KB_MACHINE_READABLE_INDEX.md
AGENT: special_ops__ai_handling_routing (AIHR)
GENERATED: 2026-05-06
STATUS: Research output for KB integration review — all items require human promotion before becoming ACCEPTED
MACHINE INDEX: read-only reference. Source of truth = listed authority files. Sidecars are generated artifacts.
-->

# RESEARCH_RESULT__APPENDIX_KB_MACHINE_READABLE_INDEX

> **Advisory boundary**: This document researches what should go into the KB index file. It does not modify KB files, does not assert routing authority, and does not promote any item to ACCEPTED status. All proposed enums, tables, and schema elements are CANDIDATE until promoted by the KB maintenance workflow.

---

## 1. Target Verdict

| field | answer |
|---|---|
| `target_file` | `appendices/APPENDIX_KB_MACHINE_READABLE_INDEX.md` |
| `file_role` | Markdown-first machine-readable index of AIHR route states, routing-card fields, stop conditions, appendix/scaffold surfaces, authority boundary fence, confidence and status enums — enabling agent fast-lookup without full KB scan |
| `ready_to_create` | **yes** |
| `highest_risk_if_missing` | Agents cannot enumerate valid route states or card fields deterministically → fall back to hallucinated enums, silent authority-boundary violations, and CANDIDATE content treated as ACCEPTED truth [cite:22][cite:42] |
| `evidence_strength` | HIGH — multi-source validated: production LLM routing research [cite:22][cite:25], agentic governance frameworks [cite:31][cite:33], structured-output schema design [cite:24][cite:30], machine-readable KB patterns [cite:36][cite:42] |
| `advisory_boundary_preserved` | Yes — this file indexes and points; it does not govern, execute, promote, or configure |
| `current_verification_posture` | All model-name, pricing, and specific-capability claims are flagged `needs_current_verification` per freshness rules. Structural/schema claims are `STABLE`. |

---

## 2. Recommended Index Sections

Research validates the following sections as high-value for agent fast-lookup. Evidence sources are cited per section.

| section | purpose | indexed_items | source_of_truth | evidence |
|---|---|---|---|---|
| `route_state_index` | Enumerate all valid AIHR route states as machine-readable rows with allowed transitions | State name, enum value, description, allowed next states, stop eligibility | `BEST_PRACTICES.md` + `TEMPLATES.md` | [cite:22][cite:28] |
| `routing_card_fields` | Normalize all fields a routing card must/may carry for reliable handoff | Field name, required/optional, data type, valid enum ref, authority source | `TEMPLATES.md` | [cite:24][cite:30] |
| `stop_condition_classes` | Enumerate stop triggers and handling class to prevent silent overrun | Class name, trigger condition, required agent action, escalation path | `MISTAKES.md` + `BEST_PRACTICES.md` | [cite:33][cite:55][cite:58] |
| `confidence_values` | List valid confidence enum values with routing implications | Enum value, routing implication, escalation threshold, example trigger | `ESSENCE.md` | [cite:22][cite:58] |
| `currentness_statuses` | Enumerate freshness states for volatile model/tool/capability claims | Status value, verification requirement, TTL/recheck cadence, promotion authority | `ESSENCE.md` | [cite:31][cite:39] |
| `source_authority_fields` | Map which KB file owns which type of truth to prevent split-truth | Authority domain, owning file, read-only consumers, mutation restriction | `ESSENCE.md` | [cite:33][cite:42] |
| `appendix_surface_map` | Index all appendix files: role, schema type, access pattern, write authority | File path, role, schema format, update cadence, write authority, read consumers | Each appendix file itself | [cite:36][cite:39] |
| `scaffold_surface_map` | Index all five scaffold files with doctype and key sections for token-efficient retrieval | File path, doctype, last-modified field, key sections list | Each scaffold file itself | [cite:2] |
| `candidate_status_values` | Enumerate lifecycle states a KB item can be in to prevent CANDIDATE promotion without review | Status value, meaning, promotion criteria, demotion path | `LEARNING_QUEUE.md` | [cite:31][cite:42] |
| `recommended_surfaces` | List valid advisory route targets with capability class and freshness flag | Surface ID, surface type, capability class, authority note, `needs_current_verification` flag | `BEST_PRACTICES.md`; volatile entries flagged | [cite:22][cite:25][cite:43] |
| `authority_boundary_index` | Quick-reference of what AIHR may NOT do — critical advisory-vs-runtime fence | Forbidden action, risk if violated, owning authority, enforcement mechanism | `ESSENCE.md` | [cite:31][cite:33] |
| `mcp_surface_registry` | Index MCP-exposed tool surfaces that AIHR may route to (advisory, not config) | Server ID, capability class, transport type, audit status, `needs_current_verification` | `BEST_PRACTICES.md` | [cite:51][cite:54][cite:57] |
| `escalation_tier_map` | Map HITL escalation tiers for stop conditions requiring human review | Tier name, approval authority, trigger condition, routing card type | `BEST_PRACTICES.md` | [cite:52][cite:55][cite:58] |

---

## 3. Normalized Enums

All enum values below are CANDIDATE status. Sourced from production routing research [cite:22][cite:25][cite:28], agentic safety frameworks [cite:33][cite:55], and structured-output schema best practice [cite:24][cite:30].

### 3.1 overload_class

| enum_group | value | meaning | allowed_action | forbidden_action |
|---|---|---|---|---|
| `overload_class` | `TOKEN_OVERLOAD` | Task context exceeds safe model window; production systems show 1M+ token windows for frontier models but smaller surfaces have hard limits [cite:19] | Recommend chunking, summarize-first path, or lighter surface | Auto-truncate without advisory note |
| `overload_class` | `LATENCY_OVERLOAD` | Task latency budget incompatible with selected surface; routing to cheaper/faster tier reduces costs up to 85% [cite:22][cite:25] | Recommend lower-cost/faster surface or async path | Override SLA config |
| `overload_class` | `COMPLEXITY_OVERLOAD` | Task requires multi-step reasoning beyond surface capability; frontier models needed for complex chained tasks [cite:22][cite:28] | Recommend deeper model or specialist-agent handoff | Chain without handoff card |
| `overload_class` | `AUTHORITY_OVERLOAD` | Task requires action outside AIHR advisory boundary (runtime config, provider policy, model registry) [cite:31] | Stop; issue escalation card to owning authority | Proceed with unauthorized action |
| `overload_class` | `FRESHNESS_OVERLOAD` | Claim requires verified current data; KB entry is stale or unverified [cite:39] | Flag `needs_current_verification`; route to research surface | Assert stale claim as current fact |
| `overload_class` | `MCP_PERMISSION_OVERLOAD` | Agent requires MCP tool permissions beyond authorized scope; MCP servers must be treated as untrusted supply-chain until audited [cite:54] | Issue HARD_STOP; escalate to security/governance authority | Silently invoke out-of-scope MCP tool |

### 3.2 recommended_surface

> ⚠️ Specific model names within each surface tier are `needs_current_verification` — model registries change frequently [cite:22][cite:50]. Surface *classes* are STABLE.

| enum_group | value | meaning | allowed_action | forbidden_action |
|---|---|---|---|---|
| `recommended_surface` | `RESEARCH_MODE` | Deep web/doc research; OpenAI Deep Research API (o3-based) supports autonomous multi-step research with `web_search_preview` tool [cite:37][cite:43] | Issue research routing card | Assert findings as ACCEPTED truth without promotion |
| `recommended_surface` | `REPO_EXEC` | Code generation/execution in repo context; use code_interpreter or sandboxed execution surface [cite:37] | Route to repo-execution surface | Bypass QA severity gate |
| `recommended_surface` | `SPECIALIST_AGENT` | Task matches named specialist agent's declared capability; MCP agent-to-agent communication now standard [cite:51][cite:60] | Issue handoff card with capability match field | Claim orchestration authority over specialist |
| `recommended_surface` | `MANUAL_REVIEW` | Task contains ambiguity or risk exceeding automated confidence threshold; HITL mandatory for high-risk actions [cite:52][cite:55] | Issue manual-review escalation card | Suppress escalation to reduce latency |
| `recommended_surface` | `FALLBACK_PATH` | Primary surface unavailable, rate-limited, or confidence below threshold [cite:22] | Route to declared fallback; log reason | Silent reroute without logging |
| `recommended_surface` | `ADVISORY_ONLY` | Task answerable within AIHR scope with no external routing needed | Issue advisory response card | Make runtime changes based on advisory |
| `recommended_surface` | `FAST_TIER` | Simple classification/extraction/formatting; cheap router tier; production routing shows 85% cost reduction routing simple tasks to nano/mini models [cite:22][cite:25][cite:28] | Route to fast-tier model class (`needs_current_verification` for specific model IDs) | Use fast tier for complex multi-step reasoning |
| `recommended_surface` | `THINKING_TIER` | Deep reasoning, math, code; frontier "Thinking" mode models [cite:23][cite:28] | Route with explicit reasoning-mode flag | Use for simple tasks (cost/latency waste) |
| `recommended_surface` | `NEEDS_CURRENT_VERIFICATION` | Surface/model/tool claim is volatile; not freshly verified against primary source | Label entry; defer to verified source | Use as authoritative routing target |

### 3.3 confidence

| enum_group | value | meaning | allowed_action | forbidden_action |
|---|---|---|---|---|
| `confidence` | `HIGH` | Strong evidence from ≥2 independent verified sources; consistent with current primary docs | Use as primary routing basis | Treat as runtime config authority |
| `confidence` | `MEDIUM` | Reasonable evidence; minor gaps or single reputable source | Use with advisory caveat | Omit caveat in routing card |
| `confidence` | `LOW` | Weak or conflicting evidence; single unverified source | Flag; escalate or defer | Route without flag |
| `confidence` | `UNVERIFIED` | Not backed by primary source; model/provider/pricing claims without official confirmation | Mark `needs_current_verification`; do not route on it | Assert as fact |

### 3.4 content_status

| enum_group | value | meaning | allowed_action | forbidden_action |
|---|---|---|---|---|
| `content_status` | `ACCEPTED` | Reviewed and promoted through KB promotion workflow; currently authoritative [cite:31] | Use freely in routing decisions | Modify without promotion workflow |
| `content_status` | `CANDIDATE` | Proposed; not yet reviewed or promoted — the most dangerous accidental-truth risk [cite:42] | Use only as advisory suggestion with explicit flag | Present as ACCEPTED truth |
| `content_status` | `DEPRECATED` | Previously ACCEPTED; superseded by newer evidence or model generation | Reference only to explain history | Use as current routing basis |
| `content_status` | `QUARANTINED` | Flagged for error, policy violation, or adversarial injection risk [cite:47] | Block from routing use; escalate | Silently ignore without escalation |
| `content_status` | `LEARNING_QUEUE` | Future improvement candidate; not yet scoped or resourced | Log for review cycle | Act on as if implemented |

### 3.5 currentness_status

| enum_group | value | meaning | allowed_action | forbidden_action |
|---|---|---|---|---|
| `currentness_status` | `VERIFIED_CURRENT` | Freshly confirmed against primary/official source with dated citation | Cite with source and date | Omit source date |
| `currentness_status` | `NEEDS_CURRENT_VERIFICATION` | Volatile claim (model name, pricing, capability, provider policy) not freshly checked; applies to all model-specific claims [cite:22][cite:50] | Flag inline; block as routing authority | Use as routing fact |
| `currentness_status` | `STABLE` | Claim unlikely to change: boundary doctrine, stop-condition logic, structural schema design | Use without rechecking cadence | Assume all KB entries are STABLE |
| `currentness_status` | `STALE` | Previously verified; TTL elapsed or source materially updated | Trigger re-verification before use | Continue routing on stale claim |

### 3.6 authority_boundary

| enum_group | value | meaning | allowed_action | forbidden_action |
|---|---|---|---|---|
| `authority_boundary` | `ADVISORY` | AIHR owns this domain; output is guidance only | Issue as recommendation | Treat as directive or runtime config |
| `authority_boundary` | `RUNTIME_CONFIG` | Owned by runtime configuration system (e.g., `openclaw.json`) [cite:31] | Reference only; do not mutate | Edit config files directly |
| `authority_boundary` | `PROVIDER_POLICY` | Owned by model provider; changes without notice [cite:33] | Cite policy; route to provider docs | Override or reinterpret provider policy |
| `authority_boundary` | `MODEL_REGISTRY` | Owned by model registry maintainer; model IDs/versions change frequently [cite:50] | Recommend surface class; flag specific models `needs_current_verification` | Hardcode model IDs as routing truth |
| `authority_boundary` | `QA_SEVERITY` | Owned by QA system; AIHR must not self-assign severity | Route to QA surface; do not assign severity | Self-assign QA severity level |
| `authority_boundary` | `ACCEPTED_TRUTH_PROMOTION` | Owned by KB promotion workflow; AIHR output is always CANDIDATE until promoted [cite:31][cite:42] | Propose candidates | Promote own advisory output to ACCEPTED truth |
| `authority_boundary` | `MCP_PERMISSIONS` | Owned by security/governance team; MCP tool scopes defined outside AIHR [cite:54][cite:57] | Reference declared permissions | Expand MCP tool scope unilaterally |

### 3.7 stop_condition_class

| enum_group | value | meaning | allowed_action | forbidden_action |
|---|---|---|---|---|
| `stop_condition_class` | `HARD_STOP` | Routing must halt: authority boundary crossed, critical ambiguity, or irreversible action pending [cite:33][cite:52] | Issue escalation card; await owning authority or human reviewer | Continue routing |
| `stop_condition_class` | `SOFT_STOP` | Routing should pause; confidence too low for safe recommendation — HITL confidence-based routing [cite:58] | Issue advisory-with-flag card; recommend clarification | Suppress flag to maintain velocity |
| `stop_condition_class` | `FRESHNESS_STOP` | Volatile claim encountered; cannot verify currentness [cite:39] | Flag `needs_current_verification`; halt dependent routing | Assert stale claim |
| `stop_condition_class` | `LOOP_STOP` | Routing cycle detected: same state visited ≥2 times [cite:22] | Break cycle; escalate with loop trace | Retry silently |
| `stop_condition_class` | `CAPACITY_STOP` | Surface unavailable, rate-limited, or overloaded [cite:22][cite:25] | Route to fallback; log reason | Drop task without fallback attempt |
| `stop_condition_class` | `PERMISSION_STOP` | MCP or tool scope exceeds authorized permission; treat MCP servers as untrusted supply chain until audited [cite:54] | Issue HARD_STOP; escalate to security authority | Silently invoke out-of-scope capability |
| `stop_condition_class` | `ADVERSARIAL_STOP` | Prompt injection or adversarial routing manipulation detected; R2A-class attacks documented against LLM routers [cite:47] | Quarantine task; escalate to security review | Continue routing with manipulated input |

### 3.8 escalation_tier (HITL)

*Source: production HITL escalation ladder patterns [cite:58][cite:52][cite:55]*

| enum_group | value | meaning | allowed_action | forbidden_action |
|---|---|---|---|---|
| `escalation_tier` | `AUTO` | Passed all automated checks; no human review needed | Proceed with routing | Skip automated checks |
| `escalation_tier` | `TEAM_MEMBER` | Any team member can approve; low-risk ambiguity [cite:58] | Route to general review queue | Escalate directly past team to executive |
| `escalation_tier` | `DOMAIN_EXPERT` | Subject-matter expert required; high-complexity or domain-sensitive decision [cite:58] | Route to named expert role | Use general reviewer for domain-sensitive decisions |
| `escalation_tier` | `EXECUTIVE` | Director/VP sign-off required; irreversible or high-stakes action [cite:52] | Issue formal approval-gate card | Self-approve or silently proceed |

---

## 4. Machine-Readable Tables to Add

| table_name | columns | purpose | risk_if_missing | evidence |
|---|---|---|---|---|
| `route_state_transition_matrix` | `from_state`, `to_state`, `condition`, `stop_condition_class`, `card_required` | Validates state transitions without full KB scan; prevents illegal routing loops; analogous to production LLM routing state machines [cite:22][cite:28] | Agents invent transitions; loops undetected | HIGH |
| `routing_card_field_registry` | `field_name`, `required`, `data_type`, `valid_enum_ref`, `authority_source`, `token_cost_estimate` | Normalizes card structure across all surfaces; enables token-efficient card assembly; mirrors JSON Schema structured output discipline [cite:24][cite:30] | Cards missing required fields; silent handoff failures | HIGH |
| `appendix_surface_directory` | `file_path`, `role`, `schema_type`, `update_cadence`, `write_authority`, `read_consumers`, `content_status` | One-stop lookup for what each appendix contains and who may modify it; prevents agents writing to wrong surface [cite:36][cite:39] | Agents write to read-only appendices or treat reference as mutable truth | HIGH |
| `scaffold_doctype_map` | `file_path`, `doctype`, `key_sections`, `last_verified`, `currentness_status` | Enables retrieval of only relevant scaffold section; reduces prompt token load — documented as critical for agent-readable KB design [cite:2] | Full scaffold injected on every call → token waste | MEDIUM |
| `authority_boundary_fence` | `action_type`, `authority_owner`, `aihr_role`, `stop_condition_if_violated`, `escalation_target` | Explicit machine-readable boundary prevents AIHR from drifting into runtime/config authority; agentic governance frameworks require explicit deny lists [cite:33][cite:31] | Advisory agent executes config mutations silently; governance failure | CRITICAL |
| `candidate_promotion_registry` | `item_id`, `description`, `content_status`, `proposed_by`, `evidence_strength`, `promotion_criteria`, `current_confidence` | Tracks LEARNING_QUEUE items without conflating them with accepted routing rules; separation of candidate/accepted is a documented production risk [cite:42][cite:31] | Candidate rules used as accepted truth; quality degrades over time | HIGH |
| `freshness_manifest` | `claim_id`, `claim_type`, `source_url`, `verified_date`, `currentness_status`, `recheck_cadence` | Systematic staleness detection for volatile model/tool/pricing claims; over 75% of teams use multiple models and model rosters change frequently [cite:22][cite:50] | Stale model claims used in routing; capability mismatch at runtime | HIGH |
| `mcp_tool_registry` | `server_id`, `capability_class`, `transport_type`, `audit_status`, `permission_scope`, `needs_current_verification` | Indexes MCP-exposed surfaces AIHR may route to (advisory); MCP is now de facto standard for agent-tool integration [cite:51][cite:54][cite:57][cite:60] | AIHR recommends out-of-scope MCP tools; permission boundary violated | HIGH |
| `recommended_surface_capability_map` | `surface_id`, `surface_type`, `task_class_match`, `cost_tier`, `latency_class`, `currentness_status` | Routes tasks to correct surface class; production routing achieves 85% cost reduction via task-class matching [cite:22][cite:25][cite:28] | Over-routing to expensive surfaces; token/cost waste | HIGH (freshness HIGH — model tiers change) |
| `hitl_escalation_decision_table` | `trigger_condition`, `confidence_threshold`, `escalation_tier`, `card_type`, `timeout_action` | Maps confidence scores and risk signals to HITL tiers; confidence-based routing is a documented HITL pattern [cite:58][cite:55][cite:52] | High-risk actions auto-approved without human review; governance failure | CRITICAL |
| `adversarial_routing_risk_register` | `attack_class`, `description`, `detection_signal`, `stop_condition_class`, `mitigation_note` | Documents known adversarial routing attacks (e.g., R2A suffix manipulation to route to expensive models [cite:47]); enables detection flags in routing cards | Adversarial routing manipulation undetected | MEDIUM (novel risk class) |

---

## 5. Sidecar Policy

### What Should Remain Markdown Authority

All enums, route states, stop conditions, authority boundary definitions, routing card field registries, escalation tier definitions, and the candidate/accepted lifecycle must remain **Markdown-first**. Markdown is human-reviewable, diff-trackable in version control, and fully readable by both humans and agents without tooling dependencies. Production KB design confirms that structured Markdown tables are the optimal format for agent context injection because they are token-efficient and parseable without preprocessing [cite:2][cite:36]. Any sidecar that diverges silently from the Markdown source creates split-truth, which is the primary structural failure mode in multi-agent KB systems [cite:42][cite:31].

### When YAML/JSON Sidecars Become Useful

Sidecars are useful only after the Markdown index is stable, validated, and confirmed ACCEPTED through the KB promotion workflow. Specific trigger conditions:

1. **CI validation pipelines**: A generated `index.json` enables schema validation scripts to check routing card outputs against the registry without parsing Markdown at runtime.
2. **Structured output schemas for agent tool calls**: When routing cards are consumed as `response_format` JSON Schema parameters in OpenAI Structured Outputs API calls, a generated schema file accelerates reliable JSON mode compliance [cite:21][cite:24][cite:30].
3. **Freshness-check automation**: A generated `freshness_manifest.json` enables scheduled re-verification runners to check TTLs and flag stale model/pricing claims programmatically [cite:39].
4. **Multi-agent handoff contracts**: As MCP agent-to-agent communication matures, generated JSON schemas for routing cards become a natural handoff contract format [cite:51][cite:60].

The trigger for generating a sidecar should always be a *repeated agent parsing failure on the Markdown tables* or a *documented CI/tooling requirement* — never mere convenience.

### Why Sidecars Must Be Generated/Derivative

Sidecars must be *generated from* the Markdown authority, never hand-authored independently. Any independently authored YAML/JSON sidecar immediately creates a second source of truth capable of silent drift. Generation should be a build step (e.g., a script that emits `index.json` from Markdown table rows), and the output should be a tracked build artifact — readable but not hand-editable [cite:42]. This mirrors the schema-driven design pattern validated in production agentic infrastructure: define structure once in a human-readable location, derive all machine-readable formats from that single source [cite:12][cite:24].

### What Must Prevent Sidecars from Becoming Conflicting Truth

- The index file must carry a machine-readable header comment: `<!-- MACHINE INDEX: read-only reference. Source of truth = listed authority files. Sidecars are generated artifacts. -->`
- Every sidecar must embed a `generated_from` field pointing to the Markdown source file path and a `generation_timestamp` ISO-8601 field.
- CI must reject pull requests that edit sidecar files directly without a corresponding Markdown change in the authority file.
- Any agent reading a sidecar must treat its contents as `content_status: CANDIDATE` unless the Markdown authority file confirms the value as `ACCEPTED`.
- Sidecar schema version must be pinned to the Markdown source commit hash; version mismatch triggers `FRESHNESS_STOP`.

---

## 6. Non-Goals for This Index File

The following must **not** appear in `appendices/APPENDIX_KB_MACHINE_READABLE_INDEX.md`:

- **Runtime configuration values**: No model IDs, API keys, provider endpoints, `openclaw.json` fields, or deployment configuration. These are owned by the runtime config system [cite:31].
- **Accepted-truth promotion**: The index lists and describes; it does not promote. Promotion is a separate workflow with its own authority [cite:42].
- **Hardcoded specific model names or pricing**: Any model capability or cost claim must be `needs_current_verification`; the index references the `freshness_manifest`, it does not assert current values [cite:22][cite:50].
- **Prompt templates or routing cookbook content**: These belong in `TEMPLATES.md` and routing-card appendices; the index only points to them.
- **Orchestration logic or agent control flow**: The index is a lookup surface, not a decision engine. It must not contain `if/then` routing rules or conditional execution logic.
- **QA severity assignments**: QA severity is owned by the QA system. The index may reference the authority boundary; it must not assign severity levels.
- **Hand-authored YAML/JSON sidecars**: Per sidecar policy, no manually authored structured data should live in or be generated by this index.
- **Narrative justification or prose reasoning**: Descriptions should be ≤1 sentence per field. Extended justification belongs in scaffold files. Token efficiency is a design constraint.
- **Speculative future routing surfaces**: Surfaces with `LEARNING_QUEUE` status must not appear in main index tables; they belong only in `candidate_promotion_registry`.
- **Adversarial attack methodology**: The adversarial routing risk register stores *detection signals and stop conditions only* — it does not document attack construction methods [cite:47].
- **Provider-specific policy text**: Policy citations belong in the authority boundary fence with a pointer to the provider source; policy text must not be reproduced inline.

---

## 7. Web-Research-Validated Context Notes

The following findings from current primary/reputable sources should inform KB integration decisions:

### 7.1 LLM Routing Infrastructure (2025–2026)

Production LLM routing is now a standard infrastructure pattern. Over 75% of enterprise teams use multiple models in production as of 2026, and intelligent routing achieves up to 85% cost reduction while maintaining 95% of frontier model quality [cite:22][cite:25]. Routing decisions are made on task complexity, latency budget, cost tier, and quality threshold. The AIHR index must normalize these dimensions as routing card fields.

The leading open routing framework **RouteLLM** (lm-sys) demonstrates that cost-quality Pareto optimization is achievable and measurable; its benchmarks confirm no single router dominates all metrics — router selection involves trade-offs [cite:50][cite:56]. This validates the KB's need for a `recommended_surface_capability_map` that is honest about trade-offs rather than asserting a single "best" route.

### 7.2 GPT-5 / Frontier Model Architecture (needs_current_verification for specific capabilities)

GPT-5 (released August 2025, broadly available by early 2026) introduced hierarchical internal routing — a "Fast" sub-model for routine tasks and a "Thinking" mode for complex reasoning [cite:20][cite:23]. This makes the surface-class distinction between `FAST_TIER` and `THINKING_TIER` structurally correct at the routing card level, even as specific model IDs and versions remain `needs_current_verification`. OpenAI's Deep Research API (June 2025) exposed autonomous multi-step research as a routable surface (`o3-deep-research` with `web_search_preview` tool) [cite:37][cite:43].

### 7.3 Structured Outputs as Routing Card Standard

OpenAI Structured Outputs (August 2024, now stable in all `gpt-4o-2024-08-06` and later models) guarantees JSON Schema compliance for model outputs [cite:21][cite:30]. Routing cards designed as JSON Schemas with `required` fields and `enum` constraints benefit directly from this: the routing card field registry in the index should be designed with downstream Structured Outputs consumption in mind. Schema design guidance: schemas too loose allow inconsistent responses; schemas too restrictive cause model failure — specify exactly what downstream processing requires [cite:24].

### 7.4 MCP as De Facto Agent-Tool Protocol

The Model Context Protocol (originally Anthropic, now donated to the Agentic AI Foundation) is the de facto standard for agent-tool integration across all major frameworks [cite:51][cite:60]. MCP servers expose capabilities via JSON-RPC 2.0 over stdio or HTTP; agents read capability manifests without hardcoded routing [cite:54]. The 2026 MCP roadmap extends to agent-to-agent communication [cite:51]. The AIHR index must include a `mcp_tool_registry` that flags all MCP surfaces as `needs_current_verification` (server capabilities change) and treats unaudited MCP servers as untrusted supply-chain [cite:54].

### 7.5 Agentic Safety, HITL, and Stop Conditions

Australian Cyber Security Centre (April 2026) guidance for agentic AI adoption explicitly requires: explicit stop conditions, fail-safe defaults, containment mechanisms, declarative safety contracts with guardrails agents cannot override, and human control points throughout agent workflows [cite:33]. HITL confidence-based routing is a documented production pattern with five core variants covering 90%+ of real-world use cases [cite:58]. The escalation ladder pattern (Auto → Team Member → Domain Expert → Executive) with confidence thresholds is the production standard [cite:58][cite:52][cite:55]. Agentic AI governance must operate at runtime, not as periodic review [cite:31].

### 7.6 Adversarial Routing Risk

R2A (Route to Rome Attack) is a documented adversarial technique that manipulates LLM routers via adversarial suffix optimization to force routing to expensive models [cite:47]. This is an active research concern as of 2025. The AIHR index should include an `adversarial_routing_risk_register` with detection signals and `ADVERSARIAL_STOP` as a stop condition class. This is a novel risk class with MEDIUM evidence strength (single academic source) — marked accordingly in the integration matrix.

---

## 8. Ranked Content to Integrate

> Sorting: **Evidence + Impact + Risk-if-missing** combined score, penalizing stale/weakly verified claims.  
> All model-name and pricing-specific claims are `needs_current_verification`. Schema/structural claims are `STABLE`.

| rank | content_to_integrate | target_file | target_section | evidence_score_1_100 | impact_score_1_100 | risk_if_missing_1_100 | freshness_sensitivity | validation_sources | verification_status | integration_priority | notes |
|---:|---|---|---|---:|---:|---:|---|---|---|---|---|
| 1 | **Authority boundary fence table** (AIHR may-not-do quick-reference with owning authority and stop condition per action) | `APPENDIX_KB_MACHINE_READABLE_INDEX.md` | `authority_boundary_fence` table | 95 | 98 | 99 | LOW (doctrine is STABLE) | [cite:31][cite:33][cite:52] | `triple_verified_current` | P0-CRITICAL | Missing = advisory agent executes runtime mutations silently; agentic governance frameworks universally require explicit deny lists |
| 2 | **stop_condition_class enum** with HARD_STOP, SOFT_STOP, FRESHNESS_STOP, LOOP_STOP, CAPACITY_STOP, PERMISSION_STOP, ADVERSARIAL_STOP | `APPENDIX_KB_MACHINE_READABLE_INDEX.md` | Section 3.7 | 92 | 97 | 98 | LOW (classes STABLE; ADVERSARIAL_STOP MEDIUM evidence) | [cite:33][cite:47][cite:52][cite:55][cite:58] | `triple_verified_current` (except ADVERSARIAL_STOP: `single_verified_current`) | P0-CRITICAL | Without normalized stop classes, agents cannot enumerate when to halt; governance failure |
| 3 | **HITL escalation tier map** (Auto → Team Member → Domain Expert → Executive) with confidence thresholds | `APPENDIX_KB_MACHINE_READABLE_INDEX.md` + `BEST_PRACTICES.md` | `hitl_escalation_decision_table` | 90 | 95 | 96 | LOW (tiers STABLE) | [cite:52][cite:55][cite:58] | `triple_verified_current` | P0-CRITICAL | Production HITL pattern covering 90%+ of real-world use cases; absence = high-risk actions auto-approved |
| 4 | **content_status enum** (ACCEPTED / CANDIDATE / DEPRECATED / QUARANTINED / LEARNING_QUEUE) with explicit separation of CANDIDATE from ACCEPTED | `APPENDIX_KB_MACHINE_READABLE_INDEX.md` | Section 3.4 | 92 | 95 | 97 | LOW (lifecycle STABLE) | [cite:31][cite:42][cite:33] | `triple_verified_current` | P0-CRITICAL | Primary failure mode: CANDIDATE content used as ACCEPTED truth; must be in index |
| 5 | **candidate_promotion_registry table** tracking LEARNING_QUEUE items separately from routing rules | `APPENDIX_KB_MACHINE_READABLE_INDEX.md` | `candidate_promotion_registry` | 90 | 93 | 95 | LOW (STABLE) | [cite:31][cite:42] | `double_verified_current` | P0-CRITICAL | Without this registry, candidates silently graduate to routing authority |
| 6 | **routing_card_field_registry** with required/optional fields, data types, enum refs, authority source — aligned to OpenAI Structured Outputs JSON Schema discipline | `APPENDIX_KB_MACHINE_READABLE_INDEX.md` | `routing_card_fields` | 93 | 94 | 93 | LOW (structure STABLE; specific model params MEDIUM) | [cite:21][cite:24][cite:30] | `triple_verified_current` | P1-HIGH | Structured Outputs guarantees schema compliance for routing card generation; normalizing fields enables downstream machine validation |
| 7 | **Sidecar-as-generated-artifact policy** (Markdown authority first; sidecars generated from Markdown, never hand-authored; CI rejects direct sidecar edits) | `APPENDIX_KB_MACHINE_READABLE_INDEX.md` | Section 5 | 88 | 92 | 91 | LOW (architectural doctrine STABLE) | [cite:12][cite:24][cite:42] | `double_verified_current` | P1-HIGH | Prevents split-truth between Markdown and YAML/JSON; documented failure mode in schema-driven KB design |
| 8 | **currentness_status enum** with VERIFIED_CURRENT / NEEDS_CURRENT_VERIFICATION / STABLE / STALE — mandatory for all model/tool/pricing claims | `APPENDIX_KB_MACHINE_READABLE_INDEX.md` + `ESSENCE.md` | Section 3.5 | 90 | 90 | 92 | HIGH (by definition — freshness tracking is for volatile claims) | [cite:22][cite:39][cite:50] | `triple_verified_current` | P1-HIGH | 75%+ of teams use multiple models; model rosters change; stale routing claims cause runtime capability mismatch |
| 9 | **freshness_manifest table** with claim_id, claim_type, source_url, verified_date, currentness_status, recheck_cadence | `APPENDIX_KB_MACHINE_READABLE_INDEX.md` | `freshness_manifest` | 88 | 90 | 91 | HIGH (this table tracks the volatile claims) | [cite:22][cite:39][cite:50] | `double_verified_current` | P1-HIGH | Enables systematic staleness detection; without it, stale model claims propagate silently |
| 10 | **recommended_surface enum** with FAST_TIER / THINKING_TIER / RESEARCH_MODE / REPO_EXEC / SPECIALIST_AGENT / MANUAL_REVIEW / FALLBACK_PATH (specific model IDs `needs_current_verification`) | `APPENDIX_KB_MACHINE_READABLE_INDEX.md` + `BEST_PRACTICES.md` | Section 3.2 | 88 | 92 | 88 | HIGH (surface classes STABLE; model IDs volatile) | [cite:22][cite:25][cite:28][cite:43] | `double_verified_current` (surface classes); `needs_current_verification` (model IDs) | P1-HIGH | Production routing shows 85% cost reduction from correct surface-class matching; must be in index as advisory basis |
| 11 | **MCP tool registry** — MCP now de facto agent-tool standard; treat unaudited MCP servers as untrusted supply chain; JSON-RPC 2.0 transport | `APPENDIX_KB_MACHINE_READABLE_INDEX.md` + `BEST_PRACTICES.md` | `mcp_tool_registry` | 87 | 88 | 85 | HIGH (MCP roadmap evolving rapidly in 2026) | [cite:51][cite:54][cite:57][cite:60] | `triple_verified_current` (protocol status); `needs_current_verification` (specific server capabilities) | P1-HIGH | MCP is now the routing layer for agent-to-tool and agent-to-agent; ignoring it creates a structural gap in surface coverage |
| 12 | **route_state_transition_matrix** with from_state, to_state, condition, stop_condition_class, card_required | `APPENDIX_KB_MACHINE_READABLE_INDEX.md` | `route_state_transition_matrix` | 85 | 90 | 88 | LOW (structural schema STABLE) | [cite:22][cite:28] | `double_verified_current` | P1-HIGH | Without explicit transitions, agents invent paths; routing loops undetected |
| 13 | **FAST_TIER / THINKING_TIER routing classification** — GPT-5 internal hierarchical router (Fast vs Thinking sub-models); task complexity classifier as routing input | `BEST_PRACTICES.md` | routing surface selection guidance | 82 | 88 | 80 | HIGH (model-specific; GPT-5 specific details `needs_current_verification`) | [cite:20][cite:23][cite:28] | `double_verified_current` (architecture class); `needs_current_verification` (specific model names/costs) | P1-HIGH | Core surface selection pattern for 2026 era; wrong tier = cost waste or quality failure |
| 14 | **OpenAI Deep Research API as RESEARCH_MODE surface** — `o3-deep-research` with `web_search_preview` tool; autonomous multi-step research since June 2025 | `BEST_PRACTICES.md` | RESEARCH_MODE surface card | 85 | 82 | 75 | HIGH (API details volatile) | [cite:37][cite:40][cite:43] | `double_verified_current` | P2-MEDIUM | Validates RESEARCH_MODE as a real routable surface with API primitives; specific params `needs_current_verification` |
| 15 | **authority_overload_class: MCP_PERMISSION_OVERLOAD** — new stop condition for MCP tool scope violation | `APPENDIX_KB_MACHINE_READABLE_INDEX.md` | Section 3.1 | 85 | 82 | 85 | MEDIUM (MCP permission model evolving) | [cite:54][cite:57][cite:33] | `double_verified_current` | P2-MEDIUM | MCP permission violations are a documented agentic security risk class; must be a HARD_STOP trigger |
| 16 | **scaffold_doctype_map** with key_sections and currentness_status per scaffold file | `APPENDIX_KB_MACHINE_READABLE_INDEX.md` | `scaffold_surface_map` | 82 | 80 | 75 | LOW (structure STABLE) | [cite:2][cite:36] | `double_verified_current` | P2-MEDIUM | Enables token-efficient retrieval of only the relevant scaffold section; reduces prompt bloat |
| 17 | **appendix_surface_directory** with write authority and read consumers per appendix file | `APPENDIX_KB_MACHINE_READABLE_INDEX.md` | `appendix_surface_map` | 80 | 82 | 78 | LOW (STABLE) | [cite:36][cite:39] | `double_verified_current` | P2-MEDIUM | Prevents agents writing to read-only surfaces or treating evidence appendices as authoritative |
| 18 | **RouteLLM / RouterEval benchmark findings** — no single router dominates all metrics; cost-quality trade-off is real; router selection requires explicit criteria | `APPENDIX_KB_MACHINE_READABLE_INDEX.md` (freshness_manifest) + `BEST_PRACTICES.md` | routing surface selection evidence | 80 | 78 | 72 | HIGH (benchmark results update) | [cite:50][cite:53][cite:56] | `double_verified_current` | P2-MEDIUM | Validates that AIHR should recommend surface class, not a single model; prevents false confidence in a "best route" |
| 19 | **Adversarial routing risk (R2A attack class)** — adversarial suffix manipulation forces expensive model routing; detection signal and ADVERSARIAL_STOP condition | `APPENDIX_KB_MACHINE_READABLE_INDEX.md` | `adversarial_routing_risk_register` | 72 | 75 | 78 | MEDIUM (active research area) | [cite:47] | `single_verified_current` | P2-MEDIUM | Novel documented risk class; single academic source; warrants CANDIDATE entry with MEDIUM evidence flag |
| 20 | **Agentic AI governance runtime posture** — governance must operate at runtime, not periodic review; 40% of enterprise apps embedding agents by end of 2026 | `ESSENCE.md` | advisory boundary doctrine | 88 | 85 | 80 | MEDIUM (Gartner projection) | [cite:31][cite:32] | `double_verified_current` | P2-MEDIUM | Validates why AIHR advisory boundary + HARD_STOP / escalation architecture is necessary at current scale |
| 21 | **confidence enum** (HIGH / MEDIUM / LOW / UNVERIFIED) with explicit UNVERIFIED blocking routing | `APPENDIX_KB_MACHINE_READABLE_INDEX.md` | Section 3.3 | 85 | 85 | 82 | LOW (STABLE) | [cite:22][cite:58] | `double_verified_current` | P1-HIGH | Confidence thresholds drive HITL escalation decisions; without normalized enum, confidence-based routing is inconsistent |
| 22 | **overload_class enum** (TOKEN / LATENCY / COMPLEXITY / AUTHORITY / FRESHNESS / MCP_PERMISSION) | `APPENDIX_KB_MACHINE_READABLE_INDEX.md` | Section 3.1 | 84 | 83 | 84 | LOW (STABLE) | [cite:22][cite:25][cite:33][cite:54] | `triple_verified_current` | P1-HIGH | Core classification for routing failure modes; must be normalized for agent fast-lookup |

---

## 9. Items Rejected or Downgraded

| item | rejection_reason | verification_status |
|---|---|---|
| Specific model pricing figures (per-token costs for any provider) | Pricing changes without notice; no freshly verified official pricing page confirmed in this research cycle | `reject_stale_or_unverified` |
| GPT-5.5 as a specific named model with specific benchmark scores | "GPT-5.5" not confirmed in official OpenAI sources as a distinct named release; seohq.github.io source is not an official primary source [cite:19] | `needs_current_verification` |
| Specific RouteLLM/NotDiamond accuracy percentages as routing truth | Benchmark scores are point-in-time; RouterEval shows rankings shift as model pools update [cite:50]; AIHR should reference benchmark methodology, not hardcode scores | `needs_current_verification` |
| Hand-authored YAML/JSON sidecar schemas | No current source validates hand-authored sidecars; schema-driven design requires generation from Markdown authority [cite:12][cite:24] | `reject_stale_or_unverified` |
| GraphRAG / vector DB specifics as routing surfaces | Out of scope for AIHR advisory routing index; belongs in data-retrieval architecture KB not routing-card registry | Out of scope |

