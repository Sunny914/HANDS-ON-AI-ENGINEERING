"""Broken summary. A later success deletes the timeout."""


def summarize(attempts: list[dict]) -> dict:
    last = attempts[-1]
    return {"status": last["status"], "attempts": [last], "retry_count": 0}
