# Stage 05 Assumptions

- Pydantic v2 is the schema tool. JSON Schema export via `model_json_schema()` is the expected method on v2 models. Confirm if a future major version renames it.
- No MCP package is required. Optional SDK use must be version-pinned in your own notes after you read current docs. This scaffold does not name a tutorial as correct.
- Provider tool-call JSON differs by vendor. Exercise fixtures are local and explicit. Do not treat them as OpenAI's or anyone else's permanent wire format.
- No API key is required.
