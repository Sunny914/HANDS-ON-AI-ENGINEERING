"""Broken fence parser. The sample does not parse."""
import json

SAMPLE = """```json
{"summary": "Budget grew", "confidence": 0.4}
```"""


def parse_summary(text: str) -> dict:
    body = text.strip()
    if body.startswith("```") and body.endswith("```"):
        body = body[3:-3]
    return json.loads(body)
