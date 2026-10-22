"""Broken stream assembler. Output is intentionally incomplete."""


def assemble(chunks: list[dict]) -> dict:
    parts: list[str] = []
    usage = None
    for chunk in chunks:
        if chunk.get("type") == "usage":
            usage = {"input_tokens": chunk["input_tokens"], "output_tokens": chunk["output_tokens"]}
            break
        delta = chunk.get("delta", "")
        if not delta.endswith(" "):
            break
        parts.append(delta)
    return {"text": "".join(parts), "usage": usage}
