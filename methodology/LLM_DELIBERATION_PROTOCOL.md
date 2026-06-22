# LLM Deliberation Protocol

## Purpose

The LLM stage performs a second synthetic decision after completion of the heuristic twenty-day ABM. It tests how a language model interprets an agent-specific, traceable cognitive dossier under a constrained output schema.

It is not a claim that the model reproduces human cognition.

## Execution order

1. Complete and validate the heuristic ABM.
2. Build one cognitive dossier per eligible agent.
3. Construct a provider request with a controlled system instruction and structured decision task.
4. Submit a synchronous pilot.
5. Validate pilot outputs and language controls.
6. Submit the full agent set through the provider's batch mechanism.
7. Retrieve and validate outputs.
8. De-anonymise option labels only after structural validation.
9. Merge decisions with ABM states and analytical attributes.

## Provider configuration recorded in the supplied run

- Provider: Anthropic Claude.
- Model identifier: `claude-sonnet-4-6`.
- Temperature: `0.35`.
- Maximum output tokens: `1,200`.
- Agent limit: 1,000 in the full profile.

These values describe the supplied execution artifacts. A future run with a different model identifier or provider version is a new experimental condition.

## Credential handling

The API key is read from `ANTHROPIC_API_KEY`. It must not be stored in the notebook, output tables, checkpoint, Git history, or release bundle.

## Cognitive dossier

A dossier may include:

- synthetic agent identifier and profile attributes;
- macro-region and controlled language-style context;
- initial and final heuristic states;
- position, confidence, uncertainty, fatigue and mobilisation;
- blank-vote and abstention propensities;
- dominant sources, motifs, semantic terms and emotions;
- direct and peer exposure summaries;
- source-trust and motif-memory summaries;
- decisive or high-impact signals;
- interaction and network context;
- allowed final decision categories.

The dossier is evidence-bounded: the LLM should reason from the supplied record rather than invent external campaign facts.

## Anonymous option handling

Candidate options may be represented with anonymous internal labels during deliberation to reduce direct name anchoring. Mapping back to named synthetic states occurs after response validation. The mapping must be versioned and preserved with the run.

## Structured output

The output schema should constrain at least:

- final decision state;
- decision confidence;
- rationale summary;
- decisive argument;
- dominant emotion;
- a synthetic social-media-style expression;
- optional uncertainty or caveat fields.

Responses are parsed and validated with a typed schema. Invalid responses are retained in an error table rather than silently coerced.

## Language protocol

Notebook documentation is in English. Synthetic political and sociolinguistic output may remain in Colombian Spanish. Regional markers are controlled stylistic features, not evidence of authentic regional speech or demographic testimony.

Language validation should check:

- permitted state labels;
- non-empty rationale;
- bounded confidence;
- prohibited identity claims;
- overuse of regional markers;
- accidental exposure of anonymous option mappings;
- instruction leakage;
- unsupported external facts.

## Failure handling

The pipeline must record:

- request identifier;
- agent identifier;
- HTTP/provider status where available;
- parse or schema error;
- raw response path or checksum when retained;
- retry status;
- final inclusion/exclusion decision.

Retries must not erase the first failed response. A retried output is a new attempt associated with the same agent.

## Reproducibility limitations

Remote LLM responses may change because of provider-side model updates, non-deterministic inference, service configuration, or unavailable historical model versions. Reproduction therefore requires the exact prompt, schema, provider, model identifier, temperature, token limit, request checksum, result checksum and execution timestamp.

The LLM layer should be described as protocol-reproducible and artifact-auditable, not guaranteed bitwise deterministic.
