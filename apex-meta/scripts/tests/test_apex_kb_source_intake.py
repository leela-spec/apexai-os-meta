import argparse
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "apex_kb.py"
SPEC = importlib.util.spec_from_file_location("apex_kb_under_test_source_intake", MODULE_PATH)
assert SPEC and SPEC.loader
apex_kb = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(apex_kb)


def args(kb_root: Path, **overrides):
    values = {
        "kb_root": str(kb_root),
        "allow_write": True,
        "dry_run": False,
        "source_path": None,
        "source_root": None,
        "pointer": None,
        "source_id": None,
        "title": None,
        "source_type": "other",
        "storage_mode": "copy_into_kb",
        "as_version": False,
        "allow_duplicate": False,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


class RecursiveSourceRootIntakeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.kb = Path(self.temp.name) / "kb"
        self.kb.mkdir(parents=True)
        (self.kb / "manifests").mkdir()
        (self.kb / "manifests" / "source-manifest.json").write_text(
            json.dumps({"schema_version": "1.0", "sources": []}), encoding="utf-8"
        )
        self.source_root = Path(self.temp.name) / "source"
        self.source_root.mkdir()
        (self.source_root / "doc.md").write_text("# Doc\n", encoding="utf-8")
        (self.source_root / "image.bin").write_bytes(b"\x00\x01\x02\x03")

    def tearDown(self):
        self.temp.cleanup()

    def test_pointer_only_recursive_intake_creates_zero_raw_files(self):
        result = apex_kb.cmd_source_intake(
            args(self.kb, source_root=str(self.source_root), storage_mode="pointer_only", source_type="ref")
        )
        self.assertEqual(result["status"], "ok")
        self.assertEqual(result["file_count"], 2)
        raw_dir = self.kb / "raw"
        raw_files = [p for p in raw_dir.rglob("*") if p.is_file()] if raw_dir.exists() else []
        self.assertEqual(raw_files, [], "pointer_only recursive intake must not copy any file into raw/")
        manifest = json.loads((self.kb / "manifests" / "source-manifest.json").read_text(encoding="utf-8"))
        modes = {entry["source_storage_mode"] for entry in manifest["sources"]}
        types = {entry["source_type"] for entry in manifest["sources"]}
        self.assertEqual(modes, {"pointer_only"})
        self.assertEqual(types, {"ref"})
        original_paths = {Path(entry["source_path"]).name for entry in manifest["sources"]}
        self.assertEqual(original_paths, {"doc.md", "image.bin"})

    def test_copy_into_kb_recursive_intake_still_copies(self):
        result = apex_kb.cmd_source_intake(
            args(self.kb, source_root=str(self.source_root), storage_mode="copy_into_kb")
        )
        self.assertEqual(result["status"], "ok")
        raw_files = sorted(p.name for p in (self.kb / "raw").rglob("*") if p.is_file())
        self.assertEqual(raw_files, ["doc.md", "image.bin"])
        manifest = json.loads((self.kb / "manifests" / "source-manifest.json").read_text(encoding="utf-8"))
        modes = {entry["source_storage_mode"] for entry in manifest["sources"]}
        self.assertEqual(modes, {"copy_into_kb"})

    def test_all_file_types_stay_custody_visible_regardless_of_storage_mode(self):
        # Non-text files (e.g. image.bin) must still be inventoried, not silently dropped -
        # this is the correct, intentional M2 behavior; only the storage mode was ever the bug.
        result = apex_kb.cmd_source_intake(
            args(self.kb, source_root=str(self.source_root), storage_mode="pointer_only")
        )
        self.assertEqual(result["file_count"], 2)


if __name__ == "__main__":
    unittest.main()
