# Tool Argument Schema

**ID:** `ex-02`
**Stage:** 05-tool-calling-structured-outputs
**Difficulty:** L2
**Category:** Focused implementation

## Objective

One Pydantic model is both the advertisement and the check.

## Prerequisites

ex-01. Pydantic v2.

## Problem

Define `GetOrderArgs` and `RefundArgs`. Export JSON Schema. Validate raw dicts.

## Requirements

Order id is a non-empty string. Refund amount is a positive int in minor units. Reason is a non-empty string.

## Constraints

No tool side effects in this exercise.

## Inputs and outputs

Dict in. Model or validation error out. Schema is a dict.

## Edge cases

Amount 0. Amount as a string. Extra key.

## Errors

Validation errors are not executed refunds. There is nothing to execute yet.

## Acceptance criteria

Tests for valid, zero amount, and wrong type. Schema contains the field names.

## Testing

Unit tests.

## Common mistakes

A second hand-written schema that drifts from the model.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

Why is a positive amount still not permission to refund?

## Extension

Add a max amount field with a default you can explain.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-02` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
