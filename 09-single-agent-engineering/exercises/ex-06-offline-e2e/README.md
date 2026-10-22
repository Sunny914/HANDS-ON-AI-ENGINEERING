# Offline End to End

**ID:** `ex-06`
**Stage:** 09-single-agent-engineering
**Difficulty:** L4
**Category:** Testing

## Objective

One test runs the service the way a caller would.

## Prerequisites

ex-01 through ex-05 in some form. You can write this against a thinner service if earlier pieces are injected.

## Problem

A three-note corpus, a script that searches and then finishes, and a result object.

## Requirements

Factory injects script, corpus, and budget. Assert tool order, stop reason, and citations.

## Constraints

No network. No LangGraph required.

## Inputs and outputs

Question in. Result out.

## Edge cases

Script asks to read an id search did not return. The tool returns not-found. The run does not crash.

## Errors

Uncaught KeyError fails the exercise.

## Acceptance criteria

Happy path and not-found path.

## Testing

This is the end-to-end test.

## Common mistakes

Asserting only that the result is non-empty.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

What would a live model add that this test cannot see?

## Extension

Parameterize a second question.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-06` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
