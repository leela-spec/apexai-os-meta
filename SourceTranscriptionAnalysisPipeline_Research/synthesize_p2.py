"""
synthesize_p2.py
Honest Pipeline 2 adapter driving transcript_engine.py.
Validates structured semantic results against source SRT transcripts without
hardcoded domain assumptions or fabricated confirmations.
"""
import sys
import json
import argparse
from pathlib import Path

# Add parent directory to import transcript_engine
sys.path.insert(0, str(Path(__file__).resolve().parent))
from transcript_engine import KnowledgeEngine, parse_srt_spoken_text, GroundingError


def run_p2(vid: str, title: str, srt_path: str, out_dir: str, semantic_path: str = None):
    srt = Path(srt_path)
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    
    if not semantic_path or not Path(semantic_path).exists():
        print(f"[P2_SYNTHESIS_PENDING] No semantic result JSON provided for '{vid}'. Skipping P2 synthesis.", file=sys.stderr)
        sys.exit(2)
        
    sem_file = Path(semantic_path)
    try:
        data = json.loads(sem_file.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"Error parsing semantic JSON '{sem_file}': {e}", file=sys.stderr)
        sys.exit(1)
        
    spoken_text = parse_srt_spoken_text(srt) if srt.exists() else None
    
    try:
        engine = KnowledgeEngine.from_semantic_result(data, spoken_text=spoken_text)
    except GroundingError as ge:
        print(f"P2 Grounding Validation Error for '{vid}': {ge}", file=sys.stderr)
        sys.exit(1)
        
    engine.write(str(out), f"{vid}_engine_wiki", f"{title} — Research Engine Analysis")
    print(f"  P2 Engine Wiki written to {out}")
    sys.exit(0)


def main():
    parser = argparse.ArgumentParser(description="Pipeline 2 Honest Adapter")
    parser.add_argument("vid", help="Video / Source ID")
    parser.add_argument("title", help="Source title")
    parser.add_argument("srt_path", help="Path to transcript SRT file")
    parser.add_argument("out_dir", help="Output directory")
    parser.add_argument("--semantic-result", default=None, help="Path to semantic result JSON")
    
    # Also support positional semantic_result for backward compatibility
    args, unknown = parser.parse_known_args()
    
    semantic_result = args.semantic_result
    if not semantic_result and unknown:
        semantic_result = unknown[0]
        
    run_p2(args.vid, args.title, args.srt_path, args.out_dir, semantic_result)


if __name__ == '__main__':
    main()
