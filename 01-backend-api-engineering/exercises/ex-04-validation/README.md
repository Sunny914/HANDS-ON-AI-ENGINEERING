# Validation and Error Bodies

**ID:** `ex-04`
**Stage:** 01-backend-api-engineering
**Difficulty:** L2
**Category:** Focused implementation

## Objective

Make malformed input a 422 and illegal business input a deliberate error.

## Prerequisites

ex-03. Pydantic v2 `field_validator` or an equivalent check.

## Problem

Clients send bad types, missing fields, and a source URL that is not http or https. The API must reject them without a 500.

## Requirements


- Malformed JSON or wrong types produce a validation error response, not an unhandled exception.
- A non-http URL is rejected with a documented status.
- The success model never includes the raw exception class name.


## Constraints

Stay on Pydantic v2. Do not install a second validation library.

## Inputs and outputs

Show one invalid payload and the status code in the test names.

## Edge cases

`null` title, missing source URL, `ftp://` URL.

## Errors

Do not catch all exceptions and return 200.

## Acceptance criteria

Three invalid cases are tested. One valid case still returns 201.

## Testing

API tests for the three cases. Optional unit test for the URL rule.

## Common mistakes

Validating only in the OpenAPI example. Using Pydantic v1 `validator`.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

Which check belongs on the model, and which belongs in the service?

## Extension

Add a response model so internal fields cannot leak.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-04` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
