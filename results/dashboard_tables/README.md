# Dashboard Tables

The static dashboard is self-contained, but these tables allow independent inspection of the displayed results.

`section_23_dashboard_manifest.csv` records file status, dimensions and SHA-256 values for supplied tables. Rows marked `not supplied` should be regenerated from Section 23 of the executed notebook before claiming a complete dashboard-table export.

Important large files:

- `agent_opinions_abm_vs_llm_all.csv`: 1,000 agent-level ABM–LLM comparison records.
- `tone_profile.csv`: one tone-analysis row per synthetic agent.
- `semantic_concept_profile.csv`: state-conditioned semantic-concept statistics.

Do not infer real public opinion from these files.
