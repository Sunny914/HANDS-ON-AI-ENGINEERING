# Conditional Route

**ID:** `ex-03`
**Stage:** 08-langgraph
**Difficulty:** L3
**Category:** Focused implementation

## Objective

Send good and bad inputs to different nodes.

## Prerequisites

ex-02.

## Problem

After validate, route to `accept` or `reject`. Each node sets a `label`.

## Requirements

The route function is unit-tested without the graph. The graph test checks the label.

## Constraints

No interrupt.

## Inputs and outputs

Text in. Label out.

## Edge cases

Whitespace-only text is reject.

## Errors

A route name you forgot to register should fail the test, not be caught and relabeled.

## Acceptance criteria

Unit tests for the route and two graph tests.

## Testing

Both kinds.

## Common mistakes

If/else inside one node that sets the label, with a conditional edge that is never used.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

When is an if inside the node the better design?

## Extension

Route a third state, `ask`, when text is a question mark only. Optional.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-03` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
