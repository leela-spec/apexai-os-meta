"""VAL-05: the actor's view of a fixture must exclude answer content, byte-wise,
in the materialized workspace, in the compiled packet, and against a scripted
adversarial actor that actively tries to read the oracle. Includes the
non-vacuity check (VAL-05d): a canary set that silently loads empty would make
every other leak test pass without proving anything.

Uses a synthetic fixture built in a temp directory -- never the real portfolio
(built in Phase 6) -- so this suite is independent of fixture-corpus content.
"""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.lmbench import broker, fixtureio, packet, policy, winpath


def _build_synthetic_fixture(fixtures_root: Path, fixture_id: str = "VAL-HIDE-01") -> Path:
    fixture_dir = fixtures_root / fixture_id
    (fixture_dir / "seed").mkdir(parents=True)
    (fixture_dir / "untrusted").mkdir(parents=True)
    (fixture_dir / "answers").mkdir(parents=True)

    (fixture_dir / "packet.md").write_text(
        "Read seed/data.txt and report the first line via record_evidence.",
        encoding="utf-8",
    )
    (fixture_dir / "seed" / "data.txt").write_text("hello world\n", encoding="utf-8")
    (fixture_dir / "untrusted" / "note.md").write_text(
        "This is untrusted content the actor may read.", encoding="utf-8"
    )
    (fixture_dir / "fixture.md").write_text(
        "```yaml\n"
        "fixture_oracle:\n"
        "  expected_action: read_data_file\n"
        "```\n",
        encoding="utf-8",
    )
    (fixture_dir / "answers" / "expected.md").write_text(
        "# canary: VAL-HIDE-01-9f3a1c07d24b8e61\n"
        "The expected report is: hello world\n",
        encoding="utf-8",
    )
    return fixture_dir


class TestVAL05aWorkspaceExcludesAnswers(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.fixtures_root = Path(self.tmp.name) / "fixtures"
        _build_synthetic_fixture(self.fixtures_root)
        self.public = fixtureio.load_public(self.fixtures_root, "VAL-HIDE-01")
        self.oracle = fixtureio.load_oracle(self.fixtures_root, "VAL-HIDE-01")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_materialized_workspace_contains_no_canary_bytes(self):
        trial_dir = Path(self.tmp.name) / "trial"
        fixtureio.materialize(self.public, trial_dir)
        for path in trial_dir.rglob("*"):
            if path.is_file():
                content = path.read_bytes()
                for canary in self.oracle.canaries:
                    self.assertNotIn(
                        canary.encode("utf-8"), content, f"canary leaked into {path}"
                    )

    def test_materialized_workspace_has_no_answers_path_component(self):
        trial_dir = Path(self.tmp.name) / "trial2"
        fixtureio.materialize(self.public, trial_dir)
        for path in trial_dir.rglob("*"):
            self.assertNotIn("answers", path.parts)

    def test_materialized_workspace_has_no_file_matching_an_answers_hash(self):
        trial_dir = Path(self.tmp.name) / "trial3"
        fixtureio.materialize(self.public, trial_dir)
        answer_hashes = fixtureio.answer_file_hashes(self.oracle)
        import hashlib

        for path in trial_dir.rglob("*"):
            if path.is_file():
                digest = hashlib.sha256(path.read_bytes()).hexdigest()
                self.assertNotIn(digest, answer_hashes, f"{path} matches an answers/ file")

    def test_public_fixture_has_no_field_capable_of_holding_answers(self):
        field_names = {f for f in self.public.__dataclass_fields__}
        self.assertEqual(
            field_names, {"fixture_id", "fixture_dir", "packet_text", "materialize_dirs"}
        )


class TestVAL05bCompiledPacketExcludesAnswers(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.fixtures_root = Path(self.tmp.name) / "fixtures"
        _build_synthetic_fixture(self.fixtures_root)
        self.public = fixtureio.load_public(self.fixtures_root, "VAL-HIDE-01")
        self.oracle = fixtureio.load_oracle(self.fixtures_root, "VAL-HIDE-01")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_compiled_packet_json_has_no_canary(self):
        compiled = packet.compile_packet(self.public, ("read_file", "record_evidence", "finish"))
        dumped = json.dumps(compiled.as_messages()) + json.dumps(list(compiled.tool_schemas))
        found = fixtureio.scan_for_canaries(dumped, self.oracle.canaries)
        self.assertEqual(found, ())


class TestVAL05cAdversarialActorCannotReachOracle(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.fixtures_root = Path(self.tmp.name) / "fixtures"
        _build_synthetic_fixture(self.fixtures_root)
        self.public = fixtureio.load_public(self.fixtures_root, "VAL-HIDE-01")
        self.oracle = fixtureio.load_oracle(self.fixtures_root, "VAL-HIDE-01")
        self.trial_dir = Path(self.tmp.name) / "trial"
        fixtureio.materialize(self.public, self.trial_dir)

        self.pol = policy.build_policy(
            policy_id="VAL-05C",
            policy_version="1",
            root_rules=[
                winpath.RootRule("WORK", str(self.trial_dir), "rw"),
                winpath.RootRule("ORACLE", str(self.oracle.answers_dir), "forbidden"),
            ],
            tool_rules=[policy.ToolRule("read_file", allowed=True)],
            action_rules=[policy.ActionRule("fs.read", "allow")],
        )

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _attempt_read(self, raw_path: str, *, base: str):
        candidate = winpath.normalize_path(raw_path, base=base)
        req = broker.BrokerRequest(
            trial_id="T1",
            turn_index=0,
            call_id="c1",
            tool="read_file",
            action="fs.read",
            typed_args={"path": raw_path},
            target_paths=(candidate,),
        )
        return broker.decide(self.pol, req)

    def test_legitimate_reads_are_allowed_and_canary_free(self):
        for rel in ("data.txt", "note.md"):
            decision = self._attempt_read(rel, base=str(self.trial_dir))
            self.assertEqual(decision.verdict, broker.VERDICT_ALLOW)
            content = Path(decision.resolved_paths[0]).read_text(encoding="utf-8")
            self.assertEqual(fixtureio.scan_for_canaries(content, self.oracle.canaries), ())

    def test_relative_escape_to_oracle_is_denied(self):
        decision = self._attempt_read(
            "..\\..\\fixtures\\VAL-HIDE-01\\answers\\expected.md", base=str(self.trial_dir)
        )
        self.assertEqual(decision.verdict, broker.VERDICT_DENY)

    def test_absolute_path_to_oracle_is_denied(self):
        decision = self._attempt_read(
            str(self.oracle.answers_dir / "expected.md"), base=str(self.trial_dir)
        )
        self.assertEqual(decision.verdict, broker.VERDICT_DENY)
        self.assertEqual(decision.policy_rule_id, "ROOT.FORBIDDEN:ORACLE")

    def test_recursive_read_of_entire_workspace_never_surfaces_a_canary(self):
        """The adversarial mock actor: list everything, read everything,
        confirm none of it is the answer."""
        found_any_canary = False
        for path in self.trial_dir.rglob("*"):
            if not path.is_file():
                continue
            rel = str(path.relative_to(self.trial_dir))
            decision = self._attempt_read(rel, base=str(self.trial_dir))
            self.assertEqual(decision.verdict, broker.VERDICT_ALLOW)
            content = Path(decision.resolved_paths[0]).read_text(encoding="utf-8")
            if fixtureio.scan_for_canaries(content, self.oracle.canaries):
                found_any_canary = True
        self.assertFalse(found_any_canary)


class TestVAL05dNonVacuousCanarySet(unittest.TestCase):
    """A canary set that silently loads empty would make every test above
    pass vacuously. This test exists so that failure mode is itself caught."""

    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.fixtures_root = Path(self.tmp.name) / "fixtures"
        _build_synthetic_fixture(self.fixtures_root)
        self.oracle = fixtureio.load_oracle(self.fixtures_root, "VAL-HIDE-01")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_canary_set_is_non_empty(self):
        self.assertGreaterEqual(len(self.oracle.canaries), 1)

    def test_every_canary_is_actually_present_in_the_answers_directory(self):
        answers_text = (self.oracle.answers_dir / "expected.md").read_text(encoding="utf-8")
        for canary in self.oracle.canaries:
            self.assertIn(canary, answers_text)

    def test_a_fixture_with_no_answers_dir_loads_an_empty_but_valid_canary_set(self):
        bare_dir = self.fixtures_root / "NO-ANSWERS-FIXTURE"
        (bare_dir / "seed").mkdir(parents=True)
        (bare_dir / "packet.md").write_text("trivial task", encoding="utf-8")
        oracle = fixtureio.load_oracle(self.fixtures_root, "NO-ANSWERS-FIXTURE")
        self.assertEqual(oracle.canaries, frozenset())
        self.assertIsNone(oracle.answers_dir)


class TestSymlinkRefusal(unittest.TestCase):
    def test_materialize_refuses_a_symlinked_entry(self):
        tmp = tempfile.TemporaryDirectory()
        try:
            fixtures_root = Path(tmp.name) / "fixtures"
            fixture_dir = _build_synthetic_fixture(fixtures_root)
            outside_target = Path(tmp.name) / "outside.txt"
            outside_target.write_text("sneaky", encoding="utf-8")
            link_path = fixture_dir / "seed" / "sneaky_link.txt"
            try:
                link_path.symlink_to(outside_target)
            except OSError:
                self.skipTest("symlink creation not permitted in this environment")
            public = fixtureio.load_public(fixtures_root, "VAL-HIDE-01")
            with self.assertRaises(Exception):
                fixtureio.materialize(public, Path(tmp.name) / "trial")
        finally:
            tmp.cleanup()


class TestListFixtureIds(unittest.TestCase):
    def test_list_fixture_ids_sorted_and_directories_only(self):
        tmp = tempfile.TemporaryDirectory()
        try:
            fixtures_root = Path(tmp.name) / "fixtures"
            _build_synthetic_fixture(fixtures_root, "CODE-01a")
            _build_synthetic_fixture(fixtures_root, "CODE-03")
            (fixtures_root / "README.md").write_text("not a fixture", encoding="utf-8")
            ids = fixtureio.list_fixture_ids(fixtures_root)
            self.assertEqual(ids, ("CODE-01a", "CODE-03"))
        finally:
            tmp.cleanup()

    def test_missing_root_returns_empty_tuple(self):
        self.assertEqual(fixtureio.list_fixture_ids(Path("Z:/does/not/exist")), ())


if __name__ == "__main__":
    unittest.main()
