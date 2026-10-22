"""Broken authorizer. The document picks the role."""

ALLOW = {"researcher": {"read"}, "admin": {"read", "deploy"}}


def allowed(principal: str, tool_name: str, document: str) -> bool:
    if "role=admin" in document:
        return True
    return tool_name in ALLOW.get(principal, set())
