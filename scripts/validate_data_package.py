#!/usr/bin/env python3
"""Validate the audited v5.1 source package without executing the ABM."""

from __future__ import annotations

import json
import math
import tempfile
import zipfile
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
ZIP_PATH = ROOT / "data/raw/colombia_2026_source_balanced_v5_1_methodological_audit.zip"
REQUIRED = {
    "signals_master_source_balanced_v5_1.csv",
    "audit_manifest_v5_1.json",
    "methodological_audit_v5_1.md",
    "frame_balance_methodology_v4.md",
}


def main() -> int:
    if not ZIP_PATH.exists():
        raise FileNotFoundError(ZIP_PATH)

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp).resolve()
        with zipfile.ZipFile(ZIP_PATH) as archive:
            names = set(archive.namelist())
            missing = REQUIRED - names
            assert not missing, f"Missing package files: {sorted(missing)}"
            for member in archive.infolist():
                target = (tmp_path / member.filename).resolve()
                assert tmp_path == target or tmp_path in target.parents, (
                    f"Unsafe ZIP member: {member.filename}"
                )
            archive.extractall(tmp_path)

        manifest = json.loads((tmp_path / "audit_manifest_v5_1.json").read_text(encoding="utf-8"))
        df = pd.read_csv(tmp_path / "signals_master_source_balanced_v5_1.csv")

        assert manifest["package_version"] == "v5.1"
        assert len(df) == manifest["master_rows"] == 207
        assert df["id"].is_unique
        assert df["source_category"].nunique() == manifest["source_categories"] == 9
        assert df["event_cluster_id"].nunique() == manifest["event_clusters"] == 201
        assert (df["observation_role"] == "canonical_signal").sum() == 201
        assert (df["observation_role"] == "supporting_observation").sum() == 6

        canonical_by_cluster = (
            df.assign(is_canonical=df["observation_role"].eq("canonical_signal"))
            .groupby("event_cluster_id")["is_canonical"]
            .sum()
        )
        assert canonical_by_cluster.eq(1).all(), "Each event cluster must have one canonical signal"

        cutoff = pd.Timestamp(manifest["cutoff_colombia_time"]).tz_convert(None)
        dates = pd.to_datetime(df["fecha"], errors="raise")
        assert dates.max() <= cutoff

        n = len(df)
        k = df["source_category"].nunique()
        counts = df["source_category"].value_counts()
        expected = df["source_category"].map(lambda c: n / (k * counts[c]))
        assert (df["source_class_balance_weight"] - expected).abs().max() < 1e-5

        expected_model = (
            df["source_class_balance_weight"] / df["event_cluster_size"]
        ).clip(upper=3)
        assert (df["model_sampling_weight"] - expected_model).abs().max() < 1e-5

    print("Data package validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
