# Shared State or Messages

**ID:** `arch-02`
**Stage:** 10-multi-agent-systems
**Difficulty:** L4
**Category:** Architecture comparison

## Objective

Choose one coordination mechanism and its failure test.

## Prerequisites

Stage 06 state ownership. ex-02.

## Problem

Write `COORDINATION.md`. Choose shared state or message handoffs for the project.

## Requirements

Name the writer for evidence ids, for each specialist conclusion, and for the final answer. Describe either the lost-id failure for messages or the double-writer failure for shared state, and the test that would catch it.

## Constraints

Do not choose both for the same fields.

## Inputs and outputs

A short design note.

## Edge cases

A worker crashes after producing ids the others have not seen.

## Errors

A second writer of the final answer.

## Acceptance criteria

The note names one mechanism, field owners, and one test.

## Testing

Not code.

## Common mistakes

A global dict with no owners.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Which choice makes prompt-injection propagation easier, and how will you contain it?

## Extension

Sketch the trace row for a dropped handoff.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `arch-02` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
