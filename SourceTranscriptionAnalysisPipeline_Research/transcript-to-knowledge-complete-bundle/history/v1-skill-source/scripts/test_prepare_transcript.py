from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("prepare_transcript.py")
spec = importlib.util.spec_from_file_location("prepare_transcript", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
import sys
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class TranscriptPreparationTests(unittest.TestCase):
    def test_whisperx_json_preserves_word_timestamps_and_speaker(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "sample.json"
            source.write_text(
                json.dumps(
                    {
                        "segments": [
                            {
                                "start": 1.25,
                                "end": 3.5,
                                "speaker": "SPEAKER_00",
                                "text": "A precise factual sentence.",
                                "words": [
                                    {"word": "A", "start": 1.25, "end": 1.4, "probability": 0.99},
                                    {"word": "precise", "start": 1.4, "end": 1.9, "probability": 0.98},
                                ],
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            out = root / "out"
            manifest = module.prepare(source, out, chunk_words=50, overlap_words=5)
            self.assertEqual(manifest["timestamp_quality"], "word")
            data = json.loads((out / "transcript.json").read_text(encoding="utf-8"))
            self.assertEqual(data["segments"][0]["speaker"], "SPEAKER_00")
            self.assertEqual(data["segments"][0]["start_hms"], "00:00:01.250")
            self.assertEqual(data["segments"][0]["words"][1]["end_hms"], "00:00:01.900")
            md = (out / "transcript.md").read_text(encoding="utf-8")
            self.assertIn("seg-000001", md)
            self.assertIn("A precise factual sentence.", md)

    def test_srt_cues_become_segment_anchors(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "sample.srt"
            source.write_text(
                "1\n00:00:01,000 --> 00:00:02,500\nAlice: First claim.\n\n"
                "2\n00:00:03,000 --> 00:00:04,000\nSecond claim.\n",
                encoding="utf-8",
            )
            segments, source_format = module.load_transcript(source)
            self.assertEqual(source_format, "srt")
            self.assertEqual(len(segments), 2)
            self.assertEqual(segments[0].speaker, "Alice")
            self.assertEqual(module.format_timestamp(segments[0].end), "00:00:02.500")

    def test_plain_text_never_fabricates_timestamps(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "sample.txt"
            source.write_text("No timestamp here.\n[00:01:02] Bob: Timed line.\n", encoding="utf-8")
            segments, _ = module.load_transcript(source)
            self.assertIsNone(segments[0].start)
            self.assertEqual(segments[1].start, 62.0)
            self.assertEqual(module.timestamp_quality(segments), "partial_segment")

    def test_chunk_overlap_is_bounded_and_anchor_preserving(self) -> None:
        segments = [
            module.Segment(
                id=f"seg-{i:06d}",
                text="one two three four five",
                start=float(i),
                end=float(i) + 0.5,
                speaker=None,
                words=(),
                source_pointer=f"line:{i}",
            )
            for i in range(1, 8)
        ]
        chunks = module.build_chunks(segments, chunk_words=12, overlap_words=5)
        self.assertGreater(len(chunks), 1)
        self.assertEqual(chunks[0]["segment_ids"][-1], chunks[1]["segment_ids"][0])
        self.assertEqual(chunks[0]["start_segment"], "seg-000001")

    def test_prepare_is_content_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "sample.srt"
            source.write_text(
                "1\n00:00:00,000 --> 00:00:01,000\nHello world.\n\n"
                "2\n00:00:01,100 --> 00:00:02,000\nAnother sentence.\n",
                encoding="utf-8",
            )
            out_a = root / "a"
            out_b = root / "b"
            module.prepare(source, out_a, 10, 2)
            module.prepare(source, out_b, 10, 2)
            for relative in ["manifest.json", "transcript.json", "transcript.md", "chunk-index.json", "task-plan.json"]:
                self.assertEqual(
                    (out_a / relative).read_bytes(),
                    (out_b / relative).read_bytes(),
                    relative,
                )

    def test_rejects_invalid_overlap(self) -> None:
        with self.assertRaises(module.TranscriptError):
            module.build_chunks([], chunk_words=100, overlap_words=100)


if __name__ == "__main__":
    unittest.main()
