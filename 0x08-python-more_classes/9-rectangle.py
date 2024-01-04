#!/usr/bin/python3
"""
a Rectangle class that defines a rectangle:
"""


class Rectangle:
    """A class representing a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    number_of_instances = 0
    """int: Represents the number of
            Rectangle instances that have been created."""

    print_symbol = '#'
    """str: The symbol used for printing the rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle with the given width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

       Args:
           value (int): The width value to be set.

       Raises:
           TypeError: If the width is not an integer.
           ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The height value to be set.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle (2 * width + 2 * height).
            If either the height or width is 0, the perimeter is 0.
        """
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """Return a string representation of the rectangle.

        Returns:
            str: A string representing the rectangle
                     as a series of '#' characters.
                 If either the height or width is 0,
                     an empty string is returned.
        """
        if self.width == 0 or self.height == 0:
            return ""
        rect = ""
        for i in range(self.height):
            rect += str(self.print_symbol) * self.width
            if i != self.height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        """Return a string representation of the rectangle for debugging.

        Returns:
            str: A string representing the rectangle
                 in the format "Rectangle(width, height)".
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Destructor method for the Rectangle class.

        Prints a farewell message when the object is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare two rectangles and return
           the one with the greater or equal area.

        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.

        Returns:
            Rectangle: The rectangle with the greater or equal area.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Create a square using the provided size.

        Args:
            cls: The class itself.
            size (int): The size of the square.

        Returns:
            Rectangle: A new instance of Rectangle representing a square.

        """
        return cls(size, size)
