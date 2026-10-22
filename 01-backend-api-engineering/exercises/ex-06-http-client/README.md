# Async Client with a Timeout

**ID:** `ex-06`
**Stage:** 01-backend-api-engineering
**Difficulty:** L3
**Category:** Focused implementation

## Objective

Call another service without hanging the event loop.

## Prerequisites

Stage 00 async preview. ex-05.

## Problem

Enrichment means `GET` on a URL the client supplied. That call must time out.

## Requirements


- An async client function or class performs GET and returns parsed JSON.
- A timeout is required, not optional in the default path.
- Timeouts become a named error your service can catch.
- Non-2xx responses become a named error that still exposes the status code.
- Tests use a fake transport or a fake function. No paid service.


## Constraints

Use `httpx.AsyncClient`. Do not use a blocking HTTP library inside `async def`.

## Inputs and outputs

Input is a URL. Output is a dict or a typed object you define.

## Edge cases

Timeout, 404, and a 200 body that is not JSON.

## Errors

Close the client. Do not leak a connection on the error path.

## Acceptance criteria

Tests cover timeout, 404, and one success using httpx's mock transport or an injected fake.

## Testing

No real network in the default test command.

## Common mistakes

`requests.get` inside an async route. Timeout of `None`.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

Where should the timeout value live: code constant, settings, or both?

## Extension

Add a test that a slow fake exceeds a short timeout.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-06` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
