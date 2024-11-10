"""EX04 - List Utility Functions"""

__author__ = "730744298"


def all(lst: list[int], num: int) -> bool:
    """Every item in a list should be equal to an integer"""
    i: int = 0
    count: int = 0
    # Returns False if list is empty
    if len(lst) == 0:
        return False
    # Continues with code if list contains items
    else:
        # Loops through list
        while i < len(lst):
            if lst[i] == num:
                count += 1
            i += 1
    # Checks if everything is met
    if count == len(lst):
        return True
    else:
        return False


def max(lst: list[int]) -> int:
    """Finds the largest item in a list"""
    # Raises error is list is empty
    if len(lst) == 0:
        raise ValueError("max() arg is an empty List")
        exit()
    # Continues with code if list contains items
    else:
        # Declares variables
        current_num: int = 0
        greatest_num: int = lst[current_num]
        # Loops through list
        while current_num < len(lst) - 1:
            if lst[current_num + 1] > greatest_num:
                greatest_num = lst[current_num + 1]
            current_num += 1
        return greatest_num


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checks if both lists are the same"""
    i: int = 0
    # Returns False if both lists are not the same length
    if len(list1) != len(list2):
        return False
    # Continues with code if both lists are the same length
    else:
        while i < len(list1):
            if list1[i] != list2[i]:
                return False
            i += 1
        return True


def extend(list1: list[int], list2: list[int]) -> None:
    """Adds both lists together"""
    i: int = 0
    while i < len(list2):
        # Adds each item of the second list to the first list
        list1.append(list2[i])
        i += 1
    return None
