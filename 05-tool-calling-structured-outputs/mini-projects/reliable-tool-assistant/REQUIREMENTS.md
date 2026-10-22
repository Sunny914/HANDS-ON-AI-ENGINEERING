# Requirements

- Tools: `get_order` and `refund`, registered with Pydantic argument models and JSON Schema.
- In-memory orders and an in-memory refund ledger.
- Principal with an id and a role: guest or support. The application constructs it. Tool arguments cannot set the role.
- Guests may get an order only when the order's owner id equals the principal id. Support may get any order in the fixture set.
- Only support may refund, and only up to a configured maximum amount.
- Refund requires an idempotency key. Repeats return the same receipt. A different amount for the same key conflicts.
- One loop function accepts a proposal dict and a principal and returns a result with a status: ok, invalid, denied, conflict, or tool_error.
- Invalid and denied proposals do not mutate the ledger.
- Tool exceptions become `tool_error` results.
- Logs include tool name, principal id, and status. They omit nothing you would not say to an auditor, and they do not include a raw API key. There is no API key in the default path.
- Optional: a fake model that returns the proposal. A live provider is behind `RUN_LIVE_LLM` and is not required.
- Optional note on how an MCP host would call the same executor. A live MCP server is not required.

Reuse Stage 01's idempotency lesson and Stage 02's distrust of model-shaped JSON. You do not need the Stage 04 retriever.
