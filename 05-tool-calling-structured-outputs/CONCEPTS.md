# Stage 05 Concepts

Read this before ex-01.

## The five steps

```text
1. Model proposes a tool name and arguments.
2. Application checks the arguments against a schema.
3. Application checks that this caller may run this tool.
4. Application executes the tool and catches its failures.
5. Application sends the result back. The model may then answer.
```

If you skip 2 or 3, the model is a confused admin. Arguments are data from an untrusted parser, even when the model is one you pay for.

## Schemas

JSON Schema or a Pydantic model is the contract. The model does not get a second, looser contract in the executor. One model, used for the advertised schema and for the runtime check.

Structured output, from Stage 02, is the model filling your object. A tool call is the model asking your code to do something. Both need validation. Only the tool has side effects.

## Reliability

A read can be retried. A charge, send, or delete cannot, unless an idempotency key makes the second call return the first result. You practiced that pattern in Stage 01. Here the side effect is a tool.

Tool failures are results: timeout, upstream 503, not found. They are not a reason to run a different tool that the model did not name, unless a policy you wrote says so.

## Permissions

Allow and deny by tool name and by argument. "The model said admin" is not a principal. The principal comes from your application: a user id, a role, or a fixed local profile in this stage.

## MCP

The Model Context Protocol is a way for a host to list tools and call them on a server, often in another process. The trust boundary is the same five steps. This stage asks you to describe that boundary and, optionally, to read the current MCP Python SDK docs. It does not require you to ship a networked MCP server. SDK names move. If you take the optional path, record the SDK version and do not copy a stale tutorial blindly.

## What this stage does not build

A general agent loop with planning and memory. That is Stage 07. One tool round-trip is enough here.
