---
type: ModuleDeepeningResult
title: A03 Battle-Proven Reuse & Minimal Adaptation Before Invention
description: Evidence-backed deepening result for the universal <reuse> module, strengthened by operator direction to preserve battle-proven implementations near their established form and restrict custom construction to verified fit gaps.
status: DONE
updated: 2026-09-07
---

# A03 — Battle-Proven Reuse & Minimal Adaptation Before Invention

## 1. Final decision

- **Module:** A03
- **XML tag:** `<reuse>`
- **Semantic purpose:** Obtain required capability from established, proven implementations before creating custom equivalents; preserve proven architecture and behavior where fit; concentrate adaptation only at verified project-specific gaps.
- **Selected deeper owner:** **No deeper artifact**
- **Selected established principles:** make/buy/reuse analysis; software/system reuse; COTS/OSS evaluation; fitness for intended use; proven operational capability; adaptation before invention.
- **Operator-directed strengthening:** research of existing systems is not sufficient if the agent then recreates their capability as a custom local imitation. The preferred realization order is reuse directly -> compose proven components -> minimally adapt -> custom-build only the verified irreducible gap.
- **Removed as primary anchor:** `KISS`. Simplicity matters, but KISS is an implementation-complexity principle and overlaps A04; it does not itself answer reuse-vs-build.

### Final root XML

```xml
<reuse principles="reuse-before-build,battle-tested-practice,adaptation-before-invention,fitness-for-use">
  Prefer battle-proven existing solutions in their established form. Reuse or compose them directly when fit; otherwise adapt only the smallest necessary surface. Invent or rebuild only when verified evidence shows suitable established options cannot meet the target or governing constraints.
</reuse>
```

### Equivalent compact Markdown control

```markdown
**Reuse — battle-proven reuse / minimal adaptation:** Prefer battle-proven existing solutions in their established form. Reuse or compose them directly when fit; otherwise adapt only the smallest necessary surface. Invent or rebuild only when verified evidence shows suitable established options cannot meet the target or governing constraints.
```

### Alternative B — AI-native reuse-before-build candidate

**Status:** unselected comparison candidate from `../../10-AI-NATIVE-RETROACTIVE-AUDIT-A01-A05.md`. The final root XML above remains the completed baseline / Alternative A until later evaluation selects a winner.

```xml
<reuse principles="reuse-before-build,fitness-for-use">
  Before creating nontrivial custom capability, inspect existing project assets first and, when an established external solution is plausibly relevant, evaluate it before building. Reuse or adapt a fit-for-purpose option when it meets the target and constraints; build new when the gap or overall trade-off justifies it.
</reuse>
```

Equivalent compact Markdown:

```markdown
**Reuse — reuse before build / fitness for use:** Before creating nontrivial custom capability, inspect existing project assets first and, when an established external solution is plausibly relevant, evaluate it before building. Reuse or adapt a fit-for-purpose option when it meets the target and constraints; build new when the gap or overall trade-off justifies it.
```

**Why retain this alternative:** current ChatGPT/Codex customization patterns explicitly favor existing reusable plugins/Skills/capabilities before custom construction, but they do not imply that every nontrivial change requires a general external landscape scan. Alternative B keeps project-local reuse first and makes external evaluation conditional on plausible relevance.

**Evaluation question:** does Alternative B preserve anti-reinvention behavior while avoiding unnecessary market/package research on tasks where external reuse is unlikely to matter?

## 2. Why this is the right method

### 2.1 Underlying discipline evidence

The strongest established analogue is **make/buy/reuse analysis**, not a blanket “never build” rule.

NASA software acquisition guidance explicitly treats the following as legitimate alternatives to evaluate against a defined need:

- acquire off-the-shelf capability;
- develop internally;
- contract development/service;
- enhance an existing product/service;
- reuse an existing product/service.

NASA guidance then evaluates candidates against requirements, environment, cost including support, performance record, risk, licensing, supplier stability, maintenance, and verification/validation needs. The decision is the best overall value for the defined need—not reuse at any cost and not custom development by default.

NASA’s Systems Engineering Handbook likewise uses a **make/buy/reuse** product-implementation decision and explicitly recognizes savings from reuse while still requiring verification and validation for the intended environment.

This gives A03 a clear positive function:

```text
required capability
      |
      v
existing project asset? ---- yes ---> reuse/adapt if fit
      |
      no / insufficient
      v
established external solution? -- yes --> reuse/adapt if fit
      |
      no / worse trade-off
      v
custom capability justified
```

The objective is **leverage**: inherit capability, accumulated testing, ecosystem knowledge, documented patterns, maintenance work, or specialized expertise when those advantages actually transfer to the present target.

### 2.2 Why blind reuse is also wrong

NASA’s COTS/GOTS/OSS/reuse guidance is equally explicit that pre-existing software must still be fit for its intended application. Relevant concerns include:

- functionality and technical fit;
- intended environment;
- documentation and test evidence;
- licensing/usage rights;
- integration and modification cost;
- maintenance and future support;
- supplier/community stability;
- reliability, safety, and security risk;
- verification/validation effort.

NASA specifically cautions that modifying off-the-shelf software from another application realm can have underestimated integration/testing costs.

Therefore A03 must prevent **two opposite errors**:

1. **reinvention bias / Not-Invented-Here behavior:** building custom capability while mature suitable options already exist;
2. **dependency maximalism / reuse cargo cult:** installing frameworks, packages, plugins, or services merely because they exist, even when the local need is simpler or the integration burden is worse.

The current pilot controls the first error well but is weaker on the second.

### 2.3 Proven agent implementations

Current mature agent systems increasingly expose **reusable capability ecosystems** rather than expecting the model to invent every workflow/tool integration itself.

- **OpenAI Codex:** OpenAI’s current Plugins repository is a curated marketplace of reusable plugin examples containing Skills, MCP integrations, agents, commands, hooks, and assets. The former standalone skills catalog now directs users to the Plugins repository. OpenAI’s own Codex repository instructions also tell contributors to leverage existing abstractions rather than plumbing equivalent functionality through multiple layers.
- **Claude Code:** Anthropic states that built-in tools cover most coding tasks, with Skills, MCP, subagents, hooks, and plugins added for specific reusable capability. Its plugin marketplace explicitly supports discovering and installing prebuilt plugins instead of always authoring custom extensions.
- **GitHub Copilot:** Copilot can use Agent Skills shared online and exposes `gh skill` to discover/install existing skills from GitHub repositories. GitHub explicitly recommends always-on instructions for broad simple rules and Skills for detailed task-specific reusable workflows.
- **Cursor:** Cursor supports portable Agent Skills and installable Plugins containing Skills, MCP servers, rules, agents, commands, and hooks. Its customization UI includes a marketplace/leaderboard intended to help teams adopt commonly used setups quickly.
- **Kiro:** Kiro Powers package established tools, workflows, best practices, MCP integrations, and Agent Skills into dynamically activated reusable capabilities; curated partner Powers are installable directly, with custom creation remaining available when needed.
- **Gemini CLI:** Gemini supports built-in, extension, user, and workspace Skills plus installable extensions from GitHub. The extension format bundles MCP tools, commands, hooks, subagents, and Skills for reuse.
- **Windsurf:** Cascade supports reusable Skills and an MCP marketplace; Skills package multi-step procedures and supporting files so the agent does not reconstruct the workflow from scratch each time.
- **Agent Skills open standard:** the standard explicitly frames Skills as reusable, portable, version-controlled knowledge/workflows. Its guidance says that when agents repeatedly reinvent the same logic, that is a signal to package and reuse a tested script instead.

These systems do not prove that any particular plugin or Skill is fit for a specific project. They do show a clear mature implementation pattern: **discover/use existing capability where it fits; extend only when there is an actual gap**.

### 2.4 Local inference / decision

The pilot currently says:

```xml
<reuse principles="reuse-before-build,KISS">
  Prefer proven existing methods, tools, and patterns before inventing a new abstraction. Custom build requires evidence that suitable existing options are insufficient.
</reuse>
```

This is directionally correct but has four weaknesses:

1. **“new abstraction” is too narrow.** Agents can reinvent scripts, integrations, workflows, adapters, parsers, schemas, or infrastructure without thinking of them as abstractions.
2. **“insufficient” is too binary.** An existing option may technically work but be a worse choice because of licensing, maintenance, integration, platform, performance, privacy, complexity, or lifecycle cost.
3. **“proven” is useful but underspecified.** Proven elsewhere is not equivalent to fit for this target/environment.
4. **KISS does not define the decision.** A small custom script may be simpler than a large framework; a mature package may be simpler than custom code. The correct comparison is fit and overall trade-off.

The replacement therefore adds:

- **project assets first** — reuse what already exists in the actual environment before external discovery;
- **established external solutions second** — avoid local reinvention when mature capability exists;
- **fit-for-purpose** — transferability to the actual target matters;
- **reuse or adapt** — full replacement is not required; bounded modification/composition is legitimate;
- **demonstrated gap or better overall trade-off** — custom work remains legitimate when it is actually superior.

## 3. Semantic contract

### MUST

- Before creating a **nontrivial custom capability**, inspect suitable existing project/repository assets and established external solutions that may already satisfy or substantially satisfy the need.
- When an established ecosystem exists, identify solutions with credible evidence of real use, maintenance, operational maturity, or established practice before authorizing an equivalent custom implementation.
- Prefer using a fit-for-purpose proven solution in its established form so its accumulated testing, architecture, maintenance knowledge, ecosystem behavior, and documented operating patterns are preserved.
- When no single solution fits completely, prefer composition of proven components or the smallest project-specific adapter over rebuilding the proven capability itself.
- Treat fitness as more than feature presence: verify the target, governing constraints, intended environment, integration surface, maintenance, licensing, security/privacy, platform, and other load-bearing requirements when relevant.
- Require verified evidence of a material fit gap, incompatible governing constraint, or genuinely project-specific boundary before replacing proven capability with custom construction.
- Keep custom code concentrated at the verified gap. Do not use a local adapter requirement as justification to recreate the surrounding mature system.
- Preserve evidence of why established options were rejected when the choice is consequential.

### MUST NOT

- Invent a custom framework, subsystem, parser, workflow, agent layer, adapter ecosystem, policy system, or reusable abstraction merely because the model can generate a plausible version.
- Research an established system, borrow its concepts, then present a newly invented local imitation as equivalent to reuse.
- Assume no suitable existing option exists without checking when the task concerns nontrivial capability with an established solution ecosystem.
- Treat model intuition that custom code is “simpler,” “cleaner,” “more flexible,” or a “better trade-off” as sufficient justification to discard proven solutions.
- Treat “open source,” “popular,” “official,” “battle-tested,” or “already installed” as automatic proof of fitness; A13/A08 must verify load-bearing claims and the option must still fit A01.
- Modify, fork, wrap, or replace more of an established solution than the target-specific gap actually requires.
- Install unrelated dependencies merely to claim reuse.
- Turn a trivial local edit into a market survey, package comparison, or architecture study.
- Use A03 to decide what work is in scope; A02 owns authorization boundaries.
- Use A03 to prescribe workflow ceremony; A04 owns execution complexity.
- Use A03 to invent the target/acceptance standard; A01 owns outcome adequacy.

### Activation condition

Always available as a preference, but **active evaluation is required only when the agent is about to create or select nontrivial capability for which meaningful reuse may exist**.

A typo fix, one-line transformation, or already-specified local edit should not trigger external option research.

### Deepen condition

A03 itself has no separate deep artifact.

When reuse selection becomes consequential:

- **A13 `<grounding>`** requires the decision to be grounded in current external reality rather than model reasoning alone and, where feasible, observed behavior or direct tests;
- **C02 `<research>`** should govern the deeper external landscape/source-verification method;
- **C01 `<decision>`** should govern trade-study presentation where material alternatives require an operator choice;
- **A08 `<evidence>`** should govern source authority, provenance, freshness, and uncertainty.

A03 should not duplicate those methods. Its responsibility is the realization preference: proven reuse first, minimal adaptation second, invention only at a verified gap.

## 4. Minimal observable reuse decision

This is explanatory guidance for evaluation, not an always-visible checklist.

For a nontrivial capability:

1. **Need:** What capability is actually required by A01 within A02’s authorized scope?
2. **Local reuse:** Does the project/repository already contain a suitable implementation, helper, Skill, tool, package, service, or pattern?
3. **External reuse:** Is there an established external solution likely to solve most/all of the need?
4. **Fit:** Does the candidate meet the actual target and material constraints in the intended environment?
5. **Trade-off:** Is reuse/adaptation better overall than custom construction after relevant integration/lifecycle costs and risks?
6. **Decision:** Reuse, adapt, compose, or build. If build wins in a consequential case, the gap/trade-off should be observable rather than assumed.

The sequence is not a mandatory six-step ritual for every task; it defines what a good decision should contain when the question is material.

## 5. Neighboring-module boundaries

### A01 `<target>` — substantive outcome and adequacy

A01 defines what useful capability/result must be realized. A03 cannot force reuse of an option that fails that outcome merely because it is mature or convenient.

**Boundary:** A01 asks “does this actually achieve the target?” A03 asks “can we obtain that capability from existing proven assets before creating it ourselves?”

### A02 `<scope>` — authorized work

A02 decides whether a capability/work item belongs inside the task. A03 only chooses **how to source/realize an in-scope capability**.

Reuse is not a license to install unrelated tools or broaden the project.

### A04 `<workflow>` — process complexity

A03 does not mean every decision needs a formal market scan or trade study. A04 governs whether the task needs planning, decomposition, delegation, comparison, or review.

A trivial task can satisfy A03 by using the obvious existing mechanism directly.

### A05 `<intent>` — ambiguity

A03 must not infer a reusable solution by narrowing or changing an ambiguous target. If a materially different interpretation changes what capability is needed, A05 resolves the intent first.

### A08 `<evidence>` — source confidence

Claims such as “battle-tested,” “maintained,” “official,” “supports Windows,” or “works offline” require evidence when they are load-bearing. A03 does not own freshness/provenance rules.

### A10 `<recovery>` — incidental failures

If a reused component fails incidentally, A10 governs workaround/recovery. A03 must not force endless repair of a dependency merely because reuse was initially preferred.

### C01 `<decision>` and C02 `<research>`

A03 establishes the **reuse-before-custom decision order**. C01 and C02 provide the deeper comparison/research machinery when the decision is material enough to justify it.

No merge is recommended now; the three responsibilities are distinct.

## 6. Failure modes this module exists to prevent

1. **Not-Invented-Here / reinvention bias:** custom-building capability that suitable established options already provide.
2. **LLM capability hallucination:** the agent assumes it can reliably recreate a specialized system because it can generate plausible code/instructions.
3. **Framework-from-scratch drift:** the agent invents a new architecture/policy/workflow instead of integrating an established one.
4. **Duplicate local capability:** the repository already has a helper, Skill, script, or component but the agent creates another.
5. **Shallow name-dropping:** the agent mentions existing products but never verifies whether they actually fit or participate in the implementation.
6. **Dependency maximalism:** “reuse” becomes installing many libraries/plugins/services with no demonstrated value.
7. **Popularity substitution:** popularity, stars, vendor branding, or “official” status is mistaken for fitness.
8. **Integration-cost blindness:** an external system technically covers the feature but creates more custom adapter/state/maintenance work than a bounded local implementation.
9. **Legacy lock-in:** reuse is preserved after material constraints or the target make the inherited component unsuitable.
10. **Research ceremony on simple tasks:** the agent spends effort comparing alternatives where the obvious existing mechanism already suffices.
11. **Custom-build loophole:** the agent asserts “nothing suitable exists” without actually checking in a domain where mature solutions are likely.
12. **Reuse as proxy:** selecting an existing product is treated as success even though the product has not been validated against the substantive target.

## 7. Wording decision

### Candidate A — current strict reuse-before-build

```xml
<reuse principles="reuse-before-build,KISS">
  Prefer proven existing methods, tools, and patterns before inventing a new abstraction. Custom build requires evidence that suitable existing options are insufficient.
</reuse>
```

**Strengths:** compact; directly attacks unnecessary invention; strongly aligned with the operator’s observed failure mode.

**Why it loses:** “new abstraction” is narrow; “insufficient” is binary; KISS is adjacent rather than defining; it does not explicitly test fitness or lifecycle/integration trade-off.

### Candidate B — mandatory landscape scan

```xml
<reuse principles="market-scan,make-buy-reuse">
  Before creating any new capability, research and compare existing solutions; custom build is allowed only after documenting why all viable alternatives fail.
</reuse>
```

**Strengths:** strongest anti-reinvention behavior.

**Why it loses:** creates unnecessary ceremony, exhaustive-search pressure, and latency even for trivial/local tasks. It also duplicates C02/C01.

### Candidate C — fit-for-purpose reuse/adapt/build — ORIGINAL RESEARCH SELECTION, SUPERSEDED

```xml
<reuse principles="make-buy-reuse,fitness-for-use">
  Before building nontrivial custom capability, check suitable existing project assets and established external solutions. Reuse or adapt a fit-for-purpose option when it meets the target and constraints; build new only when a demonstrated gap or better overall trade-off justifies it.
</reuse>
```

**Why it originally won:** it added positive leverage, made local/external reuse explicit, allowed adaptation/composition, and prevented blind dependency accumulation.

**Why it is superseded:** the operator identified that “better overall trade-off” leaves too much room for model-generated rationalization. In repeated real workflows, agents can research a proven system, decide that recreating it locally appears cleaner or simpler, and then build an unproven imitation. The governing policy therefore requires preservation of battle-proven solutions near their established form and verified evidence before custom replacement.

### Candidate E — battle-proven reuse with minimal adaptation — SELECTED

```xml
<reuse principles="reuse-before-build,battle-tested-practice,adaptation-before-invention,fitness-for-use">
  Prefer battle-proven existing solutions in their established form. Reuse or compose them directly when fit; otherwise adapt only the smallest necessary surface. Invent or rebuild only when verified evidence shows suitable established options cannot meet the target or governing constraints.
</reuse>
```

**Why it wins:** it retains fitness-for-use and legitimate project-specific adaptation while closing the model-rationalization loophole. Existing operational capability is preserved rather than treated merely as design inspiration.

### Candidate D — existing project assets only

```xml
<reuse principles="local-reuse">
  Prefer existing project code, tools, and patterns before introducing new dependencies or custom abstractions.
</reuse>
```

**Strengths:** low cost and low dependency risk.

**Why it loses:** reproduces the exact recurring failure where an agent ignores mature external systems and invents a local solution simply because the repository does not already contain one.

## 8. Scenario simulations

### Scenario A — simple / negative case

**Input:** “Fix this typo.”

- **Current pilot risk:** low, but “custom build requires evidence” can be over-read into unnecessary search.
- **Candidate behavior:** edit the typo directly. No package/Skill/product search.
- **Observable PASS:** one bounded correction; no reuse ceremony.
- **Deep guidance:** none.

### Scenario B — mature library instead of custom parser

**Input:** “Extract structured text, links, tables, comments, and media from DOCX reliably.”

- **Without A03:** agent may write a new OOXML parser because ZIP/XML manipulation is possible.
- **Candidate behavior:** inspect existing project tooling first, then established DOCX libraries/converters. Reuse/adapt a proven fit when it meets the extraction/provenance need; custom code is limited to genuine gaps/integration.
- **Observable PASS:** no bespoke parser is built without showing why mature options are inadequate.
- **Deep guidance:** C02 only if current comparative research is needed.

### Scenario C — existing project capability

**Input:** Add a second workflow that needs the same deterministic authorization validator already present in the repository.

- **Candidate behavior:** reuse the existing validator/contract rather than independently recreating the logic.
- **Observable PASS:** one canonical mechanism remains; no duplicated policy engine.
- **Deep guidance:** none unless the existing mechanism’s fit is materially uncertain.

### Scenario D — plugin/Skill ecosystem

**Input:** “Give the agent a reliable reusable workflow for a domain that already has a maintained Agent Skill/plugin.”

- **Candidate behavior:** discover/inspect the existing reusable artifact and its provenance/fit before authoring a new Skill from scratch.
- **Observable PASS:** established artifact is reused/adapted when fit; custom Skill only if the gap is demonstrated.
- **Deep guidance:** C02/C01 if alternatives are material.

### Scenario E — dependency maximalism

**Input:** Implement a deterministic 15-line normalization whose requirements are stable and already fully specified.

- **Bad reuse behavior:** add a large workflow/data-processing framework solely because it already exists.
- **Candidate behavior:** first determine whether there is an established directly fitting mechanism already available in the project/runtime. Do not adopt a large framework whose established capability is materially broader than the target merely to satisfy reuse. A tiny target-specific implementation is acceptable when there is no fit-for-purpose reusable capability to preserve.
- **Observable PASS:** A03 prevents both framework cargo-culting and reinvention. The local implementation is confined to a genuinely small target-specific gap rather than replacing an established equivalent capability.
- **Deep guidance:** none unless the existence or fitness of external equivalents is materially uncertain.

### Scenario F — popular but poor fit

**Input:** “Use an existing portfolio application as the canonical risk optimizer.” Candidate product has dashboards but lacks the required optimizer semantics.

- **Candidate behavior:** popularity/product maturity cannot substitute for fit. Reuse it only for the capability it actually provides; use another component or custom work for the material gap.
- **Observable PASS:** no false “reuse success” that fails A01.
- **Deep guidance:** C01/C02 for material architecture comparison.

### Scenario G — existing system needs bounded adaptation

**Input:** Established open-source tool covers 85% of the required workflow; one adapter is needed for the project’s source format.

- **Candidate behavior:** prefer reuse + bounded adapter if the combined solution is fit and lower-risk than rebuilding the whole capability.
- **Observable PASS:** custom code is concentrated at the proven gap, not used to replace the working 85%.
- **Deep guidance:** none unless adapter/maintenance risk is material.

### Scenario H — established options fail verified governing constraints

**Input:** Available tools are unmaintained, cloud-only despite a local-only constraint, or require an unsupported integration that prevents the target from being realized.

- **Candidate behavior:** verify those incompatibilities through A13/A08. Preserve any proven subcomponents or established methods that remain usable, and custom-build only the residual capability that established options cannot provide within the governing constraints.
- **Observable PASS:** custom construction follows verified incompatibility rather than model preference, and it does not unnecessarily recreate reusable proven capability.
- **Deep guidance:** A13/C02/A08 when current claims require external verification.

### Scenario I — explicit user constraint

**Input:** “For teaching purposes, implement this algorithm ourselves; do not use a library.”

- **Candidate behavior:** respect the governing constraint. A03 may still reuse established algorithmic methods/test vectors/patterns where compatible, but must not override the explicit no-library instruction.
- **Observable PASS:** no unwanted dependency is introduced.
- **Deep guidance:** none.

### Scenario J — research vs implementation

**Input:** “Compare existing tools and recommend the best architecture. Do not implement.”

- **Candidate behavior:** A03 drives the reuse landscape; A02 preserves the no-implementation boundary.
- **Observable PASS:** evidence-backed reuse/build recommendation only; no new system is created.
- **Deep guidance:** C01/C02 should activate.

### Scenario K — interaction with A01

**Input:** A mature existing tool technically runs but loses critical provenance required by the target.

- **Candidate behavior:** do not accept it merely because it is mature. Adapt/compose/build until the substantive A01 outcome is met.
- **Observable PASS:** reuse serves the target; target is not reduced to fit the reused tool.
- **Deep guidance:** C01/C02 if solution choice is material.

### Scenario L — XML vs Markdown control

Run Scenarios B and E with the XML wording versus the compact Markdown equivalent.

- **Expected:** both representations produce the same preference: check reuse for nontrivial capability, but allow custom work on demonstrated fit/trade-off grounds.
- **Status:** semantically equivalent by inspection; empirical cross-agent evaluation remains for the final synthesis phase.

## 9. Deeper-owner decision

**No separate Skill, reference, or scoped rule.**

This decision is deliberate even though A03 can lead to research/trade studies.

Why:

- The core A03 behavior is a universal **decision ordering**, not a domain-specific procedure.
- The root rule is self-sufficient for ordinary cases.
- A dedicated reuse Skill would duplicate the planned responsibilities of C02 `<research>` and C01 `<decision>` whenever a material landscape scan/trade study is actually needed.
- A focused reference would mostly repeat fit criteria already captured here without providing a distinct executable method.
- A scoped rule cannot determine reuse relevance from file paths.

If final cross-agent testing shows that models routinely assert “no suitable option exists” without searching, the likely remedy is **stronger A03→C02 activation coupling during synthesis**, not immediately another standalone Skill.

## 10. Alternatives rejected

| Alternative | Why rejected |
|---|---|
| **KISS as the main reuse anchor** | Simplicity is not the same as reuse selection; overlaps A04. |
| **Never build when an existing option exists** | Ignores fit, constraints, integration burden, lifecycle costs, and legitimate custom advantages. |
| **Always perform a formal market scan** | Excessive on simple tasks; duplicates C02/C01. |
| **Blindly reuse any battle-tested external product** | Battle-proven pedigree is a strong preference, not automatic fitness. Project-local proven assets, established standards/patterns, and actual target/environment constraints still matter. |
| **Local-only reuse preference** | Encourages local reinvention when mature external capability exists. |
| **Install-first experimentation** | Candidate existence is not enough; evaluation should precede integration when the dependency is material. |
| **Create an A03 Skill now** | No unique multi-step procedure remains after assigning research/trade-study mechanics to C02/C01. |

## 11. Authoritative sources

Primary/authoritative sources checked 2026-09-07:

### Reuse / make-buy-reuse / fitness

1. NASA Software Engineering Handbook — Acquisition Guidance  
   https://swehb.nasa.gov/spaces/SWEHBVB/pages/140640415/7.3%2B-%2BAcquisition%2BGuidance
2. NASA SWE-033 — Acquisition vs. Development Assessment  
   https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695412/SWE-033%2B-%2BAcquisition%2Bvs.%2BDevelopment%2BAssessment
3. NASA SWE-027 — Use of Commercial, Government, Legacy, Open Source, and Reused Software  
   https://swehb.nasa.gov/spaces/7150/pages/16449873/SWE-027%2B-%2BUse%2Bof%2BCommercial%2BGovernment%2Band%2BLegacy%2BSoftware
4. NASA Systems Engineering Handbook — Product Implementation / make-buy-reuse  
   https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf
5. The Open Group / TOGAF — Building Blocks and reuse/purchase/development alternatives  
   https://www.opengroup.org/architecture/togaf7-doc/arch/p4/bbs/bbs_adm.htm

### Mature agent reuse mechanisms

6. OpenAI Plugins repository — current curated Codex plugin examples  
   https://github.com/openai/plugins
7. OpenAI Codex repository AGENTS.md — leverage existing abstractions  
   https://github.com/openai/codex/blob/main/AGENTS.md
8. Claude Code — Extend Claude Code  
   https://code.claude.com/docs/en/features-overview
9. Claude Code — Discover/install prebuilt plugins  
   https://code.claude.com/docs/en/discover-plugins
10. GitHub Copilot — About Agent Skills  
    https://docs.github.com/en/copilot/concepts/agents/about-agent-skills
11. GitHub Copilot — Adding Agent Skills  
    https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills
12. Cursor — Agent Skills  
    https://prod.cursor.com/docs/skills
13. Cursor — Plugins / Marketplace  
    https://prod.cursor.com/docs/plugins
14. Kiro — Powers  
    https://kiro.dev/docs/powers/
15. Gemini CLI — Agent Skills  
    https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/skills.md
16. Gemini CLI — Extensions  
    https://github.com/google-gemini/gemini-cli/blob/main/docs/extensions/index.md
17. Windsurf — Cascade Skills  
    https://docs.windsurf.com/windsurf/cascade/skills
18. Windsurf — MCP integration / Marketplace  
    https://docs.windsurf.com/windsurf/cascade/mcp
19. Agent Skills open standard — Overview  
    https://agentskills.io/home
20. Agent Skills — Using scripts / reuse existing packages  
    https://agentskills.io/skill-creation/using-scripts
21. Agent Skills — Best practices / bundle repeatedly reinvented logic once  
    https://agentskills.io/skill-creation/best-practices

## 12. Evidence confidence and uncertainty

- **High confidence:** make/buy/reuse + fitness-for-use is a stronger established conceptual anchor than `reuse-before-build,KISS`.
- **High confidence:** the module should be positive leverage, not prohibition: reuse, adapt, compose, and custom build are all valid outcomes after fit/trade-off assessment.
- **High confidence:** current mature agent ecosystems increasingly provide reusable Skills/plugins/MCP packages, which makes “check existing capability before inventing it” operationally realistic across agents.
- **High confidence:** blind reuse is unsafe; lifecycle/integration/fit considerations are established parts of reuse decisions.
- **High confidence:** no dedicated A03 Skill is justified before C01/C02 are deepened; creating one now would likely duplicate their methods.
- **Moderate-high confidence:** `nontrivial custom capability` is the right threshold language to avoid ceremony. Final cross-agent evaluation should test whether different models classify “nontrivial” consistently enough.
- **Primary uncertainty for final evaluation:** whether “check suitable existing project assets and established external solutions” reliably causes agents to perform a real search when they should, or whether some models will satisfy it with a superficial assertion that no option exists.
- **Secondary uncertainty:** “better overall trade-off” is intentionally broad. C01/C02/A08 must later make consequential trade-offs evidence-backed without turning every small choice into formal MCDA.

## 13. Neighboring dependency note for later synthesis

Do not edit neighboring modules now.

For final synthesis/evaluation, specifically test:

- **A01+A03:** mature-but-inadequate product must not redefine the target;
- **A02+A03:** reuse must not broaden authorization or install unrelated systems;
- **A03+A04:** simple tasks must not trigger market-research ceremony;
- **A03+A13:** a decision to reject established capability and build custom must not rest on model reasoning alone when real-world evidence is available;
- **A03+C02:** nontrivial new capability with a mature ecosystem should cause an actual external scan rather than a claim that none exists;
- **A03+C01:** consequential reuse/adapt/build choices should become a clear trade study without duplicating A03 wording;
- **A03+A08:** “proven,” “maintained,” “supported,” and “fit” claims should be source-grounded when load-bearing.

No merge or module-count reduction is recommended from A03 research.
