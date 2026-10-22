# Context Budget

**ID:** `ex-01`
**Stage:** 02-llm-engineering-fundamentals
**Difficulty:** L1
**Category:** Focused implementation

## Objective

Decide whether a call fits in a context window.

## Prerequisites

CONCEPTS.md section before ex-01.

## Problem

You are given token counts from a counter you trust. Decide if a request fits, including room for the completion.

## Requirements

Implement `fits` and `overflow`. Document that this function does not tokenize text. Add a clearly named heuristic helper only if you want the extension.

## Constraints

No provider SDK.

## Inputs and outputs

Integers in. Boolean and overflow count out.

## Edge cases

Exact fit is allowed. Negative counts raise.

## Errors

Do not truncate silently inside this function.

## Acceptance criteria

Tests for fit, exact fit, overflow, and negative input.

## Testing

Unit tests.

## Common mistakes

Dividing character length by 4 and calling it tokenization without a label.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

Who should refuse the call: this function's caller, or the provider after a 400?

## Extension

A separate `estimate_tokens(text)` that documents the heuristic and is not used as the source of truth in `fits` tests.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-01` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
