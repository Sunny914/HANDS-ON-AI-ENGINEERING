# Gateway Boundaries

**ID:** `arch-01`
**Stage:** 02-llm-engineering-fundamentals
**Difficulty:** L4
**Category:** Architecture

## Objective

Design the multi-provider gateway before coding it.

## Prerequisites

ex-08 and ex-09.

## Problem

Write `YOUR_DESIGN.md` for the project. Include modules, the normalized types, error mapping, ledger contents, configuration, and tests that do not need a key.

## Requirements

Answer the twelve checkpoint questions in LEARNING_PROTOCOL.md that apply. Skip a question only if you say why it does not apply.

## Constraints

No gateway implementation in this exercise.

## Inputs and outputs

A design note.

## Edge cases

Say what a live key test is allowed to prove that fakes cannot.

## Errors

Name two error types that leave an adapter.

## Acceptance criteria

Vendor JSON parsing is not in the router in your design.

## Testing

List fake scripts you will need.

## Common mistakes

One class named `OpenAIGateway` that the whole app imports.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

Which provider behavior are you refusing to abstract on day one?

## Extension

Describe a streaming method without implementing it.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `arch-01` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
