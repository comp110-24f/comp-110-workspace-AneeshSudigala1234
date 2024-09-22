"""EX02 - Chardle"""

__author__ = "730744298"


def input_word() -> str:
    """Asks user for a word"""
    user_input: str = input("Enter a 5-character word: ")  # Asks for a word
    if len(user_input) == 5:  # Checks length of the word
        return user_input  # Returns the word
    else:
        print("Error: Word must contain 5 characters.")  # Prints an error message
        exit()


def input_letter() -> str:
    """Asks user for a letter"""
    user_input: str = input("Enter a single character: ")  # Asks for a letter
    if len(user_input) == 1:  # Checks length of the letter
        return user_input  # Returns the letter
    else:
        print("Error: Character must be a single character.")  # Prints an error message
        exit()


def contains_char(word: str, letter: str) -> None:
    """Checks if the letter is in the word"""
    print(
        "Searching for " + letter + " in " + word
    )  # Prints what the function is searching for
    index: int = 0  # Variable that keeps track of the indexing
    count: int = 0  # Variable that keeps track of the amount of letters found
    while index < len(word):  # Loops through the word
        if (
            word[index] == letter
        ):  # Checks if the word at that index is the same as the letter
            print(
                letter + " found at index " + str(index)
            )  # Prints the index the letter was found at
            count = count + 1
        index = index + 1  # Increases index by 1
    if count > 1:  # Checks if there is more than 1 letter found in word
        print(str(count) + " instances of " + letter + " found in " + word)
    elif count == 1:  # Checks if there is 1 letter found in word
        print(str(count) + " instance of " + letter + " found in " + word)
    else:  # Assumes there are no letters found in word
        print("No instances of " + letter + " found in " + word)


def main() -> None:
    """Main function of the program"""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
