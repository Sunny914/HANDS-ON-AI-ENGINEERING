# Unbounded Retry

**ID:** `dbg-02`
**Difficulty:** L3
**Category:** Debugging

`call` ignores `max_attempts` and keeps calling a failing adapter until a hard-coded ceiling, then raises. Fix `broken/retry.py` so a failing adapter is called at most `max_attempts` times and then raises or returns a named error. Write `FIX_NOTES.md`.

Do not debug this by waiting for the ceiling.

Hints: [HINTS.md](../../HINTS.md) `dbg-02`. Reviewer: [MENTOR_NOTES.md](./MENTOR_NOTES.md).
