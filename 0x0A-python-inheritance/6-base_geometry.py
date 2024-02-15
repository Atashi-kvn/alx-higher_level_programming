#!/usr/bin/python3
"""An empty class raising an error"""


class BaseGeometry:
    """A class with a public class area"""
    def area(self):
        """
        Calculate the area of the geometry.

        Raises:
            Exception: Indicates that the `area` method is not implemented.
        """
        raise Exception("area() is not implemented")
