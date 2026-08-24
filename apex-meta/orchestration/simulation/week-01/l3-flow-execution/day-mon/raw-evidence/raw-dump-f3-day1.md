Blocked — failing closed rather than fabricating.

**Missing input:** `/root/workspaces/Investment` does not exist in this environment.

What I checked (real execution log):

```
$ git -C /root/workspaces/Investment ...  → fatal: not a git repository
$ ls /root/workspaces/
  apexai-os-meta            # only directory present
$ find /root/workspaces/apexai-os-meta -type f
  5 files, all orchestration-simulation docs (APEX-E2E-SIM-2W-01),
  no Investment/IPOS code, no configs/, no ipos/ package
$ ls /mnt → empty (no Windows host mount available in this container)
```

The session snapshot claims `/root/workspaces/Investment` on branch `main` with `ipos/advisor/rule_engine.py`, `configs/registry.yaml`, etc., but none of those paths exist here — this docker backend has no access to that filesystem.

I will not invent indicator definitions, pandera schemas, or rule tilts against a registry file (`configs/registry.yaml`, `registry_120.yaml`) I cannot read — the whole point of the Day-1 audit is grounding in the actual 22-indicator registry and existing rule engine, so fabricated output would poison the macro-series expansion downstream.

To unblock, one of:
1. Point me at the correct path / mount containing the Investment repo in this environment.
2. Clone it: give me the remote URL (and credentials if private) and I'll clone into `/root/workspaces/Investment`.
3. Copy the tree into the container (e.g. `docker cp` or tar over stdin).

Once the repo is present I'll proceed with the full Day-1 scope: audit of `rule_engine.py` + both registries, formulated indicator definitions, pandera schemas, macro-rule tilts, and raw test/code logs written to the evidence paths.