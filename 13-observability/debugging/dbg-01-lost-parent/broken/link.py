"""Broken linker. The tool event has no parent."""


def tool_event(root: dict, name: str) -> dict:
    return {
        "name": name,
        "request_id": root["request_id"],
        "operation_id": "tool-1",
        "parent_id": None,
    }
