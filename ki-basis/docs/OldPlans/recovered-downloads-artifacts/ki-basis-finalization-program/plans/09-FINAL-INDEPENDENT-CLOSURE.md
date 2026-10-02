# Module 09 — Final Independent Closure

## Target

Fresh independent audit after Modules 01–08. Implementation agents do not certify themselves.

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

1. Docker Desktop target / WSL source separation.
2. Exactly seven canonical services on `ki-basis-net`.
3. DB/cache not host-published.
4. Hermes has no Docker socket or legacy WSL bind.
5. No tracked real secrets.
6. Fresh backup fails closed on required-artifact failure.
7. Fresh target backup includes required DB/user data and state volumes.
8. Disposable Paperless restore matches an independent SHA fixture.
9. OpenRouter/provider is configured without revealing key.
10. `paperless-local` skill calls real Paperless API.
11. `firefly-local` skill calls real Firefly API.
12. `openproject-local` skill calls real OpenProject API v3.
13. Invalid app credentials fail with no fallback.
14. Operator can access Hermes through the chosen local access surface.
15. Windows cold reboot leaves target healthy.
16. One verified second-copy backup exists off the laptop's primary storage failure domain.
17. Documentation reflects current target and clearly marks historical source evidence.
18. Performance tuning remains evidence-gated, not speculative.

Return only:

`PASS | PASS_WITH_LIMITATIONS | CORRECTION_REQUIRED | BLOCKED_HUMAN_GATE | FAIL`

For any non-PASS result, give the smallest correction; do not reopen architecture.

No push. STOP.
