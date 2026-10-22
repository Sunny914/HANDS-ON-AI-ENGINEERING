"""Broken executor. Invalid amounts still reach the tool."""
from pydantic import BaseModel, Field


class RefundArgs(BaseModel):
    order_id: str = Field(min_length=1)
    amount: int = Field(gt=0)


def refund(order_id: str, amount: int, ledger: list) -> dict:
    ledger.append({"order_id": order_id, "amount": amount})
    return {"status": "refunded", "amount": amount}


def execute(raw: dict, ledger: list) -> dict:
    return refund(raw["order_id"], raw["amount"], ledger)
