# Reckless Retry

**ID:** `dbg-02`
**Stage:** 01-backend-api-engineering
**Difficulty:** L3
**Category:** Debugging

## Objective

A small client misbehaves when the upstream fails. Find the reliability bugs.

## Problem

`broken/client.py` is used to GET a resource. In local experiments a 404 is requested more than once, and a peer that never responds is not bounded. Diagnose and fix.

## Requirements

- Write the observed call count for a 404 before you edit.
- Preserve a way to retry temporary failures.
- Add tests that would fail for the old behavior.
- Record the cause in `FIX_NOTES.md`.

## Hints

[HINTS.md](../../HINTS.md) section `dbg-02` after a hypothesis. [MENTOR_NOTES.md](./MENTOR_NOTES.md) is for a reviewer.
