"""Mutating Functions"""

__author__ = "730744298"


def manual_append(list: list[int], int: int) -> None:
    """Adds an integer to the end of the list"""
    list.append(int)


def double(list: list[int]) -> None:
    """Multiplied each item in the list by 2"""
    index: int = 0
    while index < len(list):
        list[index] = list[index] * 2
        index += 1


# Create lists
list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
# Calls double
double(list_2)
# Print output
print(list_1)
print(list_2)
