# Informatics Design Doctrine (migrated from old-apex v1 role KB)

Purpose: distilled still-valid information/file-design doctrine for any agent authoring packets, references, or state files, and for the main thread when reviewing file design.
Source basis: `apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/special_ops__informatics_design/` (ESSENCE.md, BEST_PRACTICES.md, MISTAKES.md, TEMPLATES.md, appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md). Governing baseline — already absorbed there, not repeated here: D-M6 in `apex-meta/kb/Weekly-Orchestrator/architecture/01-macro-architecture-decision.md` (MD-first + one YAML envelope, snake_case, typed labels, refs-not-copies, read_when-gated compact entrypoints, sidecars only on demonstrated consumer need) and `storage_rules` in `references/handoff-schema.md`.

## Best practices

- Rule: one chunk, one job — split a section the moment it is doing rule, evidence, open-question, and template work at once. (ESSENCE.md core rule; BEST_PRACTICES.md)
- Rule: write chunks self-contained — every major section must remain understandable when retrieved in isolation, without surrounding context. (ESSENCE.md core rule)
- Rule: headings are function-bearing, never decorative — a heading says what the section does; no `Notes`, `Misc`, or generic labels. (BEST_PRACTICES.md; MISTAKES.md MIS-INF-002)
- Rule: state a file's primary function near the top (purpose, bounded scope, explicit non-scope) so cold-start readers classify it in one glance. (BEST_PRACTICES.md audit questions; TEMPLATES.md file function template)
- Rule: one concept keeps one name across a file pack; when vocabulary is unsettled, label the term provisional instead of alternating synonyms. `apex-meta/GLOSSARY.md` is the term authority. (BEST_PRACTICES.md; MISTAKES.md MIS-INF-003)
- Rule: type files and sections by function, not by author, tool, folder, or prose habit; repeated file classes stay structurally similar enough for fast audit and reuse. (ESSENCE.md; MISTAKES.md MIS-INF-009)
- Rule: preserve structural boundaries — never cut through tables, lists, procedures, or other meaning-bearing blocks when splitting or excerpting; move the whole block if it must relocate. (ESSENCE.md; MISTAKES.md MIS-INF-004)
- Rule: keep unresolved or weakly evidenced design choices visibly provisional — separate evidence, decisions, open questions, and templates so nothing unresolved reads as settled. (ESSENCE.md; BEST_PRACTICES.md)
- Constraint: no hidden rules inside prose — rules ride on typed labels, not paragraphs; reject ambiguous "should" language and essay-style rationale in rule-bearing files. (appendices/PromptFlowInfoDesi.md machine-readability rule)

## Known failure modes

- Failure: mixed-purpose blob — a file blends concept, procedure, policy, reference, and open questions until retrieval returns noisy chunks. Countermeasure: split by function; route depth to referenced deep files. (MISTAKES.md MIS-INF-001)
- Failure: provisional hardening — an open question or weakly evidenced preference starts reading like law. Countermeasure: keep provisional status attached until separately validated. (MISTAKES.md MIS-INF-005; anti-drift DRIFT-INF-004)
- Failure: TODO fossilization — a TODO or future-work note stays active after the work was integrated, rejected, split, or deferred, misleading later agents into reopening it. Countermeasure: update the status surface in the same change that disposes of the work. (MISTAKES.md MIS-INF-010)
- Failure: uncontrolled redundancy — the same rule restated across files drifts into conflicting versions. Bounded reinforcement is allowed; each rule has one authoritative home, elsewhere reference it. (MISTAKES.md ambiguity traps)
- Failure: universal-limit overreach — numeric sentence/paragraph limits and schema-first structure are situational tools for procedures, not default law for all files. (MISTAKES.md ambiguity traps; ESSENCE.md provisional boundaries)

## Templates worth reusing

- Template: file function header — `Purpose:` one sentence, `Scope:` bounded, `Boundary:` what the file does not do; place first in any new reference or doctrine file. (TEMPLATES.md file function template)
- Template: terminology mini-table — `| term | stable meaning | use when | avoid |`; use when introducing or disambiguating terms before promoting them to GLOSSARY.md. (TEMPLATES.md)
- Template: audit mini-check — `| check | inspect | pass condition | fail condition | severity |`; use when defining acceptance checks for a file class or packet family. (TEMPLATES.md)
