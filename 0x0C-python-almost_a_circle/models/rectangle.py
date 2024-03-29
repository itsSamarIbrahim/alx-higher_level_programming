#!/usr/bin/python3
"""
model Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    A class to represent a rectangle.

    Attributes
    ----------
    width : int
        The width of the rectangle.
    height : int
        The height of the rectangle.
    x : int, optional
        The x-coordinate of the rectangle's position.
    y : int, optional
        The y-coordinate of the rectangle's position.
    id : int, optional
        The unique identifier of the rectangle.

    Methods
    -------
    __init__(width, height, x=0, y=0, id=None)
        Constructs all the necessary attributes for the rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructs all the necessary attributes for the rectangle.

        Parameters
        ----------
        width : int
            The width of the rectangle.
        height : int
            The height of the rectangle.
        x : int, optional
            The x-coordinate of the rectangle's position.
        y : int, optional
            The y-coordinate of the rectangle's position.
        id : int, optional
            The unique identifier of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """int: The x-coordinate of the rectangle's position."""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """int: The y-coordinate of the rectangle's position."""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
        int: The area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Display the rectangle as a series of '#' characters
        based on its width and height at the specified position.
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + '#' * self.width)

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.

        Returns:
        - str: A string representation of the Rectangle instance.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} \
- {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
        Update the Rectangle attributes based on the arguments provided.

        Args:
            *args: Variable length argument list.
            If provided, the arguments are assigned to the corresponding
            attributes in the order: id, width, height, x, y.

            **kwargs: Arbitrary keyword arguments.
            If provided, the key-value pairs are assigned
            to the corresponding attributes.
        """
        if args is not None and len(args) != 0:
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
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the rectangle."""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
