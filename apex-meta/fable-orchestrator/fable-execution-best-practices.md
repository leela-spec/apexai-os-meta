---
title: "Fable Execution Best Practices"
purpose: "Machine-readable operating doc for a Claude Fable 5 session acting as orchestrator over external heavy-reasoning models and Codex execution."
created: 2026-07-11
grounded_in: "Live web research (2026-07-11) + apex-meta/CODEX_EXECUTION_STANDARD.md (existing, do not duplicate)"
status: finalized_input
---

# Fable Execution Best Practices

## 1. What Fable actually is (ground truth, not assumption)

```yaml
model: Claude Fable 5
released: 2026-06-09
class: Mythos-class, Anthropic's most capable publicly-released model as of this doc
context_window: 1,000,000 tokens (default)
max_output: 128,000 tokens per request
knowledge_cutoff: 2026-01
pricing: {input: "$10 / M tokens", output: "$50 / M tokens", note: "prompt caching gives 90% input discount"}
agentic_capability:
  - "Can work for days at a time in an agent harness (Claude Code / Managed Agents): planning across stages, delegating to sub-agents, checking its own work."
  - "At higher reasoning effort, reflects on and validates its own work before finishing — this is the built-in mechanism this doc's §4 verification step should lean on, not duplicate with a separate manual pass."
  - "Real-world reference point: Stripe used it to compress a codebase-wide migration from ~2 months of team effort to 1 day."
safety_note: "Safety classifiers fall back to Opus 4.8 for cybersecurity/bio-chem/distillation topics, <5% of sessions. Irrelevant to this orchestration-architecture work unless a sub-task strays into those domains."
source: "https://www.anthropic.com/news/claude-fable-5-mythos-5"
```

**Implication for this build:** Fable's own context and agentic runtime are already built for exactly this "plan across stages, delegate, self-check" shape. The point of routing heavy reasoning *outside* Fable is token cost and access to non-Anthropic research styles (Perplexity's live web+GitHub retrieval, Gemini's Google-grounded search) — not a capability gap in Fable itself. Don't outsource something Fable can already do well and cheaply in-context just because "outsourcing" is the theme of this initiative.

## 2. Model routing table

```yaml
routing:
  fable_claude_code:
    role: orchestrator_and_direct_executor
    use_for:
      - holding cross-system context and making architecture decisions
      - authoring every prompt sent to the models below
      - grounding/verifying every result that comes back (see §4)
      - direct repo reads/writes, git operations, and calling Codex for execution (see §5)
    do_not_use_for:
      - open-web research Fable would otherwise have to reconstruct from training data (route to Gemini/Perplexity instead)

  chatgpt_deep_research_or_pro_thinking:
    role: heavy_reasoning_and_synthesis
    use_for: "Broad conceptual/strategic reasoning tasks, synthesis across many sources, deep multi-angle analysis."
    limitation: "No reliable GitHub connector as of this doc — do not ask it to read live repo files; paste in exported/summarized content instead."
    source: "operator-confirmed limitation, 2026-07-11"

  gemini_deep_research_or_pro_thinking:
    role: standard_research_only
    use_for: "General web research, Google-ecosystem-grounded questions."
    prompt_rule: "Combine 'research X' and 'write Y from what you find' into ONE instruction — Gemini handles combined research+write instructions meaningfully better than the same work split across two prompts."
    source: "https://duizendstra.com/ai/guides/gemini-prompt-engineering-guide/ (2026 practitioner guidance)"

  perplexity:
    role: repo_grounded_research
    use_for: "Anything requiring live repo-file analysis — it has a working GitHub connector (Pro/Max/Enterprise), per-user scoped, SOC2 Type II, no training on repo data."
    why_preferred_here: "The only one of the three external research tools with a reliable GitHub connector as of this doc — route repo-file-dependent research questions here first, others only after exporting/pasting relevant file content."
    source: "https://www.perplexity.ai/help-center/en/articles/12275669-github-connector-for-enterprise"

  codex:
    role: execution_only_not_reasoning
    use_for: "Deterministic repo commands, patches, commits/pushes once Fable has already decided what to do."
    contract: "Use apex-meta/CODEX_EXECUTION_STANDARD.md verbatim — do not redefine. Stupid-simple, command-oriented, main-only, no interpretation, fixed handover sentence."
    do_not: "Never ask Codex to decide architecture, reinterpret scope, or reason about what should happen next — that's Fable's job."
```

## 3. Prompt shape for each external research model

```yaml
universal_deep_research_prompt_frame:
  role: "State the analyst persona explicitly (e.g. 'act as a Claude Code / agentic-systems architecture reviewer')."
  task: "One primary objective per prompt. Split multi-part questions into separate prompts rather than bundling."
  context: "Paste the specific repo files/KB excerpts needed — do not assume the model can fetch them (except Perplexity+GitHub)."
  output_format: "Specify exact structure wanted back (e.g. 'ranked table with source citation per row', 'YAML decision list'), so the pasted-back result slots into this repo's existing doc conventions with minimal reformatting."
  source_instruction: "Always require inline citations/links — unverified claims from external models are not to be trusted at face value (see §4)."
  specificity_rule: "Vagueness produces vague research. State the exact repo path, KB name, or decision this prompt's output will feed into."
  repo_identity_rule: "Any prompt delegating research about THIS repo's systems must carry the repo's identity into the question: name the orchestration system under design, name the exact folders where its parts are defined, and name the specific KB(s) that already hold the information (e.g. apex-meta/kb/claude-code-orchestration-design). Otherwise answers come back as generic web research needing full re-grounding before they can be trusted. Highest burden on early/architecture-phase prompts. (Operator lesson, US-IDEA-01: apex-meta/orchestration/simulations/US-IDEA-01-20260711/01-candidate-entry.v2.md, review-verified, operator-accepted 2026-07-12.)"
source: "https://phrasly.ai/blog/best-prompts-for-gemini-ai/ ; https://findskill.ai/skills/productivity/deep-research-prompt-framework/ (2026)"

gemini_specific_rule: "Ask for research AND the written output in the same prompt — do not split into a research turn and a writing turn."

perplexity_specific_rule: "When the question needs live repo truth (not general practice), explicitly invoke the GitHub connector context and name the exact repo/path — don't rely on it inferring which repo you mean."
```

## 4. Mandatory verification step (non-negotiable)

```yaml
verification_contract:
  who: Fable, inside Claude Code, after any external-model result is pasted back in
  what:
    - Cross-check every material claim against the actual repo state (real files, real KBs, real prior decisions) before acting on it.
    - Explicitly downgrade confidence (e.g. "working_hypothesis") for anything that can't be grounded this way, rather than presenting it as verified.
    - Never let an external model's confident tone substitute for a real grounding check — this exact failure mode (structurally complete, semantically ungrounded output) already happened once in this repo's own KB history (see apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NextFinalization/Apex-KB-Semantic-Quality-Realization-Handover.md) and is not hypothetical.
  proven_pattern_to_reuse: >
    The 2026-07-10 KB authoring pass (apex-meta/kb/claude-code-orchestration-design/log/lifecycle-completion-report-20260710.md)
    already demonstrated this working at scale: real claim-ID grounding, explicit confidence downgrades where synthesized,
    honest "left thin" framing where source material didn't support more. Repeat that discipline for external-model output too.
```

## 5. Token-efficiency discipline for Fable's own context

```yaml
context_discipline:
  do_not: "Paste a full raw ChatGPT/Gemini/Perplexity deep-research response into the chat context and leave it there."
  instead:
    - "Write the useful, verified extract to a real file (a KB page, a decision doc, an audit item) immediately."
    - "Keep only a short pointer + one-line verdict in the running session context, not the full external response."
    - "This mirrors Anthropic's own just-in-time-retrieval guidance: keep lightweight identifiers in context, load full content only when actually acting on it."
  source: "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents"
  why_it_matters_here: "Fable's 1M context window is large but not infinite, and this build spans a 'massive' multi-KB corpus per the operator's own framing — treat context as a budget from the start, not something to worry about only when it runs out."
```

## 6. Context-budget circuit breaker (real, documented risk — not hypothetical)

```yaml
grounding: >
  This is not a precaution against a rumor. As of this doc, publicly documented Claude Code issues
  include: standing MCP/plugin connections consuming ~55,000 tokens before the first message is
  even typed; auto-compaction firing unreliably (sometimes at ~8% usage, sometimes not at all after
  large codebase analysis, letting context grow unchecked for 5-20+ turns); and every file read /
  MCP tool response / log scanned being added to context permanently for that session until
  compaction actually runs. Source: github.com/anthropics/claude-code issues #52981, #64619, #42590;
  Anthropic's own March 2026 acknowledgment that users hit usage limits "way faster than expected."
rules:
  minimal_connector_footprint: >
    Before starting a real Fable-led build session under this initiative, check which MCP
    servers/connectors/plugins are actually enabled and disable anything not needed for that
    session's phase. Standing connector cost is paid before Fable does anything, and it is not
    visible in the conversation itself.
  do_not_trust_auto_compaction_alone: >
    Auto-compaction is documented as unreliable in both directions (too early, or not at all).
    Do not treat "it'll compact when needed" as a safe default for a build spanning a genuinely
    large multi-KB corpus.
  hard_checkpoint_per_phase: >
    At the start of each phase in build-plan.md, Fable should note its own
    context usage if the harness surfaces it, and treat a session that's already heavily loaded
    before starting a new phase as a signal to close out and hand off via a written state file
    (decisions.md / user-stories.md / simulation record) rather than pushing forward in the same
    session.
  offload_immediately_not_eventually: >
    §5's "write the extract to a file immediately" rule is the actual circuit breaker, not just a
    tidiness preference — an external model's raw response sitting in context for multiple turns
    is exactly the accumulation pattern behind the documented compaction-failure reports.
  fail_loud_not_silent: >
    If a session appears to have consumed an unexpected amount of budget with no proportional
    output, say so explicitly and stop, rather than continuing and hoping a later compaction fixes
    it — matching this repo's own "no silent process substituting for the deliverable" rule (§7 below,
    memory: feedback_target_deliverable_over_process) applied to token budget specifically.
```

## 7. Session discipline (the actual failure this doc exists to prevent)

```yaml
non_negotiable_rule: >
  Every Fable session under this initiative must produce the concrete deliverable it was asked
  for, not just decisions/setup/maintenance around it. See the repo's own stored lesson on this
  exact failure mode (memory: feedback_target_deliverable_over_process). State the deliverable
  first, resolve any blocking questions in one fast batch, then spend the session actually doing
  the work — do not let a Q&A round or a maintenance pass become the whole session's output.
```

## 8. Never delete a KB or file on "looks old/superseded" alone

```yaml
rule: >
  Before deleting ANY file or KB in this repo — even one that git history confirms is "the older
  one" or that a plausible story says is superseded — grep the whole repo for its bare path/name
  first. "Older" and "duplicate" are different claims; only the second one justifies deletion.
  If anything outside the target (especially a live skill/reference file) cites it by path as a
  source or dependency, stop and report the finding before acting, even if the operator already
  gave a delete instruction — the instruction may be based on an assumption that doesn't hold
  once you actually check.
applies_to: "Any Fable session doing repo cleanup, KB reconciliation, or dedup work under this initiative."
```
