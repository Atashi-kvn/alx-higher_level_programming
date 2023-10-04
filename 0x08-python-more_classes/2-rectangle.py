#!/usr/bin/python3

class Rectangle():
    def __int__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        #getting hieght
        return self.__height
    @height.setter
    def height(self, value):
        while True:
            if not isinstance(value, int):
                raise TypeError("Hieght must be an integer")
            elif value < 0:
                raise ValueError("Height must be >= 0")
                break
        self.__heiht = value

    @property
    def width(self):
        #getting width
        return self.__width

    @width.setter
    def width(self, value):
        while True:
            if not isinstance(value, int):
                raise TypeError("Width must be an integer")
            elif value < 0:
                raise ValueError("Width must be >= 0")
            break
        self.__width = value

    def area(self):
        return(self.width * self.height)

    def perimeter(self):
        #Doing the perimeter of rectangle
        if self.width == 0 or self.height == 0:
            return 0
        return((2 * self.width) + (2 * self.height))

