# Double Effect on Resume

**ID:** `dbg-02` **Difficulty:** L4 **Category:** Debugging

`simulate_resume` enters the node twice, which is what a resume does. The ledger ends with two copies of the action even though the human approved once. Fix `broken/node.py` so one approval records one row. Reject still records nothing. Write `FIX_NOTES.md`.

You do not need a live LangGraph process to see this bug. The simulator is the stand-in. Hints: [HINTS.md](../../HINTS.md) `dbg-02`. Reviewer: [MENTOR_NOTES.md](./MENTOR_NOTES.md).
