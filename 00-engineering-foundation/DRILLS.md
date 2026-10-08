# Stage 00 — Optional Drills

**Drills are not graded.** Use them for 10–15 minutes before a session to warm up. Do not substitute drills for exercises.

## Drill format

Set a timer. No AI implementation help (H0–H3 only). Write code in a scratch file or REPL; delete or keep locally—nothing to submit.

## Fluency drills

| Drill | Prompt | Targets |
|-------|--------|---------|
| D1 | Given a list of ints, return dict of value → count | dict, loop |
| D2 | Normalize whitespace and title-case a sentence | strings |
| D3 | Merge two sorted lists into one sorted list | lists, comparison |
| D4 | Remove duplicates preserving order | set + list |
| D5 | Safe divide: return `None` on zero divisor | exceptions / guards |

## Function drills

| Drill | Prompt | Targets |
|-------|--------|---------|
| D6 | Write `clamp(n, low, high)` with clear errors for bad bounds | validation |
| D7 | Implement `group_by(items, key_fn)` | higher-order functions |
| D8 | Parse `"a=1;b=2"` into dict | parsing |

## OOP drills

| Drill | Prompt | Targets |
|-------|--------|---------|
| D9 | `BankAccount` with deposit/withdraw and insufficient funds error | classes |
| D10 | `Rectangle` with area and ordering by area | dunder methods intro |

## I/O drills

| Drill | Prompt | Targets |
|-------|--------|---------|
| D11 | Read a text file, print top 5 most common words | files, counters |
| D12 | Round-trip a dict through JSON in memory | json |

## Engineering drills

| Drill | Prompt | Targets |
|-------|--------|---------|
| D13 | Split D11 into `read_lines` + `count_words` in two functions | separation |
| D14 | Add type hints to D13 | typing |
| D15 | Write one pytest for `clamp` edge case | testing habit |

## When to stop drilling

If you complete an exercise without drills, skip drills that day. If you stumble on the same syntax three times in one week, repeat drills D1–D5 once.
