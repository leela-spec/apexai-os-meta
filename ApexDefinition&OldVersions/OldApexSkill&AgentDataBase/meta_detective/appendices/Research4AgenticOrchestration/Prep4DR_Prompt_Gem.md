## Step 1 — Understanding lock before writing the Gemini prompt

### My locked interpretation

You want **a Gemini Deep Research / Deep Research Max prompt**, not the final research output yet.

That prompt must force Gemini to research the studies listed in `studyplan.txt` and produce a **machine-readable failure-mode ledger** that can later feed **two operational agents**, especially a **Meta Detective / validation agent** and a second agent that likely uses the results for orchestration/control design.

The uploaded `studyplan.txt` already defines the correct direction: the KB must be usable, machine-readable, token-efficient, non-drift, non-ambiguous, and must map each source insight into **failure → control → verification check → implementation status**, not into prose summaries.

---

## Current Gemini / Deep Research state to design against

|Item|Current finding|Prompt-design consequence|
|---|---|---|
|**Latest Gemini family**|Google’s current model page lists **Gemini 3.1 Pro Preview** under Gemini 3, while Gemini 2.5 Pro remains available as the advanced 2.5 model for complex reasoning/coding.|Design the prompt for **Deep Research Max / Gemini 3.1-era behavior**, not older Gemini 1.5/2.0 assumptions.|
|**Deep Research agent**|Gemini Deep Research Agent “autonomously plans, executes, and synthesizes multi-step research tasks,” producing cited reports; it is preview-only through the **Interactions API**, not `generate_content`.|The prompt must include a **plan-review stage** and should assume a multi-step research agent, not a single answer model.|
|**Deep Research versions**|Google docs list `deep-research-preview-04-2026` for speed and `deep-research-max-preview-04-2026` for maximum comprehensiveness.|Use **Deep Research Max** for this task because failure-mode extraction across many studies needs exhaustiveness over speed.|
|**Collaborative planning**|Deep Research can return a proposed plan first; the user can refine or approve it before execution.|The prompt should force Gemini to output a **research plan first**, then wait for approval before full research.|
|**Tools**|Deep Research has Google Search, URL Context, and Code Execution by default; it can also use File Search and MCP tools.|Prompt must explicitly restrict sources/tools and define source classes to prevent uncontrolled web drift.|
|**MCP risk**|Deep Research supports MCP servers, including restricting allowed tools.|For this project, MCP should be **disabled unless explicitly needed** or treated as security-review only.|
|**Structured outputs**|Gemini structured outputs support JSON Schema and are recommended for predictable, parsable output; Google notes schema-conformant output still needs semantic validation.|Final Gemini output must be **schema-like YAML/JSON**, but the prompt must still require semantic validation fields.|
|**Long context**|Gemini models support very large context windows and Google says providing all relevant information upfront is viable, but long context still has limitations with multiple retrieval targets.|Put **task lock + schemas + output contract at the front and again at gates**, not buried in the middle.|
|**Grounding**|Google Search grounding is designed for real-time information, citations, and reduced hallucination.|Prompt must require **citation per claim** and reject uncited claims.|

---

## Decision Q&A — lock these before prompt construction

### A1. What exactly should Gemini produce?

**Answer:** A **failure-mode ledger**, not a report.

**Recommendation:** The final output should be a set of machine-readable records:

```
failure_mode_record:  failure_id:  label:  cluster:  description:  source_evidence:  severity_score_1_100:  frequency_signal_1_100:  evidence_strength_1_100:  implementation_risk_1_100:  control_candidates:  verification_checks:  agent_mapping:  status:
```

**Why:** The studyplan explicitly rejects a “download studies → summarize them → ask Detective to remember them” flow and requires a controlled evidence system.

---

### A2. Should Gemini rank studies or rank failure modes?

**Answer:** Rank **failure modes**, while preserving study provenance.

**Recommendation:** Use studies as evidence sources, not as the final organizing principle.

```
ranking_target: failure_modesnot: studiessource_role:  studies: evidence_inputs  ledger: operational_output
```

**Why:** The final goal is agent design. Agents need controls and checks, not literature summaries.

---

### A3. Which Gemini mode should be assumed?

**Answer:** Use **Gemini Deep Research Max**, if available.

**Recommendation:**

```
preferred_agent: deep-research-max-preview-04-2026fallback_agent: deep-research-preview-04-2026reason:  - maximum comprehensiveness  - many-source synthesis  - failure taxonomy extraction  - source conflict handling
```

Deep Research Max is explicitly described by Google as the comprehensive version for automated context gathering and synthesis.

---

### A4. Should the Gemini prompt allow a normal prose report?

**Answer:** No.

**Recommendation:** Allow only two prose zones:

```
allowed_prose:  - plan_rationale_before_execution  - short_uncertainty_notes_inside_recordsforbidden:  - narrative report  - essay  - broad theory overview  - uncited synthesis paragraphs
```

**Why:** The user’s downstream use is agent creation. Prose is high-drift and low-operational.

---

### A5. Should every study receive equal treatment?

**Answer:** No.

**Recommendation:** Use tiered extraction:

```
tier_1_full_extraction:  - MAST  - GitHub multi-agent workflows  - Structured Outputs  - Guardrails  - Handoffs  - Lost in the Middle  - COSMIR  - OWASP Agentic / GenAItier_2_targeted_extraction:  - LangGraph  - MCP  - Chain-of-Agents  - CoALA  - NIST AI RMF  - OpenTelemetry / tracing  - MetaGPT  - AutoGen
```

This matches the uploaded studyplan’s priority order and extraction depth policy.

---

### A6. How should Gemini prevent source drift?

**Answer:** Force a **source manifest first**, extraction second, synthesis third.

**Recommendation:** The Gemini prompt should require this sequence:

```
required_sequence:  1_source_access_manifest  2_study_cards  3_claim_extraction_records  4_failure_mode_matrix  5_control_candidate_matrix  6_agent_input_schema  7_unresolved_questions
```

**Guardrail:** No failure mode may enter the ranking unless it has at least one cited source and extraction record.

---

### A7. What is the smallest valid knowledge unit?

**Answer:** A **claim mapped to failure/control/check**.

**Recommendation:**

```
minimum_valid_unit:  claim:  source:  failure_mode:  control:  verification_check:  adoption_status:
```

This is directly aligned with the studyplan: “A claim mapped to a failure/control/check. Not a paragraph summary.”

---

### A8. How should the ranking be calculated?

**Answer:** Use a transparent scoring model, not Gemini’s vague judgment.

**Recommendation:**

```
ranking_formula:  total_priority_score:    severity: 0.30    frequency: 0.20    evidence_strength: 0.20    agentic_relevance: 0.15    headless_cloud_relevance: 0.10    control_feasibility: 0.05
```

**Important:** `control_feasibility` should be positive only when the control is implementable without causing new system drift.

---

### A9. Which failure clusters should be pre-seeded?

**Answer:** Pre-seed the clusters from the studyplan, but let Gemini add new ones only if evidence-backed.

**Recommendation:**

```
seed_failure_clusters:  - specification_failure  - inter_agent_misalignment  - verification_failure  - untyped_boundary  - context_degradation  - security_tool_risk  - runtime_state_loss  - observability_failure  - autonomous_loop_runaway  - source_authority_drift
```

The studyplan already contains a strong matrix mapping specification failure, inter-agent misalignment, verification failure, untyped boundaries, context degradation, security/tool risk, runtime state loss, and observability failure to controls.

---

### A10. How should the output support two agents?

**Answer:** Each record must map to **agent-usable roles**, not only abstract controls.

**Recommendation:**

```
agent_mapping:  meta_detective:    uses_for:      - failure_classification      - evidence_check      - contradiction_detection      - escalation  orchestration_or_meta_ops_agent:    uses_for:      - control_selection      - handoff_design      - runtime_gate_design      - state_checkpoint_design
```

**Interpretation:** The Detective agent should validate and classify. The orchestration/control agent should implement safe process architecture. The Detective should not implement fixes.

---

### A11. Should Gemini be allowed to infer implementation doctrine from vendor docs?

**Answer:** No.

**Recommendation:**

```
vendor_doc_policy:  allowed:    - mechanism_extraction    - terminology_extraction    - implementation_candidate  forbidden:    - treating_vendor_doc_as_universal_truth    - promoting_vendor_pattern_to_runtime_doctrine_without_gate
```

This matches the studyplan’s instruction that vendor docs can define mechanisms but should be supporting/candidate unless explicitly adopted.

---

### A12. How should Deep Research’s collaborative plan be controlled?

**Answer:** The first Gemini run should produce only a **research execution plan**.

**Recommendation:** The final prompt should say:

```
phase_0_behavior:  produce_only:    - source_plan    - extraction_plan    - output_schema_plan    - risk_controls    - missing_decisions  do_not:    - perform_full_research    - produce_final_ledger
```

Google’s Deep Research docs explicitly support collaborative planning before execution, where the agent returns a proposed research plan and can be refined before approval.

---

## Locked design decisions I recommend

|Decision|Lock|
|---|---|
|Output target|**Failure-mode ledger**, not report|
|Gemini mode|**Deep Research Max** preferred|
|First run|**Planning only**, no final research|
|Main format|YAML/JSON-like machine-readable records|
|Source handling|Source manifest mandatory|
|Claim rule|No claim without source status|
|Extraction unit|Claim → failure → control → check|
|Ranking unit|Failure modes|
|Ranking method|Weighted operational score|
|Agent target|Detective validation + orchestration/control agent|
|Vendor docs|Supporting/candidate, not doctrine|
|Headless cloud|Dedicated risk dimension|
|Final prompt style|Front-loaded task lock, schema-first, examples, forbidden outputs|

---

## What I will build in Step 2

The next output should be a **copy-paste-ready Gemini Deep Research Max prompt** with these chapters:

```
prompt_chapters:  0_model_and_execution_mode:  1_task_lock:  2_non_goals:  3_source_scope:  4_research_plan_requirements:  5_source_manifest_schema:  6_study_card_schema:  7_claim_extraction_schema:  8_failure_mode_record_schema:  9_ranking_formula:  10_control_candidate_schema:  11_verification_check_schema:  12_agent_mapping_schema:  13_headless_cloud_risk_schema:  14_output_order:  15_quality_gates:  16_forbidden_outputs:  17_few_shot_examples:  18_phase_0_planning_only_instruction:  19_phase_1_execution_instruction_after_approval:
```

My recommendation: **lock the decisions above as-is** and proceed to Step 2.

One, no, it should not only produce a failure mode ledger, but also a best practice ledger. The reason why we're doing this prompt flow is because we need to... So the reasoning behind it, but don't cause drift with this explanation. The reason why we need it is because we are going to build, later on, a new version of the knowledge base of two agents that are part of an agentic AI orchestration system. But it would be very stupid to build these agents without understanding what is actually going wrong in agentic AI orchestration. So the deep research prompt who's going to do that needs to already know best practice, failure modes, rules, design systems, correlations, how agents work together, because otherwise, the way that this knowledge base and agent is going to be built is going to be completely wrong. So we need something as a guidance for failures, for best practice, and stuff like that. This is the reason why we do that. Yes, A2, everything should be ranked. The most important rules, best practices, ideas, concepts, correlations, formats, whatever there is, it needs to be ranked so that the executing agent has an understanding on what is more important and what is not as important. Yes, A3, Gemini deep research max. Even though I don't really know what that max is. maybe give me a short representation from where this is coming from or how I can select that. A4, no, this is going to be only machine-readable, highly information-dense, token-efficient style. And by the way, what I see with the recommendation that you put in A1, these are an extreme amount of variables. This is going to complicate a lot of things. Be as simple as possible and token-efficient. So rethink if this is really necessary. A5, the tiers are accepted. A6, yes, source drift is important. A7, I do not understand that. So again, what you're doing here, right, might be logical, but it's going to be impossible for the agent to give for every idea all these variables. This is going to explode the deep research plan. What we need is an extraction of failures, of guardrails, of best practice, of inter-agent communication formats, and all that stuff. This is the most important thing. this, I guess we need to map and pre-check the studies for their specific information. And for each of those, we need to create one chapter in the final report that is going to be handed out. So we need to do a test run before we design the prompt with everything that you're presenting here, because as of now, everything that you put in here looks way over-engineered. This is one very strong failure mode when I ask you to do complex things. And also, what we need to do is only work in the output. Another failure mode of the research prompts is that it has a shit ton of theoretical background and it's not actually working on the output. We need to work on the output. We need to extract guardrails, big practices, failures, and stuff like that to give a guidance to the deep research prompt that is going to use that as a reminder on how to build a knowledge-based system that is actually agent orchestration doable and not some theory or some drift or some theoretically nice ideas that at the end don't work. LA11, I don't understand, so choose what is recommended. So A12, it's just, we are going to define what it's going to do and we are going to do a pre-run so that we are actually aligning it here. Yeah, work in these decisions and let's create a, through web search, a basically an already defined structure of the final output that we want from Gemini with everything that we can extract and is necessary. You will give me the options on what information are going to be extracted, so again, failure modes, best practice, intercorrelation, stuff like that, and all the variables, but all of that, do it as a short list, which is like for sure necessary, a long list, which would be nice but optional, and then a residual tier that is something for me to check, something that you might think is important, so I can check if that is actually included or not. Create that output now.

Thought for 34s

You are right. My previous schema was too heavy. We should **not** make Gemini fill 15 variables for every idea. The final Deep Research output should be a **ranked operational extraction pack**, not a complex evidence database disguised as research.

The corrected target is:

```
target_output:  purpose: "ranked operational guidance for rebuilding two agent KBs"  output_style: "machine_readable, dense, token_efficient"  primary_ledgers:    - failure_modes    - best_practices    - guardrails    - inter_agent_formats    - design_rules    - correlations  forbidden:    - theory_report    - literature_review    - long explanations    - uncited advice    - over-nested schemas
```

The uploaded `studyplan.txt` already supports this correction: it says the KB must not become a study dump, must preserve provenance, and must map research into usable controls/checks for OpenClaw agents.

---

# 1. Gemini Deep Research Max — what it is and how to select it

**Deep Research Max** is Google’s more comprehensive Deep Research agent configuration, announced April 21, 2026. Google says the new Deep Research agents are built with Gemini 3.1 Pro, support collaborative planning, MCP, URL context, code execution, file search, and native visualizations. Google describes **Deep Research Max** as the choice for highest-quality context gathering and analysis, while standard Deep Research is for speed/efficiency.

For API use, the current model/config ID shown in current docs/ecosystem references is:

```
gemini_deep_research:  preferred_agent: "deep-research-max-preview-04-2026"  fallback_agent: "deep-research-preview-04-2026"  access_mode: "Gemini API Interactions API"  not_generate_content: true
```

Google’s Deep Research docs state that the Deep Research Agent is available through the **Interactions API**, not the normal `generate_content` path, and that it plans, searches, reads, and writes as a multi-step background research process.

**Practical selection:** In AI Studio/API UI, select the Deep Research agent/config if exposed. In API form, use the Interactions API agent name. If the UI only gives “Deep Research” and “Deep Research Max,” choose **Max** for this task because you need exhaustive extraction and ranking, not speed.

---

# 2. Corrected output philosophy

## What Gemini should actually produce

Not:

```
wrong_output:  - research_report  - study_summaries  - theory_overview  - giant_per_claim_schema
```

But:

```
correct_output:  - ranked_failure_mode_ledger  - ranked_best_practice_ledger  - ranked_guardrail_ledger  - ranked_inter_agent_format_ledger  - ranked_design_rule_ledger  - ranked_correlation_ledger  - compact_source_index  - agent_kb_build_guidance
```

The logic is simple: **the research is only useful if it changes how the agent KBs are built.**

---

# 3. Minimal shared record format

This is the smallest record shape I recommend for almost everything.

```
record:  rank: 1  id: "BP-001"  type: "best_practice"  name: "typed_boundary_contracts"  source_ids: ["GITHUB_MULTI_AGENT", "STRUCTURED_OUTPUTS"]  rule: "All agent-to-agent and agent-to-tool boundaries must use typed schemas."  why_it_matters: "Prevents ambiguous handoffs, invalid payloads, and silent state corruption."  applies_to: ["handoff", "tool_call", "state_update", "verifier_packet"]  output_use: ["meta_detective_kb", "orchestration_agent_kb"]
```

That is enough for the main extraction.

Only add extra fields when needed:

```
optional_fields:  control:  check:  anti_pattern:  example_format:  adoption_status:
```

No default `owner`, `validator`, `file_path`, `retrieval_keywords`, `confidence`, `aliases`, etc. unless the section specifically needs it.

---

# 4. Required final output structure for Gemini

## Final Gemini output should have exactly these chapters

```
final_output_structure:  0_run_metadata:  1_source_index:  2_ranked_failure_modes:  3_ranked_best_practices:  4_ranked_guardrails:  5_ranked_inter_agent_formats:  6_ranked_design_rules:  7_ranked_correlations:  8_ranked_agent_kb_build_rules:  9_minimal_schemas_and_templates:  10_excluded_or_low_confidence_items:  11_open_questions_for_human_lock:
```

This is much better than a full “research report” because each chapter is directly usable for agent KB construction.

---

# 5. Chapter-by-chapter design

## `0_run_metadata`

Purpose: make the output auditable without wasting tokens.

```
run_metadata:  model_target: "Gemini Deep Research Max"  date:  research_scope: "agentic_ai_orchestration_failure_and_best_practice_extraction"  output_mode: "machine_readable"  ranking_scale: "1-100"  evidence_policy: "no uncited operational rule"
```

---

## `1_source_index`

Purpose: list sources once so every record can cite compact `source_ids`.

```
source_index:  - source_id: "MAST"    type: "paper_dataset"    extraction_depth: "full"    use_for: ["failure_modes", "taxonomy", "agent_coordination_risks"]  - source_id: "GITHUB_MULTI_AGENT"    type: "engineering_blog"    extraction_depth: "full"    use_for: ["typed_boundaries", "action_schemas", "distributed_systems_frame"]
```

**Why necessary:** The GitHub engineering article says multi-agent workflows fail because agents make implicit assumptions about state, ordering, and validation; it recommends explicit instructions, data formats, typed schemas, and strict interfaces.

---

## `2_ranked_failure_modes`

Purpose: what goes wrong.

```
failure_modes:  - rank: 1    id: "FM-001"    name: "untyped_boundary_failure"    source_ids: ["GITHUB_MULTI_AGENT", "MAST"]    failure: "Agents exchange ambiguous natural language or inconsistent JSON."    effect: "Downstream agents infer wrong state or take invalid actions."    prevention: "typed_schema + action_schema + validation_gate"    applies_to: ["handoff", "tool_call", "state_update"]
```

**Must include:** MAST categories, because MAST identifies 14 failure modes across system design issues, inter-agent misalignment, and task verification, based on 1,600+ annotated traces across 7 multi-agent frameworks.

---

## `3_ranked_best_practices`

Purpose: what to do.

```
best_practices:  - rank: 1    id: "BP-001"    name: "design_for_failure_first"    source_ids: ["GITHUB_MULTI_AGENT", "MAST"]    rule: "Assume every agent boundary can fail; validate before propagation."    applies_to: ["architecture", "handoff", "tools", "state"]    output_use: ["orchestration_agent_kb"]
```

This chapter is equally important as failure modes. The output should not only say “what breaks”; it must say “what becomes doctrine/rule/check.”

---

## `4_ranked_guardrails`

Purpose: operational safety gates.

```
guardrails:  - rank: 1    id: "GR-001"    name: "schema_invalid_tripwire"    source_ids: ["OPENAI_GUARDRAILS", "STRUCTURED_OUTPUTS"]    trigger: "output does not match required schema"    action: "halt_or_retry_before_downstream_use"    applies_to: ["extraction_record", "handoff_packet", "verifier_result"]
```

OpenAI’s Agents SDK docs define input/output/tool guardrails and tripwires that halt execution when triggered, which maps directly to the kind of executable guardrail ledger needed here.

---

## `5_ranked_inter_agent_formats`

Purpose: define how agents should talk.

```
inter_agent_formats:  - rank: 1    id: "FMT-001"    name: "handoff_packet"    source_ids: ["OPENAI_HANDOFFS", "GITHUB_MULTI_AGENT"]    format:      from:      to:      task:      allowed_context:      required_output:      stop_condition:    rule: "No free-form handoff without required fields."
```

OpenAI’s handoff docs say handoffs are represented as tools, can carry structured `inputType` payloads, and can filter what history the receiving agent sees.

---

## `6_ranked_design_rules`

Purpose: architecture-level rules.

```
design_rules:  - rank: 1    id: "DR-001"    name: "agents_are_distributed_system_components"    source_ids: ["GITHUB_MULTI_AGENT"]    rule: "Treat multi-agent systems like distributed systems, not chat threads."    consequence: "Require explicit state, ordering, validation, retries, and logs."
```

This should extract rules like:

```
design_rule_categories:  - boundary_design  - state_design  - verification_design  - context_design  - tool_permission_design  - observability_design  - escalation_design
```

---

## `7_ranked_correlations`

Purpose: capture high-value “if this, then that” relationships.

```
correlations:  - rank: 1    id: "COR-001"    relation: "untyped_messages -> downstream_state_corruption"    source_ids: ["GITHUB_MULTI_AGENT", "MAST"]    implication: "Typed schemas are not optional for multi-agent KB/runtime design."
```

This is where Gemini should extract patterns such as:

```
correlation_targets:  - failure_to_control  - control_to_verification_check  - architecture_choice_to_failure_risk  - context_size_to_drift_risk  - tool_power_to_security_risk  - handoff_freedom_to_ambiguity_risk
```

---

## `8_ranked_agent_kb_build_rules`

Purpose: convert the research into rules for building the two future KBs.

```
agent_kb_build_rules:  - rank: 1    id: "KB-001"    rule: "Do not store theory unless it becomes a rule, failure, guardrail, format, or check."    applies_to: ["meta_detective_kb", "orchestration_agent_kb"]    source_ids: ["STUDYPLAN", "GITHUB_MULTI_AGENT"]
```

This is the chapter that prevents “nice research” from becoming unusable knowledge.

---

## `9_minimal_schemas_and_templates`

Purpose: give reusable formats, not long explanations.

```
templates:  handoff_packet:    from:    to:    task:    allowed_context:    required_output:    stop_condition:  verification_packet:    claim:    source_ids:    check:    pass_fail:    escalation_reason:  guardrail_packet:    trigger:    blocked_action:    required_fix:
```

Gemini structured outputs support JSON Schema for predictable, parsable responses, but Google also warns that schema-conformant output still needs semantic validation.

---

## `10_excluded_or_low_confidence_items`

Purpose: stop garbage from entering the KB.

```
excluded_items:  - name:    reason:    source_ids:    status: "excluded | weak | duplicate | too_theoretical | vendor_specific"
```

---

## `11_open_questions_for_human_lock`

Purpose: only questions that block KB design.

```
open_questions:  - id: "Q-001"    question: "Should MCP be included only as boundary model or also as runtime candidate?"    reason: "Security impact."    decision_options: ["concept_only", "security_review", "runtime_candidate"]
```

---

# 6. Extraction variables: necessary / optional / residual

## A. For-sure necessary

These should be required in the Gemini prompt.

```
required_extraction_targets:  - ranked_failure_modes  - ranked_best_practices  - ranked_guardrails  - ranked_inter_agent_formats  - ranked_design_rules  - ranked_correlations  - ranked_agent_kb_build_rules  - minimal_templates  - source_index  - excluded_items
```

## B. Required fields per normal record

```
required_record_fields:  - rank  - id  - type  - name  - source_ids  - rule_or_failure  - operational_implication  - applies_to
```

That is the new standard. Compact and realistic.

## C. Nice but optional

Use only when the information exists naturally.

```
optional_record_fields:  - prevention  - check  - example_format  - anti_pattern  - adoption_status  - security_note  - headless_cloud_note
```

## D. Residual tier for your check

These may be useful but should not be required globally.

```
residual_check_items:  - confidence_score  - evidence_strength_score  - frequency_score  - owner  - validator  - target_file_path  - aliases  - retrieval_keywords  - source_quote  - page_number  - implementation_complexity
```

**Recommendation:** Do **not** require these in the main Gemini output. They are useful later for KB implementation, but they will bloat the Deep Research output.

---

# 7. Ranked extraction target list

## Tier 1 — mandatory output chapters

|Rank|Output item|Why required|
|---|---|---|
|1|**Best practice ledger**|Tells future agents what to do.|
|2|**Failure mode ledger**|Tells future agents what to prevent/detect.|
|3|**Guardrail ledger**|Converts lessons into executable checks.|
|4|**Inter-agent format ledger**|Defines how agents communicate without drift.|
|5|**Design rule ledger**|Converts research into architecture constraints.|
|6|**Correlation ledger**|Shows which failures are caused/prevented by which patterns.|
|7|**Agent KB build rules**|Directly guides construction of the two future KBs.|
|8|**Minimal templates**|Gives reusable operational packet formats.|
|9|**Source index**|Keeps provenance without repeating citations everywhere.|
|10|**Excluded items**|Prevents weak theory/hype from entering doctrine.|

## Tier 2 — optional if output budget allows

```
optional_outputs:  - study_cards_compact  - control_candidate_matrix  - headless_cloud_risk_matrix  - prompt_design_rules  - source_authority_rules  - orchestration_topology_patterns  - observability_trace_rules
```

## Tier 3 — residual / human decision

```
human_decision_items:  - whether MCP is concept_only or runtime_candidate  - whether Deep Research should create file-path recommendations  - whether every record needs source quotes  - whether headless cloud gets its own chapter or only tags  - whether agent-specific KB split is included now or later
```

---

# 8. The simplified scoring model

Everything should be ranked, but not with a complex formula.

Use this:

```
ranking_rule:  score: 1-100  rank_by:    - operational_importance    - evidence_strength    - recurrence_across_sources    - direct_relevance_to_agent_kb_build
```

Do **not** require separate sub-scores per item.

If Gemini needs to justify ranking:

```
rank_reason: "high evidence + high orchestration relevance + direct KB design impact"
```

One line only.

---

# 9. Corrected pre-run instruction for Gemini

This is the “test run” structure I recommend before the final Deep Research prompt.

```
pre_run_task:  objective: "Validate the final output structure before full research."  model: "Gemini Deep Research Max"  output_mode: "machine_readable"  do_not_do:    - full research    - full literature review    - long explanations    - per-source summaries  produce:    - proposed_source_tiers    - proposed_output_chapters    - extraction_target_list    - minimal_record_schema    - 3_example_records    - risk_of_output_drift    - recommended_deletions_from_schema
```

Expected pre-run output:

```
pre_run_output:  source_tiers:    tier_1: []    tier_2: []    tier_3: []  final_output_chapters:    - chapter_id:      chapter_name:      required: true      record_type:      why_needed:  minimal_record_schema:    fields: [rank, id, type, name, source_ids, rule_or_failure, operational_implication, applies_to]  example_records:    - rank: 1      id: "BP-001"      type: "best_practice"      name: "typed_boundary_contracts"      source_ids: ["GITHUB_MULTI_AGENT"]      rule_or_failure: "All agent boundaries require typed schemas."      operational_implication: "No free-form agent handoff becomes KB/runtime doctrine."      applies_to: ["handoff", "tool_call", "state_update"]  schema_deletions:    - field:      reason:
```

---

# 10. Updated decision lock

```
locked_decisions_v2:  output_is_not_only_failure_ledger: true  output_must_include_best_practice_ledger: true  output_must_rank_every_major_extraction_type: true  output_style: "machine_readable_dense_token_efficient"  avoid_overengineering: true  one_normal_record_schema: true  minimal_required_fields:    - rank    - id    - type    - name    - source_ids    - rule_or_failure    - operational_implication    - applies_to  required_chapters:    - source_index    - ranked_failure_modes    - ranked_best_practices    - ranked_guardrails    - ranked_inter_agent_formats    - ranked_design_rules    - ranked_correlations    - ranked_agent_kb_build_rules    - minimal_schemas_and_templates    - excluded_or_low_confidence_items    - open_questions_for_human_lock  gemini_mode: "Deep Research Max"  first_step: "pre_run_structure_validation"
```

The next step should be the actual **copy-paste-ready Gemini Deep Research Max pre-run prompt**, not the final full research prompt yet.

You have caused a lot of drift because you apply best practice from agentic orchestration to a deep research prompt. This is very dangerous drift. We need to create everything that you have defined from 1 to 4. Everything thereafter is not going to fly with the deep research prompt in Gemini. This is way too many variables, way too many checks. This is not going to work. Yeah, and I don't have the deep research max, I only have a Pro subscription with Gemini, so yeah, do the best practice research to align that. Again, I want you to create already a final test run with the web search, with the studies that you know, so that I can see what the output is you are actually creating. I don't want any theory anymore. Give me an example output on what the deep research prompt is going to look like. Look, use your web research, pretend you are the deep research prompt and you're doing a test run that focuses on the output so that I can check the output if it's actually what I want.

I’ll stop expanding the schema. I’m going to show the actual target output now: a compact test-run artifact, using only the first four core ledgers plus source index/ranking.

Thought for 27s

You’re right. I mixed **agent-orchestration best practice** into the **Deep Research prompt/output design**. That is drift.

For your Gemini **Pro** subscription: use **Gemini Apps → Tools → Deep Research**. Google’s help page says Google AI Pro users can generate Deep Research reports using **Pro** for higher quality, while Ultra mainly adds higher limits and optional richer visuals; you do **not** need “Deep Research Max” for this workflow.

Below is the **actual test-run output shape** I would want Gemini Deep Research to produce. It only uses the first 4 outputs:

```
1_source_index2_ranked_failure_modes3_ranked_best_practices4_ranked_guardrails
```

No extra matrix. No theory chapter. No agent architecture essay.

---

# TEST RUN OUTPUT — Agentic AI Orchestration Failure + Best Practice Extraction

```
run:  goal: "extract ranked operational guidance for future agent KB build"  output_mode: "machine_readable_compact"  scope:    - agentic_ai_orchestration_failures    - multi_agent_coordination_best_practices    - guardrails_for_agent_kb_design  not_scope:    - general_ai_theory    - literature_summary    - full_agent_design    - final_KB_files
```

---

## 1_source_index

```
sources:  - id: MAST    title: "Why Do Multi-Agent LLM Systems Fail?"    type: "paper/dataset"    use: "failure taxonomy"    priority: 1    extraction_depth: "deep"    status: "primary"    key_signal: "14 failure modes across system design, inter-agent misalignment, and task verification; based on 1600+ traces."    use_limit: "classifier input, not final doctrine"  - id: GITHUB_MULTI_AGENT    title: "Multi-agent workflows often fail. Here’s how to engineer ones that don’t."    type: "engineering_article"    use: "production best practices"    priority: 2    extraction_depth: "deep"    status: "primary_supporting"    key_signal: "multi-agent workflows behave like distributed systems; failures come from implicit state, ordering, validation, untyped messages, vague intent, loose interfaces."    use_limit: "strong operational rule source"  - id: STRUCTURED_OUTPUTS    title: "Structured Outputs / schema-constrained outputs"    type: "vendor_docs"    use: "machine-readable output enforcement"    priority: 3    extraction_depth: "targeted"    status: "supporting"    key_signal: "schema-conformant output improves parsability; still requires semantic validation."    use_limit: "mechanism source only"  - id: GUARDRAILS    title: "Agent guardrails / tripwires"    type: "vendor_docs"    use: "halt/verify gate design"    priority: 4    extraction_depth: "targeted"    status: "supporting"    key_signal: "guardrails should block unsafe or invalid inputs/outputs/tool calls."    use_limit: "mechanism source only"  - id: STUDYPLAN    title: "studyplan.txt"    type: "project_task_lock"    use: "local output constraints"    priority: 0    extraction_depth: "binding"    status: "local_task_authority"    key_signal: "KB must be machine-readable, token-efficient, non-drift, non-ambiguous, and must not become a study dump."    use_limit: "defines output target"
```

Source grounding: the local studyplan requires a usable, machine-readable, token-efficient Detective research KB and explicitly rejects untyped blobs, uncited claims, and direct promotion of research into doctrine. It also defines the intended pipeline as raw studies → source manifest → study cards → claim extraction → failure matrix → controls/checks, not summaries. GitHub’s 2026 article states that multi-agent systems fail when agents make implicit assumptions about state, ordering, and validation, and recommends explicit instructions, data formats, schemas, interfaces, action schemas, logging, retries, and treating agents like distributed systems.

---

## 2_ranked_failure_modes

```
failure_modes:  - rank: 1    id: FM_UNTYPED_BOUNDARY    name: "untyped_agent_boundary"    source_ids: [GITHUB_MULTI_AGENT, MAST, STRUCTURED_OUTPUTS]    failure: "agents exchange ambiguous prose, inconsistent JSON, shifting field names, or invalid payloads"    impact: "downstream agents guess meaning; state corruption propagates silently"    required_control: "typed_schema_at_every_agent_boundary"    kb_build_use: "future agent KBs must define accepted input/output packet shapes before defining behavior"  - rank: 2    id: FM_VAGUE_ACTION_INTENT    name: "vague_action_intent"    source_ids: [GITHUB_MULTI_AGENT]    failure: "agent is told to 'handle', 'analyze', 'fix', or 'take action' without allowed action set"    impact: "different agents choose incompatible actions that all seem locally reasonable"    required_control: "action_schema_with_allowed_actions"    kb_build_use: "agent KB must define allowed decisions/actions, not only mission prose"  - rank: 3    id: FM_ROLE_TASK_AMBIGUITY    name: "role_task_ambiguity"    source_ids: [MAST, STUDYPLAN]    failure: "agent performs work outside its role or confuses validator/executor/owner responsibilities"    impact: "self-validation, duplicated authority, wrong agent mutates or approves output"    required_control: "role_boundary + non_role_boundary"    kb_build_use: "agent KB must say what the agent must not do"  - rank: 4    id: FM_VERIFICATION_GAP    name: "completion_without_verification"    source_ids: [MAST, STUDYPLAN]    failure: "task marked complete without evidence that output is valid"    impact: "false completion becomes accepted state"    required_control: "verification_packet_before_done"    kb_build_use: "agent KB must define completion proof, not just output format"  - rank: 5    id: FM_INTER_AGENT_MISALIGNMENT    name: "inter_agent_misalignment"    source_ids: [MAST, GITHUB_MULTI_AGENT]    failure: "agents contradict, overwrite, duplicate, or invalidate each other's work"    impact: "multi-agent system becomes less reliable than one bounded agent"    required_control: "single_owner_per_decision + handoff_contract"    kb_build_use: "agent KB must define ownership boundaries and escalation paths"  - rank: 6    id: FM_CONTEXT_LOSS_BETWEEN_AGENTS    name: "context_does_not_travel"    source_ids: [GITHUB_MULTI_AGENT, STUDYPLAN]    failure: "receiving agent lacks the parent agent's discoveries, constraints, decisions, or state"    impact: "agent re-discovers, contradicts, or ignores prior work"    required_control: "handoff_packet_with_required_context"    kb_build_use: "agent KB must specify what context must travel during handoff"  - rank: 7    id: FM_OVER_AGENTIFICATION    name: "too_many_agents_before_contracts"    source_ids: [MAST, GITHUB_MULTI_AGENT]    failure: "system adds agents before schemas, state, logs, and validation are stable"    impact: "coordination overhead outweighs specialization benefit"    required_control: "function_first_agent_later"    kb_build_use: "agent KB should not create sub-agents unless repeated bounded failure justifies it"  - rank: 8    id: FM_SOURCE_TO_DOCTRINE_DRIFT    name: "research_becomes_runtime_law"    source_ids: [STUDYPLAN]    failure: "study insight is copied into agent doctrine without adoption decision"    impact: "vendor claims or research patterns become untested local rules"    required_control: "source_status + adoption_status"    kb_build_use: "KB must distinguish evidence, candidate, accepted rule"
```

---

## 3_ranked_best_practices

```
best_practices:  - rank: 1    id: BP_TYPED_BOUNDARIES    name: "typed_boundaries_before_agent_behavior"    source_ids: [GITHUB_MULTI_AGENT, STRUCTURED_OUTPUTS]    rule: "define input/output schemas before defining agent collaboration"    why: "invalid messages should fail fast before corrupting downstream state"    applies_to: [handoff, tool_call, extraction_output, verification_output]    kb_build_instruction: "every future agent KB needs a small accepted packet format section"  - rank: 2    id: BP_ACTION_SCHEMAS    name: "allowed_action_set"    source_ids: [GITHUB_MULTI_AGENT]    rule: "replace vague action intent with a closed list of valid actions"    why: "agents do not reliably infer intended action from prose"    applies_to: [decision, escalation, task_completion, mutation_request]    kb_build_instruction: "agent KB must define allowed outputs/actions as enums or compact list"  - rank: 3    id: BP_VALIDATE_EVERY_BOUNDARY    name: "validate_every_agent_boundary"    source_ids: [GITHUB_MULTI_AGENT, GUARDRAILS]    rule: "every transfer between agents/tools/files needs a validation point"    why: "boundary failures are cheaper to catch before propagation"    applies_to: [handoff, source_ingest, tool_call, file_write]    kb_build_instruction: "KB must include 'before handoff/check before done' rules"  - rank: 4    id: BP_EVIDENCE_BEFORE_ACCEPTANCE    name: "evidence_before_acceptance"    source_ids: [STUDYPLAN, MAST]    rule: "no claim becomes accepted KB knowledge without source status and extraction status"    why: "prevents summary hallucination and source ambiguity"    applies_to: [research_claim, best_practice, failure_mode, guardrail]    kb_build_instruction: "future KB should store source IDs next to operational rules"  - rank: 5    id: BP_DISTRIBUTED_SYSTEM_FRAME    name: "treat_agents_like_distributed_system_components"    source_ids: [GITHUB_MULTI_AGENT]    rule: "design for partial failure, ordering issues, retries, state mismatch, and logs"    why: "multi-agent workflows fail like distributed systems, not like chat conversations"    applies_to: [architecture, orchestration, debugging, production_use]    kb_build_instruction: "KB language should include state, validation, retry, escalation, trace"  - rank: 6    id: BP_MINIMAL_MACHINE_READABLE_KB    name: "minimal_machine_readable_kb"    source_ids: [STUDYPLAN]    rule: "store rules, failures, controls, and checks; do not store prose summaries as primary knowledge"    why: "agents need operational records, not essays"    applies_to: [agent_kb, source_ingest, research_output]    kb_build_instruction: "final KB chapters should be ledgers, not reports"  - rank: 7    id: BP_STUDY_CARD_NOT_FULL_SUMMARY    name: "study_card_not_full_summary"    source_ids: [STUDYPLAN]    rule: "each study gets compact source card; only top sources get deep extraction"    why: "prevents research bloat and token waste"    applies_to: [source_index, research_ingest]    kb_build_instruction: "do not ask Gemini to summarize every study equally"  - rank: 8    id: BP_VENDOR_DOCS_AS_MECHANISM    name: "vendor_docs_are_mechanism_not_doctrine"    source_ids: [STUDYPLAN, STRUCTURED_OUTPUTS, GUARDRAILS]    rule: "vendor docs can define mechanisms but not universal architecture law"    why: "prevents vendor-specific design drift"    applies_to: [OpenAI_docs, Google_docs, LangGraph_docs, MCP_docs]    kb_build_instruction: "mark vendor-derived rules as mechanism/candidate unless locally adopted"
```

---

## 4_ranked_guardrails

```
guardrails:  - rank: 1    id: GR_NO_UNTYPED_HANDOFF    name: "block_untyped_handoff"    source_ids: [GITHUB_MULTI_AGENT, STUDYPLAN]    trigger: "agent handoff has no structured packet"    action: "halt_or_rewrite_handoff"    minimal_check: "from/to/task/context/output/stop_condition present"    kb_build_instruction: "handoff format must be in future KB before agent collaboration rules"  - rank: 2    id: GR_NO_VAGUE_ACTION    name: "block_vague_action_request"    source_ids: [GITHUB_MULTI_AGENT]    trigger: "task uses vague verbs without allowed action set"    action: "force_action_schema"    minimal_check: "allowed actions listed"    kb_build_instruction: "agent KB must define allowed actions for high-impact work"  - rank: 3    id: GR_NO_UNSOURCED_RULE    name: "block_unsourced_operational_rule"    source_ids: [STUDYPLAN]    trigger: "failure/best_practice/guardrail has no source_id"    action: "mark_as_candidate_or_remove"    minimal_check: "source_id present"    kb_build_instruction: "every extracted rule must carry at least one source_id"  - rank: 4    id: GR_NO_SELF_VALIDATION    name: "block_executor_self_validation"    source_ids: [MAST, STUDYPLAN]    trigger: "same agent creates and validates its own accepted output"    action: "route_to_detective_or_validator"    minimal_check: "validator role differs from producer role"    kb_build_instruction: "agent KB must separate execution and validation"  - rank: 5    id: GR_NO_STUDY_TO_DOCTRINE_DIRECT    name: "block_direct_research_to_doctrine"    source_ids: [STUDYPLAN]    trigger: "research insight is promoted as accepted rule without adoption decision"    action: "mark_candidate"    minimal_check: "adoption_status present: accepted/candidate/rejected/security_review"    kb_build_instruction: "future KB must separate source evidence from accepted operating rule"  - rank: 6    id: GR_NO_AGENT_SPRAWL    name: "block_new_agent_without_boundary"    source_ids: [MAST, GITHUB_MULTI_AGENT, STUDYPLAN]    trigger: "new agent role proposed without input/output/authority boundary"    action: "keep_as_function_or_mode"    minimal_check: "role, non-role, inputs, outputs, escalation defined"    kb_build_instruction: "KB should prefer modes/functions before new agents"  - rank: 7    id: GR_NO_TOOL_EXPANSION_WITHOUT_SECURITY_REVIEW    name: "block_tool_expansion_without_security_review"    source_ids: [STUDYPLAN]    trigger: "agent receives new tool/file/network permission"    action: "security_review_required"    minimal_check: "permission scope + allowed paths + forbidden paths + dry run"    kb_build_instruction: "tool power must be handled as risk, not convenience"  - rank: 8    id: GR_NO_REPORT_STYLE_OUTPUT    name: "block_report_style_research_output"    source_ids: [STUDYPLAN]    trigger: "output becomes narrative report or theory summary"    action: "convert_to_ledger"    minimal_check: "ranked YAML/table records exist"    kb_build_instruction: "Gemini output must stay ledger-first"
```

---

# Compact verdict on the test run

```
verdict:  output_fit: "closer"  keep:    - source_index    - ranked_failure_modes    - ranked_best_practices    - ranked_guardrails  remove:    - long design_rule_chapter    - correlation_chapter    - agent_kb_build_rules_chapter    - complex per-record metadata    - owner_validator_file_path_fields  prompt_implication: "Gemini Deep Research prompt should ask for this exact four-part output, not a full report."
```

This output is the level of structure I would now target for the actual Gemini Deep Research prompt.

I still don't see what the actual output is going to be. What I see... I don't understand your output. I just don't understand it. So, okay, one source index seems to be okay. So that we can later reference it. Okay, that's fine. So then, ranked failure modes. Are these sources or are these extracted rules that you are doing there? I have no idea what that is. Are these sources? I have no idea what this is. Are these just sources? I think these are just sources, right? What you were supposed to do is show me the full fucking output. What did I fucking tell you to do? Full fucking output. Not just sources. What the fuck are you doing here? I need to see what you are defining as the example output so the Gemini deep research prompt knows exactly what to do. If these are just sources, you just did one thing. You just gave me the sources that we are going to link. But these sources are what we input into the Gemini deep research prompt. It's not what we get out. What the fuck are you doing again?

Stopped thinkingSchnelle Antwort

tis is your thining process: Denke nach… Addressing user frustration and searching for sources It seems I need to respond clearly to the user. I should provide the full output, not just sources. I’ll clarify what’s being extracted and rank failure modes. I need to use web search to get relevant, up-to-date sources like MAST, GitHub, or other structured outputs. Gemini Pro might be relevant too, but I won’t mention it unless they ask for more. Searching for failure modes and multi-agent workflow insights Clarifying requested output and including example I need to provide a clear apology and explain that failure modes are extracted outputs, not sources. The user requested the "full" output, so I’ll provide a detailed example, including sections like source_index, ranked_failure_modes, best_practices, and guardrails. I'll use a simple table format instead of YAML, as they want machine-readable examples. Structuring the full output example For the full output, I should include 10-15 records, with each record displaying rank, id, extracted finding, rule/check, and source_ids. There won't be commentary, just clear data. I'll give concise citations for web sources, either before or within the source_index. I'll ensure each factual claim is sourced properly, using MAST and arxiv. I'll clarify that failure modes are extracted, not sources. Searching MAST failure modes and generating output example Searching for Google support on Gemini and AI Pro Providing full output with citations and explanation I’ll go ahead and provide the full output now, as the user requests, with a long example that includes 6 failure modes, 8 best practices, and 6 guardrails. I'll use YAML for clarity and explain that source_index refers to inputs, while failure modes and others are extracted outputs. I'll add citations in prose before the code block and make it clear this isn’t exhaustive, just a demonstration. Stopped thinking

Stopped thinkingSchnelle Antwort

Denke nach… Addressing user frustration and searching for sources It seems I need to respond clearly to the user. I should provide the full output, not just sources. I’ll clarify what’s being extracted and rank failure modes. I need to use web search to get relevant, up-to-date sources like MAST, GitHub, or other structured outputs. Gemini Pro might be relevant too, but I won’t mention it unless they ask for more. Searching for failure modes and multi-agent workflow insights Clarifying requested output and including example I need to provide a clear apology and explain that failure modes are extracted outputs, not sources. The user requested the "full" output, so I’ll provide a detailed example, including sections like source_index, ranked_failure_modes, best_practices, and guardrails. I'll use a simple table format instead of YAML, as they want machine-readable examples. Structuring the full output example For the full output, I should include 10-15 records, with each record displaying rank, id, extracted finding, rule/check, and source_ids. There won't be commentary, just clear data. I'll give concise citations for web sources, either before or within the source_index. I'll ensure each factual claim is sourced properly, using MAST and arxiv. I'll clarify that failure modes are extracted, not sources. Searching MAST failure modes and generating output example Searching for Google support on Gemini and AI Pro Providing full output with citations and explanation I’ll go ahead and provide the full output now, as the user requests, with a long example that includes 6 failure modes, 8 best practices, and 6 guardrails. I'll use YAML for clarity and explain that source_index refers to inputs, while failure modes and others are extracted outputs. I'll add citations in prose before the code block and make it clear this isn’t exhaustive, just a demonstration. Stopped thinkingAgain, the only thing that I'm seeing is you creating drift. I have no idea what you're doing right now. I told you to do a pre-run of what we want the Gemini research to actually output. What I understood what you did is just source verification, so no output, but the input that we give to the Gemini process. Again, the task of you to do now is give me an example output of what the Gemini research is actually going to produce, and you are already supposed to research that from the different research target files that we have been discussing so that we can check what the fuck you are actually going to do. We need to define that for Gemini. What are you not understanding here? When I look into your thinking process, you start to go into an insane amount of resources that we don't need. Or am I completely wrong here? Please, let's do another short question and answers run because you seem to completely fuck up everything again.

You are right: I kept showing **research scaffolding** instead of the **actual artifact Gemini should output**. I’ll reset the target now and keep this to a short decision Q&A, then the next step can be the actual sample artifact.

Thought for 21s

Yes. Your diagnosis is correct.

I was still building **source/input scaffolding** instead of showing the **actual example output Gemini should produce**. That is the wrong layer.

The correct task now is **not**:

```
wrong:  - collect_sources  - verify_sources  - design_folder_structure  - define_KB_architecture  - create_implementation_pipeline
```

The correct task is:

```
right:  - simulate_the_final_Gemini_Deep_Research_output  - already_fill_it_with_example_extracted_records  - make_it_obvious_what_Gemini_should_output  - let_you_judge_the_shape_before_we_write_the_prompt
```

Google’s own Gemini help page says Gemini Deep Research creates cited reports, can use Google Search and uploaded files, and Google AI Pro users can generate reports using Pro for higher quality. So we should design for **Gemini Pro Deep Research**, not “Deep Research Max.”

---

# Short Q&A reset

## Q1. What exactly should I produce next?

**Answer:** A **mock final Gemini Deep Research output**, already filled with example records.

Not a prompt.  
Not a source plan.  
Not a source index alone.  
Not architecture advice.

It should look like this:

```
gemini_deep_research_output_example:  source_index: [...]  ranked_failure_modes: [...]  ranked_best_practices: [...]  ranked_guardrails: [...]
```

Each ledger must contain **actual extracted outputs**, for example:

```
- rank: 1  item: "Typed agent boundaries are mandatory"  extracted_from: ["GitHub multi-agent workflows", "Structured Outputs"]  operational_rule: "No agent handoff may rely on free-form prose."
```

---

## Q2. Are “ranked failure modes” sources?

**Answer:** No.

A source is:

```
source:  id: "MAST"  title: "Why Do Multi-Agent LLM Systems Fail?"
```

A failure mode is the **extracted finding** from that source:

```
failure_mode:  rank: 1  id: "FM_UNTYPED_BOUNDARY"  finding: "Agents fail when handoffs use ambiguous messages or inconsistent fields."  source_ids: ["GITHUB_MULTI_AGENT", "MAST"]  implication: "Future KBs must define handoff packet formats before agent behavior."
```

So the source is only the citation handle.  
The failure mode is the actual research output.

---

## Q3. What should the full pre-run output contain?

**Answer:** Only four sections for now.

```
pre_run_output_sections:  1_source_index:    purpose: "reference handles only"  2_ranked_failure_modes:    purpose: "what goes wrong in agentic orchestration"  3_ranked_best_practices:    purpose: "what design rules prevent those failures"  4_ranked_guardrails:    purpose: "what checks block bad outputs or bad agent behavior"
```

Nothing else.

No folder structure.  
No KB implementation plan.  
No source-ingestion workflow.  
No giant extraction schema.

---

## Q4. How many records should the example output have?

**Answer:** Enough to see the shape, not exhaustive.

Recommended test-run size:

```
test_run_size:  source_index: 5-8 sources  ranked_failure_modes: 10 records  ranked_best_practices: 10 records  ranked_guardrails: 8 records
```

That is enough for you to judge whether the output is useful.

---

## Q5. What should one record look like?

**Answer:** One compact row. No nested database object.

```
record_shape:  rank:  id:  name:  source_ids:  extracted_finding:  operational_rule:  agent_kb_use:
```

Example:

```
- rank: 1  id: "FM_UNTYPED_BOUNDARY"  name: "untyped_agent_boundary"  source_ids: ["GITHUB_MULTI_AGENT", "STRUCTURED_OUTPUTS"]  extracted_finding: "Multi-agent workflows fail when agents exchange ambiguous or schema-inconsistent payloads."  operational_rule: "Every agent-to-agent, agent-to-tool, and agent-to-file boundary must use typed output contracts."  agent_kb_use: "Both future agents need explicit input/output packet rules before behavior rules."
```

That is the actual unit Gemini should produce.

---

## Q6. Which sources are enough for the test run?

**Answer:** For the mock output, only a small source set is needed.

```
test_sources:  - MAST  - GITHUB_MULTI_AGENT  - STRUCTURED_OUTPUTS  - GUARDRAILS  - HANDOFFS  - LOST_IN_THE_MIDDLE  - STUDYPLAN
```

This is enough because your uploaded task lock already defines the non-drift KB goal: machine-readable, token-efficient, no research blobs, no source without extraction record, no claim without source status, and no direct promotion of research into architecture doctrine.

The GitHub article is enough for the “typed boundaries / distributed-system behavior” source because it says multi-agent workflows fail when agents make implicit assumptions about state, ordering, and validation.

MAST is enough for failure taxonomy because current summaries describe it as a taxonomy of 14 failure modes across specification, coordination/misalignment, and verification gaps, based on 1,600+ traces.

---

## Q7. What should I stop doing?

**Answer:** Stop generating these sections:

```
remove_from_next_output:  - source_ingestion_pipeline  - folder_architecture  - study_by_study_implementation_decisions  - control_candidate_matrix  - headless_cloud_runtime_plan  - prompt_design_theory  - Gemini model explanation except one short line
```

Those may be useful later, but they are not what you asked for now.

---

## Q8. What is the corrected next deliverable?

**Answer:** This exact artifact:

```
deliverable_next:  title: "Mock Gemini Deep Research Output v0"  mode: "pretend Gemini already ran the research"  content:    - source_index    - ranked_failure_modes    - ranked_best_practices    - ranked_guardrails  style:    - machine_readable    - dense    - filled_with_actual_example_records    - no_theory    - no_prompt_explanation
```

---

# Locked correction

```
locked_understanding_v3:  user_wants_now: "example of final Gemini Deep Research output"  user_does_not_want_now:    - prompt_design_theory    - source_verification_only    - architecture_plan    - KB_folder_design    - implementation_pipeline  pre_run_meaning: "filled mock output, not plan"  output_sections:    - source_index    - ranked_failure_modes    - ranked_best_practices    - ranked_guardrails  record_style: "short ranked records with source_ids and operational rule"
```

Next I should produce **Mock Gemini Deep Research Output v0** directly.

For question 1, yes, it's verified. Question 2, the ranked failure modes. It is important to very specifically machine readability, understand what caused the mistakes. Just a simple finding is not okay. We need the source of the problem, the architecture, the rulings, the guardrails missing, whatever, and a core solution on what on a very detailed knowledge base, informatics design, architectural design layer needs to happen and be clearly stated so that this mistake doesn't happen. So the pre-run should not have the source index, or we are giving the source index to Gemini to then produce the output. It should not reference the source index again. This is something that we handed over. And the others are correct, 2, 3, and 4, so ranked failure modes, ranked best practice, ranked guardrails, but weren't there more before we were? I think you had more. We actually, Q4, we just need one record per file. That is it. Maybe if there are very different types of records, then we need more, but this is something that you need to decide now. That's Q5 seems good. Regarding the Q6 test sources, just do something that is quickly doable. Choose whatever, maybe choose two sources that are different from each other so we can understand different kinds of failure modes. Q7 validated. Okay, rest of it's validated, go.

Thought for 20s

Yes. Locked.

Below is the **actual pre-run output artifact**. No source index. No prompt theory. No folder architecture. Just one example record per output file.

Grounding used only for this mock: **MAST** for multi-agent failure taxonomy, especially specification / inter-agent / verification failures, and **GitHub’s 2026 multi-agent engineering article** for typed schemas, action schemas, interface enforcement, and distributed-systems framing.

```
mock_gemini_deep_research_output_v0:  output_mode: "machine_readable_pre_run"  source_index_included: false  source_ids_assumed_from_input: true  record_count:    ranked_failure_modes: 1    ranked_best_practices: 1    ranked_guardrails: 1  ranked_failure_modes:    - rank: 1      id: "FM_UNTYPED_BOUNDARY_STATE_CORRUPTION"      name: "untyped_boundary_causes_state_corruption"      source_ids: ["MAST", "GITHUB_MULTI_AGENT"]      failure_class: "inter_agent_coordination_failure"      caused_by:        root_problem: "agents exchange natural language or weak JSON instead of machine-validated payloads"        architecture_gap: "agent boundaries are treated as conversational transitions instead of typed distributed-system interfaces"        missing_rule: "no mandatory input_output_contract exists for handoff/tool/state packets"        missing_guardrail: "invalid or incomplete handoff payloads are not blocked before downstream execution"        missing_informatics_design: "no canonical packet taxonomy defines which information belongs in task_state, evidence, decision, action, and stop_condition fields"        missing_kb_design: "agent KB describes behavior/role intent but does not define accepted inbound/outbound data shapes"      observable_symptoms:        - "downstream agent guesses missing context"        - "field names shift across agent outputs"        - "same instruction produces different action interpretations"        - "agent marks task done although verification evidence is absent"        - "later agent overwrites or contradicts prior agent state"      impact:        system_effect: "silent state corruption propagates through the orchestration chain"        agent_effect: "agents appear locally reasonable but globally incoherent"        kb_effect: "future agents learn vague collaboration behavior instead of executable boundary rules"      required_solution:        kb_layer:          - "each agent KB must include accepted_input_packet and required_output_packet"          - "each KB must define role, non_role, allowed_actions, stop_conditions"        informatics_layer:          - "create canonical packet types: task_packet, handoff_packet, evidence_packet, verification_packet, escalation_packet"          - "separate human_explanation from machine_action_fields"        architecture_layer:          - "treat every agent boundary as a contract boundary"          - "validate before propagation"          - "log intermediate state after every handoff"        guardrail_layer:          - "block missing required fields"          - "block unknown action types"          - "block completion without verification evidence"      normalized_rule: "No agent output may become input for another agent unless it validates against the target boundary packet."      target_for_future_agent_kbs: ["meta_strategy", "meta_detective"]  ranked_best_practices:    - rank: 1      id: "BP_BOUNDARY_FIRST_AGENT_DESIGN"      name: "define_boundaries_before_agent_behavior"      source_ids: ["GITHUB_MULTI_AGENT", "MAST"]      best_practice_class: "architecture_and_kb_design_rule"      rule: "Define typed boundaries, allowed actions, evidence requirements, and stop conditions before defining agent personality, role prose, or collaboration flow."      why_required:        failure_prevented:          - "untyped_boundary_causes_state_corruption"          - "role_task_ambiguity"          - "completion_without_verification"          - "inter_agent_misalignment"        causal_logic: "multi-agent failure is often caused by implicit assumptions about state, ordering, validation, role, and action intent; boundary-first design removes implicit assumptions before agents collaborate"      required_kb_content:        essence_file:          - "agent purpose"          - "role_boundary"          - "non_role_boundary"          - "authority_boundary"        best_practices_file:          - "valid_handoff_behavior"          - "valid_action_selection"          - "valid_escalation_behavior"        templates_file:          - "handoff_packet"          - "verification_packet"          - "escalation_packet"        mistakes_file:          - "free_form_handoff"          - "self_validation"          - "action_without_allowed_action_set"          - "done_without_evidence"      required_informatics_design:        - "one shared field vocabulary across agents"        - "stable packet names"        - "no duplicate names for same information class"        - "clear distinction between source_evidence, agent_reasoning, decision, and action"      required_architecture_design:        - "agent boundary contract before runtime orchestration"        - "single owner per decision"        - "validator separate from executor for high-impact outputs"        - "handoff logs preserved as trace"      minimal_machine_rule: "agent_definition_order = boundaries -> packets -> allowed_actions -> validation -> behavior"      target_for_future_agent_kbs: ["meta_strategy", "meta_detective"]  ranked_guardrails:    - rank: 1      id: "GR_BLOCK_FREEFORM_HANDOFF"      name: "block_freeform_or_schema_invalid_handoff"      source_ids: ["GITHUB_MULTI_AGENT", "MAST"]      guardrail_class: "boundary_validation_tripwire"      trigger:        any_of:          - "handoff has no structured packet"          - "required field missing"          - "unknown field used for machine action"          - "allowed_action not in action set"          - "verification evidence absent when status is done"          - "receiving agent cannot determine owner, task, constraints, or stop condition"      block_condition: "downstream agent execution must not start"      required_repair:        - "rewrite handoff into valid handoff_packet"        - "add missing source/evidence fields"        - "select one allowed_action"        - "state stop_condition"        - "state verification_requirement"      minimal_handoff_packet:        from_agent: "required"        to_agent: "required"        task: "required"        role_boundary: "required"        allowed_context: "required"        forbidden_context: "required"        allowed_action: "required_enum"        required_output: "required"        verification_requirement: "required"        stop_condition: "required"      kb_design_consequence:        - "TEMPLATES.md must contain the handoff_packet"        - "BEST_PRACTICES.md must say no free-form handoff is valid for machine action"        - "MISTAKES.md must list free_form_handoff as a recurring failure"        - "ESSENCE.md must define the agent's authority and non-authority boundaries"      informatics_design_consequence:        - "handoff fields must use canonical names across all agents"        - "payload fields must be reusable across strategy, detective, ops, and KB agents"      architecture_design_consequence:        - "handoff validation occurs before receiving-agent activation"        - "failed handoff routes to repair or escalation, not silent continuation"      target_for_future_agent_kbs: ["meta_strategy", "meta_detective"]
```

This is the shape I now understand you want Gemini to produce: **records that explain the causal source of the failure and exactly what the KB / informatics / architecture / guardrail layers must contain so the failure cannot repeat.**