"""Broken precision. Irrelevant ids look like hits."""


def precision_at_k(retrieved: list[str], relevant: set[str], k: int) -> float:
    top = retrieved[:k]
    hits = sum(1 for item in top if item not in relevant)
    return hits / k
