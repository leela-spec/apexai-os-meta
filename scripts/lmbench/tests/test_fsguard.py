"""VAL-01 (allowed action succeeds and is physically real) and VAL-02
(forbidden write is physically blocked) against the real filesystem broker+
fsguard pipeline -- not mocked."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.lmbench import broker, errors, fsguard, manifest, winpath


class TestFsGuardVAL01AllowedActionSucceeds(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "work").mkdir()
        self.roots = winpath.RootSet.build(
            [winpath.RootRule("WORK", str(self.root / "work"), "rw")]
        )
        self.guard = fsguard.FsGuard(self.roots)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_allowed_write_actually_lands_and_is_the_only_manifest_change(self):
        before = manifest.capture("WORK", str(self.root / "work"))

        candidate = winpath.normalize_path("ok.txt", base=str(self.root / "work"))
        self.assertIsNone(candidate.reject_code)
        self.guard.write_text(candidate.real, "hello")

        after = manifest.capture("WORK", str(self.root / "work"))
        d = manifest.diff(before, after)
        self.assertEqual(d.added, ("ok.txt",))
        self.assertEqual(d.removed, ())
        self.assertEqual(d.changed, ())
        self.assertEqual(Path(candidate.real).read_text(encoding="utf-8"), "hello")

    def test_allowed_read_returns_real_content(self):
        (self.root / "work" / "a.txt").write_text("real content", encoding="utf-8")
        candidate = winpath.normalize_path("a.txt", base=str(self.root / "work"))
        text = self.guard.read_text(candidate.real)
        self.assertEqual(text, "real content")


class TestFsGuardVAL02ForbiddenWriteBlocked(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "work").mkdir()
        (self.root / "forbidden").mkdir()
        (self.root / "forbidden" / "secret.txt").write_text("do-not-touch", encoding="utf-8")
        self.roots = winpath.RootSet.build(
            [
                winpath.RootRule("WORK", str(self.root / "work"), "rw"),
                winpath.RootRule("FORBIDDEN", str(self.root / "forbidden"), "forbidden"),
            ]
        )
        self.guard = fsguard.FsGuard(self.roots)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_broker_denies_before_any_write_is_attempted(self):
        """(a) The broker denies. No resolved path exists, so the executor has
        nothing to call fsguard with -- this is the structural half of VAL-02."""
        candidate = winpath.normalize_path("secret.txt", base=str(self.root / "forbidden"))
        pol_roots = self.roots
        from scripts.lmbench import policy

        pol = policy.build_policy(
            policy_id="P",
            policy_version="1",
            root_rules=[
                winpath.RootRule("WORK", str(self.root / "work"), "rw"),
                winpath.RootRule("FORBIDDEN", str(self.root / "forbidden"), "forbidden"),
            ],
            tool_rules=[policy.ToolRule("write_file", allowed=True)],
            action_rules=[policy.ActionRule("fs.write", "allow")],
        )
        req = broker.BrokerRequest(
            trial_id="T1",
            turn_index=0,
            call_id="c1",
            tool="write_file",
            action="fs.write",
            typed_args={"path": "secret.txt", "content": "evil"},
            target_paths=(candidate,),
        )
        decision = broker.decide(pol, req)
        self.assertEqual(decision.verdict, broker.VERDICT_DENY)
        self.assertEqual(decision.resolved_paths, ())
        # The content is untouched -- proven by direct read, not by trusting the verdict.
        self.assertEqual(
            (self.root / "forbidden" / "secret.txt").read_text(encoding="utf-8"), "do-not-touch"
        )

    def test_fsguard_independently_re_blocks_even_if_called_directly(self):
        """(b) Even if a hypothetical caller bug skipped the broker entirely
        and called fsguard straight, fsguard re-classifies the path itself
        and refuses -- this is the "physical," not "remembered `if`," half."""
        target = str(self.root / "forbidden" / "secret.txt")
        with self.assertRaises(errors.InfraInvalid):
            self.guard.write_text(target, "evil")
        self.assertEqual(
            (self.root / "forbidden" / "secret.txt").read_text(encoding="utf-8"), "do-not-touch"
        )

    def test_fsguard_refuses_write_to_read_only_root(self):
        (self.root / "readonly").mkdir()
        roots = winpath.RootSet.build(
            [winpath.RootRule("RO", str(self.root / "readonly"), "ro")]
        )
        guard = fsguard.FsGuard(roots)
        with self.assertRaises(errors.InfraInvalid):
            guard.write_text(str(self.root / "readonly" / "new.txt"), "nope")

    def test_fsguard_refuses_path_outside_every_root(self):
        with self.assertRaises(errors.InfraInvalid):
            self.guard.write_text(str(self.root / "elsewhere" / "x.txt"), "nope")


if __name__ == "__main__":
    unittest.main()
