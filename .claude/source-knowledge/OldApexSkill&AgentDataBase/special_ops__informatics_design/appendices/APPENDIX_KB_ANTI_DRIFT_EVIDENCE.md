# APPENDIX_KB_ANTI_DRIFT_EVIDENCE

## Purpose

- **Purpose:** Record the failure evidence and anti-drift controls that constrain the `special_ops__informatics_design` KB base.
- **Boundary:** This appendix is evidence and operating guidance for the agent KB. It is not a shared governance promotion packet.

## Failure patterns

| failure_id | pattern | evidence_basis | drift_effect | countermeasure | scaffold_target |
|---|---|---|---|---|---|
| DRIFT-INF-001 | Mixed-purpose blob | Information design essence and audit sources identify blended concept/procedure/policy/reference/research content as a primary retrieval failure. | File loses primary function; retrieval returns noisy or ambiguous chunks. | Enforce one chunk / one job; split sections or files when roles compete. | `BEST_PRACTICES.md`, `MISTAKES.md` |
| DRIFT-INF-002 | Generic labels hide function | Semantic labeling appears as a top-ranked rule and audit check. | Agent must infer whether content is rule, evidence, template, question, or action. | Use function-bearing headings and typed bullets. | `BEST_PRACTICES.md`, `TEMPLATES.md` |
| DRIFT-INF-003 | Terminology synonym drift | Terminology sources warn against alternating names for the same concept. | Retrieval misses relevant material and agents reason over duplicate concepts. | Use one stable term per concept; mark provisional terms explicitly. | `BEST_PRACTICES.md`, `TEMPLATES.md` |
| DRIFT-INF-004 | Provisional idea hardened into law | Open-question sources explicitly preserve unresolved sentence limits, schema strength, prompt-template placement, and redundancy boundaries. | Weak evidence becomes accepted-looking doctrine. | Keep candidate/provisional status visible; route unresolved items to `LEARNING_QUEUE.md`. | `ESSENCE.md`, `LEARNING_QUEUE.md` |
| DRIFT-INF-005 | Evidence layer becomes governance finalization | Execution handover evidence warns not to create/finalize canon, terminology, taxonomy, audit, or AGENTS outputs in an evidence-layer run. | A KB-base task mutates broader system truth. | Keep scaffold as agent KB only; do not alter shared managed rules. | `MISTAKES.md` |
| DRIFT-INF-007 | Scaffold absorbs deep evidence | Promptflow density gate says deep tables/comparisons belong in appendices. | Activation files become too long and stop being cold-start usable. | Keep appendices deep; scaffold files compact and navigational. | `ESSENCE.md`, `BEST_PRACTICES.md` |
| DRIFT-INF-008 | File type chosen by location or habit | Taxonomy sources define file type by function, not author, directory, or tool. | Files with similar names behave inconsistently and cannot be audited reliably. | Declare primary function and use templates that separate file classes. | `TEMPLATES.md` |
| DRIFT-INF-009 | Candidate state becomes untraceable | Candidate movement without visible decision/status trail hides whether material is unresolved, integrated, rejected, or deferred. | Future agents cannot distinguish unresolved, integrated, rejected, or deferred material. | Record operator decision, status transition, target location, and deletion policy in candidate ledger. | `BEST_PRACTICES.md`, `TEMPLATES.md`, `APPENDIX_KB_CANDIDATE_LEDGER.md` |
| DRIFT-INF-010 | TODO remains active after disposition | Appendix update rule requires appendices to change when candidates are integrated, rejected, deferred, split, or resolved. | Old TODOs mislead future agents into reopening completed work. | Update TODO/status surfaces when approved. | `LEARNING_QUEUE.md`, `appendices/2Dos`, `APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md` |

## Anti-drift controls

- **Control:** Use source indexes before drafting.
- **Control:** Write or update source manifest and ranking/candidate ledgers before or alongside scaffold files.
- **Control:** Keep detailed source rows, comparisons, evidence, and research planning in appendices.
- **Control:** Keep open questions visibly unresolved.
- **Control:** Treat prompt/workflow sources as creation constraints only when they define staging for information-design artifacts.
- **Control:** Do not mutate shared governance, promotion authority, or accepted truth.
- **Control:** Require candidate decision table before candidate movement.
- **Control:** Prefer status transitions over candidate-row deletion.

## Scaffold constraints derived from evidence

| scaffold | anti-drift constraint |
|---|---|
| `ESSENCE.md` | Must remain compression-only; no detailed tables or evidence rows. |
| `BEST_PRACTICES.md` | Must contain compact rules, checks, and pointers, not full source comparisons. |
| `MISTAKES.md` | Must hold reusable failure patterns and countermeasures, not raw postmortem detail. |
| `TEMPLATES.md` | Must provide reusable schemas, not become a second taxonomy/canon. |
| `LEARNING_QUEUE.md` | Must stay candidate-only; no entry may self-promote. Deferred database candidates belong here. |
| `appendices/2Dos` | Must not keep resolved next steps framed as active future work. |

## Verification notes

- **Status:** No blocking source conflict was found.
- **Risk:** The highest continuing risk is over-hardening provisional implementation choices into law.
- **Required handling:** Keep provisional items in `LEARNING_QUEUE.md` or appendices until separately validated.
