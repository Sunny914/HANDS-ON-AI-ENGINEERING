# Requirements

## Stories

- As an engineer, I rerun the same dataset version and get the same score from the same predictions.
- As a reviewer, I see which case regressed, not only a mean.
- As a release owner, I can block on a rule even when a judge likes the answer.

## Functional

- A versioned dataset of at least eight cases, with two task types. One type must be retrieval-plus-answer or an equivalent pair of scores. The other may be tool-and-task completion.
- Labels and predictions are separate files.
- Deterministic metrics from this stage. Hit@k may appear and must not replace precision and recall.
- A baseline `config_id` and one candidate.
- A regression list and a known-failure list.
- A written threshold in `GATE.md`, including what it does not prove at this sample size.
- Failure tags such as `missed_relevant`, `bad_citation`, `schema`, `wrong_tool`, `budget`, `judge_disagreement`.
- Optional stub judge. It cannot clear a rule failure.
- A report file a second process can read.
- Offline by default. `RUN_LIVE_LLM` may add a real judge and is not required.

## Nonfunctional

- No network in the default test command.
- Reports include dataset version, config id, and the metric definitions you implemented.
- Re-running on unchanged files does not change the pass bits.

## Non-goals

A public leaderboard, a vendor eval product, and a claim that the candidate is generally better.
