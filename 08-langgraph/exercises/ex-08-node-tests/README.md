# Node Tests and Graph Tests

**ID:** `ex-08`
**Stage:** 08-langgraph
**Difficulty:** L4
**Category:** Testing

## Objective

Test a pure node and the wiring separately.

## Prerequisites

ex-03.

## Problem

`score_evidence` is a pure function a node wraps. The graph only routes on the score.

## Requirements

Unit tests cover the score thresholds without `compile`. One graph test checks the route. The fake notes are local strings.

## Constraints

No model.

## Inputs and outputs

Note text in. Score and route out.

## Edge cases

Empty note scores as unusable.

## Errors

Do not catch exceptions inside the node to force a route.

## Acceptance criteria

At least two unit tests and one graph test. The unit tests do not import the compiled graph.

## Testing

This is the testing exercise.

## Common mistakes

Only testing through `invoke`, so a routing bug and a scoring bug look the same.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Which test would you run first when the route is wrong?

## Extension

Add a test that the node does not mutate the input dict.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-08` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
