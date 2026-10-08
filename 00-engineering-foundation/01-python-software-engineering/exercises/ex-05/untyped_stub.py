# RESPONSIBILITY: Specification only — implement typed code in inventory.py
# TODO: Implement the API described below with full type hints.
#
# INPUT: Product records with id (str), name (str), quantity (int), price (float).
#
# REQUIRED FUNCTIONS (signatures are conceptual — you choose exact typing style):
#   get_low_stock(products, threshold: int) -> list of products where quantity <= threshold
#   inventory_value(products) -> total float value (sum quantity * price)
#   apply_discount(products, percent: float) -> NEW list with discounted prices (do not mutate input)
#
# OUTPUT: Typed functions importable by tests you may add later.
#
# EDGE CASE: empty list, percent 0 or 100, negative quantity should raise ValueError
#
# HINT: See HINTS.md ex-05 and module README.
