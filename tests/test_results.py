from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "results/dashboard_tables"


def test_agent_level_results():
    opinions = pd.read_csv(TABLES / "agent_opinions_abm_vs_llm_all.csv")
    assert len(opinions) == 1000
    assert opinions["agent_id"].is_unique
    assert int(opinions["decision_changed"].sum()) == 156


def test_kpi_consistency():
    opinions = pd.read_csv(TABLES / "agent_opinions_abm_vs_llm_all.csv")
    kpi = pd.read_csv(TABLES / "section_23_kpi_summary.csv").iloc[0]
    assert abs(opinions["decision_changed"].mean() - kpi["decision_change_rate"]) < 1e-12
    blank = opinions["llm_final_state"].eq("Voto en blanco").mean()
    assert abs(blank - kpi["llm_blank_vote_share"]) < 1e-12


def test_tone_profile_is_agent_complete():
    tone = pd.read_csv(TABLES / "tone_profile.csv")
    assert len(tone) == 1000
    assert tone["agent_id"].is_unique
