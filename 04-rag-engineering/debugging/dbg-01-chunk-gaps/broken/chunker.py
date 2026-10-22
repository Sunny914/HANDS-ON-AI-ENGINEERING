"""Broken chunker. Some characters never appear in a chunk."""


def chunk_text(text: str, size: int = 8, overlap: int = 2) -> list[str]:
    chunks = []
    start = 0
    while start < len(text):
        chunks.append(text[start : start + size])
        start += size + overlap
    return chunks


def demo() -> None:
    text = "abcdefghij"
    print(chunk_text(text))
