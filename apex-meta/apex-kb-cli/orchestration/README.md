# Apex KB CLI orchestration package

This folder is the durable continuation context for the Apex KB CLI implementation. It exists to stop repeated architecture drift, wrong-branch work, accidental clone confusion, and proxy testing that does not prove the selected product workflow.

## Start here

Open a fresh orchestrator chat and paste the complete contents of:

`00-ORCHESTRATOR-CHAT-HANDOVER.md`

The orchestrator must then read the remaining files in the order specified there.

## File map

| File | Purpose |
|---|---|
| `00-ORCHESTRATOR-CHAT-HANDOVER.md` | Master role, target lock, current status, and immediate next iteration |
| `CURRENT-STATE.yaml` | Machine-readable branch, phase, blocker, and next-task state |
| `01-TARGET-DECISIONS-AND-VALUE-MATRIX.md` | Locked decisions and value-ranked missing capabilities |
| `02-LIVE-STATE-AND-BRANCH-SAFETY.md` | Clone, branch, commit, staging, pull, and no-deletion safety rules |
| `03-DELEGATION-AND-RECONCILIATION-CONTRACT.md` | Worker types, task packets, result envelopes, and reconciliation procedure |
| `04-WORKING-CHAT-PROMPT-TEMPLATES.md` | Copy-paste templates for research, patches, execution, verification, and browser semantic runs |

## Canonical branch

```text
codex/apex-kb-cli-phase0-integration
```

The selected Phase 0 integration commit is:

```text
93c6b5342c48fb1dd97688f47eeb3f3b24450677
```

The orchestration documents were added as later commits on the same branch. Always resolve and record the current branch HEAD before delegating work.

## Immediate target

Do not redesign Phase 0 or expand retrieval. Restore the selected repository-aware semantic workflow:

```text
CLI-generated browser prompt
→ ChatGPT browser agent reads exact GitHub evidence
→ agent writes semantic artifacts, commits, and pushes
→ local CLI safely pulls and validates
→ CLI generates the next browser prompt
```

The current local incoming-JSON semantic packet is implementation truth but not the selected final workflow.

## Working principle

Every iteration must create one visible product improvement, prove it through the public path, and stop. More checks, schemas, state, or architecture are not progress unless they directly enable the selected end-to-end knowledge-base workflow.
