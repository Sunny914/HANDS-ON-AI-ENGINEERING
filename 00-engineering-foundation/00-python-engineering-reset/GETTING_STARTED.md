# Getting Started — Module 00

You are new to this repo. That is normal. This module is designed for **you to type code**, not to read and memorize.

## What one exercise folder looks like

```text
ex-01/
  README.md      ← read this first (the assignment)
  solution.py    ← optional starter with comments (you fill in the logic)
  your_file.py   ← you can use any name; README often suggests solution.py
```

## How to run your code

From the exercise folder in a terminal:

```bash
cd path/to/ex-01
python solution.py
```

In Cursor: open `solution.py`, use **Run Python File** or the integrated terminal.

If you see `NameError: name 'describe_value' is not defined`, you usually called a function **above** its `def` line. In Python, **define functions first**, then call them at the bottom inside:

```python
if __name__ == "__main__":
    # tests / print checks here
```

## How this training repo differs from tutorials

| Tutorials often | This repo |
|-----------------|-----------|
| Show complete code | You write the code |
| One right answer | Many valid structures (later exercises) |
| Video pace | You pause and experiment |

When stuck, use hints in order: README **H1** → [HINTS.md](../HINTS.md) **H2/H3** → ask for **H4** only if you explicitly want code help.

## A simple workflow for every exercise

1. Read **Objective** and **Requirements** in README.
2. Open `solution.py` if present; read the comments (they are a map, not answers).
3. Write the smallest piece (one function).
4. Run the file. Fix errors from the **bottom** of the traceback.
5. Add `if __name__ == "__main__":` checks from **Expected behavior**.
6. When it works, commit: `feat: complete ex-01`.

## Common beginner errors (not shame—everyone hits these)

- **Calling before defining** — move calls under `if __name__ == "__main__":` at the end.
- **Printing instead of returning** — exercises often want `return` so tests or other code can use the result.
- **`type(x)` vs name** — `type(3)` is `<class 'int'>`; requirement may want the string `'int'` → look up `__name__`.
- **Wrong filename** — ex-01 README says `solution.py`; `solutions.py` is fine if you prefer, but pick one file to avoid confusion.

## Your first exercise

Start at [exercises/ex-01](./exercises/ex-01/README.md) and use the commented [solution.py](./exercises/ex-01/solution.py) starter.
