# REST Sketch for Sync Jobs

**ID:** `ex-02`
**Stage:** 01-backend-api-engineering
**Difficulty:** L1
**Category:** Conceptual reasoning

## Objective

Design a resource API on paper before writing routes.

## Prerequisites

ex-01.

## Problem

Clients will ask this service to sync a catalog item from an upstream system and later read the result. Describe the HTTP API. Do not implement it.

## Requirements


Write `API_SKETCH.md` in this folder with:
- Resources and paths
- Methods
- Request and response fields
- Status codes for success, validation failure, missing job, and conflict
- How a client supplies an idempotency key


## Constraints

No application code. One or two resources, not a platform.

## Inputs and outputs

The sketch is the deliverable.

## Edge cases

Say what happens if the same idempotency key is reused with a different body.

## Errors

Include at least one 4xx and one 5xx the client might see later.

## Acceptance criteria

A reviewer can implement the API from the sketch without inventing the resource names.

## Testing

Not applicable. Read the sketch aloud and check it against the edge case.

## Common mistakes

One POST that does three different jobs. Verbs in the path such as `/createJob`.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

What did you refuse to put in this API?

## Extension

Add a list endpoint with the query parameters you will need in ex-08.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-02` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
