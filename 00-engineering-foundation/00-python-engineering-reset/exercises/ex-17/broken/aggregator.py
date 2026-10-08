"""Deliberately buggy — ex-17. Do not use as reference implementation."""

_DEFAULT_BUCKET = []


def group_by_category(items):
    """Group dict items with 'category' key into lists."""
    groups = {}
    for item in items:
        cat = item.get("category", "uncategorized")
        if cat not in groups:
            groups[cat] = _DEFAULT_BUCKET
        groups[cat].append(item["value"])
    return groups


def total_per_category(items):
    grouped = group_by_category(items)
    return {cat: sum(vals) for cat, vals in grouped.items()}


if __name__ == "__main__":
    sample = [
        {"category": "a", "value": 1},
        {"category": "b", "value": 2},
        {"category": "a", "value": 3},
    ]
    print(total_per_category(sample))
