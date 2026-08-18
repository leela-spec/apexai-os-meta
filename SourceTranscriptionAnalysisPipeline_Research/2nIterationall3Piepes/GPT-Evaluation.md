# Re-evaluation of the repaired multi-pipeline stack

I verified the requested snapshot: `f97698cf2126ac605046667caf439f334d7b2454` exists and is the single repair commit after `6c2f1b70`, with commit message **“multi-pipeline anti-fabrication repair and fail-closed benchmark harness.”**

## Executive verdict

The repair pass **successfully fixed the most blatant P1/P2 fabrication failures**. P1 no longer contains the Huberman special-case synthesizer, P2 no longer injects generic market-cycle material, both can refuse synthesis when semantic evidence is absent, and the ASR writer is now capable of retaining word-level evidence.

But I would **not accept the handover's implied “three pipelines repaired and validated” conclusion yet**.

There are three blockers:

1. **The benchmark receipt is not actually fail-closed.** It says `all_passed: true` even though P2 is `SYNTHESIS_PENDING` for 3/4 sources, and the receipt identifies the tested Git commit as the old `6c2f1b70`, not `f97698cf`.
    
2. **P1's new word-level ASR evidence was not exercised.** The benchmark reused pre-existing SRTs instead of retranscribing them; the committed Huberman JSON is still the old segment-only schema.
    
3. **Most importantly, P3's new “full lifecycle” driver violates TTK's own architecture.** It replaces semantic Map/Reduce reasoning with deterministic copying of transcript segments, labels them all `fact`/`SUPPORTED`, and produces generic title-derived summaries. Its final validation proves provenance/structural correctness, **not knowledge-extraction quality**.
    

So the repair is a **meaningful improvement**, but the next pass should be a **correctness repair before hybrid unification**.

---

# A. Benchmark receipt verification

## Recorded execution states

|Source|P1|P2|P3|My interpretation|
|---|---|---|---|---|
|`P-h5WSQG1Sw`|`ASR_COMPLETE`|`OPERATOR_ARTIFACT_COMPLETE`|`OPERATOR_ARTIFACT_COMPLETE`|Only source with P2 semantic input|
|`CygwqaNg2PY`|`ASR_COMPLETE`|`SYNTHESIS_PENDING`|`OPERATOR_ARTIFACT_COMPLETE`|P2 correctly refuses fabrication|
|`vFTuLylvYnA`|`ASR_COMPLETE`|`SYNTHESIS_PENDING`|`OPERATOR_ARTIFACT_COMPLETE`|Same|
|`oZIsMX6WgFs`|`ASR_COMPLETE`|`SYNTHESIS_PENDING`|`OPERATOR_ARTIFACT_COMPLETE`|Same|

Those states are correctly represented inside the individual source entries.

### Receipt defect 1 — wrong aggregate result

The harness calculates success using only:

- P1 is not `FAILED`;
    
- P3 is not `FAILED`.
    

It **does not include P2 at all** in the `all_passed` calculation. Consequently, three `SYNTHESIS_PENDING` P2 executions still yield:

```text
all_passed = true
incomplete_count = 0
```

That contradicts the apparent meaning of an all-pipeline benchmark.

### Receipt defect 2 — wrong code provenance

The committed receipt says:

```text
git_commit = 6c2f1b701...
```

even though we are evaluating it as an artifact committed at `f97698cf`.

The likely explanation is straightforward: the benchmark was run while the repair existed as uncommitted working-tree changes, then those changes and the receipt were committed together. That is understandable operationally, but it means:

> **This receipt cannot prove that commit `f97698cf` itself was what was executed.**

Future benchmark receipts need `git_commit`, `git_dirty`, and ideally a worktree/diff hash, or must be generated only from a clean committed tree.

### Receipt defect 3 — P1 success means ASR only

The runner has an `IncludeSynthesis` parameter, but the actual P1 benchmark path never invokes its new grounding validator. P1 success therefore means **ASR exists**, not that the complete P1 pipeline produced validated Macro/Meso/Micro knowledge.

**Benchmark status:** **not yet a valid three-pipeline end-to-end comparison.**

---

# B. Transcript quality and evidence retention

## 1. ASR fidelity

The actual transcripts are essentially the same base-model transcripts evaluated previously because the runner skips transcription whenever the target SRT already exists.

|Source|Current qualitative ASR|Key observation|
|---|---|---|
|Huberman/Adolphs|**Good English, moderate technical/proper-name errors**|Broad discussion is very readable, but `Adolphs` becomes `Adolfs`; malformed phrases remain|
|Prechter|**Moderate**|Conceptual content survives well; names and Elliott terminology are error-prone|
|Markus Koch|**Weak–moderate domain vocabulary**|German syntax broadly understandable, but many financial names/terms are corrupted|
|Market Cycles|**Good–moderate**|Technical procedure survives surprisingly well; proper nouns and some terminology degrade|

### Examples

Huberman retains coherent neuroscience discussion but contains errors such as `Dr. Ralph Adolfs` and malformed sentences like “what tools may assistant helping.”

Prechter begins with `Elliott Pregnant`, later produces variants such as `Elliott Payf`, `alien wave`, and `UAV`, although its substantive explanations of wave counting, partial patterns, probabilities, and alternative interpretations remain intelligible.

German remains the weakest domain transcription. Current text still contains examples such as:

- `Nährstack` for Nasdaq context;
    
- `Handelsstaat`;
    
- `UE Staatsanleihen`;
    
- `Textsektor`;
    
- `Clarana`;
    
- `Bank auf America`;
    
- `gelauscht`;
    
- `Formmanager`.
    

The Market Cycles transcript preserves the actual procedural material much better: spectrum peaks, digital signal processing, ranking, stability, strength, cycle selection and the `>0.5` stability rule all survive. There are still lexical errors such as the presenter name and `face`/phase-like wording.

### Conclusion

**The repair did not yet improve measured ASR quality.** It improved the _future evidence schema_, which is different.

---

## 2. Word-level evidence retention

This part of the code repair is good.

`transcribe_audio.py` now persists, per word:

- text;
    
- start;
    
- end;
    
- probability.
    

And per segment:

- `avg_logprob`;
    
- `no_speech_prob`;
    
- `compression_ratio`;
    
- `temperature`;
    
- word records.
    

That is exactly the sort of evidence the hybrid pipeline should preserve.

### But it has not been benchmarked

The current Huberman JSON contains only:

```text
id
start
end
text
```

and no `words` field or new diagnostics because it is an old artifact.

So I rate this:

- **Implementation:** good.
    
- **Benchmark evidence:** absent.
    

A clean `--fresh-asr` benchmark is still required.

---

# C. Pipeline 1 — revised evaluation

## What is now fixed

The most serious previous failure is gone.

There is now a real fail-closed validation boundary:

- semantic JSON is required;
    
- missing semantic input exits as synthesis pending;
    
- invented Micro quotes fail;
    
- SRT metadata inside a quote fails;
    
- hard-coded Huberman synthesis is specifically regression-tested.
    

This is a major improvement.

## Remaining grounding gap

P1 currently validates **Micro quote existence**, but this is not equivalent to saying the _knowledge artifact_ is 100% grounded.

Macro fields such as:

- thesis;
    
- takeaways;
    
- taxonomy;
    
- speaker credentials;
    

and Meso:

- arguments;
    
- protocols;
    
- caveats;
    

do not have corresponding deterministic source anchors.

Yet the renderer labels the output:

> `Source Grounding: VALIDATED (100% exact verbatim match)`

The wording therefore overstates what was deterministically proven.

There is a second gap: quote validation is effectively against the normalized transcript globally. It does not prove that the supplied timestamp points to the segment containing that quote.

### External verification status bug

P1's verification status considers a claim “verified” if it either has a decisive verdict **or merely has an external source URL**:

```text
... verdict in (...) or c.external_sources
```

So URL retrieval can eventually make the overall status `COMPLETED` while claims remain `UNVERIFIED`.

That separation needs one more cleanup.

### P1 verdict

**Keep.**

P1 is now a good candidate for the canonical ASR/evidence-ingestion layer.

But use the language:

> `QUOTE_GROUNDING_VALID`

rather than:

> `100% SOURCE_GROUNDED`

until Macro/Meso and proposition support have also been evaluated.

---

# D. Pipeline 2 — revised evaluation

## The original semantic-contamination failure is fixed

`synthesize_p2.py` now does the correct thing when no semantic result exists:

```text
[P2_SYNTHESIS_PENDING]
```

and exits without fabricating a wiki.

Its engine also correctly separates:

- `claim_type`;
    
- `source_support`;
    
- external `verdict`;
    

and its verification hook explicitly leaves verdict `UNVERIFIED` when all it has done is retrieve URLs.

The tests explicitly cover that anti-fabrication behavior.

That repair is successful.

## But P2 is now clearly a representation layer, not a pipeline

The benchmark makes this visible:

**only 1 of 4 sources completes P2 synthesis.**

The other three correctly stop because there is no semantic-worker output.

That is not a defect in honesty. It reveals P2's actual architectural role:

> **typed knowledge schema + validator + renderer.**

## Provenance remains weaker than TTK

The completed Huberman artifact contains the new fields:

```text
source_segment_ids
source_start
source_end
```

but all three are empty.

Thus P2 currently proves:

> “this quote exists somewhere in the transcript”

but not:

> “this claim is anchored to these specific canonical source segments at this interval.”

Also, `source_support = SUPPORTED` is supplied by the semantic result. The deterministic engine cannot establish semantic entailment merely from substring matching.

That is acceptable **if the distinction is explicit**.

## Coverage remains unvalidated

The only completed semantic input for the 2h09m Huberman source contains:

- one Meso module from `00:00:16–00:00:53`;
    
- two Micro claims from the first minute.
    

So P2 can produce a completely valid artifact after semantically processing only a tiny fraction of the source.

This is not fabrication anymore.

It is now a **coverage/completeness failure**.

### P2 verdict

**Good library, questionable runtime stage.**

This becomes important for the hybrid architecture below.

---

# E. Pipeline 3 / TTK — revised evaluation

This is where my evaluation changes the most.

## The underlying TTK architecture is still the strongest

The actual skill contract is excellent:

> deterministic code handles custody, segmentation, validation, routing, resumability and compilation; the active reasoning model handles semantic interpretation.

It explicitly assigns to the semantic worker:

- theme interpretation;
    
- real chapter boundaries;
    
- mechanisms;
    
- claim formulation/classification;
    
- source-support judgment;
    
- Macro synthesis.
    

That separation remains the architecture I would trust most.

## But the new lifecycle driver breaks that separation

`execute_ttk_lifecycle.py` does **not** dispatch a semantic worker.

Instead, for each Map window it:

1. takes up to the first three core segments;
    
2. copies their text wholesale;
    
3. turns each into a claim;
    
4. sets:
    

```text
claim_kind = fact
source_support = SUPPORTED
```

5. generates no real mechanisms, protocols, entities, concepts, arguments or uncertainty.
    

Then Reduce:

- walks those synthetic claims in order;
    
- stops after **10 claims total**;
    
- creates one generic Meso module;
    
- uses the first 10 transcript segments as its module evidence;
    
- derives taxonomy from the video title;
    
- creates a generic Macro thesis.
    

### This is structurally valid but semantically nearly empty

TTK's validators quite correctly report:

- all 23 Huberman Map windows valid;
    
- Reduce valid;
    
- compiled current;
    
- complete true.
    

But this demonstrates that the validator is doing its intended deterministic job. It does **not** mean the generated semantics are good.

The actual Huberman Macro is:

> “Core empirical and thematic findings extracted from …”

and its only takeaway is essentially:

> source analysis completed with 10 validated claims.

The same template appears for Prechter, Koch and Market Cycles.

### The Prechter output makes the problem unmistakable

Its supposed Meso “Arguments” are literally the first pieces of transcript:

> “Elliott, thanks for joining us today…”

including the ASR error `Elliott Pregnant`.

And its Meso source range is just segments 1–10, roughly the first minute.

This is **not a semantic Meso module**.

Similarly, an example TTK Micro record classifies a fragment such as:

> “I called it the principle of antithesis is valence…”

as simply `fact`, because the driver classifies everything that way.

German fragments are likewise emitted as `fact` even when they are merely sentence fragments from commentary.

## Important distinction

P3 now has:

**excellent provenance correctness**

but

**bad semantic selection and synthesis**.

The two must not be conflated.

### P3 verdict

**Keep TTK. Remove the new pseudo-semantic lifecycle implementation.**

The TTK core is the component I would build the hybrid around.

---

# F. Updated architectural comparison matrix

Ratings are based on what is actually present at `f97698cf`, not intended future capabilities.

|Dimension|P1|P2|P3 / TTK|
|---|--:|--:|--:|
|Deterministic custody|**3/5**|**2/5**|**5/5**|
|ASR capability|**5/5**|N/A|N/A|
|Word-level evidence potential|**5/5**|**1/5**|**2/5**|
|Exact quote protection|**4/5**|**4/5**|**5/5**|
|Precise segment provenance|**2/5**|**2/5**|**5/5**|
|Claim taxonomy|**3/5**|**4/5**|**1/5 current driver**|
|Semantic coverage guarantee|**1/5**|**1/5**|**1/5 current driver**|
|Semantic synthesis quality|Not benchmarked|Only 1 hand-supplied result|**1/5 current driver**|
|External truth separation|**3/5**|**5/5**|**4/5**|
|Anti-fabrication structural safeguards|**4/5**|**4/5**|**5/5**|
|Anti-fabrication semantic safeguards|**2/5**|**2/5**|**2/5 current driver**|
|Valid token efficiency|**High**|**Very high**|**High in intended architecture**|
|Operator friction|Medium|Medium/high|Low only because semantics are currently bypassed|
|Operator artifact usefulness now|N/A|Moderate on 1 source|**Low**|
|Best architectural role|**ASR + evidence ingest**|**Schema/reference library**|**Custody + orchestration + validation + compilation**|

## Token efficiency needs special care

P3 currently appears spectacularly token-efficient because the semantic reasoning step was removed entirely.

That is **not an optimization**.

The correct token-efficiency comparison should measure:

> tokens required for **semantically acceptable output**

not merely tokens consumed by code that satisfies JSON validators.

TTK's intended model remains efficient because each raw source window is semantically read once, then Reduce works from the compact evidence ledger.

That is the token-efficient design worth preserving.

---

# G. Hybrid unification recommendation

My recommendation has changed slightly from the earlier:

```text
P1 -> P3 -> P2
```

idea.

## Recommended runtime

```text
                CANONICAL SOURCE
                       │
                       ▼
┌───────────────────────────────────────────┐
│ P1 — Faster-Whisper ASR                  │
│                                           │
│ audio                                     │
│   ↓                                       │
│ segments + words + probabilities          │
│ + ASR diagnostics + language + config     │
└────────────────────┬──────────────────────┘
                     │
                     ▼
┌───────────────────────────────────────────┐
│ TTK — deterministic evidence custody      │
│                                           │
│ SHA / canonical IDs                       │
│ windows + context halos                   │
│ packet hashes                             │
│ coverage                                  │
└────────────────────┬──────────────────────┘
                     │
                     ▼
             ACTIVE REASONING MODEL
                one Map pass/window
                     │
                     ▼
             TTK deterministic validate
                     │
                     ▼
             ACTIVE REASONING MODEL
                   Reduce
                     │
                     ▼
       deterministic grounding/coverage
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
 selective external       TTK compilation
 verification                  │
          │                     ▼
          └──────────► Operator Knowledge
```

## What happens to P2?

I would **not put the complete P2 engine in the production runtime simply because it exists**.

TTK already has:

- semantic contracts;
    
- Map/Reduce models;
    
- evidence IDs;
    
- source-support states;
    
- deterministic validators;
    
- stable claim IDs;
    
- wiki compilation.
    

Adding:

```text
TTK result
   ↓
P2 dataclass conversion
   ↓
P2 renderer
```

creates another schema translation and another failure surface without currently adding a unique capability.

### Instead, absorb P2's good ideas

Keep/reuse:

- `claim_type`;
    
- source-support vocabulary;
    
- strict external-verdict separation;
    
- empty protocol validity;
    
- its anti-fabrication regression tests.
    

Then align those fields directly into the TTK semantic contract.

**P2 can remain a reference implementation/test library rather than a mandatory production stage.**

This makes the hybrid simpler.

---

# H. Ranked next actions

|Rank|Recommendation|Impact|Evidence|Risk|
|--:|---|---|---|---|
|**1**|**Remove deterministic pseudo-semantic generation from `execute_ttk_lifecycle.py`** and restore active reasoning Map + Reduce|**High**|Directly observed in code and all four outputs|**Low–Medium**|
|**2**|**Fix benchmark truth conditions and provenance**: P2 pending must count incomplete; distinguish ASR vs synthesis; clean committed SHA required|**High**|Receipt + harness directly contradict each other|**Low**|
|**3**|**Add a forced fresh-ASR benchmark mode** and actually test new word timestamps/diagnostics|**High**|New writer exists; benchmark artifacts remain old|**Low**|
|**4**|**Make P1 JSON the canonical transcript evidence artifact and let TTK ingest it directly** instead of degrading to SRT|**High**|P1 now retains evidence TTK currently loses|**Medium**|
|**5**|**Add Reduce coverage accounting** so every Map window is represented or explicitly dismissed as non-material|**High**|Current 23-window Huberman Reduce retains only first 10 claims|**Medium**|
|**6**|**Require precise Micro provenance:** non-empty segment IDs + timestamp/range consistent with cited segment|**High**|P2 fields currently exist but are empty|**Low**|
|**7**|**Separate deterministic quote validity from semantic support.** `SUPPORTED` must be a semantic judgment, never inferred merely because a quote exists|**High**|Current P3 driver automatically sets every copied fragment `SUPPORTED`|**Low**|
|**8**|**Standardize verification vocabulary:** `verification_status` vs `external_verdict`; fix P1 URL-counting bug|**Medium**|Direct code evidence|**Low**|
|**9**|**Fresh benchmark ASR QA + selective repair**, especially proper nouns/German finance vocabulary|**Medium–High**|Persistent current transcript errors|**Medium**|
|**10**|**Do not add diarization, graph DB, vector DB, or another orchestration framework yet**|**Medium**|None addresses the current blockers|**Low**|

---

# I. The three gates I would require before hybrid implementation

### Gate 1 — genuine semantic P3 run

Run **all four sources** through actual reasoning-model Map + Reduce.

No deterministic transcript-copy substitute.

The compiled Macro should actually answer:

> What is this source fundamentally saying?

and Meso should contain actual semantic modules.

### Gate 2 — fresh ASR evidence run

Delete/bypass cached transcript artifacts and prove that new P1 outputs really contain:

```text
segment
  ├─ start/end
  ├─ avg_logprob
  ├─ no_speech_prob
  ├─ compression_ratio
  └─ words[]
       ├─ word
       ├─ start/end
       └─ probability
```

Only after that can the hybrid decide how much ASR QA/repair is worthwhile.

### Gate 3 — honest benchmark receipt

A successful receipt should require something like:

```text
ASR_COMPLETE
SOURCE_CUSTODY_VALID
MAP_COMPLETE
MAP_VALID
REDUCE_COMPLETE
GROUNDING_VALID
COVERAGE_VALID
OPERATOR_ARTIFACT_COMPLETE
```

for every pipeline stage being compared.

`SYNTHESIS_PENDING` must never result in `all_passed: true`.

---

## Bottom line

The **P1/P2 repair was successful**: the dangerous fabrication behavior is gone.

The **TTK core remains the strongest architecture**.

But the new P3 lifecycle wrapper accidentally reintroduced the same class of problem in a subtler form: instead of hallucinating domain-specific knowledge, it now produces **source-verbatim but semantically meaningless knowledge artifacts** that structural validators understandably accept.

That is the highest-priority correction.

After fixing it, I would unify around **P1 ASR + TTK custody/validation/compilation + the active reasoning model for Map/Reduce**, and **reuse P2's good schema ideas rather than force P2 itself into the production chain**. This is both simpler and more resilient than chaining all three engines.