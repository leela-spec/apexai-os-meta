# Transcript → Knowledge Production Decision Package

## Executive decision and evidence posture

**Decision:** use a **proven-component composition**, not a new bespoke TTK architecture and not a single closed “AI summarizer.” The production path with the strongest current case is:

```text
video / audio / existing transcript
        ↓
yt-dlp / local file ingestion
        ↓
FFmpeg only when normalization is needed
        ↓
existing trustworthy transcript
    OR ElevenLabs Scribe v2 ASR
        ↓
canonical source package
(transcript + words/segments + timestamps + speakers + hashes + provenance)
        ↓
LangExtract high-recall, multi-pass, source-span-grounded extraction
        ↓
grounded semantic evidence units
        ↓
Gemini 3.7 Flash full-source global synthesis
        ↓
source-support gate
        ↓
optional external factual verification
        ↓
deterministic compilation
        ↓
knowledge.md + knowledge.json + evidence.jsonl + source.json
```

For video in which slides, demonstrations, charts, code on screen, or other visuals carry material information that is absent from speech, add a **conditional Gemini 3.7 Flash visual-evidence pass** rather than pretending that the transcript alone represents the source. Gemini 3.7 Flash is now GA, accepts text, image, video, audio and PDF, has a 1,048,576-token input limit and 65,536-token output limit, supports structured outputs and search grounding, and was released on August 13, 2026. citeturn24search0turn24search1turn24search3turn24search7

**Confidence: medium-high.** The individual responsibilities can be handed to mature or credible existing systems; the uncertainty is not whether those systems execute, but whether this exact composition reaches the project's unusually demanding whole-product semantic-recall target on the project's real English and German material. There is no current public benchmark I found that measures the full target—important-insight recall, mechanisms, procedures, qualifications, corrections, contradictions, epistemic status and exact evidence—over hours-long EN/DE conversational material. That last claim is therefore an **inference from the research landscape**, not a benchmark result.

**Expected product quality:** substantially above a conventional “summary pipeline.” LangExtract exists specifically to perform structured extraction tied to exact source character offsets and uses chunking, parallelism and multiple passes for long-text extraction; Google's own explanation notes that multi-fact recall can decline even when a model technically has sufficient context, which is the reason not to rely on a single giant-prompt extraction pass. Gemini 3.7 Flash then provides a separate global reasoning pass with enough context to see the complete transcript and the extracted evidence together. citeturn21search2turn21search5turn24search1

**Reuse level:** high. Acquisition, media conversion, ASR, diarization/timestamps, long-document extraction, model reasoning and schema-constrained generation are all existing capabilities. The remaining custom ownership is deliberately small: a canonical source/evidence contract, deterministic offset-to-time mapping, an idempotent stage manifest, and final rendering templates. No custom ASR, diarizer, chunker, extraction engine, RAG framework, knowledge-graph model, LLM orchestrator or evaluation platform is justified.

**Largest risks:** first, semantic completeness must still be demonstrated on the real corpus. Second, LangExtract proves that the cited text span exists; it does **not** prove that every model-generated normalized interpretation is logically entailed by that span. Third, hosted ASR quality on domain-specific German vocabulary needs a representative-source gate rather than reliance on vendor accuracy claims. Fourth, Gemini 3.7 Flash is GA but only six days old as of August 19, 2026; the Gemini API is mature, but this exact model has little production history yet. citeturn21search2turn24search3turn24search7

**The closest existing whole product is NotebookLM / Gemini Notebook Enterprise.** NotebookLM already ingests documents, public YouTube transcripts and audio; supports source-grounded answers with inline citations; works across more than 80 languages; and creates notes, study/briefing artifacts and related notebook outputs. Google has also upgraded NotebookLM's long-document analysis stack. citeturn1search0turn1search1turn1search3turn1search4turn1search8 The reason it does **not** win as the sole production engine is automation control: the documented Gemini Notebook Enterprise `v1alpha` API currently exposes notebook, source/discovery and Audio Overview services, but I did not find a documented API service for programmatically running the core notebook chat/report/note-generation workflow. The API is also Preview/Pre-GA. That is a production-contract gap, not a criticism of NotebookLM's interactive knowledge quality. citeturn2search3turn2search4turn13view2

**NotebookLM should therefore become the reference baseline, not the core engine.** A selected vertical slice should be run through both this architecture and NotebookLM. If the proposed production artifact cannot beat or at least match NotebookLM on substantive recall while adding the required structured evidence and automation, the selected pipeline has failed its product objective.

**Evidence-class audit**

| Evidence class | Status in this research |
|---|---|
| **PROJECT EVIDENCE** | The prompt itself establishes that earlier work considered faster-whisper, WhisperX, LangExtract, DocETL, GLiNER2, TTK, various runners/schemas/compiler/evaluation machinery, and OpenClaw/Claude/Codex/Antigravity execution. The actual V1/V2/V2.1/V3 source documents were **not retrievable from the supplied project sources in this run**; file retrieval returned no available project sources. I therefore do not invent their topic-level conclusions. |
| **CURRENT EXTERNAL EVIDENCE** | Current official documentation, repositories, releases, pricing, API surfaces and current product documentation were searched across the principal end-to-end products, agent ecosystems and specialist components discussed below. |
| **INFERENCE** | No presently verified automated whole product simultaneously offers the desired semantic richness, high-recall long-source extraction, exact inspectable source evidence, EN/DE breadth, open programmatic output contract and recovery behavior. |
| **RECOMMENDATION** | Compose proven specialists, keep the original source representation authoritative, use LangExtract for high-recall evidence acquisition, use a frontier long-context model for global reasoning, and own only thin deterministic glue. |

This recommendation gives **zero architectural preference to existing TTK code**. Any existing TTK module should survive implementation only if it happens to match one of the small retained responsibilities and passes the same acceptance tests.

## Existing whole-pipeline landscape and reusable ecosystems

The research found several genuine Transcript→Knowledge or near-complete products. None should be dismissed simply because it uses different terminology.

| Candidate | Actual product and coverage | Grounding / semantic depth | EN/DE and long-source suitability | Maturity | Locality, cost, Windows, recovery | Verdict |
|---|---|---|---|---|---|---|
| **NotebookLM / Gemini Notebook Enterprise** | Source ingestion → notebook understanding → cited Q&A → notes/guides/briefings and other artifacts. Audio is transcribed on import; public captioned YouTube sources and large text/document sources are supported. citeturn1search0turn1search1turn1search8 | Strongest verified whole-product grounding in this landscape: notebook answers use source citations. It is a real knowledge product rather than merely an ASR summarizer. citeturn1search1turn1search4 | 80+ output languages and up to 500,000 words per source are documented. citeturn1search0turn1search4 | **BP4 interactive product; BP2 automation API.** The product is mature; the Enterprise API is `v1alpha` Preview. citeturn2search3turn2search4 | Cloud. Enterprise is currently advertised at $9/user/month and provides additional security/control features. citeturn17search5turn17search9 | **Best interactive baseline; do not make it the only production engine until programmatic artifact-generation APIs exist.** |
| **Podwise** | Podcast/audio/YouTube/RSS → transcript, summary, mind map, highlights/insights, Q&A and export. It now exposes CLI, Open API, MCP and installable agent skills. citeturn18search1turn18search3turn18search5turn18search12 | Search results and episode answers can point to moments/timestamps, but the published product contract is not a claim-by-claim evidence ontology preserving every mechanism, qualification, correction and contradiction. citeturn18search3turn18search10 | Advertises processing in 12 languages and accepts audio uploads; excellent podcast fit but narrower than arbitrary long-document/video knowledge. citeturn18search3 | **BP3.** Podwise currently claims 109,000+ listeners and 2,000+ reviews; its API/agent documentation is actively updated. Those adoption figures are vendor-reported. citeturn18search3turn18search11 | Hosted. Pro is $19.90/month monthly, or $142.80/year at the published annual price; API/CLI/skills are included on Pro. citeturn18search0turn18search8 | **Excellent near-complete podcast product; insufficient evidence contract and source breadth for the core target.** |
| **Recall** | YouTube/podcast/web/document → summaries and connected personal knowledge/notes. | Valuable personal knowledge workflow, but no verified production-grade span-grounding/output contract was found in the reviewed material. | Broad content-oriented product; exact EN/DE and programmatic production guarantees are not strong enough for this selection. | **BP3 product.** | Hosted, consumer/PKM orientation. | **Useful benchmark for knowledge UX, not production core.** |
| **Fabric** | Mature open-source CLI/pattern framework; directly processes YouTube material and ships patterns aimed at extracting “wisdom,” study notes and summaries. It is available on Windows as well as macOS/Linux. citeturn15search2turn15search6 | Semantic quality is fundamentally prompt/model dependent. The framework does not establish the exact-span evidence contract or whole-product completeness required here. | Model-dependent; can process long text through patterns, but no target-specific EN/DE validation was found. | **BP4 framework**, based on long-lived implementation, thousands of commits and broad tooling; the particular transcript knowledge patterns themselves should not be assigned BP4 semantic reliability merely because Fabric is mature. citeturn15search2turn15search6 | Open-source MIT, cross-platform. Provider costs depend on chosen model. citeturn15search2 | **Superb rapid baseline and operator tool; not a trust architecture.** |
| **Azure AI Video Indexer / Content Understanding** | Media → multilingual transcript, speaker diarization, timing, topics/keywords/entities/OCR and structured JSON; Content Understanding exposes audiovisual transcript phrases, timing, keyframes and structured audiovisual elements. citeturn15search0turn15search1turn15search4 | Strong media-level indexing and structured signals. It does not by itself establish the deep argument/mechanism/correction/caveat synthesis artifact requested here. | Video Indexer documents transcription/translation in 50+ languages and multilingual identification; speaker attribution is built in. citeturn15search0 | **BP4 media service.** | Hosted Azure service. Strong operational option where an Azure estate already exists. | **Strong alternative for source representation; not sufficient as the product brain.** |
| **VideoDB** | Video perception/indexing across transcript, vision/OCR and timed retrieval; agent skills make the index callable from coding agents. | Its key strength is retrieval of video moments/evidence rather than final global knowledge synthesis. | Attractive when visual/video retrieval is a dominant requirement. | **BP2–BP3**, credible and real but less established than Azure/Google media platforms. | Hosted service plus agent integrations. | **Use if the future product becomes an evidence-search/video-RAG system; not needed for the present single-source artifact pipeline.** |
| **LlamaExtract v2** | Text/PDF/image → schema-constrained structured extraction through UI, Python/TS SDK or REST API; v2 supports date-pinned configurations for production. citeturn17search12turn17search8 | Supports source citations and confidence scores, with Agentic/Agentic Plus quality tiers. citeturn10search5 | Good general document extraction; it is not itself an audio/video transcript knowledge product. | **BP3.** LlamaIndex is established, while this generation of Extract is newer. | Hosted/usage-based. Text is billed in 600-token “page” equivalents and extract tiers consume credits; EU credit pricing is documented. citeturn17search0turn17search4 | **Strong paid alternative to LangExtract, especially for fixed-schema business extraction; not enough evidence that it is superior on open-ended conversational insight recall.** |

A particularly important result from this landscape is that **product maturity and product fit diverge**. Azure Video Indexer is far more battle-proven than a new semantic extraction library, but it primarily solves media indexing. Fabric is highly mature as an AI workflow framework, but a prompt pattern is not equivalent to traceable semantic extraction. Conversely, LangExtract has a shorter operating history but directly targets the exact problem of structured information tied to source positions. citeturn15search0turn15search6turn21search2

**Agent/platform ecosystems.** OpenClaw has real native media infrastructure: its media-understanding layer can select providers and local CLI fallbacks, transcribe audio, understand video, retry alternate configured models and work on Windows on a best-effort basis. Its own documentation explicitly describes media understanding as **best-effort** and says failures do not block the normal reply flow. That makes OpenClaw useful as an invocation/integration shell, but exactly the wrong semantic trust boundary for a pipeline where missing media understanding must be visible and fail the stage. citeturn19search4turn19search7

The strongest reusable OpenClaw/agent discovery I found is actually **Podwise's cross-platform skill/CLI/MCP**, which is documented for agent workflows and can be installed for environments including OpenClaw and coding agents. citeturn18search1turn18search12 Community YouTube/transcript skills exist as well, but the ones surfaced in the research are substantially thinner transcript/summary wrappers rather than a source-grounded semantic pipeline.

Claude Code/Claude Agent infrastructure has checkpoints, hooks, subagents and an SDK for custom agentic workflows, and Anthropic has demonstrated reusable plugin/template packaging in other domains. citeturn20search3turn20search5 Codex now has formal Plugins and Skills; OpenAI describes Skills as reusable workflow folders around MCP tools, and its June 2026 plugin release bundled 110 skills across role-specific plugin collections. citeturn19search2turn19search5turn19search8 Google Antigravity 2.0 similarly exposes desktop/CLI/SDK surfaces, custom instructions/skills and persistent isolated agent environments. citeturn19search3turn19search6

**Research inference:** I did not find a first-party OpenClaw, Claude Code, Codex or Antigravity bundled workflow whose documented responsibility is the complete high-recall, evidence-linked Transcript→Knowledge target defined in the prompt. These ecosystems should therefore package or invoke the chosen pipeline; they should not dictate its semantic architecture.

**Paid/cloud option analysis.** Scribe v2 currently costs $0.22/hour for prerecorded STT; keyterm prompting is an additional $0.05/hour. Deepgram's current prerecorded Nova-3 Multilingual rate is $0.0052/minute and AssemblyAI Universal-3.5 Pro is $0.21/hour before optional add-ons. Gemini 3.7 Flash is currently $0.75/1M input tokens and $3.75/1M output tokens through December 31, 2026. citeturn16search0turn16search1turn16search2turn24search0turn24search3 LlamaIndex charges $1.25/1,000 credits in Europe and North America with tier-dependent extraction consumption. NotebookLM Enterprise is advertised at $9/user/month. citeturn17search0turn17search5

```yaml
paid_options:
  - option: ElevenLabs Scribe v2
    additional_product_value: high-quality hosted EN/DE-capable source transcription with word timing, diarization and terminology prompting in one service
    reliability_gain: avoids local CUDA/model/alignment dependency chain
    quality_gain: likely material for noisy, multi-speaker or domain-specific audio; must be proven on project audio
    operational_gain: one hosted ASR boundary
    expected_cost: "$0.22/audio-hour base; keyterm prompting +$0.05/audio-hour at current pricing"
    free_alternative: faster-whisper
    is_the_gain_material: "yes for production default, subject to vertical ASR inspection"

  - option: Gemini 3.7 Flash
    additional_product_value: full-source semantic synthesis, cross-document reasoning, structured outputs and conditional video understanding
    reliability_gain: managed long-context API
    quality_gain: material; semantic reasoning is a core product capability
    operational_gain: eliminates a custom synthesis/agent stack
    expected_cost: "usage-based; current promotional rate $0.75/M input and $3.75/M output tokens through 2026-12-31"
    free_alternative: local model through LangExtract/Ollama
    is_the_gain_material: "yes; do not trade away semantic quality merely to make the pipeline local"

  - option: LlamaExtract v2
    additional_product_value: managed schema extraction, source citations, confidence signals, production version pinning
    reliability_gain: hosted extraction service with explicit API contract
    quality_gain: potentially material for fixed-schema document extraction; not established for this project's open-ended semantic recall target
    operational_gain: removes local extraction-library/model integration
    expected_cost: "credit-based; tier and transcript length dependent"
    free_alternative: LangExtract
    is_the_gain_material: "not demonstrated for the selected target; retain as fallback"

  - option: Gemini Notebook Enterprise
    additional_product_value: extremely strong interactive source-grounded notebook and benchmark artifact
    reliability_gain: mature managed user product
    quality_gain: material as a comparison baseline and operator workspace
    operational_gain: near-zero implementation for interactive use
    expected_cost: "$9/user/month at current advertised Enterprise price"
    free_alternative: NotebookLM consumer availability / selected production pipeline
    is_the_gain_material: "yes as benchmark; no as sole automated production engine until its artifact API surface is adequate"
```

For privacy, the selected hosted design necessarily transmits audio to the ASR provider and transcript/evidence text—and visual media when the visual branch is enabled—to the semantic provider. ElevenLabs documents an Enterprise Zero Retention Mode in which STT audio input and STT text output are among the eligible data types whose request/response data are not persisted after processing. citeturn21search1 Deepgram documents an EU endpoint, and AssemblyAI likewise documents an EU endpoint at the same listed API price; both are credible alternatives when EU residency requirements dominate. citeturn16search1turn16search2

## Corrected functional pipeline and capability decision matrix

The historical list of 17 stages is too implementation-shaped. The product needs fewer **responsibility boundaries**, while some responsibilities need to be made stronger than a generic stage list suggests.

```text
SOURCE
  ↓
SOURCE ACQUISITION
  ↓
TRUSTWORTHY SOURCE REPRESENTATION
  ├─ transcript provenance
  ├─ text
  ├─ segment / word timing where available
  ├─ speakers where available
  └─ visual observations when semantically necessary
  ↓
GROUNDED SEMANTIC EVIDENCE ACQUISITION
  ↓
GLOBAL UNDERSTANDING AND ORGANIZATION
  ↓
SUPPORT / EPISTEMIC CONTROL
  ↓
[optional] EXTERNAL TRUTH VERIFICATION
  ↓
DETERMINISTIC KNOWLEDGE COMPILATION
  ↓
PRODUCT INSPECTION
  ↓
KNOWLEDGE ARTIFACT
```

The resulting status assignments are:

| Capability | Status | Decision |
|---|---|---|
| Invocation / chat command | **REMOVED** from semantic architecture | Invocation is an execution-shell concern. OpenClaw, Codex, Claude Code, Antigravity or a normal CLI can invoke the same pipeline. |
| Source acquisition | **SEPARATE_COMPONENT** | yt-dlp for supported remote media; direct filesystem ingestion for local media/transcripts. yt-dlp is extremely mature and had a current `2026.07.04` release in July 2026. citeturn15search7turn22search0 |
| Media preparation | **CONDITIONAL** | FFmpeg only when codec/container/audio normalization is needed. FFmpeg 9.0 was released August 4, 2026. citeturn21search0turn21search3 |
| Transcript / ASR | **OWNED_BY_EXISTING_SYSTEM** | Prefer trustworthy supplied/manual transcript; otherwise Scribe v2. |
| Speaker attribution / word timing | **OWNED_BY_EXISTING_SYSTEM / CONDITIONAL** | Use Scribe output when relevant. Do not add WhisperX merely because it exists. |
| Canonical custody/provenance | **CUSTOM_REQUIRED — thin contract only** | Stable source ID, hashes, provider/model metadata, transcript segments and character/time mapping. |
| Visual source evidence | **CONDITIONAL** | Gemini 3.7 Flash only where transcript omits meaningful visual information. Gemini 3.7 accepts video and structured output. citeturn24search1 |
| Long-source segmentation | **OWNED_BY_EXISTING_SYSTEM** | LangExtract chunking/parallel/multi-pass for evidence extraction. No custom chunker. citeturn21search2 |
| Semantic extraction | **OWNED_BY_EXISTING_SYSTEM** | LangExtract + strong model. |
| Structured knowledge units | **OWNED_BY_EXISTING_SYSTEM + CONFIGURATION** | Schema/few-shot configuration, not a new extraction engine. |
| Source-support checking | **OWNED_BY_EXISTING_SYSTEM + deterministic gate** | Exact source span resolution plus semantic review of normalized/global claims. |
| Global synthesis | **SEPARATE_COMPONENT** | Gemini 3.7 Flash over full canonical source + evidence units. Avoid lossy recursive-summary chains while the source fits context. |
| External factual verification | **CONDITIONAL** | Separate verification records using search-grounded semantic research; never silently overwrite what the source said. |
| Knowledge compilation | **CUSTOM_REQUIRED — deterministic** | Templates and schema validation only. |
| Product evaluation | **SEPARATE_COMPONENT** | Bounded source comparison, not an evaluation platform. |
| Recovery/resume | **CUSTOM_REQUIRED — thin deterministic state** | Immutable stage artifacts + content hashes + a small manifest. |
| Delivery integration | **CONDITIONAL** | Files first; agent skill/Obsidian/Notion/etc. only after the artifact itself is proven. |

The key semantic data contract should **not** be a bag of summary sections. A useful minimum is a flexible grounded-unit representation:

```yaml
knowledge_unit:
  id:
  kind:
    # examples, not a closed ontology:
    # thesis | fact_claim | mechanism | procedure | argument |
    # evidence | example | qualification | correction |
    # contradiction | uncertainty | prediction | opinion |
    # definition | entity_relation
  statement:
  importance:
  epistemic_status:
  speaker:
  qualifiers:
  relationships:
  evidence:
    - source_id:
      exact_text:
      char_start:
      char_end:
      segment_ids:
      start_time:
      end_time:
  support_status:
```

`kind` should remain extensible rather than forcing every idea into an ontology guessed before seeing the corpus. More importantly, `epistemic_status` must distinguish “the source asserts X” from “X is externally true.” Predictions, opinions, anecdotes and uncertainty must remain predictions, opinions, anecdotes and uncertainty.

**Complete capability/options matrix**

| Capability | Why it exists / product value | Whole-system coverage | Serious options | BP | Current evidence / quality implications | Reliability / local / cost | Prior project recommendation | **Current recommendation** | Confidence / fallback |
|---|---|---|---|---|---|---|---|---|---|
| Acquisition | Without reproducible source capture there is no trustworthy custody. | NotebookLM/Podwise acquire some source classes internally. | **yt-dlp**, direct file; provider upload. | yt-dlp **BP4** | yt-dlp remains highly active, with ~185k GitHub stars in the current release result and July 2026 release activity; project license is Unlicense. citeturn15search7turn22search0 | Local/free; Windows binaries available; site extractor breakage is expected operationally, so preserve original source URL/metadata. | Not recoverable from V1–V3 sources. | **yt-dlp + filesystem.** | High; fallback manual/downloaded media input. |
| Media normalization | Ensures ASR accepts a predictable media stream. | Hosted systems often hide this. | **FFmpeg**, provider-native input. | FFmpeg **BP4** | FFmpeg 9.0 is the current major stable release as of Aug. 4, 2026. citeturn21search0turn21search3 | Local/free; license depends on chosen build/configuration and must be checked at packaging time. | Unknown. | **Conditional FFmpeg, never mandatory transcoding.** | Very high. |
| Transcript / ASR | Source text fidelity dominates every downstream semantic stage. | NotebookLM, Podwise, Azure cover it. | **Scribe v2**, Deepgram Nova-3 Multilingual, AssemblyAI U3.5 Pro, faster-whisper. | Scribe **BP3**; Deepgram/AssemblyAI **BP4** services; faster-whisper **BP4 specialist** | Scribe advertises 90+ languages, word timing, diarization and keyterm support; Deepgram explicitly positions Nova-3 Multilingual for multilingual/noisy/crosstalk audio; AssemblyAI U3.5 Pro supports 18 languages and current keyterm/diarization options. citeturn7search1turn7search2turn7search3turn16search0turn16search1turn16search2 | Hosted default; $0.22/h Scribe base. Local fallback is MIT faster-whisper. citeturn22search1 | Prompt names faster-whisper/WhisperX historically; exact selected version is unverified. | **Trustworthy existing transcript first; otherwise Scribe v2 default.** | Medium-high until project EN/DE audio test; fallback Deepgram Nova-3 Multilingual, then faster-whisper for locality. |
| ASR quality handling | Prevents semantic corruption from terminology/numbers/names. | Some hosted systems provide confidence/context features. | Keyterm prompts; bounded human sample; second ASR provider on failed source. | Existing service capabilities BP3–4 | Costs of switching providers are tiny relative to semantic damage; current providers are all fractions of a dollar per audio hour. citeturn16search0turn16search1turn16search2 | Do not build a “quality AI.” Inspect representative slices and rerun only when meaning-changing errors occur. | Unknown. | **Bounded gate, not a custom ASR QA subsystem.** | High. |
| Diarization / alignment | Needed when who-said-what materially affects meaning. | Scribe/Azure/etc. integrate it. | Scribe; WhisperX + pyannote; Azure. | WhisperX **BP3**, pyannote **BP4 specialist** | WhisperX provides word alignment/diarization and remained actively released in 2026, but its stack is materially more complex. A current issue also flags that default non-English alignment models including German VoxPopuli models can carry CC-BY-NC licensing, despite WhisperX code itself now being BSD-2-Clause. citeturn6search1turn22search2turn22search9 | Hosted integrated approach is simpler. | WhisperX named in prompt. | **Use Scribe's native timing/diarization; do not make WhisperX core.** | High. |
| Canonical source representation | Makes every later assertion traceable to one immutable source representation. | NotebookLM keeps an internal source copy; VideoDB keeps timed indexes, but neither exposes the desired cross-provider custody contract. | Existing product internals; thin local JSON contract. | Custom contract **BP0**, deterministic mechanics | LangExtract provides exact character offsets; ASR supplies word timing, but an application-level bridge is still required. citeturn21search2turn7search1 | Local/free; very small deterministic surface. | Existing custody/provenance referenced by prompt, exact design unknown. | **CUSTOM_REQUIRED: source.json + source.txt + offset/time mapping.** | High. |
| Visual enrichment | Transcript-only pipelines can lose diagrams/slides/demo facts. | NotebookLM/video services can see media; Azure CU extracts keyframes. | **Gemini 3.7 video**, Azure Content Understanding, VideoDB. | Gemini platform **BP4**, 3.7 model fresh GA | Gemini 3.7 natively accepts video and structured output; Azure CU exposes keyframes/timing/transcript elements. citeturn24search1turn15search1 | Cloud; cost only when branch enabled. | Unknown. | **Conditional Gemini visual-observation pass.** | Medium-high. |
| Long-source segmentation | Extraction recall can degrade if one model call must locate many facts. | NotebookLM internal; LangExtract explicit. | **LangExtract**, DocETL, custom chunker. | LangExtract **BP3**; DocETL **BP3** | LangExtract intentionally combines chunking, parallel processing and multiple extraction passes, and its current release line added cross-chunk context and schema support. citeturn21search2turn8search0 | Open-source; model calls cost money. | LangExtract/DocETL appear in project history. | **LangExtract owns this. CUSTOM BUILD NOT JUSTIFIED.** | High. |
| Semantic extraction | Captures mechanisms, procedures, arguments, caveats, examples and epistemic status rather than generic summaries. | NotebookLM gives strong semantic understanding but not automatable structured contract. | **LangExtract + frontier model**, LlamaExtract, DocETL map operations, GLiNER2. | LangExtract **BP3**, LlamaExtract **BP3**, GLiNER2 **BP2–3** | LangExtract maps extraction to exact source positions; LlamaExtract offers schema/citations/confidence; GLiNER2 is a compact NER/structured extraction model, not evidence that a 205M-class local model can replace frontier semantic reasoning on arguments/mechanisms. citeturn21search2turn17search12turn10search5turn9search6 | LangExtract library is free; selected Gemini model is metered. | All three were historically considered per prompt. | **LangExtract multi-pass extraction with a rich but flexible schema.** | Medium-high; LlamaExtract Agentic is fallback. |
| Structured output / relations | Required for machine-useful knowledge and reliable compilation. | LlamaExtract/LangExtract both cover it. | **LangExtract schema**, Gemini structured output, LlamaExtract. | BP3–4 | Gemini 3.7 directly supports structured outputs; LangExtract 1.6 added output-schema support for supported providers. citeturn24search1turn8search0 | No custom parser should “repair” malformed model prose. | Existing schemas referenced but content unavailable. | **Provider-controlled structured generation + schema validation.** | High. |
| Source-support checking | Prevents fluent synthesis from becoming unsupported source claims. | NotebookLM citations are strong; LangExtract spans are machine-verifiable. | **LangExtract offsets + semantic reviewer**, LlamaExtract source citations. | BP3 | Exact source offsets are a strong deterministic primitive, but existence of a quote is not semantic entailment; normalized/global claims still need a support rule. citeturn21search2turn10search5 | Mostly deterministic + bounded Gemini review. | Existing “support checking” mentioned by prompt. | **Exact span verification for evidence; semantic review only for normalized/global claims.** | High. |
| Global synthesis | Individual evidence units do not provide thesis, hierarchy, correction chains or cross-section contradictions. | NotebookLM covers this interactively. | **Gemini 3.7 Flash**, NotebookLM baseline, DocETL reduce. | Gemini API **BP4**, exact 3.7 model new GA | 3.7 has 1M input context, 65k output, structured output and improved knowledge-work capability; it is GA. citeturn24search0turn24search1turn24search3 | Cloud; current price $0.75/M input, $3.75/M output through 2026. citeturn24search0 | Global synthesis existed historically; exact prior model unknown. | **One full-source global pass plus evidence IDs; no recursive summary unless context is actually exceeded.** | Medium-high. |
| External verification | Source support and external truth are different questions. | NotebookLM web discovery can add sources, Gemini can use search grounding. | **Gemini search grounding**, separate research workflow. | BP4 service | Gemini 3.7 supports Search grounding. citeturn24search1 | Metered search/model usage. | Mentioned historically. | **Conditional and separate. Never mutate `source_claim`.** | High. |
| Compiler/output | Human artifact must be stable and machine artifact valid. | Closed products have their own exporters. | Templates + JSON Schema; NotebookLM/Podwise exports. | Deterministic custom **BP0** | Podwise exports Markdown/PDF and PKM formats but its artifact contract is its own; the selected evidence schema therefore still needs rendering. citeturn18search0turn18search12 | Local, cheap and testable. | Existing compiler named by prompt. | **Tiny deterministic compiler; reuse existing implementation only if it matches new schema exactly.** | High. |
| Product evaluation | Automated PASS flags cannot establish knowledge usefulness. | NotebookLM acts as excellent reference comparator. | Bounded human source review; targeted automated checks. | N/A | No current candidate benchmark directly measures the entire requested product; vendor ASR/extraction benchmarks answer narrower questions. | Human time dominates; keep bounded. | Existing evaluation machinery named by prompt. | **Three real-source tests + small must-find set + evidence inspection.** | High. |
| Recovery/resume | Long jobs must not restart unnecessarily or hide half-failures. | Hosted jobs often retry internally; DocETL has pipeline infrastructure; agent runtimes have checkpoint concepts. | Immutable stage outputs + manifest; DocETL; general orchestrator. | Custom manifest BP0 | DocETL is a genuine declarative Map/Reduce/ETL framework with an optimizer and current 0.3.0 release, but introducing it merely for a linear per-source job would add an orchestration abstraction not yet earning product value. citeturn8search5 | Local deterministic metadata. | Existing runners/resume mentioned. | **Thin idempotent manifest. Do not build a workflow platform.** | Medium-high. |
| Delivery/integration | Makes artifact usable without coupling product semantics to an agent shell. | Podwise, Codex, Claude, OpenClaw skills can package workflows. | Filesystem; thin Skill/MCP wrapper later. | Platforms BP3–4 | Skills are intended to encode reusable workflows around existing tools rather than to replace the underlying data/action layer. citeturn19search5 | Very low burden after CLI works. | OpenClaw/Claude/Codex/Antigravity historically discussed. | **Files are primary API; optional skill invokes CLI.** | High. |

Two previously attractive ideas should explicitly lose core status.

**GLiNER2 should not be the semantic brain.** Its current generation is an efficient small structured-extraction/NER system, and multilingual models exist, but that is a different capability from preserving nuanced arguments, mechanisms, caveats, corrections and global source meaning. citeturn9search0turn9search1turn9search6 It could later earn a role for cheap entity/PII preprocessing, but adding it now creates an extra semantic seam without proven product gain.

**DocETL should not own the first production version.** DocETL is credible and actively maintained, with map/reduce/filter/split/gather/extract operations and an optimizer for large-data LLM pipelines. citeturn8search5 That becomes attractive when the task evolves into large repeated corpora or pipeline optimization. For one long source at a time, LangExtract already owns the difficult extraction segmentation problem, while direct long-context synthesis removes the need for a generic MapReduce layer.

## Historical reconciliation and custom-code authorization

The V1/V2/V2.1/V3 attachments are not retrievable in this research run. The only safe project evidence is what the prompt itself says: V1 is older but may contain useful options research; V2/V2.1 contain substantial research and failed assumptions; V3 is newer but not automatically correct; and the named technologies have appeared in historical work. Consequently, `U` below means **UNVERIFIED PROJECT HISTORY — source document unavailable to this run**. Any more detailed reconstruction of what a version “selected” would be fabricated.

| Topic | V1 | V2 | V2.1 | V3 | What current evidence actually supports | Current verdict |
|---|---|---|---|---|---|---|
| Overall product target | U | U | U | U | The current prompt is authoritative: semantic value and trust dominate minimalism. | **Adopt current TARGET; no version wins by chronology.** |
| Source acquisition | U | U | U | U | yt-dlp remains extremely mature and actively maintained. citeturn15search7turn22search0 | **yt-dlp/direct file.** |
| ASR | U | U | U | U | Hosted ASR is now extremely inexpensive; Scribe/Deepgram/AssemblyAI provide integrated multilingual capabilities, while faster-whisper remains a strong local option. citeturn16search0turn16search1turn16search2turn22search1 | **Scribe default; faster-whisper locality fallback.** |
| Diarization/alignment | U | U | U | U | Hosted ASR can avoid a separate local alignment/diarization stack. WhisperX remains capable but has dependency and German-alignment licensing concerns. citeturn6search1turn22search9 | **Conditional, not mandatory stage.** |
| Custody/provenance | U | U | U | U | Exact span grounding is valuable, but cross-provider custody still requires an application-level source package. citeturn21search2 | **Retain as thin deterministic responsibility.** |
| Chunking/windowing | U | U | U | U | LangExtract already implements chunked, parallel, multi-pass extraction to address multi-fact recall. citeturn21search2 | **Do not custom-build.** |
| Map/extraction | U | U | U | U | LangExtract fits this target more directly than generic DocETL or small-model GLiNER2. citeturn21search2turn8search5turn9search6 | **LangExtract.** |
| Structured output | U | U | U | U | LangExtract and Gemini both support constrained structured output. citeturn8search0turn24search1 | **Schema as configuration, not parsing invention.** |
| Source-support checking | U | U | U | U | LangExtract exact character intervals create an excellent mechanical verification primitive. citeturn21search2 | **Retain, but distinguish span existence from semantic support.** |
| Global synthesis | U | U | U | U | Current Gemini 3.7 Flash can accept a 1M-token source and return up to 65k tokens. citeturn24search1 | **Full-context global pass; avoid lossy MapReduce unless necessary.** |
| External verification | U | U | U | U | Search-grounded models can perform a separate truth-check layer. citeturn24search1 | **Conditional and separate from source fidelity.** |
| Compiler/output | U | U | U | U | Existing products export artifacts, but none provides the selected evidence schema as a programmatic contract. | **Thin deterministic compiler survives conceptually; old compiler gets no sunk-cost preference.** |
| Product evaluation | U | U | U | U | External benchmarks cover components, not this complete target. | **Bounded real-source evaluation.** |
| Resumability | U | U | U | U | Generic ETL/agent frameworks exist, but no additional framework is needed merely to record completed immutable stages. citeturn8search5turn20search3 | **Small manifest; no custom orchestration platform.** |
| OpenClaw/execution architecture | U | U | U | U | OpenClaw's native media understanding is best-effort; Claude/Codex/Antigravity all have reusable workflow mechanisms. citeturn19search7turn19search5turn19search3turn20search3 | **Execution shell only; architecture must remain shell-independent.** |

The current evidence therefore preserves **the product concerns** behind custody, high-recall extraction, grounding, synthesis, evaluation and recovery, but does **not** preserve any historical implementation merely because it already exists.

**Custom-code audit**

The first custom requirement is the canonical source package and exact transcript-span→time bridge.

```yaml
custom_authorization:
  capability: canonical source representation and evidence-time mapping
  why_the_capability_is_required_for_product_value: >
    Final knowledge claims need stable source identity and resolvable evidence.
    LangExtract returns character positions in canonical text, while ASR returns
    word/segment time positions. Production output must bridge those representations.

  existing_alternatives_examined:
    - candidate: NotebookLM
      maturity: BP4 interactive product
      relevant_capability: internal cited source representation
      observed_or_documented_limitation: >
        Does not expose the required canonical evidence/custody contract through the
        currently documented production API.
      evidence: current Notebook/Gemini Notebook API surface reviewed

    - candidate: VideoDB
      maturity: BP2-BP3
      relevant_capability: timed media indexing and evidence retrieval
      observed_or_documented_limitation: >
        Would replace the source/index layer with another hosted platform yet still
        would not supply the complete selected knowledge contract.

    - candidate: LangExtract
      maturity: BP3
      relevant_capability: exact character-span grounding
      observed_or_documented_limitation: >
        Owns text span grounding, not media timestamp/provenance custody across ASR.

  why_configuration_is_insufficient: >
    No selected component owns both canonical ASR timing and LangExtract character offsets.
  why_supported_extensions_are_insufficient: >
    Provider plugins do not create a common cross-provider evidence contract.
  why_light_adaptation_or_fork_is_insufficient: >
    Nothing needs forking; a deterministic adapter is smaller and safer.

  custom_work_required: >
    Define source.json/source.txt; assign stable segment IDs; record character bounds;
    map grounded character intervals onto intersecting timed segments/words.
  product_value_created: >
    Every important final item can resolve to exact transcript evidence and, when available,
    source time.
  maintenance_risk: low
  justification: >
    This is deterministic glue between two mature representations, not new semantic infrastructure.
```

LangExtract's exact character grounding is directly documented, while Scribe provides the time-oriented ASR side of the representation. citeturn21search2turn7search1

The second custom requirement is final compilation.

```yaml
custom_authorization:
  capability: deterministic final artifact compiler
  why_the_capability_is_required_for_product_value: >
    Users need a coherent readable knowledge artifact and machines need stable JSON,
    while evidence must survive rendering intact.

  existing_alternatives_examined:
    - candidate: NotebookLM exports
      maturity: BP4 product
      relevant_capability: useful generated notebook artifacts
      observed_or_documented_limitation: >
        Artifact shape is owned by NotebookLM and is not the selected programmatic evidence schema.

    - candidate: Podwise exports
      maturity: BP3
      relevant_capability: Markdown/PDF/PKM exports
      observed_or_documented_limitation: >
        Export contract follows Podwise's podcast product rather than this pipeline's
        evidence and epistemic fields.

    - candidate: LangExtract output
      maturity: BP3
      relevant_capability: JSONL plus source visualization
      observed_or_documented_limitation: >
        It supplies grounded extractions, not the final globally organized human artifact.

  why_configuration_is_insufficient: >
    The final artifact organization is product-specific.
  why_supported_extensions_are_insufficient: >
    Existing exporters do not expose the required source-support/epistemic contract.
  why_light_adaptation_or_fork_is_insufficient: >
    A template is smaller than adapting or forking an entire product.

  custom_work_required: >
    Schema validation plus deterministic Markdown/JSON rendering templates.
  product_value_created: >
    Stable human-readable and machine-readable knowledge without introducing additional semantics.
  maintenance_risk: low
  justification: >
    Rendering is mechanically deterministic and should remain outside the LLM.
```

The third custom requirement is resumability state.

```yaml
custom_authorization:
  capability: idempotent per-source stage manifest
  why_the_capability_is_required_for_product_value: >
    A failed semantic/API stage must be rerunnable without reacquiring,
    retranscribing or losing already inspected evidence.

  existing_alternatives_examined:
    - candidate: DocETL
      maturity: BP3
      relevant_capability: declarative LLM data pipelines and optimization
      observed_or_documented_limitation: >
        It introduces a general map/reduce/optimizer execution abstraction that is not
        otherwise needed in the selected one-source linear product path.

    - candidate: OpenClaw / coding-agent runtime state
      maturity: BP3-BP4 execution ecosystems
      relevant_capability: retries/checkpoints/tool workflows
      observed_or_documented_limitation: >
        Agent conversation/checkpoint state is not the authoritative content-addressed
        state of a production knowledge job.

  why_configuration_is_insufficient: >
    Stage completion must be tied to source/component/configuration hashes.
  why_supported_extensions_are_insufficient: >
    No selected component tracks the entire cross-provider job.
  why_light_adaptation_or_fork_is_insufficient: >
    A small manifest is itself the lightest adaptation.

  custom_work_required: >
    Record input hashes, configuration hashes, component/model versions,
    output paths, status and error category for each stage.
  product_value_created: >
    Safe rerun/resume and auditable provenance.
  maintenance_risk: low
  justification: >
    A generic workflow platform would currently add more operational surface
    than the manifest removes.
```

DocETL is a real and credible existing alternative, not an invented straw man: its current project supplies declarative map/reduce/filter/split/gather/extract operations and an optimizer, with version 0.3.0 released in June 2026. citeturn8search5 The judgment above is therefore that its **capability is real but disproportionate to this specific responsibility**.

For the following areas the verdict is explicit:

```text
custom ASR:                 CUSTOM BUILD NOT JUSTIFIED
custom diarization:         CUSTOM BUILD NOT JUSTIFIED
custom alignment model:     CUSTOM BUILD NOT JUSTIFIED
custom chunker:             CUSTOM BUILD NOT JUSTIFIED
custom semantic extractor:  CUSTOM BUILD NOT JUSTIFIED
custom NER model:           CUSTOM BUILD NOT JUSTIFIED
custom RAG framework:       CUSTOM BUILD NOT JUSTIFIED
custom workflow engine:     CUSTOM BUILD NOT JUSTIFIED
custom benchmark platform:  CUSTOM BUILD NOT JUSTIFIED
custom agent framework:     CUSTOM BUILD NOT JUSTIFIED
```

## Recommended production architecture

Only **one primary architecture** is justified. Creating three nominally different architectures would obscure a fairly clear result.

**Selected responsibility ownership**

```text
SOURCE
  │
  ├── URL ───────────────→ [yt-dlp owns acquisition]
  │
  ├── local media ───────→ [filesystem owns acquisition]
  │
  └── transcript ────────→ [transcript importer]
  │
  ▼
[FFmpeg owns media normalization ONLY when required]
  │
  ▼
[trustworthy existing transcript]
          OR
[ElevenLabs Scribe v2 owns ASR + word timing + speaker diarization]
  │
  ├──────── video with material visual-only information ────────┐
  │                                                              │
  │                                             [Gemini 3.7 Flash owns
  │                                              visual observation]
  │                                                              │
  └──────────────────────────────┬───────────────────────────────┘
                                 ▼
             [small local canonical-source adapter]
                                 │
                                 ▼
                [LangExtract 1.6.0 owns
                 chunking + multi-pass extraction
                 + exact source-span grounding
                 + extraction structure]
                                 │
                                 ▼
                    GROUNDED EVIDENCE UNITS
                                 │
                                 ▼
                 [Gemini 3.7 Flash owns
                  global semantic synthesis]
                                 │
                                 ▼
              [deterministic span/support gate]
                  + bounded semantic support review
                                 │
                 ┌───────────────┴───────────────┐
                 │                               │
          source knowledge               when requested/needed
                 │                               ▼
                 │                    [Gemini Search-grounded
                 │                     external verification]
                 │                               │
                 └───────────────┬───────────────┘
                                 ▼
                 [small deterministic compiler]
                                 │
                                 ▼
             knowledge.md + knowledge.json
             evidence.jsonl + source.json
             review.html + verification.json?
```

**Why Scribe v2 wins the initial hosted-ASR slot.** At current published pricing it costs $0.22/hour, supports 90+ languages and exposes features relevant to this product such as word timestamps, diarization and terminology prompting in one API. citeturn16search0turn7search1 That minimizes the need for an alignment/diarization chain while retaining a very cheap per-source cost. The vendor's advertised accuracy figures should **not** be treated as proof of project-specific German quality; the vertical slice decides that.

Deepgram Nova-3 Multilingual is the pre-authorized hosted fallback. Deepgram explicitly recommends its multilingual model for multilingual, noisy, crosstalk and far-field input and documents EU data residency; its prerecorded multilingual rate is currently $0.0052/minute. citeturn16search1 AssemblyAI Universal-3.5 Pro is another credible fallback, at $0.21/hour plus optional diarization/keyterm add-ons, with a documented EU region. citeturn16search2 No architecture research is needed to switch among these if the default fails the defined ASR product gate.

**Why faster-whisper survives only as the local fallback.** Version 1.2.1 remained the latest current release found, the project has roughly 25k GitHub stars and is MIT-licensed. citeturn6search0turn22search1 It is an excellent mature specialist. It loses the default only because a managed ASR call costing well under a dollar for a multi-hour source buys simpler operations and integrated speaker/timing behavior. Locality is not allowed to beat product reliability merely for philosophical reasons.

**Why WhisperX loses core status.** WhisperX is genuine and capable, providing ASR, word-level alignment and diarization, with active 2026 releases. citeturn6search1 Its additional dependency chain is unnecessary when the hosted default already owns those responsibilities; more importantly for German commercial deployment, a current repository issue documents licensing concerns around the default German VoxPopuli alignment model. citeturn22search9 WhisperX remains a specialized conditional option, not a default production dependency.

**Why LangExtract wins extraction.** Google designed LangExtract specifically around precise source grounding, schema-driven extraction and high-volume/long-document extraction, using chunking, parallelism and multiple passes. citeturn21search2 The repository is Apache-2.0 licensed and had roughly 38k stars in the current repository evidence; release 1.6.0 shipped July 1, 2026, adding output-schema support. citeturn8search0turn8search8 That combination is unusually aligned with this target: it lets a powerful semantic model perform interpretation while a proven library owns extraction mechanics and traceability.

The extraction prompt/schema should explicitly seek, in **separate passes where useful**, central claims/thesis, mechanisms/causal explanations, procedures, arguments and reasons, examples, qualifications/exceptions, corrections, contradictions, uncertainty, forecasts/opinions, definitions, numerical claims and entity relationships. Multiple passes are preferable to one enormous ontology prompt when the goal is high recall.

**Why LlamaExtract does not replace LangExtract initially.** LlamaExtract v2 is strong, exposes UI/SDK/REST, supports production version pins and offers source citation/confidence options. citeturn17search12turn17search8turn10search5 LlamaIndex's very recent ExtractBench work reports excellent structured-value and grounding results for Agentic Plus, but that benchmark is designed around extracting structured values from complex documents, not retaining open-ended argumentation and epistemic nuance from hours-long interviews. It is also product-adjacent/vendor research. The results are useful evidence that LlamaExtract is credible, not evidence that it dominates this target. citeturn10search1

**Why Gemini 3.7 Flash wins global synthesis.** As of August 19, it is Google's newest GA Flash model, introduced August 13. It supports a 1M-token context, 65,536-token outputs, structured output, thinking levels and multimodal inputs; Google explicitly describes it as improved for knowledge work and reliable complex execution. citeturn24search0turn24search1turn24search3 Its current introductory price is also below the previous 3.5 Flash price: $0.75 per million input tokens and $3.75 per million output tokens through the end of 2026. citeturn24search0turn16search3

There is one compatibility caveat: LangExtract 1.6.0 predates Gemini 3.7 Flash by about six weeks. LangExtract supports Gemini-family backends, but this exact library/model pairing did not have time to accumulate release-level validation before this research date. citeturn8search0turn24search7 The implementation preflight must therefore make one trivial extraction call through LangExtract with `gemini-3.7-flash`. If that interface fails, **do not modify LangExtract**: use its known current Gemini integration/default generation for extraction and retain 3.7 Flash for the global pass until a LangExtract update confirms the newest model. That is implementation diagnosis, not architecture reopening.

**Crucial trust rule:** three concepts must remain separate.

```text
EXACT EVIDENCE EXISTS
    ≠
THE NORMALIZED CLAIM IS SEMANTICALLY SUPPORTED
    ≠
THE CLAIM IS TRUE IN THE EXTERNAL WORLD
```

LangExtract can mechanically establish the first. citeturn21search2 A semantic reviewer establishes the second. A separate web/search verification process may investigate the third. Conflating those three is one of the easiest ways to turn an apparently “grounded” knowledge system into an untrustworthy one.

**Selected system package**

| System | Responsibility | Verified current version/model | License / terms | Installation / invocation | Key configuration |
|---|---|---|---|---|---|
| **yt-dlp** | remote source acquisition and metadata/captions | `2026.07.04` latest stable found | Unlicense; bundled executables have third-party notices. citeturn15search7turn22search0 | Standalone Windows executable or Python package | Save info metadata and original caption tracks; preserve original URL. |
| **FFmpeg** | conditional normalization/extraction of audio stream | FFmpeg 9.0, released Aug. 4, 2026. citeturn21search0 | Build-dependent licensing; verify chosen Windows distribution | Binary on PATH | Do not transcode when provider accepts source media directly; when needed, create a reproducible ASR-friendly audio derivative. |
| **ElevenLabs Scribe v2** | default ASR, word timing, speaker attribution | `Scribe v2` | Commercial API terms | Official API/SDK | Source language auto/known; enable needed diarization; use keyterm prompting only when vocabulary warrants it. |
| **LangExtract** | grounded high-recall extraction, segmentation/multi-pass | `1.6.0`, July 1 2026. citeturn8search0 | Apache-2.0. citeturn8search8 | Pin Python package | Multiple semantic passes; require grounded evidence for source assertions; save JSONL + review visualization. |
| **Gemini 3.7 Flash** | global synthesis; optional visual pass; conditional external verification | stable `gemini-3.7-flash`, GA Aug. 13 2026. citeturn24search1turn24search7 | Commercial Gemini API terms | Google Gen AI SDK / API | Structured output; medium reasoning initially; complete source in context; search grounding disabled during source-only synthesis. |
| **faster-whisper** | local/offline ASR fallback | `1.2.1` latest current release found. citeturn6search0 | MIT. citeturn22search1 | Python/CTranslate2 | `large-v3`/current suitable model chosen based on hardware; no local path should silently substitute for failed hosted ASR. |
| **NotebookLM / Gemini Notebook Enterprise** | external whole-product benchmark and optional operator notebook | current managed product | Commercial service | UI / Enterprise service | Use same canonical transcript/source for benchmark where possible; do not make its notebook the only persisted production artifact. |

At current rates, a two-hour source costs about **$0.44 for Scribe base ASR** before optional keyterm charges. citeturn16search0 Semantic model spend should normally be small relative to the human value of the artifact: even repeated processing of a transcript occupying tens of thousands of tokens is inexpensive at Gemini 3.7 Flash's current per-million-token rates, although extraction passes, thinking tokens and final-output size must be metered rather than guessed. citeturn24search0turn24search3 The practical expectation is roughly **sub-dollar ASR plus low-single-digit semantic spend for an ordinary two-hour source**, not a guaranteed price.

## Implementation authority and execution plan

**Target**

Implementation is complete when one command or callable workflow accepts an authorized URL, local video/audio file or transcript and produces a durable package:

```text
<job>/
  manifest.json
  source/
    source.json
    source.txt
    transcript.json
    media-info.json
  evidence/
    evidence.jsonl
    extraction-review.html
    visual-evidence.json          # only when required
  synthesis/
    synthesis.json
    support-review.json
    external-verification.json    # only when requested/required
  output/
    knowledge.json
    knowledge.md
```

The Markdown artifact must be useful to a human even without opening JSON. It should contain the source's central thesis and major themes, high-value facts/claims, mechanisms, procedures, reasoning and arguments, examples, qualifications and exceptions, corrections/contradictions, uncertainties, predictions/opinions, entities/relationships, and evidence references. The JSON preserves the richer machine contract.

**Implementation sequence**

**Preflight.** Start from a clean isolated environment. Verify `yt-dlp`, `ffmpeg`/`ffprobe`, Python and the required hosted API credentials. Record—not merely print—the installed versions. Run a 30–120 second ASR probe, a tiny LangExtract grounded extraction and a tiny Gemini 3.7 structured-output call. The LangExtract→Gemini 3.7 compatibility probe is mandatory because Gemini 3.7 was released after LangExtract 1.6.0. citeturn8search0turn24search7

**Source acquisition.** Save original metadata before semantic work. If a user supplies a transcript, preserve it as the primary source rather than re-ASR merely for architectural uniformity. For remote video, retrieve metadata/captions and media using yt-dlp as needed. Never treat an automatically generated caption track as equivalent to a known manual transcript without recording its provenance.

**Source representation.** For ASR sources, persist the provider's original segment/word output before flattening it. Construct `source.txt` deterministically and record each segment's character start/end in that canonical text. That allows LangExtract offsets to map back to segment and timestamp ranges without fuzzy matching.

**ASR inspection.** On the first representative EN and DE sources, inspect approximately ten minutes from early, middle and late portions, concentrating on names, technical terms, numbers, corrections and speaker changes. The goal is not a giant WER benchmark; it is to answer whether ASR errors are changing knowledge. If Scribe fails materially, use the already-selected Deepgram fallback rather than redesigning the pipeline.

**Grounded semantic extraction.** Configure LangExtract with multiple targeted extraction passes rather than one monolithic generic-summary prompt. Each extractive knowledge unit must include source text; ungrounded model output must not silently enter the “source-supported” class. LangExtract's own documented design is built around exact source grounding and repeated extraction over long material. citeturn21search2

**Global synthesis.** Give Gemini 3.7 the entire canonical transcript when it fits, plus the grounded units and the target artifact schema. The synthesis prompt must explicitly require preservation of contradictions, later corrections, qualifications, uncertainty and speaker epistemic stance. Because 3.7 provides a 1M-token context, an ordinary two-hour transcript should not be compressed through a chunk-summary cascade merely to imitate an older long-document architecture. citeturn24search1

The synthesizer must reference evidence-unit IDs for substantive source claims. If it identifies an important idea for which no satisfactory evidence unit exists, that item enters a **targeted extraction repair queue**; it does not become an unsupported final assertion.

**Support gate.** Mechanically verify that every evidence interval resolves exactly into the canonical source. Verify evidence-unit IDs and source IDs. Then run semantic support review only for normalized claims, synthesized claims and relationships where the final wording goes beyond the quoted source. The support reviewer must return `supported`, `partially_supported`, `unsupported`, or `ambiguous`; unsupported major content is rejected from the source-grounded section or explicitly labeled as inference.

**External verification.** Only after source synthesis is stable, optionally check selected externally verifiable claims. Gemini 3.7 supports Google Search grounding. citeturn24search1 Store results next to, not over, source assertions:

```yaml
source_claim: "Speaker predicts X will happen in 2027."
epistemic_status: prediction
source_support: supported
external_verification:
  status: not_applicable_or_unverifiable
```

or:

```yaml
source_claim: "Speaker says Company X had €4.2B revenue in 2025."
epistemic_status: factual_claim
source_support: supported
external_verification:
  status: contradicted
  explanation: ...
  evidence: ...
```

This preserves both “what the source said” and “what external evidence says.”

**Compilation.** Render from validated structured data. The compiler is forbidden from adding semantic content. All headings, evidence links, tables and summaries must derive from `synthesis.json`/evidence records.

**Delivery.** Persist files first. Only after the CLI/product passes acceptance should an OpenClaw/Codex/Claude/Antigravity Skill be added. The skill's responsibility is merely “invoke the pipeline and deliver artifacts,” consistent with the way modern Skills are intended to wrap repeatable workflows around tools. citeturn19search5

**Vertical product test**

The first product test should be the harder target class: a **real 90–120 minute German financial/business discussion from the project's intended corpus**, ideally with two or more speakers, numerical claims, technical terminology, forecasts/opinions, qualifications and at least one disagreement or correction.

The expected artifact is not “a good summary.” A reviewer should be able to answer:

- What is the core thesis or set of positions?
- What mechanisms or causal explanations were actually given?
- What concrete procedures/actions were proposed?
- Which statements were claims, predictions or opinions?
- What caveats materially changed conclusions?
- Did anyone correct an earlier number or assertion?
- Were disagreements preserved rather than averaged into one smooth answer?
- Can every major sourced claim be opened at its transcript evidence and, where timing exists, the relevant time range?
- Did important examples survive because they explain a mechanism, rather than being deleted as “detail”?
- Did the final artifact avoid inventing consensus?

Then run an English technical interview of similar duration and an existing-transcript input to exercise the no-ASR branch.

**Repair rules**

Use this order and do not skip ahead:

```text
correct configuration
→ documented usage
→ supported plugin/provider interface
→ documented or maintainer-known workaround
→ pre-authorized alternate proven component
→ only then architecture reversal/custom authorization
```

Ordinary defects such as a broken downloader extractor, transient API error, malformed provider response, Windows path issue or one failed extraction pass are **not** architecture evidence.

**Architecture reversal triggers**

Reopen the affected architectural decision only if real execution establishes one of these:

1. On representative EN/DE material, the selected ASR repeatedly introduces meaning-changing terminology, number or speaker errors and the pre-authorized hosted fallback does not solve them.
2. LangExtract cannot achieve acceptable important-unit recall or cannot reliably ground required semantic units after configuration and documented multi-pass use.
3. Gemini 3.7 global synthesis repeatedly drops major corrections, contradictions or uncertainty, or generates unsupported major conclusions despite the support gate.
4. A core hosted component violates the project's actual privacy/data-residency requirements and no pre-authorized alternative satisfies them.
5. Measured per-source cost exceeds the approved operational budget materially enough to threaten deployment.
6. Windows deployment proves unsupportable using documented installation paths and a bounded workaround.
7. Integration unexpectedly requires a substantial new workflow/orchestration subsystem rather than the thin adapters identified here.
8. The final artifact is materially worse than the NotebookLM comparison artifact on substantive knowledge despite being more structured.

The selected architecture does **not** get reconsidered merely because an API changed a parameter or an executor needs to debug a package installation.

The current component facts underpinning this implementation lock are: yt-dlp's July 2026 release line, FFmpeg 9.0, LangExtract 1.6.0, Gemini 3.7 Flash GA, Scribe v2 pricing/features and faster-whisper's current MIT release. citeturn15search7turn21search0turn8search0turn24search1turn16search0turn22search1

```yaml
schema: transcript-knowledge-implementation-plan.v1

target:
  product: >
    A durable source-grounded knowledge package from video, audio or an existing
    transcript, preserving important meaning rather than producing only a summary.
  product_quality_requirements:
    - high recall of important source knowledge
    - preserve thesis, facts/claims, mechanisms, procedures, arguments and examples
    - preserve qualifications, uncertainty, corrections and contradictions
    - preserve predictions/opinions as epistemic categories rather than facts
    - every major source-grounded item has resolvable evidence
    - source support and external truth verification remain separate
    - coherent global organization across the complete source
  languages:
    - en
    - de
  source_types:
    - remote_video_or_audio_url
    - local_video
    - local_audio
    - existing_transcript

architecture:
  strategy: proven-component-composition
  rationale: >
    No verified automatable whole product simultaneously provides the required
    semantic richness, exact evidence contract, source breadth and production API.
    Use mature specialists for each responsibility and keep custom work deterministic.
  flow:
    - acquire
    - represent_source
    - extract_grounded_evidence
    - synthesize_globally
    - verify_source_support
    - optionally_verify_external_truth
    - compile
    - inspect
  components:
    - id: acquisition
      responsibility: remote media and metadata acquisition
      existing_system: yt-dlp
      version_target: "2026.07.04"
      bp_rating: BP4
      evidence_status: current_verified
      configuration:
        preserve_metadata: true
        preserve_caption_tracks: true
      custom_code_required: false

    - id: media_normalization
      responsibility: conditional media conversion
      existing_system: FFmpeg
      version_target: "9.0"
      bp_rating: BP4
      evidence_status: current_verified
      configuration:
        run_only_when_required: true
      custom_code_required: false

    - id: asr
      responsibility: transcript, word timing and speaker attribution
      existing_system: ElevenLabs Scribe v2
      bp_rating: BP3
      evidence_status: current_verified_provider_capability
      configuration:
        preserve_raw_provider_output: true
        keyterm_prompting: conditional
        diarization: when_semantically_relevant
      custom_code_required: false
      fallback:
        first: Deepgram Nova-3 Multilingual
        local: faster-whisper 1.2.1

    - id: source_contract
      responsibility: canonical source text, provenance and evidence-time mapping
      existing_system: null
      bp_rating: BP0
      evidence_status: custom_authorized
      configuration:
        immutable_source_text: true
        stable_segment_ids: true
        content_hashes: true
      custom_code_required: true

    - id: visual_evidence
      responsibility: visual-only knowledge not represented in speech
      existing_system: Gemini 3.7 Flash
      bp_rating: BP3_specific_model_BP4_platform
      evidence_status: current_verified
      configuration:
        enabled: conditional
        output: timestamped_visual_observations
        prohibit_unmarked_inference: true
      custom_code_required: false

    - id: grounded_extraction
      responsibility: high-recall semantic evidence acquisition with exact source spans
      existing_system: LangExtract
      version_target: "1.6.0"
      bp_rating: BP3
      evidence_status: current_verified
      configuration:
        model_preferred: gemini-3.7-flash
        model_compatibility_preflight_required: true
        multiple_passes: true
        require_grounded_source_units: true
        save_jsonl: true
        save_review_visualization: true
      custom_code_required: false

    - id: global_synthesis
      responsibility: >
        thesis, hierarchy, mechanisms, argument structure, corrections,
        contradictions, caveats, uncertainty and global organization
      existing_system: Gemini 3.7 Flash
      bp_rating: BP3_specific_model_BP4_platform
      evidence_status: current_verified
      configuration:
        full_source_context: preferred
        structured_output: true
        search_grounding: false
        require_evidence_unit_ids: true
      custom_code_required: false

    - id: external_verification
      responsibility: optional truth checking outside the source
      existing_system: Gemini 3.7 Flash with Search grounding
      bp_rating: BP3_specific_model_BP4_platform
      evidence_status: current_verified
      configuration:
        enabled: conditional
        never_overwrite_source_claim: true
      custom_code_required: false

    - id: compiler
      responsibility: deterministic knowledge.json and knowledge.md generation
      existing_system: standard schema validation and templating libraries
      bp_rating: BP0_product_contract
      evidence_status: custom_authorized
      configuration:
        no_semantic_generation: true
      custom_code_required: true

    - id: reference_baseline
      responsibility: external whole-product quality comparison
      existing_system: NotebookLM / Gemini Notebook Enterprise
      bp_rating: BP4_interactive
      evidence_status: current_verified
      configuration:
        production_dependency: false
      custom_code_required: false

decision_lock:
  selected:
    acquisition: yt-dlp
    media_normalization: conditional_FFmpeg
    hosted_asr_default: ElevenLabs_Scribe_v2
    hosted_asr_fallback: Deepgram_Nova_3_Multilingual
    local_asr_fallback: faster_whisper_1_2_1
    grounded_extraction: LangExtract_1_6_0
    global_model: gemini_3_7_flash
    benchmark_product: NotebookLM
    external_verification: conditional_search_grounded_Gemini
    recovery: immutable_stage_outputs_plus_manifest
  explicitly_rejected:
    - custom_ASR
    - custom_diarization_model
    - custom_chunker
    - custom_semantic_extraction_engine
    - GLiNER2_as_primary_semantic_engine
    - WhisperX_as_unconditional_core_dependency
    - DocETL_as_default_orchestrator
    - Fabric_pattern_as_trust_boundary
    - OpenClaw_media_understanding_as_source_of_record
    - NotebookLM_as_only_automated_production_engine
    - giant_custom_evaluation_framework
  unresolved_local_facts:
    - actual representative EN and DE source files
    - whether specific video corpus contains important visual-only knowledge
    - organization privacy/data-residency classification
    - available local GPU if offline fallback is needed
    - LangExtract 1.6.0 runtime compatibility with newly released gemini-3.7-flash
    - approved per-source operating budget
    - which existing TTK modules, if any, conform exactly to the new contracts
  architecture_research_must_not_be_reopened_for:
    - whether to create a custom ASR system
    - whether to create a custom chunking/extraction framework
    - whether an agent runtime should own semantic truth
    - whether source support and external truth are the same concept
    - whether existing TTK code receives sunk-cost preference
    - normal package installation or API integration defects

artifacts:
  required:
    - manifest.json
    - source/source.json
    - source/source.txt
    - source/transcript.json
    - evidence/evidence.jsonl
    - synthesis/synthesis.json
    - synthesis/support-review.json
    - output/knowledge.json
    - output/knowledge.md
  conditional:
    - evidence/visual-evidence.json
    - evidence/extraction-review.html
    - synthesis/external-verification.json

preflight:
  - id: runtime
    objective: verify deterministic local dependencies
    read_only_actions:
      - report yt-dlp version
      - report ffmpeg and ffprobe version
      - report Python environment
    expected_result: required binaries resolve and versions are recorded
    if_missing: install documented selected component; do not substitute architecture

  - id: provider_access
    objective: verify hosted components without processing a full source
    read_only_actions:
      - run short Scribe transcription probe
      - run tiny Gemini 3.7 structured-output probe
      - run tiny LangExtract grounded extraction
    expected_result: all selected provider boundaries execute
    if_missing: diagnose credentials/configuration before any architecture change

  - id: langextract_model_compatibility
    objective: >
      prove LangExtract 1.6.0 can invoke gemini-3.7-flash despite the model
      being newer than the library release
    read_only_actions:
      - extract two known grounded fields from a short text
      - verify returned source intervals
    expected_result: structured grounded extraction succeeds
    if_missing: >
      use LangExtract's currently supported Gemini model for extraction while
      retaining Gemini 3.7 for global synthesis; do not fork LangExtract

work_units:
  - id: acquire_source
    objective: persist the authoritative input and source metadata
    product_value: source custody and reproducibility
    inputs:
      - source_url_or_file_or_transcript
    context_required:
      architecture_decision: acquisition and source-custody sections only
      component_documentation: yt-dlp/FFmpeg only if applicable
      previous_outputs: none
      local_files_to_inspect: supplied source
      explicitly_not_required:
        - semantic extraction research
        - historical V1-V3 architecture
    systems_used:
      - yt-dlp_if_remote
      - FFmpeg_if_required
    actions:
      - capture metadata
      - retain original transcript/captions when provided
      - hash acquired inputs
    observable_outputs:
      - source/media-info.json
      - acquired media or transcript
    product_inspection:
      - source identity correct
      - no silent substitution of an automatic caption for a supplied transcript
    acceptance: source can be reproduced and identity/provenance is explicit
    failure_classes:
      - unsupported_url
      - inaccessible_media
      - codec_problem
    retry: use documented downloader/media behavior
    reversal_trigger: none for ordinary extractor failure
    next: represent_source

  - id: represent_source
    objective: create the trustworthy canonical source representation
    product_value: all later evidence resolves to a stable source
    inputs:
      - acquired source
    context_required:
      architecture_decision: ASR and canonical-source contract
      component_documentation: Scribe v2 or selected fallback
      previous_outputs:
        - source/media-info.json
      local_files_to_inspect:
        - acquired media/transcript
      explicitly_not_required:
        - synthesis prompts
        - external verification
    systems_used:
      - Scribe_v2_if_no_trustworthy_transcript
      - canonical_source_adapter
    actions:
      - transcribe when needed
      - preserve raw provider output
      - generate stable segment IDs
      - build source.txt deterministically
      - map each segment to character bounds
    observable_outputs:
      - source/source.json
      - source/source.txt
      - source/transcript.json
    product_inspection:
      - inspect important names/numbers/technical vocabulary
      - inspect speaker assignment when relevant
      - verify beginning/middle/end samples
    acceptance: no observed meaning-changing ASR defect in inspected critical material
    failure_classes:
      - asr_semantic_error
      - diarization_error
      - transcript_parse_error
    retry:
      first: fix configuration or keyterms
      second: Deepgram_Nova_3_Multilingual
      local_privacy_case: faster_whisper
    reversal_trigger: >
      default and pre-authorized fallback both fail materially on representative corpus
    next: extract_evidence

  - id: visual_evidence
    objective: capture source information present visually but absent from transcript
    product_value: prevents transcript-only loss on slide/demo/chart-heavy video
    inputs:
      - canonical source
      - original video
    context_required:
      architecture_decision: conditional visual branch
      component_documentation: Gemini video input
      previous_outputs:
        - source/source.json
      local_files_to_inspect:
        - original video
      explicitly_not_required:
        - external web research
    systems_used:
      - Gemini_3_7_Flash
    actions:
      - decide whether visuals are semantically material
      - when material, extract timestamped visual observations
    observable_outputs:
      - evidence/visual-evidence.json
    product_inspection:
      - observations correspond to visible source evidence
      - no visual inference is mislabeled as transcript evidence
    acceptance: all retained visual observations have source time references
    failure_classes:
      - visual_branch_not_needed
      - provider_failure
      - ungrounded_visual_claim
    retry: documented provider retry then omit only if visuals are demonstrably nonessential
    reversal_trigger: material visual knowledge cannot be represented reliably
    next: extract_evidence

  - id: extract_evidence
    objective: acquire high-recall grounded semantic knowledge units
    product_value: preserve substantive source knowledge before compression
    inputs:
      - source/source.txt
      - source/source.json
      - evidence/visual-evidence.json_if_present
    context_required:
      architecture_decision: extraction taxonomy and evidence contract
      component_documentation: LangExtract
      previous_outputs:
        - canonical source
      local_files_to_inspect:
        - source/source.txt
      explicitly_not_required:
        - NotebookLM implementation details
        - agent platform architecture
    systems_used:
      - LangExtract_1_6_0
      - Gemini_model_via_LangExtract
    actions:
      - run targeted multi-pass extraction
      - retain exact source spans
      - deduplicate only semantically redundant units without deleting distinct caveats
      - map spans to segment/time evidence
    observable_outputs:
      - evidence/evidence.jsonl
      - evidence/extraction-review.html
    product_inspection:
      - thesis/claims
      - mechanisms
      - procedures
      - arguments/reasons
      - examples
      - qualifications/exceptions
      - corrections/contradictions
      - uncertainty/predictions/opinions
      - entities/relationships
    acceptance: >
      representative must-find items are present and source evidence resolves exactly
    failure_classes:
      - missed_semantic_class
      - ungrounded_extraction
      - provider_schema_error
      - excessive_duplicates
    retry:
      - correct examples/schema
      - use documented multiple passes
      - targeted extraction pass
    reversal_trigger: >
      configured LangExtract cannot achieve acceptable important-unit recall
      or source grounding on representative sources
    next: synthesize

  - id: synthesize
    objective: construct coherent global source understanding
    product_value: turn evidence units into a useful knowledge artifact without losing nuance
    inputs:
      - full canonical source
      - grounded evidence units
      - visual evidence if present
    context_required:
      architecture_decision: global synthesis and epistemic rules
      component_documentation: Gemini 3.7 structured output
      previous_outputs:
        - source/source.txt
        - evidence/evidence.jsonl
      local_files_to_inspect: []
      explicitly_not_required:
        - downloader details
        - historical implementation
    systems_used:
      - Gemini_3_7_Flash
    actions:
      - synthesize global thesis and hierarchy
      - link corrections and contradictions
      - preserve uncertainty and speaker stance
      - require evidence-unit references
      - propose missing evidence instead of inventing support
    observable_outputs:
      - synthesis/synthesis.json
    product_inspection:
      - global coherence
      - no flattened contradictions
      - no opinion-to-fact conversion
      - important mechanisms/examples retained
    acceptance: all substantive source assertions reference evidence or a repair request
    failure_classes:
      - unsupported_claim
      - major_omission
      - epistemic_flattening
      - contradiction_loss
    retry:
      - prompt/configuration correction
      - targeted evidence extraction
      - rerun synthesis only
    reversal_trigger: repeated material quality failure after support repair
    next: support_gate

  - id: support_gate
    objective: distinguish exact evidence, semantic support and external truth
    product_value: trust
    inputs:
      - synthesis/synthesis.json
      - evidence/evidence.jsonl
      - canonical source
    context_required:
      architecture_decision: support semantics
      component_documentation: Gemini only for semantic review
      previous_outputs:
        - synthesis
        - evidence
      local_files_to_inspect: []
      explicitly_not_required:
        - external truth sources unless verification requested
    systems_used:
      - deterministic_span_validation
      - Gemini_3_7_Flash_for_bounded_semantic_support
    actions:
      - verify source intervals
      - verify evidence IDs
      - review normalized/global claims that exceed verbatim evidence
    observable_outputs:
      - synthesis/support-review.json
    product_inspection:
      - unsupported major claims absent or explicitly marked
    acceptance: zero unresolved unsupported major source-grounded claims
    failure_classes:
      - invalid_span
      - unsupported_normalization
      - ambiguous_support
    retry: return affected items to extraction/synthesis
    reversal_trigger: systematic inability to ground the desired artifact
    next: optional_external_verification

  - id: optional_external_verification
    objective: investigate external truth without corrupting source fidelity
    product_value: additional trust for factual claims when required
    inputs:
      - selected verifiable source claims
    context_required:
      architecture_decision: source_vs_truth distinction
      component_documentation: Gemini Search grounding
      previous_outputs:
        - synthesis/support-review.json
      local_files_to_inspect: []
      explicitly_not_required:
        - unselected minor source details
    systems_used:
      - Gemini_3_7_Flash_with_Search
    actions:
      - verify only claims selected by policy/user
      - store corroborated/contradicted/mixed/unverifiable separately
    observable_outputs:
      - synthesis/external-verification.json
    product_inspection:
      - source wording is unchanged
      - verification evidence is separate
    acceptance: no external result silently rewrites source history
    failure_classes:
      - insufficient_external_evidence
      - conflicting_sources
    retry: mark unresolved rather than hallucinate certainty
    reversal_trigger: none; verification can remain unresolved
    next: compile

  - id: compile
    objective: create durable human and machine knowledge artifacts
    product_value: useful final product
    inputs:
      - validated synthesis
      - evidence
      - verification if present
    context_required:
      architecture_decision: final artifact contract only
      component_documentation: schema/template library only
      previous_outputs:
        - validated synthesis
        - evidence
      local_files_to_inspect:
        - output templates
      explicitly_not_required:
        - model research
        - agent ecosystem research
    systems_used:
      - deterministic_compiler
    actions:
      - validate schema
      - render knowledge.json
      - render knowledge.md
    observable_outputs:
      - output/knowledge.json
      - output/knowledge.md
    product_inspection:
      - readable hierarchy
      - evidence links
      - epistemic labels
      - corrections/contradictions
      - complete machine schema
    acceptance: human artifact is useful and machine artifact validates
    failure_classes:
      - schema_error
      - rendering_error
    retry: compiler/template repair only
    reversal_trigger: none for ordinary rendering defects
    next: product_acceptance

vertical_slice:
  source: >
    Bind PROJECT_REAL_SOURCE_DE_FINANCE_01 to a real 90-120 minute German
    multi-speaker financial/business discussion from the target corpus.
  complete_flow:
    - acquire_or_import
    - represent_source
    - inspect_ASR
    - conditionally_extract_visual_evidence
    - extract_grounded_evidence
    - synthesize
    - support_gate
    - compile
    - compare_with_source
    - compare_with_NotebookLM
  expected_artifact:
    - knowledge.md
    - knowledge.json
    - evidence.jsonl
    - source.json
  quality_requirements:
    - central positions and major reasoning retained
    - material numerical claims retained correctly
    - mechanisms and procedures retained
    - corrections/contradictions retained
    - predictions and opinions explicitly typed
    - material caveats retained
    - every major sourced assertion has resolvable evidence
  acceptance: >
    No critical unsupported claim, no critical epistemic misclassification,
    no critical correction/contradiction loss, and strong recall on a
    predeclared bounded must-find set.

end_to_end:
  sources:
    - German_financial_or_business_discussion_90_to_120_minutes
    - English_technical_interview_90_to_120_minutes
    - existing_transcript_with_or_without_timestamps
  expected_artifacts:
    - complete source package
    - grounded evidence package
    - validated structured synthesis
    - useful Markdown knowledge artifact
  quality_requirements:
    - high important-insight recall
    - source fidelity
    - semantic depth
    - global coherence
    - uncertainty and contradictions preserved
    - traceable evidence
  reliability_requirements:
    - rerun failed stage without repeating successful expensive stages
    - explicit terminal state for each stage
    - provider/configuration versions recorded
    - no silent fallback that changes product semantics
  acceptance: >
    All three representative source classes produce artifacts a reviewer
    would choose for serious knowledge reuse over an ordinary summary.

custom_code:
  - item: canonical_source_and_span_time_adapter
    authorization: approved
    smallest_required_surface: >
      stable source/segment IDs, hashes, char intervals and deterministic
      char-to-time mapping only

  - item: job_manifest
    authorization: approved
    smallest_required_surface: >
      stage status, input/config hashes, component versions, output paths,
      retry/error metadata

  - item: deterministic_compiler
    authorization: approved
    smallest_required_surface: >
      schema validation plus Markdown/JSON templates; no semantic generation

final_success: >
  A real EN/DE long-form source can be turned into a high-value,
  evidence-linked knowledge artifact with preserved qualifications,
  uncertainty, corrections and contradictions; ordinary failures resume
  cleanly; no bespoke semantic infrastructure was invented.
```

## Product validation, anti-drift audit and evidence register

The validation plan should answer the product question with the smallest credible evidence set, not grow into another architecture project.

**Representative runs.** Use three sources: the German financial/business discussion described above; a 90–120 minute English technical interview containing mechanisms, design reasoning or procedures; and one existing transcript that bypasses ASR. When a project video has substantive slides/demos, ensure at least one test exercises the visual-evidence branch.

Before looking at the final artifact, create a bounded **must-find sheet** of roughly 20–30 consequential items across the source. Include at least a thesis/central position, numerical claim, mechanism, procedure, argument, example, material caveat, uncertainty, prediction/opinion, correction and disagreement where the source contains them. This is a proposed acceptance method, not an external benchmark.

For each run, inspect three independent dimensions:

| Dimension | Required evidence |
|---|---|
| **Knowledge value** | Major must-find items are retained; mechanisms/procedures/arguments/examples survive; organization is useful rather than a transcript dump. |
| **Trust** | Every major source-grounded assertion resolves to evidence; unsupported synthesis is absent or labeled; fact/opinion/prediction status remains correct; external verification does not rewrite source content. |
| **Operations** | A deliberately interrupted semantic stage resumes without repeating acquisition/ASR; provider failure is visible; artifacts remain inspectable without the originating agent conversation. |

A reasonable release gate is **zero critical unsupported final claims, zero critical opinion/prediction→fact conversions, zero critical missed corrections/contradictions, all major cited evidence resolvable, and at least 90% weighted recall on the predeclared important-item set**. The 90% number is a recommended product threshold rather than an industry benchmark; a single catastrophic omission can still fail the source even if the arithmetic passes.

**NotebookLM comparison is mandatory for the first two long sources.** NotebookLM already provides strong source-grounded long-source interaction and cited notebook knowledge. citeturn1search1turn1search3turn1search4 The comparison is not “which Markdown is prettier?” It is: which product preserves more important knowledge, qualifications, disagreements and evidence? The custom composition only deserves production status if its structured grounding/reproducibility advantages do not come at a material loss in semantic value.

Podwise is worth one secondary comparison when the source is a conventional podcast because it already generates transcript, summary, mind map and insights and has an actual automated API/CLI path. citeturn18search1turn18search3 Fabric's `extract_wisdom`/study-note workflow is likewise a useful cheap baseline, not an architecture candidate. citeturn15search6

**Final anti-drift audit**

**TARGET audit — PASS, subject to real vertical evidence.** The architecture deliberately spends semantic-model capability where meaning matters and uses exact source evidence where trust matters. It does not optimize for the fewest stages.

**Completeness audit — PASS.** Source acquisition, source fidelity, audio/video differences, semantic extraction, structured representation, global understanding, source support, external truth distinction, compilation, evaluation and recovery all have owners.

**Reuse audit — PASS.** Every complex semantic or media function is assigned to an existing system. The only bespoke responsibilities are cross-system custody/mapping, state metadata and deterministic presentation.

**Quality audit — PASS with one important caveat.** Hosted ASR and a current frontier long-context model were selected rather than forcing the product local/free. This deliberately prevents locality and cost from degrading the target. Actual whole-product quality remains to be proven by the EN/DE vertical tests.

**Sunk-cost audit — PASS.** No existing TTK runner, schema, compiler or evaluation tool is selected because it already exists. Existing code can be reused only after demonstrating conformance to the new responsibility and product tests.

**Complexity audit — PASS.** WhisperX, GLiNER2, DocETL, VideoDB, Azure media indexing and a general workflow engine are all omitted from the default architecture because their incremental value does not currently earn an additional production seam.

**Custom-code audit — PASS.** No custom semantic model, chunker, extraction framework, ASR stack or agent framework is authorized.

**Evidence audit — PARTIAL only with respect to historical project versions.** Current-system conclusions are based on current external sources. Topic-level V1/V2/V2.1/V3 claims cannot be audited because the project attachments were not retrievable in this run; the report intentionally does not fake that reconciliation.

**Execution audit — PASS.** The selected systems, ownership boundaries, outputs, tests, fallbacks, work units and reversal conditions are fixed closely enough that an implementation AI should diagnose integration problems rather than reopen architecture research.

**Evidence register**

| Current evidence | Date/version | Fact supported | Confidence |
|---|---|---|---|
| Google NotebookLM help/product documentation. citeturn1search0turn1search1turn1search4 | current 2026 docs | Audio/document/YouTube source support, source-grounded citations, large source limits, 80+ language behavior. | High |
| Google NotebookLM 2026 product update. citeturn1search3 | June 2026 | Current long-document/agent-backed NotebookLM improvements. | High for advertised capability; internal quality evaluations remain vendor evidence |
| Gemini Notebook Enterprise API docs and RPC index. citeturn2search3turn2search4turn13view2 | `v1alpha`, Preview | Current programmatic services focus on notebook/source/discovery/Audio Overview; no documented equivalent of full notebook chat/report generation found. | High |
| Gemini Notebook Enterprise product/licensing. citeturn17search5turn17search9 | 2026 | Enterprise pricing/security/licensing context. | High |
| Podwise product and agent docs. citeturn18search1turn18search3turn18search5turn18search11 | updated July 2026 | Transcript/summary/mind-map/insight product plus API, CLI, MCP and agent skills. | High for capability; adoption figures vendor-reported |
| Podwise pricing. citeturn18search0turn18search8 | current Aug. 2026 | Pro/API pricing and export capabilities. | High |
| OpenClaw media-understanding docs. citeturn19search4turn19search7 | current Aug. 2026 | Provider/local audio/video understanding and explicit best-effort/fallback behavior. | High |
| Anthropic Claude Code autonomy/SDK announcement. citeturn20search3 | Sept. 2025 | Checkpoints, hooks, subagents, Agent SDK execution capabilities. | High |
| OpenAI Codex Plugins/Skills documentation. citeturn19search2turn19search5 | June–Aug. 2026 | Codex reusable plugins/skills and workflow packaging. | High |
| Google Antigravity I/O announcement. citeturn19search3 | May 19, 2026 | Antigravity 2.0 desktop/CLI/SDK, custom agents/skills and managed-agent ecosystem. | High |
| yt-dlp release and license. citeturn15search7turn22search0 | `2026.07.04` | Current active release and Unlicense. | High |
| FFmpeg release evidence. citeturn21search0turn21search3 | `9.0`, Aug. 4, 2026 | Current major stable release. | High |
| ElevenLabs Scribe pricing/features. citeturn16search0turn7search1 | Scribe v2 current | 90+ languages, timing/diarization/keyterm capabilities and $0.22/h base rate. | High for documented product capability; actual project WER unproven |
| ElevenLabs Zero Retention documentation. citeturn21search1 | current | Enterprise ZRM can cover STT audio input and text output. | High |
| Deepgram pricing/current Nova-3 docs. citeturn16search1turn7search2 | Nova-3 current | Multilingual/German-relevant hosted fallback, EU endpoint and current rate. | High for service features; vendor benchmark claims treated cautiously |
| AssemblyAI pricing/current model docs. citeturn16search2turn7search3 | Universal-3.5 Pro | Current prerecorded pricing, language/keyterm/diarization options and EU endpoint. | High |
| faster-whisper release/license. citeturn6search0turn22search1 | `1.2.1` | Mature current local fallback, MIT licensing. | High |
| WhisperX release/license/issues. citeturn6search1turn22search2turn22search9 | `3.8.6` stable found; 2026 issue state | Active alignment/diarization project; BSD-2 code license; German default alignment-model licensing concern. | High for repository facts; legal impact should receive formal review if deployed commercially |
| LangExtract introduction/repository/releases. citeturn21search2turn8search0turn8search8 | `1.6.0`, Jul. 1, 2026 | Exact source character grounding, structured extraction, long-document multi-pass mechanics, current release/maturity. | High |
| Gemini 3.7 Flash official model docs/release notes. citeturn24search0turn24search1turn24search3turn24search7 | GA Aug. 13, 2026 | Newest current Flash model; 1M context, 65k output, multimodality, structured output, search grounding and GA production status. | High for capability; lower operational-history confidence because model is newly released |
| Gemini pricing. citeturn16search3turn24search0 | current through Dec. 31, 2026 | $0.75/M input and $3.75/M output promotional 3.7 Flash pricing. | High |
| LlamaExtract v2 docs/pricing. citeturn17search12turn17search4turn10search5 | v2 current | Schema extraction APIs, tiers/versioning, citations/confidence and usage-based pricing. | High |
| LlamaIndex ExtractBench result. citeturn10search1 | Aug. 2026 | Evidence that Agentic Plus performs strongly on structured document extraction/grounding benchmark. | Medium for cross-product conclusion because benchmark is vendor-adjacent and does not measure this transcript target |
| DocETL repository/current release. citeturn8search5 | `0.3.0`, Jun. 17, 2026 | Real declarative LLM data pipeline/optimizer alternative. | High |
| GLiNER2 repository/model docs. citeturn9search0turn9search6 | `1.3.1`, May 2026 | Current compact local entity/structured extraction capabilities. | High |
| Azure Video Indexer/Content Understanding docs. citeturn15search0turn15search1turn15search4 | current 2026 | Multilingual media transcription, diarization, timing, structured media insights/entities/keyframes. | High |
| Fabric repository. citeturn15search2turn15search6 | current 2026 | Mature cross-platform pattern framework with YouTube/podcast knowledge-extraction workflows. | High for framework capability; semantic trust depends on pattern/model |

**Final recommendation:** build **the thin glue around the proven systems**, not another TTK semantic engine. Use Scribe v2 to obtain a high-quality timed/speaker-aware source representation when no trustworthy transcript exists; LangExtract to deliberately acquire high-recall, exactly grounded semantic evidence; Gemini 3.7 Flash to reason globally across the complete source and organize that evidence into genuinely useful knowledge; and deterministic checks/templates to make the result auditable and durable. Use NotebookLM as the whole-product benchmark that the production artifact must justify itself against. citeturn16search0turn21search2turn24search1turn1search1