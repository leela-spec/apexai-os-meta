# Normalized Evidence — F4 (apexai-os-meta, W01 tuesday)
| Sprint | Evidence Item | Normalization | Verdict |
|---|---|---|:--:|
| S1 | Structural decomposition dump (`raw-flow-dump` → normalized per raw-flow-dump-normalize v1) | normalized | PASS |
| S2 | Authored deliverable snapshot for "Rollup Sync & Fail-Closed Ledger" | normalized | PASS |
| S3 | QA/verification log with deterministic pass flags | normalized | PASS |

- Source surface routing matches `routing-ledger.jsonl` entries for F4.
- No cross-repo fact bleed detected in output diff scan.
- Provenance: simulated_execution (shadow mode); no production state touched.
