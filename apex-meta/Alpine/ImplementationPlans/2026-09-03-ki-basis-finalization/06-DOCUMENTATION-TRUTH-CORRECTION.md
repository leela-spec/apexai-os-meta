# Module 06 — Documentation Truth Correction

## Target

Apply the supplied narrow patch. Do not reopen architecture and do not rewrite whole reports.

## Defects repaired

- redact any newly exposed Paperless token from `HANDOVER-REVIEWER-DOSSIER.md`;
- remove stale `No Git Push Performed` / `NO PUSH ENFORCED` assertions and replace them with live-state guidance;
- make `ARCHITEKTUR-BASIS.md` point to `TARGET-ACCEPTANCE-REPORT.md` as current evidence while retaining the pre-migration report as history;
- ensure target backup evidence explicitly lists Hermes data and workspace archives;
- align pgvector prose with the acceptance scope instead of treating template DBs as application acceptance targets.

## Execution

Run:

```powershell
python .\patches\PATCH-06-documentation-truth.py C:\GitDev\apexai-os-meta
```

Then inspect the diff manually.

## Acceptance

- no plaintext Paperless token in tracked dossier;
- no false no-push claim;
- architecture links to target acceptance as primary evidence;
- target report lists Hermes backup artifacts;
- documentation does not broaden pgvector requirements merely for test cosmetics.

One local docs-only commit. No push. STOP.
