# Stage 02 Concepts

## Read this before ex-01

A model does not see characters as you do. A **tokenizer** splits text into token ids. A **context window** is the maximum tokens the model will accept for the prompt plus the completion. If the prompt is too large, the call fails or the product silently truncates. Truncation is a product bug until you choose it.

You are not implementing a real tokenizer in this stage. You will depend on a count that is given to you, or on a provider usage field. A character-length heuristic is only a guard when you label it as a heuristic.

**Attention**, at the level you need here: the model builds each new token using the tokens already in the context. That is why a long, messy prompt costs money and can crowd out the instruction. You do not need to derive the attention formula to build a gateway.

## Messages

Chats are a list of roles, not one string.

| Role | Typical job |
|------|-------------|
| system | Rules and identity. Not a place to hide user data you did not mean to trust. |
| user | The caller's request |
| assistant | Prior model output |

Tool messages appear in Stage 05. Do not invent a tool protocol here.

## Sampling

`temperature`, `top_p`, and `max_output_tokens` change randomness and length. They do not add knowledge. Temperature 0 is still not a formal proof of determinism across providers.

## Streaming

The provider sends deltas. Your code assembles them. The last event may be usage, not text. Dropping the tail drops the last word or the bill.

## Gateway idea

```text
caller → gateway → router → provider adapter → HTTP
                 ↘ usage ledger
```

The caller never imports a vendor SDK. Adapters translate vendor JSON into one response type. The router chooses a provider and a fallback. The ledger records tokens, latency, and estimated cost.

## What an SDK hides

Retries, default timeouts, error class names, and usage field names differ. If you cannot name those for your adapter, you do not yet have an interface. You have a demo.
