"""Visualize - Runs the concatenation and coordinates functions in a new file"""

__author__ = "Your Name"

# Imports both functions from the two different files
from CQs.cq04.concatenation import concat
from CQs.cq04.coordinates import get_coords

# Global variables
x = "123"
y = "abc"

# Combination of string x and string y
print(concat(x, y))

# Print coordinate pairs of string x and string y
get_coords(x, y)
