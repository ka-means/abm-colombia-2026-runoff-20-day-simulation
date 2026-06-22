# Model Card

## Model identification

- **Name:** Colombia 2026 Hybrid ABM–LLM Runoff Simulation
- **Version:** 1.0.0
- **Input package:** source-balanced v5.1
- **Primary implementation:** Python/Jupyter notebook
- **Simulation horizon:** twenty daily steps, 1–20 June 2026
- **Synthetic population:** 1,000 agents in the full profile
- **Cognitive provider recorded in the supplied run:** Anthropic Claude

## Summary

The model is an explanatory multi-agent computational experiment. It combines a heuristic agent-based model with a post-simulation LLM deliberation stage. The ABM creates heterogeneous synthetic agents, multiplex social networks, selective exposure, source trust, motif memory, social diffusion, fatigue, mobilisation, uncertainty, and daily voting-state transitions. The LLM stage receives a structured cognitive dossier for each agent and produces a validated synthetic decision and explanation.

## Intended uses

The model is intended for:

- studying how micro-level information and interaction rules generate macro-level patterns;
- teaching and researching agent-based modelling, computational social science, and multi-agent systems;
- testing source-balancing, event-clustering, traceability, and audit methods;
- comparing heuristic and dossier-constrained LLM decisions;
- exploring sensitivity to assumptions, parameters, network structures, and information diets.

## Out-of-scope and prohibited interpretations

The model must not be represented as:

- an opinion poll;
- an electoral forecast;
- a representative estimate of Colombian voters;
- a causal estimate of media influence;
- a measurement of individual or group psychology;
- evidence that a real region, occupation, age cohort, or socioeconomic group behaves like a synthetic stratum;
- a tool for political microtargeting, persuasion optimisation, voter suppression, or individual profiling.

## Architecture

### Heuristic ABM

The ABM includes:

- synthetic demographic and media-access attributes;
- regional and municipal heterogeneity;
- initial ideological and behavioural dispositions;
- four network layers;
- daily activation of audited signals;
- stochastic direct exposure;
- relevance-conditioned interpretation;
- adaptive source trust;
- finite motif memory;
- bounded cascade propagation;
- bounded-confidence social interaction;
- end-of-day state classification.

### Cognitive LLM layer

The LLM layer receives a dossier containing the agent's final heuristic state, information exposures, trust and memory summaries, behavioural propensities, semantic context, regional-language constraints, and decision options. A structured schema constrains the returned final state, confidence, rationale, decisive argument, emotion, and social-media-style expression.

The LLM stage does not modify the historical ABM trajectory.

## Inputs

The canonical source package contains 207 master observations across nine source categories. It distinguishes 201 canonical signals from six supporting observations grouped into 201 event clusters. It includes media observations, official social signals, campaign-personality records, international framing, amplifier records, blank-vote chronology, audits, and source-balance weights.

## Outputs

Primary outputs include:

- daily and final agent states;
- exposure, peer-transmission, interaction, cascade, trust and memory logs;
- daily entropy and emergence metrics;
- decision-attribution tables;
- semantic-dose and source-impact tables;
- cognitive dossiers;
- validated LLM decisions;
- ABM–LLM transition tables;
- sociolinguistic and tone diagnostics;
- static interactive dashboard;
- human-readable synthetic-agent records.

## Performance and quality indicators

The project evaluates data integrity, run completeness, state validity, source and event traceability, reproducibility of the heuristic layer, schema validity of LLM responses, language-style controls, and consistency between dashboard values and analytical tables.

The supplied run reports 1,000 agents, 15.6% ABM-to-LLM state change, mean LLM confidence of approximately 0.61, and a 96.7% language-audit pass rate where the audit is available. These indicators measure internal pipeline behaviour, not external predictive accuracy.

## Known limitations

- The population is synthetic and not survey-weighted.
- Behavioural rules are modeller-defined and path-dependent.
- Source availability and indexing are incomplete.
- Missing engagement metrics are unavailable, not zero.
- Source-category balancing does not establish candidate balance or population exposure.
- Network topology is synthetic.
- A single seed is insufficient for uncertainty quantification.
- LLM output may vary across model versions, service updates, temperature, prompt wording, and execution time.
- Generated regional language is controlled simulation text, not authentic testimony.
- No external ground-truth validation of vote shares is claimed.

## Maintenance

Any change to data rows, classifications, weights, rules, seeds, prompts, output schemas, or model identifiers requires a new version and updated manifests. Historical release artifacts should remain immutable.
