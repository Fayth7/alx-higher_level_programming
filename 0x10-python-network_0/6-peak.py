#!/usr/bin/python3
# This function finds a peak in a list of unsorted integers
# Prototype: def find_peak(list_of_integers):
# The algorithm has a complexity of O(log(n))

def find_peak(list_of_integers):
    # Check if the list is empty or has only one element
    if not list_of_integers:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]

    # Use binary search to find a peak
    low = 0
    high = len(list_of_integers) - 1
    while low < high:
        mid = (low + high) // 2
        # Check if the middle element is greater than its neighbors
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]
        # If the left neighbor is greater, move to the left half
        elif mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            high = mid - 1
        # Otherwise, move to the right half
        else:
            low = mid + 1

    # Return the last element as a peak
    return list_of_integers[low]
