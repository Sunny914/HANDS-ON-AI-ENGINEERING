# List Updates

**ID:** `ex-04`
**Stage:** 08-langgraph
**Difficulty:** L3
**Category:** Focused implementation

## Objective

See replace versus append.

## Prerequisites

CONCEPTS.md reducers. ex-02.

## Problem

Two nodes each add an evidence id.

## Requirements

First, demonstrate the replacement behavior if that is the default in your version. Then configure the append behavior using the documented reducer. Both tests stay in the file so the difference is visible.

## Constraints

Do not mutate the incoming state list in place.

## Inputs and outputs

State with `evidence` ids.

## Edge cases

Node returns an empty list. Node returns one id.

## Errors

If the official reducer import fails, stop and write the import you attempted in the test module docstring, then use a local reducer you understand.

## Acceptance criteria

Final evidence contains both ids in order when append is configured.

## Testing

Graph or a tiny harness around the update function.

## Common mistakes

Appending on the shared input list so tests pass by accident.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

What bug looks like a reducer bug but is actually in-place mutation?

## Extension

Add a reducer that dedupes ids.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-04` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
