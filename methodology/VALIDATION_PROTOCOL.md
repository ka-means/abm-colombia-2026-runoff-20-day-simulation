# Validation Protocol

## Validation philosophy

Validation is divided into data integrity, implementation correctness, structural realism, behavioural reasonableness, output consistency, linguistic controls, and reproducibility. Passing software tests does not establish electoral predictive validity.

## 1. Input-package validation

Required checks:

- ZIP exists and can be safely extracted;
- required files are present;
- package manifest reports version v5.1;
- master table contains 207 rows;
- IDs are unique;
- source categories equal nine;
- event clusters equal 201;
- canonical signals equal 201;
- supporting observations equal six;
- every event cluster contains exactly one canonical signal;
- dates do not exceed the declared cutoff;
- balancing fields match the documented formulas within numerical tolerance;
- missing engagement remains missing rather than zero-filled.

## 2. Synthetic-population validation

Required checks:

- number of agents equals the active profile;
- agent IDs are unique;
- all categorical fields are inside declared domains;
- numeric propensities are inside valid bounds;
- regional and profile distributions match their configured calibration targets within documented tolerance;
- no row contains real personal identifiers.

## 3. Network validation

For each layer record:

- nodes and edges;
- isolates;
- mean and maximum degree;
- component count;
- density;
- clustering where appropriate;
- reciprocity for directed layers;
- duplicate/self-loop policy.

A layer must not be accepted solely because it renders visually.

## 4. ABM execution validation

Required checks:

- twenty daily steps complete;
- final state exists for every agent;
- all final labels are allowed;
- no probability/propensity field leaves its valid range;
- exposure and transmission records reference known agents and signals;
- cascade depth never exceeds configuration;
- direct and peer effect scaling is finite;
- daily metrics contain no unexplained gaps;
- the same seed and environment reproduce the heuristic outputs.

## 5. Behavioural validation

Perform at least:

- extreme-parameter tests;
- no-signal and no-network controls;
- direct-effect and peer-effect ablations;
- memory-disabled and adaptive-trust-disabled runs;
- source-weight ablation;
- multiple-seed sensitivity analysis;
- profile-size comparison between SMOKE, PILOT and FULL.

Outputs should respond directionally to controlled changes. Unexpected invariance or explosive sensitivity requires investigation.

## 6. LLM validation

Required checks:

- one dossier per requested agent;
- no duplicate agent decisions;
- valid JSON/typed schema;
- allowed final states only;
- confidence inside the declared interval;
- no API keys or credentials in outputs;
- anonymous labels correctly mapped after validation;
- failures separated from valid decisions;
- pilot and full batch use the same prompt/schema version unless explicitly versioned otherwise.

## 7. Linguistic validation

Generated social-language output should be checked for:

- marker frequency and overuse;
- internal consistency with configured region/register;
- harmful stereotypes;
- unsupported claims of authenticity;
- excessive aggression or harassment;
- accidental reproduction of source text beyond what is necessary.

A language-audit pass rate is a pipeline indicator, not evidence that generated speech is sociolinguistically authentic.

## 8. Dashboard validation

For every KPI and chart:

- identify the source CSV/table;
- verify row and column counts;
- recompute displayed shares from raw counts;
- verify state-label order;
- check denominators and treatment of missing values;
- confirm disclaimers remain visible;
- confirm the dashboard does not load secrets or private paths;
- verify `index.html` opens without external runtime dependencies.

## 9. Release validation

Before tagging a release:

```bash
python scripts/validate_data_package.py
python scripts/validate_results.py
pytest
python scripts/generate_checksums.py --root . --output MANIFEST.sha256
```

Then execute the notebook from a clean runtime, retain the environment record, compare checksums, and attach large artifacts to the release.

## Validation status of version 1.0.0

The repository package validates the supplied data counts, existing result-table contracts, notebook structure, and absence of committed notebook outputs. It does not claim completion of multi-seed sensitivity analysis or independent external replication.
