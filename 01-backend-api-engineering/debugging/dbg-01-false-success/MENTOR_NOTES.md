# Mentor notes — dbg-01

Not for the first read. The learner instructions do not list these defects.

- A catch-all exception handler returns HTTP 200 and `{"status": "accepted"}` for `HTTPException`.
- Validation failures are therefore indistinguishable from success.
- The handler also hides unexpected bugs, which the learner should narrow rather than delete all handling.
