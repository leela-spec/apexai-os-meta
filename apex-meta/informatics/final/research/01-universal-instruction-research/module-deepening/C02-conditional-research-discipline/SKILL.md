---
name: deep-evidence-research
description: Conduct multi-step evidence research when ordinary grounding is insufficient because the task requires synthesis across multiple evidence threads, broad or representative coverage, due diligence, a literature or technology landscape, or resolution of material disagreement. Do not use for routine current facts, simple comparisons, or ordinary three-source web grounding.
---

# Deep Evidence Research

## Objective

Produce a decision-relevant, source-grounded synthesis without one-shot searching, convenience-source bias, false consensus, or unbounded research.

## Procedure

### 1. Frame the research target

Establish:

- the exact question or decision the research must support;
- scope and non-goals;
- active environment, version, platform, geography, or time window;
- governing constraints and must-use/operator-prioritized sources;
- required freshness;
- what would materially change the answer.

If a material ambiguity prevents a meaningful research frame, resolve that ambiguity before searching deeply.

### 2. Map the evidence needed

List the few evidence threads or source classes that could materially affect the conclusion.

Examples:

- official capability/current policy;
- independent production or implementation evidence;
- standards or established methodology;
- competing solutions/approaches;
- maintenance/support/security signals;
- direct local observation or repository constraints.

Do not create a generic evidence matrix when a short source map is enough.

### 3. Run an orientation scan

Search broadly enough to learn:

- established vocabulary;
- major candidate approaches;
- likely primary/authoritative sources;
- obvious disagreement;
- missing evidence classes.

Treat orientation sources as leads, not automatically as final evidence.

### 4. Verify load-bearing evidence

For each material conclusion:

- prefer current primary/authoritative evidence for capabilities, policies, versions, and standards;
- add independent/production evidence for maturity, reliability, adoption, or battle-tested claims;
- trace derivative claims back to their origin when feasible;
- distinguish direct observation from documentation and from inference.

Use A08-style claim discipline: a source may be relevant without supporting the claim actually being made.

### 5. Iterate from what the evidence reveals

Refine queries and follow important leads.

Specifically investigate:

- credible contradictions;
- missing source classes;
- version/scope mismatches;
- claims that would reverse the recommendation if false;
- serious alternatives not yet represented.

Do not repeat unchanged searches merely to increase source count.

### 6. Track gaps and conflicts

Maintain a concise working record of:

- material fact/claim;
- strongest supporting evidence;
- contradictory evidence;
- unresolved gap;
- practical consequence if unresolved.

Do not force consensus. If disagreement remains genuine, carry it into the synthesis.

### 7. Apply the stopping rule

Stop when all are true:

1. the important evidence threads are represented;
2. major credible contradictions have been resolved or explicitly preserved;
3. additional credible searches are returning mainly duplicate/non-decision-changing information;
4. new evidence is unlikely to materially change the conclusion, recommendation, or uncertainty.

Continue when a missing source class, unresolved contradiction, or fragile assumption could still change the outcome.

Do not use a fixed query count, source count, or iteration count as a substitute for this judgment.

### 8. Synthesize for the actual decision

Return the form the task needs, not a research diary.

Normally include:

- concise answer/current best-supported conclusion;
- decisive evidence and sources;
- viable alternatives or competing explanations when material;
- unresolved gaps/disagreement;
- practical consequence for the requested decision;
- what evidence would most likely change the conclusion, if any.

Cite or link sources so the result can be checked.

## Escalation patterns

Use heavier formal methods only when the task warrants them.

Examples:

- **formal literature/systematic review:** explicit protocol, eligibility criteria, comprehensive database strategy, screening, bias assessment, PRISMA-style reporting;
- **due diligence:** separate capability, operating evidence, maintenance/support, security/risk, adoption/maturity, and environment-fit evidence;
- **technology landscape:** map approach classes before comparing named products;
- **contested evidence:** characterize why sources differ before attempting synthesis.

Do not impose these patterns on ordinary product questions or small implementation comparisons.

## Boundary checks

- **Normal external/current fact:** use ordinary grounding, not this Skill.
- **Three strong sources materially agree and answer the question:** stop; do not deepen for ceremony.
- **Operator supplied source priorities:** obey them; do not let generic web prominence displace them.
- **Repository current truth conflicts with external best practice:** preserve repository authority unless the task is explicitly to challenge/change it.
- **Research ends in a material operator-owned choice:** hand the evidence/trade-off to the decision discipline; do not decide the preference inside research.
- **Evidence is insufficient:** say what remains unresolved rather than manufacturing certainty.
