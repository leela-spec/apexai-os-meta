# Project Status Package Manifest

```yaml
package_manifest:
  package_name: ProjectStatus
  package_path: .claude/skills/ProjectStatus/
  entrypoint: project-status-overview_SKILL_v3.md
  primary_output: current_project_status_overview
  files:
    - project-status-overview_SKILL_v3.md
    - project-status-overview-contract_v2_fixed.md
    - project-status-overview-template.md
    - current-project-status-overview-template.md
    - ranking-and-validation-rules.md
    - starter-manual-test-overview.md
    - package-manifest.md
  promoted_operator_template:
    artifact_id: J11
    path: project-status-overview-template.md
  truth_boundary: confirmed_durable_sources_only
```
