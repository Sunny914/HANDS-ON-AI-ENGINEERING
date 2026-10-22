# Retry versus Idempotency

**ID:** `arch-02`
**Stage:** 01-backend-api-engineering
**Difficulty:** L4
**Category:** Architecture

## Objective

Place two reliability mechanisms in different modules.

## Prerequisites

ex-07. arch-01.

## Problem

A teammate wants the HTTP client to 'just retry POSTs three times'. Explain why that is incomplete and where each mechanism lives.

## Requirements


Write `RELIABILITY.md`:
- Sequence for a new idempotency key
- Sequence for a repeated key
- Who calls `should_retry`
- What is stored so the second request can return the first result
- What is deliberately not retried


## Constraints

No code. You may sketch function names.

## Inputs and outputs

Two sequences, as numbered steps.

## Edge cases

The first request timed out after the upstream succeeded. Say what you cannot know, not a fantasy guarantee.

## Errors

Include the case where the stored result itself failed.

## Acceptance criteria

The client module does not own the idempotency table in your design.

## Testing

Name one test that would fail if retry moved into the repository.

## Common mistakes

Using the database primary key as the idempotency key without saying who generates it.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

What guarantee can you not make with only SQLite and one process?

## Extension

Describe the bug if two processes accept the same key at the same time. You do not have to solve distributed locking.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `arch-02` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
