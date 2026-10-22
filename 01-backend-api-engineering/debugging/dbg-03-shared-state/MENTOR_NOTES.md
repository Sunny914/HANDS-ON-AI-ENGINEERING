# Mentor notes — dbg-03

- `_seen` is a module-level list.
- The dependency returns that same list for every request.
- Appending therefore leaks data across callers. The fix is per-request state or real persistence, not a longer list.
