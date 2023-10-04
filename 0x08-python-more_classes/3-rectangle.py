#!/usr/bin/python3

class Rectangle():

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        """
        To provide a string when str() or print() is called
        """
        string = ""
        if self.width == 0 or self.height == 0:
            return string

        for i in range(0, self.height):
            for j in range(0, self.width):
                string += '#'
            if i != self.height - 1:
                string += '\n'
        return string

    @property
    def height(self):
        """ getter for height property """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height property """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """ getter for width property """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width property """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """ gets the area of rectangle instance """
        return (self.width * self.height)

    def perimeter(self):
        """ gets the perimeter of a rectangle instance """
        if self.width == 0 or self.height == 0:
            return 0
        return ((2 * self.width) + (2 * self.height))
