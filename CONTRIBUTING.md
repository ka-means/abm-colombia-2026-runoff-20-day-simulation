# Contributing

Contributions are welcome when they improve reproducibility, methodological clarity, validation, or software quality without converting the model into a claim about real electoral outcomes.

## Before opening a pull request

1. Create an issue describing the methodological or technical problem.
2. Identify whether the change affects data, agent rules, weights, network structure, LLM prompts, output schemas, or only presentation.
3. Preserve the original input artifact and add a new version rather than silently replacing it.
4. Add or update tests for every changed contract.
5. Run:

```bash
python scripts/validate_data_package.py
python scripts/validate_results.py
pytest
```

## Change classes

- **Documentation-only:** no model output is expected to change.
- **Presentation-only:** figures or dashboard layout change, but analytical tables remain invariant.
- **Data revision:** requires a new package version, audit manifest, checksums, and explanation of changed rows.
- **ABM rule revision:** requires a new model version, parameter record, sensitivity analysis, and comparison against the previous version.
- **LLM protocol revision:** requires a new prompt/schema version and must not be compared with the old run as if the protocol were unchanged.

## Pull-request requirements

A pull request must state:

- motivation;
- files changed;
- expected effect on results;
- tests added or updated;
- whether outputs are backward-compatible;
- whether a new release is required.

Do not commit API keys, unredacted credentials, private account identifiers, temporary batch request files, or large execution outputs that belong in GitHub Releases.
