# Groundedness Separate from Retrieval

**ID:** `ex-04`
**Stage:** 12-evaluation
**Difficulty:** L3
**Category:** Integration

## Objective

Show that a good retrieval score can still hide a bad answer.

## Prerequisites

ex-02.

## Problem

Score citations against the ids that were retrieved for that case.

## Requirements

A research case passes only when every citation was retrieved and the citation list is non-empty. Report retrieval recall and groundedness as different fields. A case may have high recall and failed groundedness.

## Constraints

Rule only. No judge.

## Inputs and outputs

Retrieved ids, citation ids, and the recall score.

## Edge cases

Duplicate citations. Citation of an id that was relevant but not retrieved. No citations.

## Errors

Do not throw away the recall number when groundedness fails.

## Acceptance criteria

One case passes both. One case has recall 1 and groundedness fail. One research case with no citations fails groundedness.

## Testing

Unit tests that assert both fields.

## Common mistakes

Setting groundedness equal to recall.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Why is a fluent answer with a fake citation worse than a short abstention?

## Extension

Require the citation to come from a `read` observation rather than a search snippet. Document the stricter rule.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-04` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
