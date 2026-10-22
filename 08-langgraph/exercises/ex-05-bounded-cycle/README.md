# Bounded Cycle

**ID:** `ex-05`
**Stage:** 08-langgraph
**Difficulty:** L3
**Category:** Integration

## Objective

Loop in the graph, not in a hidden while.

## Prerequisites

ex-01 and ex-03.

## Problem

`collect` increments `loops` and can route back to itself until a max.

## Requirements

Max is 3. A test fails if collect's counter exceeds 3. The graph reaches `done`.

## Constraints

The node itself must not contain `while loops < max`. The edge does the repetition.

## Inputs and outputs

State with `loops`.

## Edge cases

Max 0 never enters collect. Document how you set the start edge.

## Errors

A missing end edge is a failed test, not a timeout you ignore.

## Acceptance criteria

Counter test and done test.

## Testing

Graph tests. Set a recursion or step limit if your version requires one, and document it.

## Common mistakes

A while loop inside collect that makes the graph look linear.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

How is this different from Stage 07's max_steps?

## Extension

Route out early when a `found` flag is set.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-05` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
