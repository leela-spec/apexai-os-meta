# Transcript-to-Knowledge v2 — Validation Report

Date: 2026-08-18

## 1. Deterministic regression suite

Command:

```text
python scripts/test_ttk.py -v
```

Result at publication candidate: **12 / 12 passing**.

Covered failures:

1. deterministic/idempotent init and exact ordered core coverage;
2. context-only evidence is rejected;
3. non-verbatim quote is rejected;
4. stale Map packet hash is rejected;
5. untimed text never receives invented timestamps;
6. end-to-end Map -> Reduce -> selective verify -> wiki compile;
7. decisive verification verdict without evidence is rejected;
8. non-factual claims do not enter the external verification queue;
9. near-duplicate claims are flagged but not silently merged;
10. `doctor` proves the core CLI has no network/LLM dependency;
11. compiled wiki becomes `compile_stale` when a valid Reduce result changes;
12. recompile removes obsolete compiler-owned Markdown pages.

The semantic eval matrix remains in `references/evals.md`; deterministic tests cannot prove the quality of thesis/theme/claim interpretation.

## 2. Synthetic deterministic scale test

This is a transport/control-plane benchmark only. It is **not an ASR benchmark and not an LLM benchmark**.

Synthetic input:

```text
segments:       10,000
words:          212,000
raw JSON bytes: 2,486,126
```

Configuration:

```text
target_words:      1100
min_words:          700
max_words:          1500
block_segments:     4
context_segments:   1
```

Observed in the execution container:

```text
windows / Map packets:       200
elapsed wall time:            2.37 s
maximum resident set size:    144,344 KB (~141 MB)
core segment references:      10,000
context-only references:      398
context reference overhead:   3.98% of core segment count
map packet bytes total:       4,054,274
```

The normalized transcript is larger than the raw synthetic JSON because it stores canonical metadata/anchors. That is expected. Token-efficiency is achieved by semantic **read topology**, not by minimizing deterministic disk bytes: every core segment appears in one Map packet; only a small context halo repeats; Reduce consumes the compact evidence ledger rather than the raw transcript again.

## 3. Failure/recovery behavior

| Failure | Expected behavior |
|---|---|
| Process stops after some Map windows | `status` finds completed results; `next` points to first missing window |
| One Map JSON malformed | only that result is invalid; valid siblings remain reusable |
| Map packet changes | old Map result fails packet hash |
| Map evidence changes | rerun `make-reduce`; old Reduce result becomes stale |
| Reduce changes | verification queue hash changes; old verification results fail |
| Verification missing | compile is permitted; routed facts remain `UNVERIFIED` |
| Verification decisive but evidence empty | validation fails |
| Reduce/verification changes after compilation | `status=compile_stale`; `validate --complete` fails until recompile |
| Final claim source support is `UNSUPPORTED` | strict compile fails |
| Old generated wiki page no longer represented | next compile removes the stale generated page |

## 4. Validation boundaries

### What the tests prove

- stable file/state mechanics;
- deterministic source ownership;
- stale-artifact detection;
- hard provenance/quote checks;
- selective verification routing;
- deterministic compilation and link integrity;
- resumability without chat memory.

### What the tests do not prove

- the reasoning model chose the best Meso chapter boundary;
- the Macro thesis is insightful;
- every valuable source proposition was extracted;
- an external factual verdict is substantively correct;
- ASR quality for any audio backend.

Those need semantic eval fixtures and, for ASR, real hardware/audio benchmarks.

## 5. Acceptance gates before calling the pipeline production-reliable

1. **Deterministic:** all regression tests pass.
2. **Complete run:** `validate <run> --complete` succeeds.
3. **Semantic coverage fixture:** no high-value fixture fact disappears from both Map evidence and final Micro.
4. **Provenance fixture:** all sampled final claims have exact usable source evidence.
5. **Contradiction fixture:** disagreement is preserved rather than silently reconciled.
6. **Speech-act fixture:** opinions/recommendations/decisions are not mislabeled as external facts.
7. **Long-run fixture:** interrupted/resumed run produces byte-equivalent deterministic artifacts given identical semantic result files.
8. **Human spot check:** inspect Macro, each Meso module, and a stratified sample of Micro claims before adding any downstream retrieval/indexing system.

## 6. Packaging limitation

The Linux execution environment used here has no PowerShell executable, so the `.ps1` wrappers cannot be runtime-executed in this validation. Their logic is intentionally thin: locate `py -3` or `python`, invoke the Python CLI, and fail on a nonzero exit. The Python implementation they wrap is fully exercised.
