---
type: ModuleDeepeningResult
title: A11 Current-Truth / Authoritative-State Discipline
description: AI-native-first deepening result for the universal <current_truth> module, resolving overlapping guidance by explicit authority and scope, keeping live state synchronized, and separating superseded history from active instructions.
status: DONE
updated: 2026-09-07
---

# A11 — Current-Truth / Authoritative-State Discipline

## 1. Final decision

- **Module:** A11
- **XML tag:** `<current_truth>`
- **Semantic purpose:** Prevent agents from treating stale plans, superseded decisions, historical explanations, duplicated instructions, or conflicting scoped guidance as equally active. Establish which live source governs a fact/decision at the applicable scope, preserve deterministic precedence, and keep downstream representations synchronized or visibly stale.
- **Selected deeper owner:** **No deeper artifact**
- **Selected principles:** canonical current state; scope-aware precedence; consistency; history separation; configuration status discipline.
- **Key correction to the pilot:** replace the mainly editorial rule **“keep live guidance focused on the active state”** with an explicit **authority + precedence + synchronization** invariant.
- **Terminology correction:** `single-source-of-truth` is useful shorthand but should not imply one monolithic file. Mature agent systems deliberately layer global, project, path-local, and task-specific sources. The universal requirement is **one authoritative current answer per governed fact/decision at a given scope**, with deterministic precedence when layers overlap.
- **Primary AI-native anchor:** OpenAI’s production Codex harness uses a structured repository knowledge base as the system of record, mechanically checks documentation freshness, and uses a short `AGENTS.md` only as a map. Current Codex `AGENTS.md` documentation separately defines explicit scope/override precedence and mechanisms to audit stale or wrong guidance.
- **Strong final-synthesis interaction:** A11 overlaps A06 on routing and A08 on source quality, but remains distinct for now because it answers a different question: **which already-present project/instruction state is active and governing?**

### Final root XML

```xml
<current_truth principles="canonical-current-state,scope-aware-precedence,consistency,history-separation">
  Use the authoritative current source for each governed fact or decision. When active sources overlap, follow explicit precedence and the most specific applicable scope; do not synthesize contradictory guidance. Update or flag stale dependents, and keep superseded states as history rather than competing instructions.
</current_truth>
```

### Equivalent compact Markdown control

```markdown
**Current truth — canonical state / scope-aware precedence / consistency:** Use the authoritative current source for each governed fact or decision. When active sources overlap, follow explicit precedence and the most specific applicable scope; do not synthesize contradictory guidance. Update or flag stale dependents, and keep superseded states as history rather than competing instructions.
```

## 2. Why this is the right method

### 2.1 Current OpenAI / ChatGPT / Codex evidence

A11 has strong direct AI-native support. The strongest current evidence does not recommend one giant canonical document; it recommends **structured sources of truth plus explicit routing, precedence, freshness checks, and versioned history**.

#### OpenAI Harness Engineering: repository knowledge is a system of record, not a giant prompt

OpenAI’s 2026 Harness Engineering report describes a production Codex repository where a large monolithic `AGENTS.md` failed. The replacement architecture is:

```text
short AGENTS.md map
  -> structured docs/ knowledge base
  -> indexed deeper sources of truth
  -> versioned plans / decisions / architecture
  -> mechanical freshness and cross-link validation
```

OpenAI explicitly describes the structured `docs/` directory as the **system of record**. Active plans, completed plans, design documents, product specs, reliability/security material, and generated references remain distinct artifacts rather than being copied into one mega-document.

The report also describes dedicated linters/CI and a recurring **doc-gardening agent** that scans for stale or obsolete documentation that no longer reflects real code behavior and opens fixes.

This yields three direct A11 requirements:

1. current truth may be **distributed by responsibility**, not centralized in one file;
2. each responsibility needs a clear governing source and route;
3. stale/superseded representations must not remain silently competitive with live state.

Primary source:
- OpenAI — Harness engineering: leveraging Codex in an agent-first world  
  https://openai.com/index/harness-engineering/

#### Codex `AGENTS.md`: precedence is an explicit runtime concept

Current Codex documentation defines a deterministic instruction chain:

- global `AGENTS.override.md` or `AGENTS.md`;
- project-root instructions;
- nested directory instructions down to the working directory;
- files closer to the active directory appear later and override broader guidance;
- `AGENTS.override.md` takes precedence over `AGENTS.md` at the same level;
- only one applicable instruction file is selected per directory from the configured search order.

Codex also provides explicit diagnostic procedures:

- ask Codex to list/summarize active instruction sources;
- inspect session logs;
- check for unexpected overrides when wrong guidance appears;
- restart/reload when instructions look stale so the chain is rebuilt from live files.

The universal lesson is not “all agents use the same precedence order.” They do not. The lesson is:

> **when the runtime or project defines an authority/precedence chain, honor that chain rather than blending contradictory instructions.**

Primary source:
- OpenAI / ChatGPT Learn — Custom instructions with `AGENTS.md`  
  https://learn.chatgpt.com/docs/agent-configuration/agents-md

#### Current ChatGPT prompting guidance: explicitly use the latest project state

Current ChatGPT prompting guidance gives a project-status example that instructs the system to use the **latest project plan** plus relevant decisions/updates from connected sources. The same example tells ChatGPT to flag conflicting or missing information rather than silently reconciling it.

That supports two A11 behaviors:

```text
current source available -> prefer current state
conflict remains          -> expose conflict, do not manufacture consensus
```

The Codex workflow guidance also says that if a human reverts or changes an edit, tell Codex so it does not overwrite the newer human state while continuing work. This is a concrete current-state ownership problem: the agent’s remembered prior edit is not authoritative once the live worktree changed.

Primary source:
- ChatGPT Learn — Prompting  
  https://learn.chatgpt.com/docs/prompting

#### OpenAI architecture implication: source-of-truth is a routing contract

Combining the current OpenAI patterns gives a stronger definition of “source of truth” for agents:

```text
not:
  one enormous file containing every true thing

but:
  explicit owners for distinct state
  + deterministic precedence where scopes overlap
  + live-state retrieval
  + synchronized downstream representations
  + historical states retained outside the active path
```

That is the model A11 should encode.

### 2.2 Independent mature-agent convergence

The same pattern appears independently across Claude Code, GitHub Copilot, Gemini CLI, and Kiro.

#### Anthropic Claude Code: layered instructions + conflict risk + shared source reuse

Current Claude Code documentation defines multiple instruction scopes:

- managed organization policy;
- user instructions;
- project `CLAUDE.md`;
- personal project `CLAUDE.local.md`;
- directory/path-specific rules;
- task-specific Skills.

Claude loads applicable instructions into context rather than treating every source as an independently enforced configuration object.

Anthropic explicitly warns that if two `CLAUDE.md` sources conflict, Claude may choose one **arbitrarily**. The recommended operational response is therefore to avoid conflicting duplication and inspect what is actually loaded.

The documentation also gives an important canonicalization pattern: when a repository already uses `AGENTS.md`, Claude can import that file from a tiny `CLAUDE.md` rather than independently maintaining equivalent duplicated guidance. This avoids semantic drift between cross-agent instruction surfaces.

Portable lesson:

```text
shared semantic owner exists
  -> reference/import it when the runtime permits
  -> add only runtime-specific deltas locally
  -> do not independently rewrite equivalent shared policy in every client file
```

Primary sources:
- Anthropic — How Claude remembers your project  
  https://code.claude.com/docs/en/memory
- Anthropic — Steering Claude Code: when to use CLAUDE.md, skills, hooks, and subagents  
  https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more

#### GitHub Copilot: explicit precedence and scope-specific sources

Current GitHub Copilot documentation distinguishes:

- personal instructions;
- repository-wide instructions;
- path-specific repository instructions;
- `AGENTS.md`/agent instructions;
- organization instructions.

GitHub documents an explicit precedence order. Within repository instructions, applicable path-specific instructions outrank repository-wide instructions, which outrank agent instructions for supported surfaces; personal instructions rank above repository instructions, and organization instructions below them.

GitHub also explicitly says to avoid conflicting instruction sets where possible.

The important universal behavior is again not GitHub’s exact priority ordering; it is:

- scope is part of authority;
- overlapping sources need deterministic precedence;
- duplicate conflicting statements degrade reliability.

Primary sources:
- GitHub — About customizing GitHub Copilot responses  
  https://docs.github.com/en/copilot/concepts/prompting/response-customization
- GitHub — Adding repository custom instructions  
  https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions

#### Gemini CLI: hierarchical current context is inspectable and reloadable

Gemini CLI uses hierarchical context files:

- global context;
- workspace/project context;
- just-in-time local context discovered when tools access a directory.

The `/memory show` command exposes the exact concatenated instructional context; `/memory reload` / `/memory refresh` re-scans the live files and updates the model with their latest content.

Gemini’s current memory documentation additionally says durable facts should be routed to the **appropriate** Markdown file and that the system should avoid duplicating the same fact across multiple memory tiers.

This independently supports:

- scope-aware ownership;
- inspectable active state;
- reload from live sources when state changes;
- avoid duplicated copies of one governed fact.

Primary sources:
- Google Gemini CLI — Provide context with `GEMINI.md` files  
  https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/gemini-md.md
- Google Gemini CLI — Memory files  
  https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/memory.md

#### Kiro: source-of-truth artifacts + downstream regeneration

Kiro’s current spec architecture supplies particularly strong evidence for **synchronization rather than duplication**.

Kiro’s specs use separate artifacts such as:

```text
requirements.md
  -> design.md
  -> tasks.md
  -> implementation
```

Kiro explicitly says spec artifacts are used as the **source of truth during implementation**. When an upstream artifact changes, Kiro regenerates only the affected downstream artifacts:

- change tasks -> tasks only;
- change design -> design + tasks;
- change scope/requirements -> regenerate affected downstream artifacts.

Current Kiro docs also describe continuous refinement specifically to keep specs synchronized with changing requirements and technical design.

This is strong evidence for a vital A11 principle:

> **when canonical state changes, dependent representations must be updated or visibly marked stale; old copies must not continue as silent active alternatives.**

Primary sources:
- Kiro — Specs just got faster (and smarter)  
  https://kiro.dev/blog/faster-smarter-specs/
- Kiro — Requirements-First workflow  
  https://kiro.dev/docs/specs/feature-specs/requirements-first/
- Kiro — Specs best practices  
  https://kiro.dev/docs/specs/best-practices/

### 2.3 Established external discipline evidence

The AI-native evidence already defines A11’s behavior. Configuration management adds durable vocabulary and lifecycle discipline.

#### Configuration management: current baseline + controlled history

Modern configuration-management practice distinguishes:

- the **current approved baseline** used for ongoing work;
- controlled changes to that baseline;
- status accounting that exposes what version/state is current;
- retained historical configurations and change rationale.

NASA’s current systems-engineering guidance says configuration management provides a true representation of the product, keeps product information consistent with the product, distinguishes versions, and maintains both current and historical configuration documentation.

NIST configuration-management requirements similarly call for a **current baseline configuration** that is maintained under configuration control and updated when the system changes.

These disciplines reinforce a useful A11 distinction:

```text
history is valuable
but
history is not current authority
```

Secondary sources:
- NASA — 6.5 Configuration Management  
  https://www.nasa.gov/reference/6-5-configuration-management/
- NIST SP 800-171 Rev. 3 — Baseline Configuration  
  https://nvlpubs.nist.gov/nistpubs/SpecialPublications/800-171r3/NIST.SP.800-171r3.html

### 2.4 Local synthesis

The convergent current-truth model is:

```text
question / governed fact / decision
        |
        v
which source owns this kind of state?
        |
        v
which scope applies here?
        |
        v
is there an explicit runtime/project precedence rule?
        |
        +--> yes -> follow it
        |
        +--> no  -> prefer the designated canonical owner;
                   if unresolved, expose the conflict
        |
        v
read the live/current representation
        |
        v
if canonical state changed:
  update or flag dependent copies
  preserve prior state in history/change records
        |
        v
do not allow historical/superseded copies to compete as active instructions
```

The core invariant is:

```text
one governed fact/decision + one scope -> one authoritative current answer
```

This does **not** require one repository-wide truth file. Different state classes can have different owners.

## 3. Semantic contract

### MUST

- Identify the authoritative current owner for a governed project fact, decision, requirement, configuration, instruction, or plan when the task depends on it.
- Treat **scope** as part of authority. A path/subsystem-specific rule can legitimately override a broader project default when the runtime/project defines that relationship.
- Follow explicit precedence/override rules supplied by the runtime, repository, project, or operator.
- Prefer the **live current representation** over remembered prior state, an earlier chat summary, a superseded plan, an old diff, or historical documentation.
- Re-read live sources when concurrent changes, long-running work, rebases, human edits, or stale-session risk could materially change the answer or mutation target.
- Keep one authoritative current answer for the same governed fact/decision at the same scope; use references/imports/routes instead of maintaining independent semantic duplicates where practical.
- When canonical state changes, update dependent current artifacts that claim to reflect it, or explicitly mark them stale/pending regeneration.
- Preserve useful history, rationale, previous baselines, and incident records in historical/change-log surfaces rather than deleting them merely because they are no longer current.
- Distinguish **current authority** from **historical evidence**. Older material can explain why a decision changed without governing current execution.
- Expose unresolved conflicts when no applicable precedence or designated owner resolves them; do not invent a hybrid rule.
- When a runtime offers inspection/reload mechanisms for active instructions, use them when instruction-source confusion materially affects the task.

### MUST NOT

- Treat every document mentioning a topic as equally authoritative.
- Infer that the newest timestamp alone always wins; explicit authority/scope can outrank recency.
- Infer that the most specific file always wins unless the runtime/project defines specificity as precedence or the canonical owner delegates that scope.
- Merge contradictory instructions into an improvised compromise merely to avoid reporting a conflict.
- Continue using remembered state after observing that a human, tool, branch, or upstream source changed the live artifact.
- Keep multiple active copies of the same shared policy merely for convenience when one canonical owner plus runtime-specific deltas would suffice.
- Delete history solely to keep the active view clean; move/archive/version it appropriately.
- Let an old plan, completed handover, archived design, prior chat, generated summary, or stale local checkout override an explicitly current live source.
- Use A11 to decide whether an external factual claim is well-supported; A08 owns claim/evidence integrity.
- Use A11 to trigger web research for current real-world facts; A13/C02 own external grounding/research.
- Use A11 to decide how much context to load; A06 owns context selection/progressive disclosure.
- Treat `single-source-of-truth` as a mandate to centralize unrelated state into one giant file.

### Activation condition

Always available as an authority/current-state invariant, but its visible effect activates when:

- multiple candidate sources exist;
- a task spans versioned plans/specs/docs/code;
- concurrent changes may have landed;
- the agent is continuing old work;
- an instruction hierarchy is present;
- an upstream canonical artifact changed;
- a historical artifact might be mistaken for current guidance.

For a simple one-shot task with one obvious live source, A11 adds almost no ceremony.

### Deepen condition

**No dedicated A11 Skill/reference.**

Reason:

- authority rules are repository/runtime-specific and should live with the relevant source hierarchy;
- Codex/Claude/Gemini/Copilot already expose their own precedence and inspection mechanisms;
- Informatics/current-state lifecycle details belong to C03 when that domain triggers;
- a generic A11 procedure would duplicate these systems and risk becoming stale itself.

The root semantic rule is sufficient to tell the agent what invariant to preserve.

## 4. Authority model

This is explanatory evaluation guidance, not an always-loaded checklist.

### 4.1 Authority is multidimensional

A useful decision model is:

| Dimension | Question |
|---|---|
| **Declared owner** | Which artifact/system is designated to govern this state? |
| **Instruction level** | Is there a higher-level system/developer/operator authority? |
| **Scope** | Is this rule global, project-wide, subsystem/path-specific, or task-specific? |
| **Explicit precedence** | Does the runtime/project define an override order? |
| **Currentness** | Is this the live state or an old snapshot/history? |
| **Applicability** | Does the source actually govern this object/version/environment? |

Do not collapse all six dimensions into “newest file wins.”

### 4.2 Example: layered agent instructions

```text
organization/default
      |
project rule
      |
path-local rule
      |
task-specific instruction
```

If the runtime defines the lower/more-specific scope as an override, use it for that scope while preserving the broader rule elsewhere.

### 4.3 Example: product/spec state

```text
requirements.md (owns requirement)
      |
      +-> design.md (derived architecture)
             |
             +-> tasks.md (derived execution plan)
```

If a requirement changes, `design.md` / `tasks.md` must be regenerated or explicitly marked stale where affected. The old task list does not remain equally authoritative because it has a later timestamp than some unrelated source.

### 4.4 Example: history

```text
Current Truth
  status = A11 NEXT

History
  A10 was NEXT before A10 completed
```

Both statements can be historically accurate. Only one governs current execution.

## 5. Interaction with neighboring modules

### A06 `<context>`

- **A06:** which information should enter active context and when?
- **A11:** which loaded/current source governs when candidates overlap?

A06 may route to a file. A11 decides whether that file is current/authoritative for the state being used.

### A08 `<evidence>`

- **A08:** what does evidence justify claiming?
- **A11:** which project/instruction/configuration state is active and authoritative?

A historical decision can be excellent evidence about past reasoning while still not governing current execution.

### A10 `<recovery>`

After failures or uncertain side effects, A10 may require state inspection before retry. A11 ensures that inspection uses the live current state rather than the agent’s pre-failure assumption.

### A13 `<grounding>`

- **A13:** when must external reality/current sources be checked?
- **A11:** once multiple internal/current project sources exist, which one governs this project state?

### C03 `<informatics>`

C03 may define canonical metadata, index, archive, migration, or lifecycle rules for formal repository knowledge. A11 supplies the universal invariant that the current owner and superseded history must not compete.

### A07 `<realization>`

A07 keeps parent/child realization traceable. A11 complements it by requiring downstream representations to be synchronized or marked stale when a parent canonical artifact changes.

## 6. Wording alternatives evaluated

### Candidate A — current pilot

```xml
<current_truth principles="single-source-of-truth,current-state">
  Keep live guidance focused on the active state. Put superseded rationale, incident history, and changelogs in their proper historical records.
</current_truth>
```

**Strength:** compact and correctly separates active state from history.

**Weakness:** does not say how to choose among multiple active sources, does not encode precedence/scope, and can be misread as “one file must contain everything.”

**Verdict:** insufficient.

### Candidate B — canonical owner only

```xml
<current_truth principles="canonical-source,current-state">
  Use the designated canonical source for current state; treat other representations as derived or historical and keep them synchronized.
</current_truth>
```

**Strength:** very compact; strong anti-duplication behavior.

**Weakness:** too rigid for layered instruction systems where scoped overrides are legitimate and intentionally authoritative within a narrower domain.

**Verdict:** rejected.

### Candidate C — precedence-only

```xml
<current_truth principles="precedence,current-state">
  When sources conflict, follow the applicable authority and most specific current source rather than blending them.
</current_truth>
```

**Strength:** directly solves conflict.

**Weakness:** omits synchronization, history separation, and canonical ownership; “most specific” is unsafe if no project/runtime rule grants it precedence.

**Verdict:** rejected.

### Candidate D — selected

```xml
<current_truth principles="canonical-current-state,scope-aware-precedence,consistency,history-separation">
  Use the authoritative current source for each governed fact or decision. When active sources overlap, follow explicit precedence and the most specific applicable scope; do not synthesize contradictory guidance. Update or flag stale dependents, and keep superseded states as history rather than competing instructions.
</current_truth>
```

**Strengths:**

- does not require one monolithic SSOT file;
- supports layered agent instruction hierarchies;
- handles conflicts deterministically;
- protects against stale derived artifacts;
- preserves useful history;
- stays distinct from A06/A08/A13.

**Cost:** longer than Candidate A, but the added semantics address concrete current-agent failure modes.

**Verdict:** selected for pilot evaluation.

## 7. Scenario simulations

### S1 — simple / negative case: one obvious source

**Input:** “Change the typo in `README.md`.” One current file exists; no conflicting guidance.

**Current-pilot expected behavior:** edit the file; A11 has little visible effect.

**Selected-candidate behavior:** same. No authority audit ceremony is added because there is no ambiguity.

**Success:** no unnecessary source-of-truth process.

**Deep guidance:** no.

### S2 — current README vs old handover

**Input:** live program README says A11 is `NEXT`; an older handover says A08 is `NEXT`.

**Current-pilot risk:** “active state” hints at the README but does not explicitly resolve the conflict.

**Selected-candidate behavior:** use the live README because the program explicitly designates it as current truth; treat the handover snapshot as historical/background where inconsistent.

**Success:** execute A11 only.

### S3 — scoped override

**Input:** root instruction says `npm test`; `services/payments/AGENTS.override.md` says `make test-payments` for that service.

**Selected-candidate behavior:** follow the runtime’s explicit nested override precedence inside the payments scope; do not rewrite the global rule.

**Success:** correct command only in scoped work.

### S4 — conflict without declared precedence

**Input:** two peer design docs both claim to be the current architecture and materially disagree; neither is designated canonical.

**Selected-candidate behavior:** surface the unresolved authority conflict instead of averaging the designs or arbitrarily selecting one by timestamp.

**Success:** no fabricated hybrid architecture.

### S5 — human changed agent output

**Input:** agent edited a function; human reverted/changed it before the next instruction.

**Selected-candidate behavior:** re-read the live file and treat it as current. Do not restore the agent’s previous version simply because it remains in chat history.

**Success:** human current state is preserved.

### S6 — upstream spec changed

**Input:** `requirements.md` changes after `design.md` and `tasks.md` were generated.

**Selected-candidate behavior:** treat requirements as the owner of the changed requirement and regenerate/update or mark affected downstream artifacts stale; do not execute stale tasks as if still current.

**Success:** downstream state no longer silently contradicts canonical upstream state.

### S7 — historical rationale remains useful

**Input:** current architecture is v3; an archived v2 ADR explains why a technology was rejected.

**Selected-candidate behavior:** current v3 governs implementation. The v2 ADR may still be consulted as historical rationale if relevant, but it does not override v3.

**Success:** history preserved without authority confusion.

### S8 — newest timestamp is not authority

**Input:** a yesterday-created scratch note contradicts the canonical design doc updated last week.

**Selected-candidate behavior:** canonical ownership beats raw timestamp unless project rules say otherwise; note the contradiction if material.

**Success:** no “newest file wins” heuristic.

### S9 — duplicated cross-client rules drift

**Input:** `AGENTS.md` and `CLAUDE.md` independently contain the same policy but one was updated and the other was not.

**Selected-candidate behavior:** prefer the designated shared semantic owner; recommend/import/reference it where supported and retain only runtime-specific deltas in the client file. Until fixed, expose the discrepancy rather than silently choosing a blended policy.

**Success:** semantic duplication is reduced or visibly flagged.

### S10 — concurrent GitHub changes

**Input:** agent researched a module while another commit landed on `main`.

**Selected-candidate behavior:** re-read live `main`, replay only the bounded intended change onto the new head, and preserve concurrent work.

**Success:** no stale whole-file overwrite.

### S11 — XML vs Markdown control

**Input:** same conflict scenario under selected XML wording and equivalent Markdown wording.

**Expected:** both identify authority/scope, refuse contradictory synthesis, and preserve history.

**Success:** no behavior advantage is assumed merely from XML syntax; later cross-agent eval decides representation.

### S12 — false SSOT centralization

**Input:** agent proposes copying every project rule, architecture detail, current status, and procedure into one `CURRENT_TRUTH.md` to satisfy “single source of truth.”

**Selected-candidate behavior:** reject the centralization. Maintain distinct authoritative owners by responsibility and use routing/indexes/precedence to make them discoverable.

**Success:** no monolithic context/source-of-truth anti-pattern.

## 8. Failure modes A11 exists to prevent

### F1 — stale-state execution

Agent executes an old plan or remembered file content after live state changed.

### F2 — source averaging

Agent blends contradictory active instructions into a plausible compromise that no authority approved.

### F3 — timestamp authority fallacy

Agent assumes newest document automatically governs despite an explicit canonical owner.

### F4 — monolithic SSOT fallacy

Agent centralizes unrelated state into one huge file, creating bloat and new drift risk.

### F5 — duplicated-policy drift

Equivalent rules are independently maintained across `AGENTS.md`, `CLAUDE.md`, Gemini/Kiro/Cursor/Windsurf files and diverge.

### F6 — derived-artifact staleness

Requirements/design changes but old tasks/docs continue to look active.

### F7 — history contamination

Archived incidents/rationale/changelogs are treated as current operating instructions.

### F8 — specificity without authority

Agent assumes a local note overrides a canonical project rule merely because the local file is more specific.

### F9 — authority without applicability

Agent uses a formally canonical document for a different version/environment/subsystem.

### F10 — chat-memory overwrite

Agent restores a previous model-generated state after a human changed the live source.

## 9. Deeper-owner decision

### Options

| Owner | Fit | Decision |
|---|---|---|
| No deeper artifact | strong | **SELECTED** |
| Focused reference | moderate | reject; would duplicate runtime/repo-specific precedence rules |
| Scoped rule | poor | A11 itself is universal; concrete authority rules can already be scoped locally |
| Agent Skill | poor | no reusable universal multi-step procedure is justified |

### Why no deeper artifact wins

A11 is primarily an invariant:

```text
current authoritative owner
+ applicable scope / precedence
+ synchronized dependents
+ history separated from active state
```

The detailed mechanics already belong to the systems that own them:

- Codex instruction discovery/precedence;
- Claude project/rule loading;
- Copilot instruction precedence;
- Gemini hierarchical context/reload;
- Kiro spec synchronization;
- Git/version-control workflows;
- repository-specific Informatics/source-of-truth conventions.

Creating a generic Current Truth Skill would create another policy source that itself could drift from those runtime-specific mechanisms.

## 10. Final-synthesis questions

A11 should remain in the pilot, but final synthesis should test:

1. **A06 + A11 merge:** can one compact context/source-authority rule preserve both relevance routing and current-state precedence without ambiguity?
2. **A08 + A11 boundary:** do agents distinguish “evidence authority” from “project/instruction authority” reliably enough to keep both modules separate?
3. **A11 + C03 boundary:** does formal Informatics already cover enough current-state/history separation for repository-authoring tasks while A11 remains useful universally?
4. **Token-value test:** does A11 measurably reduce stale-plan execution, conflicting-instruction synthesis, or concurrent-change overwrites relative to the constitution without it?
5. **SSOT terminology:** does keeping `single-source-of-truth` anywhere in the root cause monolithic centralization behavior? The selected root deliberately avoids the label while retaining the concept of canonical ownership.

## 11. Sources

Checked 2026-09-07 unless otherwise noted.

### OpenAI / ChatGPT / Codex — primary layer

1. OpenAI — Harness engineering: leveraging Codex in an agent-first world  
   https://openai.com/index/harness-engineering/  
   **Use:** structured `docs/` as system of record; short `AGENTS.md` map; active/completed plans; mechanical stale-doc gardening.

2. ChatGPT Learn — Custom instructions with `AGENTS.md`  
   https://learn.chatgpt.com/docs/agent-configuration/agents-md  
   **Use:** explicit global/project/nested instruction discovery; overrides; merge order; inspection; stale-session reload behavior.

3. ChatGPT Learn — Prompting  
   https://learn.chatgpt.com/docs/prompting  
   **Use:** “latest project plan” connected-source example; flag conflicts/missing information; Codex guidance to account for human changes/reverts.

### Independent mature-agent layer

4. Anthropic — How Claude remembers your project  
   https://code.claude.com/docs/en/memory  
   **Use:** layered `CLAUDE.md` scopes; conflict warning; shared `AGENTS.md` import rather than duplicate policy; active-context inspection.

5. Anthropic — Steering Claude Code: when to use CLAUDE.md, skills, hooks, and subagents  
   https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more  
   **Use:** instruction mechanisms differ by load timing, persistence, and authority.

6. GitHub — About customizing GitHub Copilot responses  
   https://docs.github.com/en/copilot/concepts/prompting/response-customization  
   **Use:** explicit instruction precedence; repository-wide vs path-specific vs agent instructions; conflict avoidance.

7. GitHub — Adding repository custom instructions for GitHub Copilot  
   https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions  
   **Use:** scoped repository instructions and nearest `AGENTS.md` behavior.

8. Google Gemini CLI — Provide context with `GEMINI.md` files  
   https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/gemini-md.md  
   **Use:** global/workspace/JIT hierarchy; `/memory show`; reload/refresh of live context.

9. Google Gemini CLI — Memory files  
   https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/memory.md  
   **Use:** route durable facts to the appropriate file; avoid duplicate facts across memory tiers.

10. Kiro — Specs just got faster (and smarter)  
    https://kiro.dev/blog/faster-smarter-specs/  
    **Use:** spec artifacts as source of truth during implementation; selective downstream regeneration when upstream state changes.

11. Kiro — Requirements-First workflow  
    https://kiro.dev/docs/specs/feature-specs/requirements-first/  
    **Use:** update requirements and regenerate affected design/tasks; iteration as expected behavior.

12. Kiro — Specs best practices  
    https://kiro.dev/docs/specs/best-practices/  
    **Use:** synchronization of requirements/design/tasks as project evolves.

### Established external discipline — secondary layer

13. NASA — 6.5 Configuration Management  
    https://www.nasa.gov/reference/6-5-configuration-management/  
    **Use:** true representation of product state; current and historical configurations; baseline/change/status accounting.

14. NIST SP 800-171 Rev. 3 — Baseline Configuration  
    https://nvlpubs.nist.gov/nistpubs/SpecialPublications/800-171r3/NIST.SP.800-171r3.html  
    **Use:** maintain a current baseline configuration and update it as the system changes.

## 12. Confidence / uncertainty

- **HIGH:** A11 needs explicit authority/precedence semantics; current “active state vs history” wording is insufficient for conflicting layered agent guidance.
- **HIGH:** a universal “one file is the SSOT” interpretation is wrong for current mature agent systems.
- **HIGH:** stale dependent artifacts should be updated or visibly marked stale when canonical upstream state changes.
- **HIGH:** contradictory active guidance should not be silently synthesized when no precedence resolves it.
- **MEDIUM-HIGH:** `canonical-current-state,scope-aware-precedence,consistency,history-separation` is a portable principle set; exact labels should still be tested across agents.
- **MEDIUM:** the selected root sentence may be compressible after A12/A13/C03 are complete.
- **MEDIUM:** final synthesis may merge A11 with A06 if controlled evaluation shows the dedicated current-truth rule adds little beyond context routing plus existing runtime precedence.
