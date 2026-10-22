"""Broken node. The first pause stops the rest of that entry. Resume enters again."""


class Paused(Exception):
    """The first pause. The simulator treats this as the graph stopping."""


def approval_node(state: dict, ledger: list, pause) -> dict:
    ledger.append(state["action_id"])
    decision = pause(state["action_id"])
    return {"decision": decision}


def simulate_resume(action_id: str, decision: str) -> list:
    ledger: list = []
    entered = {"count": 0}

    def pause(_payload: str) -> str:
        entered["count"] += 1
        if entered["count"] == 1:
            raise Paused()
        return decision

    try:
        approval_node({"action_id": action_id}, ledger, pause)
    except Paused:
        pass
    approval_node({"action_id": action_id}, ledger, pause)
    return ledger
