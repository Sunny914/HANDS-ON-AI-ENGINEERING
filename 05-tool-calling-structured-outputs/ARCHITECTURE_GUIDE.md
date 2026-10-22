# Stage 05 Architecture

| Piece | Owns |
|-------|------|
| Tool spec | Name, description, argument model, side-effect flag |
| Registry | Lookup by name. Unknown name is an error. |
| Validator | Spec model applied to raw arguments |
| Policy | Principal plus tool plus arguments → allow or deny |
| Executor | Calls the function. Applies idempotency for side effects. |
| Loop | One fixture or one model turn: proposal in, result message out |

The tool function does not check the schema if the executor already did. The model client does not import the tool function. Policy does not perform I/O except what you explicitly need for a role lookup. In this stage a role can be a string on the principal.

You choose whether a denied call is a tool result the model can see or a hard stop. Document it. Both can be right. Silent success is not.
