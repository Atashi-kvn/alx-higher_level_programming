#!/usr/bin/python3

def safe_print_list_integers(my_list=[], k=0):
    """Print the first k elements of a list that are integers.

    Args:
        my_list (list): The list to print elements from.
        k (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    ret = 0
    for a in range(0, k):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
