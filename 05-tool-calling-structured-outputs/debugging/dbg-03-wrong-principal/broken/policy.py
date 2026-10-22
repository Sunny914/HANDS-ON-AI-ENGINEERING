"""Broken policy. The guest can grant themselves support."""


def allowed(principal: dict, tool: str, args: dict) -> bool:
    if tool != "refund":
        return True
    role = args.get("role", "guest")
    return role == "support"
