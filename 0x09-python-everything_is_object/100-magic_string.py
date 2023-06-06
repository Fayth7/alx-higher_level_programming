#!/usr/bin/python3
"""returns a sting n times the number of iteration"""

def magic_string():
    magic_string.count = getattr(magic_string, 'count', 0) + 1
    return "BestSchool" + ", BestSchool" * (magic_string.count - 1)
 
