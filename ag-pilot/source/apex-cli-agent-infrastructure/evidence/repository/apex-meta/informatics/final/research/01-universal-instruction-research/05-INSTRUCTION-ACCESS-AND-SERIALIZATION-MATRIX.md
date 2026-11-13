---
type: ResearchMatrix
title: Universal Agent Instruction Access and Serialization Matrix
description: Compares how agents receive always-on, scoped, semantic, manual, and deep-reference instructions, including XML versus Markdown and import behavior.
status: corrected_research_authority
created: 2026-09-04
---

# Universal Agent Instruction Access and Serialization Matrix

## Core distinction

Two separate design questions must not be conflated:

1. **How is an instruction represented?** XML, Markdown, YAML/frontmatter, plain text.
2. **When is it loaded?** Always, path-triggered, model-triggered, manually, or read on demand.

Token efficiency is controlled mainly by **loading behavior**, not by serialization alone.

## Instruction-access matrix

| Access pattern | What the model sees initially | How full guidance appears | Typical implementations | Token cost | Reliability | Best use | Apex recommendation |
|---|---|---|---|---:|---|---|---|
| **Always-on root injection** | Full root rule content every turn/session | Already present | AGENTS.md, CLAUDE.md, root GEMINI.md, global rules | High if abused; excellent when tiny | Very high | Stable universal principles and non-negotiable repo facts | **Use for tiny operating constitution only** |
| **Nested directory instruction** | Broad parent instructions; local instruction when area is active | Agent/runtime discovers nearest file | AGENTS.md hierarchy, Claude subdir CLAUDE.md, Gemini JIT context | Low-medium | High | Subsystem/path-specific conventions | **Use for repository-specific local constraints** |
| **Deterministic glob/path scope** | Nothing until matching file/path context | Runtime injects matching rule | Copilot `applyTo`, Cursor specific-file rules, Windsurf `glob`, Kiro `fileMatch`, Claude rules `paths` | Low | **Very high** | Language/file/subsystem rules | **Preferred for deterministic scope** |
| **Semantic/model-decision rule** | Usually name/description only | Model reads full rule when task seems relevant | Windsurf `model_decision`, Kiro `auto`, Cursor intelligent rules | Very low until activated | Medium-high | Behavioral/domain guidance that cannot be bound to file paths | **Strong option where runtime supports it** |
| **Agent Skill progressive disclosure** | `name` + `description` metadata only | Full `SKILL.md`; then references/scripts only as needed | Agent Skills, Claude, Windsurf, Factory, OpenHands, others | **Very low** | High if descriptions are good | Reusable method, checklist, workflow, domain procedure | **Best general deep-method mechanism** |
| **Keyword-triggered guidance** | Trigger registry/minimal metadata | Full guidance injected on matching words | OpenHands keyword skills | Very low | High for explicit vocabulary; brittle for synonyms | Narrow named technologies/domains | Optional; semantic descriptions usually better |
| **Manual `@` / slash invocation** | Only command/rule name or nothing | User explicitly invokes content | Windsurf manual rules, Kiro manual steering, Cline toggle, skills slash commands | Very low | **Very high when invoked** | Rare/sensitive/special workflows | Useful fallback and debugging surface |
| **Immediate file import** | Full referenced content is expanded into startup/current context | Happens immediately | Claude `@path`, Gemini `@file`, Copilot `@path` | Potentially high | Very high | Small mandatory shared rules | **Do NOT use for deep references when token saving is the goal** |
| **Plain path pointer + agent read** | Only the path and short routing rule | Agent uses filesystem read when condition is met | Works in most filesystem-capable coding agents | **Minimal** | Medium-high; depends on agent obeying routing instruction | Cross-agent JIT reference fallback | **Recommended portable fallback** |
| **Repository index / map** | Short map/index | Agent navigates structured docs | OpenAI Codex harness practice; docs indexes | Low | High if paths/ownership are clear | Large knowledge bases | **Use as information map, not rule duplication** |
| **Memory retrieval** | Small retrieved memory or selected notes | Runtime chooses remembered content | Windsurf Memories, Claude auto memory, product memory systems | Low | Medium | Learned preferences and ephemeral context | **Not authority for durable operating rules** |
| **Hook / policy enforcement** | Usually no prompt tokens | Deterministic code checks tool/action | Claude hooks, Cline hooks, Factory hooks, permissions systems | Near-zero prompt cost | **Very high** | Safety, irreversible actions, deterministic validation | **Move hard enforcement here where possible** |
| **Workflow command** | Workflow name only until invoked | Ordered procedure loaded/executed | Windsurf Workflows, Cline Workflows, prompt files, slash commands | Low | High for repeated manual procedures | Deployment/release/checklists | Not universal behavior; task-specific |

## Critical finding: imports are not JIT references

If the root agent file contains an import syntax that the runtime expands, the referenced content is **not** token-efficient deep context.

Examples:

- Claude `CLAUDE.md` `@path/to/file` imports are expanded and loaded with the importing file.
- Gemini `GEMINI.md` `@file.md` imports modularize maintenance but still inject imported content.
- Copilot CLI `@relative/path` references read the referenced file immediately.

Therefore this Apex pattern:

```text
<context_management ref="apex-meta/.../context-method.md">
  Keep working context to the smallest high-signal set.
  Read ref only for long/context-heavy work.
</context_management>
```

is more suitable for JIT depth than:

```text
@apex-meta/.../context-method.md
```

when the root must remain tiny.

## Serialization matrix

| Format inside always-on agent file | Cross-model readability | Human maintainability | Token overhead | Hierarchy clarity | Native framework support | Main weakness | Recommendation |
|---|---:|---:|---:|---:|---:|---|---|
| **Markdown headings + bullets** | **Very high** | **Very high** | **Low** | High | **Universal in agent files** | Boundaries can become visually loose if modules are tiny and numerous | **Safest baseline** |
| **Compact XML blocks inside Markdown** | **Very high** | High | Medium | **Very high** | Parsed as ordinary text; Anthropic/Google/Windsurf explicitly support XML-like structuring | No cross-agent semantic parser; tags add tokens | **Strong candidate for Apex L0 modules** |
| **YAML frontmatter + Markdown** | High | High | Medium | High | Native for Skills, path rules, Kiro/Cursor/Windsurf metadata | Root AGENTS.md does not standardize custom frontmatter semantics | Best for conditional files, not required for root |
| **Pure YAML** | High | Medium | Medium | High | No universal root-agent parser | Easy to over-serialize behavior; prose becomes awkward | Avoid as universal behavior surface |
| **JSON** | High | Low-medium | **High** | High | Good for runtime config, not agent prose | Quoting/braces add noise; poor for nuanced behavioral guidance | Avoid for L0 instructions |
| **Plain prose paragraphs** | High | High | Low | Low | Universal | Harder to scan, route, or isolate concepts | Use only for very small files |
| **Named principle + one-line rule** | **Very high** | **Very high** | **Lowest useful** | Medium-high | Universal | Principle name alone can be ambiguous | **Best semantic unit; combine with Markdown or XML wrapper** |

## XML evidence

XML is not an AGENTS.md standard requirement, but it has credible model-facing support:

- Anthropic's current prompting guidance explicitly recommends XML tags to separate instructions, context, examples, and inputs in complex prompts.
- Google's current prompt design guidance recommends delimiters such as `<instruction>` / `<background_information>` and `##` headings.
- Windsurf's current Rules documentation explicitly says XML tags can be an effective way to convey information and group related rules.
- OpenAI's published explanation of the Codex agent loop shows XML-like tagged instruction blocks in its constructed prompt.

Conclusion:

> **XML is a valid compact structuring syntax inside an agent file. It is not the loading mechanism and not the cross-agent standard.**

## Recommended XML design constraints

If Apex uses XML inside the root agent file:

1. Keep tags semantic and stable.
2. Put one behavior module per tag.
3. Keep the body self-sufficient in one or two sentences.
4. Put established principle names in an attribute when useful.
5. Put a normal repository path in `ref` only when deeper guidance exists.
6. Put the activation condition in `deepen_when` or the body.
7. Do not use XML for long procedural steps.
8. Do not duplicate the referenced method inside the tag.
9. Do not rely on the XML parser; models should understand it as structured text.
10. Benchmark the same semantics in compact Markdown versus XML before freezing the format.

Candidate shape:

```xml
<operating_contract>
  <target_focus
    principles="outcome-orientation,reuse-before-build,YAGNI"
    ref="apex-meta/informatics/agent-behavior/target-focus.md">
    Keep work tied to the requested deliverable. Prefer a proven existing solution before creating a new abstraction.
  </target_focus>

  <context_management
    principles="context-engineering,progressive-disclosure,JIT-retrieval"
    ref="apex-meta/informatics/agent-behavior/context-management.md"
    deepen_when="long, multi-source, or context-heavy work">
    Keep working context to the smallest high-signal set. Load deeper material only when relevant.
  </context_management>
</operating_contract>
```

The `ref` is a path for the agent to read **only when the stated condition warrants it**. It is not an automatic import.

## Best cross-agent access stack

For filesystem-capable coding agents:

```text
ROOT AGENTS.md
  tiny operating contract
  + project map
  + critical commands/constraints
       ↓
PATH-SCOPED INSTRUCTIONS
  deterministic local constraints
       ↓
AGENT SKILLS
  semantic task procedures / deeper methods
       ↓
REFERENCES / SCRIPTS / EVIDENCE
  only as needed
```

For a general chat product without repository auto-discovery:

```text
paste/supply the same tiny operating contract
       ↓
when a deeper module is needed:
  attach/paste/retrieve only that focused method
```

Thus the **semantics can be universal even when the delivery mechanism is not**.
