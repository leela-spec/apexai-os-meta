# Old Agent KB Semantic Rerun Prompt Flow

## Purpose

Use this prompt flow in another GPT-5.5 Thinking chat to rerun the LLM-owned ingestion and synthesis phases for:

```text
apex-meta/kb/old-apex-full-orchestration-agent-kb/
```

This flow builds on deterministic phases that already ran successfully. It does not restart source intake, Phase 0, lint implementation, or retrieval tooling unless verification proves the deterministic baseline is missing.

The rerun must replace the existing LLM semantic artifacts, not layer another partial continuation file on top of stale Phase 1/Phase 2 outputs.

## Source Orientation

This flow is adapted from the earlier `llm-wiki-project-repos` Phase 1 + Phase 2 prompt, but retargeted to `old-apex-full-orchestration-agent-kb` and tightened for replacement behavior.

## Target State

```yaml
repo: leela-spec/apexai-os-meta
branch: main
kb_root: apex-meta/kb/old-apex-full-orchestration-agent-kb
kb_slug: old-apex-full-orchestration-agent-kb
canonical_package: .claude/skills/apex-kb/
runtime_scripts:
  lifecycle: apex-meta/scripts/apex_kb.py
  retrieval: apex-meta/scripts/apex_kb_retrieval.py
operator_gate:
  phrase: approve ingest
  status: approved_for_this_rerun
```

## Current Known Baseline To Verify

Before producing new semantic files, the next chat must verify live repo state.

Required checks:

1. Read `.claude/skills/apex-kb/SKILL.md`.
2. Read `apex-meta/kb/old-apex-full-orchestration-agent-kb/wiki/index.md`.
3. Read `apex-meta/kb/old-apex-full-orchestration-agent-kb/ingest-analysis/phase1-completion-report.md`.
4. Read `apex-meta/kb/old-apex-full-orchestration-agent-kb/log/phase2-wiki-compile-report.md` if present.
5. Read `apex-meta/kb/old-apex-full-orchestration-agent-kb/outputs/synthesis/apex-kb-semantic-continuation-after-lint-closure.md`.
6. Inspect `manifests/phase0/` and `derived/search/` enough to confirm deterministic outputs exist.
7. Do not assume file lists from memory.

If the deterministic baseline is missing, stop with `DETERMINISTIC_BASELINE_NOT_VERIFIED` and list missing files. Do not invent replacement semantic pages.

## Replacement Policy

The rerun must replace prior LLM-owned semantic surfaces:

```yaml
replace_or_rewrite:
  ingest_analysis:
    path: apex-meta/kb/old-apex-full-orchestration-agent-kb/ingest-analysis/
    behavior: "create a new coherent Phase 1 set and replace obsolete Phase 1 semantic files if the chat has repo write access"
  wiki:
    path: apex-meta/kb/old-apex-full-orchestration-agent-kb/wiki/
    behavior: "create a new coherent Phase 2 wiki layer and replace/update existing pages"
  audit:
    path: apex-meta/kb/old-apex-full-orchestration-agent-kb/audit/
    behavior: "replace or update semantic audit items"
  log:
    path: apex-meta/kb/old-apex-full-orchestration-agent-kb/log/
    behavior: "write new rerun reports with timestamped filenames"
  outputs_synthesis:
    path: apex-meta/kb/old-apex-full-orchestration-agent-kb/outputs/synthesis/
    behavior: "read prior continuation files as evidence, but do not create another vague continuation unless needed"
```

Do not delete deterministic artifacts unless a deterministic postflight tool says they are rebuildable and stale. In normal rerun mode, semantic replacement means replacing `ingest-analysis/`, `wiki/`, `audit/`, and semantic reports only.

## Prompt Flow

### Prompt 1 — State Reconstruction

Use first:

```text
You are GPT-5.5 Thinking acting as the Apex KB semantic rerun planner.

Repository: leela-spec/apexai-os-meta
Branch: main
Target KB: apex-meta/kb/old-apex-full-orchestration-agent-kb/

Task: Reconstruct current state before rerunning the LLM-owned semantic phases.

Read the live Apex KB skill contract and the target KB index, Phase 1 report, Phase 2 report, semantic continuation file, manifests/phase0 evidence, and retrieval-derived evidence if available.

Output only:
1. deterministic baseline verification,
2. semantic files that will be replaced,
3. source families to read deeply,
4. proposed new Phase 1 file set,
5. proposed new Phase 2 wiki file set,
6. stop/go verdict.

Do not write repo files yet.
```

### Prompt 2 — Phase 1 Rerun Analysis

Use after Prompt 1 returns `GO`:

```text
You are GPT-5.5 Thinking acting as the Apex KB Phase 1 semantic rerun compiler.

Target KB: apex-meta/kb/old-apex-full-orchestration-agent-kb/

The deterministic baseline is verified. Create the replacement Phase 1 ingest-analysis set.

Rules:
- Use the existing deterministic source custody and Phase 0 navigation outputs.
- Read source evidence through the KB root, not old local paths as runtime authority.
- Treat historical OpenClaw / Windows / old-agent paths as historical evidence only.
- Every analysis file must include source scope, files read, source-grounded claims, concepts, entities, contradictions/tensions, open questions, proposed Phase 2 targets, and phase gate statement.
- The exact approval phrase `approve ingest` is present for this rerun, but Phase 2 pages must still wait until Phase 1 output exists.

Write or output replacement files under:
apex-meta/kb/old-apex-full-orchestration-agent-kb/ingest-analysis/

Also write:
apex-meta/kb/old-apex-full-orchestration-agent-kb/ingest-analysis/phase1-rerun-completion-report.md
```

### Prompt 3 — Phase 2 Replacement Wiki Compile

Use after replacement Phase 1 exists:

```text
You are GPT-5.5 Thinking acting as the Apex KB Phase 2 semantic wiki compiler.

Target KB: apex-meta/kb/old-apex-full-orchestration-agent-kb/

Operator gate status: approved. Exact phrase: approve ingest.

Create the replacement Phase 2 wiki layer from the new Phase 1 analysis.

Rules:
- Replace/update existing wiki summaries, concepts, entities, and index.
- Do not preserve thin old pages just because they exist.
- Each page must implement the Apex page value contract: Adaptive Ranked Source Set, Macro/Meso/Micro synthesis, Key Claims with source pointers and labels, Routes Here, and Uncertainty / Raw Source Triggers.
- Treat old runtime paths as historical source evidence only.
- Preserve finalized deterministic lint concepts: repo execution routing safety and historical path authority safety.
- Keep source refs and confidence labels explicit.

Allowed writes:
- wiki/summaries/*.md
- wiki/concepts/*.md
- wiki/entities/*.md
- wiki/index.md
- audit/*.md
- log/phase2-rerun-compile-report.md

Forbidden writes:
- raw/
- manifests/source-manifest.json
- manifests/phase0/
- derived/search/
- apex-meta/scripts/
- .claude/
- Apex Plan/Sync/Session/PreCap/FlowRecap/APSU surfaces
```

### Prompt 4 — Codex Postflight Prompt

Use after Phase 2 replacement files are present:

```text
You are Codex acting as deterministic Apex KB postflight executor.

Repo: leela-spec/apexai-os-meta
Branch: main
KB_ROOT=apex-meta/kb/old-apex-full-orchestration-agent-kb

Work directly on main. Do not create a branch. Do not open a PR.
Do not stop for unrelated dirty files unless they overlap KB_ROOT, apex-meta/scripts, or .claude/skills/apex-kb.

Run exactly:
python apex-meta/scripts/apex_kb.py --kb-root "$KB_ROOT" --allow-write index
python apex-meta/scripts/apex_kb_retrieval.py --kb-root "$KB_ROOT" --allow-write build-index
python apex-meta/scripts/apex_kb_retrieval.py --kb-root "$KB_ROOT" stale
python apex-meta/scripts/apex_kb.py --kb-root "$KB_ROOT" --json lint
python apex-meta/scripts/apex_kb.py --kb-root "$KB_ROOT" --json audit
python apex-meta/scripts/apex_kb.py --kb-root "$KB_ROOT" --json status

Then write:
$KB_ROOT/log/semantic-rerun-postflight-report.md

The report must include command results, changed files, index status, retrieval status, lint/audit/status verdicts, and remaining warnings.

Commit and push only the replacement semantic files and postflight outputs.
```

## Required Final Report From the Other Chat

```yaml
FINAL_REPORT:
  verdict: PASS | PASS_WITH_WARNINGS | FAIL
  kb_root: apex-meta/kb/old-apex-full-orchestration-agent-kb
  deterministic_baseline_verified: true | false
  phase1_replaced: true | false
  phase2_replaced: true | false
  postflight_prompt_created: true | false
  files_to_replace:
    ingest_analysis: []
    wiki: []
    audit: []
    log: []
  codex_required_next: true
  limitations: []
```

## Non-Goals

- Do not redesign Apex KB.
- Do not patch `apex_kb.py` or retrieval scripts during semantic rerun.
- Do not rerun source-intake or Phase 0 unless verification proves deterministic baseline is missing.
- Do not use historical old-agent paths as current runtime authority.
- Do not append another partial continuation layer when the task is replacement.
