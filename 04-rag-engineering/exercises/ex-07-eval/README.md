# Tiny Retrieval Evaluation

**ID:** `ex-07`
**Stage:** 04-rag-engineering
**Difficulty:** L4
**Category:** Testing

## Objective

Score a golden set you can fail on purpose.

## Prerequisites

ex-04 and ex-05. `fixtures/golden_retrieval.json` is only a shape. You may write your own cases.

## Problem

Implement hit@k for expected chunk ids. Build a corpus and a question list of at least three cases. One case must miss, so the score is not always 1.

## Requirements

Also check one answer fixture for inclusion of a required fact string, using the fake completer. That is the answer check. Do not call an LLM judge.

## Constraints

No network.

## Inputs and outputs

Golden file in. A report with per-case hit and the mean.

## Edge cases

k = 1 versus k = 3 can change the hit. Show that if it is true for your data.

## Errors

Missing expected id is a miss, not an exception.

## Acceptance criteria

The mean is asserted exactly. The miss case is named in the test.

## Testing

This exercise is the test.

## Common mistakes

A golden set that uses the same string as the only chunk, so retrieval cannot fail.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

What would you add before trusting this number on a real corpus?

## Extension

Add a latency field to the report using a fake clock.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-07` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
