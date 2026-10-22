"""Broken coordinator. It will delegate forever."""


def next_worker(results: dict) -> str:
    return "research"


def run(task: str, max_hops: int) -> dict:
    results: dict = {}
    hops = 0
    while hops < 10000:
        role = next_worker(results)
        hops += 1
        results[role] = {"note": task, "hop": hops}
    return {"results": results, "stop_reason": "done"}
