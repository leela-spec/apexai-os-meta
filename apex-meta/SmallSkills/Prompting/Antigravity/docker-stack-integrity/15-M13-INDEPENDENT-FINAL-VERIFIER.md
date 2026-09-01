# M13 — Independent Final Integrity Verifier

## Goal

Independently verify the complete post-correction repository and live Docker state after M01-M12, then replace the premature overall PASS with the verdict actually supported by current evidence.

## Depends on

M01-M12 PASS.

## Verifier independence

Use a fresh Antigravity verifier/auditor context. Do not give it the implementation narrative as authority. Give it:

- current branch/head;
- this module;
- compact program state;
- M01-M12 result paths;
- actual repository/runtime targets to inspect.

The verifier must inspect live Git/runtime evidence itself and may use module results only to locate claims/evidence.

## Required active context

Load only:

- correction control files;
- this module;
- `apex-meta/Alpine/INTEGRITY-CORRECTION-STATE.md`;
- M01-M12 compact result files;
- current `ki-basis/compose.yaml`;
- current `ki-basis/.env.example`;
- `.gitignore`;
- current nginx config;
- current canonical architecture/plan manifests from M06/M12;
- durable Hermes connector definitions from M08;
- backup/restore tooling and manifests from M09/M10;
- live Docker runtime.

Do not preload old chat transcripts or the pre-correction implementation plans.

## Verification matrix

### V01 — Secret/file hygiene

- `ki-basis/.env` is ignored;
- `.env.example` remains tracked;
- required secrets fail closed when absent;
- no real secrets are tracked.

### V02 — Image reproducibility

- all seven service images are pinned to tested exact versions/digests or explicitly justified immutable-equivalent references;
- no unapproved `latest` remains.

### V03 — Port truth

- Hermes dashboard/gateway labels match actual runtime endpoints everywhere;
- all human-facing ports remain localhost-only unless explicitly authorized;
- PostgreSQL/Valkey remain unexposed.

### V04 — Plan/authority integrity

- moved Antigravity links resolve;
- one canonical implementation-plan family is obvious;
- no equally authoritative duplicate sequence remains.

### V05 — OpenProject persistence

- no orphaned declared volume;
- required assets/attachments survive recreate.

### V06 — Hermes connector reproducibility

- connector/skill definitions are source-controlled without secrets;
- actual Hermes discovers them;
- authenticated reads against Firefly, Paperless and OpenProject succeed over Docker DNS;
- invalid credentials fail;
- Docker socket remains absent.

### V07 — Backup completeness

- every required state source maps to a backup artifact/procedure;
- full checksums exist;
- procedure fails on deliberate backup error rather than reporting success.

### V08 — Restore integrity

- disposable restore uses actual backed-up data;
- actual Paperless (or approved equivalent product) retrieves the restored object through its supported interface/API;
- live stack remains unchanged.

### V09 — nginx truth

- every retained advertised route works through actual nginx to the real product;
- removed unsupported routes are no longer advertised;
- nginx syntax negative test fails as expected.

### V10 — Architecture documentation truth

- current architecture matches rendered Compose/live runtime;
- historical design input is clearly distinguished;
- links resolve.

### V11 — Scope integrity

- review commits from M01-M12;
- each module changed only its promised scope plus shared state/result files;
- no unrelated architecture drift or data deletion occurred.

### V12 — Cold restart

- full stack restart/recreate without volume deletion returns all required services to healthy/up state;
- known non-sensitive proof objects remain retrievable.

### V13 — Final branch/evidence integrity

- actual pushed `main` head matches reported final commit;
- working tree is clean except explicitly documented local secret/runtime files;
- all M01-M12 results exist and state says accepted through M12 before final verdict.

## Final artifact

Write:

`apex-meta/Alpine/INTEGRITY-VERIFICATION-REPORT.md`

It must include:

- exact branch/head;
- one row per V01-V13 with PASS/FAIL and concrete evidence pointer;
- unresolved limitations;
- final verdict: `PASS`, `PASS_WITH_LIMITATIONS`, `CORRECTION_REQUIRED`, or `FAIL`;
- explicit statement whether the previous `INTEGRATION-ACCEPTANCE-REPORT.md` verdict is superseded.

If final verdict is PASS, update the compact program state to COMPLETE. Do not rewrite the historical acceptance report to hide the earlier premature verdict; link/supersede it transparently.

## Adversarial rule

If any test merely proves configuration intent rather than runtime behavior, downgrade it and inspect the actual target. If any required evidence is missing, do not infer success from prior agent prose.

## Acceptance

M13 itself passes only when the independent verifier can reproduce the required evidence and the final report is committed on the actual pushed branch head.

Commit only final verification/state/supersession documentation and STOP the program.