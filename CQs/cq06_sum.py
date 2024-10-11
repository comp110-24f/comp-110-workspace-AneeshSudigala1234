"""Summing the elements of a list using different loops"""

__author__ = "730744298"


def w_sum(vals: list[float]) -> float:
    """Sums the elements of a list using a while loop"""
    sum: float = 0.0
    index: int = 0
    while index < len(vals):
        sum += vals[index]
        index += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Sums the elements of a list using a for loop"""
    sum: float = 0.0
    for item in vals:
        sum += item
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Sums the elements of a list using a for loop and range function"""
    sum: float = 0.0
    for item in range(len(vals)):
        sum += vals[item]
    return sum
