# SQLite Repository

**ID:** `ex-09`
**Stage:** 01-backend-api-engineering
**Difficulty:** L3
**Category:** Integration

## Objective

Move the job store behind a repository without teaching the route SQL.

## Prerequisites

ex-05 and ex-08.

## Problem

In-memory jobs vanish on restart. Persist them in SQLite and keep SQL out of the router.

## Requirements


- A repository creates the table if needed, inserts, fetches by id, and lists a page.
- The service depends on the repository. The route depends on the service.
- Tests use a temporary database file.
- Connections are closed on both success and failure.


## Constraints

Standard-library `sqlite3` only. No ORM required.

## Inputs and outputs

The service still speaks in job objects, not raw row tuples, at its public boundary.

## Edge cases

Missing id. Duplicate id if you use client-supplied ids. Empty list.

## Errors

A failed insert does not leave the API returning 200.

## Acceptance criteria

Create, restart the repository object against the same file, and fetch the same job. API test uses a temp file.

## Testing

Repository tests plus one API test.

## Common mistakes

SQL strings inside the route. A connection opened and never closed.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

Which function would change if the table moved to Postgres?

## Extension

Add an index you can justify, and say what query it serves.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-09` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
