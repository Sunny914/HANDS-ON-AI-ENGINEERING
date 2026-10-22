# Stage 11 Assumptions

- Python 3.10 or newer. Pydantic v2 is allowed for the pending-action model and is not required if you validate manually.
- LangGraph is optional. Exercises are written so a file-backed pending store is the checkpoint. If you call `interrupt`, confirm the API in the installed LangGraph and reread the Stage 08 note that a resumed node runs from the top.
- There is no real identity provider. Principals are strings such as `requester:riley` and `approver:sam`, checked against a role table in the application.
- `deploy` and `send_message` are fakes. They must not shell out, open a socket, or touch a real account.
- Time comes from a clock argument. Do not rely on the timezone of the laptop beyond storing timezone-aware timestamps or explicit integers.
