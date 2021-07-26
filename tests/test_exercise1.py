from scripts.exercise1 import prod
from scripts.exercise1 import fact_gen


def test_prod_returns_product_of_a_and_b():
    assert prod(8, 5) == 40


def test_fact_gen_returns_1factorial():
    my_gen = fact_gen()
    num = 1
    result = 0
    for i in range(num):
        result = next(my_gen)
    assert result == 1


def test_fact_gen_returns_2factorial():
    my_gen = fact_gen()
    num = 2
    result = 0
    for i in range(num):
        result = next(my_gen)
    assert result == 2
