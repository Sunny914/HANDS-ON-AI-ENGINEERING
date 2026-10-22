# Trust Boundary

**ID:** `arch-01`
**Stage:** 05-tool-calling-structured-outputs
**Difficulty:** L4
**Category:** Architecture

## Objective

Design the tool assistant before coding it.

## Prerequisites

ex-07.

## Problem

Write `YOUR_DESIGN.md`. The assistant can get an order and request a refund for a support principal. Guests can get their own order only.

## Requirements

Answer: modules, principal source, where schema lives, where policy lives, where the ledger lives, what is logged, what a model fixture is allowed to contain, and which tests use no network.

## Constraints

No assistant package yet.

## Inputs and outputs

Design note.

## Edge cases

Same idempotency key, different amount.

## Errors

Show denial versus validation versus tool failure as three results.

## Acceptance criteria

The principal is not parsed out of the tool arguments alone.

## Testing

List the fakes: orders and ledger.

## Common mistakes

A single `agent.py` that both calls the provider and mutates the ledger with `**kwargs`.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

What will Stage 07 add that you are not building?

## Extension

Note how an MCP host would call the same executor.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `arch-01` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
