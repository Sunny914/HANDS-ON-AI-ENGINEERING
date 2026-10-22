# Stage 12 Testing

- Metric tests use hand-computed cases, including a short retrieved list and an empty relevant set.
- Groundedness tests fail when a citation was not retrieved, even if the prose looks finished.
- Regression tests freeze `dataset_version` and two `config_id` values.
- No network in the default suite.
- A judge test uses a stub that returns the opposite of the rule, and the gate still fails.
