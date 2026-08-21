import importlib.util
import subprocess
import sys
import unittest
from pathlib import Path


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

        spec = importlib.util.spec_from_file_location("transcribe", SCRIPT_PATH)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertEqual(module.format_srt_timestamp(3661.234), "01:01:01,234")


if __name__ == "__main__":
    unittest.main()
