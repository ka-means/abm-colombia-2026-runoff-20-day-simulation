# Source Balancing and Event-Cluster Methodology

## Objective

The source-balancing design reduces the risk that categories with many collected observations dominate simulation draws merely because they are more numerous in the research package.

It is an experimental design correction, not a survey weight and not an estimate of real population exposure.

## Source-category weight

For source category `c`:

```text
source_class_balance_weight_c = N / (K × n_c)
```

where:

- `N` is the number of rows in the master table;
- `K` is the number of source categories;
- `n_c` is the number of rows in category `c`.

For v5.1:

- `N = 207`;
- `K = 9`.

The resulting category weights are recorded in `audit_manifest_v5_1.json`.

## Event-level model weight

For observation `j`:

```text
model_sampling_weight_j = min(
    3,
    source_class_balance_weight_c / event_cluster_size_j
)
```

Dividing by event-cluster size prevents repeated coverage of one underlying event from acquiring excessive sampling mass. The cap of three limits domination by very rare source categories.

## Cluster-integrity contract

Each `event_cluster_id` must correspond to one underlying event and contain exactly one row marked `canonical_signal`. Additional reporting of the same event is marked `supporting_observation`.

This prevents:

1. treating repeated coverage of one event as multiple independent shocks; and
2. collapsing distinct events into one broad thematic bundle.

## What the weights do

The weights:

- equalise aggregate sampling mass across source categories;
- attenuate duplicate coverage within an event cluster;
- provide controlled input to the simulation's exposure-selection mechanism.

## What the weights do not do

The weights do not:

- estimate how many real voters saw an item;
- correct to the Colombian electorate;
- prove ideological neutrality;
- force equal candidate counts;
- transform unavailable engagement into exposure;
- establish causal effects.

## Candidate balance versus source balance

The package is source-category balanced, not candidate-count balanced. The master table contains different numbers of observations for De la Espriella, Cepeda, both candidates, and blank vote. Those differences must remain visible and must not be described as equal candidate representation.

## Piece-level classification

An outlet or person is not assigned one permanent ideological label. Each article, broadcast, interview, or post is classified individually according to its observed frame or alignment. A mixed interview remains mixed unless explicit support is present.

## Revision rule

Any append, deletion, recategorisation, cluster split, or cluster merge requires:

1. recalculation of both weight fields;
2. regeneration of the audit manifest;
3. validation of exactly one canonical signal per cluster;
4. a package-version increment;
5. a changelog describing the affected records.
