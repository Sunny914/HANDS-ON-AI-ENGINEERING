"""One-shot scaffold helper. Safe to delete after generation."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TEMPLATE = """# {title}

**ID:** `{ex_id}`  
**Level:** {level}  
**Module path:** `{module_path}`

## Objective

{objective}

## Prerequisites

{prerequisites}

## Requirements

{requirements}

## Constraints

{constraints}

## Expected behavior

{expected}

## Edge cases

{edge_cases}

## Acceptance criteria

{acceptance}

## Common mistakes

{mistakes}

## H1 hint

{h1}

## Files

{files_note}

## Hints elsewhere

See [HINTS.md]({hints_rel}) for H2/H3 on marked exercises (`{ex_id}`).
"""


def write_readme(folder: Path, data: dict) -> None:
    folder.mkdir(parents=True, exist_ok=True)
    if "module_path" not in data:
        data = {**data, "module_path": folder.relative_to(ROOT).as_posix()}
    md = TEMPLATE.format(
        title=data["title"],
        ex_id=data["ex_id"],
        level=data["level"],
        module_path=data["module_path"],
        objective=data["objective"],
        prerequisites=data["prerequisites"],
        requirements=data["requirements"],
        constraints=data["constraints"],
        expected=data["expected"],
        edge_cases=data["edge_cases"],
        acceptance=data["acceptance"],
        mistakes=data["mistakes"],
        h1=data["h1"],
        files_note=data.get("files_note", "Create your own `.py` files in this folder unless the exercise provides a starter."),
        hints_rel=data.get("hints_rel", "../../../HINTS.md"),
    )
    (folder / "README.md").write_text(md, encoding="utf-8")


def bullet(lines: list[str]) -> str:
    return "\n".join(f"- {x}" for x in lines)


# --- Module 00 ---
M00 = ROOT / "00-python-engineering-reset" / "exercises"
m00_specs: list[dict] = [
    {
        "path": M00 / "ex-01",
        "ex_id": "ex-01",
        "module_path": "00-python-engineering-reset/exercises/ex-01",
        "title": "Expression Evaluator and Types",
        "level": "L1",
        "objective": "Practice literals, operators, and type introspection without libraries.",
        "prerequisites": bullet(["Variables", "int/float/str/bool", "arithmetic operators"]),
        "requirements": bullet([
            "Implement `describe_value(x)` returning a dict with keys: `type_name` (str), `is_numeric` (bool), `repr` (str from `repr()`).",
            "Implement `safe_add(a, b)` returning the sum if both numeric, else `None`.",
        ]),
        "constraints": bullet(["No third-party imports", "Single file `solution.py` acceptable"]),
        "expected": bullet([
            "`describe_value(3)` → type_name `'int'`, is_numeric True",
            "`safe_add('1', 2)` → None",
        ]),
        "edge_cases": bullet(["bool is numeric for `is_numeric`", "None input to describe_value"]),
        "acceptance": bullet(["Manual checks or tiny asserts in `if __name__` block", "You can explain bool vs int"]),
        "mistakes": bullet(["Using `type()` display name wrong", "Treating bool as non-numeric"]),
        "h1": "Numeric means `int` or `float` in this exercise; decide explicitly whether `bool` counts.",
    },
    {
        "path": M00 / "ex-02",
        "ex_id": "ex-02",
        "title": "Text Normalization Pipeline",
        "level": "L1",
        "objective": "Chain string operations into reusable steps.",
        "prerequisites": bullet(["str methods", "f-strings or format"]),
        "requirements": bullet([
            "Implement `normalize_whitespace(text) -> str` collapsing internal runs to single spaces, strip ends.",
            "Implement `slugify(text) -> str`: lowercase, whitespace to `-`, remove non-alphanumeric except hyphen.",
            "Implement `pipeline(text) -> str` applying normalize then slugify.",
        ]),
        "constraints": bullet(["Standard library only"]),
        "expected": bullet(['`pipeline("  Hello, World!  ")` → `hello-world` (punctuation removed)']),
        "edge_cases": bullet(["Empty string", "Only spaces", "Unicode letters—document if stripped or kept"]),
        "acceptance": bullet(["Three functions with docstrings", "Three examples printed"]),
        "mistakes": bullet(["Forgetting strip", "Replacing only first space"]),
        "h1": "Solve normalize first; slugify should assume already normalized or call normalize internally.",
    },
    {
        "path": M00 / "ex-03",
        "ex_id": "ex-03",
        "title": "List Algorithms Without Imports",
        "level": "L1",
        "objective": "Manipulate lists: search, insert, aggregate.",
        "prerequisites": bullet(["lists", "for loops", "indices"]),
        "requirements": bullet([
            "`second_largest(nums) -> int | None`",
            "`rotate_left(nums, k) -> list` (new list, not mutate unless you document)",
            "`chunk(nums, size) -> list[list]`",
        ]),
        "constraints": bullet(["No `max()` for second_largest if you want extra challenge—allowed if documented"]),
        "expected": bullet(["`second_largest([1,2,3])` → 2", "`chunk([1,2,3,4,5], 2)` → [[1,2],[3,4],[5]]"]),
        "edge_cases": bullet(["Duplicates in second_largest", "k=0", "size<=0"]),
        "acceptance": bullet(["Handle empty list for second_largest", "chunk last partial"]),
        "mistakes": bullet(["Mutating while iterating", "Off-by-one on k"]),
        "h1": "Second largest needs a pass or sort—consider duplicate max values.",
    },
    {
        "path": M00 / "ex-04",
        "ex_id": "ex-04",
        "title": "Control Flow: Ticket Pricing",
        "level": "L1",
        "objective": "Model rules with branches and compound conditions.",
        "prerequisites": bullet(["if/elif/else", "comparison operators"]),
        "requirements": bullet([
            "`ticket_price(age: int, is_student: bool, is_weekend: bool) -> float` with documented rules you choose (must include at least 3 tiers and one weekend modifier).",
            "Document rules in module docstring.",
        ]),
        "constraints": bullet(["No input(); use function only"]),
        "expected": bullet(["Deterministic floats", "Negative age raises ValueError"]),
        "edge_cases": bullet(["age 0", "very large age"]),
        "acceptance": bullet(["ValueError on invalid age", "Table of 5 scenarios in comments"]),
        "mistakes": bullet(["Overlapping elif leaving gaps", "Float rounding surprises"]),
        "h1": "Write rules as table on paper first, then encode without nested ternaries.",
    },
    {
        "path": M00 / "ex-05",
        "ex_id": "ex-05",
        "title": "Functions: Unit Conversion",
        "level": "L1",
        "objective": "Compose small conversion functions.",
        "prerequisites": bullet(["functions", "return", "float"]),
        "requirements": bullet([
            "Implement km↔mi, c↔f, kg↔lb (pick formulas, document constants).",
            "`convert(value, from_unit, to_unit)` dispatching via dict or if chain.",
        ]),
        "constraints": bullet(["Raise ValueError for unknown units"]),
        "expected": bullet(["Round-trip within tolerance 1e-6 for floats"]),
        "edge_cases": bullet(["Negative distances?", "Unknown unit strings"]),
        "acceptance": bullet(["At least 6 unit tokens supported", "Docstring lists units"]),
        "mistakes": bullet(["Inverted formula", "Case-sensitive units"]),
        "h1": "Centralize constants; conversion functions stay pure.",
    },
    {
        "path": M00 / "ex-06",
        "ex_id": "ex-06",
        "title": "Records with Dicts, Sets, Tuples",
        "level": "L2",
        "objective": "Choose structures for membership and record lookup.",
        "prerequisites": bullet(["dict", "set", "tuple"]),
        "requirements": bullet([
            "Given list of user dicts `{id, name, tags: list[str]}`, build indexes: by_id, tag → set of ids.",
            "`users_with_all_tags(index, tags) -> list[int]`",
        ]),
        "constraints": bullet(["Pure functions"]),
        "expected": bullet(["Correct sets for overlapping tags"]),
        "edge_cases": bullet(["Unknown tag", "empty tags list meaning all users?—define"]),
        "acceptance": bullet(["Define empty tags behavior in docstring"]),
        "mistakes": bullet(["Storing lists where sets belong", "Mutating input dicts"]),
        "h1": "Invert index once; query functions stay cheap.",
    },
    {
        "path": M00 / "ex-07",
        "ex_id": "ex-07",
        "title": "Comprehensions and Transformations",
        "level": "L2",
        "objective": "Use comprehensions and map/filter style clearly.",
        "prerequisites": bullet(["list/dict comprehensions"]),
        "requirements": bullet([
            "From list of sentences, produce word frequency dict ignoring case and punctuation (define punctuation set).",
            "Implement same with at least one comprehension and one loop version; compare readability in comment.",
        ]),
        "constraints": bullet(["No collections.Counter"]),
        "expected": bullet(["'Hello hello' counts hello twice"]),
        "edge_cases": bullet(["Empty sentence list", "Punctuation-only tokens"]),
        "acceptance": bullet(["Both versions pass same tests"]),
        "mistakes": bullet(["Not normalizing case", "Empty string keys"]),
        "h1": "Tokenize by splitting and stripping punctuation per word.",
    },
    {
        "path": M00 / "ex-08",
        "ex_id": "ex-08",
        "title": "Flexible Formatters",
        "level": "L2",
        "objective": "Use `*args` and `**kwargs` deliberately.",
        "prerequisites": bullet(["function arguments"]),
        "requirements": bullet([
            "`make_table(headers, *rows, **options)` → str; options: `padding` int default 1, `delimiter` str default `|`.",
            "Validate row width matches headers.",
        ]),
        "constraints": bullet(["Raise ValueError on ragged rows"]),
        "expected": bullet(["Aligned simple table string"]),
        "edge_cases": bullet(["No rows", "Unicode width not required"]),
        "acceptance": bullet(["kwargs override defaults"]),
        "mistakes": bullet(["Mutating headers", "Forgetting to stringify cells"]),
        "h1": "Build row strings in a loop; kwargs only affect formatting.",
    },
    {
        "path": M00 / "ex-09",
        "ex_id": "ex-09",
        "title": "Scope and Mutable Defaults",
        "level": "L2",
        "objective": "Implement correct patterns and explain broken ones.",
        "prerequisites": bullet(["scope", "default arguments"]),
        "requirements": bullet([
            "Implement `append_item_wrong` (intentionally uses mutable default) and `append_item_right`.",
            "Demonstrate difference in `demo()` printing results.",
            "Implement `counter()` factory using closure or class—your choice—to return increment function.",
        ]),
        "constraints": bullet(["Document why wrong version fails"]),
        "expected": bullet(["Right version isolated", "Wrong shares state"]),
        "edge_cases": bullet(["Multiple callers"]),
        "acceptance": bullet(["Written explanation in comments"]),
        "mistakes": bullet(["Using mutable default", "Confusing global vs closure"]),
        "h1": "Mutable default is evaluated once at function definition time.",
    },
    {
        "path": M00 / "ex-10",
        "ex_id": "ex-10",
        "title": "Copying Nested Structures",
        "level": "L2",
        "objective": "Shallow vs deep copy behavior.",
        "prerequisites": bullet(["copy module", "nested lists/dicts"]),
        "requirements": bullet([
            "Given nested dict, functions `shallow_copy_change` and `deep_copy_change` that modify nested value and return copies.",
            "Explain in comments which original changes.",
        ]),
        "constraints": bullet(["Use copy.copy and copy.deepcopy"]),
        "expected": bullet(["Demonstration script output documented"]),
        "edge_cases": bullet(["Immutable nested values"]),
        "acceptance": bullet(["Commentary matches behavior"]),
        "mistakes": bullet(["Assuming assignment copies", "Deep copying everything always"]),
        "h1": "Shallow copy shares nested references.",
    },
    {
        "path": M00 / "ex-11",
        "ex_id": "ex-11",
        "title": "Safe Batch Operations and Exceptions",
        "level": "L3",
        "objective": "Handle failures per item without stopping whole batch.",
        "prerequisites": bullet(["try/except", "raise"]),
        "requirements": bullet([
            "`safe_divide_batch(pairs: list[tuple]) -> list` returning results or None per pair on zero division.",
            "`parse_ints(lines: list[str]) -> tuple[list[int], list[str]]` successes and error messages.",
        ]),
        "constraints": bullet(["No bare except"]),
        "expected": bullet(["Batch completes"]),
        "edge_cases": bullet(["Empty input", "non-numeric strings"]),
        "acceptance": bullet(["Specific exception types caught"]),
        "mistakes": bullet(["Bare except", "Losing error context"]),
        "h1": "Catch narrow exceptions; collect errors instead of printing inside parser.",
    },
    {
        "path": M00 / "ex-12",
        "ex_id": "ex-12",
        "title": "JSON Settings Load/Save",
        "level": "L3",
        "objective": "Round-trip configuration with validation.",
        "prerequisites": bullet(["json", "files", "with statement"]),
        "requirements": bullet([
            "Schema: `{theme: str, font_size: int, features: list[str]}`.",
            "`load_settings(path)`, `save_settings(path, data)`, `validate_settings(data) -> None` raises ValueError.",
        ]),
        "constraints": bullet(["UTF-8", "Pretty print on save with indent"]),
        "expected": bullet(["Invalid types rejected before save"]),
        "edge_cases": bullet(["Missing file", "Malformed JSON"]),
        "acceptance": bullet(["ValueError messages mention field"]),
        "mistakes": bullet(["Not validating on load", "Silent defaults hiding bugs"]),
        "h1": "Validate after load and before save.",
    },
    {
        "path": M00 / "ex-13",
        "ex_id": "ex-13",
        "title": "Two-Module Word Statistics",
        "level": "L3",
        "objective": "Split code across modules with clear imports.",
        "prerequisites": bullet(["modules", "packages basics"]),
        "requirements": bullet([
            "Package `wordstats` with `tokenize.py` and `stats.py` and `__main__.py`.",
            "CLI: `python -m wordstats path/to/file.txt` prints top 5 tokens.",
        ]),
        "constraints": bullet(["Relative imports within package"]),
        "expected": bullet(["Runs as module"]),
        "edge_cases": bullet(["Empty file", "binary file error"]),
        "acceptance": bullet(["No circular imports"]),
        "mistakes": bullet(["Running submodule directly breaking imports", "Logic all in __main__"]),
        "h1": "__main__ orchestrates; tokenize vs aggregate split.",
    },
    {
        "path": M00 / "ex-14",
        "ex_id": "ex-14",
        "title": "Parse and Aggregate CSV-like Rows",
        "level": "L3",
        "objective": "Combine parsing, dicts, and aggregation.",
        "prerequisites": bullet(["strings", "dicts", "split"]),
        "requirements": bullet([
            "Parse lines `name,amount,category` (no quoted commas) into records.",
            "`summary_by_category(rows) -> dict[str, float]` totals.",
        ]),
        "constraints": bullet(["Skip malformed lines with warning to stderr"]),
        "expected": bullet(["Correct sums"]),
        "edge_cases": bullet(["Negative amounts", "blank lines"]),
        "acceptance": bullet(["Malformed line count reported"]),
        "mistakes": bullet(["Not stripping", "Float parse errors"]),
        "h1": "Parse line → validate → accumulate; keep parse pure.",
    },
    {
        "path": M00 / "ex-15",
        "ex_id": "ex-15",
        "title": "Grade Book CLI (Design)",
        "level": "L4",
        "objective": "Design and implement a small multi-function grade book.",
        "prerequisites": bullet(["functions", "dicts", "CLI input optional"]),
        "requirements": bullet([
            "Store students → list of scores; support add_score, average, letter_grade (your scale).",
            "Simple menu loop or command args—your choice.",
        ]),
        "constraints": bullet(["At least 3 modules or 3 files"]),
        "expected": bullet(["Session usable interactively"]),
        "edge_cases": bullet(["No scores", "unknown student"]),
        "acceptance": bullet(["You can draw module diagram"]),
        "mistakes": bullet(["Global dict everywhere", "No separation of I/O"]),
        "h1": "Separate storage from presentation from grading rules.",
    },
    {
        "path": M00 / "ex-16",
        "ex_id": "ex-16",
        "title": "Notes Manager (Multi-File Design)",
        "level": "L4",
        "objective": "Persist notes to JSON with CRUD.",
        "prerequisites": bullet(["json", "ex-12"]),
        "requirements": bullet([
            "CRUD for notes `{id, title, body, updated_at}` persisted to file.",
            "CLI commands: add, list, view, delete.",
        ]),
        "constraints": bullet(["Atomic save strategy documented"]),
        "expected": bullet(["Survives restart"]),
        "edge_cases": bullet(["Duplicate titles allowed?", "corrupt file"]),
        "acceptance": bullet(["README in folder how to run"]),
        "mistakes": bullet(["Overwrite file without temp", "IDs as ints vs str inconsistency"]),
        "h1": "Pick ID strategy first; storage layer knows file format only.",
    },
    {
        "path": M00 / "ex-17",
        "ex_id": "ex-17",
        "title": "Debug: Mutation in Aggregation",
        "level": "L5",
        "objective": "Diagnose incorrect totals caused by mutation.",
        "prerequisites": bullet(["debugging guide"]),
        "requirements": bullet([
            "Run `broken/aggregator.py`; output is wrong for multi-group input.",
            "Fix code; document root cause.",
        ]),
        "constraints": bullet(["Do not rewrite from scratch unless needed"]),
        "expected": bullet(["Tests in README table pass after fix"]),
        "edge_cases": bullet(["Single group", "multiple groups"]),
        "acceptance": bullet(["2-3 sentence postmortem in FIX_NOTES.md"]),
        "mistakes": bullet(["Fixing symptom by copy-paste without understanding"]),
        "h1": "Watch shared list references across groups.",
        "files_note": "Starter: `broken/aggregator.py`. Create `FIX_NOTES.md`.",
    },
    {
        "path": M00 / "ex-18",
        "ex_id": "ex-18",
        "title": "Debug: None and Truthiness",
        "level": "L5",
        "objective": "Fix logic errors involving None and empty collections.",
        "prerequisites": bullet(["None", "bool context"]),
        "requirements": bullet(["Fix `broken/profile_merge.py` so merged profiles correct"]),
        "constraints": bullet(["Keep function signatures"]),
        "expected": bullet(["Examples in README pass"]),
        "edge_cases": bullet(["Empty dict fields", "zero values"]),
        "acceptance": bullet(["FIX_NOTES.md"]),
        "mistakes": bullet(["Using `if not value` when 0 valid"]),
        "h1": "Distinguish missing key vs empty vs zero.",
        "files_note": "Starter: `broken/profile_merge.py`.",
    },
    {
        "path": M00 / "ex-19",
        "ex_id": "ex-19",
        "title": "Debug: File Paths and Encoding",
        "level": "L5",
        "objective": "Fix file handling bugs.",
        "prerequisites": bullet(["paths", "encoding"]),
        "requirements": bullet(["Fix `broken/read_config.py` to read `data/settings.json` reliably from exercise dir"]),
        "constraints": bullet(["Use pathlib or os.path consistently"]),
        "expected": bullet(["Works when cwd is not exercise folder if you support `--path`"]),
        "edge_cases": bullet(["Missing file", "UTF-8 content"]),
        "acceptance": bullet(["FIX_NOTES.md"]),
        "mistakes": bullet(["Relative path only from cwd"]),
        "h1": "Anchor paths to `__file__` location.",
        "files_note": "Starter: `broken/read_config.py`, sample `data/settings.json`.",
    },
    {
        "path": M00 / "ex-20",
        "ex_id": "ex-20",
        "title": "Debug: Imports and Package Layout",
        "level": "L5",
        "objective": "Fix import errors in small package.",
        "prerequisites": bullet(["packages"]),
        "requirements": bullet(["Make `broken/pkg` importable and `python -m broken.pkg.main` work"]),
        "constraints": bullet(["Minimal changes"]),
        "expected": bullet(["Command runs without ImportError"]),
        "edge_cases": bullet(["Running as script vs module"]),
        "acceptance": bullet(["FIX_NOTES.md explains fix"]),
        "mistakes": bullet(["Circular imports", "missing __init__"]),
        "h1": "Trace import graph from entry point.",
        "files_note": "Starter under `broken/pkg/`.",
    },
    {
        "path": M00 / "ex-21",
        "ex_id": "ex-21",
        "title": "Library Catalog (Basic OOP)",
        "level": "L4",
        "objective": "Model entities with classes.",
        "prerequisites": bullet(["classes", "methods"]),
        "requirements": bullet([
            "Classes `Book`, `Member`, `Library` with checkout/return rules (max 3 books per member).",
            "Raise domain errors you define.",
        ]),
        "constraints": bullet(["No persistence required"]),
        "expected": bullet(["In-memory demo in main"]),
        "edge_cases": bullet(["Checkout unavailable", "return unknown book"]),
        "acceptance": bullet(["At least 2 custom exception types"]),
        "mistakes": bullet(["God class", "Public mutable lists without invariants"]),
        "h1": "Library orchestrates; Book/Member enforce local rules.",
    },
    {
        "path": M00 / "ex-22",
        "ex_id": "ex-22",
        "title": "Merge and Dedupe Record Lists",
        "level": "L3",
        "objective": "Combine records from two sources by key.",
        "prerequisites": bullet(["dicts", "list comprehensions"]),
        "requirements": bullet([
            "Records `{id, ...}`; merge B into A with B wins on conflict; dedupe by id stable order.",
        ]),
        "constraints": bullet(["O(n) average"]),
        "expected": bullet(["Predictable ordering documented"]),
        "edge_cases": bullet(["Missing id", "duplicate within same list"]),
        "acceptance": bullet(["Tests as assert block"]),
        "mistakes": bullet(["Nested loops O(n^2) unnecessarily"]),
        "h1": "Index by id with dict.",
    },
    {
        "path": M00 / "ex-23",
        "ex_id": "ex-23",
        "title": "Integration: Config + Report Pipeline",
        "level": "L3/L4",
        "objective": "Wire JSON config to file processing pipeline.",
        "prerequisites": bullet(["ex-12", "ex-14"]),
        "requirements": bullet([
            "Config selects input path and categories filter.",
            "Read CSV-like sales file, emit summary report to stdout and optional output path.",
        ]),
        "constraints": bullet(["3+ modules", "logging at INFO for skipped lines"]),
        "expected": bullet(["End-to-end run documented"]),
        "edge_cases": bullet(["All lines skipped", "bad config"]),
        "acceptance": bullet(["Follow implementation workflow"]),
        "mistakes": bullet(["Monolith main", "No validation on config"]),
        "h1": "Vertical slice: config load → parse one line → full file.",
    },
]

for spec in m00_specs:
    write_readme(spec["path"], spec)

# --- Module 01 core ---
M01 = ROOT / "01-python-software-engineering" / "exercises"
m01_core: list[dict] = [
    {
        "path": M01 / "ex-01",
        "ex_id": "ex-01",
        "module_path": "01-python-software-engineering/exercises/ex-01",
        "title": "Pure Validation Functions",
        "level": "L1",
        "objective": "Write testable validators without I/O.",
        "prerequisites": bullet(["functions", "strings"]),
        "requirements": bullet([
            "`is_valid_email(s) -> bool` (pragmatic rules documented)",
            "`is_strong_password(s) -> bool` (length + char classes—you define)",
        ]),
        "constraints": bullet(["No regex required unless you choose"]),
        "expected": bullet(["Clear True/False"]),
        "edge_cases": bullet(["Empty", "unicode local part"]),
        "acceptance": bullet(["Docstring lists rules"]),
        "mistakes": bullet(["Overly strict RFC", "Printing inside validators"]),
        "h1": "Validators return bool; caller decides error messages.",
    },
    {
        "path": M01 / "ex-02",
        "ex_id": "ex-02",
        "module_path": "01-python-software-engineering/exercises/ex-02",
        "title": "Multi-Function Text Utilities Module",
        "level": "L1→L2",
        "objective": "Grow a single module with related functions.",
        "prerequisites": bullet(["module 00 strings"]),
        "requirements": bullet([
            "Module `textutils.py`: truncate, wrap, excerpt, count_lines.",
            "Each function documented with examples.",
        ]),
        "constraints": bullet(["No classes yet"]),
        "expected": bullet(["Importable without side effects"]),
        "edge_cases": bullet(["truncate shorter than limit", "wrap width 1"]),
        "acceptance": bullet(["`if __name__` demo only"]),
        "mistakes": bullet(["Side effects on import"]),
        "h1": "Keep functions pure; shared helpers prefixed with _.",
    },
    {
        "path": M01 / "ex-03",
        "ex_id": "ex-03",
        "module_path": "01-python-software-engineering/exercises/ex-03",
        "title": "Package Layout: textstats",
        "level": "L2",
        "objective": "Create installable-style package layout.",
        "prerequisites": bullet(["packages"]),
        "requirements": bullet([
            "Package `textstats/` with submodules for tokenize, frequencies, cli.",
            "Entry via `python -m textstats`.",
        ]),
        "constraints": bullet(["src layout or flat—document choice"]),
        "expected": bullet(["Imports clean"]),
        "edge_cases": bullet(["empty input"]),
        "acceptance": bullet(["README how to run"]),
        "mistakes": bullet(["Implicit namespace packages confusion"]),
        "h1": "Pick flat vs src layout and stick to it.",
    },
    {
        "path": M01 / "ex-04",
        "ex_id": "ex-04",
        "module_path": "01-python-software-engineering/exercises/ex-04",
        "title": "Dataclass Domain Models",
        "level": "L2",
        "objective": "Model data with dataclasses and invariants.",
        "prerequisites": bullet(["dataclasses"]),
        "requirements": bullet([
            "`Order`, `LineItem` with computed `total`.",
            "Method `add_item` enforcing positive quantity and price.",
        ]),
        "constraints": bullet(["Use @dataclass"]),
        "expected": bullet(["Immutability optional—document"]),
        "edge_cases": bullet(["zero quantity rejected"]),
        "acceptance": bullet(["__post_init__ or methods enforce rules"]),
        "mistakes": bullet(["Mutable default lists on dataclass"]),
        "h1": "Put validation in __post_init__ or add_item.",
    },
    {
        "path": M01 / "ex-05",
        "ex_id": "ex-05",
        "module_path": "01-python-software-engineering/exercises/ex-05",
        "title": "Type Hints and Static Reasoning",
        "level": "L2",
        "objective": "Add types to untyped module and fix mismatches.",
        "prerequisites": bullet(["typing basics"]),
        "requirements": bullet([
            "Take provided `untyped_stub.py` (comment-only spec) and implement typed `inventory.py` API from README signatures.",
            "Run mypy if installed; otherwise manual review checklist in TYPES_CHECKLIST.md.",
        ]),
        "constraints": bullet(["No Any unless justified"]),
        "expected": bullet(["Signatures match README"]),
        "edge_cases": bullet(["Optional fields"]),
        "acceptance": bullet(["TYPES_CHECKLIST.md completed"]),
        "mistakes": bullet(["Dict without key types", "ignoring None"]),
        "h1": "Model optional as Optional[T] or | None.",
        "files_note": "Implement `inventory.py`; `untyped_stub.py` is comment-only spec.",
    },
    {
        "path": M01 / "ex-06",
        "ex_id": "ex-06",
        "module_path": "01-python-software-engineering/exercises/ex-06",
        "title": "Custom Iterator",
        "level": "L2",
        "objective": "Implement iterator protocol.",
        "prerequisites": bullet(["iter", "next"]),
        "requirements": bullet([
            "Class `Range` or `BatchIterator` over a sequence with given batch size.",
        ]),
        "constraints": bullet(["No itertools.batched unless you reimplement first"]),
        "expected": bullet(["for-loop works"]),
        "edge_cases": bullet(["empty seq", "batch size > len"]),
        "acceptance": bullet(["StopIteration at end"]),
        "mistakes": bullet(["Infinite loop", "reusing exhausted iterator"]),
        "h1": "Separate iterator state from collection.",
    },
    {
        "path": M01 / "ex-07",
        "ex_id": "ex-07",
        "module_path": "01-python-software-engineering/exercises/ex-07",
        "title": "Generator-Based Line Processing",
        "level": "L2",
        "objective": "Stream lines without loading entire file.",
        "prerequisites": bullet(["generators", "yield"]),
        "requirements": bullet([
            "`iter_lines(path)`, `iter_nonempty_stripped(path)`, `grep(path, substring)` generators.",
        ]),
        "constraints": bullet(["Handle missing file with FileNotFoundError"]),
        "expected": bullet(["Memory stable on large file—you can fake with generator"]),
        "edge_cases": bullet(["empty file", "encoding errors policy"]),
        "acceptance": bullet(["Document encoding default"]),
        "mistakes": bullet(["Reading all lines into list"]),
        "h1": "yield inside with-open loop.",
    },
    {
        "path": M01 / "ex-08",
        "ex_id": "ex-08",
        "module_path": "01-python-software-engineering/exercises/ex-08",
        "title": "Timing Decorator",
        "level": "L2",
        "objective": "Cross-cutting concern with decorator.",
        "prerequisites": bullet(["decorators", "functools.wraps"]),
        "requirements": bullet([
            "`@timed` logging duration to stdout or logger.",
            "Preserve function metadata.",
        ]),
        "constraints": bullet(["Use wraps"]),
        "expected": bullet(["Nested calls show separate timings"]),
        "edge_cases": bullet(["exceptions still record time?—document"]),
        "acceptance": bullet(["Docstring on decorator"]),
        "mistakes": bullet(["Forgetting wraps", "timing including argument stringify"]),
        "h1": "Decorator returns wrapper accepting *args, **kwargs.",
    },
    {
        "path": M01 / "ex-09",
        "ex_id": "ex-09",
        "module_path": "01-python-software-engineering/exercises/ex-09",
        "title": "Context Manager for Temporary State",
        "level": "L2",
        "objective": "Implement context manager (class or @contextmanager).",
        "prerequisites": bullet(["with statement"]),
        "requirements": bullet([
            "`temporary_env(vars: dict)` setting os.environ keys, restoring after block.",
        ]),
        "constraints": bullet(["Restore even on exception"]),
        "expected": bullet(["Nested contexts behave"]),
        "edge_cases": bullet(["Key existed before", "delete vs restore"]),
        "acceptance": bullet(["Tests or demo script"]),
        "mistakes": bullet(["Not restoring on error"]),
        "h1": "Save old values in __enter__.",
    },
    {
        "path": M01 / "ex-10",
        "ex_id": "ex-10",
        "module_path": "01-python-software-engineering/exercises/ex-10",
        "title": "Configuration from Env + File",
        "level": "L3",
        "objective": "Layered config with precedence.",
        "prerequisites": bullet(["json/yaml optional", "os.environ"]),
        "requirements": bullet([
            "Load defaults, overlay file, overlay env vars with prefix `APP_`.",
            "Expose `Settings` object with typed fields.",
        ]),
        "constraints": bullet(["Document precedence"]),
        "expected": bullet(["Missing file uses defaults"]),
        "edge_cases": bullet(["Invalid env int", "unknown keys ignored or strict—choose"]),
        "acceptance": bullet(["Small settings.json example"]),
        "mistakes": bullet(["Global mutable settings everywhere"]),
        "h1": "Load once; pass Settings into services.",
    },
    {
        "path": M01 / "ex-11",
        "ex_id": "ex-11",
        "module_path": "01-python-software-engineering/exercises/ex-11",
        "title": "Logging Policy Across Modules",
        "level": "L3",
        "objective": "Configure logging in one place, use in modules.",
        "prerequisites": bullet(["logging module"]),
        "requirements": bullet([
            "`logging_config.py` sets format/level from settings.",
            "At least two modules log with module-level loggers.",
        ]),
        "constraints": bullet(["No print in library code"]),
        "expected": bullet(["Consistent format"]),
        "edge_cases": bullet(["DEBUG off hides debug"]),
        "acceptance": bullet(["README how to change level"]),
        "mistakes": bullet(["basicConfig in every file"]),
        "h1": "getLogger(__name__) pattern.",
    },
    {
        "path": M01 / "ex-12",
        "ex_id": "ex-12",
        "module_path": "01-python-software-engineering/exercises/ex-12",
        "title": "Custom Exceptions + Service Boundary",
        "level": "L3",
        "objective": "Translate storage errors to domain errors.",
        "prerequisites": bullet(["exceptions", "modules"]),
        "requirements": bullet([
            "In-memory `UserRepository` raising `UserNotFound`.",
            "`UserService` catching/converting lower-level errors.",
            "CLI prints friendly message.",
        ]),
        "constraints": bullet(["3+ files"]),
        "expected": bullet(["Stack trace not shown to user for expected errors"]),
        "edge_cases": bullet(["duplicate user"]),
        "acceptance": bullet(["Exception hierarchy diagram in comments"]),
        "mistakes": bullet(["except Exception everywhere"]),
        "h1": "Domain errors cross service boundary; CLI maps to text.",
    },
]

for spec in m01_core:
    write_readme(spec["path"], spec)

# Architecture
ARCH = M01 / "architecture"
arch_specs = [
    {
        "path": ARCH / "arch-01-json-records-report",
        "ex_id": "arch-01",
        "module_path": "01-python-software-engineering/exercises/architecture/arch-01-json-records-report",
        "title": "JSON Records → Validated Report",
        "level": "Architecture",
        "objective": "Design structure for load → validate → transform → report.",
        "prerequisites": bullet(["module 01 ex-01–05"]),
        "requirements": bullet([
            "Load records from JSON file (schema in REQUIREMENTS.md).",
            "Validate, compute per-category totals and top spenders, write text report.",
            "Do NOT open REFERENCE.md until design written.",
        ]),
        "constraints": bullet(["You choose file layout", "Tests required"]),
        "expected": bullet(["CLI: `python -m app` or similar documented"]),
        "edge_cases": bullet(["invalid records", "empty file"]),
        "acceptance": bullet(["Architecture answers in `YOUR_ARCHITECTURE.md`", "REFERENCE comparison notes"]),
        "mistakes": bullet(["Validation inside print statements", "no separation"]),
        "h1": "Start from data flow diagram, not file names.",
        "files_note": "See REQUIREMENTS.md and REFERENCE.md (after design).",
    },
    {
        "path": ARCH / "arch-02-expense-ledger",
        "ex_id": "arch-02",
        "module_path": "01-python-software-engineering/exercises/architecture/arch-02-expense-ledger",
        "title": "Expense Ledger CLI",
        "level": "Architecture",
        "objective": "CRUD + summaries with explicit layers.",
        "prerequisites": bullet(["arch-01 experience"]),
        "requirements": bullet([
            "Commands: add, list, summary by month, export csv.",
            "Persistence JSON; validation at boundary.",
        ]),
        "constraints": bullet(["Service/repository split required"]),
        "expected": bullet(["Month filter correct"]),
        "edge_cases": bullet(["timezone on dates—use naive ISO dates"]),
        "acceptance": bullet(["YOUR_ARCHITECTURE.md + tests"]),
        "mistakes": bullet(["CLI parses business rules"]),
        "h1": "Repository knows file format; service knows use cases.",
        "files_note": "REQUIREMENTS.md, REFERENCE.md after design.",
    },
    {
        "path": ARCH / "arch-03-layered-config-service",
        "ex_id": "arch-03",
        "module_path": "01-python-software-engineering/exercises/architecture/arch-03-layered-config-service",
        "title": "Layered Service with Config",
        "level": "Architecture",
        "objective": "Combine config, logging, exceptions in one app.",
        "prerequisites": bullet(["ex-10–12"]),
        "requirements": bullet([
            "Feature: import CSV users, dedupe by email, save JSON report.",
            "Full logging and settings.",
        ]),
        "constraints": bullet(["No monolith >400 lines in one file"]),
        "expected": bullet(["Dedupe policy documented"]),
        "edge_cases": bullet(["malformed csv rows"]),
        "acceptance": bullet(["Compare REFERENCE.md"]),
        "mistakes": bullet(["Config read in repository"]),
        "h1": "Dependency injection via constructor parameters.",
        "files_note": "REQUIREMENTS.md, REFERENCE.md.",
    },
]
for spec in arch_specs:
    write_readme(spec["path"], spec)

# Testing track
TEST = M01 / "testing"
test_specs = [
    ("test-01-unit-basics", "test-01", "Unit Tests for Pure Functions", "Implement `mathutils.py` per spec; write tests in `tests/test_mathutils.py` per REQUIREMENTS.md."),
    ("test-02-edge-exceptions", "test-02", "Edge Cases and Exceptions", "Implement `divide` and `parse_ratio`; tests must cover zero division and bad input."),
    ("test-03-parametrize", "test-03", "Parameterized Cases", "Email validator from ex-01; write parametrized tests for valid/invalid table."),
    ("test-04-fixtures", "test-04", "Fixtures for File Setup", "Implement loader; tests use tmp_path fixture for sample JSON."),
    ("test-05-mocking", "test-05", "Mock External Boundary", "WeatherService calls `fetch_json(url)`; mock fetch for tests."),
]
for folder, ex_id, title, req_summary in test_specs:
    write_readme(
        TEST / folder,
        {
            "path": TEST / folder,
            "ex_id": ex_id,
            "module_path": f"01-python-software-engineering/exercises/testing/{folder}",
            "title": title,
            "level": "Testing",
            "objective": "Write pytest suite from natural language requirements.",
            "prerequisites": bullet(["pytest installed", "TESTING_GUIDE.md"]),
            "requirements": bullet([req_summary, "Read REQUIREMENTS.md for case list"]),
            "constraints": bullet(["You write all test code", "No solution tests provided"]),
            "expected": bullet(["pytest passes when product correct"]),
            "edge_cases": bullet(["Listed in REQUIREMENTS.md"]),
            "acceptance": bullet(["At least one test per requirement bullet in REQUIREMENTS.md"]),
            "mistakes": bullet(["Testing implementation not behavior", "over-mocking"]),
            "h1": "Write failing test first for one requirement.",
            "files_note": "REQUIREMENTS.md is authoritative; create product code as needed.",
        },
    )

# Debugging track
DBG = M01 / "debugging"
dbg_specs = [
    ("dbg-01-mutation", "dbg-01", "Mutation in Service Layer"),
    ("dbg-02-imports", "dbg-02", "Import and Package Errors"),
    ("dbg-03-resources", "dbg-03", "Resource Management"),
    ("dbg-04-types-none", "dbg-04", "Types and None Handling"),
    ("dbg-05-tests-misleading", "dbg-05", "Tests and Production Mismatch"),
]
for folder, ex_id, title in dbg_specs:
    write_readme(
        DBG / folder,
        {
            "path": DBG / folder,
            "ex_id": ex_id,
            "module_path": f"01-python-software-engineering/exercises/debugging/{folder}",
            "title": title,
            "level": "Debugging",
            "objective": "Something is wrong. Diagnose and fix.",
            "prerequisites": bullet(["DEBUGGING_GUIDE.md"]),
            "requirements": bullet([
                "Run broken starter; reproduce failure.",
                "Fix minimally; record FIX_NOTES.md.",
                "Use HINTS.md in this folder (H1→H3) only after hypothesis.",
            ]),
            "constraints": bullet(["Do not read H2/H3 first"]),
            "expected": bullet(["Behavior matches README acceptance table"]),
            "edge_cases": bullet(["See README table"]),
            "acceptance": bullet(["FIX_NOTES.md with root cause"]),
            "mistakes": bullet(["Random changes without reproduction"]),
            "h1": "Read traceback; localize smallest failing input.",
            "files_note": "Broken code under `broken/`; hints in `HINTS.md`.",
        },
    )

# Module 02
M02 = ROOT / "02-async-python-preview" / "exercises"
m02_specs = [
    ("ex-01", "Blocking Sequential Fetch Simulation", "L1", "Implement `fetch_all(urls)` using `time.sleep` to simulate latency sequentially; print total time."),
    ("ex-02", "Introducing async/await", "L2", "Rewrite one fetch as async sleep; run with asyncio.run."),
    ("ex-03", "Tasks and asyncio.gather", "L3", "Concurrent fetches with gather; compare count and timing."),
    ("ex-04", "Timeouts", "L3", "Add per-task timeout; handle asyncio.TimeoutError gracefully."),
    ("ex-05", "Sequential vs Concurrent Comparison", "L4", "Two implementations; table of timings in COMPARISON.md you write."),
    ("ex-06", "Bounded Concurrency", "L4", "Limit concurrent tasks (e.g. semaphore); document why."),
]
for ex_id, title, level, req in m02_specs:
    write_readme(
        M02 / ex_id,
        {
            "path": M02 / ex_id,
            "ex_id": ex_id,
            "module_path": f"02-async-python-preview/exercises/{ex_id}",
            "title": title,
            "level": level,
            "objective": "Bridge async concepts toward Stage 01.",
            "prerequisites": bullet(["asyncio docs skim"]),
            "requirements": bullet([req, "Use asyncio.sleep not time.sleep in async exercises"]),
            "constraints": bullet(["No real HTTP unless extension"]),
            "expected": bullet(["Documented timings"]),
            "edge_cases": bullet(["empty url list", "timeout shorter than sleep"]),
            "acceptance": bullet(["Runnable script or module"]),
            "mistakes": bullet(["Blocking sleep in async def", "forgetting await"]),
            "h1": "Blocking call inside async def blocks the event loop.",
        },
    )

print(
    f"Wrote {len(m00_specs)} m00, {len(m01_core)} m01, {len(arch_specs)} arch, "
    f"{len(test_specs)} test, {len(dbg_specs)} dbg, {len(m02_specs)} m02 readmes"
)
