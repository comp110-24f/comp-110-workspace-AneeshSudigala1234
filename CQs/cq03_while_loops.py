"""While Loops Challenge Question"""

__author__ = "730744298"


# Function that counts the instances of a speicifc character in a phrase
def num_instances(phrase: str, search_char: str) -> int:
    # Local variable that keeps track of instances
    count: int = 0
    # Local variable that keeps track of sequencing
    index: int = 0
    # While loop that iterates through the phrase
    while index < len(phrase):
        # If loop that checks if the specific character exists
        if phrase[index] == search_char:
            # Increase count if the specific character exists
            count += 1
        # Increase the index if the specific character exists or not
        index += 1
    # Return the instances of the specific character in a phrase
    return count
