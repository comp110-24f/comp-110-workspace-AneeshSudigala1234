"""File to Define Unit Tests"""

__author__ = "730744298"


import pytest
from exercises.ex05.utils import only_evens, sub, add_at_index

# Test for only_evens


def test_only_evens1() -> None:
    """Test 1"""
    input_list: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(input_list) == [2, 4, 6]


def test_only_evens2() -> None:
    """Test 2"""
    input_list: list[int] = [7, 8, 9, 10, 11, 12]
    assert only_evens(input_list) == [8, 10, 12]


def test_only_evens_edge_case3() -> None:
    """Test 3 (Edge Case)"""
    input_list: list[int] = [1, 5, 3]
    assert only_evens(input_list) == []


# Test for sub


def test_sub1() -> None:
    """Test 1"""
    input_list: list[int] = [10, 20, 30, 40]
    assert sub(input_list, 1, 3) == [20, 30]


def test_sub2() -> None:
    """Test 2"""
    input_list: list[int] = [1, 2, 3, 4]
    assert sub(input_list, 1, 3) == [2, 3]


def test_sub3_edge_case() -> None:
    """Test 3 (Edge Case)"""
    input_list: list[int] = []
    assert sub(input_list, 1, 3) == []


# Test for add_at_index


def test_add_at_index1() -> None:
    """Test 1"""
    input_list: list[int] = [1, 2, 3, 5]
    add_at_index(input_list, 4, 3)
    assert input_list == [1, 2, 3, 4, 5]


def test_add_at_index2() -> None:
    """Test 2"""
    input_list: list[int] = [6, 7, 8, 10]
    add_at_index(input_list, 9, 3)
    assert input_list == [6, 7, 8, 9, 10]


def test_add_at_index_raises_indexerror() -> None:
    """Test 3 (Edge Case)"""
    input_list: list[int] = []
    with pytest.raises(IndexError):
        add_at_index(input_list, 1, 1)
