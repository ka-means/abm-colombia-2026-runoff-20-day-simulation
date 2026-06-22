# Ethics, Interpretation Boundary, and Limitations

## Core boundary

This project simulates synthetic agents. It does not observe, survey, diagnose, or predict identifiable people.

The output must not be presented as a measurement of the Colombian electorate or as evidence about how real demographic groups think.

## Political-use restrictions

The project is not designed for:

- individual voter profiling;
- campaign targeting or message optimisation;
- persuasion experiments on real users;
- voter suppression or turnout manipulation;
- automated political advertising;
- inferring political beliefs from personal data;
- ranking real people by susceptibility, ideology, or misinformation risk.

## Synthetic population

A population of 1,000 agents improves numerical resolution but does not create representativeness. Synthetic regional, age, occupation, socioeconomic, language and media-access variables are modelling constructs.

Regional shares in the dashboard are conditional model outputs, not regional polling estimates.

## Information-environment limitations

The audited corpus is curated and temporally bounded. It may omit unindexed broadcasts, private messaging, deleted posts, local communication, offline campaigning, late corrections, and events outside the collection process.

Category balancing reduces one form of collection imbalance but cannot prove neutrality, completeness, or equal real-world exposure.

## Annotation limitations

Motif, frame, direction, emotion, credibility and misinformation-risk fields involve analytical judgement. They should be audited and versioned. Disagreement is not automatically an error; undocumented or inconsistent application is.

## Behavioural-model limitations

The ABM uses bounded, fixed update rules. These rules simplify human political behaviour and cannot capture every factor relevant to real voting, including private experience, family history, strategic reasoning, material conditions, candidate evaluation, institutional trust, or last-minute events.

## Network limitations

The four network layers are synthetic. Their topology and interaction rules may generate diffusion patterns that differ substantially from real networks. Cascade results are therefore mechanism demonstrations.

## LLM limitations

Claude's output is generated from a dossier and prompt. It may display:

- provider/model biases;
- sensitivity to wording and option ordering;
- stochastic variation;
- overconfident explanations;
- plausible but unsupported inference;
- language stereotypes;
- changes across provider updates.

A coherent rationale is not evidence that the decision process is human-like or empirically valid.

## Sociolinguistic limitations

Generated Colombian Spanish and regional markers are stylised controls. They are not authentic testimony and must not be treated as representative speech samples. Overuse can become caricature; the language audit is intended to detect some, not all, such failures.

## Uncertainty limitations

A single run and seed do not quantify uncertainty. The published percentages are outcomes of one configured simulation. Scientific interpretation requires repeated seeds, parameter sweeps, alternative network structures, input perturbations, and LLM-protocol robustness checks.

## Candidate and blank-vote treatment

Candidate counts in the source table are not equal. Blank vote has specialised records and rules. These modelling choices must remain transparent because they can affect exposure and salience.

## Communication standard

Every public presentation should include language equivalent to:

> This is a synthetic ABM–LLM mechanism study. It is not polling, forecasting, representative estimation, causal inference, or measurement of real human cognition.

Results should be described as model-internal shares, transitions, associations, or emergent patterns—not as voter intention.
