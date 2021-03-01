import pytest

from coin_change.solution_sebastian import Solution as sebastian_solution


@pytest.mark.parametrize("solution_class", [sebastian_solution])
def test_example1(solution_class):
    coins = [1, 2, 5]
    amount = 11
    sol = solution_class()
    assert sol.coinChange(coins, amount) == 3


@pytest.mark.parametrize("solution_class", [sebastian_solution])
def test_example2(solution_class):
    coins = [1]
    amount = 11
    sol = solution_class()
    assert sol.coinChange(coins, amount) == 11


@pytest.mark.parametrize("solution_class", [sebastian_solution])
def test_example3(solution_class):
    coins = [2]
    amount = 11
    sol = solution_class()
    assert sol.coinChange(coins, amount) == -1


@pytest.mark.parametrize("solution_class", [sebastian_solution])
def test_example4(solution_class):
    coins = [2]
    amount = 0
    sol = solution_class()
    assert sol.coinChange(coins, amount) == 0


@pytest.mark.parametrize("solution_class", [sebastian_solution])
def test_example5(solution_class):
    coins = [27]
    amount = 2
    sol = solution_class()
    assert sol.coinChange(coins, amount) == -1


@pytest.mark.parametrize("solution_class", [sebastian_solution])
def test_example5(solution_class):
    coins = [186, 419, 83, 408]
    amount = 6249
    sol = solution_class()
    assert sol.coinChange(coins, amount) == 20
