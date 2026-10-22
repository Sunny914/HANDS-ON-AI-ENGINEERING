# Stage 01 Assumptions

Verified on 2026-10-21 against FastAPI's Pydantic migration guide:

- Current FastAPI releases require **Pydantic v2**. Pydantic v1 support inside FastAPI was removed by the 0.128 line.
- Use `fastapi`, `pydantic`, `httpx`, `pytest`, and `pytest-asyncio` if you write async tests.
- Uvicorn is the local server. Versions move. Install current releases and read their docs if an import fails.
- SQLite is the intended Stage 01 database. Do not block this stage on PostgreSQL.
- No paid API is required. Point the upstream client at a local fake or at a public endpoint you are allowed to call.

See `requirements.txt` for the install set. Pins are floors, not a lockfile.
