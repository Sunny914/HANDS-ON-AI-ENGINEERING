# Mentor notes — dbg-02

The loop stops at a hard-coded ceiling of 10000 and never reads `max_attempts`.

Cap the attempts with `max_attempts`. After the last failure, stop. Raising the ceiling hides the missing guard.
