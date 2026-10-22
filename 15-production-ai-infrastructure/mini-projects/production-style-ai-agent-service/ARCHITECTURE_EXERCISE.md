# Architecture Exercise

Write `DEPLOY.md`, `ADR.md`, and `YOUR_DESIGN.md` before the container build.

The design splits settings, HTTP, authorizer, adapter, store, and trace. The adapter is the only place a live SDK would go, and tests do not import one.

You choose module names. Do not copy a tree from Stage 01 line for line if your boundaries differ. You may reuse its HTTP library.
