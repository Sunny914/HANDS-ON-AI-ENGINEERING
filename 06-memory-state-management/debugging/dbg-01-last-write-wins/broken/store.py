"""Broken store. A second save drops earlier fields."""


def save(db: dict, user_id: str, fields: dict) -> None:
    db[user_id] = {"user_id": user_id, **fields}
