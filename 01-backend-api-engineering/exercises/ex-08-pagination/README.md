# Pagination Contract

**ID:** `ex-08`
**Stage:** 01-backend-api-engineering
**Difficulty:** L3
**Category:** Focused implementation

## Objective

Return a stable page of jobs.

## Prerequisites

ex-03 store, or the repository from ex-09 if you already built it.

## Problem

`GET /sync-jobs` cannot return every row forever.

## Requirements


- Query parameters `page` and `page_size`.
- Response includes the items, page, page_size, and total count.
- `page_size` is at least 1 and at most 100.
- Page numbers start at 1.
- A page past the end returns an empty list and the true total, with status 200.


## Constraints

Do not invent cursor pagination in this exercise.

## Inputs and outputs

Document an example response with two items.

## Edge cases

page 0, page_size 0, page_size 101, empty store.

## Errors

Invalid page parameters are 422.

## Acceptance criteria

Tests for the first page, a short last page, an empty page, and a rejected page size.

## Testing

Unit-test the slice math as well as one API test.

## Common mistakes

Off-by-one so page 1 skips the first row. Returning 404 for an empty page.

## Completion checklist

- [ ] Behavior matches the acceptance criteria
- [ ] Tests you were asked to write are present and passing
- [ ] You can explain the design without reading the hint file

## Reflection

What would a client do if you later switched to cursor pages?

## Extension

Add a `status` filter that composes with pagination.

## Hints

Attempt the exercise before opening hints. In [../../HINTS.md](../../HINTS.md), read only the `ex-08` section, and stop at the first level that unblocks you.

- H1 is a concept
- H2 is structure
- H3 is a next step, not a finished implementation
- H4 is a review of your attempt. Bring the code to a reviewer. This file does not contain that review.
