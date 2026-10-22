# Validate Structured Output

**ID:** `ex-06`
**Stage:** 02-llm-engineering-fundamentals
**Difficulty:** L3
**Category:** Focused implementation

## Objective

Turn untrusted model text into a typed object.

## Prerequisites

Pydantic v2 from Stage 01.

## Problem

The model was asked for a JSON object with `title` and `confidence`. Sometimes it wraps that object in a markdown fence.

## Requirements

Extract JSON, validate it, and return the model. Confidence is a float from 0 to 1. Title is non-empty.

## Constraints

Do not eval the text. `json.loads` only.

## Inputs and outputs

String in. Typed object or a validation error.

## Edge cases

Fence with a language tag. Leading prose before the fence. Two JSON objects. Confidence 1.5.

## Errors

Invalid JSON and schema failures are different error types or different codes you can test.

## Acceptance criteria

Tests for raw JSON, fenced JSON, prose-plus-fence, and an out-of-range confidence.

## Testing

Unit tests. No model.

## Common mistakes

Taking the first `{` and the first `}` when the string is nested.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

Why is this still not a guarantee the title is true?

## Extension

If both a fence and a raw object exist, define which wins.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-06` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
