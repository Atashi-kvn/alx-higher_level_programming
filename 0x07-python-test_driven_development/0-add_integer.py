#!/usr/bin/python3
"""Addition of integers"""


def add_integer(a, b=98):
    "adding 2 integers"
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
