"""Broken loop. The step budget is not honored."""


def run(actions: list[str], max_steps: int) -> dict:
    trace = []
    for _ in range(max_steps * 4):
        if not actions:
            break
        trace.append(actions[len(trace) % len(actions)])
    return {"trace": trace, "stop_reason": "done"}
