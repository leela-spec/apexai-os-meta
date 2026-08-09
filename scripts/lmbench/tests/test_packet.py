"""Work-packet compiler mechanics."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.lmbench import fixtureio, packet


def _build_fixture(root: Path) -> None:
    fixture_dir = root / "F1"
    (fixture_dir / "seed").mkdir(parents=True)
    (fixture_dir / "packet.md").write_text("Do the thing.", encoding="utf-8")


class TestCompilePacket(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        _build_fixture(self.root)
        self.public = fixtureio.load_public(self.root, "F1")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_user_message_is_the_packet_text_verbatim(self):
        compiled = packet.compile_packet(self.public, ("finish",))
        self.assertEqual(compiled.user_message, "Do the thing.")

    def test_system_message_is_the_fixed_preamble(self):
        compiled = packet.compile_packet(self.public, ("finish",))
        self.assertEqual(compiled.system_message, packet.SYSTEM_PREAMBLE)

    def test_only_requested_tools_are_offered(self):
        compiled = packet.compile_packet(self.public, ("read_file", "finish"))
        names = {s["function"]["name"] for s in compiled.tool_schemas}
        self.assertEqual(names, {"read_file", "finish"})

    def test_as_messages_shape(self):
        compiled = packet.compile_packet(self.public, ("finish",))
        messages = compiled.as_messages()
        self.assertEqual(messages[0]["role"], "system")
        self.assertEqual(messages[1]["role"], "user")

    def test_authority_preamble_is_identical_regardless_of_tool_selection(self):
        """The authority text is fixed independent of what's offered -- a
        future context-tier fixture must not be able to squeeze it out by
        offering more tools/filler; this pins that invariant now."""
        a = packet.compile_packet(self.public, ("finish",))
        b = packet.compile_packet(self.public, ("read_file", "write_file", "run_command", "finish"))
        self.assertEqual(a.system_message, b.system_message)


if __name__ == "__main__":
    unittest.main()
