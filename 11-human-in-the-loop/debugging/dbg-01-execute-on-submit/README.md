# Execute on Submit

**ID:** `dbg-01`
**Difficulty:** L3
**Category:** Debugging

Submitting a `send_message` proposal increments the ledger immediately. No human has approved it. Fix `broken/flow.py` so submit only stores a pending action.

Add a test that submit leaves the counter at 0 and that execute after a separate approval increments it once. Write `FIX_NOTES.md`.

Hints: [HINTS.md](../../HINTS.md) section `dbg-01`. Reviewer notes: [MENTOR_NOTES.md](./MENTOR_NOTES.md).
