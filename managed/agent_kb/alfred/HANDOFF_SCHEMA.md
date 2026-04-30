# HANDOFF_SCHEMA

## Status

```yaml
agent_id: alfred
file_status: absorbed_redirect
canonical_owner: managed/agent_kb/alfred/TEMPLATES.md
process_authority: managed/processes/AGENT_HANDOFF_CONTRACTS.md
secondary_canonical_owners:
  - managed/agent_kb/alfred/BEST_PRACTICES.md
  - managed/agent_kb/alfred/MISTAKES.md
redirect_reason: reusable_alfred_route_brief_and_handoff_forms_absorbed_into_TEMPLATES_process_level_handoff_authority_resolves_to_managed_processes
absorbed_in_commit: 9a7d27c37dd79bb07631ed7585b7ff8556cf544a
source_posture: no_runtime_truth_here
validator: meta_ops
review_due: 2026-07-25
```

## Redirect

This file no longer acts as an Alfred KB authority or handoff-schema authority.

Use:

- `TEMPLATES.md` for Alfred reusable intake forms, route briefs, handoff packets, escalation forms, validation challenge requests, knowledge-placement/source-gap requests, and KB repair report formats.
- `BEST_PRACTICES.md` for Alfred handoff practice, route practice, source-gap handling, EVD/IMP/RSK practice, and boundary discipline.
- `MISTAKES.md` for invalid handoff patterns, appendix-as-authority drift, template-governance confusion, source-gap hardening, and self-validation under risk.
- `managed/processes/AGENT_HANDOFF_CONTRACTS.md` for process-level first-wave agent handoff authority, standard handoff packet requirements, lifecycle rules, stop conditions, and cross-agent handoff contracts.
- `SOURCE_MANIFEST.md` and `COVERAGE_AUDIT.md` for source/audit status when handoff evidence depends on source posture.

## Maintenance rule

Do not add new handoff templates or process rules here.

Route reusable Alfred-specific forms to `TEMPLATES.md`. Route Alfred handoff practice to `BEST_PRACTICES.md`. Route invalid handoff patterns to `MISTAKES.md`. Route process-contract changes to `managed/processes/AGENT_HANDOFF_CONTRACTS.md` through the governed promotion path.

Truth-bearing or process-authority changes must not be applied through this redirect file.
