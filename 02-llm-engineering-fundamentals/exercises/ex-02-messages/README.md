# Message Transcripts

**ID:** `ex-02`
**Stage:** 02-llm-engineering-fundamentals
**Difficulty:** L2
**Category:** Focused implementation

## Objective

Model system, user, and assistant messages.

## Prerequisites

ex-01.

## Problem

A gateway cannot pass a single concatenated string and keep a straight face. Build a transcript type.

## Requirements

Validate roles, reject empty content, and render a debug string that shows roles. Do not call a model.

## Constraints

Pydantic v2 or dataclasses. Your choice, documented.

## Inputs and outputs

A list of messages in. A transcript object out.

## Edge cases

Two system messages: allow or reject, but document it. Whitespace-only content is empty.

## Errors

Unknown role is a validation error.

## Acceptance criteria

Tests for a valid three-message chat and for an unknown role.

## Testing

Unit tests.

## Common mistakes

Stuffing the system prompt into the user string so you only have one field.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

Why should user text not be concatenated in front of the system rules without a boundary?

## Extension

Add a token-count field that the caller fills in, still without tokenizing here.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-02` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
