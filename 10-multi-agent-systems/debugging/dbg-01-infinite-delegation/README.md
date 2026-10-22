# Infinite Delegation

**ID:** `dbg-01`
**Difficulty:** L3
**Category:** Debugging

`run` ignores `max_hops`. It keeps delegating to research, then returns `done` after a hard-coded ceiling. Fix `broken/delegate.py` so a hop limit ends the run with the results collected so far. Do not debug it by waiting on the ceiling.

Add a test where the next role would always be research. Assert the number of delegations and a stop reason. Write `FIX_NOTES.md` with the symptom, the cause, and the check you added.

Hints: [HINTS.md](../../HINTS.md) section `dbg-01`. Reviewer notes, not the first read: [MENTOR_NOTES.md](./MENTOR_NOTES.md).
