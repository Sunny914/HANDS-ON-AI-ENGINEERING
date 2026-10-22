# Mentor notes — dbg-01

`submit` calls `execute` before any approval state exists. The pending dict is built and then ignored.

Submit should store status `pending` and return. Execution belongs on a later call after an approval decision.
