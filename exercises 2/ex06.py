"""Dictionary Utility Functions"""

__author__ = "730744298"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Switches keys and values of a dictionary"""
    inverted_dict: dict[str, str] = {}
    # Loop through dictionary
    for key in input_dict:
        value: str = input_dict[key]
        if value in inverted_dict:
            raise KeyError(f"KeyError: Duplicate Key Found: '{value}'")
        inverted_dict[value] = key
    return inverted_dict


def favorite_color(input_dict: dict[str, str]) -> str:
    """Finds the most frequent color"""
    color_count: dict[str, int] = {}
    # Loop through dictionary
    for name in input_dict:
        color: str = input_dict[name]
        # Checks if the color exists is the variable
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    # Finds the most frequent color
    max_count = 0
    most_popular: str = ""
    for color in input_dict.values():
        if color_count[color] > max_count:
            max_count = color_count[color]
            most_popular = color
        elif color_count[color] == max_count and most_popular is None:
            most_popular = color

    return most_popular


def count(input_list: list[str]) -> dict[str, int]:
    """Finds the frequency of a value in a list"""
    dict_count: dict[str, int] = {}
    # Loops through list
    for i in input_list:
        # Checks if the value exists in the dictionary
        if i in dict_count:
            dict_count[i] += 1
        else:
            dict_count[i] = 1
    return dict_count


def alphabetizer(input_list: list[str]) -> dict[str, list[str]]:
    """Makes a dictionary where keys are letters and values are words that start with that letter"""
    return_dict: dict[str, list[str]] = {}
    # Loops through dictionary
    for word in input_list:
        # Make lowercase to make searching easier
        first_letter = word[0].lower()
        if first_letter in return_dict:
            return_dict[first_letter].append(word)
        else:
            return_dict[first_letter] = [word]
    return return_dict


def update_attendance(input_dict: dict[str, list[str]], day: str, student: str) -> None:
    """Puts new attendance information in a dictionary"""
    # Finds if informaiton exists already
    if day in input_dict:
        if student not in input_dict[day]:
            input_dict[day].append(student)
    else:
        input_dict[day] = [student]
    return None
