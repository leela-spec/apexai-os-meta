import re
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORKSPACE_SKILLS = ROOT / "artifacts" / "openai_workspace_skills"
ORIGINAL = WORKSPACE_SKILLS / "authentic-obsidian-wiki-ingest" / "wiki-ingest"
TARGET = WORKSPACE_SKILLS / "obsidian-wiki-ingest"
ARCHIVE = WORKSPACE_SKILLS / "obsidian-wiki-ingest.zip"


def body_lines(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    match = re.match(r"\A---\n.*?\n---\n", text, flags=re.DOTALL)
    if match:
        text = text[match.end():]
    return text.splitlines()


def is_subsequence(expected: list[str], actual: list[str]) -> bool:
    cursor = iter(actual)
    return all(any(candidate == line for candidate in cursor) for line in expected)


class ObsidianWorkspaceSkillTest(unittest.TestCase):
    def test_original_skill_body_is_preserved_in_order(self):
        self.assertTrue(
            is_subsequence(body_lines(ORIGINAL / "SKILL.md"), body_lines(TARGET / "SKILL.md")),
            "The target must preserve every original SKILL.md body line in order.",
        )

    def test_original_references_are_preserved_without_semantic_changes(self):
        for original in (ORIGINAL / "references").glob("*.md"):
            target = TARGET / "references" / original.name
            self.assertTrue(target.exists(), original.name)
            expected = original.read_text(encoding="utf-8").replace("\r\n", "\n").rstrip()
            actual = target.read_text(encoding="utf-8").replace("\r\n", "\n").rstrip()
            self.assertEqual(actual, expected, original.name)

    def test_long_source_contract_and_no_mandatory_packaging_script(self):
        long_source = TARGET / "references" / "long-source-integrity.md"
        self.assertTrue(long_source.exists())
        text = long_source.read_text(encoding="utf-8")
        for contract in (
            "NEEDS_PREPROCESSING",
            "coverage_status",
            "no_relevant_knowledge",
            "affected_ranges",
            "remediation",
            "CENTRAL_EVIDENCE_NOT_VERIFIABLE",
        ):
            self.assertIn(contract, text)
        self.assertFalse((TARGET / "scripts" / "package_vault.py").exists())
        self.assertNotIn("package_vault.py", (TARGET / "SKILL.md").read_text(encoding="utf-8"))

    def test_upload_archive_has_one_expected_top_level_folder(self):
        self.assertTrue(ARCHIVE.exists())
        with zipfile.ZipFile(ARCHIVE) as archive:
            names = archive.namelist()
        self.assertTrue(names)
        self.assertTrue(all(name.startswith("obsidian-wiki-ingest/") for name in names))
        self.assertIn("obsidian-wiki-ingest/SKILL.md", names)
        self.assertIn("obsidian-wiki-ingest/references/long-source-integrity.md", names)
        self.assertNotIn("obsidian-wiki-ingest/scripts/package_vault.py", names)


if __name__ == "__main__":
    unittest.main()
