"""CQ07 - Unit Tests for find_max.py"""

__author__ = "730744298"

from find_max import find_and_remove_max


def test_return_largest_value() -> None:
    """Makre sure function returns the expected largest value"""
    input_list: list[int] = [4, 7, 2, 7, 5, 7, 1]
    expected_value: int = 7
    result: int = find_and_remove_max(input_list)
    assert result == expected_value


def test_input_list_mutation() -> None:
    """Make sure function mutates the input list in the expected way"""
    input_list: list[int] = [4, 7, 2, 7, 5, 7, 1]
    find_and_remove_max(input_list)
    expected_list: list[int] = [4, 2, 5, 1]
    assert input_list == expected_list


def test_empty_list() -> None:
    """Make sure function returns -1 for an empty list"""
    input_list: list[int] = []
    expected_value: int = -1
    result: int = find_and_remove_max(input_list)
    assert result == expected_value
