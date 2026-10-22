# False Success

**ID:** `dbg-01`
**Stage:** 01-backend-api-engineering
**Difficulty:** L2
**Category:** Debugging

## Objective

Find why failed requests look successful.

## Prerequisites

ex-04. [DEBUGGING_GUIDE.md](../../DEBUGGING_GUIDE.md).

## Problem

Run the app in `broken/` and POST an item with `qty` less than 1. Also POST a body that is not valid JSON. Something about the responses is wrong. Diagnose and fix it.

## Requirements

- Reproduce both requests.
- Write the status code you observed before editing.
- Fix the failure behavior.
- Add `FIX_NOTES.md` with the cause and the test you added.

## Constraints

Do not rewrite the app into the mini-project. Change the broken behavior.

## Acceptance criteria

- Invalid `qty` is not reported as success.
- The response status matches the failure.
- A regression test fails if the bug returns.

## Hints

Use [HINTS.md](../../HINTS.md) section `dbg-01` after you have a hypothesis. Do not open [MENTOR_NOTES.md](./MENTOR_NOTES.md) first.
