"""
ex-01 — Expression Evaluator and Types

HOW TO USE THIS FILE:
1. Read README.md in this folder.
2. Fill in each function body where you see TODO.
3. Only run manual checks at the bottom inside `if __name__ == "__main__":`.
4. Do not call describe_value() above the def lines — Python has not defined them yet.
"""


def describe_value(x):
    """
    Return a dict describing x (do not print — return).

    Required keys:
      - type_name (str): short type name, e.g. 'int', 'str', 'bool', 'NoneType'
      - is_numeric (bool): README says int/float count; YOU decide if bool counts too
      - repr (str): use repr(x) — e.g. strings include quotes in repr

    TODO:
      1. Get the type name string (hint: type(x).__name__).
      2. Decide is_numeric with isinstance(...) or type checks.
      3. Build and return the dict with exactly those three keys.
    """
    # --- your code below ---
    return {"data_type": type(x).__name__, "is_numeric": isinstance(x, (int, float)), "repr": repr(x)}

def safe_add(a, b):
    """
    Return a + b only when both operands are numeric (per your rule in describe_value).

    Otherwise return None (not print, not raise).

    TODO:
      1. Check types of a and b.
      2. If both allowed numeric types, return their sum.
      3. Else return None.

    Examples from README:
      safe_add(1, 2) -> 3
      safe_add('1', 2) -> None
    """
    # --- your code below ---
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
      return a+b
    #else None

if __name__ == "__main__":
    # Manual checks — add prints or asserts after your functions work.
    # Expected shape for describe_value(3):
    #   {'type_name': 'int', 'is_numeric': True, 'repr': '3'}

    # TODO: print(describe_value(3))
    # TODO: print(describe_value(True))   # think: is bool numeric for YOU?
    # TODO: print(describe_value(None))
    # TODO: print(safe_add(1, 2))
    # TODO: print(safe_add("1", 2))

    print(describe_value(55555555))
    print(safe_add(244.44,66.66))
