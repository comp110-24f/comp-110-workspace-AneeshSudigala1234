"""File to Implement List Utility Functions"""

__author__ = "730744298"


def only_evens(input_lst: list[int]) -> list[int]:
    """Makes a new list with all the even items"""
    even_lst: list[int] = []
    # Loops through all items
    for i in input_lst:
        # Checks if item is even
        if i % 2 == 0:
            even_lst.append(i)
    return even_lst


def sub(input_lst: list[int], start_index: int, end_index: int) -> list[int]:
    """Returns a new list from a specific index to another index"""
    sub_lst: list[int] = []
    # Checks for Edge Cases
    if start_index < 0:
        start_index = 0
    if end_index > len(input_lst) - 1:
        end_index = len(input_lst)
    if len(input_lst) == 0 or start_index >= len(input_lst) or end_index <= 0:
        return []
    # Code to return new list
    for i in range(start_index, end_index):
        sub_lst.append(input_lst[i])
    return sub_lst


def add_at_index(lst, element, index) -> None:
    """Adds an integer at a specific index"""
    # Checks for wrong input
    if index < 0 or index > len(lst):
        raise IndexError("Index is out of bounds for the input list")
    # Expands list for more space
    lst.append(None)
    for i in range(len(lst) - 1, index, -1):
        lst[i] = lst[i - 1]
    lst[index] = element
