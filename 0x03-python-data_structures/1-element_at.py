#!/usr/bin/python3
def element_at(my_list, idx):
    """To retrive an element from my list."""
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    return (my_list[idx])
