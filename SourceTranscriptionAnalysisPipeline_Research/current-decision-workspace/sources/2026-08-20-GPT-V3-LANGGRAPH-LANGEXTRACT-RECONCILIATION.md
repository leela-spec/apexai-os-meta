# GPT analysis capture — V3, LangGraph, LangExtract, local/cloud reconciliation

**Captured:** 2026-08-20  
**Role:** immutable research source / conversation output snapshot  
**Authority:** research evidence only; later operator decisions override recommendations in this capture.

---

You’re right. **“Can it be reduced?” is a diagnostic question, not a design instruction.** I had turned simplification into the objective. The objective stays: **maximum product value, reliability, and reuse of proven systems.** A stage disappears or gets merged only when we can show that doing so does **not** remove useful capability.

I checked V3, the original V2.1 material, the deep-research report, LangGraph, and current LangExtract documentation again.

# 1. What V3 actually adds

V3 does **not** provide a materially different finished transcript→knowledge algorithm. Its strongest contribution is a much better **decision process for selecting the algorithm**.

V3 explicitly says V2.1 made a mistake by freezing a bespoke 15-stage architecture before proving whether existing systems could solve larger portions of the problem. Its replacement principle is:

> find proven systems → run them → compare actual products → identify gaps → benchmark components only for those gaps → integrate the smallest winning composition.

That is worth preserving.

| V3 idea | Material value to our current work | Keep? |
|---|---:|---|
| **Complete/near-complete systems before components** | **Very high.** Directly attacks the recurring “AI invents infrastructure” failure. | **YES** |
| **TTK becomes candidate, not sacred core** | **Very high.** V3 explicitly says retain only pieces that demonstrate value. | **YES** |
| **Candidate ≠ production component** | **Very high.** LangExtract, DocETL, WhisperX etc. must earn their position. | **YES** |
| **Custom-code authorization test** | **Very high.** Existing solution must fail before custom abstraction is authorized. | **YES** |
| **Product-first tests** | **Very high.** Run real source and inspect actual knowledge before building more infrastructure. | **YES** |
| **Two-strike stop rule** | High. Stops endless repairs. | **YES** |
| **One source first → finalists → EN/DE corpus** | High. Much cheaper than repeatedly rerunning everything. | **YES** |
| **8 V3 execution modules instead of 15 stages** | Useful for *development organization*, but it tells us nothing about how many runtime processes the product needs. | **DO NOT CONFUSE WITH PRODUCT PIPELINE** |
| **OpenClaw → Antigravity relay** | Little value to the transcript algorithm itself. It is control-plane infrastructure. | **KEEP OUT OF PRODUCT DECISION FOR NOW** |

One particularly important finding: **V3 never got to the point where its M01 “proven systems” selection produced results in the repository.** The V3 directory currently contains architecture, plan, registry, orchestration docs and execution modules, but no results directory or completed product-selection evidence.

So:

**V3 gives us better rules. It does not give us a proven winning pipeline.**

That means our current matrix should become:

> **V2.1 candidate knowledge + DR research + V3 selection rules.**

Not V3 blindly replacing V2.1.

---

# 2. LangGraph was missing — and it should be in the matrix

There are two very similarly named things here:

| | **LangExtract** | **LangGraph** |
|---|---|---|
| What is it? | **Information-extraction library** | **Workflow/orchestration runtime** |
| Solves | “What valuable information is in this text, and where exactly did it come from?” | “Which pipeline step runs next, what state exists, what happens after failure, and how do I resume?” |
| Controls an AI? | It constrains an LLM extraction task | It controls **workflow execution**, including AI and non-AI functions |
| Does semantic reasoning itself? | No — an LLM underneath does | No |
| Can run locally? | **Yes**, library is local; can use local Ollama model | **Yes** |
| Cloud/API required? | No if Ollama; yes if Gemini/OpenAI | No |
| Relevant to distrust of autonomous CLI agents? | **Partially** | **Very much** |
| Potential place in pipeline | Knowledge extraction | Pipeline controller/resume/fallback |

LangGraph is a low-level runtime for **stateful, durable workflows**. It provides checkpoints, failure recovery, explicit nodes/edges, persistence and human intervention. It does not require an AI agent to decide what to do next.

For example:

```text
INGEST
   ↓
TRANSCRIBE
   ↓
EXTRACT
   ↓
SYNTHESIZE
   ↓
VALIDATE
   ↓
COMPILE
```

Those are actual functions/nodes.

LangGraph stores state after completed nodes. If `SYNTHESIZE` fails, it can resume there instead of asking some CLI AI to figure out where the run was.

### Why wasn't it in the previous matrix?

Because neither V3's pipeline component registry nor the DR prime recommendation selected LangGraph. The repository does contain LangGraph material in imported source knowledge, but it was never promoted into the transcript-pipeline architecture.

That explains the omission, but **it does not justify excluding it now**.

### Corrected position on LangGraph

**Add it to the matrix as an orchestration/resume option. Do not automatically adopt it.**

| Orchestration option | Value | Evidence | Complexity | Position |
|---|---:|---:|---:|---|
| Plain Python sequential runner | High | Very high | **Low** | Reference |
| **LangGraph** | **High if resume/branching/fallbacks matter** | **Very high**; mature framework for durable workflows | Medium | **Serious challenger** |
| Custom TTK workflow/state machinery | Potentially high | Low/project-specific | Medium-high | Must justify itself |
| Autonomous CLI AI decides workflow | Potentially high | low observed reliability in project | High operational risk | Avoid as production controller unless it earns role |
| OpenClaw controller | Useful external process supervisor | Real software | Medium | Integration later, not semantic pipeline core |

LangGraph becomes especially attractive if retries, fallback ASR, conditional processing, resumability and human checkpoints are required.

If the final workflow is only a few simple functions that almost never branch, plain Python may still be better.

**Decide from actual workflow requirements, not from “simpler = better.”**

---

# 3. What LangExtract actually does

LangExtract is **not an AI agent** and it does not send an instruction to Claude Code and hope Claude figures everything out.

Its actual pipeline is roughly:

```text
your transcript
      ↓
LangExtract
      ↓
splits long text into manageable pieces
      ↓
asks an LLM a narrowly defined extraction question
      ↓
can repeat extraction several times for higher recall
      ↓
merges structured results
      ↓
maps every extracted item back to the
exact character position in the transcript
      ↓
structured grounded extraction
```

Its documented long-document functionality includes chunking, parallel processing and multiple extraction passes.

### Concrete example

Suppose the source says:

> “Our margin fell from 31% to 27%, primarily because energy costs increased. We expect this to normalize next quarter, although that depends on gas prices.”

We give LangExtract a predefined extraction specification such as:

```text
Extract:
- factual claims
- numbers
- causal mechanisms
- forecasts
- uncertainty/qualifications
- corrections
- contradictions
```

LangExtract might return conceptually:

```json
{
  "type": "causal_claim",
  "claim": "Higher energy costs caused margin compression",
  "source_text": "primarily because energy costs increased",
  "char_start": 42,
  "char_end": 83
}
```

Plus separate structured objects for the 31%→27% change, forecast, and qualification.

The **LLM still interprets the source**.

What LangExtract adds is machinery around that model:

**schema + task examples + chunking + repeated passes + parallelism + exact source-position grounding + structured output.**

It cannot guarantee that an LLM interpretation is correct merely because cited words exist. It gives stronger **mechanical discipline** around an LLM, not mathematical semantic correctness.

---

# 4. What does “LangExtract with Gemini provider” mean?

It means an API.

LangExtract ships with provider implementations including Gemini, Ollama and OpenAI.

```text
Python pipeline
      ↓
LangExtract library       ← runs locally
      ↓
Gemini provider           ← code supplied by LangExtract
      ↓
Gemini API                ← runs in Google cloud
      ↓
model response
      ↓
LangExtract grounding/
merging/structuring        ← runs locally
```

There is **no CLI AI involved** in that route.

### Fully-local variant

```text
Python
  ↓
LangExtract
  ↓
Ollama
  ↓
local LLM
```

No API key and no cloud required.

The unresolved question is not whether this path exists. It is:

> **Can a local model that runs acceptably on the operator machine provide enough semantic quality for this extraction task?**

That needs a real test.

### LangExtract → Claude Code/Codex/Antigravity CLI

LangExtract has a custom-provider plugin mechanism. But the specific CLI provider would be **custom project code unless a maintained existing plugin is found**.

Therefore do not start there under the reuse-before-invention rule.

---

# 5. Can 14 stages be reduced?

Correct answer:

## **Probably operationally, but it has not yet been proven which ones should disappear.**

Several V2.1 stages are separate **responsibilities** that could happen inside one proven component.

For example, LangExtract itself can cover:

```text
chunking
+ repeated semantic extraction
+ structured output
+ source-span grounding
```

V2.1 represented these concerns across parts of S5, S7, S8 and S9.

That does **not** mean validation is unnecessary. It means four conceptual responsibilities may not require four separately engineered subsystems.

| V2.1 stages | Responsibility | Could be one runtime process? | Should capability disappear? |
|---|---|---:|---:|
| S0 + S1 | Start job + obtain source | **Yes, probably** | No |
| S2 + S3 | Transcript + timestamps/speakers | **Yes, if ASR provides all three** | No |
| S4 | Canonical source identity/provenance | Could be lightweight | **No** |
| S5 | Chunking/windowing | **Possibly absorbed by LangExtract** | Chunking still happens |
| S6 | GLiNER2 pre-extraction | Entirely optional | **Possibly yes** |
| S7 + S8 | Semantic extraction + structured result | **Yes** | No |
| S9 | Mechanical evidence validation | Could run inside extraction module | **No** |
| S10 | Semantic source-support review | Could potentially be combined with extraction/review | Depends on trust mode |
| S11 | Global synthesis | Distinct semantic task | **Probably keep** |
| S12 | External truth verification | Conditional/off-path | **Not every run** |
| S13 | Compile/output | Could be tiny | **Keep** |
| S14 | Evaluation | **Not production hot path at all** | Keep as testing |

So there may eventually be fewer operational nodes while retaining more conceptual responsibilities.

This is different from arbitrarily shrinking the pipeline.

---

# 6. Everything discussed: local vs external/paid

| Component | What it does | Completely local possible? | API/cloud/payment? |
|---|---|---:|---|
| **yt-dlp** | Downloads media | ✅ | No |
| **FFmpeg** | Media conversion | ✅ | No |
| **faster-whisper** | ASR | ✅ | No per-use cost |
| **Parakeet TDT** | ASR | ✅ | No per-use cost; heavier local stack |
| **WhisperX** | Alignment | ✅ | Local after model download |
| **pyannote** | Diarization | ✅ inference | Model access/download may require Hugging Face account/token |
| **TTK** | Current custom custody/windows/validation/compiler | ✅ | No |
| **LangExtract library** | Extraction orchestration + grounding | ✅ | Library itself free/open source |
| **LangExtract + Ollama** | Grounded extraction with local LLM | ✅ **fully local** | No |
| **LangExtract + Gemini** | Grounded extraction | ❌ | **Gemini API** |
| **LangExtract + OpenAI** | Grounded extraction | ❌ | **OpenAI API** |
| **LangGraph** | Workflow/state/resume/retries | ✅ | Open-source runtime; LangSmith cloud optional |
| **GLiNER2** | Local entities/relations/schema extraction | ✅ | No |
| **NuExtract** | Local schema extraction | ✅ | No, but bigger local model |
| **mDeBERTa** | Local entailment warning | ✅ | No |
| **HHEM** | Local hallucination/consistency signal | ✅ | No |
| **Instructor** | Output/schema/retry library | ✅ library | Model underneath may be local or paid |
| **DocETL** | LLM ETL/orchestration | ✅ framework | Model underneath depends on provider |
| **Gemini 3.7 Flash** | Long-context synthesis / video / verification | ❌ | **Paid cloud API** |
| **ElevenLabs Scribe v2** | Hosted ASR | ❌ | Paid hosted service |
| **Deepgram Nova-3** | Hosted ASR | ❌ | Paid cloud API |
| **NotebookLM** | Whole-product benchmark | ❌ | Google cloud service |
| **Claude Code CLI** | Semantic model/client | ❌ inference | Subscription/account-backed cloud model |
| **Codex CLI** | Semantic model/client | ❌ inference | Subscription/account-backed cloud model |
| **Antigravity CLI** | Agent/executor | ❌ inference | Account/cloud-backed semantic execution |
| **OpenClaw** | Local orchestration/process shell | ✅ framework | Invoked semantic model may be external |
| **Web factual verification** | External truth checking | ❌ | Requires internet/provider |

The DR recommended design is therefore not local-only. A fully-local counterpart is technically possible:

```text
yt-dlp/ffmpeg
   ↓
faster-whisper / Parakeet
   ↓
LangExtract
   ↓
Ollama local model
   ↓
local synthesis model
   ↓
local deterministic compile
```

But there is not yet evidence that local semantic models give sufficient knowledge quality.

---

# 7. ASR, explained

ASR means only: **turn spoken audio into trustworthy text.**

Everything after it depends on the transcript. If “15 percent” becomes “50 percent,” later semantic quality cannot repair the source corruption reliably.

| | Existing trustworthy transcript | Scribe v2 | Deepgram Nova-3 | faster-whisper | Parakeet |
|---|---|---|---|---|---|
| Input | transcript | audio | audio | audio | audio |
| Output | text/timestamps if supplied | text + word timing + speaker information | text + timing; diarization available | segments/words/timing/confidence | text + timestamps |
| Runs where? | Local | cloud | cloud | **Local** | **Local** |
| Integration | very low | low | low | medium | higher |
| Per-use cost | none | paid | paid | none | none |
| Privacy | highest | audio uploaded | audio uploaded | local | local |
| Infrastructure | almost none | API key + upload | API key + upload | model + Python/CTranslate2 | heavier model/runtime stack |

The actual decision is:

> **How much external dependency are we willing to accept in exchange for simpler operation and potentially better transcription?**

This should be resolved from a small difficult EN/DE same-fixture benchmark, not vendor claims.

---

# 8. Only use something actually built

Rule:

> **Every capability must initially be owned by an existing maintained product/library/model. Custom code may connect components, translate formats, or compile outputs, but may not invent a capability that an existing solution already provides.**

Examples:

```text
✅ small conversion between existing schemas
✅ LangGraph node calling LangExtract
✅ deterministic hash
✅ output Markdown template

❌ custom semantic chunking system when LangExtract already does it
❌ custom retry/workflow framework when LangGraph already exists and fits
❌ custom CLI-LangExtract provider unless no existing provider satisfies requirement and value justifies it
❌ custom ASR
❌ custom diarization
❌ custom semantic support classifier when existing alternatives cover the role
```

---

# 9. LangExtract choices

### LangExtract + Gemini

```text
transcript
   ↓
LangExtract   [LOCAL CODE]
   ↓
Gemini API    [CLOUD AI]
   ↓
LangExtract   [LOCAL grounding/merging]
   ↓
structured evidence
```

Value: straightforward supported route. Risk: paid/cloud dependency. Custom invention: low.

### LangExtract + Ollama

```text
transcript
   ↓
LangExtract   [LOCAL]
   ↓
Ollama        [LOCAL]
   ↓
local LLM
   ↓
structured evidence
```

Value: fully local supported route. Risk: semantic quality may be lower. Custom invention: low. Deserves real benchmark.

### LangExtract + Claude/Codex/Antigravity CLI

```text
LangExtract
   ↓
our provider plugin
   ↓
CLI
   ↓
cloud model
```

Value: could reuse subscriptions. Risk: recreates unstable CLI automation seam. Not preferred starting option unless it earns substantial value.

---

# 10. Full-source synthesis explained

After extraction we may have hundreds of evidence units. The final synthesis can receive:

| Approach | Model sees | Advantage | Main danger |
|---|---|---|---|
| **Full transcript only** | original transcript | maximum context; simplest | important needles can be missed; grounding weaker |
| **Evidence only** | extracted evidence | compact, focused, cheaper | anything extraction missed is permanently invisible |
| **Full transcript + extracted evidence** | both | extraction acts as attention/index while source remains recoverable | more context/cost |

If LangExtract misses an important correction, evidence-only synthesis cannot recover it. Full-source+evidence may still recover it because the original transcript remains available.

Current hypothesis was full-source+evidence, but it must beat alternatives on real source output.

---

# 11. Updated pipeline hypothesis — without prematurely shrinking it

```text
[ORCHESTRATION]
plain deterministic Python
vs
LangGraph
        │
        ▼
[1 SOURCE / INGEST]
yt-dlp + FFmpeg
        │
        ▼
[2 TRANSCRIPT]
existing trustworthy transcript
vs hosted ASR
vs faster-whisper / Parakeet
        │
        ▼
[3 SOURCE CUSTODY]
TTK functions
vs thin canonical representation
        │
        ▼
[4 GROUNDED EXTRACTION]
LangExtract + strong external provider
vs LangExtract + local Ollama
vs direct model control
        │
        ▼
[5 GLOBAL KNOWLEDGE SYNTHESIS]
full source
vs evidence only
vs full source + evidence
        │
        ▼
[6 TRUST]
source-support validation as required by product mode
+
conditional external factual verification
        │
        ▼
[7 OUTPUT]
deterministic knowledge compiler
        │
        ▼
[EVALUATION — OFF PRODUCTION PATH]
real source checklist
+ human inspection
+ strong existing product comparison
```

This is **not a decision to make it seven steps**. It is a responsibility map. Additional pieces stay when they demonstrate product value.

The next decision at that time was orchestration before ASR because distrust of CLI AI materially changes who owns pipeline state. That recommendation is now superseded in part by the operator decisions recorded in `../02-DECISIONS.md`.