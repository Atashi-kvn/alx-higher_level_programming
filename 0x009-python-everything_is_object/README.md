# Project 0x09. Python - Everything is object

## Background Context

In this project, we'll explore Python's unique approach to objects and variables. We'll investigate how Python works with different types of objects and variables. We'll also delve into the concept of mutability and immutability.

Have you ever modified a variable without intending to? For example:

```python
>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
```

Or what about this?

```python
>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
```

This project will be a bit different from the usual projects. The first part consists of questions about Python's specifics, like "What would be the result of...". You should start by reading the documentation thoroughly, then take some time to think and discuss with your peers about what you think and why. Try to do this without coding anything for a few hours.

Attempting examples directly in the Python interpreter might give you answers without deep thought. Avoid taking this route. Instead, read, think, brainstorm, and discuss. Only then should you test in the interpreter.

It's essential to genuinely understand the reasoning behind the answers to these tasks so that you can apply the same logic to other variables and variable types. These kinds of questions are commonly asked in Python job interviews.

All your answers should be a single line in a file, with no space before or after the answer.

## Resources

Before you begin, make sure to read or watch the following resources:

- [9.10. Objects and values](https://docs.python.org/3/reference/datamodel.html#objects-values)
- [9.11. Aliasing](https://docs.python.org/3/reference/datamodel.html#aliasing)
- [Immutable vs mutable types](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable)
- [Mutation (Only this chapter)](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable)
- [9.12. Cloning lists](https://docs.python.org/3/tutorial/introduction.html#lists)
- [Python tuples: immutable but potentially changing](https://docs.python.org/3/faq/design.html#how-are-tuples-different-from-lists)

## Learning Objectives

By the end of this project, you should be able to explain the following concepts without the need for external references:

- Why Python programming is awesome
- What is an object
- The difference between a class and an object or instance
- The difference between an immutable object and a mutable object
- What is a reference
- What is an assignment
- What is an alias
- How to determine if two variables are identical
- How to determine if two variables are linked to the same object
- How to display the variable identifier (memory address in CPython implementation)
- Understanding mutability and immutability
- Knowledge of built-in mutable types
- Knowledge of built-in immutable types
- How Python passes variables to functions

## Requirements

### Python Scripts

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
- All your files should end with a newline character
- The first line of all your script files should be exactly `#!/usr/bin/python3`
- You must include a README.md file at the root of the project folder
- Your code should adhere to Pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using `wc`

### .txt Answer Files

- Each answer should be a single line
- Do not include a Shebang in answer files
- All answer files should end with a newline character

## Tasks

### 0. Who am I?

**Question:** What function would you use to get the type of an object?

**Answer:** `type`

**File:** [0-answer.txt](./0-answer.txt)

### 1. Where are you?

**Question:** How do you get the variable identifier (which is the memory address in the CPython implementation)?

**Answer:** `id`

**File:** [1-answer.txt](./1-answer.txt)

### 2. Right count

**Question:** In the following code, do `a` and `b` point to the same object? Answer with Yes or No.

```python
>>> a = 89
>>> b = 100
```

**Answer:** No

**File:** [2-answer.txt](./2-answer.txt)

### 3. Right count =

**Question:** In the following code, do `a` and `b` point to the same object? Answer with Yes or No.

```python
>>> a = 89
>>> b = 89
```

**Answer:** Yes

**File:** [3-answer.txt](./3-answer.txt)

### 4. Right count =

**Question:** In the following code, do `a` and `b` point to the same object? Answer with Yes or No.

```python
>>> a = 89
>>> b = a
```

**Answer:** Yes

**File:** [4-answer.txt](./4-answer.txt)

### 5. Right count =+

**Question:** In the following code, do `a` and `b` point to the same object? Answer with Yes or No.

```python
>>> a = 89
>>> b = a + 1
```

**Answer:** No

**File:** [5-answer.txt](./5-answer.txt)

### 6. Is equal

**Question:** What do these 3 lines print?

```python
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```

**Answer:** True

**File:** [6-answer.txt](./6-answer.txt)

### 7. Is the same

**Question:** What do these 3 lines print?

```python
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```

**Answer:** True

**File:** [7-answer.txt](./7-answer.txt)

### 8. Is really equal

**Question:** What do these 3 lines print?

```python
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```

**Answer:** True

**File:**

 [8-answer.txt](./8-answer.txt)

### 9. Is really the same

**Question:** What do these 3 lines print?

```python
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```

**Answer:** True

**File:** [9-answer.txt](./9-answer.txt)

### 10. And with a list, is it equal

**Question:** What do these 3 lines print?

```python
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```

**Answer:** True

**File:** [10-answer.txt](./10-answer.txt)

### 11. And with a list, is it the same

**Question:** What do these 3 lines print?

```python
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```

**Answer:** False

**File:** [11-answer.txt](./11-answer.txt)

### 12. And with a list, is it really equal

**Question:** What do these 3 lines print?

```python
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```

**Answer:** True

**File:** [12-answer.txt](./12-answer.txt)

### 13. And with a list, is it really the same

**Question:** What do these 3 lines print?

```python
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```

**Answer:** True

**File:** [13-answer.txt](./13-answer.txt)

### 14. List append

**Question:** What does this script print?

```python
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```

**Answer:** `[1, 2, 3, 4]`

**File:** [14-answer.txt](./14-answer.txt)

### 15. List add

**Question:** What does this script print?

```python
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```

**Answer:** `[1, 2, 3]`

**File:** [15-answer.txt](./15-answer.txt)

### 16. Integer incrementation

**Question:** What does this script print?

```python
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```

**Answer:** `1`

**File:** [16-answer.txt](./16-answer.txt)

### 17. List incrementation

**Question:** What does this script print?

```python
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```

**Answer:** `[1, 2, 3, 4]`

**File:** [17-answer.txt](./17-answer.txt)

### 18. List assignation

**Question:** What does this script print?

```python
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```

**Answer:** `[1, 2, 3]`

**File:** [18-answer.txt](./18-answer.txt)

### 19. Copy a list object

**Question:** Write a function `def copy_list(l):` that returns a copy of a list.

- The input list can contain any type of objects.
- Your file should be maximum 3 lines long (no documentation needed).
- You are not allowed to import any module.

**File:** [19-copy_list.py](./19-copy_list.py)

### 20. Tuple or not?

**Question:** Is `a` a tuple? Answer with Yes or No.

```python
a = ()
```

**Answer:** Yes

**File:** [20-answer.txt](./20-answer.txt)

### 21. Tuple or not?

**Question:** Is `a` a tuple? Answer with Yes or No.

```python
a = (1, 2)
```

**Answer:** Yes

**File:** [21-answer.txt](./21-answer.txt)

### 22. Tuple or not?

**Question:** Is `a` a tuple? Answer with Yes or No.

```python
a = (1)
```

**Answer:** No

**File:** [22-answer.txt](./22-answer.txt)

### 23. Tuple or not?

**Question:** Is `a` a tuple? Answer with Yes or No.

```python
a = (1, )
```

**Answer:** Yes

**File:** [23-answer.txt](./23-answer.txt)

### 24. Who I am?

**Question:** What does this script print?

```python
a = (1)
b = (1)
a is b
```

**Answer:** False

**File:** [24-answer.txt](./24-answer.txt)

### 25. Tuple or not

**Question:** What does this script print?

```python
a = (1, 2)
b = (1, 2)
a is b
```

**Answer:** False

**File:** [25-answer.txt](./25-answer.txt)

### 26. Empty is not empty

**Question:** What does this script print?

```python
a = ()
b = ()
a is b
```

**Answer:** True

**File:** [26-answer.txt](./26-answer.txt)

### 27. Still the same?

**Question:** 

```python
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```

Will the last line of this script print `139926795932424`? Answer with Yes or No.

**Answer:** No

**File:** [27-answer.txt](./27-answer.txt)

### 28. Same or not?

**Question:** 

```python
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```

Will the last line of this script print `139926795932424`? Answer with Yes or No.

**Answer:** No

**File:** [28-answer.txt](./28-answer.txt
