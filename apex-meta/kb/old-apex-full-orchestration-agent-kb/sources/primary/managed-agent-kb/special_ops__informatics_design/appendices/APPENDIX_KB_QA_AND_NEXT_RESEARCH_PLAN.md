# APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN

## Purpose

- **Purpose:** Record functional readiness, unresolved database candidates, research backlog, attach-pack guidance, and next research candidates for `special_ops__informatics_design`.
- **Scope:** `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__informatics_design/`.
- **Boundary:** This appendix is planning support for this agent KB. It does not mutate shared governance truth.

## Functional Readiness

| surface | readiness | notes |
|---|---|---|
| `ESSENCE.md` | strong | Activation, role boundary, operating priorities, stop conditions, and appendix read order are compact. |
| `BEST_PRACTICES.md` | strong | Captures compact information-design practices and candidate handling without absorbing appendix-level evidence. |
| `MISTAKES.md` | strong | Captures failure modes for scaffold bloat, file typing, provisional hardening, and stale TODOs. |
| `TEMPLATES.md` | strong | Provides reusable file, source, ranking, candidate, anti-drift, terminology, and audit templates. |
| `LEARNING_QUEUE.md` | good | Keeps unresolved/provisional items and now captures deferred database/source-notes/examples candidates. |
| `APPENDIX_KB_SOURCE_MANIFEST.md` | strong | Maintains source coverage and authority-risk boundaries. |
| `APPENDIX_KB_INFORMATION_RANKING_LEDGER.md` | strong | Continues to preserve ranking logic and scaffold/appendix placement. |
| `APPENDIX_KB_CANDIDATE_LEDGER.md` | strong | Preserves candidate IDs and records approved decisions/dispositions. |
| `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md` | strong | Maintains failure evidence and anti-drift controls. |
| `APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md` | good | Planning support surface; requires future update after subsequent research runs. |

## Missing Database Candidates

| candidate | status | why it matters | next action |
|---|---|---|---|
| `APPENDIX_KB_SOURCE_NOTES.md` or SN database | deferred | Could preserve detailed source notes if future agents need source-level replay. | Locate actual SN file or create bounded source-notes appendix only when needed. |
| JSON/YAML sidecars | deferred | Could improve automated querying beyond Markdown tables. | Add only if Markdown ledgers cause retrieval/query failures. |
| Separate QA report appendix | represented_here | Current QA and next-research plan is sufficient for this phase. | Split into `APPENDIX_KB_QA_REPORT.md` only if QA becomes large or recurring. |
| Examples appendix | deferred | Before/after transformations could help future agents apply templates. | Add 3-5 examples only if template misuse recurs. |
| Variant comparison appendix | deferred | Could preserve full Gemini/Perplexity variants for research replay. | Add only if source-conflict or variant-depth review becomes necessary. |

## Research Backlog

| id | question | impact | recommended_status | next_action |
|---|---|---:|---|---|
| RB-INF-001 | Should sentence-level strictness remain guidance or become procedure-only rule? | medium | candidate | Validate against repeated procedure-file failures. |
| RB-INF-002 | Should numeric limits ever be used, or only semantic checks? | medium | candidate | Keep provisional until evidence shows numeric gates improve execution. |
| RB-INF-003 | Should ledgers be mirrored as JSON/YAML for agent ingestion? | medium | deferred | Reopen after observing Markdown query failures. |
| RB-INF-004 | What is the minimal sidecar schema that helps without bureaucracy? | medium | deferred | Draft only with a concrete consuming workflow. |
| RB-INF-005 | Are prompt templates a governed file type, operational support asset, or prompts-workflows concern? | medium | candidate | Coordinate with prompts/workflows owner before hardening. |
| RB-INF-006 | When does a prompt template become system knowledge rather than workflow tooling? | medium | candidate | Treat as adjacent until evidence shows governance impact. |
| RB-INF-007 | Is plain-language file-type declaration enough? | medium | needs_validation | Audit future failures caused by inconsistent declaration patterns. |
| RB-INF-008 | Should governed files require frontmatter fields such as `class`, `role`, `surface`, `quality`, `scope`, `purpose`, and `dependencies`? | medium | candidate | Keep as future metadata question, not current KB law. |
| RB-INF-009 | How much repetition between scaffold and appendices is useful? | low-medium | needs_validation | Watch for contradiction drift or retrieval miss issues. |
| RB-INF-010 | When does reinforcement become contradiction risk? | low-medium | needs_validation | Use future maintenance evidence. |

## Recommended Attach Pack

| use case | attach/read pack |
|---|---|
| Runtime activation | `ESSENCE.md`, then `BEST_PRACTICES.md` if the task requires action. |
| Scaffold edit | `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md`, relevant appendix. |
| Candidate disposition | `APPENDIX_KB_CANDIDATE_LEDGER.md`, `LEARNING_QUEUE.md`, `TEMPLATES.md`, relevant source/ranking rows. |
| Research planning or audit | `APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md`, `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`, `TEMPLATES.md`. |
| Full rebuild or research replay | all scaffold files plus all appendices and `KB_SYSTEM_RELIABILITY_AUDIT_V1`. |

## Next Research Candidates

| candidate | status | trigger |
|---|---|---|
| `APPENDIX_KB_SOURCE_NOTES.md` | deferred | Create if source-note replay is needed and actual SN file is not found. |
| `APPENDIX_KB_EXAMPLES.md` | deferred | Create if agents misuse templates or need before/after examples. |
| JSON/YAML sidecars | deferred | Create only with explicit schema and consuming workflow. |
| Variant comparison appendix | deferred | Create only if future source conflicts require deeper replay. |

## Update log

| event | status | notes |
|---|---|---|
| QA/next research appendix creation | complete | This appendix resolves the approved `2Dos` best-next-step item. |
| Deferred database/source-note/example candidates | recorded | Deferred in `LEARNING_QUEUE.md` and this appendix. |

## Status

- **Status:** Next-research plan initialized.
- **Owner:** `special_ops__informatics_design`
- **Validator:** `special_ops__hygiene_clean`
