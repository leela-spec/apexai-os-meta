import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "transcribe.py"


class TranscribeCliTest(unittest.TestCase):
    def test_help_and_srt_timestamp_are_available_without_loading_a_model(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT_PATH), "--help"],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("--input", result.stdout)
        self.assertIn("--text-out", result.stdout)
        self.assertIn("--srt-out", result.stdout)
        self.assertIn("--segments-json-out", result.stdout)

        spec = importlib.util.spec_from_file_location("transcribe", SCRIPT_PATH)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertEqual(module.format_srt_timestamp(3661.234), "01:01:01,234")

    def test_write_outputs_preserves_available_asr_segment_metadata(self):
        spec = importlib.util.spec_from_file_location("transcribe", SCRIPT_PATH)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        segments = [
            SimpleNamespace(
                start=0.0,
                end=1.25,
                text=" Exact evidence ",
                avg_logprob=-0.42,
                compression_ratio=1.31,
                no_speech_prob=0.02,
                temperature=0.0,
            )
        ]

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            metadata_path = root / "transcript.segments.json"
            module.write_outputs(
                segments,
                root / "transcript.txt",
                root / "transcript.srt",
                metadata_path,
            )

            payload = json.loads(metadata_path.read_text(encoding="utf-8"))
            self.assertEqual(payload["schema_version"], "1.0")
            self.assertEqual(payload["segments"][0]["text"], "Exact evidence")
            self.assertEqual(payload["segments"][0]["avg_logprob"], -0.42)
            self.assertEqual(payload["segments"][0]["compression_ratio"], 1.31)
            self.assertEqual(payload["segments"][0]["no_speech_prob"], 0.02)


if __name__ == "__main__":
    unittest.main()
