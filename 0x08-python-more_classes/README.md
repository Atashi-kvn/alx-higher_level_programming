# Python - More Classes and Objects

## Table of Contents
###Task
   - [Task 0: Simple Rectangle](#task-0-simple-rectangle)
   - [Task 1: Real Definition of a Rectangle](#task-1-real-definition-of-a-rectangle)
   - [Task 2: Area and Perimeter](#task-2-area-and-perimeter)
   - [Task 3: String Representation](#task-3-string-representation)
   - [Task 4: Eval is Magic](#task-4-eval-is-magic)
   - [Task 5: Detect Instance Deletion](#task-5-detect-instance-deletion)
   - [Task 6: How Many Instances](#task-6-how-many-instances)
   - [Task 7: Change Representation](#task-7-change-representation)
   - [Task 8: Compare Rectangles](#task-8-compare-rectangles)
   - [Task 9: A Square is a Rectangle](#task-9-a-square-is-a-rectangle)



## Learning Objectives
By the end of this project, you will have gained knowledge in the following areas:
- Understanding the principles of object-oriented programming
- Creating and using classes and objects
- Working with attributes and methods in Python classes
- Implementing class methods, static methods, and properties
- Overriding special methods like `__str__` and `__repr__`
- Handling instance deletion and tracking instances
- Using class attributes for counting instances


## Tasks
### Task 0: Simple Rectangle
Write an empty class `Rectangle` that defines a rectangle without importing any modules.

### Task 1: Real Definition of a Rectangle
Define a class `Rectangle` with private instance attributes `width` and `height`. Implement properties and setters for these attributes to ensure they are integers and non-negative. Allow instantiation with optional width and height.

### Task 2: Area and Perimeter
Enhance the `Rectangle` class to include public instance methods `area()` and `perimeter()` that calculate the area and perimeter of the rectangle. Handle cases where width or height is zero.

### Task 3: String Representation
Implement the `__str__` method to provide a string representation of the rectangle using the `#` character. Also, implement the `__repr__` method for creating a string representation that allows recreating a new instance using `eval()`.

### Task 4: Eval is Magic
Enhance the `Rectangle` class to support creating new instances using `eval()`. The `__repr__` method should provide a string representation for this purpose.

### Task 5: Detect Instance Deletion
Modify the `Rectangle` class to print "Bye rectangle..." when an instance is deleted.

### Task 6: How Many Instances
Implement a class attribute `number_of_instances` in the `Rectangle` class to track the number of instances. Increment it during instantiation and decrement it during deletion.

### Task 7: Change Representation
Add a class attribute `print_symbol` to the `Rectangle` class to customize the character used for string representation. Modify the `__str__` method to use this symbol.

### Task 8: Compare Rectangles
Implement a static method `bigger_or_equal(rect_1, rect_2)` that returns the rectangle with the larger area. Ensure that `rect_1` and `rect_2` are instances of `Rectangle`.

### Task 9: A Square is a Rectangle
Create a class method `square(cls, size=0)` that returns a new instance of `Rectangle` with equal width and height (i.e., a square).
