"""Broken retry. It never stops."""


def call(adapter, max_attempts: int) -> str:
    attempts = 0
    while attempts < 10000:
        attempts += 1
        try:
            return adapter()
        except TimeoutError:
            continue
    raise RuntimeError("still failing")
