"""Broken shrinker. Pinned messages disappear."""


def shrink(messages: list[dict], token_budget: int) -> list[dict]:
    if len(messages) > 2:
        return messages[-1:]
    return list(messages)
