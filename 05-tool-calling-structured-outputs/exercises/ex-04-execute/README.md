# Validate Then Execute

**ID:** `ex-04`
**Stage:** 05-tool-calling-structured-outputs
**Difficulty:** L3
**Category:** Integration

## Objective

Run a tool only after the schema succeeds.

## Prerequisites

ex-03.

## Problem

`get_order` reads an in-memory dict of orders. Bad arguments never call it.

## Requirements

A probe or fake records calls. Validation failure means zero calls. Success returns the order. Missing order is a tool error result or a named error. Document which.

## Constraints

Still no permission check. That is ex-05.

## Inputs and outputs

Tool name and raw dict in. A result object out.

## Edge cases

Unknown tool. Unknown order id. Valid id.

## Errors

Unknown tool and validation failure are different.

## Acceptance criteria

Three tests: valid, bad type, unknown tool. The probe count is asserted.

## Testing

Unit tests with an in-memory order table.

## Common mistakes

`**raw_args` into the function and a crash as the only validation.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

What did the probe prove that a status string would not?

## Extension

Add a timeout around the callable using a fake that sleeps. Optional if you inject the clock.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-04` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
