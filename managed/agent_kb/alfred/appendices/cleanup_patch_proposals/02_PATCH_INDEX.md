# Patch Proposal Index

| patch_file | target_file | action | depends_on | operator_status | git_apply_check | notes |
|---|---|---|---|---|---|---|
| `managed/agent_kb/alfred/appendices/cleanup_patch_proposals/0001_delete__appendices__APEX_ALFRED_CANONICAL_PATCH_DIFFS_OPTION_B.patch.diff` | `managed/agent_kb/alfred/appendices/APEX_ALFRED_CANONICAL_PATCH_DIFFS_OPTION_B.patch` | delete | source/audit/reference cleanup as applicable | pending | not_run | delete historical patch artifact after validation |
| `managed/agent_kb/alfred/appendices/cleanup_patch_proposals/0002_delete__working__APEX_VARIABLES_HANDOFF_DECISION_LOCK.md.diff` | `managed/agent_kb/alfred/working/APEX_VARIABLES_HANDOFF_DECISION_LOCK.md` | delete | source/audit/reference cleanup as applicable | pending | not_run | delete after refs; high-impact content appears promoted |
| `managed/agent_kb/alfred/appendices/cleanup_patch_proposals/0003_delete__working__APEX_ALFRED_KB_INTEGRATION_PROMPT_FLOW.md.diff` | `managed/agent_kb/alfred/working/APEX_ALFRED_KB_INTEGRATION_PROMPT_FLOW.md` | delete | source/audit/reference cleanup as applicable | pending | not_run | delete after refs; non-canonical handover prompt flow |
| `managed/agent_kb/alfred/appendices/cleanup_patch_proposals/0004_delete__working__ALFRED_WORKFLOW_DECISION_LOCK.md.diff` | `managed/agent_kb/alfred/working/ALFRED_WORKFLOW_DECISION_LOCK.md` | delete | full final high-impact check | pending | not_run | needs revision before apply |
| `managed/agent_kb/alfred/appendices/cleanup_patch_proposals/0005_delete__working__ALFRED_WORKFLOW_PREFILLED_QA.md.diff` | `managed/agent_kb/alfred/working/ALFRED_WORKFLOW_PREFILLED_QA.md` | delete | full final high-impact check | pending | not_run | needs revision before apply |
| `managed/agent_kb/alfred/appendices/cleanup_patch_proposals/0006_delete__working__APEX_ALFRED_CANONICAL_PATCH_HANDOVER.md.diff` | `managed/agent_kb/alfred/working/APEX_ALFRED_CANONICAL_PATCH_HANDOVER.md` | delete | provenance/reference check | pending | not_run | needs revision before apply |
| `managed/agent_kb/alfred/appendices/cleanup_patch_proposals/0007_delete__AGENT_CARD.md.diff` | `managed/agent_kb/alfred/AGENT_CARD.md` | delete | README/source-audit cleanup after approval | pending | not_run | exact deletion hunk embedded |
| `managed/agent_kb/alfred/appendices/cleanup_patch_proposals/0008_delete__DOCTRINE.md.diff` | `managed/agent_kb/alfred/DOCTRINE.md` | delete | README/source-audit cleanup after approval | pending | not_run | exact deletion hunk embedded |
| `managed/agent_kb/alfred/appendices/cleanup_patch_proposals/0009_delete__ROLE_BOUNDARIES.md.diff` | `managed/agent_kb/alfred/ROLE_BOUNDARIES.md` | delete | README/source-audit cleanup after approval | pending | not_run | needs revision before apply |
| `managed/agent_kb/alfred/appendices/cleanup_patch_proposals/0010_delete__HANDOFF_SCHEMA.md.diff` | `managed/agent_kb/alfred/HANDOFF_SCHEMA.md` | delete | README/source-audit cleanup after approval | pending | not_run | needs revision before apply |
| `managed/agent_kb/alfred/appendices/cleanup_patch_proposals/0011_delete__ROUTING_CONTRACT.md.diff` | `managed/agent_kb/alfred/ROUTING_CONTRACT.md` | delete | README/source-audit cleanup after approval | pending | not_run | exact deletion hunk embedded |
| `managed/agent_kb/alfred/appendices/cleanup_patch_proposals/0012_delete__WORKFLOW_PLAYBOOK.md.diff` | `managed/agent_kb/alfred/WORKFLOW_PLAYBOOK.md` | delete | README/source-audit cleanup after approval | pending | not_run | needs revision before apply |

## Stop checkpoint

No cleanup patch has been applied. Operator validation is required before any deletion or final Codex apply-instruction file can be created.
