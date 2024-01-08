#!/usr/bin/python3
"""
Module 4-inherits_from.py
a function that returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class;
otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Check if the object `obj` is an instance of a subclass of `a_class`.

    Args:
    obj: The object to be checked.
    a_class: The class to check against.

    Returns:
    True if `obj` is an instance of a subclass of `a_class`, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
