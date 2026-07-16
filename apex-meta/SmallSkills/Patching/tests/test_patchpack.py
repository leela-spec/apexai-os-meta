import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "patchpack.py"
SPEC = importlib.util.spec_from_file_location("patchpack_under_test", MODULE_PATH)
assert SPEC and SPEC.loader
patchpack = importlib.util.module_from_spec(SPEC)
sys.modules["patchpack_under_test"] = patchpack
SPEC.loader.exec_module(patchpack)


def git(*args, cwd):
    subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True)


def init_repo(root: Path) -> str:
    root.mkdir(parents=True, exist_ok=True)
    git("init", "-q", cwd=root)
    git("config", "user.email", "test@example.com", cwd=root)
    git("config", "user.name", "Test", cwd=root)
    (root / "target.py").write_text("VALUE = 1\nOTHER = 2\n", encoding="utf-8")
    git("add", "-A", cwd=root)
    git("commit", "-q", "-m", "initial", cwd=root)
    return patchpack.git_head(root)


def write_pack(pack_dir: Path, manifest: dict, patch_text: str, new_file_rel: str = None, new_file_content: bytes = b""):
    pack_dir.mkdir(parents=True, exist_ok=True)
    (pack_dir / "patches").mkdir(exist_ok=True)
    (pack_dir / "patches" / "N1.exact-match.md").write_text(patch_text, encoding="utf-8")
    if new_file_rel:
        dest = pack_dir / "new-files" / new_file_rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(new_file_content)
    (pack_dir / patchpack.MANIFEST_NAME).write_text(json.dumps(manifest), encoding="utf-8")


class PatchPackTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.repo = Path(self.temp.name) / "repo"
        self.pack = Path(self.temp.name) / "pack"
        self.head = init_repo(self.repo)

    def tearDown(self):
        self.temp.cleanup()

    def _manifest(self, **overrides):
        base = {
            "inspected_commit": self.head,
            "modules": [{"id": "N1", "name": "demo", "depends_on": []}],
            "existing_files_patched": ["target.py"],
            "new_files": [],
            "patch_order": ["patches/N1.exact-match.md"],
            "artifact_sha256": {},
        }
        base.update(overrides)
        return base

    def test_check_reports_ok_for_matching_block(self):
        patch_text = "<file>target.py</file>\n<old>\nVALUE = 1\n</old>\n<new>\nVALUE = 42\n</new>\n"
        write_pack(self.pack, self._manifest(), patch_text)
        report = patchpack.check_pack(self.pack, self.repo)
        self.assertEqual(report["status"], "ok")
        self.assertEqual(report["blocks"][0]["status"], "ok")

    def test_check_reports_zero_match(self):
        patch_text = "<file>target.py</file>\n<old>\nVALUE = 999\n</old>\n<new>\nVALUE = 42\n</new>\n"
        write_pack(self.pack, self._manifest(), patch_text)
        report = patchpack.check_pack(self.pack, self.repo)
        self.assertEqual(report["status"], "blocked")
        self.assertEqual(report["blocks"][0]["status"], "zero_match")

    def test_check_reports_multi_match(self):
        (self.repo / "target.py").write_text("VALUE = 1\nVALUE = 1\n", encoding="utf-8")
        patch_text = "<file>target.py</file>\n<old>\nVALUE = 1\n</old>\n<new>\nVALUE = 42\n</new>\n"
        write_pack(self.pack, self._manifest(), patch_text)
        report = patchpack.check_pack(self.pack, self.repo)
        self.assertEqual(report["status"], "blocked")
        self.assertEqual(report["blocks"][0]["status"], "multi_match")

    def test_baseline_mismatch_blocks_check(self):
        patch_text = "<file>target.py</file>\n<old>\nVALUE = 1\n</old>\n<new>\nVALUE = 42\n</new>\n"
        write_pack(self.pack, self._manifest(inspected_commit="0" * 40), patch_text)
        report = patchpack.check_pack(self.pack, self.repo)
        self.assertEqual(report["status"], "blocked")
        self.assertFalse(report["baseline_ok"])
        self.assertIn("baseline_mismatch", report)

    def test_apply_writes_content_and_creates_new_file_atomically(self):
        patch_text = "<file>target.py</file>\n<old>\nVALUE = 1\n</old>\n<new>\nVALUE = 42\n</new>\n"
        write_pack(
            self.pack,
            self._manifest(new_files=["created.md"]),
            patch_text,
            new_file_rel="created.md",
            new_file_content=b"# hello\n",
        )
        report = patchpack.apply_pack(self.pack, self.repo)
        self.assertEqual(report["status"], "ok")
        self.assertTrue(report["applied"])
        self.assertEqual((self.repo / "target.py").read_text(encoding="utf-8"), "VALUE = 42\nOTHER = 2\n")
        self.assertEqual((self.repo / "created.md").read_bytes(), b"# hello\n")
        # no leftover temp files
        leftovers = [p for p in self.repo.rglob(".*.tmp")]
        self.assertEqual(leftovers, [])

    def test_apply_refuses_when_check_is_blocked(self):
        patch_text = "<file>target.py</file>\n<old>\nVALUE = 999\n</old>\n<new>\nVALUE = 42\n</new>\n"
        write_pack(self.pack, self._manifest(), patch_text)
        original = (self.repo / "target.py").read_text(encoding="utf-8")
        report = patchpack.apply_pack(self.pack, self.repo)
        self.assertEqual(report["status"], "blocked")
        self.assertFalse(report["applied"])
        self.assertEqual((self.repo / "target.py").read_text(encoding="utf-8"), original)

    def test_apply_preserves_crlf_newline_style(self):
        # core.autocrlf=true normalizes CRLF->LF when staging, so a second commit of CRLF
        # content over identical (post-normalization) text produces no new blob. patchpack.py
        # reads/writes actual filesystem bytes regardless of git's index, so this rewrites the
        # working-tree file directly (uncommitted) against the existing baseline commit - a
        # perfectly normal real-world state (e.g. after a manual edit or an autocrlf checkout).
        (self.repo / "target.py").write_bytes(b"VALUE = 1\r\nOTHER = 2\r\n")
        patch_text = "<file>target.py</file>\n<old>\nVALUE = 1\n</old>\n<new>\nVALUE = 42\n</new>\n"
        write_pack(self.pack, self._manifest(), patch_text)
        report = patchpack.apply_pack(self.pack, self.repo)
        self.assertEqual(report["status"], "ok")
        raw = (self.repo / "target.py").read_bytes()
        self.assertIn(b"\r\n", raw)
        self.assertEqual(raw, b"VALUE = 42\r\nOTHER = 2\r\n")

    def test_verify_manifest_detects_mismatch_and_unhashed_file(self):
        patch_text = "<file>target.py</file>\n<old>\nVALUE = 1\n</old>\n<new>\nVALUE = 42\n</new>\n"
        write_pack(self.pack, self._manifest(), patch_text)
        patch_path = self.pack / "patches" / "N1.exact-match.md"
        manifest = self._manifest(artifact_sha256={"patches/N1.exact-match.md": "0" * 64})
        (self.pack / patchpack.MANIFEST_NAME).write_text(json.dumps(manifest), encoding="utf-8")
        report = patchpack.verify_manifest(self.pack)
        self.assertEqual(report["status"], "mismatch")
        statuses = {item["path"]: item["status"] for item in report["artifacts"]}
        self.assertEqual(statuses["patches/N1.exact-match.md"], "mismatch")

    def test_verify_manifest_ok_when_hashes_match(self):
        patch_text = "<file>target.py</file>\n<old>\nVALUE = 1\n</old>\n<new>\nVALUE = 42\n</new>\n"
        write_pack(self.pack, self._manifest(), patch_text)
        patch_path = self.pack / "patches" / "N1.exact-match.md"
        actual_hash = patchpack.sha256_file(patch_path)
        manifest = self._manifest(artifact_sha256={"patches/N1.exact-match.md": actual_hash})
        (self.pack / patchpack.MANIFEST_NAME).write_text(json.dumps(manifest), encoding="utf-8")
        report = patchpack.verify_manifest(self.pack)
        self.assertEqual(report["status"], "ok")

    def test_new_baseline_reports_head_and_hashes(self):
        report = patchpack.new_baseline(self.repo, ["target.py"])
        self.assertEqual(report["inspected_commit"], self.head)
        self.assertIn("target.py", report["target_hashes"])


if __name__ == "__main__":
    unittest.main()
