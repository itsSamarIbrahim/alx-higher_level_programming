#!/usr/bin/python3

def lookup(obj):
    """
    This function takes an object as input and returns a list of
    valid attributes and methods for that object.

    Args:
    obj: Any Python object.

    Returns:
    A list of strings representing the valid attributes
    and methods of the input object.
    """
    return dir(obj)
