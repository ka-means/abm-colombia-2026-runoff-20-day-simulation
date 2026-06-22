# Tests

The test suite verifies:

- v5.1 data-package counts and event-cluster integrity;
- existence and dimensions of core result tables;
- consistency of key KPI values with agent-level records;
- publication notebook output removal and duplicate-cell removal;
- dashboard entry-file presence.

Run with:

```bash
pytest
```

These are implementation-integrity tests, not external validation of electoral accuracy.
