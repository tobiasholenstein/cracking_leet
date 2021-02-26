import pytest

from minimum_window_substring.solution_sebastian import Solution as sebastian_solution


@pytest.mark.parametrize("solution_class", [sebastian_solution])
def test_example1(solution_class):
    s = "ADOBECODEBANC"
    t = "ABC"
    sol = solution_class()
    assert sol.minWindow(s, t) == "BANC"


@pytest.mark.parametrize("solution_class", [sebastian_solution])
def test_example2(solution_class):
    s = "a"
    t = "a"
    sol = solution_class()
    assert sol.minWindow(s, t) == "a"


@pytest.mark.parametrize("solution_class", [sebastian_solution])
def test_empty_sol(solution_class):
    s = "abcdefghijk"
    t = "al"
    sol = solution_class()
    assert sol.minWindow(s, t) == ""


@pytest.mark.parametrize("solution_class", [sebastian_solution])
def test_t_non_unique(solution_class):
    s = "abcdefghiajk"
    t = "aa"
    sol = solution_class()
    assert sol.minWindow(s, t) == "abcdefghia"
