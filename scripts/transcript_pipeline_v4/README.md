# Transcript Pipeline V4

The V4 deterministic runner turns an HTTP/HTTPS media URL, a local audio/video file, or an existing transcript into a normalized transcript artifact (`transcript.txt` and `transcript.srt`). Semantic distillation is performed downstream by the `obsidian-wiki` (`wiki-ingest`) agent skill into the cumulative vault (`knowledge/transcript-wiki/`).

```powershell
.\scripts\transcript_pipeline_v4\run_v4.ps1 -Source <URL-or-path> [-Language en|de] [-Force]
```

The selected local path is fixed:

- URL acquisition: `yt-dlp` with FFmpeg, using the source's yt-dlp ID.
- ASR: `transcribe.py` with faster-whisper `large-v3-turbo`, CPU/int8, and VAD.
- Downstream Semantic Compilation: `obsidian-wiki` (`wiki-ingest`) distilling into `knowledge/transcript-wiki/`.

Outputs are written below `artifacts/transcript_pipeline_v4/<source_id>/`:

- `transcript.txt` — deterministic UTF-8 text. SRT/VTT cue numbers, timestamps, metadata, and inline markup are removed without semantic rewriting.
- `transcript.srt` — timestamped ASR output for media inputs.
- `transcript.segments.json` — source-order segments plus available Whisper decoder metadata. These values are warning proxies, not accuracy scores.
- `run.log` — timestamped stage, tool/model, reuse, fallback, and error facts. It does not claim semantic quality.
- `source/` — downloaded URL media and yt-dlp metadata when available.

Non-empty downloaded media and `transcript.txt` are reused. Empty files never count as completed outputs. `-Force` regenerates transcript artifacts while allowing already downloaded source media to be reused. Original local transcript and media files are read in place and are not copied or modified.

Prerequisites for deterministic transcription are `yt-dlp`, FFmpeg/ffprobe, and the Python environment prepared for `transcribe.py` (with `faster-whisper`). The runner prefers `scripts/transcript_pipeline_v4/.venv/Scripts/python.exe`, then falls back to `python` on `PATH`.

Run the fast behavioral and ASR interface tests without downloading media or loading a model:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\transcript_pipeline_v4\tests\test_run_v4.ps1
python -m unittest discover -s .\scripts\transcript_pipeline_v4\tests -p 'test_*.py'
```

Prepare a deterministic upload bundle for a long transcript when needed:

```powershell
python .\scripts\transcript_pipeline_v4\prepare_web_bundle.py `
  --input .\artifacts\transcript_pipeline_v4\<source_id>\transcript.srt `
  --asr-json .\artifacts\transcript_pipeline_v4\<source_id>\transcript.segments.json `
  --output .\artifacts\transcript_pipeline_v4\<source_id>\transcript-bundle
```

The bundle partitions complete cues without overlap. Its manifest records source and part hashes, structural findings, coverage, and any original Whisper warning proxies.

Vault verification and health checks:

```powershell
python -m obsidian_wiki lint knowledge/transcript-wiki
python -m obsidian_wiki doctor
```

For isolated automation, `TRANSCRIPT_PIPELINE_V4_OUTPUT_ROOT` may point output to a different directory. Relative values resolve from the repository root.
