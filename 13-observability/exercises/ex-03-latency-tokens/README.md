# Latency and Token Fields

**ID:** `ex-03`
**Stage:** 13-observability
**Difficulty:** L2
**Category:** Focused implementation

## Objective

Measure with a fake clock.

## Prerequisites

ex-01.

## Problem

Start and finish an operation. Record duration and, for model events, token counts.

## Requirements

Duration is non-negative milliseconds. Token fields are absent or null on tool events. A finish without start is an error.

## Constraints

No sleep. No price API.

## Inputs and outputs

Clock readings and optional token counts.

## Edge cases

Zero duration. Finish called twice. Negative token count.

## Errors

Negative tokens are rejected. Negative duration is rejected.

## Acceptance criteria

A 15 ms span, a tool span without tokens, and a double-finish error.

## Testing

Unit tests.

## Common mistakes

Calling `time.sleep` so the test is slow and flaky.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Why is a token count not yet a cost?

## Extension

Add an estimate field that multiplies tokens by a rate passed into the constructor. Label it `estimate`.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-03` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
