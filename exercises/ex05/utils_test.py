"Testing for utils.py!"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_a() -> None:
    """Testing only_evens with all odds (edge case)."""
    arg: list[int] = [1, 7, 13, 9]
    assert only_evens(arg) == []


def test_only_evens_b() -> None:
    """Testing only_evens with repeating evens and 0 (use case)."""
    arg: list[int] = [1, 0, 2, 2, 2]
    assert only_evens(arg) == [0, 2, 2, 2]


def test_sub_a() -> None:
    """Testing sub with empty given list (edge case)."""
    arg: list[int] = []
    assert sub(arg, 2, 3) == []


def test_sub_b() -> None:
    """Testing sub with expected use (use case)."""
    arg: list[int] = [1, 0, 2, 2, 2]
    assert sub(arg, 1, 3) == [0, 2]


def test_concat_a() -> None:
    """Testing concat where one list is empty (edge case)."""
    arg1: list[int] = []
    arg2: list[int] = [1, 0, 2, 2, 2]
    assert concat(arg1, arg2) == [1, 0, 2, 2, 2]


def test_concat_b() -> None:
    """Testing concat with expected use (use case)."""
    arg1: list[int] = [2, 4, 5]
    arg2: list[int] = [6, 7, 9]
    assert concat(arg1, arg2) == [2, 4, 5, 6, 7, 9]
