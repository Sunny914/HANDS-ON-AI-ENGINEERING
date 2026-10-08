"""Deliberately buggy — dbg-04."""


def parse_amount(raw):
    return raw + 0


def total(rows):
    return sum(parse_amount(r["amount"]) for r in rows)
