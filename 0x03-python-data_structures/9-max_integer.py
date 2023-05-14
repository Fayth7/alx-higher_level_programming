#!/usr/bin/python3
# 9-max_integer.py
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    
    max_value = my_list[0]  # Assume the first element is the largest
    
    for num in my_list:
        if num > max_value:
            max_value = num
    
    return max_value
