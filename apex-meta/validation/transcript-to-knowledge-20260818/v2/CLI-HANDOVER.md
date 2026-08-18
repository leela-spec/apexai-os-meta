# Handover — Install and Run Transcript-to-Knowledge v2 from a CLI

## Mission for the receiving CLI/agent

Install/use the repository-local `transcript-to-knowledge` skill and complete one transcript-to-wiki run without depending on Apex KB.

The deterministic CLI never calls an LLM or the web. A capable semantic agent fills Map/Reduce result JSON; optional live research fills verification result JSON.

## 1. Repository preflight

From the repo root on Windows PowerShell:

```powershell
git status -sb
git pull --ff-only origin main
```

Do not create a branch for this project workflow unless the operator explicitly changes the repository policy.

Skill path:

```text
.claude/skills/transcript-to-knowledge/
```

## 2. Runtime preflight

```powershell
$Skill = ".\.claude\skills\transcript-to-knowledge"
py -3 "$Skill\scripts\ttk.py" doctor
```

Expected:

```text
python_ok: True
stdlib_only: True
network_calls_in_cli: False
llm_calls_in_cli: False
```

If `py -3` is unavailable, try `python`. Python must be >= 3.10.

No `pip install` is required for the core pipeline.

## 3. Run deterministic tests before real work

```powershell
py -3 "$Skill\scripts\test_ttk.py" -v
```

Publication baseline: 12 tests passing.

## 4. Initialize a real transcript run

Set paths:

```powershell
$Source = ".\input\episode-01.json"
$Run = ".\artifacts\transcript-knowledge\episode-01"
```

Initialize:

```powershell
py -3 "$Skill\scripts\ttk.py" init "$Source" --output "$Run"
```

Alternative wrapper:

```powershell
& "$Skill\scripts\prepare-transcript.ps1" -InputPath "$Source" -OutputPath "$Run"
```

Supported: Whisper/faster-whisper/WhisperX JSON/JSONL/NDJSON, SRT, VTT, TXT, Markdown.

## 5. Inspect diagnostics before semantic work

```powershell
Get-Content "$Run\source\diagnostics.json"
Get-Content "$Run\manifest.json"
```

Do not “repair” missing timing or speakers by invention. If the transcript itself is materially bad, stop and improve the source/ASR first.

## 6. Map loop

Ask for the exact next work item:

```powershell
py -3 "$Skill\scripts\ttk.py" next "$Run" --json-output
```

For a Map stage it returns:

- packet path;
- expected result path;
- packet SHA-256;
- semantic contract pointer.

The semantic agent must:

1. read the exact Map packet;
2. read `.claude/skills/transcript-to-knowledge/references/semantic-contracts.md`, section **Map result**;
3. write only the requested `work/results/map/window-XXXX.json`;
4. use exact segment refs/quotes;
5. never cite `context_only` segments;
6. repeat `next` until no Map work remains.

Validate periodically:

```powershell
py -3 "$Skill\scripts\ttk.py" validate "$Run"
```

A bad window does not require rerunning valid windows.

## 7. Build Reduce packet

When `status` says `reduce_packet_ready`:

```powershell
py -3 "$Skill\scripts\ttk.py" make-reduce "$Run"
```

This creates the evidence ledger and `work/packets/reduce.json`.

The Reduce semantic worker reads that compact packet—not the full raw transcript by default—and writes `work/results/reduce.json` per the contract.

## 8. Selective external verification

After Reduce validates:

```powershell
py -3 "$Skill\scripts\ttk.py" make-verify "$Run" --min-checkworthiness medium
```

Only factual, supported-enough, medium/high check-worthy claims enter the queue.

If web research is available, write `work/results/verify/results.json` per the external verification contract. If not, skip it; the compiler marks those facts `[UNVERIFIED]`.

Do not convert transcript support into a factual verdict. A source-supported speaker assertion may still be externally contradicted.

## 9. Compile

```powershell
py -3 "$Skill\scripts\ttk.py" compile "$Run"
py -3 "$Skill\scripts\ttk.py" validate "$Run" --complete
```

Final outputs are under `$Run\wiki`.

## 10. Resume after interruption

Never reconstruct state from chat history. Run:

```powershell
py -3 "$Skill\scripts\ttk.py" status "$Run" --json-output
py -3 "$Skill\scripts\ttk.py" next "$Run" --json-output
```

Important states:

- `map`: fill the specified Map result;
- `map_invalid`: fix only invalid result(s);
- `reduce_packet_ready`: run `make-reduce`;
- `reduce`: fill Reduce result;
- `reduce_invalid`: fix Reduce result;
- `verify_queue_ready`: run `make-verify`;
- `verify_invalid`: repair/remove invalid verification result;
- `compile_ready`: compile now;
- `compile_stale`: upstream semantic/verification result changed; compile again;
- `compiled`: current compiled artifacts match upstream hashes.

## 11. Do not install these by default

Do not add:

- Apex KB;
- LangChain/LlamaIndex runtime;
- graph DB;
- vector DB;
- workflow engine;
- hosted LLM SDK;
- local entailment model;
- ASR model.

Only add an adapter after a real need appears.

## 12. Optional audio path

If the input is audio rather than a transcript, treat ASR as a separate benchmarked stage. For Intel Windows targets, compare OpenVINO GenAI Whisper on GPU against faster-whisper CPU/int8 rather than assuming the NPU is reliable. Chunk long audio before ASR until current backend behavior is proven stable. WhisperX is optional when speaker diarization/forced alignment materially improves the use case.

## 13. Completion receipt

Before declaring success, capture:

```powershell
py -3 "$Skill\scripts\ttk.py" status "$Run" --json-output
py -3 "$Skill\scripts\ttk.py" validate "$Run" --complete --json-output
Get-ChildItem "$Run\wiki" -Recurse
```

Success means validation exits 0, `complete=true`, `compiled_current=true`, and the generated wiki is inspectable without Apex KB.
