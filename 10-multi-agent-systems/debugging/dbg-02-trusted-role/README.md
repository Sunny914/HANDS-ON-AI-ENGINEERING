# Trusted Role Claim

**ID:** `dbg-02`
**Difficulty:** L3
**Category:** Debugging

A worker payload can set `role` to `coordinator` and then pass the allow check for any tool. The role that should matter is the one the coordinator assigned. Fix `broken/allow.py`.

Test that a payload role of coordinator still cannot call `shell` when the assigned role is `research`. Test that `research` can call `search`. Write `FIX_NOTES.md`.

Hints: [HINTS.md](../../HINTS.md) section `dbg-02`. Reviewer notes: [MENTOR_NOTES.md](./MENTOR_NOTES.md).
