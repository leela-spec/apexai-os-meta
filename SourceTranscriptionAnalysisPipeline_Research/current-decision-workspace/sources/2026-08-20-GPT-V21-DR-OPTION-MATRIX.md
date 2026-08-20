# GPT analysis capture — V2.1 × Deep Research overview matrix

**Captured:** 2026-08-20  
**Role:** immutable research source / conversation output snapshot  
**Authority:** research evidence only; later operator decisions override recommendations in this capture.

---

# V2.1 × Deep Research reconciliation

V2.1 is treated as the baseline design to dissect, not as something to blindly implement.

The named V2.1 paths on `main` became V3 supersession wrappers; the original V2.1 architecture and implementation plan remain under `v2-reuse-bakeoff/archive-pre-v3-authority/` and were used for the comparison.

A major evidence correction is that repository V2.1 selection/final-handover files claimed essentially complete/PASS execution, while the real operator outcome was no satisfactory working pipeline. Therefore those internal PASS labels are not accepted as product evidence.

The Deep Research report also stated that it could not retrieve the live V2/V2.1 project files during its run. Its recommendations therefore require reconciliation against the actual repository architecture rather than automatic authority.

## Rating system

| Rating | Meaning |
|---|---|
| **V1–V5** | Product value if the option works; V5 = critical/high leverage. |
| **E4** | Mature/publicly proven component or standard practice. |
| **E3** | Real, maintained, documented component; credible but not necessarily proven for this exact problem. |
| **E2** | Real technology, but new/vendor evidence/limited production history. |
| **E1** | Project-specific architectural hypothesis/custom integration. |
| **E0** | Unverified/effectively hallucinated. |
| **R1–R5** | Complexity/integration/operational risk; R5 = very high. |

`E3/1` means the tool itself is E3 but the proposed use/integration is only E1.

## V2.1 × Deep Research overview matrix

| Pipeline process | Option A — V2.1/simple path | Option B — V2.1 challenger | Option C — DR/external alternative | Starting position at capture time |
|---|---|---|---|---|
| **S0 Trigger / orchestration** | Thin Python/PS CLI runner — `V5 E4/3 R1` | APEX/OpenClaw first — `V2 E3/1 R4` | heavyweight workflow engine — `V1 E4/1 R5` | Keep thin deterministic runner; OpenClaw after product works. |
| **S1 Source acquisition** | yt-dlp + FFmpeg — `V5 E4 R1` | browser/manual fallback — `V2 E3 R3` | turnkey product ingestion — `V2 E3-4 R2` | Keep yt-dlp/FFmpeg. |
| **S2 Transcript / ASR** | faster-whisper — `V5 E4/2 R2` | Parakeet TDT 0.6B v3 — `V4 E3/2 R4` | Scribe v2 / Deepgram — `V5 E3/2 R2` | Reopen local vs hosted quality tradeoff. |
| **S3 Alignment / diarization** | no extra stage if sufficient — `V4 E4 R1` | WhisperX + pyannote — `V3 E3 R3-4` | hosted ASR built-in timing/diarization — `V4 E3 R1-2` | Conditional only. |
| **Visual-only evidence** | absent in V2.1 | full video indexing stack | conditional multimodal pass | At capture time proposed conditional addition; later operator decision moved this out of current scope. |
| **S4 Canonical source / custody** | TTK custody — `V5 E1-2 R3` | database/vector store — `V1 E4/1 R4` | thin canonical source package — `V5 E4/2 R2` | Preserve requirements, not automatic TTK ownership. |
| **S5 Chunking / processing windows** | TTK 700–1500-word windows + halo — `V4 E1 R3` | generic chunkers / DocETL split/gather — `V2 E3/1 R3-4` | LangExtract native long-doc chunking + parallel multipass — `V5 E3/3 R2` | If LangExtract wins, likely let it own extraction chunking. |
| **S6 Pre-extraction** | none — `V4 E4 R1` | GLiNER2 — `V2-3 E3/1 R3` | NuExtract — `V2 E3/1 R4` | Default none; test only if a measured gap exists. |
| **S7 Grounded semantic extraction** | direct strong CLI — `V4 E4/2 R2` | LangExtract + homemade subscription-CLI provider — `V5 E3/1 R4` | LangExtract + supported/native provider — `V5 E3/3 R2` | Native/supported provider leading; custom CLI integration downgraded. |
| **S8 Structured output / retry** | provider-native schema + deterministic validation — `V5 E4 R1-2` | Instructor/Pydantic — `V3 E3 R3` | custom parser/retry wrapper — `V1 E1 R4` | Native first; Instructor only if measured need. |
| **S9 Deterministic provenance validation** | TTK validator — `V5 E1-2 R2` | LangExtract source locations — `V4 E3 R1-2` | small generic validator — `V5 E4/2 R1-2` | Keep valuable exact invariants; implementation open. |
| **S10 Semantic source-support** | strong semantic worker — `V5 E4/2 R2` | mDeBERTa/HHEM advisory — `V2-3 E3/1 R3` | explicit bounded source-support review — `V5 E3/2 R2` | Strong semantic gate first; specialists only if measured. |
| **S11 Global synthesis / Reduce** | direct strong CLI over compact evidence ledger; raw transcript forbidden — `V5 E4/1 R3` | DocETL — `V4 E3/1 R4` | full source + grounded evidence with long-context model — `V5 E3/2 R2` | Major architecture decision to revisit; evidence-only restriction was project invention. |
| **S12 External factual verification** | selective TTK queue + CLI web tools — `V4 E4/2 R3` | verify everything — `V1 E1 R5` | selective search-grounded model route — `V4 E3/2 R2` | Keep selective and separate from source support. |
| **S13 Compilation / knowledge output** | TTK compiler — `V5 E1-2 R2-3` | Fabric/Open Notebook view — `V3 E3 R3` | small deterministic compiler/templates — `V5 E4/2 R1` | Compiler should be boring; reuse selectively. |
| **S14 Product evaluation** | TTK validators + human gold/checklists — `V5 E3 R2` | DeepEval + NLI/HHEM — `V2-3 E3 R3` | must-find checklist + human review + strong product baseline — `V5 E4/3 R2` | Product artifact quality outranks receipts. |
| **Resume/recovery** | TTK packet/result/hash state — `V4 E1-2 R3` | full workflow engine — `V2 E4/1 R5` | tiny stage manifest + hashes — `V4 E4/2 R1-2` | Minimal state unless actual requirements prove need for more. |

## Public evidence vs architectural invention

Several V2.1 components are real, maintained tools: faster-whisper, Parakeet, WhisperX, GLiNER2, DocETL, mDeBERTa, LangExtract and others.

The key problem is that **a real component does not make the proposed project composition battle-proven**.

Examples:

- LangExtract is real and provides exact source grounding, long-document chunking, parallel processing and multiple extraction passes.
- But `TTK window → LangExtract → custom subscription-CLI provider plugin → TTK translation` is a project-specific architecture.
- DocETL is real.
- But `TTK evidence → DocETL → custom subscription CLI adapter → TTK Reduce` is likewise project-specific.

This distinction is retained as a governing rule in the current decision workspace.

## Five high-impact decisions identified in the capture

### A — ASR local-first vs quality-first

V2.1 centered on faster-whisper with Parakeet challenger. DR proposed trustworthy existing transcript first, otherwise strong hosted ASR, with local ASR when locality/offline/privacy warrants it.

This is a cost/privacy/quality/complexity tradeoff and must be benchmarked rather than assumed.

### B — TTK windows vs LangExtract native long-doc process

If LangExtract is selected, pre-windowing everything through TTK may duplicate LangExtract's own long-document chunking, parallel processing and multiple passes.

Initial capture recommendation: let LangExtract own extraction chunking unless a measured gap says otherwise.

### C — LangExtract native provider vs custom CLI adapter

A custom provider is technically supported, but possible ≠ proven. Native provider routes reduce custom semantic transport code.

Initial capture recommendation: do not start with a custom CLI provider adapter.

### D — Evidence-only Reduce vs full-source global reasoning

V2.1 forbade the Reduce stage from rereading the complete transcript. This makes Map omissions unrecoverable.

DR proposed complete source + grounded evidence for global synthesis.

This was identified as one of the highest-leverage architecture choices and is now explicitly scheduled for an empirical three-way test in the current workspace.

### E — Evaluation must measure actual product value

The old implementation produced extensive PASS machinery without a satisfactory product. The evaluation target therefore must be the artifact itself: important-insight retention, usefulness, faithfulness, uncertainty/corrections, source traceability where required, EN/DE performance, and comparison with strong existing product baselines.

## Candidate responsibility map at capture time

```text
INPUT
 URL / media / trustworthy transcript
        │
        ▼
1. acquisition
   yt-dlp / local file / FFmpeg if needed
        │
        ▼
2. transcript selection / ASR
        │
        ▼
3. canonical source
        │
        ▼
4. grounded extraction
   LangExtract candidate
        │
        ▼
5. global synthesis
   compare full source / evidence / both
        │
        ▼
6. source-support as required
        │
        ▼
7. selective external verification if required
        │
        ▼
8. deterministic compile
        │
        ▼
9. product evaluation off hot path
```

This was explicitly a candidate responsibility map, **not a decision to force the pipeline to nine steps**.

## Capture conclusion

The correct synthesis of the historical work was:

> **V2.1 candidate knowledge + Deep Research + V3 selection rules**

with components promoted only by real output evidence and no sunk-cost authority.