#!/usr/bin/python3

"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        number_of_instances += 1
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of the rectangle"""

        area = self.__width * self.__height
        return area

    def perimeter(self):
        """Return the perimeter of the Rectangle."""

        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """returns the printable represntation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        rec_str = ""
        for _ in range(self.__height):
            rec_str += "#" * self.__width + "\n"
        return rec_str.rstrip()

    def __repr__(self):
        """Return a string representation that can recreate the object."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Perform cleanup when an instance of Rectangle is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
#!/usr/bin/python3

"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        number_of_instances += 1
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of the rectangle"""

        area = self.__width * self.__height
        return area

    def perimeter(self):
        """Return the perimeter of the Rectangle."""

        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """returns the printable represntation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        rec_str = ""
        for _ in range(self.__height):
            rec_str += "#" * self.__width + "\n"
        return rec_str.rstrip()

    def __repr__(self):
        """Return a string representation that can recreate the object."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Perform cleanup when an instance of Rectangle is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
#!/usr/bin/python3

"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        number_of_instances += 1
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of the rectangle"""

        area = self.__width * self.__height
        return area

    def perimeter(self):
        """Return the perimeter of the Rectangle."""

        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """returns the printable represntation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        rec_str = ""
        for _ in range(self.__height):
            rec_str += "#" * self.__width + "\n"
        return rec_str.rstrip()

    def __repr__(self):
        """Return a string representation that can recreate the object."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Perform cleanup when an instance of Rectangle is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
#!/usr/bin/python3

"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        number_of_instances += 1
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of the rectangle"""

        area = self.__width * self.__height
        return area

    def perimeter(self):
        """Return the perimeter of the Rectangle."""

        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """returns the printable represntation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        rec_str = ""
        for _ in range(self.__height):
            rec_str += "#" * self.__width + "\n"
        return rec_str.rstrip()

    def __repr__(self):
        """Return a string representation that can recreate the object."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Perform cleanup when an instance of Rectangle is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
