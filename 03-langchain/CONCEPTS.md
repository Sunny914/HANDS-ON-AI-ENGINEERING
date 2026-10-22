# Stage 03 Concepts

## Before ex-01

A chain is a function from input values to an output. You can write that with plain callables. LangChain's LCEL expresses the same idea with `|`:

```text
input dict → prompt template → chat model → output parser → value
```

If you cannot say what each arrow adds, do not add the framework yet. ex-01 is the plain version. ex-03 is the framework version of a similar flow.

## What to use

Verified against LangChain's docs on 2026-10-21:

- Current line is **LangChain 1.x**. `LLMChain` is legacy. It lives in `langchain-classic` and is deprecated. Do not use it.
- Build sequences with `|` from `langchain_core`.
- Prompts: `ChatPromptTemplate` in `langchain_core.prompts`.
- String parsing: `StrOutputParser`.
- Real model construction, when you opt in: `init_chat_model` from `langchain.chat_models`.
- The `langchain` 1.x package also exposes agent helpers such as `create_agent`. Ignore them in this stage.

## Fakes

`langchain_core` has shipped fake chat models under names such as `FakeListChatModel` or `GenericFakeChatModel`. Confirm the class in the version you installed. If the name moved, write a tiny fake with `invoke` and `ainvoke` that returns a `AIMessage`. Do not skip tests because the class name differed. Record the name you used in your exercise notes.

## What the framework does not own

File loading, which excerpt is relevant, cost limits, and your HTTP status codes stay in your code. The runnable should be a collaborator, not the whole program.
