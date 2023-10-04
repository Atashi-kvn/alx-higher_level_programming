#!/usr/bin/python3

class Rectangle():
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        while True:
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            break
        self.__height = value

    @property
    def width(self):
        """
        getting width
        """
        return self.__height
    @width.setter
    def width(self, value):
        while True:
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            break
        self.__width = value
