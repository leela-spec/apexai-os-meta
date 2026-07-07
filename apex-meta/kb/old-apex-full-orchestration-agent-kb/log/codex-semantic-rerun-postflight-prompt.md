# Codex Postflight Prompt — Old Agent KB Semantic Rerun

Repo: `leela-spec/apexai-os-meta`
Branch: `main`
KB root: `apex-meta/kb/old-apex-full-orchestration-agent-kb`

Work directly on `main`. Do not create a branch. Do not open a PR. Do not stop for unrelated dirty files unless they overlap the KB root, `apex-meta/scripts/`, or `.claude/skills/apex-kb/`.

Run exactly:

```bash
KB_ROOT="apex-meta/kb/old-apex-full-orchestration-agent-kb"
python apex-meta/scripts/apex_kb.py --kb-root "$KB_ROOT" --allow-write index
python apex-meta/scripts/apex_kb_retrieval.py --kb-root "$KB_ROOT" --allow-write build-index
python apex-meta/scripts/apex_kb_retrieval.py --kb-root "$KB_ROOT" stale
python apex-meta/scripts/apex_kb.py --kb-root "$KB_ROOT" --json lint
python apex-meta/scripts/apex_kb.py --kb-root "$KB_ROOT" --json audit
python apex-meta/scripts/apex_kb.py --kb-root "$KB_ROOT" --json status
```

Then write:

```text
apex-meta/kb/old-apex-full-orchestration-agent-kb/log/semantic-rerun-postflight-report.md
```

The report must include command results, changed files, index status, retrieval status, lint/audit/status verdicts, and remaining warnings.

Commit and push only semantic rerun files and postflight outputs.
