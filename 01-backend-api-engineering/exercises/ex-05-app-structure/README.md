# Routers, Settings, and Logging

**ID:** `ex-05`
**Stage:** 01-backend-api-engineering
**Difficulty:** L2
**Category:** Integration

## Objective

Split the app so routes, settings, and logs have homes.

## Prerequisites

ex-04. Stage 00 logging and environment variables.

## Problem

The single-file API is about to gain a client and a database. Split it first.

## Requirements


- Routes live on an `APIRouter` included by the app entry.
- Settings come from environment variables: at least log level and the shared auth token you will use in ex-10. A default is allowed for local development and must be documented.
- Logging is configured once. The route logs the job id at info when a job is created. It does not log the full upstream body.
- A dependency provides settings to the route.


## Constraints

At least three modules. No circular imports.

## Inputs and outputs

Document the environment variable names in the exercise README you add, or in a comment at the top of the settings module.

## Edge cases

Missing log level falls back to INFO.

## Errors

Import errors from circular imports fail the exercise even if the happy path works in one process.

## Acceptance criteria

App still passes ex-04 tests after the split. A test or manual run shows a log line without a secret.

## Testing

Existing API tests still pass. Add one test that overrides the settings dependency.

## Common mistakes

`os.environ` read inside the business function. `basicConfig` in every module.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

What would you have to edit to add a second resource?

## Extension

Add a `/health` route that does not require auth later.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-05` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
