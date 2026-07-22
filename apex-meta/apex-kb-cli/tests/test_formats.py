from __future__ import annotations

from pathlib import Path

from apex_kb.extractors import extract_file

from .helpers import write_docx, write_pdf, write_pptx, write_xlsx


def test_text_and_office_extractors_have_stable_pointers(tmp_path: Path):
    markdown = tmp_path / "source.md"
    markdown.write_text("# Skill Tree\nEpic Block Chunk\n", encoding="utf-8")
    docx = tmp_path / "source.docx"
    pptx = tmp_path / "source.pptx"
    xlsx = tmp_path / "source.xlsx"
    write_docx(docx, "Skill Tree document")
    write_pptx(pptx, "Skill Tree slide")
    write_xlsx(xlsx, "Skill Tree cell")
    assert extract_file(markdown)["segments"][0]["pointer"] == "line:1"
    assert extract_file(docx)["segments"][0] == {"pointer": "paragraph:1", "text": "Skill Tree document"}
    assert extract_file(pptx)["segments"][0] == {"pointer": "slide:1", "text": "Skill Tree slide"}
    assert extract_file(xlsx)["segments"][0] == {"pointer": "sheet:1!A1", "text": "Skill Tree cell"}


def test_pdf_and_unsupported_files_remain_visible(tmp_path: Path):
    pdf = tmp_path / "blank.pdf"
    write_pdf(pdf)
    result = extract_file(pdf)
    assert result["format"] == "pdf" and result["status"] in {"success", "metadata_only"}
    unknown = tmp_path / "source.xyz"
    unknown.write_bytes(b"abc")
    assert extract_file(unknown)["status"] == "unsupported"


def test_structured_text_code_pdf_and_image_formats(tmp_path: Path):
    from .helpers import write_text_pdf

    json_path = tmp_path / "source.json"
    json_path.write_text('{"skill_tree": {"owner": "Epic"}}', encoding="utf-8")
    yaml_path = tmp_path / "source.yaml"
    yaml_path.write_text("skill_tree:\n  owner: Epic\n", encoding="utf-8")
    csv_path = tmp_path / "source.csv"
    csv_path.write_text("concept,owner\nSkill Tree,Epic\n", encoding="utf-8")
    code_path = tmp_path / "source.py"
    code_path.write_text("SKILL_TREE_OWNER = 'Epic'\n", encoding="utf-8")
    pdf_path = tmp_path / "source.pdf"
    write_text_pdf(pdf_path, "Skill Tree PDF evidence")
    image_path = tmp_path / "source.png"
    image_path.write_bytes(b"not-a-real-image-but-inventory-visible")

    assert "skill_tree" in extract_file(json_path)["text"]
    assert extract_file(yaml_path)["segments"][0]["pointer"] == "line:1"
    assert extract_file(csv_path)["segments"][2] == {"pointer": "row:2:column:1", "text": "Skill Tree"}
    assert extract_file(code_path)["segments"][0] == {"pointer": "line:1", "text": "SKILL_TREE_OWNER = 'Epic'"}
    pdf = extract_file(pdf_path)
    assert pdf["status"] == "success" and pdf["segments"] == [{"pointer": "page:1", "text": "Skill Tree PDF evidence"}]
    image = extract_file(image_path)
    assert image["status"] == "metadata_only" and image["format"] == "image"


def test_corrupt_ooxml_and_missing_optional_pdf_dependency_are_reason_coded(tmp_path: Path, monkeypatch):
    import builtins

    corrupt = tmp_path / "corrupt.docx"
    corrupt.write_bytes(b"not-a-zip")
    result = extract_file(corrupt)
    assert result["status"] == "error" and result["error"].startswith("BadZipFile:")

    from .helpers import write_text_pdf

    pdf = tmp_path / "source.pdf"
    write_text_pdf(pdf, "Skill Tree")
    real_import = builtins.__import__

    def blocked_import(name, *args, **kwargs):
        if name == "pypdf":
            raise ImportError("simulated missing dependency")
        return real_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", blocked_import)
    result = extract_file(pdf)
    assert result["status"] == "unsupported"
    assert result["error"].startswith("pypdf_unavailable:")
