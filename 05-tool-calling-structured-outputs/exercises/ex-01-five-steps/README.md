# Trace a Tool Call

**ID:** `ex-01`
**Stage:** 05-tool-calling-structured-outputs
**Difficulty:** L1
**Category:** Conceptual reasoning

## Objective

Name the five steps on a concrete payload.

## Prerequisites

CONCEPTS.md.

## Problem

Use `fixtures/tool_call.json`. Write `TRACE.md` that walks the five steps. Say what your code does at each step and what the model must not do.

## Requirements

Include one sentence on a bad `order_id` and one on a caller who is not allowed to read orders.

## Constraints

No tool implementation required.

## Inputs and outputs

A markdown trace.

## Edge cases

The fixture is well formed. You still describe the ill-formed case.

## Errors

Do not treat the JSON file as already safe.

## Acceptance criteria

A reviewer can point to steps 2 and 3 as application code.

## Testing

Not code. Read it against CONCEPTS.md.

## Common mistakes

Step 4 is 'the model calls the database'.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

Which step is missing in a demo that passes model JSON straight into a function?

## Extension

Add a sixth line for the audit log fields you would keep.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-01` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
