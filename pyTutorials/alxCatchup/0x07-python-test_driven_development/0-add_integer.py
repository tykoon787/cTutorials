#!/usr/bin/python3
"""

add_integer:
    Checks if args are int
    Returns sum of args
"""


def add_integer(a, b=98):
    """Function to Add an Integer"""
    if (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        a = int(a)
        b = int(b)
        return a + b
    else:
        raise TypeError("a must be an integer or b must be an integer")

