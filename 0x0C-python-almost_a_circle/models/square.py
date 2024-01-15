#!/usr/bin/python3
"""
model-2 Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class representing a square, inheriting from the Rectangle class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
        size (int): The size of the square.
        x (int, optional):
        The x-coordinate of the square's position. Defaults to 0.

        y (int, optional):
        The y-coordinate of the square's position. Defaults to 0.

        id (int, optional): The identifier of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the Square instance.

        Returns:
        str: A string representing the Square instance.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
