# Fallback Routing

**ID:** `ex-09`
**Stage:** 02-llm-engineering-fundamentals
**Difficulty:** L4
**Category:** Integration

## Objective

Fail over to a second provider without looping on the first.

## Prerequisites

ex-07 and ex-08.

## Problem

Primary times out twice. Secondary returns text. A caller error on the primary must not be retried on the secondary if you document the call as invalid.

## Requirements

Ordered candidates. Retry limit per provider. Ledger rows for each attempt. Result includes which provider served the text.

## Constraints

Inject providers. No network.

## Inputs and outputs

Request plus route config in. Response plus attempt count out.

## Edge cases

All providers fail. Duplicate name in the candidate list.

## Errors

When all fail, raise a typed error that includes the attempt count.

## Acceptance criteria

Tests: timeout then success; caller error stops; all fail; ledger length matches attempts.

## Testing

Fakes only.

## Common mistakes

Catching `Exception` and always falling over, including bugs in your own code.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

When is fallback the wrong product behavior?

## Extension

Add a simple latency budget that skips a provider.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-09` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
