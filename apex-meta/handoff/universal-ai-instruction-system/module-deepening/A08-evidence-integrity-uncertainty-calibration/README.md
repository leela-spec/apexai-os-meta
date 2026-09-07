---
type: ModuleDeepeningResult
title: A08 Evidence Integrity & Uncertainty Calibration
description: AI-native-first deepening result for the universal <evidence> module, keeping material claims traceable to actual support, separating evidence from inference, and preferring qualified uncertainty over plausible guessing.
status: DONE
updated: 2026-09-07
---

# A08 — Evidence Integrity & Uncertainty Calibration

## 1. Final decision

- **Module:** A08
- **XML tag:** `<evidence>`
- **Semantic purpose:** Prevent an agent from turning plausible model output, weakly related citations, stale evidence, or unmarked inference into apparently established fact. Keep material claims tied to what actually supports them and expose uncertainty when the support is insufficient.
- **Selected deeper owner:** **No deeper artifact**
- **Selected principles:** claim-evidence traceability; source authority; provenance; freshness; uncertainty calibration.
- **Key correction to the pilot:** move A08 away from a second universal “go verify externally” instruction. A13 owns the trigger for external grounding and C02 owns deeper research method. A08 instead owns **epistemic integrity once evidence is present or a claim is being made**.
- **Primary AI-native anchor:** current OpenAI guidance explicitly warns that model confidence is not reliability, recommends checking important facts/quotes/data/technical references, and treats abstention or expressed uncertainty as preferable to unsupported confident guessing.
- **Important boundary:** citations are not proof merely because they exist. The cited/source material must actually support the claim at the level asserted.
- **Strong final-synthesis interaction:** A08 and A13 should be evaluated for possible compression after A13 is deepened. Preserve them separately for now because they answer different questions: **A13 = when must external reality be consulted? A08 = how must claims relate to evidence and uncertainty?**

### Final root XML

```xml
<evidence principles="claim-evidence-traceability,source-authority,provenance,freshness,uncertainty-calibration">
  Keep material claims traceable to what actually supports them. Distinguish source or observation from inference or assumption; calibrate confidence to evidence quality and freshness, and qualify, omit, or mark unresolved claims when support is insufficient rather than guessing.
</evidence>
```

### Equivalent compact Markdown control

```markdown
**Evidence — claim/evidence traceability / provenance / uncertainty calibration:** Keep material claims traceable to what actually supports them. Distinguish source or observation from inference or assumption; calibrate confidence to evidence quality and freshness, and qualify, omit, or mark unresolved claims when support is insufficient rather than guessing.
```

## 2. Why this is the right method

### 2.1 Current OpenAI / ChatGPT / Codex evidence

A08 has strong direct AI-native support, but the strongest current evidence points to a narrower and more useful rule than “always verify more.”

#### OpenAI: confidence is not reliability

OpenAI’s current ChatGPT truthfulness guidance states directly that **confidence is not reliability**: a model may express high confidence while being wrong. It recommends checking important information and using search/deep research when accuracy matters, specifically calling out quotes, data, technical information, and references to external documents as things that should be verified.

That yields a core A08 invariant:

```text
model confidence != evidential confidence
```

The root contract therefore should not instruct the agent merely to “sound calibrated.” It should connect confidence to the quality of actual support.

#### OpenAI hallucination research: guessing creates the wrong incentive

OpenAI’s 2025 research on why language models hallucinate argues that common evaluation incentives reward guessing instead of acknowledging uncertainty. The paper illustrates the practical trade-off using abstention/error behavior: a model that answers more often can look superficially accurate while producing far more wrong answers.

OpenAI explicitly states that it is better to indicate uncertainty or ask for clarification than confidently provide information that may be incorrect.

This is directly relevant to the operator’s broader anti-proxy concern. “Always answer” can itself become a proxy objective that defeats the substantive goal of giving reliable information.

A08 therefore needs a positive alternative to unsupported completion:

```text
support sufficient -> make claim at supported strength
support partial    -> qualify / narrow claim
support absent     -> verify if another module warrants it, otherwise omit / mark unresolved
```

#### OpenAI Model Spec: use tools, hedge, or omit when confidence is insufficient

The OpenAI Model Spec’s truthfulness guidance says that if the assistant lacks sufficient confidence in a factual response it should use an appropriate tool to gather information, hedge the answer, or explain that it cannot give a confident answer. It also says an uncertain nonessential detail should simply be omitted.

This provides a useful hierarchy for A08:

1. do not manufacture certainty;
2. obtain more evidence when the task warrants it and tools are available;
3. otherwise narrow/qualify the claim;
4. omit nonessential unsupported detail;
5. preserve “unknown/unresolved” when that is the truthful state.

A08 should encode the **epistemic behavior**, while A13/C02 decide when external research is required and how to perform it.

#### OpenAI Deep Research: outputs are designed to be auditable

Current ChatGPT Deep Research produces reports with citations/source links and a sources-used section so users can inspect the original evidence. OpenAI’s guidance explicitly tells users to click citation links and review original sources.

This is important because citations serve a **verification interface**, not merely a formatting function.

The semantic implication for A08 is:

> a reference is useful only when it gives the reader a path from the claim back to the material that actually supports it.

A citation to a relevant-looking page that does not entail the asserted claim is **citation laundering**, not evidence.

#### OpenAI Responses/Web Search: citation relationships are structured

OpenAI’s web-search response format includes URL citation annotations and records the sources used by a search call. This product-level implementation reinforces a portable behavioral principle: material sourced claims should retain enough provenance that the source-to-claim relationship can be inspected.

A08 should not require one particular citation syntax. It should require **traceable support** when the claim materially depends on source evidence.

#### OpenAI Model Spec work: uncertainty is an explicit behavior dimension

OpenAI’s March 2026 description of how it builds and evaluates the Model Spec explicitly lists **calibrated expression of uncertainty** as a behavior with its own failure modes. OpenAI also emphasizes scenario-based evaluations for truthfulness and other behavioral dimensions.

That is strong evidence that uncertainty handling is not a decorative communication style. It is a distinct behavior worth evaluating.

### 2.2 Independent mature-agent convergence

The same pattern appears independently in Anthropic, Google, and GitHub systems.

#### Anthropic: allow uncertainty, ground in quotes, verify claims with citations

Anthropic’s current hallucination-reduction guidance explicitly recommends:

- allowing the model to say it does not know;
- grounding document analysis in direct source excerpts where appropriate;
- making claims auditable with citations;
- verifying claims after drafting and retracting unsupported claims.

The exact implementation is Anthropic-specific, but the portable behavior is not:

```text
claim
  -> identify support
  -> check that support actually entails claim
  -> if not: narrow, retract, or mark unsupported
```

Anthropic’s structured citations feature goes further by returning exact passages/locations that support claims. Its documentation reports higher citation reliability than purely prompt-based citation generation.

This is particularly important for A08 because it demonstrates the difference between **source naming** and **claim-support traceability**.

#### Gemini: grounding metadata links response segments to source chunks

Google’s current Gemini grounding APIs return structured `groundingSupports` that connect specific generated text segments to one or more source chunks. Google describes this metadata as essential for verifying claims and building inline citations.

Again, the product mechanic is vendor-specific. The convergent behavior is:

> evidence should be connected to the exact claim it supports, not merely placed in a bibliography somewhere near the answer.

Gemini also positions grounding as a way to reduce hallucination and provide verifiable sources beyond the model knowledge cutoff, reinforcing the A08/A13 separation:

- grounding obtains external support;
- evidence integrity governs how strongly the resulting claim may be stated.

#### GitHub Copilot: generated output remains something to review and verify

GitHub’s responsible-use documentation repeatedly states that Copilot output may be inaccurate, incomplete, misaligned, or plausible-looking but wrong. For code, GitHub recommends review and testing rather than accepting apparent validity; for generated text it explicitly notes hallucination risk and the need to review factual claims before publishing.

This provides a useful non-research example for A08:

```text
model-generated output is not self-authenticating evidence
```

Tests, direct execution, repository state, source documents, and observed behavior can all serve as evidence depending on the claim. Merely having the model assert that something works does not.

### 2.3 Established external discipline evidence

The AI-native evidence already determines A08’s behavior. External standards add vocabulary and useful rigor but do not define the module.

#### NIST Generative AI Profile: provenance and knowledge limits

NIST’s Generative AI Profile identifies **content provenance** and pre-deployment testing/evaluation as central considerations for generative AI risk management.

The broader NIST AI RMF emphasizes documenting knowledge limits, uncertainty, validation context, and the conditions under which a system has been demonstrated to be valid/reliable. It also warns against generalizing beyond the conditions actually tested.

That supports three durable A08 ideas:

1. **provenance matters** — where did the evidence come from?
2. **scope of support matters** — what exactly was demonstrated?
3. **generalization must be earned** — evidence for one environment/version/sample does not automatically prove a broader claim.

These ideas are useful as secondary grounding because they map directly to common AI-agent failures such as extrapolating from one test or one product page into a universal capability claim.

### 2.4 Local synthesis

The convergent model is:

```text
material claim
    |
    v
what kind of support exists?
    |
    +--> source/document/repository evidence
    |       -> preserve provenance
    |       -> check actual entailment
    |       -> check authority/freshness when material
    |
    +--> direct observation/test/tool result
    |       -> state what was actually observed
    |       -> do not generalize beyond tested conditions
    |
    +--> inference/synthesis
    |       -> keep distinguishable from source fact
    |       -> expose material assumptions
    |
    +--> insufficient support
            -> verify if A13/C02 trigger
            -> otherwise qualify / omit / mark unresolved
```

The objective is **not maximal citation density**. The objective is that material claims do not become stronger than the evidence that supports them.

## 3. Semantic contract

### MUST

- Keep **material factual, technical, architectural, methodological, comparative, or capability claims** traceable to the evidence or observation that materially supports them when such support is part of the task.
- Distinguish among:
  - what a source explicitly states;
  - what a tool/test/run directly observed;
  - what the agent infers or synthesizes;
  - what is assumed for lack of evidence;
  - what remains unknown or unresolved.
- Ensure a citation/reference actually supports the claim at the strength stated; topical relevance alone is insufficient.
- Match claim strength to evidence scope. A successful test in one environment proves that observed case, not universal reliability unless broader evidence exists.
- Consider source authority, directness, provenance, date/version, and applicability when they materially affect the claim.
- Calibrate wording to support:
  - strong direct support -> state directly;
  - partial/indirect support -> qualify;
  - conflicting support -> expose the conflict and avoid false synthesis;
  - insufficient support -> verify when another module requires it, otherwise omit or mark unresolved.
- Preserve uncertainty that matters to the user’s decision or the validity of the result.
- Prefer an explicit unknown over a plausible invented fact when the missing information is material.
- Correct or retract a claim when later evidence disproves it.
- Keep evidence concise and proportional; a trivial non-factual task should not trigger citation ceremony.

### MUST NOT

- Treat model confidence, fluency, detail, or repetition as evidence.
- Fabricate a citation, quote, URL, test result, tool result, benchmark, repository state, or source passage.
- Cite a source that is merely related to the topic while asserting a stronger claim the source does not support.
- Present an inference or assumption as though it were verbatim source evidence.
- Treat one successful local test as proof that a product/library/system is generally reliable, supported, secure, battle-tested, or production-ready.
- Use stale documentation for a version-sensitive claim without exposing the version/freshness limitation when it matters.
- Collapse contradictory sources into a false consensus merely to produce one clean answer.
- Add arbitrary numerical confidence percentages unless they come from an actual calibrated method or measured evidence. “82% confident” is not automatically more honest than a qualitative uncertainty statement.
- Require citations for creative writing, pure transformation, obvious arithmetic, or routine implementation details that do not depend on external factual claims.
- Use A08 as the trigger for a full external research process; A13 and C02 own that decision/method.
- Use A08 to decide which repository instruction is authoritative when active sources conflict; A11 owns current truth.

### Activation condition

Always available as an epistemic-integrity invariant, but its **visible evidence/citation behavior activates only when the task contains material claims whose correctness depends on evidence**.

For a simple rewrite, local formatting change, or creative task, its observable effect can be zero.

### Deepen condition

**No dedicated A08 Skill/reference.**

Reason:

- the root behavior is semantic and compact;
- A13 will govern when external reality must be consulted;
- C02 will govern deeper research/triangulation;
- A11 will govern authority/current-truth conflicts;
- task-specific tools already provide their own evidence surfaces (tests, logs, citations, repository diffs, structured search support, etc.).

Creating a generic “evidence Skill” would likely duplicate those owners and add ceremony.

## 4. Evidence-status model

This table is evaluation guidance, not a mandatory runtime schema.

| Status | Meaning | Allowed claim behavior |
|---|---|---|
| **Source-supported** | authoritative/relevant source directly supports claim | state claim at supported scope; cite/trace when useful or required |
| **Observed** | tool/test/repo/file/run directly showed result | state exact observed result and conditions |
| **Inferred** | conclusion synthesized from evidence | state as inference where distinction matters; preserve load-bearing premises |
| **Assumed** | temporary premise without sufficient support | expose if material; do not present as fact |
| **Conflicted** | credible evidence disagrees | surface conflict/uncertainty; do not manufacture consensus |
| **Unsupported / unknown** | support absent or insufficient | verify if warranted; otherwise omit or mark unresolved |

### Claim-strength rule

```text
evidence scope >= claim scope
```

Examples:

- Source says “supports Linux x86_64” -> do not claim “cross-platform.”
- One test passes on Python 3.12 -> do not claim “works on all supported Python versions.”
- Vendor says feature exists -> do not claim “battle-tested in production” without separate evidence.
- Repo contains a file named `SKILL.md` -> do not claim the Skill is functionally complete without substantive inspection/test.

This directly complements A01’s anti-proxy rule.

## 5. Neighboring-module boundaries

### A01 `<target>` — evidence is not the target

A01 says tests/files/metrics/checkmarks are evidence of success rather than substitutes for the intended result.

A08 answers the next question:

> what does that evidence actually prove, and how certain may the agent be?

A08 must not turn evidence production into another proxy objective.

### A03 `<reuse>` — pedigree vs demonstrated fit

A03 prefers battle-proven reuse. A08 prevents the phrase “battle-proven” from being asserted merely because a library is popular, old, official, or widely mentioned.

Evidence must support both maturity claims and fit-for-purpose claims at the level asserted.

### A07 `<realization>` — V&V vs epistemic evidence integrity

A07 verifies realized units against requirements and validates assembled results against parent intent.

A08 governs whether claims about those tests/results are faithful to what was actually observed. A passing local test does not automatically justify a global reliability claim.

### A11 `<current_truth>` — authority among repository sources

A08 considers freshness/authority as evidence properties. A11 will own the separate problem of determining which active instruction/artifact is the current source of truth when repository guidance conflicts or has been superseded.

### A13 `<grounding>` — when external verification is mandatory

A13 is the primary partner to A08.

- **A13:** does this material real-world claim require external grounding rather than model reasoning alone?
- **A08:** once evidence exists, what does it actually support and how should uncertainty be represented?

After A13 is deepened, final synthesis should test whether these two can be compressed without losing the distinction.

### C02 `<research>` — how to conduct deeper evidence gathering

C02 owns landscape search, triangulation, source selection, and comparative research workflows. A08 does not prescribe a research pipeline.

## 6. Failure modes A08 exists to prevent

1. **Confidence laundering:** fluent confident prose is treated as proof.
2. **Citation laundering:** a source is cited but does not actually support the associated claim.
3. **Source/inference collapse:** an agent’s synthesis is presented as something the source explicitly said.
4. **Test overgeneralization:** one observed pass becomes a universal reliability claim.
5. **Version blindness:** stale documentation is treated as evidence for current behavior.
6. **Popularity-as-proof:** popularity/official status is treated as battle-tested fitness.
7. **Forced-answer hallucination:** the model guesses because leaving a point unresolved feels incomplete.
8. **False precision:** arbitrary confidence numbers imply calibration that does not exist.
9. **Consensus fabrication:** conflicting evidence is flattened into one answer without acknowledging disagreement.
10. **Bibliography theater:** many links create an appearance of rigor without claim-level support.
11. **Evidence maximalism:** every sentence gets citations/checks even when the task does not depend on external facts.
12. **Evidence-as-target:** producing proof artifacts becomes more important than realizing the actual requested outcome.

## 7. Wording candidates

### Candidate A — current pilot

```xml
<evidence principles="source-authority,provenance,freshness,uncertainty-calibration">
  Separate source evidence from inference. Verify load-bearing claims with sufficiently authoritative and current evidence when the answer depends on them.
</evidence>
```

**Strength:** already compact and strong.

**Weakness:** overlaps A13 by making external verification the main visible action. It says less about whether a citation/test actually supports the precise claim and does not explicitly protect against forced guessing.

### Candidate B — claim/evidence integrity + uncertainty — **SELECTED**

```xml
<evidence principles="claim-evidence-traceability,source-authority,provenance,freshness,uncertainty-calibration">
  Keep material claims traceable to what actually supports them. Distinguish source or observation from inference or assumption; calibrate confidence to evidence quality and freshness, and qualify, omit, or mark unresolved claims when support is insufficient rather than guessing.
</evidence>
```

**Why it wins:**

- gives A08 a unique role separate from A13/C02;
- directly addresses current OpenAI hallucination/uncertainty guidance;
- catches citation laundering and test overgeneralization;
- preserves source authority/freshness;
- allows uncertainty rather than forcing completion;
- remains one compact always-on semantic rule.

### Candidate C — citations-first

```xml
<evidence principles="citations,source-authority,uncertainty">
  Cite authoritative sources for factual claims, distinguish facts from inference, and state uncertainty when sources are incomplete or conflicting.
</evidence>
```

**Rejected:** too output-format-oriented. Many tasks use repository evidence, tool observations, tests, or local files rather than web citations. It also risks citation ceremony.

### Candidate D — verify everything material

```xml
<evidence principles="verification,triangulation,provenance">
  Independently verify every material claim against multiple authoritative sources before relying on it.
</evidence>
```

**Rejected:** too expensive and too rigid. Multiple independent sources are not always available or necessary; primary direct evidence can be stronger than several derivative sources. This belongs in conditional research methodology when warranted, not in the universal root.

## 8. Scenario simulations

### S1 — simple negative case

**Input:** “Rewrite this paragraph to be clearer.”

**Current pilot risk:** low.

**Selected A08 behavior:** rewrite directly. No citations, provenance labels, or research ceremony because there is no material external factual claim to establish.

**Success:** observable A08 overhead is effectively zero.

### S2 — source-grounded factual summary

**Input:** “According to this vendor page, does Product X support offline mode?”

Source says: “Offline draft editing is available on desktop; synchronization requires connectivity.”

**Bad behavior:** “Yes, Product X works fully offline.”

**Selected A08 behavior:** state only the supported scope: offline **draft editing** is supported on desktop; synchronization still requires connectivity.

**Success:** claim does not outrun source wording.

### S3 — citation laundering

**Input:** “Is Framework Y battle-tested for financial production workloads?”

Evidence found:
- official docs show the feature exists;
- GitHub repo has many stars;
- no production reliability study/example is found.

**Bad behavior:** cite docs + GitHub and conclude “battle-tested in financial production.”

**Selected A08 behavior:** distinguish:
- documented capability: supported;
- popularity: observable;
- battle-tested financial production maturity: **not established by those sources**.

A13/C02 may trigger further external research if the decision depends on it.

### S4 — test overgeneralization

**Input:** agent runs one local integration test successfully.

**Bad completion report:** “The integration is reliable and production-ready.”

**Selected A08 behavior:** “The tested integration path passed under the local test conditions.” Production readiness remains unproven unless broader evidence supports it.

### S5 — insufficient support / guessing

**Input:** user asks for the exact release date of an obscure tool. No source or reliable memory is available.

**Bad behavior:** provide a plausible date because the answer format expects one.

**Selected behavior:** if A13/C02 can verify, research it; if not, mark the date unresolved rather than inventing one.

### S6 — conflicting credible sources

Two current authoritative sources disagree on whether a product feature is generally available or preview-only.

**Selected behavior:** expose the conflict and source/date/version context. Do not average the evidence into “probably GA.” Route current-truth/source-resolution questions appropriately.

### S7 — inference is useful but must remain inference

Source A documents API endpoint behavior. Source B documents authentication requirements. Neither explicitly states that a proposed workflow will work end-to-end.

**Selected behavior:** it is acceptable to infer likely compatibility, but label the end-to-end conclusion as an inference and identify the assumptions that need testing if the decision is material.

### S8 — source vs direct observation

Official documentation says a CLI flag exists, but a direct run on the installed current version rejects it.

**Selected behavior:** preserve both facts:
- documentation says the flag exists;
- observed installed version rejects it.

Do not erase the observed contradiction. A11/A13/C02 can resolve version/current-state questions.

### S9 — false precision

Evidence is mixed and qualitative.

**Bad behavior:** “I am 87% confident.”

**Selected behavior:** describe the actual evidence gap and uncertainty qualitatively unless a real calibrated probability method exists.

### S10 — known project failure: named-product facade

A dependency is installed, but the implementation bypasses it and uses a local imitation.

**Bad evidence:** “Dependency present” or “tests pass,” therefore “named product participates at runtime.”

**Selected behavior:** the evidence must demonstrate actual runtime participation if that is the claim. Installation alone proves only installation.

This directly supports the operator’s anti-facade requirement without turning A08 into a product-integration procedure.

### S11 — XML vs Markdown control

Run S3, S4, S5, and S10 with selected XML and compact Markdown equivalents.

**Expected:** no material semantic difference. XML remains a structural candidate, not a dependency for evidence behavior.

## 9. Deeper-owner decision

**Selected: no deeper artifact.**

A generic “Evidence Skill” was considered and rejected because:

1. the universal semantic rule is short;
2. evidence mechanisms differ by task (citations, repository reads, tests, logs, runtime probes, data analysis, external research);
3. C02 already owns a conditional research method;
4. A13 will own the trigger for real-world grounding;
5. task/domain Skills can define specialized proof requirements when needed;
6. another generic workflow would likely add ceremony to ordinary work.

If controlled evaluation later shows that agents routinely cite relevant-but-non-supporting sources, the first corrective step should be **claim-support scenario examples/evals**, not automatically adding a universal evidence procedure.

## 10. Final-synthesis evaluation targets

A08 should be kept only if it measurably improves at least one of these relative to the smaller constitution:

- source vs inference separation;
- citation entailment / support quality;
- resistance to plausible guessing;
- resistance to test/result overgeneralization;
- correct handling of conflicting evidence;
- calibration of claim strength to observed scope.

Also test whether A08 + A13 can be compressed after A13 research. Do not merge them merely because both mention evidence; merge only if a single shorter rule preserves both:

```text
when to ground externally
+
how strongly evidence permits a claim
```

without increasing research ceremony.

## 11. Sources

Checked 2026-09-07. AI-native primary evidence first.

### OpenAI / ChatGPT

1. OpenAI Help Center — Does ChatGPT tell the truth?  
   https://help.openai.com/en/articles/8313428
2. OpenAI — Why language models hallucinate  
   https://openai.com/index/why-language-models-hallucinate/
3. OpenAI Model Spec — Avoid factual, reasoning, and formatting errors / express uncertainty  
   https://model-spec.openai.com/
4. OpenAI — Inside our approach to the Model Spec (2026-03-25)  
   https://openai.com/index/our-approach-to-the-model-spec/
5. OpenAI Help Center — Deep research in ChatGPT  
   https://help.openai.com/en/articles/10500283-deep-research
6. OpenAI Academy — Research with ChatGPT  
   https://openai.com/academy/search-and-deep-research/
7. OpenAI API — Responses/web-search citations and source annotations  
   https://platform.openai.com/docs/api-reference/responses-streaming/response/content_part
8. OpenAI — Findings from a pilot Anthropic–OpenAI alignment evaluation exercise (hallucination evaluation)  
   https://openai.com/index/openai-anthropic-safety-evaluation/

### Independent mature-agent systems

9. Anthropic — Reduce hallucinations  
   https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
10. Anthropic — Citations  
    https://platform.claude.com/docs/en/build-with-claude/citations
11. Anthropic — Search results / cited RAG sources  
    https://platform.claude.com/docs/en/build-with-claude/search-results
12. Google AI for Developers — Grounding with Google Search  
    https://ai.google.dev/gemini-api/docs/google-search
13. Google AI for Developers — URL context / citations  
    https://ai.google.dev/gemini-api/docs/url-context
14. GitHub — Responsible use of Copilot inline suggestions / generated content  
    https://docs.github.com/en/copilot/responsible-use/inline-suggestions
15. GitHub — Responsible use of Copilot Chat  
    https://docs.github.com/copilot/responsible-use/chat-in-github

### External discipline / standard

16. NIST — Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (AI 600-1; updated 2026)  
    https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
17. NIST AI Resource Center — AI RMF Core (knowledge limits, uncertainty, validation/generalizability)  
    https://airc.nist.gov/airmf-resources/airmf/5-sec-core/

## 12. Evidence confidence and open uncertainty

- **High confidence:** current AI guidance strongly supports explicit uncertainty instead of forced guessing.
- **High confidence:** citations/references should support the actual associated claim rather than merely be topically relevant.
- **High confidence:** model confidence and fluent prose are not evidence.
- **High confidence:** A08 should not duplicate A13/C02 by making every material claim trigger a generic research workflow.
- **High confidence:** no universal evidence Skill is justified at this stage.
- **Moderate-high confidence:** `claim-evidence-traceability` is the clearest compact principle label for the selected behavior even though individual vendors expose it through different product mechanics (citation spans, grounding metadata, tests/logs, etc.).
- **Primary evaluation uncertainty:** whether always including `source-authority,provenance,freshness,uncertainty-calibration` in the principle attribute materially improves behavior beyond the sentence itself, or merely consumes context. Final prompt eval should test a shorter attribute set.
- **Secondary evaluation uncertainty:** A08 and A13 may overlap enough that final synthesis can merge them. Keep separate until A13 is researched under the same AI-native-first standard.

## 13. Final recommendation

Keep A08 as a **small universal epistemic-integrity rule**, not a research procedure.

Its unique value is:

```text
claim strength must not exceed evidence strength
```

and the agent should preserve the distinction among **source, observation, inference, assumption, conflict, and unknown** whenever that distinction materially affects the answer or decision.
