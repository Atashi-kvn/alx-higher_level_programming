This repository contains solutions to various programming tasks related to Python test-driven development (TDD).

Tasks
0. Integers addition (mandatory)
Write a function that adds 2 integers.

Prototype: def add_integer(a, b=98):
a and b must be integers or floats, otherwise raise a TypeError exception with the message a must be an integer or b must be an integer
a and b must be first casted to integers if they are float
Returns an integer: the addition of a and b
You are not allowed to import any module
1. Divide a matrix (mandatory)
Write a function that divides all elements of a matrix.

Prototype: def matrix_divided(matrix, div):
matrix must be a list of lists of integers or floats, otherwise raise a TypeError exception with the message matrix must be a matrix (list of lists) of integers/floats
Each row of the matrix must be of the same size, otherwise raise a TypeError exception with the message Each row of the matrix must have the same size
div must be a number (integer or float), otherwise raise a TypeError exception with the message div must be a number
div can’t be equal to 0, otherwise raise a ZeroDivisionError exception with the message division by zero
All elements of the matrix should be divided by div, rounded to 2 decimal places
Returns a new matrix
You are not allowed to import any module
2. Say my name (mandatory)
Write a function that prints "My name is <first name> <last name>".

Prototype: def say_my_name(first_name, last_name=""):
first_name and last_name must be strings otherwise, raise a TypeError exception with the message first_name must be a string or last_name must be a string
You are not allowed to import any module
3. Print square (mandatory)
Write a function that prints a square with the character #.

Prototype: def print_square(size):
size is the size length of the square
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
If size is less than 0, raise a ValueError exception with the message size must be >= 0
If size is a float and is less than 0, raise a TypeError exception with the message size must be an integer
You are not allowed to import any module
4. Text indentation (mandatory)
Write a function that prints a text with 2 new lines after each of these characters: ., ?, and :.

Prototype: def text_indentation(text):
text must be a string, otherwise raise a TypeError exception with the message text must be a string
There should be no space at the beginning or at the end of each printed line
You are not allowed to import any module
5. Max integer - Unittest (mandatory)
Write unittests for the function def max_integer(list=[]):.

Your test file should be inside a folder tests
You have to use the unittest module
Your test file should be python files (extension: .py)
Your test file should be executed by using this command: python3 -m unittest tests.6-max_integer_test
All tests you make must be passable by the function below
Repository
GitHub Repository: alx-higher_level_programming
Directory: 0x07-python-test_driven_development
Files:
0-add_integer.py
1-matrix_divided.py
2-say_my_name.py
3-print_square.py
4-text_indentation.py
tests/5-text_indentation.txt
tests/6-max_integer_test.py
Feel free to clone this repository and explore the solutions! If you have any questions or feedback, please let us know.