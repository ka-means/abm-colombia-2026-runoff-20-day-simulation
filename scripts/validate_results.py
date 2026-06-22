#!/usr/bin/env python3
"""Validate the supplied dashboard tables and headline KPI consistency."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "results/dashboard_tables"
ALLOWED_STATES = {"Cepeda", "De la Espriella", "Voto en blanco", "No alineado", "Abstencion"}


def main() -> int:
    required = [
        "section_23_kpi_summary.csv",
        "model_shares.csv",
        "agent_opinions_abm_vs_llm_all.csv",
        "tone_profile.csv",
        "regional_shares.csv",
    ]
    missing = [name for name in required if not (TABLES / name).exists()]
    assert not missing, f"Missing required result tables: {missing}"

    opinions = pd.read_csv(TABLES / "agent_opinions_abm_vs_llm_all.csv")
    kpi = pd.read_csv(TABLES / "section_23_kpi_summary.csv").iloc[0]
    shares = pd.read_csv(TABLES / "model_shares.csv")
    tone = pd.read_csv(TABLES / "tone_profile.csv")

    assert len(opinions) == int(kpi["synthetic_agents"]) == 1000
    assert opinions["agent_id"].is_unique
    assert set(opinions["llm_final_state"].dropna()).issubset(ALLOWED_STATES)
    assert len(tone) == 1000 and tone["agent_id"].is_unique

    changed = opinions["decision_changed"].astype(str).str.lower().eq("true").mean()
    assert abs(changed - float(kpi["decision_change_rate"])) < 1e-9

    llm_shares = opinions["llm_final_state"].value_counts(normalize=True)
    blank = float(llm_shares.get("Voto en blanco", 0.0))
    assert abs(blank - float(kpi["llm_blank_vote_share"])) < 1e-9

    share_map = shares.set_index("state")["LLM"].to_dict()
    for state, value in llm_shares.items():
        assert abs(float(share_map[state]) - float(value)) < 1e-9

    print("Result-table validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
