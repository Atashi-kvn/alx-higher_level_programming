#!/usr/bin/python3


class Rectangle():

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        
        if self.width == 0 or self.height == 0:
            return ""

        string = ""
        for i in range(0, self.height):
            for j in range(0, self.width):
                string += str(self.print_symbol)
            if i != self.height - 1:
                string += '\n'
        return string

    def __repr__(self):
        """ For object when repr() is called
        """
        string = "Rectangle("
        string += str(self.width)
        string += ", " + str(self.height) + ")"
        return string

    def __del__(self):
        """ For when a rectangle instance is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def height(self):
        """ for getting height property """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height property """
        while True:
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
                break
                
            self.__height = value

    @property
    def width(self):
        """ getter for width property """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width property """
        while True:
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
                break
                
            self.__width = value

    def area(self):
        """ gets the area of rectangle instance """
        return (self.width * self.height)

    def perimeter(self):
        """ gets the perimeter of a rectangle instance """
        if self.width == 0 or self.height == 0:
            return 0
        return ((2 * self.width) + (2 * self.height))

    def bigger_or_equal(rect_1, rect_2):
        """ returns biggest rectangle based on area """
        
        while True:
            if not isinstance(rect_1, Rectangle):
                raise TypeError("rect_1 must be an instance of Rectangle")
            if not isinstance(rect_2, Rectangle):
                raise TypeError("rect_2 must be an instance of Rectangle")
            if rect_2.area() > rect_1.area():
                return rect_2
                break
                
            return rect_1
