---
class: reference
role: SOURCE_NOTES
surface: agent_kb_appendix
quality: reliable
scope: agent
purpose: record source-by-source use guidance and anti-overuse boundaries for Prompts Workflows KB maintenance
dependencies: APPENDIX_KB_SOURCE_MANIFEST.md | APPENDIX_KB_INFORMATION_RANKING_LEDGER.md | APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md
status: candidate_patch
owner: special_ops__prompts_workflows
validator: meta_ops
---

# APPENDIX_KB_SOURCE_NOTES

## Purpose

This appendix explains how each source class should be used in future Prompts Workflows KB updates.

It does not replace `APPENDIX_KB_SOURCE_MANIFEST.md`. The manifest records provenance and coverage. This file records use guidance, reusable patterns, and anti-overuse boundaries.

## Use rule

- Use this file before mining sources for scaffold updates.
- Promote only compact, validated, non-duplicate findings into F5 scaffold files.
- Keep source-specific details in appendices unless they materially improve runtime prompt/workflow behavior.

## Source-note schema

| Field | Meaning |
|---|---|
| `source_id` | Source identifier from `APPENDIX_KB_SOURCE_MANIFEST.md`. |
| `use_as` | How future agents should use the source. |
| `strongest_reusable_pattern` | Highest-value pattern to reuse. |
| `do_not_overuse_as` | Boundary preventing source misuse. |
| `known_overlap` | Existing scaffold or appendix entry that already covers the same idea. |
| `best_runtime_pointer` | Best F5 or appendix file to cite when the pattern matters. |

## Source notes

| source_id | use_as | strongest_reusable_pattern | do_not_overuse_as | known_overlap | best_runtime_pointer |
|---|---|---|---|---|---|
| `SRC-PW-001` | primary index | Exact source-slice and target-lock discipline for KB-base builds. | Do not use as proof that unlisted sources may be searched. | Promptflow source-lock behavior in `TEMPLATES.md`. | `TEMPLATES.md`, `APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md` |
| `SRC-PW-002` | primary ranking ledger | Candidate prioritization by agent fit and evidence weight. | Do not promote ranking rows without overlap checks. | `APPENDIX_KB_INFORMATION_RANKING_LEDGER.md`. | `LEARNING_QUEUE.md`, ranking ledger |
| `SRC-PW-003` | primary inventory ledger | Duplicate and triage control for source corpus. | Do not treat inventory presence as acceptance. | Source manifest gap-risk register. | `APPENDIX_KB_SOURCE_MANIFEST.md` |
| `SRC-PW-004` | supporting candidate ledger | Compact doctrine candidate extraction. | Do not use candidate wording as accepted scaffold text by default. | `LEARNING_QUEUE.md` candidate-only boundary. | `LEARNING_QUEUE.md` |
| `SRC-PW-005` | evidence ledger | Failure and anti-drift safeguards. | Do not generalize one failure into universal doctrine without convergence. | `MISTAKES.md`, anti-drift appendix. | `MISTAKES.md`, `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md` |
| `SRC-PW-006` | primary prompt doctrine | Target, scope, authority, preservation, integrity, and stop-rule prompt structure. | Do not turn prompt-design guidance into global governance. | `PW-BP-002`, `PW-TPL-002`, `PW-TPL-003`. | `BEST_PRACTICES.md`, `TEMPLATES.md` |
| `SRC-PW-007` | primary workflow doctrine | Bounded execution, one deliverable, grounding, migration decision, verification. | Do not force one-deliverable rule when a closed promptflow file set is approved. | `SOURCE_CONFLICT_REPORT.md#PW-CONFLICT-002`, `PW-BP-003`. | `BEST_PRACTICES.md`, `TEMPLATES.md` |
| `SRC-PW-008` | workflow research synthesis | Evidence-weighted workflow tiers and workflow anti-patterns. | Do not duplicate broad workflow research in F5 scaffold. | `PW-BP-003`, `PW-MK-003`. | `APPENDIX_KB_INFORMATION_RANKING_LEDGER.md`, `BEST_PRACTICES.md` |
| `SRC-PW-009` | supporting research output | Candidate rule inventory and 80/20 work protocol. | Do not promote alternate phrasing when accepted doctrine already covers it. | `PW-LQ-002`. | `LEARNING_QUEUE.md` |
| `SRC-PW-010` | supporting prompt specimen | Frozen target frame and output contract for research prompts. | Do not treat specimen-specific sections as mandatory universal schema. | `PW-TPL-002`. | `TEMPLATES.md` |
| `SRC-PW-011` | supporting authority doctrine | Source authority, confidence, verification, stop/escalation wording. | Do not claim QA or escalation authority for this KB lane. | `PW-BP-004`, `PW-MK-002`, `PW-MK-004`. | `BEST_PRACTICES.md`, `MISTAKES.md` |
| `SRC-PW-012` | supporting repo execution doctrine | Bounded repo execution, path discipline, mode locks, review gates. | Do not copy Codex-specific execution details into general promptflow doctrine unless needed. | `PW-TPL-003`. | `TEMPLATES.md` |
| `SRC-PW-013` | supporting execution prompt | Out-of-mode improvement capture and closed creation policy. | Do not use improvement capture as permission to apply adjacent work. | `PW-BP-005`, `PW-MK-006`. | `BEST_PRACTICES.md`, `MISTAKES.md`, examples appendix |
| `SRC-PW-014` | supporting promptflow example | Source lock, contradiction matrix, manifest freeze, handoff staging. | Do not reopen broad harmonization architecture from a local KB update. | `PW-TPL-004`. | `TEMPLATES.md`, examples appendix |
| `SRC-PW-015` | supporting handoff example | Clean continuation with non-redesign, non-redo, exact next-job discipline. | Do not use as a general permission model for all agents. | `PW-BP-006`, `PW-TPL-005`. | `TEMPLATES.md`, examples appendix |

## Source-use decisions

- **Decision:** Source notes are use guidance, not source authority.
- **Decision:** Scaffold updates require overlap checks against accepted entries before promotion.
- **Decision:** If a source supplies only alternate wording for an accepted rule, keep it appendix-only or queue it for variant comparison.
- **Decision:** If a source supplies a new reusable structure, route it to `TEMPLATES.md` only after validation.

## Anti-overuse boundaries

| Risk | Boundary |
|---|---|
| Source manifest becomes scaffold substitute | Keep provenance in manifest and use guidance here; F5 gets only compact runtime rules. |
| Candidate wording becomes accepted doctrine | Route through `LEARNING_QUEUE.md` and promotion review. |
| Prompt examples become governance | Keep examples as behavioral tests and construction aids. |
| Codex execution rules overtake promptflow design | Keep executor-specific preflights separate from promptflow skeletons. |
| Duplicate workflow variants inflate scaffold | Use variant comparison before adding new accepted entries. |

## Recommended next use

Before any new F5 scaffold update:

1. identify source ids used;
2. check `known_overlap` above;
3. decide whether the value is a scaffold rule, template, mistake entry, appendix-only example, or learning queue candidate;
4. update only the minimal target file;
5. record evidence references.
