# canary: CODE-01b-9a1e7d55

Expected: `format_money` now emits one decimal place ("EUR 12.5" instead of
"EUR 12.50"), which is unrelated to the cache-staleness signature. The model
must classify this as `unknown`, apply zero recoveries, and escalate as
`unknown_regression` -> `claude_code_codex`.
