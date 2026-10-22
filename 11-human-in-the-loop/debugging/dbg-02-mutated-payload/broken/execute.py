"""Broken execute. The live arguments replace the approved snapshot."""


def execute_approved(pending: dict, current_args: dict, tool) -> dict:
    if pending["status"] != "approved":
        return {"status": "refused"}
    tool(current_args)
    return {"status": "executed", "args": current_args}
