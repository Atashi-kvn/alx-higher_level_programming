#!/usr/bin/python3

class Square:
    """
    The class Square has the following attribute:
                 size
         Protected from input
         """
    def --init--(self, size=0):
        """
        initialization of the function square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be great than 0")
        else:
            self.__size = size

    def area(self):
        """
        will calculate the area of the square
        """
        return self.__size ** 2
