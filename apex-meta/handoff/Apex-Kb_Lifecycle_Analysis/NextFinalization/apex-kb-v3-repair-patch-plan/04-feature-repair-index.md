# Feature Repair Index

| feature | status | target plan | evidence basis | repair decision |
|---|---|---|---|---|
| `cli_flag_placement` | REPAIR_PARTIAL | `targets/006`, `targets/007`, `targets/008` | Normalization exists, but must be regression-tested and docs must match actual parser behavior. | Preserve shim; validate before and after subcommand flags. |
| `output_json` | KEEP_REAL | `targets/006`, `targets/007`, `targets/010` | `maybe_write_output_json` exists in both scripts and constrains output path under KB root. | Regression-test with PowerShell-safe path output. |
| `pointer_only_phase0` | REPLACE_STUB | `targets/001` | Pointer-only files are resolved after Phase 0 artifacts are already built; unresolved/warnings are hardcoded. | Include safe resolved text files in scanning or report unresolved. |
| `status_freshness_split` | REPAIR_PARTIAL | `targets/005` | `wiki_index_status` exists; `retrieval_index_status` is present/missing only. | Add freshness comparison to retrieval index metadata if feasible. |
| `quality_coverage` | REPLACE_STUB | `targets/002` | Maps and candidate lists exist but are empty shells. | Compute source/page maps and deterministic repair candidates. |
| `query_eval` | REPLACE_STUB | `targets/003` | Command returns path and empty arrays; no read/init/validate behavior. | Implement deterministic pack read/init/schema validation. |
| `graph_process_flow` | REPLACE_STUB | `targets/004` | Extractor returns empty arrays and writes no artifacts. | Extract deterministic edge families and optionally write JSON artifacts. |
| `script_command_contract_alignment` | DOCS_ONLY_REPAIR | `targets/008` | Contract overclaims current behavior for quality/query-eval/graph/pointer-only. | Rewrite to match repaired behavior only. |
| `kb_contract_alignment` | DOCS_ONLY_REPAIR | `targets/009` | Contract is mostly valid; add/confirm pointer-only and derived-artifact boundaries as needed. | Minimal alignment only. |
| `phase2_value_contract_alignment` | DOCS_ONLY_REPAIR | `targets/011` | Existing value contract is largely correct; quality repair should align lint/reporting language. | Keep contract, align reporting language. |
| `acceptance_tests` | DOCS_ONLY_REPAIR | `targets/010` | Current tests lack explicit pointer-only, quality, query-eval, graph acceptance checks. | Add deterministic smoke checks. |
