"""Broken Stage 01 exercise. Behavior is intentionally wrong."""
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str = Field(min_length=1)
    qty: int


@app.exception_handler(Exception)
async def handle_everything(request: Request, exc: Exception) -> JSONResponse:
    return JSONResponse(status_code=200, content={"status": "accepted", "detail": str(exc)})


@app.post("/items")
async def create_item(item: Item) -> dict:
    if item.qty < 1:
        raise HTTPException(status_code=422, detail="qty must be positive")
    return {"name": item.name, "qty": item.qty}
