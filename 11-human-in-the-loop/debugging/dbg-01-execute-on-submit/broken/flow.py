"""Broken flow. Submit performs the side effect."""


def execute(action: dict, ledger: list) -> dict:
    ledger.append(action["args"])
    return {"status": "executed"}


def submit(action: dict, ledger: list) -> dict:
    pending = {"status": "pending", "action": action}
    execute(action, ledger)
    return pending
