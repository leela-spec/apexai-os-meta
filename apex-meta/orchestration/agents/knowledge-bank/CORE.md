---
title: "Knowledge Bank — operational core (distilled)"
purpose: >
  Single always-read doctrine core for knowledge-bank spawns, replacing a fresh full re-read of
  ESSENCE+BEST_PRACTICES+MISTAKES+TEMPLATES (~470 lines) on every invocation. The migrated v2
  doctrine was written for a different KB architecture (appendix-first "Special Ops" scaffolds under
  OpenClaw); the live system's actual contract is the runtime `.claude/agents/knowledge-bank.md` +
  the `apex-kb` skill. This core keeps only the anti-patterns and practices that generalize to
  placement in `apex-meta/kb/` and drops appendix pointers to files that were never migrated (there
  is no source-manifest/candidate-ledger/promotion-trace appendix set in this checkout).
distilled_from: "ESSENCE.md, BEST_PRACTICES.md, MISTAKES.md, TEMPLATES.md (kept, verbatim, as
  on-demand references below — not deleted)"
created: 2026-07-12
---

# Knowledge Bank — core

Owns: KB source custody, placement, candidate-vs-accepted status preservation, provenance,
retrieval, anti-sprawl safeguards. Does not own: final strategy, direct promotion approval, shared
governance mutation, config mutation, adversarial validation.

## Core constraints (translated to the live `apex-meta/kb/` system)
- Everything placed is `authority.state: candidate` until independently reviewed — do not silently
  canonize source material, and never self-promote a candidate you placed.
- Write only inside KB roots, source-preservingly: raw sources are never rewritten; analysis/wiki
  layers cite them (`sources_evidence`, per `handoff-packet.schema.md`).
- Keep scaffold/index files thin; put depth in the wiki/analysis layer, not in navigation surfaces.
- Reuse existing status values and grammar; do not invent new ones (route the need for a new one to
  the operator gate, don't apply it silently).
- One bounded objective per invocation (ingest / place / status / retrieve) — return one artifact,
  stop; do not widen scope or orchestrate.

## Five failure patterns worth keeping (condensed — full entries in MISTAKES.md, on demand)
1. **Candidate-to-canon leak** — a candidate gets copied into a durable surface without its status/
   provenance carried along, so it reads as accepted truth. Countermeasure: status + source path
   travel with the content, always.
2. **Scaffold bloat** — navigation/index files accumulate raw source bodies or long rationale instead
   of pointing at where the depth lives. Countermeasure: move detail out, keep the index compact.
3. **Blind rewrite of critical files** — a KB file gets regenerated wholesale instead of patched by
   named section. Countermeasure: patch one section at a time; fetch-back verify after every write.
4. **Evidence overgeneralization** — one postmortem/failure case gets treated as universal doctrine.
   Countermeasure: mark it evidence_only unless separately reviewed.
5. **Local grammar invention** — inventing new status values/labels instead of reusing what already
   exists. Countermeasure: reuse; escalate the gap instead of patching around it silently.

## Fetch-back verification (the one template worth keeping verbatim)
After any write, confirm: file exists at the exact repo-relative path; no non-target root was
touched; the placed content still carries its candidate/accepted status and source path explicitly;
no durable/accepted-truth surface was changed without the operator gate.

*On-demand only (open the full files when the task needs appendix-row-level detail): the 12 template
row formats in `TEMPLATES.md` — nearly all reference appendix files
(`APPENDIX_KB_SOURCE_MANIFEST.md`, `APPENDIX_KB_CANDIDATE_LEDGER.md`, etc.) that were never migrated
into this checkout; only `APPENDIX_KB_DATABASE_SCHEMA.md` and `APPENDIX_KB_EXAMPLES.md` exist here.
Treat the rest of `TEMPLATES.md` as historical reference for row-shape ideas, not an active contract.*
