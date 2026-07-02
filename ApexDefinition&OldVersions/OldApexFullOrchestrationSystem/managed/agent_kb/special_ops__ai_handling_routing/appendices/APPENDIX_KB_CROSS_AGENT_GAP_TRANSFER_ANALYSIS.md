---
class: trace
role: AUDIT
surface: agent_kb_appendix
quality: reliable
scope: agent
purpose: compare informatics-design KB gaps against AI Handling Routing and rank common versus agent-specific improvements
dependencies: APPENDIX_KB_QUALITY_IMPROVEMENT_ANALYSIS.md | APPENDIX_KB_SOURCE_MANIFEST.md | APPENDIX_KB_INFORMATION_RANKING_LEDGER.md | APPENDIX_KB_CANDIDATE_LEDGER.md | APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md | ESSENCE.md | BEST_PRACTICES.md | MISTAKES.md | TEMPLATES.md | LEARNING_QUEUE.md | INformaticsDesignValidation&FutureResearch.md
status: improvement_analysis
owner: special_ops__ai_handling_routing
validator: meta_ops
---

# APPENDIX_KB_CROSS_AGENT_GAP_TRANSFER_ANALYSIS

## Purpose

- **Decision:** This audit checks whether the gaps and future-research possibilities identified for `special_ops__informatics_design` also apply to `special_ops__ai_handling_routing`.
- **Decision:** The goal is to identify high-impact shared KB-system improvements and high-impact agent-specific improvements.
- **Constraint:** This analysis is not an applied patch and does not authorize runtime config, model registry, provider-policy, or all-agent orchestration changes.
- **Constraint:** Recommendations that add files or change accepted scaffolds require a later bounded patch pass.

## Source basis

- **Source:** `INformaticsDesignValidation&FutureResearch.md` — external comparison input containing informatics-design file list, database-pack recommendation, gaps, research questions, and next-step proposal.
- **Source:** `APPENDIX_KB_QUALITY_IMPROVEMENT_ANALYSIS.md` — existing AI Handling Routing quality analysis.
- **Source:** current AI Handling Routing scaffold and appendix files.

## Transfer verdict

- **Verdict:** most informatics-design gaps transfer to AI Handling Routing, but not with the same priority.
- **High transfer:** source-notes database, machine-readable sidecar, QA/next-research appendix, runtime examples, status vocabulary, read-budget profile, template chooser.
- **Partial transfer:** governed Markdown strictness, prompt-template placement, file-type declaration, redundancy discipline.
- **Low transfer:** full Gemini/Perplexity variant import as such; for this agent the equivalent is model/mode/provider/capability comparison with current-verification boundaries.
- **Critical AIHR-specific gap:** current model/provider/tool claims cannot be embedded as accepted doctrine without live verification and review.

## Gap transfer matrix

| Informatics finding/gap | Transfers to AI Handling Routing? | AIHR priority | Why | Best target |
|---|---|---:|---|---|
| No dedicated `SOURCE_NOTES` / SN database | Yes | P1 | AIHR depends heavily on knowing what each source can decide, cannot decide, and how stale it may be. A source-note layer would prevent source-authority blur and current-provider drift. | `appendices/APPENDIX_KB_SOURCE_NOTES.md` |
| No machine-readable sidecar | Yes | P1/P2 | Routing cards, states, stop conditions, and template schemas are highly machine-usable. A sidecar could improve automation, but must remain derivative of Markdown authority. | `appendices/APPENDIX_KB_MACHINE_READABLE_INDEX.md` first; optional YAML later |
| No explicit test/audit result file | Yes | P1 | Current AIHR has quality analysis but not a formal QA run artifact with test matrix, changed-file coverage, and closure state. | `appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md` |
| No source conflict report | Conditional | P3 now / P1 when conflict exists | No blocking conflict currently; create only if source conflict appears, especially around model/tool claims or advisory-vs-config authority. | `appendices/SOURCE_CONFLICT_REPORT.md` only if needed |
| No direct full variant import | Partial | P2 | The AIHR equivalent is not full Gemini/Perplexity informatics variants; it is comparison across Agent Mode, thinking mode, Deep Research, Codex/repo execution, connector execution, and current model/provider docs. | `appendices/APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md` |
| No runtime examples | Yes | P1 | AIHR is operationally about routing decisions; examples would strongly increase usability and reduce wrong-template selection. | `appendices/APPENDIX_KB_ROUTING_EXAMPLES.md` or `TEMPLATES.md` examples section |
| Governed Markdown strictness research | Partial | P3 | Useful only insofar as routing templates and handoff notes remain compact and unambiguous. Informatics owns the deeper doctrine. | `LEARNING_QUEUE.md` candidate only |
| Schema/database structure research | Yes | P1 | AIHR templates and route states are schema-like and would benefit from normalization. | `APPENDIX_KB_MACHINE_READABLE_INDEX.md`; later optional sidecars |
| Prompt-template placement research | Yes | P1 | AIHR has templates, but prompt-workflow ownership must remain separate. Need boundary between routing card, handoff template, and prompt cookbook. | `LEARNING_QUEUE.md`; cross-link to `special_ops__prompts_workflows` |
| File-type declaration research | Partial | P2 | Useful for KB consistency, especially appendices as trace/ledger/audit surfaces, but not central to AIHR decisions. | common KB standard |
| Redundancy discipline research | Yes | P2 | AIHR has intentional scaffold/appendix repetition. Needs clear reinforcement vs contradiction rule. | `ESSENCE.md`; `APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md` |

## AIHR-specific missing or underdeveloped elements

### AIHR-GAP-001 — Source notes with authority-scope windows

- **Finding:** Current source manifest lists sources and actual use, but does not include per-source `authority_scope`, `non_authority_scope`, `freshness_sensitivity`, and `route_use` fields.
- **Why high impact:** AIHR is a source-authority and routing agent; this is more important here than in informatics design.
- **Recommended artifact:** `appendices/APPENDIX_KB_SOURCE_NOTES.md`.
- **Minimal fields:** `source_id`, `source_path`, `authority_scope`, `not_authoritative_for`, `freshness_sensitivity`, `routing_use`, `known_gap`, `scaffold_refs`.
- **Priority:** P1.

### AIHR-GAP-002 — Formal QA and next research plan

- **Finding:** `APPENDIX_KB_QUALITY_IMPROVEMENT_ANALYSIS.md` exists, but it is an improvement audit rather than a formal QA + research-plan artifact.
- **Why high impact:** A formal QA plan gives later agents a durable status surface instead of requiring reconstruction from chat or commits.
- **Recommended artifact:** `appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md`.
- **Minimal sections:** `QA Status`, `Functional Readiness`, `Missing Database Candidates`, `Research Backlog`, `Recommended Attach Pack`, `Next Patch Candidates`, `Closure State`.
- **Priority:** P1.

### AIHR-GAP-003 — Runtime routing examples

- **Finding:** `TEMPLATES.md` provides schemas but not worked examples.
- **Why high impact:** This KB is used to choose routes. Examples reduce ambiguity faster than more doctrine.
- **Recommended artifact:** `appendices/APPENDIX_KB_ROUTING_EXAMPLES.md`.
- **Example set:**
  - simple browser-chat answer
  - current model/provider claim requiring web verification
  - repo write requiring exact path/mode/checks
  - config-impacting recommendation that stops for review
  - source-conflict case that escalates
  - premature handoff repaired into valid handoff
- **Priority:** P1.

### AIHR-GAP-004 — Mode/tool/provider variant comparison

- **Finding:** Current files mention route surfaces and current-verification requirements, but no compact comparison exists across mode/tool surfaces.
- **Why high impact:** AIHR's core job is mode/tool routing, so this is the closest equivalent to informatics-design variant comparison.
- **Recommended artifact:** `appendices/APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`.
- **Minimal comparison rows:** `browser_chat`, `deep_research`, `web_current_verification`, `repo_connector_write`, `Codex-style execution`, `manual_review`, `QA/audit`, `specialist_handoff`.
- **Required columns:** `use_when`, `do_not_use_when`, `required_inputs`, `stop_conditions`, `verification_needed`, `common_failure`.
- **Priority:** P1/P2.

### AIHR-GAP-005 — Machine-readable route index

- **Finding:** Templates are already YAML-like, but there is no machine-oriented index of states, templates, and stop conditions.
- **Why high impact:** AIHR's reusable units are route-state enums and decision-card schemas.
- **Recommended artifact:** start with Markdown table in `appendices/APPENDIX_KB_MACHINE_READABLE_INDEX.md`; later optional `.yaml` only if automation actually needs it.
- **Priority:** P2.

### AIHR-GAP-006 — Prompt-template ownership boundary

- **Finding:** AIHR owns routing cards and handoff notes, while `special_ops__prompts_workflows` owns prompt design and workflow prompting.
- **Why high impact:** Without a boundary, routing templates can become prompt cookbook content or vice versa.
- **Recommendation:** Add a learning-queue item and a short boundary rule: AIHR templates decide routing/handoff structure; prompts-workflows templates write executable prompt language.
- **Priority:** P1.

### AIHR-GAP-007 — Provider/currentness research lane

- **Finding:** The KB correctly excludes current model/provider/cost claims, but has no formal research lane for when those claims become necessary.
- **Why high impact:** Many real routing questions depend on current model capability, tool availability, price, latency, or policy.
- **Recommendation:** Add a candidate research plan for `current_model_provider_matrix`, explicitly requiring fresh sources and non-config authority.
- **Priority:** P1.

## Common high-impact improvements across both KB agents

| Common improvement | Applies to informatics? | Applies to AIHR? | Shared priority | Common implementation |
|---|---|---|---:|---|
| `APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md` | yes | yes | P1 | Standard post-run QA + research-plan appendix for every Special Ops KB. |
| `APPENDIX_KB_SOURCE_NOTES.md` | yes | yes | P1 | Lightweight per-source notes database, not full source copying. |
| `APPENDIX_KB_MACHINE_READABLE_INDEX.md` | yes | yes | P1/P2 | Markdown-first schema/index that can later generate YAML/JSON if needed. |
| `APPENDIX_KB_EXAMPLES.md` / examples appendix | yes | yes | P1/P2 | For informatics: before/after structure examples. For AIHR: routing card examples. |
| Status vocabulary normalization | yes | yes | P1 | Define `accepted_in_kb_base`, `candidate`, `needs_validation`, `deferred`, `runtime_authority_not_granted`. |
| Read-budget profiles | yes | yes | P2 | Define `activation`, `normal`, `risk`, and `audit` load paths. |
| Candidate-to-scaffold traceability | yes | yes | P2 | Add `realized_as` or `scaffold_refs` column. |
| Source-gap severity labels | yes | yes | P2 | Distinguish blocking gaps from non-blocking research debt. |
| Redundancy discipline | yes | yes | P2 | Preserve useful reinforcement; prevent scaffold/appendix contradiction. |
| Prompt-template ownership boundary | yes | stronger for AIHR | P1 for AIHR / P2 common | Cross-link AIHR and prompts-workflows ownership. |

## Individual high-impact improvement ranking for AIHR

| Rank | Improvement | Impact | Effort | Risk | Recommended action |
|---:|---|---:|---:|---:|---|
| 1 | Add `APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md` | very high | low | low | create next |
| 2 | Add `APPENDIX_KB_SOURCE_NOTES.md` | very high | medium | low | create after QA plan |
| 3 | Add routing examples appendix | very high | medium | low | create 5–6 worked examples |
| 4 | Add status vocabulary + read-budget profiles to `ESSENCE.md` | high | low | low | bounded patch |
| 5 | Add template chooser to `TEMPLATES.md` | high | low | low | bounded patch |
| 6 | Add mode/tool variant comparison appendix | high | medium | medium | create only with current boundaries and no provider claims unless verified |
| 7 | Add source-gap severity labels to source manifest | medium-high | low | low | bounded patch |
| 8 | Add candidate `realized_as` links | medium-high | medium | medium | patch candidate ledger carefully |
| 9 | Add machine-readable Markdown index | medium-high | medium | medium | create as Markdown first |
| 10 | Add optional YAML/JSON sidecars | high for automation, low now | medium | medium | defer until automation need is proven |

## Common KB-system patch sequence

### Common Patch 1 — QA/research plan standard

- **Target:** both KBs.
- **Artifact:** `appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md`.
- **Reason:** Gives every KB a durable readiness and next-research status.
- **Priority:** P1.

### Common Patch 2 — Source notes standard

- **Target:** both KBs.
- **Artifact:** `appendices/APPENDIX_KB_SOURCE_NOTES.md`.
- **Reason:** Bridges between raw source manifest and extracted ranking ledger without copying full sources.
- **Priority:** P1.

### Common Patch 3 — Activation/read-budget normalization

- **Target:** `ESSENCE.md` in both KBs.
- **Changes:** status vocabulary, read-budget profiles, KB map.
- **Reason:** Highest token-efficiency gain per edit.
- **Priority:** P1/P2.

### Common Patch 4 — Examples appendix

- **Target:** both KBs, content differs by agent.
- **Artifact:** informatics gets structure examples; AIHR gets routing examples.
- **Reason:** Examples are compact operational tests.
- **Priority:** P2.

### Common Patch 5 — Machine-readable index

- **Target:** both KBs.
- **Artifact:** Markdown-first machine-readable index.
- **Reason:** Enables future automation without adding sidecar complexity too early.
- **Priority:** P2.

## AIHR-specific research backlog

A. **Current model/tool/provider verification**

1. What sources should be accepted for current model/provider/cost/capability claims?
2. What freshness window is required for routing-critical claims: same day, 30 days, or source-specific?
3. How should the KB phrase model-specific recommendations without becoming a stale model registry?

B. **Mode/tool routing taxonomy**

4. What is the canonical difference between browser-chat reasoning, Deep Research, repo connector execution, Codex-style execution, and manual review?
5. Which tasks are categorically unsafe for one-pass execution?
6. Which tasks must always include post-write or fetch-back verification?

C. **Prompt-template boundary**

7. When is a routing card an AIHR template versus a prompts-workflows template?
8. Should AIHR provide handoff shape only, while prompts-workflows provides full prompt language?

D. **Handoff and escalation semantics**

9. What fields are mandatory before delegating to another agent or tool?
10. When should a route be rejected rather than clarified?
11. How should `needs_input`, `manual_review`, `escalate`, and `refuse` differ in downstream behavior?

E. **Database and sidecar structure**

12. Which KB tables deserve normalized machine-readable exports?
13. Is Markdown table structure sufficient for current agents, or do future agents need YAML/JSON ingestion?
14. Should sidecars be generated artifacts rather than hand-authored truth surfaces?

## Do-not-apply findings

- **Do not:** import full provider/model rankings into accepted scaffold without current verification.
- **Do not:** let AIHR own prompt cookbook content that belongs to `special_ops__prompts_workflows`.
- **Do not:** let examples become hidden runtime authority.
- **Do not:** create a source conflict report when no material conflict exists.
- **Do not:** replace appendices with sidecars; sidecars should be derivative if added.
- **Do not:** expand this KB into all-agent orchestration law.

## Final recommendation

- **Recommendation:** Apply the informatics-design gap set to AIHR selectively, not mechanically.
- **Recommendation:** Treat `SOURCE_NOTES`, QA/research plan, routing examples, status vocabulary, and template chooser as the highest-impact next work.
- **Recommendation:** Defer YAML/JSON sidecars until automation need exists; use Markdown-first machine-readable indexes now.
- **Recommendation:** Treat current model/provider research as a separate validation-gated research lane, not as accepted KB scaffold content.
