# Transcript Pipeline V4

The V4 runner turns an HTTP/HTTPS media URL, a local audio/video file, or an existing transcript into a normalized transcript and a local knowledge artifact.

```powershell
.\scripts\transcript_pipeline_v4\run_v4.ps1 -Source <URL-or-path> [-Language en|de] [-Force]
```

The selected local path is fixed:

- URL acquisition: `yt-dlp` with FFmpeg, using the source's yt-dlp ID.
- ASR: `transcribe.py` with faster-whisper `large-v3-turbo`, CPU/int8, and VAD.
- Knowledge transform: Fabric `extract_wisdom` through vendor `Ollama`, model `qwen3.5:9b`, context length `65536`, and thinking `off`.

Outputs are written below `artifacts/transcript_pipeline_v4/<source_id>/`:

- `transcript.txt` — deterministic UTF-8 text. SRT/VTT cue numbers, timestamps, metadata, and inline markup are removed without semantic rewriting.
- `transcript.srt` — timestamped ASR output for media inputs.
- `knowledge.md` — Fabric output.
- `run.log` — timestamped stage, tool/model, reuse, fallback, and error facts. It does not claim semantic quality.
- `source/` — downloaded URL media and yt-dlp metadata when available.

Non-empty downloaded media, `transcript.txt`, and `knowledge.md` are reused. Empty files never count as completed outputs. `-Force` regenerates transcript and knowledge while allowing already downloaded source media to be reused. Original local transcript and media files are read in place and are not copied or modified.

Prerequisites are `yt-dlp`, FFmpeg/ffprobe, Ollama with `qwen3.5:9b`, Fabric, and the Python environment prepared for `transcribe.py`. The runner prefers `scripts/transcript_pipeline_v4/.venv/Scripts/python.exe` and `%LOCALAPPDATA%\Microsoft\WinGet\Links\fabric.exe`, then falls back to commands on `PATH`.

Run the fast behavioral and ASR interface tests without downloading media or loading a model:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\transcript_pipeline_v4\tests\test_run_v4.ps1
python -m unittest discover -s .\scripts\transcript_pipeline_v4\tests -p 'test_*.py'
```

For isolated automation, `TRANSCRIPT_PIPELINE_V4_OUTPUT_ROOT` may point output to a different directory. Relative values resolve from the repository root.
