# One Budget Object

**ID:** `ex-03`
**Stage:** 09-single-agent-engineering
**Difficulty:** L3
**Category:** Focused implementation

## Objective

Stop scattering counters across the loop.

## Prerequisites

Stage 07 budgets.

## Problem

`Budget` tracks steps, milliseconds, and tokens. The loop consults it.

## Requirements

`consume` and `exhausted_reason`. First exhausted resource wins and is named. Inject the clock.

## Constraints

No sleep.

## Inputs and outputs

Limits and a clock.

## Edge cases

All remaining zero. Exact fit.

## Errors

Negative consume raises.

## Acceptance criteria

Three exhaustion tests.

## Testing

Unit tests plus one loop test that stops because the object says so.

## Common mistakes

A second hidden counter in the loop that disagrees with the object.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

Where should the budget be created: per request or per process?

## Extension

Add a cost field using fictional prices.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-03` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
