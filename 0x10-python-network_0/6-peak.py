#!/usr/bin/python3
"""
Find a peak in a list of integers.

This function takes a list of unsorted integers as input and 
returns a peak value from the list

Args:
    list_of_integers (List[int]): A list of unsorted integers.

Returns:
    int: The peak value found in the list.

If the list is empty, the function returns None.
"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None

    length = len(list_of_integers)
    low, high = 0, length - 1

    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] <= list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return list_of_integers[low]
