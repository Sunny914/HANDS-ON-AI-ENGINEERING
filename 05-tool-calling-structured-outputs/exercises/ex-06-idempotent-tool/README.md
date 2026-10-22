# Idempotent Refund

**ID:** `ex-06`
**Stage:** 05-tool-calling-structured-outputs
**Difficulty:** L3
**Category:** Integration

## Objective

Retry a side effect without doing it twice.

## Prerequisites

ex-05. Stage 01 idempotency idea.

## Problem

`refund` appends a ledger row. The same idempotency key returns the same receipt and does not append again.

## Requirements

The key is an argument you validate, or a header-like field on the call context. Pick one and document it. A different key creates a second row.

## Constraints

In-memory ledger.

## Inputs and outputs

Refund args plus key. Receipt out.

## Edge cases

Same key with a different amount. Treat as conflict. Do not apply the second amount.

## Errors

Conflict is distinct from denial.

## Acceptance criteria

Two calls, one ledger row, same receipt id. Conflict test. Denial still creates nothing.

## Testing

Unit tests.

## Common mistakes

Key stored after the append, so a crash window is ignored and also the happy path double-applies. Look at the order.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

What is still unsafe if two processes share nothing?

## Extension

Store the request hash beside the key.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-06` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
