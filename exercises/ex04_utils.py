"""EX04 - List Utility Functions"""

__author__ = "730744298"


def all(list: list[int], int: int) -> bool:
    """Checks if each item in 'list' is equal to 'int'"""
    while len(list) > 0:
        i = list.pop()
        if i != int:
            return False
    return True


def max(list: list[int]) -> int:
    """Finds the largest iteam in 'list'"""
    # Error if length of 'list' is 0
    if len(list) == 0:
        raise ValueError("max() arg is an empty List")
    # Code if length of 'list' is not 0
    else:
        max: int = 0
        while len(list) > 0:
            i = list.pop()
            if i > max:
                max = i
        return max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checks if 'list1' is equal to 'list2'"""
    # Loops through 'list2' inside of the loop of 'list1'
    while len(list1) > 0:
        i = list1.pop()
        while len(list2) > 0:
            j = list2.pop()
            if i != j:
                return False
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    """Combines 'list1' and 'list2'"""
    list1 += list2
