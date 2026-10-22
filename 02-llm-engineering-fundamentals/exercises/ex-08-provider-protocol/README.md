# Provider Protocol and a Fake

**ID:** `ex-08`
**Stage:** 02-llm-engineering-fundamentals
**Difficulty:** L4
**Category:** Integration

## Objective

Define the interface a router can call.

## Prerequisites

ex-05, ex-06, Stage 01 timeout errors.

## Problem

Implement a protocol or equivalent structural interface, a fake provider, and one adapter that reads Provider A fixture JSON as if it were the HTTP body.

## Requirements

The fake can be scripted to return a response, raise a timeout, or raise a caller error. The fixture adapter does not open a socket. Optional: a live adapter behind an env flag, skipped by default.

## Constraints

No API keys in files.

## Inputs and outputs

Normalized request in. Normalized response out.

## Edge cases

The fake's script is exhausted.

## Errors

Timeout and caller error are distinguishable.

## Acceptance criteria

A test swaps the fake without changing the caller. A test parses the A fixture through the adapter.

## Testing

No live network in default tests.

## Common mistakes

Importing the fake inside the router so tests cannot replace it. Subclassing a vendor client you do not have.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

What would a second vendor adapter be forbidden to import?

## Extension

Implement Provider B's fixture as a second adapter.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-08` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
