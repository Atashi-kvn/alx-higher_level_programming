#!/usr/bin/python3
for number in range(0, 8):
    for i in range(number + 1, 10):
        print("{:d}{:d}".format(number, i), end=', ')
print("{:d}{:d}".format(number + 1, i))
