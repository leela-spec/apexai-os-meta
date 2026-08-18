# Operator Runbook — Windows / PowerShell

## 1. Prerequisites

- Windows PowerShell or PowerShell 7.
- Python 3.10+ available as `py -3` or `python`.
- The skill folder installed or present in the repository.
- No Python packages are required by the core CLI.

From the repository root:

```powershell
py -3 .\.claude\skills\transcript-to-knowledge\scripts\ttk.py doctor
```

Expected key fields:

```text
python_ok: True
stdlib_only: True
network_calls_in_cli: False
llm_calls_in_cli: False
```

## 2. Initialize a run

```powershell
$Skill = ".\.claude\skills\transcript-to-knowledge"
$Run = ".\artifacts\transcript-knowledge\episode-01"
$Source = ".\input\episode-01.json"

py -3 "$Skill\scripts\ttk.py" init "$Source" --output "$Run"
```

Or use the wrapper:

```powershell
& "$Skill\scripts\prepare-transcript.ps1" `
  -InputPath "$Source" `
  -OutputPath "$Run"
```

Supported transcript inputs:
- Whisper/faster-whisper/WhisperX-style JSON/JSONL/NDJSON;
- SRT;
- WebVTT;
- timestamped or untimed TXT/Markdown.

The run directory is self-contained. Initialization refuses to overwrite a non-empty directory unless it is byte/config-equivalent to the same existing run.

## 3. Inspect source diagnostics

```powershell
Get-Content "$Run\source\diagnostics.json"
Get-Content "$Run\windows\index.json"
```

Diagnostics report missing timing/speakers, timestamp ordering problems, large gaps, consecutive duplicate text, and low word-confidence counts when probabilities exist. They do not invent corrections.

## 4. Run the semantic Map loop

```powershell
py -3 "$Skill\scripts\ttk.py" next "$Run" --json-output
```

The output points at a Map packet such as:

```text
work/packets/map/window-0001.json
```

The semantic agent reads that packet plus `references/semantic-contracts.md#1-map-result`, then writes:

```text
work/results/map/window-0001.json
```

Repeat `next` until all windows are complete.

Check at any time:

```powershell
py -3 "$Skill\scripts\ttk.py" status "$Run"
py -3 "$Skill\scripts\ttk.py" validate "$Run"
```

## 5. Build the compact evidence ledger

After every Map result is valid:

```powershell
py -3 "$Skill\scripts\ttk.py" make-reduce "$Run"
```

This creates:

```text
ledger/evidence.json
ledger/coverage.json
work/packets/reduce.json
```

The Reduce packet contains validated evidence cards rather than the full transcript.

## 6. Run the semantic Reduce step

Ask the CLI:

```powershell
py -3 "$Skill\scripts\ttk.py" next "$Run" --json-output
```

Read `work/packets/reduce.json` and write `work/results/reduce.json` using the Reduce contract.

Validate:

```powershell
py -3 "$Skill\scripts\ttk.py" validate "$Run"
```

## 7. Route fact checks

Default: verify medium/high check-worthy facts only.

```powershell
py -3 "$Skill\scripts\ttk.py" make-verify "$Run" --min-checkworthiness medium
```

The queue is:

```text
work/packets/verify-queue.json
```

If live research is available, write results to:

```text
work/results/verify/results.json
```

You may skip this semantic/web step. The compiler leaves unverified factual claims as `[UNVERIFIED]`.

## 8. Compile final wiki

```powershell
py -3 "$Skill\scripts\ttk.py" compile "$Run"
py -3 "$Skill\scripts\ttk.py" validate "$Run" --complete
```

Output:

```text
wiki/
  index.md
  compiled.json
  summaries/Macro.md
  modules/*.md
  claims/Claim-*.md
  concepts/*.md
  entities/*.md
```

All compiler-generated wikilinks are path-qualified to avoid orphan links/collisions.

## 9. Recovery

### One Map result is bad

Run `validate`; fix only the listed `work/results/map/window-XXXX.json`. Valid windows stay accepted.

### A source or packet changed

The result's echoed packet hash no longer matches. Regenerate that semantic result. Never hand-edit hashes.

### Reduce became stale

Run `make-reduce` again after Map changes. Then regenerate `work/results/reduce.json` from the new packet.

### Verification became stale

Run `make-verify` again after Reduce changes. Old verification output is rejected by queue hash.

### Wiki became stale

`status` reports `compile_stale` when a valid Reduce result or valid verification result changed after the last compile. Run `compile` again. The compiler removes only its own generated Markdown pages before rebuilding, preventing removed modules/claims from lingering.

### Need to see exactly where to continue

```powershell
py -3 "$Skill\scripts\ttk.py" next "$Run" --json-output
```

## 10. What not to install by default

Do not install or configure a vector database, graph database, LangChain/LlamaIndex runtime, workflow engine, hosted LLM SDK, or Apex KB to run this pipeline. Add those only as downstream adapters after a concrete retrieval/export requirement justifies them.
