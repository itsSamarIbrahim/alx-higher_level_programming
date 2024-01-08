#!/usr/bin/python3
"""
Module: 2-is_same_class
a function that returns True if the object is exactly
an instance of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Check if the given object is an instance of the specified class.

    Args:
    obj: Any Python object.
    a_class: A Python class.

    Returns:
    True if the object is an instance of the specified class, False otherwise.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
