# Model Granted Itself Access

**ID:** `dbg-02` **Difficulty:** L3 **Category:** Debugging

A guest principal still runs `send` when the proposal contains `allow: true`. Fix `broken/gate.py`. Test guest denied and support allowed. The proposal's `allow` field must not matter. `FIX_NOTES.md` required.

Hints: [HINTS.md](../../HINTS.md) `dbg-02`. Reviewer: [MENTOR_NOTES.md](./MENTOR_NOTES.md).
