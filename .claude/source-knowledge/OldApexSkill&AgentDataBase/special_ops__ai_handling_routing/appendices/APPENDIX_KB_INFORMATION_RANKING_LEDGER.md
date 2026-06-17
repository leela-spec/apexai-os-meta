---
class: trace
role: LEDGER
surface: agent_kb_appendix
quality: reliable
scope: agent
purpose: rank information units extracted for Special Ops AI Handling Routing KB base construction
dependencies: APPENDIX_KB_SOURCE_MANIFEST.md
status: kb_base_built
owner: special_ops__ai_handling_routing
validator: meta_ops
---

# APPENDIX_KB_INFORMATION_RANKING_LEDGER

## Purpose

- **Decision:** This ledger maps extracted information units to scaffold placement.
- **Constraint:** Rows are KB-construction guidance, not runtime config authority.
- **Scoring scale:** `agent_relevance`, `actionability`, `evidence_strength`, `reuse_frequency_likelihood`, and `drift_risk` use `1` low to `5` high.

## Ranking ledger

| info_id | source_path | source_role | source_section_or_candidate_id | information_unit | agent_relevance | actionability | evidence_strength | reuse_frequency_likelihood | drift_risk | recommended_target_file | appendix_pointer | scaffold_summary_needed | status |
|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|---|---|
| AIHR-INFO-001 | `SingleGuide_Claude.md` | primary | Task framing / hard limits | State what the task is and is not before routing or output. | 5 | 5 | 5 | 5 | 3 | `BEST_PRACTICES.md` | manifest/source-slice | yes | accepted_for_scaffold |
| AIHR-INFO-002 | `SingleGuide_Claude.md` | primary | Ambiguity handling | Name ambiguity and ask one focused question when material routing information is missing. | 5 | 5 | 5 | 5 | 4 | `BEST_PRACTICES.md` | manifest/source-slice | yes | accepted_for_scaffold |
| AIHR-INFO-003 | `SingleGuide_Claude.md` | primary | Module references | Load specialized modules only when the task requires that domain. | 5 | 4 | 5 | 4 | 3 | `BEST_PRACTICES.md` | manifest/source-slice | yes | accepted_for_scaffold |
| AIHR-INFO-004 | `SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md` | primary | Source tiers | Decide source authority before deciding whether output is verified. | 5 | 5 | 5 | 5 | 4 | `BEST_PRACTICES.md` | anti-drift/source-authority | yes | accepted_for_scaffold |
| AIHR-INFO-005 | `SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md` | primary | Confidence tiers / escalation states | Use `VERIFIED`, `PROBABLE`, `WEAK`, `UNSAFE`, `NEEDS_INPUT`, `ESCALATE`, and `REFUSE` as routing states when uncertainty matters. | 5 | 5 | 5 | 5 | 3 | `TEMPLATES.md` | templates/confidence-routing-card | yes | accepted_for_scaffold |
| AIHR-INFO-006 | `SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md` | primary | Stop conditions | Stop when required sources are missing, primary sources conflict, or output confidence is unsafe. | 5 | 5 | 5 | 5 | 5 | `MISTAKES.md` | anti-drift/stop-conditions | yes | accepted_for_scaffold |
| AIHR-INFO-007 | `CODEX_RESILIENT_MIGRATION_PROCESS.md` | supporting | Execution mode lock | Route repo work by declared mode such as `MOVE_ONLY`, `CREATE_ONLY`, `PATCH_PATHS_ONLY`, `CONTENT_DRAFT_ONLY`, or `VALIDATE_ONLY`. | 4 | 5 | 5 | 4 | 4 | `TEMPLATES.md` | templates/repo-execution-router | yes | accepted_for_scaffold |
| AIHR-INFO-008 | `CODEX_RESILIENT_MIGRATION_PROCESS.md` | supporting | Path discipline | Use exact repo-relative paths; stop on ambiguity instead of guessing. | 5 | 5 | 5 | 4 | 5 | `BEST_PRACTICES.md` | anti-drift/path-drift | yes | accepted_for_scaffold |
| AIHR-INFO-009 | `CODEX_EXECUTION_INSTRUCTION_RELIABLE_REPRODUCED.md` | supporting | Authority order | Frozen task brief outranks research notes for repo execution. | 4 | 5 | 5 | 4 | 4 | `BEST_PRACTICES.md` | anti-drift/authority-blur | yes | accepted_for_scaffold |
| AIHR-INFO-010 | `CODEX_EXECUTION_INSTRUCTION_RELIABLE_REPRODUCED.md` | supporting | One-file-at-a-time rule | Large repo work should route as one declared file or one declared operation at a time. | 4 | 5 | 5 | 4 | 4 | `BEST_PRACTICES.md` | anti-drift/overload | yes | accepted_for_scaffold |
| AIHR-INFO-011 | `LIMITED_AGENT_STYLE_GUIDE.md` | supporting | Escalate instead of guessing | Escalate when class, role, surface, truth-change, or full governance behavior is unclear. | 4 | 4 | 4 | 4 | 3 | `MISTAKES.md` | anti-drift/surface-unclear | yes | accepted_for_scaffold |
| AIHR-INFO-012 | `WORKFLOW_BEST_PRACTICES_RESEARCH.md` | supporting | Overload classification | Classify prompts as safe in one pass, needing decomposition, or unsafe in one pass before execution. | 5 | 5 | 5 | 5 | 4 | `BEST_PRACTICES.md` | templates/routing-decision-card | yes | accepted_for_scaffold |
| AIHR-INFO-013 | `WORKFLOW_BEST_PRACTICES_RESEARCH.md` | supporting | Patch before rewrite | Route bounded repairs to patch/update discipline; broad rewrite needs explicit authority. | 4 | 5 | 5 | 4 | 4 | `MISTAKES.md` | anti-drift/rewrite-reflex | yes | accepted_for_scaffold |
| AIHR-INFO-014 | `HARMONIZATION_RISK_REGISTER.md` | evidence | RSK-01 / RSK-03 / RSK-05 | Stage confusion, authority drift, and premature handoff are routing risks. | 4 | 4 | 4 | 4 | 5 | `MISTAKES.md` | anti-drift/risk-register | yes | accepted_for_scaffold |
| AIHR-INFO-015 | `special_ops__ai_handling_routing.md` seed | current seed | Failure safeguards | AI Handling Routing is advisory only and must not mutate `openclaw.json`. | 5 | 5 | 5 | 5 | 5 | `ESSENCE.md` | manifest/current-seed-boundary | yes | accepted_for_scaffold |

## Scaffold placement summary

| Target file | Information units |
|---|---|
| `ESSENCE.md` | lane identity, owns/does-not-own, advisory-only boundary, config-review stop |
| `BEST_PRACTICES.md` | task framing, ambiguity routing, source authority, module selection, repo-path discipline, overload classification |
| `MISTAKES.md` | scope drift, authority blur, unsafe source gaps, rewrite reflex, premature handoff, config-authority overreach |
| `TEMPLATES.md` | routing decision card, source authority card, model/tool fit card, repo execution router, handoff note |
| `LEARNING_QUEUE.md` | candidate-only future improvements requiring validation |

## Non-scaffolded material

- **Excluded:** live provider pricing, current model rankings, or API performance claims, because they require current verification and are unstable.
- **Excluded:** direct config mutation instructions, because this lane is advisory only.
- **Excluded:** broad all-agent orchestration doctrine, because this lane does not own orchestration authority.
