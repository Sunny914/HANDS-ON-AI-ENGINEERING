# Mentor notes — dbg-01

`tool_event` sets `parent_id` to `None` and does not copy `root["operation_id"]`.

The child must point at the root operation. Leaving the request id equal is not the same as a parent link.
