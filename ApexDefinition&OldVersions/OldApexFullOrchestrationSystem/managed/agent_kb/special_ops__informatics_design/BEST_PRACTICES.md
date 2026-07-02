# BEST_PRACTICES

## Purpose

Compact operating practices for `special_ops__informatics_design`.

This file is scaffold guidance. Detailed evidence lives in appendices.

## Source appendices

- `appendices/APPENDIX_KB_SOURCE_MANIFEST.md`
- `appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md`
- `appendices/APPENDIX_KB_CANDIDATE_LEDGER.md`
- `appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`

## Core practices

- **Practice:** Write information as small, self-contained, explicitly labeled, function-typed units.
- **Practice:** Keep one chunk to one job; split when a section is doing rule, evidence, question, and template work at once.
- **Practice:** Use function-bearing headings and typed bullets so retrieved chunks remain understandable without surrounding context.
- **Practice:** Keep terminology stable across a file pack; one concept should keep one name.
- **Practice:** Keep repeated file classes structurally similar enough for fast audit and cold-start reuse.
- **Practice:** Type files and sections by function, not by author, tool, location, or prose habit.
- **Practice:** Preserve structural boundaries: do not cut through tables, lists, procedures, or meaning-bearing sections.
- **Practice:** Use index-detail layering when an overview would otherwise absorb too much detail.
- **Practice:** Keep unresolved or weakly evidenced design choices visibly provisional.
- **Practice:** Prefer retrieval clarity, ambiguity reduction, handoff reliability, and maintainability over aesthetic prose.

## File-design defaults

| design object | default rule | appendix basis |
|---|---|---|
| chunk | self-contained and locally interpretable | `APPENDIX_KB_INFORMATION_RANKING_LEDGER.md` |
| heading | function-bearing, not decorative | `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md` |
| terminology | stable name per concept | `APPENDIX_KB_CANDIDATE_LEDGER.md` |
| file type | declared by function | `APPENDIX_KB_CANDIDATE_LEDGER.md` |
| scaffold | compact activation and navigation only | `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md` |
| appendix | deep evidence, variants, ledgers, tables | `APPENDIX_KB_SOURCE_MANIFEST.md` |

## Audit questions before accepting a structure

- **Check:** Can each major chunk be understood if retrieved alone?
- **Check:** Does each heading say what the section does?
- **Check:** Is the file's primary function visible near the top?
- **Check:** Are evidence, decisions, questions, and templates separated?
- **Check:** Are provisional items marked as provisional?
- **Check:** Are detailed ledgers and comparisons kept in appendices instead of scaffold files?
- **Check:** Does every integrated or resolved candidate retain traceability to its source, decision, and target location?

## Candidate handling practices

- **Rule:** Strong candidates may be integrated only after an explicit operator decision or predeclared approval rule.
- **Rule:** Appendix rows should normally transition status rather than disappear.
- **Rule:** Use `integrated_into_scaffold`, `represented_in_appendix`, `deferred`, `rejected`, or `resolved` status language when candidate state changes.
- **Rule:** When a candidate is split, record both scaffold target and appendix retention reason.
- **Constraint:** Do not delete a candidate row unless the integration location and status history are preserved elsewhere.

## Non-goals

- **Constraint:** Do not validate factual content truth for other domains.
- **Constraint:** Do not mutate shared governance or promotion authority.
- **Constraint:** Do not turn prompt templates into hidden runtime law.
- **Constraint:** Do not harden sentence-count, schema-first, or redundancy rules into universal law from this KB base.

## Status

- **Status:** KB-base practices are accepted for this agent scaffold.
- **Owner:** `special_ops__informatics_design`
- **Validator:** `special_ops__hygiene_clean`
