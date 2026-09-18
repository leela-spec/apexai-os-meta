---
type: ModuleDeepeningResult
title: A13 External Grounding & Real-World Verification
description: AI-native-first deepening result for the universal <grounding> module, defining when latent model knowledge is insufficient and external reality must be consulted without turning ordinary tasks into mandatory research.
status: DONE
updated: 2026-09-18
---

# A13 — External Grounding & Real-World Verification

## 1. Final decision

- **Module:** A13
- **XML tag:** `<grounding>`
- **Semantic purpose:** Decide **when model knowledge/reasoning is not enough** and the agent must consult external reality before making a material claim or decision.
- **Selected deeper owner:** **C02 `<research>` when a deeper research process is actually triggered; no A13-specific Skill or reference.**
- **Selected root principles:** external grounding; real-world verification.
- **Key wording changes:**
  1. expand the trigger from **material decision** to **material claim or decision**;
  2. make the activation threshold explicit: current/changeable, niche, named-system, environment-specific, capability/support, maturity/reliability facts, plus explicit research/verification requests;
  3. make direct observation/testing conditional on being both **load-bearing** and **feasible**;
  4. remove `source-authority` from A13's principle list because A08/A11 already own evidence authority, freshness, provenance, and local governing precedence;
  5. do not repeat A08's uncertainty-calibration rule in A13.
- **A08 merge decision:** keep A08 and A13 separate for the pilot. A08 controls what evidence justifies saying; A13 controls whether external evidence must be acquired at all. Re-test merge/delete during final synthesis.
- **Source-Governed Execution Contract:** preserve `14-SOURCE-GOVERNED-EXECUTION-CONTRACT-CANDIDATE.md` as a later synthesis / operational-integration item. A13 records the interaction but does **not** absorb its P0-P3 source-governance schema.

### Final root XML

```xml
<grounding principles="external-grounding,real-world-verification">
  Use external grounding when explicitly requested or when a material claim or decision depends on real-world facts that are current, changeable, niche, environment-specific, or about a named system's capability, support, maturity, or reliability. Do not rely on model knowledge alone: consult authoritative external evidence and, when actual behavior is load-bearing and feasible to observe or test, verify it directly.
</grounding>
```

### Equivalent compact Markdown control

```markdown
**Grounding — external grounding / real-world verification:** Use external grounding when explicitly requested or when a material claim or decision depends on real-world facts that are current, changeable, niche, environment-specific, or about a named system's capability, support, maturity, or reliability. Do not rely on model knowledge alone: consult authoritative external evidence and, when actual behavior is load-bearing and feasible to observe or test, verify it directly.
```

## 2. Why the current pilot needed correction

The previous pilot said:

```text
When a material decision depends on real-world facts ... verify externally.
```

That was directionally right but too narrow in one place and too duplicated in another.

### 2.1 Too narrow: claims can fail before a decision exists

A user may ask:

- “Does product X currently support Y?”
- “Is this library maintained?”
- “Is this API available in the current version?”
- “Is this tool battle-proven?”
- “Does the connected runtime actually expose this capability?”

Those are material factual claims even when no explicit decision is requested. If A13 only triggers on a “decision,” the agent can still canonize stale or invented capability claims and later decisions inherit the error.

### 2.2 Too duplicated: source authority is already owned elsewhere

A13 should not become a second evidence-governance module.

- **A08 `<evidence>`:** authority, provenance, freshness, claim/evidence fit, uncertainty.
- **A11 `<current_truth>`:** which active project/repository/instruction source governs.
- **A13 `<grounding>`:** whether external reality must be consulted at all.
- **C02 `<research>`:** how deeper research is performed once triggered.

Removing `source-authority` from A13's principle list makes the architecture more orthogonal and saves always-loaded context.

## 3. Current OpenAI / ChatGPT / Codex evidence

Research date: **2026-09-18**. Current product behavior is time-sensitive; these findings should be rechecked before future propagation.

### 3.1 ChatGPT Search: web access is a distinct capability used when web information helps

OpenAI's current ChatGPT Search documentation says ChatGPT can automatically search when a question may benefit from web information and returns links/citations to sources. This directly supports a **conditional grounding trigger**, not universal mandatory browsing.

Portable lesson:

```text
latent model knowledge
  -> sufficient for some tasks
  -> external search when current/web information materially improves correctness
```

Source:
https://help.openai.com/en/articles/9237897-chatgpt-search

### 3.2 OpenAI truthfulness guidance: training knowledge is bounded; confidence is not reliability

OpenAI's current truthfulness guidance states that model knowledge is bounded by a cutoff unless tools are used and warns that confidence is not reliability. It recommends checking important external information and using Search or Deep Research when accuracy depends on it.

This is the core reason A13 exists: a fluent answer about a current real-world system is not self-validating.

Source:
https://help.openai.com/en/articles/8313428-does-chatgpt-tell-the-truth

### 3.3 Deep Research: complex external questions justify a deeper, source-controlled workflow

Current Deep Research guidance distinguishes multi-step research from ordinary search. Users can provide files, restrict or prioritize websites, specify sources to include/exclude, review a proposed research plan, and receive citations/source links.

That supports a clean A13/C02 boundary:

- **A13:** trigger external grounding.
- **C02:** own the deeper research method when the question is comparative, contested, broad, or requires triangulation.

It also supports preserving the Source-Governed Execution Contract as a separate later integration candidate: OpenAI explicitly allows source restriction and source steering, but that does not mean every grounding event needs a P0-P3 contract.

Sources:
https://help.openai.com/en/articles/10500283-deep-research-faq
https://openai.com/index/introducing-deep-research/

### 3.4 OpenAI web-search tooling: current information is obtained through an explicit tool surface

OpenAI's current web-search documentation describes web search as the mechanism for accessing up-to-date internet information and returning cited sources. Current agent/web-search surfaces distinguish live, cached/indexed, and disabled modes and can constrain allowed domains.

Important implication:

> “The task requires grounding” does not prove that the current runtime actually has live search.

A13 defines the behavioral requirement. The executor still has to verify its actual tool surface. If the required grounding tool is unavailable, the correct result is “not externally verified in this environment,” not an invented verification claim.

Sources:
https://developers.openai.com/api/docs/guides/tools-web-search
https://developers.openai.com/docs/agent-approvals-security

### 3.5 Current model guidance: use hosted tools when they fit, but evaluate behavior empirically

OpenAI's current model guidance recommends hosted tools such as web search when they fit the workflow and emphasizes model-specific evaluation rather than preserving old prompt scaffolding by habit. Older/current family guidance also explicitly recommends web research over assumptions when facts are uncertain or incomplete.

Portable A13 lesson:

- do not encode obsolete “always browse” or “never browse” folklore;
- encode the semantic trigger;
- let the actual runtime/tool surface implement it;
- validate the compact rule through representative scenarios.

Source:
https://developers.openai.com/api/docs/guides/latest-model

## 4. Independent mature-agent convergence

### 4.1 Anthropic Claude: web search exists specifically to go beyond the knowledge cutoff

Anthropic's current web-search tool gives Claude current web content with citations and supports allowed/blocked domains and bounded search-use counts. Newer variants can filter search results before filling context.

Portable convergence:

1. external search is a distinct tool, not an implicit property of model reasoning;
2. current information beyond training knowledge is a primary trigger;
3. source scope and search budget can be bounded;
4. grounding should not require flooding context with every result.

Source:
https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool

### 4.2 GitHub Copilot: recent/new/highly specific topics are explicit search triggers

GitHub's responsible-use documentation says Copilot may use Bing for questions involving recent events, new trends or technologies, highly specific subjects, or when the user explicitly asks for web search.

This is unusually close to the selected A13 trigger:

```text
explicit request
OR current/new
OR highly specific
-> external search becomes relevant
```

GitHub separately recommends reviewing and testing generated code, especially for critical/sensitive use, which supports direct observation when actual behavior matters.

Sources:
https://docs.github.com/en/copilot/responsible-use/chat
https://docs.github.com/en/copilot/how-tos/manage-your-account/manage-policies

### 4.3 Gemini: grounding connects the model to real-time information and citations

Google's current Gemini grounding documentation explicitly positions Google Search grounding as a way to:

- access real-time information;
- improve factual accuracy;
- reduce hallucination risk;
- return verifiable citations.

The model can decide whether a search would improve the answer once the tool is enabled.

Portable convergence:

> current/external reality should be retrieved when it materially improves factual correctness, but the search mechanism itself can remain conditional.

Source:
https://ai.google.dev/gemini-api/docs/google-search

### 4.4 Cross-agent synthesis

Across OpenAI, Anthropic, GitHub, and Google, the convergence is stronger than any vendor-specific implementation detail:

```text
stable/local/supplied transformation
-> do not force web research

current/changeable/niche/named-system fact
-> external retrieval becomes appropriate

environment-specific operational claim
-> observed/tested behavior may be required

complex comparative/contested question
-> deeper research workflow

search result obtained
-> separate evidence-quality rules still apply
```

This supports keeping A13 small and semantic.

## 5. Established external grounding

The AI-native evidence already determines the module. External disciplines add durable validation concepts.

### 5.1 NIST GenAI Profile: confabulation is a real-world risk, especially for consequential decisions

NIST AI 600-1 defines confabulation as confidently generated erroneous/false content and notes that risks increase when people act on false outputs, particularly in consequential real-world applications.

A13 does not need NIST terminology in the root prompt. The durable lesson is simply:

> consequential real-world facts should not be accepted merely because a generative model states them fluently.

Source:
https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf

### 5.2 NIST AI RMF TEVV: validate in conditions similar to deployment

NIST's AI RMF Measure function calls for testing, evaluation, verification, and validation, including demonstrating system behavior in conditions similar to deployment and monitoring actual behavior in operation.

This supports A13's direct-observation clause, but only with correct scope:

- documentation answers what a product claims/supports generally;
- a direct test answers what happened in the tested environment;
- neither automatically replaces the other;
- when they conflict, record the conflict and reason about the specific claim.

Source:
https://airc.nist.gov/airmf-resources/airmf/5-sec-core/

## 6. Semantic contract

### MUST

A13 MUST trigger external grounding when:

- the user explicitly asks to **research, search, look up, verify, check current status, or confirm against external sources**;
- a material claim/decision depends on a **current or changeable** real-world fact;
- the claim concerns a **named product, service, API, library, integration, standard, law/regulation, market offering, or other externally maintained system** whose state may have changed;
- the task depends on whether a capability is **actually supported, available, maintained, mature, reliable, or battle-proven**;
- the answer depends on **environment-specific behavior** that model training data cannot establish;
- the topic is sufficiently **niche/specific** that relying on latent familiarity would create a material risk of invention;
- a high-consequence decision depends on an external factual premise that can reasonably be checked.

When A13 triggers:

1. consult authoritative external evidence;
2. if the actual local/runtime behavior is itself load-bearing and feasible to observe/test, inspect or test it;
3. pass resulting claims/evidence to A08 for authority/freshness/support/uncertainty handling;
4. use C02 only when the grounding question requires a deeper research process rather than a bounded lookup/verification.

### MUST NOT

A13 MUST NOT:

- force web search for rewriting, summarization, translation, formatting, creative writing, simple arithmetic, or other tasks whose answer is fully determined by supplied material;
- force browsing for a stable conceptual explanation merely because external sources exist;
- replace current repository/project authority with web material; A11 owns current local truth;
- silently override operator-designated source roles; the Source-Governed Execution Contract remains a separate candidate owner for that problem;
- duplicate A08 by prescribing claim confidence, citation density, source freshness, or provenance mechanics;
- duplicate C02 by requiring landscape scans, multi-source triangulation, candidate matrices, or exhaustive research every time grounding triggers;
- assume a tool/API/CLI capability exists because another runtime documents it;
- treat vendor documentation as proof that the active local environment is configured correctly;
- treat one successful local test as proof of general support, maturity, or reliability;
- make direct runtime testing mandatory when it is impossible, disproportionate, unsafe, or irrelevant to the claim;
- hide lack of verification by falling back to plausible model knowledge.

### Activation threshold

A13 is **always available as a root invariant but should often have zero visible effect**.

Use this test:

```text
Would an error in an external real-world fact materially change the claim,
recommendation, architecture, action, or user's understanding?

AND

Is that fact current/changeable, niche, named-system-specific,
environment-specific, or about support/maturity/reliability?

YES -> ground externally
NO  -> do not add research ceremony
```

Explicit user requests for research/verification activate A13 regardless of the first test.

## 7. Documentation vs direct observation

A13 should not encode a universal “tests always outrank docs” rule.

Use claim-specific authority:

| Claim | Strongest direct evidence |
|---|---|
| “Vendor officially supports feature Y” | current official vendor documentation / release information |
| “Feature Y is exposed in this connected runtime” | direct inspection of the active tool/runtime surface |
| “Feature Y works in this exact environment/configuration” | direct execution/test plus relevant environment details |
| “Feature Y is mature/battle-proven” | broader maintenance/adoption/production evidence, not one local test |
| “This API existed in version N” | versioned official docs/changelog |
| “This workflow currently succeeds here” | observed run/test |

If official documentation says an integration exists but the active environment lacks it, the correct conclusion is not “docs are wrong” or “runtime is wrong” by default. Record:

```text
official/general support: documented
active environment availability: not observed / absent
integration decision: cannot assume available here
```

That is the exact failure mode A13 should prevent.

## 8. Module boundaries

### A13 vs A08 `<evidence>`

- **A13:** must we consult external reality?
- **A08:** what does the resulting evidence justify saying?

A08 can correctly say “uncertain” without initiating retrieval. A13 supplies the missing retrieval obligation when external reality is load-bearing.

### A13 vs A11 `<current_truth>`

- **A11:** which active project/repository/instruction source governs?
- **A13:** when external real-world state must be checked?

Web research cannot silently supersede a P0/current project instruction.

### A13 vs A03 `<reuse>`

- **A03:** prefer proven reuse before invention.
- **A13:** establish whether the claimed existing capability/provenness is real.

“Battle-proven” is therefore a grounding-sensitive claim, not a model intuition.

### A13 vs A04 `<workflow>`

- **A04:** how much planning/process is proportionate?
- **A13:** whether external reality must enter the evidence base.

A13 can trigger one quick lookup without requiring a research project.

### A13 vs C02 `<research>`

- **A13:** trigger.
- **C02:** deeper method.

This is the selected deepening boundary.

### A13 vs Source-Governed Execution Contract candidate

The candidate in `14-SOURCE-GOVERNED-EXECUTION-CONTRACT-CANDIDATE.md` governs how explicitly designated sources are ranked/used and audited.

A13 must not become permission to displace those sources. During later synthesis, integrate the two as:

```text
source contract decides WHAT external material may govern/supplement/verify
A13 decides WHETHER external reality must be consulted
C02 decides HOW deeper research is executed
A08 decides WHAT the resulting evidence supports
```

No part of the P0-P3 scheme is added to the A13 root block in this run.

## 9. Alternatives considered

| Candidate | Result | Reason |
|---|---|---|
| Keep current A13 unchanged | Reject | “material decision” misses load-bearing factual claims; `source-authority` duplicates A08/A11. |
| “Always browse for factual tasks” | Reject | Over-triggers rewrites/stable explanations/local work and creates cost/latency/context noise. |
| “Browse only for latest/current” | Reject | Misses niche capability, maturity, environment-specific, and battle-proven claims. |
| A08 only, delete A13 | Reject for pilot | A08 governs claim/evidence integrity but does not reliably create an obligation to retrieve missing external evidence. |
| Merge A08 + A13 now | Defer | Possible context saving, but scenario test shows separable trigger vs evidence-strength behavior. Test in final synthesis. |
| Dedicated A13 Skill | Reject | No stable reusable procedure beyond the trigger; deeper procedure belongs to C02. |
| Dedicated A13 reference | Reject | The root rule + this module result fully capture the semantic boundary; no runtime JIT reference is needed. |
| C02 as deeper owner | **Select** | Deeper research procedure should activate only when grounding needs more than a bounded lookup/test. |

## 10. Bounded scenario evaluation

### Scenario 1 — simple rewrite

**Input:** “Rewrite this paragraph for clarity.”

**Selected A13 behavior:** no web/search; supplied text is sufficient.

**Without A13:** usually same.

**Observable pass:** no external-research ceremony, no new factual claims.

**Deeper owner:** none.

### Scenario 2 — current product capability

**Input:** “Does product X currently support Y?”

**Selected A13 behavior:** ground in current official product documentation; if the question is “can our active runtime do Y?”, inspect/test that runtime when feasible.

**Failure prevented:** stale training knowledge becoming a current capability claim.

**Observable pass:** capability claim is externally checked; local availability is not inferred from generic product docs.

**Deeper owner:** normally none; C02 only if evidence is conflicting/complex.

### Scenario 3 — battle-proven architecture recommendation

**Input:** “Use only proven existing tools for this pipeline.”

**Selected A13 behavior:** externally verify existence, support, maintenance/maturity, and relevant capability before A03 selects reuse.

**Failure prevented:** name recognition/popularity being laundered into “battle-proven.”

**Observable pass:** load-bearing provenness/capability claims have external support.

**Deeper owner:** C02 likely activates because comparison/maturity research is nontrivial.

### Scenario 4 — user provides binding P0/P1 sources

**Input:** user gives three designated governing/primary sources and asks for synthesis.

**Selected A13 behavior:** do not automatically search outside them. External grounding is used only if the task/source contract permits verification, contradiction detection, gap filling, or discovery.

**Failure prevented:** “ground externally” becoming permission to replace the user's selected basis.

**Observable pass:** must-use sources remain governing; any external conflict is separated and labeled.

**Deeper owner:** Source-Governed Execution Contract candidate in later synthesis; C02 only if external research is authorized/needed.

### Scenario 5 — docs vs observed behavior conflict

**Input:** official docs say an integration exists; connected tool surface does not expose it.

**Selected A13 behavior:** preserve both facts:
- documented general capability/support;
- active environment capability not observed/available.

Do not design the actual workflow as though the capability is available here.

**Failure prevented:** product-level documentation being mistaken for current environment capability.

**Observable pass:** architecture reflects the observed execution surface and records the discrepancy.

**Deeper owner:** none unless diagnosis becomes research.

### Scenario 6 — stale model knowledge

**Input:** task depends on current API behavior that may have changed since training.

**Selected A13 behavior:** verify current official docs/changelog; do not rely on remembered API semantics.

**Failure prevented:** stale interface/version assumptions.

**Observable pass:** current version/source identified or uncertainty remains explicit through A08.

**Deeper owner:** normally none.

### Scenario 7 — stable conceptual explanation

**Input:** “Explain the difference between verification and validation.”

**Selected A13 behavior:** no external research by default if the user only wants a general explanation and no current external decision depends on it.

**Failure prevented:** turning every educational answer into slow web research.

**Observable pass:** useful explanation without unnecessary browsing.

**Deeper owner:** none.

### Scenario 8 — unsupported real-world claim

**Input:** a material claim is externally checkable, but no reliable evidence can be found.

**Selected A13 behavior:** search/verify was attempted; do not backfill the gap from plausible model memory.

**A08 behavior:** narrow/qualify/mark unresolved.

**Observable pass:** “unverified” remains a valid outcome.

**Deeper owner:** C02 if broader research may materially resolve the gap.

### Scenario 9 — A08/A13 merge test

**Task:** current product support claim.

| Configuration | Expected failure/success |
|---|---|
| A08 only | Can correctly demand support/uncertainty but may stop at “not sure” or use available evidence without explicitly retrieving current external state. |
| A13 only | Triggers external lookup/test but does not fully govern evidence strength, freshness, conflict, or uncertainty. |
| A08 + A13 | External reality is retrieved when needed, then claim strength is calibrated to the evidence. |
| merged rule | Potentially shorter, but risks mixing trigger, research, evidence quality, and uncertainty into one oversized root sentence. |

**Decision:** retain separate through module deepening; final synthesis must benchmark merge/delete on token cost and behavior.

### Scenario 10 — XML vs compact Markdown

**Task:** apply the selected A13 control to scenarios 1, 2, 5, and 7.

**Expected:** XML and compact Markdown encode the same semantics.

**Observed design conclusion:** no evidence from this desk evaluation shows XML itself improves grounding behavior. XML remains the program's structural pilot, not a behavioral requirement.

**Final-synthesis requirement:** cross-agent eval must compare actual adherence/token cost; do not retain XML by preference alone.

## 11. Deeper-owner decision

### Dedicated A13 Skill — rejected

A grounding Skill would duplicate Search/Deep Research/C02 and would need a recognizable reusable workflow, not merely a semantic trigger.

### Dedicated A13 reference — rejected

The behavior is compact enough for the root contract. Detailed search, triangulation, source selection, contradiction handling, and stopping criteria belong to C02 or task-specific tooling.

### C02 `<research>` — selected conditional deeper owner

Routing:

```text
A13 triggered
   |
   +-- bounded current fact / official capability check
   |      -> direct search/look-up/test
   |
   +-- broad, contested, comparative, multi-source question
          -> deepen to C02 research method
```

This keeps A13 small while preventing shallow model-only answers.

## 12. Context-budget decision

A13 currently earns a pilot slot because it addresses a failure not fully covered by A08:

```text
A08: don't overclaim from weak/missing evidence
A13: don't stay inside model memory when external reality is load-bearing
```

Final synthesis must still test:

1. no A13;
2. A13 standalone;
3. A08 + A13;
4. merged A08/A13;
5. A13 as only a conditional trigger rather than universal root text.

Metrics:

- hallucinated/stale capability claims;
- missed searches on current/niche/environment-specific tasks;
- unnecessary searches on stable/local/transformation tasks;
- correct separation of official support vs observed local behavior;
- unresolved-uncertainty quality;
- token/context cost;
- cross-agent portability.

## 13. Source record

### Tier 1 — current OpenAI / ChatGPT / Codex

1. **OpenAI Help — ChatGPT Search**  
   https://help.openai.com/en/articles/9237897-chatgpt-search  
   Load-bearing findings: ChatGPT can automatically search when a question may benefit from web information; search returns links/citations; search is a distinct tool-mediated behavior.

2. **OpenAI Help — Does ChatGPT tell the truth?**  
   https://help.openai.com/en/articles/8313428-does-chatgpt-tell-the-truth  
   Load-bearing findings: model knowledge has a cutoff absent tools; confidence is not reliability; important external information should be checked.

3. **OpenAI Help — Deep Research in ChatGPT**  
   https://help.openai.com/en/articles/10500283-deep-research-faq  
   Load-bearing findings: deeper research is a separate multi-step workflow; users can supply/restrict/prioritize sources; outputs include citations/source links.

4. **OpenAI — Introducing deep research**  
   https://openai.com/index/introducing-deep-research/  
   Load-bearing finding: complex knowledge work may require active multi-source web research rather than latent model knowledge.

5. **OpenAI Developers — Web search**  
   https://developers.openai.com/api/docs/guides/tools-web-search  
   Load-bearing findings: web search provides current internet information/citations; live/cached behavior and domain controls are explicit tool mechanics.

6. **OpenAI Developers — Agent approvals and security / Codex network controls**  
   https://developers.openai.com/docs/agent-approvals-security  
   Load-bearing findings: network/search availability is runtime-controlled; web search can be cached/live/disabled; external content remains untrusted input.

7. **OpenAI Developers — Model guidance**  
   https://developers.openai.com/api/docs/guides/latest-model  
   Load-bearing findings: current models are tool-capable; hosted tools should be used where they fit; prompts and behavior should be validated empirically rather than inherited from old model generations.

### Tier 2 — independent mature-agent systems

8. **Anthropic — Web search tool**  
   https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool  
   Findings: web search supplies current content beyond cutoff with citations; allowed/blocked domains and bounded use keep grounding targeted.

9. **GitHub — Responsible use of Copilot Chat**  
   https://docs.github.com/en/copilot/responsible-use/chat  
   Findings: web search is relevant for recent events, new technologies, highly specific topics, or explicit search requests; generated output should be reviewed/tested.

10. **GitHub — Copilot web-search policy**  
    https://docs.github.com/en/copilot/how-tos/manage-your-account/manage-policies  
    Finding: Bing access is separately enabled/disabled, reinforcing that external grounding depends on actual tool availability.

11. **Google — Gemini Grounding with Google Search**  
    https://ai.google.dev/gemini-api/docs/google-search  
    Findings: grounding connects Gemini to real-time web information, improves factual accuracy, and provides citations; search remains a tool-enabled operation.

### Tier 3 — established external discipline

12. **NIST AI RMF 1.0 — Measure / TEVV**  
    https://airc.nist.gov/airmf-resources/airmf/5-sec-core/  
    Findings: test/evaluate systems under conditions similar to deployment, document limits, monitor actual behavior, and use repeatable TEVV where appropriate.

13. **NIST AI 600-1 — Generative AI Profile**  
    https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf  
    Findings: generative systems can confidently confabulate false information; consequences are particularly material when users act on those outputs.

## 14. Important uncertainties

- Search/tool behavior is product- and runtime-specific and will change. A13 must remain a semantic rule, not a hard-coded assumption that every agent can browse.
- “Authoritative external evidence” is deliberately not fully defined by A13; A08/C02/source-governance owners handle authority, freshness, triangulation, and conflicts.
- Direct observation is highly valuable for active-environment capability but may be impossible or unsafe. The rule therefore says **when load-bearing and feasible**, not always.
- One local test can falsify “works here right now” but cannot by itself establish broad maturity, official support, security, or production reliability.
- Explicit user source authority can constrain what external grounding is permitted to change. Candidate 14 must be resolved during final synthesis rather than silently imported now.
- The current wording intentionally names several trigger classes. Final cross-agent evaluation may show that a shorter formulation such as “externally checkable load-bearing facts not reliably established by model knowledge” performs equally well; if so, compress later.
- Stable conceptual knowledge is the main over-trigger risk. Scenario evaluation must include enough negative cases to ensure A13 does not become “always search.”

## 15. Final-synthesis implications

Carry forward these explicit tests:

1. **A08 vs A13 vs merged rule** on current capability, unsupported claim, and stable-concept scenarios.
2. **A13 token-budget defense:** measure missed grounding vs unnecessary grounding.
3. **Source-Governed Execution Contract integration:** preserve it as a separate operational mechanism and decide how P0-P3/source-use roles constrain A13/C02.
4. **C02 boundary:** ensure C02 does not duplicate A13's trigger and A13 does not grow into a research workflow.
5. **Actual-tool realism:** cross-agent evaluation must distinguish “agent should ground” from “this runtime has the tool to ground.”
6. **Official docs vs observed runtime:** include at least one deliberate mismatch scenario.
7. **XML vs Markdown:** evaluate actual adherence and token cost rather than aesthetic preference.

## 16. Decision summary

The selected invariant is:

```text
If a load-bearing real-world fact may be stale, specific, external,
environment-dependent, or otherwise unreliable from model memory,
check reality instead of guessing.

If the task is fully determined by supplied/local/stable information,
do not add research ceremony.
```

A13 therefore remains a **small universal trigger**, not a search methodology and not a source-governance system.

Its operational relationship is:

```text
A13 -> decide whether external reality must be consulted
A08 -> decide what the evidence supports
C02 -> perform deeper research when needed
A11 -> preserve current local/project authority
Candidate 14 -> later govern explicit source roles/coverage
```
