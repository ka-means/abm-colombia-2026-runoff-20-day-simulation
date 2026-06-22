# Data Dictionary

This dictionary documents the principal fields in `signals_master_source_balanced_v5_1.csv`. Exact data types should be inferred and validated during ingestion rather than assumed from this prose alone.

| Field | Meaning |
|---|---|
| `id` | Unique observation identifier. |
| `fecha` | Observation/event date used by the temporal schedule. |
| `titulo` | Short source-grounded title or event descriptor. |
| `descripcion` | Expanded description of the observation. |
| `tipo` | Signal or record type. |
| `fuente` | Named source, outlet, programme, account, or originating entity. |
| `fuente_url` | Provenance URL when available. |
| `legal_status` | Coded legal/evidentiary status used by the truth-aware layer; not legal advice. |
| `candidato_afectado` | Candidate/event scope: Cepeda, De la Espriella, both, or blank vote. |
| `direccion` | Coded direction such as positive, negative, mixed, contextual, or contrast. |
| `motif_primary` | Primary recurring narrative motif. |
| `frame` | Analytical framing category for the individual observation. |
| `emocion` | Dominant coded emotional register. |
| `dimension_impacto` | Main impact dimension used by agent interpretation. |
| `region` | Geographic relevance or scope where coded. |
| `intensidad` | Normalised signal intensity parameter. |
| `credibilidad` | Internal credibility/evidence parameter used by the experiment. |
| `riesgo_desinformacion` | Internal misinformation-risk parameter; not a definitive truth ruling. |
| `canales_probables` | Likely exposure channels represented as a coded collection. |
| `perfiles_relevantes` | Synthetic agent profiles for which the observation may be more relevant. |
| `resumen_para_agente` | Concise description supplied to agent-facing interpretation logic. |
| `fecha_corte` | Data-cutoff field associated with the record. |
| `source_strict` | Indicator that interpretation must remain source-traceable. |
| `source_category` | One of the nine source categories used for balancing. |
| `ownership_type` | Coded ownership/institutional type of source. |
| `geographic_scope` | Local, regional, national, international, or other coded scope. |
| `candidate_scope` | Normalised candidate/event scope used by the model. |
| `observation_role` | `canonical_signal` or `supporting_observation`. |
| `event_cluster_id` | Identifier for observations referring to the same underlying event. |
| `event_cluster_size` | Number of observations in the event cluster. |
| `source_class_balance_weight` | `N / (K × n_c)` inverse-frequency source-category weight. |
| `model_sampling_weight` | Source weight divided by cluster size and capped at three. |
| `engagement_likes` | Available like count; missing means unavailable. |
| `engagement_reposts` | Available repost/share count; missing means unavailable. |
| `engagement_comments` | Available comment count; missing means unavailable. |
| `engagement_views` | Available view count; missing means unavailable. |
| `engagement_status` | Availability/quality indicator for engagement fields. |

## Result-table fields

### `agent_opinions_abm_vs_llm_all.csv`

| Field | Meaning |
|---|---|
| `agent_id` | Unique synthetic-agent identifier. |
| `macro_region`, `department`, `municipality` | Synthetic geographic attributes. |
| `generation_cohort` | Synthetic generational cohort. |
| `residential_stratum` | Synthetic residential-stratum category. |
| `current_state` | Final heuristic ABM state before LLM deliberation. |
| `llm_final_state` | Validated final LLM state. |
| `decision_transition` | Human-readable ABM-to-LLM transition. |
| `decision_changed` | Boolean indicator that final states differ. |
| `comparison_status` | Merge/validation status for the comparison. |
| `confidence` | Final heuristic confidence indicator. |
| `uncertainty` | Final heuristic uncertainty indicator. |
| `decision_confidence` | Structured LLM confidence. |
| `heuristic_signal_title` | High-attribution signal title used in heuristic reconstruction. |
| `dominant_motif` | Dominant motif associated with the agent record. |
| `dominant_source_category` | Dominant source category associated with the agent record. |
| `abm_dominant_emotion` | Dominant heuristic emotion. |
| `heuristic_reconstructed_opinion` | Natural-language reconstruction of ABM state; not a literal conversation. |
| `heuristic_reconstruction_basis` | Structured basis of the reconstructed opinion. |
| `decisive_argument` | LLM-generated decisive argument. |
| `rationale_summary` | LLM-generated rationale summary. |
| `dominant_emotion` | LLM-generated dominant emotion. |
| `social_media_post` | Synthetic stylised post generated for analysis. |

### `section_23_kpi_summary.csv`

Contains one row of dashboard headline values. Fields include agent count, candidate leaders, state-change rate, LLM confidence, blank-vote share, entropy, language-audit pass rate, tone score, top internal driver/source/semantic concepts, and the mandatory interpretation boundary.

## Missing-value contract

Missing values must preserve the distinction between “not observed/not available” and numerical zero. Any imputation must be explicit, versioned, justified, and tested.
