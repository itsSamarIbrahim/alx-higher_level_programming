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

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
            value (int): The new size of the square.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the square's attributes based on
        the provided arguments and keyworded arguments.

        Args:
            *args: Variable length argument list.
            The order of arguments should be id, size, x, y.

            **kwargs: Arbitrary keyword arguments.
            Each key represents an attribute to be updated.
        """
        """ if args is not None and len(args) != 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Return the dictionary representation of the square.

        Returns
        -------
        dict
            a dictionary containing the id, size, x,
            and y attributes of the square
        """
        return {
           'id': self.id,
           'size': self.size,
           'x': self.x,
           'y': self.y
        }
