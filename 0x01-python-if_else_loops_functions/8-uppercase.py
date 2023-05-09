#!/usr/bin/python3
# 8-uppercase.py
def uppercase(str):
    for char in str:
        uppercase_char = chr(ord(char) - 32) if ord(char) >= 97 and ord(char) <= 122 else char
        print("{}".format(uppercase_char), end='')
    print()
