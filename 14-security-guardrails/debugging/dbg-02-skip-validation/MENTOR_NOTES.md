# Mentor notes — dbg-02

`handle` calls `tool` before checking `record_id`.

Validate first. On failure, return an error and do not call the tool.
