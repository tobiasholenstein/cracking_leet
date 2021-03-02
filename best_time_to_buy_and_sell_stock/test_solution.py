import pytest

from best_time_to_buy_and_sell_stock.solution_sebastian import Solution as sebastian_solution


@pytest.mark.parametrize("solution_class", [sebastian_solution])
def test_example1(solution_class):
    prices = [7, 1, 5, 3, 6, 4]
    sol = solution_class()
    assert sol.maxProfit(prices) == 5


@pytest.mark.parametrize("solution_class", [sebastian_solution])
def test_example2(solution_class):
    prices = [7, 6, 4, 3, 1]
    sol = solution_class()
    assert sol.maxProfit(prices) == 0
