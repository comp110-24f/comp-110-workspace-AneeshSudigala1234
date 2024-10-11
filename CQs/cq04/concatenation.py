"""Concatenation - Defines a function to combine two strings"""

__author__ = "Your Name"


def concat(str1: str, str2: str) -> str:
    """Combines two strings and returns it"""
    return str1 + str2


# Global variables
word1 = "happy"
word2 = "tuesday"

# Allows the function to be called only within this file
if __name__ == "__main__":
    print(concat(word1, word2))
