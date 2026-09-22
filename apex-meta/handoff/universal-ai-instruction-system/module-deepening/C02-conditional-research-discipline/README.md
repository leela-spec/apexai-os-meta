---
type: ModuleDeepeningResult
title: C02 Conditional Research Discipline
description: Evidence-backed deepening result for the conditional research module, separating ordinary A13 grounding from genuinely multi-step research that requires coverage, synthesis, contradiction handling, and an explicit stopping rule.
status: DONE
updated: 2026-09-22
---

# C02 — Conditional Research Discipline

## 1. Final decision

- **Module:** C02
- **XML tag:** <research>
- **Semantic purpose:** Escalate from ordinary grounding into a deliberate multi-step research process only when the answer depends on evidence coverage, synthesis across source classes, or resolution of material disagreement.
- **Selected deeper owner:** **Agent Skill**
- **Candidate Skill:** SKILL.md in this folder, intentionally non-installed.
- **Selected established principles:** research planning; iterative search; source triangulation; contradiction tracking; stopping criteria; transparent synthesis.
- **Key correction to the pilot:** the old trigger was too broad because "current, external, niche, contested, or comparative" work is already normal A13 territory. C02 now activates only when ordinary grounding is insufficient and research depth itself becomes part of the task.

### Final root XML

~~~xml
<research when="the task requires multi-step evidence synthesis, broad or representative coverage, or resolution of material disagreement beyond normal grounding"
          principles="research-planning,iterative-search,source-triangulation,contradiction-tracking,stopping-criteria"
          ref="apex-meta/handoff/universal-ai-instruction-system/module-deepening/C02-conditional-research-discipline/SKILL.md"
          deepen_when="ordinary grounding is insufficient because the answer depends on coverage, synthesis, or unresolved conflicting evidence">
  Frame the research question and decision need, plan the evidence needed, search and follow leads iteratively across appropriate source classes, and preserve material gaps or conflicts. Stop when additional searching is unlikely to change the answer materially; synthesize only what the evidence supports.
</research>
~~~

### Equivalent compact Markdown control

~~~markdown
**Research — planning / iterative search / triangulation / contradiction tracking / stopping criteria:** Use a deep research process only when ordinary grounding is insufficient because the task needs multi-step synthesis, broad or representative coverage, or resolution of material disagreement. Frame the question and decision need, plan the evidence needed, search and follow leads iteratively across appropriate source classes, preserve gaps and conflicts, and stop when more searching is unlikely to change the answer materially.
~~~

## 2. What problem C02 actually solves

C02 is not the instruction "use the web." A13 already owns that behavior.

C02 exists for the different failure mode:

~~~text
agent performs one or two searches
-> finds plausible sources
-> stops at the first coherent narrative
-> misses a major source class, contradiction, or competing explanation
-> presents a recommendation as researched
~~~

The desired replacement is:

~~~text
ordinary A13 grounding proves insufficient
-> frame the research question and decision need
-> identify what evidence would materially answer it
-> search/read iteratively across the needed source classes
-> follow important leads and contradictions
-> synthesize only after checking coverage and disagreement
-> stop when new evidence is unlikely to change the conclusion materially
~~~

This is a research-process rule, not an evidence-claim rule. A08 still owns what individual claims may assert.

## 3. Why this is the right method

### 3.1 Current OpenAI / ChatGPT evidence

OpenAI's current Deep Research product draws a clear boundary between ordinary search and deeper investigation. Deep Research is described as a workflow for complex questions that plans, researches, and synthesizes into a documented report. Current product guidance explicitly includes:

- a stated desired outcome and constraints;
- a proposed research plan that the user can review;
- use of the public web, specific sites, uploaded files, and connected apps;
- iterative progress that can be steered while the work runs;
- a final structured report with citations/source links.

The February 2026 Deep Research update also added the ability to restrict or prioritize trusted sites and connect MCP/apps. That supports source-strategy control rather than indiscriminate browsing.

OpenAI Academy separately distinguishes ordinary Search from Deep Research and frames research as moving from a fuzzy question to a plan/sub-questions, gathering and comparing sources, identifying gaps or contradictions, and producing evidence-backed outputs. This supports a proportional escalation boundary rather than deep-research ceremony on every factual task.

Portable implication:

~~~text
normal external fact / recommendation
-> ordinary search + grounding

complex evidence question
-> explicit research plan
-> multi-step search/read/synthesis
-> cited, reviewable result
~~~

C02 should encode that boundary, not duplicate the product UI.

### 3.2 Independent mature-agent convergence

**Google Gemini Deep Research.** Google's current Deep Research agent explicitly uses the loop Plan -> Search -> Read -> Iterate -> Output for workloads such as market analysis, due diligence, literature reviews, and competitive landscaping. It also supports collaborative plan review and multiple tool/source types. This independently supports iterative research as a specialized mode distinct from low-latency ordinary chat/search.

**GitHub Copilot.** GitHub Copilot CLI now exposes a dedicated /research command that invokes a specialized research agent for exhaustive, cited investigation across codebases, GitHub repositories, and the web. GitHub documents that this research agent must be explicitly invoked rather than being automatically triggered by the normal agent. Copilot cloud agent also separates repository research/planning from implementation.

The portable convergence is:

- deep research is a recognizable task class, not the default for every query;
- it benefits from a distinct workflow/context;
- the workflow is iterative, source-aware, and citation-producing;
- planning and synthesis are explicit stages;
- the research result should be reviewable before it becomes implementation or decision authority.

### 3.3 Established external research discipline

Systematic-review and evidence-synthesis practice contributes durable concepts, but it must not be copied wholesale into normal agent work.

Cochrane's current handbook emphasizes:

- define the review question/scope before searching;
- use an explicit search strategy;
- search across sources appropriate to the question rather than one convenient database;
- reduce selection bias by avoiding ad hoc source selection;
- document search/selection decisions;
- treat contradictions, missing results, and bias as part of interpretation.

PRISMA 2020 and PRISMA-S reinforce transparent reporting of how evidence was found and selected.

These practices are useful as escalation patterns for high-rigor research, but they are too formal to become the universal C02 procedure. C02 borrows only the durable ideas: pre-frame the question, search systematically enough for the decision, avoid convenience-source bias, preserve gaps/conflicts, and make the process auditable when consequence warrants it.

### 3.4 Local synthesis

The old pilot trigger was:

~~~text
current OR external OR niche OR contested OR comparative
-> research
~~~

That collides with A13 because nearly every recommendation, implementation-method question, or current product question is external/current/comparative.

The corrected boundary is:

~~~text
A13 normal grounding
-> enough evidence + material congruence
-> proceed

IF answer still depends on:
- multi-step synthesis,
- broad/representative coverage, or
- unresolved material disagreement

THEN C02 deepens
-> research plan
-> iterative search/read/follow-up
-> contradiction/gap tracking
-> evidence-changing stop rule
-> synthesis
~~~

## 4. Semantic contract

### MUST

- Start from the actual research question, intended use/decision, scope, constraints, and required freshness.
- Identify the evidence categories or source classes that could materially change the answer before broad searching.
- Prefer current primary/authoritative sources for capability, policy, version, standard, or vendor claims; add independent/production evidence where maturity or real-world performance matters.
- Search iteratively: use early evidence to refine queries, follow important citations/leads, and investigate contradictions rather than running a fixed one-shot query list.
- Distinguish source coverage from source count. Several derivative pages repeating the same origin do not establish broad evidence.
- Keep material contradictory evidence and unresolved gaps visible until they are resolved or explicitly carried into the conclusion.
- Reassess the research question when new evidence changes the frame.
- Use a proportional stopping condition: stop when additional credible searching is unlikely to change the material conclusion, decision, or uncertainty enough to justify more effort.
- Synthesize only claims supported under A08 and preserve uncertainty when the evidence cannot settle the question.
- Produce a source-grounded deliverable suitable for the requested decision or downstream work, not a bibliography dump.

### MUST NOT

- Trigger C02 merely because a question is current, factual, external, niche, or comparative.
- Replace A13's ordinary three-source grounding pass with a mandatory research project.
- Treat source quantity as a substitute for source diversity, authority, independence, or decision relevance.
- Search indefinitely for "completeness" without a decision-relevant stopping rule.
- Use systematic-review ceremony, PRISMA flow diagrams, formal inclusion/exclusion tables, or exhaustive literature searches unless the task actually requires that rigor.
- Flatten credible source conflict into a single synthetic consensus.
- Let a vendor's own documentation alone establish independent maturity, reliability, battle-tested status, or ecosystem consensus.
- Let community discussion alone establish normative capability/policy when a current primary source exists.
- Turn research findings directly into an operator-owned decision; C01 still owns the final material choice where applicable.
- Absorb the separate Source-Governed Execution Contract. If the operator supplies must-use or priority sources, those authorities govern the research input.

### Activation condition

C02 activates when **ordinary A13 grounding is not sufficient** because the task needs one or more of:

1. **multi-step evidence synthesis** — the answer depends on combining several evidence threads or subquestions;
2. **broad or representative coverage** — missing a source class or major alternative could materially bias the answer;
3. **material disagreement resolution** — credible sources conflict in a way that could change the conclusion;
4. an explicitly requested deep-research class such as due diligence, literature review, market/competitive landscape, technology landscape, or evidence synthesis.

C02 does not activate solely because more than one source is useful.

### Deepen condition

Load the candidate Research Skill when the activation condition above is met.

Do not load it for ordinary A13 grounding. This preserves context and keeps simple work simple.

## 5. Neighboring-module boundaries

**A13 <grounding>** is the gateway. It owns the normal pattern: actual frame/problem/task/environment -> web search -> at least three verified-quality sources by default -> congruence check -> reason from evidence. C02 begins only when that process is insufficient.

**A08 <evidence>** governs what the collected evidence actually supports, including source-vs-inference separation, claim strength, freshness, and uncertainty. C02 gathers and organizes evidence; A08 constrains claims.

**A11 <current_truth>** governs which active repository/local source is authoritative when local artifacts conflict. C02 must not use general web evidence to displace a governing current local authority.

**C01 <decision>** owns a material operator choice after evidence is gathered. C02 can reduce uncertainty and eliminate non-viable options; it must not hide value judgments inside "research."

**A03 <reuse>** may use C02 when the reuse landscape is genuinely complex, but a normal tool/library check stays A13 unless broader coverage or disagreement matters.

**A04 <workflow>** governs proportional execution generally. C02 is one specialized deep workflow, not a global rigor taxonomy.

**C03 <informatics>** will govern formal repository knowledge/authoring when its trigger matches. C02 may produce research findings that C03 later structures, but research procedure and formal authoring remain separate.

**Source-Governed Execution Contract** remains a separate later synthesis item. C02 does not redefine operator-selected source precedence.

## 6. Deep method

The executable deep method lives in SKILL.md. Its compact loop is:

~~~text
1. Frame
   -> question / decision / scope / constraints / freshness

2. Map evidence needs
   -> source classes and subquestions that could change the result

3. Scan
   -> establish vocabulary, major candidates, and likely primary sources

4. Verify
   -> inspect primary/authoritative evidence and independent evidence where needed

5. Iterate
   -> follow leads, search missing classes, investigate contradictions

6. Synthesize
   -> claim-level support, alternatives, gaps, disagreement, practical implications

7. Stop
   -> when new credible evidence is unlikely to materially change the conclusion
~~~

The Skill deliberately does not mandate a universal source count, fixed query count, fixed number of iterations, or formal evidence matrix.

## 7. Scenario simulations

| Scenario | Current-pilot risk | Candidate behavior | Observable pass criterion | Skill? |
|---|---|---|---|---|
| **Simple / negative:** "What is the current supported Python version for Tool X?" | Old trigger fires because claim is current/external | A13 checks current authoritative docs plus corroboration; if congruent, answer directly | no plan/report ceremony; no C02 activation | No |
| **Positive:** "Compare the established approaches for long-running AI-agent memory and recommend what fits our local-first environment" | Old rule says "research" but gives no actual method | frame decision; map architecture/source classes; inspect current vendor/agent guidance and battle-tested implementations; track trade-offs/conflicts; synthesize when coverage stabilizes | major approach classes and conflicts are represented; recommendation traceable to evidence | Yes |
| **Due diligence:** "Is product Y mature enough to become a core dependency?" | vendor docs may dominate because they are easy to find | split capability, maintenance, adoption/production, security/support, and environment-fit evidence; seek independent signals; preserve unsupported maturity claims | no "battle-tested" conclusion from vendor docs alone | Yes |
| **Ambiguous:** "Research the best workflow system" | broad search could explode without a decision frame | use A05/target context to establish intended use and decisive constraints before deep research | research scope becomes decision-relevant rather than generic | Conditional |
| **Conflict:** two current official sources disagree on feature availability | first coherent source may win | investigate version, scope, dates, release channel, direct observation; preserve conflict if unresolved | no false consensus; conclusion conditional if necessary | Yes |
| **Comparative but shallow:** "A or B for this one small script?" and both have clear current docs | old trigger fires because comparative | A13 verifies fit and decides/uses C01 only if operator-owned trade-off remains | C02 does not activate | No |
| **Known failure:** agent finds three SEO summaries that repeat the same vendor announcement and calls that "triangulated" | current pilot names triangulation but does not define independence | trace derivative claims to origin, add independent/primary evidence, mark missing source classes | source duplication cannot masquerade as independent evidence | Yes |
| **Research inflation:** agent keeps searching long after ten strong sources converge | no stopping condition | stop once new credible evidence no longer changes the material conclusion or uncertainty | bounded research; explicit reason to stop | Yes |
| **XML vs Markdown control** | structured XML may be assumed superior | same trigger and deep method under both representations | no presumed semantic advantage; final full-contract evaluation decides | N/A |

## 8. Realistic orchestration / agent user stories

### US-C02-01 — ordinary fact stays ordinary

**Input:** current product capability question.

**Expected:** A13 grounds it quickly. C02 remains dormant unless sources materially conflict or the answer unexpectedly expands into a multi-part evidence problem.

### US-C02-02 — architecture landscape

**Input:** choose among existing orchestration systems for a complex environment.

**Expected:** C02 maps the relevant solution classes before recommending, verifies current capabilities and maturity, follows contradictions, and synthesizes only after the landscape is sufficiently represented.

### US-C02-03 — repository + external research

**Input:** determine whether an existing external framework can replace a custom internal component.

**Expected:** inspect local constraints/current truth first, then research external options. C02 does not let generic best practice override repository authority; it tests fit against the actual environment.

### US-C02-04 — contested practice

**Input:** authoritative sources disagree materially.

**Expected:** identify whether disagreement comes from version, scope, evidence quality, or a genuine unresolved controversy. Preserve uncertainty if the conflict cannot be resolved.

### US-C02-05 — research to operator decision

**Input:** after research, two viable approaches remain and the difference is mainly operator preference.

**Expected:** C02 ends with evidence and trade-offs; C01 surfaces the full material operator decision rather than hiding it inside a research recommendation.

## 9. Wording alternatives considered

### Candidate A — current pilot

~~~xml
<research when="the task depends on current, external, niche, contested, or comparative evidence"
          principles="landscape-scan,source-authority,triangulation">
  Research before canonizing a recommendation. Prefer primary or authoritative sources and distinguish verified facts from inference.
</research>
~~~

**Rejected:** duplicates A13's normal trigger, under-specifies the deep method, and lacks a stop condition.

### Candidate B — "complex or disputed" only

~~~xml
<research when="the task is complex or credible sources disagree">
  Plan and perform deeper research until the evidence is sufficient.
</research>
~~~

**Rejected:** "complex" is too vague; "sufficient" gives no observable stop rule; misses landscape/coverage tasks where sources may agree but incomplete sampling would bias the result.

### Candidate C — systematic-review style

~~~xml
<research when="research is required">
  Define protocol, inclusion criteria, source databases, search strings, screening process, extraction schema, bias assessment, and synthesis method before searching.
</research>
~~~

**Rejected:** rigorous for formal evidence syntheses but far too ceremonial for general AI-agent research. Use such methods only when the domain/task explicitly needs them.

### Candidate D — selected

The selected wording uses the unique trigger: **multi-step synthesis, representative coverage, or material disagreement beyond normal grounding**, with an iterative research loop and a material-conclusion stopping rule.

## 10. Deeper-owner decision

**Selected: Agent Skill.**

Why a Skill is justified:

1. C02 has a recognizable semantic trigger.
2. The method is genuinely multi-step and reusable.
3. OpenAI, Google, and GitHub independently separate deep research from ordinary search/chat rather than keeping the whole procedure always loaded.
4. The procedure benefits from progressive disclosure because most tasks do not need it.
5. A short Skill can encode the research loop without adding a permanent token burden to every agent task.

Why **not** a focused reference:

A reference would explain the concept but would not give agents an executable research loop and stop condition.

Why **not** a scoped rule:

Applicability is semantic, not reliably tied to a file path or subsystem.

Why **not** no deeper artifact:

The root sentence alone does not define enough procedure to prevent one-shot searching, convenience-source bias, contradiction loss, or endless searching.

The candidate is intentionally not installed. Final cross-module evaluation must still verify that loading it improves research outcomes enough to justify activation.

## 11. Sources

Checked 2026-09-22. Current AI-native primary evidence first.

### OpenAI / ChatGPT

1. OpenAI Help Center — Deep research in ChatGPT
   https://help.openai.com/en/articles/10500283-deep-research
2. OpenAI — Introducing deep research; includes February 10, 2026 update on trusted sites, MCP/apps, progress steering
   https://openai.com/index/introducing-deep-research/
3. OpenAI Academy — Research with ChatGPT
   https://openai.com/academy/search-and-deep-research/
4. OpenAI Academy — ChatGPT for research
   https://openai.com/academy/research/
5. OpenAI — Deep research system card
   https://openai.com/index/deep-research-system-card/

### Independent mature-agent systems

6. Google AI for Developers — Gemini Deep Research agent
   https://ai.google.dev/gemini-api/docs/deep-research
7. GitHub Docs — Researching with GitHub Copilot CLI
   https://docs.github.com/en/copilot/concepts/agents/copilot-cli/research
8. GitHub Docs — About custom agents; built-in research agent and separate context/subagents
   https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-custom-agents
9. GitHub Docs — Research, plan, and iterate on code changes with Copilot cloud agent
   https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/research-plan-iterate

### Established external research discipline

10. Cochrane Handbook — Chapter 1: Starting a review
    https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-01
11. Cochrane Handbook — Chapter 4: Searching for and selecting studies
    https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04
12. PRISMA 2020
    https://www.prisma-statement.org/prisma-2020
13. PRISMA-S — reporting literature searches
    https://www.prisma-statement.org/prisma-search

## 12. Evidence confidence and open uncertainty

- **High confidence:** C02 must not duplicate A13; ordinary current/external/comparative questions should not automatically invoke deep research.
- **High confidence:** planning, iterative search/read, explicit source strategy, and cited synthesis converge across OpenAI, Google, and GitHub deep-research implementations.
- **High confidence:** a stopping rule is needed to prevent research inflation; "search until exhaustive" is not proportionate for general agent work.
- **High confidence:** source coverage/independence matters more than raw count in deep research.
- **High confidence:** formal systematic-review methods are useful only as task-specific escalation, not as the generic agent procedure.
- **Moderate-high confidence:** "additional searching is unlikely to change the answer materially" is the simplest portable stop rule. It is intentionally qualitative rather than a fabricated numeric saturation threshold.
- **Primary evaluation uncertainty:** whether the root rule plus Skill trigger reliably separates A13 from C02 across different agent runtimes. Final controlled evaluation should explicitly test over-triggering.
- **Secondary evaluation uncertainty:** whether the Skill should eventually live as a general Agent Skill, a ChatGPT Skill, or a runtime-specific research agent profile. This run defines behavior, not propagation.

## 13. Final invariant

~~~text
A13 = normal grounding
C02 = research escalation

Do not deepen because a fact is merely external/current/comparative.

Deepen when the answer itself depends on:
- multi-step synthesis,
- representative coverage, or
- resolving material disagreement.

Then:
frame -> map evidence -> scan -> verify -> iterate -> synthesize -> stop
when new credible evidence is unlikely to change the material conclusion.
~~~
