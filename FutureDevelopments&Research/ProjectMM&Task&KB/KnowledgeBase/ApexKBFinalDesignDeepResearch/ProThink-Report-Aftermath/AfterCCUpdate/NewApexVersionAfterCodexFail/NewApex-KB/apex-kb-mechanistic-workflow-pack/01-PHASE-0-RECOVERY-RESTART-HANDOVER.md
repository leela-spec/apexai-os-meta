# Apex KB Phase 0 Recovery — Fresh-Chat Handover

## Mission

Repair and prove the existing Apex KB **new-KB Start vertical slice**, then run the first real Leela **Phase 0 Setup** canary.

Do not redesign Apex KB. Do not create another patch pack, orchestration system, simulation, run ledger, Q&A version, or handover chain.

## Repository

```yaml
repository: leela-spec/apexai-os-meta
branch: main
canonical_recovery_file: FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/ApexKBFinalDesignDeepResearch/ProThink-Report-Aftermath/AfterCCUpdate/NewApexVersionAfterCodexFail/NewApex-KB/apex-kb-mechanistic-workflow-pack/00-PHASE-0-RECOVERY-CANON.okf.yaml
```

Read the canonical recovery file completely. It supersedes the older Phase 0 test packs, patch proposals, handovers, and failure-learning documents for this recovery task.

## Target behavior

A fresh Codex conversation receiving only:

```text
$apex-kb Create a new Apex KB from the Leela source corpus. Run only Phase 0 Setup and stop before deterministic corpus intelligence.
```

must begin the fixed Start configuration flow.

It must not begin with:

> Can the executor run repository Python commands in a live worktree and capture the command, exit status, stdout, and stderr?

## Work sequence

### 1. Establish live truth

Record current `main` HEAD and read these current files completely:

```text
AGENTS.md
.claude/skills/apex-kb/SKILL.md
.claude/skills/apex-kb/package-manifest.md
.claude/skills/apex-kb/references/start-input.schema.json
.claude/skills/apex-kb/references/script-command-contract.md
.claude/skills/apex-kb/references/acceptance-tests.md
.claude/skills/apex-kb/examples/lifecycle-runbook.md
.claude/skills/apex-kb/examples/powershell-commands.md
apex-meta/scripts/apex_kb.py
apex-meta/scripts/apex_kb_start.py
apex-meta/scripts/apex_kb_control.py
apex-meta/scripts/tests/test_apex_kb_start.py
```

Use the selected existing frontend field model from:

```text
FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/ApexKBFinalDesignDeepResearch/ProThink-Report-Aftermath/AfterCCUpdate/NewApexVersionAfterCodexFail/NewApex-KB/apex-kb-mechanistic-workflow-pack/templates/start-qa-option-a-v3-example-guidance.md
```

Do not create another Q&A variant.

### 2. Repair only the unfinished integration

Make the smallest coherent live edits required so that:

1. root Codex guidance routes a new Apex KB request to the live Apex KB skill;
2. the live skill routes a new KB to Start without asking the old capability question;
3. existing controlled KBs continue through `control next`, `control run`, and `control reconcile`;
4. the public `apex_kb.py start` entrypoint supports the documented Start flags and resilient flag placement;
5. package manifest, command contract, runbook, PowerShell examples, and acceptance tests describe the same Start-first lifecycle;
6. any new Start workflow reference or template is added only when the live skill actually consumes it.

Do not modify Phase 1, Phase 2, retrieval, corpus ranking, or unrelated files.

### 3. Prove the repair before any real canary

Run from one live checkout:

```powershell
python -m unittest apex-meta/scripts/tests/test_apex_kb_start.py -v
python -m unittest discover -s apex-meta/scripts/tests -p "test_apex_kb_control*.py" -v
python apex-meta/scripts/apex_kb.py start --help
```

Add and run focused regression coverage proving:

- Start help exposes the intended public flags;
- accepted global-flag placement works through `apex_kb.py start`;
- a synthetic preview creates no KB files;
- writes require explicit `--allow-write`;
- a new-KB routing fixture contains the Start route and excludes the old capability-first route;
- existing controlled-KB routing remains unchanged.

If any proof fails, repair only that failure and rerun. Do not compensate with more process documentation.

### 4. Run a fresh uncoached canary

Only after all integration proofs pass, open a fresh Codex conversation from the repository root and provide only:

```text
$apex-kb Create a new Apex KB from the Leela source corpus. Run only Phase 0 Setup and stop before deterministic corpus intelligence.
```

During the canary:

- answer only questions produced by the live Start workflow;
- verify repository, source folder, destination, topics, questions, exclusions, source handling, semantic depth, output tier, and non-text policy;
- confirm only after the generated readback is correct;
- never suggest low-level control commands manually;
- stop after Setup artifacts;
- do not run deterministic corpus intelligence, semantic work, retrieval, commit, or push of canary artifacts unless separately authorized.

## Required final report

Return one concise report containing:

```yaml
runtime_commit: ""
root_cause: ""
changed_files: []
tests:
  start: "pass | fail"
  control: "pass | fail"
  help_and_flags: "pass | fail"
  preview_no_write: "pass | fail"
canary:
  exact_prompt: ""
  first_response_class: "start_flow | old_capability_question | other"
  operator_confirmation: false
  setup_artifacts: []
  source_mutation: false
  deterministic_corpus_intelligence_started: false
  semantic_artifacts_created: false
final_status: "canary_proven | repair_tested | blocked"
remaining_blocker: null
```

Do not call the repair complete unless the fresh canary proves the Start flow. Stop before deterministic corpus intelligence.
