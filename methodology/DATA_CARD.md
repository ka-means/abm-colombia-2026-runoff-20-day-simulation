# Data Card

## Dataset name

**Colombia 2026 source-balanced signal package — v5.1**

## Purpose

The package provides an audited information environment for a twenty-day synthetic ABM–LLM experiment. It is designed to support source traceability, event-level de-duplication, category-balanced experimental sampling, semantic analysis, and agent-specific information exposure.

It is not a voter dataset, polling microdata file, social-media firehose, or comprehensive archive of Colombian political communication.

## Temporal scope

- Earliest master date: 31 May 2026.
- Latest master date: 20 June 2026.
- Formal cutoff: `2026-06-20T23:59:59-05:00` Colombia time.
- Audit date: 21 June 2026.

## Package composition

| File | Role |
|---|---|
| `signals_master_source_balanced_v5_1.csv` | Canonical master table used by the model. |
| `media_coverage_observations_v3.csv` | Media coverage observations and context. |
| `social_signals_x_and_engagement_v2.csv` | Publicly indexed X/social records and available engagement fields. |
| `campaign_personality_signals_v2.csv` | Campaign-personality and public-position records. |
| `international_media_frame_balanced_v4.csv` | International outlet observations classified by piece-level frame. |
| `digital_amplifiers_frame_balanced_v4.csv` | Digital/editorial amplifier observations classified by individual piece. |
| `frame_balance_audit_v4.csv/json` | Frame and alignment audit. |
| `blank_vote_coverage_2026_v5_1.csv` | Specialised blank-vote chronology. |
| `blank_vote_public_position_audit_2026_v1.csv` | Public-position audit for blank-vote coverage. |
| `audit_manifest_v5_1.json` | Version, counts, weight rules, and cluster-integrity contract. |
| `methodological_audit_v5_1.md` | Weight and cluster correction record. |
| `frame_balance_methodology_v4.md` | International and amplifier frame methodology. |
| `source_balanced_signal_package_v5_1.xlsx` | Spreadsheet representation for inspection. |

## Master-table scale

- Rows: 207.
- Columns: 37.
- Event clusters: 201.
- Canonical signals: 201.
- Supporting observations: 6.
- Source categories: 9.

The difference between 207 master rows and 201 strategic signals is intentional: six rows are supporting observations attached to an underlying canonical event.

## Source-category distribution

| Category | Rows |
|---|---:|
| television | 39 |
| social_oficial | 38 |
| otro | 36 |
| radio | 29 |
| prensa_privada | 27 |
| alternativo_investigativo | 14 |
| internacional | 14 |
| medio_publico | 5 |
| regional | 5 |

## Candidate/event scope in the master table

| Scope | Rows |
|---|---:|
| De la Espriella | 74 |
| Both candidates | 71 |
| Cepeda | 54 |
| Blank vote | 8 |

These counts describe coded observations. They are not equal exposure quotas, endorsements, sentiment scores, or estimated real-world reach.

## Core master schema

The master table includes:

- identifier, date, title, description and type;
- source name and URL;
- legal/status and source-strict indicators;
- affected candidate/scope and direction;
- primary motif, frame, emotion and impact dimension;
- region, intensity, credibility and misinformation risk;
- probable channels and relevant agent profiles;
- agent-facing summary and cutoff date;
- source category, ownership type and geographic scope;
- observation role and event-cluster fields;
- balancing and model-sampling weights;
- available engagement metrics and an engagement-status field.

See `data/source_package_v5_1/signals_master_source_balanced_v5_1.csv` for exact column names.

## Collection and classification principles

- Classifications apply to each individual piece, not permanently to an outlet, host, programme, or person.
- Interviews are not endorsements unless explicit support is documented.
- International framing distinguishes security/market, economic, social-rights, institutional/descriptive, conflict-memory/human-rights, and comparative-polarisation frames.
- Digital amplifiers are classified as favourable/critical toward either side or mixed/informational at the piece level.
- Repeated coverage of one event is attached as supporting observation rather than counted as an independent shock.
- Distinct events sharing a topic must not be collapsed into one event cluster.

## Missing data

Blank engagement values mean unavailable. They must remain missing and must not be converted to zero. Public indexing does not provide a complete or probability-based sample of all posts or interactions.

## Data quality controls

The package contract requires:

- unique master IDs;
- exactly one canonical signal per event cluster;
- recalculated weights after append, deletion, or recategorisation;
- explicit cutoff compliance;
- preservation of source URLs and row-level provenance;
- audit-manifest regeneration for every package revision.

## Ethical and rights considerations

The dataset contains political source metadata and derived annotations, not personal voter records. Third-party source content remains governed by its original rights holders. The package should not be expanded with private individuals' data, non-public account information, or sensitive profiling attributes.

## Recommended use

Use the package for controlled computational experiments, audit demonstrations, semantic analysis, and reproducibility studies. Do not use it as an exhaustive media census or as direct evidence of population-level exposure.
