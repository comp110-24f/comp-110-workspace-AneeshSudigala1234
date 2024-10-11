"""Coordinates - Defines a function that prints coordinates from two strings"""

__author__ = "Your Name"


def get_coords(xs: str, ys: str) -> None:
    """Prints formatted coordinates from two strings"""
    index = 0
    while index < len(xs):
        count = 0
        while count < len(ys):
            print("(" + xs[index] + "," + ys[count] + ")")
            count += 1
        index += 1
