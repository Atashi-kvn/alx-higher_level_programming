#!/usr/bin/python3

def print_square(size):
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    elif size < 0:
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")
        
    size = int(size)
    k = 0

    for k in range(0, size):
        m = 0
        for m in range(0, size):
            print("#", end="")
        print()