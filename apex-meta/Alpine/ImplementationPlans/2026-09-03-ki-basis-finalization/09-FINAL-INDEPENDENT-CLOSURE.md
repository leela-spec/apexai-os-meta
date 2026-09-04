# Module 09 — Final Independent Closure

## Target

Fresh independent audit of the current platform + CLI-reasoning/Hermes-routing bridge. The final product skill library is explicitly outside this closure because the operator will supply it later. Implementation agents do not certify themselves.

## Verifier input

Give the fresh verifier only:

- current accepted architecture file;
- current `compose.yaml`;
- current verification/backup/restore scripts;
- current Hermes skill sources;
- current sanitized target acceptance evidence;
- live runtime access;
- this final acceptance list.

Do not provide implementation success prose as authority.

## Final acceptance

Verify independently:

1. accepted Windows/Hyper-V Linux-container runtime remains intact;
2. Docker Dashboard is not required for routine operation;
3. seven canonical services remain on `ki-basis-net`;
4. PostgreSQL/Valkey remain internal-only;
5. Hermes has no Docker socket or legacy WSL bind;
6. no tracked real secrets;
7. backup/restore/auth hardening from M01-M04 remains intact;
8. Hermes official API server is enabled, authenticated and published loopback-only on port 8642;
9. invalid Hermes API key is rejected;
10. `invoke-hermes.ps1` succeeds with valid key and does not contain product business logic;
11. Hermes has one configured provider and can answer a non-sensitive API request;
12. architecture clearly distinguishes upstream CLI reasoning from Hermes' own provider-backed routing/tool execution;
13. no permanent parallel direct-product CLI-agent control logic has been created;
14. full Firefly/Paperless/OpenProject skill implementation and `ki-basis-control` are explicitly deferred until real skills arrive;
15. Docker Desktop restart restores the bridge and seven-service runtime;
16. Docker Desktop/Windows research provenance is preserved;
17. performance tuning remains evidence-gated;
18. privacy documentation does not falsely claim OpenRouter is private merely because an upstream CLI agent performs heavy reasoning.

Not required for current PASS:

- final product skills;
- `ki-basis-control` bundle;
- cross-application skill proof;
- write-capable skills;
- fully local model runtime;
- manual Hyper-V Linux-VM migration;
- forced Windows reboot before the next natural reboot;
- off-host backup platform;
- speculative resource tuning.

Return only:

`PASS | PASS_WITH_LIMITATIONS | CORRECTION_REQUIRED | BLOCKED_HUMAN_GATE | FAIL`

For any non-PASS result, give the smallest correction; do not reopen architecture.

No push. STOP.
