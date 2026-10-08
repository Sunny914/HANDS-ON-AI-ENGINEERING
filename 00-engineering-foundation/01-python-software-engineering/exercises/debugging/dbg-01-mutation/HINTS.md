# dbg-01 Hints

**H1:** Two service instances may share hidden global state.

**H2:** `clear` does not create a new list; `add_item` mutates a shared structure.

**H3:** `clear` should assign a fresh empty list; avoid module-level mutable cache for per-instance data.
