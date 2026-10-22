"""Broken gateway. The tool runs before validation."""


def handle(args: dict, tool, ledger: list) -> dict:
    tool(args, ledger)
    if "record_id" not in args:
        return {"status": "error"}
    return {"status": "ok"}
