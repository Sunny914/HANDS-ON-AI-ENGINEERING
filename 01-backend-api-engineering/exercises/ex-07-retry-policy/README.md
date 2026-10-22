# Retry Policy

**ID:** `ex-07`
**Stage:** 01-backend-api-engineering
**Difficulty:** L3
**Category:** Focused implementation

## Objective

Decide retries from the kind of failure, not from frustration.

## Prerequisites

ex-01 and ex-06.

## Problem

The upstream catalog sometimes times out and sometimes returns 503 or 429. It also returns 404 when the item does not exist. Blind retries would amplify 404s and duplicate unsafe POSTs.

## Requirements


- Implement a pure `should_retry` decision.
- Retry timeouts, 429, and 503, up to a configured limit.
- Do not retry 400, 401, 404, or 422.
- Do not retry POST unless the caller marks the operation idempotent.
- A separate loop may call the decision. Sleeping is allowed in the loop, not inside the decision.


## Constraints

The decision function performs no I/O.

## Inputs and outputs

Document the arguments. Return bool.

## Edge cases

Attempt already equal to the limit. Status missing because the failure was a timeout.

## Errors

A permanent error returns without another call.

## Acceptance criteria

Tests cover timeout, 503, 404, POST without the flag, and POST with the flag.

## Testing

Unit tests only.

## Common mistakes

`except Exception: retry`. Retrying until the process dies.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

What state would you need before a POST is safe to retry?

## Extension

Add a maximum elapsed time, not only a maximum attempt count.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-07` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
