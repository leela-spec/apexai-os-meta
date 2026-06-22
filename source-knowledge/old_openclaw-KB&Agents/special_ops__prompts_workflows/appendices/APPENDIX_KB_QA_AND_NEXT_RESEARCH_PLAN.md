---
class: trace
role: AUDIT
surface: agent_kb_appendix
quality: reliable
scope: agent
purpose: capture Prompts Workflows KB gap analysis, F5 scaffold promotion candidates, and future improvement research backlog
dependencies: PROMPTFLOW_KB_BASE_BUILD.md | ESSENCE.md | Prompts&WorkflowsFuture.md | SOURCE_CONFLICT_REPORT.md
status: created
generated_at: 2026-05-04
owner: special_ops__prompts_workflows
validator: meta_ops
---

# APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN

## Purpose

This appendix records the bounded execution result for the Prompts Workflows KB after reviewing the current scaffold, appendices, and prior future-analysis artifact.

It answers three control questions:

1. Which appendices currently exist or are explicitly expected by the KB flow?
2. Which appendix or research content should be promoted into the F5 scaffold, and under what gate?
3. What future research and improvement work should be queued for the whole KB system?

## Scope lock

- **Working repo:** `leela-spec/MasterOfArts`
- **Target KB root:** `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/`
- **Target appendix root:** `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/`
- **F5 scaffold files:** `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md`, `LEARNING_QUEUE.md`
- **Execution boundary:** research and planning artifact only; no direct scaffold mutation in this pass

## User-intent versus executed-promptflow gap analysis

| Item | User intended task | Promptflow text / repo evidence | Gap | Disposition in this artifact |
|---|---|---|---|---|
| `GAP-PW-QA-001` | Identify all appendices. | Base build requires source manifest, ranking ledger, candidate ledger, anti-drift evidence, and conditional source conflict report before scaffold drafting. | Prior assistant only validated one guardrail promptflow file and did not inventory KB appendices. | Appendix inventory added below. |
| `GAP-PW-QA-002` | Understand what should be promoted into the F5 scaffold. | Scaffold must stay compact; detailed evidence belongs in appendices; learning queue is candidate-only. | Prior assistant did not map appendix/research material to scaffold targets. | F5 promotion matrix added below. |
| `GAP-PW-QA-003` | Research future improvements for the whole KB system. | Existing future analysis recommends QA/next research, source notes, examples, variant comparison, QA report, and YAML sidecars. | Prior assistant stopped after no-op validation instead of executing future-research synthesis. | Research backlog and patch candidates added below. |
| `GAP-PW-QA-004` | Execute in steps. | Base promptflow stages appendices before scaffold and ESSENCE last; future improvements are not automatic scaffold truth. | Prior assistant collapsed execution into a single no-op. | This artifact separates inventory, promotion candidates, research backlog, and next patch candidates. |

## Current appendix inventory

| Appendix / artifact | Status | Function | Current F5 relationship | Next action |
|---|---|---|---|---|
| `appendices/APPENDIX_KB_SOURCE_MANIFEST.md` | existing required appendix | Source provenance, coverage, duplication, gap risk, authority risk. | Supports all scaffold evidence references; should not be compressed into scaffold. | Keep as source database; later add source-notes companion. |
| `appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md` | existing required appendix | Ranked information units and recommended targets. | Supplies evidence for `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md`, and `ESSENCE.md`. | Keep as appendix; use only high-confidence deltas for scaffold promotion. |
| `appendices/APPENDIX_KB_CANDIDATE_LEDGER.md` | existing required appendix | Candidate entries before validation or promotion. | Feeds `LEARNING_QUEUE.md` and later scaffold updates. | Keep candidate-only; do not promote by placement. |
| `appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md` | existing required appendix | Failure evidence and countermeasure basis. | Feeds compact mistake and best-practice entries. | Mine only non-duplicate patterns into `MISTAKES.md` after validation. |
| `appendices/SOURCE_CONFLICT_REPORT.md` | existing conditional appendix | Resolved conflicts: patch/full-body/live-edit, stop-after-step vs closed promptflow, template-use vs governance authority. | Already reflected in scaffold doctrine and templates. | Consider adding a more formal patch/full-body/live-edit decision tree to `TEMPLATES.md`. |
| `appendices/Prompts&WorkflowsFuture.md` | existing future-analysis artifact | Gap transfer analysis from informatics-design and future improvement package. | Source for this QA/next-research plan. | Supersede operationally with this appendix; keep as historical/future-analysis source. |
| `appendices/PROMPTFLOW_PROMPTS_WORKFLOWS_BOUNDED_EXECUTION_GUARDRAILS.md` | existing guardrail promptflow | Bounded artifact-manufacturing contract for future promptflow iterations. | Supports `TEMPLATES.md` and `MISTAKES.md`; not itself scaffold doctrine except as pattern evidence. | Use as source for promptflow examples and regression tests. |
| `appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md` | created in this pass | Durable QA, gap, promotion-candidate, and research-backlog control artifact. | Does not mutate scaffold; nominates candidate updates. | Use as next patch-sequence controller. |

## F5 scaffold promotion matrix

| Candidate | Promote to | Promotion class | Evidence basis | Gate | Recommendation |
|---|---|---|---|---|---|
| `PW-PROMO-001` QA permanence rule: verification must be durable, not only chat-local. | `BEST_PRACTICES.md` | best practice | Future analysis says permanent QA artifact is missing; base build requires fetch-back verification. | MetaOps validation; avoid duplicating Hygiene QA authority. | Promote compact rule after validation. |
| `PW-PROMO-002` Completion proof failure: no-op or prior-summary completion is insufficient without current file evidence. | `MISTAKES.md` | mistake | Failure-analysis learning and this session's initial no-op mismatch. | Validate wording against existing `PW-MK` entries to avoid duplicate failure pattern. | Promote as new or merged mistake entry. |
| `PW-PROMO-003` Promptflow execution contract must distinguish user-intent task from current artifact contract. | `TEMPLATES.md` | template field / preflight check | User-intent gap in this session; guardrail promptflow requires explicit current phase and exact artifact. | Add only if not already covered by `PW-TPL-003` or `PW-TPL-004`. | Candidate for template update. |
| `PW-PROMO-004` Prompt/workflow examples are behavioral tests, not decorative appendix material. | `ESSENCE.md` or `BEST_PRACTICES.md` | essence note or best practice | Future analysis says examples/regression layer is core for this lane. | Operator approval because this elevates examples from optional appendix to core practice. | Strong candidate. |
| `PW-PROMO-005` Patch vs full-body vs live-edit decision tree. | `TEMPLATES.md` | template | Source conflict report already resolves the conflict contextually. | Validate decision tree against conflict report and current best practice `PW-BP-001`. | Promote as compact chooser template. |
| `PW-PROMO-006` Source notes prevent source-manifest overuse. | `BEST_PRACTICES.md` or appendix only | best practice / appendix structure | Future analysis recommends source notes as P1. | Create `APPENDIX_KB_SOURCE_NOTES.md` first; scaffold only gets a pointer if needed. | Create appendix before scaffold change. |
| `PW-PROMO-007` Template catalog sidecar improves machine querying. | `LEARNING_QUEUE.md` | candidate | Future analysis rates sidecars P2 and template catalog as most valuable sidecar for this lane. | Do not promote to accepted scaffold until sidecar schema is validated by Informatics Design / Knowledge Bank. | Queue as candidate, not scaffold now. |

## What should not be promoted directly

| Item | Reason | Correct handling |
|---|---|---|
| Audit severity model | Prompts Workflows does not own QA severity authority. | Route to Hygiene / QA surfaces. |
| Global file-type or sentence-level Markdown strictness | Informatics Design owns file semantics and global structure. | Consume future decisions as constraints, not local law. |
| KB placement or promotion approval authority | This lane owns prompt/workflow construction, not KB governance. | Route through Knowledge Bank / MetaOps promotion path. |
| Historical chat text from `Prompts&WorkflowsFuture.md` | It is useful evidence but not clean runtime doctrine. | Extract only bounded conclusions into this appendix and later candidates. |

## Current QA status

| Check | Status | Evidence / note |
|---|---|---|
| Repo boundary | pass | Current target remains `leela-spec/MasterOfArts`. |
| Target root boundary | pass | This artifact is under the Prompts Workflows appendix root. |
| F5 scaffold identified | pass | Base promptflow defines the five scaffold files. |
| Required appendix set identified | pass | Source manifest, ranking ledger, candidate ledger, anti-drift evidence, and source conflict report are accounted for. |
| Future improvement artifact found | pass | `Prompts&WorkflowsFuture.md` already contains a P1/P2 improvement package. |
| Scaffold mutation performed | not performed | This pass intentionally records promotion candidates rather than applying scaffold changes. |
| Open operator questions | none blocking this artifact | Future scaffold promotion still requires validation / operator approval where it changes accepted scaffold content. |

## Functional readiness assessment

| Area | Rating | Reason |
|---|---|---|
| Base scaffold | strong | F5 exists and is compact, navigational, and evidence-linked. |
| Appendix provenance | strong | Required provenance, ranking, candidate, evidence, and conflict appendices exist. |
| QA durability | weak-to-medium | Verification history exists, but durable QA/reporting was missing before this artifact. |
| Examples / regression tests | weak | No dedicated examples appendix exists yet. |
| Source-use guidance | medium | Source manifest exists; source-notes usage guidance is still missing. |
| Machine-readable readiness | medium | Markdown ledgers exist; YAML/JSON sidecars are still future work. |
| Cross-KB generalization | medium-high | Future analysis identifies shared KB-base conventions, but ownership and schema still need validation. |

## Research backlog

| ID | Research question | Priority | Owner suggestion | Output target | Why |
|---|---|---|---|---|---|
| `PW-RQ-001` | When does a prompt template become system knowledge instead of workflow tooling? | P1 | Prompts Workflows + Knowledge Bank | `APPENDIX_KB_VARIANT_COMPARISON.md` and possible `BEST_PRACTICES.md` update | Prevents templates from becoming hidden governance. |
| `PW-RQ-002` | What is the formal decision tree for patch vs full-body vs live-edit? | P1 | Prompts Workflows + Hygiene | `TEMPLATES.md` candidate and examples appendix | Operationalizes an already resolved conflict. |
| `PW-RQ-003` | What is the maximum safe promptflow file set before decomposition is required? | P1 | Prompts Workflows + MetaOps | `BEST_PRACTICES.md` or `TEMPLATES.md` candidate | Clarifies one-artifact-per-step vs closed promptflow execution. |
| `PW-RQ-004` | What regression examples best detect prompt drift? | P1 | Prompts Workflows + Hygiene | `APPENDIX_KB_EXAMPLES.md` | This lane needs behavioral test cases. |
| `PW-RQ-005` | Which source variants add new value versus duplicate phrasing? | P2 | Prompts Workflows + Informatics Design | `APPENDIX_KB_VARIANT_COMPARISON.md` | Prevents duplicate doctrine promotion. |
| `PW-RQ-006` | Should prompt templates have frontmatter metadata? | P2 | Informatics Design + Prompts Workflows | `APPENDIX_KB_TEMPLATE_CATALOG.yaml` candidate | Useful for machine query, but schema must not become bureaucracy. |
| `PW-RQ-007` | What belongs in promptflow skeletons versus Codex execution preflights? | P2 | Prompts Workflows + AI Handling/Routing | `TEMPLATES.md` candidate | Prevents planning/execution tool conflation. |
| `PW-RQ-008` | Should every Special Ops KB get QA plan, source notes, examples, sidecars, and attach-pack definitions? | P1 | Knowledge Bank + MetaOps | shared KB-base convention proposal | Whole-KB-system improvement pattern. |

## Next patch candidates

| Order | Candidate file / target | Action | Priority | Notes |
|---:|---|---|---|---|
| 1 | `appendices/APPENDIX_KB_EXAMPLES.md` | create | P1 | Highest practical value for this lane; examples act as regression tests. |
| 2 | `appendices/APPENDIX_KB_SOURCE_NOTES.md` | create | P1 | Add source-by-source use guidance without duplicating manifest. |
| 3 | `TEMPLATES.md` | update | P1 | Add patch/full-body/live-edit chooser only after examples/source notes are stable. |
| 4 | `MISTAKES.md` | update | P1 | Add or merge current-run failure pattern around completion-from-artifact mismatch. |
| 5 | `appendices/APPENDIX_KB_VARIANT_COMPARISON.md` | create | P2 | Compare source variants before deeper mining. |
| 6 | `appendices/APPENDIX_KB_TEMPLATE_CATALOG.yaml` | create | P2 | Machine-readable template catalog; validate schema first. |
| 7 | source/ranking/candidate YAML mirrors | create | P2 | Shared KB-system automation work, not required for this lane alone. |

## Recommended attach packs

| Use case | Attach pack |
|---|---|
| Runtime prompt/workflow construction | `ESSENCE.md`, `BEST_PRACTICES.md`, `TEMPLATES.md`, `MISTAKES.md`, and `SOURCE_CONFLICT_REPORT.md` if patch/full-body/live-edit choice matters. |
| New promptflow build or scaffold update | `PROMPTFLOW_KB_BASE_BUILD.md`, `APPENDIX_KB_SOURCE_MANIFEST.md`, `APPENDIX_KB_INFORMATION_RANKING_LEDGER.md`, `APPENDIX_KB_CANDIDATE_LEDGER.md`, `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`, `SOURCE_CONFLICT_REPORT.md`, and this appendix. |
| Future KB-system improvement research | this appendix, `Prompts&WorkflowsFuture.md`, `LEARNING_QUEUE.md`, and relevant peer KB QA/next-research appendices. |
| Drift/regression investigation | `MISTAKES.md`, `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`, `PROMPTFLOW_PROMPTS_WORKFLOWS_BOUNDED_EXECUTION_GUARDRAILS.md`, and future `APPENDIX_KB_EXAMPLES.md`. |

## Execution stop

This pass creates one durable appendix only.

No F5 scaffold file was edited in this pass because the scaffold promotion items above remain candidates until validation and, where required, operator approval.
