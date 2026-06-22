# Reproducibility Guide

## Reproduction levels

### Level 1 — Artifact inspection

Inspect the audited ZIP, extracted tables, supplied result CSVs, dashboard and executed release notebook without rerunning the model.

### Level 2 — Heuristic ABM reproduction

Run the twenty-day heuristic model with the same data package, code, configuration, seed and dependency environment. This layer is expected to be deterministic under compatible numerical libraries.

### Level 3 — LLM protocol reproduction

Recreate dossiers and provider requests using the same prompt, schema, provider, model identifier, temperature and token limit. Exact textual identity is not guaranteed because remote inference may be non-deterministic or versioned by the provider.

### Level 4 — Scientific replication

Independently reimplement or rerun the model, conduct multiple-seed and parameter sensitivity analyses, and evaluate whether substantive conclusions remain stable.

## Required run metadata

Every run should retain:

- project and notebook version;
- Git commit SHA;
- UTC timestamp;
- operating system and Python version;
- dependency versions;
- run profile;
- complete model configuration;
- random seed;
- input ZIP filename and SHA-256;
- extracted-file SHA-256 values;
- LLM provider and model identifier;
- prompt and schema versions/checksums;
- request and result checksums;
- final table and figure checksums;
- failure and retry counts.

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Set the package path:

```bash
export COLOMBIA_ABM_PACKAGE_PATH="$PWD/data/raw/colombia_2026_source_balanced_v5_1_methodological_audit.zip"
```

Select a profile:

```bash
export COLOMBIA_HYBRID_PROFILE="SMOKE"   # or PILOT / FULL
```

The LLM phase additionally requires:

```bash
export ANTHROPIC_API_KEY="..."
export CLAUDE_MODEL="claude-sonnet-4-6"
export CLAUDE_TEMPERATURE="0.35"
export CLAUDE_MAX_OUTPUT_TOKENS="1200"
```

## Clean execution procedure

1. Start from a fresh environment.
2. Install declared dependencies.
3. Validate the data package.
4. Run the notebook from the first cell without manual state injection.
5. Do not reorder cells.
6. Preserve warnings and failed validations.
7. Export the final checkpoint and analytical tables.
8. Generate checksums.
9. Compare against the historical artifact where exact reproduction is expected.
10. Record every intentional deviation.

## Notebook copies

- The repository notebook has outputs removed and is suitable for version control.
- The executed notebook belongs in a GitHub Release and preserves output evidence.
- Do not overwrite a historical executed notebook with a later rerun under the same release name.

## Dependency locking

`requirements.txt` provides compatible minimum/range declarations. For an archival release, generate a lock from the successful clean environment:

```bash
python -m pip freeze > requirements-lock.txt
```

Store the lock with the release that it reproduces. Do not assume a future provider model or Python package remains behaviourally identical under the same name.

## Randomness

Python's `random` module and NumPy are seeded with the configured seed. Any additional stochastic library must be seeded explicitly and added to the run manifest.

## Large artifacts

Do not store large execution histories in ordinary Git commits. Attach them to a versioned GitHub Release and publish `SHA256SUMS.txt`.

## Expected versus non-expected identity

- Input validation: exact.
- Heuristic ABM with identical environment: exact or numerically equivalent within documented tolerance.
- Dashboard derived from identical tables: exact.
- Remote LLM natural-language output: not guaranteed exact.
- LLM structured state distributions: subject to protocol and provider variation; compare explicitly rather than assuming identity.
