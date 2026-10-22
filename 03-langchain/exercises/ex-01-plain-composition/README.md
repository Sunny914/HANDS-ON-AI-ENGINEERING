# Compose Without LangChain

**ID:** `ex-01`
**Stage:** 03-langchain
**Difficulty:** L1
**Category:** Conceptual reasoning

## Objective

Build a three-step pipeline with plain functions.

## Prerequisites

Stage 02 messages. CONCEPTS.md.

## Problem

Given a question and an excerpt, render messages, complete them with an injected fake, and strip the answer. No LangChain imports.

## Requirements

The fake is passed in. The pipeline returns a string. A test proves the fake received a system message and a user message.

## Constraints

Do not import langchain.

## Inputs and outputs

Dict with `question` and `excerpt`. String out.

## Edge cases

Empty excerpt returns a named error and does not call the fake.

## Errors

The fake's exception propagates or is wrapped. Document which.

## Acceptance criteria

One test uses a fake that records messages. One test covers the empty excerpt.

## Testing

pytest. No framework.

## Common mistakes

Jumping to LangChain so you never see the data.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

What did the middle function need that a string prompt hides?

## Extension

Return the messages alongside the answer for debugging.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-01` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
