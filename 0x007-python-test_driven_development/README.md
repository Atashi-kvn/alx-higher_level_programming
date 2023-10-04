# 0x07 - Python, Test-Driven Development

![Python Logo](https://www.python.org/static/img/python-logo.png)

## Introduction

Welcome to 0x07 - Python, Test-Driven Development! This project focuses on Test-Driven Development (TDD) in Python, a software development approach where tests are written before the code. We'll explore various Python programming concepts and implement them using TDD methodologies.


## Concepts

For this project, we expect you to understand the following concept:

- **Never Forget a Test**

## Background Context

Important notice regarding intranet checks for Python projects:

Starting today:

- Write documentation (module(s) + function(s)) and tests first, before coding.
- Intranet checks for Python projects won't be released until their first deadline to focus on TDD.
- Collaborate on test cases but not their implementation.
- Always consider edge cases; don't trust the user.

## Resources

Read or watch the following resources to help you with this project:

- [doctest — Test interactive Python examples](https://docs.python.org/3/library/doctest.html) (until "26.2.3.7. Warnings" included)
- [doctest – Testing through documentation](https://docs.python.org/3/library/doctest.html#what-s-next)
- [Unit Tests in Python](https://docs.python.org/3/library/unittest.html)
- [Unittest module](https://docs.python.org/3/library/unittest.html#module-unittest)
- [Interactive and Non-interactive tests](https://docs.python.org/3/library/doctest.html#other-examples)

## Learning Objectives

By the end of this project, you should be able to explain the following without Google's help:

### General

- Why Python programming is awesome.
- What an interactive test is.
- Why tests are important.
- How to write Docstrings to create tests.
- How to write documentation for each module and function.
- What are the basic option flags to create tests.
- How to find edge cases.

## Copyright - Plagiarism

- Come up with solutions yourself to meet the learning objectives.
- Avoid copying and pasting others' work.
- Do not publish any content from this project.
- Plagiarism is strictly forbidden and will result in program removal.

## Requirements

**Python Scripts:**

- Allowed editors: vi, vim, emacs.
- All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5.
- All files should end with a new line.
- The first line of all files should be `#!/usr/bin/python3`.
- A `README.md` file at the root of the project folder is mandatory.
- Your code should use the `pycodestyle` (version 2.8.*).
- All files must be executable.
- The length of your files will be tested using `wc`.

**Python Test Cases:**

- Allowed editors: vi, vim, emacs.
- All files should end with a new line.
- All test files should be inside a folder named `tests`.
- All test files should be text files with the extension `.txt`.
- Run tests using the command: `python3 -m doctest ./tests/*`
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`).
- All functions should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`).
- Documentation should be meaningful sentences explaining the purpose of the module, class, or method.

## Tasks

### 0. Integers Addition

Write a function that adds two integers.

- Prototype: `def add_integer(a, b=98):`
- `a` and `b` must be integers or floats; otherwise, raise a `TypeError` exception with the message `a must be an integer` or `b must be an integer`.
- `a` and `b` must be first cast to integers if they are float.
- Returns an integer: the addition of `a` and `b`.
- You are not allowed to import any module.

**Example:**

```python
print(add_integer(1, 2))  # Output: 3
print(add_integer(100, -2))  # Output: 98
print(add_integer(2))  # Output: 100
print(add_integer(100.3, -2))  # Output: 98
try:
    print(add_integer(4, "School"))  # Output: "b must be an integer"
except Exception as e:
    print(e)
try:
    print(add_integer(None))  # Output: "a must be an integer"
except Exception as e:
    print(e)
```

### 1. Divide a Matrix

Write a function that divides all elements of a matrix.

- Prototype: `def matrix_divided(matrix, div):`
- `matrix` must be a list of lists of integers or floats; otherwise, raise a `TypeError` exception with the message `matrix must be a matrix (list of lists) of integers/floats`.
- Each row of the matrix must be of the same size; otherwise, raise a `TypeError` exception with the message `Each row of the matrix must have the same size`.
- `div` must be a number (integer or float); otherwise, raise a `TypeError` exception with the message `div must be a number`.
- `div` can't be equal to 0; otherwise, raise a `ZeroDivisionError` exception with the message `division by zero`.
- All elements of the matrix should be divided by `div` and rounded to 2 decimal places.
- Returns a new matrix.
- You are not allowed to import any module.

**Example:**

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
# Output: [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
```

### 2. Say My Name

Write a function that prints "My name is \<first name\> \<last name\>."

- Prototype: `def say_my_name(first_name, last_name=""):`
- `first_name` and `last_name` must be strings; otherwise, raise a `TypeError` exception with the message `first_name must be a string` or `last_name must be a string`.
- You are not allowed to import any module.

**Example:**

```python
say_my_name("John", "Smith")  # Output: "My name is John Smith."
say_my_name("Walter", "White")  # Output: "My name is Walter White."


say_my_name("Bob")  # Output: "My name is Bob."
try:
    say_my_name(12, "White")  # Output: "first_name must be a string"
except Exception as e:
    print(e)
```

### 3. Print Square

Write a function that prints a square with the character `#`.

- Prototype: `def print_square(size):`
- `size` is the size length of the square.
- `size` must be an integer; otherwise, raise a `TypeError` exception with the message `size must be an integer`.
- If `size` is less than 0, raise a `ValueError` exception with the message `size must be >= 0`.
- If `size` is a float and is less than 0, raise a `TypeError` exception with the message `size must be an integer`.
- You are not allowed to import any module.

**Example:**

```python
print_square(4)
# Output:
# ####
# ####
# ####
# ####

print_square(1)
# Output:
# #

print_square(0)
# Output: (No output, size is 0)
```

### 4. Text Indentation

Write a function that prints a text with 2 new lines after each of these characters: `.` (period), `?` (question mark), and `:` (colon).

- Prototype: `def text_indentation(text):`
- `text` must be a string; otherwise, raise a `TypeError` exception with the message `text must be a string`.
- There should be no space at the beginning or at the end of each printed line.
- You are not allowed to import any module.

**Example:**

```python
text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")
# Output:
# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Quonam modo?
# Utrum igitur tibi litteram videor an totas paginas commovere?
# Non autem hoc: igitur ne illud quidem.
# Fortasse id optimum, sed ubi illud:
# Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere.
# Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens.
# Si id dicis, vicimus.
# Inde sermone vario sex illa a Dipylo stadia confecimus.
# Sin aliud quid voles, postea.
# Quae animi affectio suum cuique tribuens atque hanc, quam dico.
# Utinam quidem dicerent alium alio beatiorem! Iam ruinas videres
```

### 5. Max Integer - Unittest

Since the beginning, you have been creating "Interactive tests." For this exercise, you will add Unittests.

In this task, you will write unittests for the function `def max_integer(list=[]):`.

- Your test file should be inside a folder named `tests`.
- Use the `unittest` module.
- Your test file should be Python files with the extension `.py`.
- Run tests using the command: `python3 -m unittest tests.6-max_integer_test`.
- All tests you make must be passable by the function below.
- Collaborate on test cases to ensure you don't miss any edge case.

**Example:**

```python
# 6-max_integer.py

#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
```

```python
# 6-main.py

#!/usr/bin/python3
max_integer = __import__('6-max_integer').max_integer

print(max_integer([1, 2, 3, 4]))  # Output: 4
print(max_integer([1, 3, 4, 2]))  # Output: 4
```

```python
# tests/6-max_integer_test.py

#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer

 = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
```

## Repository

- **GitHub Repository:** [alx-higher_level_programming](https://github.com/Atashi-Kvn/alx-higher_level_programming)
- **Directory:** 0x07-python-test_driven_development!
