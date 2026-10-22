# Shared Request State

**ID:** `dbg-03`
**Stage:** 01-backend-api-engineering
**Difficulty:** L3
**Category:** Debugging

## Objective

Two clients should not see each other's names in a per-request collection.

## Problem

POST `/events?name=ada` and then POST `/events?name=grace` with a fresh process. The second response reports a count that includes Ada. Find why and fix it.

## Requirements

- Reproduce with two requests.
- Fix isolation.
- Add a regression test.
- `FIX_NOTES.md` names the shared object.

## Hints

[HINTS.md](../../HINTS.md) section `dbg-03`. Reviewer detail is in [MENTOR_NOTES.md](./MENTOR_NOTES.md).
