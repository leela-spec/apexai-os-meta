# APPENDIX_KB_CANDIDATE_LEDGER

## Purpose

- **Purpose:** Preserve candidate-level information-design units before compact scaffold extraction.
- **Boundary:** Candidate rows are not promoted doctrine. They are reusable KB-base material with explicit target placement.

## Candidate rows

| candidate_id | source_candidate | candidate_summary | target_file | status | validation_pair | notes |
|---|---|---|---|---|---|---|
| CAND-INF-001 | KB-INFORMATICS-DESIGN-017 | Keep unresolved design issues visibly provisional instead of hardening them into default law. | `ESSENCE.md`, `LEARNING_QUEUE.md` | integrated_into_scaffold | special_ops__informatics_design + special_ops__hygiene_clean | Provisional-boundary rule represented in `ESSENCE.md`; unresolved variants remain in `LEARNING_QUEUE.md`. |
| CAND-INF-002 | KB-INFORMATICS-DESIGN-045 / 032 | Audit all governed files for self-contained chunks, semantic labels, terminology consistency, structural-boundary preservation, and mixed-purpose drift. | `BEST_PRACTICES.md`, `TEMPLATES.md` | integrated_into_scaffold | special_ops__informatics_design + special_ops__hygiene_clean | Audit checks and decision/proof templates represented in scaffold. |
| CAND-INF-003 | KB-INFORMATICS-DESIGN-048 / 063 | Declare file type by function; distinguish canon, terminology, taxonomy, audit, policy, procedure, concept, reference, research note, summary, handoff, and memory/index roles. | `BEST_PRACTICES.md`, `TEMPLATES.md` | integrated_into_scaffold | special_ops__informatics_design + special_ops__hygiene_clean | Function-based file choice retained as scaffold rule; full taxonomy evidence remains appendix-level. |
| CAND-INF-004 | KB-INFORMATICS-DESIGN-050 / 067 | Optimize in order: retrieval/context efficiency, ambiguity reduction, handoff reliability, maintainability, aesthetics. | `ESSENCE.md`, `BEST_PRACTICES.md` | integrated_into_scaffold | special_ops__informatics_design + special_ops__hygiene_clean | Operating priorities preserved in activation and practice layer. |
| CAND-INF-005 | KB-INFORMATICS-DESIGN-054 / 070 | Stabilize core vocabulary and prevent synonym drift: one concept keeps one name; provisional terms stay marked. | `BEST_PRACTICES.md`, `TEMPLATES.md` | integrated_into_scaffold | special_ops__informatics_design + special_ops__hygiene_clean | Terminology stability remains scaffold rule and template support. |
| CAND-INF-006 | KB-INFORMATICS-DESIGN-009 / 010 | Evidence-layer and KB-base runs must not drift into governance finalization or accepted-truth mutation. | `MISTAKES.md`, `LEARNING_QUEUE.md` | integrated_into_scaffold | special_ops__informatics_design + special_ops__hygiene_clean | Anti-drift failures and non-promotion boundaries represented in scaffold. |
| CAND-INF-007 | KB-CODEX-EXECUTION-PROCESS-071 / 072 | Referenced process rules must function as active gates, not decorative background context. | `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md` | integrated_into_scaffold | meta_ops + special_ops__prompts_workflows | Integrated only where it constrains information-design artifact creation and proof. |
| CAND-INF-008 | LIMITED_AGENT_STYLE_GUIDE | Use typed bullets, explicit dependencies, and bounded sections for limited-context agent usability. | `BEST_PRACTICES.md`, `TEMPLATES.md` | integrated_into_scaffold | special_ops__informatics_design + special_ops__hygiene_clean | Style-supporting, not standalone governance. |
| CAND-INF-009 | ROLE_AND_KB_TARGET_MAP | Informatics Design owns structure, functional labels, terminology stability, retrieval clarity, and cold-start usability; it does not own content validation, strategic direction, or promotion approval. | `ESSENCE.md` | integrated_into_scaffold | special_ops__informatics_design + special_ops__hygiene_clean | Agent boundary anchor preserved. |
| CAND-INF-010 | Promptflow.md | Terminology and audit artifact creation should use staged prompts only as creation constraints, not as hidden runtime law. | `LEARNING_QUEUE.md`, appendices | deferred | special_ops__prompts_workflows + meta_ops | Adjacent constraint remains provisional/deferred; not hardened as runtime law. |
| CAND-INF-011 | KB_SYSTEM_RELIABILITY_AUDIT_V1 | Add hard execution contracts, path/diff-based proof, changed-file-set reporting, and no prior-summary completion claims. | `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md`, `appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md` | integrated_into_scaffold | special_ops__informatics_design + special_ops__hygiene_clean | Integrated as machine-executable KB-base contract and proof templates. |
| CAND-INF-012 | appendices/2Dos | Create QA and next research plan appendix for fetch-back, readiness, database candidates, research backlog, attach packs, and next patch candidates. | `appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md` | resolved | special_ops__informatics_design + special_ops__hygiene_clean | Resolved by creating the QA/next research appendix; future optional files remain deferred. |

## Candidate decision record

| candidate_id/source | recommendation | operator_decision | disposition |
|---|---|---|---|
| CAND-INF-001 | split_between_scaffold_and_appendix | approved | Scaffold provisional boundary + learning queue retention. |
| CAND-INF-002 | integrate_into_scaffold | approved | Integrated into audit practices and templates. |
| CAND-INF-003 | split_between_scaffold_and_appendix | approved | Scaffold function-typing rule + appendix evidence retention. |
| CAND-INF-004 | integrate_into_scaffold | approved | Integrated as operating priorities. |
| CAND-INF-005 | integrate_into_scaffold | approved | Integrated as terminology stability practice/template. |
| CAND-INF-006 | integrate_into_scaffold | approved | Integrated as anti-governance-drift failure rule. |
| CAND-INF-007 | split_between_scaffold_and_appendix | approved | Integrated as active-gate execution rule and retained as drift evidence. |
| CAND-INF-008 | integrate_into_scaffold | approved | Integrated as typed-bullet/template practice. |
| CAND-INF-009 | integrate_into_scaffold | approved | Integrated as agent boundary. |
| CAND-INF-010 | keep_as_candidate | approved | Retained as deferred/provisional adjacent promptflow issue. |
| KB_SYSTEM_RELIABILITY_AUDIT_V1 | needs_operator_decision | approved | Integrated as hard execution-contract layer. |
| appendices/2Dos QA plan | integrate_into_appendix | approved | Resolved by new QA/next research appendix. |
| appendices/2Dos source notes | needs_operator_decision | approved | Deferred in learning queue and QA appendix. |
| appendices/2Dos sidecars | keep_as_candidate | approved | Deferred in learning queue and QA appendix. |
| appendices/2Dos examples | defer | approved | Deferred in learning queue and QA appendix. |

## Candidate placement rules

- **ESSENCE.md:** only compression, boundary, activation rules, and compact execution contract gates.
- **BEST_PRACTICES.md:** reusable operating rules with appendix pointers.
- **MISTAKES.md:** failure patterns that the agent must recognize and counteract.
- **TEMPLATES.md:** schemas, tables, and reusable file/audit/terminology/proof shapes.
- **LEARNING_QUEUE.md:** unresolved, deferred, adjacent, or promotion-dependent candidates only.
- **Appendices:** detailed source comparisons, ledgers, evidence, QA status, and next research planning.

## Candidate status notes

- **integrated_into_scaffold:** candidate has a compact scaffold representation and remains traceable here.
- **represented_in_appendix:** candidate is retained as evidence, variant, or planning material without scaffold doctrine.
- **resolved:** appendix TODO or candidate has been dispositioned by a concrete target update.
- **deferred:** useful but not currently integrated; retained for later validation.
- **candidate:** useful but narrower, adjacent, or requiring more validation.
- **provisional-boundary:** should be visible but not normalized into hard law.

## Deletion policy

- **Decision:** No candidate rows were deleted in this update.
- **Reason:** Status transition preserves traceability better than hard deletion for this appendix design.
