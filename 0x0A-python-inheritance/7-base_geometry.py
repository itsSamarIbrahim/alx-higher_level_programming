#!/usr/bin/python3
"""

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

    def integer_validator(self, name, value):
        """
        Validate if the given value is an integer and greater than 0.

        Args:
        name (str): The name of the value being validated.
        value (int): The value to be validated.

        Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is not greater than 0.
        """
        if type(value) != int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
