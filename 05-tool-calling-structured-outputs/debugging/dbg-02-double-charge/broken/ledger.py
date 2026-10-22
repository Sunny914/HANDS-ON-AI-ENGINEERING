"""Broken refund ledger. The same key charges twice."""


def refund(key: str, amount: int, rows: list, seen: dict) -> dict:
    if key in seen:
        return seen[key]
    receipt = {"key": key, "amount": amount}
    rows.append(receipt)
    return receipt
