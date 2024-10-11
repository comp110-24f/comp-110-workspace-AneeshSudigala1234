"""Wordle"""

__author__: str = "730744298"


def input_guess(secret_word_len: int) -> str:
    """Checks if user_input is the same length as the secret"""
    user_input: str = input(f"Enter a {secret_word_len} character word: ")
    # asks the user to input another word if the lengths don't match
    while len(user_input) != secret_word_len:
        new_input: str = input(f"That wasn't {secret_word_len} chars! Try again: ")
        user_input = new_input
    return str(user_input)


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Checks if char_guess is present within secret_word"""
    assert len(char_guess) == 1
    i: int = 0
    # returns true if the character is anywhere in the string of the secret word
    while i + 1 <= len(secret_word):
        if str(secret_word[i]) == str(char_guess):
            return True
            exit()
        else:
            i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Checks and returns a string of emojis"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    color_result: str = ""
    # checks if and where  character is on word, returns color
    # prints green if in same spot
    # yellow if elsewhere on the word
    # white if not on the word
    while i < len(guess):
        if guess[i] == secret[i]:
            color_result += GREEN_BOX
            i += 1
        elif contains_char(secret, guess[i]):
            color_result += YELLOW_BOX
            i += 1
        else:
            color_result += WHITE_BOX
            i += 1
    return str(color_result)


def main(secret: str) -> None:
    """Entrypoint of the program"""
    turns: int = 1
    win: bool = False
    while turns <= 6 and not win:
        # goes through each turn and receives user_input from input_guess function
        print(f"== Turn {turns}/6 ==")
        guess: str = input_guess(len(secret))
        # calls the emojified function to print out the images of colors
        emoji_str: str = emojified(secret, guess)
        print(emoji_str)
        # if the user input is the same as the secret word, the bool win is true
        if guess == secret:
            win = True
        else:
            turns += 1
    # user wins if bool=True and user loses if bool=False
    if win:
        print(f"You won in {turns}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
