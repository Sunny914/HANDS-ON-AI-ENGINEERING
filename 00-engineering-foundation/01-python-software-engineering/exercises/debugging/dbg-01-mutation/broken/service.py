"""Deliberately buggy — dbg-01."""

_CACHE = {"items": []}


class CatalogService:
    def list_items(self):
        return _CACHE["items"]

    def add_item(self, name):
        item = {"name": name}
        _CACHE["items"].append(item)
        return item

    def clear(self):
        _CACHE["items"] = _CACHE["items"]
