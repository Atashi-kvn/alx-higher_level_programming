#!/usr/bin/python3

class Rectangle():
    def __int__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        for i in range(0, self.width):
            for k in range(0, self.width):
                string += "#"
            if i != self.height - 1:
                string += "\n"
        return string
    def __repr__(self):
        """
        to return a string that represents the objects state
        """
        string = "Rectangle("
        string += str(self.width)
        string += ", " + str(self.height) + ")"
        return string
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
        
        return self.__width

    @width.setter
    def width(self, value):
    
        Try:
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

