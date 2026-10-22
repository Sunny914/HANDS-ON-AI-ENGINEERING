# Precision and Recall at k

**ID:** `ex-02`
**Stage:** 12-evaluation
**Difficulty:** L2
**Category:** Focused implementation

## Objective

Implement the retrieval definitions from the concept notes.

## Prerequisites

ex-01. Stage 04 hit@k. [CONCEPTS.md](../../CONCEPTS.md).

## Problem

Compute hit@k, precision@k, and recall@k for one case.

## Requirements

Use denominator k for precision even when the retrieved list is shorter than k. Recall is undefined when there are no relevant ids. Do not report undefined recall as 1.

## Constraints

Pure functions. No embeddings.

## Inputs and outputs

Relevant ids, ordered retrieved ids, and k.

## Edge cases

k larger than the list. Duplicate ids in the retrieved list. Empty relevant set. k of 0.

## Errors

k less than 1 raises a named error. Duplicate retrieved ids count once. Document that rule.

## Acceptance criteria

The case in [CONCEPTS.md](../../CONCEPTS.md) with retrieved `["a"]`, relevant `{a, b}`, and k of 3 returns precision 1/3 and recall 1/2. A no-relevant case does not return recall 1. Hit@k is 1 or 0 and is not used as precision.

## Testing

Hand-computed unit tests.

## Common mistakes

Dividing precision by the length of the returned list while claiming the concept definition.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Which user is harmed by high precision and low recall?

## Extension

Add F1@k only when both inputs are defined.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-02` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
