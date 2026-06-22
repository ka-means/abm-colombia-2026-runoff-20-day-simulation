# Data Directory

## Canonical input

`raw/colombia_2026_source_balanced_v5_1_methodological_audit.zip` is the canonical transport artifact used by the notebook.

## Extracted inspection copy

`source_package_v5_1/` mirrors the ZIP contents to make GitHub inspection, diffs and validation easier. Do not edit extracted files in place. Create a new source-package version and regenerate the ZIP and manifest.

## Integrity

Run:

```bash
python scripts/validate_data_package.py
```

The validator checks package files, counts, unique IDs, event-cluster integrity, cutoff compliance and documented weights.

## Missing values

Unavailable engagement metrics must remain missing. Do not replace them with zero.

## Rights

See `../THIRD_PARTY_NOTICES.md`, `../LICENSE-DATA.md`, and `../methodology/DATA_CARD.md`.
