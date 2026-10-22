# Mentor notes — dbg-01

`ready` returns `live()` and never reads `store_up`.

Readiness must be false when the dependency flag is false. Liveness can remain true.
