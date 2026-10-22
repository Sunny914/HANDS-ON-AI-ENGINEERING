"""Broken allow-list. The message picks its own role."""

TOOLS = {
    "research": {"search", "read"},
    "verification": {"read"},
    "coordinator": {"shell"},
}


def allowed(assigned_role: str, tool_name: str, message: dict) -> bool:
    role = message["role"]
    return tool_name in TOOLS.get(role, set())
