from service import CatalogService


def main():
    a = CatalogService()
    b = CatalogService()
    a.add_item("one")
    b.add_item("two")
    print("a", a.list_items())
    print("b", b.list_items())


if __name__ == "__main__":
    main()
