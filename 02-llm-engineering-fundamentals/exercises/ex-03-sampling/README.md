# Sampling Parameters

**ID:** `ex-03`
**Stage:** 02-llm-engineering-fundamentals
**Difficulty:** L2
**Category:** Focused implementation

## Objective

Validate generation settings before a provider sees them.

## Prerequisites

CONCEPTS.md sampling section.

## Problem

Callers pass temperature, top_p, and max output tokens. Reject impossible combinations.

## Requirements

Define ranges in one place. Temperature 0 through 2. top_p above 0 and at most 1. max output tokens at least 1. Include the model name as a non-empty string.

## Constraints

No HTTP.

## Inputs and outputs

A settings object.

## Edge cases

Temperature 0 is valid. top_p 0 is invalid.

## Errors

Validation error, not a provider call.

## Acceptance criteria

Boundary tests for each field.

## Testing

Unit tests.

## Common mistakes

Assuming temperature 0 means the provider is deterministic.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

Which of these settings affect cost directly?

## Extension

Add a seed field that is optional and passed through unchanged.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-03` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
