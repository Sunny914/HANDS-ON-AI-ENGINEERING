# Bearer Check and Test Boundaries

**ID:** `ex-10`
**Stage:** 01-backend-api-engineering
**Difficulty:** L4
**Category:** Integration

## Objective

Protect mutating routes and prove you know what each test is for.

## Prerequisites

ex-05 settings and ex-09.

## Problem

Anyone who can reach the port can create jobs. Require a bearer token from settings. Keep `/health` open if you added it.

## Requirements


- Missing or wrong token on create returns 401.
- The comparison does not log the token.
- One unit test calls the auth dependency or pure checker with headers and settings.
- One API test covers 401 and one authorized create.
- The unit test does not start a socket. The API test may use TestClient.


## Constraints

This is a shared secret, not OAuth and not user accounts. Say that in the module docstring.

## Inputs and outputs

`Authorization: Bearer <token>`.

## Edge cases

Empty bearer, wrong scheme such as `Basic`, extra whitespace.

## Errors

401 must not include the expected token in the body.

## Acceptance criteria

Both test types exist and fail if you remove the check.

## Testing

As stated in the requirements. No snapshot of the entire OpenAPI schema required.

## Common mistakes

Checking the token inside SQL. Treating a unit test of the route function as an API test when it skips dependencies.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

What would you add before this could be called authorization rather than authentication?

## Extension

Allow a read-only token that can list but not create. That is optional and is real authorization.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-10` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
