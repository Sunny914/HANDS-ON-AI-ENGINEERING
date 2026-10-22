# Mentor notes — dbg-02

`execute_approved` passes `current_args` into the tool and never reads `pending["args"]`.

The approved snapshot is the only payload that may run. If the current args differ, refuse. Do not overwrite `pending["args"]` with the new values.
