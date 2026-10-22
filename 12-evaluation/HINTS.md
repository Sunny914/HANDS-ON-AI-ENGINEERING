# Stage 12 Hints

Stop at the first level that helps. H4 is a review of your code and is not written here.

## ex-01

- **H1:** A label and a prediction are different records.
- **H2:** Require `dataset_version`, case id, and a task type. Reject a duplicate case id.
- **H3:** Add a field for tags. A missing version is an error, not `"latest"`.

## ex-02

- **H1:** The denominator is part of the definition.
- **H2:** Precision divides by k. Recall divides by the size of the relevant set. Hit@k is a separate function.
- **H3:** For retrieved `["a"]`, relevant `{"a","b"}`, and k of 3, precision is 1/3 and recall is 1/2. Write that case as a test before generalizing.

## ex-03

- **H1:** Schema validity is not answer quality.
- **H2:** Check required keys and types. Ignore prose.
- **H3:** A missing `citations` list fails. An extra key fails if the schema is closed. An empty list can be valid for a non-research task. Document which.

## ex-04

- **H1:** Groundedness looks at citations and retrieved ids, not at how nice the sentence is.
- **H2:** Subset check. Order does not matter.
- **H3:** Retrieved `{n1}` and citations `["n1","n9"]` fail. Citations `[]` fail a research case. A high recall score does not change either result.

## ex-05

- **H1:** The tool name and the arguments are two checks.
- **H2:** Canonicalize JSON object key order before compare. Compare only the labeled required fields, then reject unknown fields.
- **H3:** Expected `search` with `{q: refund}` fails a prediction of `search` with `{q: refund, limit: 1}` if the schema is closed. Task success also requires the stop reason the label allows.

## ex-06

- **H1:** A metric answers one question. Write the question in a sentence.
- **H2:** For each scenario, name the metric someone might brag about and the failure it hides.
- **H3:** Draft the three scenarios before you look at the acceptance examples again. Include one case where accuracy is high because most examples are easy.

## ex-07

- **H1:** A regression is a case that used to pass.
- **H2:** Key the join by case id. Require equal `dataset_version`.
- **H3:** Baseline passes c1 and c2. Candidate fails c1 and passes c2. The regression list is `[c1]`. A candidate-only case id is a dataset mismatch, not a regression.

## ex-08

- **H1:** The judge is not the gate.
- **H2:** Store rule outcome, judge outcome, and disagreements. The gate reads the rule for citation checks.
- **H3:** Stub the judge to return pass on a case the rule fails. Assert the gate fails and the disagreement list contains that case id.

## arch-01

- **H1:** A gate you cannot explain will be turned off during a release.
- **H2:** Pick two blocking checks and one report-only metric. Say who is harmed by a false pass.
- **H3:** Groundedness failures block. Mean latency is reported and does not block unless you write a separate reason. Five cases do not justify a claim of general superiority.

## dbg-01

- **H1:** Compute the metric by hand for one list.
- **H2:** See which ids increment the hit count.
- **H3:** Count ids that are in the relevant set. Divide by k. Add a test where a wrong id must lower precision.

## dbg-02

- **H1:** Two booleans go in. The release decision uses only one of them today.
- **H2:** Find the flag that is ignored.
- **H3:** Fail the gate when the rule failed, and keep the judge result in the report.
