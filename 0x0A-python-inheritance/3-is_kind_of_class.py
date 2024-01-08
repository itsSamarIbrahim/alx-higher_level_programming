#!/usr/bin/python3
"""
Module: is_kind_of_class
a function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the given object is an instance of
    the specified class or a subclass of it.

    Args:
    obj: Any Python object.
    a_class: A Python class.

    Returns:
    True if the object is an instance of the specified class
    or a subclass of it, False otherwise.
    """
    return isinstance(obj, a_class)
