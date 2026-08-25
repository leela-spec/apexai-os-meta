# Regression and Semantic Evaluation Matrix

## Deterministic regression fixtures

1. **WhisperX JSON:** preserve segment/word timing and speaker labels.
2. **SRT/VTT:** preserve cue times and voice/speaker labels.
3. **Untimed text:** never fabricate timestamps.
4. **Diagnostics:** flag non-monotonic timing, large gaps, duplicates, and low-confidence words when available.
5. **Core coverage:** every segment belongs to exactly one Map core window, in source order.
6. **Context halo:** context-only segments may appear in the packet but cannot be cited by that Map result.
7. **Determinism:** same source bytes/config produce byte-identical deterministic artifacts.
8. **Packet freshness:** stale Map/Reduce/verification hashes are rejected.
9. **Quote grounding:** every claim quote is a literal substring of its cited normalized segment.
10. **Exact dedupe:** exact normalized claim text may merge evidence mechanically.
11. **Near dedupe:** similar but non-identical claims are flagged, never silently merged.
12. **Verification routing:** only factual, sufficiently source-supported, threshold-meeting claims enter the queue.
13. **Verification evidence:** decisive verdicts require URL-backed evidence records.
14. **Strict compile:** final `UNSUPPORTED` Micro claims fail strict compilation.
15. **Wiki integrity:** all generated internal wikilinks resolve to generated Markdown pages.
16. **Resume:** missing/invalid artifacts produce one clear next state without rerunning valid work.

Run:

```powershell
cd scripts
python test_ttk.py -v
```

## Semantic evaluation fixtures

These require a capable reasoning model; deterministic code can validate the result shape/provenance but not guarantee interpretation quality.

### S1 — Single-speaker lecture with real topic shifts

Expected:
- processing windows need not match final Meso boundaries;
- Reduce creates coherent semantic modules;
- Macro covers early, middle, and late material;
- no arbitrary module count.

### S2 — Two-speaker disagreement and correction

Expected:
- opposing claims stay separate until evidence resolves them;
- correction/uncertainty is visible at Meso and Macro levels;
- quote evidence identifies which speaker said what.

### S3 — Fact + opinion + prediction + recommendation

Expected:
- only factual assertions are candidates for external truth verification;
- other speech acts remain useful knowledge but compile as `NOT_APPLICABLE` for external truth.

### S4 — Repeated idea with subtly different scope

Expected:
- deterministic near-duplicate warning fires when lexical overlap is high;
- Reduce decides whether claims are equivalent, narrower, broader, or contradictory;
- no automatic semantic collapse.

### S5 — Noisy ASR / partial timing

Expected:
- transcript evidence remains usable through segment IDs;
- missing timing is explicit;
- semantic worker lowers certainty or records source-quality caveats rather than inventing words/times.

### S6 — Important factual claim with weak transcript support

Expected:
- source support is `PARTIAL`, `AMBIGUOUS`, or `UNSUPPORTED` as appropriate;
- external sources cannot repair a transcript-grounding failure;
- strict compilation rejects unsupported final claims.

### S7 — Speaker accurately states a false fact

Expected:
- source support can be `SUPPORTED`;
- external status can independently become `CONTRADICTED`;
- original quote remains unchanged.

### S8 — Long transcript where raw text exceeds comfortable model context

Expected:
- Map windows finish independently;
- Reduce consumes only evidence ledger;
- one failed window can be retried without replaying all source text;
- Macro retains coverage across the full source.

## Acceptance criteria

A release is not accepted merely because scripts run. It should satisfy:
- deterministic test suite passes;
- at least one end-to-end synthetic run reaches compiled wiki;
- a real transcript can resume after intentional interruption;
- quote mismatch and stale-packet negative tests fail closed;
- semantic spot-check confirms Macro/Meso/Micro outputs remain traceable to source segments;
- no graph/vector/Apex dependency is required for the happy path.
