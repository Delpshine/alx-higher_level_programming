#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    "To replace an element in a copied list at a specified index."
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    copy = copy.copy (my_list)
    copy[idx] = element
    return (copy)
