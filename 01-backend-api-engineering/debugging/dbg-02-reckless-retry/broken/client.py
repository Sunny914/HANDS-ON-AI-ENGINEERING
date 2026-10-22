"""Broken Stage 01 client. Behavior is intentionally wrong."""
import httpx


async def fetch_json(url: str) -> dict:
    last_error = None
    for _ in range(4):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url)
                response.raise_for_status()
                return response.json()
        except Exception as exc:
            last_error = exc
    if last_error is None:
        raise RuntimeError("no attempt")
    raise last_error
