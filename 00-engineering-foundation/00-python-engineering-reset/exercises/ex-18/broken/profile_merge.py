"""Deliberately buggy — ex-18."""

def merge_profiles(primary, secondary):
    """Merge profile dicts; secondary overrides primary."""
    result = {}
    for key in ("name", "age", "score"):
        result[key] = secondary.get(key) or primary.get(key)
    return result


if __name__ == "__main__":
    p = {"name": "Ada", "age": 0, "score": 10}
    s = {"age": 25}
    print(merge_profiles(p, s))
