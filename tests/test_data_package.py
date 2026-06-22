import json
import tempfile
import zipfile
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
ZIP_PATH = ROOT / "data/raw/colombia_2026_source_balanced_v5_1_methodological_audit.zip"


def load_package():
    temp = tempfile.TemporaryDirectory()
    root = Path(temp.name)
    with zipfile.ZipFile(ZIP_PATH) as z:
        z.extractall(root)
    manifest = json.loads((root / "audit_manifest_v5_1.json").read_text())
    data = pd.read_csv(root / "signals_master_source_balanced_v5_1.csv")
    return temp, manifest, data


def test_package_counts_and_ids():
    temp, manifest, data = load_package()
    try:
        assert manifest["package_version"] == "v5.1"
        assert data.shape[0] == 207
        assert data["id"].is_unique
        assert data["event_cluster_id"].nunique() == 201
        assert data["source_category"].nunique() == 9
    finally:
        temp.cleanup()


def test_one_canonical_signal_per_cluster():
    temp, _, data = load_package()
    try:
        counts = (
            data.assign(canonical=data["observation_role"].eq("canonical_signal"))
            .groupby("event_cluster_id")["canonical"]
            .sum()
        )
        assert counts.eq(1).all()
    finally:
        temp.cleanup()
