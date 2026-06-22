# Release Assets

Large and execution-specific artifacts should be attached to a GitHub Release rather than committed to normal Git history.

For release `v1.0.0`, attach:

1. `Colombia_2026_Presidential_Runoff_Executed_v1.0.0.ipynb`
2. `Claude_Agent_Simulation_History_20260622T102929Z.zip`
3. `Colombia_2026_Hybrid_ABM_LLM_Dashboard.html`
4. `colombia_2026_source_balanced_v5_1_methodological_audit.zip`
5. `SHA256SUMS.txt`

The separately supplied `release-assets-v1.0.0/` directory contains these files.

## Release notes must state

- exact input-package checksum;
- commit SHA;
- run profile and seed;
- LLM provider/model/temperature/token limit;
- notebook and data-package versions;
- known incomplete exports;
- interpretation disclaimer.

Historical release assets should remain immutable. Corrections require a new release tag.
