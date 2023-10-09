Task 0: Lookup

In this task, you need to write a function called lookup(obj) that returns the list of available attributes and methods of an object. You should not import any modules for this task. The function should return a list of object attributes and methods.
Task 1: My List

Task 1 involves creating a class called MyList that inherits from the built-in list class. This class should have a method print_sorted(self) that prints the list sorted in ascending order. You can assume that all elements in the list will be integers.
Task 2: Exact Same Class

In Task 2, you are required to write a function is_same_class(obj, a_class) that checks if an object is an instance of the specified class. If it is, the function should return True; otherwise, it should return False. You should not import any modules for this task.
Task 3: Same Class or Inherit From

Task 3 involves writing a function is_kind_of_class(obj, a_class) that checks if an object is an instance of, or inherits from, the specified class. If it is, the function should return True; otherwise, it should return False. You should not import any modules for this task.
Task 4: Only Subclass Of

In Task 4, you need to write a function inherits_from(obj, a_class) that checks if an object is an instance of a class that inherits (directly or indirectly) from the specified class. If it is, the function should return True; otherwise, it should return False. You should not import any modules for this task.
Task 5: Geometry Module

Task 5 requires you to create an empty class called BaseGeometry. You should not import any modules for this task.
Task 6: Improve Geometry

Task 6 involves enhancing the BaseGeometry class from Task 5 by adding a public instance method called area(self). This method should raise an Exception with the message "area() is not implemented" when called. You should not import any modules for this task.
Task 7: Integer Validator

In Task 7, you need to extend the BaseGeometry class from Task 6 by adding a public instance method called integer_validator(self, name, value). This method should validate the value as follows:

    Check if value is an integer. If not, raise a TypeError with the message <name> must be an integer.
    Check if value is less than or equal to 0. If so, raise a ValueError with the message <name> must be greater than 0. You should not import any modules for this task.

Task 8: Rectangle

Task 8 involves creating a class called Rectangle that inherits from the BaseGeometry class from Task 7. This class should have a constructor __init__(self, width, height) that takes width and height as arguments. Both width and height should be positive integers validated by the integer_validator method from Task 7.
Task 9: Full Rectangle

Task 9 extends the Rectangle class from Task 8 by implementing the area() method. Additionally, the print() method should print the rectangle description in the format [Rectangle] <width>/<height>.
Task 10: Square #1

In Task 10, you need to create a class called Square that inherits from the Rectangle class from Task 9. The Square class should have a constructor __init__(self, size) that takes a size argument. The size should be a positive integer validated by the integer_validator method from Task 7.
Task 11: Square #2

Task 11 extends the Square class from Task 10 by customizing the print and str methods to print the square description in the format [Square] <width>/<height>
