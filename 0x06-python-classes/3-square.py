#!/usr/bin/python3

class Square:
    """
    The class Square has attributes:
                 size
         Protected from input
         """
    def --init--(self, size=0):
        """
        initialization function for our square clasee
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        calculates the area of the square
        """
        return self.__size ** 2
