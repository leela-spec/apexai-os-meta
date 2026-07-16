#!/usr/bin/env python3
"""Integration checks that run after the patch is applied to the live repo."""

from __future__ import annotations

import argparse
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parents[1]
CORE_PATH = SCRIPT_DIR / "apex_kb.py"
CONTROL_PATH = SCRIPT_DIR / "apex_kb_control.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@unittest.skipUnless(CORE_PATH.exists() and CONTROL_PATH.exists(), "run after applying the patch pack to the repository")
class ApexKbControlIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.core = load_module("apex_kb_live_for_control_tests", CORE_PATH)
        cls.control = load_module("apex_kb_control_live_for_tests", CONTROL_PATH)

    def test_live_parser_exposes_nested_control_commands(self):
        parser = self.core.build_parser()
        parsed = parser.parse_args(
            [
                "--kb-root",
                "apex-meta/kb/example",
                "control",
                "next",
            ]
        )
        self.assertEqual(parsed.command, "control")
        self.assertEqual(parsed.control_action, "next")

    def test_source_root_intake_keeps_unsupported_files_visible(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            kb = root / "kb"
            source = root / "source"
            source.mkdir()
            (source / "readme.md").write_text("# Read me\n", encoding="utf-8")
            (source / "diagram.bin").write_bytes(b"\x00\x01\x02\x03")

            scaffold_args = argparse.Namespace(
                kb_root=str(kb),
                allow_write=True,
                dry_run=False,
                title="Fixture",
                topic_title=None,
                force=False,
            )
            self.core.cmd_scaffold(scaffold_args)
            intake_args = argparse.Namespace(
                kb_root=str(kb),
                allow_write=True,
                dry_run=False,
                source_root=str(source),
                source_path=None,
                pointer=None,
                source_id=None,
                title=None,
                source_type="other",
                storage_mode="copy_into_kb",
                as_version=False,
                allow_duplicate=False,
            )
            result = self.core.cmd_source_intake(intake_args)
            self.assertEqual(result["status"], "ok")
            self.assertEqual(result["file_count"], 2)
            self.assertEqual((kb / "raw/other/diagram.bin").read_bytes(), b"\x00\x01\x02\x03")
            manifest = json.loads((kb / "manifests/source-manifest.json").read_text(encoding="utf-8"))
            originals = {Path(item["original_source_path"]).name for item in manifest["sources"]}
            self.assertEqual(originals, {"diagram.bin", "readme.md"})


if __name__ == "__main__":
    unittest.main()
