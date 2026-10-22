"""
ex-02 — Text Normalization Pipeline

Work top to bottom: normalize_whitespace → slugify → pipeline.
Run: python solution.py
"""


def normalize_whitespace(text):
    """
    Collapse runs of whitespace to a single space; strip leading/trailing space.

    TODO:
      - Handle str input (assume str for Stage 0).
      - "a    b" -> "a b"
      - "  hi  " -> "hi"

    Hints (not code):
      - .split() with no args splits on any whitespace and drops empties
      - then " ".join(...) puts single spaces back
    """
    


def slugify(text):
    """
    Lowercase; spaces to hyphens; remove chars that are not alphanumeric or hyphen.

    TODO:
      - Often easier if text is already normalized (spaces single).
      - Decide what to do with punctuation (README: removed).

    Build this after normalize_whitespace works.
    """
    raise NotImplementedError


def pipeline(text):
    """
    Apply normalize_whitespace then slugify.

    TODO:
      - Call your two functions in order and return the final str.
    """
    raise NotImplementedError


if __name__ == "__main__":
    # README example:
    # pipeline("  Hello, World!  ") -> "hello-world"

    # TODO: print(pipeline("  Hello, World!  "))
    # TODO: try edge cases: "", "   ", "UPPER"

    pass
