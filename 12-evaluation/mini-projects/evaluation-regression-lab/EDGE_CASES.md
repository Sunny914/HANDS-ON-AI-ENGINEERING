# Edge Cases

| Case | Behavior |
|------|----------|
| Relevant set empty | Recall undefined, not 1 |
| Retrieved list shorter than k | Precision still divides by k |
| Citation not retrieved | Groundedness fails even if recall is high |
| Dataset versions differ | Comparison refused |
| Case failed in both configs | Known failure, not a regression |
| Judge passes, rule fails | Gate fails |
| Duplicate case id | Dataset rejected |
| Live judge flag unset | Suite stays offline |
