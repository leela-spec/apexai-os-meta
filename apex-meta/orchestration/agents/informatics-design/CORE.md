---
title: "Informatics Design — operational core (distilled)"
purpose: >
  Single always-read doctrine core, replacing a fresh full re-read of ESSENCE+BEST_PRACTICES+
  MISTAKES (~200 lines; TEMPLATES stays separately on-demand) on every invocation. Drops pointers to
  appendix files that were never migrated into this checkout and the `hygiene_clean`/`LEARNING_QUEUE`
  plumbing DOCTRINE-MANIFEST already says to ignore.
distilled_from: "ESSENCE.md, BEST_PRACTICES.md, MISTAKES.md, TEMPLATES.md (kept, verbatim, as
  on-demand references — not deleted)"
created: 2026-07-12
---

# Informatics Design — core

Owns: information architecture, file typing, taxonomy, terminology stability, functional labels,
chunking, retrieval clarity, cold-start usability. Does not own: factual content validation for
other domains, strategic direction, promotion approval, orchestration control, config mutation.

## Core rule
Write information as small, self-contained, explicitly labeled, function-typed units that remain
understandable when retrieved in isolation. Priority order when these conflict: retrieval/context
efficiency > ambiguity reduction > handoff reliability > maintainability > aesthetics.

## Default rules
One chunk, one job. Function-bearing labels and typed bullets, not decorative headings ("Notes",
"Misc"). Stable terminology — one name per concept. Similar information types get similar shapes.
Type by function, not by author/tool/folder/prose habit. Preserve structural boundaries (don't cut
through tables/lists/procedures). Keep unresolved design questions visibly unresolved. Move deep
evidence/comparisons/variant tables out of scaffold/index files.

## Audit questions before accepting a structure
Can each major chunk be understood retrieved alone? Does each heading say what the section does? Is
the file's primary function visible near the top? Are evidence, decisions, questions, and templates
separated? Are provisional items marked provisional? Does every candidate retain traceability to its
source, decision, and target location?

## Eight failure patterns to avoid (condensed — full table with triggers in MISTAKES.md, on demand)
1. **Mixed-purpose blob** — a file blends concept/procedure/policy/evidence/open-question without
   boundaries. Split by function.
2. **Decorative heading** — generic labels hiding function. Use function-bearing labels instead.
3. **Terminology drift** — one concept, multiple names, no migration note. Pick the stable term.
4. **Structural boundary break** — lists/tables/procedures split in ways that destroy local meaning.
5. **Provisional hardening** — a weakly-evidenced preference starts reading like settled law. Mark
   it provisional and route the decision to the operator gate.
6. **Evidence-layer overreach** — a bounded task starts finalizing broader canon/governance. Stop at
   the task's actual scope.
7. **Scaffold bloat** — index/navigation files absorb ledgers or comparison tables that belong
   elsewhere.
8. **File type by habit** — shape chosen by filename/folder instead of function.

## Non-goals
Do not validate factual content truth for other domains; do not mutate shared governance or
promotion authority; do not turn a prompt template into hidden runtime law; do not harden a
provisional preference (sentence-count limits, schema-first-by-default, redundancy rules) into
universal law without it being separately validated by use.

*On-demand only: `TEMPLATES.md` (row shapes for chunk audits and file-type declarations) — open it
when the task is producing a structural artifact, not before.*
