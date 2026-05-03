# APPENDIX_KB_ANTI_DRIFT_EVIDENCE

## Purpose

- **Purpose:** Record the failure evidence and anti-drift controls that constrain the `special_ops__informatics_design` KB base.
- **Boundary:** This appendix is evidence and operating guidance for the agent KB. It is not a shared governance promotion packet.
- **Apex status:** Evidence rows constrain KB-base operation but do not authorize runtime/config mutation.

## Failure patterns

| failure_id | pattern | evidence_basis | drift_effect | countermeasure | scaffold_target |
|---|---|---|---|---|---|
| DRIFT-INF-001 | Mixed-purpose blob | Information design essence and audit sources identify blended concept/procedure/policy/reference/research content as a primary retrieval failure. | File loses primary function; retrieval returns noisy or ambiguous chunks. | Enforce one chunk / one job; split sections or files when roles compete. | `BEST_PRACTICES.md`, `MISTAKES.md` |
| DRIFT-INF-002 | Generic labels hide function | Semantic labeling appears as a top-ranked rule and audit check. | Agent must infer whether content is rule, evidence, template, question, or action. | Use function-bearing headings and typed bullets. | `BEST_PRACTICES.md`, `TEMPLATES.md` |
| DRIFT-INF-003 | Terminology synonym drift | Terminology sources warn against alternating names for the same concept. | Retrieval misses relevant material and agents reason over duplicate concepts. | Use one stable term per concept; mark provisional terms explicitly. | `BEST_PRACTICES.md`, `TEMPLATES.md` |
| DRIFT-INF-004 | Provisional idea hardened into law | Open-question sources explicitly preserve unresolved sentence limits, schema strength, prompt-template placement, and redundancy boundaries. | Weak evidence becomes accepted-looking doctrine. | Keep candidate/provisional status visible; route unresolved items to `LEARNING_QUEUE.md`. | `ESSENCE.md`, `LEARNING_QUEUE.md` |
| DRIFT-INF-005 | Evidence layer becomes governance finalization | Execution handover evidence warns not to create/finalize canon, terminology, taxonomy, audit, or AGENTS outputs in an evidence-layer run. | A KB-base task mutates broader system truth. | Keep scaffold as agent KB only; do not alter shared managed rules. | `MISTAKES.md` |
| DRIFT-INF-006 | Process docs treated as background | Failure postmortem evidence says process rules were cited but not enforced as gates. | The run appears compliant while violating source boundaries or target locks. | Convert source constraints into explicit gates and verify them before write/fetch-back. | `MISTAKES.md`, `TEMPLATES.md` |
| DRIFT-INF-007 | Scaffold absorbs deep evidence | Promptflow density gate says deep tables/comparisons belong in appendices. | Activation files become too long and stop being cold-start usable. | Keep appendices deep; scaffold files compact and navigational. | `ESSENCE.md`, `BEST_PRACTICES.md` |
| DRIFT-INF-008 | File type chosen by location or habit | Taxonomy sources define file type by function, not author, directory, or tool. | Files with similar names behave inconsistently and cannot be audited reliably. | Declare primary function and use templates that separate file classes. | `TEMPLATES.md` |

## Anti-drift controls

- **Control:** Use source indexes before drafting.
- **Control:** Write source manifest and ranking ledger before scaffold files.
- **Control:** Keep detailed source rows, comparisons, and evidence in appendices.
- **Control:** Keep open questions visibly unresolved.
- **Control:** Treat prompt/workflow sources as creation constraints only when they define staging for information-design artifacts.
- **Control:** Do not mutate shared governance, promotion authority, or accepted truth.
- **Control:** In Apex AI OS, keep KB-base guidance separate from runtime/config authority.
- **Control:** Fetch back written files and verify target repo/path boundary.

## Scaffold constraints derived from evidence

| scaffold | anti-drift constraint |
|---|---|
| `ESSENCE.md` | Must remain compression-only; no detailed tables or evidence rows. |
| `BEST_PRACTICES.md` | Must contain compact rules and pointers, not full source comparisons. |
| `MISTAKES.md` | Must hold reusable failure patterns and countermeasures, not raw postmortem detail. |
| `TEMPLATES.md` | Must provide reusable schemas and audit shapes, not become a second taxonomy/canon. |
| `LEARNING_QUEUE.md` | Must stay candidate-only; no entry may self-promote. |

## Verification notes

- **Status:** No blocking source conflict was found.
- **Risk:** The highest continuing risk is over-hardening provisional implementation choices into law.
- **Required handling:** Keep provisional items in `LEARNING_QUEUE.md` or appendices until separately validated.
- **Apex handling:** Treat this appendix as evidence for agent-KB behavior, not as release-pack approval.
