# Python - Import & Modules

This repository contains a collection of Python programs that demonstrate the usage of importing functions and creating modules. It also covers additional topics such as using the `dir()` function and working with command line arguments in Python programs.

## Tasks

### 0. Import a simple function from a simple file
- File: [0-add.py](./0-add.py)
- Description: This Python program imports the function `def add(a, b):` from the file [add_0.py](./add_0.py) and prints the result of the addition `1 + 2 = 3`.
- Output: `<a value> + <b value> = <add(a, b) value>` followed by a new line.

### 1. My first toolbox!
- File: [1-calculation.py](./1-calculation.py)
- Description: This Python program imports functions from the file [calculator_1.py](./1-calculator.py) and prints the result of the addition, subtraction, multiplication, and division of `10` and `5`.
- Output: `<a value> <operator> <b value> = <operation(a, b) value>` followed by a new line.

### 2. How to make a script dynamic!
- File: [2-args.py](./2-args.py)
- Description: This Python program prints the number of arguments and a list of its arguments.
- Output:
  - `[Number of arguments] argument` (if the number is one) or `arguments` (otherwise), followed by
  - `:` (or `.` if no arguments were passed), followed by
  - A new line, followed by
  - One argument per line - the position of the argument (starting at `1`) followed by `:` followed by the argument value and another new line.

### 3. Infinite addition
- File: [3-infinite_add.py](./3-infinite_add.py)
- Description: This Python program prints the result of the addition of all arguments.
- Output: Sum of the arguments followed by a new line.

### 4. Who are you?
- File: [4-hidden_discovery.py](./4-hidden_discovery.py)
- Description: This Python program prints all the names defined by the compiled module `hidden_4.pyc`.
- Output: One name per line in alphabetical order.
- Names starting with `__` are not printed.

### 5. Everything can be imported
- File: [5-variable_load.py](./5-variable_load.py)
- Description: This Python program imports the variable `a` from the file [variable_load_5.py](./variable_load_5.py) and prints its value.

### 6. Build my own calculator!
- File: [100-my_calculator.py](./100-my_calculator.py)
- Description: This Python program imports all functions from the file [calculator_1.py](./calculator_1.py) and handles basic operations based on command line arguments.
- Usage: `./100-my_calculator.py <a> <operator> <b>` followed by a new line.
- Output: `<a> <operator> <b> = <result>` followed by a new line.
- The parameter `operator` can be:
  - `+` for addition
  - `-` for subtraction
  - `*` for multiplication
  - `/` for division
- If the operator is none of the above, the function prints `Unknown operator. Available operators: +, -, *, and /` followed by a new line and exits with a status value of `1`.
- If the number of arguments is not three, the program prints `Usage:

 ./100-my_calculator.py <a> <operator> <b>` followed by a new line and exits with a status value of `1`.

### 7. Easy print
- File: [101-easy_print.py](./101-easy_print.py)
- Description: This Python program prints `#pythoniscool` followed by a new line in the standard output without using `print`, `eval`, `open`, or `sys`.

### 8. ByteCode -> Python #3
- File: [102-magic_calculation.py](./102-magic_calculation.py)
- Description: This Python function matches exactly a bytecode provided by ALX.

### 9. Fast alphabet
- File: [103-fast_alphabet.py](./103-fast_alphabet.py)
- Description: This Python program prints the alphabet in uppercase, followed by a new line, without using loops, conditionals, `str.join()`, string literals, or system calls.

Feel free to explore and learn from these examples!

