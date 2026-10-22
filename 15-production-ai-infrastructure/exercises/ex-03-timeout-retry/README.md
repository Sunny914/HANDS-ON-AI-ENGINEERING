# Bounded Timeout and Retry

**ID:** `ex-03`
**Stage:** 15-production-ai-infrastructure
**Difficulty:** L3
**Category:** Focused implementation

## Objective

Stop retrying forever.

## Prerequisites

Stage 01 retry versus idempotency. ex-01.

## Problem

Call an adapter with a timeout and a retry policy.

## Requirements

Retry only timeout and 503. Maximum three calls. A validation error is one call. The sleeper is injected and records the delays. Backoff may be constant in this exercise if you document full jitter as a follow-on.

## Constraints

No real sleep in the assertion path.

## Inputs and outputs

An adapter callable and a policy.

## Edge cases

Success on the second call. Always timeout. Non-retryable error.

## Errors

The final error names the attempt count.

## Acceptance criteria

Three tests matching those edges. The always-timeout test calls the adapter three times.

## Testing

Unit tests.

## Common mistakes

Retrying HTTP 400.

## Completion checklist

- [ ] Acceptance criteria pass on code you wrote
- [ ] Required tests exist and you ran them
- [ ] You can explain the design without the hint file

## Reflection

What side effect makes a retry unsafe even for a timeout?

## Extension

Add jitter by injecting a random function and asserting the delay changed.

## Hints

Attempt the work first. Then open [../../HINTS.md](../../HINTS.md) section `ex-03` and stop at the first level that unblocks you. H3 is a next step, not a solution. H4 is a review of your attempt and is not written in that file.
