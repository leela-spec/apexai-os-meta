import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "prepare_web_bundle.py"


class PrepareWebBundleTest(unittest.TestCase):
    def run_cli(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT_PATH), *args],
            capture_output=True,
            text=True,
            check=False,
        )

    def test_srt_is_partitioned_at_whole_cues_without_overlap(self):
        srt = (
            "1\n00:00:00,000 --> 00:00:10,000\nEarly fact\n\n"
            "2\n00:00:10,000 --> 00:00:20,000\nMiddle fact\n\n"
            "3\n00:00:20,000 --> 00:00:30,000\nLate fact\n"
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            source = root / "transcript.srt"
            output = root / "bundle"
            source.write_text(srt, encoding="utf-8")

            result = self.run_cli(
                "--input", str(source),
                "--output", str(output),
                "--max-cues", "2",
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["preflight"]["status"], "PASS_WITH_WARNINGS")
            self.assertEqual(manifest["source"]["unit_count"], 3)
            self.assertEqual(manifest["integrity"]["parts_count"], 2)
            self.assertEqual(manifest["integrity"]["units_across_parts"], 3)
            self.assertEqual(manifest["parts"][0]["first_unit"], 1)
            self.assertEqual(manifest["parts"][0]["last_unit"], 2)
            self.assertEqual(manifest["parts"][1]["first_unit"], 3)
            self.assertEqual(manifest["parts"][1]["last_unit"], 3)
            reconstructed = []
            for part in manifest["parts"]:
                payload = json.loads((output / part["path"]).read_text(encoding="utf-8"))
                reconstructed.extend(unit["raw"] for unit in payload["units"])
            self.assertEqual("".join(reconstructed), source.read_bytes().decode("utf-8"))
            copied = output / "source" / "original.srt"
            self.assertEqual(copied.read_bytes(), source.read_bytes())
            self.assertEqual(
                manifest["source"]["sha256"],
                hashlib.sha256(source.read_bytes()).hexdigest(),
            )

    def test_txt_reconstructs_exact_source_lines(self):
        text = "alpha\n\nbeta\ngamma\n"

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            source = root / "transcript.txt"
            output = root / "bundle"
            source.write_text(text, encoding="utf-8", newline="")

            result = self.run_cli(
                "--input", str(source),
                "--output", str(output),
                "--max-utf8-bytes", "7",
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
            units = []
            for part in manifest["parts"]:
                payload = json.loads((output / part["path"]).read_text(encoding="utf-8"))
                units.extend(unit["raw"] for unit in payload["units"])
            self.assertEqual("".join(units), text)
            self.assertEqual(manifest["integrity"]["units_across_parts"], len(units))

    def test_invalid_srt_reports_all_blocking_reasons(self):
        srt = (
            "1\nnot-a-timestamp\nBroken first cue\n\n"
            "2\n00:00:05,000 --> 00:00:04,000\nBroken duration\n"
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            source = root / "broken.srt"
            output = root / "bundle"
            source.write_text(srt, encoding="utf-8")

            result = self.run_cli("--input", str(source), "--output", str(output))

            self.assertEqual(result.returncode, 2)
            manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["preflight"]["status"], "NEEDS_PREPROCESSING")
            codes = {reason["code"] for reason in manifest["preflight"]["reasons"]}
            self.assertEqual(codes, {"PARSE_FAILED", "INVALID_TIMESTAMPS"})
            for reason in manifest["preflight"]["reasons"]:
                self.assertTrue(reason["affected_ranges"])
                self.assertTrue(reason["evidence"])
                self.assertTrue(reason["remediation"])
            self.assertEqual(manifest["parts"], [])

    def test_duplicate_srt_counters_block_ambiguous_unit_identity(self):
        srt = (
            "1\n00:00:00,000 --> 00:00:01,000\nFirst\n\n"
            "1\n00:00:01,000 --> 00:00:02,000\nSecond\n"
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            source = root / "duplicate.srt"
            output = root / "bundle"
            source.write_text(srt, encoding="utf-8")

            result = self.run_cli("--input", str(source), "--output", str(output))

            self.assertEqual(result.returncode, 2)
            manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
            reasons = manifest["preflight"]["reasons"]
            self.assertIn("PARSE_FAILED", {item["code"] for item in reasons})
            self.assertTrue(any("duplicate" in item["evidence"].lower() for item in reasons))

    def test_whisper_json_carries_real_proxy_metrics_and_flags(self):
        payload = {
            "segments": [
                {
                    "start": 0.0,
                    "end": 5.0,
                    "text": "Repeated evidence",
                    "avg_logprob": -1.2,
                    "compression_ratio": 2.5,
                    "no_speech_prob": 0.7,
                    "temperature": 0.8,
                }
            ]
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            source = root / "transcript.segments.json"
            output = root / "bundle"
            source.write_text(json.dumps(payload), encoding="utf-8")

            result = self.run_cli("--input", str(source), "--output", str(output))

            self.assertEqual(result.returncode, 0, result.stderr)
            manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["preflight"]["accuracy_assessed"], "asr_proxy_only")
            warning_codes = {warning["code"] for warning in manifest["preflight"]["warnings"]}
            self.assertIn("ASR_RISKY_SEGMENTS", warning_codes)
            part = json.loads((output / manifest["parts"][0]["path"]).read_text(encoding="utf-8"))
            self.assertEqual(part["units"][0]["asr"]["avg_logprob"], -1.2)
            self.assertEqual(part["units"][0]["asr"]["compression_ratio"], 2.5)


if __name__ == "__main__":
    unittest.main()
