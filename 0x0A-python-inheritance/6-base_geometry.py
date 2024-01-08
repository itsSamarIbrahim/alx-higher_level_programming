#!/usr/bin/python3
"""
Module: 6-base_geometry
a class BaseGeometry
Public instance method: def area(self): that raises an Exception
with the message area() is not implemented
"""


class BaseGeometry:
    """
    A base class for geometric shapes.

    Methods:
    area(self): Raises an exception indicating that
                the area calculation is not implemented.
    """
    def area(self):
        """
        This method raises an exception to indicate that
        the area calculation is not implemented for this geometric shape.

        Raises:
        Exception: Always raises an exception
        with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")
