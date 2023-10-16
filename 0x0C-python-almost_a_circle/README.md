# 0x0C. Python - Almost a circle

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

**General:**

- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

## Requirements

**Python Scripts:**

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should be documented: `python3 -c 'print(__import__("my_module").__doc__)'`
- All your classes should be documented: `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`
- All your functions (inside and outside a class) should be documented: `python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)`
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class, or method (the length of it will be verified)

**Python Unit Tests:**

- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- You have to use the unittest module
- All your test files should be python files (extension: .py)
- All your test files and folders should start with test_
- Your file organization in the tests folder should be the same as your project: ex: for models/base.py, unit tests must be in: tests/test_models/test_base.py
- All your tests should be executed by using this command: `python3 -m unittest discover tests`
- You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base.py`
- We strongly encourage you to work together on test cases so that you don’t miss any edge case

## Tasks

1. **If it's not tested it doesn't work**

    - All your files, classes, and methods must be unit tested and be PEP 8 validated.

2. **Base class**

    - Write the first class Base:
        - Create a folder named models with an empty file __init__.py inside - with this file, the folder will become a Python package
        - Create a file named models/base.py:
        - Class Base:
            - Private class attribute `__nb_objects = 0`
            - Class constructor: `def __init__(self, id=None):`
                - if id is not None, assign the public instance attribute id with this value
                - otherwise, increment `__nb_objects` and assign the new value to the public instance attribute id
                - this class is intended to be the "base" of all other classes in this project
                - you will write the first task to test this new class
        - Create a file named tests/test_models/test_base.py
            - Test:
                - Class: TestBase
                - function: test_docstring
                - test the documentation
                - You are not allowed to use isinstance

3. **First Rectangle**

    - Write a class Rectangle that inherits from Base:
        - This class will be the "base" of all other classes in this project
        - You're not allowed to import any module
        - Class Rectangle:
            - Private instance attribute: `__width`
            - property `def width(self):` to retrieve it
            - property `def width(self, value):` to set it:
                - width must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
                - if width is less than 0, raise a `ValueError` exception with the message `width must be >= 0`
            - Private instance attribute `__height`
            - property `def height(self):` to retrieve it
            - property `def height(self, value):` to set it:
                - height must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
                - if height is less than 0, raise a `ValueError` exception with the message `height must be >= 0`
            - Instantiation with width and height: `def __init__(self, width, height, x=0, y=0, id=None):`
                - `x` and `y` are always 0
                - `id` is an argument of type `int` and it is the public instance attribute
                - you are allowed to override your `__init__` method from Base with the following `__init__:`

    ```
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    ```

    - you are not allowed to import any module
    - Update the test file: `tests/test_models/test_base.py` (up to 3 tests)
    - Please adjust attribute id (no testing of id != None) so each instance has a unique id (especially for the tests cases)

4. **Area first**

    - Write a class Rectangle that inherits from Base (Task 2):
        - Class Rectangle:
            - Add the public method `def area(self):` that returns the area value of the Rectangle instance
    - You are not allowed to import any module
    - Update the test file: `tests/test_models/test_base.py` (up to 3 tests)

5. **Display #0**

    - Write a class Rectangle that inherits from Base (Task 4):
        - Class Rectangle:
            - Add the public method `def display(self):` that prints in stdout the Rectangle instance with the character `#` - you don’t need to handle `x` and `y` here
    - You are not allowed to import any module
    - Update the test file: `tests/test_models/test_base.py` (up to 3 tests)

6. **Str**

    - Write a class Rectangle that inherits from Base (Task 5):
        - Class Rectangle:
            - Add the `__str__` method so that it returns `[Rectangle] (<id>) <x>/<y> - <width>/<height>`
    - You are not allowed to import any module
    - Update the test file: `tests/test_models/test_base.py` (up to 3 tests)

7. **Update #0**

    - Write a class Rectangle that inherits from Base (Task 6):
        - Class Rectangle:
            - Add the public method `def update(self, *args):` that assigns an argument to each attribute
        - You are not allowed to import any module
        - Update the test file: `tests/test_models/test_base.py` (up to 3 tests)

8. **Update #1**

    - Write a class Rectangle that inherits from Base (Task 7):
        - Class Rectangle:
            - Update the class Rectangle by adding the public method `def update(self, *args, **kwargs)` that assigns attributes
        - You are not allowed to import any module
        - Update the test file: `tests/test_models/test_base.py` (up to 3 tests)
        - 1
            - 9. UPDATE #3
            - Write a class Rectangle that inherits from Base (Task 8):
            - Class Rectangle:
            - Update the class Rectangle by adding the public method `def update(self, *args, **kwargs)` that assigns attributes:
            - You are not allowed to import any module
            - Update the test file: `tests/test_models/test_base.py` (up to 3 tests)

10. **Dictionary to JSON string**

    - Write a class Rectangle that inherits from Base (Task 9):
        - Class Rectangle:
            - Add the public method `def to_dictionary(self):` that returns the dictionary representation of a Rectangle
    - You are not allowed to import any module
    - Update the test file: `tests/test_models/test_base.py` (up to 3 tests)

