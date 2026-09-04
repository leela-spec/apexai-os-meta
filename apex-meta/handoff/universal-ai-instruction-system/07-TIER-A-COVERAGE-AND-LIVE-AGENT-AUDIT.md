---
type: AuditAndDecision
Title: Tier A Coverage and Live Agent Instruction Audit
description: Maps operator-provided instruction modules to the proposed universal agent constitution, quantifies the compact XML surface, audits live repo agent instructions against current cross-agent best practices, and identifies the safest pilot.
status: research_complete_pilot_ready
created: 2026-09-04
---

# Tier A Coverage and Live Agent Instruction Audit

## Executive answer

The desired architecture is already a strong convergent best practice:

```text
small always-loaded operating surface
→ conditional/path/semantic routing
→ focused Skill/method
→ deep references/examples/scripts only when needed
```

The important correction is that the operator's existing modules should **not all become separate always-loaded procedures**. Their portable principles should be compressed into a small Tier A constitution; task-specific mechanics remain conditional or deep.

The current Informatics XML snippet is a good **conditional Informatics module**, not a complete universal agent constitution. It contains about 1,195 characters / 119 whitespace-delimited words and loads no external reference by itself. Depending on tokenizer, that is only a few hundred tokens. It gives the model five concrete formal-authoring rules plus one routing gate, but it does not provide target alignment, reuse-before-build, anti-drift, complexity routing, intent clarification, hierarchical realization, evidence discipline, completion verification, decision discipline, or recovery behavior.

Practical coverage: it strongly covers the **Informatics/output-authoring domain** and partially covers universal **context/progressive-disclosure** and **current-truth/communication** behavior. It is closer to ~15–25% of the intended universal behavior surface than to a complete agent constitution.

## 1. Operator-provided modules → correct ownership

Source: `apex-meta/AI-Snippets/Snippets.md`.

| Existing operator module | Preserve? | Tier A compression | Deeper owner | Decision |
|---|---|---|---|---|
| Target focus / anti-drift | **Yes — essential** | Target, Scope, Reuse, Complexity, Recovery | anti-drift / reuse method if needed | Split its principles across 4–5 tiny universal rules; do not keep the full 8-rule block always loaded. |
| Minimalism / overcorrecting | **Yes** | Scope + Complexity + Communication | none normally | Compress to one rule: use the smallest process that safely delivers the target. |
| Iterative & context work | **Principle yes; procedure no** | Complexity + Context + Hierarchical realization | project/specification workflow | Do not force the master-matrix/file-per-step protocol on simple work. |
| REI formula | **Conditional only** | Decision discipline says use grounded trade-offs | decision/trade-study reference | Do not put the numerical formula in Tier A; it can create false precision. |
| Macro → Meso → Micro | **Yes** | Hierarchical realization & V&V | `apex-meta/informatics/MMM/working-method.md` | Keep concept + one sentence in Tier A; load method only for dependent multilevel work. |
| Context Bloat | **Yes — essential** | Context engineering / progressive disclosure | context method | Universal principle. |
| Research & Output prompt | **Principle yes; workflow no** | Evidence & uncertainty | research Skill/reference | Full candidate-discovery/scoring/prototype workflow is conditional. |
| Q&A format | **Conditional** | Decision discipline | decision/Q&A method | Use only for material decisions or when operator asks for Q&A. |
| Exact-match patch protocol | **No in Tier A** | none | task-specific patch Skill/workflow | Too specialized and currently pollutes the root agent surface when universally loaded. |
| Informatics XML: serialization | **Conditional** | none universal | Informatics rule / standard | Apply only to relevant knowledge/document authoring. |
| Informatics XML: information mapping | **Conditional** | Communication only at principle level | Informatics rule / standard | Do not impose tables/blocks on every answer. |
| Informatics XML: STE prose | **Conditional** | Communication economy only | Informatics rule / style method | Useful for formal procedural docs, over-constraining for general work. |
| Informatics XML: progressive disclosure | **Yes — universal** | Context engineering | Informatics/context references | Keep. |
| Informatics XML: current truth | **Yes — high-value universal** | Context + Communication | current-truth conventions | Keep as a short universal rule; deep lifecycle/history handling remains scoped. |

## 2. Is the compact XML architecture best practice?

### Architecture: YES

Strong current evidence converges on a small always-on surface plus progressive disclosure:

- OpenAI's 2026 Codex harness case study says a large `AGENTS.md` failed and recommends a short map to deeper repository knowledge; its published example is roughly 100 lines.
- Claude Code recommends specific, concise instructions, targets under 200 lines per `CLAUDE.md`, and moves multi-step or local procedures into Skills/path-scoped rules.
- Agent Skills formalizes progressive disclosure: metadata at startup, full `SKILL.md` on activation, resources only as needed.
- Cursor separates Always Apply, intelligent relevance, path-specific, and manual rules; its docs say to reference files instead of copying them.
- Kiro separates `always`, `fileMatch`, `auto`, and `manual` steering.
- GitHub Copilot separates repository-wide, path-specific, and task-specific prompt instructions.

### XML representation: GOOD CANDIDATE, NOT A CROSS-AGENT STANDARD

XML is a credible compact representation inside the always-loaded file because descriptive tags make module boundaries and triggers explicit. Anthropic explicitly recommends XML tags for complex prompt components. However, `AGENTS.md`, `CLAUDE.md`, Cursor rules, Kiro steering, Copilot instructions, and Agent Skills are fundamentally Markdown/frontmatter ecosystems. Therefore:

- use XML **inside** the Markdown agent carrier if it improves adherence/scanability;
- do not depend on XML parser semantics;
- do not maintain a second XML policy authority;
- benchmark XML against equivalent compact Markdown across Codex/Claude/Gemini/rule-driven clients.

### Current Informatics XML wording: GOOD PROTOTYPE, NOT YET FINAL BEST-PRACTICE WORDING

Strengths:

- explicit applicability gate;
- descriptive tags;
- one behavior per rule;
- short direct commands;
- progressive disclosure;
- current-truth rule.

Weaknesses:

1. `formal_standards` is broader than necessary. "technical documentation" can accidentally include artifacts that should not receive YAML/frontmatter or rigid STE rules.
2. `WHEN ... OTHERWISE` inside XML is understandable, but a `when="..."` attribute is more compact and structurally regular.
3. The module has no explicit canonical `ref` / `deepen_when`, so the model knows *that* deeper references may exist but not exactly where or when to read them.
4. "Ban dense narrative walls" is too absolute; it can degrade tasks where cohesive prose is the right output.
5. YAML frontmatter on every matching artifact is a local Informatics convention, not a universal agent behavior.
6. Principle names can improve semantic anchoring, but labels alone are not sufficient. Best candidate grammar remains: **principle name(s) + one local semantic rule + optional trigger/ref**.

## 3. How much should Tier A contain?

There is no universal safe maximum. The governing constraint is adherence and context competition, not file format capacity.

Evidence-backed guardrails:

- Claude Code: target **under 200 lines** per `CLAUDE.md`; shorter instructions are followed more consistently.
- OpenAI production case study: short `AGENTS.md`, roughly **100 lines**, used as a map rather than a manual.
- Agent Skills: about **100 tokens of metadata per skill** at startup; full skill is delayed until activation.

Recommended Apex pilot budget — a local engineering target, not an upstream standard:

| Surface | Recommended pilot budget | Purpose |
|---|---:|---|
| Universal Tier A behavior | 8–12 modules; roughly 400–800 tokens | stable cross-task behavior |
| Project/root map + truly universal invariants | roughly 300–700 tokens | project identity, authority, key routes |
| Total root always-on surface | roughly 700–1,500 tokens; preferably <100–150 lines | enough to orient, not enough to become a manual |
| Conditional rule/Skill metadata | minimal descriptions | activation only |
| Deep method/reference | unlimited by root budget; loaded JIT | procedure/evidence/examples |

The existing Informatics XML is only about 1,195 characters / 119 words, so adding the missing Tier A behaviors in the same compact style is feasible without approaching a problematic root size.

## 4. Live repository audit

### 4.1 Root `AGENTS.md`

**Score: 6.5/10 — concise, but poor separation of universal vs task-specific behavior.**

Strengths:

- only ~4.4 KB;
- strong target/directness language;
- clear stop/escalation behavior;
- points to canonical Informatics and Apex KB owners instead of embedding them.

Problems:

- `Git Dispatch` is operationally specific but always loaded.
- `Apex KB Patch Safety` is a specialized exact-match mutation protocol but always loaded.
- `Apex KB Dispatch` is domain-specific and occupies root context for unrelated tasks.
- `Directness`, `Core Intent Execution`, and `Scope` repeat overlapping semantics.
- missing or incomplete Tier A principles: reuse-before-invention, explicit complexity routing, intent/clarification threshold, context engineering, MMM/V&V, evidence/uncertainty, general acceptance verification, decision discipline.

Recommendation: **do not simply append Tier A to the current file.** First replace duplicated/specialized root blocks with compact Tier A semantics and route specialized Git/KB/patch procedures conditionally.

### 4.2 `.claude/CLAUDE.md`

**Score: 8.5/10 — strong router/map architecture.**

Strengths:

- explicitly calls itself a compact activation/routing surface;
- cleanly separates Weekly Orchestrator, Multi-Agent Orchestration, and the Plan-Sync-Session backbone;
- routes detailed behavior to Skills and agent contracts;
- instructs JIT reading rather than broad repo loading;
- defines authority and mutation boundaries.

Weaknesses:

- some global boundaries duplicate behavior that could ultimately live once in Tier A/root semantics;
- Claude-specific routing still depends on a separate `AGENTS.md`, so two always-on surfaces can drift.

Recommendation: treat this as the **best current in-repo reference implementation** for routing, but converge shared behavior with the cross-agent root instead of duplicating it.

### 4.3 `.claude/rules/informatics.md`

**Score: 5/10 — content good, loading configuration wrong for its stated scope.**

The prose says it applies only when working under `apex-meta/informatics/` or `apex-meta/SmallSkills/OKF_Format/`, but the file has no `paths:` frontmatter. Current Claude Code documentation states rules without `paths` are loaded unconditionally at launch.

Recommendation: make it genuinely path-scoped or replace it with a conditional semantic Skill/rule. This is an immediate low-risk pilot candidate for progressive disclosure.

### 4.4 Cursor / Kiro / Windsurf Obsidian rules

| Runtime file | Current mode | Score | Finding |
|---|---|---:|---|
| `.cursor/rules/obsidian-wiki.mdc` | `globs: "**/*"`, `alwaysApply: true` | 3/10 | Large domain rule always injected for every task. |
| `.kiro/steering/obsidian-wiki.md` | `inclusion: always` | 3/10 | Same issue; Kiro directly supports conditional/auto inclusion. |
| `.windsurf/rules/obsidian-wiki.md` | `activation: "always-on"` | 3/10 | Same issue; should not be universal unless the entire repo session is always an Obsidian task. |

These files duplicate a routing table that already points into Skills. They are excellent examples of where **skill metadata / semantic activation** should replace large always-on route tables.

### 4.5 `.hermes.md`

**Score: 5.5/10 — functionally useful but duplicated and drift-prone.**

It is near-duplicate root operating content headed `Codex Operating Note`, but it already differs from `AGENTS.md` (for example, Informatics routing is absent). Manually maintaining parallel always-on files guarantees semantic drift over time.

Recommendation: establish one canonical Tier A semantic source and render/mirror only when a runtime cannot consume `AGENTS.md` directly. Do not independently author equivalent policies in several root files.

## 5. Specialist agent audit (`.claude/agents/`)

Overall: **8/10 architecture; generally better than the root instruction surfaces.**

The agents are usually short, role-bounded, explicit about what they own/must not own, and use deeper doctrine/Skills only when invoked.

| Agent | Assessment | Main strength | Main improvement |
|---|---:|---|---|
| `alfred.md` | 8.5/10 | clear operator-interface accountability and explicit no-inference confirmation rule | repeated orchestration/Weekly disclaimers partly duplicate shared routing; keep only what materially improves activation precision |
| `apex-kb-operator.md` | 9/10 | compact, Skill-backed, CLI-as-authority contract | strongest pattern; use as model for other operational agents |
| `apex-plan-ops.md` | 9/10 | tiny role shell around `apex-plan` Skill | little to change |
| `apex-sync-ops.md` | 9/10 | tiny deterministic worker shell around `apex-sync` | little to change |
| `apex-review-validity.md` | 8/10 | strong bounded output schema and independent-review lens | large prompt is acceptable because conditional, but duplicated review mechanics may belong in one review Skill/reference |
| `apex-review-alignment.md` | 8/10 | same; strict lens separation | same consolidation opportunity |
| `informatics-design.md` | 9/10 | explicit `CORE.md` first, deeper files only when CORE points there | near-ideal progressive-disclosure pattern |
| `knowledge-bank.md` | 7.5/10 | source custody/provenance boundaries are clear | contract itself admits many appendix pointers were never migrated; stale/dead reference topology should be cleaned or indexed |
| `meta-detective.md` | 8/10 | independent read-only reviewer, strong falsification rule | `CORE.md` is ~9.4 KB: still conditional, but not especially "core"; consider a smaller quick core if eval shows context cost/adherence issue |
| `meta-ops.md` | 9/10 | `ESSENCE.md` is only ~1 KB; 5 KB integration doc is loaded only before backbone interaction | excellent JIT separation; reference model |
| `meta-strategy.md` | 8.5/10 | bounded options/evidence contract, no self-validation | repeated run-boundary boilerplate could be reduced once shared contract is reliable |
| `prompts-workflows.md` | 9/10 | bounded objective + CORE-first + Skill delegation | strong model |

### Cross-agent structural issue

Many specialist descriptions repeat variants of:

- only inside active Multi-Agent Orchestration;
- do not auto-activate;
- not Weekly Orchestrator;
- do not orchestrate outside role.

Some repetition is justified because descriptions influence selection. However, repeated paragraphs should be measured: if a shared runtime boundary already prevents misactivation, the per-agent description can become shorter and use the saved tokens for the actual trigger and accountability.

## 6. Best pilot against the existing repo

Do **not** rewrite every agent at once.

Run three bounded changes/evals:

### Pilot A — Tier A root contract

Test the compact Tier A XML candidate against the current `AGENTS.md` on a fixed task suite. Do not append it to the existing file unchanged; compare:

1. current root;
2. current root + XML (control for additive overload);
3. **replacement/refactored root**: Tier A XML + tiny project map + JIT routes;
4. equivalent compact Markdown semantics.

### Pilot B — fix one obvious progressive-disclosure violation

Use `.claude/rules/informatics.md` because the task trigger is already explicit. Add true path scoping in a test branch/worktree or controlled eval and compare `/context` / InstructionsLoaded evidence before and after.

### Pilot C — convert one always-on domain router to semantic/conditional activation

Use the Obsidian Wiki rule in one supported client (Kiro is especially direct because `auto` is official and description-driven). Compare activation accuracy on Obsidian vs unrelated tasks.

## 7. Decision

**Keep:** small always-loaded constitution, XML as one candidate syntax, established principle names + one local rule, optional `ref` + `deepen_when`, Skills/path/model activation, JIT references.

**Change from current repo:** remove specialized operational procedures from always-on surfaces; stop pretending prose-scoped files are runtime-scoped; reduce duplicated cross-client rule tables; converge shared semantics before adding more instructions.

**Do not yet:** propagate the candidate across all agents. The next technical step is a controlled Tier A pilot plus one real loading-scope correction, then measure adherence, unwanted activation, context cost, and missed deep-reference retrievals.

## Primary external sources

- OpenAI — Harness engineering: https://openai.com/index/harness-engineering/
- Claude Code — project instructions/rules: https://code.claude.com/docs/en/memory
- Anthropic — prompting/XML guidance: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-templates-and-variables
- Agent Skills specification: https://agentskills.io/specification
- Cursor Rules: https://cursor.com/docs/rules
- Kiro Steering: https://kiro.dev/docs/steering/
- Gemini CLI context: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/gemini-md.md
- GitHub Copilot custom instructions: https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions
