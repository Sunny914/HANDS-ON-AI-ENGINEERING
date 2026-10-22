"""Broken prompt wiring. Invoke keys do not match the template."""
from langchain_core.prompts import ChatPromptTemplate


def build_prompt() -> ChatPromptTemplate:
    return ChatPromptTemplate.from_messages(
        [
            ("system", "Answer using only the context."),
            ("human", "{query}\n\n{context}"),
        ]
    )


def answer(question: str, excerpt: str) -> str:
    prompt = build_prompt()
    messages = prompt.invoke({"question": question, "excerpt": excerpt})
    return str(messages)
