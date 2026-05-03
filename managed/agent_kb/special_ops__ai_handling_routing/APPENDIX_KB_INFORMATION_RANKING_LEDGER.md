---
class: trace
role: LEDGER
surface: agent_kb_appendix
quality: reliable
scope: agent
purpose: record candidate routing knowledge before validation or promotion
dependencies: APPENDIX_KB_INFORMATION_RANKING_LEDGER.md | LEARNING_QUEUE.md
status: kb_base_built
owner: special_ops__ai_handling_routing
validator: meta_ops
---

# APPENDIX_KB_CANDIDATE_LEDGER

## Purpose

- **Decision:** This ledger records candidate entries surfaced during KB-base construction.
- **Constraint:** Candidate rows are not accepted truth and do not authorize runtime config changes.
- **Promotion route:** Candidate material must pass through `LEARNING_QUEUE.md`, `meta_ops` validation, and the governed promotion path before becoming accepted scaffold doctrine.

## Candidate ledger

| candidate_id | candidate_summary | source_basis | proposed_target | validation_need | risk_if_unvalidated | status |
|---|---|---|---|---|---|---|
| AIHR-CAND-001 | Add a compact source-authority routing card for deciding whether the user prompt, repo file, external doc, or agent memory controls. | `SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md` | `TEMPLATES.md` | Validate with `meta_ops` against current handoff contract. | Authority blur; wrong-source routing. | promoted_to_scaffold_as_template |
| AIHR-CAND-002 | Add an overload classifier: one-pass safe, decomposition needed, unsafe in one pass. | `WORKFLOW_BEST_PRACTICES_RESEARCH.md` | `BEST_PRACTICES.md` / `TEMPLATES.md` | Validate threshold examples with active agent lanes. | Multi-objective prompts routed as one broad task. | promoted_to_scaffold_as_rule_and_template |
| AIHR-CAND-003 | Add a repo-execution router that separates browser-chat advisory work from Codex-style repo execution. | `CODEX_RESILIENT_MIGRATION_PROCESS.md`; `CODEX_EXECUTION_INSTRUCTION_RELIABLE_REPRODUCED.md` | `TEMPLATES.md` | Validate with `special_ops__prompts_workflows` if later turned into a reusable prompt. | Prompt-flow work becomes direct repo execution without mode lock. | promoted_to_scaffold_as_template |
| AIHR-CAND-004 | Add a model/tool fit note that avoids current provider claims unless verified live. | promptflow target lock; source manifest gap check | `BEST_PRACTICES.md` | Validate against future current-model evidence source before any specific model recommendation. | Stale model/provider routing claims. | promoted_to_scaffold_as_boundary_rule |
| AIHR-CAND-005 | Add config-impact manual-review stop rule. | current seed boundary; promptflow target lock | `ESSENCE.md` / `MISTAKES.md` | Already aligned to seed; validate no config text authorizes mutation. | Advisory agent becomes config authority. | promoted_to_scaffold_as_boundary_and_mistake |
| AIHR-CAND-006 | Add a failure pattern for premature handoff when a task lacks objective, source authority, or success criteria. | `SingleGuide_Claude.md`; `HARMONIZATION_RISK_REGISTER.md` | `MISTAKES.md` | Validate example wording against handoff contract. | Specialists receive ambiguous or unactionable work. | promoted_to_scaffold_as_mistake |
| AIHR-CAND-007 | Add a fallback posture field to every material routing recommendation. | current seed boundary; handoff contract snippet | `TEMPLATES.md` | Validate exact field names with process surface when needed. | Route has no recovery path when first choice fails. | promoted_to_scaffold_as_template_field |
| AIHR-CAND-008 | Keep detailed evidence and source notes in appendices rather than scaffolds. | promptflow architecture lock | appendices | Verify scaffold density gate after write. | Scaffold bloat; low activation speed. | applied_as_architecture_rule |

## Deferred candidates

| candidate_id | candidate_summary | reason_deferred | required future evidence | status |
|---|---|---|---|---|
| AIHR-DEFER-001 | Current model/provider cost-quality matrix. | Requires live/current provider data and may change quickly. | Current verified model/provider source and operator approval. | deferred |
| AIHR-DEFER-002 | Automated config-routing policy. | Outside this advisory lane and may touch runtime config authority. | Separate governance/config authority and operator review. | deferred |
| AIHR-DEFER-003 | New agent creation or domain-master routing scheme. | Outside first-wave agent set and all-agent orchestration authority. | Meta-governance approval and role-boundary review. | deferred |

## Promotion constraints

- **Constraint:** No candidate self-promotes from this appendix.
- **Constraint:** No candidate modifies `openclaw.json` or a runtime model registry.
- **Constraint:** No candidate creates new first-wave agent roles.
- **Constraint:** Provider/model-specific claims must be marked `needs_current_verification` unless verified in the current run.
