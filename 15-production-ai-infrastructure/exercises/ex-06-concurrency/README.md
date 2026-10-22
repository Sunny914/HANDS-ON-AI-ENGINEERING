# Concurrency Limit

**ID:** `ex-06`
**Stage:** 15-production-ai-infrastructure
**Difficulty:** L4
**Category:** Focused implementation

## Objective

Reject or hold work past a cap.

## Prerequisites

Stage 01 async basics. ex-03.

## Problem

Allow at most two adapter calls in flight.

## Requirements

The third call receives a named busy error, or it waits until a slot frees. Tests must be deterministic. A counter or a fake adapter that tracks `in_flight` is enough if a real thread race is hard to assert. Document the choice.

## Constraints

No flaky sleep assertion.

## Inputs and outputs

Three overlapping calls.

## Edge cases

Cap of 1. Cap of 2 with two successes. A call that errors still releases its slot.

## Errors

A leaked slot that makes every later call busy fails the exercise.

## Acceptance criteria

The third call is busy or ordered behind the first two, as you documented. An error path decrements the counter.

## Testing

Unit tests.

## Common mistakes

A global counter that never decrements.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

How is this different from a queue you did not build?

## Extension

Record a rejected count on the Stage 13 event store.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-06` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
