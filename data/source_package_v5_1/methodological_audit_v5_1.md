# Colombia 2026 source-balanced signal package — v5.1 methodological audit

## Corrections introduced
1. The source-class balancing coefficients were recalculated after the v5 append operation.
2. The specialized blank-vote chronology was reconciled with the master table and now contains 11 records, including the grouped AtlasIntel/La Silla Vacía observation already present as S042.

## Weighting rule
For source category c:

    source_class_balance_weight_c = N / (K * n_c)

where N is the total number of master rows, K is the number of source categories, and n_c is the number of rows in category c.

The event-level sampling coefficient is:

    model_sampling_weight_j = min(3, source_class_balance_weight_c / event_cluster_size_j)

The inverse-frequency correction equalizes the aggregate sampling mass of source categories. The cap of 3 prevents very rare categories from dominating a simulation draw. These are experimental design weights, not survey expansion factors or estimates of population exposure.

## Current parameters
- N = 207 master rows.
- K = 9 source categories.
- Blank-vote chronology = 11 records.
- Public-position audit = 4 records.

## Reproducibility rule
Any append, deletion, or recategorization of a master row requires recalculation of both weight fields and regeneration of the audit manifest.

## Event-cluster integrity correction
A cluster must refer to the same underlying event, not merely a shared topic. Theme bundles introduced during the 20 June append were split into unique event clusters. Every cluster now contains exactly one `canonical_signal`; additional reports of the same event are coded as `supporting_observation`.

This correction prevents two opposite errors:
- counting repeated coverage of one event as multiple independent shocks; and
- collapsing distinct events into one thematic cluster.
