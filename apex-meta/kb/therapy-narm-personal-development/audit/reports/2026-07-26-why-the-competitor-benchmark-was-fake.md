---
type: audit-followup
title: Why the 2026-07-24 competitor benchmark was not a real measurement
description: Plain-language explanation of why Apex KB scored itself level with or above established projects while eleven real-world runs against the Leela corpus produced nothing usable — written after the operator asked directly why the self-audit was fake.
date: 2026-07-26
supersedes_nothing: true
references:
  - apex-meta/kb/therapy-narm-personal-development/audit/reports/2026-07-24-apex-kb-value-audit.md
  - apex-meta/apex-kb-cli/docs/PROJECT-STATUS.md
---

# Why the 2026-07-24 competitor benchmark was not a real measurement

**Plain-language summary for a non-coder.** The July 24 audit produced a scoreboard where Apex KB
(≈63–69) sits ahead of GraphRAG (≈50), Odysseus (≈42), and a "concept file with no code" (≈30), and
almost tied with OpenKB (≈65) — the one system its own report calls "the architectural mirror of
Apex's intent." That scoreboard is not fabricated in the sense of invented numbers, but it is **not a
real measurement** either. Four separate weaknesses combined to produce a self-flattering result, and
the report itself admits three of the four in plain text. Nobody read those admissions before treating
the scoreboard as evidence Apex was working.

This document is the missing piece: it explains *why* a system that scored well here has since failed
eleven consecutive times on a harder, real corpus (the Leela project), and it gives the four reasons in
order of how much each one contributed.

## Reason 1 — most competitor scores were never actually run; they were read off a README

Open `2026-07-24-apex-kb-value-audit.md` Part B (line 241 onward) and Part C (line 269 onward). Column
after column reads `N/E` — "insufficient evidence" — for Odysseus, deepwiki-open, GraphRAG, and the
memory-tool comparators, on the exact dimensions that matter most: answer quality, retrieval precision,
retrieval recall, semantic depth. The report is honest about this at line 170: *"Capability is split
into VERIFIED (code/doc evidence) vs CLAIMED (marketing/third-party)."* But once the matrix is
collapsed into one weighted number at line 296, that distinction disappears. A 42 built mostly from
`N/E` cells and a 63 built from actually running the tool both come out looking like comparable,
measured scores. They are not the same kind of number, and averaging them together erases the
difference.

**What this means in practice:** Apex was graded on hard evidence. Most of its competitors were graded
on guesses conservative enough to "look competitive." A scoreboard where one contestant runs the race
and the others are scored from their brochure is not a race result.

## Reason 2 — the test corpus was the easiest possible case, and it is not the corpus that matters

Every number in that matrix — for Apex and for every competitor — comes from the **therapy/NARM**
knowledge base: about 11 personal notes files, 903 KB, no code, no authority hierarchy, no
contradictions between document versions, and reflective questions with no single checkable right
answer (the report's own example, quoted at line 21 of the source audit region: *"anger may protect
vulnerable affect **or** convey valid present boundary information; the function cannot be selected in
advance"*).

The corpus this tool actually needs to work on — this Leela project — is the opposite on every axis
that matters: 1,371 files, 11 topics, documents that openly contradict earlier documents, code as a
mandatory source of truth, and questions with one exact, checkable right answer (example: "quote the
XP formula's coefficients verbatim" — a question a `grep` can get exactly right or exactly wrong).

**A tool validated on a corpus with no hard cases will always look good, because it was never asked a
hard case.** Deploying that same tool, unchanged, on a corpus built specifically to have hard cases
was always going to fail — and it did, eleven times.

## Reason 3 — the audit admits, in writing, that the one number that matters was never measured

This is the most important reason, because the report says it about itself, more than once, and those
statements were never acted on:

- Line 101: *"50 tests prove structure, determinism, identity, migration, and rejection of malformed
  input... **Zero** golden-query, precision/recall, claim-entailment, or token-savings benchmarks
  exist. The 50-test 'pass' is a deterministic-contract guarantee, not an answer-quality guarantee."*
- Line 226 (row A20, "Semantic acceptance"): claimed availability 80, demonstrated **15**. The report's
  own scoring convention (line 198) puts 15 in the "weak/early" band.
- Line 274 (Part C, "Target-question answer quality"): Apex scores **72** — but this is the exact
  dimension the report just said, twice, was never independently checked. It is a plausible-sounding
  guess wearing the same number format as a measured score.
- Line 353: *"Build the missing benchmark... This is the gate for everything in Phase III."* The report
  correctly identifies the benchmark as a **gate** — work that should block further development until
  it exists.

**What actually happened next, from the tool's own commit history:** commit `412c873e`, titled "Rescope
Apex KB improvement docs to CLI infrastructure; defer KB testing," deferred exactly this gate. Every
commit after the audit fixed plumbing (a stale-pointer probe, a canonical ledger, an honest state label,
a skill rewrite, a date bug) — genuinely useful work, but none of it touches whether an answer is
*true*. The gate the report itself demanded was never installed, so nothing since has been able to
fail. Eleven iterations without a test they could fail were eleven iterations with no way to
distinguish progress from motion.

## Reason 4 — the tool graded itself, and that is a documented, measurable bias, not a hunch

The same process that designed, ran, and audited Apex KB also assigned it its own scores. This is not
a uniquely Apex problem — it is a named, actively studied failure mode in AI research called
**self-preference bias**: language models rate their own outputs, or outputs from their own model
family, higher than independent evaluators would. Current research puts a number on it — self-
preference bias has been measured to skew scores by up to 10 points on subjective benchmarks, and on
rubrics where a generator actually fails, a same-family judge can be up to 50% more likely to wrongly
mark it as passing (see Sources below). Apex's real margin over its nearest competitor, OpenKB, was
**63 vs 65 — inside that documented bias band.** The two systems are not distinguishable by this
scoreboard; the audit says as much at line 297 ("the two are within noise").

Mitigations exist and are well documented — using multiple *independent* judges instead of one, and
decomposing "is this good?" into narrower sub-questions before scoring — but none were used here. One
process wrote the product, wrote the test, and graded the exam.

## The combined effect

Stack the four reasons and the result stops being surprising: a tool was graded by the process that
built it (Reason 4), on the one dimension it admits was never checked (Reason 3), against competitors
mostly scored from their marketing copy (Reason 1), on a corpus specifically chosen to have no hard
cases (Reason 2). Every individual step is defensible in isolation — even honestly labeled in the
document itself — but combined, they guarantee a flattering score regardless of whether the tool
actually works. That is why "we still produce absolutely shit and detect nothing" and "it ranks itself
as better than established repos" are **both true at once**, without contradiction: the scoreboard and
real-world performance were never measuring the same thing.

## What actually fixes this (already done, this session, in the Leela repo — not here)

A scoreboard becomes real the moment it can fail. On 2026-07-26 a small, falsifiable answer key —
`docs/ssot/_reviews/kb-gold-set.md` in the Leela-Cloud-2026 repo — was built from questions whose
answers were already independently confirmed by opening the originating file, not by asking any tool.
A plain, cheap method (read the locked decisions first, then grep for exact rare terms, then read whole
files) was run **blind** against it — the runner never saw the answer key — and scored 8 out of 8,
correctly cited its sources, and found four things the answer key itself did not contain. Apex KB, run
against the same eight questions, cannot reach six of them because its own configuration excludes the
folder holding the answers, and cannot read the other two because it cannot process `.dart` source
code at all. It is recorded in that file as **not scored**, not as a loss — a fair score requires fixing
that configuration first.

No claim about "better" or "worse" retrieval should be made again — about Apex or anything that
replaces it — without a line in a gold-set-style answer key like this one, scored by a party that did
not write the answer key.

## Sources

- [Play Favorites: A Statistical Method to Measure Self-Bias in LLM-as-a-Judge](https://arxiv.org/pdf/2508.06709)
- [Self-Preference Bias in LLM-as-a-Judge](https://arxiv.org/pdf/2410.21819)
- [LLM-as-a-Judge in 2026: How It Works, When It Fails](https://futureagi.com/blog/llm-as-a-judge/)
- [Quantifying and Mitigating Self-Preference Bias of LLM Judges](https://arxiv.org/abs/2604.22891)
- [RAG Evaluation Metrics: Best Practices for Evaluating RAG Systems](https://www.patronus.ai/llm-testing/rag-evaluation-metrics)
