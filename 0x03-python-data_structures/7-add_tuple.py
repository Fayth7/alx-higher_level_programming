#!/usr/bin/python3
# 7-add_tuple.py
def add_tuple(tuple_a=(), tuple_b=()):
    # Extract the first two elements from each tuple
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0
    
    # Perform addition of the extracted elements
    result = (a1 + b1, a2 + b2)
    return result
