#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    different_elements_set = set()
    for element in set_1:
        if element not in set_2:
            different_elements_set.add(element)
    for element in set_2:
        if element not in set_1:
            different_elements_set.add(element)
    return (different_elements_set)
