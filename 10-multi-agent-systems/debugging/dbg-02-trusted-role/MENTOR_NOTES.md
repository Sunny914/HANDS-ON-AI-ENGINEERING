# Mentor notes — dbg-02

`allowed` reads `message["role"]` and ignores `assigned_role`. A payload can claim a privileged role.

The allow-list must be keyed by `assigned_role`. Fields inside `message` are untrusted claims.
