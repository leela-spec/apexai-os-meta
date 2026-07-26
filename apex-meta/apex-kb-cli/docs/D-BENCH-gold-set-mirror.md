---
type: benchmark-mirror
title: D-BENCH gold set (mirror) — falsifiable answer benchmark for KB retrieval methods
description: Read-only mirror of the gold set built in Leela-Cloud-2026 to fill the D-BENCH gap this project's own PROJECT-STATUS.md names as deferred. Do not edit here — edit the source and re-mirror.
mirrored_from: https://github.com/leela-spec/Leela-Cloud-2026/blob/master/docs/ssot/_reviews/kb-gold-set.md
mirrored_date: 2026-07-26
source_of_truth: Leela-Cloud-2026 repo, docs/ssot/_reviews/kb-gold-set.md — this file may lag it
tags: [benchmark, gold-set, d-bench, retrieval, evaluation, mirror]
---

# D-BENCH gold set (mirror)

> **This is a mirror, not the source.** The living, currently-correct version is
> `docs/ssot/_reviews/kb-gold-set.md` in the `Leela-Cloud-2026` repository. Edit that file, not this
> one — this copy exists so Apex KB's own future development can find it without crossing repos, per
> `PROJECT-STATUS.md`'s roadmap item **D-BENCH** ("golden query set, expected-answer rubric,
> claim-entailment set, retrieval precision/recall set, token-savings measurement") — this is the first
> real instance of that, built against the harder Leela corpus rather than the therapy/NARM one.

**Why this exists.** Eleven Apex KB iterations produced nothing of value on the Leela corpus while its
own 2026-07-24 audit (`kb/therapy-narm-personal-development/audit/reports/2026-07-24-apex-kb-value-
audit.md`) scored it level with established projects (Apex ≈ 63→69 vs OpenKB ≈ 65). That audit is
explicit that answer quality was never measured (§3.3) and that the benchmark which would have caught
it — this one — was scoped and then deferred (commit `412c873e`). Full account of why that scoring was
unreliable: `kb/therapy-narm-personal-development/audit/reports/2026-07-26-why-the-competitor-
benchmark-was-fake.md`.

## Scoring sheet (8 questions, answers pre-verified, run blind against any method)

| # | Question | Established answer | Proof |
|---|---|---|---|
| G1 | What is the XP formula, and do its quality-multiplier coefficients differ anywhere in the corpus? | `XP = round(actual_min × priority_weight × quality)`, `quality = clamp(Π mults, 0.8, 1.6)` — spacing 1.2 · testing/recap 1.15 · interleaving 1.1 · application 1.1. Implemented twice, consistent. | `supabase/migrations/20260718150000_harmonization.sql:616`; `lib/features/harmonization/harmonization_xp.dart:26,30,44`; `docs/ssot/decisions/2026-07-25-metric-spine-resolved.md:75-78` (Leela repo) |
| G2 | Was the Rhythm Balancer (RB) dropped, or renamed to BP? | Both halves required: name RB → BP (index survives, a decision record needs amending); the *separate* RB wellness gauge is retired. | `docs/ssot/decisions/2026-07-25-metric-spine-resolved.md:73-74,101` vs. `2026-07-24-rhythm-balancer-dropped.md:13` (Leela repo) |
| G3 | Is there an `ExecutionStyle` concept distinct from `Variant`? | No — invented by an AI. Real concept: `SequenceTemplateFamily{templateId, displayName, variantIds, defaultVariantId, isCustom}`. | `lib/features/rhythm/domain/sequence_template_family.dart:4,8,9`; absence: `rg -c 'ExecutionStyle' lib/` → 0 |
| G4 | How many recommendation-ranking formulas exist, and which governs? | Four coexist; ST-022 governs; XP/min is display-only. | `docs/ssot/decisions/2026-07-25-metric-spine-resolved.md:17-45` (Leela repo) |
| G5 | Does Rhythm place accepted Sequence Instances? | No — places variants only; no Instance identity in the placement model. | Absence: `rg -c 'instanceId\|structureHash' lib/features/rhythm/` → 0 |
| G6 | Is BP a 0–100 weekly index or a per-candidate product? | Both, deliberately — weekly index is current definition; the product is preserved as a per-candidate estimate. | `docs/ssot/decisions/2026-07-25-metric-spine-resolved.md:51-70` (Leela repo) |
| G7 | Is `LeelaChunkMaturity.mastered` operator truth? | No — drift. Retire across 7 Dart call sites (plus a DB column — see baseline finding 4 below). | `docs/ssot/decisions/2026-07-25-metric-spine-resolved.md:80-93` (Leela repo) |
| G8 | Does the Sequencing Builder exist and rank correctly? | Exists, 5 steps, ranks by `isRecommended, xpPerMinute` — violates ST-022 but faithfully implements Harmonization Spec v1. Fix ranking, don't discard. | `docs/ssot/decisions/OPEN_QUESTIONS.md:126` (QA-75, resolved) (Leela repo) |

## Result log

| Date | Method | Found | Grounded | No false conflict | Score | Notes |
|---|---|---|---|---|---|---|
| 2026-07-26 | Cheap baseline — decisions-first authority order + rare-identifier grep + whole-file reads. Blind run, ~5.5 min, ~97k tokens. | 8/8 | 8/8 | 8/8 | **8/8** | Also found 4 findings this gold set didn't contain (see full file). n=1, no variance — re-run before treating as a stable rate. |
| — | *Apex KB* | — | — | — | **not scored** | Its run-config excludes `docs/ssot/decisions/`, so 6 of 8 proof artifacts are unreachable, and it cannot extract `.dart`, making 2 more impossible. To score it fairly: un-exclude `docs/ssot/decisions/`, add code extraction, replace raw-term scoring with something IDF/length-normalized. |

**Full detail (claim-entailment spot-check, known-hard-case design, caveats)**: see the source file in
`Leela-Cloud-2026`. Not duplicated here to avoid this mirror silently going stale on the parts most
likely to be revised.
