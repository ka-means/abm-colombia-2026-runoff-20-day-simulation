import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "notebooks/Colombia_2026_Presidential_Runoff_The_20_Day_Simulation.ipynb"


def test_publication_notebook_has_no_outputs_or_duplicate_code_cells():
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    hashes = set()
    for cell in notebook["cells"]:
        if cell["cell_type"] == "code":
            assert cell.get("outputs", []) == []
            assert cell.get("execution_count") is None
            source = "".join(cell.get("source", [])).strip()
            if source:
                digest = hashlib.sha256(source.encode()).hexdigest()
                assert digest not in hashes
                hashes.add(digest)


def test_notebook_public_version():
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    assert notebook["metadata"]["project"]["version"] == "1.0.0"


def test_github_pages_entry_file_exists():
    index = ROOT / "docs/index.html"
    assert index.exists()
    assert "synthetic model behaviour" in index.read_text(encoding="utf-8").lower()
