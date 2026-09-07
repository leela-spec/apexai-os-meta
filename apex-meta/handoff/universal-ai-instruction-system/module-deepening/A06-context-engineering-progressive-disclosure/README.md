---
type: ModuleDeepeningResult
title: A06 Context Engineering / Progressive Disclosure
description: AI-native-first deepening result for the universal <context> module, using lean persistent guidance, progressive disclosure, and just-in-time context loading without starving the task of necessary information.
status: DONE
updated: 2026-09-07
---

# A06 — Context Engineering / Progressive Disclosure

## 1. Final decision

- **Module:** A06
- **XML tag:** `<context>`
- **Semantic purpose:** Keep the agent's working context sufficient, relevant, and navigable while preventing large always-loaded instruction sets, indiscriminate document reads, tool-output accumulation, or broad reference loading from crowding out the actual task.
- **Selected deeper owner:** **No deeper artifact**
- **Selected principles:** context engineering; progressive disclosure; just-in-time retrieval/loading; scoped instruction routing.
- **Key correction to the pilot:** replace **"smallest high-signal set"** with **"sufficient high-signal working context."** Context economy must not become context starvation.
- **Primary AI-native anchor:** OpenAI's current Codex/ChatGPT guidance and 2026 Harness Engineering evidence: keep `AGENTS.md` small, use it as a map rather than an encyclopedia, route to deeper sources of truth, and progressively disclose richer Skills/references only when relevant.

### Final root XML

```xml
<context principles="context-engineering,progressive-disclosure,JIT-retrieval">
  Maintain a sufficient high-signal working context. Keep always-loaded guidance lean and navigable; load deeper instructions, sources, files, skills, or tools just in time for the specific decision or work step that needs them, rather than bulk-loading available context upfront.
</context>
```

### Equivalent compact Markdown control

```markdown
**Context — context engineering / progressive disclosure / JIT retrieval:** Maintain a sufficient high-signal working context. Keep always-loaded guidance lean and navigable; load deeper instructions, sources, files, skills, or tools just in time for the specific decision or work step that needs them, rather than bulk-loading available context upfront.
```

## 2. Why this is the right method

### 2.1 Current OpenAI / ChatGPT / Codex evidence

A06 has unusually strong direct AI-native evidence.

#### OpenAI Harness Engineering: the monolithic instruction manual failed

OpenAI's February 2026 Harness Engineering report documents a real production experiment in which Codex generated and maintained a roughly million-line product repository. Context management became one of the team's central scaling problems.

The team explicitly reports that a single large `AGENTS.md` failed because:

- instruction context competes with the task, code, and relevant documentation;
- when too much guidance is marked important, guidance loses discriminating value;
- monolithic guidance becomes stale and difficult to maintain;
- a single instruction blob is difficult to verify for coverage, freshness, ownership, and cross-links.

Their replacement architecture is directly relevant to this program:

```text
short, stable AGENTS.md map
  -> structured repository knowledge base / system of record
  -> pointers to deeper current sources
  -> agent follows only what the active task needs
```

OpenAI describes this as **progressive disclosure**: start with a small stable entry point and teach the agent where to look next instead of overwhelming it up front.

This evidence strongly supports the program's locked architecture and also reveals a weakness in the current A06 wording: the core behavior is not merely "use fewer tokens." It is **make the right context discoverable at the right level and time**.

#### Current ChatGPT/Codex customization guidance: keep persistent instructions small

Current ChatGPT/Codex customization documentation says `AGENTS.md` should provide durable project guidance and explicitly says to **keep it small**.

It recommends:

- start with only instructions that matter;
- codify recurring feedback rather than every conceivable rule;
- put guidance in the closest directory where it applies;
- add routing guidance when the agent finds the right files but reads too many documents;
- use Skills for richer reusable workflows so those instructions do not bloat context up front.

This is not merely a token-cost optimization. It is a **scope and relevance architecture** for instructions.

#### Current OpenAI Skills: progressive disclosure is implemented mechanically

OpenAI's current Skills implementation is a concrete three-level loading pattern:

1. **Discovery metadata first:** skill name + description are visible so the host can match capability to task.
2. **Full `SKILL.md` only after selection:** procedural content is loaded only when the Skill is chosen.
3. **References/scripts only as needed:** deeper resources remain outside active context until the workflow needs them.

Codex also caps the startup Skills listing at **2% of the model context window**, or 8,000 characters when the window is unknown, specifically to avoid crowding out the rest of the prompt. If many Skills are installed, descriptions are shortened first and some may eventually be omitted.

This is strong direct evidence for two A06 design requirements:

- discovery/routing metadata should be compact but informative enough to select the right deeper source;
- deep material should remain available without being preloaded.

#### Current model guidance: large windows do not make instruction hygiene irrelevant

Current OpenAI model guidance warns that newer frontier models can be **more sensitive** to instructions in Skills and files such as `AGENTS.md`; unclear or conflicting guidance can cause the model to pause, change direction, or block work early.

Current OpenAI models expose context windows around one million tokens, but the guidance still emphasizes auditing loaded instruction files and reducing conflicting scaffolding. Therefore **capacity is not the same as useful working context**.

A06 should not encode an arbitrary token ceiling. It should encode the more durable behavior: **keep persistent context lean, route by relevance, and disclose deeper material only when the active work requires it**.

#### OpenAI Codex operating practice: context should be supplied at the point of use

OpenAI's Codex best-practice guidance recommends issue-shaped prompts with file paths, component names, diffs, documentation snippets, and analogous implementations **when relevant**. It also uses `AGENTS.md` for context the code cannot reliably convey by itself.

This supports a balanced rule:

- do not assume the model should infer all project context;
- do not dump all possible context into every run;
- supply the **specific context that changes the active decision or implementation**.

### 2.2 Independent mature-agent convergence

The same architecture appears independently across mature agent systems.

#### Anthropic Claude / Claude Code

Anthropic's Agent Skills architecture explicitly calls its loading model **progressive disclosure**:

- Level 1: Skill metadata is always loaded;
- Level 2: `SKILL.md` instructions load when the Skill triggers;
- Level 3+: bundled references load only when actually read, while scripts can execute without their source code entering context.

Anthropic's Skill authoring guidance calls the context window a **public good** shared with the system prompt, conversation history, Skill metadata, and the user's actual request. It therefore recommends concise Skills even after activation.

Anthropic's current context-management guidance adds a second important finding: **context rot**. Accuracy and recall can degrade as context grows, even when the hard context limit has not been reached. Its current production guidance therefore uses compaction/context editing for long-running workflows to keep the active working set focused.

This independently falsifies the naive rule:

> "If the model has a very large context window, load everything that might be useful."

#### GitHub Copilot

GitHub Copilot distinguishes context owners by applicability:

- repository-wide custom instructions for rules that apply broadly;
- path-specific instructions for relevant files/directories;
- `AGENTS.md` for standing cross-agent rules;
- Agent Skills for detailed workflows loaded on demand.

GitHub explicitly recommends custom instructions for simple rules relevant to almost every task and Skills for more detailed instructions that should only be accessed when relevant.

This is the same universal separation A06 needs:

```text
broad + durable -> persistent context
scoped by path -> local context
semantic workflow trigger -> Skill / on-demand context
```

#### Gemini CLI

Gemini CLI uses hierarchical instructional context:

- global context;
- workspace/project context;
- **just-in-time context files** discovered when a tool accesses a directory.

Gemini's Skills separately keep specialized workflows on demand rather than in general `GEMINI.md`. Gemini also documents subagents as specialists with independent context windows specifically to avoid cluttering the parent agent's context with noisy or specialized work.

This reinforces both **spatial routing** (path/locality) and **semantic routing** (Skill/subagent activation).

#### Kiro

Kiro Steering supports `always`, `auto`, `fileMatch`, and `manual` inclusion modes, while Skills/Powers package reusable specialized workflows. This is another current implementation of the same distinction between always-on context and context activated by relevance.

### 2.3 Established external discipline evidence

The AI-native evidence already determines the architecture. External disciplines add useful vocabulary rather than governing it.

#### Progressive disclosure

In human-computer interaction, progressive disclosure means presenting primary/high-frequency information first while deferring advanced or rarely needed detail until requested or relevant. The benefit is not simply "less information"; it is **reduced immediate complexity without removing access to deeper capability**.

That maps cleanly to agent context:

- universal rules remain visible;
- specialized rules remain discoverable;
- deeper content is disclosed when the task activates it.

#### Information scent / information foraging

Information-foraging research uses **information scent** for the cues that let a user estimate whether a deeper source is likely to satisfy the current information need before opening it.

This adds a useful design implication to A06: links, Skill descriptions, index entries, and routing metadata must be **specific enough to support correct selection**. A tiny map with vague labels such as `More`, `Guidance`, or `Reference` is not useful progressive disclosure because the agent cannot reliably decide what to load.

This supports **lean but navigable**, rather than merely lean.

### 2.4 Local synthesis

The convergent pattern is:

```text
active task / decision
      |
      v
small durable guidance + current task context
      |
      v
is deeper context needed to decide/act correctly?
      |
     no -----------------> continue
      |
     yes
      v
select the highest-signal scoped source
(path rule / source-of-truth file / Skill / tool / external source)
      |
      v
load only the needed depth
      |
      v
continue; deepen again only if a real information gap remains
```

The objective is **not minimum tokens**. The objective is **maximum decision usefulness per unit of active context while preserving enough information to act correctly**.

That is why the selected wording begins with **sufficient high-signal working context**.

## 3. Semantic contract

### MUST

- Maintain enough active context to interpret the task and execute it correctly; context economy must not remove load-bearing information.
- Keep always-loaded/root guidance limited to durable, broadly applicable information that materially changes behavior across many tasks.
- Prefer a compact **map/index/routing surface** over embedding full procedures, examples, histories, and references in the root contract.
- Load deeper information only when the active task, decision, file scope, workflow, or evidence gap makes it relevant.
- Prefer the **most specific sufficient source** over reading multiple broad sources that duplicate one another.
- Use scoped mechanisms when the runtime supports them:
  - nested/path-specific instructions for file/subsystem-local rules;
  - Skills for semantically triggered reusable procedures;
  - subagents or isolated tools for context-heavy specialist work when A04 justifies delegation;
  - retrieval/search for specific factual/source needs.
- Ensure routing metadata has enough information scent to let the agent predict why a deeper source is relevant before loading it.
- Deepen progressively: if a summary/index answers the active need, do not automatically read every linked reference; if it does not, retrieve the next necessary layer.
- In long-running work, use runtime-supported compaction, summaries, notes, or re-fetchable sources when accumulated history/tool output is no longer the best representation of current working state.
- Preserve task-critical decisions and constraints when compacting or summarizing; efficiency must not erase governing information.

### MUST NOT

- Treat "smallest context" as a license to skip needed repository instructions, requirements, architecture, evidence, or source material.
- Preload every potentially relevant document merely because the model has a large context window.
- Read an entire documentation tree before establishing which branch is relevant to the task.
- Auto-expand every `ref`, import, link, Skill, or nearby instruction file without an activation reason.
- Put detailed task-specific procedures into the always-loaded root contract merely to make them discoverable.
- Re-read or duplicate the same large material when a current compact representation already preserves what the active task needs.
- Use A06 to decide which factual source is authoritative; A08/A13/C02 own evidence authority and research depth.
- Use A06 to decide which instruction is current when sources conflict; A11 owns current-truth/authority resolution.
- Use A06 to decide whether a task should be delegated; A04 owns workflow/delegation decisions, though context isolation can be one factor.
- Use context minimization to reduce substantive rigor or completeness; A01 owns outcome adequacy.

### Activation condition

Always active as a context-selection invariant. On a trivial task its visible effect should be almost zero.

### Deepen condition

No dedicated A06 Skill/reference is required. The deeper content already exists in the runtime-specific mechanisms A06 is choosing among: scoped instructions, Skills, source files, tools, retrieval, subagents, and compaction/memory facilities.

## 4. Context-selection model

This is explanatory evaluation guidance, not an always-loaded checklist.

| Information class | Default treatment | Typical mechanism |
|---|---|---|
| Universal durable behavior | Keep compact and always visible | root `AGENTS.md` / equivalent |
| Repository-wide conventions | Persistent if broadly relevant | repo `AGENTS.md` / custom instructions |
| Directory/subsystem-specific rules | Load/apply only in matching scope | nested `AGENTS.md`, path instruction, JIT `GEMINI.md` |
| Reusable multi-step procedure | Discover cheaply; load when task matches | Agent Skill |
| Large reference corpus | Keep external; retrieve only relevant section | docs index/search/reference file |
| External/current facts | Retrieve when task requires grounding | web/MCP/research tools under A13/C02 |
| Noisy specialist analysis | Isolate when workflow benefit justifies it | subagent / separate context |
| Long-running accumulated history | Compact/summarize when supported and safe | compaction/current-state notes |
| Superseded or irrelevant detail | Do not actively re-load | historical record / archive |

The matrix intentionally separates **where information lives** from **when it enters active context**.

## 5. Neighboring-module boundaries

### A01 `<target>` — substantive adequacy

A06 controls what information is active, not how much substantive work is enough. A task must receive enough context to meet A01's intended outcome.

**Failure interaction:** "keep context small" must never become an excuse to skip a required specification or source file.

### A02 `<scope>` — authorization

A02 determines what work is authorized. A06 may retrieve context needed to understand that work, but reading a nearby document does not authorize implementation of adjacent work.

### A03 `<reuse>` — established capability

A03 can require checking an existing system or project asset. A06 decides how much of its documentation/implementation needs to be loaded to judge fit; it should not ingest the whole ecosystem by default.

### A04 `<workflow>` — planning/delegation

A04 decides whether subagents, decomposition, or reviews are worthwhile. A06 contributes a context-cost signal: a specialist subagent can protect the parent context from a noisy research stream, but A06 does not mandate delegation by itself.

### A05 `<intent>` — clarification

A05 says to resolve readily available ambiguity before asking. A06 bounds this search: use the highest-signal readily available sources, not an exhaustive repository/world scan for every minor uncertainty.

### A07 `<realization>` — hierarchical work

A07 may require Macro→Meso→Micro decomposition. A06 should load the context appropriate to the currently active level instead of loading every layer's full detail simultaneously.

### A08 `<evidence>` and A13 `<grounding>`

A06 governs **context selection/loading**. A08 governs evidence quality and uncertainty; A13 decides when real-world external grounding is mandatory. If A13 activates, authoritative external evidence becomes relevant context even if it was not initially local.

### A11 `<current_truth>`

A06 asks "what is relevant now?" A11 asks "which source is current/authoritative when versions conflict?" Do not merge these responsibilities.

### C02 `<research>`

A06 can trigger targeted retrieval; C02 owns a full research method when current/external/comparative evidence requires deeper investigation.

## 6. Failure modes this module exists to prevent

1. **Context bloat:** relevant task information is crowded by large generic instructions, references, conversation history, or tool output.
2. **Context starvation:** a minimalism rule causes the agent to skip load-bearing instructions or evidence.
3. **Monolithic manual failure:** everything is placed in one always-loaded file, making guidance noisy, stale, and hard to navigate.
4. **Large-window fallacy:** a 1M-token window is treated as justification to load everything.
5. **Auto-expansion cascade:** every link/ref recursively loads more material regardless of task relevance.
6. **Broad-scan reflex:** the agent reads the whole repo/document tree before identifying the likely branch.
7. **Weak routing metadata:** a compact map exists, but labels are too vague for the model to select the right next source.
8. **Repeated large reads:** already-processed raw material remains the working representation even when a compact state/summary would suffice.
9. **Stale context dominance:** old discussion or output remains cognitively salient after the active task has moved on; A11 resolves authority, A06 prevents unnecessary re-loading.
10. **Procedure leakage:** specialized workflows are copied into root instructions instead of remaining behind a Skill or scoped trigger.
11. **Tool-context pollution:** huge tool results accumulate in the main agent when only a small extracted result is needed.
12. **Context isolation misuse:** subagents are spawned solely to hide context even when coordination cost exceeds the benefit; A04 must still justify delegation.

## 7. Wording alternatives

### Candidate A — current pilot

```xml
<context principles="context-engineering,progressive-disclosure,JIT-retrieval">
  Keep active context to the smallest high-signal set. Read deeper references only when they are relevant to the active task.
</context>
```

**Strengths:** compact; recognizes high signal and progressive disclosure.

**Weaknesses:**

- `smallest` can become context starvation / artificial minimalism;
- `references` is too narrow: relevant context can be instructions, source files, Skills, tools, external evidence, or current state;
- it does not distinguish persistent guidance from task-specific working context;
- `relevant to the active task` can be interpreted too broadly and still justify loading an entire project corpus.

**Decision:** reject as final wording.

### Candidate B — hard context budget

```xml
<context principles="context-budgeting,progressive-disclosure">
  Keep persistent instructions below a fixed token budget and load all other context on demand.
</context>
```

**Why rejected:** OpenAI's 2% budget is specifically for the Codex Skills discovery list, not a universal AGENTS/context budget. Fixed numerical limits vary by runtime, model, and task and would turn current implementation detail into fake universality.

### Candidate C — repository-map only

```xml
<context principles="map-not-manual,progressive-disclosure">
  Use the root instruction file as a small map to deeper repository sources and read the needed source when a task reaches it.
</context>
```

**Why rejected:** excellent Codex/repository pattern but too narrow for non-repository work, ChatGPT Work, external research, Skills, files, and tool-heavy workflows.

### Candidate D — selected

```xml
<context principles="context-engineering,progressive-disclosure,JIT-retrieval">
  Maintain a sufficient high-signal working context. Keep always-loaded guidance lean and navigable; load deeper instructions, sources, files, skills, or tools just in time for the specific decision or work step that needs them, rather than bulk-loading available context upfront.
</context>
```

**Why selected:** preserves the strongest OpenAI production finding while generalizing it across agent runtimes; explicitly protects against both context bloat and context starvation; keeps persistent guidance and task-specific context distinct; remains self-sufficient without requiring a procedure.

## 8. Scenario simulations

### S1 — simple / negative case

**Input:** "Change this sentence from passive to active voice."

**Current-pilot risk:** usually fine, but a literal "read deeper references when relevant" interpretation could still cause unnecessary style/profile loading if references are nearby.

**Selected behavior:** use the supplied sentence and directly applicable standing style instructions only. Do not scan project documentation.

**Observable success:** immediate correct rewrite; no unrelated retrieval.

**Deep guidance:** none.

### S2 — clear positive case: repository feature

**Input:** "Add retry behavior to the payments client using our existing pattern."

Repository contains:

- short root `AGENTS.md` pointing to architecture/index material;
- a payments-local instruction file;
- a retry implementation in a sibling client;
- many unrelated design docs.

**Selected behavior:** read the root map, relevant local instruction, referenced retry pattern, and files needed for implementation. Do not preload all architecture/design docs.

**Observable success:** enough context to preserve the established pattern without a repository-wide reading phase.

### S3 — progressive Skill activation

**Input:** "Fill this PDF form."

A PDF Skill exists with metadata, `SKILL.md`, `FORMS.md`, and unrelated OCR guidance.

**Selected behavior:** discovery metadata identifies the PDF Skill; load `SKILL.md`; read `FORMS.md` because form filling needs it; do not load OCR material unless the document actually requires OCR.

**Observable success:** correct workflow with staged context loading.

### S4 — large-window fallacy

**Input:** "Review this 150-file subsystem. We have a million-token context window, so read the whole repository first."

**Selected behavior:** user explicitly requested the subsystem review, not indiscriminate full-repo ingestion. Start from maps/indexes and relevant subsystem paths, broaden only when dependencies/evidence require it. A large window permits breadth when useful but does not make irrelevant context helpful.

**Observable success:** review covers dependencies that matter without bulk-loading unrelated domains.

### S5 — ambiguity and A05 interaction

**Input:** "Use the same deployment pattern as last time." The prior deployment decision is recorded in a known current project file; many archived deployment documents also exist.

**Selected behavior:** inspect the current high-signal project record first. If it resolves the pattern, proceed. Do not ask immediately and do not inspect every archived deployment discussion.

**Observable success:** A05 receives enough evidence without A06 becoming an exhaustive search mandate.

### S6 — conflict / current-truth boundary

**Input:** root guidance links to two versions of a specification with contradictory requirements.

**Selected behavior:** A06 can identify both as relevant but must not invent precedence from proximity or file size. Route authority/currentness to A11; load only enough evidence to resolve which source governs.

**Observable success:** relevant context is retrieved without silently treating all loaded context as equally authoritative.

### S7 — long-running tool-heavy task

**Input:** a multi-hour analysis repeatedly retrieves large logs and source files.

**Selected behavior:** where the runtime supports it, preserve a compact task state/decision record and clear/compact old re-fetchable tool output rather than carrying every raw result indefinitely. Re-fetch exact details if later needed.

**Observable success:** current goals, constraints, key findings, and open issues remain available while raw noise stops dominating the working set.

### S8 — known failure: one giant instruction manual

**Input:** repository root contains a 1,000-line instruction file covering every subsystem, historical incident, workflow, and optional tool.

**Selected behavior:** in evaluation/design, flag this as a context-architecture problem: preserve universal rules and a navigable map at root; route subsystem/procedure/history detail into scoped current sources. Do not merely shorten prose while leaving all concepts always loaded.

**Observable success:** lower always-on context with no loss of discoverability.

### S9 — XML vs Markdown control

Run S2, S3, S5, and S8 with the selected XML and equivalent Markdown rule.

**Expected:** no meaningful semantic difference. The representation is not the mechanism; routing, relevance, and progressive disclosure are.

## 9. Deeper-owner decision

**Selected: no deeper artifact.**

A dedicated A06 Skill would be conceptually backwards: A06 is the universal rule that decides **when deeper artifacts should enter context**. Making that rule itself dependent on optional Skill activation would weaken the invariant.

A separate reference is also unnecessary now because:

- the root rule is self-sufficient;
- the detailed examples/failure modes live in this module result for evaluation;
- runtime-specific mechanisms already have their own authoritative documentation;
- A06 should not become a custom context-management framework that competes with native Skills, scoped instructions, subagents, retrieval, or compaction.

If later cross-agent evaluation shows a repeatable context-audit task is valuable (for example, auditing an existing repository's instruction architecture for bloat), that can become a **separate task-specific Skill**. It should not be the deeper owner of universal A06.

## 10. Important uncertainty / evaluation targets

### 10.1 "Sufficient" must beat both extremes

The most important evaluation question is whether agents correctly distinguish:

- **context bloat**: loading information with weak marginal relevance;
- **context starvation**: failing to load a specification/source because the rule over-rewards brevity.

Paired evals should hold task size constant while changing whether one deeper source contains a load-bearing constraint.

### 10.2 Routing quality matters as much as token count

A tiny root map with vague links can perform worse than a slightly larger map with strong information scent. Evaluate whether the agent chooses the right deeper source from names/descriptions alone.

### 10.3 Native runtime behavior differs

- OpenAI, Anthropic, GitHub, Gemini, Kiro, Cursor, and Windsurf differ in exactly when scoped rules or Skills are injected.
- Some runtimes support compaction/context editing directly; others do not.
- Some hosts expose a million-token window; others use smaller effective windows.

Therefore A06 should specify **behavioral intent**, not hard-coded token thresholds or one vendor's loading semantics.

### 10.4 Large context windows remain useful

The conclusion is not "long context is bad." Large context is valuable when the task genuinely depends on broad material. The rule is to load breadth because it improves the decision/outcome, not because capacity exists.

## 11. Sources

Primary/authoritative sources checked 2026-09-07.

### Current OpenAI / ChatGPT / Codex — primary layer

1. OpenAI — Harness engineering: leveraging Codex in an agent-first world (2026-02-11)  
   https://openai.com/index/harness-engineering/
2. ChatGPT Learn — Customization overview (current; `AGENTS.md` small, routing guidance, Skills)  
   https://learn.chatgpt.com/docs/customization/overview
3. ChatGPT Learn — Build Skills (current progressive-disclosure mechanics and Skills-list context budget)  
   https://learn.chatgpt.com/docs/build-skills
4. OpenAI API — Model guidance (current model behavior and sensitivity to loaded Skills/instructions)  
   https://developers.openai.com/api/docs/guides/latest-model
5. OpenAI — How OpenAI uses Codex (persistent context + relevant issue-shaped prompt context)  
   https://openai.com/business/guides-and-resources/how-openai-uses-codex/

### Independent mature-agent systems

6. Anthropic — Agent Skills overview (progressive disclosure)  
   https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
7. Anthropic — Skill authoring best practices (context window as shared/public resource)  
   https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
8. Anthropic — Context windows / context rot  
   https://platform.claude.com/docs/en/build-with-claude/context-windows
9. Anthropic — Context editing / compaction guidance  
   https://platform.claude.com/docs/en/build-with-claude/context-editing  
   https://platform.claude.com/docs/en/build-with-claude/compaction
10. Anthropic Cookbook — Context engineering: memory, compaction, and tool clearing (2026-03-20)  
    https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools
11. GitHub — About Copilot code review / custom instructions vs path rules vs `AGENTS.md` vs Skills  
    https://docs.github.com/en/copilot/concepts/agents/code-review
12. GitHub — Adding Agent Skills for Copilot  
    https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills
13. GitHub — Adding repository custom instructions  
    https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions
14. Gemini CLI — `GEMINI.md` hierarchical and JIT context  
    https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/gemini-md.md
15. Gemini CLI — Agent Skills (on-demand expertise)  
    https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/skills.md
16. Gemini CLI — Subagents (independent context windows)  
    https://github.com/google-gemini/gemini-cli/blob/main/docs/core/subagents.md
17. Kiro — Powers / Steering inclusion modes (updated 2026-09-02)  
    https://kiro.dev/docs/powers/

### Established external discipline

18. Nielsen Norman Group — Progressive Disclosure  
    https://www.nngroup.com/articles/progressive-disclosure/
19. Nielsen Norman Group — Information Scent: How Users Decide Where to Go Next  
    https://www.nngroup.com/articles/information-scent/

## 12. Evidence confidence

- **Very high confidence:** the current pilot needs to replace `smallest` with a sufficiency-oriented formulation. OpenAI and Anthropic independently show that both context overload and missing context are real failure modes.
- **Very high confidence:** persistent guidance should remain lean and deeper procedures should use progressive disclosure/JIT activation. This is implemented directly by OpenAI, Anthropic, GitHub, Gemini, and Kiro.
- **High confidence:** a map/index needs strong routing metadata; mere shortness is not sufficient.
- **High confidence:** no dedicated A06 Skill/reference is justified.
- **Moderate-high confidence:** the exact selected sentence is compact enough for the root constitution; later cross-agent eval should test whether listing `instructions, sources, files, skills, or tools` materially improves routing or can be shortened without losing behavior.
- **Moderate confidence:** runtime-supported compaction belongs in the deeper semantic contract but not in the root sentence because implementation support varies.

## 13. Final recommendation

Keep A06 as an always-on **context-selection invariant**, but change its center of gravity from **minimum context** to **sufficient, high-signal, progressively disclosed context**.

The durable operating model is:

```text
lean persistent map
  -> specific current task
  -> retrieve/activate the next needed context layer
  -> stop deepening when the active decision is sufficiently informed
```

This is directly aligned with current OpenAI production experience and current Skills architecture, independently reproduced by Anthropic, GitHub Copilot, Gemini CLI, and Kiro. It also preserves the user's anti-minimalism requirement: context should be economical because irrelevant context can harm focus, **not** because fewer tokens are an end in themselves.
