"""Broken threshold. Similarity is higher when nearer."""


def keep(rows: list[tuple[str, float]], minimum: float) -> list[str]:
    return [doc_id for doc_id, score in rows if score <= minimum]
