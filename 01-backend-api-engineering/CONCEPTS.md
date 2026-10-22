# Stage 01 Concepts

Understand these before the matching exercise. Use the official docs for the library details. This page is the checklist, not a second textbook.

## Before any FastAPI code

| Concept | You can explain |
|---------|-----------------|
| Request line, headers, body | What the application actually receives |
| Status codes | 200, 201, 204, 400, 401, 404, 409, 422, 429, 500, 503 |
| Resource versus RPC | Nouns and verbs in a URL |
| Idempotency | Why a retried POST can double-charge or double-create |
| Timeout | A hung peer is not a slow success |

## Before the service grows

| Concept | You can explain |
|---------|-----------------|
| Pydantic v2 model | Validation at the boundary, not inside the route by accident |
| `APIRouter` and `Depends` | Where a request is parsed versus where a rule lives |
| Settings object | One load, injected downward. No scattered `os.environ` |
| Repository | SQL or files stay out of the route |
| Async client | `await` on I/O. Do not call a blocking client inside an `async def` route |
| Retry classes | Network and 429/503 differ from 400/401/404 |
| Pagination | Page size is a contract, not an accident of `list` |

## FastAPI shapes to look up

Checked against current FastAPI docs at generation time: recent FastAPI requires **Pydantic v2**. Use `BaseModel`, `Field`, and `field_validator`. Do not use Pydantic v1 `validator` or `orm_mode`.

Route dependencies use `Depends`. Raise `HTTPException` for expected HTTP failures. Let unexpected exceptions surface in tests until you add a deliberate handler.

## Persistence choice

Stage 01 uses the standard-library `sqlite3` module so you can learn a repository boundary without a new database server. SQLAlchemy and PostgreSQL are not required here. Stage 04 introduces PostgreSQL for vector search.
