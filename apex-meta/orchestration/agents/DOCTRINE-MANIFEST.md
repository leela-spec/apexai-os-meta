---
title: "Agent Doctrine Manifest — deterministic move record + translation rules"
purpose: >
  The record of the 2026-07-11 evaluation and deterministic (byte-identical, sha256-verified)
  move of the old Apex v2 per-agent doctrine into the live agent domains. Copies are VERBATIM
  source evidence; the translation rules below govern how agents read them. Source KB
  (apex-meta/kb/old-apex-full-orchestration-agent-kb-v2/raw/other/managed/) stays intact.
created: 2026-07-11
method: "two parallel evaluation passes over all 9 v2 roles (227 files); verdicts MOVE / REFERENCE / SKIP; MOVE = cp + sha256 equality check"
---

# Agent Doctrine Manifest

## What moved (39 files, all hash-verified — hashes in the move-commit log)

| Domain | Files moved | Origin (v2 role) |
|---|---|---|
| `alfred/` | ROLE-SEED, ESSENCE | alfred |
| `meta-strategy/` | ROLE-SEED (⚠ patch-packet wrapper — real doctrine is the fenced `md` body inside), ESSENCE | meta_strategy |
| `meta-ops/` | ROLE-SEED, ESSENCE, legacy-hygiene-clean-TEMPLATES (P0–P3 severity crib, closure-validity checklist, execution-mode lock) | meta_ops, hygiene_clean |
| `meta-detective/` | ROLE-SEED, ESSENCE, BEST_PRACTICES (DET-BP-001..010), MISTAKES (DET-MIS-001..010), TEMPLATES (8 instruments), APPENDIX_INTERNAL_MODES (5-mode playbook) | meta_detective — the only role whose accumulated KB was actually populated |
| `knowledge-bank/` | ESSENCE, BEST_PRACTICES (BP-KB-001..009), MISTAKES, TEMPLATES, APPENDIX_KB_DATABASE_SCHEMA, APPENDIX_KB_EXAMPLES | special_ops__knowledge_bank |
| `informatics-design/` | ESSENCE, BEST_PRACTICES, MISTAKES, TEMPLATES + legacy-hygiene-clean-{ESSENCE, BEST_PRACTICES, MISTAKES} (structural-QA doctrine) | special_ops__informatics_design, hygiene_clean |
| `prompts-workflows/` | ESSENCE, BEST_PRACTICES (v2, PW-BP-001..011), MISTAKES (PW-MK-001..011), TEMPLATES (10), APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS, APPENDIX_KB_EXAMPLES, APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT | special_ops__prompts_workflows |
| `.claude/skills/AIRouting/references/legacy-v2-doctrine/` | ESSENCE, BEST_PRACTICES, MISTAKES, TEMPLATES, APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON, APPENDIX_KB_ROUTING_EXAMPLE | special_ops__ai_handling_routing (role dropped; its job = AIRouting skill) |

## What did NOT move (and why — honest verdicts)

- **Empty scaffolds (SKIP):** alfred/meta_ops/meta_strategy BEST_PRACTICES, MISTAKES, TEMPLATES + all LEARNING_QUEUEs were EMPTY_STATE schema stubs or dead promotion machinery. Finding on record: the v2 promotion pipeline produced accumulated content for exactly one of nine roles (meta_detective) — the machinery was mostly overhead.
- **REFERENCE (stay in KB, cite only):** ~135 files — research dumps (some with fabricated "GPT-5.5-era" model claims: never promote), build-provenance ledgers, patch/campaign logs, chat exports, the 610K Studies/ source library, duplicates (ResearchOnAIFailure_claude.md ≡ Studies_Claude.md). Also hygiene_clean/prompt-transport appendices obsoleted by the Edit tool + deterministic-markdown-patcher skills.

## Translation rules (how a live agent must read these copies)

The copies are verbatim v2 artifacts. Four of their assumptions are **superseded**; the doctrine transfers, the mechanism does not:

1. **Always-on swarm → ephemeral invocations.** Ignore `owner:`/`validator:`/`review_due:` plumbing and named-agent routing tables (validator `hygiene_clean` etc. no longer exist). Cross-checks route through `workflows/detective-review.md`; escalations collapse to the operator gate.
2. **Per-agent promotion queues → single mutation surface.** Any "promotion ledger / LEARNING_QUEUE promotion route" = today: `authority.state: candidate` → Detective review → operator gate → apex-session write. Candidate-vs-canon separation survives; the routes are dead.
3. **STATE_BLOCK / constant-frame machinery → harness-carried state.** (prompts-workflows files) Keep the discipline — explicit task contract, atomic scope, no implicit continuation, HALT/CLARIFY as routing signals; drop the literal state-block relay mechanics.
4. **"Modes are not sub-agents" (detective APPENDIX_INTERNAL_MODES) → inverted.** That rule guarded against expensive always-on agents; with ephemeral subagents, a mode MAY run as a throwaway invocation. The per-mode owns/does-not-own boundaries still bind.
5. **Stale paths and model claims.** `OpenClaw/...`, `AIHowTo/...`, `leela-spec/MasterOfArts` paths and all pre-2026-07 model/provider claims are historical; per AIHR's own rule, treat as `needs_current_verification`.

## Read order for an agent entering its domain

ESSENCE → BEST_PRACTICES → MISTAKES (before acting) → TEMPLATES (when producing) → appendices (only when the task matches their subject). ROLE-SEED is historical context, superseded by the live `.claude/agents/<name>.md` contract — on conflict, the live contract wins.
