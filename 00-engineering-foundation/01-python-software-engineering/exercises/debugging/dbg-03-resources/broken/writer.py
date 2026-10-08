"""Deliberately buggy — dbg-03."""


def write_lines(path, lines):
    f = open(path, "w", encoding="utf-8")
    for line in lines:
        if "ERROR" in line:
            raise ValueError("refusing error line")
        f.write(line + "\n")
    f.close()
