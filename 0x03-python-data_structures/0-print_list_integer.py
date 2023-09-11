#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Print all integers of a list on a new line each."""
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))

