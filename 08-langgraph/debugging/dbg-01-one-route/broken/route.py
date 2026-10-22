"""Broken router. Both states take the same edge."""


def route(state: dict) -> str:
    if state.get("ok"):
        return "collect"
    return "collect"
