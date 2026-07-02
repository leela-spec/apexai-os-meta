---
class: trace
role: AUDIT
surface: agent_kb_appendix
quality: reliable
scope: agent
purpose: preserve anti-drift evidence and countermeasures for Special Ops AI Handling Routing
dependencies: APPENDIX_KB_SOURCE_MANIFEST.md | APPENDIX_KB_INFORMATION_RANKING_LEDGER.md
status: kb_base_built
owner: special_ops__ai_handling_routing
validator: meta_ops
---

# APPENDIX_KB_ANTI_DRIFT_EVIDENCE

## Purpose

- **Decision:** This appendix stores the detailed failure evidence behind the compact scaffold rules.
- **Constraint:** Scaffold files may summarize these risks but should not absorb the full evidence body.
- **Boundary:** Evidence here supports advisory routing, not runtime config mutation.

## Drift evidence ledger

| evidence_id | failure pattern | source basis | routing risk | countermeasure | scaffold target |
|---|---|---|---|---|---|
| AIHR-DRIFT-001 | Scope expansion before routing | `SingleGuide_Claude.md`; `WORKFLOW_BEST_PRACTICES_RESEARCH.md` | Agent accepts broad request and routes or executes without knowing target, non-goals, or deliverable. | State task and non-task; classify overload; route only after objective freeze. | `BEST_PRACTICES.md`; `MISTAKES.md` |
| AIHR-DRIFT-002 | Silent ambiguity resolution | `SingleGuide_Claude.md`; `SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md` | Agent guesses missing source, authority, or success criteria. | Name ambiguity; ask one focused question or mark `NEEDS_INPUT`. | `BEST_PRACTICES.md`; `TEMPLATES.md` |
| AIHR-DRIFT-003 | Source authority blur | `SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md` | Derived summaries, old chats, or speculative reasoning are treated as primary truth. | Choose authority tier before verification; prefer direct/current source over summary. | `BEST_PRACTICES.md`; `MISTAKES.md` |
| AIHR-DRIFT-004 | Verification theater | `SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md`; `WORKFLOW_BEST_PRACTICES_RESEARCH.md` | Fluent handoff or recommendation is accepted without evidence, diff, read-back, or source check. | Use explicit confidence states; no verification equals no approval. | `TEMPLATES.md`; `MISTAKES.md` |
| AIHR-DRIFT-005 | Prompt-flow work routed as repo execution without mode lock | `CODEX_RESILIENT_MIGRATION_PROCESS.md`; `CODEX_EXECUTION_INSTRUCTION_RELIABLE_REPRODUCED.md` | Browser-chat synthesis and repo write execution collapse into one ambiguous task. | Select execution surface and operation class; require repo-relative path and closed target set for repo execution. | `TEMPLATES.md`; `BEST_PRACTICES.md` |
| AIHR-DRIFT-006 | Rewrite reflex for bounded repair | `CODEX_RESILIENT_MIGRATION_PROCESS.md`; `WORKFLOW_BEST_PRACTICES_RESEARCH.md` | Agent routes a small fix into whole-file rewrite or broad cleanup. | Patch before rewrite; preserve untouched content; escalate if rewrite authority is required. | `MISTAKES.md` |
| AIHR-DRIFT-007 | Path drift | `CODEX_RESILIENT_MIGRATION_PROCESS.md`; `CODEX_EXECUTION_INSTRUCTION_RELIABLE_REPRODUCED.md` | Agent uses vague filename, guessed target, or Windows path as repo authority. | Use exact repo-relative path; stop on ambiguity. | `BEST_PRACTICES.md`; `TEMPLATES.md` |
| AIHR-DRIFT-008 | Premature handoff | `HARMONIZATION_RISK_REGISTER.md`; `SingleGuide_Claude.md` | Task is delegated before objective, source authority, constraints, and fallback posture are visible. | Require routing card fields before handoff. | `TEMPLATES.md`; `MISTAKES.md` |
| AIHR-DRIFT-009 | Completion illusion | `HARMONIZATION_RISK_REGISTER.md`; `SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md` | Existing artifact or scaffold presence is mistaken for verified completion. | Fetch back or inspect relevant current file; mark candidate vs accepted status. | `MISTAKES.md`; `BEST_PRACTICES.md` |
| AIHR-DRIFT-010 | Config authority overreach | current seed boundary; promptflow target lock | Advisory routing recommendation mutates or implies mutation of runtime config. | Stop for operator review whenever config or runtime authority is implicated. | `ESSENCE.md`; `MISTAKES.md`; `TEMPLATES.md` |
| AIHR-DRIFT-011 | Stale model/provider claim | source manifest gap check | Routing recommendation cites pricing, model capability, or provider availability without current verification. | Mark as `needs_current_verification` and verify live before use. | `BEST_PRACTICES.md`; `TEMPLATES.md` |

## Reusable stop conditions

- **Stop:** required source is missing.
- **Stop:** current authoritative file conflicts with summary or memory.
- **Stop:** target path, execution surface, or operation mode is ambiguous.
- **Stop:** task would require runtime config mutation.
- **Stop:** routing would create a new agent, new authority lane, or orchestration role.
- **Stop:** model/provider/cost claim is not currently verified and the decision depends on it.
- **Stop:** handoff lacks objective, target agent, source authority, success criteria, fallback posture, or review owner.

## Routing-risk checklist

| Check | Pass condition | Fail action |
|---|---|---|
| Objective bounded? | task, non-task, and deliverable are explicit | ask or mark `NEEDS_INPUT` |
| Authority named? | primary source or governing instruction is identified | stop or escalate |
| Execution surface clear? | browser/chat, repo execution, research, or review surface is explicit | ask or narrow |
| Operation class clear for repo work? | mode and target paths are declared | stop |
| Config impact present? | no, or operator review is explicitly required | stop for review |
| Current model claim needed? | verified current source exists | mark `needs_current_verification` |
| Handoff complete? | target, constraints, success criteria, fallback, validator included | reject or revise handoff |

## Evidence compression rule

- **Rule:** Keep this appendix as the evidence body.
- **Rule:** Scaffold files should contain the rule, template, or warning only.
- **Rule:** If a scaffold starts explaining a failure history in detail, move that detail back here.
