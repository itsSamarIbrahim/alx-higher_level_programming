#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Returns the sum of two integers.

    Args:
    a (int or float): The first number.
    b (int or float): The second number. Defaults to 98.

    Returns:
    int: The sum of a and b.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
