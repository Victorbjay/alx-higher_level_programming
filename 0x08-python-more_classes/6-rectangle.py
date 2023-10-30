#!/usr/bin/python3
"""6-rectangle Module.

This module is based on the `5-rectangle` module. \
    As an improvement, it keeps track of number of rectangle instances.
"""


class Rectangle:
    """Rectangle Class.

    This class defines a Rectangle.
    """

    number_of_instances = 0
    """This keeps track of all instances of Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialize Instance.

        This method initializes a rectangle instance.

        Args:
            width(int): width of rectangle.
            height(int): height of rectangle.
        """
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Area of the Rectangle.

        This calculates the area of the rectangle.

        Return:
            the area.
        """
        return self.width * self.height

    def perimeter(self):
        """Perimeter of the Rectangle.

        This calculates the perimeter of the rectangle.

        Return:
            the perimeter or zero if either width of height is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Representation of the rectangle.

        This prints # according to the perimeter of the rectangle.
        """
        if self.perimeter() > 0:
            for i in range(self.height - 1):
                print("#" * self.width)
            print("#" * self.width, end="")
        return ""

    def __repr__(self):
        """Formal representation of the rectangle.

        This returns a string representation of the rectangle
        to be able to recreate a new instance by using eval()
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Deconstructor.

        This is the deconstructor for a Rectangle object.
        It is called just before the instance is being deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
