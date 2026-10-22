# Notes on your first attempt (`solutions.py`)

This is feedback on what you tried — not a full solution. Use [solution.py](./solution.py) as your working file if you like.

## What you did well

- You experimented with many types: `int`, `float`, `str`, `bool`, `None`, list, tuple, dict.
- You started a `describe_value` function — that is the right idea.

## Gaps vs the README requirements

| Topic | Your attempt | Exercise wants |
|-------|----------------|----------------|
| Output | `print(...)` | **`return` a dict** with keys `type_name`, `is_numeric`, `repr` |
| Type display | `type(value)` in an f-string | `type_name` should be like `'int'`, not `<class 'int'>` |
| Second function | Missing | Implement **`safe_add(a, b)`** |
| Order of code | Calls on lines 1–10 **before** `def` | Define functions first; call them under `if __name__ == "__main__":` at the **bottom** |
| Filename | `solutions.py` | README suggests `solution.py` (either works if you stay consistent) |

## Why order matters

Python runs the file from top to bottom. Lines 1–10 call `describe_value` before it exists → **NameError**.

Pattern to use:

```text
1. imports (if any)
2. def describe_value ...
3. def safe_add ...
4. if __name__ == "__main__":
       # your experiments and print checks here
```

## Next steps (you do these)

1. Copy anything useful from `solutions.py` into `solution.py`, or rename your file.
2. Implement `describe_value` to **return** the dict (use `repr(x)` for the `repr` key).
3. Decide: is `bool` numeric? README H1 says **you choose** — then use the same rule in `safe_add`.
4. Implement `safe_add`.
5. Uncomment the check lines at the bottom of `solution.py` and run: `python solution.py`.

If you want a nudge without full code, ask: **"H2 for ex-01 describe_value dict"**.
