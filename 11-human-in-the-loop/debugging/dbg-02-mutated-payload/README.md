# Mutated Payload

**ID:** `dbg-02`
**Difficulty:** L4
**Category:** Debugging

A human approved a send to `finance@example.com`. Before execute, another part of the program replaced the recipient with `other@example.com`. The tool sends to the new address. Fix `broken/execute.py` so only the approved snapshot runs.

Test that the tool receives the approved recipient. Write `FIX_NOTES.md`.

Hints: [HINTS.md](../../HINTS.md) section `dbg-02`. Reviewer notes: [MENTOR_NOTES.md](./MENTOR_NOTES.md).
