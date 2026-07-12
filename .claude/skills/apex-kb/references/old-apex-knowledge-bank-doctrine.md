# Old-Apex Knowledge Bank Doctrine

```yaml
artifact_name: old_apex_knowledge_bank_doctrine
package_path: .claude/skills/apex-kb/references/old-apex-knowledge-bank-doctrine.md
consumer: apex-kb skill during source intake, Phase 2 compile, and lint/audit work
source_basis: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/special_ops__knowledge_bank/
purpose: >
  Still-valid KB operating doctrine distilled from the old-apex v1 knowledge-bank
  role. Only items not already covered by the apex-kb contract, promotion rules,
  or lifecycle references appear here. Historical file paths in citations are
  evidence, not authority.
```

## Best practices

- **improvement_capture** — A better idea discovered during a bounded KB run (structure fix, template gap, routing tweak) that falls outside the authorized mode or target files is captured as an audit item or backlog entry, never applied silently within the run. Silent improvement application is scope drift onto unapproved surfaces. Source: `BEST_PRACTICES.md` BP-KB-004.
- **narrow_authority_stack** — Only sources recorded in the source manifest and the explicitly authorized target files carry execution authority for a run. Any additional material read for orientation is explanatory context and may not drive page content, claims, or writes unless first added to the manifest. Source: `BEST_PRACTICES.md` BP-KB-005.
- **durable_qa_backlog** — Run-level verification findings, readiness gaps, open research questions, and deferred repair candidates are written to `audit/` (or the KB's backlog surface), never left only in chat. KB continuity depends on traceable improvement queues that survive the session. Source: `BEST_PRACTICES.md` BP-KB-009.

## Known failure modes

- **compiled_page_bloat** — Raw source bodies, long rationale, or archive excerpts get pasted into compiled wiki pages instead of synthesized claims with source pointers. Pages become context-heavy and low-retrieval. Countermeasure: pages carry synthesis plus pointers; depth stays in preserved `raw/` sources reachable via Routes Here and raw-source triggers. Source: `MISTAKES.md` MK-KB-002.
- **local_grammar_invention** — The compiler invents new status values, label types, or row grammars to make the current artifact "cleaner," degrading cross-run retrieval and validation. Countermeasure: reuse the status vocabulary and field shapes declared in `kb-schema.md` and the lifecycle state machine; route unresolved grammar needs to an audit item instead of inventing locally. Source: `MISTAKES.md` MK-KB-004.
- **waterfall_overfit** — A complete page or index skeleton is frozen before the corpus is understood, forcing emerging knowledge into premature structure and hiding gaps under neat headings. Countermeasure: for uncertain corpora, draft hypothesis-first structure, then let Phase 0/Phase 1 evidence and quality checks settle the final page set before compile is declared done. Source: `MISTAKES.md` MK-KB-006.
- **evidence_overgeneralization** — A vivid failure/postmortem source is written into compiled pages as universal doctrine rather than bounded incident evidence. Countermeasure: mark postmortem-derived claims as evidence-scoped (uncertainty trigger or audit flag) unless separately validated through the promotion gate. Source: `MISTAKES.md` MK-KB-007.

## Templates worth reusing

- **improvement_opportunity_block** — Form for capturing an out-of-mode improvement without applying it. Source: `TEMPLATES.md` TPL-KB-005.

```md
### IMP-KB-### — <short title>

- **Affected area:** <file, page, index, or process>
- **Type:** source_gap | structure_improvement | validation_improvement | template_improvement | routing_improvement
- **Observed issue:** <what was noticed>
- **Why it may improve the system:** <one compact explanation>
- **Why it was not applied now:** <scope or mode boundary>
- **Smallest safe future mode:** <audit item, operator review, bounded patch>
- **Risk if left unchanged:** <risk>
- **Risk if changed during this run:** <risk>
- **Status:** not_applied_in_this_run
```
