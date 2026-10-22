# Edge Cases

| Case | Behavior |
|------|----------|
| Missing path | Named error |
| Empty file | Named error, no call |
| No paragraph matches | Named error, no call, if you use keyword selection |
| Excerpt over the cap | Truncate with a marker, or reject. Test the one you chose. |
| Model returns a fence | Accepted if the JSON is valid |
| Model returns prose | Named parse error |
| Confidence 1.2 | Parse error |
| `invoke` inside async entry | Not acceptable. Use `ainvoke`. |
