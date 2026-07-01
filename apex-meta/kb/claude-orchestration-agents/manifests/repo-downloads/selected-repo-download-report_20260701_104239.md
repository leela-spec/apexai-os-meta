# Apex Claude Orchestration Repo Download Report

Generated: `2026-07-01T10:42:39Z`

## Scope

Only the locked first-batch repos were included:

```yaml
first_batch_to_clone:
  - "shanraisshan/claude-code-best-practice"
  - "bmad-code-org/BMAD-METHOD"
  - "amanaiproduct/personal-os"
  - "iannuttall/claude-agents"

first_batch_to_read_only:
  - "hesreallyhim/awesome-claude-code"
  - "Aider-AI/aider"
  - "princeton-nlp/SWE-agent"
```

## Run Configuration

```yaml
target_root: 'C:\\GitDev\\apexai-os-meta\\apex-meta\\kb\\claude-orchestration-agents'
parent_repo_root: 'C:\\GitDev\\apexai-os-meta'
git_version: 'git version 2.52.0.windows.1'
dry_run: False
force: True
update: False
sparse_checkout: True
keep_nested_git_dirs: False
depth: 1
```

## Parent Git Status Before Download

```text
?? apex-meta/kb/claude-orchestration-agents/log/
?? apex-meta/kb/claude-orchestration-agents/manifests/repo-downloads/
?? apex-meta/kb/claude-orchestration-agents/raw/notes/OrchestrationAgentsInCC_RepoResearch_CC.md
?? apex-meta/kb/claude-orchestration-agents/raw/notes/OrchestrationAgentsInCC_RepoResearch_CC_FBGem.md
?? apex-meta/kb/claude-orchestration-agents/raw/notes/Untitled.md
?? apex-meta/kb/claude-orchestration-agents/raw/repos/
?? apex-meta/kb/claude-skill-design/manifests/projectrepos-corpus-intelligence/file-inventory.json
?? apex-meta/kb/lika-verein-taxes-accounting/raw/notes/ResearchAfterFirstKB/
```

## Status Counts

| Status | Count |
|---|---:|
| downloaded | 7 |

## Downloaded Tree

```text
apex-meta/kb/claude-orchestration-agents/
  raw/
    repos/
      first-batch-to-clone/
        shanraisshan__claude-code-best-practice/
        bmad-code-org__BMAD-METHOD/
        amanaiproduct__personal-os/
        iannuttall__claude-agents/
      first-batch-to-read-only/
        hesreallyhim__awesome-claude-code/
        Aider-AI__aider/
        princeton-nlp__SWE-agent/
  manifests/
    repo-downloads/
  log/
```

## Repo Results

| Repo | Group | Decision | Status | Files | Bytes | Head | Missing requested paths | Target | Error |
|---|---|---|---|---:|---:|---|---|---|---|
| `shanraisshan/claude-code-best-practice` | `first_batch_to_clone` | `must_clone_and_study` | `downloaded` | 173 | 11148676 | `9a5e4033f924` | `` | `C:\GitDev\apexai-os-meta\apex-meta\kb\claude-orchestration-agents\raw\repos\first-batch-to-clone\shanraisshan__claude-code-best-practice` |  |
| `bmad-code-org/BMAD-METHOD` | `first_batch_to_clone` | `must_clone_and_study` | `downloaded` | 512 | 3845536 | `67f4499e3130` | `` | `C:\GitDev\apexai-os-meta\apex-meta\kb\claude-orchestration-agents\raw\repos\first-batch-to-clone\bmad-code-org__BMAD-METHOD` |  |
| `amanaiproduct/personal-os` | `first_batch_to_clone` | `clone_selectively` | `downloaded` | 17 | 61327 | `34aa5918ea59` | `GOALS.md, templates/, workspace/` | `C:\GitDev\apexai-os-meta\apex-meta\kb\claude-orchestration-agents\raw\repos\first-batch-to-clone\amanaiproduct__personal-os` |  |
| `iannuttall/claude-agents` | `first_batch_to_clone` | `clone_selectively` | `downloaded` | 10 | 43487 | `f7df2c3e7395` | `` | `C:\GitDev\apexai-os-meta\apex-meta\kb\claude-orchestration-agents\raw\repos\first-batch-to-clone\iannuttall__claude-agents` |  |
| `hesreallyhim/awesome-claude-code` | `first_batch_to_read_only` | `read_only_reference` | `downloaded` | 26 | 125899 | `29755104e1f1` | `` | `C:\GitDev\apexai-os-meta\apex-meta\kb\claude-orchestration-agents\raw\repos\first-batch-to-read-only\hesreallyhim__awesome-claude-code` |  |
| `Aider-AI/aider` | `first_batch_to_read_only` | `read_only_reference` | `downloaded` | 91 | 494267 | `5dc9490bb35f` | `LICENSE, docs/` | `C:\GitDev\apexai-os-meta\apex-meta\kb\claude-orchestration-agents\raw\repos\first-batch-to-read-only\Aider-AI__aider` |  |
| `princeton-nlp/SWE-agent` | `first_batch_to_read_only` | `read_only_reference` | `downloaded` | 103 | 3416047 | `d336402e7f7e` | `` | `C:\GitDev\apexai-os-meta\apex-meta\kb\claude-orchestration-agents\raw\repos\first-batch-to-read-only\princeton-nlp__SWE-agent` |  |

## Safety Notes

- The script does not run any scripts from downloaded repositories.
- By default it strips nested `.git` folders after recording source metadata, avoiding accidental nested-repo/submodule behavior inside `apexai-os-meta`.
- Use `--keep-git` only when you explicitly want live nested clones for later `--update` runs.
- Any missing requested sparse paths are reported; they usually mean the upstream repo tree changed or the prior path claim was stale.
