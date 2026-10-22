# When the Metric Misleads

**ID:** `ex-06`
**Stage:** 12-evaluation
**Difficulty:** L3
**Category:** Failure analysis

## Objective

Refuse a single score as a description of the system.

## Prerequisites

ex-02 and ex-04.

## Problem

Write `MISLEADING.md` for three situations.

## Requirements

Situations:

1. Accuracy is 0.9 because 9 of 10 cases are easy refusals, and the one research case is wrong.
2. Precision@1 is 1.0 while recall@5 is low.
3. A judge prefers the longer answer, and the longer answer cites an id that was not retrieved.

For each, name the flattering metric, the hidden failure, and the extra number you would report.

## Constraints

No code required. You may add a tiny numeric example.

## Inputs and outputs

A markdown note.

## Edge cases

A metric that is valid and still insufficient.

## Errors

Do not conclude that metrics are useless.

## Acceptance criteria

All three situations have a flattering metric and a counter-metric. The note says one number cannot clear a release.

## Testing

Self-review against the acceptance section after a draft.

## Common mistakes

Replacing the metric with a vibe check.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Which situation is closest to a system you would actually ship?

## Extension

Add a fourth situation about a leaked label in the prompt.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-06` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
