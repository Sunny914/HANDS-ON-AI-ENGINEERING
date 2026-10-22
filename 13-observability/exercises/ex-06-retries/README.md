# Retries Stay Visible

**ID:** `ex-06`
**Stage:** 13-observability
**Difficulty:** L3
**Category:** Failure analysis

## Objective

Stop a later success from hiding an earlier failure.

## Prerequisites

ex-05.

## Problem

Record two attempts of one tool. The first times out. The second succeeds.

## Requirements

Both events remain. `attempt` is 1 then 2. A summary includes `retry_count`. The timeout status is still queryable.

## Constraints

Injected clock.

## Inputs and outputs

Two attempt results.

## Edge cases

Three attempts. First attempt succeeds so retry count is 0.

## Errors

Overwriting attempt 1 fails the test.

## Acceptance criteria

The timeout-then-ok test and the single-success test.

## Testing

Unit tests.

## Common mistakes

Storing a list of statuses on one event and losing durations.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

When is a final `ok` a bad alert to suppress?

## Extension

Add a metric count of timeouts across requests.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-06` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
