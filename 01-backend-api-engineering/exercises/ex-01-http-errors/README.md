# HTTP Failure Classes

**ID:** `ex-01`
**Stage:** 01-backend-api-engineering
**Difficulty:** L1
**Category:** Focused implementation

## Objective

Classify HTTP failures before you hide them in a framework.

## Prerequisites

Stage 00 functions and tests. Read the status-code rows in CONCEPTS.md.

## Problem

A later retry policy needs to know whether a response is a caller mistake, a temporary outage, or an unexpected crash. Build that classification now, with no web server.

## Requirements


- Implement a pure function that takes an integer status code and an HTTP method.
- Return a small set of labels you define, covering at least: success, caller error, temporary failure, unexpected.
- Document which codes land in which label. Include 200, 201, 204, 400, 401, 404, 409, 422, 429, 500, and 503.


## Constraints

No FastAPI. No network. Standard library only.

## Inputs and outputs

Input is a status code and a method string. Output is your label, not a printed line.

## Edge cases

Unknown codes such as 418 and 599 need a documented default. Method case should not change the label.

## Errors

Do not raise for ordinary 4xx codes. Raise only if the status is not an integer in 100–599, if you choose to validate that.

## Acceptance criteria


- A table of at least those eleven codes is covered by tests.
- 429 and 503 are temporary. 404 and 422 are caller errors. 500 is unexpected.
- You can say why 409 is not the same thing as 503.


## Testing

pytest tests for the table. No mocks.

## Common mistakes

Treating every 4xx as retryable. Printing instead of returning.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

Which label would you retry, and which would you show to the client unchanged?

## Extension

Add a second function that maps a label to a default client-facing message without leaking internal exception text.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-01` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
