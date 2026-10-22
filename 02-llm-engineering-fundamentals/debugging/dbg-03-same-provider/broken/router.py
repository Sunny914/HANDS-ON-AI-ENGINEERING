"""Broken router. Fallback selection is intentionally wrong."""


def attempts(providers: list[str], primary_failures: int) -> list[str]:
    chosen: list[str] = []
    failures_left = primary_failures
    index = 0
    while failures_left >= 0 and len(chosen) < 4:
        index = 0
        chosen.append(providers[index])
        if index == 0 and failures_left > 0:
            failures_left -= 1
            continue
        index += 1
        if index >= len(providers):
            break
    return chosen
