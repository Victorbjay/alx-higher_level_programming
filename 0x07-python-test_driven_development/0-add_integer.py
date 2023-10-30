#!/usr/bin/python3
"""Add Integer Module.

This module performs addition on integers.
It contains only one function that performs addition.
"""


def add_integer(a, b=98):
    """Addition Function.

    This function adds 2 integers together.

    Args:
        a (int): The first integer.
        b (int): The second Integer.

    Returns:
        int: The sum of a and b.
    """
    # ensuring the parameters are either of type int or float
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError("a must be an integer or b must be an integer")

    # typecasting the integers incase any is a float
    a = int(a)
    b = int(b)

    return (a + b)
