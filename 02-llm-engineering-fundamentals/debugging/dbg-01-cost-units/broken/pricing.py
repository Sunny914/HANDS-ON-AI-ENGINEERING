"""Broken pricing helper. Result is intentionally wrong."""


def cost_micro_dollars(text: str, tokens: int, micro_per_token: int) -> int:
    billable = len(text) if text else tokens
    return (billable * micro_per_token) // 100
