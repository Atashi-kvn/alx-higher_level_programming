# README for 0x0B. Python - Input/Output



## Resources

Read or watch:

- [7.2. Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [8.7. Predefined Clean-up Actions](https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions)
- [Dive Into Python 3: Chapter 11. Files](https://www.diveinto.org/python3/files.html) (until "11.4 Binary Files" (included))
- [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- [Learn to Program 8 : Reading / Writing Files](https://www.youtube.com/watch?v=LULkDvz9EvE)
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/2e/chapter8/) (Chapter 8 p. 180-183 and Chapter 14 p. 326-333)
- [All about py-file I/O](https://docs.python.org/3/tutorial/inputoutput.html)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- Why Python programming is awesome
- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the with statement
- What is JSON
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure

## Copyright - Plagiarism

- You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

### Python Scripts

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using `wc`

### Python Test Cases

- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- All your test files should be text files (extension: .txt)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class, or method (the length of it will be verified)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

## Tasks

### 0. Read file

Write a function that reads a text file (UTF8) and prints it to stdout:

- Prototype: `def read_file(filename=""):`
- You must use the with statement
- You don’t need to manage file permission or file doesn't exist exceptions.
- You are not allowed to import any module



guillaume@ubuntu:~/0x0B$ cat 0-main.py
#!/usr/bin/python3
read_file = __import__('0-read_file').read_file

read_file("my_file_0.txt")

guillaume@ubuntu:~/0x0B$ cat my_file_0.txt
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
guillaume@ubuntu:~/0x0B$ ./0-main.py
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
guillaume@ubuntu:~/0x0B$
```

### 1. Write to a file

Write a function that writes a string to a text file (UTF8) and returns the number of characters written:

- Prototype: `def write_file(filename="", text=""):`
- You must use the with statement
- You don’t need to manage file permission exceptions.
- Your function should create the file if it doesn’t exist.
- Your function should overwrite the content of the file if it already exists.
- You are not allowed to import any module


guillaume@ubuntu:~/0x0B$ cat 1-main.py
#!/usr/bin/python3
write_file = __import__('1-write_file').write_file

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)

guillaume@ubuntu:~/0x0B$ ./1-main.py
29
guillaume@ubuntu:~/0x0B$ cat my_first_file.txt
This School is so cool!
guillaume@ubuntu:~/0x0B$
```

### 2. Append to a file

Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:

- Prototype: `def append_write(filename="", text=""):`
- If the file doesn’t exist, it should be created
- You must use the with statement
- You don’t need to manage file permission or file doesn't exist exceptions.
- You are not allowed to import any modu


guillaume@ubuntu:~/0x0B$ cat 2-main.py
#!/usr/bin/python3
append_write = __import__('2-append_write').append_write

nb_characters_added = append_write("file_append

.txt", "Holberton School is so cool!\n")
print(nb_characters_added)

guillaume@ubuntu:~/0x0B$ cat file_append.txt
Holberton School is so cool!
guillaume@ubuntu:~/0x0B$ ./2-main.py
28
guillaume@ubuntu:~/0x0B$ cat file_append.txt
Holberton School is so cool!
Holberton School is so cool!
guillaume@ubuntu:~/0x0B$
```

### 3. To JSON string

Write a function that returns an object (Python data structure) represented by a JSON string:

- Prototype: `def to_json_string(my_obj):`
- You don’t need to manage exceptions if the object can’t be serialized.
- You don’t need to manage file permission exceptions.


guillaume@ubuntu:~/0x0B$ cat 3-main.py
#!/usr/bin/python3
to_json_string = __import__('3-to_json_string').to_json_string

my_list = [1, 2, 3]
s_my_list = to_json_string(my_list)
print(s_my_list)
print(type(s_my_list))

my_dict = {
    'id': 12,
    'name': "John",
    'places': ["San Francisco", "Tokyo"],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
s_my_dict = to_json_string(my_dict)
print(s_my_dict)
print(type(s_my_dict))

try:
    my_set = {132, 3}
    s_my_set = to_json_string(my_set)
    print(s_my_set)
    print(type(s_my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x0B$ ./3-main.py
"[1, 2, 3]"
<class 'str'>
"{"id": 12, "name": "John", "places": ["San Francisco", "Tokyo"], "is_active": true, "info": {"age": 36, "average": 3.1400000000000001}}"
<class 'str'>
[TypeError] Object of type set is not JSON serializable
guillaume@ubuntu:~/0x0B$
```

### 4. From JSON string to Object

Write a function that returns an object (Python data structure) represented by a JSON string:

- Prototype: `def from_json_string(my_str):`
- You don’t need to manage exceptions if the JSON string doesn’t represent an object.
- You don’t need to manage file permissions or file doesn't exist exceptions.



guillaume@ubuntu:~/0x0B$ cat 4-main.py
#!/usr/bin/python3
from_json_string = __import__('4-from_json_string').from_json_string

s_my_list = "[1, 2, 3]"
my_list = from_json_string(s_my_list)
print(my_list)
print(type(my_list))

s_my_dict = """
{
    "id": 12,
    "name": "John",
    "places": ["San Francisco", "Tokyo"],
    "is_active": true,
    "info": {
        "age": 36,
        "average": 3.14
    }
}
"""
my_dict = from_json_string(s_my_dict)
print(my_dict)
print(type(my_dict))

try:
    s_my_set = "[132, 3]"
    my_set = from_json_string(s_my_set)
    print(my_set)
    print(type(my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x0B$ ./4-main.py
[1, 2, 3]
<class 'list'>
{'id': 12, 'name': 'John', 'places': ['San Francisco', 'Tokyo'], 'is_active': True, 'info': {'age': 36, 'average': 3.14}}
<class 'dict'>
[TypeError] the JSON object must be str, bytes or bytearray, not 'list'
guillaume@ubuntu:~/0x0B$
```

### 5. Save Object to a file

Write a function that writes an Object to a text file, using a JSON representation:

- Prototype: `def save_to_json_file(my_obj, filename):`
- You must use the with statement
- You don’t need to manage exceptions if the object can’t be serialized.
- You don’t need to manage file permissions or file doesn't exist exceptions.

```python
guillaume@ubuntu:~/0x0B$ cat 5-main.py
#!/usr/bin/python3
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "my_list.json"
my_list = [1, 2, 3]
save_to_json_file(my_list, filename)

guillaume@ubuntu:~/0x0B$ cat my_list.json
[1, 2, 3]
guillaume@ubuntu:~/0x0B$ cat 5-main.py
#!/usr/bin/python3
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "my_dict.json"
my_dict = { 
    'id': 12,
    'name': "John",
    'places': ["San Francisco", "Tokyo"],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
save_to_json_file(my_dict, filename)

guillaume@ubuntu:~/0x0B$ cat my_dict.json
{"id": 12, "name": "John", "places": ["San Francisco", "Tokyo"], "is_active": true, "info": {"age": 36, "average": 3.1400000000000001}}
guillaume@ubuntu:~/0x0B$
```

### 6. Create object from a JSON file

Write a function that creates an Object from a “JSON file”:

- Prototype: `def load_from_json_file(filename):`
- You must use the with statement
- You don’t need to manage exceptions if the JSON string doesn’t represent an object.
- You don’t need to manage file permissions or file doesn't exist exceptions.


guillaume@ubuntu:~/0x0B$ cat 6-main.py
#!/usr/bin/python3
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "my_list.json"
my_list = load_from_json_file(filename)
print(my_list)
print(type(my_list))

filename = "my_dict.json"
my_dict = load_from_json_file(filename)
print(my_dict)
print(type(my_dict))

guillaume@ubuntu:~/0x0B$ ./6-main.py
[1, 2, 3]
<class 'list'>
{'id': 12, 'name': 'John', 'places': ['San Francisco', 'Tokyo'], 'is_active': True, 'info': {'age': 36, 'average': 3.14}}
<class 'dict'>
guillaume@ubuntu:~/0x0B$
```

### 

7. Load, add, save

Write a script that adds all arguments to a Python list, and then save them to a file.

- The list must be saved as a JSON representation in a file named `add_item.json`.
- If the file doesn’t exist, it is created.
- You don’t need to manage file permissions or file doesn't exist exceptions.


guillaume@ubuntu:~/0x0B$ cat 7-main.py
#!/usr/bin/python3
add_item = __import__('7-add_item').add_item

add_item()
guillaume@ubuntu:~/0x0B$ cat add_item.json
[]
guillaume@ubuntu:~/0x0B$ ./7-main.py
guillaume@ubuntu:~/0x0B$ cat add_item.json
[]
guillaume@ubuntu:~/0x0B$ ./7-main.py Hello
guillaume@ubuntu:~/0x0B$ cat add_item.json
["Hello"]
guillaume@ubuntu:~/0x0B$ ./7-main.py World
guillaume@ubuntu:~/0x0B$ cat add_item.json
["Hello", "World"]
guillaume@ubuntu:~/0x0B$
```

### 8. Class to JSON

Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:

- Prototype: `def class_to_json(obj):`
- `obj` is an instance of a Class
- All attributes of the obj are serializable: list, dictionary, string, integer and boolean
- You are not allowed to import any module



guillaume@ubuntu:~/0x0B$ cat 8-main.py
#!/usr/bin/python3
class_to_json = __import__('8-class_to_json').class_to_json

class MyClass:
    pass

class_to_json_obj = class_to_json(MyClass)
print(class_to_json_obj)

class_to_json_list = class_to_json([1, 2, 3])
print(class_to_json_list)

class_to_json_dict = class_to_json({"id": 12, "name": "John"})
print(class_to_json_dict)

guillaume@ubuntu:~/0x0B$ ./8-main.py
{}
[1, 2, 3]
{"id": 12, "name": "John"}
guillaume@ubuntu:~/0x0B$
```

### 9. Student to JSON

Write a class `Student` that defines a student by:

- Public instance attributes:
  - `first_name`
  - `last_name`
  - `age`
- Instantiation with `first_name`, `last_name`, and `age`: `def __init__(self, first_name, last_name, age):`
- Public method:
  - `def to_json(self):` that retrieves a dictionary representation of a `Student` instance


guillaume@ubuntu:~/0x0B$ cat 9-main.py
#!/usr/bin/python3
Student = __import__('9-student').Student

student_1 = Student("John", "Doe", 23)
j_student_1 = student_1.to_json()
print(type(j_student_1))
print(j_student_1)

student_2 = Student("Bob", "Dylan", 27)
j_student_2 = student_2.to_json()
print(type(j_student_2))
print(j_student_2)

guillaume@ubuntu:~/0x0B$ ./9-main.py
<class 'dict'>
{'first_name': 'John', 'last_name': 'Doe', 'age': 23}
<class 'dict'>
{'first_name': 'Bob', 'last_name': 'Dylan', 'age': 27}
guillaume@ubuntu:~/0x0B$
```

### 10. Student to JSON with filter

Write a class `Student` that defines a student by:

- Public instance attributes:
  - `first_name`
  - `last_name`
  - `age`
- Instantiation with `first_name`, `last_name`, and `age`: `def __init__(self, first_name, last_name, age):`
- Public method:
  - `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance (same as `9-student.py`):
    - If `attrs` is a list of strings, only attribute names contained in this list must be retrieved.
- You are not allowed to import any module


guillaume@ubuntu:~/0x0B$ cat 10-main.py
#!/usr/bin/python3
Student = __import__('10-student').Student

student_1 = Student("John", "Doe", 23)
j_student_1 = student_1.to_json()
print(type(j_student_1))
print(j_student_1)

student_2 = Student("Bob", "Dylan", 27)
j_student_2 = student_2.to_json(["first_name", "age"])
print(type(j_student_2))
print(j_student_2)

guillaume@ubuntu:~/0x0B$ ./10-main.py
<class 'dict'>
{'first_name': 'John', 'last_name': 'Doe', 'age': 23}
<class 'dict'>
{'first_name': 'Bob', 'age': 27}
guillaume@ubuntu:~/0x0B$
```

### 11. Student to disk and reload

Write a class `Student` that defines a student by:

- Public instance attributes:
  - `first_name`
  - `last_name`
  - `age`
- Instantiation with `first_name`, `last_name`, and `age`: `def __init__(self, first_name, last_name, age):`
- Public method:
  - `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance (same as `10-student.py`):
    - If `attrs` is a list of strings, only attribute names contained in this list must be retrieved.
- Public method:
  - `def reload_from_json(self, json):` that replaces all attributes of the `Student` instance:

You are not allowed to import any module


guillaume@ubuntu:~/0x0B$ cat 11-main.py
#!/usr/bin/python3
Student = __import__('11-student').Student

student_1 = Student("John", "Doe", 23)
j_student_1 = student_1.to_json()
print(type(j_student_1))
print(j_student_1)

student_2 = Student("Bob", "Dylan", 27)
j_student_2 = student_2.to_json(["first_name", "age"])
print(type(j_student_2))
print(j_student_2)

filename = "student.json"
Student.save_to_file(student_1, filename)

del student_1
del student_2

student_3 = Student("Bob", "Dylan", 27)
Student.reload_from_json(student_3, filename)
j_student_3 = student_3.to_json()
print(type(j_student_3))
print(j_student_3)

guillaume@ubuntu:~/0x0B$ ./11-main.py
<class '

dict'>
{'first_name': 'John', 'last_name': 'Doe', 'age': 23}
<class 'dict'>
{'first_name': 'Bob', 'age': 27}
<class 'dict'>
{'first_name': 'John', 'last_name': 'Doe', 'age': 23}
guillaume@ubuntu:~/0x0B$
```

### 12. Pascal's Triangle

**Technical interview preparation**:

- You are not allowed to google anything
- Whiteboard first

Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of `n`:

- Returns an empty list if `n <= 0`
- You can assume `n` will be always an integer


guillaume@ubuntu:~/0x0B$ cat 12-main.py
#!/usr/bin/python3
pascal_triangle = __import__('12-pascal_triangle').pascal_triangle

my_list = pascal_triangle(5)
for i in my_list:
    print(i)

guillaume@ubuntu:~/0x0B$ ./12-main.py
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
guillaume@ubuntu:~/0x0B$
```


Here's a breakdown of the tasks in this project:

0. **Read file**
   - Create a function that reads a text file and prints its content to the standard output.

1. **Write to a file**
   - Write a function that writes a string to a text file and returns the number of characters written.

2. **Append to a file**
   - Write a function that appends a string to the end of a text file and returns the number of characters added.

3. **To JSON string**
   - Create a function that converts a Python object to a JSON string.

4. **From JSON string to Object**
   - Write a function that converts a JSON string to a Python object.

5. **Save Object to a file**
   - Create a function that saves a Python object to a file in JSON format.

6. **Create object from a JSON file**
   - Write a function that creates a Python object from a JSON file.

7. **Load, add, save**
   - Write a script that adds all command-line arguments to a list and saves the list to a JSON file.

8. **Class to JSON**
   - Implement a function that converts a Python object (with simple data structures) to a dictionary for JSON serialization.

9. **Student to JSON**
   - Create a class `Student` with attributes and a method to convert the object to a dictionary.

10. **Student to JSON with filter**
    - Modify the `Student` class to filter the attributes to be converted to a dictionary.

11. **Student to disk and reload**
    - Extend the `Student` class with methods to save and reload objects from JSON files.

12. **Pascal's Triangle**
    - Create a function that generates Pascal's triangle and returns it as a list of lists.

