from scripts.exercise1 import prod
from scripts.exercise1 import fact_gen


def test_prod_returns_product_of_a_and_b():
    assert prod(8, 5) == 40
