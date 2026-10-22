# In-Memory Job API

**ID:** `ex-03`
**Stage:** 01-backend-api-engineering
**Difficulty:** L2
**Category:** Focused implementation

## Objective

Serve one resource with FastAPI without a database yet.

## Prerequisites

ex-02 sketch. FastAPI install from requirements.txt.

## Problem

Implement create and fetch for sync jobs stored in memory, so you can learn the HTTP adapter before persistence.

## Requirements


- `POST` creates a job with a title and a source URL.
- `GET` by id returns the job.
- Missing id returns 404.
- Create returns 201 and a generated id.
- The store is not a global list mutated from the route body. Put it behind a small object or function.


## Constraints

No SQLite yet. No upstream HTTP call yet. Pydantic models for the bodies.

## Inputs and outputs

JSON in, JSON out, plus status codes.

## Edge cases

Empty title is invalid. Very long title: reject or document a limit.

## Errors

404 body is JSON with a stable `detail` field.

## Acceptance criteria

TestClient or equivalent covers create, fetch, missing id, and empty title.

## Testing

API tests. Restarting the process may drop data. Document that.

## Common mistakes

Business rules only as `print`. Returning 200 for a missing job.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

What breaks if two tests share one process-wide list?

## Extension

Add delete. Decide whether delete of a missing id is 404 or 204, and test it.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-03` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
