"""Broken Stage 01 app. Behavior is intentionally wrong."""
from fastapi import Depends, FastAPI

app = FastAPI()
_seen: list[str] = []


def tracker() -> list[str]:
    return _seen


@app.post("/events")
async def add_event(name: str, seen: list[str] = Depends(tracker)) -> dict:
    seen.append(name)
    return {"count": len(seen), "names": list(seen)}
