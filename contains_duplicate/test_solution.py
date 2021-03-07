import pytest

from contains_duplicate.solution_sebastian import Solution as sebastian_solution


@pytest.mark.parametrize("solution_class", [sebastian_solution])
def test_example1(solution_class):
    nums = [7, 1, 5, 3, 6, 4]
    sol = solution_class()
    assert sol.containsDuplicate(nums) == False


@pytest.mark.parametrize("solution_class", [sebastian_solution])
def test_example2(solution_class):
    nums = [7, 6, 4, 3, 7, 1]
    sol = solution_class()
    assert sol.containsDuplicate(nums) == True
