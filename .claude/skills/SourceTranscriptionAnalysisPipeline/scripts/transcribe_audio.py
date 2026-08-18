#!/usr/bin/env python3
"""
transcribe_audio.py
Fast, local, offline Whisper transcription powered by faster-whisper (CTranslate2).
Zero external API dependencies. Runs on local CPU or GPU.
"""

import os
import sys
import json
import time
import argparse
from pathlib import Path
from faster_whisper import WhisperModel

def format_timestamp(seconds: float) -> str:
    """Format seconds into SRT timestamp format: HH:MM:SS,mmm"""
    millis = int((seconds % 1) * 1000)
    seconds = int(seconds)
    mins, secs = divmod(seconds, 60)
    hours, mins = divmod(mins, 60)
    return f"{hours:02d}:{mins:02d}:{secs:02d},{millis:03d}"

def format_readable_time(seconds: float) -> str:
    """Format seconds into readable MM:SS or HH:MM:SS"""
    seconds = int(seconds)
    mins, secs = divmod(seconds, 60)
    hours, mins = divmod(mins, 60)
    if hours > 0:
        return f"{hours:02d}:{mins:02d}:{secs:02d}"
    return f"{mins:02d}:{secs:02d}"

def main():
    parser = argparse.ArgumentParser(description="Local Whisper audio transcription")
    parser.add_argument("--input", required=True, help="Path to input audio/video file")
    parser.add_argument("--output_dir", required=True, help="Directory to save output files")
    parser.add_argument("--model", default="base", help="Whisper model size (tiny, base, small, medium, large-v3-turbo)")
    parser.add_argument("--language", default=None, help="Language code (e.g. 'de', 'en') or omit for auto-detect")
    parser.add_argument("--device", default="cpu", choices=["cpu", "cuda", "auto"], help="Device to use")
    parser.add_argument("--compute_type", default="int8", help="Compute quantization (int8, float16, float32)")
    parser.add_argument("--beam_size", type=int, default=5, help="Beam search size")
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)
        
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    stem = input_path.stem
    print(f"Loading Whisper model '{args.model}' on {args.device} ({args.compute_type})...")
    start_load = time.time()
    
    model = WhisperModel(
        model_size_or_path=args.model,
        device=args.device,
        compute_type=args.compute_type,
        cpu_threads=os.cpu_count() or 4
    )
    print(f"Model loaded in {time.time() - start_load:.2f}s.")
    
    print(f"Transcribing '{input_path.name}' with VAD filter enabled...")
    start_transcribe = time.time()
    
    segments, info = model.transcribe(
        str(input_path),
        beam_size=args.beam_size,
        language=args.language,
        vad_filter=True,
        vad_parameters=dict(min_silence_duration_ms=500),
        word_timestamps=True
    )
    
    detected_lang = info.language
    lang_prob = info.language_probability
    duration = info.duration
    
    print(f"Detected language: '{detected_lang}' (confidence: {lang_prob*100:.1f}%), Audio duration: {duration:.1f}s")
    
    segment_list = []
    plain_text_lines = []
    srt_lines = []
    md_sections = []
    
    srt_index = 1
    for seg in segments:
        words_data = []
        if hasattr(seg, "words") and seg.words:
            for w in seg.words:
                words_data.append({
                    "word": w.word,
                    "start": round(w.start, 3),
                    "end": round(w.end, 3),
                    "probability": round(w.probability, 4)
                })

        seg_data = {
            "id": seg.id,
            "start": round(seg.start, 3),
            "end": round(seg.end, 3),
            "text": seg.text.strip(),
            "avg_logprob": getattr(seg, "avg_logprob", None),
            "no_speech_prob": getattr(seg, "no_speech_prob", None),
            "compression_ratio": getattr(seg, "compression_ratio", None),
            "temperature": getattr(seg, "temperature", None),
            "words": words_data
        }
        segment_list.append(seg_data)
        plain_text_lines.append(seg.text.strip())
        
        # SRT block
        srt_lines.append(f"{srt_index}\n{format_timestamp(seg.start)} --> {format_timestamp(seg.end)}\n{seg.text.strip()}\n")
        srt_index += 1
        
        # Markdown block
        md_sections.append(f"**[{format_readable_time(seg.start)} - {format_readable_time(seg.end)}]** {seg.text.strip()}")
        
    elapsed = time.time() - start_transcribe
    speedup = duration / max(elapsed, 0.001)
    print(f"Transcription completed in {elapsed:.2f}s ({speedup:.1f}x real-time speed).")
    
    # Write files
    txt_file = output_dir / f"{stem}.txt"
    srt_file = output_dir / f"{stem}.srt"
    json_file = output_dir / f"{stem}.json"
    md_file = output_dir / f"{stem}.md"
    
    full_text = "\n".join(plain_text_lines)
    txt_file.write_text(full_text, encoding="utf-8")
    srt_file.write_text("\n".join(srt_lines), encoding="utf-8")
    
    meta_json = {
        "audio_file": input_path.name,
        "model": args.model,
        "detected_language": detected_lang,
        "language_probability": lang_prob,
        "duration_seconds": duration,
        "processing_time_seconds": elapsed,
        "speedup_factor": speedup,
        "segment_count": len(segment_list),
        "segments": segment_list
    }
    json_file.write_text(json.dumps(meta_json, indent=2, ensure_ascii=False), encoding="utf-8")
    
    md_content = f"""# Audio Transcript: {input_path.name}

- **Language Detected:** `{detected_lang}` ({lang_prob*100:.1f}%)
- **Audio Duration:** {format_readable_time(duration)} ({duration:.1f}s)
- **Whisper Model:** `{args.model}` (Local CPU / CTranslate2)
- **Processing Time:** {elapsed:.2f}s ({speedup:.1f}x real-time)

---

## Timed Transcript

{chr(10).join(md_sections)}

---

## Full Text

{full_text}
"""
    md_file.write_text(md_content, encoding="utf-8")
    
    print(f"Saved artifacts to {output_dir}:")
    print(f"  - Plain text: {txt_file.name}")
    print(f"  - Subtitles:  {srt_file.name}")
    print(f"  - Metadata:   {json_file.name}")
    print(f"  - Markdown:   {md_file.name}")

if __name__ == "__main__":
    main()
