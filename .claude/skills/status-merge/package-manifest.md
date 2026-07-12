# Status Merge Package Manifest

```yaml
package_manifest:
  package_name: status-merge
  entrypoint: SKILL.md
  primary_output: status_merge_packet
  durable_owner: apex-session
  files:
    - SKILL.md
    - references/status-merge-packet-contract.md
    - references/next-precaphandoff-context-contract.md
    - templates/status-merge-packet-template.md
    - templates/status-merge-decision-card-template.md
    - package-manifest.md
  promoted_operator_template:
    artifact_id: J9
    path: templates/status-merge-decision-card-template.md
```
