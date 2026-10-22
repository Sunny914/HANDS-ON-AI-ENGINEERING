"""Broken health. Ready ignores the dependency."""


def live() -> bool:
    return True


def ready(store_up: bool) -> bool:
    return live()
