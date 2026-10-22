# Two-Node Graph

**ID:** `ex-02`
**Stage:** 08-langgraph
**Difficulty:** L2
**Category:** Focused implementation

## Objective

Compile a graph that is only a straight line.

## Prerequisites

ex-01. ASSUMPTIONS.md imports.

## Problem

Validate text, then mark the state ready.

## Requirements

Use `StateGraph`. Empty text is not ready. Invoke once. No checkpoint yet.

## Constraints

No model. No cycle.

## Inputs and outputs

Initial dict with `text`. Final state includes `ok`.

## Edge cases

Empty string. A normal sentence.

## Errors

If `END` import differs, record the name that worked. Do not leave the test skipped.

## Acceptance criteria

Two invoke tests.

## Testing

Graph tests.

## Common mistakes

Doing both jobs in one node and adding a second node that returns nothing, just to look like a graph.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

What is the partial update of the second node?

## Extension

Add a third node that copies `text` into `echo` only when `ok` is true, still with a normal edge.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-02` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
