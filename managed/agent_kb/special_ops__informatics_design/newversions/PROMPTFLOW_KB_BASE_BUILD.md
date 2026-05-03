# MISTAKES

## Purpose

Reusable failure patterns and countermeasures for `special_ops__informatics_design`.

This file is compact scaffold guidance. Full evidence lives in `appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`.

## Failure patterns

| id | pattern | trigger | countermeasure |
|---|---|---|---|
| MIS-INF-001 | Mixed-purpose blob | A file or section blends concept, procedure, policy, reference, evidence, and open questions without clear boundaries. | Split by function; keep one section to one job; route deep detail to appendices. |
| MIS-INF-002 | Decorative heading | Headings say `Notes`, `Misc`, or other generic labels that hide function. | Replace with function-bearing labels: Rule, Evidence, Template, Open Question, Candidate, Audit. |
| MIS-INF-003 | Terminology drift | The same concept appears under multiple names without a declared synonym or migration note. | Use the stable term; add provisional labels where vocabulary is not settled. |
| MIS-INF-004 | Structural boundary break | Lists, tables, procedures, or checklists are split in ways that destroy local meaning. | Preserve meaning-bearing blocks; move whole tables/lists to appendices when large. |
| MIS-INF-005 | Provisional hardening | Open questions or weakly evidenced implementation preferences start reading like law. | Mark provisional status and route to `LEARNING_QUEUE.md` or appendix evidence. |
| MIS-INF-006 | Evidence-layer overreach | A KB-base or research run starts finalizing broader canon, taxonomy, audit, or governance surfaces. | Stop at agent-KB scope; do not mutate shared accepted truth. |
| MIS-INF-007 | Process rule as decoration | A source constraint is cited but not enforced as a gate before writing. | Turn constraints into explicit pre-write and fetch-back checks. |
| MIS-INF-008 | Scaffold bloat | Scaffold files absorb detailed ledgers, source comparisons, or variant tables. | Keep scaffolds compact; move depth to appendices and link outward. |
| MIS-INF-009 | File type by habit | File shape is chosen by filename, folder, or prior habit instead of function. | Declare primary function and use the matching template. |

## High-risk ambiguity traps

- **Trap:** Sentence-level strictness is useful for procedures but is not universal law.
- **Trap:** Schema-first structure is a later-phase option, not a Phase-1 default requirement.
- **Trap:** Prompt templates can support artifact creation but do not automatically belong inside information-design governance.
- **Trap:** Bounded reinforcement is useful; uncontrolled redundancy creates drift.

## Review questions

- **Check:** Is the file doing more than one primary job?
- **Check:** Would a retrieved chunk make sense without surrounding text?
- **Check:** Are terms stable and intentionally reused?
- **Check:** Is any unresolved question being treated as settled?
- **Check:** Did the scaffold stay compact enough for cold-start use?

## Status

- **Status:** KB-base mistakes are accepted for this agent scaffold.
- **Owner:** `special_ops__informatics_design`
- **Validator:** `special_ops__hygiene_clean`
