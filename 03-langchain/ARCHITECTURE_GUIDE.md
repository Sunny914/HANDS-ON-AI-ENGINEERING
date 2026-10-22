# Stage 03 Architecture

```text
document loader → excerpt selector → chain input dict → runnable → your result type
```

The loader and selector are plain Python. The runnable is the LangChain seam. Callers of the assistant depend on your function, not on `Runnable` types, unless a module is explicitly the chain module.

Do not put `ChatPromptTemplate` construction inside the HTTP layer if you add one. This stage does not require FastAPI. A function or CLI is enough.
