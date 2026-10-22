# Stage 12 Architecture

```text
dataset version
  → runner (fake system or recorded predictions)
  → metric functions (pure)
  → report
  → gate
```

The runner may call a system you already built. The metric functions must not call a model. A judge, if you add one, is a separate function whose output cannot erase a rule failure.

Do not import a vendor eval SDK for the default path. Names such as LangSmith or DeepEval are optional later. They are not the measurement.
