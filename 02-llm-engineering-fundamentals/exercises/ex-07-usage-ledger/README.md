# Usage and Cost Ledger

**ID:** `ex-07`
**Stage:** 02-llm-engineering-fundamentals
**Difficulty:** L3
**Category:** Focused implementation

## Objective

Record tokens, latency, and a fictional cost.

## Prerequisites

ex-04.

## Problem

Each attempt should append a ledger row. Cost uses a price card you define in integer units so tests stay exact.

## Requirements

Price card: input and output price per thousand tokens, labeled fictional. Ledger lists rows. A summary totals tokens and cost.

## Constraints

No floats for money unless you quantize and test the rounding rule.

## Inputs and outputs

Usage, latency milliseconds, provider name, model name.

## Edge cases

Zero completion tokens. Two attempts summed.

## Errors

Negative tokens rejected.

## Acceptance criteria

A known usage yields the cost you computed by hand in the test docstring.

## Testing

Unit tests.

## Common mistakes

Using `len(text)` as the token count after you already have usage.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

What must never be copied into the ledger from the user message?

## Extension

Add a per-request id so retries group into one call.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-07` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
