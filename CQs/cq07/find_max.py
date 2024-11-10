"""CQ07 - Find and Remove the Largest Integer"""

__author__ = "730744298"


def find_and_remove_max(input_list: list[int]) -> int:
    """Finds and removes the largest integer from a list and returns it"""
    # Returns -1 if the list is empty
    if len(input_list) == 0:
        return -1
    else:
        # Finds largest integer
        largest_int: int = input_list[0]
        for i in input_list:
            if i > largest_int:
                largest_int = i
        # Removes the largest integer
        index = 0
        while index < len(input_list):
            if input_list[index] == largest_int:
                input_list.pop(index)
            else:
                index += 1
        # Returns largest integer
        return largest_int
