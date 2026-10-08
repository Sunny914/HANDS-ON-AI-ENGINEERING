"""Deliberately buggy — ex-19."""

import json


def load_settings():
    with open("data/settings.json") as f:
        return json.load(f)


if __name__ == "__main__":
    print(load_settings())
