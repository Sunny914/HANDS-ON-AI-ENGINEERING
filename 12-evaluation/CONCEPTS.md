# Stage 12 Concepts

Read this before scoring anything. Stage 04 already taught hit@k on a golden retrieval file. This stage adds metrics that answer different questions, and it keeps those questions apart.

## What a case is

A case is one labeled example: an id, an input, the behavior you expect, and tags such as `retrieval` or `refusal`. A dataset is a list of cases plus a `dataset_version` string. Changing a label changes the version. A score from version `v1` is not a regression against version `v2`.

Do not put the system output you hope to grade into the case as if it were the label. The label is what a correct system should do. The prediction is what this run did.

Leakage means the model, or you, saw the labels as part of the prompt or the corpus. A fixture that includes the expected answer inside the retrieved text is a leaked case. Mark it. Do not use it as evidence of quality.

## Retrieval metrics

For one case, `relevant` is the set of ids that should be found. `retrieved` is the ordered list the system returned. `top_k` is the first k ids, or the whole list if it is shorter.

- Hit@k is 1 when `top_k` intersects `relevant`, otherwise 0. Stage 04 owns this check.
- Precision@k is the count of ids in `top_k` that are in `relevant`, divided by k. Empty slots in a short list count as not relevant, so the denominator stays k.
- Recall@k is that same count divided by the number of relevant ids.

If `relevant` is empty, recall is undefined. Return a named error or skip the case. Do not treat 0/0 as a perfect score.

Worked precision and recall, which your tests can copy: retrieved `["a"]`, relevant `{a, b}`, k = 3. One relevant id is in the top, so precision is 1/3 and recall is 1/2. Hit@k is 1.

F1@k is the harmonic mean `2 * p * r / (p + r)` when both p and r are defined. If either is 0, F1 is 0. If either is undefined, F1 is undefined.

A high precision with terrible recall means the few items you returned were right and you missed the rest. A high recall with terrible precision means you returned almost everything. One number does not describe the system.

## Generation and grounding

Retrieval recall does not mean the answer is faithful. Groundedness here is a rule, not a model opinion:

- Every citation id in the answer was in that case's retrieved ids.
- A research-style case with no citations is not grounded.
- Extra fluent text is not a pass.

Answer relevance, as a string check, can be "the required fact string appears." That is weaker than human relevance. Say so in the report.

## Tools, tasks, and approval

- Tool selection is correct when the chosen tool name equals the labeled name.
- Argument correctness is canonical equality of the required fields. Extra fields fail a closed schema.
- Task completion requires the labeled outcome, a passed evidence or schema check, and no budget overrun. `partial` is not success unless the label says partial is the expected stop.
- Approval compliance means a labeled high-risk action did not execute without an approval record. Stage 11 owns the mechanism. This stage only scores the trace.

## Judges

A model judge is another model call that labels a case. It has false positives and false negatives. When a deterministic rule fails and the judge passes, the release gate keeps the failure. Record the disagreement. Do not average them into a friendlier score.

A judge is optional. Default tests use rules and fixtures.

## Regression

Store a report with `dataset_version`, `config_id`, per-case outcomes, and aggregate metrics that are defined. A regression is a case id that passed under the baseline config and fails under the candidate, on the same dataset version. A new case is a dataset change, not a regression.

With a handful of cases, the report is descriptive. It does not prove one configuration is better in general. Write that limit next to any threshold.

## Release gates

A gate is a rule such as "groundedness failures must be zero" or "mean precision@3 is at least the baseline." A gate can block a bad change and still miss harms you did not label. Thresholds are choices. Document who is hurt by a false pass and by a false fail.
