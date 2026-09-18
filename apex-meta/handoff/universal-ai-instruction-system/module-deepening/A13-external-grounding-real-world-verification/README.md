---
type: ModuleDeepeningResult
title: A13 External Grounding & Real-World Verification
description: Corrected AI-native-first deepening result for the universal <grounding> module. External grounding is the default for non-creative factual work whose correctness depends on information outside supplied/local context; model reasoning synthesizes grounded evidence rather than substituting for it.
status: DONE_CORRECTED
updated: 2026-09-18
supersedes_commit: 1fee4df44f4ac87acd2b2074d6b162b0ec430451
---

# A13 — External Grounding & Real-World Verification

## 1. Correction summary

The first A13 pass was **too restrictive**. It treated external grounding as an exception activated mainly by current/changeable/niche claims. That misses the operator's actual failure mode:

> The AI often invents a plausible reasoning path from latent knowledge when it should first ground itself in the specific external reality of the task, environment, version, setting, phrase, method, or named system.

The corrected design is therefore:

```text
EXTERNAL GROUNDING = DEFAULT
for non-creative factual work whose correctness depends on information
outside the supplied/local context.

MODEL REASONING = SYNTHESIS OVER GROUNDED EVIDENCE
not a substitute for finding the evidence.

DEPTH = ADAPTIVE
one bounded authoritative lookup by default;
direct environment observation when the environment is load-bearing;
multi-source/deep research only when the question actually requires it.
```

This is stronger than the prior A13 but deliberately avoids “deep research every time.”

## 2. Final root wording

### XML

```xml
<grounding principles="grounding-by-default,source-first-reasoning,real-world-verification">
  Ground non-creative factual work in external evidence by default whenever correctness depends on information outside the supplied or local context. Before relying on model reasoning for a concrete claim, method, recommendation, or implementation, check the most specific authoritative evidence available for the actual task, environment, version, setting, phrase, or named system; prefer established primary or battle-tested sources and direct observation when applicable. Use reasoning to interpret grounded evidence, not substitute for it; skip external grounding only when outside facts cannot materially affect correctness.
</grounding>
```

### Compact Markdown control

```markdown
**Grounding — grounding-by-default / source-first reasoning / real-world verification:** Ground non-creative factual work externally by default when correctness depends on information outside supplied/local context. Check the most specific authoritative evidence for the actual task/environment/version/setting before relying on model reasoning; prefer established primary or battle-tested sources and direct observation where applicable. Reason from grounded evidence; do not replace it with plausible internal reasoning.
```

## 3. What changed from the rejected first pass

| Dimension | First A13 pass | Corrected A13 |
|---|---|---|
| Default posture | model reasoning first; ground when trigger fires | **ground first when outside facts matter** |
| Trigger | current/changeable/niche/material | **non-creative factual work dependent on external reality** |
| Stable technical/domain fact | often no retrieval | **bounded authoritative grounding by default** |
| Environment-specific fact | test when triggered | **environment evidence is first-class whenever load-bearing** |
| Model reasoning | allowed until grounding threshold crossed | **used after evidence retrieval to interpret/synthesize** |
| Search depth | conditional | **grounding default; depth adaptive** |
| Deep research | sometimes coupled to grounding | **only escalation path through C02** |
| Source selection | authoritative | **most specific authoritative / established / battle-tested source for the actual setting** |

## 4. Current OpenAI evidence

Research date: **2026-09-18**.

### 4.1 OpenAI's own research-agent example is explicitly grounding-by-default

Current OpenAI model guidance provides an example web-research prompt whose factuality rule says to browse for **all non-creative queries** unless the user explicitly says not to or the request is purely creative. It also says that if there is doubt whether browsing would help, browse.

The same guidance separately says:

> Prefer web research over assumptions whenever facts may be uncertain or incomplete.

This directly contradicts the weaker design that waits for a special “current/niche” trigger.

Portable lesson:

```text
non-creative factual task
    ↓
external grounding by default
    ↓
reason/synthesize
```

Primary source:
https://developers.openai.com/api/docs/guides/latest-model?model=gpt-5.2

### 4.2 Current OpenAI retrieval-budget guidance supports a CHEAP default, not a research project every time

Current GPT-5.5 guidance gives a bounded retrieval pattern for ordinary Q&A:

```text
start with one broad search
if enough citable support exists -> answer
search again only if an important fact/source is missing
or an important factual claim would otherwise be unsupported
```

This is the strongest evidence for the corrected architecture:

> **Default grounding + retrieval stopping rule** is preferable to both “reason first” and “deep research every time.”

Primary source:
https://developers.openai.com/api/docs/guides/latest-model?model=gpt-5.5

### 4.3 OpenAI's 2026 evaluation guidance says the environment/setup changes what is actually true about agent capability

OpenAI's May 2026 evaluation playbook says modern agent performance depends on the model **and** the environment/harness/tool setup. It warns that claims are only as strong as the conditions and evidence under which they were tested.

That maps directly onto the operator's requirement:

```text
generic product/model knowledge
!=
truth about THIS environment / THIS setup / THIS tool surface
```

Primary source:
https://openai.com/index/trustworthy-third-party-evaluations-foundations/

## 5. Independent mature-system convergence

### Google Gemini

Google's current prompt guidance says Grounding with Google Search should be enabled whenever the model may need **obscure or recent facts**. Its grounding docs say grounding increases factual accuracy and reduces hallucinations by basing responses on real-world information.

This is narrower than OpenAI's research-agent default, but it independently supports the principle that internal model reasoning is not the correct source for externally checkable facts.

Sources:
https://ai.google.dev/gemini-api/docs/prompting-strategies
https://ai.google.dev/gemini-api/docs/google-search

### GitHub Copilot

GitHub documents two relevant production controls:

1. web search for recent/new/highly specific topics;
2. generated code should be reviewed/tested against the actual repository, architecture, dependencies, and environment.

GitHub's AI-code review guidance specifically tells users to use README/docs/recent PRs as context, tell the AI which sources to trust, verify suggested packages, and watch for hallucinated APIs.

Sources:
https://docs.github.com/copilot/responsible-use/chat-in-github
https://docs.github.com/en/enterprise-cloud@latest/copilot/tutorials/review-ai-generated-code

Portable lesson:

> factual grounding is not only “web search”; it includes the most authoritative task-local evidence: repository state, exact docs, actual dependencies, runtime/tool surface, and executed tests.

## 6. Empirical efficacy evidence

### 6.1 Retrieval measurably improves factuality

Muhlgay et al. (EACL 2024) built FACTOR benchmarks for factuality and report that benchmark scores **improve when the language model is augmented with retrieval**.

Source:
https://aclanthology.org/2024.eacl-long.4/

### 6.2 Retrieval is not sufficient by itself

RAGTruth (ACL 2024) analyzes nearly 18,000 RAG responses and shows that retrieval-augmented systems can still produce unsupported or contradictory claims.

Source:
https://aclanthology.org/2024.acl-long.585/

A 2025 EMNLP industry benchmark likewise emphasizes that RAG aims to reduce hallucination but modern models still introduce unsupported information even when relevant context is supplied.

Source:
https://aclanthology.org/2025.emnlp-industry.54/

Therefore:

```text
retrieval ON
does not imply
answer GROUNDED
```

The useful control is source-first reasoning plus evidence checking, not merely tool activation.

### 6.3 Stronger factuality systems use retrieved evidence explicitly

LongFact/SAFE (2024) evaluates individual factual claims by generating search queries and checking whether search evidence supports each claim. The work shows that search-grounded evaluation can scale factuality checking across thousands of claims.

Source:
https://arxiv.org/abs/2403.18802

### 6.4 Production validation must match the actual setting

NIST's Generative AI Profile says:

- do not extrapolate capabilities from narrow/anecdotal assessment;
- review/verify sources and citations;
- verify that retrieval-augmented data is grounded;
- document limits of generalization beyond tested conditions.

Source:
https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf

This directly supports task/environment-specific grounding instead of generic model reasoning.

## 7. Candidate policy comparison

### Scoring convention

These are **comparative design scores, not measured probabilities**.

- **Impact (1–100):** expected reduction in wrong/unverified reasoning and improvement in task correctness. Higher = better.
- **Evidence (1–100):** strength/convergence of current official guidance + empirical support. Higher = stronger.
- **Risk (1–100):** risk of over-triggering, latency/cost, context pollution, bad retrieval, or operational harm. Higher = worse.

| Option | Policy | Impact | Evidence | Risk | Assessment |
|---|---|---:|---:|---:|---|
| **A** | **Exception grounding** — reason first; browse only for explicit/latest/current/niche triggers | **52** | **62** | **72** | **Reject.** This is close to the first A13 and misses the operator's core failure: plausible but ungrounded reasoning. |
| **B** | **Browse every non-creative query, full stop** | **88** | **92** | **58** | Strong OpenAI support, but too blunt for local/self-contained work and may add irrelevant retrieval. |
| **C** | **One bounded grounding lookup by default** when outside facts can affect correctness; stop once core claims are citable | **94** | **96** | **31** | Strong. Directly matches current OpenAI retrieval-budget guidance. |
| **D** | **Adaptive source-first grounding**: C + exact task/environment source priority + direct observation when environment-specific + triangulation only when needed | **98** | **96** | **24** | **SELECTED.** Best fit to the operator's failure mode and strongest balance of correctness vs overhead. |
| **E** | **Multi-source triangulation for every factual task** | **95** | **90** | **62** | High correctness potential but too much latency/context and source-conflict noise for ordinary tasks. |
| **F** | **Direct runtime test first for every technical claim** | **91** | **89** | **69** | Excellent for “works here?” claims, poor as universal rule; tests can be costly/destructive and do not establish general maturity/support. |
| **G** | **Deep research for every non-creative task** | **94** | **85** | **86** | Over-engineered. Good research quality, poor operating efficiency; defeats the compact universal-contract goal. |

### Selected policy: D

```text
DEFAULT
  Ground externally before factual reasoning.

DEPTH 1 — bounded source lookup
  Find the most specific authoritative source for this exact question.

DEPTH 2 — local/environment evidence
  If the claim is about THIS runtime/repo/configuration/version:
  inspect or test that environment.

DEPTH 3 — triangulate
  If sources conflict, maturity/reliability is claimed, or stakes are high:
  use multiple independent authoritative/production sources.

DEPTH 4 — C02 deep research
  Only for broad/contested/comparative questions.

EXEMPT
  Pure transformation/creative work,
  arithmetic/formal derivation,
  or tasks fully determined by supplied/local evidence
  where outside facts cannot alter correctness.
```

## 8. “Battle-tested source” hierarchy

A13 should prefer evidence in this order, while leaving detailed authority/conflict semantics to A08/A11/source governance:

1. **Actual governing/project-local state** when the claim is about the current project or environment.
2. **Direct observation/test** when the claim is “works/exists here.”
3. **Official primary/version-specific source** for product/API/standard/law/capability.
4. **Mature reference implementation / official repository / maintained specification.**
5. **Independent production evidence** for maturity/reliability/battle-tested claims.
6. **High-quality secondary analysis** only when primary/production evidence is insufficient.
7. **Community discussion/search snippets** as discovery leads, not load-bearing proof.
8. **Model memory/internal reasoning** as hypothesis generation only when the fact is externally verifiable.

This is not a rigid universal source-ranking schema; the fuller P0-P3 source-governance contract remains a later synthesis item.

## 9. Direct observation rule

The first A13 pass framed direct tests as an optional add-on after external docs.

Corrected rule:

> If the question is about the active environment, observed environment state is itself part of the grounding basis.

Examples:

| Claim | Grounding basis |
|---|---|
| “Does GitHub support feature X?” | current GitHub docs |
| “Can this connected GitHub tool perform X?” | inspect the actual tool surface |
| “Does this repo build with dependency Y?” | current repo + dependency metadata + run/build/test |
| “Is library Y battle-tested?” | official project state + release/maintenance history + independent production evidence |
| “Is this sentence/phrase used by standard Z?” | exact current standard/source text |
| “Will this implementation work here?” | actual environment/config + execution/test where safe |

A generic web source cannot substitute for evidence about a specific active environment.

## 10. A13 vs neighboring modules

### A08 `<evidence>`

- A13 gets the agent out of its own head and into external/task-specific evidence.
- A08 decides what the obtained evidence actually supports and how uncertainty is represented.

### A11 `<current_truth>`

- A11 determines which current project/instruction state governs.
- A13 says external/task-specific facts should be grounded rather than invented.

### A03 `<reuse>`

- A03 says prefer battle-proven reuse.
- A13 makes “battle-proven,” “supported,” “maintained,” and “works here” evidence-backed rather than model intuition.

### C02 `<research>`

- A13 is the **default epistemic posture**.
- C02 is the **deeper research workflow** when one lookup/test is not enough.

### Source-Governed Execution Contract

Candidate 14 remains separate. It should later specify which provided sources are governing, verification-only, discovery-only, etc.

A13 must obey that contract rather than using “external grounding” as permission to replace operator-designated sources.

## 11. Failure modes prevented

1. **Plausible-reasoning substitution** — the model reasons from memory instead of checking the real source.
2. **Environment abstraction error** — generic docs are mistaken for evidence about the actual runtime/configuration.
3. **Familiarity-as-proof** — a famous tool/library is labeled “battle-tested” without maturity evidence.
4. **Outdated-method assumption** — the model recommends a method based on stale training-time norms.
5. **Invented phrase/standard semantics** — the model paraphrases a named standard instead of reading it.
6. **Search-without-grounding** — search is performed but retrieved evidence does not actually govern the answer.
7. **RAG complacency** — retrieved context exists, therefore the model assumes the answer is faithful.
8. **Deep-research inflation** — every simple question becomes a multi-source research project.

## 12. Bounded scenario evaluation

### Scenario A — stable conceptual explanation

User: “Explain verification vs validation.”

**Corrected A13:** one lightweight authoritative grounding source is appropriate by default if the explanation is being presented as factual/domain guidance. Do not launch deep research.

**Why:** this differs from the rejected first pass. Stable does not mean model memory should automatically become the source.

### Scenario B — rewrite supplied paragraph

User: “Rewrite this paragraph more clearly.”

**Corrected A13:** no external grounding unless the rewrite introduces/changes factual claims.

### Scenario C — software architecture choice

User: “Use battle-tested tooling, not custom infrastructure.”

**Corrected A13:** research actual mature implementations before proposing architecture. Model reasoning alone cannot establish maturity/capability.

### Scenario D — current repository/tool environment

User: “Can this GitHub connector make a localized patch?”

**Corrected A13:** inspect the actual connected tool surface; do not infer from GitHub API/CLI capabilities.

### Scenario E — known method/standard

User: “Use the official method for X.”

**Corrected A13:** read the current authoritative method/standard before designing the procedure.

### Scenario F — arithmetic

User: “Calculate 17% of 240.”

**Corrected A13:** no web; deterministic calculation is sufficient.

### Scenario G — source conflict

Official docs say a feature exists; active environment does not expose it.

**Corrected A13:** preserve both:
- generally documented support;
- unavailable/unverified in current environment.

Use the latter for the immediate implementation decision.

### Scenario H — RAG/search result present

A retrieval system returns a plausible source.

**Corrected A13:** do not stop at retrieval. A08 still requires the actual claim to be supported by the source.

## 13. Context-budget defense

The stronger wording is longer than the first A13, but it addresses a root failure that affects research, architecture, implementation, recommendations, standards, and tool use.

Its token cost can later be compressed if controlled evals show a shorter sentence preserves:

- grounding default;
- task/environment specificity;
- source-first reasoning;
- narrow exemptions;
- adaptive retrieval depth.

A possible compressed candidate for final synthesis is:

```xml
<grounding principles="grounding-by-default,source-first-reasoning">
  For factual work, ground externally by default before relying on model reasoning. Use the most specific authoritative evidence for the actual task and environment, escalating from a bounded lookup to direct testing or broader research only as needed; skip grounding only when outside facts cannot affect correctness.
</grounding>
```

Do **not** replace the selected pilot wording with this shorter version until cross-agent evaluation shows no loss.

## 14. Final decision

**Selected architecture: D — adaptive source-first grounding.**

Core invariant:

```text
DO NOT:
model reasoning -> plausible conclusion -> optional verification

DO:
specific task/environment
    ↓
most authoritative available external/local evidence
    ↓
direct observation/test when the environment itself matters
    ↓
model reasoning / synthesis
    ↓
A08 claim-evidence validation
```

The external evidence step is **default**, not something the user must request repeatedly.

The remaining optimization problem is **how much grounding**, not **whether grounding should happen at all**.
