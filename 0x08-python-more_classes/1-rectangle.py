#!/usr/bin/python3
"""Rectangle Module.

This script defines a Rectangle.
"""


class Rectangle:
    """Rectangle Class.

    This class defines a Rectangle.
    """

    def __init__(self, width=0, height=0):
        """Initialize Instance.

        This method initializes a rectangle instance.

        Args:
            width(int): width of rectangle.
            height(int): height of rectangle.
        """
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """
        Getter method for rectangle height.

        Returns:
        int: The height of the rectangle.
        """
        return self.__height

    @property
    def width(self):
        """
        Getter method for rectangle width.

        Returns:
        int: The width of the rectangle.
        """
        return self.__width

    @height.setter
    def height(self, value):
        """
        Setter method for rectangle height.

        Args:
            value(int): new height

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is < 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @width.setter
    def width(self, value):
        """
        Setter method for rectangle width.

        Args:
            value(int): new width

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is < 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
