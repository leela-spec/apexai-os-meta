# meta-release-v0.1 RELEASE_NOTES

## Summary

`meta-release-v0.1` is the first bootstrap release candidate for the ApexAI_OS Meta Operating Core.

It captures the accepted governance, routing, ritual, agent-seed, agent-KB, knowledge, process, and companion-doc surfaces merged through bootstrap PR #1.

## Accepted source

```yaml
repo: leela-spec/apexai-os-meta
branch: main
commit: ec2eeaed4b713eb16b842c33322a85c1862c6eb1
bootstrap_pr: 1
```

## What this release contains

- root repo governance shell
- managed constitutional rules
- managed ritual protocols
- first-wave agent seed files
- first-wave five-file agent KB scaffold
- managed knowledge surfaces
- managed process surfaces
- companion docs
- learning inbox placeholder

## What this release intentionally excludes

- runtime/server config
- user memory and identity surfaces
- staging/research folders
- raw project data
- credentials or secrets

## Runtime config boundary

`managed/config/openclaw.json` is not included.

Reason:

- it is runtime/server-local config
- it still belongs behind manual review
- config must not silently host markdown canon or release truth

## Project template boundary

The project template is not fully materialized in this release PR.

`templates/project/` remains a placeholder and should be filled by the next staged PR.

## Release interpretation

This is a commit-anchored release manifest.

The canonical payload is the accepted root-level meta operating core at the commit named in `MANIFEST.md`, not a duplicated second copy of every file under `releases/`.

## Follow-up PRs

Recommended next PRs:

1. Materialize `templates/project/` from the accepted meta core.
2. Add a first project repo scaffold or project-template export package.
3. Add release tagging only after the manifest and template posture are accepted.
